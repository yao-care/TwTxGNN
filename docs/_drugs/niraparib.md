---
layout: default
title: Niraparib
parent: 中證據等級 (L3-L4)
nav_order: 193
evidence_level: L3
indication_count: 10
---

# Niraparib
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Niraparib：從卵巢癌到囊性腫瘤（Cystic Neoplasm）

## 一句話總結

Niraparib 是一種口服 PARP 抑制劑，原本用於卵巢癌（含輸卵管癌、原發性腹膜癌）的維持治療。
TxGNN 模型預測它可能對**囊性腫瘤 (Cystic Neoplasm)** 有效，
目前有 **3 個臨床試驗**（均為相關的子宮內膜癌研究，其中 1 項已終止、1 項撤回）和 **10 篇文獻**，但多數為間接證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 晚期卵巢癌之第一線維持治療；復發性卵巢癌之維持治療（對含鉑化療有完全或部分反應的表皮卵巢癌、輸卵管腫瘤或原發性腹膜癌成年病人） |
| 預測新適應症 | 囊性腫瘤 (Cystic Neoplasm) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 4 張（有效單方 1／有效複方 2／已註銷 1） |
| 建議決策 | Hold（列為研究問題，待更具體的疾病定義與證據） |

> 說明：預測清單中排名第 1 的是「會厭腫瘤」，但其僅有模型預測、無任何試驗或文獻（L5）。本報告改以證據最完整的第 2 名「囊性腫瘤」為主軸，並於結論中說明。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位未收錄）。就一般藥理認知，Niraparib 為 PARP1/2 抑制劑，可使 DNA 修復受損，並將 PARP 困在 DNA 上，在同源重組缺陷（HRD）的腫瘤中產生合成致死效應。

原適應症卵巢癌中，高惡性度漿液性卵巢癌常屬 HRD 腫瘤，在組織學上屬於漿液性／囊性腫瘤類別。因此模型把 Niraparib 與「囊性腫瘤」連結，有一定的合理性。

