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
        "citrus fruits": "柑橘類水果",
        "soft drinks": "汽水/碳酸飲料",
        "caffeine": "咖啡因",
        "dairy products": "乳製品",
        "high-fiber foods": "高纖維食物",
        "high-fat meals": "高脂肪餐",
        "vitamin k-rich foods": "高維生素 K 食物",
        "tyramine-containing foods": "含酪胺食物",
        "charbroiled food": "炭烤食物",
        "cruciferous vegetables": "十字花科蔬菜",
        "spinach": "菠菜",
        "rhubarb": "大黃"
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


def format_dfi_section(interactions: list) -> str:
    """Format DFI interactions as markdown."""
    lines = ["### 藥物-食物交互作用 (DFI)", ""]
    lines.append('<div class="dfi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a></div>')
    lines.append("")

    for i in interactions:
        food_display = f"{i['food_zh']}" if i['food_zh'] != i['food'] else i['food']
        if i['food_zh'] != i['food']:
            food_display += f" ({i['food']})"

        lines.append(f"**{food_display}** {format_severity_badge(i['severity'])}")

        # Clean up interaction text (truncate if too long)
        interaction_text = i['interaction']
        if len(interaction_text) > 200:
            interaction_text = interaction_text[:200] + "..."
        lines.append(f"- 影響：{interaction_text}")

        management_text = i['management']
        if len(management_text) > 200:
            management_text = management_text[:200] + "..."
        lines.append(f"- 建議：{management_text}")
        lines.append("")

    return "\n".join(lines)


def update_report(report_path: Path, drug_name: str, interactions: list) -> bool:
    """Update a drug report with DFI information."""
    if not interactions:
        return False

    # Read report
    with open(report_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if already has DDInter DFI section
    if "DDInter 2.0" in content and "藥物-食物交互作用 (DFI)" in content:
        return False  # Already has DDInter DFI

    # Remove old curated DFI section if exists
    # Pattern: ### 藥物-食物交互作用 (DFI) ... ### 藥物-草藥交互作用 (DHI)
    old_dfi_pattern = r"### 藥物-食物交互作用 \(DFI\)\n\n(?:(?!###).)*?(?=### 藥物-草藥交互作用|## 結論與下一步)"
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
