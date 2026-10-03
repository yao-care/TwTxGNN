---
layout: default
title: Gemcitabine
parent: 高證據等級 (L1-L2)
nav_order: 113
evidence_level: L2
indication_count: 10
---

# Gemcitabine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Gemcitabine：從轉移性大腸直腸癌到女性乳腺癌

## 一句話總結

Gemcitabine 原本用於治療多種癌症，包括非小細胞肺癌、胰臟癌、膀胱癌、乳癌（與 paclitaxel 併用）、卵巢癌與膽道癌。
TxGNN 模型預測它可能對**女性乳腺癌 (female breast carcinoma)** 有效，
目前有 **10 個臨床試驗**和 **12 篇文獻**支持這個方向。

<!-- review:begin gemcitabine-summary-indication-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「Gemcitabine 原本用於治療多種癌症，包括轉移性大腸直腸癌。」。「轉移性大腸直腸癌」取自 bevacizumab（艾法施）許可證；台灣 gemcitabine 核准適應症為非小細胞肺癌、胰臟癌、膀胱癌、乳癌（併用 paclitaxel）、卵巢癌（第二線）與膽道癌。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end gemcitabine-summary-indication-2026-10-03 -->

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 非小細胞肺癌、胰臟癌、膀胱癌、乳癌（與 paclitaxel 併用）、卵巢癌（第二線）、膽道癌 |
| 預測新適應症 | 女性乳腺癌 (female breast carcinoma) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L2 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

<!-- review:begin gemcitabine-original-indication-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「原適應症／轉移性大腸直腸癌」。原寫內容取自 bevacizumab（艾法施，衛部菌疫輸字第001117號）的許可證；已改為台灣 gemcitabine 許可證的核准適應症。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end gemcitabine-original-indication-2026-10-03 -->

<!-- review:begin gemcitabine-breast-rereview-2026-10-03 -->

> **待重審（2026-10-03）**：這筆預測的推論前提與許可證不符，且乳癌（併用 paclitaxel）已是 gemcitabine 的核准適應症（見上方查核更正與加註），已標記待重審；證據等級、文獻與決策在重審完成前不更動。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end gemcitabine-breast-rereview-2026-10-03 -->

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Gemcitabine 是抗癌藥物的一部分，
其成分在轉移性大腸直腸癌中的療效已被證實，機轉上可能適用於女性乳腺癌。

<!-- review:begin gemcitabine-why-premise-2026-10-03 -->

> **查核加註（2026-10-03）**：這句推論的前提與許可證不符：「轉移性大腸直腸癌」是 bevacizumab 的適應症，不是 gemcitabine；而台灣 gemcitabine 許可證本來就核准與 paclitaxel 併用治療特定轉移性乳癌。推論原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end gemcitabine-why-premise-2026-10-03 -->

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06027268](https://clinicaltrials.gov/study/NCT06027268) | Phase 2 | ACTIVE_NOT_RECRUITING | 36 | 測試 trilaciclib、pembrolizumab、gemcitabine 和 carboplatin 在局部晚期不可切除或轉移性三陰性乳腺癌中的組合效果 |
| [NCT00561119](https://clinicaltrials.gov/study/NCT00561119) | Phase 3 | COMPLETED | 326 | 比較 gemcitabine 和 paclitaxel 在轉移性乳腺癌中的維持治療效果 |
| [NCT02139358](https://clinicaltrials.gov/study/NCT02139358) | Phase 1/2 | COMPLETED | 15 | 評估 gemcitabine 與 trastuzumab 和 pertuzumab 在 HER2+ 乳腺癌中的安全性和活性 |
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | COMPLETED | N/A | 比較 gemcitabine 和 paclitaxel 在不可切除的局部復發或轉移性乳腺癌中的效果 |
| [NCT00003540](https://clinicaltrials.gov/study/NCT00003540) | Phase 2 | COMPLETED | 30 | 研究 gemcitabine 在先前接受過 Adriamycin 和 Taxol 治療的轉移性乳腺癌患者中的效果 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | RCT | Breast cancer research and treatment | 研究 mifepristone、carboplatin 和 gemcitabine 在 GR-positive 乳腺癌中的效果 |
| [24824628](https://pubmed.ncbi.nlm.nih.gov/24824628/) | 2015 | RCT | International journal of cancer | 評估 cisplatin 和 gemcitabine 在轉移性三陰性乳腺癌中的第一線療效 |
| [12057039](https://pubmed.ncbi.nlm.nih.gov/12057039/) | 2002 | In vitro | Clinical breast cancer | 研究 gemcitabine 和 trastuzumab 在乳腺和肺癌細胞中的作用 |
| [15685819](https://pubmed.ncbi.nlm.nih.gov/15685819/) | 2004 | Review | Oncology (Williston Park, N.Y.) | 分析 gemcitabine 和 paclitaxel 在轉移性乳腺癌中的療效 |
| [14754469](https://pubmed.ncbi.nlm.nih.gov/14754469/) | 2004 | Review | Clinical breast cancer | 討論 gemcitabine 和 trastuzumab 在 HER2/neu 過度表現的乳腺癌中的組合療效 |

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛署藥輸字第025899號 | 健仕平"山德士"40毫克/毫升注射劑 | 注射劑 | 非小細胞肺癌、胰臟癌、膀胱癌；與 paclitaxel 併用於曾使用過 anthracycline 之局部復發且無法手術切除或轉移性之乳癌；含鉑類藥物治療後復發且間隔至少 6 個月之卵巢癌第二線治療；膽道癌 |

<!-- review:begin gemcitabine-tw-license-table-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「衛部菌疫輸字第001117號／艾法施注射液／注射液劑／轉移性大腸直腸癌、轉移性乳癌、惡性神經膠質瘤、非鱗狀非小細胞肺癌、子宮頸癌、卵巢上皮細胞癌」。「艾法施注射液」主成分是 bevacizumab，不是 gemcitabine；已改列 gemcitabine 許可證。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end gemcitabine-tw-license-table-2026-10-03 -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物 |
| 骨髓抑制風險 | 中度 |
| 致吐性分級 | 中度 |
| 監測項目 | CBC（含分類）、肝腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

- **藥物交互作用**：與 Naltrexone 可能有中度交互作用，與 Levofloxacin 有輕微交互作用。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Gemcitabine 在乳腺癌中的多項臨床試驗顯示出潛在療效，且有多篇文獻支持其在乳腺癌中的應用。

**若要推進需要：**
- 更詳細的作用機轉資料（MOA）
- 特定族群的安全性監測計畫

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「原本用於…包括轉移性大腸直腸癌」 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 原適應症取自 bevacizumab 許可證 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表列 bevacizumab 製劑「艾法施注射液」 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 預測理由「在轉移性大腸直腸癌中的療效已被證實」 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 女性乳腺癌預測標記待重審 | 標記待重審 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

