#!/usr/bin/env python3
"""
Integrate DFI (Drug-Food Interactions) and DHI (Drug-Herb Interactions) into drug reports.

This script:
1. Reads DFI and DHI curated datasets
2. Matches interactions with drugs in our project
3. Updates the "安全性考量" section of each drug report
"""

import json
import re
from pathlib import Path
from typing import Optional

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
DRUGS_DIR = PROJECT_ROOT / "docs" / "_drugs"
DFI_FILE = PROJECT_ROOT / "data" / "external" / "dfi" / "dfi_curated.json"
DHI_FILE = PROJECT_ROOT / "data" / "external" / "dhi" / "dhi_curated.json"
DRUG_LIST_FILE = SCRIPT_DIR / "drug_list.json"


def load_dfi_data() -> dict:
    """Load DFI curated data."""
    if not DFI_FILE.exists():
        return {"interactions": [], "food_categories": {}}

    with open(DFI_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_dhi_data() -> dict:
    """Load DHI curated data."""
    if not DHI_FILE.exists():
        return {"interactions": [], "herb_categories": {}}

    with open(DHI_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_drug_interactions(drug_name: str, dfi_data: dict, dhi_data: dict) -> dict:
    """Get DFI and DHI interactions for a specific drug."""
    # Normalize drug name for matching
    drug_lower = drug_name.lower().strip()

    # Find DFI interactions
    dfi_interactions = []
    for interaction in dfi_data.get("interactions", []):
        if interaction["drug"].lower() == drug_lower:
            food_key = interaction["food"]
            food_info = dfi_data.get("food_categories", {}).get(food_key, {})
            dfi_interactions.append({
                "food": food_info.get("name_zh", food_key),
                "severity": interaction["severity"],
                "effect": interaction["effect_zh"],
                "management": interaction["management_zh"]
            })

    # Find DHI interactions
    dhi_interactions = []
    for interaction in dhi_data.get("interactions", []):
        if interaction["drug"].lower() == drug_lower:
            herb_key = interaction["herb"]
            herb_info = dhi_data.get("herb_categories", {}).get(herb_key, {})
            dhi_interactions.append({
                "herb": herb_info.get("name_zh", herb_key),
                "severity": interaction["severity"],
                "effect": interaction["effect_zh"],
                "management": interaction["management_zh"]
            })

    return {
        "dfi": dfi_interactions,
        "dhi": dhi_interactions
    }


def format_severity_badge(severity: str) -> str:
    """Format severity as a badge."""
    color_map = {
        "Major": "🔴",
        "Moderate": "🟡",
        "Minor": "🟢"
    }
    return f"{color_map.get(severity, '⚪')} {severity}"


def format_interaction_section(interactions: dict) -> str:
    """Format DFI/DHI interactions as markdown."""
    sections = []

    # DFI Section
    if interactions["dfi"]:
        dfi_lines = ["### 藥物-食物交互作用 (DFI)", ""]
        for i in interactions["dfi"]:
            dfi_lines.append(f"**{i['food']}** {format_severity_badge(i['severity'])}")
            dfi_lines.append(f"- 影響：{i['effect']}")
            dfi_lines.append(f"- 建議：{i['management']}")
            dfi_lines.append("")
        sections.append("\n".join(dfi_lines))

    # DHI Section
    if interactions["dhi"]:
        dhi_lines = ["### 藥物-草藥交互作用 (DHI)", ""]
        for i in interactions["dhi"]:
            dhi_lines.append(f"**{i['herb']}** {format_severity_badge(i['severity'])}")
            dhi_lines.append(f"- 影響：{i['effect']}")
            dhi_lines.append(f"- 建議：{i['management']}")
            dhi_lines.append("")
        sections.append("\n".join(dhi_lines))

    return "\n".join(sections)


def update_report(report_path: Path, drug_name: str, interactions: dict) -> bool:
    """Update a drug report with DFI/DHI information."""
    if not interactions["dfi"] and not interactions["dhi"]:
        return False

    # Read report
    with open(report_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if already has DFI/DHI sections
    if "藥物-食物交互作用 (DFI)" in content or "藥物-草藥交互作用 (DHI)" in content:
        return False  # Already has these sections

    # Format new interaction section
    new_section = format_interaction_section(interactions)

    # Find the safety section
    # Pattern: ## 安全性考量 ... ## 結論與下一步
    safety_pattern = r"(## 安全性考量\s*\n)(.*?)(## 結論與下一步)"

    match = re.search(safety_pattern, content, re.DOTALL)
    if match:
        # Insert after the existing safety content
        existing_safety = match.group(2).rstrip()
        new_safety = f"{existing_safety}\n\n{new_section}\n\n"
        new_content = content[:match.start(2)] + new_safety + match.group(3) + content[match.end():]

        with open(report_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True

    return False


def main():
    print("=" * 60)
    print("Integrating DFI/DHI into Drug Reports")
    print("=" * 60)

    # Load data
    dfi_data = load_dfi_data()
    dhi_data = load_dhi_data()

    print(f"\nLoaded {len(dfi_data.get('interactions', []))} DFI interactions")
    print(f"Loaded {len(dhi_data.get('interactions', []))} DHI interactions")

    # Load drug list
    with open(DRUG_LIST_FILE, "r", encoding="utf-8") as f:
        drug_list = json.load(f)

    updated = 0
    skipped = 0
    no_interactions = 0

    for drug in drug_list["drugs"]:
        drug_name = drug["name"]
        file_name = drug["file"]
        report_path = DRUGS_DIR / file_name

        if not report_path.exists():
            skipped += 1
            continue

        # Get interactions for this drug
        interactions = get_drug_interactions(drug_name, dfi_data, dhi_data)

        if not interactions["dfi"] and not interactions["dhi"]:
            no_interactions += 1
            continue

        # Update report
        if update_report(report_path, drug_name, interactions):
            print(f"  Updated: {drug_name}")
            print(f"    - DFI: {len(interactions['dfi'])} interactions")
            print(f"    - DHI: {len(interactions['dhi'])} interactions")
            updated += 1
        else:
            skipped += 1

    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"  Updated: {updated}")
    print(f"  Skipped (already has or no match): {skipped}")
    print(f"  No interactions found: {no_interactions}")


if __name__ == "__main__":
    main()
