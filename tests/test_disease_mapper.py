"""測試疾病映射模組"""

import pytest
import pandas as pd

from twtxgnn.mapping.disease_mapper import (
    load_disease_vocab,
    build_disease_index,
    extract_indications,
    translate_indication,
    map_indication_to_disease,
    get_indication_mapping_stats,
)


class TestLoadDiseaseVocab:
    """測試 load_disease_vocab 函數"""

    def test_returns_dataframe(self):
        df = load_disease_vocab()
        assert isinstance(df, pd.DataFrame)

    def test_has_required_columns(self):
        df = load_disease_vocab()
        assert "disease_id" in df.columns
        assert "disease_name" in df.columns

    def test_has_diseases(self):
        df = load_disease_vocab()
        assert len(df) > 10000


class TestExtractIndications:
    """測試 extract_indications 函數"""

    def test_single_indication(self):
        result = extract_indications("癲癇")
        assert "癲癇" in result

    def test_multiple_indications_comma(self):
        result = extract_indications("高血壓、糖尿病、心臟病")
        assert len(result) == 3
        assert "高血壓" in result
        assert "糖尿病" in result

    def test_removes_prefix(self):
        result = extract_indications("用於治療高血壓")
        assert "高血壓" in result

    def test_complex_indication(self):
        result = extract_indications("預防或緩解動暈症（暈車、暈船、暈機）引起之頭暈、噁心、嘔吐等症狀。")
        assert len(result) > 0


class TestTranslateIndication:
    """測試 translate_indication 函數"""

    def test_single_disease(self):
        result = translate_indication("高血壓")
        assert "HYPERTENSION" in result

    def test_multiple_diseases(self):
        result = translate_indication("高血壓合併糖尿病")
        assert "HYPERTENSION" in result
        assert "DIABETES" in result

    def test_no_match(self):
        result = translate_indication("某種罕見疾病")
        assert result == []


class TestMapIndicationToDisease:
    """測試 map_indication_to_disease 函數"""

    @pytest.fixture
    def disease_index(self):
        df = load_disease_vocab()
        return build_disease_index(df)

    def test_maps_hypertension(self, disease_index):
        results = map_indication_to_disease("高血壓", disease_index)
        assert len(results) > 0
        # 至少有一個匹配包含 hypertension
        disease_names = [r[1].lower() for r in results]
        assert any("hypertension" in name for name in disease_names)

    def test_maps_diabetes(self, disease_index):
        results = map_indication_to_disease("糖尿病", disease_index)
        assert len(results) > 0

    def test_no_match_returns_empty(self, disease_index):
        results = map_indication_to_disease("某種不存在的疾病", disease_index)
        assert results == []


class TestGetIndicationMappingStats:
    """測試 get_indication_mapping_stats 函數"""

    def test_returns_dict(self):
        df = pd.DataFrame({
            "提取適應症": ["高血壓", "糖尿病", "某病"],
            "disease_id": ["D001", "D002", None],
            "disease_name": ["hypertension", "diabetes", None],
        })
        stats = get_indication_mapping_stats(df)
        assert isinstance(stats, dict)
        assert stats["total_indications"] == 3
        assert stats["mapped_indications"] == 2
