---
layout: default
title: Ribavirin
parent: 高證據等級 (L1-L2)
nav_order: 243
evidence_level: L2
indication_count: 9
monitor_inn: "Ribavirin"
predicted_indications: ["chronic hepatitis B virus infection", "early-onset familial noncirrhotic portal hypertension", "hepatoportal sclerosis", "hepatopulmonary syndrome", "primitive portal vein thrombosis", "hepatic porphyria", "IgG4-related pachymeningitis", "eosinophilic angiocentric fibrosis", "IgG4-related mesenteritis"]
last_modified_at: 2026-10-29
description: "Ribavirin：預測新適應症為慢性 B 型肝炎 (chronic hepatitis B virus infection)（證據等級 L2）。原適應症：與 peginterferon α 或 α-interferon 併用…"
---

# Ribavirin
{: .fs-9 }

證據等級: **L2** | 預測適應症: **9** 個
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

## Ribavirin：從慢性 C 型肝炎到慢性 B 型肝炎
{: .text-alpha }

## 一句話總結

Ribavirin 是核苷類抗病毒藥物，在台灣核准用於與干擾素併用治療慢性 C 型肝炎。
TxGNN 模型預測它可能對**慢性 B 型肝炎 (chronic hepatitis B virus infection)** 有效，
目前有 **15 個相關臨床試驗登記**和 **20 篇文獻**，但多數文獻為綜述，且直接針對 B 型肝炎的 ribavirin 試驗有限。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 與 peginterferon α 或 α-interferon 併用，治療曾以 α-interferon 單一療法治療後復發的慢性 C 型肝炎，以及首次接受治療的慢性 C 型肝炎 |
| 預測新適應症 | 慢性 B 型肝炎 (chronic hepatitis B virus infection) |
| TxGNN 預測分數 | 0.9986 |
| 證據等級 | L2 |
| 台灣上市 | 上市中（有效許可證 2 張／共 13 張） |
| 許可證數 | 13 張（有效單方 2／有效複方 0／已註銷 11） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。依據本報告彙整的資料，ribavirin 可抑制 IMP 去氫酶（造成 GTP 耗竭），並具有免疫調節作用，可能增強干擾素為基礎療法的反應。

C 型與 B 型肝炎同為慢性病毒性肝炎，臨床上常以干擾素為治療骨幹，且兩者可能共同感染。因此「peginterferon 加 ribavirin」的做法，自然延伸到 B 型肝炎的研究。

但需要注意：ribavirin 對 B 型肝炎病毒本身的直接抗病毒活性偏弱，目前並非公認的 B 型肝炎治療藥物。支持證據主要來自與 peginterferon 併用的試驗，而不是 ribavirin 單獨使用。

## 臨床試驗證據

