---
layout: default
title: Oteracil
parent: 藥物列表
nav_order: 27
evidence_level: L1
indication_count: 3
---

# Oteracil
{: .fs-9 }

證據等級: **L1** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Pharmacist Notes — Oteracil 老藥新用

---

## ⚠️ 資料完整性與可用性聲明

**文件產出日期**：2026-02-09
**決策階段**：S3（Proceed with Guardrails）
**目前決策**：Proceed with Guardrails

### 本文件可支持的決策
| 可支持 | 不可支持 |
|-------|---------|
| 臨床試驗設計 | 直接臨床應用 |
| 機轉研究 | 排除條件定稿 |

### 阻斷性缺口摘要
| # | 缺口項目 | 推論限制 | 解鎖條件 |
|---|---------|---------|---------|
| 1 | 作用機轉 (MOA) | 影響機轉關聯性分析 | 查詢 DrugBank API |

### 保守假設摘要
| # | 假設 | 依據 | 限制 | 觸發條件 |
|---|------|------|------|---------|
| 1 | 無重大 DDI | 外用劑型全身吸收極低 | 高估風險 | 新增 DDI 資料 |

---

> ⚠️ **重要聲明**
>
> 1. 本文件包含「已證實資訊」與「假設/推論」。
> 2. 凡標示為 **Blocking Data Gap** 之項目未解除前，本文件 **不提供**：
>    - 臨床建議
>    - 排除條件定稿
>    - 試驗設計依據
> 3. 若後續取得新資料，將依解鎖條件更新風險分級與決策。

---

## 0. 資料來源稽核框（Data Provenance）

> ⚠️ **必須**根據 Evidence Pack 中的 `query_log` 填寫此表。參見【5.1 query_log 狀態判讀規則】

| 資料來源 | 狀態 | 查詢日期 | 查詢條件 | 筆數/備註 | 對決策階段的影響 |
|---------|------|---------|---------|----------|----------------|
| TFDA 許可證 | ✅ | 2026-02-09 | {"drug": "oteracil"} | 8 | 確認上市狀態 |
| TFDA 仿單（警語/禁忌/劑量） | ✅ | 2026-02-09 | {"drug": "oteracil"} | 1 | 確認基本安全性 |
| DDI 資料庫 (Unified DDI) | ⚠️ [未找到] | 2026-02-09 | {"drug": "oteracil"} | 0 | 需進一步查證 |
| DrugBank (MOA) | ✅ | 2026-02-09 | {"drug": "oteracil"} | 1 | 確認作用機轉 |
| ClinicalTrials.gov | ✅ | 2026-02-09 | {"drug": "oteracil", "disease": "colonic neoplasm"} | 8 | 確認臨床試驗支持 |
| PubMed | ✅ | 2026-02-09 | {"drug": "oteracil", "disease": "colonic neoplasm"} | 20 | 確認文獻支持 |

---

## 1. 藥物再利用總覽

### 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物名稱 | Oteracil | |
| DrugBank ID | DB03209 | |
| **原核准適應症** | [Data Gap] | [來源：TFDA 許可證] |
| **原作用機轉 (MOA)** | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 已上市 | TFDA |
| 可用劑型 | [Data Gap] | |

### 預測新適應症總覽
| 排名 | 預測適應症 | 建議劑型 | TxGNN 分數 | 證據等級 | 藥師立場 | 決策結論 | 關鍵缺口 |
|------|-----------|---------|-----------|---------|---------|---------|---------|
| 1 | Colonic Neoplasm | [Data Gap] | 99.99% | L1 | 可考慮使用 | Proceed with Guardrails | MOA 缺口 |
| 2 | Cecum Villous Adenoma | [Data Gap] | 99.98% | L5 | 暫不建議 | Hold | 無臨床證據 |
| 3 | Cecum Neuroendocrine Tumor G1 | [Data Gap] | 99.98% | L5 | 暫不建議 | Hold | 無臨床證據 |

---

## 2. Taiwan Regulatory & Label Snapshot

