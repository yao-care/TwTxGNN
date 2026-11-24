---
layout: default
title: Ipilimumab
parent: 僅模型預測 (L5)
nav_order: 153
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
description: "Ipilimumab：預測新適應症為脈絡膜缺失症 (Choroideremia)（證據等級 L5）。原適應症：無法切除或轉移性黑色素瘤（併用 nivolumab）、晚期腎細胞癌、MSI-H/dMMR 轉移性大腸直腸癌、肝細胞癌、非小細胞肺癌…"
monitor_inn: "Ipilimumab"
predicted_indications: ["choroideremia"]
---

# Ipilimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Ipilimumab：從無法切除或轉移性黑色素瘤到脈絡膜缺失症 (Choroideremia)
{: .text-alpha }

## 一句話總結

Ipilimumab 是抗 CTLA-4 的免疫檢查點抑制劑，原本用於無法切除或轉移性黑色素瘤等多種癌症。
TxGNN 模型預測它可能對**脈絡膜缺失症 (Choroideremia)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無法切除或轉移性黑色素瘤（併用 nivolumab）、晚期腎細胞癌、MSI-H/dMMR 轉移性大腸直腸癌、肝細胞癌、非小細胞肺癌、惡性肋膜間皮瘤、食道鱗狀細胞癌 |
| 預測新適應症 | 脈絡膜缺失症 (Choroideremia) |
| TxGNN 預測分數 | 0.9906 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效單方 1／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Ipilimumab 仿單（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「CTLA-4 是 T 細胞活性的負向調節因子。Ipilimumab 是一種單株抗體，可與 CTLA-4 結合，並阻斷 CTLA-4 與其配體 CD80/CD86 之間的交互作用。研究顯示，阻斷 CTLA-4 可增強 T 細胞的活化及增生，包括腫瘤浸潤性效應 T 細胞的活化及增生。」英文原文："CTLA-4 is a negative regulator of T-cell activity. Ipilimumab is a monoclonal antibody that binds to CTLA-4 and blocks the interaction of CTLA-4 with its ligands, CD80/CD86. Blockade of CTLA-4 has been shown to augment T-cell activation and proliferation, including the activation and proliferation of tumor infiltrating T-effector cells."（[DailyMed: Yervoy (ipilimumab) prescribing information, E.R. Squibb & Sons, L.L.C.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2265ef30-253e-11df-8a39-0800200c9a66)，版本日期 2026-08-20；查閱日期 2026-11-19）。根據已知資訊，Ipilimumab 透過阻斷 CTLA-4 來解除 T 細胞的活化抑制，增強抗腫瘤 T 細胞反應，這也是它在黑色素瘤等癌症中有效的原因。

脈絡膜缺失症是一種 X 染色體連鎖的單基因視網膜退化疾病，起因是 CHM/REP1 基因功能喪失。它與腫瘤免疫沒有已知的關聯，也沒有已建立的免疫檢查點機轉。

因此，這個預測的合理性目前僅來自 TxGNN 模型的分數。原適應症與新適應症在機轉和疾病性質上差異很大，無法從現有資料推導出可信的藥理關聯。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-11-24），主成分含 Ipilimumab 的不重複許可證共 **1 張**：有效單方 1 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-11-24）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部菌疫輸字第000958號 | 益伏注射劑 5毫克/毫升 | 注射液劑 | 台灣必治妥施貴寶股份有限公司 | 2029/08/18 | 1.無法切除或轉移性黑色素瘤：併用 nivolumab 適用於治療無法切除或轉移性黑色素瘤之12歲以上病人。 2.晚期腎細胞癌：併用 nivolumab 適用於中度/重度風險 (i… |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 免疫治療（抗 CTLA-4 單株抗體），非傳統細胞毒性藥物 |
| 其他項目（骨髓抑制風險、致吐性、監測項目、處置防護） | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：已查詢到 132 筆交互作用，以下列出主要類別：
  - **Major 等級**：抗凝血藥物，包括 Apixaban、Betrixaban、Edoxaban、Dalteparin、Danaparoid、Bivalirudin、Desirudin、Argatroban。
  - **Moderate 等級**：
    - 皮質類固醇：Hydrocortisone、Prednisone、Prednisolone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide。
    - 其他：Metronidazole、Tinidazole、Naltrexone、Rosuvastatin、Simvastatin。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測僅有模型分數支持，沒有臨床試驗、文獻或機轉證據。
- 脈絡膜缺失症是單基因視網膜退化疾病，與免疫檢查點阻斷缺乏合理的生物學連結。
- Ipilimumab 有嚴重的免疫相關不良反應風險，在沒有任何療效訊號的非腫瘤疾病中不宜推進。

**若要推進需要：**
- 釐清 CTLA-4 抑制與 CHM/REP1 缺失造成的視網膜退化之間有無可驗證的機轉假說。
- 進行前臨床研究（如視網膜細胞或動物模型），以取得初步療效與安全性訊號。
- 補齊 DrugBank 作用機轉資料。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯與英文原文）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國仿單節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Yervoy (ipilimumab) prescribing information, E.R. Squibb & Sons, L.L.C.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2265ef30-253e-11df-8a39-0800200c9a66) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

