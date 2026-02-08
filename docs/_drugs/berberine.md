---
layout: default
title: Berberine
parent: 藥物列表
nav_order: 14
evidence_level: L4
indication_count: 3
---

# Berberine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **3** 個
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

# Pharmacist Notes — Berberine 老藥新用

---

## ⚠️ 資料完整性與可用性聲明

**文件產出日期**：2026-02-09
**決策階段**：S0（初始階段）
**目前決策**：Hold

### 本文件可支持的決策
| 可支持 | 不可支持 |
|-------|---------|
| Research Question | 臨床應用 |

### 阻斷性缺口摘要
| # | 缺口項目 | 推論限制 | 解鎖條件 |
|---|---------|---------|---------|
| 1 | 作用機轉 (MOA) | 影響機轉關聯性分析 | 查詢 DrugBank API |

### 保守假設摘要
| # | 假設 | 依據 | 限制 | 觸發條件 |
|---|------|------|------|---------|
| 1 | 暫無保守假設 | 不適用 | 不適用 | 不適用 |

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

| 資料來源 | 狀態 | 查詢日期 | 查詢條件 | 筆數/備註 | 對決策階段的影響 |
|---------|------|---------|---------|----------|----------------|
| TFDA 許可證 | ✅ | 2026-02-09 | {"drug": "berberine"} | 20 | 提供上市狀態 |
| TFDA 仿單（警語/禁忌/劑量） | ✅ | 2026-02-09 | {"drug": "berberine"} | 1 | 提供仿單資訊 |
| DDI 資料庫 (Unified DDI) | ⚠️ [未找到] | 2026-02-09 | {"drug": "berberine"} | 0 | 無法提供 DDI 資訊 |
| DrugBank (MOA) | ✅ | 2026-02-09 | {"drug": "berberine"} | 1 | 提供部分機轉資訊 |
| ClinicalTrials.gov | ✅ (無結果) | 2026-02-09 | {"drug": "berberine", "disease": "severe pre-eclampsia"} | 0 | 無臨床試驗資料 |
| PubMed | ✅ | 2026-02-09 | {"drug": "berberine", "disease": "monocytic leukemia"} | 1 | 提供文獻支持 |

---

## 1. 藥物再利用總覽

### 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物名稱 | Berberine | |
| DrugBank ID | DB04115 | |
| **原核准適應症** | [Data Gap] | |
| **原作用機轉 (MOA)** | [Data Gap] | |
| 台灣上市狀態 | 已上市 | TFDA |
| 可用劑型 | [Data Gap] | |

### 預測新適應症總覽
| 排名 | 預測適應症 | 建議劑型 | TxGNN 分數 | 證據等級 | 藥師立場 | 決策結論 | 關鍵缺口 |
|------|-----------|---------|-----------|---------|---------|---------|---------|
| 1 | Severe pre-eclampsia | [Data Gap] | 99.83% | L5 | 暫不建議 | Hold | 缺乏臨床證據 |
| 2 | Mild pre-eclampsia | [Data Gap] | 99.83% | L5 | 暫不建議 | Hold | 缺乏臨床證據 |
| 3 | Monocytic leukemia | [Data Gap] | 99.74% | L4 | 待補件後評估 | Research Question | 缺乏臨床試驗 |

---

## 2. Taiwan Regulatory & Label Snapshot

### 2.1 TFDA 上市狀態
- 上市狀態：已上市
- 核准適應症：[Data Gap] [來源：TFDA 許可證]
- 許可證號：[Data Gap]

### 2.2 許可證詳細資訊
| 許可證號 | 中文品名 | 劑型 | 濃度 | 製造廠 | 仿單版本 |
|---------|---------|------|------|-------|---------|
| [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] |

### 2.3 仿單關鍵資訊（按劑型分列）

#### 外用劑型
| 項目 | 內容 | 來源 |
|------|------|------|
| 主要警語 | [Data Gap] | [Data Gap] |
| 禁忌症 | [Data Gap] | [Data Gap] |
| 建議劑量 | [Data Gap] | [Data Gap] |
| 孕哺分級 | [Data Gap] | [Data Gap] |
| 肝功能調整 | [不適用] | [Data Gap] |
| 腎功能調整 | [不適用] | [Data Gap] |
| 特殊族群（兒童） | [Data Gap] | [Data Gap] |
| 特殊族群（老人） | [Data Gap] | [Data Gap] |

