---
layout: default
title: Mycophenolate Mofetil
parent: 高證據等級 (L1-L2)
nav_order: 186
evidence_level: L2
indication_count: 10
monitor_inn: "Mycophenolate mofetil"
predicted_indications: ["HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "bone Paget disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "multiple sclerosis", "hemosiderosis", "Heiner syndrome", "African iron overload", "neonatal hemochromatosis"]
last_modified_at: 2026-10-16
description: "Mycophenolate Mofetil：預測新適應症為HIV 感染 (HIV infectious disease)（證據等級 L2）。原適應症：與 Cyclosporin 和類固醇合併使用，以預防或緩解腎臟移植之急性器官排斥、預防心臟和肝臟移植之急性器官排斥"
---

# Mycophenolate Mofetil
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

## Mycophenolate mofetil：從器官移植排斥到 HIV 感染
{: .text-alpha }

## 一句話總結

Mycophenolate mofetil（黴酚酸嗎啉乙酯，MMF）原本用於預防腎、心、肝臟移植的急性器官排斥，以及治療狼瘡性腎炎。
TxGNN 模型預測它可能對 **HIV 感染 (HIV infectious disease)** 有效，
目前有 **4 個臨床試驗**和 **20 篇文獻**與此方向相關，但直接證據有限：唯一直接評估 MMF 抗病毒活性的試驗已撤案（0 人入組）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 與 Cyclosporin 和類固醇合併使用，以預防或緩解腎臟移植之急性器官排斥、預防心臟和肝臟移植之急性器官排斥 |
| 預測新適應症 | HIV 感染 (HIV infectious disease) |
| TxGNN 預測分數 | 0.9986 |
| 證據等級 | L2 |
| 台灣上市 | 上市中（有效許可證 5 張／共 10 張） |
| 許可證數 | 10 張（有效單方 5／有效複方 0／已註銷 5） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供）。根據已知的藥理背景，MMF 的活性代謝物黴酚酸 (mycophenolic acid) 會抑制 IMPDH，使鳥嘌呤核苷酸耗竭，進而限制淋巴球增殖。

在 HIV 的情境下，這個機轉有兩個可能的作用：
1. 減少被活化的 CD4⁺ T 細胞（病毒的目標細胞）數量。
2. 耗竭細胞內 dGTP，可能增強 abacavir 等核苷類逆轉錄酶抑制劑的活性。

