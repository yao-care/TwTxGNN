"""測試 TxGNN 深度學習模型模組

這些測試主要測試不需要 TxGNN 套件的功能。
需要 TxGNN 套件的測試會自動跳過。
"""

import pytest
import pandas as pd
from pathlib import Path
import tempfile
import os

from twtxgnn.predict.txgnn_model import (
    detect_device,
    check_dependencies,
    CheckpointManager,
)


class TestDetectDevice:
    """測試 detect_device 函數"""

    def test_returns_string(self):
        """確認回傳字串"""
        device = detect_device()
        assert isinstance(device, str)

    def test_returns_valid_device(self):
        """確認回傳有效的裝置名稱"""
        device = detect_device()
        # 應該是 cuda:0 或 cpu
        assert device in ["cuda:0", "cpu"]


class TestCheckDependencies:
    """測試 check_dependencies 函數"""

    def test_returns_tuple(self):
        """確認回傳元組"""
        result = check_dependencies()
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_first_element_is_bool(self):
        """確認第一個元素是布林值"""
        deps_ok, missing = check_dependencies()
        assert isinstance(deps_ok, bool)

    def test_second_element_is_list(self):
        """確認第二個元素是列表"""
        deps_ok, missing = check_dependencies()
        assert isinstance(missing, list)

    def test_consistent_result(self):
        """確認結果一致性"""
        deps_ok, missing = check_dependencies()
        # 如果全部安裝，missing 應該為空
        if deps_ok:
            assert len(missing) == 0
        # 如果有缺少，missing 應該非空
        else:
            assert len(missing) > 0


class TestCheckpointManager:
    """測試 CheckpointManager 類別"""

    def test_init_with_nonexistent_file(self, tmp_path):
        """確認初始化時處理不存在的檔案"""
        checkpoint_path = tmp_path / "checkpoint.csv"
        manager = CheckpointManager(checkpoint_path)
        assert manager.checkpoint_path == checkpoint_path
        assert len(manager.processed_drugs) == 0

    def test_load_empty(self, tmp_path):
        """確認載入空 checkpoint"""
        checkpoint_path = tmp_path / "checkpoint.csv"
        manager = CheckpointManager(checkpoint_path)
        processed = manager.load()
        assert len(processed) == 0

    def test_append_and_load(self, tmp_path):
        """測試寫入和讀取 checkpoint"""
        checkpoint_path = tmp_path / "checkpoint.csv"
        manager = CheckpointManager(checkpoint_path)

        # 寫入資料
        predictions = [
            {
                "drugbank_id": "DB00001",
                "drug_name": "Drug A",
                "disease_name": "Disease 1",
                "txgnn_score": 0.8,
            },
            {
                "drugbank_id": "DB00001",
                "drug_name": "Drug A",
                "disease_name": "Disease 2",
                "txgnn_score": 0.6,
            },
        ]
        manager.append(predictions)

        # 確認檔案已建立
        assert checkpoint_path.exists()

        # 確認已處理清單已更新
        assert "DB00001" in manager.processed_drugs

        # 確認可以讀取結果
        results = manager.get_results()
        assert len(results) == 2
        assert "drugbank_id" in results.columns
        assert "txgnn_score" in results.columns

    def test_is_processed(self, tmp_path):
        """測試 is_processed 方法"""
        checkpoint_path = tmp_path / "checkpoint.csv"
        manager = CheckpointManager(checkpoint_path)

        # 初始應該都沒處理過
        assert not manager.is_processed("DB00001")
        assert not manager.is_processed("DB00002")

        # 寫入資料
        predictions = [
            {
                "drugbank_id": "DB00001",
                "drug_name": "Drug A",
                "disease_name": "Disease 1",
                "txgnn_score": 0.8,
            },
        ]
        manager.append(predictions)

        # 確認狀態
        assert manager.is_processed("DB00001")
        assert not manager.is_processed("DB00002")

    def test_clear(self, tmp_path):
        """測試清除 checkpoint"""
        checkpoint_path = tmp_path / "checkpoint.csv"
        manager = CheckpointManager(checkpoint_path)

        # 寫入資料
        predictions = [
            {
                "drugbank_id": "DB00001",
                "drug_name": "Drug A",
                "disease_name": "Disease 1",
                "txgnn_score": 0.8,
            },
        ]
        manager.append(predictions)
        assert checkpoint_path.exists()
        assert manager.is_processed("DB00001")

        # 清除
        manager.clear()
        assert not checkpoint_path.exists()
        assert not manager.is_processed("DB00001")

    def test_append_empty_list(self, tmp_path):
        """測試寫入空列表"""
        checkpoint_path = tmp_path / "checkpoint.csv"
        manager = CheckpointManager(checkpoint_path)

        # 寫入空列表不應該創建檔案
        manager.append([])
        assert not checkpoint_path.exists()

    def test_multiple_appends(self, tmp_path):
        """測試多次寫入"""
        checkpoint_path = tmp_path / "checkpoint.csv"
        manager = CheckpointManager(checkpoint_path)

        # 第一次寫入
        manager.append([
            {"drugbank_id": "DB00001", "drug_name": "Drug A",
             "disease_name": "Disease 1", "txgnn_score": 0.8},
        ])

        # 第二次寫入
        manager.append([
            {"drugbank_id": "DB00002", "drug_name": "Drug B",
             "disease_name": "Disease 2", "txgnn_score": 0.7},
        ])

        # 確認結果
        results = manager.get_results()
        assert len(results) == 2
        assert manager.is_processed("DB00001")
        assert manager.is_processed("DB00002")

    def test_load_existing_checkpoint(self, tmp_path):
        """測試載入現有 checkpoint"""
        checkpoint_path = tmp_path / "checkpoint.csv"

        # 先建立 checkpoint
        manager1 = CheckpointManager(checkpoint_path)
        manager1.append([
            {"drugbank_id": "DB00001", "drug_name": "Drug A",
             "disease_name": "Disease 1", "txgnn_score": 0.8},
            {"drugbank_id": "DB00002", "drug_name": "Drug B",
             "disease_name": "Disease 2", "txgnn_score": 0.7},
        ])

        # 新建 manager 並載入
        manager2 = CheckpointManager(checkpoint_path)
        processed = manager2.load()

        assert len(processed) == 2
        assert "DB00001" in processed
        assert "DB00002" in processed