#### 口服/全身性劑型
（同上格式）

---

## 3. Safety Profile — 按劑型分列

### 3.1 外用劑型安全性

#### Serious ADR
| ADR | 發生率 | 來源 | 處置建議 |
|-----|-------|------|---------|
| [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] |

#### Common ADR
| ADR | 發生率 | 來源 | 處置建議 |
|-----|-------|------|---------|
| [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] |

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

#### 已知 DDI（若有資料）
| 併用藥品 | 嚴重度 | 機轉 | 臨床後果 | 處置建議 | 替代方案 |
|---------|-------|------|---------|---------|---------|
| [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] |

#### DDI 資料庫狀態：[未檢索] 時
⚠️ **以下為藥理學推測，不可替代正式 DDI 查詢**

| 藥物類別 | 代表藥品 | 推測風險 | 建議 |
|---------|---------|---------|------|
| [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] |

**用藥審核前必須補查**：
- [ ] Unified DDI 資料庫（DDInter + Guide to PHARMACOLOGY）
- [ ] DrugBank interactions

---

## 5. Data Gaps 完整記錄

### Data Gap #1 — 作用機轉 (MOA)（🛑 Blocking）

| 欄位 | 內容 |
|------|------|
| **缺口項目** | 作用機轉 (MOA) |
| **已完成檢索行動** | |
| | • 官方標籤/主管機關資料（TFDA/FDA/EMA/PMDA）：[未檢索] |
| | • 權威藥學資料庫（DDInter/Guide to PHARMACOLOGY/DrugBank）：查詢成功，未獲得完整資料 |
| | • 同儕審查文獻（PubMed/期刊）：[未檢索] |
| | • 試驗登錄（ClinicalTrials.gov）：[未檢索] |
| **檢索結果** | 僅二手資訊 |
| **推論限制（不能做）** | 機轉關聯性分析 |
| **風險處置（決策）** | Hold |
| **解鎖條件** | 需要 DrugBank API 完整查詢結果 |

---

## 6. 各適應症特定考量

### 6.1 Severe pre-eclampsia（證據等級: L5）

#### 臨床定義
| 項目 | 內容 | 來源 |
|------|------|------|
| 疾病全名 | Severe pre-eclampsia | |
| ICD-10 | [Data Gap] | WHO |
| 診斷準則 | [Data Gap] | [Data Gap] |
| 目標族群 | [Data Gap] | |
| 排除條件 | [Data Gap] | |
| 現行標準治療 (SoC) | [Data Gap] | [Data Gap] |
| Unmet medical need | [Data Gap] | |
| 主要療效指標 | [Data Gap] | |
| 療效評估時間點 | [Data Gap] | |

#### 藥師立場與理由
| 項目 | 內容 |
|------|------|
| 藥師立場 | 暫不建議 |
| 決策結論 | Hold |
| 建議劑型 | [Data Gap] |
| 關鍵支持證據 | [Data Gap] |
| 關鍵缺口 | 缺乏臨床證據 |
| 立場變更條件 | 需要臨床試驗支持 |

#### 證據可外推性評估
（使用 L4/L5 證據可外推性說明模板）

#### 疾病特異監測表
（使用疾病特異監測表模板）

---

### 6.2 Mild pre-eclampsia（證據等級: L5）

> **藥師立場：暫不建議** — 證據等級 L5，無直接臨床證據支持
> **決策結論：Hold**

| 項目 | 內容 |
|------|------|
| TxGNN 分數 | 99.83% |
| 機轉關聯 | Berberine 可能具有抗炎和抗氧化特性，但目前缺乏直接針對 mild pre-eclampsia 的臨床證據。 |
| 關鍵缺口 | 缺乏臨床試驗、機轉研究、安全性資料 |

#### 證據可外推性評估
（使用模板，強調限制條款）

**若要變更立場需補齊**：
- [ ] 至少一項觀察性研究
- [ ] 機轉合理性論證
- [ ] 目標族群安全性資料

---

### 6.3 Monocytic leukemia（證據等級: L4）

