"""測試 prepare_external_data 腳本的資料提取函數"""

import pytest
import pandas as pd
from pathlib import Path
import sys

# 將 scripts 加入 Python 路徑
scripts_path = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(scripts_path))

from prepare_external_data import (
    extract_drugbank_vocab,
    extract_disease_vocab,
    extract_drug_disease_relations,
)


class TestExtractDrugbankVocab:
    """測試 extract_drugbank_vocab 函數"""

    def test_extracts_drug_nodes_only(self):
        """確認只提取 drug 類型的節點"""
        mock_nodes = pd.DataFrame({
            "node_id": ["DB00001", "DB00002", "DOID:1", "12345"],
            "node_name": ["Drug A", "Drug B", "Disease X", "Gene Y"],
            "node_type": ["drug", "drug", "disease", "gene/protein"],
            "node_index": [0, 1, 100, 200],
        })

        result = extract_drugbank_vocab(mock_nodes)

        assert len(result) == 2
        assert set(result["drugbank_id"]) == {"DB00001", "DB00002"}

    def test_has_required_columns(self):
        """確認輸出包含必要欄位"""
        mock_nodes = pd.DataFrame({
            "node_id": ["DB00001"],
            "node_name": ["Aspirin"],
            "node_type": ["drug"],
            "node_index": [0],
        })

        result = extract_drugbank_vocab(mock_nodes)

        assert "drugbank_id" in result.columns
        assert "drug_name" in result.columns
        assert "drug_name_upper" in result.columns

    def test_uppercase_conversion(self):
        """確認大寫轉換正確"""
        mock_nodes = pd.DataFrame({
            "node_id": ["DB00001"],
            "node_name": ["Aspirin"],
            "node_type": ["drug"],
            "node_index": [0],
        })

        result = extract_drugbank_vocab(mock_nodes)

        assert result.iloc[0]["drug_name"] == "Aspirin"
        assert result.iloc[0]["drug_name_upper"] == "ASPIRIN"

    def test_removes_duplicates(self):
        """確認移除重複項"""
        mock_nodes = pd.DataFrame({
            "node_id": ["DB00001", "DB00001"],
            "node_name": ["Aspirin", "Aspirin"],
            "node_type": ["drug", "drug"],
            "node_index": [0, 0],
        })

        result = extract_drugbank_vocab(mock_nodes)

        assert len(result) == 1

    def test_empty_input(self):
        """測試空輸入"""
        mock_nodes = pd.DataFrame({
            "node_id": [],
            "node_name": [],
            "node_type": [],
            "node_index": [],
        })

        result = extract_drugbank_vocab(mock_nodes)

        assert len(result) == 0
        assert "drugbank_id" in result.columns


class TestExtractDiseaseVocab:
    """測試 extract_disease_vocab 函數"""

    def test_extracts_disease_nodes_only(self):
        """確認只提取 disease 類型的節點"""
        mock_nodes = pd.DataFrame({
            "node_id": ["DB00001", "DOID:1", "DOID:2", "12345"],
            "node_name": ["Drug A", "Diabetes", "Cancer", "Gene Y"],
            "node_type": ["drug", "disease", "disease", "gene/protein"],
            "node_index": [0, 100, 101, 200],
        })

        result = extract_disease_vocab(mock_nodes)

        assert len(result) == 2
        assert set(result["disease_id"]) == {"DOID:1", "DOID:2"}

    def test_has_required_columns(self):
        """確認輸出包含必要欄位"""
        mock_nodes = pd.DataFrame({
            "node_id": ["DOID:1"],
            "node_name": ["diabetes mellitus"],
            "node_type": ["disease"],
            "node_index": [100],
        })

        result = extract_disease_vocab(mock_nodes)

        assert "disease_id" in result.columns
        assert "disease_name" in result.columns
        assert "disease_name_upper" in result.columns

    def test_uppercase_conversion(self):
        """確認大寫轉換正確"""
        mock_nodes = pd.DataFrame({
            "node_id": ["DOID:1"],
            "node_name": ["diabetes mellitus"],
            "node_type": ["disease"],
            "node_index": [100],
        })

        result = extract_disease_vocab(mock_nodes)

        assert result.iloc[0]["disease_name"] == "diabetes mellitus"
        assert result.iloc[0]["disease_name_upper"] == "DIABETES MELLITUS"


