---
layout: default
title: Clobetasone
parent: 藥物列表
nav_order: 18
evidence_level: L5
indication_count: 1
---

# Clobetasone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Pharmacist Notes — Clobetasone 老藥新用

---

## ⚠️ 資料完整性與可用性聲明

**文件產出日期**：2026-02-09
**決策階段**：S0（初始評估）
**目前決策**：Hold

### 本文件可支持的決策
| 可支持 | 不可支持 |
|-------|---------|
| 暫停所有臨床應用 | 直接臨床建議 |

### 阻斷性缺口摘要
| # | 缺口項目 | 推論限制 | 解鎖條件 |
|---|---------|---------|---------|
| 1 | 作用機轉 (MOA) | 影響機轉關聯性分析 | 查詢 DrugBank API |

### 保守假設摘要
| # | 假設 | 依據 | 限制 | 觸發條件 |
|---|------|------|------|---------|
| 無 | 無 | 無 | 無 | 無 |

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
| TFDA 許可證 | ✅ | 2026-02-09 | {"drug": "clobetasone"} | 20 | 無 |
| TFDA 仿單（警語/禁忌/劑量） | ✅ | 2026-02-09 | {"drug": "clobetasone"} | 1 | 無 |
| DDI 資料庫 (Unified DDI) | ⚠️ [未找到] | 2026-02-09 | {"drug": "clobetasone"} | 0 | 無 |
| DrugBank (MOA) | ✅ | 2026-02-09 | {"drug": "clobetasone"} | 1 | 影響機轉分析 |
| ClinicalTrials.gov | ✅ (無結果) | 2026-02-09 | {"drug": "clobetasone", "disease": "primary cutaneous T-cell lymphoma"} | 0 | 無 |
| PubMed | ✅ (無結果) | 2026-02-09 | {"drug": "clobetasone", "disease": "primary cutaneous T-cell lymphoma"} | 0 | 無 |

---

## 1. 藥物再利用總覽

### 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物名稱 | Clobetasone | |
| DrugBank ID | DB13158 | |
| **原核准適應症** | [Data Gap] | |
| **原作用機轉 (MOA)** | [Data Gap] | |
| 台灣上市狀態 | 已上市 | TFDA |
| 可用劑型 | [Data Gap] | |

### 預測新適應症總覽
| 排名 | 預測適應症 | 建議劑型 | TxGNN 分數 | 證據等級 | 藥師立場 | 決策結論 | 關鍵缺口 |
|------|-----------|---------|-----------|---------|---------|---------|---------|
| 1 | Primary cutaneous T-cell lymphoma | [Data Gap] | 99.97% | L5 | 暫不建議 | Hold | 機轉與臨床證據缺乏 |
| 2 | Sezary syndrome | [Data Gap] | 99.78% | L5 | 暫不建議 | Hold | 機轉與臨床證據缺乏 |
| 3 | Primary cutaneous B-cell lymphoma | [Data Gap] | 99.77% | L5 | 暫不建議 | Hold | 機轉與臨床證據缺乏 |

---

## 2. Taiwan Regulatory & Label Snapshot

### 2.1 TFDA 上市狀態
- 上市狀態：已上市
- 核准適應症：[Data Gap]
- 許可證號：[Data Gap]

### 2.2 許可證詳細資訊
| 許可證號 | 中文品名 | 劑型 | 濃度 | 製造廠 | 仿單版本 |
|---------|---------|------|------|-------|---------|
| [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] |

### 2.3 仿單關鍵資訊（按劑型分列）

#### 外用劑型
| 項目 | 內容 | 來源 |
|------|------|------|
| 主要警語 | [Data Gap] | |
| 禁忌症 | [Data Gap] | |
| 建議劑量 | [Data Gap] | |
| 孕哺分級 | [Data Gap] | |
| 肝功能調整 | [不適用] | |
| 腎功能調整 | [不適用] | |
| 特殊族群（兒童） | [Data Gap] | |
| 特殊族群（老人） | [Data Gap] | |

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
| | • 官方標籤/主管機關資料（TFDA/FDA/EMA/PMDA）：未找到 |
| | • 權威藥學資料庫（DDInter/Guide to PHARMACOLOGY/DrugBank）：查詢成功，未取得詳細機轉 |
| | • 同儕審查文獻（PubMed/期刊）：未找到 |
| | • 試驗登錄（ClinicalTrials.gov）：未找到 |
| **檢索結果** | 僅二手資訊 |
| **推論限制（不能做）** | 機轉分析 |
| **風險處置（決策）** | Hold |
| **解鎖條件** | 需要從 DrugBank 獲取詳細的作用機轉資料 |

