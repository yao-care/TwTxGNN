---
layout: default
title: Cobicistat
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 3
---

# Cobicistat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Cobicistat：從 HIV-1 感染到猿猴免疫缺乏病毒感染

## 一句話總結

Cobicistat 是一種 CYP3A 抑制劑，在台灣以複方形式用於 HIV-1 感染治療，作為抗反轉錄病毒藥物的藥動學增強劑。
TxGNN 模型預測它可能對**猿猴免疫缺乏病毒感染 (simian immunodeficiency virus infection)** 有效，
但目前**沒有任何臨床試驗與文獻**支持，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 感染第一型人類免疫缺乏病毒（HIV-1）的成人、青少年與兒童病人（目前許可證皆為複方，無單方許可證） |
| 預測新適應症 | 猿猴免疫缺乏病毒感染 (simian immunodeficiency virus infection) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 3 張（有效單方 0／有效複方 3／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Cobicistat 是複方的一部分，是 CYP3A 抑制劑，本身沒有抗病毒活性，用途是提高併用抗反轉錄病毒藥物的血中濃度。

TxGNN 給出高分，可能是因為猿猴免疫缺乏病毒（SIV）與 HIV-1 同屬慢病毒，在知識圖譜中關聯緊密。不過，這比較像是疾病名稱相似造成的圖譜關聯，並非 cobicistat 對 SIV 有直接作用的證據。

SIV 是非人類靈長類的疾病，沒有人類臨床意義。要推進這個預測，只有在動物模型研究中才有意義，而目前沒有任何相關資料。

此外，同一份預測清單中還有「貓後天免疫缺乏症候群」（分數 99.92%，獸醫領域疾病）與「伴有共濟失調步態、無語言及皮質白質減少的神經發展障礙」（分數 99.91%，罕見遺傳疾病）。兩者同樣沒有證據，後者與 CYP3A 抑制之間也看不出合理的機轉關聯，較可能是圖譜運算的假象。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Cobicistat 的不重複許可證共 **3 張**：有效單方 0 張、有效複方 3 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（3 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛部藥輸字第027001號 | 捷扶康 膜衣錠 | tenofovir alafenamide fumarate、cobicistat、EMTRICITABINE、elvi… | 膜衣錠 | 下列感染第一型人類免疫缺乏病毒(HIV-1)且不具已知與嵌入酶抑制劑類藥品、emtricitabine或tenofovir抗藥性相關的突變的病人： (1) 12歲(含)以上且體重至… |
| 衛部藥輸字第027263號 | 普澤力膜衣錠 | cobicistat、DARUNAVIR ETHANOLATE | 膜衣錠 | 適用於與其他抗反轉錄病毒藥物併用，以治療 未曾接受治療及曾經接受治療且未發生darunavir抗藥性 相關取代（V11I、V32I、L33F、I47V、I50V、I54L、I54M… |
| 衛部藥輸字第027613號 | 信澤力膜衣錠 | tenofovir alafenamide fumarate、DARUNAVIR ETHANOLATE、EMTRICIT… | 膜衣錠 | SYMTUZA 為一個完整治療配方，適用於治療下列感染人類免疫不全病毒第1 型（HIV-1）的成人患者以及體重至少40公斤的兒童病人： ● 先前無任何抗反轉錄病毒藥物治療紀錄，或… |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：資料庫共收錄 420 筆交互作用，以下為部分代表性項目：
  - **嚴重 (Major)**：Loperamide、Triamcinolone、Cisapride、Budesonide
  - **中度 (Moderate)**：Hydrocortisone、Aprepitant、Betamethasone、Dexamethasone、Clarithromycin、Repaglinide、Metoclopramide、Clotrimazole 等
  - **輕微 (Minor)**：Prucalopride

  這些交互作用與 cobicistat 抑制 CYP3A 的特性一致，併用時需評估藥物濃度升高的風險。

其他安全性資訊（警語、禁忌症）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 三個預測適應症均無臨床試驗與文獻佐證，證據等級為 L5。
- Cobicistat 本身沒有抗病毒活性，預測的疾病分別屬於非人類靈長類疾病、獸醫疾病與罕見遺傳疾病，缺乏人類臨床意義或合理機轉。

**若要推進需要：**
- 補充詳細的作用機轉資料（MOA）。
- 若有意探討 SIV 相關用途，需有動物模型的前臨床證據；對人類而言，建議將研究重心放在已核准的 HIV-1 藥動學增強用途。
- 針對神經發展障礙的預測，需先確認是否存在任何生物學關聯，否則應視為圖譜假象排除。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

