#!/bin/bash
# 每週排程：TFDA 資料集 36 下載 → 程式化許可證表重產 → 重套查核紀錄 → gate（2026-11-24，用戶決定接進排程）。
# 以前要人手動跑 regenerate_tfda_tables.py，頁面停在舊資料集，每次 TFDA 更新都冒出一批「TFDA 許可證變更」issue。
# 任一步失敗：還原 docs／snapshots、exit 1（workflow 另開 issue）。成功只改工作目錄，commit 由 workflow 做。
# 用法（repo 根目錄）：bash scripts/tfda_regen_weekly.sh   （需要 .venv；寫 GITHUB_OUTPUT 的 data_date、pages）
set -uo pipefail
cd "$(dirname "$0")/.."
PY=${PY:-.venv/bin/python}
out() { [ -n "${GITHUB_OUTPUT:-}" ] && echo "$1" >> "$GITHUB_OUTPUT"; echo "$1"; }
fail() { echo "✗ $1" >&2; git checkout -- docs snapshots 2>/dev/null; out "ok=0"; exit 1; }

mkdir -p data/raw
curl -fsSL --retry 3 --max-time 900 -o data/raw/fda_36.zip "https://data.fda.gov.tw/data/opendata/export/36/json" || fail "TFDA 資料集 36 下載失敗"
DATE=$("$PY" -c "import zipfile,sys;z=zipfile.ZipFile('data/raw/fda_36.zip');i=max(z.infolist(),key=lambda x:x.file_size);print('%04d-%02d-%02d'%i.date_time[:3])") || fail "讀不到 ZIP 檔案日期"
"$PY" scripts/process_fda_data.py > /tmp/tfda_process.log 2>&1 || fail "process_fda_data.py 失敗：$(tail -3 /tmp/tfda_process.log)"
n=$("$PY" -c "import json;print(len(json.load(open('data/raw/tw_fda_drugs.json'))))")
[ "$n" -ge 60000 ] || fail "資料集只有 $n 筆（少於 60,000），疑似來源異常，不重產"
log=$("$PY" scripts/regenerate_tfda_tables.py --data-date "$DATE" 2>&1) || fail "regenerate_tfda_tables.py 失敗：$(echo "$log" | tail -3)"
summary=$(echo "$log" | grep "頁面改動")
echo "$summary"
echo "$summary" | grep -q "全站重套後仍變動 0 頁" || fail "重套查核紀錄後仍有頁面變動：$summary"
echo "$summary" | grep -q "問題 0 項" || fail "重產後有問題：$summary"
"$PY" scripts/apply_drug_reviews.py --check > /tmp/tfda_apply.log 2>&1 || fail "查核紀錄檢查沒過：$(tail -3 /tmp/tfda_apply.log)"
"$PY" scripts/check_seo_docs.py > /tmp/tfda_gate.log 2>&1 || fail "gate（check_seo_docs.py）沒過：$(tail -5 /tmp/tfda_gate.log)"
out "ok=1"
out "data_date=$DATE"
out "pages=$(git status --porcelain -- docs/_drugs | wc -l | tr -d ' ')"
