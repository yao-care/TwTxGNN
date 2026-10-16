---
layout: default
title: Icatibant
parent: 高證據等級 (L1-L2)
nav_order: 142
evidence_level: L1
indication_count: 7
---

# Icatibant
{: .fs-9 }

證據等級: **L1** | 預測適應症: **7** 個
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

# Icatibant：從遺傳性血管性水腫到 C1 酯酶抑制劑缺乏症

## 一句話總結

Icatibant 是一種緩激肽 B2 受體拮抗劑，原本用於遺傳性血管性水腫 (HAE) 急性發作的症狀治療。
TxGNN 模型預測它對 **C1 酯酶抑制劑缺乏症 (C1 inhibitor deficiency)** 有效，目前有 **11 個臨床試驗**和 **20 篇文獻**支持這個方向。
需要注意：HAE 本身就是由 C1 酯酶抑制劑不足所致，因此這個預測與現有核准適應症高度重疊，屬於仿單內使用，而非全新的再利用方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 體內 C1 酯酶抑制劑不足的成人、青少年及 2 歲以上兒童，在遺傳性血管性水腫 (HAE) 急性發作時進行症狀治療 |
| 預測新適應症 | C1 酯酶抑制劑缺乏症 (C1 inhibitor deficiency) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 2 張（有效單方 2／有效複方 0／已註銷 0） |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Icatibant 是選擇性的緩激肽 B2 受體拮抗劑（藥理資料顯示其作用標的包含 B1、B2 受體）。

C1 酯酶抑制劑缺乏會使激肽釋放酶-激肽系統失控活化，造成緩激肽過量，進而引發血管性水腫發作。Icatibant 直接阻斷緩激肽與 B2 受體結合，因此在機轉上與疾病病理高度吻合。

