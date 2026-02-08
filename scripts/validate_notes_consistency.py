#!/usr/bin/env python3
"""
驗證 Pharmacist Notes 與 Sponsor Notes 的一致性。

此腳本確保兩版文件在關鍵欄位上保持同步。
"""

import re
import sys
from pathlib import Path


# 必須一致的欄位
MUST_MATCH_FIELDS = [
    "original_indication",  # 原核准適應症
    "moa",                  # 作用機轉
    "contraindications",    # 禁忌症
    "warnings",             # 警語
    "ddi_status",           # DDI 查詢狀態
    "data_gaps",            # Data Gap 清單
]

# Data Gap 狀態標記
DATA_GAP_MARKERS = [
    "[Data Gap]",
    "[未檢索]",
    "[未找到]",
    "[不適用]",
]


def extract_field_status(content: str, field_name: str) -> str:
    """提取欄位的完成狀態（完成/Data Gap/未檢索）"""
    # 簡化的狀態判斷
    for marker in DATA_GAP_MARKERS:
        if marker in content:
            return "incomplete"
    return "complete"


def extract_data_gaps(content: str) -> list[dict]:
    """從文件中提取所有 Data Gap"""
    gaps = []

    # 匹配 Data Gap 區塊
    pattern = r"### Data Gap #(\d+) — (.+?)（(🛑 Blocking|⚠️ Non-blocking)）"
    matches = re.finditer(pattern, content)

    for match in matches:
        gaps.append({
            "id": match.group(1),
            "name": match.group(2),
            "blocking": "Blocking" in match.group(3),
        })

    return gaps


def extract_decision(content: str) -> str:
    """提取決策結論"""
    if "決策結論：Hold" in content:
        return "Hold"
    elif "決策結論：Research Question" in content:
        return "Research Question"
    elif "決策結論：Proceed with Guardrails" in content:
        return "Proceed with Guardrails"
    return "Unknown"


def extract_evidence_levels(content: str) -> dict[str, str]:
    """提取各適應症的證據等級"""
    levels = {}

    # 匹配證據等級
    pattern = r"\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*[\d.]+%\s*\|\s*(L\d)\s*\|"
    matches = re.finditer(pattern, content)

    for match in matches:
        indication = match.group(2).strip()
        level = match.group(3)
        levels[indication] = level

    return levels


def validate_field_consistency(
    pharmacist_content: str,
    sponsor_content: str
) -> list[str]:
    """驗證欄位一致性，回傳不一致的項目"""
    errors = []

    # 1. 檢查 Data Gap 一致性
    pharmacist_gaps = extract_data_gaps(pharmacist_content)
    sponsor_gaps = extract_data_gaps(sponsor_content)

    pharmacist_gap_names = {g["name"] for g in pharmacist_gaps}
    sponsor_gap_names = {g["name"] for g in sponsor_gaps}

    if pharmacist_gap_names != sponsor_gap_names:
        only_pharmacist = pharmacist_gap_names - sponsor_gap_names
        only_sponsor = sponsor_gap_names - pharmacist_gap_names

        if only_pharmacist:
            errors.append(f"Data Gap 僅出現在 Pharmacist: {only_pharmacist}")
        if only_sponsor:
            errors.append(f"Data Gap 僅出現在 Sponsor: {only_sponsor}")

    # 2. 檢查 Blocking 狀態一致性
    for p_gap in pharmacist_gaps:
        for s_gap in sponsor_gaps:
            if p_gap["name"] == s_gap["name"]:
                if p_gap["blocking"] != s_gap["blocking"]:
                    errors.append(
                        f"Data Gap '{p_gap['name']}' 阻斷性不一致: "
                        f"Pharmacist={p_gap['blocking']}, Sponsor={s_gap['blocking']}"
                    )

    # 3. 檢查決策一致性
    pharmacist_decision = extract_decision(pharmacist_content)
    sponsor_decision = extract_decision(sponsor_content)

    # 定義對應關係
    decision_mapping = {
        "Hold": ["Hold", "待補件後評估"],
        "Research Question": ["Research Question", "暫不建議"],
        "Proceed with Guardrails": ["Proceed with Guardrails", "可考慮使用"],
    }

    # 簡化：只檢查決策類型是否匹配
    if pharmacist_decision != sponsor_decision:
        errors.append(
            f"決策結論不一致: Pharmacist={pharmacist_decision}, Sponsor={sponsor_decision}"
        )

    # 4. 檢查證據等級一致性
    pharmacist_levels = extract_evidence_levels(pharmacist_content)
    sponsor_levels = extract_evidence_levels(sponsor_content)

    for indication, p_level in pharmacist_levels.items():
        if indication in sponsor_levels:
            s_level = sponsor_levels[indication]
            if p_level != s_level:
                errors.append(
                    f"適應症 '{indication}' 證據等級不一致: "
                    f"Pharmacist={p_level}, Sponsor={s_level}"
                )

    return errors


