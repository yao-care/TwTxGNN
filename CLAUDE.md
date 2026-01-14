# TwTxGNN - Claude CLI 使用指引

本文件用於引導 Claude CLI 自動化執行台灣健保藥品老藥新用預測實驗。

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

## 注意事項

- 本專案結果僅供研究參考，不構成醫療建議
- 老藥新用候選需經過臨床驗證才能應用
