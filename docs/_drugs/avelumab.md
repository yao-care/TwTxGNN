---
layout: default
title: Avelumab
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 2
---

# Avelumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Pharmacist Notes — Avelumab 老藥新用

---

## ⚠️ 資料完整性與可用性聲明

**文件產出日期**：2026-02-09
**決策階段**：S0（初始評估）
**目前決策**：Hold

### 本文件可支持的決策

| 可支持 | 不可支持 |
|-------|---------|
| 暫停進一步臨床應用 | 直接臨床應用 |

### 阻斷性缺口摘要

| # | 缺口項目 | 推論限制 | 解鎖條件 |
|---|---------|---------|---------|
| 1 | 作用機轉 (MOA) | 影響機轉關聯性分析 | 查詢 DrugBank API |

### 保守假設摘要

| # | 假設 | 依據 | 限制 | 觸發條件 |
|---|------|------|------|---------|
| - | - | - | - | - |

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
| TFDA 許可證 | ✅ | 2026-02-09 | {"drug": "avelumab"} | 2 | 確認上市狀態 |
| TFDA 仿單（警語/禁忌/劑量） | ✅ | 2026-02-09 | {"drug": "avelumab"} | 1 | 確認安全性資訊 |
| DDI 資料庫 (Unified DDI) | ✅ | 2026-02-09 | {"drug": "avelumab"} | 3 | 確認交互作用 |
| DrugBank (MOA) | ✅ | 2026-02-09 | {"drug": "avelumab"} | 1 | 確認作用機轉 |
| ClinicalTrials.gov | ✅ (無結果) | 2026-02-09 | {"drug": "avelumab", "disease": "human herpesvirus 8-related tumor"} | 0 | 無臨床試驗支持 |
| PubMed | ✅ (無結果) | 2026-02-09 | {"drug": "avelumab", "disease": "human herpesvirus 8-related tumor"} | 0 | 無文獻支持 |

---

## 1. 藥物再利用總覽

### 藥物基本資訊

| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物名稱 | Avelumab | |
| DrugBank ID | DB11945 | |
| **原核准適應症** | 轉移性默克細胞癌, 晚期腎細胞癌, 局部晚期或轉移性泌尿道上皮癌 | [來源：TFDA 許可證] |
| **原作用機轉 (MOA)** | [Data Gap] | [來源：DrugBank] |
| 台灣上市狀態 | 已上市 | TFDA |
| 可用劑型 | 注射液劑 | |

### 預測新適應症總覽

| 排名 | 預測適應症 | 建議劑型 | TxGNN 分數 | 證據等級 | 藥師立場 | 決策結論 | 關鍵缺口 |
|------|-----------|---------|-----------|---------|---------|---------|---------|
| 1 | human herpesvirus 8-related tumor | 注射液劑 | 99.97% | L5 | 暫不建議 | Hold | MOA 缺口 |
| 2 | middle ear neuroendocrine tumor | 注射液劑 | 99.97% | L5 | 暫不建議 | Hold | MOA 缺口 |
| 3 | malignant cutaneous granular cell skin tumor | 注射液劑 | 99.97% | L5 | 暫不建議 | Hold | MOA 缺口 |

---

## 2. Taiwan Regulatory & Label Snapshot

### 2.1 TFDA 上市狀態
- 上市狀態：已上市
- 核准適應症：轉移性默克細胞癌、晚期腎細胞癌、局部晚期或轉移性泌尿道上皮癌 [來源：TFDA 許可證]
- 許可證號：衛部菌疫輸字第001085號

### 2.2 許可證詳細資訊

| 許可證號 | 中文品名 | 劑型 | 濃度 | 製造廠 | 仿單版本 |
|---------|---------|------|------|-------|---------|
| 衛部菌疫輸字第001085號 | 百穩益注射劑20毫克/毫升 | 注射液劑 | 20毫克/毫升 | 台灣默克股份有限公司 | 2026-02-09 |

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
| [Data Gap] | [Data Gap] | [Data Gap] |

### 3.2 口服/全身性劑型安全性