class TestExtractDrugDiseaseRelations:
    """測試 extract_drug_disease_relations 函數"""

    def test_extracts_indication_and_contraindication(self):
        """確認只提取 indication 和 contraindication 關係"""
        mock_kg = pd.DataFrame({
            "relation": ["indication", "contraindication", "protein_protein", "drug_drug"],
            "x_id": ["DB00001", "DB00002", "12345", "DB00003"],
            "x_name": ["Drug A", "Drug B", "Gene X", "Drug C"],
            "y_id": ["DOID:1", "DOID:2", "67890", "DB00004"],
            "y_name": ["Diabetes", "Hypertension", "Gene Y", "Drug D"],
        })

        result = extract_drug_disease_relations(mock_kg)

        assert len(result) == 2
        assert set(result["relation"]) == {"indication", "contraindication"}

    def test_has_required_columns(self):
        """確認輸出包含必要欄位"""
        mock_kg = pd.DataFrame({
            "relation": ["indication"],
            "x_id": ["DB00001"],
            "x_name": ["Aspirin"],
            "y_id": ["DOID:1"],
            "y_name": ["pain"],
        })

        result = extract_drug_disease_relations(mock_kg)

        assert "relation" in result.columns
        assert "x_id" in result.columns
        assert "x_name" in result.columns
        assert "y_id" in result.columns
        assert "y_name" in result.columns

    def test_removes_duplicates(self):
        """確認移除重複項"""
        mock_kg = pd.DataFrame({
            "relation": ["indication", "indication"],
            "x_id": ["DB00001", "DB00001"],
            "x_name": ["Drug A", "Drug A"],
            "y_id": ["DOID:1", "DOID:1"],
            "y_name": ["Diabetes", "Diabetes"],
        })

        result = extract_drug_disease_relations(mock_kg)

        assert len(result) == 1

    def test_empty_when_no_matching_relations(self):
        """測試沒有符合的關係時回傳空 DataFrame"""
        mock_kg = pd.DataFrame({
            "relation": ["protein_protein", "drug_drug"],
            "x_id": ["12345", "DB00001"],
            "x_name": ["Gene X", "Drug A"],
            "y_id": ["67890", "DB00002"],
            "y_name": ["Gene Y", "Drug B"],
        })

        result = extract_drug_disease_relations(mock_kg)

        assert len(result) == 0


# 以下測試需要實際的 TxGNN 資料
DATA_DIR = Path(__file__).parent.parent / "data"
NODE_CSV_EXISTS = (DATA_DIR / "node.csv").exists()
KG_CSV_EXISTS = (DATA_DIR / "kg.csv").exists()

SKIP_REASON = (
    "需要 TxGNN 資料檔案。\n"
    "請先下載 node.csv 和 kg.csv 到 data/ 目錄。"
)


@pytest.mark.skipif(not NODE_CSV_EXISTS, reason=SKIP_REASON)
class TestExtractDrugbankVocabWithRealData:
    """使用真實資料測試 extract_drugbank_vocab"""

    def test_extracts_thousands_of_drugs(self):
        """確認能提取數千個藥品"""
        from prepare_external_data import load_node_csv

        nodes_df = load_node_csv(DATA_DIR / "node.csv")
        result = extract_drugbank_vocab(nodes_df)

        # TxGNN 應該有 7000+ 藥品
        assert len(result) > 7000

    def test_all_drugbank_ids_start_with_db(self):
        """確認所有 DrugBank ID 都以 DB 開頭"""
        from prepare_external_data import load_node_csv

        nodes_df = load_node_csv(DATA_DIR / "node.csv")
        result = extract_drugbank_vocab(nodes_df)

        for db_id in result["drugbank_id"]:
            assert db_id.startswith("DB"), f"Invalid DrugBank ID: {db_id}"


@pytest.mark.skipif(not NODE_CSV_EXISTS, reason=SKIP_REASON)
class TestExtractDiseaseVocabWithRealData:
    """使用真實資料測試 extract_disease_vocab"""

    def test_extracts_thousands_of_diseases(self):
        """確認能提取數千個疾病"""
        from prepare_external_data import load_node_csv

        nodes_df = load_node_csv(DATA_DIR / "node.csv")
        result = extract_disease_vocab(nodes_df)

        # TxGNN 應該有 17000+ 疾病
        assert len(result) > 17000


@pytest.mark.skipif(not KG_CSV_EXISTS, reason=SKIP_REASON)
class TestExtractDrugDiseaseRelationsWithRealData:
    """使用真實資料測試 extract_drug_disease_relations"""

    def test_extracts_thousands_of_relations(self):
        """確認能提取數萬個關係"""
        from prepare_external_data import load_kg_csv

        kg_df = load_kg_csv(DATA_DIR / "kg.csv")
        result = extract_drug_disease_relations(kg_df)

        # TxGNN 應該有 40000+ 藥物-疾病關係
        assert len(result) > 40000

    def test_only_indication_and_contraindication(self):
        """確認只有 indication 和 contraindication"""
        from prepare_external_data import load_kg_csv

        kg_df = load_kg_csv(DATA_DIR / "kg.csv")
        result = extract_drug_disease_relations(kg_df)

        unique_relations = set(result["relation"].unique())
        assert unique_relations == {"indication", "contraindication"}
