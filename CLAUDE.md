# TwTxGNN - Claude CLI 使用指引

本文件用於引導 Claude CLI 自動化執行台灣健保藥品老藥新用預測實驗。

- **GitHub**: https://github.com/yao-care/TwTxGNN
- **網站**: https://twtxgnn.yao.care/

## 專案概述

使用 TxGNN 知識圖譜對台灣健保藥品進行 drug repurposing（老藥新用）預測。

| 方法 | 速度 | 精準度 | 環境需求 |
|------|------|--------|----------|
| 知識圖譜方法 | 快（幾秒） | 較低 | uv（無特殊需求） |
| 深度學習方法 | 慢（數小時） | 較高 | Conda + PyTorch + DGL |

---

## Claude CLI 自動化流程

當使用者要求重現實驗結果時，請依序執行以下步驟：

### 步驟 1：檢查並下載資料

先檢查資料是否存在，若不存在則下載：

```bash
# 建立目錄
mkdir -p data/raw

# 下載 TxGNN 資料（前景執行，確保完成）
[ ! -f data/node.csv ] && curl -L -o data/node.csv "https://dataverse.harvard.edu/api/access/datafile/7144482"
[ ! -f data/kg.csv ] && curl -L -o data/kg.csv "https://dataverse.harvard.edu/api/access/datafile/7144484"

# 下載 FDA 資料（若 JSON 和 ZIP 都不存在）
[ ! -f data/raw/tw_fda_drugs.json ] && [ -z "$(ls data/raw/*.zip 2>/dev/null)" ] && \
  curl -L -o data/raw/fda_36.zip "https://data.fda.gov.tw/data/opendata/export/36/json"

# 驗證下載
ls data/node.csv data/kg.csv
ls data/raw/*.zip 2>/dev/null || ls data/raw/tw_fda_drugs.json
```

### 步驟 2：安裝依賴

```bash
uv sync
```

### 步驟 3：處理 FDA 資料

將下載的 FDA ZIP 檔案解壓縮並轉換為 JSON：

```bash
uv run python scripts/process_fda_data.py

# 驗證
ls data/raw/tw_fda_drugs.json
```

這會產生 `data/raw/tw_fda_drugs.json`。

### 步驟 4：準備詞彙表資料

從 TxGNN 資料提取知識圖譜方法所需的詞彙表：

```bash
uv run python scripts/prepare_external_data.py

# 驗證
ls data/external/drugbank_vocab.csv data/external/disease_vocab.csv data/external/drug_disease_relations.csv
```

這會產生：
- `data/external/drugbank_vocab.csv`
- `data/external/disease_vocab.csv`
- `data/external/drug_disease_relations.csv`

### 步驟 5：執行知識圖譜方法

```bash
uv run python scripts/run_kg_prediction.py

# 驗證
ls data/processed/repurposing_candidates.csv.gz
```

**結果檔案**：`data/processed/repurposing_candidates.csv.gz`

輸出的候選數、涉及藥物數、潛在新適應症數用這行查（2026-11-05 起不在這裡寫死數字；現行 Release 的值見 `docs/_data/prediction_stats.json` 的 kg_candidates、kg_drugs、kg_diseases）：

```bash
python3 -c "import pandas as pd;c=pd.read_csv('data/processed/repurposing_candidates.csv.gz');print(len(c),c['藥物成分'].nunique(),c['潛在新適應症'].nunique())"
```

---

### 步驟 6（選用）：深度學習方法

深度學習方法需要額外環境設定，請告知使用者：

1. 需要手動下載模型檔案：[Google Drive](https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj)
2. 需要設定 Conda 環境（Python 3.11 + PyTorch + DGL）
3. 執行時間較長（數小時）且需要 16GB+ RAM

詳細步驟請參考 README.md「步驟 6、7」。

### 步驟 7：整合 KG 和 DL 預測結果

當 KG 和 DL 預測都完成後，執行整合腳本：

```bash
uv run python scripts/integrate_predictions.py --dl-threshold 0.9

# 驗證
ls data/processed/integrated_predictions.csv.gz data/processed/integration_stats.json
```

**結果檔案**：
- `data/processed/integrated_predictions.csv.gz` - 整合後的預測結果（gzip 壓縮的 CSV；`scripts/integrate_predictions.py` 的 OUTPUT_FILE）
- `data/processed/integration_stats.json` - 統計摘要

**整合統計（2026-03-04）**：下面兩張表是 2026-03-04 執行 `integrate_predictions.py --dl-threshold 0.9` 時的 `integration_stats.json`（commit e4dd734e5 記下），數字照當時紀錄、不更新；之後整合方式改過（現行 Release 的 integration_stats.json 也收 DL 分數低於 0.9 的配對，by_confidence 有 low、medium），現行 Release 的值用這行查（先還原本站 Release 的 data/）：

```bash
python3 -c "import json;print(json.load(open('data/processed/integration_stats.json')))"
```

| 指標 | 數值 |
|------|------|
| 總預測數 | 3,452,680 |
| 唯一藥物 | 1,484 |
| 唯一適應症 | 10,497 |
| 台灣藥品許可證 | 17,842 |

**信心度分布**：

| 信心度 | 來源 | 筆數 | 說明 |
|--------|------|------|------|
| very_high | KG + DL | 87,401 | 兩種方法都支持，DL score ≥ 0.9 |
| high | DL only | 3,310,352 | 僅 DL 支持，score ≥ 0.9 |
| medium | KG only | 54,927 | 僅 KG 支持 |

---

## 常用命令

```bash
# 執行所有測試
uv run pytest tests/ -v

# 處理 FDA 資料
uv run python scripts/process_fda_data.py

# 準備詞彙表資料
uv run python scripts/prepare_external_data.py

# 執行知識圖譜方法
uv run python scripts/run_kg_prediction.py

# 執行深度學習方法（需 conda 環境）
conda activate txgnn
python scripts/run_txgnn_prediction.py

# 整合 KG 和 DL 預測結果
uv run python scripts/integrate_predictions.py --dl-threshold 0.9

# 執行藥品映射發現（提高映射率）
RXNORM_MAX_QUERIES=10000 uv run python scripts/build_rxnorm_synonyms.py
PUBCHEM_MAX_QUERIES=10000 uv run python scripts/build_pubchem_mapping.py
CHEMBL_MAX_QUERIES=10000 uv run python scripts/build_chembl_mapping.py
```

## 藥品映射發現 SOP

當需要提高藥品映射率時，請參考 [映射發現 SOP](docs/sop/mapping-discovery.md)。

**快速流程**：
1. 執行 API 查詢（RxNorm/PubChem/ChEMBL）
2. 驗證映射目標存在於 DrugBank
3. 整合到 `src/twtxgnn/mapping/drugbank_mapper.py` 的 `synonym_map`
4. 重跑 `run_kg_prediction.py` 驗證改善

## 首頁圖表資料維護

當需要更新首頁 D3 圖表資料時，請參考 [圖表資料維護 SOP](docs/sop/chart-data-maintenance.md)。

### 關鍵檔案

| 檔案 | 用途 |
|------|------|
| `docs/_data/drug_stats.json` | D3 圖表資料來源 |
| `docs/_includes/d3-charts.html` | D3 圖表程式碼 |

### 快速更新 NCT 數量

當藥物頁面更新後，需重新計算臨床試驗數量：

```python
import json, re
from pathlib import Path

with open('docs/_data/drug_stats.json') as f:
    stats = json.load(f)

for drug in stats['all_drugs']:
    md = Path(f"docs/_drugs/{drug['slug']}.md")
    if md.exists():
        drug['nct_count'] = len(set(re.findall(r'NCT\d+', md.read_text())))

with open('docs/_data/drug_stats.json', 'w') as f:
    json.dump(stats, f, indent=2, ensure_ascii=False)
```

