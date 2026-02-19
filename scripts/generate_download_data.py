#!/usr/bin/env python3
"""
產生可供下載的資料摘要檔案
"""

import json
import csv
from pathlib import Path
from datetime import datetime


def load_drug_evidence():
    """從 drug pages 載入證據等級資料"""
    drugs_dir = Path(__file__).parent.parent / 'docs' / '_drugs'
    drugs = []

    for md_file in sorted(drugs_dir.glob('*.md')):
        content = md_file.read_text(encoding='utf-8')

        # 解析 front matter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                front_matter = {}
                for line in parts[1].strip().split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        front_matter[key.strip()] = value.strip().strip('"')

                drugs.append({
                    'drug_name': front_matter.get('title', ''),
                    'evidence_level': front_matter.get('evidence_level', 'L5'),
                    'indication_count': int(front_matter.get('indication_count', 0)),
                    'parent_category': front_matter.get('parent', ''),
                    'url': f"/drugs/{md_file.stem}/"
                })

    return drugs


def generate_summary_csv(drugs, output_path):
    """產生藥物摘要 CSV"""
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'drug_name', 'evidence_level', 'indication_count', 'parent_category', 'url'
        ])
        writer.writeheader()
        writer.writerows(drugs)


def generate_summary_json(drugs, output_path):
    """產生藥物摘要 JSON"""
    output = {
        'generated_at': datetime.now().isoformat(),
        'total_drugs': len(drugs),
        'evidence_distribution': {},
        'drugs': drugs
    }

    # 計算證據等級分布
    for drug in drugs:
        level = drug['evidence_level']
        output['evidence_distribution'][level] = output['evidence_distribution'].get(level, 0) + 1

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)


def generate_high_evidence_csv(drugs, output_path):
    """產生高證據等級 (L1-L2) 藥物 CSV"""
    high_evidence = [d for d in drugs if d['evidence_level'] in ['L1', 'L2']]

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'drug_name', 'evidence_level', 'indication_count', 'url'
        ])
        writer.writeheader()
        for drug in high_evidence:
            writer.writerow({
                'drug_name': drug['drug_name'],
                'evidence_level': drug['evidence_level'],
                'indication_count': drug['indication_count'],
                'url': f"https://twtxgnn.yao.care{drug['url']}"
            })


def main():
    """主程式"""
    downloads_dir = Path(__file__).parent.parent / 'docs' / 'downloads'
    downloads_dir.mkdir(exist_ok=True)

    print("載入藥物資料...")
    drugs = load_drug_evidence()
    print(f"找到 {len(drugs)} 個藥物")

    # 產生摘要 CSV
    summary_csv = downloads_dir / 'twtxgnn_drugs_summary.csv'
    generate_summary_csv(drugs, summary_csv)
    print(f"✅ 已產生: {summary_csv.name}")

    # 產生摘要 JSON
    summary_json = downloads_dir / 'twtxgnn_drugs_summary.json'
    generate_summary_json(drugs, summary_json)
    print(f"✅ 已產生: {summary_json.name}")

    # 產生高證據等級 CSV
    high_evidence_csv = downloads_dir / 'twtxgnn_high_evidence.csv'
    generate_high_evidence_csv(drugs, high_evidence_csv)
    print(f"✅ 已產生: {high_evidence_csv.name}")

    # 統計
    evidence_dist = {}
    for drug in drugs:
        level = drug['evidence_level']
        evidence_dist[level] = evidence_dist.get(level, 0) + 1

    print("\n證據等級分布:")
    for level in ['L1', 'L2', 'L3', 'L4', 'L5']:
        count = evidence_dist.get(level, 0)
        print(f"  {level}: {count} 個藥物")


if __name__ == '__main__':
    main()
