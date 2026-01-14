"""測試 TxGNN 整合模組

這些測試需要 TxGNN 資料檔案（node.csv）才能執行。
如果資料檔案不存在，相關測試會被跳過。
"""

import pytest
import pandas as pd
from pathlib import Path

from twtxgnn.predict.prepare_for_txgnn import (
    load_txgnn_nodes,
    build_drugbank_to_node_index,
    build_disease_node_mappings,
    prepare_drug_list_for_txgnn,
    get_drug_node_mapping_stats,
)

from twtxgnn.predict.process_txgnn_results import (
    filter_by_score_threshold,
    merge_with_kg_candidates,
    generate_txgnn_report,
    compare_with_existing_indications,
)


# 檢查 node.csv 是否存在
DATA_DIR = Path(__file__).parent.parent / "data"
NODE_CSV_EXISTS = (DATA_DIR / "node.csv").exists()

# 如果資料不存在，跳過相關測試的原因說明
SKIP_REASON = (
    "需要 TxGNN 資料檔案 (data/node.csv)。\n"
    "請先下載資料: https://dataverse.harvard.edu/api/access/datafile/7144482"
)


@pytest.mark.skipif(not NODE_CSV_EXISTS, reason=SKIP_REASON)
class TestLoadTxGNNNodes:
    """測試 load_txgnn_nodes 函數"""

    def test_returns_dataframe(self):
        """確認回傳 DataFrame"""
        df = load_txgnn_nodes()
        assert isinstance(df, pd.DataFrame)

    def test_has_required_columns(self):
        """確認包含必要欄位"""
        df = load_txgnn_nodes()
        assert "node_id" in df.columns
        assert "node_name" in df.columns
        assert "node_type" in df.columns
        assert "node_index" in df.columns

    def test_has_drug_nodes(self):
        """確認有藥物節點"""
        df = load_txgnn_nodes()
        drug_nodes = df[df["node_type"] == "drug"]
        assert len(drug_nodes) > 1000, f"藥物節點數量不足: {len(drug_nodes)}"

    def test_has_disease_nodes(self):
        """確認有疾病節點"""
        df = load_txgnn_nodes()
        disease_nodes = df[df["node_type"] == "disease"]
        assert len(disease_nodes) > 1000, f"疾病節點數量不足: {len(disease_nodes)}"


class TestLoadTxGNNNodesErrorHandling:
    """測試 load_txgnn_nodes 錯誤處理"""

    def test_missing_file_raises_error(self, tmp_path):
        """確認找不到檔案時會拋出錯誤並提供指引"""
        fake_path = tmp_path / "nonexistent.csv"
        with pytest.raises(FileNotFoundError) as exc_info:
            load_txgnn_nodes(fake_path)

        error_msg = str(exc_info.value)
        assert "找不到" in error_msg
        assert "下載連結" in error_msg


@pytest.mark.skipif(not NODE_CSV_EXISTS, reason=SKIP_REASON)
class TestBuildDrugbankToNodeIndex:
    """測試 build_drugbank_to_node_index 函數"""

    def test_returns_dict(self):
        """確認回傳字典"""
        nodes_df = load_txgnn_nodes()
        mapping = build_drugbank_to_node_index(nodes_df)
        assert isinstance(mapping, dict)

    def test_contains_drugbank_ids(self):
        """確認包含 DrugBank ID"""
        nodes_df = load_txgnn_nodes()
        mapping = build_drugbank_to_node_index(nodes_df)
        # DrugBank IDs start with DB
        sample_key = list(mapping.keys())[0]
        assert sample_key.startswith("DB"), f"DrugBank ID 格式錯誤: {sample_key}"

    def test_values_are_integers(self):
        """確認值為整數"""
        nodes_df = load_txgnn_nodes()
        mapping = build_drugbank_to_node_index(nodes_df)
        sample_value = list(mapping.values())[0]
        assert isinstance(sample_value, (int, float))


