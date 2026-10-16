---
layout: default
title: Dexketoprofen
parent: 高證據等級 (L1-L2)
nav_order: 85
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-16
description: "Dexketoprofen：預測新適應症為偏頭痛 (Migraine Disorder)（證據等級 L1）。原適應症：治療輕度至中等強度疼痛症狀，如肌肉骨骼疼痛、經痛、牙痛"
---

# Dexketoprofen
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Dexketoprofen：從輕中度疼痛到偏頭痛

## 一句話總結

Dexketoprofen（克痛停）是一種非類固醇消炎止痛藥（NSAID），原本用於肌肉骨骼疼痛、經痛、牙痛等輕至中度疼痛。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，
目前有 **5 個臨床試驗**和 **20 篇文獻**支持這個方向，其中包含 1 篇隨機對照試驗的統合分析。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 治療輕度至中等強度疼痛症狀，如肌肉骨骼疼痛、經痛、牙痛 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L1 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 2 張（有效單方 1／有效複方 1／已註銷 0） |
| 建議決策 | Proceed with Guardrails |

> 說明：預測清單中排名第 1 的是肌腱炎（證據僅 L4），但證據最完整的是第 6 名的偏頭痛，因此本報告以偏頭痛為主要評估對象。同屬頭痛類的「頭痛疾患」(Headache Disorder，L2) 亦有延伸支持。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Dexketoprofen 屬於 NSAID，作用為抑制環氧化酶（COX-1/COX-2），減少前列腺素合成，進而降低發炎與疼痛訊號。

偏頭痛發作時，神經性發炎與疼痛訊號傳遞扮演重要角色，前列腺素參與其中。原適應症同為疼痛症狀，因此機轉上合理推測它可緩解偏頭痛發作的頭痛。

臨床上也有直接證據：多項隨機試驗（包含安慰劑對照）與一篇 RCT 統合分析探討了 dexketoprofen 對急性偏頭痛的效果。另有研究探討它與 frovatriptan（一種 triptan）併用的效果。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02159547](https://clinicaltrials.gov/study/NCT02159547) | Phase 4 | 完成 | 224 | 急診中靜脈注射 dexketoprofen 對比安慰劑，檢驗能否終止偏頭痛發作 |
| [NCT01730326](https://clinicaltrials.gov/study/NCT01730326) | Phase 4 | 完成 | 200 | 急診中靜脈 dexketoprofen 對比 paracetamol，治療急性偏頭痛頭痛 |
| [NCT04252521](https://clinicaltrials.gov/study/NCT04252521) | NA | 完成 | 150 | 靜脈 metoclopramide、dexketoprofen trometamol 及兩者併用的雙盲隨機試驗 |
| [NCT04533568](https://clinicaltrials.gov/study/NCT04533568) | Phase 4 | 完成 | 160 | 靜脈 ibuprofen 對比靜脈 dexketoprofen，治療無預兆偏頭痛相關頭痛 |
| [NCT04372264](https://clinicaltrials.gov/study/NCT04372264) | Phase 4 | 未知 | 210 | 靜脈 paracetamol、dexketoprofen、ibuprofen 對疼痛視覺類比量表（VAS）的影響 |

以上試驗摘要僅呈現設計與比較對象，登錄資料中未提供結果數據。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31725614](https://pubmed.ncbi.nlm.nih.gov/31725614/) | 2019 | 統合分析 | Medicine | 以 RCT 統合分析評估 dexketoprofen 相對安慰劑對偏頭痛疼痛控制的效果 |
| [24412801](https://pubmed.ncbi.nlm.nih.gov/24412801/) | 2014 | RCT | The Journal of Pain | Phase II 雙盲交叉安慰劑對照試驗，比較 25 mg、50 mg dexketoprofen 與安慰劑（93 位患者） |
| [25944813](https://pubmed.ncbi.nlm.nih.gov/25944813/) | 2016 | RCT | Cephalalgia | 急診中靜脈 dexketoprofen 對比安慰劑，評估終止偏頭痛的效果 |
| [24394884](https://pubmed.ncbi.nlm.nih.gov/24394884/) | 2014 | RCT | Emerg Med J | 急診中靜脈 paracetamol 與 dexketoprofen 治療急性偏頭痛的比較 |
| [32359776](https://pubmed.ncbi.nlm.nih.gov/32359776/) | 2020 | RCT | Am J Emerg Med | 靜脈 metoclopramide、dexketoprofen trometamol 及併用的止痛效果與安全性 |
| [34085549](https://pubmed.ncbi.nlm.nih.gov/34085549/) | 2021 | RCT | Ann Saudi Med | 皮內美容療法與靜脈 dexketoprofen 治療無預兆偏頭痛的比較 |
| [24363238](https://pubmed.ncbi.nlm.nih.gov/24363238/) | 2014 | RCT | Cephalalgia | Frovatriptan 加 dexketoprofen（25 或 37.5 mg）對比單用 frovatriptan |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | 指引／回顧 | Headache | 美國頭痛學會 2025 年急診偏頭痛注射藥物指引更新 |
| [37291500](https://pubmed.ncbi.nlm.nih.gov/37291500/) | 2023 | 網絡統合分析 | BMC Neurol | 比較 metoclopramide 與其他偏頭痛藥物的療效與安全性 |
| [25056381](https://pubmed.ncbi.nlm.nih.gov/25056381/) | 2014 | 回顧 | Expert Rev Neurother | Frovatriptan 與 dexketoprofen 治療急性偏頭痛的療效與耐受性 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Dexketoprofen 的不重複許可證共 **2 張**：有效單方 1 張、有效複方 1 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第026487號 | 克痛停錠25毫克 | 膜衣錠 | 裕利股份有限公司 | 2030/03/26 | 治療輕度至中等強度疼痛症狀，如肌肉骨骼疼痛、經痛、牙痛。 |

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（1 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛部藥輸字第027628號 | 舒宜達膜衣錠75毫克/25毫克 | Dexketoprofen trometamol、TRAMADOL HCL | 膜衣錠 | 須使用dexketoprofen及tramadol合併療法之成人中度至重度急性疼痛短期治療 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

安全性資訊請參考原廠仿單。

作為 NSAID，一般應留意胃腸道、腎臟與心血管風險，但這些屬藥物類別的通則，本次資料中並無 dexketoprofen 特定的警語、禁忌或交互作用資料。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 偏頭痛有多個 Phase 4 試驗（含安慰劑對照）、多篇 RCT 及一篇 RCT 統合分析支持，證據明顯強於其他預測適應症。
- 試驗多為土耳其急診的「靜脈注射」劑型，而台灣核准的是口服膜衣錠，劑型與給藥途徑尚需確認。目前也缺乏作用機轉與安全性的完整資料。

**若要推進需要：**
- 詳讀統合分析與各 RCT 的結果數據，確認療效幅度與疼痛緩解的時間點
- 評估口服劑型（台灣已核准劑型）治療偏頭痛的證據，並確認劑量
- 補充作用機轉資料（目前為缺口）與完整仿單的警語、禁忌及藥物交互作用
- 確認申請新適應症的法規路徑與目標族群
- 其他預測適應症（如肌腱炎 L4，纖維肌痛、類風濕性關節炎等 L5）證據不足，建議暫列 Hold 或僅作為研究問題
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

