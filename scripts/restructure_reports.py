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
from typing import Optional, List

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
BUNDLES_DIR = PROJECT_ROOT / "data" / "bundles"
DRUGS_DIR = PROJECT_ROOT / "docs" / "_drugs"
DRUG_LIST_FILE = SCRIPT_DIR / "drug_list.json"


def calculate_evidence_level(indication: dict) -> str:
    """
    Calculate evidence level for a single indication based on clinical trials and papers.

    Evidence Level Criteria:
    - L1: Multiple Phase 3/4 completed trials (多個大型 RCT)
    - L2: Single Phase 3 or multiple Phase 2 trials (單一 RCT 或多個 Phase 2)
    - L3: Phase 1/2 trials or observational studies (觀察性研究)
    - L4: Has PubMed articles but no/minimal trials (前臨床/機轉研究)
    - L5: No trials, no articles (僅 AI 預測)
    """
    trials = indication.get("clinical_trials", [])
    articles = indication.get("pubmed_articles", [])

    # Count trials by phase
    phase3_4_count = 0
    phase2_count = 0
    phase1_count = 0
    other_trial_count = 0

    for trial in trials:
        phase = trial.get("phase", "").upper()
        status = trial.get("status", "").upper()

        # Count completed or active Phase 3/4 trials
        if "PHASE3" in phase or "PHASE4" in phase or "PHASE 3" in phase or "PHASE 4" in phase:
            phase3_4_count += 1
        elif "PHASE2" in phase or "PHASE 2" in phase:
            phase2_count += 1
        elif "PHASE1" in phase or "PHASE 1" in phase:
            phase1_count += 1
        elif phase and phase != "N/A":
            other_trial_count += 1

    total_trials = len(trials)
    total_articles = len(articles)

    # Determine evidence level
    if phase3_4_count >= 2:
        return "L1"  # Multiple large RCTs
    elif phase3_4_count >= 1 or phase2_count >= 2:
        return "L2"  # Single RCT or multiple Phase 2
    elif phase2_count >= 1 or phase1_count >= 1 or total_trials >= 1:
        return "L3"  # Has trials (observational/early phase)
    elif total_articles >= 1:
        return "L4"  # Has literature but no trials
    else:
        return "L5"  # AI prediction only


def get_evidence_level_description(level: str) -> str:
    """Get Chinese description for evidence level."""
    descriptions = {
        "L1": "多個大型 RCT 支持",
        "L2": "單一 RCT 或多個 Phase 2",
        "L3": "有臨床試驗進行中",
        "L4": "有文獻支持",
        "L5": "僅模型預測"
    }
    return descriptions.get(level, "僅模型預測")


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

    # Extract "為什麼這個預測合理？" section (H2 level only, not H3)
    # Use \n## to ensure we match H2 headers at the start of a line
    rationale_match = re.search(
        r"\n## 為什麼這個預測合理[？?]?\s*\n(.*?)(?=\n## |\n---|\Z)",
        content,
        re.DOTALL
    )
    if rationale_match:
        sections["rationale"] = rationale_match.group(1).strip()

    # Also try variant without "這個"
    if "rationale" not in sections:
        rationale_match = re.search(
            r"\n## 為什麼預測合理[？?]?\s*\n(.*?)(?=\n## |\n---|\Z)",
            content,
            re.DOTALL
        )
        if rationale_match:
            sections["rationale"] = rationale_match.group(1).strip()

    # Extract clinical trials table
    trials_match = re.search(
        r"\n## 臨床試驗證據?\s*\n(.*?)(?=\n## |\n---|\Z)",
        content,
        re.DOTALL
    )
    if trials_match:
        sections["trials"] = trials_match.group(1).strip()

    # Extract literature table
    lit_match = re.search(
        r"\n## 文獻證據\s*\n(.*?)(?=\n## |\n---|\Z)",
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
    existing_sections: dict
) -> str:
    """Format a single indication as an accordion section."""
    name = indication.get("disease_name", "Unknown")
    score = indication.get("txgnn_score", 0) * 100

    # Calculate evidence level from this indication's own data
    level = calculate_evidence_level(indication)
    level_desc = get_evidence_level_description(level)

    trials = indication.get("clinical_trials", [])
    articles = indication.get("pubmed_articles", [])

    open_attr = " open" if is_primary else ""
    primary_badge = ' <span class="primary-badge">主要分析</span>' if is_primary else ""

    html = f"""
<details class="indication-section"{open_attr}>
<summary>
<span class="indication-name">{index}. {name}</span>
<span class="evidence-badge evidence-{level}">{level}</span>
<span class="prediction-score">{score:.2f}%</span>{primary_badge}
</summary>
<div class="indication-content" markdown="1">
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
        # Show TxGNN info
        html += f"""
### TxGNN 預測資訊

- **預測分數**：{score:.2f}%
- **證據等級**：{level}（{level_desc}）