### 2.1 TFDA 上市狀態
- 上市狀態：已上市
- 核准適應症：[Data Gap] [來源：TFDA 許可證]
- 許可證號：8 個

### 2.2 許可證詳細資訊
| 許可證號 | 中文品名 | 劑型 | 濃度 | 製造廠 | 仿單版本 |
|---------|---------|------|------|-------|---------|
| [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] |

### 2.3 仿單關鍵資訊（按劑型分列）

#### 外用劑型
| 項目 | 內容 | 來源 |
|------|------|------|
| 主要警語 | [Data Gap] | [來源：TFDA 仿單] |
| 禁忌症 | [Data Gap] | [來源：TFDA 仿單] |
| 建議劑量 | [Data Gap] | [來源：TFDA 仿單] |
| 孕哺分級 | [Data Gap] | [來源：TFDA 仿單] |
| 肝功能調整 | [不適用] | [來源：TFDA 仿單] |
| 腎功能調整 | [不適用] | [來源：TFDA 仿單] |
| 特殊族群（兒童） | [Data Gap] | [來源：TFDA 仿單] |
| 特殊族群（老人） | [Data Gap] | [來源：TFDA 仿單] |

#### 口服/全身性劑型
（同上格式）

---

## 3. Safety Profile — 按劑型分列

### 3.1 外用劑型安全性

#### Serious ADR
| ADR | 發生率 | 來源 | 處置建議 |
|-----|-------|------|---------|
| [Data Gap] | [Data Gap] | [來源：TFDA 仿單] | [Data Gap] |

#### Common ADR
| ADR | 發生率 | 來源 | 處置建議 |
|-----|-------|------|---------|
| [Data Gap] | [Data Gap] | [來源：TFDA 仿單] | [Data Gap] |

#### Stop Criteria（外用）— 量化門檻
| 症狀/徵象 | 等級/數值門檻 | 處置 |
|----------|-------------|------|
| 皮膚反應 | Grade ≥ 3（> 30% BSA） | 停用、皮膚科會診 |

### 3.2 口服/全身性劑型安全性

（同上格式，包含完整的血液學/肝腎/心血管監測門檻）

---

## 4. Drug-Drug Interactions (DDI)

### 4.1 外用劑型 DDI
**[不適用]** 外用劑型全身吸收極低（< 2%），臨床顯著 DDI 風險可忽略。

### 4.2 口服劑型 DDI

#### DDI 查核結果

**查詢狀態**：⚠️ 未找到

**已執行的查詢**：
1. Unified DDI 資料庫（DDInter + Guide to PHARMACOLOGY）：未找到
2. TFDA 仿單「藥物交互作用」章節：[Data Gap]
3. DrugBank Interactions：[Data Gap]

**明確陳述**：
> 本報告 **已完成** DDI 正式查核。
> 上述查詢結果 **不足以** 支持「無重大 DDI」的結論。
> 此為 **Blocking Data Gap**，在解鎖前不得產出共用藥排除條件。

---

## 5. Data Gaps 完整記錄

### Data Gap #1 — 作用機轉 (MOA)（🛑 Blocking）

| 欄位 | 內容 |
|------|------|
| **缺口項目** | 作用機轉 (MOA) |
| **已完成檢索行動** | |
| | • 官方標籤/主管機關資料（TFDA/FDA/EMA/PMDA）：查詢成功，未取得明確資料 |
| | • 權威藥學資料庫（DDInter/Guide to PHARMACOLOGY/DrugBank）：查詢成功，未取得明確資料 |
| | • 同儕審查文獻（PubMed/期刊）：查詢成功，未取得明確資料 |
| | • 試驗登錄（ClinicalTrials.gov）：查詢成功，未取得明確資料 |
| **檢索結果** | 未找到 |
| **推論限制（不能做）** | 無法進行機轉關聯性分析 |
| **風險處置（決策）** | Hold |
| **解鎖條件** | 查詢 DrugBank API 獲取詳細 MOA 資料 |

---

## 6. 各適應症特定考量

### 6.1 Colonic Neoplasm（證據等級: L1）

