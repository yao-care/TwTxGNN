# Claude 工作狀態記錄

**記錄時間**: 2026-02-08
**分支**: `feature/validation-tools`

---

## 今天完成的工作 (2026-02-08)

### 1. 修復 Evidence Pack JSON 序列化問題
- **檔案**: `src/twtxgnn/reviewer/drug_evidence_pack.py`
- **修改**: 改進 `_parse_response` 方法的 JSON 解析邏輯
- **解決**: Evidence Pack JSON 檔案現在可以正確儲存完整內容（之前僅有 `{}`）

### 2. 驗證 Writer 流程
- **測試結果**: 301 項測試全部通過
- **確認**: Writer 模組正常運作，可正確讀取 Evidence Pack JSON

### 3. DDI 資料來源更換
- **移除**: Lexicomp（私有資料，無法公開使用）
- **新增資料源**:
  - **DDInter**: 222,391 筆藥物交互作用
  - **Guide to PHARMACOLOGY**: 4,636 筆藥物交互作用
- **整合**: 建立 `UnifiedDDICollector` 整合雙來源

### 4. 新建立的檔案
```
src/twtxgnn/collectors/ddinter.py              # DDInter 資料收集器
src/twtxgnn/collectors/pharmacology.py         # Guide to PHARMACOLOGY 收集器
src/twtxgnn/collectors/unified_ddi.py          # 整合 DDI 收集器
tests/test_collectors_ddinter.py               # DDInter 測試
tests/test_collectors_unified_ddi.py           # 整合 DDI 測試
```

### 5. 測試結果
- **總計**: 341 項測試全部通過
- **涵蓋**: Collectors、Reviewer、Writer、Paths 等所有模組

---

## 下次進入時要做的事

### 優先順序 1: 產生完整 Evidence Packs
1. 設定 `OPENAI_API_KEY` 環境變數
2. 產生以下藥物的 Evidence Pack:
   - **Minoxidil** (新)
   - **Warfarin** (新)
   - **levamisole** (重新產生，使用修復後的 JSON 序列化)
   - **travoprost** (重新產生，使用修復後的 JSON 序列化)

### 優先順序 2: 產生完整報告
1. 使用修復後的 Evidence Pack 產生所有藥物的報告
2. 驗證 Pharmacist Notes 和 Sponsor Notes 的一致性
3. 使用 `scripts/validate_notes_consistency.py` 進行驗證

### 優先順序 3: 文件更新
1. 更新 README.md 說明新的 DDI 資料來源
2. 記錄 Evidence Pack JSON 修復的技術細節

---

## 專案現況

### 測試狀態
- ✅ 341 項測試全部通過

### 資料檔案
- ✅ node.csv (TxGNN 節點資料)
- ✅ kg.csv (TxGNN 知識圖譜)
- ✅ edges.csv (TxGNN 邊資料)
- ✅ tw_fda_drugs.json (台灣 FDA 藥品資料)

### 預測結果
- ✅ 知識圖譜預測: 142,351 筆
- ✅ 深度學習預測: 23,925,564 筆

### Evidence Pack 狀態
| 藥物 | .md Evidence Pack | .json Evidence Pack | Pharmacist Notes | Sponsor Notes |
|------|-------------------|---------------------|------------------|---------------|
| levamisole | ✅ 4.5KB | ⚠️ 需重新產生 | ✅ 320行 | ⚠️ 需重新產生 |
| travoprost | ✅ 5.1KB | ⚠️ 需重新產生 | ⚠️ 需重新產生 | ⚠️ 需重新產生 |
| minoxidil | ❌ 待產生 | ❌ 待產生 | ❌ 待產生 | ❌ 待產生 |
| warfarin_af | ❌ 待產生 | ❌ 待產生 | ❌ 待產生 | ❌ 待產生 |

---

## 架構概覽

### Writer 模組
```
src/twtxgnn/writer/
├── base.py                 # BaseNotesWriter 抽象基底
├── pharmacist.py           # PharmacistNotesWriter (v1)
├── sponsor.py              # SponsorNotesWriter (v1)
├── drug_pharmacist.py      # DrugPharmacistNotesWriter (v4)
└── drug_sponsor.py         # DrugSponsorNotesWriter (v4)
```

### Collectors 模組
```
src/twtxgnn/collectors/
├── base.py                 # BaseCollector 抽象基底
├── bundle.py               # 資料收集器整合
├── tfda.py                 # 台灣 FDA 資料收集器
├── ddinter.py              # DDInter 藥物交互作用收集器
├── pharmacology.py         # Guide to PHARMACOLOGY 收集器
└── unified_ddi.py          # 整合 DDI 收集器
```

### Reviewer 模組
```
src/twtxgnn/reviewer/
├── drug_evidence_pack.py   # Evidence Pack 產生器（已修復 JSON 序列化）
└── llm_client.py           # LLM 客戶端
```

---

## 相關檔案路徑

```
# 核心模組
src/twtxgnn/reviewer/drug_evidence_pack.py   # Evidence Pack 產生器（已修復）
src/twtxgnn/reviewer/llm_client.py           # LLM 客戶端
src/twtxgnn/writer/base.py                   # Writer 基底類別
src/twtxgnn/collectors/unified_ddi.py        # 整合 DDI 收集器（新）

# Prompts
prompts/Notes Writer/pharmacist_v4_drug_centric.md
prompts/Notes Writer/sponsor_v4_drug_centric.md

# 產出
data/evidence_packs/                         # Evidence Packs
data/notes/                                  # 產生的筆記

# 驗證腳本
scripts/validate_notes_consistency.py
scripts/validate_report.py
scripts/run_validation_pipeline.py
```

---

## 快速指令

```bash
# 執行所有測試
uv run pytest tests/ -v

# 執行 Writer 測試
uv run pytest tests/test_writer.py -v

# 執行 Reviewer 測試
uv run pytest tests/test_reviewer.py -v

# 執行 Collectors 測試
uv run pytest tests/test_collectors_*.py -v

# 檢查 Evidence Pack 內容
cat data/evidence_packs/levamisole/levamisole_drug_evidence_pack.json

# 驗證筆記一致性
uv run python scripts/validate_notes_consistency.py

# 產生 Evidence Pack（需設定 OPENAI_API_KEY）
export OPENAI_API_KEY="your-api-key"
uv run python -c "from src.twtxgnn.reviewer.drug_evidence_pack import DrugEvidencePack; ..."
```

---

## 已解決的問題

### ✅ 問題 1: Evidence Pack JSON 為空
- **位置**: `data/evidence_packs/*/xxx_drug_evidence_pack.json`
- **症狀**: 檔案內容僅 `{}`，但對應的 `.md` 有完整內容
- **影響**: Writer 讀取 JSON 失敗，導致報告產生失敗
- **根因**: `src/twtxgnn/reviewer/drug_evidence_pack.py` JSON 序列化有問題
- **解決**: 修改 `_parse_response` 方法，改進 JSON 解析邏輯（2026-02-08）

### ✅ 問題 2: Lexicomp DDI 資料無法公開使用
- **症狀**: Lexicomp 是私有資料庫，無法在開源專案中使用
- **解決**: 移除 Lexicomp，改用 DDInter (222,391 筆) 和 Guide to PHARMACOLOGY (4,636 筆)
- **實作**: 建立 `UnifiedDDICollector` 整合雙來源（2026-02-08）
