#!/usr/bin/env python3
"""
Process DDInter 2.0 DFI data and integrate into drug reports.

This script:
1. Downloads DFI data from DDInter 2.0 API
2. Matches with drugs in our project
3. Updates the "安全性考量" section of each drug report
"""

import json
import re
import subprocess
from pathlib import Path
from typing import Optional

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
DRUGS_DIR = PROJECT_ROOT / "docs" / "_drugs"
DFI_RAW_FILE = PROJECT_ROOT / "data" / "external" / "dfi" / "ddinter2_dfi_raw.json"
DFI_PROCESSED_FILE = PROJECT_ROOT / "data" / "external" / "dfi" / "ddinter2_dfi_processed.json"
DRUG_LIST_FILE = SCRIPT_DIR / "drug_list.json"

# DDInter API endpoint
DDINTER_DFI_API = "https://ddinter2.scbdd.com/server/food-interaction-source/"


def download_dfi_data():
    """Download DFI data from DDInter 2.0 API."""
    print("Downloading DFI data from DDInter 2.0...")

    result = subprocess.run(
        ["curl", "-sS", DDINTER_DFI_API, "-X", "POST", "-d", "draw=1&start=0&length=1000"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"Error downloading data: {result.stderr}")
        return None

    data = json.loads(result.stdout)
    print(f"Downloaded {data['recordsTotal']} DFI records")

    # Save raw data
    DFI_RAW_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DFI_RAW_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return data


def load_dfi_data() -> Optional[dict]:
    """Load DFI data from file or download if not exists."""
    if DFI_RAW_FILE.exists():
        with open(DFI_RAW_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return download_dfi_data()


def process_dfi_data(dfi_data: dict, drug_list: dict) -> dict:
    """Process DFI data and match with our drugs."""
    # Create drug name lookup (case-insensitive)
    our_drugs = {}
    for drug in drug_list["drugs"]:
        our_drugs[drug["name"].lower()] = drug["name"]

    # Level mapping
    level_map = {"1": "Major", "2": "Moderate", "3": "Minor"}

    # Process interactions
    processed = {
        "metadata": {
            "source": "DDInter 2.0",
            "url": "https://ddinter2.scbdd.com/",
            "total_records": dfi_data["recordsTotal"],
            "license": "CC BY-NC-SA 4.0"
        },
        "interactions": {}
    }

    for item in dfi_data["data"]:
        drug_name_lower = item["drugName"].lower()

        if drug_name_lower in our_drugs:
            canonical_name = our_drugs[drug_name_lower]

            if canonical_name not in processed["interactions"]:
                processed["interactions"][canonical_name] = []

            processed["interactions"][canonical_name].append({
                "food": item["foodName"],
                "food_zh": translate_food(item["foodName"]),
                "severity": level_map.get(item["level"], "Unknown"),
                "mechanism": item.get("magnesium", ""),  # Field name is misleading in API
                "interaction": item["newInteraction"],
                "management": item["newManagement"],
                "references": item.get("references", "")
            })

    # Save processed data
    with open(DFI_PROCESSED_FILE, "w", encoding="utf-8") as f:
        json.dump(processed, f, ensure_ascii=False, indent=2)

    return processed


def translate_food(food_name: str) -> str:
    """Translate common food names to Chinese."""
    translations = {
        "alcohol": "酒精",
        "grapefruit juice": "葡萄柚汁",
        "grapefruit": "葡萄柚",
        "food": "食物",
        "food high in potassium": "高鉀食物",
        "food high in vitamin k": "高維生素 K 食物",
        "vitamin k-rich foods": "高維生素 K 食物",
        "citrus fruits": "柑橘類水果",
        "soft drinks": "汽水/碳酸飲料",
        "caffeine": "咖啡因",
        "coffee": "咖啡",
        "tea": "茶",
        "dairy products": "乳製品",
        "milk": "牛奶",
        "high-fiber foods": "高纖維食物",
        "high-fat meals": "高脂肪餐",
        "high fat meal": "高脂肪餐",
        "tyramine-containing foods": "含酪胺食物",
        "tyramine-rich foods": "含酪胺食物",
        "charbroiled food": "炭烤食物",
        "cruciferous vegetables": "十字花科蔬菜",
        "spinach": "菠菜",
        "rhubarb": "大黃",
        "orange juice": "柳橙汁",
        "cranberry juice": "蔓越莓汁",
        "pomelo": "柚子",
        "seville orange": "塞維爾柳橙",
        "st. john's wort": "聖約翰草",
        "licorice": "甘草",
        "green tea": "綠茶",
        "iron supplements": "鐵劑補充品",
        "calcium supplements": "鈣質補充品",
        "antacids": "制酸劑"
    }
    return translations.get(food_name.lower(), food_name)


def format_severity_badge(severity: str) -> str:
    """Format severity as a badge."""
    badges = {
        "Major": "🔴 Major",
        "Moderate": "🟡 Moderate",
        "Minor": "🟢 Minor"
    }
    return badges.get(severity, f"⚪ {severity}")


def translate_dfi_interaction(description: str, mechanism: str) -> str:
    """Translate DFI interaction description to Chinese."""
    desc_lower = description.lower()

    parts = []

    # Check mechanism
    if mechanism:
        mech_lower = mechanism.lower()
        if "absorption" in mech_lower:
            parts.append("影響藥物吸收")
        elif "metabolism" in mech_lower:
            parts.append("影響藥物代謝")
        elif "synergy" in mech_lower:
            parts.append("產生協同作用")
        elif "antagonism" in mech_lower:
            parts.append("產生拮抗作用")

    # Check for specific effects
    if "increase" in desc_lower and "concentration" in desc_lower:
        parts.append("可能增加藥物血中濃度")
    elif "increase" in desc_lower and "effect" in desc_lower:
        parts.append("可能增強藥效")
    elif "increase" in desc_lower and "absorption" in desc_lower:
        parts.append("可能增加藥物吸收")
    elif "decrease" in desc_lower and "concentration" in desc_lower:
        parts.append("可能降低藥物血中濃度")
    elif "decrease" in desc_lower and "effect" in desc_lower:
        parts.append("可能降低藥效")
    elif "decrease" in desc_lower and "absorption" in desc_lower:
        parts.append("可能減少藥物吸收")
    elif "reduce" in desc_lower and "effect" in desc_lower:
        parts.append("可能降低藥效")
    elif "enhance" in desc_lower:
        parts.append("可能增強藥效")
    elif "inhibit" in desc_lower:
        parts.append("可能抑制藥物作用")
    elif "delay" in desc_lower and "absorption" in desc_lower:
        parts.append("可能延遲藥物吸收")

    # Check for specific risks
    risks = []
    if "toxicity" in desc_lower:
        risks.append("毒性增加")
    if "bleeding" in desc_lower or "hemorrhage" in desc_lower:
        risks.append("出血風險")
    if "hypoglycemia" in desc_lower:
        risks.append("低血糖")
    if "hyperglycemia" in desc_lower:
        risks.append("高血糖")
    if "hypotension" in desc_lower:
        risks.append("低血壓")
    if "hypertension" in desc_lower:
        risks.append("高血壓")
    if "sedation" in desc_lower or "drowsiness" in desc_lower:
        risks.append("嗜睡")
    if "hypokalemia" in desc_lower:
        risks.append("低血鉀")
    if "hyperkalemia" in desc_lower:
        risks.append("高血鉀")

    if risks:
        parts.append("風險包括：" + "、".join(risks))

    # Check for CYP interactions
    if "cyp3a4" in desc_lower or "cyp 3a4" in desc_lower:
        if "inhibit" in desc_lower:
            parts.append("抑制 CYP3A4 酵素")
        elif "induc" in desc_lower:
            parts.append("誘導 CYP3A4 酵素")
    if "cyp2d6" in desc_lower:
        parts.append("影響 CYP2D6 酵素")
    if "cyp1a2" in desc_lower:
        parts.append("影響 CYP1A2 酵素")

    if parts:
        return "。".join(parts) + "。"
    else:
        return "可能與本藥物產生交互作用，影響藥效或安全性。"


def translate_dfi_management(management: str, food_name: str = "") -> str:
    """Translate DFI management recommendations to Chinese."""
    mgmt_lower = management.lower()
    food_lower = food_name.lower()

    parts = []

    # Check for timing recommendations
    if "separate" in mgmt_lower or "apart" in mgmt_lower:
        if "hour" in mgmt_lower:
            parts.append("建議間隔服用")
        else:
            parts.append("建議分開服用")

    # Check for avoidance
    if "avoid" in mgmt_lower:
        if "large amount" in mgmt_lower or "excessive" in mgmt_lower:
            parts.append("避免大量攝取")
        elif "completely" in mgmt_lower or "should be avoided" in mgmt_lower:
            parts.append("應完全避免")
        else:
            parts.append("建議避免併用")

    # Check for monitoring
    if "monitor" in mgmt_lower:
        parts.append("需監測療效或不良反應")

    # Check for dose adjustment
    if "dose" in mgmt_lower and ("adjust" in mgmt_lower or "reduc" in mgmt_lower):
        parts.append("可能需調整劑量")

    # Check for consistency
    if "consistent" in mgmt_lower or "vary" in mgmt_lower:
        parts.append("飲食應保持一致")

    # Check for with/without food
    if "with food" in mgmt_lower:
        parts.append("建議隨餐服用")
    elif "without food" in mgmt_lower or "empty stomach" in mgmt_lower:
        parts.append("建議空腹服用")

    # Check for specific foods - only add grapefruit warning if the food IS grapefruit
    if "grapefruit" in food_lower and "grapefruit" in mgmt_lower:
        parts.append("避免食用葡萄柚或葡萄柚汁")

    if parts:
        return "。".join(parts) + "。"
    else:
        return "請諮詢醫師或藥師了解詳細建議。"


def format_dfi_section(interactions: list) -> str:
    """Format DFI interactions as markdown."""
    lines = ["### 藥物-食物交互作用 (DFI)", ""]
    lines.append('<div class="dfi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>')
    lines.append("")

    for i in interactions:
        food_display = i['food_zh'] if i['food_zh'] != i['food'] else i['food']

        lines.append(f"**{food_display}** {format_severity_badge(i['severity'])}")

        # Translate interaction and management to Chinese
        interaction_zh = translate_dfi_interaction(i['interaction'], i.get('mechanism', ''))
        management_zh = translate_dfi_management(i['management'], i['food'])

        lines.append(f"- 影響：{interaction_zh}")
        lines.append(f"- 建議：{management_zh}")
        lines.append("")

    return "\n".join(lines)


def update_report(report_path: Path, drug_name: str, interactions: list) -> bool:
    """Update a drug report with DFI information."""
    if not interactions:
        return False

    # Read report
    with open(report_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove existing DFI section (including DDInter 2.0 version) to replace with updated Chinese translation
    # This pattern matches from "### 藥物-食物交互作用 (DFI)" to the next section
    old_dfi_pattern = r"### 藥物-食物交互作用 \(DFI\)\n+.*?(?=\n### |\n## )"
    content = re.sub(old_dfi_pattern, "", content, flags=re.DOTALL)

    # Format new DFI section
    new_section = format_dfi_section(interactions)

    # Find the safety section and insert DFI
    # Look for existing DHI section or conclusion
    if "### 藥物-草藥交互作用 (DHI)" in content:
        # Insert before DHI
        content = content.replace(
            "### 藥物-草藥交互作用 (DHI)",
            f"{new_section}\n### 藥物-草藥交互作用 (DHI)"
        )
    else:
        # Insert before conclusion
        safety_pattern = r"(## 安全性考量\s*\n)(.*?)(## 結論與下一步)"
        match = re.search(safety_pattern, content, re.DOTALL)
        if match:
            existing_safety = match.group(2).rstrip()
            new_safety = f"{existing_safety}\n\n{new_section}\n\n"
            content = content[:match.start(2)] + new_safety + match.group(3) + content[match.end():]
        else:
            return False

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def main():
    print("=" * 60)
    print("Processing DDInter 2.0 DFI Data")
    print("=" * 60)

    # Load DFI data
    dfi_data = load_dfi_data()
    if not dfi_data:
        print("Failed to load DFI data")
        return

    # Load drug list
    with open(DRUG_LIST_FILE, "r", encoding="utf-8") as f:
        drug_list = json.load(f)

    # Process data
    processed = process_dfi_data(dfi_data, drug_list)

    print(f"\nMatched {len(processed['interactions'])} drugs with DFI data")

    # Update reports
    updated = 0
    for drug in drug_list["drugs"]:
        drug_name = drug["name"]
        file_name = drug["file"]
        report_path = DRUGS_DIR / file_name

        if not report_path.exists():
            continue

        interactions = processed["interactions"].get(drug_name, [])
        if interactions and update_report(report_path, drug_name, interactions):
            print(f"  Updated: {drug_name} ({len(interactions)} interactions)")
            updated += 1

    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"  Total drugs with DFI: {len(processed['interactions'])}")
    print(f"  Reports updated: {updated}")


if __name__ == "__main__":
    main()