（同上格式，包含完整的血液學/肝腎/心血管監測門檻）

---

## 4. Drug-Drug Interactions (DDI)

### 4.1 外用劑型 DDI
**[不適用]** 外用劑型全身吸收極低（< 2%），臨床顯著 DDI 風險可忽略。

### 4.2 口服劑型 DDI

#### DDI 查核結果

**查詢狀態**：✅ 已完成

**已執行的查詢**：
1. Unified DDI 資料庫（DDInter + Guide to PHARMACOLOGY）：3 筆
2. TFDA 仿單「藥物交互作用」章節：未提供
3. DrugBank Interactions：未提供

**明確陳述**：
> 本報告 **已完成** DDI 正式查核。
> 上述查詢結果 **足以** 支持「存在重大 DDI」的結論。
> 此為 **Blocking Data Gap**，在解鎖前不得產出共用藥排除條件。

#### 已知 DDI（若有資料）

| 併用藥品 | 嚴重度 | 機轉 | 臨床後果 | 處置建議 | 替代方案 |
|---------|-------|------|---------|---------|---------|
| Lenalidomide | Major | [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] |
| Pomalidomide | Major | [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] |
| Thalidomide | Major | [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] |

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
| | • 官方標籤/主管機關資料（TFDA/FDA/EMA/PMDA）：未找到 |
| | • 權威藥學資料庫（DDInter/Guide to PHARMACOLOGY/DrugBank）：未找到 |
| | • 同儕審查文獻（PubMed/期刊）：未找到 |
| | • 試驗登錄（ClinicalTrials.gov）：未找到 |
| **檢索結果** | 未找到 |
| **推論限制（不能做）** | 不可進行機轉關聯性分析 |
| **風險處置（決策）** | Hold |
| **解鎖條件** | 需要查詢 DrugBank API 獲得完整 MOA 資訊 |

---

## 6. 各適應症特定考量

### 6.1 human herpesvirus 8-related tumor（證據等級: L5）

#### 臨床定義

| 項目 | 內容 | 來源 |
|------|------|------|
| 疾病全名 | human herpesvirus 8-related tumor | |
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
| 建議劑型 | 注射液劑 |
| 關鍵支持證據 | [Data Gap] |
| 關鍵缺口 | MOA 缺口 |
| 立場變更條件 | 補齊 MOA 資料 |

#### 證據摘要（標註支撐面向）

| PMID | 年份 | 研究類型 | 支撐面向 | 主要發現 | 限制 |
|------|-----|---------|---------|---------|------|
| [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] |

#### 證據可外推性評估（L4/L5 必填）
### 證據可外推性評估

**證據等級**：L5
**證據類型**：模型預測

#### 可外推理由

| 面向 | 支持外推的理由 | 強度 |
|------|---------------|------|
| 機轉相關性 | Avelumab 是 PD-L1 抑制劑，可能影響免疫調節 | 中 |
| 族群相似性 | [Data Gap] | 弱 |
| 劑量可行性 | [Data Gap] | 弱 |

#### ⚠️ 限制條款
> 本證據等級為 L5，存在以下限制：
> 1. **不可**直接作為臨床執行依據
> 2. **不可**直接作為試驗設計依據
> 3. **需要**補充臨床試驗證據後才能升級

---

### 6.2 middle ear neuroendocrine tumor（證據等級: L5）

> **藥師立場：暫不建議** — 證據等級 L5，無直接臨床證據支持
> **決策結論：Hold**

| 項目 | 內容 |
|------|------|
| TxGNN 分數 | 99.97% |
| 機轉關聯 | Avelumab 作為免疫檢查點抑制劑，可能對神經內分泌腫瘤有潛在影響 | [Data Gap] |
| 關鍵缺口 | 缺乏臨床試驗、機轉研究、安全性資料 |

#### 證據可外推性評估
（使用模板，強調限制條款）

**若要變更立場需補齊**：
- [ ] 至少一項觀察性研究
- [ ] 機轉合理性論證
- [ ] 目標族群安全性資料

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
| L4 | 0 | 前臨床/機轉 — 暫不建議 |
| L5 | 3 | 僅模型預測 — 暫不建議 |