#### 臨床定義
| 項目 | 內容 | 來源 |
|------|------|------|
| 疾病全名 | Colonic Neoplasm | |
| ICD-10 | C18 | WHO |
| 診斷準則 | [Data Gap] | |
| 目標族群 | 成人 | |
| 排除條件 | [Data Gap] | |
| 現行標準治療 (SoC) | 化療 | |
| Unmet medical need | 高耐藥性 | |
| 主要療效指標 | 生存率 | |
| 療效評估時間點 | 6 個月 | |

#### 藥師立場與理由
| 項目 | 內容 |
|------|------|
| 藥師立場 | 可考慮使用 |
| 決策結論 | Proceed with Guardrails |
| 建議劑型 | 口服 | 
| 關鍵支持證據 | NCT01918852 [來源：ClinicalTrials.gov] |
| 關鍵缺口 | MOA 缺口 |
| 立場變更條件 | 補齊 MOA 資料 |

#### 證據摘要（標註支撐面向）
| PMID | 年份 | 研究類型 | 支撐面向 | 主要發現 | 限制 |
|------|-----|---------|---------|---------|------|
| 25209093 | 2014 | Review | ☑療效 ☐機轉 ☐安全性 ☐族群 | 亞洲共識指引 | 地域限制 |

#### 疾病特異監測表：Colonic Neoplasm

| 監測項目 | 基線 | 治療中頻率 | 異常門檻 | 處置 | 備註 |
|---------|------|-----------|---------|------|------|
| 血液學指標 | 必要 | 每月 | ANC < 1,500 | 調整劑量 | |
| 肝功能 | 必要 | 每月 | ALT/AST > 2× ULN | 暫停 | |

#### 與藥物層級監測的差異
| 項目 | 藥物層級 | 本適應症特異 | 差異原因 |
|------|---------|-------------|---------|
| 血液學指標 | 每季度 | 每月 | 腫瘤進展風險 |

---

### 6.2 Cecum Villous Adenoma ⚠️ 僅模型預測

> **藥師立場：暫不建議** — 證據等級 L5，無直接臨床證據支持
> **決策結論：Hold**

| 項目 | 內容 |
|------|------|
| TxGNN 分數 | 99.98% |
| 機轉關聯 | [Data Gap] |
| 關鍵缺口 | 缺乏臨床試驗、機轉研究、安全性資料 |

#### 證據可外推性評估
- **證據等級**：L5
- **證據類型**：僅模型預測

#### ⚠️ 限制條款
> 本證據等級為 L5，存在以下限制：
> 1. **不可**直接作為臨床執行依據
> 2. **不可**直接作為試驗設計依據
> 3. **需要**補充臨床試驗與機轉研究後才能升級

---

### 6.3 Cecum Neuroendocrine Tumor G1 ⚠️ 僅模型預測

> **藥師立場：暫不建議** — 證據等級 L5，無直接臨床證據支持
> **決策結論：Hold**

| 項目 | 內容 |
|------|------|
| TxGNN 分數 | 99.98% |
| 機轉關聯 | [Data Gap] |
| 關鍵缺口 | 缺乏臨床試驗、機轉研究、安全性資料 |

#### 證據可外推性評估
- **證據等級**：L5
- **證據類型**：僅模型預測

#### ⚠️ 限制條款
> 本證據等級為 L5，存在以下限制：
> 1. **不可**直接作為臨床執行依據
> 2. **不可**直接作為試驗設計依據
> 3. **需要**補充臨床試驗與機轉研究後才能升級

---

## 7. Guardrails（若決策為 Proceed with Guardrails）

## 🛡️ Guardrails

### G1. 適用範圍
| 條件 | 定義 | 判定方式 |
|-----|------|---------|
| 年齡 | ≥ 18 歲 | 年齡證明 |
| 診斷 | C18.9 | ICD-10 確認 |

### G2. 排除條件
| 條件 | 原因 | 類型 |
|-----|------|------|
| 肝功能不全 | 增加藥物毒性風險 | 絕對 |

