#!/usr/bin/env python3
"""
Regenerate indication content in drug reports.

This script:
1. Reads drug_bundle.json for each drug
2. Generates HTML tables for indications with data
3. Uses concise notice for indications without data
4. Preserves existing "為什麼這個預測合理？" content for primary indication
5. Uses pure HTML format (no markdown="1") to ensure table rendering
"""

import json
import re
from pathlib import Path
from typing import Optional
from html import escape

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
BUNDLES_DIR = PROJECT_ROOT / "data" / "bundles"
DRUGS_DIR = PROJECT_ROOT / "docs" / "_drugs"
DRUG_LIST_FILE = SCRIPT_DIR / "drug_list.json"


def calculate_evidence_level(indication: dict) -> str:
    """Calculate evidence level based on clinical trials and papers."""
    trials = indication.get("clinical_trials", [])
    articles = indication.get("pubmed_articles", [])

    phase3_4_count = 0
    phase2_count = 0
    phase1_count = 0

    for trial in trials:
        phase = trial.get("phase", "").upper()
        if "PHASE3" in phase or "PHASE4" in phase or "PHASE 3" in phase or "PHASE 4" in phase:
            phase3_4_count += 1
        elif "PHASE2" in phase or "PHASE 2" in phase:
            phase2_count += 1
        elif "PHASE1" in phase or "PHASE 1" in phase:
            phase1_count += 1

    total_articles = len(articles)

    if phase3_4_count >= 2:
        return "L1"
    elif phase3_4_count >= 1 or phase2_count >= 2:
        return "L2"
    elif phase2_count >= 1 or phase1_count >= 1 or len(trials) >= 1:
        return "L3"
    elif total_articles >= 1:
        return "L4"
    else:
        return "L5"


def load_drug_bundle(drug_name: str) -> Optional[dict]:
    """Load drug bundle JSON."""
    slug = drug_name.lower().replace(" ", "_").replace("-", "_")
    bundle_path = BUNDLES_DIR / slug / "drug_bundle.json"
    if not bundle_path.exists():
        return None
    with open(bundle_path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_primary_content(content: str) -> dict:
    """Extract existing content from the primary indication."""
    sections = {}

    # First, try to extract from Markdown H3 inside first accordion (current structure)
    h3_rationale = re.search(
        r"<details[^>]*open[^>]*>.*?### 為什麼這個預測合理[？?]?\s*\n(.*?)(?=\n### |\n</div>)",
        content,
        re.DOTALL
    )
    if h3_rationale:
        sections["rationale"] = h3_rationale.group(1).strip()

    # Try HTML <h3> format (already converted reports)
    if not sections.get("rationale"):
        html_h3_rationale = re.search(
            r"<details[^>]*open[^>]*>.*?<h3>為什麼這個預測合理[？?]?</h3>\s*(.*?)(?=<h3>|\n</div>)",
            content,
            re.DOTALL
        )
        if html_h3_rationale:
            sections["rationale"] = html_h3_rationale.group(1).strip()
            sections["is_html"] = True  # Flag that content is already HTML

    # Try to extract clinical trials from Markdown H3
    h3_trials = re.search(
        r"<details[^>]*open[^>]*>.*?### 臨床試驗\s*\n(.*?)(?=\n### |\n</div>)",
        content,
        re.DOTALL
    )
    if h3_trials:
        sections["trials"] = h3_trials.group(1).strip()

    # Try HTML <h3> format for trials
    if not sections.get("trials"):
        html_h3_trials = re.search(
            r"<details[^>]*open[^>]*>.*?<h3>臨床試驗[^<]*</h3>\s*(.*?)(?=<h3>|\n</div>)",
            content,
            re.DOTALL
        )
        if html_h3_trials:
            sections["trials"] = html_h3_trials.group(1).strip()
            sections["trials_is_html"] = True

    # Try to extract literature from Markdown H3
    h3_lit = re.search(
        r"<details[^>]*open[^>]*>.*?### 相關文獻\s*\n(.*?)(?=\n### |\n</div>)",
        content,
        re.DOTALL
    )
    if h3_lit:
        sections["literature"] = h3_lit.group(1).strip()

    # Try HTML <h3> format for literature
    if not sections.get("literature"):
        html_h3_lit = re.search(
            r"<details[^>]*open[^>]*>.*?<h3>相關文獻[^<]*</h3>\s*(.*?)(?=<h3>|\n</div>)",
            content,
            re.DOTALL
        )
        if html_h3_lit:
            sections["literature"] = html_h3_lit.group(1).strip()
            sections["literature_is_html"] = True

    # If no H3 content found, try H2 level (old structure)
    if not sections.get("rationale"):
        h2_rationale = re.search(
            r"\n## 為什麼這個預測合理[？?]?\s*\n(.*?)(?=\n## |\n---|\Z)",
            content,
            re.DOTALL
        )
        if h2_rationale:
            sections["rationale"] = h2_rationale.group(1).strip()

    return sections


def convert_markdown_to_html(md_content: str) -> str:
    """Convert simple markdown content to HTML."""
    if not md_content:
        return ""

    lines = md_content.split("\n")
    html_lines = []
    list_type = None  # 'ul', 'ol', or None
    in_table = False
    table_lines = []

    for line in lines:
        stripped = line.strip()

        # Handle markdown tables
        if stripped.startswith("|") and stripped.endswith("|"):
            if not in_table:
                in_table = True
                table_lines = []
            table_lines.append(stripped)
            continue
        elif in_table:
            # End of table
            html_lines.append(convert_md_table_to_html(table_lines))
            in_table = False
            table_lines = []

        # Handle bullet points
        if stripped.startswith("- "):
            if list_type != 'ul':
                if list_type:
                    html_lines.append(f"</{list_type}>")
                html_lines.append("<ul>")
                list_type = 'ul'
            html_lines.append(f"<li>{process_inline_markdown(stripped[2:])}</li>")
            continue

        # Handle numbered lists
        if re.match(r"^\d+\.\s", stripped):
            content = re.sub(r"^\d+\.\s", "", stripped)
            if list_type != 'ol':
                if list_type:
                    html_lines.append(f"</{list_type}>")
                html_lines.append("<ol>")
                list_type = 'ol'
            html_lines.append(f"<li>{process_inline_markdown(content)}</li>")
            continue

        # Close any open list if we're not in a list item
        if list_type and stripped:
            html_lines.append(f"</{list_type}>")
            list_type = None

        # Regular paragraph
        if stripped:
            html_lines.append(f"<p>{process_inline_markdown(stripped)}</p>")
        else:
            html_lines.append("")

    if list_type:
        html_lines.append(f"</{list_type}>")
    if in_table:
        html_lines.append(convert_md_table_to_html(table_lines))

    return "\n".join(html_lines)


def process_inline_markdown(text: str) -> str:
    """Process inline markdown (bold, links, etc.)."""
    # Bold: **text** or __text__
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"__(.+?)__", r"<strong>\1</strong>", text)
    # Links: [text](url)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def convert_md_table_to_html(table_lines: list) -> str:
    """Convert markdown table lines to HTML table."""
    if len(table_lines) < 2:
        return ""

    html = ["<table>", "<thead>", "<tr>"]

    # Header row
    headers = [cell.strip() for cell in table_lines[0].split("|")[1:-1]]
    for header in headers:
        html.append(f"<th>{process_inline_markdown(header)}</th>")
    html.append("</tr>")
    html.append("</thead>")
    html.append("<tbody>")

    # Data rows (skip separator row)
    for row in table_lines[2:]:
        cells = [cell.strip() for cell in row.split("|")[1:-1]]
        html.append("<tr>")
        for cell in cells:
            html.append(f"<td>{process_inline_markdown(cell)}</td>")
        html.append("</tr>")

    html.append("</tbody>")
    html.append("</table>")
    return "\n".join(html)


