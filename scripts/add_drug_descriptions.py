#!/usr/bin/env python3
"""
批次為藥物報告加入 Meta Description
"""
import os
import re
from pathlib import Path

DRUGS_DIR = Path(__file__).parent.parent / "docs" / "_drugs"

def extract_front_matter(content: str) -> tuple[dict, str]:
    """提取 front matter 和內容"""
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not match:
        return {}, content

    fm_text = match.group(1)
    body = match.group(2)

    # 簡單解析 YAML
    fm = {}
    for line in fm_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            fm[key.strip()] = value.strip().strip('"').strip("'")

    return fm, body

def generate_description(title: str, evidence_level: str, indication_count: str) -> str:
    """產生藥物報告的 description"""
    count = int(indication_count) if indication_count.isdigit() else 0

    level_map = {
        'L1': '最高證據等級 L1',
        'L2': '高證據等級 L2',
        'L3': '中等證據等級 L3',
        'L4': '初步證據等級 L4',
        'L5': '模型預測等級 L5'
    }

    level_desc = level_map.get(evidence_level, f'證據等級 {evidence_level}')

    if count > 0:
        return f"{title} 的老藥新用潛力分析。{level_desc}，包含 {count} 個預測適應症。查看 AI 預測與臨床證據完整報告。"
    else:
        return f"{title} 的老藥新用潛力分析。{level_desc}。查看 AI 預測與臨床證據完整報告。"

def update_drug_file(filepath: Path) -> bool:
    """更新單一藥物檔案，加入 description"""
    content = filepath.read_text(encoding='utf-8')
    fm, body = extract_front_matter(content)

    if not fm:
        print(f"  跳過 {filepath.name}: 無法解析 front matter")
        return False

    # 檢查是否已有 description
    if 'description' in fm:
        print(f"  跳過 {filepath.name}: 已有 description")
        return False

    title = fm.get('title', filepath.stem)
    evidence_level = fm.get('evidence_level', 'L5')
    indication_count = fm.get('indication_count', '0')

    description = generate_description(title, evidence_level, indication_count)

    # 重建 front matter
    new_fm_lines = ['---']
    for line in content.split('---')[1].strip().split('\n'):
        new_fm_lines.append(line)
        # 在 title 後面加入 description
        if line.startswith('title:'):
            new_fm_lines.append(f'description: "{description}"')
    new_fm_lines.append('---')

    new_content = '\n'.join(new_fm_lines) + '\n' + body
    filepath.write_text(new_content, encoding='utf-8')
    return True

def main():
    """主函數"""
    if not DRUGS_DIR.exists():
        print(f"錯誤：找不到目錄 {DRUGS_DIR}")
        return

    drug_files = list(DRUGS_DIR.glob("*.md"))
    print(f"找到 {len(drug_files)} 個藥物報告")

    updated = 0
    for filepath in sorted(drug_files):
        if update_drug_file(filepath):
            updated += 1
            print(f"  已更新: {filepath.name}")

    print(f"\n完成！共更新 {updated} 個檔案")

if __name__ == "__main__":
    main()