---

## 6. 各適應症特定考量

### 6.1 Primary cutaneous T-cell lymphoma（證據等級: L5）

#### 臨床定義
| 項目 | 內容 | 來源 |
|------|------|------|
| 疾病全名 | Primary cutaneous T-cell lymphoma | |
| ICD-10 | [Data Gap] | WHO |
| 診斷準則 | [Data Gap] | |
| 目標族群 | [Data Gap] | |
| 排除條件 | [Data Gap] | |
| 現行標準治療 (SoC) | [Data Gap] | |
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
| 關鍵缺口 | 機轉與臨床證據缺乏 |
| 立場變更條件 | 需要臨床試驗數據和機轉研究支持 |

#### 證據可外推性評估
| 面向 | 支持外推的理由 | 強度 |
|------|---------------|------|
| 機轉相關性 | Clobetasone 可能具有抗炎和免疫抑制作用 | 弱 |
| 族群相似性 | 無直接臨床證據支持 | 弱 |
| 劑量可行性 | 劑型和途徑尚未確定 | 弱 |

#### ⚠️ 限制條款
> 本證據等級為 L5，存在以下限制：
> 1. **不可**直接作為臨床執行依據
> 2. **不可**直接作為試驗設計依據
> 3. **需要**補充臨床試驗數據後才能升級

---

## 7. Guardrails（若決策為 Proceed with Guardrails）

**目前無法設立**

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
| [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] |

---

## 9. Evidence Summary

### 9.1 證據等級分布
| 等級 | 適應症數 | 臨床意義 |
|-----|---------|---------|
| L1 | 0 | 無 |
| L2 | 0 | 無 |
| L3 | 0 | 無 |
| L4 | 0 | 無 |
| L5 | 3 | 暫不建議 |

### 9.2 Limitations
- 缺乏詳細的機轉資料
- 無臨床試驗支持

---

## 10. 補件追蹤表

| # | 缺口 | 阻斷性 | 資料來源 | 負責人 | 截止日 | 狀態 | 影響章節 |
|---|-----|-------|---------|-------|-------|------|---------|
| 1 | 作用機轉 (MOA) | 🛑 | DrugBank | 未指派 | 未設定 | ⏳ | §5 |

---

## 附錄：資料收集日誌

| # | 資料來源 | 查詢日期 | 查詢條件 | 結果 | 原始結果連結 |
|---|---------|---------|---------|------|-------------|
| 1 | TFDA | 2026-02-09 | {"drug": "clobetasone"} | 20 | [snapshot] |
| 2 | DDI | 2026-02-09 | {"drug": "clobetasone"} | 0 | [snapshot] |
| 3 | DrugBank | 2026-02-09 | {"drug": "clobetasone"} | 1 | [snapshot] |

---

## 文件版本資訊

| 項目 | 內容 |
|------|------|
| 文件版本 | v1.0 |
| 產生日期 | 2026-02-09 |
| 資料截止日 | 2026-02-09 |
| Evidence Pack 版本 | clobetasone_v4_2026-02-09.json |

---

<div id="sponsor">

## 贊助商報告

</div>

# Sponsor Notes — Clobetasone 老藥新用開發評估

---

## ⚠️ 資料完整性與可用性聲明

**文件產出日期**：2026-02-09
**決策階段**：S0（初步評估）
**目前決策**：Hold

### 本文件可支持的決策
| 可支持 | 不可支持 |
|-------|---------|
| 確定資料缺口 | 直接進入開發 |

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
>    - 開發建議（Go/Conditional Go）
>    - 排除條件定稿
>    - 試驗設計依據
> 3. 若後續取得新資料，將依解鎖條件更新風險分級與決策。

