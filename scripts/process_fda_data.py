#!/usr/bin/env python3
"""處理台灣 FDA 藥品資料

將手動下載的 FDA 藥品 ZIP 檔案解壓縮並轉換為 JSON 格式。

使用方法:
    uv run python scripts/process_fda_data.py

前置條件:
    需要先手動下載 FDA 資料 ZIP 檔案到 data/raw/ 目錄：
    https://data.fda.gov.tw/data/opendata/export/36/json

產生檔案:
    data/raw/tw_fda_drugs.json
"""

import json
import zipfile
from pathlib import Path


def find_fda_zip(raw_dir: Path) -> Path:
    """在 raw 目錄中尋找 FDA ZIP 檔案

    Args:
        raw_dir: data/raw/ 目錄路徑

    Returns:
        找到的 ZIP 檔案路徑

    Raises:
        FileNotFoundError: 找不到 ZIP 檔案
    """
    # 尋找所有 ZIP 檔案
    zip_files = list(raw_dir.glob("*.zip"))

    if not zip_files:
        raise FileNotFoundError(
            f"在 {raw_dir} 找不到 ZIP 檔案\n"
            f"請先從以下網址下載 FDA 資料並放到 data/raw/ 目錄：\n"
            f"https://data.fda.gov.tw/data/opendata/export/36/json"
        )

    # 如果有多個 ZIP，優先選擇名稱包含 '36' 的（FDA 藥品資料編號）
    for zf in zip_files:
        if "36" in zf.name:
            return zf

    # 否則回傳第一個
    return zip_files[0]


def process_fda_zip(zip_path: Path, output_path: Path) -> Path:
    """解壓縮並轉換 FDA ZIP 檔案為 JSON

    Args:
        zip_path: ZIP 檔案路徑
        output_path: 輸出 JSON 檔案路徑

    Returns:
        輸出檔案路徑
    """
    print(f"讀取 ZIP 檔案: {zip_path}")
    print(f"檔案大小: {zip_path.stat().st_size / 1024 / 1024:.1f} MB")

    # 解壓縮
    print("解壓縮中...")
    with zipfile.ZipFile(zip_path, 'r') as zf:
        # 找到 JSON 檔案
        json_files = [f for f in zf.namelist() if f.endswith('.json')]
        if not json_files:
            raise ValueError("ZIP 檔案中找不到 JSON 檔案")

        json_filename = json_files[0]
        print(f"找到資料檔案: {json_filename}")

        # 讀取 JSON 內容
        with zf.open(json_filename) as f:
            file_content = f.read().decode('utf-8')
            data = json.loads(file_content)

    # 確保輸出目錄存在
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 儲存 JSON
    print(f"儲存至: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"完成！共 {len(data)} 筆藥品資料")
    return output_path


def main():
    print("=" * 60)
    print("處理台灣 FDA 藥品資料")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    raw_dir = base_dir / "data" / "raw"
    output_path = raw_dir / "tw_fda_drugs.json"

    # 確保 raw 目錄存在
    raw_dir.mkdir(parents=True, exist_ok=True)

    # 尋找並處理 ZIP 檔案
    zip_path = find_fda_zip(raw_dir)
    process_fda_zip(zip_path, output_path)

    print()
    print("下一步: 準備詞彙表資料")
    print("  uv run python scripts/prepare_external_data.py")


if __name__ == "__main__":
    main()