這個預測與 Icatibant 已核准的 HAE 適應症基本上是同一個疾病範疇，所以是仿單內使用。較有新意的延伸方向是**後天性 C1 酯酶抑制劑缺乏**（acquired angioedema, AAE）：已有一項 8 名病人的真實世界觀察研究（PMID 22686628），但樣本很小，且目前尚無該族群的核准療法。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00097695](https://clinicaltrials.gov/study/NCT00097695) | Phase 3 | 完成 | 84 | 隨機、雙盲、安慰劑對照，評估皮下注射 Icatibant 治療 HAE 急性發作的療效與安全性 |
| [NCT00912093](https://clinicaltrials.gov/study/NCT00912093) | Phase 3 | 完成 | 98 | 隨機、雙盲、安慰劑對照，評估 Icatibant 對 HAE 急性發作的療效與安全性 |
| [NCT00500656](https://clinicaltrials.gov/study/NCT00500656) | Phase 3 | 完成 | 85 | 雙盲對照，Icatibant 對比口服傳明酸 (tranexamic acid)，主要指標為症狀緩解起始時間 |
| [NCT00997204](https://clinicaltrials.gov/study/NCT00997204) | Phase 3 | 完成 | 151 | 開放標籤，評估病人自行注射的安全性、局部耐受性與療效 |
| [NCT01386658](https://clinicaltrials.gov/study/NCT01386658) | Phase 3 | 完成 | 32 | 兒童及青少年 HAE 的藥物動力學、耐受性與安全性 |
| [NCT03888755](https://clinicaltrials.gov/study/NCT03888755) | Phase 3 | 完成 | 8 | 日本 I 型或 II 型 HAE 急性發作的療效、藥動學與安全性 |
| [NCT04654351](https://clinicaltrials.gov/study/NCT04654351) | Phase 3 | 完成 | 2 | 日本兒童及青少年 HAE 的安全性與療效（人數極少，參考價值有限） |
| [NCT01457430](https://clinicaltrials.gov/study/NCT01457430) | Phase 4 | 完成 | 19 | 開放標籤，評估自行注射 Icatibant 的安全性、便利性與療效 |
| [NCT07290855](https://clinicaltrials.gov/study/NCT07290855) | Phase 4 | 完成 | 5 | 台灣研究，評估 Icatibant 對緩激肽相關血管性水腫病人的安全性與療效 |
| [NCT04057131](https://clinicaltrials.gov/study/NCT04057131) | N/A | 完成 | 179 | 日本上市後一般使用結果調查，收集真實世界安全性與療效資料 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29757016](https://pubmed.ncbi.nlm.nih.gov/29757016/) | 2018 | Cohort/回顧 | Expert Rev Clin Immunol | 隨機雙盲、開放延伸及前瞻觀察研究顯示 Icatibant 對 2 歲以上兒童與青少年 HAE 安全有效 |
| [22686628](https://pubmed.ncbi.nlm.nih.gov/22686628/) | 2012 | 觀察性研究 | Allergy | 8 名後天性 C1 抑制劑缺乏病人，48 次中重度發作以 Icatibant 30 mg 治療 |
| [23420425](https://pubmed.ncbi.nlm.nih.gov/23420425/) | 2013 | 系統性回顧 | Pneumonol Alergol Pol | 比較 conestat alfa、人類 C1 抑制劑與 Icatibant 治療成人 HAE 急性發作的療效 |
| [20030426](https://pubmed.ncbi.nlm.nih.gov/20030426/) | 2010 | Review | Drugs | FAST-1 試驗主要指標未達統計顯著，但多項其他指標顯示 Icatibant 有效 |
| [33602658](https://pubmed.ncbi.nlm.nih.gov/33602658/) | 2021 | Review | J Investig Allergol Clin Immunol | 回顧 C1-INH-HAE 現行療法與研發中藥物 |
| [37716525](https://pubmed.ncbi.nlm.nih.gov/37716525/) | 2023 | 回溯性研究 | J Allergy Clin Immunol Pract | 後天性 C1 抑制劑缺乏血管性水腫的診斷、病程與治療，目前無核准療法 |
| [32753245](https://pubmed.ncbi.nlm.nih.gov/32753245/) | 2020 | 建議/指引 | Rev Med Interne | 後天性 C1 抑制劑缺乏血管性水腫的診斷與治療建議 |
| [24925394](https://pubmed.ncbi.nlm.nih.gov/24925394/) | 2014 | Review | Chem Immunol Allergy | 緩激肽介導疾病皆以血管性水腫為主要表現 |
| [20135020](https://pubmed.ncbi.nlm.nih.gov/20135020/) | 2009 | Review | Drugs Today | 緩激肽是 HAE 的主要介質，Icatibant 為針對性治療 |
| [21284353](https://pubmed.ncbi.nlm.nih.gov/21284353/) | 2010 | Review | Prescrire Int | 評論認為 HAE 發作首選仍為靜脈注射 C1 酯酶抑制劑 |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Icatibant 的不重複許可證共 **2 張**：有效單方 2 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部罕藥製字第000021號 | 益康倍注射劑 | 注射液劑 | 南光化學製藥股份有限公司 | 2031/01/28 | 適用於體內C1酯酶抑制劑不足的成人、青少年及2歲以上兒童，在其遺傳性血管性水腫 (hereditary angioedema，HAE)急性發作時進行症狀治療。 |
| 衛部罕藥輸字第000066號 | 凡得適注射劑30毫克 | 注射液劑 | 台灣武田藥品工業股份有限公司 | 2031/01/28 | 適用於體內C1酯酶抑制劑不足的成人、青少年及2歲以上兒童，在其遺傳性血管性水腫 (hereditary angioedema，HAE)急性發作時進行症狀治療。 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 安全性考量

- **藥物交互作用**：資料庫共記錄 12 筆交互作用相關項目，其中 10 筆為中度 (Moderate) 等級，皆為 ACE 抑制劑類藥物：Benazepril、Captopril、Enalapril、Perindopril、Trandolapril、Moexipril、Lisinopril、Quinapril、Ramipril、Fosinopril。其餘 2 筆為藥理標的資料（緩激肽 B1、B2 受體），並非藥物交互作用。

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多個已完成的 Phase 3 試驗（包含安慰劑對照及傳明酸對照的隨機雙盲試驗），Icatibant 對 C1 酯酶抑制劑不足所致 HAE 的療效已有充分證據，並已在台灣取得核准。
- 此預測本質上與現有適應症重疊，並非新的再利用機會；真正有探索價值的是後天性 C1 酯酶抑制劑缺乏，但目前僅有小型觀察性研究支持。

**若要推進需要：**
- 釐清評估目標：若僅為現有 HAE 適應症，無需額外再利用評估；若針對後天性 C1 酯酶抑制劑缺乏，則需更大規模的前瞻性研究。
- 補充詳細的作用機轉資料（MOA）。
- 確認與 ACE 抑制劑併用的風險管理與病人用藥審查。
- 確認特定族群（兒童、老年人）的安全性監測計畫。

---

**附註：其他預測適應症（暫不建議推進）**

其餘 6 個預測適應症僅有 TxGNN 模型預測（證據等級 L5），無臨床試驗與文獻支持，且機轉上與緩激肽 B2 受體拮抗缺乏明確關聯，建議 **Hold**：

| 預測適應症 | TxGNN 分數 | 決策 |
|-----------|-----------|------|
| 毒性絲胺酸蛋白酶抑制劑聚合病 (serpinopathy with toxic serpin polymerization) | 99.99% | Hold |
| 偽性血管性血友病 (pseudo-von Willebrand disease) | 99.21% | Hold |
| 血小板原發性釋放障礙 (primary release disorder of platelets) | 99.14% | Hold |
| 免疫介導壞死性肌病 (immune-mediated necrotizing myopathy) | 99.06% | Hold |
| 抗合成酶症候群 (antisynthetase syndrome) | 99.02% | Hold |
| 血小板無力症 (Glanzmann thrombasthenia) | 99.00% | Hold |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

