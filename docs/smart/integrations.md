---
layout: default
title: 整合資源
parent: 🏥 SMART on FHIR
nav_order: 3
description: TwTxGNN SMART App 整合的外部資源，包含臨床試驗查詢、藥物交互作用檢查、CDS Hooks 服務
permalink: /smart/integrations/
---

# 整合資源

TwTxGNN SMART App 整合了多個外部資源，提供更完整的臨床決策支援。

---

## 臨床試驗查詢

每個預測適應症旁都有「🔬 臨床試驗」按鈕，即時查詢 ClinicalTrials.gov 相關臨床試驗。

| 資源 | 說明 | 連結 |
|------|------|------|
| **ClinicalTrials.gov API v2** | 美國 NIH 臨床試驗資料庫，提供全球臨床試驗搜尋 | [API 文件](https://clinicaltrials.gov/data-api/api) |

### 功能說明

- 即時搜尋藥物 + 適應症的相關臨床試驗
- 顯示試驗狀態（招募中、進行中、已完成等）
- 顯示試驗階段（Phase 1-4）
- 直接連結到 ClinicalTrials.gov 詳細頁面

---

## 藥物交互作用檢查

查詢多個藥物時，頁面會用 `ddi-checker.js` 內建的 15 條規則檢查常見的高風險藥物組合（DDI）並顯示警示。這不是完整的資料庫比對：沒有警示不代表沒有交互作用。

| 資源 | 說明 | 連結 |
|------|------|------|
| **DDInter** | 內建規則參考 DDInter；藥物報告的 DDI 用 DDInter 1.0 下載檔（222,391 筆，見[安全性資料]({{ '/nav-safety/' | relative_url }})） | [DDInter 網站](https://ddinter2.scbdd.com/) |
| **Guide to PHARMACOLOGY** | IUPHAR/BPS 藥理學指南，藥物報告使用其核准藥物交互作用資料；頁面即時檢查不使用 | [官方網站](https://www.guidetopharmacology.org/) |

### 警示等級

| 等級 | 說明 | 顯示顏色 |
|------|------|----------|
| **Major（重度）** | 需要立即注意，可能危及生命 | 紅色 |
| **Moderate（中度）** | 需要注意，可能需要調整 | 黃色 |
| **Minor（輕度）** | 輕微風險，告知即可 | 藍色 |

### 涵蓋的重要交互作用

- Warfarin + NSAIDs（出血風險）
- Colchicine + CYP3A4 抑制劑（毒性風險）
- QT 延長藥物組合（心律不整風險）
- Digoxin + Amiodarone（Digoxin 毒性）
- SSRI + Tramadol（血清素症候群）

---

## CDS Hooks 服務

TwTxGNN 提供 CDS Hooks 服務的描述與瀏覽器端示範。本站是靜態網站，沒有能接收 EHR 請求的服務端點；要接進 EHR 的處方流程，需要另外架設能接收 POST 請求的伺服器。

### 可用服務

| 服務 ID | Hook | 說明 |
|---------|------|------|
| `twtxgnn-ddi-check` | order-sign | 處方時檢查藥物交互作用 |
| `twtxgnn-repurposing` | order-sign | 顯示老藥新用候選 |
| `twtxgnn-trial-match` | patient-view | 臨床試驗配對 |

### 服務端點

**服務描述**：[/cds-hooks/cds-services.json](/cds-hooks/cds-services.json)（只是描述檔，不是可呼叫的服務）

<div style="margin: 20px 0;">
  <a href="/cds-hooks/demo.html" style="display: inline-block; padding: 12px 24px; background: #17a2b8; color: white; text-decoration: none; border-radius: 8px; font-weight: 500;">測試 CDS Hooks Demo</a>
</div>

### 整合方式

1. 在自行架設的伺服器上提供服務發現端點，並註冊到您的 EHR 系統
2. 配置 prefetch 以提供 MedicationRequest 資源
3. 在 order-sign hook 觸發時呼叫服務
4. 顯示回傳的 cards 給臨床人員

---

## 標準規範參考

| 標準 | 說明 | 連結 |
|------|------|------|
| **HL7 PDDI-CDS IG** | 藥物交互作用臨床決策支援實作指引 | [GitHub](https://github.com/HL7/PDDI-CDS) |
| **CDS Hooks** | SMART on FHIR 臨床決策支援標準 | [官方規範](https://cds-hooks.org/) |
| **CQL (Clinical Quality Language)** | 臨床品質語言，用於定義決策規則 | [HL7 CQL](https://cql.hl7.org/) |

---

## CQL 規則庫

TwTxGNN 提供 CQL 格式的 DDI 檢查規則，可用於整合至符合標準的 CDS 系統。

**CQL 檔案**：[/cql/TwTxGNN_DDI_CDS.cql](/cql/TwTxGNN_DDI_CDS.cql)

### 包含的規則

- Warfarin-NSAID 交互作用檢查
- Metformin-顯影劑交互作用檢查
- Colchicine-CYP3A4 抑制劑檢查
- QT 延長藥物組合檢查
- 血清素症候群風險檢查

---

## 外部資源連結

| 資源 | 說明 | 連結 |
|------|------|------|
| ClinicalTrials.gov | 臨床試驗搜尋 | [clinicaltrials.gov](https://clinicaltrials.gov/) |
| DDInter 2.0 | 藥物交互作用資料庫 | [ddinter2.scbdd.com](https://ddinter2.scbdd.com/) |
| Guide to PHARMACOLOGY | 藥理學資料庫 | [guidetopharmacology.org](https://www.guidetopharmacology.org/) |
| HL7 PDDI-CDS IG | PDDI 實作指引 | [GitHub](https://github.com/HL7/PDDI-CDS) |
| CDS Hooks | 臨床決策支援標準 | [cds-hooks.org](https://cds-hooks.org/) |
| HL7 CQL | 臨床品質語言 | [cql.hl7.org](https://cql.hl7.org/) |
