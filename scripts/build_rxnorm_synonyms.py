#!/usr/bin/env python3
"""使用 RxNorm API 為未映射成分建立同義詞對照表

此腳本會：
1. 載入目前未映射的成分清單
2. 使用 RxNorm API 查詢每個成分的同義詞
3. 找出與 DrugBank 匹配的同義詞
4. 輸出可加入 drugbank_mapper.py 的同義詞對照
"""

import json
import logging
import sys
from pathlib import Path

import pandas as pd

# 添加 src 到路徑
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from twtxgnn.mapping.rxnorm_bridge import RxNormBridge

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def load_unmapped_ingredients() -> list:
    """載入未映射成分清單"""
    unmapped_file = Path("data/processed/unmapped_ingredients.csv")
    if not unmapped_file.exists():
        logger.error("請先執行 analyze_unmapped_ingredients.py 產生未映射成分清單")
        sys.exit(1)

    df = pd.read_csv(unmapped_file)
    # 按使用藥品數排序，優先處理高影響力成分
    df = df.sort_values("使用藥品數", ascending=False)
    return df["成分"].tolist()


def load_drugbank_names() -> set:
    """載入 DrugBank 藥物名稱"""
    drugbank_file = Path("data/external/drugbank_vocab.csv")
    df = pd.read_csv(drugbank_file)
    return set(df["drug_name_upper"].str.upper())


def main():
    print("=" * 60)
    print("RxNorm 同義詞橋接")
    print("=" * 60)

    # 載入資料
    unmapped = load_unmapped_ingredients()
    drugbank_names = load_drugbank_names()

    print(f"未映射成分數: {len(unmapped)}")
    print(f"DrugBank 藥物數: {len(drugbank_names)}")

    # 過濾掉已知無法映射的類型
    skip_patterns = [
        "EXTRACT", "POWDER", "OIL", "TINCTURE", "DRIED",
        "TOXOID", "VACCINE", "ANTIGEN", "RADIX", "HERBA",
        "FLOS", "FRUCTUS", "SEMEN", "CORTEX", "RHIZOMA", "FOLIUM",
        "WATER", "SOLUTION", "EMULSION", "FLUID"
    ]

    candidates = []
    for ing in unmapped:
        ing_upper = ing.upper()
        if not any(pattern in ing_upper for pattern in skip_patterns):
            candidates.append(ing)

    print(f"可查詢候選數: {len(candidates)}")
    print()

    # 使用 RxNorm 查詢
    bridge = RxNormBridge()
    found_mappings = {}
    not_found = []

    # 限制查詢數量（可透過環境變數 RXNORM_MAX_QUERIES 調整）
    import os
    max_queries = int(os.environ.get("RXNORM_MAX_QUERIES", 200))
    max_queries = min(max_queries, len(candidates))
    print(f"將查詢前 {max_queries} 個候選成分...")
    print()

    for i, ingredient in enumerate(candidates[:max_queries]):
        if i % 10 == 0:
            print(f"進度: {i}/{max_queries}")

        ingredient_upper = ingredient.upper().strip()

        # 查詢 RxNorm
        rxnorm_candidates = bridge.find_drugbank_candidates(ingredient_upper)

        # 找出與 DrugBank 匹配的候選
        matched = None
        for candidate in rxnorm_candidates:
            if candidate in drugbank_names:
                matched = candidate
                break

        if matched:
            found_mappings[ingredient_upper] = matched
            logger.info(f"找到映射: {ingredient_upper} -> {matched}")
        else:
            not_found.append(ingredient_upper)

        # 定期儲存快取
        if (i + 1) % 50 == 0:
            bridge.save()

    # 最終儲存
    bridge.save()

    # 輸出結果
    print()
    print("=" * 60)
    print("查詢結果")
    print("=" * 60)
    print(f"成功映射: {len(found_mappings)}")
    print(f"未找到映射: {len(not_found)}")
    print()

    if found_mappings:
        print("【新發現的同義詞映射】")
        print("可加入 drugbank_mapper.py 的 synonym_map：")
        print("-" * 60)
        print()
        for orig, target in sorted(found_mappings.items()):
            print(f'        "{orig}": "{target}",')
        print()

        # 儲存到檔案
        output_file = Path("data/processed/rxnorm_mappings.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(found_mappings, f, ensure_ascii=False, indent=2)
        print(f"已儲存到: {output_file}")

    # 顯示部分未找到的成分
    if not_found:
        print()
        print("【部分未找到映射的成分】")
        for ing in not_found[:20]:
            print(f"  - {ing}")
        if len(not_found) > 20:
            print(f"  ... 共 {len(not_found)} 個")


if __name__ == "__main__":
    main()
