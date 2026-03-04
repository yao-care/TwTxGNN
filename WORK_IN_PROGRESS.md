# 工作進度記錄

**最後更新**: 2026-03-04

## 目前狀態

### 背景執行中的任務

`batch_collect_bundles.py` 正在背景收集藥物 bundles。

```
進度: 88/1293 (6.8%)
Bundles 總數: 279 (原本 193，新增 86)
預估剩餘時間: ~80 分鐘
```

### 已完成的工作

1. ✅ KG 預測完成 (`data/processed/repurposing_candidates.csv`)
2. ✅ DL 預測完成 (`data/processed/txgnn_dl_predictions.csv`)
3. ✅ 整合 KG + DL 預測 (`data/processed/integrated_predictions.csv`)
4. ✅ 更新 CLAUDE.md 文件
5. ✅ Git commit 整合結果
6. 🔄 收集新藥物 bundles (進行中)

### 整合統計

| 指標 | 數值 |
|------|------|
| 總預測數 | 3,452,680 |
| 唯一藥物 | 1,484 |
| 唯一適應症 | 10,497 |
| 台灣藥品許可證 | 17,842 |

---

## 下次繼續工作指南

### 情境 1: batch_collect_bundles 仍在執行

```bash
# 檢查是否仍在執行
ps aux | grep batch_collect | grep -v grep

# 檢查進度
ls data/bundles/ | wc -l
```

### 情境 2: batch_collect_bundles 已完成

執行以下步驟完成網站更新：

```bash
# 1. 重新生成 search-index.json
uv run python scripts/generate_search_index.py

# 2. 更新 drug_stats.json (如果有新藥物頁面)
# 這需要先生成藥物頁面，然後更新統計

# 3. Git commit
git add .
git commit -m "feat(bundles): add new drug bundles from DL predictions"
git push origin main
```

### 情境 3: batch_collect_bundles 中斷了

重新執行，會自動跳過已存在的 bundles：

```bash
uv run python scripts/batch_collect_bundles.py --all --min-score 0.9 --skip-existing --top-n 10
```

---

## 待辦事項

- [ ] 等待 batch_collect_bundles 完成
- [ ] 重新生成 search-index.json
- [ ] 更新 drug_stats.json
- [ ] 生成新藥物頁面 (如需要)
- [ ] Git commit 並 push

---

## 關鍵檔案位置

| 檔案 | 說明 |
|------|------|
| `data/processed/integrated_predictions.csv` | 整合後的預測結果 |
| `data/processed/integration_stats.json` | 整合統計 |
| `data/bundles/` | 藥物 bundles 目錄 |
| `docs/data/search-index.json` | 網站搜尋索引 |
| `docs/_data/drug_stats.json` | 首頁圖表資料 |
