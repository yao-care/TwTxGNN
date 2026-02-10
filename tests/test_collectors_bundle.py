"""Tests for bundle aggregator and related classes."""

import json
import pytest
from datetime import datetime
from pathlib import Path

from twtxgnn.collectors.bundle import (
    CandidateInfo,
    EvidenceBundle,
    BundleAggregator,
)
from twtxgnn.collectors.base import BaseCollector, CollectorResult


class TestCandidateInfo:
    """Tests for CandidateInfo dataclass."""

    def test_create_minimal(self):
        """Should create with just INN."""
        candidate = CandidateInfo(inn="warfarin")
        assert candidate.inn == "warfarin"
        assert candidate.drugbank_id is None
        assert candidate.indication_raw is None

    def test_create_full(self):
        """Should create with all fields."""
        candidate = CandidateInfo(
            inn="warfarin",
            drugbank_id="DB00682",
            brand_name_zh="華法林",
            license_id="12345",
            indication_raw="atrial fibrillation",
            txgnn_score=0.85,
            txgnn_rank=10,
            model_version="1.0",
            run_date="2024-01-01",
        )
        assert candidate.inn == "warfarin"
        assert candidate.drugbank_id == "DB00682"
        assert candidate.brand_name_zh == "華法林"
        assert candidate.txgnn_score == 0.85

    def test_to_dict(self):
        """Should convert to dictionary."""
        candidate = CandidateInfo(
            inn="warfarin",
            drugbank_id="DB00682",
            txgnn_score=0.85,
        )
        d = candidate.to_dict()
        assert d["inn"] == "warfarin"
        assert d["drugbank_id"] == "DB00682"
        assert d["txgnn_score"] == 0.85
        assert d["brand_name_zh"] is None


class TestEvidenceBundle:
    """Tests for EvidenceBundle dataclass."""

    def test_create_minimal(self):
        """Should create with minimal info."""
        candidate = CandidateInfo(inn="warfarin")
        bundle = EvidenceBundle(candidate=candidate)
        assert bundle.candidate.inn == "warfarin"
        assert bundle.tfda == {"found": False, "records": []}
        assert bundle.trials == {"clinicaltrials_gov": [], "who_ictrp": []}

    def test_default_metadata_timestamp(self):
        """Should add created_at timestamp."""
        candidate = CandidateInfo(inn="warfarin")
        bundle = EvidenceBundle(candidate=candidate)
        assert "created_at" in bundle.metadata

    def test_preserves_existing_metadata(self):
        """Should preserve existing metadata."""
        candidate = CandidateInfo(inn="warfarin")
        bundle = EvidenceBundle(
            candidate=candidate,
            metadata={"custom": "value", "created_at": "existing"},
        )
        assert bundle.metadata["custom"] == "value"
        assert bundle.metadata["created_at"] == "existing"

    def test_to_dict(self):
        """Should convert to dictionary."""
        candidate = CandidateInfo(inn="warfarin")
        bundle = EvidenceBundle(
            candidate=candidate,
            tfda={"found": True, "records": [{"id": 1}]},
        )
        d = bundle.to_dict()
        assert d["candidate"]["inn"] == "warfarin"
        assert d["tfda"]["found"] is True
        assert len(d["tfda"]["records"]) == 1

    def test_to_json(self):
        """Should convert to JSON string."""
        candidate = CandidateInfo(inn="warfarin")
        bundle = EvidenceBundle(candidate=candidate)
        json_str = bundle.to_json()
        data = json.loads(json_str)
        assert data["candidate"]["inn"] == "warfarin"

    def test_to_json_unicode(self):
        """Should handle unicode in JSON."""
        candidate = CandidateInfo(inn="warfarin", brand_name_zh="華法林")
        bundle = EvidenceBundle(candidate=candidate)
        json_str = bundle.to_json()
        assert "華法林" in json_str

    def test_save_and_load(self, tmp_path):
        """Should save and load bundle."""
        candidate = CandidateInfo(
            inn="warfarin",
            drugbank_id="DB00682",
            indication_raw="af",
        )
        bundle = EvidenceBundle(
            candidate=candidate,
            tfda={"found": True, "records": [{"id": 1}]},
            pubmed={"query": "warfarin af", "results": [{"pmid": "123"}]},
        )

        # Save
        output_path = bundle.save(output_dir=tmp_path)
        assert output_path.exists()
        assert output_path.name == "bundle.json"

        # Load
        loaded = EvidenceBundle.load(output_path)
        assert loaded.candidate.inn == "warfarin"
        assert loaded.candidate.drugbank_id == "DB00682"
        assert loaded.tfda["found"] is True
        assert len(loaded.pubmed["results"]) == 1

    def test_save_creates_directory(self, tmp_path):
        """Should create directory if not exists."""
        candidate = CandidateInfo(inn="warfarin", indication_raw="af")
        bundle = EvidenceBundle(candidate=candidate)
        output_dir = tmp_path / "nested" / "dir"
        output_path = bundle.save(output_dir=output_dir)
        assert output_path.exists()

    def test_load_handles_missing_fields(self, tmp_path):
        """Should handle missing optional fields."""
        # Create minimal JSON
        data = {
            "candidate": {"inn": "warfarin"},
        }
        path = tmp_path / "minimal.json"
        with open(path, "w") as f:
            json.dump(data, f)

        loaded = EvidenceBundle.load(path)
        assert loaded.candidate.inn == "warfarin"
        assert loaded.tfda == {"found": False, "records": []}