class TestCheckpointManagerEdgeCases:
    """測試 CheckpointManager 邊界情況"""

    def test_special_characters_in_path(self, tmp_path):
        """測試路徑包含特殊字元"""
        special_dir = tmp_path / "dir with spaces"
        special_dir.mkdir()
        checkpoint_path = special_dir / "checkpoint.csv"

        manager = CheckpointManager(checkpoint_path)
        manager.append([
            {"drugbank_id": "DB00001", "drug_name": "Drug A",
             "disease_name": "Disease 1", "txgnn_score": 0.8},
        ])

        assert checkpoint_path.exists()
        results = manager.get_results()
        assert len(results) == 1

    def test_unicode_in_data(self, tmp_path):
        """測試資料包含中文字元"""
        checkpoint_path = tmp_path / "checkpoint.csv"
        manager = CheckpointManager(checkpoint_path)

        manager.append([
            {"drugbank_id": "DB00001", "drug_name": "藥物A",
             "disease_name": "糖尿病", "txgnn_score": 0.8},
        ])

        results = manager.get_results()
        assert len(results) == 1
        assert results.iloc[0]["drug_name"] == "藥物A"
        assert results.iloc[0]["disease_name"] == "糖尿病"


class TestCheckpointManagerColumns:
    """測試 CheckpointManager 欄位處理"""

    def test_columns_constant(self):
        """確認 COLUMNS 常數正確"""
        assert CheckpointManager.COLUMNS == [
            "drugbank_id", "drug_name", "disease_name", "txgnn_score"
        ]

    def test_get_results_empty_file(self, tmp_path):
        """測試空檔案回傳正確欄位"""
        checkpoint_path = tmp_path / "checkpoint.csv"
        manager = CheckpointManager(checkpoint_path)

        results = manager.get_results()
        assert len(results) == 0
        assert list(results.columns) == CheckpointManager.COLUMNS


# 以下測試需要 TxGNN 套件
try:
    import torch
    import dgl
    import txgnn
    TXGNN_AVAILABLE = True
except ImportError:
    TXGNN_AVAILABLE = False

SKIP_TXGNN_REASON = (
    "需要 TxGNN 相關套件 (torch, dgl, txgnn)。\n"
    "請參考 README.md 安裝深度學習環境。"
)


@pytest.mark.skipif(not TXGNN_AVAILABLE, reason=SKIP_TXGNN_REASON)
class TestTxGNNPredictorSetup:
    """測試 TxGNNPredictor 設定（需要 TxGNN 套件）"""

    # 這些測試在沒有 TxGNN 時會被跳過
    pass
