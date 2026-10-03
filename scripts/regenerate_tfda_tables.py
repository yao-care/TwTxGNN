#!/usr/bin/env python3
"""全站藥物頁：清理產線開場白／內部用語、以程式產生的 TFDA 許可證表與張數取代 LLM 寫的版本。

做的事（可重複執行，結果相同）：
  1. 每頁先拿掉查核框（之後由 apply_drug_reviews.py 重套），再跑
     twtxgnn.regulatory.page_postprocess（開場白、Evidence Pack 用語、許可證表、張數）。
  2. 寫出 snapshots/tfda_licenses.json.gz（每頁的許可證清單快照；gate 與沒有資料集時的產線用）。
  3. 查核紀錄裡錨點落在被取代的許可證表或張數上的，標 status=superseded（紀錄保留）。
  4. 跑 apply_drug_reviews 重套其餘紀錄。
頁面上若還有不屬於這個藥的許可證字號（驗證不過），列出來並以 exit 1 結束，不寫該頁。

用法：
  python3 scripts/regenerate_tfda_tables.py --data-date 2026-09-29
  （需要 data/raw/tw_fda_drugs.json；由 scripts/process_fda_data.py 從 TFDA 資料集 36 產生）
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from twtxgnn.regulatory import tfda_licenses as T  # noqa: E402
from twtxgnn.regulatory.page_postprocess import (  # noqa: E402
    REVIEW_RE, clean_llm_output, postprocess_with_licenses, replace_tfda)
import apply_drug_reviews as A  # noqa: E402

DRUGS = ROOT / "docs" / "_drugs"
COUNT_RE = re.compile(r"\d[\d,，]*\s*張[^。；\n]{0,30}許可證")
SUPERSEDED_BY = "程式化許可證表（scripts/regenerate_tfda_tables.py，2026-10-03 依 TFDA 資料集 36 重產）"


def title_of(text: str) -> str:
    m = re.search(r"^title:\s*(.+)$", text, re.M)
    return m.group(1).strip().strip('"').strip("'") if m else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-date", required=True)
    args = ap.parse_args()
    recs = T.load_records()
    if not recs:
        sys.exit("找不到 data/raw/tw_fda_drugs.json")
    by_id = T.dedupe(recs)
    data = json.loads(A.DATA.read_text(encoding="utf-8"))
    by_file = {}
    for r in data["records"]:
        by_file.setdefault(r["file"], []).append(r)

    pages, snap = {}, {}
    for p in sorted(DRUGS.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        slug, title = p.stem, title_of(text)
        query = T.SLUG_QUERY.get(slug, title)
        lics = [T.compact(x) for x in T.licenses_for_drug(query, by_id)]
        snap[slug] = {"query": query, "licenses": lics}
        pages[p] = (REVIEW_RE.sub("", text), title, lics)

    # 1) 判定 superseded：錨點落在被取代的許可證表／「許可證數」列，或更正內容本身是張數
    sup = 0
    for p, (base, title, lics) in pages.items():
        t1 = replace_tfda(clean_llm_output(base), title, lics, args.data_date)
        body = REVIEW_RE.sub("", t1)
        for r in by_file.get(p.name, []):
            if r["action"] == "section" or r.get("status") == "superseded":
                continue
            if r["action"] == "correct":
                gone = r["replacement"] not in body and r["claim"] not in body
                owns_count = bool(COUNT_RE.search(r["replacement"]))
            else:
                gone = (r.get("anchor") or r["claim"]) not in body
                owns_count = bool(COUNT_RE.search(r.get("anchor") or r["claim"]))  # 加註的對象就是張數
            if gone or owns_count:
                r["status"] = "superseded"
                r["superseded_by"] = SUPERSEDED_BY
                sup += 1
    A.DATA.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    # 2) 重產：superseded 的更正先還原成原句（與從 notes 重產時看到的一樣），再走產線同一套後處理
    failed, changed = {}, 0
    for p, (base, title, lics) in pages.items():
        for r in by_file.get(p.name, []):
            if r.get("status") == "superseded" and r["action"] == "correct" and r["replacement"] in base:
                base = base.replace(r["replacement"], r["claim"], 1)
        new, bad = postprocess_with_licenses(base, title, lics, args.data_date, slug=p.stem)
        if bad:
            failed[p.name] = bad
            continue
        old = p.read_text(encoding="utf-8")
        if new != old:
            changed += 1
            p.write_text(new, encoding="utf-8")
    T.write_snapshot(snap, args.data_date)

    problems, applied = A.run()
    print(f"頁面改動 {changed} 頁；本次新標 superseded {sup} 筆；全站重套後仍變動 {len(applied)} 頁（應為 0）、問題 {len(problems)} 項")
    for f, bad in failed.items():
        print(f"  ✗ {f}：頁面上仍有不屬於本藥的許可證字號 {bad}（未寫入）")
    for x in problems:
        print("  ✗", x)
    sys.exit(1 if (failed or problems or applied) else 0)


if __name__ == "__main__":
    main()