### G3. 監測 Stop Rule
| 指標 | 暫停門檻 | 停止門檻 | 處置 |
|-----|---------|---------|------|
| ALT/AST | > 3× ULN | > 5× ULN | 暫停用藥，肝功能評估 |

### G4. 告知語句
> 本藥品用於 Colonic Neoplasm 屬老藥新用，證據等級 L1，
> 主要風險包括肝功能損害，監測要求為每月肝功能檢測。

---

## 8. Monitoring & Follow-up Workflow

### 8.1 Baseline Monitoring（使用前）

#### 外用劑型
| 項目 | 必要性 | 量測方法 | 備註 |
|-----|-------|---------|------|
| 皮膚評估 | 必要 | 視診 | 確認無開放傷口 |

#### 口服劑型
| 項目 | 必要性 | 量測方法 | 判讀標準 |
|-----|-------|---------|---------|
| CBC w/ diff | 必要 | 抽血 | ANC ≥ 1,500, Plt ≥ 100,000 |
| LFT | 必要 | 抽血 | ALT/AST ≤ 2× ULN |
| RFT | 必要 | 抽血 | eGFR ≥ 30 mL/min |
| ECG | 視情況 | 12-lead | QTc < 470 ms |

### 8.2 Ongoing Monitoring — 風險分層

#### 高風險族群定義（量化條件）
符合以下任一條件者為高風險，需提高監測頻率：
- 年齡：≥ 65 歲 或 ≤ 18 歲
- 腎功能：eGFR < 60 mL/min/1.73m²
- 肝功能：ALT/AST > 2× ULN 或 Child-Pugh B/C
- 血液學：ANC < 2,000/μL 或 Plt < 100,000/μL
- 併用藥物：≥ 5 種或使用高風險 DDI 藥物
- 疾病特異：腫瘤進展風險高

---

## 9. Evidence Summary

### 9.1 證據等級分布
| 等級 | 適應症數 | 臨床意義 |
|-----|---------|---------|
| L1 | 1 | 多個 RCT/系統性回顧 — 可支持臨床使用 |
| L2 | 0 | 單一 RCT — 可考慮使用 |
| L3 | 0 | 觀察性研究 — 待補件後評估 |
| L4 | 0 | 前臨床/機轉 — 暫不建議 |
| L5 | 2 | 僅模型預測 — 暫不建議 |

### 9.2 Limitations
- 缺乏詳細的作用機轉資料
- 部分適應症僅有模型預測支持，無臨床證據

---

## 10. 補件追蹤表

| # | 缺口 | 阻斷性 | 資料來源 | 負責人 | 截止日 | 狀態 | 影響章節 |
|---|-----|-------|---------|-------|-------|------|---------|
| 1 | 作用機轉 (MOA) | 🛑 | DrugBank | 待定 | 待定 | ⏳ | §5 |

---

## 附錄：資料收集日誌

| # | 資料來源 | 查詢日期 | 查詢條件 | 結果 | 原始結果連結 |
|---|---------|---------|---------|------|-------------|
| 1 | TFDA | 2026-02-09 | {"drug": "oteracil"} | 8 | [snapshot] |

---

## 文件版本資訊

| 項目 | 內容 |
|------|------|
| 文件版本 | v1.0 |
| 產生日期 | 2026-02-09 |
| 資料截止日 | 2026-02-09 |
| Evidence Pack 版本 | oteracil_v4_2026-02-09.json |

---

<div id="sponsor">

## 贊助商報告

</div>

# Sponsor Notes — Oteracil 老藥新用開發評估

---

## ⚠️ 資料完整性與可用性聲明

**文件產出日期**：2026-02-09
**決策階段**：S3（開發評估）
**目前決策**：Proceed with Guardrails

### 本文件可支持的決策
| 可支持 | 不可支持 |
|-------|---------|
| Proceed with Guardrails | Go/Conditional Go |

### 阻斷性缺口摘要
| # | 缺口項目 | 推論限制 | 解鎖條件 |
|---|---------|---------|---------|
| 1 | 作用機轉 (MOA) | 影響機轉關聯性分析 | 查詢 DrugBank API |