以下列出與慢性 B 型肝炎關聯較直接的試驗，以及其他代表性試驗。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00114361](https://clinicaltrials.gov/study/NCT00114361) | Phase 3 | 完成 | 138 | Peginterferon alfa-2a 併用 ribavirin vs. 單用 peginterferon，用於 HBeAg 陰性慢性 B 型肝炎（PARC 研究） |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Phase 2/3 | 完成 | 120 | Interferon alpha-2b 併用 ribavirin 治療慢性 B 型肝炎的先導研究 |
| [NCT03759782](https://clinicaltrials.gov/study/NCT03759782) | Phase 3 | 未知 | 24 | 以 ribavirin 的免疫調節作用增強 B 型肝炎核苷類似物療效的先導試驗 |
| [NCT00154869](https://clinicaltrials.gov/study/NCT00154869) | Phase 3 | 未知 | 320 | Peginterferon alfa-2a 併用 ribavirin，用於 C/B 型肝炎共同感染及慢性 C 型肝炎 |
| [NCT00117533](https://clinicaltrials.gov/study/NCT00117533) | Phase 4 | 未知 | 20 | Peginterferon alfa-2b 併用 ribavirin，用於 B 型合併 D 型肝炎感染 |
| [NCT02219477](https://clinicaltrials.gov/study/NCT02219477) | Phase 3 | 完成 | 36 | 含 ribavirin 的直接作用抗病毒藥物方案，用於失代償肝硬化的 C 型肝炎（與 B 型肝炎關聯間接） |
| [NCT01447420](https://clinicaltrials.gov/study/NCT01447420) | Phase 4 | 完成 | 129 | Peginterferon alfa-2a 加 ribavirin 治療第 1 型 C 型肝炎，探討 IL-28B 表現（C 型肝炎研究） |
| [NCT01195181](https://clinicaltrials.gov/study/NCT01195181) | Phase 4 | 完成 | 506 | 慢性 C 型肝炎抗病毒治療的使用、療效、安全性與病毒動力學監測 |
| [NCT01309932](https://clinicaltrials.gov/study/NCT01309932) | Phase 2 | 完成 | 165 | Peginterferon lambda 加 ribavirin 與直接作用抗病毒藥物，用於第 1 型 C 型肝炎 |
| [NCT01425970](https://clinicaltrials.gov/study/NCT01425970) | Phase 2 | 終止 | 210 | INX-08189 併用 peginterferon 與 ribavirin，用於第 2、3 型 C 型肝炎 |

直接涉及 B 型肝炎的試驗為 NCT00114361、NCT00275938、NCT03759782、NCT00154869 與 NCT00117533。其餘多屬 C 型肝炎研究，僅能作為間接參考。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | C/B 型肝炎共同感染的處理；過去建議以 peginterferon 加 ribavirin 治療 HCV RNA 陽性者 |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | C 型與 B 型肝炎雙重感染的治療與預後更新 |
| [27433078](https://pubmed.ncbi.nlm.nih.gov/27433078/) | 2016 | 文獻回顧 | World J Gastroenterol | 干擾素加或不加 ribavirin 為 HBV 與 HCV 的早期治療，直接作用抗病毒藥物已改變治療標準 |
| [26284971](https://pubmed.ncbi.nlm.nih.gov/26284971/) | 2015 | Review | Curr Opin Virol | IL28B 基因型對 B 型與 C 型肝炎治療反應的影響 |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | Review | World J Gastroenterol | IL28B 基因多型性與 B 型肝炎感染結果的關聯 |
| [25048716](https://pubmed.ncbi.nlm.nih.gov/25048716/) | 2015 | Review | Hepatology | B 型與 C 型肝炎抗病毒治療的免疫學層面 |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | 文獻回顧 | Annu Rev Med | 慢性 B 型與 C 型肝炎的治療策略 |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Review | Expert Rev Anti Infect Ther | 兒童慢性 B 型與 C 型肝炎的治療選擇 |
| [24379612](https://pubmed.ncbi.nlm.nih.gov/24379612/) | 2013 | Review | World J Gastroenterol | 慢性 B/C 型肝炎相關肝細胞癌的預防 |
| [11070570](https://pubmed.ncbi.nlm.nih.gov/11070570/) | 2000 | 文獻回顧 | Int J Clin Pract | 慢性病毒性肝炎；標準治療為 α-干擾素加 ribavirin（針對 C 型肝炎） |

上述文獻均為綜述或回顧，未見針對 ribavirin 治療 B 型肝炎的獨立隨機對照試驗報告。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Ribavirin 的不重複許可證共 **13 張**：有效單方 2 張、有效複方 0 張、已註銷 11 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第048027號 | 摩舒肝清膠囊 | 膠囊劑 | 東生華製藥股份有限公司 | 2031/06/20 | 與PEGINTERFERON α 或 α -INTERFERON併用治療：1.曾經使用 α -INTERFERON單一療法治療後又復發的慢性C型肝炎。2.首次接受治療的慢性C型肝炎… |
| 衛署藥製字第048152號 | 源展膠囊200毫克 | 膠囊劑 | 健喬信元醫藥生技股份有限公司 | 2031/08/02 | 與peginterferon α 或α-interferon 併用治療：1.曾經使用α-interferon 單一療法後又復發的慢性C型肝炎。2.首次接受治療的慢性C型肝炎。 |

<details><summary><strong>已註銷</strong>（11 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第027769號</td><td>速百敏膠囊</td><td>BIOTIN、CHLORPHENIRAMINE MALEATE、GLYCYRRHIZIN (AMMONIATED)、RI…</td><td>1991/09/24</td></tr><tr><td>衛署藥製字第044650號</td><td>羅拔除膠囊200毫克</td><td>RIBAVIRIN</td><td>2021/10/21</td></tr><tr><td>衛署藥輸字第017379號</td><td>丕拉弱凍晶吸入劑</td><td>RIBAVIRIN</td><td>1995/09/18</td></tr><tr><td>衛署藥輸字第021029號</td><td>丕拉弱凍晶吸入劑</td><td>RIBAVIRIN</td><td>1998/08/05</td></tr><tr><td>衛署藥輸字第022173號</td><td>丕拉弱凍晶吸入劑</td><td>RIBAVIRIN</td><td>2013/12/16</td></tr><tr><td>衛署藥輸字第023204號</td><td>利必妥合併療法（因治隆注射液六百萬單位﹨毫升合併瑞比達膠囊２</td><td>RIBAVIRIN、INTERFERON ALPHA- 2B</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第023205號</td><td>利必妥合併療法（因治隆注射液一千五百萬單位/毫升合併瑞比達膠</td><td>INTERFERON ALPHA- 2B、RIBAVIRIN</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第023208號</td><td>瑞比達膠囊</td><td>RIBAVIRIN</td><td>2019/02/12</td></tr><tr><td>衛署藥輸字第025232號</td><td>適維肝膠囊 200 毫克</td><td>RIBAVIRIN</td><td>2022/06/23</td></tr><tr><td>衛署藥輸字第025605號</td><td>可珮格膜衣錠200毫克</td><td>RIBAVIRIN</td><td>2021/10/20</td></tr><tr><td>衛署藥輸字第025995號</td><td>立貝維爾</td><td>Ribavirin</td><td>2024/05/02</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

Ribavirin 屬抗病毒藥物，非典型的抗腫瘤藥物，故不列細胞毒性章節。

## 安全性考量

- **禁忌症（知識圖譜關聯，非仿單內容）**：知識圖譜記錄的相關疾病包括肝硬化、慢性阻塞性肺病、氣喘、鐮刀型貧血與血色素病變、各類貧血（含溶血性貧血）、全血球低下、心肌梗塞與冠狀動脈疾病、腎功能不全、間質性肺病、結節病、自體免疫性肝炎、胰臟炎等。實際禁忌症請以原廠仿單為準。
- **藥物交互作用**：資料庫共記錄 105 筆交互作用，但嚴重度分級皆為未知。部分列出的藥物包括 calcitriol、pantoprazole、glimepiride、mesalazine、doxycycline、metformin、omeprazole、prednisone、amphotericin B 等。
- **其他提醒**：文獻顯示 ribavirin 造成的溶血與鐵質變化，以及與干擾素併用時，可能誘發或加重卟啉症、肺部肉芽腫等不良事件。

主要警語請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有 1 項已完成的 Phase 3 試驗（NCT00114361）直接評估 peginterferon 加 ribavirin 用於 HBeAg 陰性慢性 B 型肝炎，另有 Phase 2/3 先導研究，故證據等級為 L2。但 ribavirin 對 HBV 的直接抗病毒活性弱，且目前 B 型肝炎已有更成熟的標準療法，因此只適合在嚴格限制下作為研究性探索。

**若要推進需要：**
- 取得 NCT00114361 與 NCT00275938 的完整結果，確認 ribavirin 相對單用干擾素的實際增益
- 追蹤 NCT03759782（ribavirin 搭配核苷類似物）的後續結果
- 補充 ribavirin 的作用機轉資料與完整仿單警語
- 規劃血液學（溶血、貧血）監測與生育風險管理
- 與現行 B 型肝炎標準療法比較其臨床定位

其他預測適應症（如早發性家族性非肝硬化門脈高壓、肝門脈硬化、肝肺症候群、原發性門靜脈血栓、肝性卟啉症等）目前僅有模型預測或間接個案報告，建議暫列 Hold。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表「速威干軟膠囊100毫克等」列 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