def generate_trials_table(trials: list) -> str:
    """Generate HTML table for clinical trials."""
    if not trials:
        return "<p>目前尚無針對此適應症的臨床試驗登記。</p>"

    html = [
        "<table>",
        "<thead>",
        "<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>",
        "</thead>",
        "<tbody>"
    ]

    # Show up to 5 trials
    for trial in trials[:5]:
        nct_id = trial.get("nct_id", trial.get("id", "N/A"))
        phase = trial.get("phase", "N/A")
        status = trial.get("status", "N/A")
        enrollment = trial.get("enrollment", "N/A")
        title = trial.get("title", trial.get("brief_title", ""))[:80]
        if len(trial.get("title", "")) > 80:
            title += "..."

        if nct_id.startswith("NCT"):
            nct_link = f'<a href="https://clinicaltrials.gov/study/{nct_id}" target="_blank">{nct_id}</a>'
        else:
            nct_link = nct_id

        html.append(f"<tr><td>{nct_link}</td><td>{escape(str(phase))}</td><td>{escape(str(status))}</td><td>{escape(str(enrollment))}</td><td>{escape(title)}</td></tr>")

    html.append("</tbody>")
    html.append("</table>")

    if len(trials) > 5:
        html.append(f"<p><em>...及其他 {len(trials) - 5} 項試驗</em></p>")

    return "\n".join(html)


def generate_literature_table(articles: list) -> str:
    """Generate HTML table for literature."""
    if not articles:
        return "<p>目前尚無針對此適應症的相關文獻。</p>"

    html = [
        "<table>",
        "<thead>",
        "<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>",
        "</thead>",
        "<tbody>"
    ]

    # Show up to 5 articles
    for article in articles[:5]:
        pmid = article.get("pmid", "N/A")
        year = article.get("year", article.get("pub_year", "N/A"))
        article_type = article.get("type", article.get("publication_type", "Article"))
        journal = article.get("journal", "N/A")[:20]
        title = article.get("title", "")[:60]
        if len(article.get("title", "")) > 60:
            title += "..."

        if pmid and pmid != "N/A":
            pmid_link = f'<a href="https://pubmed.ncbi.nlm.nih.gov/{pmid}/" target="_blank">{pmid}</a>'
        else:
            pmid_link = pmid

        html.append(f"<tr><td>{pmid_link}</td><td>{escape(str(year))}</td><td>{escape(str(article_type))}</td><td>{escape(journal)}</td><td>{escape(title)}</td></tr>")

    html.append("</tbody>")
    html.append("</table>")

    if len(articles) > 5:
        html.append(f"<p><em>...及其他 {len(articles) - 5} 篇文獻</em></p>")

    return "\n".join(html)


