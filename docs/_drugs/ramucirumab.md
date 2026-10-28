---
layout: default
title: Ramucirumab
parent: 僅模型預測 (L5)
nav_order: 239
evidence_level: L5
indication_count: 10
monitor_inn: "Ramucirumab"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "cervical adenosquamous carcinoma, glassy cell variant", "uterine ligament endometrioid adenocarcinoma", "uterine ligament clear cell adenocarcinoma", "uterine ligament mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-10-29
description: "Ramucirumab：預測新適應症為子宮韌帶腺癌 (Uterine Ligament Adenocarcinoma)（證據等級 L5）。原適應症：胃癌：與 paclitaxel 併用…"
---

# Ramucirumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Ramucirumab：從胃癌到子宮韌帶腺癌
{: .text-alpha }

## 一句話總結

Ramucirumab 是一種 VEGFR-2 拮抗型單株抗體，原本用於治療晚期胃癌、非小細胞肺癌、大腸直腸癌與肝細胞癌。
TxGNN 模型預測它可能對**子宮韌帶腺癌 (Uterine Ligament Adenocarcinoma)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃癌：與 paclitaxel 併用，或單一藥物用於接受過 fluoropyrimidine 和 platinum 化學治療後仍惡化之晚期或轉移性胃腺癌（或胃食道接合處腺癌） |
| 預測新適應症 | 子宮韌帶腺癌 (Uterine Ligament Adenocarcinoma) |
| TxGNN 預測分數 | 0.9995 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效單方 1／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ramucirumab 是針對 VEGFR-2 的單株抗體，能阻斷 VEGF 驅動的腫瘤血管新生。原適應症皆為實體腫瘤（胃腺癌、肺癌、大腸直腸癌、肝細胞癌），其療效與抑制腫瘤血管新生有關。

子宮韌帶腺癌同屬腺癌，若腫瘤依賴 VEGF 訊號促進血管新生，理論上 VEGFR-2 阻斷可能有效。此外，模型同時預測了多種子宮頸及子宮韌帶腺癌亞型（如子宮頸內膜癌、子宮頸腺樣囊性癌、腸型子宮頸黏液腺癌等），顯示預測集中在婦科腺癌這一方向。

但需強調，這些推論僅屬機轉上的合理推測，沒有針對此疾病的臨床或文獻證據，預測完全依賴 TxGNN 分數。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Ramucirumab 的不重複許可證共 **1 張**：有效單方 1 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部菌疫輸字第000999號 | 欣銳擇 注射劑 | 注射劑 | 台灣禮來股份有限公司 | 2030/12/24 | 1.胃癌： (1)Ramucirumab併用paclitaxel適用於治療正接受或接受過fluoropyrimidine和platinum化學治療仍疾病惡化之晚期或轉移性胃腺癌(或… |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（抗 VEGFR-2 單株抗體），非傳統細胞毒性藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：本報告彙整的資料中共有 127 筆交互作用紀錄。列出的項目多為與出血風險相關的藥物，包括：
  - **嚴重 (Major)**：Acetylsalicylic acid（阿斯匹靈）、Clopidogrel、Cilostazol、Apixaban、Alteplase、Dalteparin、Abciximab、Bivalirudin、Cangrelor、Deferasirox 等
  - **中度 (Moderate)**：Fenfluramine、Dexfenfluramine、Sibutramine

  併用抗凝血或抗血小板藥物時，應特別留意出血風險。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
預測新適應症僅有 TxGNN 模型分數（證據等級 L5），沒有臨床試驗或文獻佐證，且缺乏作用機轉資料。目前不足以支持推進。

**若要推進需要：**
- 補充詳細的作用機轉（MOA）資料
- 搜尋子宮頸／子宮韌帶腺癌中抗 VEGF/VEGFR-2 治療的前臨床與臨床研究
- 評估是否有適合的病患族群與試驗設計（如先行探索性 Phase 2）
- 評估出血、血栓等與抗血管新生藥物相關的安全性，以及與抗凝血藥物併用的風險管理計畫

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證數寫 4 張 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