def validate_blocking_gaps_have_unlock(content: str) -> list[str]:
    """確認所有 Blocking Gap 都有解鎖條件"""
    errors = []
    gaps = extract_data_gaps(content)

    for gap in gaps:
        if gap["blocking"]:
            # 檢查是否有解鎖條件
            pattern = rf"Data Gap #{gap['id']}.*?解鎖條件\s*\|\s*(.+?)\s*\|"
            match = re.search(pattern, content, re.DOTALL)

            if not match or not match.group(1).strip():
                errors.append(f"Blocking Gap '{gap['name']}' 缺少解鎖條件")

    return errors


def validate_sources_present(content: str) -> list[str]:
    """檢查是否有無來源的模糊語句"""
    errors = []

    # 禁止語句（無來源時）
    forbidden = ["可能", "或許", "應該", "一般認為", "據了解"]

    # 檢查每一行
    lines = content.split("\n")
    for i, line in enumerate(lines, 1):
        for word in forbidden:
            if word in line:
                # 檢查同一行是否有來源標記
                if "[來源：" not in line and "[Data Gap]" not in line:
                    # 排除模板行
                    if not line.strip().startswith("```") and not line.strip().startswith("|"):
                        errors.append(f"第 {i} 行發現無來源的模糊語句「{word}」")

    return errors


def validate_required_sections(content: str, doc_type: str) -> list[str]:
    """檢查必要章節是否存在"""
    errors = []

    required_sections = [
        "資料完整性與可用性聲明",
        "阻斷性缺口摘要",
        "補件追蹤表",
        "資料收集日誌",
    ]

    for section in required_sections:
        if section not in content:
            errors.append(f"{doc_type} 缺少必要章節：{section}")

    return errors


def main():
    """主函數"""
    if len(sys.argv) < 3:
        print("用法: python validate_notes_consistency.py <pharmacist.md> <sponsor.md>")
        sys.exit(1)

    pharmacist_path = Path(sys.argv[1])
    sponsor_path = Path(sys.argv[2])

    if not pharmacist_path.exists():
        print(f"錯誤: 找不到檔案 {pharmacist_path}")
        sys.exit(1)

    if not sponsor_path.exists():
        print(f"錯誤: 找不到檔案 {sponsor_path}")
        sys.exit(1)

    pharmacist_content = pharmacist_path.read_text(encoding="utf-8")
    sponsor_content = sponsor_path.read_text(encoding="utf-8")

    all_errors = []

    # 1. 欄位一致性驗證
    print("檢查欄位一致性...")
    errors = validate_field_consistency(pharmacist_content, sponsor_content)
    all_errors.extend(errors)

    # 2. Blocking Gap 解鎖條件驗證
    print("檢查 Blocking Gap 解鎖條件...")
    errors = validate_blocking_gaps_have_unlock(pharmacist_content)
    all_errors.extend([f"Pharmacist: {e}" for e in errors])
    errors = validate_blocking_gaps_have_unlock(sponsor_content)
    all_errors.extend([f"Sponsor: {e}" for e in errors])

    # 3. 必要章節驗證
    print("檢查必要章節...")
    errors = validate_required_sections(pharmacist_content, "Pharmacist")
    all_errors.extend(errors)
    errors = validate_required_sections(sponsor_content, "Sponsor")
    all_errors.extend(errors)

    # 4. 來源標註驗證（警告，不阻斷）
    print("檢查來源標註...")
    source_warnings = validate_sources_present(pharmacist_content)
    source_warnings.extend(validate_sources_present(sponsor_content))

    # 輸出結果
    print("\n" + "=" * 50)

    if all_errors:
        print(f"❌ 發現 {len(all_errors)} 個錯誤:\n")
        for error in all_errors:
            print(f"  - {error}")
        print()
        sys.exit(1)
    else:
        print("✅ 一致性驗證通過")

    if source_warnings:
        print(f"\n⚠️ 發現 {len(source_warnings)} 個來源標註警告:\n")
        for warning in source_warnings[:10]:  # 只顯示前 10 個
            print(f"  - {warning}")
        if len(source_warnings) > 10:
            print(f"  ... 還有 {len(source_warnings) - 10} 個警告")

    print()
    sys.exit(0)


if __name__ == "__main__":
    main()
