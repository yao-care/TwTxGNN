#!/usr/bin/env python3
"""證據包 tfda 區塊收錯的許可證移出（2026-11-25 第五輪，用戶決定；規則見 config/bundle_record_exclusions.json）。

Release 的證據包 tfda.records 有一部分是 2026-10-03 以前用全文子字串收的（例 atracurium_besylate 收到 cisatracurium）。
許可證字號在 TFDA 資料集（data/raw/tw_fda_drugs.json）裡、卻不在本藥依 tfda_licenses 主成分比對的結果裡（有頁的用
snapshots/tfda_licenses.json.gz 的該頁許可證＝頁面許可證表，沒頁的用 licenses_for_drug(drug.inn)），就從 tfda.records 移到
tfda.excluded_records（附 excluded、excluded_reason、excluded_basis），total_matches 改成留下的不重複字號數。
config 的 keep 照留；資料集沒有的字號照留。只移不刪、可重複執行。每週 license-refresh.yml 在 license_refresh 前先跑。
用法（repo 根目錄，先還原 data/）：python3 scripts/exclude_mismatched_records.py [--dry-run]
"""
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from twtxgnn.regulatory import tfda_licenses as T  # noqa: E402

CONF = ROOT / "config" / "bundle_record_exclusions.json"


def run(dry=False):
    today = time.strftime("%Y-%m-%d")
    records = T.load_records()
    if len(records) < 60000:
        sys.exit(f"TFDA 資料集只有 {len(records)} 筆（data/raw/tw_fda_drugs.json），不判定")
    by_id = T.dedupe(records)
    snap = T.load_snapshot()
    pages = snap.get("drugs", snap)
    keep = {k: set(v["ids"]) for k, v in (json.loads(CONF.read_text(encoding="utf-8")).get("keep") or {}).items()}
    moved, touched = 0, []
    for f in sorted((ROOT / "data" / "bundles").glob("*/drug_bundle.json")):
        name = f.parent.name
        b = json.loads(f.read_text(encoding="utf-8"))
        t = b.get("tfda") or {}
        recs = t.get("records") or []
        if not recs:
            continue
        if name in pages:
            allowed = {x["id"] for x in pages[name].get("licenses") or []}
            basis = f"頁面許可證表（snapshots/tfda_licenses.json.gz，資料集 {(snap.get('meta') or {}).get('data_date', '')}）"
        else:
            q = T.SLUG_QUERY.get(name) or (b.get("drug") or {}).get("inn") or name.replace("_", " ")
            allowed = {x["id"] for x in T.licenses_for_drug(q, by_id)}
            basis = f"tfda_licenses.licenses_for_drug({q!r})"
        allowed |= keep.get(name, set())
        out, kept = [], []
        for r in recs:
            lid = r.get("license_id")
            if lid in by_id and lid not in allowed:
                x = by_id[lid]
                out.append(dict(r, excluded=today,
                                excluded_reason=f"主成分（{x.get('主成分略述') or x.get('英文品名') or ''}）依 tfda_licenses 主成分比對不是本藥（2026-10-03 前全文子字串比對收進來的）",
                                excluded_basis=f"{T.SOURCE_LABEL}；{basis}"))
            else:
                kept.append(r)
        if not out:
            continue
        for r in out:
            print(f"  {name}: 移出 {r.get('license_id')} {str(r.get('brand_name_en'))[:40]}（{str(r.get('ingredients'))[:50]}）")
        moved += len(out)
        touched.append(name)
        if dry:
            continue
        t["records"] = kept
        t["excluded_records"] = (t.get("excluded_records") or []) + out
        t["total_matches"] = len({r.get("license_id") for r in kept})
        if not kept:
            t["found"] = False
        b["tfda"] = t
        f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"證據包收錯品項：移出 {moved} 筆（{len(touched)} 個證據包）{'（試跑，沒寫檔）' if dry else ''}")
    return touched


if __name__ == "__main__":
    run(dry="--dry-run" in sys.argv[1:])
