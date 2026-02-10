"""Tests for TFDA collector."""

import json
import pytest
from pathlib import Path

from twtxgnn.collectors.tfda import TFDACollector


@pytest.fixture
def sample_tfda_data():
    """Sample TFDA drug records."""
    return [
        {
            "許可證字號": "衛部藥製字第000001號",
            "中文品名": "華法林錠",
            "英文品名": "Warfarin Tablets",
            "主成分略述": "WARFARIN SODIUM",
            "適應症": "預防或治療因心房纖維顫動引起之血栓性栓塞症",
            "劑型": "錠劑",
            "製造廠名稱": "測試藥廠",
            "申請商名稱": "測試公司",
            "發證日期": "2020-01-01",
            "有效日期": "2025-01-01",
            "註銷狀態": "",
            "用法用量": "每日一次，依醫師指示",
        },
        {
            "許可證字號": "衛部藥製字第000002號",
            "中文品名": "阿斯匹靈錠",
            "英文品名": "Aspirin Tablets",
            "主成分略述": "ASPIRIN",
            "適應症": "鎮痛、解熱、抗發炎",
            "劑型": "錠劑",
            "製造廠名稱": "另一藥廠",
            "申請商名稱": "另一公司",
            "發證日期": "2019-01-01",
            "有效日期": "2024-01-01",
            "註銷狀態": "",
        },
        {
            "許可證字號": "衛部藥製字第000003號",
            "中文品名": "另一華法林品牌",
            "英文品名": "Warfarin Brand B",
            "主成分略述": "WARFARIN SODIUM",
            "適應症": "抗凝血劑用於靜脈栓塞預防",
            "劑型": "錠劑",
            "製造廠名稱": "第三藥廠",
            "申請商名稱": "第三公司",
            "發證日期": "2021-01-01",
            "有效日期": "2026-01-01",
            "註銷狀態": "",
        },
    ]


@pytest.fixture
def tfda_data_file(tmp_path, sample_tfda_data):
    """Create temporary TFDA data file."""
    data_file = tmp_path / "tw_fda_drugs.json"
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(sample_tfda_data, f, ensure_ascii=False)
    return data_file