def format_indication_html(
    index: int,
    indication: dict,
    is_primary: bool,
    existing_content: dict
) -> str:
    """Format indication as HTML accordion section."""
    name = indication.get("disease_name", "Unknown")
    score = indication.get("txgnn_score", 0) * 100
    level = calculate_evidence_level(indication)

    trials = indication.get("clinical_trials", [])
    articles = indication.get("pubmed_articles", [])

    open_attr = " open" if is_primary else ""
    primary_badge = ' <span class="primary-badge">主要分析</span>' if is_primary else ""

    html = f'''
<details class="indication-section"{open_attr}>
<summary>
<span class="indication-name">{index}. {escape(name)}</span>
<span class="evidence-badge evidence-{level}">{level}</span>
<span class="prediction-score">{score:.2f}%</span>{primary_badge}
</summary>
<div class="indication-content">
'''

    if is_primary and existing_content.get("rationale"):
        # Use existing content for primary indication
        # Check if content is already HTML (skip conversion)
        if existing_content.get("is_html"):
            rationale_html = existing_content["rationale"]
        else:
            rationale_html = convert_markdown_to_html(existing_content["rationale"])
        html += f'''
<h3>為什麼這個預測合理？</h3>

{rationale_html}
'''
        # Use existing trials/literature if available, otherwise generate from data
        if existing_content.get("trials"):
            if existing_content.get("trials_is_html"):
                trials_html = existing_content["trials"]
            else:
                trials_html = convert_markdown_to_html(existing_content["trials"])
            html += f'''
<h3>臨床試驗</h3>

{trials_html}
'''
        elif trials:
            html += f'''
<h3>臨床試驗</h3>

{generate_trials_table(trials)}
'''
        else:
            html += '''
<h3>臨床試驗</h3>

<p>目前無針對此特定適應症的臨床試驗登記。</p>
'''

        if existing_content.get("literature"):
            if existing_content.get("literature_is_html"):
                lit_html = existing_content["literature"]
            else:
                lit_html = convert_markdown_to_html(existing_content["literature"])
            html += f'''
<h3>相關文獻</h3>

{lit_html}
'''
        elif articles:
            html += f'''
<h3>相關文獻</h3>

{generate_literature_table(articles)}
'''

    else:
        # Non-primary indication: show data or notice
        has_data = trials or articles

        if has_data:
            if trials:
                html += f'''
<h3>臨床試驗（{len(trials)} 項）</h3>

{generate_trials_table(trials)}
'''
            if articles:
                html += f'''
<h3>相關文獻（{len(articles)} 篇）</h3>

{generate_literature_table(articles)}
'''
        else:
            # No data - concise notice
            html += '''
<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>
'''

    html += '''
</div>
</details>
'''
    return html


def regenerate_report(drug_name: str, report_path: Path) -> bool:
    """Regenerate indication content in a drug report."""
    bundle = load_drug_bundle(drug_name)
    if not bundle:
        return False

    indications = bundle.get("drug", {}).get("predicted_indications", [])
    if len(indications) <= 1:
        return False

    with open(report_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract existing content from primary indication
    existing_content = extract_primary_content(content)

    # Calculate highest evidence level
    highest_level = "L5"
    level_order = {"L1": 1, "L2": 2, "L3": 3, "L4": 4, "L5": 5}
    for indication in indications:
        ind_level = calculate_evidence_level(indication)
        if level_order.get(ind_level, 5) < level_order.get(highest_level, 5):
            highest_level = ind_level

    # Update YAML front matter
    content = re.sub(r"(evidence_level:\s*)\w+", f"\\1{highest_level}", content)

    # Build new accordion section
    accordion_html = "\n## 預測適應症詳細分析\n"
    for i, indication in enumerate(indications):
        is_primary = (i == 0)
        accordion_html += format_indication_html(
            i + 1, indication, is_primary, existing_content
        )

    # Replace existing accordion section
    patterns = [
        r"(## 預測適應症詳細分析.*?)(## 台灣上市(?:資訊|狀態|情形))",
        r"(## 為什麼這個預測合理[？?]?.*?)(## 台灣上市(?:資訊|狀態|情形))",
        r"(## 為什麼預測合理[？?]?.*?)(## 台灣上市(?:資訊|狀態|情形))",
    ]

    new_content = None
    for pattern in patterns:
        new_content, count = re.subn(
            pattern,
            accordion_html + "\n\n\\2",
            content,
            flags=re.DOTALL
        )
        if count > 0:
            break

    if new_content is None or new_content == content:
        print(f"  Could not find sections to replace in {drug_name}")
        return False

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def main():
    print("=" * 60)
    print("Regenerating Indication Content (HTML Format)")
    print("=" * 60)

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
            skipped += 1
            continue

        try:
            if regenerate_report(drug_name, report_path):
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
