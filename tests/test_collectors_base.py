"""Tests for base collector classes."""

import pytest
from datetime import datetime

from twtxgnn.collectors.base import CollectorResult, BaseCollector


class TestCollectorResult:
    """Tests for CollectorResult dataclass."""

    def test_create_basic(self):
        """Should create result with basic fields."""
        result = CollectorResult(
            source="test",
            query={"drug": "warfarin"},
            data={"results": []},
        )
        assert result.source == "test"
        assert result.query == {"drug": "warfarin"}
        assert result.data == {"results": []}
        assert result.success is True
        assert result.error_message is None

    def test_default_timestamp(self):
        """Should set timestamp to now by default."""
        before = datetime.now()
        result = CollectorResult(
            source="test",
            query={},
            data=None,
        )
        after = datetime.now()
        assert before <= result.timestamp <= after

    def test_custom_timestamp(self):
        """Should accept custom timestamp."""
        custom_time = datetime(2024, 1, 1, 12, 0, 0)
        result = CollectorResult(
            source="test",
            query={},
            data=None,
            timestamp=custom_time,
        )
        assert result.timestamp == custom_time

    def test_error_result(self):
        """Should create error result."""
        result = CollectorResult(
            source="test",
            query={"drug": "invalid"},
            data=None,
            success=False,
            error_message="API error",
        )
        assert result.success is False
        assert result.error_message == "API error"

    def test_to_dict(self):
        """Should convert to dictionary."""
        result = CollectorResult(
            source="pubmed",
            query={"drug": "warfarin", "disease": "af"},
            data={"count": 10},
            success=True,
        )
        d = result.to_dict()
        assert d["source"] == "pubmed"
        assert d["query"] == {"drug": "warfarin", "disease": "af"}
        assert d["data"] == {"count": 10}
        assert d["success"] is True
        assert d["error_message"] is None
        assert "timestamp" in d
        # Timestamp should be ISO format string
        assert isinstance(d["timestamp"], str)

    def test_to_dict_with_error(self):
        """Should include error message in dict."""
        result = CollectorResult(
            source="test",
            query={},
            data=None,
            success=False,
            error_message="Something went wrong",
        )
        d = result.to_dict()
        assert d["success"] is False
        assert d["error_message"] == "Something went wrong"


class ConcreteCollector(BaseCollector):
    """Concrete implementation for testing."""

    source_name = "test_collector"

    def __init__(self, return_data=None, raise_error=False):
        self.return_data = return_data or {"default": "data"}
        self.raise_error = raise_error
        self.search_calls = []

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        self.search_calls.append((drug, disease))
        if self.raise_error:
            raise ValueError("Test error")
        return self._make_result(
            query={"drug": drug, "disease": disease},
            data=self.return_data,
        )


class TestBaseCollector:
    """Tests for BaseCollector abstract class."""

    def test_source_name(self):
        """Should have source_name attribute."""
        collector = ConcreteCollector()
        assert collector.source_name == "test_collector"

    def test_search(self):
        """Should call search method."""
        collector = ConcreteCollector(return_data={"test": "data"})
        result = collector.search("warfarin", "af")
        assert result.source == "test_collector"
        assert result.data == {"test": "data"}
        assert result.query == {"drug": "warfarin", "disease": "af"}
        assert result.success is True

    def test_search_drug_only(self):
        """Should work with drug only."""
        collector = ConcreteCollector()
        result = collector.search("aspirin")
        assert result.query == {"drug": "aspirin", "disease": None}

    def test_batch_search(self):
        """Should search multiple pairs."""
        collector = ConcreteCollector()
        pairs = [
            ("warfarin", "af"),
            ("aspirin", "pain"),
            ("metformin", "diabetes"),
        ]
        results = collector.batch_search(pairs)
        assert len(results) == 3
        assert len(collector.search_calls) == 3
        for i, (drug, disease) in enumerate(pairs):
            assert results[i].query["drug"] == drug
            assert results[i].query["disease"] == disease

    def test_batch_search_handles_errors(self):
        """Should handle errors in batch search."""
        collector = ConcreteCollector(raise_error=True)
        pairs = [("drug1", "disease1"), ("drug2", "disease2")]
        results = collector.batch_search(pairs)
        assert len(results) == 2
        for result in results:
            assert result.success is False
            assert "Test error" in result.error_message

    def test_batch_search_empty(self):
        """Should handle empty pairs list."""
        collector = ConcreteCollector()
        results = collector.batch_search([])
        assert results == []

    def test_make_result_helper(self):
        """Should create result with helper method."""
        collector = ConcreteCollector()
        result = collector._make_result(
            query={"drug": "test"},
            data={"result": "data"},
        )
        assert result.source == "test_collector"
        assert result.query == {"drug": "test"}
        assert result.data == {"result": "data"}
        assert result.success is True

    def test_make_result_with_error(self):
        """Should create error result with helper."""
        collector = ConcreteCollector()
        result = collector._make_result(
            query={"drug": "test"},
            data=None,
            success=False,
            error_message="Error occurred",
        )
        assert result.success is False
        assert result.error_message == "Error occurred"


class TestBaseCollectorAbstract:
    """Tests for abstract behavior."""

    def test_cannot_instantiate_base(self):
        """Should not be able to instantiate BaseCollector directly."""
        with pytest.raises(TypeError):
            BaseCollector()

    def test_must_implement_search(self):
        """Should require search method implementation."""

        class IncompleteCollector(BaseCollector):
            source_name = "incomplete"

        with pytest.raises(TypeError):
            IncompleteCollector()
