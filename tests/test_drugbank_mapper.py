"""測試 DrugBank 映射模組"""

import pytest
import pandas as pd

from twtxgnn.mapping.drugbank_mapper import (
    load_drugbank_vocab,
    build_name_index,
    map_ingredient_to_drugbank,
    get_mapping_stats,
)


class TestLoadDrugbankVocab:
    """測試 load_drugbank_vocab 函數"""

    def test_returns_dataframe(self):
        """確認回傳 DataFrame"""
        df = load_drugbank_vocab()
        assert isinstance(df, pd.DataFrame)

    def test_has_required_columns(self):
        """確認包含必要欄位"""
        df = load_drugbank_vocab()
        assert "drugbank_id" in df.columns
        assert "drug_name" in df.columns
        assert "drug_name_upper" in df.columns

    def test_has_drugs(self):
        """確認有藥品資料"""
        df = load_drugbank_vocab()
        assert len(df) > 7000


class TestBuildNameIndex:
    """測試 build_name_index 函數"""

    def test_returns_dict(self):
        """確認回傳字典"""
        df = load_drugbank_vocab()
        index = build_name_index(df)
        assert isinstance(index, dict)

    def test_includes_synonyms(self):
        """確認包含同義詞"""
        df = load_drugbank_vocab()
        index = build_name_index(df)

        # CAFFEINE ANHYDROUS 應該映射到 CAFFEINE
        assert "CAFFEINE ANHYDROUS" in index
        assert "CAFFEINE" in index
        assert index["CAFFEINE ANHYDROUS"] == index["CAFFEINE"]


class TestMapIngredientToDrugbank:
    """測試 map_ingredient_to_drugbank 函數"""

    @pytest.fixture
    def name_index(self):
        df = load_drugbank_vocab()
        return build_name_index(df)

    def test_exact_match(self, name_index):
        """完全匹配"""
        result = map_ingredient_to_drugbank("METFORMIN", name_index)
        assert result is not None
        assert result.startswith("DB")

    def test_with_salt_suffix(self, name_index):
        """帶鹽類後綴"""
        result = map_ingredient_to_drugbank("METFORMIN HCL", name_index)
        assert result is not None

    def test_with_l_prefix(self, name_index):
        """帶 L- 前綴"""
        result = map_ingredient_to_drugbank("L-MENTHOL", name_index)
        assert result is not None

    def test_unmappable_returns_none(self, name_index):
        """無法映射回傳 None"""
        result = map_ingredient_to_drugbank("SOME_FAKE_DRUG_12345", name_index)
        assert result is None


class TestGetMappingStats:
    """測試 get_mapping_stats 函數"""

    def test_returns_dict(self):
        """確認回傳字典"""
        df = pd.DataFrame({
            "標準化成分": ["A", "B", "C"],
            "drugbank_id": ["DB001", None, "DB002"],
            "映射成功": [True, False, True],
        })
        stats = get_mapping_stats(df)
        assert isinstance(stats, dict)
        assert stats["total_ingredients"] == 3
        assert stats["mapped_ingredients"] == 2
        assert stats["mapping_rate"] == pytest.approx(2/3)
