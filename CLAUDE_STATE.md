# Claude 工作狀態記錄

**記錄時間**: 2026-02-08
**分支**: `feature/validation-tools`

---

## 分支目標

建立「驗證 TwTxGNN 老藥新用推薦藥品」的完整工具流程：

```
TxGNN 預測結果
    ↓
[validation-tools 流程]
    ↓
├── drug_pharmacist_notes (藥師決策參考)
└── drug_sponsor_notes (申辦者決策參考)
```

---

## v4 架構升級（已完成）

### 已解決的問題
| 問題 | 根因 | 解決方案 |
|-----|------|---------|
| 資料截斷 | LLM 選擇性簡化 | v4: 程式化資料傳輸 + LLM 只分析 |
| 狀態標記錯誤 | 無顯式查詢追蹤 | CollectionStatus 追蹤每次查詢 |
| 空 Notes 資料夾 | 缺乏錯誤處理 | 重試機制 + 輸出驗證 |

### v4 核心變更
1. **CollectionStatus** - 追蹤每個資料來源的查詢狀態
2. **Evidence Pack v4** - 程式化資料傳輸，100% 保真
3. **Notes 狀態判讀** - 根據 query_log 正確顯示狀態
4. **驗證管線** - 自動驗證資料完整性

---

## 完成狀態

### ✅ 核心功能
| 項目 | 狀態 | 說明 |
|------|------|------|
| DrugBundle 收集器 | ✅ | 整合 TFDA、DDI、臨床試驗、PubMed + CollectionStatus 追蹤 |
| DrugEvidencePackGenerator | ✅ | v4 架構：程式化資料傳輸 + LLM 分析 |
| DrugPharmacistNotesWriter | ✅ | v4 prompt：正確解讀 query_log 狀態 |
| DrugSponsorNotesWriter | ✅ | v4 prompt：正確解讀 query_log 狀態 |
| 公開 DDI 資料來源 | ✅ | DDInter (222,391 筆) + PHARMACOLOGY (4,636 筆) |
| 驗證管線 | ✅ | validate_data_pipeline.py |

### ✅ 測試
- **341 項測試全部通過**
- 涵蓋：Collectors、Reviewer、Writer、Paths 等所有模組

---

## 使用方式

### 1. 環境設定
```bash
# 安裝依賴
uv sync

# 設定 OpenAI API Key (用於 LLM 分析)
export OPENAI_API_KEY="your-api-key"
```

### 2. 單一藥物完整處理（推薦）
```bash
# 使用 regenerate_drug.py 執行完整流程
uv run python scripts/regenerate_drug.py minoxidil --top-n 5

# 可選參數
#   --skip-bundle   跳過 Bundle 收集（使用現有）
#   --skip-ep       跳過 Evidence Pack 產生
#   --skip-notes    跳過 Notes 產生
```

### 3. 驗證資料管線
```bash
# 驗證單一藥物
uv run python scripts/validate_data_pipeline.py --drug minoxidil -v

# 驗證所有藥物
uv run python scripts/validate_data_pipeline.py --all --summary
```

### 4. Python API 使用
```python
from src.twtxgnn.collectors import DrugBundleAggregator
from src.twtxgnn.reviewer import DrugEvidencePackGenerator
from src.twtxgnn.writer import DrugPharmacistNotesWriter, DrugSponsorNotesWriter

# 收集資料（含 CollectionStatus 追蹤）
aggregator = DrugBundleAggregator(save_collected=True)
bundle = aggregator.collect(drug_name="minoxidil", top_n=5, min_score=0.99)
bundle.save()  # 儲存 bundle

# 產生 Evidence Pack（v4：資料 100% 保真）
ep_generator = DrugEvidencePackGenerator()
json_path, md_path = ep_generator.generate_and_save(
    bundle=bundle,
    output_dir="data/evidence_packs/minoxidil",
    validate=True,  # 啟用輸出驗證
)

# 產生筆記
pharmacist_writer = DrugPharmacistNotesWriter()
sponsor_writer = DrugSponsorNotesWriter()

# 載入 Evidence Pack
import json
with open(json_path) as f:
    ep_data = json.load(f)

pharmacist_writer.generate_and_save(ep_data, "data/notes/minoxidil/drug_pharmacist_notes.md")
sponsor_writer.generate_and_save(ep_data, "data/notes/minoxidil/drug_sponsor_notes.md")
```

