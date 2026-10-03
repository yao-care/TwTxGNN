---
layout: default
title: Sacituzumab Govitecan
parent: 僅模型預測 (L5)
nav_order: 232
evidence_level: L5
indication_count: 4
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Sacituzumab Govitecan：從三陰性乳癌到新適應症探索

## 一句話總結

Sacituzumab govitecan 原本用於治療晚期三陰性乳癌及 HR+/HER2- 乳癌。TxGNN 模型預測它可能對**藥物誘發性骨質疏鬆症 (drug-induced osteoporosis)** 有效，但目前僅有模型預測支持，缺乏臨床證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 晚期三陰性乳癌、HR+/HER2- 乳癌 |
| 預測新適應症 | 藥物誘發性骨質疏鬆症 (drug-induced osteoporosis) |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L5 |
| 台灣上市 | 已上市 |
| 許可證數 | 1 張（有效單方 1／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Sacituzumab govitecan 是一種抗體藥物複合體（ADC），由抗 Trop-2 抗體與 SN-38（irinotecan 的活性代謝物）連結：

1. **Trop-2 靶點**：Trop-2（tumor-associated calcium signal transducer 2）主要在上皮細胞表達，在多種實體腫瘤中過度表達。

2. **細胞毒性機轉**：SN-38 是拓撲異構酶 I 抑制劑，主要用於抗腫瘤治療。

3. **預測適應症的合理性存疑**：藥物誘發性骨質疏鬆症與 Trop-2 或拓撲異構酶 I 抑制劑的作用機轉缺乏明確關聯，此預測的生物學合理性較低。

## 臨床試驗證據

目前無 Sacituzumab govitecan 用於藥物誘發性骨質疏鬆症的臨床試驗登記。

## 文獻證據

目前無相關文獻支持。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Sacituzumab Govitecan 的不重複許可證共 **1 張**：有效單方 1 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部菌疫輸字第001206號 | 拓達維注射劑 | 凍晶注射劑 | 香港商吉立亞醫藥有限公司台灣分公司 | 2027/11/15 | 1. 適用於治療先前已接受兩次以上全身性治療無效(其中一次需為治療晚期疾病)之無法切除的局部晚期或轉移性的三陰性乳癌成年病人。 2.適用於治療患有無法切除的局部晚期或轉移性的荷爾蒙… |

<!-- tfda-licenses:end -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 抗體藥物複合體 (ADC) |
| 骨髓抑制風險 | 高 - 中性粒細胞減少症是常見嚴重不良反應 |
| 致吐性分級 | 中度 |
| 監測項目 | 完整血球計數、肝腎功能、腹瀉症狀 |
| 處置防護 | 需遵循細胞毒性藥物處理標準 |

## 安全性考量

### 重大藥物交互作用

| 交互作用藥物 | 嚴重程度 | 來源 |
|-------------|---------|------|
| Deferiprone | 重大 | DDInter |
| Irinotecan | 重大 | DDInter |
| Leflunomide | 重大 | DDInter |
| Natalizumab | 重大 | DDInter |
| Adalimumab | 重大 | DDInter |
| Infliximab | 重大 | DDInter |
| Etanercept | 重大 | DDInter |
| Fingolimod | 重大 | DDInter |
| Apalutamide | 重大 | DDInter |

### 藥理學標靶

| 標靶 | 基因名稱 | 說明 |
|-----|---------|------|
| TROP-2 (tumor associated calcium signal transducer 2) | TACSTD2 | Sacituzumab govitecan 的抗體部分與 TROP-2 結合 |

### 重要警語

- **嚴重中性粒細胞減少症**：可能導致發熱性中性粒細胞減少症
- **嚴重腹瀉**：SN-38 可引起嚴重腹瀉
- **過敏反應**：輸注相關反應
- **UGT1A1 多型性**：UGT1A1*28 同型合子患者可能有更高毒性風險

## 結論與下一步

**決策：Hold**

**理由：**
1. 預測適應症（藥物誘發性骨質疏鬆症）與藥物作用機轉缺乏生物學合理性
2. 無臨床試驗或文獻證據支持
3. 作為細胞毒性藥物，用於非惡性疾病的安全性堪慮
4. 成本效益比不適合骨質疏鬆症適應症

**若要推進需要：**
- 發現 Trop-2 在骨代謝中的相關作用
- 基礎研究證明機轉合理性
- 考慮到毒性，此適應症不建議進一步探索

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