class TestBuildDrugbankToNodeIndexWithMockData:
    """使用模擬資料測試 build_drugbank_to_node_index"""

    def test_with_mock_data(self):
        """使用模擬資料測試"""
        mock_df = pd.DataFrame({
            "node_id": ["DB00001", "DB00002", "12345"],
            "node_name": ["Drug A", "Drug B", "Gene X"],
            "node_type": ["drug", "drug", "gene/protein"],
            "node_index": [0, 1, 2],
        })
        mapping = build_drugbank_to_node_index(mock_df)
        assert len(mapping) == 2
        assert mapping["DB00001"] == 0
        assert mapping["DB00002"] == 1


@pytest.mark.skipif(not NODE_CSV_EXISTS, reason=SKIP_REASON)
class TestBuildDiseaseNodeMappings:
    """測試 build_disease_node_mappings 函數"""

    def test_returns_two_dicts(self):
        """確認回傳兩個字典"""
        nodes_df = load_txgnn_nodes()
        idx_to_name, idx_to_id = build_disease_node_mappings(nodes_df)
        assert isinstance(idx_to_name, dict)
        assert isinstance(idx_to_id, dict)

    def test_same_length(self):
        """確認兩個字典長度相同"""
        nodes_df = load_txgnn_nodes()
        idx_to_name, idx_to_id = build_disease_node_mappings(nodes_df)
        assert len(idx_to_name) == len(idx_to_id)


class TestBuildDiseaseNodeMappingsWithMockData:
    """使用模擬資料測試 build_disease_node_mappings"""

    def test_with_mock_data(self):
        """使用模擬資料測試"""
        mock_df = pd.DataFrame({
            "node_id": ["DOID:1", "DOID:2", "DB00001"],
            "node_name": ["Disease A", "Disease B", "Drug X"],
            "node_type": ["disease", "disease", "drug"],
            "node_index": [100, 101, 0],
        })
        idx_to_name, idx_to_id = build_disease_node_mappings(mock_df)
        assert len(idx_to_name) == 2
        assert idx_to_name[100] == "Disease A"
        assert idx_to_id[101] == "DOID:2"


@pytest.mark.skipif(not NODE_CSV_EXISTS, reason=SKIP_REASON)
class TestPrepareDrugListForTxGNN:
    """測試 prepare_drug_list_for_txgnn 函數"""

    def test_with_valid_input(self):
        """測試有效輸入"""
        # 建立測試資料
        drug_mapping = pd.DataFrame({
            "許可證字號": ["A001", "A002"],
            "中文品名": ["藥物A", "藥物B"],
            "標準化成分": ["ASPIRIN", "IBUPROFEN"],
            "drugbank_id": ["DB00945", "DB01050"],
        })

        result = prepare_drug_list_for_txgnn(drug_mapping)
        assert isinstance(result, pd.DataFrame)
        assert "drugbank_id" in result.columns
        assert "node_index" in result.columns

    def test_filters_invalid_drugbank_ids(self):
        """確認過濾無效的 DrugBank ID"""
        drug_mapping = pd.DataFrame({
            "許可證字號": ["A001", "A002"],
            "中文品名": ["藥物A", "藥物B"],
            "標準化成分": ["ASPIRIN", "UNKNOWN"],
            "drugbank_id": ["DB00945", None],
        })

        result = prepare_drug_list_for_txgnn(drug_mapping)
        # 只有 ASPIRIN 應該被映射
        assert len(result) <= 1


class TestPrepareDrugListWithMockNodes:
    """使用模擬節點資料測試 prepare_drug_list_for_txgnn"""

    def test_with_mock_nodes(self):
        """使用模擬節點資料測試"""
        mock_nodes = pd.DataFrame({
            "node_id": ["DB00001", "DB00002"],
            "node_name": ["Drug A", "Drug B"],
            "node_type": ["drug", "drug"],
            "node_index": [0, 1],
        })
        drug_mapping = pd.DataFrame({
            "許可證字號": ["A001", "A002", "A003"],
            "中文品名": ["藥物A", "藥物B", "藥物C"],
            "標準化成分": ["DRUG_A", "DRUG_B", "DRUG_C"],
            "drugbank_id": ["DB00001", "DB00002", "DB99999"],
        })

        result = prepare_drug_list_for_txgnn(drug_mapping, mock_nodes)
        assert len(result) == 2  # DB99999 不存在於 mock_nodes
        assert set(result["drugbank_id"]) == {"DB00001", "DB00002"}


