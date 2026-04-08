---
nav_exclude: true
---

# TwTxGNN 藥品映射發現 - 標準作業程序 (SOP)

## 目錄

1. [系統概述](#1-系統概述)
2. [前置作業](#2-前置作業)
3. [執行 API 查詢](#3-執行-api-查詢)
4. [驗證新映射](#4-驗證新映射)
5. [整合到主流程](#5-整合到主流程)
6. [驗證改善成效](#6-驗證改善成效)
7. [網站與資源更新](#7-網站與資源更新)
8. [Commit 規範](#8-commit-規範)
9. [疑難排解](#9-疑難排解)

---

## 1. 系統概述

### 1.1 架構圖

```
FDA 成分名稱 (未映射)
         │
         ├─ 分析 ─→ 產生 data/processed/drug_mapping.csv
         │
         ├─ API 查詢（三擇一或並行）
         │  ├─ build_rxnorm_synonyms.py    → rxnorm_mappings.json
         │  ├─ build_pubchem_mapping.py    → pubchem_mappings.json
         │  └─ build_chembl_mapping.py     → chembl_mappings.json
         │
         ├─ 人工驗證 ─→ 檢查映射目標是否在 DrugBank 中
         │
         └─ 整合 ─→ src/twtxgnn/mapping/drugbank_mapper.py
                    └─ synonym_map 字典
```

### 1.2 資料流程

| 檔案 | 類型 | 用途 |
|------|------|------|
| `data/processed/drug_mapping.csv` | 輸入 | 目前映射結果（含未映射成分） |
| `data/external/drugbank_vocab.csv` | 參考 | DrugBank 詞彙表（驗證映射目標） |
| `data/external/rxnorm_cache.json` | 快取 | RxNorm API 查詢結果快取 |
| `data/external/pubchem_cache.json` | 快取 | PubChem API 查詢結果快取 |
| `data/external/chembl_cache.json` | 快取 | ChEMBL API 查詢結果快取 |
| `data/processed/rxnorm_mappings.json` | 輸出 | RxNorm 發現的映射 |
| `src/twtxgnn/mapping/drugbank_mapper.py` | 最終 | 人工驗證後整合到 `synonym_map` |

### 1.3 API 特性比較

| API | 成功率 | 速度 | 適用情境 |
|-----|--------|------|---------|
| **PubChem** | ~17% | 中 | 營養素、化學名、草藥成分 |
| **RxNorm** | ~5% | 快 | 常見藥物、維生素、鹽類變體 |
| **ChEMBL** | ~40%* | 慢 | 歐洲藥物、研究用藥 |

*ChEMBL 成功率高但 API 不穩定

---

## 2. 前置作業

### 2.1 何時需要執行

- **定期維護**：每季度檢查一次
- **新藥品資料**：FDA 資料更新後
- **映射率過低**：當映射率低於 80% 時

### 2.2 確認環境

```bash
# 確認依賴已安裝
uv sync

# 確認資料完整
ls data/external/drugbank_vocab.csv
ls data/raw/tw_fda_drugs.json
```

### 2.3 執行基準預測

```bash
# 先跑一次預測，取得目前映射率
uv run python scripts/run_kg_prediction.py
```

記錄目前的映射率作為基準。

---

## 3. 執行 API 查詢

### 3.1 RxNorm API

```bash
# 查詢所有未映射成分
RXNORM_MAX_QUERIES=10000 uv run python scripts/build_rxnorm_synonyms.py

# 或限制查詢數量
RXNORM_MAX_QUERIES=500 uv run python scripts/build_rxnorm_synonyms.py
```

**輸出**：`data/processed/rxnorm_mappings.json`

### 3.2 PubChem API

```bash
# 查詢所有未映射成分
PUBCHEM_MAX_QUERIES=10000 uv run python scripts/build_pubchem_mapping.py
```

**輸出**：`data/processed/pubchem_mappings.json`

### 3.3 ChEMBL API

```bash
# 查詢所有未映射成分
CHEMBL_MAX_QUERIES=10000 uv run python scripts/build_chembl_mapping.py
```

**輸出**：`data/processed/chembl_mappings.json`

### 3.4 預期執行時間

| API | 100 筆 | 500 筆 | 全部 (~7000 筆) |
|-----|--------|--------|-----------------|
| RxNorm | ~1 分鐘 | ~5 分鐘 | ~1 小時 |
| PubChem | ~5 分鐘 | ~25 分鐘 | ~3-4 小時 |
| ChEMBL | ~2 分鐘 | ~10 分鐘 | ~1-2 小時 |

---

## 4. 驗證新映射

### 4.1 驗證目標是否在 DrugBank 中

**關鍵原則**：映射目標必須存在於 DrugBank 詞彙表中，否則無效。

```python
import pandas as pd
import json

# 載入 DrugBank 詞彙表
drugbank_df = pd.read_csv("data/external/drugbank_vocab.csv")
drugbank_names = set(drugbank_df["drug_name_upper"].str.upper())

# 載入映射結果
with open("data/processed/rxnorm_mappings.json", "r") as f:
    mappings = json.load(f)

# 驗證每個映射目標
valid = {}
invalid = {}

for source, target in mappings.items():
    if target.upper() in drugbank_names:
        valid[source] = target
    else:
        invalid[source] = target
        print(f"✗ {source} -> {target} (NOT IN DRUGBANK)")

print(f"\n有效映射: {len(valid)}/{len(mappings)}")
```

### 4.2 常見的無效映射

需要排除的映射目標（不在 DrugBank 中）：

| 目標 | 原因 |
|------|------|
| SILYBIN | DrugBank 不收錄 |
| SILYMARIN | DrugBank 不收錄 |
| LYSOZYME | 非藥物酶 |
| CHLOROPHYLLIN | 營養補充品 |
| VALERIC ACID | 只有衍生物 |

### 4.3 驗證映射方向

**正確**：FDA 名稱 → DrugBank 名稱
```python
"VITAMIN B1": "THIAMINE"  # ✓
```

**錯誤**：DrugBank 名稱 → FDA 名稱
```python
"THIAMINE": "VITAMIN B1"  # ✗
```

---

## 5. 整合到主流程

### 5.1 定位整合位置

編輯 `src/twtxgnn/mapping/drugbank_mapper.py`，找到 `synonym_map` 字典。

### 5.2 整合格式

```python
synonym_map = {
    # ===== [分類名稱] =====
    # [來源] 發現
    "FDA_NAME": "DRUGBANK_NAME",

    # ===== RxNorm API 橋接發現的同義詞 =====
    "GENTAMYCIN": "GENTAMICIN",
    "CEPHRADINE": "CEFRADINE",

    # ===== PubChem 橋接發現的同義詞 =====
    "ALCOHOL 95%": "ETHANOL",

    # ===== ChEMBL 橋接發現的同義詞 =====
    "GRAMICIDIN": "GRAMICIDIN D",
}
```

### 5.3 整合步驟

1. 找到對應分類（若無則新增）
2. 加上來源註解
3. 檢查是否已存在（避免重複）
4. 依字母排序（建議）

---

## 6. 驗證改善成效

### 6.1 重跑預測

```bash
uv run python scripts/run_kg_prediction.py
```

### 6.2 比較結果

| 指標 | 改善前 | 改善後 | 變化 |
|------|--------|--------|------|
| 成分映射率 | 82.71% | ? | +?% |
| DrugBank 藥品數 | 1,447 | ? | +? |
| 候選數 | 142,328 | ? | +? |

---

## 7. 網站與資源更新

映射改善後，需要更新以下相關資源：

### 7.1 重新生成 FHIR 資源

當預測結果更新後，需要重新生成 FHIR 資源：

```bash
# 重新生成 FHIR 資源
uv run python scripts/generate_fhir_resources.py

# 驗證資源數量
ls docs/fhir/MedicationKnowledge/ | wc -l
ls docs/fhir/ClinicalUseDefinition/ | wc -l
```

### 7.2 更新搜尋索引

```bash
# 搜尋索引會在生成 FHIR 資源時自動更新
# 確認 search-index.json 已更新
ls -la docs/data/search-index.json
```

### 7.3 更新新聞關鍵字

如果有新的適應症被加入預測，需要更新新聞監測關鍵字：

```bash
# 重新生成新聞關鍵字（只包含有藥物預測的適應症）
uv run python scripts/generate_news_keywords.py

# 複製到網站目錄
cp data/news/keywords.json docs/data/keywords.json
```

### 7.4 觸發網站部署

```bash
# 手動觸發 Jekyll 部署（排程推送不會自動觸發）
gh workflow run "Deploy Jekyll to GitHub Pages"
```

### 7.5 完整更新流程

```bash
# 1. 重跑預測（映射改善後）
uv run python scripts/run_kg_prediction.py

# 2. 重新生成 FHIR 資源
uv run python scripts/generate_fhir_resources.py

# 3. 更新新聞關鍵字
uv run python scripts/generate_news_keywords.py
cp data/news/keywords.json docs/data/keywords.json

# 4. Commit 並推送
git add .
git commit -m "feat: update predictions and resources after mapping improvement"
git push

# 5. 觸發網站部署
gh workflow run "Deploy Jekyll to GitHub Pages"
```

---

## 8. Commit 規範

### 8.1 Commit Message 格式

```
feat(mapping): add [API] discovered synonyms

- [API] 發現的同義詞:
  - [成分1] -> [DrugBank 名稱1]
  - [成分2] -> [DrugBank 名稱2]
- 修正錯誤映射（若有）
- 映射率: [舊%] -> [新%] (+[差值]%)
- DrugBank 涵蓋: [舊數] -> [新數] 藥物

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

---

## 9. 疑難排解

### 9.1 常見錯誤

| 錯誤 | 原因 | 解決方式 |
|------|------|---------|
| `ConnectionError` | 網路問題 | 等待後重試，快取已保留 |
| `Rate limit exceeded` | 請求過快 | 降低 `MAX_QUERIES` |
| JSON 解析錯誤 | 快取損壞 | 刪除快取檔案重新查詢 |

### 9.2 快取檔案損壞

```bash
# 備份並刪除舊快取
mv data/external/rxnorm_cache.json data/external/rxnorm_cache.json.bak

# 重新執行查詢
uv run python scripts/build_rxnorm_synonyms.py
```

---

## 附錄：快速參考

### 完整工作流程

```bash
# 1. 基準測試
uv run python scripts/run_kg_prediction.py

# 2. 執行 API 查詢
RXNORM_MAX_QUERIES=10000 uv run python scripts/build_rxnorm_synonyms.py
PUBCHEM_MAX_QUERIES=10000 uv run python scripts/build_pubchem_mapping.py
CHEMBL_MAX_QUERIES=10000 uv run python scripts/build_chembl_mapping.py

# 3. 驗證映射（人工執行）
# - 檢查 *_mappings.json
# - 確認目標存在於 DrugBank 中

# 4. 整合到 drugbank_mapper.py（手動編輯）

# 5. 驗證改善
uv run python scripts/run_kg_prediction.py

# 6. Commit
git add src/twtxgnn/mapping/drugbank_mapper.py
git commit -m "feat(mapping): add API discovered synonyms ..."
git push
```

---

## 執行記錄

### 2026-03-03 完整 API 查詢

| 項目 | 數值 |
|------|------|
| **執行日期** | 2026-03-03 |
| **查詢範圍** | 所有未映射成分 |

**API 查詢結果**：

| API | 發現映射數 | 狀態 |
|-----|-----------|------|
| RxNorm | 92 | ✅ 完成 |
| PubChem | 265 | ✅ 完成 |
| ChEMBL | 271 | ✅ 完成（部分 SSL 錯誤） |
| **去重後總計** | **409** | - |

**映射改善**：

| 指標 | 改善前 | 改善後 | 變化 |
|------|--------|--------|------|
| 成分映射率 | 56.05% | 83.89% | +27.84% |
| 映射成功數 | 25,172 | 37,676 | +12,504 |
| DrugBank 藥物數 | 1,447 | 1,594 | +147 |

**映射來源分布**：

| 來源 | 數量 | 佔比 |
|------|------|------|
| drugbank (直接匹配) | 37,128 | 98.5% |
| herbal (中草藥) | 424 | 1.1% |
| drugbank_synonym | 124 | 0.3% |

**KG 預測結果**：
- 候選數：142,351 筆
- FHIR 資源：189 MedicationKnowledge, 1,267 ClinicalUseDefinition

**Commit**：`eeefa00` feat(mapping): complete API discovery with 409 new synonyms

---

**文件版本**：1.1
**最後更新**：2026-03-03
**維護者**：TwTxGNN Team
