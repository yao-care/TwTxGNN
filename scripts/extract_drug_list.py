#!/usr/bin/env python3
"""
Extract drug list from docs/_drugs/*.md files.
Creates a JSON file with drug names, evidence levels, and indication counts.
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from twtxgnn.regulatory import withdrawn as W  # noqa: E402


def parse_front_matter(content: str) -> dict:
    """Parse YAML front matter from markdown content."""
    if not content.startswith("---"):
        return {}

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}

    front_matter = {}
    for line in parts[1].strip().split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            front_matter[key] = value

    return front_matter


def extract_predicted_indication(content: str) -> str:
    """Extract predicted indication from the drug report."""
    # Look for the pattern in the quick overview table
    match = re.search(r'\|\s*預測新適應症\s*\|\s*([^|]+)\s*\|', content)
    if match:
        return match.group(1).strip()
    return ""


def withdrawn_predictions(reviews_file: Path) -> dict:
    """查核紀錄裡重審撤回（verdict=withdraw）的預測：{頁面檔名: {預測名稱（小寫）}}。

    2026-11-03 用戶決定：撤回的預測不再做證據監測（不開 issue）。front matter 的 predicted_indications
    依站方規則原文不刪，名單以 docs/_data/drug_reviews.json 為準（規則見 src/twtxgnn/regulatory/withdrawn.py）。
    """
    return {f"{slug}.md": names for slug, names in W.load(reviews_file).items()}


def main():
    drugs_dir = Path(__file__).parent.parent / "docs" / "_drugs"
    reviews_file = Path(__file__).parent.parent / "docs" / "_data" / "drug_reviews.json"
    withdrawn = withdrawn_predictions(reviews_file)
    skipped = []
    output_file = Path(__file__).parent / "drug_list.json"

    drugs = []

    for md_file in sorted(drugs_dir.glob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        front_matter = parse_front_matter(content)

        drug_name = front_matter.get("title", md_file.stem)
        evidence_level = front_matter.get("evidence_level", "")
        indication_count = front_matter.get("indication_count", "0")

        # Extract predicted indication for search queries
        predicted_indication = extract_predicted_indication(content)

        # 2026-10-16：監測改用 front matter 的英文 INN 與預測新適應症（不分語言）；
        # 沒有這兩個欄位的頁（轉址頁、無新預測頁）不監測
        try:
            predicted_indications = json.loads(front_matter.get("predicted_indications", "[]"))
        except ValueError:
            predicted_indications = []
        monitor_inn = front_matter.get("monitor_inn", "")
        gone = withdrawn.get(md_file.name, set())
        if gone:
            skipped += [(md_file.name, p) for p in predicted_indications if p.strip().lower() in gone]
            predicted_indications = [p for p in predicted_indications if p.strip().lower() not in gone]
        if not predicted_indications or not monitor_inn:
            continue

        drugs.append({
            "name": drug_name,
            "file": md_file.name,
            "evidence_level": evidence_level,
            "indication_count": int(indication_count) if indication_count.isdigit() else 0,
            "predicted_indication": predicted_indication,
            "inn": monitor_inn,
            "predicted_indications": predicted_indications,
        })

    # Save to JSON
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({
            "total": len(drugs),
            "generated_at": __import__("datetime").datetime.now().isoformat(),
            "drugs": drugs
        }, f, indent=2, ensure_ascii=False)

    print(f"Extracted {len(drugs)} drugs to {output_file}")
    print(f"Skipped {len(skipped)} withdrawn predictions (docs/_data/drug_reviews.json verdict=withdraw)")
    unmatched = sorted((f, n) for f, ns in withdrawn.items() for n in ns
                       if (f, n) not in {(sf, sp.strip().lower()) for sf, sp in skipped})
    for f, n in unmatched:
        print(f"  ⚠ 撤回紀錄的預測不在 {f} 的 predicted_indications：{n}")

    # Print summary
    level_counts = {}
    for drug in drugs:
        level = drug["evidence_level"] or "Unknown"
        level_counts[level] = level_counts.get(level, 0) + 1

    print("\nEvidence level distribution:")
    for level in sorted(level_counts.keys()):
        print(f"  {level}: {level_counts[level]}")


if __name__ == "__main__":
    main()
