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

## 完成狀態

### ✅ 核心功能
| 項目 | 狀態 | 說明 |
|------|------|------|
| DrugBundle 收集器 | ✅ | 整合 TFDA、DDI、臨床試驗、PubMed |
| DrugEvidencePack 產生器 | ✅ | LLM 分析藥物所有預測適應症 |
| DrugPharmacistNotesWriter | ✅ | 產生藥師決策筆記 |
| DrugSponsorNotesWriter | ✅ | 產生申辦者決策筆記 |
| 公開 DDI 資料來源 | ✅ | DDInter (222,391 筆) + PHARMACOLOGY (4,636 筆) |

### ✅ 測試
- **341 項測試全部通過**
- 涵蓋：Collectors、Reviewer、Writer、Paths 等所有模組

### ✅ 驗證範例
已成功產生 20 個藥物的完整報告：
- aspirin, clopidogrel, dexamethasone, fluorouracil, gemcitabine
- ibuprofen, levamisole, lidocaine, metformin, methotrexate
- minoxidil, nystatin, paclitaxel, prednisolone, propranolol
- tamoxifen, travoprost, tretinoin, vincristine, warfarin

---

## 使用方式

### 1. 環境設定
```bash
# 安裝依賴
uv sync

# 設定 OpenAI API Key (用於 LLM 分析)
export OPENAI_API_KEY="your-api-key"
```

### 2. 單一藥物處理
```python
from src.twtxgnn.collectors import DrugBundleAggregator
from src.twtxgnn.reviewer import DrugEvidencePack
from src.twtxgnn.writer import DrugPharmacistNotesWriter, DrugSponsorNotesWriter

# 收集資料
aggregator = DrugBundleAggregator(save_collected=True)
bundle = aggregator.collect(drug_name="aspirin", top_n=10, min_score=0.99)

# 產生 Evidence Pack
ep = DrugEvidencePack()
ep.generate(bundle)
ep.save()

# 產生筆記
pharmacist_writer = DrugPharmacistNotesWriter()
sponsor_writer = DrugSponsorNotesWriter()

pharmacist_writer.generate_and_save(ep.to_dict(), "data/notes/aspirin/drug_pharmacist_notes.md")
sponsor_writer.generate_and_save(ep.to_dict(), "data/notes/aspirin/drug_sponsor_notes.md")
```

### 3. 批次處理
```bash
# 使用批次腳本
uv run python scripts/batch_collect_bundles.py
```

### 4. 驗證一致性
```bash
# 驗證 Pharmacist/Sponsor Notes 一致性
uv run python scripts/validate_notes_consistency.py \
    data/notes/aspirin/drug_pharmacist_notes.md \
    data/notes/aspirin/drug_sponsor_notes.md
```

---

## 架構概覽

### Collectors 模組
```
src/twtxgnn/collectors/
├── base.py                 # BaseCollector 抽象基底
├── bundle.py               # BundleAggregator (drug-disease pair)
├── drug_bundle.py          # DrugBundleAggregator (drug-centric)
├── tfda.py                 # 台灣 FDA 資料收集器
├── ddinter.py              # DDInter 藥物交互作用收集器
├── pharmacology.py         # Guide to PHARMACOLOGY 收集器
└── unified_ddi.py          # 整合 DDI 收集器
```

### Reviewer 模組
```
src/twtxgnn/reviewer/
├── drug_evidence_pack.py   # DrugEvidencePack 產生器
├── evidence_pack.py        # EvidencePack (drug-disease pair)
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

---

## 產出檔案結構

```
data/
├── bundles/                    # 收集的原始資料
│   └── {drug_name}/
│       └── drug_bundle.json
├── evidence_packs/             # LLM 分析結果
│   └── {drug_name}/
│       ├── {drug}_drug_evidence_pack.json
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

## Git 提交記錄

```
32c6583 Add batch bundle collection script for parallel drug processing
5ee3c76 Fix PharmacologyCollector CSV parsing for quoted comment lines
bf75ed9 Add validation tools and replace Lexicomp with public DDI sources
02b7af3 Update README with download links and deep learning statistics
1641413 Add TxGNN Taiwan drug repurposing prediction implementation
```

---

## 快速指令

```bash
# 執行所有測試
uv run pytest tests/ -v

# 執行特定模組測試
uv run pytest tests/test_collectors_*.py -v
uv run pytest tests/test_writer.py -v
uv run pytest tests/test_reviewer.py -v

# 驗證筆記一致性
uv run python scripts/validate_notes_consistency.py <pharmacist.md> <sponsor.md>
```
