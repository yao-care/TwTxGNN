#!/usr/bin/env python3
"""
批量為藥物頁面加入 AI 分析按鈕
"""

import os
import re
from pathlib import Path

DRUGS_DIR = Path(__file__).parent.parent / "docs" / "_drugs"

def add_ai_analysis(content: str) -> str:
    """在社群分享按鈕前加入 AI 分析區塊"""

    # 檢查是否已經有 ai-analysis
    if "ai-analysis" in content or "{% include ai-analysis.html %}" in content:
        return content

    # 在 "{% include social-share.html %}" 前加入
    social_pattern = r"({% include social-share\.html %})"
    replacement = r"{% include ai-analysis.html %}\n\n\1"

    if re.search(social_pattern, content):
        return re.sub(social_pattern, replacement, content, count=1)

    # 備用：在 "## 引用本報告" 前加入
    citation_pattern = r"(## 引用本報告)"
    replacement2 = r"{% include ai-analysis.html %}\n\n\1"

    if re.search(citation_pattern, content):
        return re.sub(citation_pattern, replacement2, content, count=1)

    return content

def process_all_drugs():
    """處理所有藥物頁面"""
    updated = 0
    skipped = 0
    errors = []

    drug_files = list(DRUGS_DIR.glob("*.md"))
    print(f"找到 {len(drug_files)} 個藥物檔案")

    for drug_file in drug_files:
        try:
            content = drug_file.read_text(encoding="utf-8")

            # 檢查是否已有 ai-analysis
            if "ai-analysis" in content:
                skipped += 1
                continue

            new_content = add_ai_analysis(content)

            if new_content != content:
                drug_file.write_text(new_content, encoding="utf-8")
                updated += 1
                print(f"✓ 更新: {drug_file.name}")
            else:
                skipped += 1

        except Exception as e:
            errors.append((drug_file.name, str(e)))
            print(f"✗ 錯誤: {drug_file.name} - {e}")

    print(f"\n=== 完成 ===")
    print(f"更新: {updated} 個檔案")
    print(f"略過: {skipped} 個檔案")
    print(f"錯誤: {len(errors)} 個檔案")

    return updated, skipped, errors

if __name__ == "__main__":
    process_all_drugs()
