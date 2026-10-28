---
layout: default
title: Pitolisant
parent: 僅模型預測 (L5)
nav_order: 219
evidence_level: L5
indication_count: 3
monitor_inn: "Pitolisant"
predicted_indications: ["insomnia (disease)", "attention deficit-hyperactivity disorder", "faciodigitogenital syndrome"]
last_modified_at: 2026-10-29
description: "Pitolisant：預測新適應症為失眠 (Insomnia)（證據等級 L4）。原適應症：1、治療 6 歲以上猝睡症（伴隨或未伴隨猝倒現象）的病人。2、改善患有 OSA 成人病人的覺醒狀態並減少日間過度嗜睡（EDS）…"
---

# Pitolisant
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

## Pitolisant：失眠 (Insomnia)
{: .text-alpha }

## 一句話總結

Pitolisant 是一種組織胺 H3 受體拮抗劑／反向促效劑，原本用於治療猝睡症及阻塞性睡眠呼吸中止（OSA）病人的日間過度嗜睡。
TxGNN 模型預測它可能對**失眠 (Insomnia)** 有效，但目前**沒有臨床試驗**，也沒有直接針對失眠的研究；現有文獻都圍繞在嗜睡症狀。
此預測的藥理方向與失眠治療需求相反，證據薄弱，應視為待驗證的研究問題。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 1、治療 6 歲以上猝睡症（伴隨或未伴隨猝倒現象）的病人。2、改善患有 OSA 成人病人的覺醒狀態並減少日間過度嗜睡（EDS），這些病人的 EDS 無法透過 CPAP 等 OSA 主要治療方式得到滿意成果或無法耐受。 |
| 預測新適應症 | 失眠 (Insomnia) |
| TxGNN 預測分數 | 0.9971 |
| 證據等級 | L5（僅有機轉與綜述文獻，無失眠相關臨床試驗） |
| 台灣上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效單方 2／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據文獻，pitolisant 是選擇性組織胺 H3 受體反向促效劑，能提高腦內組織胺的釋放，增強促醒的神經傳導。

這正是預測的問題所在：失眠需要的是降低覺醒，而 pitolisant 的作用是促進覺醒，方向相反。現有證據都針對猝睡症與 OSA 的日間嗜睡，並非失眠本身。TxGNN 模型（深度學習）給出的分數很高，但這個分數來自模型，可能反映模型學到的相關疾病之間的相似性，而非生物學證據，也不代表治療方向一致。

文獻中雖提到組織胺系統與失眠有關（例如 H1 拮抗劑 doxepin 用於改善失眠），但那是另一類受體機轉，不能直接推論到 pitolisant。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下文獻與 pitolisant 及睡眠疾病相關，但**沒有一篇直接評估失眠**：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | RCT | The Lancet Neurology | 第 3 期研究，評估 pitolisant 用於 6 歲以上猝睡症兒童的安全性與療效 |
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | RCT | Chest | 評估 pitolisant 用於持續使用 CPAP 後仍有日間嗜睡的 OSA 病人 |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | RCT | Am J Respir Crit Care Med | 評估 pitolisant 用於拒絕 CPAP 的中重度 OSA 病人之日間嗜睡 |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | Cohort | Revista de neurologia | 真實世界 WAKE 研究，探討 pitolisant 用於先前治療無效的第一型猝睡症 |
| [41588264](https://pubmed.ncbi.nlm.nih.gov/41588264/) | 2026 | Cohort | Neurological Sciences | 中國兒童猝睡症的真實世界回溯研究（40 名病人） |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Des Devel Ther | 回顧 pitolisant 用於猝睡症的設計、開發與治療定位 |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Review | Current Neuropharmacology | 討論神經精神疾病中的組織胺系統變化，提及 pitolisant 與 doxepin |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Review | Handbook of Clinical Neurology | 組織胺受體、促效劑與拮抗劑在健康與疾病中的角色 |
| [42525367](https://pubmed.ncbi.nlm.nih.gov/42525367/) | 2026 | Review | Neurology and Therapy | 兒童睡眠疾病的現行與新興療法 |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Review | Clinical Neuropharmacology | pitolisant 作為青少年猝睡症合併難治性嗜睡的替代刺激劑 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Pitolisant 的不重複許可證共 **2 張**：有效單方 2 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第028103號 | 唯醒膜衣錠4.5毫克 | 膜衣錠 | 信東生技股份有限公司 | 2031/07/13 | 1、治療6歲以上猝睡症(伴隨或未伴隨猝倒現象)的病人。 2、改善患有阻塞性睡眠呼吸中止 (OSA)成人病人的覺醒狀態並減少日間過度嗜睡(EDS)，這些病人的EDS無法透過如持續性呼… |
| 衛部藥輸字第028104號 | 唯醒膜衣錠18毫克 | 膜衣錠 | 信東生技股份有限公司 | 2031/07/13 | １、治療6歲以上猝睡症(伴隨或未伴隨猝倒現象)的病人。 ２、改善患有阻塞性睡眠呼吸中止 (OSA)成人病人的覺醒狀態並減少日間過度嗜睡(EDS)，這些病人的EDS無法透過如持續性呼… |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：已查得 196 筆交互作用紀錄，以下列出部分：
  - 嚴重（Major）：Bupropion、Dolasetron
  - 中度（Moderate）：Famotidine、Hydrocortisone、Metformin、Loperamide、Triamcinolone、Morphine、Acetylsalicylic acid、Dexamethasone、Clarithromycin 等

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測的藥理方向與失眠治療相反：pitolisant 是促醒藥物，現有證據只支持猝睡症與 OSA 的日間嗜睡，沒有任何失眠臨床試驗，高分預測不足以支持推進。
- 排名第 2 的注意力不足過動症（ADHD）僅有機轉與綜述文獻支持，排名第 3 的 faciodigitogenital syndrome 則完全沒有證據，兩者皆不足以改變決策。

**若要推進需要：**
- 補齊作用機轉資料，並釐清 TxGNN 高分是否源自路徑相近性而非治療方向
- 先做文獻與機轉層面的重新評估，確認是否有失眠相關的合理假說（例如特定亞型或共病情境）
- 若假說成立，再設計小型探索性臨床研究，並特別評估 pitolisant 可能加重失眠的風險
- 取得完整的仿單警語與禁忌症，並審視上述嚴重交互作用（Bupropion、Dolasetron）的臨床意義

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 唯醒膜衣錠4.5毫克許可證效期 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 唯醒膜衣錠18毫克許可證效期 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