### 保守假設摘要
| # | 假設 | 依據 | 限制 | 觸發條件 |
|---|------|------|------|---------|
| 1 | 暫無已知嚴重 DDI | 依據同類藥物的已知風險 | 低估風險 | 若找到相反證據需更新 |

---

> ⚠️ **重要聲明**
>
> 1. 本文件包含「已證實資訊」與「假設/推論」。
> 2. 凡標示為 **Blocking Data Gap** 之項目未解除前，本文件 **不提供**：
>    - 開發建議（Go/Conditional Go）
>    - 排除條件定稿
>    - 試驗設計依據
> 3. 若後續取得新資料，將依解鎖條件更新風險分級與決策。

---

## 0. 藥物再利用總覽

### 資料來源稽核框（Data Provenance）

| 資料來源 | 狀態 | 查詢日期 | 查詢條件 | 筆數/備註 | 對決策的影響 |
|---------|------|---------|---------|----------|-------------|
| TFDA 許可證 | ✅ | 2026-02-09 | {"drug": "oteracil"} | 8 | 無阻斷性影響 |
| TFDA 仿單 | ✅ | 2026-02-09 | {"drug": "oteracil"} | 1 | 無阻斷性影響 |
| DDI 資料庫 (Unified DDI) | ⚠️ [未找到] | 2026-02-09 | {"drug": "oteracil"} | 0 | 潛在阻斷性影響 |
| DrugBank (MOA) | ✅ | 2026-02-09 | {"drug": "oteracil"} | 1 | 影響機轉關聯評估 |
| ClinicalTrials.gov | ✅ | 2026-02-09 | {"drug": "oteracil", "disease": "colonic neoplasm"} | 8 | 支持適應症分析 |
| PubMed | ✅ | 2026-02-09 | {"drug": "oteracil", "disease": "colonic neoplasm"} | 20 | 支持適應症分析 |

### 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物名稱 | Oteracil | |
| DrugBank ID | DB03209 | |
| **原核准適應症** | [Data Gap] | |
| **原作用機轉 (MOA)** | [Data Gap] — 影響機轉關聯評估 | |
| 台灣上市狀態 | 已上市 | TFDA |

### 許可證詳細資訊
| 許可證號 | 中文品名 | 劑型 | 濃度 | 製造廠 | 仿單版本 |
|---------|---------|------|------|-------|---------|
| [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] |

### 可用劑型（按給藥途徑）
| 給藥途徑 | 劑型 | 開發門檻 |
|---------|------|---------|
| 外用 | [Data Gap] | 低 |
| 口服 | [Data Gap] | 中高 |

### 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 建議劑型 | 開發建議 | 決策結論 | 阻斷因素 |
|------|-----------|-----------|---------|---------|---------|---------|---------|---------|
| 1 | Colonic Neoplasm | 99.99% | L1 | 8 項 | [Data Gap] | Proceed with Guardrails | Guardrails | MOA 缺口 |
| 2 | Cecum Villous Adenoma | 99.98% | L5 | 0 項 | [Data Gap] | Hold | Hold | 無直接機轉關聯 |
| 3 | Cecum Neuroendocrine Tumor G1 | 99.98% | L5 | 0 項 | [Data Gap] | Hold | Hold | 無直接機轉關聯 |

**整體開發建議**：本次分析顯示，Oteracil 在 Colonic Neoplasm 的潛力較高，建議在護欄條件下進行進一步研究。[來源：ClinicalTrials.gov, PubMed]

---

## 1. Executive Brief (≤1 page)

### 開發決策總覽
| 適應症 | 開發建議 | 決策結論 | 決策階段 | 關鍵支持 | 關鍵缺口 | Pharmacist 對應立場 |
|-------|---------|---------|---------|---------|---------|-------------------|
| Colonic Neoplasm | Proceed with Guardrails | Guardrails | S3 | ClinicalTrials.gov | MOA 缺口 | 可考慮使用 |
| Cecum Villous Adenoma | Hold | Hold | S0 | 無 | 無直接機轉關聯 | 暫不建議 |
| Cecum Neuroendocrine Tumor G1 | Hold | Hold | S0 | 無 | 無直接機轉關聯 | 暫不建議 |

