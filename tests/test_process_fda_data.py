"""測試 process_fda_data.py 腳本"""

import json
import tempfile
import zipfile
from pathlib import Path

import pytest

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from process_fda_data import find_fda_zip, process_fda_zip


class TestFindFdaZip:
    """測試 find_fda_zip 函數"""

    def test_finds_zip_file(self, tmp_path):
        """測試能找到 ZIP 檔案"""
        # 建立測試 ZIP 檔案
        zip_path = tmp_path / "test.zip"
        zip_path.touch()

        result = find_fda_zip(tmp_path)
        assert result == zip_path

    def test_prefers_36_in_filename(self, tmp_path):
        """測試優先選擇包含 36 的檔案名"""
        # 建立多個 ZIP 檔案
        (tmp_path / "other.zip").touch()
        (tmp_path / "36.zip").touch()

        result = find_fda_zip(tmp_path)
        assert "36" in result.name

    def test_raises_error_when_no_zip(self, tmp_path):
        """測試找不到 ZIP 時拋出錯誤並顯示下載連結"""
        with pytest.raises(FileNotFoundError) as exc_info:
            find_fda_zip(tmp_path)

        error_message = str(exc_info.value)
        assert "找不到 ZIP 檔案" in error_message
        assert "https://data.fda.gov.tw/data/opendata/export/36/json" in error_message


class TestProcessFdaZip:
    """測試 process_fda_zip 函數"""

    def test_extracts_json_from_zip(self, tmp_path):
        """測試從 ZIP 解壓縮 JSON"""
        # 建立測試 ZIP 檔案
        test_data = [{"id": 1, "name": "Test Drug"}]
        zip_path = tmp_path / "test.zip"
        output_path = tmp_path / "output.json"

        with zipfile.ZipFile(zip_path, 'w') as zf:
            zf.writestr("data.json", json.dumps(test_data))

        result = process_fda_zip(zip_path, output_path)

        assert result == output_path
        assert output_path.exists()

        with open(output_path, encoding='utf-8') as f:
            loaded_data = json.load(f)

        assert loaded_data == test_data

    def test_raises_error_when_no_json_in_zip(self, tmp_path):
        """測試 ZIP 中沒有 JSON 時拋出錯誤"""
        zip_path = tmp_path / "test.zip"
        output_path = tmp_path / "output.json"

        with zipfile.ZipFile(zip_path, 'w') as zf:
            zf.writestr("data.txt", "not json")

        with pytest.raises(ValueError) as exc_info:
            process_fda_zip(zip_path, output_path)

        assert "找不到 JSON 檔案" in str(exc_info.value)

    def test_creates_output_directory(self, tmp_path):
        """測試自動建立輸出目錄"""
        test_data = [{"id": 1}]
        zip_path = tmp_path / "test.zip"
        output_path = tmp_path / "subdir" / "output.json"

        with zipfile.ZipFile(zip_path, 'w') as zf:
            zf.writestr("data.json", json.dumps(test_data))

        process_fda_zip(zip_path, output_path)

        assert output_path.exists()
        assert output_path.parent.exists()


class TestFdaZipExistence:
    """測試 FDA ZIP 檔案是否存在"""

    @pytest.fixture
    def raw_dir(self):
        """取得 data/raw 目錄路徑"""
        return Path(__file__).parent.parent / "data" / "raw"

    def test_fda_zip_or_json_exists(self, raw_dir):
        """測試 FDA 資料是否已存在（ZIP 或 JSON）

        如果這個測試失敗，請先下載 FDA 資料：
        1. 下載 ZIP 檔案：https://data.fda.gov.tw/data/opendata/export/36/json
        2. 將檔案放到 data/raw/ 目錄
        3. 執行 uv run python scripts/process_fda_data.py
        """
        json_exists = (raw_dir / "tw_fda_drugs.json").exists()
        zip_exists = len(list(raw_dir.glob("*.zip"))) > 0

        if not json_exists and not zip_exists:
            pytest.skip(
                "FDA 資料尚未下載。請先從以下網址下載 ZIP 檔案到 data/raw/ 目錄：\n"
                "https://data.fda.gov.tw/data/opendata/export/36/json"
            )

        assert json_exists or zip_exists
