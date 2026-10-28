---
layout: default
title: Sacituzumab Govitecan
parent: 僅模型預測 (L5)
nav_order: 250
evidence_level: L5
indication_count: 4
monitor_inn: "Sacituzumab govitecan"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract"]
last_modified_at: 2026-10-29
description: "Sacituzumab Govitecan：預測新適應症為藥物誘發性骨質疏鬆 (Drug-induced Osteoporosis)（證據等級 L5）。原適應症：1. 先前已接受兩次以上全身性治療無效（其中一次需為治療晚期疾病）之無法切除的局部晚期或轉移性三陰性乳癌成年病人。2. 荷爾蒙受體（HR）…"
---

# Sacituzumab Govitecan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## Sacituzumab govitecan：從三陰性乳癌到藥物誘發性骨質疏鬆
{: .text-alpha }

## 一句話總結

Sacituzumab govitecan（商品名：拓達維）是一種以 Trop-2 為標的的抗體藥物複合體（ADC），原本用於治療無法切除的局部晚期或轉移性乳癌。
TxGNN 模型預測它可能對**藥物誘發性骨質疏鬆 (Drug-induced Osteoporosis)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 1. 先前已接受兩次以上全身性治療無效（其中一次需為治療晚期疾病）之無法切除的局部晚期或轉移性三陰性乳癌成年病人。2. 荷爾蒙受體（HR）陽性、HER2 陰性（IHC 0、IHC 1+ 或 IHC 2+/ISH–）、無法切除的局部晚期或轉移性乳癌，且過去曾接受至少 2 次轉移性乳癌全身性治療的成年病人 |
| 預測新適應症 | 藥物誘發性骨質疏鬆 (Drug-induced Osteoporosis) |
| TxGNN 預測分數 | 0.9978 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效單方 1／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Sacituzumab govitecan 是以 Trop-2 為標的的抗體，連結 SN-38（拓樸異構酶 I 抑制劑）作為細胞毒性藥物載荷，用於已多線治療的乳癌。

**坦白說，這個預測在機轉上缺乏合理性。** 目前沒有任何證據顯示 Trop-2 標的的細胞毒性藥物與骨重塑或骨質疏鬆有關。細胞毒性載荷反而可能對骨骼健康造成不利影響，而非改善。這項預測完全來自 TxGNN 的計算分數，沒有臨床或前臨床研究佐證。

其他排名較前的預測（嚴重非增殖性糖尿病視網膜病變、糖尿病視網膜病變、糖尿病白內障）同樣沒有試驗或文獻支持，也缺乏機轉依據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Sacituzumab Govitecan 的不重複許可證共 **1 張**：有效單方 1 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部菌疫輸字第001206號 | 拓達維注射劑 | 凍晶注射劑 | 香港商吉立亞醫藥有限公司台灣分公司 | 2027/11/15 | 1. 適用於治療先前已接受兩次以上全身性治療無效(其中一次需為治療晚期疾病)之無法切除的局部晚期或轉移性的三陰性乳癌成年病人。 2.適用於治療患有無法切除的局部晚期或轉移性的荷爾蒙… |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 抗體藥物複合體（ADC），載荷 SN-38 為拓樸異構酶 I 抑制劑，屬細胞毒性藥物 |
| 骨髓抑制風險 | 高（系統性細胞毒性，常見嗜中性白血球低下） |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | CBC（含分類）、肝腎功能、腹瀉與脫水狀況 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

其餘細節請參考原廠仿單的警語與注意事項。

## 安全性考量

- **藥物交互作用**：已查詢到 40 筆交互作用，以下列出部分重點：
  - **Major（嚴重）**：Irinotecan（與 SN-38 同屬拓樸異構酶 I 抑制劑）、Deferiprone、Fostamatinib、Adalimumab、Apalutamide、Certolizumab pegol、Cladribine、Dacomitinib、Leflunomide、Natalizumab、Nilotinib、Ozanimod
  - **Moderate（中度）**：Alefacept、Alemtuzumab、Anakinra、Canakinumab、Dimethyl fumarate、Lorlatinib、Ocrelizumab、Omacetaxine mepesuccinate

  多數屬免疫抑制劑或具骨髓抑制作用的藥物，合併使用時需留意感染與血球低下風險。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測僅來自模型分數，沒有任何臨床試驗或文獻，證據等級為 L5。
- 機轉上沒有合理連結，且系統性細胞毒性藥物用於非腫瘤的慢性疾病，風險效益比不利。

**若要推進需要：**
- 取得詳細的作用機轉資料（MOA），評估與骨代謝是否有任何關聯
- 先進行文獻與前臨床證據的系統性檢索，確認是否有支持訊號
- 若無任何支持證據，建議不再推進此預測，並優先評估其他排名較高、機轉較合理的候選適應症

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證數寫 3 張 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

