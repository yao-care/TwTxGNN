---
layout: default
title: Busulfan
parent: 高證據等級 (L1-L2)
nav_order: 49
evidence_level: L2
indication_count: 10
monitor_inn: "Busulfan"
predicted_indications: ["myelodysplastic syndrome", "refractory cytopenia of childhood", "unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "seborrheic keratosis", "simian immunodeficiency virus infection"]
last_modified_at: 2026-10-29
description: "Busulfan：預測新適應症為骨髓增生異常症候群 (myelodysplastic syndrome)（證據等級 L2）。原適應症：慢性、亞急性骨髓性白血病"
---

# Busulfan
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

## Busulfan：烷化劑類細胞毒性藥物 → 骨髓增生異常症候群 (myelodysplastic syndrome)
{: .text-alpha }

## 一句話總結

Busulfan 是一種雙功能烷化劑，作用於造血幹細胞與前驅細胞。
TxGNN 模型預測它可能對**骨髓增生異常症候群 (myelodysplastic syndrome)** 有效，
目前資料中有 **多項以 busulfan 為核心的條件療法臨床試驗**，以及 **多篇相關文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性、亞急性骨髓性白血病; 慢性骨髓性白血病、真性紅血球增多症、自發性血小板增多症; 慢性骨髓細胞白血病; 併用化療藥物及/或放射線治療，作為下列患者進行造血前驅細胞移植前之條件療法(CONDITIONING REGIMEN)：急性淋巴性白血病，急性非淋巴性白血病，急性骨髓性白血病，慢性骨髓性白血病，非何杰金氏淋巴瘤，何杰金氏淋巴瘤，多發性骨髓瘤。 |
| 預測新適應症 | 骨髓增生異常症候群 (myelodysplastic syndrome) |
| TxGNN 預測分數 | 0.9962 |
| 證據等級 | L2 |
| 台灣上市 | 上市中（有效許可證 1 張／共 4 張） |
| 許可證數 | 4 張（有效單方 1／有效複方 0／已註銷 3） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Busulfan 是雙功能烷化劑，可使 DNA 交叉連結，並清除造血幹細胞與前驅細胞。這種骨髓清除作用使它成為異體造血幹細胞移植前，骨髓清除性或減低強度條件療法的常用骨幹藥物。

骨髓增生異常症候群 (MDS) 是造血幹細胞的克隆性疾病，異體造血幹細胞移植是目前唯一可能治癒的方式，也是適合患者（特別是較高風險者）的標準治療。移植前需要清除異常骨髓並讓出空間給供體細胞，這正是 busulfan 的藥理作用。

需要注意的是，目前缺乏詳細的作用機轉資料（MOA）。上述機轉說明來自藥物類別與移植條件療法的文獻脈絡。Busulfan 在此是移植條件療法的一部分，而非直接治療 MDS 的單一藥物。

## 臨床試驗證據

以下列出與 MDS 最相關的試驗（資料中共有多項，此處列出 10 個）。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00005866](https://clinicaltrials.gov/study/NCT00005866) | Phase 3 | 完成 | 240 | 比較 busulfan-全身放射線與 cyclophosphamide-全身放射線作為進階 MDS 或 MDS 相關 AML 的移植前處置 |
| [NCT00822393](https://clinicaltrials.gov/study/NCT00822393) | Phase 3 | 完成 | 570 | 比較 treosulfan 與減低強度 busulfan 條件療法，用於 AML 或 MDS |
| [NCT04708054](https://clinicaltrials.gov/study/NCT04708054) | Phase 2/3 | 招募中 | 324 | 在分次 busulfan 療程中加入 venetoclax，用於高風險 AML 與 MDS |
| [NCT05453552](https://clinicaltrials.gov/study/NCT05453552) | Phase 2/3 | 未知 | 242 | 比較 G-CSF+decitabine+busulfan/cyclophosphamide 與 busulfan/fludarabine，用於高風險 MDS |
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Phase 2 | 進行中（不招募） | 116 | Venetoclax 加分次 busulfan、cladribine、fludarabine 條件療法，用於 AML 與 MDS 移植 |
| [NCT01643668](https://clinicaltrials.gov/study/NCT01643668) | Phase 2 | 完成 | 34 | Busulfan/clofarabine 減低強度條件療法後接異體移植 |
| [NCT00502905](https://clinicaltrials.gov/study/NCT00502905) | Phase 2 | 完成 | 200 | 高劑量靜脈 busulfan 加 fludarabine，用於 AML 與 MDS 異體移植 |
| [NCT01056614](https://clinicaltrials.gov/study/NCT01056614) | Phase 2 | 完成 | 23 | Fludarabine 加目標劑量靜脈 busulfan 條件療法，用於骨髓性惡性疾病 |
| [NCT01168219](https://clinicaltrials.gov/study/NCT01168219) | Phase 2 | 完成 | 68 | Busulfan、fludarabine、ATG 減低強度移植加 azacitidine，用於 MDS 與年長 AML |
| [NCT06247917](https://clinicaltrials.gov/study/NCT06247917) | Phase 2 | 未知 | 59 | FLU-BU-MEL 條件療法用於 MDS 異體移植的單臂研究 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | RCT | The Lancet. Haematology | 年長 AML 或 MDS 患者，比較 treosulfan 加 fludarabine 與減低強度 busulfan 加 fludarabine 的非劣性第三期試驗 |
| [42285355](https://pubmed.ncbi.nlm.nih.gov/42285355/) | 2026 | RCT | Transplantation and Cellular Therapy | 比較兩種 busulfan 分次方案（搭配 fludarabine 與 cladribine），用於 AML 或 MDS |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | 世代研究 | American Journal of Hematology | 年長 AML／MDS 患者中，treosulfan 相較減低強度 busulfan 的最終分析 |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Review | American Journal of Hematology | 異體移植用於骨髓纖維化與 MDS 的當代回顧 |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | 系統性回顧與統合分析 | Frontiers in Oncology | 比較 MDS 與 AML 移植前 treosulfan 與 busulfan 條件療法的長期結果 |
| [34692485](https://pubmed.ncbi.nlm.nih.gov/34692485/) | 2021 | 統合分析 | Frontiers in Oncology | 減低強度條件療法用於 AML 與 MDS 的隨機試驗統合分析 |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | 回溯性分析 | Bone Marrow Transplantation | MDS 中比較 fludarabine/busulfan 與 busulfan/cyclophosphamide 的傾向分數配對分析 |
| [35296446](https://pubmed.ncbi.nlm.nih.gov/35296446/) | 2022 | 回溯性分析 | Transplantation and Cellular Therapy | MDS 中比較骨髓清除性與減低強度 fludarabine/busulfan |
| [38197938](https://pubmed.ncbi.nlm.nih.gov/38197938/) | 2024 | 世代研究 | Blood Advances | Ven/FluBu2 條件療法後，以 venetoclax/azacitidine 做預防性維持治療 |
| [37856098](https://pubmed.ncbi.nlm.nih.gov/37856098/) | 2024 | 風險評估 | Pediatric Blood & Cancer | Busulfan 暴露與後續惡性腫瘤的證據型風險評估 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Busulfan 的不重複許可證共 **4 張**：有效單方 1 張、有效複方 0 張、已註銷 3 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第023785號 | 補束剋 注射劑 | 注射劑 | 台灣大塚製藥股份有限公司 | 2028/07/23 | 併用化療藥物及/或放射線治療，作為下列患者進行造血前驅細胞移植前之條件療法(CONDITIONING REGIMEN)：急性淋巴性白血病，急性非淋巴性白血病，急性骨髓性白血病，慢性… |

<details><summary><strong>已註銷</strong>（3 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥輸字第002940號</td><td>白血寧</td><td>BUSULFAN</td><td>1985/08/14</td></tr><tr><td>衛署藥輸字第009115號</td><td>邁樂寧錠２毫克</td><td>BUSULFAN</td><td>2024/05/06</td></tr><tr><td>衛署藥輸字第011705號</td><td>補素芬錠２公絲</td><td>BUSULFAN</td><td>1999/10/25</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（烷化劑） |
| 骨髓抑制風險 | 高（作為骨髓清除性條件療法的核心作用） |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 全血球計數（CBC）、肝腎功能；依移植條件療法需求評估 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

- **藥物交互作用**：資料中共有 228 筆交互作用紀錄，其中較重要者包括：
  - Metronidazole（Major，嚴重）
  - Aprepitant（Moderate，中度）
  - Miconazole（Moderate，中度）
  - Levofloxacin（Minor，輕微）
- 其他紀錄（如 amphotericin B、各類制酸劑、類固醇、止吐藥等）分級未明，使用時需逐項評估。
- 其餘警語與禁忌資料請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多項 Phase 2 與 Phase 3 試驗，直接以 busulfan 為基礎的條件療法治療 MDS 患者，另有多篇隨機試驗與回溯性研究。
- Busulfan 在此是移植條件療法的一環，而非單獨療法；且其骨髓毒性高，必須在有移植經驗的中心使用。

**若要推進需要：**
- 補齊詳細的作用機轉（MOA）資料。
- 確認台灣現行許可證適應症與 MDS 移植用途的對應，必要時評估適應症擴充。
- 建立目標劑量監測（藥物暴露量）與血液學、肝毒性（含肝靜脈阻塞性疾病）的監測計畫。
- 針對年長或共病患者，評估減低強度與骨髓清除性方案的選擇。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表中 3 張口服製劑皆已註銷 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