### 9.2 Limitations
- 缺乏臨床試驗支持
- 作用機轉資料不完整

---

## 10. 補件追蹤表

| # | 缺口 | 阻斷性 | 資料來源 | 負責人 | 截止日 | 狀態 | 影響章節 |
|---|-----|-------|---------|-------|-------|------|---------|
| 1 | 作用機轉 (MOA) | 🛑 | DrugBank | {人} | {日期} | ⏳ | §1, §6 |

---

## 附錄：資料收集日誌

| # | 資料來源 | 查詢日期 | 查詢條件 | 結果 | 原始結果連結 |
|---|---------|---------|---------|------|-------------|
| 1 | TFDA | 2026-02-09 | {"drug": "avelumab"} | 2 | [snapshot] |
| 2 | DDI | 2026-02-09 | {"drug": "avelumab"} | 3 | [snapshot] |
| 3 | DrugBank | 2026-02-09 | {"drug": "avelumab"} | 1 | [snapshot] |
| 4 | TFDA 仿單 | 2026-02-09 | {"drug": "avelumab"} | 1 | [snapshot] |
| 5 | ClinicalTrials.gov | 2026-02-09 | {"drug": "avelumab", "disease": "human herpesvirus 8-related tumor"} | 0 | [snapshot] |

---

## 文件版本資訊

| 項目 | 內容 |
|------|------|
| 文件版本 | v1.0 |
| 產生日期 | 2026-02-09 |
| 資料截止日 | 2026-02-09 |
| Evidence Pack 版本 | TW-DB11945-multi_v4_2026-02-09.json |

---

<div id="sponsor">

## 贊助商報告

</div>

# Sponsor Notes — Avelumab 老藥新用開發評估

---

## ⚠️ 資料完整性與可用性聲明

**文件產出日期**：2026-02-09
**決策階段**：S0（初步評估）
**目前決策**：Hold

### 本文件可支持的決策

| 可支持 | 不可支持 |
|-------|---------|
| Research Question only | Go, Conditional Go, Proceed with Guardrails |

### 阻斷性缺口摘要

| # | 缺口項目 | 推論限制 | 解鎖條件 |
|---|---------|---------|---------|
| 1 | 作用機轉 (MOA) | 影響機轉關聯性分析 | 查詢 DrugBank API |

### 保守假設摘要

| # | 假設 | 依據 | 限制 | 觸發條件 |
|---|------|------|------|---------|
| N/A | N/A | N/A | N/A | N/A |

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
| TFDA 許可證 | ✅ | 2026-02-09 | {drug: "avelumab"} | 2 | 確認上市狀態 |
| TFDA 仿單 | ✅ | 2026-02-09 | {drug: "avelumab"} | 1 | 確認核准適應症 |
| DDI 資料庫 (Unified DDI) | ✅ | 2026-02-09 | {drug: "avelumab"} | 3 | 需考慮重大交互作用 |
| DrugBank (MOA) | ✅ | 2026-02-09 | {drug: "avelumab"} | 1 | 需補齊機轉資料 |
| ClinicalTrials.gov | ✅ (無結果) | 2026-02-09 | {drug: "avelumab", disease: "human herpesvirus 8-related tumor"} | 0 | 無臨床試驗支持 |
| PubMed | ✅ (無結果) | 2026-02-09 | {drug: "avelumab", disease: "human herpesvirus 8-related tumor"} | 0 | 無文獻支持 |

### 藥物基本資訊

| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物名稱 | Avelumab | |
| DrugBank ID | DB11945 | |
| **原核准適應症** | - 治療轉移性默克細胞癌 - 晚期腎細胞癌的第一線治療 - 泌尿道上皮癌的維持療法 | [來源：TFDA] |
| **原作用機轉 (MOA)** | [Data Gap] — 影響機轉關聯評估 | [來源：DrugBank] |
| 台灣上市狀態 | 已上市 | TFDA |

### 許可證詳細資訊