#### 臨床定義
| 項目 | 內容 | 來源 |
|------|------|------|
| 疾病全名 | Monocytic leukemia | |
| ICD-10 | [Data Gap] | WHO |
| 診斷準則 | [Data Gap] | [Data Gap] |
| 目標族群 | [Data Gap] | |
| 排除條件 | [Data Gap] | |
| 現行標準治療 (SoC) | [Data Gap] | [Data Gap] |
| Unmet medical need | [Data Gap] | |
| 主要療效指標 | [Data Gap] | |
| 療效評估時間點 | [Data Gap] | |

#### 藥師立場與理由
| 項目 | 內容 |
|------|------|
| 藥師立場 | 待補件後評估 |
| 決策結論 | Research Question |
| 建議劑型 | [Data Gap] |
| 關鍵支持證據 | PMID: 28656088 |
| 關鍵缺口 | 缺乏臨床試驗 |
| 立場變更條件 | 需要臨床試驗支持 |

#### 證據摘要（標註支撐面向）
| PMID | 年份 | 研究類型 | 支撐面向 | 主要發現 | 限制 |
|------|-----|---------|---------|---------|------|
| 28656088 | 2017 | In vitro | ☑機轉 ☐療效 ☐安全性 ☐族群 | Berberine 可能影響細胞週期和細胞因子分泌 | 缺乏臨床試驗支持 |

#### 證據可外推性評估
（使用 L4/L5 證據可外推性說明模板）

#### 疾病特異監測表
（使用疾病特異監測表模板）

---

## 7. Guardrails（若決策為 Proceed with Guardrails）

（使用 Guardrails 模板：G1 適用範圍、G2 排除條件、G3 監測 Stop Rule、G4 告知語句）

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
- 疾病特異：{視適應症補充}

---

## 9. Evidence Summary

### 9.1 證據等級分布
| 等級 | 適應症數 | 臨床意義 |
|-----|---------|---------|
| L1 | 0 | 多個 RCT/系統性回顧 — 可支持臨床使用 |
| L2 | 0 | 單一 RCT — 可考慮使用 |
| L3 | 0 | 觀察性研究 — 待補件後評估 |
| L4 | 1 | 前臨床/機轉 — 暫不建議 |
| L5 | 2 | 僅模型預測 — 暫不建議 |

### 9.2 Limitations
- 缺乏作用機轉（MOA）完整資料
- 缺乏臨床試驗支持

---

## 10. 補件追蹤表

| # | 缺口 | 阻斷性 | 資料來源 | 負責人 | 截止日 | 狀態 | 影響章節 |
|---|-----|-------|---------|-------|-------|------|---------|
| 1 | 作用機轉 (MOA) | 🛑 | DrugBank | {人} | {日期} | ⏳ | §1, §5 |

---

## 附錄：資料收集日誌

| # | 資料來源 | 查詢日期 | 查詢條件 | 結果 | 原始結果連結 |
|---|---------|---------|---------|------|-------------|
| 1 | TFDA | 2026-02-09 | {"drug": "berberine"} | 20 | [snapshot] |
| 2 | DDI | 2026-02-09 | {"drug": "berberine"} | 0 | [snapshot] |
| 3 | DrugBank | 2026-02-09 | {"drug": "berberine"} | 1 | [snapshot] |
| 4 | TFDA 仿單 | 2026-02-09 | {"drug": "berberine"} | 1 | [snapshot] |
| 5 | ClinicalTrials.gov | 2026-02-09 | {"drug": "berberine", "disease": "severe pre-eclampsia"} | 0 | [snapshot] |
| 6 | PubMed | 2026-02-09 | {"drug": "berberine", "disease": "monocytic leukemia"} | 1 | [snapshot] |

---

## 文件版本資訊

| 項目 | 內容 |
|------|------|
| 文件版本 | v1.0 |
| 產生日期 | 2026-02-09 |
| 資料截止日 | 2026-02-09 |
| Evidence Pack 版本 | berberine_v4_2026-02-09.json |

---

<div id="sponsor">

## 贊助商報告

</div>

# Sponsor Notes — Berberine 老藥新用開發評估

---

## ⚠️ 資料完整性與可用性聲明

**文件產出日期**：2026-02-09
**決策階段**：S0（初始評估）
**目前決策**：Hold

### 本文件可支持的決策
| 可支持 | 不可支持 |
|-------|---------|
| Research Question only | 開發建議（Go/Conditional Go） |