---

## 0. 藥物再利用總覽

### 資料來源稽核框（Data Provenance）

| 資料來源 | 狀態 | 查詢日期 | 查詢條件 | 筆數/備註 | 對決策的影響 |
|---------|------|---------|---------|----------|-------------|
| TFDA 許可證 | ✅ | 2026-02-09 | {"drug": "clobetasone"} | 20 | 確認上市狀態 |
| TFDA 仿單 | ✅ | 2026-02-09 | {"drug": "clobetasone"} | 1 | 確認安全資訊 |
| DDI 資料庫 (Unified DDI) | ⚠️ [未找到] | 2026-02-09 | {"drug": "clobetasone"} | 0 | 影響 DDI 評估 |
| DrugBank (MOA) | ✅ | 2026-02-09 | {"drug": "clobetasone"} | 1 | 影響機轉分析 |
| ClinicalTrials.gov | ✅ (無結果) | 2026-02-09 | {"drug": "clobetasone", "disease": "primary cutaneous T-cell lymphoma"} | 0 | 無臨床試驗支持 |
| PubMed | ✅ (無結果) | 2026-02-09 | {"drug": "clobetasone", "disease": "primary cutaneous T-cell lymphoma"} | 0 | 無文獻支持 |

### 藥物基本資訊
| 項目 | 內容 | 來源 |
|------|------|------|
| 藥物名稱 | Clobetasone | |
| DrugBank ID | DB13158 | |
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
| 1 | Primary cutaneous T-cell lymphoma | 99.97% | L5 | 0 項 | [Data Gap] | Hold | Hold | 機轉與路徑資料缺乏 |
| 2 | Sezary syndrome | 99.78% | L5 | 0 項 | [Data Gap] | Hold | Hold | 機轉與路徑資料缺乏 |
| 3 | Primary cutaneous B-cell lymphoma | 99.77% | L5 | 0 項 | [Data Gap] | Hold | Hold | 機轉與路徑資料缺乏 |

**整體開發建議**：目前所有預測適應症均因資料缺口而處於 Hold 階段，需補充機轉與路徑資料以進一步評估。[來源：DrugBank]

---

## 1. Executive Brief (≤1 page)

### 開發決策總覽
| 適應症 | 開發建議 | 決策結論 | 決策階段 | 關鍵支持 | 關鍵缺口 | Pharmacist 對應立場 |
|-------|---------|---------|---------|---------|---------|-------------------|
| Primary cutaneous T-cell lymphoma | Hold | Hold | S0 | [Data Gap] | MOA, DDI | 暫不建議 |
| Sezary syndrome | Hold | Hold | S0 | [Data Gap] | MOA, DDI | 暫不建議 |
| Primary cutaneous B-cell lymphoma | Hold | Hold | S0 | [Data Gap] | MOA, DDI | 暫不建議 |

### 整體決策建議
- **最優先開發**：暫無 — 需補充資料
- **次優先開發**：暫無 — 需補充資料
- **Hold**：所有預測適應症 — 需補件後可升級
- **No-Go**：暫無 — 需補充資料後評估

### Top 3 Key Points
1. Clobetasone 缺乏明確的作用機轉資料，影響新適應症的機轉關聯性分析。[來源：DrugBank]
2. 所有預測適應症目前無臨床試驗或文獻支持，需進一步研究。[來源：ClinicalTrials.gov, PubMed]
3. DDI 資料缺乏，影響安全性評估。[來源：DDI 資料庫]

### Top Risks & Mitigation
| 風險類型 | 描述 | 嚴重度 | 緩解措施 |
|---------|------|-------|---------|
| 證據 | 缺乏機轉和臨床支持 | 高 | 補充機轉與臨床試驗數據 |
| 安全性 | DDI 資料缺乏 | 中 | 查詢更多 DDI 資料 |
| 法規 | 無法確定適應症的法規路徑 | 高 | 確認法規需求 |

