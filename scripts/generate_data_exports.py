#!/usr/bin/env python3
"""
產生 CSV 和 JSON 資料匯出檔案
"""
import json
import csv
import re
from pathlib import Path

DRUGS_DIR = Path(__file__).parent.parent / "docs" / "_drugs"
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "data"

def extract_front_matter(content: str) -> dict:
    """提取 front matter"""
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not match:
        return {}

    fm_text = match.group(1)
    fm = {}
    for line in fm_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            value = value.strip().strip('"').strip("'")
            # 嘗試轉換數字
            if value.isdigit():
                value = int(value)
            fm[key.strip()] = value
    return fm

def extract_quick_overview(content: str) -> dict:
    """從內容中提取快速總覽表格"""
    overview = {}

    # 找到快速總覽表格
    table_match = re.search(r'## 快速總覽\n\n\|[^\n]+\n\|[^\n]+\n((?:\|[^\n]+\n)+)', content)
    if table_match:
        rows = table_match.group(1).strip().split('\n')
        for row in rows:
            cols = [c.strip() for c in row.split('|')[1:-1]]
            if len(cols) >= 2:
                key = cols[0].strip()
                value = cols[1].strip()
                if key == '原適應症':
                    overview['original_indication'] = value
                elif key == '預測新適應症':
                    overview['predicted_indication'] = value
                elif key == 'TxGNN 預測分數':
                    overview['txgnn_score'] = value
                elif key == '台灣上市':
                    overview['taiwan_approved'] = '已上市' in value or '✓' in value
                elif key == '建議決策':
                    overview['decision'] = value

    return overview

def load_all_drugs() -> list:
    """載入所有藥物資料"""
    drugs = []

    for filepath in sorted(DRUGS_DIR.glob("*.md")):
        content = filepath.read_text(encoding='utf-8')
        fm = extract_front_matter(content)
        overview = extract_quick_overview(content)

        if fm:
            drug = {
                'slug': filepath.stem,
                'name': fm.get('title', filepath.stem),
                'evidence_level': fm.get('evidence_level', 'L5'),
                'indication_count': fm.get('indication_count', 0),
                'original_indication': overview.get('original_indication', ''),
                'predicted_indication': overview.get('predicted_indication', ''),
                'txgnn_score': overview.get('txgnn_score', ''),
                'taiwan_approved': overview.get('taiwan_approved', False),
                'decision': overview.get('decision', ''),
                'url': f'/drugs/{filepath.stem}/'
            }
            drugs.append(drug)

    return drugs

def generate_json(drugs: list, output_path: Path):
    """產生 JSON 檔案"""
    output = {
        'generated': '2026-02-19',
        'total_count': len(drugs),
        'source': 'TwTxGNN - https://twtxgnn.yao.care/',
        'drugs': drugs
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"  JSON: {output_path} ({len(drugs)} 筆)")

def generate_csv(drugs: list, output_path: Path):
    """產生 CSV 檔案"""
    fieldnames = [
        'name', 'slug', 'evidence_level', 'indication_count',
        'original_indication', 'predicted_indication', 'txgnn_score',
        'taiwan_approved', 'decision', 'url'
    ]

    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(drugs)

    print(f"  CSV: {output_path} ({len(drugs)} 筆)")

def generate_summary_by_level(drugs: list, output_path: Path):
    """產生按證據等級分組的 JSON"""
    by_level = {}
    for drug in drugs:
        level = drug['evidence_level']
        if level not in by_level:
            by_level[level] = []
        by_level[level].append({
            'name': drug['name'],
            'slug': drug['slug'],
            'decision': drug['decision'],
            'indication_count': drug['indication_count']
        })

    output = {
        'generated': '2026-02-19',
        'source': 'TwTxGNN - https://twtxgnn.yao.care/',
        'summary': {
            level: {
                'count': len(items),
                'drugs': items
            }
            for level, items in sorted(by_level.items())
        }
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"  Summary JSON: {output_path}")

def main():
    """主函數"""
    # 建立輸出目錄
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("載入藥物資料...")
    drugs = load_all_drugs()
    print(f"  共 {len(drugs)} 個藥物\n")

    print("產生匯出檔案...")
    generate_json(drugs, OUTPUT_DIR / "drugs.json")
    generate_csv(drugs, OUTPUT_DIR / "drugs.csv")
    generate_summary_by_level(drugs, OUTPUT_DIR / "drugs-by-level.json")

    print("\n完成！")

if __name__ == "__main__":
    main()