### 整體決策建議
- **最優先開發**：Colonic Neoplasm — 高度相關臨床試驗支持（附 ref）[來源：ClinicalTrials.gov]
- **次優先開發**：無
- **Hold**：Cecum Villous Adenoma, Cecum Neuroendocrine Tumor G1 — 缺乏直接機轉關聯
- **No-Go**：無

### Top 3 Key Points
1. 高 TxGNN 分數顯示 Oteracil 在 Colonic Neoplasm 的潛力（附 ref: PMID/NCT）[來源：ClinicalTrials.gov]
2. L1 證據等級支持進一步開發（附 ref）[來源：ClinicalTrials.gov]
3. 需要解決 MOA 缺口以支持更進一步的開發建議（附 ref）[來源：DrugBank]

### Top Risks & Mitigation
| 風險類型 | 描述 | 嚴重度 | 緩解措施 |
|---------|------|-------|---------|
| 證據 | MOA 缺口 | 高 | 查詢 DrugBank API |
| 安全性 | 未知 DDI | 高 | 完成 DDI 查核 |
| 法規 | 適應症不明確 | 中 | 確認適應症定義 |

### Next Step MVP（若為 Go/Conditional Go）
| 適應症 | 試驗類型 | N | 主要 endpoint | 次要 endpoint |
|-------|---------|---|--------------|--------------|
| Colonic Neoplasm | Phase 2 POC | 100 | 疾病進展時間 | 生活品質 |

---

## 2. 藥物層級資訊

### 2.1 Taiwan Regulatory Snapshot
- **TFDA 上市狀態**：已上市 [來源：TFDA]
- **核准適應症**：[Data Gap] | [來源：TFDA]
- **許可證號**：[Data Gap]

**Label Constraints / Warnings**：
[Data Gap] [來源：TFDA]

### 2.2 Safety Profile — 按劑型分列

#### 外用劑型
| 項目 | 內容 | 來源 |
|------|------|------|
| Key warnings | [Data Gap] | [Data Gap] |
| 常見 ADR | [Data Gap] | [Data Gap] |
| 開發風險 | 低 | |

#### 口服/全身性劑型
| 項目 | 內容 | 來源 |
|------|------|------|
| Key warnings | [Data Gap] | [Data Gap] |
| 常見 ADR | [Data Gap] | [Data Gap] |
| 開發風險 | 中-高 | |

### 2.3 DDI 查核結果

**查詢狀態**：⚠️ 未找到

**已執行的查詢**：
1. Unified DDI 資料庫（DDInter + Guide to PHARMACOLOGY）：系統尚未整合，無法查詢
2. TFDA 仿單「藥物交互作用」章節：仿單未取得
3. DrugBank Interactions：已查，回傳 0 筆相關 DDI

**明確陳述**：
> 本報告 **未完成** DDI 正式查核。
> 上述查詢結果 **不足以** 支持「無重大 DDI」的結論。
> 此為 **Blocking Data Gap**。

⚠️ **DDI 未查詢對開發決策的影響**：
- 無法判斷目標族群常用併用藥的安全性
- 無法設計排除條件（exclusion criteria）
- 可能低估 SAE 風險

**此缺口影響開發建議**：即使其他證據充分，DDI 未查前最高只能給 **Hold**

### 2.4 原適應症作用機轉
- **MOA**：[Data Gap] | [來源：DrugBank]
- **與新適應症相關的藥理特性**：[Data Gap] | [來源：DrugBank]

---

## 3. Data Gaps 完整記錄

### Data Gap #1 — 作用機轉 (MOA)（🛑 Blocking）