不過需要注意，現有相關證據集中在婦科漿液性癌（如子宮內膜漿液性癌、子宮漿液性癌），而非明確定義的「囊性腫瘤」本身。這個預測目前較像是對「HRD 相關漿液性腫瘤」的間接支持，而非對該疾病實體的直接驗證。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04716686](https://clinicaltrials.gov/study/NCT04716686) | Phase 2 | 招募中 | 83 | Niraparib 單藥用於子宮內膜漿液性癌的維持與復發治療；尚無結果 |
| [NCT04159155](https://clinicaltrials.gov/study/NCT04159155) | Phase 2/3 | 已終止 | 11 | 漿液性或 p53 突變子宮內膜癌的多組別前線與維持治療試驗（含 Niraparib）；僅收 11 人，難以解讀療效 |
| [NCT05289648](https://clinicaltrials.gov/study/NCT05289648) | Early Phase 1 | 已撤回 | 0 | 術前使用 Niraparib 於高惡性度子宮內膜癌的探索性研究；未收案，無資料 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40702505](https://pubmed.ncbi.nlm.nih.gov/40702505/) | 2025 | Cohort | Journal of Ovarian Research | 建立高惡性度漿液性卵巢癌的幹細胞相關亞型與預後模型 |
| [41323499](https://pubmed.ncbi.nlm.nih.gov/41323499/) | 2025 | Cohort | Pathology Oncology Research | 以 FoundationOne CDx 的 HRD 檢測引導卵巢癌 PARP 抑制劑用藥建議 |
| [40473279](https://pubmed.ncbi.nlm.nih.gov/40473279/) | 2025 | 試驗計畫書 | BMJ Open | Niraparib 用於子宮漿液性癌維持治療的 Phase 2 試驗設計 |
| [42157333](https://pubmed.ncbi.nlm.nih.gov/42157333/) | 2026 | Cohort | Clinical Epigenetics | 以 HRR 基因啟動子甲基化建立預測 PARP 抑制劑療效的列線圖 |
| [42442041](https://pubmed.ncbi.nlm.nih.gov/42442041/) | 2026 | Cohort | Gynecologic Oncology | 探討 BRCA 野生型高惡性度漿液性癌的 HRD 檢測與 MYC 擴增作為替代標記 |
| [31466953](https://pubmed.ncbi.nlm.nih.gov/31466953/) | 2019 | Case report | BMJ Case Reports | Niraparib 用於卵巢癌合併腦轉移病人的維持治療 |
| [34321239](https://pubmed.ncbi.nlm.nih.gov/34321239/) | 2021 | 體外／PDX 研究 | Cancer Research | RAD51C 啟動子甲基化喪失導致 PARP 抑制劑抗藥性 |
| [41520277](https://pubmed.ncbi.nlm.nih.gov/41520277/) | 2026 | 體外研究 | Cancer Biology & Therapy | 以球體與類器官評估 Carboplatin 合併 PARP 抑制劑的效果 |
| [41465250](https://pubmed.ncbi.nlm.nih.gov/41465250/) | 2025 | 體外研究 | Int J Mol Sci | PARP 抑制劑在高惡性度漿液性卵巢癌細胞中的蛋白質體多重藥理效應 |
| [41214101](https://pubmed.ncbi.nlm.nih.gov/41214101/) | 2025 | 體外研究 | Scientific Reports | Claudin-4 同時調控高惡性度漿液性癌的基因體穩定性與免疫逃避 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Niraparib 的不重複許可證共 **4 張**：有效單方 1 張、有效複方 2 張、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第028651號 | 截永樂錠100毫克 | 膜衣錠 | 台灣武田藥品工業股份有限公司 | 2029/02/28 | １、晚期卵巢癌之第一線維持治療：用於對第一線含鉑化療有完全或部分反應的晚期表皮卵巢癌、輸卵管腫瘤或原發性腹膜癌成年病人之維持治療。 ２、復發性卵巢癌之維持治療：用於對含鉑化療有完全… |

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（2 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛部藥輸字第028616號 | 澤截膜衣錠100/500毫克 | Abiraterone Acetate、Niraparib tosylate monohydrate | 膜衣錠 | 與prednisone 或prednisolone 併用，用於： １、與雄性素去除療法併用，治療具BRCA1/2 (遺傳性及/或體細胞)致病性或疑似致病性突變的轉移性去勢敏感性前列… |
| 衛部藥輸字第028617號 | 澤截膜衣錠50/500毫克 | Niraparib tosylate monohydrate、Abiraterone Acetate | 膜衣錠 | 與prednisone 或prednisolone 併用，用於： １、與雄性素去除療法併用，治療具BRCA1/2 (遺傳性及/或體細胞)致病性或疑似致病性突變的轉移性去勢敏感性前列… |

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛部藥輸字第027764號</td><td>截永樂膠囊</td><td>Niraparib tosylate monohydrate</td><td></td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（PARP 抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單（一般需監測血液學參數，如 CBC） |
| 處置防護 | 請參考原廠仿單與院內抗腫瘤藥物處置規範 |

## 安全性考量

- **藥物交互作用**：資料庫共收錄 351 筆交互作用。列出的項目中，屬 **Major** 的有 Deferiprone、Samarium (153Sm) lexidronam；其餘多為 Moderate，包括：
  - 抗凝血／抗血小板類：Acetylsalicylic acid、Apixaban、Dipyridamole、Cilostazol、Cangrelor、Abciximab、Alteplase 等
  - 放射性藥物類：Iobenguane (I-131)、Ibritumomab tiuxetan、Tositumomab、Strontium chloride Sr-89
  - 其他：Rolapitant、Palifermin

主要警語與禁忌症的資料目前缺漏，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 「囊性腫瘤」並非明確定義的疾病實體，現有試驗與文獻多是針對子宮內膜／子宮漿液性癌及卵巢漿液性癌的間接證據。3 項試驗中，1 項仍在招募且無結果，1 項提早終止（僅 11 人），1 項撤回（0 人），尚無可解讀的療效數據。
- 證據等級為 L3，較合適的定位是「研究問題」，而非可直接推進的適應症。
- 預測排名第 1 的「會厭腫瘤」及其餘多數預測（良性腫瘤、神經母細胞瘤等）僅有模型分數，無任何研究支持，且對良性腫瘤使用 PARP 抑制劑的風險效益不佳，均建議維持 Hold。

**若要推進需要：**
- 釐清「囊性腫瘤」的具體病理定義，並聚焦於 HRD 陽性的漿液性腫瘤亞型
- 等待 NCT04716686 的結果，並追蹤子宮漿液性癌 Phase 2 計畫（BMJ Open）的進展
- 補齊 Niraparib 的作用機轉資料（DrugBank MOA）
- 取得仿單的警語與禁忌症，並評估血液學毒性監測計畫與抗凝血類藥物的交互作用管理

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「原適應症」只寫 mCRPC | 報告重生後已無此錯誤（2026-10-15：新報告「原適應症」列為 niraparib 單方許可證的卵巢癌維持治療；原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

