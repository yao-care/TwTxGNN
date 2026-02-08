"""Tests for Unified DDI collector."""

import pytest

from twtxgnn.collectors import UnifiedDDICollector


@pytest.fixture
def collector():
    """Create Unified DDI collector with default data sources."""
    return UnifiedDDICollector()


def test_collector_initialization(collector):
    """Test that collector initializes correctly."""
    assert collector.source_name == "unified_ddi"
    assert collector.ddinter is not None
    assert collector.pharmacology is not None


def test_search_existing_drug(collector):
    """Test searching for a drug that exists in the databases."""
    result = collector.search("Dolutegravir")

    assert result.success
    assert result.source == "unified_ddi"
    assert result.query == {"drug": "Dolutegravir"}
    assert isinstance(result.data, list)
    assert len(result.data) > 0

    # Check structure of first interaction
    first_interaction = result.data[0]
    assert "interacting_drug" in first_interaction
    assert "level" in first_interaction
    assert "source" in first_interaction
    assert "details" in first_interaction
    assert first_interaction["source"] in ["ddinter", "pharmacology"]


def test_search_case_insensitive(collector):
    """Test that search is case-insensitive."""
    result_lower = collector.search("dolutegravir")
    result_upper = collector.search("DOLUTEGRAVIR")
    result_mixed = collector.search("DoLuTeGrAvIr")

    assert result_lower.success
    assert result_upper.success
    assert result_mixed.success
    # All should return the same number of results
    assert len(result_lower.data) == len(result_upper.data)
    assert len(result_lower.data) == len(result_mixed.data)


def test_search_nonexistent_drug(collector):
    """Test searching for a drug that doesn't exist."""
    result = collector.search("NonexistentDrug12345")

    assert result.success  # Not finding data is not an error
    assert result.data == []


def test_search_ignores_disease(collector):
    """Test that disease parameter is ignored for DDI lookup."""
    result1 = collector.search("Dolutegravir", disease=None)
    result2 = collector.search("Dolutegravir", disease="HIV")

    assert len(result1.data) == len(result2.data)


def test_merged_results_no_duplicates(collector):
    """Test that merged results don't contain duplicates."""
    result = collector.search("Dolutegravir")

    # Check for duplicate interacting drugs (case-insensitive)
    interacting_drugs = [i["interacting_drug"].lower() for i in result.data]
    assert len(interacting_drugs) == len(set(interacting_drugs))


def test_source_labeling(collector):
    """Test that all interactions are properly labeled with their source."""
    result = collector.search("Dolutegravir")

    if result.data:
        for interaction in result.data:
            assert interaction["source"] in ["ddinter", "pharmacology"]


def test_ddinter_interactions_have_levels(collector):
    """Test that DDInter interactions have severity levels."""
    result = collector.search("Dolutegravir")

    ddinter_interactions = [i for i in result.data if i["source"] == "ddinter"]
    for interaction in ddinter_interactions:
        assert interaction["level"] in ["Major", "Moderate", "Minor"]


def test_pharmacology_interactions_no_levels(collector):
    """Test that PHARMACOLOGY interactions don't have severity levels."""
    result = collector.search("Dolutegravir")

    pharmacology_interactions = [
        i for i in result.data if i["source"] == "pharmacology"
    ]
    for interaction in pharmacology_interactions:
        assert interaction["level"] is None


def test_get_severe_interactions_major(collector):
    """Test filtering for major interactions only."""
    severe = collector.get_severe_interactions("Dolutegravir", min_level="Major")

    assert isinstance(severe, list)
    # All should be Major level and from DDInter
    for interaction in severe:
        assert interaction["level"] == "Major"
        assert interaction["source"] == "ddinter"


def test_get_severe_interactions_moderate(collector):
    """Test filtering for moderate and above interactions."""
    severe = collector.get_severe_interactions("Dolutegravir", min_level="Moderate")

    assert isinstance(severe, list)
    # Should include both Major and Moderate, all from DDInter
    for interaction in severe:
        assert interaction["level"] in ["Major", "Moderate"]
        assert interaction["source"] == "ddinter"


def test_get_severe_interactions_only_ddinter(collector):
    """Test that severe interactions only come from DDInter source."""
    severe = collector.get_severe_interactions("Dolutegravir", min_level="Minor")

    # All should be from DDInter
    for interaction in severe:
        assert interaction["source"] == "ddinter"