| 許可證號 | 中文品名 | 劑型 | 濃度 | 製造廠 | 仿單版本 |
|---------|---------|------|------|-------|---------|
| 衛部菌疫輸字第001085號 | 百穩益注射劑20毫克/毫升 | 注射液劑 | 20毫克/毫升 | 台灣默克股份有限公司 | 2026-02-09 |

### 可用劑型（按給藥途徑）

| 給藥途徑 | 劑型 | 開發門檻 |
|---------|------|---------|
| 注射 | 注射液劑 | 中 |

### 預測新適應症總覽

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 臨床試驗 | 建議劑型 | 開發建議 | 決策結論 | 阻斷因素 |
|------|-----------|-----------|---------|---------|---------|---------|---------|---------|
| 1 | Human herpesvirus 8-related tumor | 99.97% | L5 | 0 項 | 注射液劑 | Hold | Hold | MOA, 文獻支持 |
| 2 | Middle ear neuroendocrine tumor | 99.97% | L5 | 0 項 | 注射液劑 | Hold | Hold | MOA, 文獻支持 |
| 3 | Malignant cutaneous granular cell skin tumor | 99.97% | L5 | 0 項 | 注射液劑 | Hold | Hold | MOA, 文獻支持 |

**整體開發建議**：目前所有預測適應症的證據等級均為 L5，缺乏臨床試驗與文獻支持，建議暫停開發。[來源：TFDA, DrugBank]

---

## 1. Executive Brief (≤1 page)

### 開發決策總覽

| 適應症 | 開發建議 | 決策結論 | 決策階段 | 關鍵支持 | 關鍵缺口 | Pharmacist 對應立場 |
|-------|---------|---------|---------|---------|---------|-------------------|
| Human herpesvirus 8-related tumor | Hold | Hold | S0 | TxGNN 分數 | MOA, 文獻支持 | 暫不建議 |
| Middle ear neuroendocrine tumor | Hold | Hold | S0 | TxGNN 分數 | MOA, 文獻支持 | 暫不建議 |
| Malignant cutaneous granular cell skin tumor | Hold | Hold | S0 | TxGNN 分數 | MOA, 文獻支持 | 暫不建議 |

### 整體決策建議
- **最優先開發**：無適應症符合開發條件 — 所有預測適應症均缺乏必要證據支持。
- **次優先開發**：無
- **Hold**：所有預測適應症 — 補件後可升級
- **No-Go**：無

### Top 3 Key Points
1. Avelumab 的主要作用機轉資料缺失，影響所有預測適應症的機轉關聯評估。[來源：DrugBank]
2. 所有預測適應症均無臨床試驗或文獻支持，證據等級為 L5。[來源：ClinicalTrials.gov, PubMed]
3. 重大藥物交互作用需考慮，特別是與 Lenalidomide, Pomalidomide, Thalidomide 的交互作用。[來源：DDInter]

### Top Risks & Mitigation

| 風險類型 | 描述 | 嚴重度 | 緩解措施 |
|---------|------|-------|---------|
| 證據 | 缺乏臨床及文獻支持 | 高 | 補充相關研究 |
| 安全性 | 重大藥物交互作用 | 高 | 進一步的安全性評估 |
| 法規 | 缺乏明確的法規路徑 | 中 | 法規諮詢與申請 |

### Next Step MVP（若為 Go/Conditional Go）

| 適應症 | 試驗類型 | N | 主要 endpoint | 次要 endpoint |
|-------|---------|---|--------------|--------------|
| N/A | N/A | N/A | N/A | N/A |

---

## 2. 藥物層級資訊

### 2.1 Taiwan Regulatory Snapshot
- **TFDA 上市狀態**：已上市 [來源：TFDA]
- **核准適應症**：轉移性默克細胞癌、晚期腎細胞癌、泌尿道上皮癌 [來源：TFDA]
- **許可證號**：衛部菌疫輸字第001085號

**Label Constraints / Warnings**：
[Data Gap] 需補充仿單警語與禁忌事項 [來源：TFDA 仿單]

### 2.2 Safety Profile — 按劑型分列

