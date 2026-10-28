---
layout: default
title: Perindopril
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-29
description: "Perindopril：預測新適應症為惡性高血壓性腎病變 (Malignant Hypertensive Renal Disease)（證據等級 L4）。原適應症：高血壓、充血性心臟衰竭"
monitor_inn: "perindopril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Perindopril
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

## Perindopril：從高血壓到惡性高血壓性腎病變
{: .text-alpha }

## 一句話總結

Perindopril 是一種血管張力素轉化酶（ACE）抑制劑，原本用於治療高血壓、充血性心臟衰竭，並用於有心肌梗塞或血管重建病史者的心臟事件風險降低。
TxGNN 模型預測它可能對**惡性高血壓性腎病變 (Malignant Hypertensive Renal Disease)** 有效。
目前**沒有臨床試驗**，僅有 **1 篇間接相關文獻**，證據仍屬初步的模型預測階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓、充血性心臟衰竭；對於有心肌梗塞及/或血管重建病史的病人，併用傳統心絞痛治療藥物，可降低心臟事件的危險 |
| 預測新適應症 | 惡性高血壓性腎病變 (Malignant Hypertensive Renal Disease) |
| TxGNN 預測分數 | 0.9977 |
| 證據等級 | L5（僅有間接的文獻，無臨床試驗） |
| 台灣上市 | 上市中（有效許可證 12 張／共 24 張） |
| 許可證數 | 24 張（有效單方 8／有效複方 4／已註銷 12） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。不過 perindopril 屬於 ACE 抑制劑，一般認為它能減少血管張力素 II 所引起的血管收縮，並降低腎臟出球小動脈的張力，進而降低腎絲球內壓力。

高血壓與腎臟損傷關係密切：長期高壓會損傷腎臟微血管，而降低腎絲球內壓力理論上有助於減緩腎臟傷害。因此，從機轉上推論，perindopril 可能對高血壓相關的腎病變有幫助。

但需要注意，目前對「惡性」型態（急遽惡化的嚴重高血壓合併器官損傷）並沒有直接證據，所有推論都屬間接。