## 專案結構

```
TwTxGNN/
├── README.md                    # 完整說明文件
├── CLAUDE.md                    # 本文件
├── pyproject.toml               # Python 套件設定
│
├── data/                        # 資料目錄（需下載）
│   ├── node.csv                 # TxGNN 節點資料
│   ├── kg.csv                   # TxGNN 知識圖譜
│   ├── edges.csv                # TxGNN 邊資料（深度學習用）
│   ├── raw/
│   │   └── tw_fda_drugs.json    # 台灣 FDA 藥品資料
│   ├── external/                # 由 prepare_external_data.py 產生
│   │   ├── drugbank_vocab.csv
│   │   ├── disease_vocab.csv
│   │   └── drug_disease_relations.csv
│   └── processed/               # 預測結果
│       ├── repurposing_candidates.csv  # 知識圖譜方法結果
│       └── txgnn_dl_predictions.csv    # 深度學習方法結果
│
├── docs/                        # Jekyll 文件網站
│
├── scripts/                     # 執行腳本
│   ├── process_fda_data.py      # 處理 FDA 資料
│   ├── prepare_external_data.py # 準備詞彙表資料
│   ├── run_kg_prediction.py     # 執行知識圖譜方法
│   └── run_txgnn_prediction.py  # 執行深度學習方法
│
├── src/twtxgnn/                 # 核心程式碼
└── tests/                       # 測試程式
```

## 資料流程

```
FDA ZIP 檔案 (手動下載)         TxGNN 資料 (node.csv, kg.csv)
        ↓                               ↓
   process_fda_data.py           prepare_external_data.py
        ↓                               ↓
   tw_fda_drugs.json             data/external/ (詞彙表)
        ↓                               ↓
        └───────────────────────────────┘
                        ↓
               run_kg_prediction.py
                        ↓
           repurposing_candidates.csv.gz
```

## 疑難排解

### 找不到 tw_fda_drugs.json
1. 先手動下載 FDA ZIP 檔案到 `data/raw/` 目錄：
   https://data.fda.gov.tw/data/opendata/export/36/json
2. 執行 `uv run python scripts/process_fda_data.py` 處理 ZIP 檔案

### 找不到 drugbank_vocab.csv 等檔案
執行 `uv run python scripts/prepare_external_data.py` 產生詞彙表。

### 找不到 node.csv / kg.csv
請先下載 TxGNN 資料：
- node.csv: https://dataverse.harvard.edu/api/access/datafile/7144482
- kg.csv: https://dataverse.harvard.edu/api/access/datafile/7144484

### 測試失敗
確認已執行 `uv sync` 安裝依賴。

## 藥品覆蓋率改善

提升台灣 FDA 藥品成分到 DrugBank 的映射成功率，以增加老藥新用候選數量。

### 改善歷程

| 日期 | 改善方向 | 映射成功率 | 成功映射成分 | DrugBank 藥物 |
|------|----------|-----------|-------------|--------------|
| 2026-03-02 | 基準線 | 46.4% | 1,632 | 1,392 |
| 2026-03-02 | 方向 1：擴充同義詞映射 | 49.3% | 1,731 (+99) | 1,411 (+19) |
| 2026-03-03 | 方向 3：RxNorm API 橋接 | 51.0% | 1,791 (+60) | 1,434 (+23) |

### 三個改善方向

#### 方向 1：擴充同義詞映射 ✅

手動新增常見藥物名稱變體到 `synonym_map`：
- 維生素變體（THIAMINE → VITAMIN B1）
- 鹽類/水合物後綴（MONOHYDRATE、DIHYDRATE 等）
- 藥典標準後綴（USP、BP、JP、EP）

#### 方向 2：分析未映射成分 ✅

執行分析腳本找出改善潛力：
```bash
uv run python scripts/analyze_unmapped_ingredients.py
```

產出：
- `data/processed/unmapped_ingredients.csv` - 未映射成分清單
- `data/processed/potential_mappings.csv` - 潛在可映射清單

#### 方向 3：RxNorm API 橋接 ✅

使用 RxNorm API 自動發現同義詞：
```bash
uv run python scripts/build_rxnorm_synonyms.py
```

產出：
- `data/external/rxnorm_cache.json` - API 查詢快取
- `data/processed/rxnorm_mappings.json` - 新發現的映射

### 未映射成分分析

剩餘 1,723 個未映射成分，主要類型：

| 類型 | 數量 | 說明 |
|------|------|------|
| 中草藥/植物萃取物 | 159 | EXTRACT、RADIX、HERBA 等，DrugBank 不收錄 |
| 疫苗/生物製劑 | ~50 | TOXOID、ANTIGEN、VACCINE 等 |
| 賦形劑/輔料 | ~100 | POWDER、OIL、WATER 等 |

這些成分在 DrugBank 中不存在，無法透過同義詞映射解決。

### 相關檔案

- `src/twtxgnn/mapping/drugbank_mapper.py` - 主要映射邏輯與 synonym_map
- `src/twtxgnn/mapping/rxnorm_bridge.py` - RxNorm API 橋接模組
- `scripts/analyze_unmapped_ingredients.py` - 未映射成分分析
- `scripts/build_rxnorm_synonyms.py` - RxNorm 同義詞發現

---

## 藥物交互作用 (DDI) 資料維護

專案使用兩個公開 DDI 資料來源，**建議每季更新一次**：

### 資料來源

| 來源 | 網址 | 涵蓋範圍 |
|------|------|----------|
| DDInter | https://ddinter2.scbdd.com | 網站統計 302,516 DDI、2,310 藥物（DDInter 2.0 網站自己的數字）；本站用的下載檔 `ddinter_code_*.csv` 的列數、配對數、藥名數見下方查詢指令 |
| Guide to PHARMACOLOGY | https://www.guidetopharmacology.org/download.jsp | 核准藥物的藥物–標靶資料（不是 DDI） |

### 更新 DDI 資料

```bash
# 建立目錄
mkdir -p data/external/ddi/ddinter
mkdir -p data/external/ddi/pharmacology

# 下載 Guide to PHARMACOLOGY（直接下載）
curl -L -o data/external/ddi/pharmacology/approved_drug_detailed_interactions.csv \
  "https://www.guidetopharmacology.org/DATA/approved_drug_detailed_interactions.csv"

# DDInter 需從網站手動下載：
# 1. 訪問 https://ddinter2.scbdd.com/download/（1.0 的 ddinter.scbdd.com/download/ 提供同一組檔案）
# 2. 下載 8 個 ddinter_downloads_code_{A,B,D,H,L,P,R,V}.csv
# 3. 改名為 ddinter_code_{A,...}.csv，放置到 data/external/ddi/ddinter/
```

### 資料檔案結構

```
data/external/ddi/
├── ddinter/                    # DDInter 下載檔
│   └── ddinter_code_*.csv      # DDI 資料集（8 檔，依 ATC 分類）
└── pharmacology/               # Guide to PHARMACOLOGY 資料
    └── approved_drug_detailed_interactions.csv  # 核准藥物的藥物–標靶資料
```

### 上次更新時間

