---
layout: default
title: Busulfan
parent: 高證據等級 (L1-L2)
nav_order: 49
evidence_level: L2
indication_count: 10
monitor_inn: "Busulfan"
predicted_indications: ["myelodysplastic syndrome", "refractory cytopenia of childhood", "unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "seborrheic keratosis", "simian immunodeficiency virus infection"]
last_modified_at: 2026-10-16
description: "Busulfan：預測新適應症為骨髓發育不良症候群 (Myelodysplastic Syndrome)（證據等級 L2）。原適應症：併用化療藥物及/或放射線治療，作為造血前驅細胞移植前之條件療法（適用於急性淋巴性白血病、急性非淋巴性白血病、急性骨髓性白血病…"
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

## Busulfan：從慢性骨髓性白血病到骨髓發育不良症候群
{: .text-alpha }

## 一句話總結

Busulfan（白血寧）是一種烷化劑，原本用於慢性骨髓性白血病，以及造血前驅細胞移植前的條件療法（conditioning regimen）。
TxGNN 模型預測它可能對**骨髓發育不良症候群 (Myelodysplastic Syndrome, MDS)** 有效，
目前有 **多個 Phase 2/3 臨床試驗**（含 1 個已完成的 Phase 3 RCT）和 **多篇文獻**（含隨機試驗）支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 併用化療藥物及/或放射線治療，作為造血前驅細胞移植前之條件療法（適用於急性淋巴性白血病、急性非淋巴性白血病、急性骨髓性白血病、慢性骨髓性白血病、非何杰金氏淋巴瘤、何杰金氏淋巴瘤、多發性骨髓瘤） |
| 預測新適應症 | 骨髓發育不良症候群 (Myelodysplastic Syndrome) |
| TxGNN 預測分數 | 99.62% |
| 證據等級 | L2 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 4 張（有效單方 1／有效複方 0／已註銷 3） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位未收錄）。不過，Busulfan 是已知的雙功能烷化劑，會使 DNA 交叉連結，進而清除造血幹細胞與前驅細胞。這項特性使它成為異體造血幹細胞移植前清髓（myeloablative）或減低強度條件療法的核心骨架。

台灣已核准的適應症本身就是白血病與移植前條件療法。MDS 與急性骨髓性白血病同屬骨髓惡性疾病，且異體移植是高風險 MDS 目前唯一可能治癒的方式。因此，把 Busulfan 的移植前條件療法用途延伸到 MDS，在機轉與臨床脈絡上都相當合理。

需要留意的是，這個「新適應症」實質上是延伸其移植條件療法的角色，而不是用它直接治療 MDS。

## 臨床試驗證據

資料中共有 30 多項與 MDS 相關的試驗，以下列出最相關的 10 項：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00005866](https://clinicaltrials.gov/study/NCT00005866) | Phase 3 | 完成 | 240 | 比較 Busulfan-TBI 與 Cyclophosphamide-TBI 作為進展期 MDS 或 MDS 相關 AML 的移植前處置 |
| [NCT00822393](https://clinicaltrials.gov/study/NCT00822393) | Phase 3 | 完成 | 570 | Treosulfan 與減低強度 Busulfan 條件療法比較，對象為不適合標準條件療法的 AML/MDS 患者 |
| [NCT04708054](https://clinicaltrials.gov/study/NCT04708054) | Phase 2/3 | 招募中 | 324 | 在分次 Busulfan 方案中加入 Venetoclax，用於高風險 AML/MDS |
| [NCT05453552](https://clinicaltrials.gov/study/NCT05453552) | Phase 2/3 | 未知 | 242 | G-CSF+Decitabine 搭配 BUCY 與 BF 兩種條件療法，用於高風險 MDS |
| [NCT04713956](https://clinicaltrials.gov/study/NCT04713956) | Phase 2/3 | 未知 | 242 | 同上，對象為 RAEB-1/2 與 MDS 繼發 AML |
| [NCT00502905](https://clinicaltrials.gov/study/NCT00502905) | Phase 2 | 完成 | 200 | 高劑量靜脈 Busulfan 加 Fludarabine，用於 AML 與 MDS 的異體移植 |
| [NCT01643668](https://clinicaltrials.gov/study/NCT01643668) | Phase 2 | 完成 | 34 | Busulfan/Clofarabine 減低強度條件療法 |
| [NCT01168219](https://clinicaltrials.gov/study/NCT01168219) | Phase 2 | 完成 | 68 | Busulfan、Fludarabine 與 ATG 加 Azacitidine，用於高風險 MDS 與年長 AML |
| [NCT06247917](https://clinicaltrials.gov/study/NCT06247917) | Phase 2 | 未知 | 59 | FLU-BU-MEL 條件療法，單臂研究，用於 MDS |
| [NCT07183878](https://clinicaltrials.gov/study/NCT07183878) | NA | 招募中 | 138 | 隨機比較 Venetoclax 加強型 BUCY 與標準 BUCY |

此外，NCT06337331 已撤案、入組人數為 0，不提供任何結果資料。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | RCT（Phase 3） | Lancet Haematol | Treosulfan 加 Fludarabine 對比減低強度 Busulfan 加 Fludarabine，用於年長 AML/MDS 的非劣性試驗 |
| [42285355](https://pubmed.ncbi.nlm.nih.gov/42285355/) | 2026 | RCT（Phase 2） | Transplant Cell Ther | 比較兩種分次清髓性 Busulfan 搭配 Fludarabine 與 Cladribine 的方案 |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | 前瞻性隨機試驗最終分析 | Am J Hematol | Treosulfan 相較減低強度 Busulfan，改善年長 AML/MDS 患者的移植結果 |
| [34692485](https://pubmed.ncbi.nlm.nih.gov/34692485/) | 2021 | 統合分析 | Front Oncol | 減低強度與清髓性條件療法於 AML/MDS 的比較 |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | 系統性回顧與統合分析 | Front Oncol | Treosulfan 與 Busulfan 條件療法的長期結果比較 |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | 回溯性（傾向分數配對） | Bone Marrow Transplant | MDS 中 Flu/Bu4 與 Bu4/Cy 的清髓性條件療法比較 |
| [35296446](https://pubmed.ncbi.nlm.nih.gov/35296446/) | 2022 | 回溯性（傾向分數配對） | Transplant Cell Ther | MDS 中 Flu/Bu4 與 Flu/Bu2 的比較 |
| [37579918](https://pubmed.ncbi.nlm.nih.gov/37579918/) | 2023 | 回溯性研究 | Transplant Cell Ther | 清髓劑量 Busulfan 加 Fludarabine 與體內 T 細胞清除，對 AML/MDS 安全且有效 |
| [38197938](https://pubmed.ncbi.nlm.nih.gov/38197938/) | 2024 | Phase 1 | Blood Adv | Ven/FluBu2 移植後預防性維持治療 |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Review | Am J Hematol | 異體移植是 MDS 與骨髓纖維化唯一可能治癒的療法 |

文獻多數是以 Treosulfan 或其他藥物對比 Busulfan 的研究，Busulfan 常扮演對照組或方案骨幹。這些證據支持它在 MDS 移植中的應用，但不代表它優於其他條件療法。

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
| 骨髓抑制風險 | 高（用於清髓性條件療法時，目的即為清除骨髓；知識圖譜亦列出血小板低下、嗜中性白血球低下、無顆粒球症、貧血等相關關聯） |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | CBC（含分類）、肝功能、腎功能；高劑量使用時建議依指引評估血中藥物濃度 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

- **知識圖譜標示的禁忌或風險疾病**（來自 TxGNN 知識圖譜，非仿單內容）：癲癇、血小板低下、嗜中性白血球低下、無顆粒球症、貧血（含巨球性貧血與 Fanconi 貧血）、高血糖、鉀缺乏、感染性疾病（含黴菌感染與皮癬菌病）、肺纖維化。
- **藥物交互作用**：共查得 228 筆。主要者包括：
  - 重大（Major）：Metronidazole
  - 中度（Moderate）：Aprepitant、Miconazole
  - 輕微（Minor）：Levofloxacin
  - 其餘如 Amphotericin B、Pantoprazole、Omeprazole、Dexamethasone 等，等級未定。
- **其他**：文獻指出 Busulfan 與後續續發性惡性腫瘤風險有關，發生率被認為偏低，但目前特性仍不明確（PMID 37856098）。

詳細警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有 1 個完成的 Phase 3 RCT（NCT00005866）直接以 Busulfan 為試驗組，對象為進展期 MDS，另有多個 Phase 2/3 與 Phase 2 試驗，機轉上也合理。
- 台灣有效許可證僅注射劑 1 張，核准的是移植前條件療法，用於 MDS 屬於證據導向的延伸使用，且藥物毒性高，需要嚴格把關。

**若要推進需要：**
- 確認 MDS 是否納入現行仿單適應症，必要時評估適應症擴增申請。
- 取得詳細的作用機轉資料與完整仿單警語。
- 限定於具移植經驗的醫療機構，並建立劑量調整與血中濃度監測機制。
- 追蹤進行中的 Phase 2/3 試驗（NCT04708054、NCT05453552）結果，並比較 Busulfan 與 Treosulfan 的條件療法優劣。

**其他預測適應症簡要說明：**
- 兒童難治性血球減少症（Refractory cytopenia of childhood）、再生不良性貧血相關貧血（aregenerative anemia）：證據等級 L3，以單臂試驗與回溯性研究為主，建議列為研究問題。
- HIV 感染：Busulfan 僅作為基因修飾幹細胞移植的條件療法，並非直接作用於病毒，證據等級 L3，建議列為研究問題。
- 未分類 MDS：僅有一篇較舊的觀察性報告（L3），建議列為研究問題。
- 5 號染色體長臂部分缺失、重度先天性低色素貧血伴環狀鐵粒幼細胞、神經發育障礙、脂漏性角化症、猴免疫缺乏病毒感染：僅有模型預測、缺乏實際研究（L5），建議暫緩（Hold）。其中神經發育障礙與脂漏性角化症找不到合理的機轉連結。

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

