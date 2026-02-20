#!/usr/bin/env python3
"""
批量為藥物頁面加入社群分享按鈕
"""

import os
import re
from pathlib import Path

DRUGS_DIR = Path(__file__).parent.parent / "docs" / "_drugs"

def add_social_share(content: str) -> str:
    """在引用區塊前加入社群分享按鈕"""

    # 檢查是否已經有 social-share
    if "social-share" in content or "{% include social-share.html %}" in content:
        return content

    # 在 "## 引用本報告" 前加入
    citation_pattern = r"(---\s*\n\n## 引用本報告)"
    replacement = r"---\n\n{% include social-share.html %}\n\n## 引用本報告"

    if re.search(citation_pattern, content):
        return re.sub(citation_pattern, replacement, content)

    # 備用：在 "## 引用本報告" 前加入（沒有前置 ---）
    citation_pattern2 = r"(\n## 引用本報告)"
    replacement2 = r"\n{% include social-share.html %}\n\n## 引用本報告"

    if re.search(citation_pattern2, content):
        return re.sub(citation_pattern2, replacement2, content, count=1)

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

            # 檢查是否已有 social-share
            if "social-share" in content:
                skipped += 1
                continue

            new_content = add_social_share(content)

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