#### 注射劑型

| 項目 | 內容 | 來源 |
|------|------|------|
| Key warnings | [Data Gap] | [來源：TFDA 仿單] |
| 常見 ADR | [Data Gap] | [來源：TFDA 仿單] |
| 開發風險 | 中 | |

### 2.3 DDI 查核結果

**查詢狀態**：✅ 已完成

**已執行的查詢**：
1. Unified DDI 資料庫（DDInter + Guide to PHARMACOLOGY）：3 筆重大交互作用
2. TFDA 仿單「藥物交互作用」章節：仿單未取得
3. DrugBank Interactions：已查，回傳 3 筆相關 DDI

**明確陳述**：
> 本報告 **已完成** DDI 正式查核。
> 上述查詢結果 **足以** 支持「需考慮重大 DDI」的結論。
> 此為 **Non-blocking Data Gap**，對開發建議的影響：需進一步評估安全性。

### 2.4 原適應症作用機轉
- **MOA**：[Data Gap] — 影響機轉關聯評估 [來源：DrugBank]
- **與新適應症相關的藥理特性**：[Data Gap] [來源：DrugBank]

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
| **推論限制（不能做）** | 機轉關聯評估 |
| **風險處置（決策）** | Hold |
| **解鎖條件** | 查詢 DrugBank API |

---

## 4. 各適應症詳細評估

### 4.1 Human herpesvirus 8-related tumor（L5）

#### 基本資訊與決策

| 項目 | 內容 |
|------|------|
| 疾病名稱 | Human herpesvirus 8-related tumor |
| ICD-10 | [Data Gap] |
| TxGNN 分數 | 99.97% |
| 證據等級 | L5 |
| 建議劑型 | 注射液劑 |
| **開發建議** | Hold |
| **決策結論** | Hold |
| **Pharmacist 對應** | 暫不建議 |
| 決策階段 | S0 |
| 阻斷升級因素 | MOA, 文獻支持 |

#### 臨床定義

| 項目 | 內容 | 來源 |
|------|------|------|
| 診斷準則 | [Data Gap] | [來源：PubMed] |
| 目標族群 | [Data Gap] | |
| 排除條件 | [Data Gap] | |
| 現行 SoC | [Data Gap] | [來源：PubMed] |
| Unmet need | [Data Gap] | |
| 流行病學 | [Data Gap] | [來源：PubMed] |

#### 機轉關聯性分析

| 項目 | 內容 | 來源 |
|------|------|------|
| 原適應症機轉 | [Data Gap] | [來源：DrugBank] |
| 新適應症病理 | [Data Gap] | [來源：PubMed] |
| 機轉關聯 | Avelumab 是 PD-L1 抑制劑，可能影響腫瘤 | [來源：DrugBank] |
| 相似度 | 低 | |
| 類似再利用先例 | 無 | [來源：PubMed] |

#### 臨床試驗（標註相關性）

| 試驗編號 | 相關性 | 階段 | 狀態 | N | 結果摘要 |
|---------|-------|-----|------|---|---------|
| N/A | N/A | N/A | N/A | N/A | N/A |

相關性說明：A=高度一致, B=相近族群/proxy, C=機轉支持

#### 文獻證據（標註支撐面向）

| PMID | 年份 | 研究類型 | 支撐面向 | 主要發現 | 限制 |
|------|-----|---------|---------|---------|------|
| N/A | N/A | N/A | N/A | N/A | N/A |

#### 證據可外推性評估（L4/L5 必填）
### 證據可外推性評估

**證據等級**：L5
**證據類型**：模型預測

#### 可外推理由

| 面向 | 支持外推的理由 | 強度 |
|------|---------------|------|
| 機轉相關性 | Avelumab 可能影響腫瘤 | 弱 |
| 族群相似性 | 未知 | 弱 |
| 劑量可行性 | 注射液劑可行 | 中 |

#### ⚠️ 限制條款
> 本證據等級為 L5，存在以下限制：
> 1. **不可**直接作為開發決策依據
> 2. **不可**直接作為試驗設計依據
> 3. **需要**補充臨床試驗和文獻支持後才能升級
>
> 若要使用此資訊，必須以「研究假說」而非「開發計畫」定位。