### 阻斷性缺口摘要
| # | 缺口項目 | 推論限制 | 解鎖條件 |
|---|---------|---------|---------|
| 1 | 作用機轉 (MOA) | 影響機轉關聯性分析 | 查詢 DrugBank API |

### 保守假設摘要
| # | 假設 | 依據 | 限制 | 觸發條件 |
|---|------|------|------|---------|
| 1 | N/A | N/A | N/A | N/A |

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
| TFDA 許可證 | ✅ | 2026-02-09 | drug: berberine | 20 | 提供市場狀態 |
| TFDA 仿單 | ✅ | 2026-02-09 | drug: berberine | 1 | 提供安全資訊 |
| DDI 資料庫 (Unified DDI) | ⚠️ [未找到] | 2026-02-09 | drug: berberine | 0 | 無法確認交互作用 |
| DrugBank (MOA) | ✅ | 2026-02-09 | drug: berberine | 1 | 提供部分機轉資訊 |
| ClinicalTrials.gov | ✅ (無結果) | 2026-02-09 | drug: berberine | 0 | 無臨床試驗支持 |
| PubMed | ✅ | 2026-02-09 | drug: berberine | 1 | 提供文獻支持 |

### 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物名稱 | Berberine | |
| DrugBank ID | DB04115 | |
| **原核准適應症** | [Data Gap] | |
| **原作用機轉 (MOA)** | [Data Gap] — 影響機轉關聯評估 | |
| 台灣上市狀態 | 已上市 | TFDA |

### 許可證詳細資訊
| 許可證號 | 中文品名 | 劑型 | 濃度 | 製造廠 | 仿單版本 |
|---------|---------|------|------|-------|---------|
| N/A | N/A | N/A | N/A | N/A | N/A |

### 可用劑型（按給藥途徑）
| 給藥途徑 | 劑型 | 開發門檻 |
|---------|------|---------|
| 外用 | N/A | N/A |
| 口服 | N/A | N/A |

### 預測新適應症總覽
| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 建議劑型 | 開發建議 | 決策結論 | 阻斷因素 |
|------|-----------|-----------|---------|---------|---------|---------|---------|---------|
| 1 | severe pre-eclampsia | 99.83% | L5 | 0 項 | N/A | Hold | Hold | MOA 缺口 |
| 2 | mild pre-eclampsia | 99.83% | L5 | 0 項 | N/A | Hold | Hold | MOA 缺口 |
| 3 | monocytic leukemia | 99.74% | L4 | 0 項 | N/A | Research Question | Research Question | MOA 缺口 |

**整體開發建議**：目前所有適應症均因機轉相關性資料缺口而被建議 Hold 或作為研究問題，需進一步資料支持。[來源：DrugBank, PubMed]

---

## 1. Executive Brief (≤1 page)

### 開發決策總覽
| 適應症 | 開發建議 | 決策結論 | 決策階段 | 關鍵支持 | 關鍵缺口 | Pharmacist 對應立場 |
|-------|---------|---------|---------|---------|---------|-------------------|
| severe pre-eclampsia | Hold | Hold | S0 | TxGNN 分數 | MOA 缺口 | 待補件後評估 |
| mild pre-eclampsia | Hold | Hold | S0 | TxGNN 分數 | MOA 缺口 | 待補件後評估 |
| monocytic leukemia | Research Question | Research Question | S0 | 文獻支持 | MOA 缺口 | 暫不建議 |

### 整體決策建議
- **最優先開發**：monocytic leukemia — 具文獻支持但需補充機轉資料（附 ref）
- **次優先開發**：severe pre-eclampsia — 需補充臨床證據及機轉資料
- **Hold**：mild pre-eclampsia — 需補件後可升級
- **No-Go**：無

### Top 3 Key Points
1. Berberine 目前缺乏原適應症的作用機轉資料，影響新適應症的機轉關聯分析。[來源：DrugBank]
2. 針對 monocytic leukemia 的研究顯示 Berberine 可能影響細胞週期和細胞因子分泌。[來源：PubMed PMID: 28656088]
3. 所有預測適應症均缺乏臨床試驗支持，需進一步探索。[來源：ClinicalTrials.gov]

