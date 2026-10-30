"""TW（衛福部食藥署開放資料 36 號：全部藥品許可證）下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：https://data.fda.gov.tw/data/opendata/export/36/json（zip 內為 JSON，免金鑰）。欄位：許可證字號、註銷狀態、註銷日期、有效日期。
證據包紀錄：license_id＝許可證字號、license_status（valid／cancelled／expired）、status（註銷狀態原文）、cancel_date、expiry_date。
對應：註銷狀態有值 → cancelled（status＝原文、cancel_date＝註銷日期）；否則有效日期已過 → expired；否則 valid（expiry_date 同步）。
Tw 的頁面許可證表與張數由 Tw 自己的 tfda 程式產生，且有人工查核紀錄：排程只更新證據包，頁面不由本流程改
（license_table_sync 對 Tw 不動頁）；頁面更新照 Tw 既有流程，查核頁由用戶簽核。新檔沒有的字號保留原狀態。
"""
import io
import json
import time
import zipfile

import requests

RAW_FILE = "raw/tfda_license_status.json"
URL = "https://data.fda.gov.tw/data/opendata/export/36/json"


def fetch():
    for attempt in range(4):
        try:
            r = requests.get(URL, timeout=600)
            r.raise_for_status()
            z = zipfile.ZipFile(io.BytesIO(r.content))
            break
        except Exception:
            if attempt == 3:
                raise
            time.sleep(20 * (attempt + 1))
    data = json.loads(z.read(z.namelist()[0]).decode("utf-8-sig"))
    return [{"no": (x.get("許可證字號") or "").strip(), "cancel": (x.get("註銷狀態") or "").strip(),
             "cancel_date": (x.get("註銷日期") or "").strip(), "expiry": (x.get("有效日期") or "").strip()} for x in data if x.get("許可證字號")]


def validate(new, old):
    p = []
    if len(new) < 50000:
        p.append(f"只解析出 {len(new)} 筆（TFDA 通常 >60,000），疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    today = time.strftime("%Y/%m/%d")
    idx = {}
    for r in new:
        if r["cancel"]:
            idx[r["no"]] = ("cancelled", r["cancel"], r["cancel_date"], r["expiry"])
        elif r["expiry"] and r["expiry"] < today:
            idx[r["no"]] = ("expired", "", "", r["expiry"])
        else:
            idx[r["no"]] = ("valid", "", "", r["expiry"])
    return idx


def record_id(rec):
    return str(rec.get("license_id") or "").strip()


def update(rec, new):
    cls, text, cdate, exp = new
    cur = rec.get("license_status") or ("cancelled" if rec.get("status") else "valid")
    if cur == cls:
        return False  # 狀態意義沒變（日期等欄位不動，避免無意義改證據包）
    rec["license_status"] = cls
    if cls == "cancelled":
        rec["status"], rec["cancel_date"] = text, cdate
    elif cls == "valid":
        rec["status"], rec["cancel_date"] = "", ""
    rec["expiry_date"] = exp
    return True