### 臨床證據

"""
        # Show evidence based on what's available
        if trials:
            html += f"**臨床試驗**：共 {len(trials)} 項\n\n"
            # Show trial phases summary
            phase_counts = {}
            for trial in trials:
                phase = trial.get("phase", "N/A")
                phase_counts[phase] = phase_counts.get(phase, 0) + 1
            phase_summary = ", ".join([f"{p}: {c}項" for p, c in sorted(phase_counts.items())])
            html += f"- 試驗階段分布：{phase_summary}\n\n"

        if articles:
            html += f"**相關文獻**：共 {len(articles)} 篇\n\n"

        if not trials and not articles:
            html += """<div class="no-evidence-warning">
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

    # Check if already has accordion structure
    has_accordion = "## 預測適應症詳細分析" in content and "indication-section" in content
    has_h2_rationale = "\n## 為什麼這個預測合理" in content or "\n## 為什麼預測合理" in content

    # Extract existing sections (for reports with old H2-level structure)
    existing_sections = extract_sections(content)

    # If already has accordion but no H2 rationale, try to extract from first accordion item
    if has_accordion and not has_h2_rationale and not existing_sections.get("rationale"):
        # Try to extract rationale from first accordion's H3 section
        h3_rationale_match = re.search(
            r"### 為什麼這個預測合理[？?]?\s*\n(.*?)(?=\n### |\n</div>|\Z)",
            content,
            re.DOTALL
        )
        if h3_rationale_match:
            existing_sections["rationale"] = h3_rationale_match.group(1).strip()

        # Try to extract trials from first accordion
        h3_trials_match = re.search(
            r"### 臨床試驗\s*\n(.*?)(?=\n### |\n</div>|\Z)",
            content,
            re.DOTALL
        )
        if h3_trials_match:
            existing_sections["trials"] = h3_trials_match.group(1).strip()

        # Try to extract literature from first accordion
        h3_lit_match = re.search(
            r"### 相關文獻\s*\n(.*?)(?=\n### |\n</div>|\Z)",
            content,
            re.DOTALL
        )
        if h3_lit_match:
            existing_sections["literature"] = h3_lit_match.group(1).strip()

    if not existing_sections:
        print(f"  Could not extract sections from {drug_name}")
        return False

    # Calculate highest evidence level among all indications for YAML front matter
    highest_level = "L5"
    level_order = {"L1": 1, "L2": 2, "L3": 3, "L4": 4, "L5": 5}
    for indication in indications:
        ind_level = calculate_evidence_level(indication)
        if level_order.get(ind_level, 5) < level_order.get(highest_level, 5):
            highest_level = ind_level

    # Update YAML front matter evidence_level
    content = re.sub(
        r"(evidence_level:\s*)\w+",
        f"\\1{highest_level}",
        content
    )

    # Build new accordion section
    accordion_html = "\n## 預測適應症詳細分析\n"

    for i, indication in enumerate(indications):
        is_primary = (i == 0)
        accordion_html += format_indication_accordion(
            i + 1, indication, is_primary, existing_sections
        )

    # Find where to insert the accordion
    # Try to match existing accordion structure first (for updates)
    accordion_pattern = r"(## 預測適應症詳細分析.*?)(## 台灣上市資訊)"
    new_content, count = re.subn(
        accordion_pattern,
        accordion_html + "\n\n\\2",
        content,
        flags=re.DOTALL
    )

    if count == 0:
        # Try old-style report structure (question mark is optional)
        old_pattern = r"(## 為什麼這個預測合理[？?]?.*?)(## 台灣上市資訊)"
        new_content, count = re.subn(
            old_pattern,
            accordion_html + "\n\n\\2",
            content,
            flags=re.DOTALL
        )

    if count == 0:
        # Try variant: "為什麼這個預測不合理"
        variant_pattern = r"(## 為什麼這個預測不?合理[？?]?.*?)(## 台灣上市資訊)"
        new_content, count = re.subn(
            variant_pattern,
            accordion_html + "\n\n\\2",
            content,
            flags=re.DOTALL
        )

    if count == 0:
        # Try variant: "為什麼預測合理" (without "這個") with different taiwan section names
        variant2_pattern = r"(## 為什麼預測合理[？?]?.*?)(## 台灣上市(?:資訊|狀態|情形))"
        new_content, count = re.subn(
            variant2_pattern,
            accordion_html + "\n\n\\2",
            content,
            flags=re.DOTALL
        )

    if count == 0:
        # Try starting from 快速總覽 with any Taiwan section variant
        overview_pattern = r"(## 快速總覽.*?)(## 台灣上市(?:資訊|狀態|情形))"
        new_content, count = re.subn(
            overview_pattern,
            "## 快速總覽\n\n" + existing_sections.get("overview", "（見下方詳細分析）") + accordion_html + "\n\n\\2",
            content,
            flags=re.DOTALL
        )

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
