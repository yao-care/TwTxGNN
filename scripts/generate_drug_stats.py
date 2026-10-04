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
另外同步「不能用 Liquid」的寫死數字（2026-10-04 補）：front matter description（jekyll-seo-tag 直接輸出成
meta description／og:description）、ld+json 的 numberOfItems（gate 要把它當 JSON 解析）、README.md、
CITATION.cff 等不經 Jekyll 的檔。清單在 COUNT_SPOTS；能用 Liquid 的地方一律寫
{{ site.data.drug_stats.total_drugs }}／level_counts，不列在這裡。gate（check_seo_docs.py 第 7c 項）用
同一份清單檢查數字一致。
  total     ＝ drug_stats.json 的 total_drugs（藥物頁數）
  keywords  ＝ docs/data/keywords.json 的藥物數（新聞監測的藥物數，與報告數不同）
  L1…L5     ＝ drug_stats.json 的 level_counts
用法：python3 scripts/generate_drug_stats.py（可重複執行，結果相同）
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRUGS = ROOT / "docs" / "_drugs"
OUT = ROOT / "docs" / "_data" / "drug_stats.json"


# (檔案, 正則（group 2 是數字）, 數字來源)
COUNT_SPOTS = [
    ("docs/index.md", r'(^description: "[^"\n]*?提供 )(\d+)( 個藥物)', "total"),
    ("docs/downloads.md", r'(^description: "[^"\n]*?包含 )(\d+)( 個藥物)', "total"),
    ("docs/about.md", r'(^description: "[^"\n]*?提供 )(\d+)( 個台灣健保藥品)', "total"),
    ("docs/nav-drugs.md", r'(^description: "瀏覽 )(\d+)( 份)', "total"),
    ("docs/news.md", r'(^description: "自動監測 )(\d+)( 種藥物)', "keywords"),
    ("docs/news.md", r'(自動追蹤 )(\d+)( 種藥物)', "keywords"),
    ("docs/_includes/head_custom.html", r'(自動監測 )(\d+)( 種藥物)', "keywords"),
    ("docs/_includes/head_custom.html", r'("numberOfItems": )(\d+)()', "total"),
    ("README.md", r'(\| \*\*藥物報告\*\* \| )(\d+)( 份)', "total"),
    ("README.md", r'(\| \*\*涵蓋藥物\*\* \| )(\d+)( 種)', "total"),  # 一份報告對應一個藥
    *[("README.md", rf'(^\| \*\*L{n}\*\* \| )(\d+)( \|)', f"L{n}") for n in range(1, 6)],
    ("CITATION.cff", r'(provides )(\d+)( drug validation reports)', "total"),
    ("docs/sop/chart-data-maintenance.md", r'("total_drugs": )(\d+)()', "total"),
]


def count_sources(stats):
    kw = ROOT / "docs" / "data" / "keywords.json"
    k = json.loads(kw.read_text(encoding="utf-8")) if kw.exists() else {}
    return {"total": stats["total_drugs"], "keywords": k.get("drug_count", len(k.get("drugs", []))),
            **stats["level_counts"]}


def count_spot_problems(stats, fix=False):
    """stats＝drug_stats.json 內容。回傳寫死數字與來源不符的清單；fix=True 時直接改檔（保留原換行字元）。"""
    src, errs = count_sources(stats), []
    by_file = {}
    for rel, pat, key in COUNT_SPOTS:
        by_file.setdefault(rel, []).append((re.compile(pat, re.M), key))
    for rel, rules in by_file.items():
        path = ROOT / rel
        text = path.read_bytes().decode("utf-8")
        new = text
        for rx, key in rules:
            ms = list(rx.finditer(new))
            if len(ms) != 1:
                errs.append(f"{rel}：找不到（或不只一處）{rx.pattern}")
                continue
            want = str(src[key])
            if ms[0].group(2) != want:
                errs.append(f"{rel}：寫死的數字 {ms[0].group(2)} 應為 {want}（{key}）")
                new = rx.sub(lambda m: m.group(1) + want + m.group(3), new, count=1)
        if fix and new != text:
            path.write_bytes(new.encode("utf-8"))
    return errs


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
    fixed = count_spot_problems(out, fix=True)
    print(f"寫死的藥物數：更新 {len([e for e in fixed if '應為' in e])} 處")
    for e in fixed:
        if "應為" not in e:
            print("  ✗", e)


if __name__ == "__main__":
    main()