@pytest.mark.skipif(not NODE_CSV_EXISTS, reason=SKIP_REASON)
class TestGetDrugNodeMappingStats:
    """測試 get_drug_node_mapping_stats 函數"""

    def test_returns_dict(self):
        """確認回傳字典"""
        drug_mapping = pd.DataFrame({
            "drugbank_id": ["DB00945", "DB01050", None],
        })
        stats = get_drug_node_mapping_stats(drug_mapping)
        assert isinstance(stats, dict)

    def test_has_required_keys(self):
        """確認包含必要欄位"""
        drug_mapping = pd.DataFrame({
            "drugbank_id": ["DB00945", "DB01050"],
        })
        stats = get_drug_node_mapping_stats(drug_mapping)
        assert "total_unique_drugbank_ids" in stats
        assert "found_in_txgnn" in stats
        assert "mapping_rate" in stats


class TestGetDrugNodeMappingStatsWithMockData:
    """使用模擬資料測試 get_drug_node_mapping_stats"""

    def test_with_mock_data(self):
        """使用模擬資料測試"""
        mock_nodes = pd.DataFrame({
            "node_id": ["DB00001", "DB00002"],
            "node_name": ["Drug A", "Drug B"],
            "node_type": ["drug", "drug"],
            "node_index": [0, 1],
        })
        drug_mapping = pd.DataFrame({
            "drugbank_id": ["DB00001", "DB00002", "DB99999"],
        })

        stats = get_drug_node_mapping_stats(drug_mapping, mock_nodes)
        assert stats["total_unique_drugbank_ids"] == 3
        assert stats["found_in_txgnn"] == 2
        assert stats["not_found_in_txgnn"] == 1
        assert stats["mapping_rate"] == pytest.approx(2/3)


class TestFilterByScoreThreshold:
    """測試 filter_by_score_threshold 函數"""

    def test_filters_correctly(self):
        """確認正確過濾"""
        df = pd.DataFrame({
            "drug": ["A", "B", "C"],
            "disease": ["D1", "D2", "D3"],
            "txgnn_score": [0.8, 0.3, 0.6],
        })

        filtered = filter_by_score_threshold(df, threshold=0.5)
        assert len(filtered) == 2
        assert filtered["txgnn_score"].min() >= 0.5

    def test_adds_rank_column(self):
        """確認加入排名欄位"""
        df = pd.DataFrame({
            "drug": ["A", "B", "C"],
            "disease": ["D1", "D2", "D3"],
            "txgnn_score": [0.8, 0.3, 0.6],
        })

        filtered = filter_by_score_threshold(df, threshold=0.5)
        assert "rank" in filtered.columns
        assert filtered["rank"].tolist() == [1, 2]

    def test_empty_dataframe(self):
        """測試空 DataFrame"""
        df = pd.DataFrame({
            "drug": [],
            "disease": [],
            "txgnn_score": [],
        })
        filtered = filter_by_score_threshold(df, threshold=0.5)
        assert len(filtered) == 0

    def test_all_filtered_out(self):
        """測試所有資料都被過濾"""
        df = pd.DataFrame({
            "drug": ["A", "B"],
            "disease": ["D1", "D2"],
            "txgnn_score": [0.1, 0.2],
        })
        filtered = filter_by_score_threshold(df, threshold=0.5)
        assert len(filtered) == 0


class TestGenerateTxGNNReport:
    """測試 generate_txgnn_report 函數"""

    def test_empty_dataframe(self):
        """測試空 DataFrame"""
        empty_df = pd.DataFrame()
        report = generate_txgnn_report(empty_df)
        assert report["total_predictions"] == 0

    def test_with_data(self):
        """測試有資料的情況"""
        df = pd.DataFrame({
            "drugbank_id": ["DB001", "DB001", "DB002"],
            "藥物成分": ["DRUG_A", "DRUG_A", "DRUG_B"],
            "潛在新適應症": ["disease1", "disease2", "disease1"],
            "txgnn_score": [0.8, 0.6, 0.7],
        })

        report = generate_txgnn_report(df)
        assert report["total_predictions"] == 3
        assert report["unique_drugs"] == 2
        assert report["unique_diseases"] == 2
        assert report["max_score"] == 0.8
        assert len(report["top_predictions"]) <= 10

    def test_report_top_predictions_limit(self):
        """確認 top_predictions 最多 10 筆"""
        df = pd.DataFrame({
            "drugbank_id": [f"DB{i:05d}" for i in range(20)],
            "藥物成分": [f"DRUG_{i}" for i in range(20)],
            "潛在新適應症": [f"disease_{i}" for i in range(20)],
            "txgnn_score": [0.9 - i * 0.01 for i in range(20)],
        })
        report = generate_txgnn_report(df)
        assert len(report["top_predictions"]) == 10