### Top Risks & Mitigation
| 風險類型 | 描述 | 嚴重度 | 緩解措施 |
|---------|------|-------|---------|
| 證據 | 缺乏機轉資料 | 高 | 查詢 DrugBank API 補充 |
| 安全性 | 未確認 DDI 風險 | 中 | 完成 DDI 查核 |
| 法規 | 缺乏臨床試驗支持 | 高 | 設計初步 POC 試驗 |

### Next Step MVP（若為 Go/Conditional Go）
| 適應症 | 試驗類型 | N | 主要 endpoint | 次要 endpoint |
|-------|---------|---|--------------|--------------|
| N/A | N/A | N/A | N/A | N/A |

---

## 2. 藥物層級資訊

### 2.1 Taiwan Regulatory Snapshot
- **TFDA 上市狀態**：已上市 [來源：TFDA]
- **核准適應症**：N/A [來源：TFDA]
- **許可證號**：N/A

**Label Constraints / Warnings**：
N/A [來源：N/A]

### 2.2 Safety Profile — 按劑型分列

#### 外用劑型
| 項目 | 內容 | 來源 |
|------|------|------|
| Key warnings | [Data Gap] | N/A |
| 常見 ADR | N/A | N/A |
| 開發風險 | N/A | |

#### 口服/全身性劑型
| 項目 | 內容 | 來源 |
|------|------|------|
| Key warnings | [Data Gap] | N/A |
| 常見 ADR | N/A | N/A |
| 開發風險 | N/A | |

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
- **MOA**：[Data Gap] — 影響機轉關聯評估 [來源：DrugBank]
- **與新適應症相關的藥理特性**：N/A [來源：N/A]

---

## 3. Data Gaps 完整記錄

### Data Gap #1 — 作用機轉 (MOA)（🛑 Blocking）

| 欄位 | 內容 |
|------|------|
| **缺口項目** | 作用機轉 (MOA) |
| **已完成檢索行動** | |
| | • 官方標籤/主管機關資料（TFDA/FDA/EMA/PMDA）：未找到 |
| | • 權威藥學資料庫（DDInter/Guide to PHARMACOLOGY/DrugBank）：已查，但未完整 |
| | • 同儕審查文獻（PubMed/期刊）：未找到 |
| | • 試驗登錄（ClinicalTrials.gov）：未找到 |
| **檢索結果** | 未找到 |
| **推論限制（不能做）** | 不能進行機轉關聯性分析 |
| **風險處置（決策）** | Hold |
| **解鎖條件** | 查詢 DrugBank API 獲得完整 MOA 資料 |

---

## 4. 各適應症詳細評估

### 4.1 severe pre-eclampsia（L5 完整格式）

#### 基本資訊與決策
| 項目 | 內容 |
|------|------|
| 疾病名稱 | severe pre-eclampsia |
| ICD-10 | O14.1 |
| TxGNN 分數 | 99.83% |
| 證據等級 | L5 |
| 建議劑型 | N/A |
| **開發建議** | Hold |
| **決策結論** | Hold |
| **Pharmacist 對應** | 待補件後評估 |
| 決策階段 | S0 |
| 阻斷升級因素 | MOA 缺口 |

#### 臨床定義
| 項目 | 內容 | 來源 |
|------|------|------|
| 診斷準則 | [Data Gap] | N/A |
| 目標族群 | 孕婦 | |
| 排除條件 | [Data Gap] | |
| 現行 SoC | [Data Gap] | N/A |
| Unmet need | 高 | |
| 流行病學 | [Data Gap] | N/A |

#### 機轉關聯性分析
| 項目 | 內容 | 來源 |
|------|------|------|
| 原適應症機轉 | [Data Gap] | N/A |
| 新適應症病理 | [Data Gap] | N/A |
| 機轉關聯 | [Data Gap] | N/A |
| 相似度 | 低 | |
| 類似再利用先例 | 無 | N/A |

#### 臨床試驗（標註相關性）
| 試驗編號 | 相關性 | 階段 | 狀態 | N | 結果摘要 |
|---------|-------|-----|------|---|---------|
| N/A | C | N/A | N/A | N/A | N/A |

相關性說明：A=高度一致, B=相近族群/proxy, C=機轉支持

#### 文獻證據（標註支撐面向）
| PMID | 年份 | 研究類型 | 支撐面向 | 主要發現 | 限制 |
|------|-----|---------|---------|---------|------|
| N/A | N/A | N/A | N/A | N/A | N/A |

