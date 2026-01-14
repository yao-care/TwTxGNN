"""測試資料載入模組"""

import pytest
from pathlib import Path

from twtxgnn.data.loader import load_fda_drugs, filter_active_drugs, get_drug_summary


class TestLoadFdaDrugs:
    """測試 load_fda_drugs 函數"""

    def test_load_returns_dataframe(self):
        """確認載入後回傳 DataFrame"""
        df = load_fda_drugs()
        assert hasattr(df, "columns")
        assert len(df) > 0

    def test_load_has_required_columns(self):
        """確認包含必要欄位"""
        df = load_fda_drugs()
        required_columns = ["許可證字號", "中文品名", "主成分略述", "適應症", "註銷狀態"]
        for col in required_columns:
            assert col in df.columns, f"缺少欄位: {col}"

    def test_load_total_count(self):
        """確認總筆數約 7 萬筆"""
        df = load_fda_drugs()
        assert len(df) > 70000


class TestFilterActiveDrugs:
    """測試 filter_active_drugs 函數"""

    def test_filter_removes_cancelled(self):
        """確認過濾掉已註銷藥品"""
        df = load_fda_drugs()
        active = filter_active_drugs(df)

        # 確認沒有已註銷的藥品
        assert (active["註銷狀態"] != "已註銷").all()

    def test_filter_removes_empty_ingredients(self):
        """確認過濾掉無主成分的藥品"""
        df = load_fda_drugs()
        active = filter_active_drugs(df)

        # 確認都有主成分
        assert active["主成分略述"].notna().all()
        assert (active["主成分略述"] != "").all()

    def test_filter_count_reasonable(self):
        """確認有效藥品數量合理（約 2 萬多）"""
        df = load_fda_drugs()
        active = filter_active_drugs(df)

        assert len(active) > 20000
        assert len(active) < 30000


class TestGetDrugSummary:
    """測試 get_drug_summary 函數"""

    def test_summary_has_keys(self):
        """確認摘要包含必要欄位"""
        df = load_fda_drugs()
        active = filter_active_drugs(df)
        summary = get_drug_summary(active)

        assert "total_count" in summary
        assert "with_ingredient" in summary
        assert "unique_ingredients" in summary
