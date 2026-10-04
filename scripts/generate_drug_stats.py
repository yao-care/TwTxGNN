#!/usr/bin/env python3
"""產生 docs/_data/drug_stats.json（首頁 D3 圖表資料，見 docs/_includes/d3-charts.html）。

2026-10-04 建：之前這份檔只有 docs/sop/chart-data-maintenance.md 裡的手動片段在更新，
停在 191 個藥、等級也是舊的。改成一律從 docs/_drugs/*.md 重算：
  level             ＝ 頁首 front matter evidence_level（由產線依快速總覽重算，
                       src/twtxgnn/regulatory/page_format.py）
  indication_count  ＝ front matter indication_count
  nct_count         ＝ 頁面上不重複的 NCT 編號數
  prediction_score  ＝ 0（沿用既有欄位；圖表未使用）
排序：indication_count 由多到少、同數依 slug；top_by_indications 取前 20。
用法：python3 scripts/generate_drug_stats.py（可重複執行，結果相同）
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRUGS = ROOT / "docs" / "_drugs"
OUT = ROOT / "docs" / "_data" / "drug_stats.json"


def front(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    meta = {}
    for line in (m.group(1).splitlines() if m else []):
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta


def main():
    drugs = []
    for p in sorted(DRUGS.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        fm = front(text)
        if fm.get("search_exclude", "").lower() == "true":
            continue
        drugs.append({
            "name": fm.get("title", p.stem),
            "slug": p.stem,
            "level": fm.get("evidence_level", "L5"),
            "indication_count": int(fm.get("indication_count") or 0),
            "prediction_score": 0,
            "nct_count": len(set(re.findall(r"NCT\d{8}", text))),
        })
    drugs.sort(key=lambda d: (-d["indication_count"], d["slug"]))
    counts = {f"L{n}": sum(d["level"] == f"L{n}" for d in drugs) for n in range(1, 6)}
    out = {"total_drugs": len(drugs), "level_counts": counts,
           "top_by_indications": drugs[:20], "all_drugs": drugs}
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"drug_stats.json：{len(drugs)} 個藥，{counts}")


if __name__ == "__main__":
    main()
