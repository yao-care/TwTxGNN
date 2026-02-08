# TwTxGNN - 台灣健保藥品老藥新用預測

使用 TxGNN 知識圖譜對台灣健保藥品進行老藥新用（drug repurposing）預測。

## 注意事項

- 本專案結果僅供研究參考，不構成醫療建議
- 老藥新用候選需經過臨床驗證才能應用

## 專案成果

依照 TxGNN 規劃，有兩種方法可以進行預測：

| 方法 | 速度 | 精準度 | 環境需求 | 下載結果 |
|------|------|--------|----------|---|
| 知識圖譜方法 | 快（幾秒） | 較低 | 無特殊需求 | [GitHub Release](https://github.com/yao-care/TwTxGNN/releases/tag/v1.0.0) |
| 深度學習方法 | 慢（數小時） | 較高 | Conda + PyTorch + DGL | [Google Drive](https://drive.google.com/file/d/1aNQHgq2Jae99p1CtItwHz8_zj0cn1bfq/view?usp=sharing) (683MB) |

**差異說明**：知識圖譜方法直接查詢已知的藥物-疾病關係；深度學習方法使用神經網路模型推論潛在關係，並計算信心分數。

### 知識圖譜方法

```bash
uv run python scripts/run_kg_prediction.py
```

直接查詢 TxGNN 知識圖譜中的藥物-疾病關係。

**結果檔案**：`data/processed/repurposing_candidates.csv`

| 指標 | 數值 |
|------|------|
| 台灣 FDA 總藥品數 | 71,552 |
| 有效藥品數 | 23,612 (33%) |
| 對應 DrugBank 藥品數 | 1,404 (<6%) |
| DrugBank 成分映射率 | 73.87% |
| 對應到疾病數 | 166 (<12%) |
| 適應症映射率 | 44.85% |
| 老藥新用候選數 | 142,328 |
| 涉及藥物數 | 677 |
| 潛在新適應症數 | 1,035 |

### 深度學習方法

```bash
# 使用 conda 環境執行（需先安裝 PyTorch + DGL）
conda activate txgnn
python scripts/run_txgnn_prediction.py
```

使用 TxGNN 預訓練神經網路模型計算預測分數。

**結果檔案**：`data/processed/txgnn_dl_predictions.csv`

| 指標 | 數值 |
|------|------|
| 總預測數 | 23,925,564 |
| 涉及藥物數 | 1,404 |
| 涉及適應症數 | 17,041 |
| 平均信心分數 | 0.1932 |
| 最高信心分數 | 1.0 |
| 高信心預測 (>0.9) | 133,499 |
| 中高信心預測 (>0.7) | 433,136 |
| 中等信心預測 (>0.5) | 1,995,813 |

### 驗證流程

```bash
uv run python scripts/run_validation_pipeline.py --drug warfarin --disease "atrial fibrillation"
```

針對 TxGNN 預測結果進行多來源資料驗證，產生專業報告。

**流程架構**：
```
TxGNN 預測結果
      ↓
┌─────────────────────────────────────┐
│ Step 1: Data Collectors             │
│   TFDA、ClinicalTrials、PubMed、    │
│   Unified DDI、WHO ICTRP            │
│   → bundle.json                     │
├─────────────────────────────────────┤
│ Step 2: Evidence Pack Reviewer      │
│   LLM 審閱、證據分級 (L1-L5)         │
│   → evidence_pack.json/md           │
├─────────────────────────────────────┤
│ Step 3: Notes Writer                │
│   → pharmacist_notes.md (藥師要點)   │
│   → sponsor_notes.md (藥廠要點)      │
└─────────────────────────────────────┘
```

---

## 快速開始

### 步驟 1：下載資料

| 檔案 | 下載連結 | 放置位置 | 用途 |
|------|----------|----------|------|
| FDA 藥品資料 | [食藥署開放資料](https://data.fda.gov.tw/data/opendata/export/36/json) | `data/raw/` (ZIP 檔案) | 台灣藥品資料 |
| node.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144482) | `data/node.csv` | 節點資料 |
| kg.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144484) | `data/kg.csv` | 知識圖譜 |
| edges.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144483) | `data/edges.csv` | 邊資料（深度學習用） |
| model_ckpt.zip | [Google Drive](https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj) | 解壓縮到 `model_ckpt/` | 預訓練模型（深度學習用） |

### 步驟 2：安裝環境

```bash
# 安裝基本依賴
uv sync

# 程式測試
uv run pytest tests/
```

### 步驟 3：處理 FDA 資料

將下載的 FDA ZIP 檔案解壓縮並轉換為 JSON：

```bash
uv run python scripts/process_fda_data.py
```

這會產生 `data/raw/tw_fda_drugs.json`。

