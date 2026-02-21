#!/usr/bin/env python3
"""
Restructure drug reports to use accordion layout for multiple indications.

This script:
1. Reads drug_bundle.json to get all predicted indications
2. Reads existing markdown report to extract current content
3. Restructures the report with accordion sections for each indication
"""

import json
import re
from pathlib import Path
from typing import Optional

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
BUNDLES_DIR = PROJECT_ROOT / "data" / "bundles"
DRUGS_DIR = PROJECT_ROOT / "docs" / "_drugs"
DRUG_LIST_FILE = SCRIPT_DIR / "drug_list.json"


def load_drug_bundle(drug_name: str) -> Optional[dict]:
    """Load drug bundle JSON."""
    slug = drug_name.lower().replace(" ", "_").replace("-", "_")
    bundle_path = BUNDLES_DIR / slug / "drug_bundle.json"

    if not bundle_path.exists():
        return None

    with open(bundle_path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_sections(content: str) -> dict:
    """Extract existing sections from markdown content."""
    sections = {}

    # Extract "為什麼這個預測合理？" section
    rationale_match = re.search(
        r"## 為什麼這個預測合理[？?]\s*\n(.*?)(?=\n## |\n---|\Z)",
        content,
        re.DOTALL
    )
    if rationale_match:
        sections["rationale"] = rationale_match.group(1).strip()

    # Extract clinical trials table
    trials_match = re.search(
        r"## 臨床試驗證據\s*\n(.*?)(?=\n## |\n---|\Z)",
        content,
        re.DOTALL
    )
    if trials_match:
        sections["trials"] = trials_match.group(1).strip()

    # Extract literature table
    lit_match = re.search(
        r"## 文獻證據\s*\n(.*?)(?=\n## |\n---|\Z)",
        content,
        re.DOTALL
    )
    if lit_match:
        sections["literature"] = lit_match.group(1).strip()

    # Extract Taiwan market info
    taiwan_match = re.search(
        r"## 台灣上市資訊\s*\n(.*?)(?=\n## |\n---|\Z)",
        content,
        re.DOTALL
    )
    if taiwan_match:
        sections["taiwan"] = taiwan_match.group(1).strip()

    # Extract safety section
    safety_match = re.search(
        r"## 安全性考量\s*\n(.*?)(?=\n## |\n---|\Z)",
        content,
        re.DOTALL
    )
    if safety_match:
        sections["safety"] = safety_match.group(1).strip()

    # Extract conclusion
    conclusion_match = re.search(
        r"## 結論與下一步\s*\n(.*?)(?=\n---|\Z)",
        content,
        re.DOTALL
    )
    if conclusion_match:
        sections["conclusion"] = conclusion_match.group(1).strip()

    return sections


def format_indication_accordion(
    index: int,
    indication: dict,
    is_primary: bool,
    existing_sections: dict,
    drug_evidence_level: str = "L5"
) -> str:
    """Format a single indication as an accordion section."""
    name = indication.get("disease_name", "Unknown")
    score = indication.get("txgnn_score", 0) * 100
    # Use drug's evidence level for primary, L5 for others
    level = drug_evidence_level if is_primary else "L5"

    open_attr = " open" if is_primary else ""
    primary_badge = ' <span class="primary-badge">主要分析</span>' if is_primary else ""

    html = f"""
<details class="indication-section"{open_attr}>
<summary>
<span class="indication-name">{index}. {name}</span>
<span class="evidence-badge evidence-{level}">{level}</span>
<span class="prediction-score">{score:.2f}%</span>{primary_badge}
</summary>
<div class="indication-content">
"""

    if is_primary:
        # Use existing content for primary indication
        if existing_sections.get("rationale"):
            html += f"""
### 為什麼這個預測合理？

{existing_sections["rationale"]}
"""

        if existing_sections.get("trials"):
            html += f"""
### 臨床試驗

{existing_sections["trials"]}
"""

        if existing_sections.get("literature"):
            html += f"""
### 相關文獻

{existing_sections["literature"]}
"""
    else:
        # Basic info for non-primary indications
        html += f"""
### TxGNN 預測資訊

- **預測分數**：{score:.2f}%
- **證據等級**：{level}（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>
"""

    html += """
</div>
</details>
"""
    return html


def restructure_report(drug_name: str, report_path: Path) -> bool:
    """Restructure a single drug report."""
    # Load bundle
    bundle = load_drug_bundle(drug_name)
    if not bundle:
        print(f"  No bundle found for {drug_name}")
        return False

    # Get predicted indications
    indications = bundle.get("drug", {}).get("predicted_indications", [])
    if len(indications) <= 1:
        # No need to restructure if only 1 or no indications
        return False

    # Read existing report
    with open(report_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract evidence level from front matter
    level_match = re.search(r"evidence_level:\s*(\w+)", content)
    drug_evidence_level = level_match.group(1) if level_match else "L5"

    # Extract existing sections
    existing_sections = extract_sections(content)
    if not existing_sections:
        print(f"  Could not extract sections from {drug_name}")
        return False

    # Build new accordion section
    accordion_html = "\n## 預測適應症詳細分析\n"

    for i, indication in enumerate(indications):
        is_primary = (i == 0)
        accordion_html += format_indication_accordion(
            i + 1, indication, is_primary, existing_sections, drug_evidence_level
        )

    # Find where to insert the accordion
    # Replace the old sections with the new accordion structure
    # Pattern: from "## 為什麼這個預測合理" to before "## 台灣上市資訊"
    pattern = r"(## 為什麼這個預測合理[？?].*?)(## 台灣上市資訊)"
    replacement = accordion_html + "\n\n\\2"

    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)

    if count == 0:
        print(f"  Could not find sections to replace in {drug_name}")
        return False

    # Write updated report
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def main():
    print("=" * 60)
    print("Restructuring Drug Reports with Accordion Layout")
    print("=" * 60)

    # Load drug list
    with open(DRUG_LIST_FILE, "r", encoding="utf-8") as f:
        drug_list = json.load(f)

    updated = 0
    skipped = 0
    errors = 0

    for drug in drug_list["drugs"]:
        drug_name = drug["name"]
        file_name = drug["file"]
        report_path = DRUGS_DIR / file_name

        if not report_path.exists():
            print(f"  Skipping {drug_name}: file not found")
            skipped += 1
            continue

        try:
            if restructure_report(drug_name, report_path):
                print(f"  Updated: {drug_name}")
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  Error processing {drug_name}: {e}")
            errors += 1

    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"  Updated: {updated}")
    print(f"  Skipped: {skipped}")
    print(f"  Errors: {errors}")


if __name__ == "__main__":
    main()