- DDInter 下載檔: 2026-02-08（8 個 `ddinter_code_*.csv`，每檔第一行是標題列）。1.0 與 2.0 下載頁提供的是同一組檔案（2026-11-05 比對位元組一致），檔案本身不標版本，所以不寫版本號
- Guide to PHARMACOLOGY: 檔案第一行是版本註記（版本與發布日），第二行是標題列；2026-11-05 經 replace-gtopdb.yml 換進 Release（哪一版見 site_data 的 gtopdb_release），藥物報告尚未用新版重產
- 現在的筆數、版本（2026-11-05 起不在這裡寫死）記在 `.github/ddi-versions.json` 的 site_data，網站頁面經 `scripts/sync_ddi_sources.py` 讀同一份；查目前記的值：

  ```bash
  python3 -c "import json;sd=json.load(open('.github/ddi-versions.json'))['site_data'];print({k:v for k,v in sd.items() if not k.endswith(('note','files'))})"
  ```

  要從資料檔重算，照 site_data.note 裡每個欄位的指令跑（先還原本站 Release 的 data/）。

> **提醒**：DDI 資料會定期更新，建議每季檢查是否有新版本。

---

## SMART on FHIR 整合維護

### 功能概述

TwTxGNN 提供 SMART on FHIR 整合，包含：

1. **SMART App**：從 EHR 讀取病患用藥，查詢老藥新用候選
2. **FHIR API**：將預測結果以 FHIR 格式提供

### 檔案結構

```
docs/
├── smart/
│   ├── index.md          # 說明頁面
│   ├── launch.html       # OAuth 啟動端點
│   ├── app.html          # 主應用程式
│   └── standalone.html   # 獨立測試模式
├── fhir/
│   ├── metadata          # CapabilityStatement
│   ├── MedicationKnowledge/   # 藥物資源 (189 個)
│   ├── ClinicalUseDefinition/ # 預測適應症 (1267 個)
│   └── Bundle/
│       └── all-predictions.json
└── assets/js/
    ├── smart-app.js          # SMART App 主邏輯
    └── smart-fhir-mapper.js  # 藥物名稱映射
```

### 常用命令

```bash
# 重新生成 FHIR 資源（當 search-index.json 更新後）
uv run python scripts/generate_fhir_resources.py

# 驗證 FHIR 資源數量
ls docs/fhir/MedicationKnowledge/ | wc -l
ls docs/fhir/ClinicalUseDefinition/ | wc -l
```

### 測試 SMART App

