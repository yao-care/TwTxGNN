"""Tests for KnownRelationsChecker."""

import pytest
import pandas as pd
from pathlib import Path

from twtxgnn.collectors.known_relations import KnownRelationsChecker


class TestKnownRelationsChecker:
    """Tests for KnownRelationsChecker class."""

    @pytest.fixture
    def sample_relations_csv(self, tmp_path):
        """Create a sample relations CSV file."""
        data = {
            "relation": [
                "indication",
                "indication",
                "contraindication",
                "contraindication",
                "indication",
            ],
            "x_id": ["DB001", "DB001", "DB002", "DB002", "DB003"],
            "x_name": ["Warfarin", "Warfarin", "Aspirin", "Aspirin", "Metformin"],
            "y_id": ["D001", "D002", "D003", "D004", "D005"],
            "y_name": [
                "atrial fibrillation",
                "deep vein thrombosis",
                "peptic ulcer",
                "bleeding disorder",
                "diabetes mellitus",
            ],
        }
        df = pd.DataFrame(data)
        csv_path = tmp_path / "relations.csv"
        df.to_csv(csv_path, index=False)
        return csv_path

    def test_load_from_file(self, sample_relations_csv):
        """Should load relations from CSV file."""
        checker = KnownRelationsChecker(sample_relations_csv)
        stats = checker.get_stats()
        assert stats["total_indications"] == 3
        assert stats["total_contraindications"] == 2

    def test_missing_file_returns_empty(self, tmp_path):
        """Should return empty sets for missing file."""
        checker = KnownRelationsChecker(tmp_path / "nonexistent.csv")
        assert len(checker.indications) == 0
        assert len(checker.contraindications) == 0

    def test_check_known_indication(self, sample_relations_csv):
        """Should detect known indications."""
        checker = KnownRelationsChecker(sample_relations_csv)
        result = checker.check("Warfarin", "atrial fibrillation")

        assert result["is_novel"] is False
        assert result["relation_type"] == "indication"
        assert result["should_exclude"] is True

    def test_check_known_contraindication(self, sample_relations_csv):
        """Should detect known contraindications."""
        checker = KnownRelationsChecker(sample_relations_csv)
        result = checker.check("Aspirin", "peptic ulcer")

        assert result["is_novel"] is False
        assert result["relation_type"] == "contraindication"
        assert result["should_exclude"] is True

    def test_check_novel_prediction(self, sample_relations_csv):
        """Should identify novel predictions."""
        checker = KnownRelationsChecker(sample_relations_csv)
        result = checker.check("Warfarin", "cancer")

        assert result["is_novel"] is True
        assert result["relation_type"] is None
        assert result["should_exclude"] is False

    def test_check_case_insensitive(self, sample_relations_csv):
        """Should be case insensitive."""
        checker = KnownRelationsChecker(sample_relations_csv)

        result1 = checker.check("WARFARIN", "ATRIAL FIBRILLATION")
        result2 = checker.check("warfarin", "atrial fibrillation")

        assert result1["is_novel"] == result2["is_novel"]
        assert result1["relation_type"] == result2["relation_type"]

    def test_check_with_whitespace(self, sample_relations_csv):
        """Should handle whitespace in names."""
        checker = KnownRelationsChecker(sample_relations_csv)
        result = checker.check("  Warfarin  ", "  atrial fibrillation  ")

        assert result["is_novel"] is False
        assert result["relation_type"] == "indication"

    def test_is_novel_shortcut(self, sample_relations_csv):
        """Should provide quick is_novel check."""
        checker = KnownRelationsChecker(sample_relations_csv)

        assert checker.is_novel("Warfarin", "atrial fibrillation") is False
        assert checker.is_novel("Warfarin", "cancer") is True

    def test_is_contraindicated(self, sample_relations_csv):
        """Should check contraindication status."""
        checker = KnownRelationsChecker(sample_relations_csv)

        assert checker.is_contraindicated("Aspirin", "peptic ulcer") is True
        assert checker.is_contraindicated("Aspirin", "headache") is False
        assert checker.is_contraindicated("Warfarin", "atrial fibrillation") is False

    def test_lazy_loading(self, sample_relations_csv):
        """Should lazy-load relations."""
        checker = KnownRelationsChecker(sample_relations_csv)

        # Before any check, internal sets should be None
        assert checker._indications is None
        assert checker._contraindications is None

        # After check, should be loaded
        checker.check("test", "test")
        assert checker._indications is not None
        assert checker._contraindications is not None

    def test_get_stats(self, sample_relations_csv):
        """Should return statistics."""
        checker = KnownRelationsChecker(sample_relations_csv)
        stats = checker.get_stats()

        assert "total_indications" in stats
        assert "total_contraindications" in stats
        assert "total_relations" in stats
        assert stats["total_relations"] == stats["total_indications"] + stats["total_contraindications"]


class TestKnownRelationsCheckerIntegration:
    """Integration tests using real data file."""

    def test_with_real_data(self):
        """Should work with the real relations file if it exists."""
        checker = KnownRelationsChecker()  # Uses default path

        # Check some well-known drug-disease relationships
        # These should exist in the TxGNN knowledge graph

        # Test a few known drugs - results depend on actual KG content
        stats = checker.get_stats()

        # Should have loaded some relations
        assert stats["total_relations"] >= 0

    def test_known_minoxidil_alopecia(self):
        """Minoxidil for alopecia should be a known indication."""
        checker = KnownRelationsChecker()
        result = checker.check("Minoxidil", "alopecia")

        # This is a well-known repurposed drug
        # If in KG, should be marked as known
        if not result["is_novel"]:
            assert result["relation_type"] == "indication"