class MockCollector(BaseCollector):
    """Mock collector for testing."""

    source_name = "mock"

    def __init__(self, data=None, success=True, error=None):
        self.data = data
        self.success = success
        self.error = error

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        if self.error:
            raise self.error
        return self._make_result(
            query={"drug": drug, "disease": disease},
            data=self.data,
            success=self.success,
        )


class TestBundleAggregator:
    """Tests for BundleAggregator class."""

    def test_register_collector(self):
        """Should register collectors."""
        aggregator = BundleAggregator(save_collected=False)
        collector = MockCollector()
        aggregator.register_collector("mock", collector)
        assert "mock" in aggregator.collectors

    def test_collect_single_source(self, tmp_path):
        """Should collect from single source."""
        aggregator = BundleAggregator(save_collected=False)
        aggregator.register_collector("mock", MockCollector(data={"result": "data"}))

        candidate = CandidateInfo(inn="warfarin", indication_raw="af")
        bundle = aggregator.collect(candidate, save_bundle=False)

        assert bundle.other["mock"] == {"result": "data"}

    def test_collect_multiple_sources(self, tmp_path):
        """Should collect from multiple sources."""
        aggregator = BundleAggregator(save_collected=False)
        aggregator.register_collector("source1", MockCollector(data={"s1": "data"}))
        aggregator.register_collector("source2", MockCollector(data={"s2": "data"}))

        candidate = CandidateInfo(inn="warfarin")
        bundle = aggregator.collect(candidate, save_bundle=False)

        assert "source1" in bundle.other
        assert "source2" in bundle.other

    def test_collect_specific_sources(self, tmp_path):
        """Should collect only from specified sources."""
        aggregator = BundleAggregator(save_collected=False)
        aggregator.register_collector("source1", MockCollector(data={"s1": "data"}))
        aggregator.register_collector("source2", MockCollector(data={"s2": "data"}))

        candidate = CandidateInfo(inn="warfarin")
        bundle = aggregator.collect(
            candidate, sources=["source1"], save_bundle=False
        )

        assert "source1" in bundle.other
        assert "source2" not in bundle.other

    def test_collect_handles_errors(self, tmp_path):
        """Should handle collector errors."""
        aggregator = BundleAggregator(save_collected=False)
        aggregator.register_collector(
            "failing", MockCollector(error=ValueError("Test error"))
        )

        candidate = CandidateInfo(inn="warfarin")
        bundle = aggregator.collect(candidate, save_bundle=False)

        assert "errors" in bundle.metadata
        assert "failing" in bundle.metadata["errors"]

    def test_collect_skips_unknown_sources(self, tmp_path):
        """Should skip sources not registered."""
        aggregator = BundleAggregator(save_collected=False)
        aggregator.register_collector("known", MockCollector(data={"k": "data"}))

        candidate = CandidateInfo(inn="warfarin")
        bundle = aggregator.collect(
            candidate, sources=["known", "unknown"], save_bundle=False
        )

        assert "known" in bundle.other
        assert "unknown" not in bundle.other

    def test_merge_tfda_result(self, tmp_path):
        """Should merge TFDA result to correct field."""
        aggregator = BundleAggregator(save_collected=False)
        tfda_data = {"found": True, "records": [{"id": 1}]}
        aggregator.register_collector("tfda", MockCollector(data=tfda_data))

        candidate = CandidateInfo(inn="warfarin")
        bundle = aggregator.collect(candidate, save_bundle=False)

        assert bundle.tfda == tfda_data

    def test_merge_clinicaltrials_result(self, tmp_path):
        """Should merge ClinicalTrials result to correct field."""
        aggregator = BundleAggregator(save_collected=False)
        trials_data = [{"nct_id": "NCT001"}]
        aggregator.register_collector("clinicaltrials", MockCollector(data=trials_data))

        candidate = CandidateInfo(inn="warfarin")
        bundle = aggregator.collect(candidate, save_bundle=False)

        assert bundle.trials["clinicaltrials_gov"] == trials_data

    def test_merge_pubmed_result(self, tmp_path):
        """Should merge PubMed result to correct field."""
        aggregator = BundleAggregator(save_collected=False)
        pubmed_data = {"query": "test", "results": [{"pmid": "123"}]}
        aggregator.register_collector("pubmed", MockCollector(data=pubmed_data))

        candidate = CandidateInfo(inn="warfarin")
        bundle = aggregator.collect(candidate, save_bundle=False)

        assert bundle.pubmed == pubmed_data

    def test_merge_unified_ddi_result(self, tmp_path):
        """Should merge Unified DDI result to correct field."""
        aggregator = BundleAggregator(save_collected=False)
        ddi_data = [{"interacting_drug": "aspirin", "level": "Major", "source": "ddinter"}]
        aggregator.register_collector("unified_ddi", MockCollector(data=ddi_data))

        candidate = CandidateInfo(inn="warfarin")
        bundle = aggregator.collect(candidate, save_bundle=False)

        assert bundle.safety["ddi"] == ddi_data

    def test_merge_ictrp_result(self, tmp_path):
        """Should merge ICTRP result to correct field."""
        aggregator = BundleAggregator(save_collected=False)
        ictrp_data = [{"trial_id": "EUCTR001"}]
        aggregator.register_collector("ictrp", MockCollector(data=ictrp_data))

        candidate = CandidateInfo(inn="warfarin")
        bundle = aggregator.collect(candidate, save_bundle=False)

        assert bundle.trials["who_ictrp"] == ictrp_data

    def test_does_not_merge_failed_result(self, tmp_path):
        """Should not merge failed results."""
        aggregator = BundleAggregator(save_collected=False)
        aggregator.register_collector(
            "tfda", MockCollector(data={"found": True}, success=False)
        )

        candidate = CandidateInfo(inn="warfarin")
        bundle = aggregator.collect(candidate, save_bundle=False)

        assert bundle.tfda == {"found": False, "records": []}

    def test_metadata_contains_sources_queried(self, tmp_path):
        """Should record sources queried in metadata."""
        aggregator = BundleAggregator(save_collected=False)
        aggregator.register_collector("mock", MockCollector(data={"test": "data"}))

        candidate = CandidateInfo(inn="warfarin", indication_raw="af")
        bundle = aggregator.collect(candidate, save_bundle=False)

        assert "sources_queried" in bundle.metadata
        assert "mock" in bundle.metadata["sources_queried"]