另外，本次資料中同時預測的其他疾病（惡性腎血管性高血壓、兩類肺動脈高血壓、Braddock 症候群）證據更少，皆僅有模型預測，建議維持在 Hold 狀態。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36382821](https://pubmed.ncbi.nlm.nih.gov/36382821/) | 2022 | 世代研究 | Urologiia | 探討腎癌腎臟切除術後單一腎臟的功能狀態；與本藥的關聯為間接，並非直接評估 perindopril |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Perindopril 的不重複許可證共 **24 張**：有效單方 8 張、有效複方 4 張、已註銷 12 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（8 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第048972號 | 欣脈平錠 4 毫克 | 錠劑 | 優良化學製藥股份有限公司 | 2027/08/17 | 高血壓，充血性心臟衰竭。對於有心肌梗塞及/或血管重建病史得病人，併用傳統心絞痛治療藥物，可以降低心臟事件的危險。 |
| 衛署藥製字第049178號 | 倍立平錠 4 毫克 | 錠劑 | 健喬信元醫藥生技股份有限公司 | 2027/11/29 | 高血壓，充血性心臟衰竭。對於有心肌梗塞及/或血管重建病史的病人，併用傳統心絞痛治療藥物，可以降低心臟事件的危險。 |
| 衛署藥製字第049904號 | 依心舒錠 4 毫克 | 錠劑 | 永信藥品工業股份有限公司 | 2029/01/12 | 高血壓、充血性心臟衰竭。對於有心肌梗塞及/或血管重建病史的病人，併用傳統心絞痛治療藥物，可以降低心臟事件的危險。 |
| 衛署藥製字第054966號 | 脈平穩錠 8 毫克 | 錠劑 | 健喬信元醫藥生技股份有限公司 | 2030/04/30 | 高血壓。充血性心臟衰竭。對於有心肌梗塞及/或血管重建病史的病人，併用傳統心絞痛治療藥物，可以降低心臟事件的危險。 |
| 衛署藥製字第057413號 | 欣脈平錠8毫克 | 錠劑 | 優良化學製藥股份有限公司 | 2027/10/24 | 高血壓、充血性心臟衰竭。對於有心肌梗塞及／或血管重建病史的病人，併用傳統心絞痛治療藥物，可以降低心臟事件的危險。 |
| 衛署藥輸字第024725號 | 雅施達膜衣錠5毫克 | 膜衣錠 | 新加坡商施維雅股份有限公司台灣分公司 | 2027/10/23 | 高血壓、充血性心臟衰竭、對於有心肌梗塞及/或血管重建病史的病人，併用傳統心絞痛治療藥物，可降低心臟事件的危險。 |
| 衛署藥輸字第025596號 | 叔丁胺培林口朵普利 | （粉） | 宇直泰貿易股份有限公司 | 2026/12/30 | 降血壓劑。 |
| 衛署藥輸字第026071號 | 叔丁胺培林哚普利 | （粉） | 鴻傑藥品有限公司 | 2028/06/22 | 降血壓劑。 |

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（4 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第049756號 | 脈利舒複方錠 | INDAPAMIDE、PERINDOPRIL TERT-BUTYLAMINE | 錠劑 | 本態性動脈高血壓。 |
| 衛署藥輸字第025046號 | 雅施達 加強錠 5 毫克/1.25 毫克 | PERINDOPRIL ARGININE、INDAPAMIDE | 膜衣錠 | 本態性高血壓。當perindopril單方無法有效控制血壓時可用雅詩達加強錠 5mg/1.25mg治療。 |
| 衛部藥製字第058573號 | 複倍立平錠 | INDAPAMIDE、PERINDOPRIL TERT-BUTYLAMINE | 錠劑 | 本態性動脈高血壓。 |
| 衛部藥輸字第026653號 | 康復來 5毫克 / 5毫克 | PERINDOPRIL ARGININE、AMLODIPINE BESILATE | 錠劑 | 治療Perindopril每日5mg無法理想控制血壓之高血壓 |

<details><summary><strong>已註銷</strong>（12 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第019238號</td><td>雅施達錠４毫克</td><td>PERINDOPRIL SALIFIED WITH TERT-BUTYLAMINE</td><td>2023/07/14</td></tr><tr><td>衛署藥輸字第019431號</td><td>雅施達錠２公絲</td><td>PERINDOPRIL</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第023757號</td><td>配德利錠</td><td>INDAPAMIDE、PERINDOPRIL TERT-BUTYLAMINE SALT</td><td>2025/07/08</td></tr><tr><td>衛署藥輸字第023758號</td><td>雅施達加強錠</td><td>PERINDOPRIL TERT-BUTYLAMINE SALT、INDAPAMIDE</td><td>2021/08/04</td></tr><tr><td>衛署藥輸字第024108號</td><td>培林多皮爾</td><td>PERINDOPRIL ERBUMINE</td><td>2026/05/22</td></tr><tr><td>衛署藥輸字第024304號</td><td>雅施達錠8毫克</td><td>PERINDOPRIL SALIFIED WITH TERT-BUTYLAMINE</td><td>2021/02/19</td></tr><tr><td>衛署藥輸字第024855號</td><td>雅施達膜衣錠10毫克</td><td>PERINDOPRIL ARGININE</td><td>2021/02/19</td></tr><tr><td>衛署藥輸字第025045號</td><td>配德利 錠 2.5 毫克/0.625 毫克</td><td>PERINDOPRIL ARGININE、INDAPAMIDE</td><td>2021/02/19</td></tr><tr><td>衛署藥輸字第025409號</td><td>貝林達“山德士”4毫克錠</td><td>PERINDOPRIL TERT-BUTYLAMINE</td><td>2018/03/23</td></tr><tr><td>衛部藥製字第058258號</td><td>降壓平順錠8毫克</td><td>PERINDOPRIL TERT-BUTYLAMINE</td><td>2023/07/07</td></tr><tr><td>衛部藥輸字第026990號</td><td>雅康來錠3.5毫克/2.5毫克</td><td>AMLODIPINE BESILATE、PERINDOPRIL ARGININE</td><td>2022/05/04</td></tr><tr><td>衛部藥輸字第026991號</td><td>雅康來 7毫克/5毫克</td><td>AMLODIPINE BESILATE、PERINDOPRIL ARGININE</td><td>2021/05/14</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物－疾病關聯資料，並非仿單文字）：腎臟疾病、肝臟疾病、膽囊疾病、血管性水腫（含後天性、遺傳性及 RAAS 阻斷劑誘發型）、嗜中性白血球低下、顆粒球缺乏症、低血壓性疾病、結締組織疾病、骨疾病、軟骨疾病、腎動脈阻塞、輸尿管積膿。
- **藥物交互作用**：本次共查得 213 筆交互作用，以下為部分例子：
  - 嚴重（Major）：檸檬酸鉀、碳酸氫鉀（高血鉀風險）
  - 中度（Moderate）：糖皮質素類（hydrocortisone、dexamethasone、betamethasone、triamcinolone、budesonide）、降血糖藥（metformin、alogliptin、saxagliptin、canagliflozin、dapagliflozin、empagliflozin、chlorpropamide）、bupropion、morphine、阿斯匹靈、dronabinol、瀉劑類（picosulfuric acid、含電解質的 polyethylene glycol）

此外，對於雙側腎動脈狹窄或單一狹窄腎臟的病人，ACE 抑制劑有急性腎功能惡化的風險，這與預測的腎臟相關適應症特別有關。其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 模型分數很高，但目前沒有任何臨床試驗，唯一的文獻也只是間接相關，且作用機轉資料缺漏。
- 惡性高血壓合併腎病變屬高風險族群，而 ACE 抑制劑本身有腎功能與高血鉀的風險，在缺乏直接證據前不宜推進。

**若要推進需要：**
- 補齊 perindopril 的作用機轉資料（DrugBank）
- 系統性搜尋 ACE 抑制劑用於惡性高血壓／高血壓性腎病變的臨床與觀察性研究
- 評估腎功能惡化、高血鉀與血管性水腫的風險管理計畫
- 若有初步證據，再設計小規模前瞻性研究，並先確認適用族群與排除條件
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

