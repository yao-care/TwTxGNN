---
layout: default
title: Norethindrone Enanthate
parent: 僅模型預測 (L5)
nav_order: 197
evidence_level: L5
indication_count: 10
---

# Norethindrone Enanthate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Norethindrone enanthate：從抑制排卵（許可證已註銷）到抗凝血酶缺乏症第 2 型

<!-- review:begin norethindrone-enanthate-historic-license-title-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「# Norethindrone enanthate：從（原適應症資料缺漏）到抗凝血酶缺乏症第 2 型」。台灣曾核發衛署藥輸字第013079號「能無妊注射劑」（NORISTERAT，主成分 norethindrone enantate），適應症為「抑制排卵」，已於 1991-06-07 註銷；目前沒有有效許可證。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end norethindrone-enanthate-historic-license-title-2026-10-16 -->

## 一句話總結

Norethindrone enanthate 是一種長效注射型黃體素（progestin）酯類藥物，台灣曾核發的許可證（衛署藥輸字第013079號「能無妊注射劑」，已於 1991-06-07 註銷）適應症為抑制排卵。
TxGNN 模型預測分數最高的新適應症是**第 2 型抗凝血酶缺乏症 (Antithrombin deficiency type 2)**，但目前**沒有任何臨床試驗，也沒有直接相關文獻**支持。
此預測僅來自模型推論，屬於證據等級 L5。

<!-- review:begin norethindrone-enanthate-historic-license-summary-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「本次資料中未取得台灣許可證所載的原適應症。」。台灣曾核發衛署藥輸字第013079號「能無妊注射劑」（NORISTERAT，主成分 norethindrone enantate），適應症為「抑制排卵」，已於 1991-06-07 註銷；目前沒有有效許可證。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end norethindrone-enanthate-historic-license-summary-2026-10-16 -->

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抑制排卵（衛署藥輸字第013079號「能無妊注射劑」，已於 1991-06-07 註銷） |
| 預測新適應症 | 第 2 型抗凝血酶缺乏症 (Antithrombin deficiency type 2) |
| TxGNN 預測分數 | 98.93% |
| 證據等級 | L5 |
| 台灣上市 | 未上市 |
| 許可證數 | 1 張（有效單方 0／有效複方 0／已註銷 1） |
| 建議決策 | Hold |

<!-- review:begin norethindrone-enanthate-historic-license-2026-10-03 -->

> **查核加註（2026-10-03）**：台灣曾核發衛署藥輸字第013079號「能無妊注射劑」（Noristerat），適應症為抑制排卵，已於 1991-06-07 註銷；目前沒有有效許可證。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end norethindrone-enanthate-historic-license-2026-10-03 -->

<!-- review:begin norethindrone-enanthate-historic-license-row-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「原適應症／無資料（台灣無許可證）」。台灣曾核發衛署藥輸字第013079號「能無妊注射劑」（NORISTERAT，主成分 norethindrone enantate），適應症為「抑制排卵」，已於 1991-06-07 註銷；目前沒有有效許可證。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end norethindrone-enanthate-historic-license-row-2026-10-16 -->

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Norethindrone enanthate 屬於黃體素類藥物，一般作為長效注射避孕劑使用。

坦白說，這個預測在機轉上**缺乏支持**。黃體素酯類並不會調節抗凝血酶的功能，而外源性黃體素在血栓傾向（thrombophilia）患者中，反而通常被視為需要考量的血栓風險。這項關聯很可能只是知識圖譜中與凝血相關基因的網路鄰近性所造成的結果。

排名前 10 的預測還包括念珠菌感染、肝素輔因子 2 缺乏症、類風濕性關節炎、痲瘋病、心臟腫瘤、心血管疾病、漿細胞骨髓瘤等。其中數項（如第 5 因子過量伴自發性血栓、血栓傾向、抗凝血酶缺乏）與藥物本身的血栓風險方向相反，更應視為安全性疑慮而非治療機會。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對排名第 1 的預測（第 2 型抗凝血酶缺乏症），目前無相關文獻。

以下為排名第 8 預測（心血管疾病）下檢索到的文獻，僅供參考。內容多為避孕使用時的心血管與代謝安全性，並非治療效益證據：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1533383](https://pubmed.ncbi.nlm.nih.gov/1533383/) | 1992 | Cohort | Horm Metab Res | 比較兩種長效注射避孕劑（DMPA 與 norethisterone oenanthate）使用一年對血清及脂蛋白脂質的影響 |
| [1424623](https://pubmed.ncbi.nlm.nih.gov/1424623/) | 1992 | Cohort | Contraception | 56 位長期使用者與 30 位非使用者比較，三酸甘油酯、總膽固醇、LDL 與 VLDL 無顯著差異，HDL 平均值有顯著降低 |
| [2967589](https://pubmed.ncbi.nlm.nih.gov/2967589/) | 1987 | Review | Wien Med Wochenschr | 探討長效黃體素注射劑的作用方式、適應症、禁忌症與優缺點，適用於不宜使用雌激素複方者 |
| [4011568](https://pubmed.ncbi.nlm.nih.gov/4011568/) | 1985 | Review | The Practitioner | 荷爾蒙避孕方法概述（無摘要） |
| [6434228](https://pubmed.ncbi.nlm.nih.gov/6434228/) | 1984 | Case series | Contraception | 系統性紅斑狼瘡患者使用黃體素避孕：norethisterone enanthate 與 levonorgestrel 組的疾病活動發作與對照組相比無顯著差異 |
| [5351331](https://pubmed.ncbi.nlm.nih.gov/5351331/) | 1969 | Case series | Dtsch Med Wochenschr | 長效注射避孕劑使用期間的觀察研究（無摘要） |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Norethindrone Enanthate 的不重複許可證共 **1 張**：有效單方 0 張、有效複方 0 張、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第013079號</td><td>能無妊注射劑</td><td>NORETHINDRONE ENANTATE (NORETHISTERONE ENANTHATE)</td><td>1991/06/07</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **血栓風險**：預測清單中多項疾病（血栓傾向、第 5 因子相關血栓、抗凝血酶與肝素輔因子 2 缺乏）屬於血栓傾向族群，荷爾蒙避孕劑在此類患者中通常需特別留意血栓風險。
- **脂質代謝**：現有文獻顯示長期使用者的 HDL 有降低的現象。

其餘警語、禁忌症與藥物交互作用資料不足，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有臨床試驗與直接文獻，機轉上也缺乏合理連結，且與藥物的血栓風險方向相矛盾。
- 台灣目前無許可證，且安全性與作用機轉資料不完整。

**若要推進需要：**
- 補齊 TFDA 仿單的警語與禁忌症，以及 DrugBank 的作用機轉資料
- 確認該藥物在凝血相關疾病患者中的血栓風險評估
- 以文獻系統性檢索確認是否有任何臨床或前臨床證據支持此適應症
- 若要重新排序候選適應症，建議優先評估機轉上較合理、且不涉及血栓風險的項目

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「台灣上市：未上市」 | 加註（2026-10-15 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 標題寫原適應症資料缺漏 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 一句話總結稱未取得台灣許可證所載的原適應症 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 原適應症寫無資料、台灣無許可證 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