def test_get_stats(collector):
    """Test getting statistics from both sources."""
    stats = collector.get_stats()

    assert isinstance(stats, dict)
    assert "ddinter" in stats
    assert "pharmacology" in stats
    assert "unified" in stats

    # Check DDInter stats
    assert "drugs_count" in stats["ddinter"]
    assert "total_interactions" in stats["ddinter"]
    assert "data_dir" in stats["ddinter"]

    # Check PHARMACOLOGY stats
    assert "drugs_count" in stats["pharmacology"]
    assert "total_target_records" in stats["pharmacology"]
    assert "data_file" in stats["pharmacology"]

    # Check unified stats
    assert "total_drugs" in stats["unified"]
    assert "common_drugs" in stats["unified"]


def test_get_available_drugs(collector):
    """Test getting list of available drugs from both sources."""
    drugs = collector.get_available_drugs()

    assert isinstance(drugs, list)
    assert len(drugs) > 0
    assert all(isinstance(drug, str) for drug in drugs)
    # Should be sorted
    assert drugs == sorted(drugs)


def test_get_interaction_count(collector):
    """Test getting interaction count from both sources."""
    count = collector.get_interaction_count("Dolutegravir")

    assert isinstance(count, int)
    assert count > 0


def test_get_interaction_count_nonexistent(collector):
    """Test interaction count for nonexistent drug."""
    count = collector.get_interaction_count("NonexistentDrug12345")

    assert count == 0


def test_get_ddinter_only(collector):
    """Test filtering for DDInter interactions only."""
    ddinter_only = collector.get_ddinter_only("Dolutegravir")

    assert isinstance(ddinter_only, list)
    for interaction in ddinter_only:
        assert interaction["source"] == "ddinter"
        assert interaction["level"] in ["Major", "Moderate", "Minor"]


def test_get_pharmacology_only(collector):
    """Test filtering for PHARMACOLOGY interactions only."""
    pharmacology_only = collector.get_pharmacology_only("Dolutegravir")

    assert isinstance(pharmacology_only, list)
    for interaction in pharmacology_only:
        assert interaction["source"] == "pharmacology"
        assert interaction["level"] is None


def test_details_field_structure(collector):
    """Test that details field contains original data."""
    result = collector.search("Dolutegravir")

    if result.data:
        for interaction in result.data:
            assert "details" in interaction
            assert isinstance(interaction["details"], dict)

            # Details should contain source-specific fields
            if interaction["source"] == "ddinter":
                assert "interacting_drug" in interaction["details"]
                assert "level" in interaction["details"]
            elif interaction["source"] == "pharmacology":
                # PHARMACOLOGY details should contain target information
                assert isinstance(interaction["details"], dict)


def test_result_to_dict(collector):
    """Test converting result to dictionary."""
    result = collector.search("Dolutegravir")
    result_dict = result.to_dict()

    assert isinstance(result_dict, dict)
    assert "source" in result_dict
    assert "query" in result_dict
    assert "data" in result_dict
    assert "timestamp" in result_dict
    assert "success" in result_dict
    assert result_dict["source"] == "unified_ddi"


def test_both_sources_contribute(collector):
    """Test that both sources contribute to results (if data exists)."""
    result = collector.search("Dolutegravir")

    if len(result.data) > 0:
        sources = {interaction["source"] for interaction in result.data}
        # At least one source should contribute
        assert len(sources) > 0
        assert sources.issubset({"ddinter", "pharmacology"})


def test_comparison_with_individual_sources(collector):
    """Test that unified results handle duplicates correctly."""
    drug = "Dolutegravir"

    # Get unified results
    unified_result = collector.search(drug)
    unified_count = len(unified_result.data)

    # Get DDInter results
    ddinter_result = collector.ddinter.search(drug)
    ddinter_count = len(ddinter_result.data) if ddinter_result.data else 0

    # Get PHARMACOLOGY results
    pharmacology_result = collector.pharmacology.search(drug)
    pharmacology_count = (
        len(pharmacology_result.data) if pharmacology_result.data else 0
    )

    # Unified removes duplicates, so it should be <= the sum of both sources
    assert unified_count <= ddinter_count + pharmacology_count

    # Unified should have at least some results if either source has results
    if ddinter_count > 0 or pharmacology_count > 0:
        assert unified_count > 0


def test_custom_data_paths():
    """Test initialization with custom data paths."""
    from pathlib import Path

    # Create collector with custom (likely non-existent) paths
    custom_collector = UnifiedDDICollector(
        ddinter_data_dir=Path("/tmp/nonexistent_ddinter"),
        pharmacology_data_file=Path("/tmp/nonexistent_pharmacology.csv"),
    )

    # Should still initialize without errors
    assert custom_collector.source_name == "unified_ddi"

    # Search should return empty results (no data)
    result = custom_collector.search("SomeDrug")
    assert result.success
    assert result.data == []
