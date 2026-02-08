"""Tests for DDInter collector."""

import pytest

from twtxgnn.collectors import DDInterCollector


@pytest.fixture
def collector():
    """Create DDInter collector with default data directory."""
    return DDInterCollector()


def test_collector_initialization(collector):
    """Test that collector initializes correctly."""
    assert collector.source_name == "ddinter"
    assert collector.data_dir.exists()


def test_search_existing_drug(collector):
    """Test searching for a drug that exists in the database."""
    result = collector.search("Dolutegravir")

    assert result.success
    assert result.source == "ddinter"
    assert result.query == {"drug": "Dolutegravir"}
    assert isinstance(result.data, list)
    assert len(result.data) > 0

    # Check structure of first interaction
    first_interaction = result.data[0]
    assert "interacting_drug" in first_interaction
    assert "level" in first_interaction
    assert "source" in first_interaction
    assert first_interaction["source"] == "ddinter"
    assert first_interaction["level"] in ["Major", "Moderate", "Minor"]


def test_search_case_insensitive(collector):
    """Test that search is case-insensitive."""
    result_lower = collector.search("dolutegravir")
    result_upper = collector.search("DOLUTEGRAVIR")
    result_mixed = collector.search("DoLuTeGrAvIr")

    assert result_lower.success
    assert result_upper.success
    assert result_mixed.success
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


def test_get_available_drugs(collector):
    """Test getting list of available drugs."""
    drugs = collector.get_available_drugs()

    assert isinstance(drugs, list)
    assert len(drugs) > 0
    assert all(isinstance(drug, str) for drug in drugs)
    # Should be sorted
    assert drugs == sorted(drugs)


def test_get_severe_interactions_major(collector):
    """Test filtering for major interactions only."""
    severe = collector.get_severe_interactions("Dolutegravir", min_level="Major")

    assert isinstance(severe, list)
    # All should be Major level
    for interaction in severe:
        assert interaction["level"] == "Major"


def test_get_severe_interactions_moderate(collector):
    """Test filtering for moderate and above interactions."""
    severe = collector.get_severe_interactions("Dolutegravir", min_level="Moderate")

    assert isinstance(severe, list)
    # Should include both Major and Moderate
    levels = {interaction["level"] for interaction in severe}
    assert levels.issubset({"Major", "Moderate"})


def test_get_interaction_count(collector):
    """Test getting interaction count."""
    count = collector.get_interaction_count("Dolutegravir")

    assert isinstance(count, int)
    assert count > 0


def test_get_interaction_count_nonexistent(collector):
    """Test interaction count for nonexistent drug."""
    count = collector.get_interaction_count("NonexistentDrug12345")

    assert count == 0


def test_interaction_bidirectional(collector):
    """Test that interactions are stored bidirectionally."""
    # If Drug A interacts with Drug B, then Drug B should interact with Drug A
    result_a = collector.search("Naltrexone")
    assert result_a.success
    assert len(result_a.data) > 0

    # Find an interacting drug
    interacting_drug = result_a.data[0]["interacting_drug"]

    # Search for the interacting drug
    result_b = collector.search(interacting_drug)
    assert result_b.success

    # Naltrexone should be in the interactions list
    interacting_drugs = [i["interacting_drug"] for i in result_b.data]
    assert "Naltrexone" in interacting_drugs


def test_data_caching(collector):
    """Test that data is cached after first load."""
    # First search loads data
    collector.search("Dolutegravir")
    assert collector._cache is not None

    # Second search uses cache
    cache_before = id(collector._cache)
    collector.search("Naltrexone")
    cache_after = id(collector._cache)

    assert cache_before == cache_after


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
    assert result_dict["source"] == "ddinter"
