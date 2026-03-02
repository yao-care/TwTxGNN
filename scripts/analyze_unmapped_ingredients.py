#!/usr/bin/env python3
"""分析未映射成功的藥品成分，找出擴增潛力"""

import json
import pandas as pd
from collections import Counter
from pathlib import Path

# 添加 src 到路徑
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from twtxgnn.mapping.normalizer import extract_ingredients, normalize_ingredient, get_all_synonyms
from twtxgnn.mapping.drugbank_mapper import build_name_index, map_ingredient_to_drugbank


def load_data():
    """載入資料"""
    # FDA 藥品資料
    with open("data/raw/tw_fda_drugs.json", "r", encoding="utf-8") as f:
        fda_data = json.load(f)
    fda_df = pd.DataFrame(fda_data)

    # DrugBank 詞彙表
    drugbank_df = pd.read_csv("data/external/drugbank_vocab.csv")

    return fda_df, drugbank_df


def analyze_mapping():
    """分析成分映射情況"""
    print("=" * 60)
    print("台灣 FDA 藥品成分映射分析")
    print("=" * 60)

    fda_df, drugbank_df = load_data()

    # 過濾有效藥品
    active_df = fda_df[
        (fda_df["註銷狀態"].isna() | (fda_df["註銷狀態"] == "") | (fda_df["註銷狀態"] == "未註銷")) &
        (fda_df["主成分略述"].notna()) &
        (fda_df["主成分略述"] != "")
    ].copy()

    print(f"\n總藥品數: {len(fda_df):,}")
    print(f"有效藥品數（有主成分）: {len(active_df):,}")

    # 建立 DrugBank 名稱索引
    name_index = build_name_index(drugbank_df)
    print(f"DrugBank 詞彙表大小: {len(drugbank_df):,}")

    # 提取所有唯一成分
    all_ingredients = set()
    ingredient_to_drugs = {}  # 成分 -> 使用該成分的藥品數

    for _, row in active_df.iterrows():
        ingredient_str = row["主成分略述"]
        if pd.isna(ingredient_str):
            continue

        ingredients = extract_ingredients(ingredient_str)
        for ing in ingredients:
            normalized = normalize_ingredient(ing)
            if normalized:
                all_ingredients.add(normalized)
                if normalized not in ingredient_to_drugs:
                    ingredient_to_drugs[normalized] = 0
                ingredient_to_drugs[normalized] += 1

    print(f"\n唯一成分數: {len(all_ingredients):,}")

    # 映射每個成分
    mapped = {}
    unmapped = {}

    for ing in all_ingredients:
        drugbank_id = map_ingredient_to_drugbank(ing, name_index)
        drug_count = ingredient_to_drugs.get(ing, 0)

        if drugbank_id:
            mapped[ing] = (drugbank_id, drug_count)
        else:
            unmapped[ing] = drug_count

    print(f"\n映射成功: {len(mapped):,} ({100*len(mapped)/len(all_ingredients):.1f}%)")
    print(f"映射失敗: {len(unmapped):,} ({100*len(unmapped)/len(all_ingredients):.1f}%)")

    # 分析映射成功的唯一 DrugBank ID
    unique_drugbank_ids = set(v[0] for v in mapped.values())
    print(f"對應到的唯一 DrugBank 藥物: {len(unique_drugbank_ids):,}")

    # 分析未映射成分
    print("\n" + "=" * 60)
    print("未映射成分分析")
    print("=" * 60)

    # 按使用藥品數排序
    unmapped_sorted = sorted(unmapped.items(), key=lambda x: x[1], reverse=True)

    print("\n【高影響力未映射成分】（使用藥品數 >= 50）:")
    print("-" * 60)
    high_impact = [(ing, count) for ing, count in unmapped_sorted if count >= 50]
    for ing, count in high_impact[:30]:
        print(f"  {ing:<50} ({count:,} 藥品)")
    print(f"\n  ... 共 {len(high_impact)} 個高影響力成分")

    print("\n【中影響力未映射成分】（使用藥品數 10-49）:")
    mid_impact = [(ing, count) for ing, count in unmapped_sorted if 10 <= count < 50]
    print(f"  共 {len(mid_impact)} 個成分")
    for ing, count in mid_impact[:20]:
        print(f"  {ing:<50} ({count:,} 藥品)")

    # 分析未映射成分的模式
    print("\n" + "=" * 60)
    print("未映射成分模式分析")
    print("=" * 60)

    # 1. 含有特定後綴的成分
    suffix_patterns = {
        "EXTRACT": [],
        "POWDER": [],
        "OIL": [],
        "DRIED": [],
        "WATER": [],
        "TINCTURE": [],
        "FLUID": [],
        "SOLUTION": [],
    }

    for ing, count in unmapped_sorted:
        for suffix in suffix_patterns:
            if suffix in ing:
                suffix_patterns[suffix].append((ing, count))
                break

    print("\n按類型分類:")
    for suffix, items in suffix_patterns.items():
        if items:
            total_drugs = sum(c for _, c in items)
            print(f"  含 '{suffix}': {len(items)} 成分, 影響 {total_drugs:,} 藥品")

    # 2. 中草藥/植物萃取物
    herbal_keywords = ["EXTRACT", "RADIX", "HERBA", "FLOS", "FRUCTUS", "SEMEN", "CORTEX", "RHIZOMA", "FOLIUM"]
    herbal = []
    for ing, count in unmapped_sorted:
        if any(kw in ing for kw in herbal_keywords):
            herbal.append((ing, count))

    print(f"\n中草藥/植物成分: {len(herbal)} 成分")
    for ing, count in herbal[:15]:
        print(f"  {ing:<50} ({count:,} 藥品)")

    # 3. 維生素/礦物質
    vitamin_keywords = ["VITAMIN", "VIT ", "VIT.", "CALCIUM", "MAGNESIUM", "ZINC", "IRON", "POTASSIUM", "SODIUM"]
    vitamins = []
    for ing, count in unmapped_sorted:
        if any(kw in ing for kw in vitamin_keywords):
            vitamins.append((ing, count))

    print(f"\n維生素/礦物質: {len(vitamins)} 成分")
    for ing, count in vitamins[:15]:
        print(f"  {ing:<50} ({count:,} 藥品)")

    # 4. 可能可以透過簡化名稱映射的成分
    print("\n" + "=" * 60)
    print("可能可透過擴展同義詞映射的成分")
    print("=" * 60)

    # 嘗試更激進的標準化
    potential_matches = []
    for ing, count in unmapped_sorted:
        # 移除更多後綴
        simplified = ing
        for suffix in ["ANHYDROUS", "MONOHYDRATE", "DIHYDRATE", "TRIHYDRATE",
                      "USP", "BP", "JP", "EP", "MICRONIZED", "GRANULE", "POWDER"]:
            simplified = simplified.replace(suffix, "").strip()

        # 檢查簡化後是否能映射
        if simplified != ing and simplified:
            drugbank_id = map_ingredient_to_drugbank(simplified, name_index)
            if drugbank_id:
                potential_matches.append((ing, simplified, drugbank_id, count))

    if potential_matches:
        print(f"\n可透過擴展標準化映射的成分: {len(potential_matches)}")
        for orig, simp, db_id, count in potential_matches[:20]:
            print(f"  {orig:<40} -> {simp:<25} ({count:,} 藥品)")

    # 5. 檢查 TxGNN 知識圖譜中有哪些藥物我們沒匹配到
    print("\n" + "=" * 60)
    print("TxGNN 知識圖譜分析")
    print("=" * 60)

    try:
        relations_df = pd.read_csv("data/external/drug_disease_relations.csv")
        txgnn_drugs = set(relations_df["x_name"].str.upper().unique())

        print(f"TxGNN 中的藥物數: {len(txgnn_drugs):,}")

        # 我們映射到的 DrugBank 藥物
        our_drugs = set()
        for ing, (db_id, _) in mapped.items():
            # DrugBank ID 對應的藥物名稱
            matching = drugbank_df[drugbank_df["drugbank_id"] == db_id]
            if len(matching) > 0:
                drug_name = matching.iloc[0]["name"].upper()
                our_drugs.add(drug_name)

        print(f"我們映射到的藥物: {len(our_drugs):,}")

        # 在 TxGNN 中但我們沒映射到的
        missing_in_txgnn = txgnn_drugs - our_drugs
        print(f"TxGNN 中但我們未映射到: {len(missing_in_txgnn):,}")

        # 檢查未映射成分是否直接在 TxGNN 中
        direct_matches = []
        for ing, count in unmapped_sorted:
            if ing in txgnn_drugs:
                direct_matches.append((ing, count))

        if direct_matches:
            print(f"\n未映射成分直接存在於 TxGNN: {len(direct_matches)}")
            for ing, count in direct_matches[:20]:
                print(f"  {ing:<50} ({count:,} 藥品)")
    except Exception as e:
        print(f"無法載入 TxGNN 資料: {e}")

    # 輸出詳細報告
    print("\n" + "=" * 60)
    print("輸出詳細報告")
    print("=" * 60)

    # 儲存未映射成分清單
    unmapped_df = pd.DataFrame([
        {"成分": ing, "使用藥品數": count}
        for ing, count in unmapped_sorted
    ])
    unmapped_df.to_csv("data/processed/unmapped_ingredients.csv", index=False, encoding="utf-8-sig")
    print(f"已儲存: data/processed/unmapped_ingredients.csv ({len(unmapped_df)} 筆)")

    # 儲存潛在可映射清單
    if potential_matches:
        potential_df = pd.DataFrame([
            {"原始成分": orig, "簡化後": simp, "DrugBank_ID": db_id, "使用藥品數": count}
            for orig, simp, db_id, count in potential_matches
        ])
        potential_df.to_csv("data/processed/potential_mappings.csv", index=False, encoding="utf-8-sig")
        print(f"已儲存: data/processed/potential_mappings.csv ({len(potential_df)} 筆)")

    return unmapped_sorted, potential_matches


if __name__ == "__main__":
    analyze_mapping()