class TestTFDACollector:
    """Tests for TFDACollector class."""

    def test_source_name(self, tfda_data_file):
        """Should have correct source name."""
        collector = TFDACollector(data_path=tfda_data_file)
        assert collector.source_name == "tfda"

    def test_search_by_english_name(self, tfda_data_file):
        """Should find drugs by English name."""
        collector = TFDACollector(data_path=tfda_data_file)
        result = collector.search("warfarin")

        assert result.success is True
        assert result.data["found"] is True
        assert len(result.data["records"]) == 2  # Two warfarin products

    def test_search_by_chinese_name(self, tfda_data_file):
        """Should find drugs by Chinese name."""
        collector = TFDACollector(data_path=tfda_data_file)
        result = collector.search("華法林")

        assert result.success is True
        assert result.data["found"] is True
        assert len(result.data["records"]) == 2

    def test_search_by_ingredient(self, tfda_data_file):
        """Should find drugs by ingredient."""
        collector = TFDACollector(data_path=tfda_data_file)
        result = collector.search("ASPIRIN")

        assert result.success is True
        assert result.data["found"] is True
        assert len(result.data["records"]) == 1

    def test_search_case_insensitive(self, tfda_data_file):
        """Should search case insensitively."""
        collector = TFDACollector(data_path=tfda_data_file)

        # Lowercase
        result1 = collector.search("warfarin")
        # Uppercase
        result2 = collector.search("WARFARIN")
        # Mixed case
        result3 = collector.search("Warfarin")

        assert result1.data["found"] == result2.data["found"] == result3.data["found"]
        assert (
            len(result1.data["records"])
            == len(result2.data["records"])
            == len(result3.data["records"])
        )

    def test_search_not_found(self, tfda_data_file):
        """Should return found=False for unknown drug."""
        collector = TFDACollector(data_path=tfda_data_file)
        result = collector.search("unknown_drug_xyz")

        assert result.success is True
        assert result.data["found"] is False
        assert result.data["records"] == []

    def test_search_with_disease_filter(self, tfda_data_file):
        """Should filter by disease/indication."""
        collector = TFDACollector(data_path=tfda_data_file)
        result = collector.search("warfarin", disease="心房纖維顫動")

        assert result.success is True
        assert result.data["found"] is True
        # Only one record has 心房纖維顫動 in indication
        assert len(result.data["records"]) == 1
        assert "心房纖維顫動" in result.data["records"][0]["indication"]

    def test_search_disease_filter_no_match_returns_all(self, tfda_data_file):
        """Should return all drug matches if disease filter has no matches."""
        collector = TFDACollector(data_path=tfda_data_file)
        result = collector.search("warfarin", disease="不存在的疾病")

        assert result.success is True
        assert result.data["found"] is True
        assert len(result.data["records"]) == 2  # Returns all warfarin matches

    def test_record_fields(self, tfda_data_file):
        """Should return properly formatted records."""
        collector = TFDACollector(data_path=tfda_data_file)
        result = collector.search("aspirin")

        record = result.data["records"][0]
        assert "license_id" in record
        assert "brand_name_zh" in record
        assert "brand_name_en" in record
        assert "ingredients" in record
        assert "indication" in record
        assert "dosage_form" in record
        assert "manufacturer" in record
        assert "license_holder" in record
        assert "approval_date" in record
        assert "expiry_date" in record
        assert "status" in record

    def test_record_values(self, tfda_data_file):
        """Should extract correct field values."""
        collector = TFDACollector(data_path=tfda_data_file)
        result = collector.search("aspirin")

        record = result.data["records"][0]
        assert record["license_id"] == "衛部藥製字第000002號"
        assert record["brand_name_zh"] == "阿斯匹靈錠"
        assert record["brand_name_en"] == "Aspirin Tablets"
        assert record["ingredients"] == "ASPIRIN"

    def test_total_matches_count(self, tfda_data_file):
        """Should include total matches count."""
        collector = TFDACollector(data_path=tfda_data_file)
        result = collector.search("warfarin")

        assert result.data["total_matches"] == 2

    def test_package_insert_summary(self, tfda_data_file):
        """Should include package insert summary."""
        collector = TFDACollector(data_path=tfda_data_file)
        result = collector.search("warfarin")

        assert "package_insert" in result.data
        pkg = result.data["package_insert"]
        assert "warnings" in pkg
        assert "contraindications" in pkg
        assert "dosage" in pkg
        assert "special_populations" in pkg

    def test_limits_records_to_20(self, tmp_path):
        """Should limit records to 20."""
        # Create data with more than 20 records
        data = [
            {
                "許可證字號": f"衛部藥製字第{i:06d}號",
                "中文品名": f"測試藥品{i}",
                "英文品名": f"Test Drug {i}",
                "主成分略述": "TEST INGREDIENT",
                "適應症": "測試適應症",
            }
            for i in range(30)
        ]
        data_file = tmp_path / "many_drugs.json"
        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

        collector = TFDACollector(data_path=data_file)
        result = collector.search("TEST")

        assert len(result.data["records"]) == 20
        assert result.data["total_matches"] == 30

    def test_get_by_license_id(self, tfda_data_file):
        """Should get record by license ID."""
        collector = TFDACollector(data_path=tfda_data_file)
        record = collector.get_by_license_id("衛部藥製字第000002號")

        assert record is not None
        assert record["中文品名"] == "阿斯匹靈錠"

    def test_get_by_license_id_not_found(self, tfda_data_file):
        """Should return None for unknown license ID."""
        collector = TFDACollector(data_path=tfda_data_file)
        record = collector.get_by_license_id("不存在的字號")

        assert record is None

    def test_caching(self, tfda_data_file):
        """Should cache loaded data."""
        collector = TFDACollector(data_path=tfda_data_file)

        # First search loads data
        collector.search("warfarin")
        assert collector._data is not None

        # Second search uses cached data
        cached_data = collector._data
        collector.search("aspirin")
        assert collector._data is cached_data

    def test_missing_data_file(self, tmp_path):
        """Should handle missing data file gracefully."""
        collector = TFDACollector(data_path=tmp_path / "nonexistent.json")
        result = collector.search("warfarin")

        assert result.success is True
        assert result.data["found"] is False
        assert result.data["records"] == []

    def test_query_in_result(self, tfda_data_file):
        """Should include query in result."""
        collector = TFDACollector(data_path=tfda_data_file)
        result = collector.search("warfarin", disease="af")

        assert result.query == {"drug": "warfarin", "disease": "af"}

    def test_search_by_indication(self, tfda_data_file):
        """Should find drugs by indication text."""
        collector = TFDACollector(data_path=tfda_data_file)
        result = collector.search("血栓")

        assert result.success is True
        assert result.data["found"] is True

    def test_handles_empty_fields(self, tmp_path):
        """Should handle records with empty fields."""
        data = [
            {
                "許可證字號": "TEST001",
                "中文品名": "",
                "英文品名": "Test Drug",
                "主成分略述": "",
                "適應症": "",
            }
        ]
        data_file = tmp_path / "sparse.json"
        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

        collector = TFDACollector(data_path=data_file)
        result = collector.search("Test Drug")

        assert result.success is True
        assert result.data["found"] is True

    def test_default_data_path(self):
        """Should use default data path."""
        collector = TFDACollector()
        expected_suffix = Path("data") / "raw" / "tw_fda_drugs.json"
        assert collector.data_path.parts[-3:] == expected_suffix.parts

    def test_handles_json_error(self, tmp_path):
        """Should handle invalid JSON file."""
        data_file = tmp_path / "invalid.json"
        with open(data_file, "w") as f:
            f.write("invalid json content")

        collector = TFDACollector(data_path=data_file)
        result = collector.search("test")

        assert result.success is False
        assert result.data["found"] is False
        assert result.error_message is not None
