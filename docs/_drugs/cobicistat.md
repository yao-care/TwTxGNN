---
layout: default
title: Cobicistat
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 3
monitor_inn: "Cobicistat"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-23
description: "Cobicistat：預測新適應症為貓後天免疫缺乏症候群 (feline acquired immunodeficiency syndrome)（證據等級 L5）。原適應症：感染第一型人類免疫缺乏病毒（HIV-1）"
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

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Cobicistat：從 HIV-1 感染到貓後天免疫缺乏症候群
{: .text-alpha }

## 一句話總結

Cobicistat 是一種藥物動力學增強劑（CYP3A 抑制劑），在台灣僅以複方形式核准，用於治療 HIV-1 感染。
TxGNN 模型預測它可能對**貓後天免疫缺乏症候群 (feline acquired immunodeficiency syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 感染第一型人類免疫缺乏病毒（HIV-1）（僅有複方許可證，無單方許可證） |
| 預測新適應症 | 貓後天免疫缺乏症候群 (feline acquired immunodeficiency syndrome) |
| TxGNN 預測分數 | 0.9992 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效單方 0／有效複方 3／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Cobicistat 是機轉型 CYP3A 抑制劑，本身沒有抗 HIV 活性，作用是提高併用抗反轉錄病毒藥物的血中濃度。

貓免疫缺乏病毒（FIV）與 HIV-1 同屬慢病毒，因此模型預測在機轉上有些許關聯。但這種關聯只能建立在「作為增強劑搭配其他抗病毒藥物」的前提上，單用 Cobicistat 不具抗病毒作用。目前沒有任何獸醫領域的證據。

另外兩個預測（猴免疫缺乏病毒感染、一種罕見的神經發展障礙）同樣為 L5。前者是動物模型而非人類治療適應症；後者與 CYP3A 抑制沒有明顯機轉關聯，高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Cobicistat 的不重複許可證共 **3 張**：有效單方 0 張、有效複方 3 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（3 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛部藥輸字第027001號 | 捷扶康 膜衣錠 | tenofovir alafenamide fumarate、cobicistat、elvitegravir、EMTRI… | 膜衣錠 | 下列感染第一型人類免疫缺乏病毒(HIV-1)且不具已知與嵌入酶抑制劑類藥品、emtricitabine或tenofovir抗藥性相關的突變的病人： (1) 12歲(含)以上且體重至… |
| 衛部藥輸字第027263號 | 普澤力膜衣錠 | DARUNAVIR ETHANOLATE、cobicistat | 膜衣錠 | 適用於與其他抗反轉錄病毒藥物併用，以治療 未曾接受治療及曾經接受治療且未發生darunavir抗藥性 相關取代（V11I、V32I、L33F、I47V、I50V、I54L、I54M… |
| 衛部藥輸字第027613號 | 信澤力膜衣錠 | EMTRICITABINE、DARUNAVIR ETHANOLATE、cobicistat、tenofovir alaf… | 膜衣錠 | SYMTUZA 為一個完整治療配方，適用於治療下列感染人類免疫不全病毒第1 型（HIV-1）的成人患者以及體重至少40公斤的兒童病人： ● 先前無任何抗反轉錄病毒藥物治療紀錄，或… |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：共查得 420 筆交互作用紀錄。部分列舉如下：
  - 嚴重（Major）：Loperamide、Triamcinolone、Cisapride、Budesonide
  - 中度（Moderate）：Hydrocortisone、Aprepitant、Betamethasone、Dexamethasone、Clarithromycin、Repaglinide、Metoclopramide 等
  - 輕微（Minor）：Prucalopride

  這些多與 CYP3A 抑制導致併用藥物濃度上升有關，使用前需逐一審視併用藥物。

其餘警語與禁忌症資料請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型，沒有任何臨床試驗或文獻直接支持，證據等級為 L5。
- Cobicistat 本身無抗病毒活性，且預測的新適應症為動物疾病，不屬於人類藥物再利用的直接範圍。

**若要推進需要：**
- 取得 Cobicistat 的作用機轉資料
- 搜尋並確認有無 FIV 的獸醫體外或動物研究
- 釐清是否有合適的搭配抗病毒藥物，以及獸醫使用的法規與安全性路徑
- 確認 TxGNN 模型（深度學習）的高分是否僅反映模型學到的相關疾病之間的相似性，而非生物學證據，必要時以其他方法交叉驗證
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