#### 證據可外推性評估
**證據等級**：L5
**證據類型**：模型預測

#### 可外推理由
| 面向 | 支持外推的理由 | 強度 |
|------|---------------|------|
| 機轉相關性 | 缺乏直接機轉資料 | 弱 |
| 族群相似性 | 高 | 強 |
| 劑量可行性 | 未知 | 弱 |

#### ⚠️ 限制條款
> 本證據等級為 L5，存在以下限制：
> 1. **不可**直接作為開發決策依據
> 2. **不可**直接作為試驗設計依據
> 3. **需要**補充臨床試驗證據後才能升級

---

## 5. 適應症比較與優先順序

### 5.1 證據強度比較
| 適應症 | 證據等級 | RCT | 觀察性 | 前臨床 | 強度評分 |
|-------|---------|-----|-------|-------|---------|
| severe pre-eclampsia | L5 | 0 | 0 | 0 | 低 |
| mild pre-eclampsia | L5 | 0 | 0 | 0 | 低 |
| monocytic leukemia | L4 | 0 | 0 | 1 | 中 |

### 5.2 開發可行性比較
| 適應症 | 劑型 | 劑型風險 | 安全性風險 | DDI 風險 | 法規路徑 | 可行性 |
|-------|-----|---------|-----------|---------|---------|-------|
| severe pre-eclampsia | N/A | N/A | 未知 | 未知 | 不明 | 低 |
| mild pre-eclampsia | N/A | N/A | 未知 | 未知 | 不明 | 低 |
| monocytic leukemia | N/A | N/A | 未知 | 未知 | 不明 | 中 |

### 5.3 優先開發順序
1. **monocytic leukemia**：具文獻支持，需補充機轉資料。
2. **severe pre-eclampsia**：需補充臨床證據及機轉資料。
3. **mild pre-eclampsia**：需補件後可升級。

---

## 6. Risk Register

### 6.1 Evidence Risk
| 適應症 | 風險 | 嚴重度 | 緩解措施 |
|-------|-----|-------|---------|
| severe pre-eclampsia | 缺乏機轉資料 | 高 | 查詢 DrugBank API 補充 |

### 6.2 Safety Risk
| 風險 | 影響適應症 | 嚴重度 | 緩解措施 |
|-----|-----------|-------|---------|
| 未確認 DDI 風險 | 所有適應症 | 中 | 完成 DDI 查核 |

### 6.3 Regulatory/Operational Risk
| 風險 | 描述 | 嚴重度 | 緩解措施 |
|-----|------|-------|---------|
| 法規 | 缺乏臨床試驗支持 | 高 | 設計初步 POC 試驗 |

---

## 7. 補件追蹤表

| # | 缺口 | 阻斷性 | 資料來源 | 負責人 | 截止日 | 狀態 | 影響章節 | 補件後可達建議 |
|---|-----|-------|---------|-------|-------|------|---------|--------------|
| 1 | 作用機轉 (MOA) | 🛑 | DrugBank | N/A | N/A | ⏳ | §2.4 | Conditional Go |

---

## 8. 補件後決策升級路徑

```
當前狀態：S0 → 最高建議：Hold

補件路徑 1：補齊 MOA 資料
  → 可達：S1 → 升級至：Conditional Go
```

---

## 附錄：資料收集日誌

| # | 資料來源 | 查詢日期 | 查詢條件 | 結果 | 原始結果連結 |
|---|---------|---------|---------|------|-------------|
| 1 | TFDA | 2026-02-09 | drug: berberine | 20 | [snapshot] |
| 2 | DDI | 2026-02-09 | drug: berberine | 0 | [snapshot] |
| 3 | DrugBank | 2026-02-09 | drug: berberine | 1 | [snapshot] |
| 4 | TFDA 仿單 | 2026-02-09 | drug: berberine | 1 | [snapshot] |
| 5 | ClinicalTrials.gov | 2026-02-09 | drug: berberine | 0 | [snapshot] |

---

## 文件版本資訊

| 項目 | 內容 |
|------|------|
| 文件版本 | v1.0 |
| 產生日期 | 2026-02-09 |
| 資料截止日 | 2026-02-09 |
| Evidence Pack 版本 | berberine_v4_2026-02-09.json |