文獻中有小型研究支持這個想法，例如在失敗病例中加入 MMF 後，細胞內 dGTP 下降且血漿 HIV-1 RNA 減少（5 位病人）。但 HIV 患者使用免疫抑制劑也有安全疑慮，可能影響淋巴球重建與 HIV 特異性免疫，目前沒有證實的臨床獲益。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 2 | 撤案 | 0 | 評估 MMF 併用 abacavir 的安全性與抗病毒活性；未入組，無證據產出 |
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 2 | 完成 | 56 | 安慰劑對照先導試驗，比較 DAPD 與 DAPD＋MMF 加入現有抗 HIV 療法；結果摘要未提供 |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | 終止 | 8 | 抗 EPO 相關純紅血球再生不全，以 cyclosporine＋MMF 治療；非 HIV 試驗，僅佐證免疫抑制機轉與耐受性 |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | N/A | 完成 | 5 | HIV 陽性者異體幹細胞移植，MMF 為移植後免疫抑制的一部分；並非檢驗 MMF 對 HIV 的效果 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | RCT | AIDS | 在未治療過的 HIV-1 患者中，比較 HAART 加或不加 MMF 對血漿 HIV-1 RNA 下降速率及潛伏感染細胞庫的影響 |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | Cohort | AIDS Res Hum Retroviruses | MMF 併用 HAART 在未治療的急性與慢性 HIV-1 患者中，未見明顯不利的免疫學影響 |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | Cohort | Clin Pharmacokinet | 低劑量 MMF 併用 abacavir、efavirenz、nelfinavir 的藥動／藥效學研究，建議進行藥物監測 |
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | 病例系列 | J Acquir Immune Defic Syndr | 5 位治療失敗者加入 MMF 後，細胞內 dGTP 下降、血漿 HIV-1 RNA 降低 |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | 討論免疫抑制藥物在 HIV 疾病中的角色 |
| [16515490](https://pubmed.ncbi.nlm.nih.gov/16515490/) | 2006 | Review | Curr Pharm Des | 以 virostatics 作為 HIV 治療策略的回顧 |
| [12003181](https://pubmed.ncbi.nlm.nih.gov/12003181/) | 2002 | Review | J Biol Regul Homeost Agents | 免疫調節在 HIV-1 長期控制中的潛在角色 |
| [20840478](https://pubmed.ncbi.nlm.nih.gov/20840478/) | 2010 | 回溯研究 | Am J Transplant | 巴黎 27 位 HIV 感染者腎臟移植經驗，免疫抑制方案含 MMF、類固醇與 tacrolimus 或 cyclosporine |
| [23622672](https://pubmed.ncbi.nlm.nih.gov/23622672/) | 2013 | 病例系列 | Transplant Proc | HIV 感染者腎臟移植的西班牙醫院經驗與文獻回顧 |
| [19112763](https://pubmed.ncbi.nlm.nih.gov/19112763/) | 2008 | 病例報告 | J Drugs Dermatol | HIV 患者的乾癬與乾癬性關節炎使用 MMF，治療安全且有效 |
| [39396546](https://pubmed.ncbi.nlm.nih.gov/39396546/) | 2025 | 病例報告 | Trop Doct | HIV 成人 IgA 血管炎，以類固醇加 MMF 達到完全腎臟緩解 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Mycophenolate Mofetil 的不重複許可證共 **10 張**：有效單方 5 張、有效複方 0 張、已註銷 5 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（5 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第050154號 | 異莫分膠囊 250 毫克 | 膠囊劑 | 友華生技醫藥股份有限公司 | 2029/05/26 | 與CYCLOSPORIN和類固醇合併使用，以預防或緩解腎臟移植之急性器官排斥、預防心臟和肝臟移植之急性器官排斥。 與皮質類固醇合併使用，Cellcept適用於在患有Internat… |
| 衛署藥製字第050866號 | 喜妥善膠囊 250 毫克 | 膠囊劑 | 健亞生物科技股份有限公司 | 2029/09/02 | 與Cyclosporin和類固醇合併使用，以預防或緩解腎臟移植之急性器官排斥、預防心臟和肝臟移植之急性器官排斥。與皮質類固醇合併使用，Mycocep適用於在患有Internatio… |
| 衛署藥輸字第021757號 | 山喜多膠囊２５０毫克 | 膠囊劑 | 羅氏大藥廠股份有限公司 | 2027/06/13 | 與CYCLOSPORIN和類固醇合併使用，以預防或緩解腎臟移植之急性器官排斥、預防心臟和肝臟移植之急性器官排斥。 與皮質類固醇合併使用，Cellcept適用於在患有Internat… |
| 衛署藥輸字第024215號 | 山喜多膜衣錠500毫克 | 膜衣錠 | 羅氏大藥廠股份有限公司 | 2030/04/29 | 與cyclosporin和類固醇合併使用，以預防或緩解腎臟移植之急性器官排斥、預防心臟和肝臟移植之急性器官排斥。 與皮質類固醇合併使用，Cellcept適用於在患有Internat… |
| 衛署藥輸字第025321號 | 移安“山德士”膜衣錠 500 毫克 | 膜衣錠 | 台灣山德士藥業股份有限公司 | 2031/01/17 | 與cyclosporin和類固醇合併使用，以預防或緩解腎臟移植之急性器官排斥、預防心臟和肝臟移植之急性器官排斥。與皮質類固醇合併使用，Mycophenolate mofetil適用… |

<details><summary><strong>已註銷</strong>（5 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第048247號</td><td>黴酚酸嗎啉乙酯</td><td>Mycophenolate mofetil</td><td>2023/11/22</td></tr><tr><td>衛署藥製字第055288號</td><td>“台耀”恩美芙</td><td>Mycophenolate Mofetil“F.L.”</td><td>2025/07/28</td></tr><tr><td>衛署藥輸字第024623號</td><td>山喜多注射劑500毫克</td><td>MYCOPHENOLATE MOFETIL HYDROCHLORIDE</td><td>2023/06/02</td></tr><tr><td>衛部藥輸字第026397號</td><td>免達抑膠囊250毫克</td><td>MYCOPHENOLATE MOFETIL</td><td>2025/04/28</td></tr><tr><td>衛部藥輸字第027227號</td><td>山喜多注射劑500毫克(法國廠)</td><td>MYCOPHENOLATE MOFETIL HYDROCHLORIDE</td><td>2024/04/29</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **禁忌症（知識圖譜推論，非仿單內容）**：知識圖譜顯示與 MMF 相關的禁忌疾病包括肝病、膽囊疾病、嗜中性白血球低下、顆粒球缺乏症、活動性消化性潰瘍、巨細胞病毒感染、單純疱疹、帶狀疱疹、進行性多發性腦白質病變、淋巴瘤、皮膚癌，以及再生不良性貧血等多種血液疾病。實際禁忌請以仿單為準。
- **藥物交互作用**：共查得 92 筆交互作用，以下為部分範例：
  - 重度：活性碳 (Activated charcoal)
  - 中度：質子幫浦抑制劑（rabeprazole、omeprazole、esomeprazole、lansoprazole、dexlansoprazole）、抗生素（doxycycline、amoxicillin、tetracycline、clarithromycin、minocycline、vancomycin、kanamycin、paromomycin）、制酸劑（氧化鎂、氫氧化鋁、碳酸鈣）
  - 輕度：鋅（zinc sulfate、zinc acetate）、鐵
- **HIV 情境的額外考量**：對 HIV 患者施以免疫抑制可能影響免疫重建與 HIV 特異性免疫，且 MMF 與抗病毒藥物之間需做藥物監測。

其他警語請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 分數很高，機轉上也有合理假設（IMPDH 抑制、增強核苷類藥物），但直接評估 MMF 對 HIV 的試驗已撤案，其餘試驗多為間接證據。
- 現有研究以小型研究、病例與回顧為主，尚未證實臨床獲益，且免疫抑制在 HIV 中有安全疑慮。證據等級雖標為 L2，但實質支持度偏弱。

**若要推進需要：**
- 設計並執行 MMF 加抗病毒療法的前瞻性 RCT，以病毒量、病毒庫大小與 CD4 重建為主要終點。
- 釐清 MMF 的完整作用機轉資料（目前 DrugBank 缺乏）。
- 建立 HIV 族群的安全性監測與藥物濃度監測計畫，尤其針對感染風險與抗病毒藥物交互作用。
- 重新評估第 6 順位預測「多發性硬化症」，該方向有隨機試驗與 Cochrane 系統性回顧可供參考，但現有回顧指出療效證據不足，仍屬探索性方向。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表「新睦樂凍晶注射劑」一列 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