---

## 架構概覽

### Collectors 模組
```
src/twtxgnn/collectors/
├── base.py                 # BaseCollector 抽象基底
├── bundle.py               # BundleAggregator (drug-disease pair)
├── drug_bundle.py          # DrugBundleAggregator (drug-centric) + CollectionStatus
├── tfda.py                 # 台灣 FDA 資料收集器
├── ddinter.py              # DDInter 藥物交互作用收集器
├── pharmacology.py         # Guide to PHARMACOLOGY 收集器
└── unified_ddi.py          # 整合 DDI 收集器
```

### Reviewer 模組
```
src/twtxgnn/reviewer/
├── drug_evidence_pack.py   # DrugEvidencePackGenerator (v4 架構)
├── evidence_pack.py        # EvidencePackGenerator (舊版)
└── llm_client.py           # LLM 客戶端
```

### Writer 模組
```
src/twtxgnn/writer/
├── base.py                 # BaseNotesWriter 抽象基底
├── drug_pharmacist.py      # DrugPharmacistNotesWriter
├── drug_sponsor.py         # DrugSponsorNotesWriter
├── pharmacist.py           # PharmacistNotesWriter (舊版)
└── sponsor.py              # SponsorNotesWriter (舊版)
```

### 驗證腳本
```
scripts/
├── regenerate_drug.py           # 單一藥物完整流程
├── validate_data_pipeline.py    # 資料管線驗證
├── validate_notes_consistency.py # Notes 一致性驗證
└── batch_collect_bundles.py     # 批次收集 Bundle
```

---

## 產出檔案結構

```
data/
├── bundles/                    # 收集的原始資料
│   └── {drug_name}/
│       └── drug_bundle.json    # 含 collection_log
├── evidence_packs/             # LLM 分析結果
│   └── {drug_name}/
│       ├── {drug}_drug_evidence_pack.json  # 含 query_log
│       ├── {drug}_drug_evidence_pack.md
│       └── raw_llm_response.txt
└── notes/                      # 決策筆記
    └── {drug_name}/
        ├── drug_pharmacist_notes.md
        └── drug_sponsor_notes.md
```

---

## DDI 資料維護

DDI 資料來自公開資料庫，建議每季更新：

### DDInter 2.0
- **來源**: https://ddinter2.scbdd.com
- **下載**: Download → Bulk Download → All DDIs
- **格式**: ZIP 檔案，解壓縮後放入 `data/external/ddi/ddinter/`

### Guide to PHARMACOLOGY
- **來源**: https://www.guidetopharmacology.org/download.jsp
- **下載**: Interactions data (CSV)
- **格式**: CSV 檔案，放入 `data/external/ddi/pharmacology/interactions.csv`

---

## v4 query_log 狀態對應

Notes 中的「資料來源稽核框」根據 Evidence Pack 的 `query_log` 判讀：

| query_log.result_status | result_count | 顯示 |
|------------------------|--------------|------|
| `success` | > 0 | ✅ |
| `success` | = 0 | ✅ (無結果) |
| `error` | - | ❌ |
| `not_found` | - | ⚠️ [未找到] |
| 未出現在 query_log | - | ⏸️ [未檢索] |

---

## 快速指令

```bash
# 執行所有測試
uv run pytest tests/ -v

# 執行特定模組測試
uv run pytest tests/test_collectors_*.py -v
uv run pytest tests/test_writer.py -v
uv run pytest tests/test_reviewer.py -v

# 單一藥物完整處理
uv run python scripts/regenerate_drug.py minoxidil --top-n 5

# 驗證資料管線
uv run python scripts/validate_data_pipeline.py --drug minoxidil -v
uv run python scripts/validate_data_pipeline.py --all --summary
```

---

## 待完成

需要重新產生所有藥物的 Bundle、Evidence Pack 和 Notes：

```bash
# 使用新的 v4 流程重新產生
export OPENAI_API_KEY="your-api-key"

# 逐一處理藥物
for drug in minoxidil warfarin aspirin gemcitabine; do
    uv run python scripts/regenerate_drug.py $drug --top-n 5
done
```