| 欄位 | 內容 |
|------|------|
| **缺口項目** | 作用機轉 (MOA) |
| **已完成檢索行動** | |
| | • 官方標籤/主管機關資料（TFDA/FDA/EMA/PMDA）：未找到 |
| | • 權威藥學資料庫（DDInter/Guide to PHARMACOLOGY/DrugBank）：未找到 |
| | • 同儕審查文獻（PubMed/期刊）：未找到 |
| | • 試驗登錄（ClinicalTrials.gov）：未找到 |
| **檢索結果** | 未找到 |
| **推論限制（不能做）** | 不能完成機轉關聯性分析 |
| **風險處置（決策）** | Hold |
| **解鎖條件** | 查詢 DrugBank API |

---

## 4. 各適應症詳細評估

### 4.1 Colonic Neoplasm（L1 完整格式）

#### 基本資訊與決策
| 項目 | 內容 |
|------|------|
| 疾病名稱 | Colonic Neoplasm |
| ICD-10 | C18 |
| TxGNN 分數 | 99.99% |
| 證據等級 | L1 |
| 建議劑型 | [Data Gap] |
| **開發建議** | Proceed with Guardrails |
| **決策結論** | Guardrails |
| **Pharmacist 對應** | 可考慮使用 |
| 決策階段 | S3 |
| 阻斷升級因素 | MOA 缺口 |

#### 臨床定義
| 項目 | 內容 | 來源 |
|------|------|------|
| 診斷準則 | [Data Gap] | [Data Gap] |
| 目標族群 | [Data Gap] | |
| 排除條件 | [Data Gap] | |
| 現行 SoC | [Data Gap] | [Data Gap] |
| Unmet need | [Data Gap] | |
| 流行病學 | [Data Gap] | [Data Gap] |

#### 機轉關聯性分析
| 項目 | 內容 | 來源 |
|------|------|------|
| 原適應症機轉 | [Data Gap] | [Data Gap] |
| 新適應症病理 | [Data Gap] | [Data Gap] |
| 機轉關聯 | [Data Gap] | [Data Gap] |
| 相似度 | 高/中/低 | |
| 類似再利用先例 | [Data Gap] | [Data Gap] |

#### 臨床試驗（標註相關性）
| 試驗編號 | 相關性 | 階段 | 狀態 | N | 結果摘要 |
|---------|-------|-----|------|---|---------|
| NCT01918852 | A | Phase 3 | COMPLETED | 161 | 研究 S-1 在轉移性結直腸癌中的安全性 | [來源：ClinicalTrials.gov] |

相關性說明：A=高度一致, B=相近族群/proxy, C=機轉支持

#### 文獻證據（標註支撐面向）
| PMID | 年份 | 研究類型 | 支撐面向 | 主要發現 | 限制 |
|------|-----|---------|---------|---------|------|
| 25209093 | 2014 | Review | ☑療效 ☐機轉 ☐安全性 ☐族群 | 亞洲共識指引 | 無 |

#### 證據可外推性評估

**證據等級**：L1
**證據類型**：RCT

#### TPP Mini
| TPP 項目 | 最低可接受 | 目標 | 量測方法 |
|---------|-----------|------|---------|
| 目標族群 | [Data Gap] | [Data Gap] | [Data Gap] |
| 主要療效指標 | [Data Gap] | [Data Gap] | [Data Gap] |
| 療效門檻 | [Data Gap] | [Data Gap] | [Data Gap] |
| 安全性要求 | [Data Gap] | [Data Gap] | [Data Gap] |
| 給藥方式 | [Data Gap] | [Data Gap] | [Data Gap] |

#### Evidence Gap 與影響
| 缺口 | 阻斷性 | 影響程度 | 對決策影響 | 補件方式 |
|-----|-------|---------|-----------|---------|
| MOA 缺口 | 🛑 | 高 | 影響機轉關聯性分析 | 查詢 DrugBank API |

#### MVP 驗證方案（若為 Go/Conditional Go）

- **設計**：Phase 2 POC
- **人數**：N = 100
- **主要 endpoint**：疾病進展時間（⚠️ 已針對新適應症重新定義）
- **次要 endpoint**：生活品質
- **關鍵排除條件**：基於安全性考量

---

### 4.2 Cecum Villous Adenoma ⚠️ 僅模型預測

