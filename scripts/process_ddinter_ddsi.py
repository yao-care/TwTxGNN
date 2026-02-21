#!/usr/bin/env python3
"""
Process DDInter 2.0 DDSI (Drug-Disease/Syndrome Interaction) data and integrate into drug reports.

This script:
1. Downloads DDSI data from DDInter 2.0 API
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
DDSI_RAW_FILE = PROJECT_ROOT / "data" / "external" / "ddsi" / "ddinter2_ddsi_raw.json"
DDSI_PROCESSED_FILE = PROJECT_ROOT / "data" / "external" / "ddsi" / "ddinter2_ddsi_processed.json"
DRUG_LIST_FILE = SCRIPT_DIR / "drug_list.json"

# DDInter API endpoint
DDINTER_DDSI_API = "https://ddinter2.scbdd.com/server/disease-interaction-source/"


def download_ddsi_data():
    """Download DDSI data from DDInter 2.0 API."""
    print("Downloading DDSI data from DDInter 2.0...")

    # First get total count
    result = subprocess.run(
        ["curl", "-sS", DDINTER_DDSI_API, "-X", "POST", "-d", "draw=1&start=0&length=1"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"Error downloading data: {result.stderr}")
        return None

    initial_data = json.loads(result.stdout)
    total = initial_data['recordsTotal']
    print(f"Total DDSI records: {total}")

    # Download all records in batches
    all_data = []
    batch_size = 1000
    for start in range(0, total, batch_size):
        print(f"  Downloading {start} - {min(start + batch_size, total)}...")
        result = subprocess.run(
            ["curl", "-sS", DDINTER_DDSI_API, "-X", "POST", "-d", f"draw=1&start={start}&length={batch_size}"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            batch_data = json.loads(result.stdout)
            all_data.extend(batch_data['data'])

    data = {
        "recordsTotal": total,
        "recordsFiltered": total,
        "data": all_data
    }
    print(f"Downloaded {len(all_data)} DDSI records")

    # Save raw data
    DDSI_RAW_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DDSI_RAW_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return data


def load_ddsi_data() -> Optional[dict]:
    """Load DDSI data from file or download if not exists."""
    if DDSI_RAW_FILE.exists():
        with open(DDSI_RAW_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return download_ddsi_data()


def process_ddsi_data(ddsi_data: dict, drug_list: dict) -> dict:
    """Process DDSI data and match with our drugs."""
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
            "total_records": ddsi_data["recordsTotal"],
            "license": "CC BY-NC-SA 4.0"
        },
        "interactions": {}
    }

    for item in ddsi_data["data"]:
        drug_name_lower = item["drugName"].lower()

        if drug_name_lower in our_drugs:
            canonical_name = our_drugs[drug_name_lower]

            if canonical_name not in processed["interactions"]:
                processed["interactions"][canonical_name] = []

            processed["interactions"][canonical_name].append({
                "disease": item["diseaseName"],
                "disease_zh": translate_disease(item["diseaseName"]),
                "severity": level_map.get(item["level"], "Unknown"),
                "description": item.get("text", ""),
                "references": item.get("references", "")
            })

    # Save processed data
    with open(DDSI_PROCESSED_FILE, "w", encoding="utf-8") as f:
        json.dump(processed, f, ensure_ascii=False, indent=2)

    return processed


def translate_disease(disease_name: str) -> str:
    """Translate common disease names to Chinese."""
    translations = {
        "liver diseases": "肝臟疾病",
        "kidney diseases": "腎臟疾病",
        "cardiovascular diseases": "心血管疾病",
        "heart failure": "心臟衰竭",
        "hypertension": "高血壓",
        "hypotension": "低血壓",
        "diabetes mellitus": "糖尿病",
        "seizure disorders": "癲癇",
        "epilepsy": "癲癇",
        "asthma": "氣喘",
        "copd": "慢性阻塞性肺病",
        "glaucoma": "青光眼",
        "thyroid disorders": "甲狀腺疾病",
        "hyperthyroidism": "甲狀腺機能亢進",
        "hypothyroidism": "甲狀腺機能低下",
        "bleeding disorders": "出血性疾病",
        "peptic ulcer": "消化性潰瘍",
        "gastrointestinal bleeding": "胃腸道出血",
        "renal impairment": "腎功能不全",
        "hepatic impairment": "肝功能不全",
        "pregnancy": "懷孕",
        "breast-feeding": "哺乳",
        "depression": "憂鬱症",
        "bipolar disorder": "躁鬱症",
        "psychosis": "精神病",
        "parkinson's disease": "帕金森氏症",
        "myasthenia gravis": "重症肌無力",
        "porphyria": "紫質症",
        "g6pd deficiency": "G6PD 缺乏症",
        "hyperparathyroidism": "副甲狀腺機能亢進",
        "osteoporosis": "骨質疏鬆症",
        "prostatic hyperplasia": "前列腺肥大",
        "urinary retention": "尿滯留",
        "angle-closure glaucoma": "隅角閉鎖性青光眼",
        "qt prolongation": "QT 間期延長",
        "arrhythmias": "心律不整",
        "bradycardia": "心搏過緩",
        "tachycardia": "心搏過速"
    }
    return translations.get(disease_name.lower(), disease_name)


def format_severity_badge(severity: str) -> str:
    """Format severity as a badge."""
    badges = {
        "Major": "🔴 Major",
        "Moderate": "🟡 Moderate",
        "Minor": "🟢 Minor"
    }
    return badges.get(severity, f"⚪ {severity}")


def translate_description(description: str) -> str:
    """Translate DDSI description to Traditional Chinese summary."""
    # Key phrase translations for medical content
    translations = {
        # Actions/Recommendations
        "should be administered cautiously": "應謹慎使用",
        "is contraindicated": "為禁忌",
        "are contraindicated": "為禁忌",
        "is not recommended": "不建議使用",
        "should be avoided": "應避免使用",
        "should be used with caution": "應謹慎使用",
        "use with caution": "謹慎使用",
        "caution is advised": "建議謹慎",
        "caution is recommended": "建議謹慎",
        "should be monitored": "應監測",
        "monitor patients": "監測病患",
        "monitoring is recommended": "建議監測",
        "dose adjustment": "劑量調整",
        "dosage adjustment": "劑量調整",
        "dose reduction": "減少劑量",
        "lower doses": "較低劑量",
        "therapy should be discontinued": "應停止治療",
        "therapy should be withheld": "應暫停治療",
        "withhold treatment": "暫停治療",
        "discontinue": "停用",

        # Conditions
        "hepatic impairment": "肝功能不全",
        "renal impairment": "腎功能不全",
        "liver disease": "肝臟疾病",
        "kidney disease": "腎臟疾病",
        "cardiovascular disease": "心血管疾病",
        "heart failure": "心臟衰竭",
        "hypertension": "高血壓",
        "hypotension": "低血壓",
        "diabetes": "糖尿病",
        "seizures": "癲癇發作",
        "bleeding": "出血",
        "hemorrhage": "出血",
        "infection": "感染",
        "pregnancy": "懷孕",
        "breast-feeding": "哺乳",
        "elderly": "老年人",
        "pediatric": "兒童",

        # Effects
        "may increase": "可能增加",
        "may decrease": "可能降低",
        "may cause": "可能導致",
        "may result in": "可能導致",
        "may exacerbate": "可能加重",
        "may worsen": "可能惡化",
        "increased risk": "風險增加",
        "risk of": "...的風險",
        "adverse effects": "不良反應",
        "side effects": "副作用",
        "toxicity": "毒性",
        "hepatotoxicity": "肝毒性",
        "nephrotoxicity": "腎毒性",
        "cardiotoxicity": "心臟毒性",

        # Severity
        "fatal": "致命",
        "severe": "嚴重",
        "serious": "嚴重",
        "life-threatening": "危及生命",
    }

    # Create Chinese summary
    summary_parts = []
    desc_lower = description.lower()

    # Check for contraindication
    if "contraindicated" in desc_lower:
        summary_parts.append("此情況下為禁忌")
    elif "should be avoided" in desc_lower:
        summary_parts.append("應避免使用")
    elif "not recommended" in desc_lower:
        summary_parts.append("不建議使用")
    elif "caution" in desc_lower:
        summary_parts.append("應謹慎使用")

    # Check for monitoring
    if "monitor" in desc_lower:
        summary_parts.append("需密切監測")

    # Check for dose adjustment
    if "dose adjustment" in desc_lower or "dosage adjustment" in desc_lower:
        summary_parts.append("可能需調整劑量")
    elif "dose reduction" in desc_lower or "lower dose" in desc_lower:
        summary_parts.append("可能需降低劑量")

    # Check for specific risks
    if "hepatotoxicity" in desc_lower or "liver" in desc_lower:
        if "hepatotoxicity" in desc_lower:
            summary_parts.append("有肝毒性風險")
    if "nephrotoxicity" in desc_lower:
        summary_parts.append("有腎毒性風險")
    if "bleeding" in desc_lower or "hemorrhage" in desc_lower:
        summary_parts.append("有出血風險")
    if "hypoglycemia" in desc_lower:
        summary_parts.append("有低血糖風險")
    if "hyperglycemia" in desc_lower:
        summary_parts.append("有高血糖風險")
    if "fatal" in desc_lower or "death" in desc_lower:
        summary_parts.append("可能有致命風險")

    if summary_parts:
        return "；".join(summary_parts) + "。"
    else:
        return "請參閱 DDInter 2.0 了解詳情。"


def format_ddsi_section(interactions: list) -> str:
    """Format DDSI interactions as markdown."""
    lines = ["### 藥物-疾病注意事項 (DDSI)", ""]
    lines.append('<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>')
    lines.append("")

    # Sort by severity (Major first)
    severity_order = {"Major": 0, "Moderate": 1, "Minor": 2, "Unknown": 3}
    sorted_interactions = sorted(interactions, key=lambda x: severity_order.get(x["severity"], 3))

    # Show ALL interactions (no limit)
    for i in sorted_interactions:
        disease_display = i['disease_zh'] if i['disease_zh'] != i['disease'] else i['disease']

        lines.append(f"**{disease_display}** {format_severity_badge(i['severity'])}")

        # Translate description to Chinese summary
        chinese_summary = translate_description(i['description'])
        lines.append(f"- {chinese_summary}")
        lines.append("")

    return "\n".join(lines)


def update_report(report_path: Path, drug_name: str, interactions: list) -> bool:
    """Update a drug report with DDSI information."""
    if not interactions:
        return False

    # Read report
    with open(report_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove old DDSI section if exists
    if "藥物-疾病注意事項 (DDSI)" in content:
        # Pattern to match DDSI section until next section or conclusion
        ddsi_pattern = r"### 藥物-疾病注意事項 \(DDSI\).*?(?=\n### |\n## 結論與下一步)"
        content = re.sub(ddsi_pattern, "", content, flags=re.DOTALL)
        # Clean up extra newlines
        content = re.sub(r"\n{3,}", "\n\n", content)

    # Format new DDSI section
    new_section = format_ddsi_section(interactions)

    # Find the right place to insert DDSI
    # Priority: after DHI, after DFI, after DDI, before conclusion
    if "### 藥物-草藥交互作用 (DHI)" in content:
        # Insert after DHI section
        dhi_pattern = r"(### 藥物-草藥交互作用 \(DHI\).*?)(\n## 結論與下一步)"
        match = re.search(dhi_pattern, content, re.DOTALL)
        if match:
            content = content[:match.end(1)] + f"\n\n{new_section}" + content[match.start(2):]
    elif "### 藥物-食物交互作用 (DFI)" in content:
        # Insert after DFI section
        dfi_pattern = r"(### 藥物-食物交互作用 \(DFI\).*?)(\n### 藥物-草藥|\n## 結論與下一步)"
        match = re.search(dfi_pattern, content, re.DOTALL)
        if match:
            content = content[:match.end(1)] + f"\n\n{new_section}" + content[match.start(2):]
    else:
        # Insert before conclusion
        safety_pattern = r"(## 安全性考量\s*\n.*?)(\n## 結論與下一步)"
        match = re.search(safety_pattern, content, re.DOTALL)
        if match:
            content = content[:match.end(1)] + f"\n\n{new_section}" + content[match.start(2):]
        else:
            return False

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def main():
    print("=" * 60)
    print("Processing DDInter 2.0 DDSI Data")
    print("=" * 60)

    # Load DDSI data (download if needed)
    ddsi_data = download_ddsi_data()  # Force download to get latest
    if not ddsi_data:
        print("Failed to load DDSI data")
        return

    # Load drug list
    with open(DRUG_LIST_FILE, "r", encoding="utf-8") as f:
        drug_list = json.load(f)

    # Process data
    processed = process_ddsi_data(ddsi_data, drug_list)

    print(f"\nMatched {len(processed['interactions'])} drugs with DDSI data")

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
            print(f"  Updated: {drug_name} ({len(interactions)} disease interactions)")
            updated += 1

    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"  Total drugs with DDSI: {len(processed['interactions'])}")
    print(f"  Reports updated: {updated}")


if __name__ == "__main__":
    main()
