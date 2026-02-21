#!/usr/bin/env python3
"""
Update drug reports with complete predicted indications.

This script:
1. Reads txgnn_dl_predictions.csv to get all predictions
2. Updates drug_list.json with all indications for each drug
3. Updates markdown reports with complete indication lists
"""

import csv
import json
import re
from pathlib import Path
from collections import defaultdict

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
PREDICTIONS_FILE = PROJECT_ROOT / "data" / "processed" / "txgnn_dl_predictions.csv"
DRUG_LIST_FILE = SCRIPT_DIR / "drug_list.json"
DRUGS_DIR = PROJECT_ROOT / "docs" / "_drugs"

# Translation dictionary for common disease terms (English -> Chinese)
# This is a subset - many will remain in English
DISEASE_TRANSLATIONS = {
    "female breast carcinoma": "女性乳腺癌",
    "neuroblastoma": "神經母細胞瘤",
    "ganglioneuroblastoma": "神經節母細胞瘤",
    "retroperitoneal neoplasm": "腹膜後腫瘤",
    "monocytic leukemia": "單核細胞白血病",
    "cardiomyopathy": "心肌病變",
    "preeclampsia": "子癲前症",
    "anxiety disorder": "焦慮症",
    "acne": "青春痘",
    "dermatitis": "皮膚炎",
}


def load_predictions() -> dict:
    """Load all predictions grouped by drug name."""
    predictions = defaultdict(list)

    with open(PREDICTIONS_FILE, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            drug_name = row["drug_name"]
            indication = row["潛在新適應症"]
            score = float(row["txgnn_score"])
            predictions[drug_name].append({
                "indication": indication,
                "score": score
            })

    # Sort each drug's predictions by score (descending)
    for drug_name in predictions:
        predictions[drug_name].sort(key=lambda x: x["score"], reverse=True)

    return predictions


def load_drug_list() -> dict:
    """Load the drug list."""
    with open(DRUG_LIST_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_drug_list(data: dict):
    """Save the drug list."""
    with open(DRUG_LIST_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def format_indication(indication: str) -> str:
    """Format indication with Chinese translation if available."""
    indication_lower = indication.lower()

    # Check for direct translation
    for eng, chi in DISEASE_TRANSLATIONS.items():
        if eng.lower() == indication_lower:
            return chi

    # Return original if no translation
    return indication


def get_top_indications(predictions: list, count: int) -> list:
    """Get top N indications for a drug."""
    return [p["indication"] for p in predictions[:count]]


def update_markdown_report(drug_name: str, indications: list, file_path: Path) -> bool:
    """Update a single markdown report with new indications."""
    if not file_path.exists():
        print(f"  Warning: File not found: {file_path}")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Format indications string (Chinese comma separated)
    indications_str = "、".join([format_indication(ind) for ind in indications])

    # Find and replace the indication line in the quick overview table
    # Pattern: | 預測新適應症 | ... | or | TxGNN 預測新適應症 | ... |
    patterns = [
        r'(\| 預測新適應症 \|)[^\|]+(\|)',
        r'(\| TxGNN 預測新適應症 \|)[^\|]+(\|)',
    ]

    updated = False
    for pattern in patterns:
        if re.search(pattern, content):
            new_content = re.sub(pattern, rf'\1 {indications_str} \2', content)
            if new_content != content:
                content = new_content
                updated = True
                break

    if updated:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    else:
        print(f"  Warning: Could not find indication pattern in {file_path}")
        return False


def main():
    print("=" * 60)
    print("Updating Drug Indications")
    print("=" * 60)

    # Load data
    print("\nLoading predictions...")
    predictions = load_predictions()
    print(f"  Loaded predictions for {len(predictions)} drugs")

    print("\nLoading drug list...")
    drug_list = load_drug_list()
    print(f"  Loaded {drug_list['total']} drugs")

    # Track updates
    updated_count = 0
    skipped_count = 0
    missing_predictions = []

    # Update each drug
    print("\nUpdating drugs...")
    for drug in drug_list["drugs"]:
        drug_name = drug["name"]
        indication_count = drug.get("indication_count", 1)

        # Get predictions for this drug
        drug_predictions = predictions.get(drug_name, [])

        if not drug_predictions:
            missing_predictions.append(drug_name)
            skipped_count += 1
            continue

        # Get top N indications
        top_indications = get_top_indications(drug_predictions, indication_count)

        # Format as string
        indications_str = "、".join([format_indication(ind) for ind in top_indications])

        # Check if update is needed
        current = drug.get("predicted_indication", "")
        if current != indications_str:
            drug["predicted_indication"] = indications_str

            # Update markdown file
            file_path = DRUGS_DIR / drug["file"]
            if update_markdown_report(drug_name, top_indications, file_path):
                print(f"  Updated: {drug_name} ({indication_count} indications)")
                updated_count += 1
            else:
                print(f"  Skipped markdown: {drug_name}")

    # Save updated drug list
    print("\nSaving drug list...")
    save_drug_list(drug_list)

    # Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"  Updated: {updated_count} drugs")
    print(f"  Skipped: {skipped_count} drugs")
    if missing_predictions:
        print(f"  Missing predictions: {len(missing_predictions)}")
        print(f"    Examples: {missing_predictions[:5]}")

    print("\nDone!")


if __name__ == "__main__":
    main()