### 步驟 4：準備詞彙表資料

從下載的 TxGNN 資料提取詞彙表：

```bash
uv run python scripts/prepare_external_data.py
```

這會產生 `data/external/` 目錄下的三個檔案：
- `drugbank_vocab.csv` - DrugBank 藥品詞彙表
- `disease_vocab.csv` - 疾病詞彙表
- `drug_disease_relations.csv` - 藥物-疾病關係

### 步驟 5：執行知識圖譜方法

```bash
uv run python scripts/run_kg_prediction.py
```

### 步驟 6：搭建深度學習環境

深度學習方法需要 PyTorch + DGL，建議使用 Conda 環境：

```bash
# 1. 建立 conda 環境（Python 3.11，DGL 相容性較好）
conda create -n txgnn python=3.11 -y
conda activate txgnn

# 2. 安裝 PyTorch（Intel Mac 使用 2.2.2，CUDA 用戶可用更新版本）
# Intel Mac / CPU:
pip install torch==2.2.2 torchvision==0.17.2

# CUDA 用戶（Linux/Windows with NVIDIA GPU）:
# pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# 3. 安裝 DGL（圖神經網路套件）
# Intel Mac / CPU:
pip install dgl==1.1.3

# CUDA 用戶:
# pip install dgl -f https://data.dgl.ai/wheels/cu118/repo.html

# 4. 安裝 TxGNN（從 GitHub，PyPI 版本有 bug）
pip install git+https://github.com/mims-harvard/TxGNN.git

# 5. 安裝其他依賴
pip install pandas tqdm pyyaml pydantic ogb

# 6. 驗證安裝
python -c "import torch; import dgl; import txgnn; print('安裝成功！')"
```

**注意事項**：
- Apple Silicon (M1/M2/M3) 目前 DGL 不支援 MPS，會自動使用 CPU
- Intel Mac 需使用 PyTorch 2.2.2（2.3+ 不支援）
- 預測過程記憶體需求較高，建議至少 16GB RAM

### 步驟 7：執行深度學習方法

```bash
# 解壓縮模型檔案
unzip -n model_ckpt.zip

# 啟動 conda 環境並執行預測
conda activate txgnn
python scripts/run_txgnn_prediction.py
```

執行過程支援斷點續傳，中途中斷可重新執行繼續。

---

## 相關資源