### Next Step MVP（若為 Go/Conditional Go）
| 適應症 | 試驗類型 | N | 主要 endpoint | 次要 endpoint |
|-------|---------|---|--------------|--------------|
| 暫無 | 暫無 | 暫無 | 暫無 | 暫無 |

---

## 2. 藥物層級資訊

### 2.1 Taiwan Regulatory Snapshot
- **TFDA 上市狀態**：已上市 [來源：TFDA]
- **核准適應症**：[Data Gap] [來源：TFDA]
- **許可證號**：[Data Gap]

**Label Constraints / Warnings**：
[Data Gap] 影響安全性評估 [來源：TFDA 仿單]

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
- **MOA**：[Data Gap] [來源：DrugBank]
- **與新適應症相關的藥理特性**：待確認 [來源：DrugBank]

---

## 3. Data Gaps 完整記錄

### Data Gap #1 — 作用機轉 (MOA)（🛑 Blocking）

| 欄位 | 內容 |
|------|------|
| **缺口項目** | 作用機轉 (MOA) |
| **已完成檢索行動** | |
| | • 官方標籤/主管機關資料（TFDA/FDA/EMA/PMDA）：未找到 |
| | • 權威藥學資料庫（DDInter/Guide to PHARMACOLOGY/DrugBank）：查詢 DrugBank，未找到具體資料 |
| | • 同儕審查文獻（PubMed/期刊）：未找到 |
| | • 試驗登錄（ClinicalTrials.gov）：未找到 |
| **檢索結果** | 未找到 |
| **推論限制（不能做）** | 無法進行機轉關聯性分析 |
| **風險處置（決策）** | Hold |
| **解鎖條件** | 需要 DrugBank API 提供的詳細 MOA 資料 |

---

## 4. 各適應症詳細評估

### 4.1 Primary cutaneous T-cell lymphoma（L5）

#### 基本資訊與決策
| 項目 | 內容 |
|------|------|
| 疾病名稱 | Primary cutaneous T-cell lymphoma |
| ICD-10 | [Data Gap] |
| TxGNN 分數 | 99.97% |
| 證據等級 | L5 |
| 建議劑型 | [Data Gap] |
| **開發建議** | Hold |
| **決策結論** | Hold |
| **Pharmacist 對應** | 暫不建議 |
| 決策階段 | S0 |
| 阻斷升級因素 | 機轉與路徑資料缺乏 |

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
| 相似度 | 中 | |
| 類似再利用先例 | 無 | [Data Gap] |

#### 臨床試驗（標註相關性）
| 試驗編號 | 相關性 | 階段 | 狀態 | N | 結果摘要 |
|---------|-------|-----|------|---|---------|
| [Data Gap] | C | [Data Gap] | [Data Gap] | [Data Gap] | [Data Gap] |

相關性說明：A=高度一致, B=相近族群/proxy, C=機轉支持

#### 文獻證據（標註支撐面向）
| PMID | 年份 | 研究類型 | 支撐面向 | 主要發現 | 限制 |
|------|-----|---------|---------|---------|------|
| [Data Gap] | [Data Gap] | [Data Gap] | ☐療效 ☐機轉 ☐安全性 ☐族群 | [Data Gap] | [Data Gap] |

#### 證據可外推性評估

**證據等級**：L5
**證據類型**：模型預測

#### 可外推理由
| 面向 | 支持外推的理由 | 強度 |
|------|---------------|------|
| 機轉相關性 | [Data Gap] | 弱 |
| 族群相似性 | [Data Gap] | 弱 |
| 劑量可行性 | [Data Gap] | 弱 |

#### ⚠️ 限制條款
> 本證據等級為 L5，存在以下限制：
> 1. **不可**直接作為開發決策依據
> 2. **不可**直接作為試驗設計依據
> 3. **需要**補充臨床試驗數據後才能升級

#### Evidence Gap 與影響
| 缺口 | 阻斷性 | 影響程度 | 對決策影響 | 補件方式 |
|-----|-------|---------|-----------|---------|
| MOA | 🛑 | 高 | 無法進行機轉分析 | 查詢 DrugBank API |

---

