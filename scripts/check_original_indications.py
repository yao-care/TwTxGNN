#!/usr/bin/env python3
"""「原適應症」列的程式化交叉驗證（只列待查，不改頁面）。

做法：把每頁快速總覽「原適應症／原核准適應症」的文字切成詞組，逐一比對
  (a) 本藥的 TFDA 許可證適應症（依 twtxgnn.regulatory.tfda_licenses 的主成分比對）；
  (b) 其他藥的許可證適應症。
某詞組在 (a) 找不到、卻在 (b) 找得到，就是「只出現在不屬於本藥的許可證」的詞組。
一頁有這種詞組且占該列詞組一半以上，就寫進 docs/_data/drug_reviews_uncertain.json
（source＝原適應症交叉驗證；每次執行整批替換這個 source 的項目），交人工判讀。

用法：python3 scripts/check_original_indications.py   （需要 data/raw/tw_fda_drugs.json）
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from twtxgnn.regulatory import tfda_licenses as T  # noqa: E402
from twtxgnn.regulatory.page_postprocess import REVIEW_RE  # noqa: E402

UNCERTAIN = ROOT / "docs" / "_data" / "drug_reviews_uncertain.json"
SOURCE = "原適應症交叉驗證（scripts/check_original_indications.py）"
ROW_RE = re.compile(r"^\|\s*原(?:核准)?適應症\s*\|([^|\n]*)\|", re.M)
SPLIT_RE = re.compile(r"[、，,；;／/（）()\s]+|及|與|和|或|等")


def phrases(cell: str) -> list[str]:
    cell = re.sub(r"\*\*|\[[^\]]*\]\([^)]*\)", "", cell)
    out = []
    for p in SPLIT_RE.split(cell):
        p = p.strip(" .。:：-")
        if len(p) >= 3 and not re.fullmatch(r"[A-Za-z0-9 .-]+", p):
            out.append(p)
    return out


def main():
    recs = T.load_records()
    if not recs:
        sys.exit("找不到 data/raw/tw_fda_drugs.json")
    by_id = T.dedupe(recs)
    all_ind = {lid: re.sub(r"\s+", "", r.get("適應症") or "") for lid, r in by_id.items()}
    items = []
    for p in sorted((ROOT / "docs" / "_drugs").glob("*.md")):
        text = REVIEW_RE.sub("", p.read_text(encoding="utf-8"))
        m = ROW_RE.search(text)
        if not m:
            continue
        title = re.search(r"^title:\s*(.+)$", text, re.M).group(1).strip()
        own_ids = {x["id"] for x in T.licenses_for_drug(T.SLUG_QUERY.get(p.stem, title), by_id)}
        own = "\n".join(all_ind[i] for i in own_ids)
        ph = phrases(m.group(1))
        if not ph:
            continue
        foreign_only = {}
        for x in ph:
            k = re.sub(r"\s+", "", x)
            if k in own:
                continue
            hits = [lid for lid, ind in all_ind.items() if lid not in own_ids and k in ind]
            if hits:
                foreign_only[x] = hits[:3]
        if foreign_only and len(foreign_only) * 2 >= len(ph):
            ex = "；".join(f"「{k}」見於 {'、'.join(v)}" for k, v in foreign_only.items())
            items.append({
                "file": p.name,
                "claim": m.group(0).strip(),
                "why": (f"原適應症 {len(ph)} 個詞組中有 {len(foreign_only)} 個在本藥（主成分比對）的 TFDA 許可證適應症裡找不到，"
                        f"卻出現在其他藥的許可證：{ex}。可能取自別藥或複方的適應症，需人工確認。"),
                "found": "2026-10-03",
                "batch": SOURCE,
            })
    doc = json.loads(UNCERTAIN.read_text(encoding="utf-8"))
    doc["items"] = [i for i in doc["items"] if i.get("batch") != SOURCE] + items
    UNCERTAIN.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"原適應症交叉驗證：{len(items)} 頁列入待查")
    for i in items:
        print("  -", i["file"], i["claim"][:80])


if __name__ == "__main__":
    main()