- [TxGNN 論文](https://www.nature.com/articles/s41591-024-03233-x)
- [TxGNN GitHub](https://github.com/mims-harvard/TxGNN)
- [TxGNN Explorer](http://txgnn.org) - 互動式預測查詢

| 資料 | 來源 | 說明 |
|------|------|------|
| 台灣 FDA 藥品 | [食藥署開放資料](https://data.fda.gov.tw/data/opendata/export/36/json) | 71,545 筆藥品許可證 |
| TxGNN 知識圖譜 | [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM) | 17,080 種疾病、7,957 個藥品 |

## 專案介紹

### 目錄結構

```
TwTxGNN/
├── README.md                    # 專案文件
├── CLAUDE.md                    # AI 助手指引
├── pyproject.toml               # Python 套件設定
│
├── data/                        # 資料目錄
│   ├── kg.csv                   # 🟡 TxGNN 知識圖譜
│   ├── node.csv                 # 🟡 TxGNN 節點資料
│   ├── edges.csv                # 🟡 TxGNN 邊資料
│   ├── kg_directed.csv          # 🔵 TxGNN 處理後生成
│   ├── complex_disease_42/      # 🔵 TxGNN 訓練/驗證/測試分割
│   │   ├── train.csv
│   │   ├── valid.csv
│   │   └── test.csv
│   ├── raw/
│   │   └── tw_fda_drugs.json           # 🟢 台灣 FDA 藥品資料
│   ├── external/                       # 🔵 由 prepare_external_data.py 產生
│   │   ├── drugbank_vocab.csv          # DrugBank 詞彙表
│   │   ├── disease_vocab.csv           # 疾病詞彙表
│   │   └── drug_disease_relations.csv  # 藥物-疾病關係
│   ├── processed/
│   │   ├── drug_mapping.csv            # 🔵 台灣藥品→DrugBank 映射
│   │   ├── indication_mapping.csv      # 🔵 適應症→疾病映射
│   │   ├── repurposing_candidates.csv  # 🔵 知識圖譜方法結果
│   │   └── txgnn_dl_predictions.csv    # 🔵 深度學習方法結果
│   ├── collected/                      # 🟠 驗證流程 - 原始收集資料
│   │   ├── clinicaltrials/             # ClinicalTrials.gov 資料
│   │   ├── pubmed/                     # PubMed 文獻
│   │   ├── tfda/                       # TFDA 藥品資料
│   │   ├── unified_ddi/                # DDI 資料 (DDInter + PHARMACOLOGY)
│   │   └── ictrp/                      # WHO ICTRP 資料
│   ├── bundles/                        # 🟠 驗證流程 - 整合資料包
│   │   └── {drug}_{disease}/
│   │       └── bundle.json
│   ├── evidence_packs/                 # 🟠 驗證流程 - 證據包
│   │   └── {drug}_{disease}/
│   │       ├── evidence_pack.json
│   │       └── evidence_pack.md
│   └── notes/                          # 🟠 驗證流程 - 最終報告
│       └── {drug}_{disease}/
│           ├── pharmacist_notes.md
│           └── sponsor_notes.md
│
├── prompts/                            # 🟠 LLM System Prompts
│   ├── Evidence Pack Reviewer/
│   │   └── v1.md
│   └── Notes Writer/
│       ├── pharmacist_v1.md
│       └── sponsor_v1.md
│
├── model_ckpt/                  # 🟡 TxGNN 預訓練模型
│   ├── model.pt                 # 模型權重
│   ├── config.pkl               # 模型設定
│   ├── node_emb.pkl             # 節點嵌入向量
│   └── ...
│
├── src/twtxgnn/                        # 🔵 核心程式碼
│   ├── data/
│   │   └── loader.py                   # FDA 藥品資料載入
│   ├── mapping/
│   │   ├── normalizer.py               # 藥品成分標準化
│   │   ├── drugbank_mapper.py          # DrugBank ID 映射
│   │   └── disease_mapper.py           # 適應症→疾病映射
│   ├── predict/
│   │   ├── repurposing.py              # 知識圖譜方法預測
│   │   ├── txgnn_model.py              # 深度學習方法預測
│   │   ├── prepare_for_txgnn.py        # TxGNN 資料準備工具
│   │   └── process_txgnn_results.py    # 預測結果處理工具
│   ├── collectors/                     # 🟠 驗證流程 - 資料收集
│   │   ├── base.py                     # BaseCollector 介面
│   │   ├── bundle.py                   # EvidenceBundle 整合
│   │   ├── tfda.py                     # TFDA 藥品資料
│   │   ├── clinicaltrials.py           # ClinicalTrials.gov
│   │   ├── pubmed.py                   # PubMed 文獻
│   │   ├── unified_ddi.py              # Unified DDI (DDInter + PHARMACOLOGY)
│   │   └── ictrp.py                    # WHO ICTRP
│   ├── reviewer/                       # 🟠 驗證流程 - LLM 審閱
│   │   ├── llm_client.py               # OpenAI API 封裝
│   │   └── evidence_pack.py            # Evidence Pack 產生
│   ├── writer/                         # 🟠 驗證流程 - 報告產生
│   │   ├── base.py                     # BaseNotesWriter 介面
│   │   ├── pharmacist.py               # 藥師要點
│   │   └── sponsor.py                  # 藥廠要點
│   └── paths.py                        # 路徑管理
│
├── scripts/                            # 🔵 執行腳本
│   ├── process_fda_data.py             # 處理 FDA 資料
│   ├── prepare_external_data.py        # 準備詞彙表資料
│   ├── run_kg_prediction.py            # 執行知識圖譜方法
│   ├── run_txgnn_prediction.py         # 執行深度學習方法
│   └── run_validation_pipeline.py      # 執行驗證流程
│
└── tests/                       # 🔵 測試程式
    ├── test_loader.py
    ├── test_normalizer.py
    ├── test_drugbank_mapper.py
    ├── test_disease_mapper.py
    ├── test_repurposing.py
    └── test_txgnn_integration.py
```

**圖例**：🔵 專案開發 | 🟢 台灣資料 | 🟡 TxGNN 資料 | 🟠 驗證流程

### 資料流程

```
FDA ZIP 檔案 (手動下載)         TxGNN 資料 (node.csv, kg.csv)
        ↓                               ↓
   process_fda_data.py           prepare_external_data.py
        ↓                               ↓
   tw_fda_drugs.json             data/external/ (詞彙表)
        ↓                               ↓
        └───────────────────────────────┘
                        ↓
           標準化成分名稱 (normalizer.py)
                        ↓
           映射到 DrugBank ID (data/processed/drug_mapping.csv)
                        ↓
           映射適應症到疾病 (data/processed/indication_mapping.csv)
                        ↓
   ┌─────────────────────────────────────────────┐
   │                                             │
   ▼                                             ▼
知識圖譜方法                               深度學習方法
(repurposing.py)                         (txgnn_model.py)
   │                                             │
   ▼                                             ▼
repurposing_candidates.csv              txgnn_dl_predictions.csv
```
