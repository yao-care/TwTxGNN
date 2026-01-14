"""測試主成分標準化模組"""

import pytest

from twtxgnn.mapping.normalizer import (
    normalize_ingredient,
    extract_ingredients,
    extract_primary_ingredient,
    get_all_synonyms,
)


class TestNormalizeIngredient:
    """測試 normalize_ingredient 函數"""

    def test_simple_name(self):
        """簡單名稱不變"""
        assert normalize_ingredient("METRONIDAZOLE") == "METRONIDAZOLE"

    def test_removes_eq_to_synonym(self):
        """移除 EQ TO 同義詞"""
        result = normalize_ingredient("SODIUM BICARBONATE ( EQ TO SODIUM HYDROGEN CARBONATE)")
        assert result == "SODIUM BICARBONATE"

    def test_removes_vitamin_notation(self):
        """移除維生素標註"""
        result = normalize_ingredient("RIBOFLAVIN (VIT B2)")
        assert result == "RIBOFLAVIN"

    def test_uppercase(self):
        """統一大寫"""
        assert normalize_ingredient("metronidazole") == "METRONIDAZOLE"

    def test_removes_extra_spaces(self):
        """移除多餘空白"""
        result = normalize_ingredient("SODIUM   BICARBONATE")
        assert result == "SODIUM BICARBONATE"

    def test_empty_string(self):
        """空字串處理"""
        assert normalize_ingredient("") == ""
        assert normalize_ingredient(None) == ""


class TestExtractIngredients:
    """測試 extract_ingredients 函數"""

    def test_single_ingredient(self):
        """單一成分"""
        result = extract_ingredients("METRONIDAZOLE")
        assert result == ["METRONIDAZOLE"]

    def test_multiple_ingredients_semicolon(self):
        """多成分（分號分隔）"""
        result = extract_ingredients("DEXTROMETHORPHAN HBR;;DIPHENHYDRAMINE HCL")
        assert result == ["DEXTROMETHORPHAN HBR", "DIPHENHYDRAMINE HCL"]

    def test_multiple_ingredients_single_semicolon(self):
        """多成分（單分號分隔）"""
        result = extract_ingredients("VITAMIN A;VITAMIN C;VITAMIN E")
        assert result == ["VITAMIN A", "VITAMIN C", "VITAMIN E"]

    def test_removes_duplicates(self):
        """移除重複成分"""
        result = extract_ingredients("SUCROSE;;SUCROSE;;SUCROSE")
        assert result == ["SUCROSE"]

    def test_complex_with_synonyms(self):
        """複雜格式：多成分加同義詞"""
        result = extract_ingredients(
            "THIAMINE DISULFIDE;;RIBOFLAVIN (VIT B2)"
        )
        assert result == ["THIAMINE DISULFIDE", "RIBOFLAVIN"]


class TestExtractPrimaryIngredient:
    """測試 extract_primary_ingredient 函數"""

    def test_returns_first(self):
        """回傳第一個成分"""
        result = extract_primary_ingredient("VITAMIN A;;VITAMIN C")
        assert result == "VITAMIN A"

    def test_empty_returns_empty(self):
        """空輸入回傳空字串"""
        assert extract_primary_ingredient("") == ""


class TestGetAllSynonyms:
    """測試 get_all_synonyms 函數"""

    def test_single_eq_to(self):
        """單一 EQ TO 同義詞"""
        result = get_all_synonyms(
            "SODIUM BICARBONATE ( EQ TO SODIUM HYDROGEN CARBONATE)"
        )
        assert len(result) == 1
        assert result[0][0] == "SODIUM BICARBONATE"
        assert "SODIUM HYDROGEN CARBONATE" in result[0][1]

    def test_multiple_eq_to(self):
        """多個 EQ TO 同義詞"""
        result = get_all_synonyms(
            "WHITE SOFT PARAFFIN (EQ TO WHITE PETROLATUM)(EQ TO PARAFFIN WHITE SOFT)"
        )
        assert len(result) == 1
        assert result[0][0] == "WHITE SOFT PARAFFIN"
        assert len(result[0][1]) == 2

    def test_no_synonyms(self):
        """無同義詞"""
        result = get_all_synonyms("METRONIDAZOLE")
        assert len(result) == 1
        assert result[0][0] == "METRONIDAZOLE"
        assert result[0][1] == []
