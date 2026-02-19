#!/usr/bin/env python3
"""
批次為藥物報告加入相關藥物推薦
基於相同證據等級推薦相關藥物
"""
import os
import re
import random
from pathlib import Path
from collections import defaultdict

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

def load_all_drugs() -> dict:
    """載入所有藥物資訊並按證據等級分組"""
    drugs_by_level = defaultdict(list)

    for filepath in DRUGS_DIR.glob("*.md"):
        content = filepath.read_text(encoding='utf-8')
        fm, _ = extract_front_matter(content)
        if fm:
            level = fm.get('evidence_level', 'L5')
            title = fm.get('title', filepath.stem)
            drugs_by_level[level].append({
                'slug': filepath.stem,
                'title': title,
                'level': level
            })

    return drugs_by_level

def get_related_drugs(current_slug: str, current_level: str, drugs_by_level: dict, count: int = 5) -> list:
    """取得相關藥物推薦"""
    same_level_drugs = [d for d in drugs_by_level.get(current_level, []) if d['slug'] != current_slug]

    # 如果同等級藥物不足，從相鄰等級補充
    if len(same_level_drugs) < count:
        adjacent_levels = {
            'L1': ['L2'],
            'L2': ['L1', 'L3'],
            'L3': ['L2', 'L4'],
            'L4': ['L3', 'L5'],
            'L5': ['L4']
        }
        for adj_level in adjacent_levels.get(current_level, []):
            same_level_drugs.extend([d for d in drugs_by_level.get(adj_level, []) if d['slug'] != current_slug])

    # 隨機選擇
    random.seed(hash(current_slug))  # 使結果可重複
    selected = random.sample(same_level_drugs, min(count, len(same_level_drugs)))

    return selected

def generate_related_section(related_drugs: list) -> str:
    """產生相關藥物區塊 HTML"""
    if not related_drugs:
        return ""

    items = []
    for drug in related_drugs:
        items.append(f'- [{drug["title"]}]({{{{ "/drugs/{drug["slug"]}/" | relative_url }}}}) - 證據等級 {drug["level"]}')

    return f'''

---

## 相關藥物報告

{chr(10).join(items)}
'''

def update_drug_file(filepath: Path, drugs_by_level: dict) -> bool:
    """更新單一藥物檔案，加入相關藥物推薦"""
    content = filepath.read_text(encoding='utf-8')

    # 檢查是否已有相關藥物區塊
    if '## 相關藥物報告' in content:
        return False

    fm, body = extract_front_matter(content)
    if not fm:
        print(f"  跳過 {filepath.name}: 無法解析 front matter")
        return False

    current_slug = filepath.stem
    current_level = fm.get('evidence_level', 'L5')

    # 取得相關藥物
    related_drugs = get_related_drugs(current_slug, current_level, drugs_by_level)
    related_section = generate_related_section(related_drugs)

    if not related_section:
        return False

    # 在引用區塊之前插入相關藥物
    # 找到 "## 引用本報告" 的位置
    citation_pattern = r'\n---\n\n## 引用本報告'
    if re.search(citation_pattern, content):
        new_content = re.sub(citation_pattern, related_section + '\n---\n\n## 引用本報告', content)
    else:
        # 如果沒有引用區塊，在最後加入
        new_content = content.rstrip() + related_section

    filepath.write_text(new_content, encoding='utf-8')
    return True

def main():
    """主函數"""
    if not DRUGS_DIR.exists():
        print(f"錯誤：找不到目錄 {DRUGS_DIR}")
        return

    # 載入所有藥物
    print("載入藥物資訊...")
    drugs_by_level = load_all_drugs()

    for level, drugs in sorted(drugs_by_level.items()):
        print(f"  {level}: {len(drugs)} 個藥物")

    drug_files = list(DRUGS_DIR.glob("*.md"))
    print(f"\n開始處理 {len(drug_files)} 個藥物報告...")

    updated = 0
    for filepath in sorted(drug_files):
        if update_drug_file(filepath, drugs_by_level):
            updated += 1
            print(f"  已更新: {filepath.name}")

    print(f"\n完成！共更新 {updated} 個檔案")

if __name__ == "__main__":
    main()