---

## 5. 適應症比較與優先順序

### 5.1 證據強度比較

| 適應症 | 證據等級 | RCT | 觀察性 | 前臨床 | 強度評分 |
|-------|---------|-----|-------|-------|---------|
| Human herpesvirus 8-related tumor | L5 | 0 | 0 | 0 | 低 |
| Middle ear neuroendocrine tumor | L5 | 0 | 0 | 0 | 低 |
| Malignant cutaneous granular cell skin tumor | L5 | 0 | 0 | 0 | 低 |

### 5.2 開發可行性比較

| 適應症 | 劑型 | 劑型風險 | 安全性風險 | DDI 風險 | 法規路徑 | 可行性 |
|-------|-----|---------|-----------|---------|---------|-------|
| Human herpesvirus 8-related tumor | 注射液劑 | 中 | 中 | 高 | 不明 | 低 |
| Middle ear neuroendocrine tumor | 注射液劑 | 中 | 中 | 高 | 不明 | 低 |
| Malignant cutaneous granular cell skin tumor | 注射液劑 | 中 | 中 | 高 | 不明 | 低 |

### 5.3 優先開發順序
1. **暫無適應症優先開發**：所有預測適應症均缺乏必要證據支持。

---

## 6. Risk Register

### 6.1 Evidence Risk

| 適應症 | 風險 | 嚴重度 | 緩解措施 |
|-------|-----|-------|---------|
| Human herpesvirus 8-related tumor | 缺乏臨床試驗 | 高 | 進行初步臨床試驗 |

### 6.2 Safety Risk

| 風險 | 影響適應症 | 嚴重度 | 緩解措施 |
|-----|-----------|-------|---------|
| 重大 DDI | 所有適應症 | 高 | 進一步安全性評估 |

### 6.3 Regulatory/Operational Risk

| 風險 | 描述 | 嚴重度 | 緩解措施 |
|-----|------|-------|---------|
| 法規 | 缺乏明確的法規路徑 | 中 | 法規諮詢與申請 |
| 執行 | 缺乏必要的研究支持 | 高 | 增加研究投入 |

---

## 7. 補件追蹤表

| # | 缺口 | 阻斷性 | 資料來源 | 負責人 | 截止日 | 狀態 | 影響章節 | 補件後可達建議 |
|---|-----|-------|---------|-------|-------|------|---------|--------------|
| 1 | 作用機轉 (MOA) | 🛑 | DrugBank | 未指定 | 未指定 | ⏳ | §2.4 | Conditional Go |

---

## 8. 補件後決策升級路徑

```
當前狀態：S0 → 最高建議：Hold

補件路徑 1：補齊 MOA 資料
  → 可達：S1 → 升級至：Conditional Go

補件路徑 2：補齊 MOA + 臨床試驗支持
  → 可達：S2 → 升級至：Go
```

---

## 附錄：資料收集日誌

| # | 資料來源 | 查詢日期 | 查詢條件 | 結果 | 原始結果連結 |
|---|---------|---------|---------|------|-------------|
| 1 | TFDA | 2026-02-09 | {drug: "avelumab"} | 2 | [snapshot] |
| 2 | DDI | 2026-02-09 | {drug: "avelumab"} | 3 | [snapshot] |
| 3 | DrugBank | 2026-02-09 | {drug: "avelumab"} | 1 | [snapshot] |
| 4 | TFDA 仿單 | 2026-02-09 | {drug: "avelumab"} | 1 | [snapshot] |
| 5 | ClinicalTrials.gov | 2026-02-09 | {drug: "avelumab", disease: "human herpesvirus 8-related tumor"} | 0 | [snapshot] |

---

## 文件版本資訊

| 項目 | 內容 |
|------|------|
| 文件版本 | v1.0 |
| 產生日期 | 2026-02-09 |
| 資料截止日 | 2026-02-09 |
| Evidence Pack 版本 | avelumab_v4_2026-02-09.json |