### 4.x Sezary syndrome ⚠️ 僅模型預測

| 項目 | 內容 |
|------|------|
| TxGNN 分數 | 99.78% |
| 證據等級 | L5 |
| **開發建議** | Hold |
| **決策結論** | Hold |
| **Pharmacist 對應** | 暫不建議 |

**阻斷/Hold 原因**：機轉與路徑資料缺乏

#### 證據可外推性評估
（使用模板，強調限制條款）

**若要升級至 Hold/Conditional Go 需補齊**：
- [ ] 作用機轉資料
- [ ] 臨床試驗數據

---

## 5. 適應症比較與優先順序

### 5.1 證據強度比較
| 適應症 | 證據等級 | RCT | 觀察性 | 前臨床 | 強度評分 |
|-------|---------|-----|-------|-------|---------|
| Primary cutaneous T-cell lymphoma | L5 | 0 | 0 | 0 | 低 |
| Sezary syndrome | L5 | 0 | 0 | 0 | 低 |
| Primary cutaneous B-cell lymphoma | L5 | 0 | 0 | 0 | 低 |

### 5.2 開發可行性比較
| 適應症 | 劑型 | 劑型風險 | 安全性風險 | DDI 風險 | 法規路徑 | 可行性 |
|-------|-----|---------|-----------|---------|---------|-------|
| Primary cutaneous T-cell lymphoma | [Data Gap] | 中 | 高 | 高 | 不明 | 低 |
| Sezary syndrome | [Data Gap] | 中 | 高 | 高 | 不明 | 低 |
| Primary cutaneous B-cell lymphoma | [Data Gap] | 中 | 高 | 高 | 不明 | 低 |

### 5.3 優先開發順序
1. **Primary cutaneous T-cell lymphoma**：需補充機轉與臨床資料
2. **Sezary syndrome**：需補充機轉與臨床資料
3. **Primary cutaneous B-cell lymphoma**：需補充機轉與臨床資料

---

## 6. Risk Register

### 6.1 Evidence Risk
| 適應症 | 風險 | 嚴重度 | 緩解措施 |
|-------|-----|-------|---------|
| Primary cutaneous T-cell lymphoma | 缺乏機轉資料 | 高 | 查詢 DrugBank API |

### 6.2 Safety Risk
| 風險 | 影響適應症 | 嚴重度 | 緩解措施 |
|-----|-----------|-------|---------|
| DDI 資料缺乏 | 所有適應症 | 高 | 查詢更多 DDI 資料 |

### 6.3 Regulatory/Operational Risk
| 風險 | 描述 | 嚴重度 | 緩解措施 |
|-----|------|-------|---------|
| 法規 | 適應症法規路徑不明 | 高 | 確認法規需求 |
| 執行 | 缺乏試驗支持 | 高 | 設計前期試驗 |

---

## 7. 補件追蹤表

| # | 缺口 | 阻斷性 | 資料來源 | 負責人 | 截止日 | 狀態 | 影響章節 | 補件後可達建議 |
|---|-----|-------|---------|-------|-------|------|---------|--------------|
| 1 | MOA | 🛑 | DrugBank | [負責人] | [日期] | ⏳ | §2.4 | Conditional Go |

---

## 8. 補件後決策升級路徑

```
當前狀態：S0 → 最高建議：Hold

補件路徑 1：補齊 MOA 資料
  → 可達：S1 → 升級至：Conditional Go

補件路徑 2：補齊 MOA + 臨床試驗數據
  → 可達：S2 → 升級至：Go
```

---

## 附錄：資料收集日誌

| # | 資料來源 | 查詢日期 | 查詢條件 | 結果 | 原始結果連結 |
|---|---------|---------|---------|------|-------------|
| 1 | TFDA | 2026-02-09 | {"drug": "clobetasone"} | 20 | [snapshot] |

---

## 文件版本資訊

| 項目 | 內容 |
|------|------|
| 文件版本 | v1.0 |
| 產生日期 | 2026-02-09 |
| 資料截止日 | 2026-02-09 |
| Evidence Pack 版本 | TW-DB13158-multi_v4_2026-02-09.json |
