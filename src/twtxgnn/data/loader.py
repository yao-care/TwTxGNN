"""FDA 藥品資料載入與過濾"""

import json
from pathlib import Path
from typing import Optional

import pandas as pd


def load_fda_drugs(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入台灣 FDA 藥品資料

    Args:
        filepath: JSON 檔案路徑，預設為 data/raw/tw_fda_drugs.json

    Returns:
        包含所有藥品的 DataFrame

    Raises:
        FileNotFoundError: 找不到 FDA 資料檔案時，提供下載指引
    """
    if filepath is None:
        # loader.py -> data -> twtxgnn -> src -> TwTxGNN
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "raw" / "tw_fda_drugs.json"

    if not filepath.exists():
        raise FileNotFoundError(
            f"找不到 FDA 藥品資料: {filepath}\n"
            f"請先執行以下步驟：\n"
            f"1. 下載 ZIP 檔案: https://data.fda.gov.tw/data/opendata/export/36/json\n"
            f"2. 放到 data/raw/ 目錄\n"
            f"3. 執行: uv run python scripts/process_fda_data.py"
        )

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    return df


def filter_active_drugs(df: pd.DataFrame) -> pd.DataFrame:
    """過濾有效藥品（排除已註銷）

    Args:
        df: 原始藥品 DataFrame

    Returns:
        僅包含有效藥品的 DataFrame
    """
    # 過濾未註銷的藥品
    active = df[df["註銷狀態"] != "已註銷"].copy()

    # 過濾有主成分的藥品（TxGNN 需要）
    active = active[active["主成分略述"].notna() & (active["主成分略述"] != "")]

    # 重設索引
    active = active.reset_index(drop=True)

    return active


def get_drug_summary(df: pd.DataFrame) -> dict:
    """取得藥品資料摘要統計

    Args:
        df: 藥品 DataFrame

    Returns:
        摘要統計字典
    """
    return {
        "total_count": len(df),
        "with_ingredient": df["主成分略述"].notna().sum(),
        "with_indication": df["適應症"].notna().sum(),
        "unique_ingredients": df["主成分略述"].nunique(),
        "dosage_forms": df["劑型"].value_counts().to_dict(),
    }