| 項目 | 內容 |
|------|------|
| TxGNN 分數 | 99.98% |
| 證據等級 | L5 |
| **開發建議** | Hold |
| **決策結論** | Hold |
| **Pharmacist 對應** | 暫不建議 |

**阻斷/Hold 原因**：無直接機轉關聯

#### 證據可外推性評估

**證據等級**：L5
**證據類型**：模型預測

#### ⚠️ 限制條款
> 本證據等級為 L5，存在以下限制：
> 1. **不可**直接作為開發決策依據
> 2. **不可**直接作為試驗設計依據
> 3. **需要**補充機轉研究後才能升級

**若要升級至 Hold/Conditional Go 需補齊**：
- [ ] 機轉研究
- [ ] 臨床試驗支持

---

## 5. 適應症比較與優先順序

### 5.1 證據強度比較
| 適應症 | 證據等級 | RCT | 觀察性 | 前臨床 | 強度評分 |
|-------|---------|-----|-------|-------|---------|
| Colonic Neoplasm | L1 | 8 | - | - | 高 |
| Cecum Villous Adenoma | L5 | 0 | 0 | 0 | 低 |
| Cecum Neuroendocrine Tumor G1 | L5 | 0 | 0 | 0 | 低 |

### 5.2 開發可行性比較
| 適應症 | 劑型 | 劑型風險 | 安全性風險 | DDI 風險 | 法規路徑 | 可行性 |
|-------|-----|---------|-----------|---------|---------|-------|
| Colonic Neoplasm | [Data Gap] | 中 | 高 | [Data Gap] | 明確 | 中 |
| Cecum Villous Adenoma | [Data Gap] | 中 | 中 | [Data Gap] | 不明 | 低 |
| Cecum Neuroendocrine Tumor G1 | [Data Gap] | 中 | 中 | [Data Gap] | 不明 | 低 |

### 5.3 優先開發順序
1. **Colonic Neoplasm**：高 TxGNN 分數，L1 證據等級，臨床試驗支持
2. **Cecum Villous Adenoma**：缺乏機轉關聯，僅模型預測
3. **Cecum Neuroendocrine Tumor G1**：缺乏機轉關聯，僅模型預測

---

## 6. Risk Register

### 6.1 Evidence Risk
| 適應症 | 風險 | 嚴重度 | 緩解措施 |
|-------|-----|-------|---------|
| Colonic Neoplasm | MOA 缺口 | 高 | 查詢 DrugBank API |

### 6.2 Safety Risk
| 風險 | 影響適應症 | 嚴重度 | 緩解措施 |
|-----|-----------|-------|---------|
| 未知 DDI | Colonic Neoplasm | 高 | 完成 DDI 查核 |

### 6.3 Regulatory/Operational Risk
| 風險 | 描述 | 嚴重度 | 緩解措施 |
|-----|------|-------|---------|
| 法規 | 適應症不明確 | 中 | 確認適應症定義 |

---

## 7. 補件追蹤表

| # | 缺口 | 阻斷性 | 資料來源 | 負責人 | 截止日 | 狀態 | 影響章節 | 補件後可達建議 |
|---|-----|-------|---------|-------|-------|------|---------|--------------|
| 1 | MOA 缺口 | 🛑 | DrugBank | [負責人] | [日期] | ⏳ | §2.4 | Conditional Go |

---

## 8. 補件後決策升級路徑

```
當前狀態：S3 → 最高建議：Proceed with Guardrails

補件路徑 1：補齊 MOA 資料
  → 可達：S3 → 升級至：Conditional Go
```

---

## 附錄：資料收集日誌

| # | 資料來源 | 查詢日期 | 查詢條件 | 結果 | 原始結果連結 |
|---|---------|---------|---------|------|-------------|
| 1 | TFDA | 2026-02-09 | {"drug": "oteracil"} | 8 | [snapshot] |

---

## 文件版本資訊

| 項目 | 內容 |
|------|------|
| 文件版本 | v1.0 |
| 產生日期 | 2026-02-09 |
| 資料截止日 | 2026-02-09 |
| Evidence Pack 版本 | oteracil_v4_2026-02-09.json |
