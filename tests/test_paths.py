"""Tests for path management utilities."""

import pytest
from pathlib import Path

from twtxgnn.paths import (
    get_project_root,
    get_data_dir,
    get_prompts_dir,
    get_collected_dir,
    get_bundles_dir,
    get_evidence_packs_dir,
    get_notes_dir,
    slugify,
    get_candidate_dir,
    ensure_candidate_dirs,
)


class TestGetProjectRoot:
    """Tests for get_project_root function."""

    def test_returns_path(self):
        """Should return a Path object."""
        result = get_project_root()
        assert isinstance(result, Path)

    def test_contains_expected_files(self):
        """Should return a directory containing expected project files."""
        root = get_project_root()
        # Check for typical project files
        assert (root / "pyproject.toml").exists() or (root / "src").exists()


class TestGetDataDir:
    """Tests for get_data_dir function."""

    def test_returns_path(self):
        """Should return a Path object."""
        result = get_data_dir()
        assert isinstance(result, Path)

    def test_is_under_project_root(self):
        """Should be under project root."""
        data_dir = get_data_dir()
        project_root = get_project_root()
        assert data_dir.parent == project_root

    def test_named_data(self):
        """Should be named 'data'."""
        data_dir = get_data_dir()
        assert data_dir.name == "data"


class TestGetPromptsDir:
    """Tests for get_prompts_dir function."""

    def test_returns_path(self):
        """Should return a Path object."""
        result = get_prompts_dir()
        assert isinstance(result, Path)

    def test_named_prompts(self):
        """Should be named 'prompts'."""
        prompts_dir = get_prompts_dir()
        assert prompts_dir.name == "prompts"


class TestGetCollectedDir:
    """Tests for get_collected_dir function."""

    def test_without_source(self):
        """Should return base collected directory."""
        result = get_collected_dir()
        assert result.name == "collected"
        assert result.parent == get_data_dir()

    def test_with_source(self):
        """Should return source-specific directory."""
        result = get_collected_dir("clinicaltrials")
        assert result.name == "clinicaltrials"
        assert result.parent.name == "collected"

    def test_various_sources(self):
        """Should work with various source names."""
        sources = ["clinicaltrials", "pubmed", "tfda", "ictrp", "unified_ddi"]
        for source in sources:
            result = get_collected_dir(source)
            assert result.name == source


class TestGetBundlesDir:
    """Tests for get_bundles_dir function."""

    def test_returns_path(self):
        """Should return a Path object."""
        result = get_bundles_dir()
        assert isinstance(result, Path)

    def test_named_bundles(self):
        """Should be named 'bundles'."""
        assert get_bundles_dir().name == "bundles"


class TestGetEvidencePacksDir:
    """Tests for get_evidence_packs_dir function."""

    def test_returns_path(self):
        """Should return a Path object."""
        result = get_evidence_packs_dir()
        assert isinstance(result, Path)

    def test_named_evidence_packs(self):
        """Should be named 'evidence_packs'."""
        assert get_evidence_packs_dir().name == "evidence_packs"


class TestGetNotesDir:
    """Tests for get_notes_dir function."""

    def test_returns_path(self):
        """Should return a Path object."""
        result = get_notes_dir()
        assert isinstance(result, Path)

    def test_named_notes(self):
        """Should be named 'notes'."""
        assert get_notes_dir().name == "notes"


class TestSlugify:
    """Tests for slugify function."""

    def test_lowercase(self):
        """Should convert to lowercase."""
        assert slugify("WARFARIN") == "warfarin"
        assert slugify("Atrial Fibrillation") == "atrial_fibrillation"

    def test_spaces_to_underscores(self):
        """Should replace spaces with underscores."""
        assert slugify("atrial fibrillation") == "atrial_fibrillation"
        assert slugify("hello world") == "hello_world"

    def test_special_chars(self):
        """Should replace special characters."""
        # Hyphens are kept by \w pattern, slashes and @ are replaced
        assert slugify("test/case") == "test_case"
        assert slugify("test@case") == "test_case"
        # Hyphens are preserved (part of \w- pattern)
        result = slugify("drug-name")
        assert result in ["drug_name", "drug-name"]  # Either is acceptable

    def test_consecutive_underscores(self):
        """Should remove consecutive underscores."""
        assert slugify("test  case") == "test_case"
        assert slugify("a   b   c") == "a_b_c"

    def test_leading_trailing_underscores(self):
        """Should remove leading/trailing underscores."""
        assert slugify(" test ") == "test"
        assert slugify("_test_") == "test"

    def test_max_length(self):
        """Should truncate to 50 characters."""
        long_text = "a" * 100
        result = slugify(long_text)
        assert len(result) == 50

    def test_preserves_alphanumeric(self):
        """Should preserve alphanumeric characters."""
        assert slugify("drug123") == "drug123"
        assert slugify("test_2024") == "test_2024"


class TestGetCandidateDir:
    """Tests for get_candidate_dir function."""

    def test_drug_only(self):
        """Should create directory for drug only."""
        result = get_candidate_dir("warfarin")
        assert result.name == "warfarin"

    def test_drug_and_disease(self):
        """Should create directory for drug-disease pair."""
        result = get_candidate_dir("warfarin", "atrial fibrillation")
        assert result.name == "warfarin_atrial_fibrillation"

    def test_custom_base_dir(self, tmp_path):
        """Should use custom base directory."""
        result = get_candidate_dir("warfarin", "af", base_dir=tmp_path)
        assert result.parent == tmp_path

    def test_default_base_dir(self):
        """Should use bundles dir as default."""
        result = get_candidate_dir("warfarin")
        assert result.parent == get_bundles_dir()

    def test_slugifies_names(self):
        """Should slugify drug and disease names."""
        result = get_candidate_dir("WARFARIN", "Atrial Fibrillation")
        assert result.name == "warfarin_atrial_fibrillation"


class TestEnsureCandidateDirs:
    """Tests for ensure_candidate_dirs function."""

    def test_returns_dict(self):
        """Should return dictionary with paths."""
        result = ensure_candidate_dirs("warfarin", "af")
        assert isinstance(result, dict)
        assert "bundles" in result
        assert "evidence_packs" in result
        assert "notes" in result

    def test_creates_directories(self):
        """Should create all directories."""
        result = ensure_candidate_dirs("test_drug_xyz", "test_disease_xyz")
        for key, path in result.items():
            assert path.exists(), f"{key} directory should exist"
            # Clean up
            path.rmdir()

    def test_paths_are_correct(self):
        """Should return correct paths."""
        result = ensure_candidate_dirs("warfarin", "atrial fibrillation")
        expected_name = "warfarin_atrial_fibrillation"
        assert result["bundles"].name == expected_name
        assert result["evidence_packs"].name == expected_name
        assert result["notes"].name == expected_name

    def test_drug_only(self):
        """Should work with drug only."""
        result = ensure_candidate_dirs("aspirin")
        assert result["bundles"].name == "aspirin"
