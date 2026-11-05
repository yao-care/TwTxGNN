#!/usr/bin/env python3
"""README「預測方法」段的知識圖譜／深度學習數字（2026-11-05）：從 Release 的 data/ 算出來，寫進
docs/_data/prediction_stats.json；README 裡的數字由 scripts/generate_drug_stats.py 的 COUNT_SPOTS 依這份檔同步，
scripts/check_seo_docs.py 第 7c 項擋不一致。

data/ 不進 git（成果放本 repo 的 Release，還原：cat TwTxGNN-data.tar.gz.part-* | tar xzf -）。還原後在 repo 根目錄執行：
    uv run python scripts/generate_prediction_stats.py --release data-YYYYMMDD-HHMMSS
    python3 scripts/generate_drug_stats.py      # 把新數字寫進 README

算法（每項都只數檔案，不做推估）：
    fda_records          data/raw/tw_fda_drugs.json 的筆數
    fda_license_ids      同檔中不重複的「許可證字號」數（一張許可證可有多筆資料）
    fda_active           同檔中「註銷狀態」不是「已註銷」且「主成分略述」不空的筆數（同 twtxgnn.data.filter_active_drugs）
    ingredient_mapping_rate / drugbank_ids
                         data/processed/drug_mapping.csv：映射成功列／全部列；映射成功列的不重複 drugbank_id
    indication_mapping_rate / mapped_diseases
                         data/processed/indication_mapping.csv：disease_id 不空的列／全部列；不重複 disease_id
    kg_candidates / kg_drugs / kg_diseases
                         data/processed/repurposing_candidates.csv.gz：列數；不重複「藥物成分」；不重複「潛在新適應症」
    dl_rows / dl_drugs / dl_diseases / dl_gt_0_9 / dl_gt_0_7 / dl_min_score
                         data/processed/txgnn_dl_predictions.csv.gz：列數；不重複 drugbank_id；不重複「潛在新適應症」；
                         txgnn_score > 0.9、> 0.7 的列數；最低分（檔案只存分數 ≥ 這個值的配對）
    integration_*        data/processed/integration_stats.json 的 total_predictions、unique_drugs
    kg_vocab_diseases / kg_vocab_drugs
                         data/external/disease_vocab.csv、drugbank_vocab.csv 的列數（TxGNN 知識圖譜的疾病、藥品節點）
"""
import argparse
import csv
import gzip
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "docs" / "_data" / "prediction_stats.json"


def rows(path):
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8-sig", newline="") as f:
        yield from csv.DictReader(f)


def build():
    fda = json.loads((DATA / "raw" / "tw_fda_drugs.json").read_text(encoding="utf-8"))
    active = [d for d in fda if d.get("註銷狀態") != "已註銷" and d.get("主成分略述")]

    n = ok = 0
    db = set()
    for r in rows(DATA / "processed" / "drug_mapping.csv"):
        n += 1
        if str(r.get("映射成功", "")).strip().lower() == "true":
            ok += 1
            db.add(r["drugbank_id"])
    ind_n = ind_ok = 0
    dis = set()
    for r in rows(DATA / "processed" / "indication_mapping.csv"):
        ind_n += 1
        if r.get("disease_id"):
            ind_ok += 1
            dis.add(r["disease_id"])
    kg = list(rows(DATA / "processed" / "repurposing_candidates.csv.gz"))
    dl_n = gt9 = gt7 = 0
    dl_min = None
    dl_drugs, dl_dis = set(), set()
    for r in rows(DATA / "processed" / "txgnn_dl_predictions.csv.gz"):
        dl_n += 1
        s = float(r["txgnn_score"])
        gt9 += s > 0.9
        gt7 += s > 0.7
        dl_min = s if dl_min is None else min(dl_min, s)
        dl_drugs.add(r["drugbank_id"])
        dl_dis.add(r["潛在新適應症"])
    integ = json.loads((DATA / "processed" / "integration_stats.json").read_text(encoding="utf-8"))
    vocab = {k: sum(1 for _ in rows(DATA / "external" / f"{k}_vocab.csv")) for k in ("disease", "drugbank")}

    v = {
        "fda_records": len(fda),
        "fda_license_ids": len({d.get("許可證字號") for d in fda if d.get("許可證字號")}),
        "fda_active": len(active),
        "ingredient_mapping_rate": ok / n,
        "drugbank_ids": len(db),
        "indication_mapping_rate": ind_ok / ind_n,
        "mapped_diseases": len(dis),
        "kg_candidates": len(kg),
        "kg_drugs": len({r["藥物成分"] for r in kg}),
        "kg_diseases": len({r["潛在新適應症"] for r in kg}),
        "dl_rows": dl_n,
        "dl_drugs": len(dl_drugs),
        "dl_diseases": len(dl_dis),
        "dl_gt_0_9": gt9,
        "dl_gt_0_7": gt7,
        "dl_min_score": dl_min,
        "integration_total": integ["total_predictions"],
        "integration_drugs": integ["unique_drugs"],
        "kg_vocab_diseases": vocab["disease"],
        "kg_vocab_drugs": vocab["drugbank"],
    }
    # Jekyll／README 沒有千分位與百分比格式，顯示用字串一起產生（COUNT_SPOTS 比對的是這些字串）
    display = {k: (f"{x:.2%}" if k.endswith("_rate") else f"{x:g}" if k == "dl_min_score" else f"{x:,}") for k, x in v.items()}
    return v, display


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--release", required=True, help="還原的 data/ 來自哪個 Release（例：data-20261102-155217）")
    a = ap.parse_args()
    v, display = build()
    data = {
        "_source": f"本 repo Release {a.release} 的 data/（算法見 scripts/generate_prediction_stats.py 開頭）。"
                   "由 scripts/generate_prediction_stats.py 產生，勿手改；README 數字由 scripts/generate_drug_stats.py 同步。",
        "release": a.release,
        **v,
        "display": display,
    }
    text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
        OUT.write_text(text, encoding="utf-8")
        print(f"更新 {OUT.relative_to(ROOT)}")
    else:
        print(f"{OUT.relative_to(ROOT)} 不變")
    for k, s in display.items():
        print(f"  {k}: {s}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