1. 前往 [SMART Launcher](https://launch.smarthealthit.org/)
2. 設定：
   - Launch Type: Provider EHR Launch
   - FHIR Version: R4
   - App Launch URL: `https://twtxgnn.yao.care/smart/launch.html`
3. 選擇測試病患並啟動

### 獨立測試模式

不需 EHR 即可測試：`https://twtxgnn.yao.care/smart/standalone.html`

### SMART App 技術規格

| 項目 | 值 |
|------|------|
| FHIR 版本 | R4 |
| Client ID | `twtxgnn-smart-app` |
| 授權方式 | OAuth 2.0 with PKCE |
| 請求權限 | `launch`, `patient/Patient.read`, `patient/MedicationRequest.read`, `patient/MedicationStatement.read`, `openid`, `fhirUser` |

### 藥物映射流程

```
EHR MedicationRequest
    │
    ├─ 提取 RxCUI (RxNorm 代碼)
    │
    ├─ RxNorm API 查詢成分名
    │   GET https://rxnav.nlm.nih.gov/REST/rxcui/{rxcui}/related.json?tty=IN
    │
    ├─ 名稱正規化（移除鹽類後綴、同義詞對照）
    │
    └─ Fuse.js 模糊比對 search-index.json
```

### 疑難排解

#### SMART App 無法啟動

1. 確認從 EHR 系統或 SMART Launcher 啟動
2. 檢查瀏覽器 console 是否有 CORS 錯誤
3. 確認 `search-index.json` 可正常載入

#### 藥物映射失敗

1. 確認藥物名稱為英文
2. 檢查 RxNorm API 是否可用
3. 嘗試在獨立測試模式手動輸入藥物名稱測試

#### FHIR 資源過期

當 `search-index.json` 更新後，需重新生成 FHIR 資源：

```bash
uv run python scripts/generate_fhir_resources.py
```

---

## 健康新聞監測系統維護

### 系統架構

```
synonyms.json (手動維護)     search-index.json (藥物資料庫)
         │                            │
         └────────────┬───────────────┘
                      ▼
       generate_news_keywords.py
       (產生只有藥物連結的關鍵字)
                      │
                      ▼
              keywords.json (自動產生，勿手動編輯)
                      │
                      ▼
              process_news.py
              (匹配新聞、產生頁面)
                      │
                      ▼
        matched_news.json + docs/_news/*.md
```

### 重要原則

1. **`keywords.json` 是自動產生的**，不要手動編輯
2. **只有在資料庫中有相關藥物的關鍵字才會被納入**
3. **在源頭過濾，而非下游補救**

### 維護操作對照表

| 需求 | 編輯檔案 | 執行指令 |
|------|----------|----------|
| 新增疾病中文同義詞 | `data/news/synonyms.json` | `uv run python scripts/generate_news_keywords.py` |
| 新增通用關鍵字模式 | `scripts/generate_news_keywords.py` | `uv run python scripts/generate_news_keywords.py` |
| 新增新聞來源 | `scripts/fetchers/` | 新增 fetcher 腳本 |
| 手動更新新聞 | - | `uv run python scripts/fetchers/google_rss.py && uv run python scripts/process_news.py` |

### 新增疾病同義詞

編輯 `data/news/synonyms.json`：

```json
{
  "indication_synonyms": {
    "diabetes mellitus": ["糖尿病", "血糖高", "糖尿"],
    "hypertension": ["高血壓", "血壓高"],
    // ... 新增其他同義詞
  }
}
```

然後執行：

```bash
uv run python scripts/generate_news_keywords.py
cp data/news/keywords.json docs/data/keywords.json
```

**注意**：如果 `search-index.json` 中沒有藥物預測該適應症，該同義詞不會被納入 `keywords.json`。

### 新增通用關鍵字模式

若需要將多個預測適應症歸類到同一個通用關鍵字（如「癌症」對應所有 cancer/carcinoma/tumor），編輯 `scripts/generate_news_keywords.py` 中的 `GENERIC_KEYWORD_PATTERNS`：

```python
GENERIC_KEYWORD_PATTERNS = {
    "_generic_cancer": [
        "cancer", "carcinoma", "tumor", "tumour", "neoplasm", "malignant",
        "leukemia", "lymphoma", "melanoma", "sarcoma", "myeloma"
    ],
    # ... 新增其他模式
}
```

### 排程工作流程

新聞監測由 GitHub Actions 每小時自動執行：

- 工作流程：`.github/workflows/news-monitor.yml`
- 執行時間：每小時整點
- 注意：排程推送不會自動觸發 Jekyll 部署，需手動執行 `gh workflow run "Deploy Jekyll to GitHub Pages"`

### 疑難排解

#### 新聞匹配到但沒有藥物連結

1. 檢查 `synonyms.json` 中是否有該疾病的同義詞
2. 檢查 `search-index.json` 中是否有藥物預測該適應症
3. 若資料庫中無相關藥物，該新聞會被自動過濾

#### 新聞頁面未更新

排程工作流程使用 GITHUB_TOKEN 推送，不會觸發 Jekyll 部署：

```bash
# 手動觸發部署
gh workflow run "Deploy Jekyll to GitHub Pages"
```

---

## Jekyll 文件撰寫規範

產生 `docs/` 目錄下的 Jekyll 內容時，**必須遵守以下規則**：

### 必須使用
- **標準 Markdown 語法**：表格、粗體、連結、標題等
- **內嵌 HTML/CSS**：需要自訂樣式時，使用完整的 `<style>` 區塊
- **Jekyll Liquid 語法**：`{{ '/path/' | relative_url }}` 等

### 禁止使用
- **Kramdown 特有屬性語法**：`{: .class-name }`, `{: .text-green-300 }` 等
- **主題特定的 CSS 類別**：除非已驗證可正常運作
- **未經測試的複雜格式**

### 原因
Kramdown 屬性語法在某些情況下不會被正確處理，會直接顯示為原始文字（如 `{: .note-title }`），造成頁面呈現異常。

### 範例

**錯誤做法：**
```markdown
這是重點內容
{: .text-green-300 .fw-500 }
```

**正確做法：**
```markdown
**這是重點內容**
```

或使用內嵌 HTML：
```html
<span style="color: green; font-weight: 500;">這是重點內容</span>
```

---

## 任務完成品質關卡

**每當完成任務並說「完成」時，必須先執行以下檢查，全部通過才能回報完成。**

### 任務開始時

接到新任務時，先建立本次檢查清單：

```
## 本次任務檢查清單

- 任務目標：[描述]
- 預計修改檔案：
  - [ ] 檔案1
  - [ ] 檔案2
- 預計新增內容：
  - [ ] 內容1
  - [ ] 內容2
- 適用的條件式檢查：[列出]
- 是否涉及 docs/ 目錄：是/否
- 是否為 YMYL 內容：是（本專案涉及藥物/健康）
```

---

### 1. 連結檢查

- [ ] 所有新增/修改的內部連結正常，無 404
- [ ] 所有新增/修改的外部連結正常
- [ ] 無死連結或斷裂連結

---

### 2. 內容更新確認

- [ ] 列出本次預計修改的所有檔案
- [ ] 逐一確認每個檔案都已正確更新
- [ ] 修改內容與任務要求一致
- [ ] 所有表格正常渲染（HTML/Markdown 表格有邊框、對齊正確）
- [ ] D3.js 圖表呈現正常（若頁面有使用）
- [ ] 無遺漏項目

---

### 3. Git 狀態檢查

- [ ] 所有變更已 commit
- [ ] commit message 清楚描述本次變更
- [ ] 已 push 到 Github（除非另有指示）
- [ ] 遠端分支已更新

---

### 4. SOP 完成度檢查

- [ ] 回顧原始任務需求
- [ ] 原訂 SOP 每個步驟都已執行
- [ ] 無遺漏的待辦項目
- [ ] 無「之後再處理」的項目

---

### 5. YMYL 檢查（本專案必檢）

本專案涉及藥物/健康內容，屬於 YMYL（Your Money Your Life）類型：

- [ ] 內容標註「僅供研究參考，不構成醫療建議」
- [ ] 預測結果需標註「需經臨床驗證」
- [ ] 藥物資訊來源已標註（如 TxGNN、FDA）

---

### 6. docs/ 目錄 SEO 檢查（僅適用於 docs/ 修改）

若本次任務涉及 `docs/` 目錄，需額外執行以下檢查：

#### 6.1 Meta 標籤

- [ ] `<title>` 存在且 ≤ 60 字，含核心關鍵字
- [ ] `<meta name="description">` 存在且 ≤ 155 字
- [ ] `og:title`, `og:description`, `og:image`, `og:url` 存在
- [ ] `og:type` = "article"
- [ ] `article:published_time`, `article:modified_time` 存在（ISO 8601 格式）
- [ ] `twitter:card` = "summary_large_image"

#### 6.2 JSON-LD Schema（依內容判斷）

| Schema | 觸發條件 | 必填欄位 |
|--------|----------|----------|
| Article | 所有文章頁 | author, datePublished, dateModified |
| BreadcrumbList | 所有頁面 | position 從 1 開始連續編號 |
| FAQPage | 有 Q&A 內容 | 3-5 個 Question + Answer |
| HowTo | 有步驟教學 | step, totalTime |

#### 6.3 SGE/AEO 標記（AI 引擎優化）

| 標記 | 要求 |
|------|------|
| `.key-answer` | 每個 H2 必須有，含 `data-question` 屬性 |
| `.key-takeaway` | 文章重點摘要（2-3 個） |
| `.expert-quote` | 專家引言（至少 1 個） |
| `.actionable-steps` | 行動步驟清單 |
| `.comparison-table` | 比較表格（若有） |

#### 6.4 E-E-A-T 信號

- [ ] 作者資訊完整（專業背景、認證）
- [ ] 至少 2 個高權威外部連結（.gov、學術期刊、專業協會）

---

### 檢查報告格式

完成檢查後，輸出以下格式：

```
## 完成檢查報告

| 類別 | 狀態 | 問題（如有） |
|------|------|-------------|
| 連結檢查 | ✅/❌ | |
| 內容更新 | ✅/❌ | |
| Git 狀態 | ✅/❌ | |
| SOP 完成度 | ✅/❌ | |
| YMYL 檢查 | ✅/❌ | |
| SEO 檢查 | ✅/❌/N/A | |

**總結**：X/Y 項通過，狀態：通過/未通過
```

---

### 檢查未通過時

1. **不回報完成**
2. 列出所有未通過項目
3. 立即修正問題
4. 重新執行檢查
5. 全部通過才能說「完成」

---

## docs/ 目錄 SEO/AEO 完整規則

> **適用範圍**：僅適用於 `docs/` 目錄下的 Jekyll 頁面

### JSON-LD Schema 類型定義

#### 必填 Schema（適用於所有 docs/ 頁面）

##### 1. Article

```json
{
  "@type": "Article",
  "@id": "{{CANONICAL_URL}}#article",
  "headline": "{{TITLE}}",
  "description": "{{META_DESCRIPTION}}",
  "author": { "@type": "Person", "name": "{{AUTHOR_NAME}}" },
  "datePublished": "{{PUBLISHED_DATE}}",
  "dateModified": "{{MODIFIED_DATE}}",
  "publisher": {
    "@type": "Organization",
    "name": "TwTxGNN",
    "url": "{{SITE_URL}}"
  },
  "isAccessibleForFree": true
}
```

##### 2. BreadcrumbList

```json
{
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "首頁", "item": "{{SITE_URL}}" },
    { "@type": "ListItem", "position": 2, "name": "{{SECTION}}", "item": "{{SECTION_URL}}" },
    { "@type": "ListItem", "position": 3, "name": "{{TITLE}}", "item": "{{CANONICAL_URL}}" }
  ]
}
```

#### 條件式 Schema

| Schema | 觸發條件 | 必填欄位 |
|--------|----------|----------|
| FAQPage | 有 Q&A 內容 | mainEntity（3-5 個 Question） |
| HowTo | 有步驟教學 | step, totalTime |
| ItemList | 有排序清單 | itemListElement |
| Table | 有比較表格 | about, description |

---

### Meta 標籤規範

```html
<title>{{TITLE}}（含關鍵字，60字內）</title>
<meta name="description" content="{{DESCRIPTION}}（155字內，含關鍵字）" />
<link rel="canonical" href="{{CANONICAL_URL}}" />

<!-- Open Graph -->
<meta property="og:title" content="{{TITLE}}" />
<meta property="og:description" content="{{DESCRIPTION}}" />
<meta property="og:image" content="{{OG_IMAGE}}" />
<meta property="og:url" content="{{CANONICAL_URL}}" />
<meta property="og:type" content="article" />
<meta property="article:published_time" content="{{PUBLISHED_DATE}}" />
<meta property="article:modified_time" content="{{MODIFIED_DATE}}" />

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{{TITLE}}" />
<meta name="twitter:description" content="{{DESCRIPTION}}" />
<meta name="twitter:image" content="{{OG_IMAGE}}" />
```

---

### SGE/AEO 標記規範

#### HTML Class 標記

| 標記 | CSS Class | 用途 | 範例 |
|------|-----------|------|------|
| **關鍵答案** | `.key-answer` | 每個 H2 開頭的直接答案 | `<p class="key-answer" data-question="什麼是老藥新用">老藥新用是指...</p>` |
| **重點摘要** | `.key-takeaway` | 文章核心要點 | `<div class="key-takeaway">重點：...</div>` |
| **專家引言** | `.expert-quote` | 帶署名的引用 | `<blockquote class="expert-quote">...</blockquote>` |
| **行動步驟** | `.actionable-steps` | 可執行的步驟清單 | `<ol class="actionable-steps">...</ol>` |
| **比較表格** | `.comparison-table` | 結構化比較資訊 | `<table class="comparison-table">...</table>` |

#### .key-answer 使用規則

```html
<h2>什麼是老藥新用？</h2>
<p class="key-answer" data-question="什麼是老藥新用">
  <strong>老藥新用（Drug Repurposing）</strong>是將已核准的藥物應用於新的適應症。
</p>
```

---

### E-E-A-T 信號要求

#### 作者資訊

- `knowsAbout`：至少 2 個專長領域
- `hasCredential`：至少 1 個認證/資格（若有）
- `sameAs`：至少 1 個社群連結（若有）

#### 權威來源連結

文章必須包含至少 2 個高權威外部連結：

| 優先級 | 來源類型 | 範例 |
|--------|----------|------|
| 1 | 政府機構 | 衛福部、FDA、.gov |
| 2 | 學術期刊 | PubMed、DOI 連結 |
| 3 | 專業資料庫 | DrugBank、TxGNN |

---

### YMYL 免責聲明（本專案必用）

所有涉及藥物/健康內容的頁面必須包含：

```html
<div class="disclaimer">
  <strong>免責聲明</strong>：本網站內容僅供研究參考，不能取代專業醫療建議。
  所有藥物再利用預測結果需經過臨床驗證才能應用。如有健康問題，請諮詢合格醫療人員。
</div>
```

#### YMYL 專屬欄位

| 欄位 | 說明 | 格式 |
|------|------|------|
| `lastReviewed` | 最後審核日期 | ISO 8601（如 2026-02-19） |
| `reviewedBy` | 審核者資訊 | Person 名稱 + 資格 |

---

### SEO 檢查清單

#### 關鍵字優化

- [ ] 標題（H1/title）包含核心關鍵字
- [ ] 第一段（前 100 字）包含關鍵字
- [ ] H2 標題自然融入關鍵字
- [ ] 包含 3-5 個語意相關詞

#### 結構優化

- [ ] H1 唯一且包含關鍵字
- [ ] H2 數量 4-6 個
- [ ] 段落長度 150-300 字

#### 連結優化

- [ ] 內部連結 3+ 個
- [ ] 外部權威連結 2+ 個
- [ ] 無斷裂連結

#### 圖片優化

- [ ] 所有圖片有 alt 文字
- [ ] 首屏圖片 `loading="eager"`
- [ ] 非首屏圖片 `loading="lazy"`

#### URL 優化

- [ ] URL slug 使用英文小寫
- [ ] URL slug 使用連字號（-）分隔
- [ ] URL slug 包含核心關鍵字

---

### 驗證方式

將完成的 JSON-LD 貼入以下工具驗證：
- Google Rich Results Test: https://search.google.com/test/rich-results
- Schema Markup Validator: https://validator.schema.org/

---

## 參考文件

完整 SEO/AEO 規則請參照：
- `/Users/lightman/weiqi.kids/agent.idea/seo/CLAUDE.md` - SEO + AEO 規則庫
- `/Users/lightman/weiqi.kids/agent.idea/seo/writer/CLAUDE.md` - Writer 執行流程
- `/Users/lightman/weiqi.kids/agent.idea/seo/review/CLAUDE.md` - Reviewer 檢查清單

---

## 注意事項

- 本專案結果僅供研究參考，不構成醫療建議
- 老藥新用候選需經過臨床驗證才能應用
- DDI 資料需定期更新以確保準確性
- 所有 docs/ 頁面需包含 YMYL 免責聲明

---

## 藥物頁人工查核紀錄（2026-10-03 起）

藥物頁 `docs/_drugs/*.md` 是產線生成的（`sync_notes_to_docs.py`／`build_docs.py` 會整頁覆寫）。人工對照仿單或 TFDA 許可證所做的更正、加註、待重審標記、附來源的作用機轉段，**一律記在 `docs/_data/drug_reviews.json`**，由 `scripts/apply_drug_reviews.py` 套到頁面（頁面上以「查核更正／查核加註／待重審」引言框與每頁「查核紀錄」表呈現）。

- 兩支生成腳本結尾會自動重套；其他會改寫藥物頁的腳本跑完後，手動跑 `python3 scripts/apply_drug_reviews.py`。
- `python3 scripts/check_seo_docs.py` 會擋下「紀錄沒套在頁面上」的情況。
- 原則：基本藥理事實照仿單或許可證更正；模型預測原文一律不刪不改寫，只加註；證據等級與決策只能經下方重審機制變更。之後補的藥沿用同一份 JSON。
- 重審（2026-10-03 起）：「待重審」的預測依 `docs/methodology.md` 的 L1–L5 定義重審（扣掉錯誤前提看剩餘理由；PubMed、ClinicalTrials.gov 正反證據都查，查無結果的查詢記在 `searches`），結論寫成 `action: rereview_result`，用 `resolves` 指回原 rereview（原紀錄改標 `status: rereviewed` 保留）。頁面上「待重審」框原位換成「重審結果」框（維持／降級／升級／撤回、原等級→新等級、理由、文獻）。只有降級、升級或撤回才用 `table_updates` 改頁面上該適應症的等級／決策儲存格，原值留在紀錄並列在查核紀錄表。升級（2026-10-16 起，用戶核准）只限重審找到符合 methodology 定義、可查證（PMID／NCT）的本藥證據，而頁面等級低於該定義的情形。
- 頁首等級（2026-10-04 起全站）：每頁的 front matter `evidence_level`、`parent` 與頁首「證據等級」列＝快速總覽「證據等級」列的最高等級（同格多個等級取數字最小者；該列沒有 Lx 就不動）。規則在 `src/twtxgnn/regulatory/page_format.py`，產線 `process_for_site()` 與 `apply_drug_reviews.py` 都套；`sync_notes_to_docs.py`／`build_docs.py` 的解析式已改成整格取最高等級（舊式只認純值儲存格，帶說明文字就落到預設 L5）。頁首有變動的頁在 `drug_reviews.json` 各有一筆 `action: header_level`（原值 `original_level`／`original_parent`），查核紀錄表顯示「頁首等級依總覽表重算（原 Lx→Ly）」。
- 主預測撤回→N/A（2026-11-03 用戶決定）：重審撤回把快速總覽「證據等級」格換成「撤回：…」後，頁首改取本頁其他預測表（表頭有「證據等級」欄的表）保留的最高等級，沒有就是 N/A、parent 歸 known-uses 列表頁（標題「僅已知用途／主預測已撤回」，清單依 `header_level` 的 `trigger: withdraw` 用 Liquid 標「主預測已撤回」；改標題時所有 N/A 頁的 parent 要一起改）（不解析敘述文字裡的等級）。規則同在 `page_format.py`（`target_level`），頁首有變動的頁記 `action: header_level`＋`trigger: withdraw`、`based_on`；「結論與下一步」的決策段另加查核加註。front matter description 只能經 `action: description_level` 紀錄改：只把「證據等級 Lx」換成目前頁首等級（N/A 頁換成「僅已知用途」），其他文字不動，原文記在 `original_description`；gate 第 7 項會擋 description 等級與頁首不一致。verdict=withdraw 的預測不進證據監測：`scripts/extract_drug_list.py` 依 `drug_reviews.json` 的 `known_use_exclusion[].predicted`／`withdrawn_predictions` 排除，front matter `predicted_indications` 不動；同一份名單（`src/twtxgnn/regulatory/withdrawn.py`）也讓 `generate_search_index.py`（含 `--levels-from-pages`）與 `generate_fhir_resources.py`（只清撤回預測用 `--prune-withdrawn`）不發布撤回的預測，gate 第 7d 項檢查。
- 表格前空行：表格第一列前面不是空行時，kramdown 會把整張表排成純文字；後處理（`page_format.fix_table_spacing`）自動補。
- 吃等級的衍生檔都從藥物頁頁首重算，頁面重產後要一起跑：`scripts/generate_drug_stats.py`（`docs/_data/drug_stats.json`，首頁圖表）、`scripts/generate_data_exports.py`（`docs/data/drugs*.json/csv`）、`scripts/generate_download_data.py`（`docs/downloads/`）、`scripts/build_lookup_pages.py`（`tw-availability.md`、`nct-lookup.md`）、`scripts/generate_search_index.py --levels-from-pages`（搜尋索引的藥物層等級）；`scripts/generate_fhir_resources.py --sync-from-files`（FHIR MedicationKnowledge 等級對頁首、拿掉 noindex／轉址頁的藥、Bundle 與 metadata 數字對實際檔案，2026-11-03 起，gate 第 7e 項檢查）；新聞頁由新聞排程依 `docs/data/drugs.json` 重產。公開頁面上的藥物總數與等級分布數字一律用 Liquid 讀 `site.data.drug_stats`（`total_drugs`、`level_counts`），不要手寫；不能用 Liquid 的地方（front matter `description`、ld+json `numberOfItems`、`README.md`、`CITATION.cff` 等）列在 `scripts/generate_drug_stats.py` 的 `COUNT_SPOTS`，由該腳本改寫，gate 第 7c 項檢查。新增這類數字時要嘛用 Liquid，要嘛加進 `COUNT_SPOTS`。
- 同 id 重發的紀錄：前版整筆存進該筆的 `history`（`retired`、`reason`），不覆蓋丟棄；頁面停在前版更正文字時，套用會把它換成新版。
- 待查清單 `docs/_data/drug_reviews_uncertain.json` 的項目不刪：查清標 `status: resolved`（附 `record_ids`），查不出定論標 `status: unresolvable`（附 `searched`、`unresolvable_reason`）。
- 2026-11-12 正文張數對 TFDA 快照再掃一次：oxytetracycline 兩句（「有效許可證僅 1 張口服膠囊」，實際 3 張含 1 張皮膚外用軟膏）以 `oxytetracycline-*-2026-11-12` 更正；`urea-dpp4-not-urea-derivative-2026-10-03` 同 id 重發（更正文字的「上表 4 張」在程式化許可證表依主成分比對後已不成立）。其餘「N 張」敘述由 `page_postprocess.rewrite_count_prose` 產生，跟快照一致。

## 藥物頁許可證表與張數：程式產生（2026-10-03 起）

- 「許可證數」與「台灣上市資訊」的許可證表，一律由 `src/twtxgnn/regulatory/tfda_licenses.py` 依 TFDA「全部藥品許可證資料集」（`data/raw/tw_fda_drugs.json`，由 `scripts/process_fda_data.py` 產生）確定性產生：張數＝不重複字號數，分有效單方／有效複方／已註銷，不設上限；比對規則看該檔開頭說明（主成分比對，不用全文子字串）。LLM 只拿結構化結果，prompt 裡許可證表是佔位，不准自行列字號。
- 產線寫頁前一律走 `src/twtxgnn/regulatory/page_postprocess.py` 的 `process_for_site()`：清 LLM 開場白與「Evidence Pack」用語 → 替換許可證表與「許可證數」列 → 套查核紀錄 → 改寫其他「N 張許可證」敘述 → 驗證頁面上每個許可證字號都屬於這個藥；不符就不寫該頁。
- `llm_client.py` 呼叫 `claude -p` 時帶 `--disable-slash-commands --setting-sources ""`（不載技能與設定），回應再過 `clean_response()`。
- 既有頁面重產：`python3 scripts/regenerate_tfda_tables.py --data-date <資料集檔案日期>`（可重複執行）；它同時更新 `snapshots/tfda_licenses.json.gz`（gate 與沒有資料集時的產線用）。
- 每週排程自動重產（2026-11-24 用戶決定）：以前這步要人手動跑，頁面停在 2026-09-29 資料集，check-new-evidence 每次 TFDA 更新都開一批 label=tfda 的「TFDA 許可證變更」issue（11-20 18 個、11-24 12 個）。
  `.github/workflows/license-refresh.yml` 在許可證排程 commit 之後跑 `scripts/tfda_regen_weekly.sh`（下載資料集 36 → process_fda_data → regenerate_tfda_tables，資料集日期取 ZIP 檔案日期 → apply_drug_reviews --check → check_seo_docs；
  資料集少於 60,000 筆、重套後仍有頁面變動、有問題項或 gate 沒過就還原頁面、開 issue），通過才 commit；接著 `scripts/close_reflected_tfda_issues.py` 逐筆確認 tfda issue 列的變更都在頁面上
  （註銷→在已註銷區、展延→有效日期相符（複方表沒有有效日期欄）、新增→字號在頁上；製造廠變更頁面不顯示；字號不屬於任何藥物頁的另註明），全部確認得到才留言關閉，確認不了的留給人看。
  2026-11-24 對當天處理的 30 個 issue 試跑判定與人工結果一致，另以錯的有效日期、頁面仍有效卻寫註銷、空內文三種假 issue 確認不會誤關。
- 查核紀錄的錨點落在被取代的許可證表或張數上時，該筆標 `status: superseded`＋`superseded_by`，紀錄保留、頁面不顯示框，查核紀錄表註明「已由程式化許可證表取代」。
- 比對用的別名（INN 別名、鹽類／酯類、放射性核種寫法、拼字變體）放在 `config/tfda_synonyms.json`，每筆附依據；只收同一個藥的寫法。改完重跑 `scripts/regenerate_tfda_tables.py`。
- gate（`scripts/check_seo_docs.py`）第 6 項會擋：不屬於該藥的許可證字號、許可證表不是程式區塊、張數與快照不符、殘留開場白或「Evidence Pack」；另外被 superseded 的查核紀錄裡確認屬於本藥的字號（`asserted_license_ids`）必須都在程式表裡——比對漏同義名時會在這裡被擋下。
- gate 第 7 項（2026-10-04 起）會擋：頁首等級不等於快速總覽最高等級、表格前面缺空行、上列衍生檔的等級與頁首不一致（或缺藥）、`COUNT_SPOTS` 裡寫死的藥物數或等級分布與 `drug_stats.json` 不符。
- 「原適應症」列的交叉驗證：`python3 scripts/check_original_indications.py`，只把可疑頁寫進 `docs/_data/drug_reviews_uncertain.json`，不改頁面。

## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 285 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「目前缺乏詳細的作用機轉資料。」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `<藥>-moa-fda-<日期>（本站 id 慣例）`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：本站語言（繁體中文）的出處句＋節錄的忠實翻譯（標明「非官方翻譯」）＋英文原文（照引、為準）＋DailyMed 連結、仿單版本、取用日期（用戶 2026-11-19 決定「當地語言摘要＋英文原文」）。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 翻譯：節錄的翻譯是 AI 輔助的忠實翻譯（不增不減，藥名、基因與受體符號、數字、「[…]」照原文），2026-11-19 批次產生，存在紀錄 sources 的 translation（translation_lang、translation_note 註明非官方、英文原文為準）；頁面上同時列英文原文。`--translations <檔>` 讀翻譯、`--need <檔>` 列出還沒翻的節錄（這些頁那次不寫紀錄，gate 會擋，翻好再跑）。
- 2026-11-19 結果：212 頁寫入紀錄（美國仿單 189、ChEMBL 23），72 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 16 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 本站 2026-10-03 起另有 10 頁以 action＝section 加的「附來源的作用機轉段」（用戶拍板例外），照舊保留；這次的 mechanism 紀錄只換「缺乏作用機轉資料」那一句，兩者並存。
- 注意：節錄的是美國仿單，劑型與適應症可能跟本站市場的產品不同（例如取到外用仿單）；文字上已寫明是美國 FDA 核准仿單。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。
- 2026-11-20 補做：程式更新：同頁不只一句「不可得」時每句各一筆紀錄（-1、-2…）；同頁別筆紀錄的更正文字、錨點與已套上的節錄不再當成「不可得」句；gate 改成公開頁仍寫「不可得」、又沒列待查就擋（不再只看該頁有沒有紀錄）；同頁第二句起補 2 筆紀錄（id 結尾 -2）；ChEMBL 譯文（詞組清單）後補句號 23 筆；同 id 重發，前版 replacement 存 history。
- 2026-11-20 試跑母目錄「交付前驗證」規則時補做：偵測改成原條件不動、另加新增寫法（L2，比中的再用 NOT 排除以缺資料為前提的模型推論），字樣用獨立、更寬的偵測全量掃出的候選句逐句標註校準（A 沒有漏、B 沒有誤中）；節錄後面接著 AI 說明「上面描述依據」的句子（會讀成美國仿單的出處）1 筆改成那句在節錄前（原文不改，只換順序）；同頁重複引用同一段節錄的 2 筆改成指向上方節錄的一句（附同一個來源連結）；以上同 id 重發，前版存 history。程式另加 reorder_src_tail、同頁已引用同一段節錄時改指向上方（產生器 txgnn/.claude/moa_rollout_20261119/fix_20261120/）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 證據包 tfda 區塊收錯的許可證移出（2026-11-25 第五輪）

用戶 2026-11-25 決定（第五輪第 1 條）：Release 的證據包（data/bundles/*/drug_bundle.json）tfda.records 有一部分是 2026-10-03 以前的收集器用全文子字串收的（成分、品名、適應症出現藥名就收）：atracurium_besylate 收到 cisatracurium 7 筆、hydroxyurea 收到適應症提到 hydroxyurea 的 ruxolitinib 8 筆、axitinib 收到 avelumab／pembrolizumab 9 筆等。頁面許可證表與張數由 tfda_licenses.py 依 TFDA 全量資料集產生（atracurium_besylate 頁的程式表本來就只有 atracurium 6 張），不受影響；證據包的 local_regulatory 是從 tfda.records 算的，會跟著錯。
- `scripts/exclude_mismatched_records.py`＋`config/bundle_record_exclusions.json`：字號在 TFDA 資料集、卻不在本藥的主成分比對結果（有頁的用 snapshots/tfda_licenses.json.gz 的該頁許可證＝頁面許可證表，沒頁的用 licenses_for_drug(drug.inn)）裡，就移到 `tfda.excluded_records`（附 excluded、excluded_reason、excluded_basis；total_matches 改成留下的不重複字號數）；config 的 keep 照留（isosorbide_mononitrate 的稀硝酸異山梨酯原料藥、conjugated_estrogens 的 3 張「CONJUGATED ESTROGENS」品名、主成分登載 OESTRONE SODIUM SULPHATE），資料集沒有的字號照留。collectors/tfda.py 10-03 起已用同一套比對；`.github/workflows/license-refresh.yml` 在 license_refresh 之前跑（有移出就照常發新 Release）。
- 套用（Release data-20261124-083842、資料集 2026-11-24）：14 個證據包移出 75 筆（axitinib 9、hydroxyurea 8、atracurium_besylate 7、durvalumab 7、enfortumab_vedotin 7、anastrozole 6、ipilimumab 6、mycophenolate_mofetil 6、palbociclib 6、ravulizumab 4、remdesivir 4、alpha-tocopherol_succinate 2〔tocopherol nicotinate〕、guaiacol 2〔tetracycline guaiacol sulfonate〕、titanium_dioxide 1〔piracetam 膠囊的賦形劑〕）；證據包 local_regulatory 重算 14 個（alpha-tocopherol_succinate 證據包原本只收到這 2 筆，重算後為 0 張；頁面依 TFDA 全量是 49 張，證據包 tfda 區塊整體仍是 10-03 前的舊收錄）。頁面、快照沒有變；checker 前後相同；gate exit 0。
- 另寫的頁面程式表全量偵測（比對到的成分名多出本藥以外的字）找到同類：scopolamine 頁含 butylscopolamine（BROMOBUTYLATE、N-BUTYLBROMIDE 等約 90 張）與 methscopolamine（METHOBROMIDE、METHYLNITRATE 16 張）、guaiacol 頁含 guaifenesin（GLYCERYL ETHER／GLYCOLATE EQ TO GUAIFENESIN 1,088 張）與 potassium guaiacolsulfonate 16 張、thiamine 頁含 bisbentiamine、fursultiamine、sulbutiamine、cocarboxylase、dibenzoylthiamine（約 160 張）、inositol 頁含 inositol nicotinate 38 張、lactic_acid 頁含 zinc lactate 4 張、urea（noindex）含 urea peroxide 8 張。這些頁的原適應症、品名與張數說法是依這些許可證寫的（scopolamine 頁 2026-10-03 已加註、原文保留），換表會連帶改動正文，沒有套用，待用戶決定（做法：config/tfda_synonyms.json 的 exclude 加這些字樣後跑 regenerate_tfda_tables.py）。

## 程式許可證表排除名字相近的別的藥（2026-11-25 第六輪）

用戶 2026-11-25 決定（第六輪第 2 條）：第五輪量到的「比對到的成分名多出本藥以外字樣」的程式表，照 config/tfda_synonyms.json 的 exclude 排除，跟新表矛盾的正文照查核機制寫紀錄更正。
- `config/tfda_synonyms.json` exclude（每筆附 note 依據）：guaiacol（GLYCERYL／GLYCERIN／GLYCOLATE＝guaifenesin、SULPHONATE＝potassium guaiacolsulfonate、CARBONATE＝guaiacol carbonate）、thiamine（DISULFIDE＝thiamine disulfide、fursultiamine、sulbutiamine、bisbentiamine、bisbutiamine；DIBENZOYL、COCARBOXYLASE／PYROPHOSPHATE、PHOSPHORIC＝磷酸酯；HCL、MONONITRATE、DICETYLSULFATE、THIOCYANATE 等鹽照收）、scopolamine（BUTYL、METHYL、METHOBROMIDE、METHONITRATE＝butylscopolamine、methscopolamine）、inositol（NIACINATE／NICOTINATE）、lactic acid（ZINC＝zinc lactate）、urea（PEROXID＝urea peroxide，含試劑盒誤植的 UREA PEROXIDASE；UREA C-13 照收）；
  另寫的全量偵測（每頁程式表比對到的成分名扣掉藥名、鹽類、水合物、劑型字樣後剩下的字，171 組逐組看）找到同類 7 條一併加：vitamin E（NICOTINATE）、salicylic acid（ESTER＝glycol salicylate 等）、theophylline（OXYPROPYL＝proxyphylline）、mannitol（ISND＝以甘露醇稀釋的 isosorbide dinitrate）、glycerin（FATTY ACID ESTER）、polyethylene glycol（STEARATE）、methionine（SULFOX）。其餘是同一分子的鹽、酯、水合物或劑型寫法（steroid 各酯、aluminum hydroxide gel、penicillin G 各鹽等），照收。
- `src/twtxgnn/regulatory/tfda_licenses.py`：exclude 改成「比對到的成分全部是別的藥才排除」（之前只要有一個比對到的成分含 exclude 字樣就整張排除；複方同時含 thiamine 與 thiamine disulfide 會被漏掉），單方判定也只算本藥成分；對既有 7 條 exclude 的結果不變（全站比對 0 頁不同）。
- 快速總覽「台灣上市」列改由程式維護（`page_postprocess._count_row`，同「許可證數」列）：2026-10-20 母目錄統一成「上市中（有效許可證 V 張／共 N 張）」「未上市（已註銷許可證 N 張／共 N 張）」之後沒有程式跟著快照更新（母目錄 sync_market_rows 跳過 Tw），量到 37 頁跟快照差 1～3 張、checker M1 37 項；只改已是這兩種寫法的列。每週 tfda_regen_weekly.sh 重產時一併更新。
- `scripts/apply_drug_reviews.py` 加 correct＋`field: "description"`（只改 front matter description 那一行、不插框、只列在查核紀錄表、可重複執行）。
- 2026-11-25 套用（資料集 36，檔案日期 2026-11-24）：程式表 13 頁改變（guaiacol 1080→11 張、全部已註銷；thiamine 2707→2282；scopolamine 179→82，有效單方只剩衛署藥製字第007944號；inositol 400→362；urea 80→72（noindex）；lactic acid、vitamin E、salicylic acid、theophylline、mannitol、glycerin、PEG、methionine 各少 1～5 張）；「台灣上市」列 48 頁由程式同步。
  查核紀錄 10 筆：guaiacol 一句話總結（清痰片與感冒咳嗽複方是 guaifenesin）、原適應症列、description（括號內適應症取自 guaifenesin 許可證）更正，「為什麼合理」與決策理由所引的鼻部症狀複方加註（決策未改）；scopolamine 原適應症列由 10-03 的加註同 id 重發成更正（改為 scopolamine 本身有效單方許可證的適應症，前版存 history）、description 更正；inositol 原適應症列加註（「末梢血管循環障礙」多見於 inositol nicotinate 許可證，肌醇本身登載的有效單方有血順錠、築野肌醇）；camphor、tyrosine 依舊資料集寫死的有效張數 2 句更正（不寫張數）。
  證據包：`scripts/exclude_mismatched_records.py` 依新快照從 13 個證據包移出 1,616 筆（guaifenesin、thiamine 衍生物等），第二次跑 0 筆；證據包 local_regulatory 重算 12 個（refresh_pack_regulatory），經 data-overlay 推進 Release。
- 驗證：regenerate_tfda_tables.py 再跑 0 頁；apply --check 0；gate exit 0；checker（還原 bundles 後）M1 37→0，P 類前後相同（P1 63、P2 10、P3 18、P6 10、P7 60，跟許可證無關）。
- 沒處理（回報待決定）：calcium lactate（70 張）、sodium lactate 照原規則仍算 lactic acid；inositol 有 2 張已註銷許可證品名「六菸/肌醇」「六菸　肌醇」（inositol hexanicotinate）主成分欄卻登載 INOSITOL，依主成分照收；search-index.json 的 original 取自證據包 drug.original_indications（guaiacol、scopolamine、inositol、PEG 等仍是別的藥的適應症），沒有跟頁面更正，要整份重產或另訂規則。

## 第七輪：乳酸鈉／乳酸鈣排除、search-index 原適應症讀頁面、交叉驗證不覆蓋已查項目（2026-11-25）

用戶 2026-11-25 決定（第七輪第 3 條）：
- (a) `config/tfda_synonyms.json` 的 LACTIC ACID exclude 照排除 zinc lactate 的同一理由加 CALCIUM、SODIUM（乳酸鈣是補鈣劑、乳酸鈉是輸液與透析液的鹼化劑與電解質，作用不是來自乳酸；SOLUTION／ANHYDROUS／L-、S- 寫法一併排除；同一張證另有 LACTIC ACID 成分的照收）。`regenerate_tfda_tables.py --data-date 2026-11-24`：lactic_acid 程式表 264→31 張（有效單方 9 張全為外用洗潔液、有效複方 7 張、已過期 1、已註銷 14），其他頁不變。
  查核紀錄說明寫「有效單方除 1 張乳酸鈉原料藥溶液（衛部藥輸字第027230號）外都是外用液劑」「含乳酸鹽的口服錠只有鈣補充劑（006734、007474）」的 2 筆（`lactic-acid-summary-oral-uses-2026-10-03`、`lactic-acid-why-oral-premise-2026-10-03`）同 id 重發（前版存 history），不再點名已不屬本藥的字號；正文其他句子跟新表一致。證據包 tfda 區塊由每週排程的 exclude_mismatched_records.py 依新快照移出（這次沒還原 bundles）。
- 順帶修 `scripts/regenerate_tfda_tables.py`：重產前「已套用的更正先還原成原句」也還原了 resolved_by_program 的更正（這種更正已寫進本文、apply 不重套），11-23 重產時 sodium_carbonate 的原適應症列與一句話總結被改回 10-28 前的錯句（「取自單方且仍有效的許可證，其適應症為抗生素」）；改成跳過 resolved_by_program，頁面兩句照紀錄還原，再跑重產 0 頁。全站 resolved_by_program 更正只有這 2 句被改回。
- (b) `scripts/generate_search_index.py` 加 `_sync_originals_from_pages()`（`--levels-from-pages` 與完整重產都跑）：drugs[].original 與 indications[].drugs[].original 改成藥物頁上的原適應症（快速總覽「原適應症」格；沒有就 description 的「原適應症：…」；都沒有＝空字串，SMART 顯示「—」），照舊截 50 字。以前取自證據包 drug.original_indications（10-03 前舊收錄，常是別的藥，例 axitinib 寫成 avelumab 的默克細胞癌、guaiacol 寫成 guaifenesin 的鎮咳袪痰、scopolamine 寫成 butylscopolamine 的胃腸痙攣、PEG 寫成 Mircera 的腎性貧血）。292 個藥 270 個改變；已知用途頁沒有原適應症格的 5 頁（aluminum_hydroxide、dl-alpha-tocopherol、emedastine、norethindrone_enanthate、silicon_dioxide）改成空字串。inositol 照頁面是「末梢血管循環障礙」（第六輪已加註，原文保留）。
- (c) `scripts/generate_data_exports.py` 重跑：drugs.json／drugs.csv 原本空白的 5 筆（etanercept、lorcaserin、niraparib、sorafenib、vonoprazan）補上頁面原適應症；第 6 筆 sodium_carbonate 是頁面被 11-23 重產改錯，頁面還原後跟匯出一致。另寫一支比對（search-index original 對 drugs.json 全格）0 筆不符。
- (d) `scripts/check_original_indications.py` 不再整批替換：resolved／unresolvable 原樣保留、同頁同句已查過的不重列、同頁已有 open 就更新、其餘新增（found＝執行日），不刪項目。這次跑出 7 頁：inositol、salicylic_acid 已有加註紀錄，標 resolved 附 record_ids；enfortumab_vedotin、erdafitinib、polyethylene_glycol_400、potassium_iodide、vitamin_e 5 項 open 待人工判讀；第二次跑新增 0。舊版會把既有 15 筆 resolved 換掉。
- 驗證：regenerate 再跑 0 頁、問題 0；apply --check 0；gate exit 0；母目錄 checker M 類 0（本機沒還原 bundles，P1 292 跟許可證無關）。
