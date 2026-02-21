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
    """Generate Chinese description based on key information."""
    desc_lower = description.lower()

    parts = []

    # 1. Determine the main action/recommendation
    if "contraindicated" in desc_lower:
        parts.append("本藥物在此情況下禁用")
    elif "should not be used" in desc_lower or "should not be treated" in desc_lower:
        parts.append("不應使用本藥物")
    elif "should be avoided" in desc_lower:
        parts.append("應避免使用本藥物")
    elif "not recommended" in desc_lower:
        parts.append("不建議使用本藥物")
    elif "caution" in desc_lower:
        parts.append("應謹慎使用本藥物")

    # 2. Check for specific requirements
    requirements = []
    if "monitor" in desc_lower:
        if "closely" in desc_lower:
            requirements.append("需密切監測")
        else:
            requirements.append("需定期監測")

    if "dose adjustment" in desc_lower or "dosage adjustment" in desc_lower:
        if "no dose adjustment" in desc_lower or "not necessary" in desc_lower:
            requirements.append("通常無需調整劑量")
        else:
            requirements.append("可能需要調整劑量")
    elif "dose reduction" in desc_lower or "lower dose" in desc_lower or "reduced dose" in desc_lower:
        requirements.append("可能需要降低劑量")

    if requirements:
        parts.extend(requirements)

    # 3. Check for specific risks
    risks = []
    if "hepatotoxicity" in desc_lower:
        risks.append("肝毒性")
    if "nephrotoxicity" in desc_lower:
        risks.append("腎毒性")
    if "cardiotoxicity" in desc_lower:
        risks.append("心臟毒性")
    if "neurotoxicity" in desc_lower:
        risks.append("神經毒性")
    if "myelosuppression" in desc_lower or "bone marrow" in desc_lower:
        risks.append("骨髓抑制")
    if "bleeding" in desc_lower or "hemorrhage" in desc_lower:
        risks.append("出血")
    if "hypoglycemia" in desc_lower:
        risks.append("低血糖")
    if "hyperglycemia" in desc_lower:
        risks.append("高血糖")
    if "hypotension" in desc_lower:
        risks.append("低血壓")
    if "hypertension" in desc_lower and "uncontrolled" in desc_lower:
        risks.append("血壓控制不良")
    if "qt prolongation" in desc_lower or "arrhythmia" in desc_lower:
        risks.append("心律不整")
    if "seizure" in desc_lower:
        risks.append("癲癇發作")
    if "infection" in desc_lower:
        risks.append("感染")
    if "thrombosis" in desc_lower or "thrombo" in desc_lower:
        risks.append("血栓")
    if "anemia" in desc_lower:
        risks.append("貧血")

    if risks:
        parts.append("風險包括：" + "、".join(risks))

    # 4. Check severity
    if "fatal" in desc_lower or "death" in desc_lower:
        parts.append("可能有致命風險")
    elif "life-threatening" in desc_lower:
        parts.append("可能危及生命")
    elif "serious" in desc_lower or "severe" in desc_lower:
        parts.append("可能有嚴重不良反應")

    # 5. Special populations
    populations = []
    if "elderly" in desc_lower:
        populations.append("老年人")
    if "pediatric" in desc_lower or "children" in desc_lower:
        populations.append("兒童")
    if "pregnan" in desc_lower:
        populations.append("孕婦")
    if "breast-feeding" in desc_lower or "nursing" in desc_lower or "lactation" in desc_lower:
        populations.append("哺乳婦女")
    if "renal impairment" in desc_lower or "kidney" in desc_lower:
        if "severe renal" in desc_lower:
            populations.append("嚴重腎功能不全者")
        elif "mild renal" in desc_lower:
            populations.append("輕度腎功能不全者")
        elif "moderate renal" in desc_lower:
            populations.append("中度腎功能不全者")
    if "hepatic impairment" in desc_lower or "liver" in desc_lower:
        if "severe hepatic" in desc_lower:
            populations.append("嚴重肝功能不全者")
        elif "mild hepatic" in desc_lower:
            populations.append("輕度肝功能不全者")
        elif "moderate hepatic" in desc_lower:
            populations.append("中度肝功能不全者")

    if populations and not any("功能不全" in p for p in populations):
        parts.append("特別注意族群：" + "、".join(populations))

    # 6. Therapy recommendations
    if "discontinue" in desc_lower or "withhold" in desc_lower:
        if "symptoms" in desc_lower or "signs" in desc_lower:
            parts.append("出現症狀時應考慮停藥")
        else:
            parts.append("必要時應停止治療")

    # Build final result
    if parts:
        result = "。".join(parts) + "。"
    else:
        # Fallback: extract first sentence and key info
        first_sentence = description.split('.')[0] if '.' in description else description[:150]
        result = f"注意事項：{first_sentence[:150]}..."

    return result


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
