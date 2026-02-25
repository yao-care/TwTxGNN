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
ls data/processed/repurposing_candidates.csv
```

**結果檔案**：`data/processed/repurposing_candidates.csv`

預期輸出：
- 老藥新用候選數：142,328
- 涉及藥物數：677
- 潛在新適應症數：1,035

---

### 步驟 6（選用）：深度學習方法

深度學習方法需要額外環境設定，請告知使用者：

1. 需要手動下載模型檔案：[Google Drive](https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj)
2. 需要設定 Conda 環境（Python 3.11 + PyTorch + DGL）
3. 執行時間較長（數小時）且需要 16GB+ RAM

詳細步驟請參考 README.md「步驟 6、7」。

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
           repurposing_candidates.csv (142,328 筆)
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

## 藥物交互作用 (DDI) 資料維護

專案使用兩個公開 DDI 資料來源，**建議每季更新一次**：

### 資料來源

| 來源 | 網址 | 涵蓋範圍 |
|------|------|----------|
| DDInter 2.0 | https://ddinter2.scbdd.com | 302,516 DDI、2,310 藥物 |
| Guide to PHARMACOLOGY | https://www.guidetopharmacology.org/download.jsp | 核准藥物交互作用 |

### 更新 DDI 資料

```bash
# 建立目錄
mkdir -p data/external/ddi/ddinter
mkdir -p data/external/ddi/pharmacology

# 下載 Guide to PHARMACOLOGY（直接下載）
curl -L -o data/external/ddi/pharmacology/interactions.csv \
  "https://www.guidetopharmacology.org/DATA/approved_drug_detailed_interactions.csv"

# DDInter 2.0 需從網站手動下載：
# 1. 訪問 https://ddinter2.scbdd.com/download/
# 2. 下載 DDI 資料集（CSV 或 JSON 格式）
# 3. 放置到 data/external/ddi/ddinter/
```

### 資料檔案結構

```
data/external/ddi/
├── ddinter/                    # DDInter 2.0 資料
│   └── ddinter_downloads.csv   # DDI 資料集
└── pharmacology/               # Guide to PHARMACOLOGY 資料
    └── interactions.csv        # 核准藥物交互作用
```

### 上次更新時間

- DDInter 1.0: 2026-02-08 (222,391 筆 DDI)
- Guide to PHARMACOLOGY: 2026-02-08 (v2025.4, 4,636 筆)

> **提醒**：DDI 資料會定期更新，建議每季檢查是否有新版本。

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
