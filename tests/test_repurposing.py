"""測試老藥新用預測模組"""

import pytest
import pandas as pd

from twtxgnn.predict.repurposing import (
    load_drug_disease_relations,
    build_drug_indication_map,
    generate_repurposing_report,
)


class TestLoadDrugDiseaseRelations:
    """測試 load_drug_disease_relations 函數"""

    def test_returns_dataframe(self):
        df = load_drug_disease_relations()
        assert isinstance(df, pd.DataFrame)

    def test_has_required_columns(self):
        df = load_drug_disease_relations()
        assert "relation" in df.columns
        assert "x_name" in df.columns
        assert "y_name" in df.columns

    def test_has_relations(self):
        df = load_drug_disease_relations()
        assert len(df) > 40000


class TestBuildDrugIndicationMap:
    """測試 build_drug_indication_map 函數"""

    def test_returns_dict(self):
        df = load_drug_disease_relations()
        drug_map = build_drug_indication_map(df)
        assert isinstance(drug_map, dict)

    def test_contains_drugs(self):
        df = load_drug_disease_relations()
        drug_map = build_drug_indication_map(df)
        assert len(drug_map) > 1000

    def test_drug_has_diseases(self):
        df = load_drug_disease_relations()
        drug_map = build_drug_indication_map(df)
        # 任意一個藥物應該有至少一個適應症
        for drug, diseases in list(drug_map.items())[:10]:
            assert len(diseases) > 0


class TestGenerateRepurposingReport:
    """測試 generate_repurposing_report 函數"""

    def test_empty_dataframe(self):
        empty_df = pd.DataFrame()
        report = generate_repurposing_report(empty_df)
        assert report["total_candidates"] == 0

    def test_with_data(self):
        df = pd.DataFrame({
            "許可證字號": ["A001", "A001", "A002"],
            "中文品名": ["藥物A", "藥物A", "藥物B"],
            "藥物成分": ["DRUG_A", "DRUG_A", "DRUG_B"],
            "drugbank_id": ["DB001", "DB001", "DB002"],
            "潛在新適應症": ["disease1", "disease2", "disease1"],
            "來源": ["TxGNN", "TxGNN", "TxGNN"],
        })
        report = generate_repurposing_report(df)
        assert report["total_candidates"] == 3
        assert report["unique_drugs"] == 2
        assert report["unique_diseases"] == 2