class TestMergeWithKGCandidates:
    """測試 merge_with_kg_candidates 函數"""

    def test_merges_scores(self):
        """確認分數合併"""
        txgnn = pd.DataFrame({
            "drugbank_id": ["DB001", "DB001"],
            "disease_name": ["disease1", "disease2"],
            "txgnn_score": [0.8, 0.6],
        })

        kg = pd.DataFrame({
            "許可證字號": ["A001", "A001", "A001"],
            "drugbank_id": ["DB001", "DB001", "DB001"],
            "藥物成分": ["DRUG_A", "DRUG_A", "DRUG_A"],
            "潛在新適應症": ["disease1", "disease2", "disease3"],
        })

        result = merge_with_kg_candidates(txgnn, kg)
        assert "txgnn_score" in result.columns

        # disease1 and disease2 should have scores
        has_score = result["txgnn_score"].notna().sum()
        assert has_score == 2

    def test_empty_txgnn_predictions(self):
        """測試空的 TxGNN 預測"""
        txgnn = pd.DataFrame({
            "drugbank_id": [],
            "disease_name": [],
            "txgnn_score": [],
        })
        kg = pd.DataFrame({
            "許可證字號": ["A001"],
            "drugbank_id": ["DB001"],
            "藥物成分": ["DRUG_A"],
            "潛在新適應症": ["disease1"],
        })
        result = merge_with_kg_candidates(txgnn, kg)
        assert len(result) == 1
        assert result["txgnn_score"].isna().all()


class TestCompareWithExistingIndications:
    """測試 compare_with_existing_indications 函數"""

    def test_marks_novel_correctly(self):
        """確認正確標記新穎性"""
        predictions = pd.DataFrame({
            "許可證字號": ["A001", "A001"],
            "潛在新適應症": ["diabetes", "cancer"],
            "txgnn_score": [0.8, 0.7],
        })

        indications = pd.DataFrame({
            "許可證字號": ["A001", "A001"],
            "disease_name": ["diabetes", "hypertension"],
        })

        result = compare_with_existing_indications(predictions, indications)
        assert "is_novel" in result.columns

        # diabetes exists -> not novel
        # cancer doesn't exist -> novel
        diabetes_row = result[result["潛在新適應症"] == "diabetes"].iloc[0]
        cancer_row = result[result["潛在新適應症"] == "cancer"].iloc[0]

        assert diabetes_row["is_novel"] == False
        assert cancer_row["is_novel"] == True

    def test_all_novel(self):
        """測試所有都是新穎的"""
        predictions = pd.DataFrame({
            "許可證字號": ["A001", "A001"],
            "潛在新適應症": ["cancer", "flu"],
            "txgnn_score": [0.8, 0.7],
        })
        indications = pd.DataFrame({
            "許可證字號": ["A001"],
            "disease_name": ["diabetes"],
        })
        result = compare_with_existing_indications(predictions, indications)
        assert result["is_novel"].all()

    def test_none_novel(self):
        """測試所有都不是新穎的"""
        predictions = pd.DataFrame({
            "許可證字號": ["A001", "A001"],
            "潛在新適應症": ["diabetes", "hypertension"],
            "txgnn_score": [0.8, 0.7],
        })
        indications = pd.DataFrame({
            "許可證字號": ["A001", "A001"],
            "disease_name": ["diabetes", "hypertension"],
        })
        result = compare_with_existing_indications(predictions, indications)
        assert not result["is_novel"].any()
