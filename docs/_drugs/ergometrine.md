---
layout: default
title: Ergometrine
parent: 中證據等級 (L3-L4)
nav_order: 94
evidence_level: L3
indication_count: 10
---

# Ergometrine
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

# Ergometrine：從子宮收縮到偏頭痛

## 一句話總結

Ergometrine 是麥角生物鹼類藥物，原本作為子宮收縮劑用於產後出血與相關出血症狀，台灣已有 101 張許可證（有效 18 張）。TxGNN 模型對其預測了 10 個潛在新適應症；其中 **偏頭痛 (Migraine Disorder)** 是最具臨床意義的預測，目前有 **20 篇文獻**支持，且部分台灣核准仿單已明列「偏頭痛」，具備監理先例。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 產後出血、子宮血崩、月經過多 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 101 張（有效單方 17／有效複方 1／已註銷 83） |
| 建議決策 | Proceed with Guardrails |

<!-- review:begin ergometrine-migraine-rereview-result-2026-10-03 -->

> **重審結果（2026-10-03）**：**維持**（證據等級 L3 不變）。機轉說明裡「經 α 受體抑制三叉神經源性炎症」不成立，但 L3 原本就不是靠這段機轉：本藥有一篇 40 人、無對照的月經性偏頭痛觀察性研究（[PMID 2759844](https://pubmed.ncbi.nlm.nih.gov/2759844/)），另有前臨床研究顯示 ergometrine 可抑制三叉神經元放電（[PMID 9448572](https://pubmed.ncbi.nlm.nih.gov/9448572/)）。methylergonovine 的研究是同系物，只能當旁證。查無 RCT，ClinicalTrials.gov 也查無登錄試驗；另有冠狀動脈痙攣等安全性報告（[PMID 23216317](https://pubmed.ncbi.nlm.nih.gov/23216317/)）。依據：[PubMed：Menstrual migraine and intermittent ergonovine therapy（PMID 2759844）](https://pubmed.ncbi.nlm.nih.gov/2759844/)；[PubMed：Microiontophoretic application of serotonin (5HT)1B/1D agonists inhibits trigeminal cell firing in the cat（PMID 9448572）](https://pubmed.ncbi.nlm.nih.gov/9448572/)；[PubMed：Oral methylergonovine maleate for refractory migraine and cluster headache prevention（PMID 23432443）](https://pubmed.ncbi.nlm.nih.gov/23432443/)；[PubMed：Efficacy and tolerability of intravenous methylergonovine in migraine female patients attending the emergency department: a pilot open-label study（PMID 19895705）](https://pubmed.ncbi.nlm.nih.gov/19895705/)；[PubMed：QT prolongation, Torsade de Pointes, myocardial ischemia from coronary vasospasm, and headache medications. Part 1: review of serotonergic cardiac adverse events with a triptan case（PMID 23216317）](https://pubmed.ncbi.nlm.nih.gov/23216317/)；[PubMed：Pleural thickening caused by Sansert and Ergotrate in the treatment of migraine（PMID 6773347）](https://pubmed.ncbi.nlm.nih.gov/6773347/)。

<!-- review:end ergometrine-migraine-rereview-result-2026-10-03 -->

> **附註**：TxGNN 分數最高的預測為毛髮過多症 (Hypertrichosis，99.96%)，但該適應症缺乏臨床證據且機轉連結薄弱（評等 L5，建議 Hold）。本報告以最具臨床意義的預測（偏頭痛）為主要分析對象。

---

<!-- review:begin ergometrine-moa-2026-10-03 -->

## Ergometrine 的作用機轉

<!-- moa-sourced: 2026-10-03 用戶拍板例外，只限附來源的作用機轉段 -->

以下只說明這個藥原本怎麼作用，每一點都摘自官方仿單的藥理段落並附連結；與本頁的老藥新用預測無關，也不構成用藥建議。

- Ergometrine 屬麥角生物鹼，透過對子宮肌層 5-HT2 受體與 α 腎上腺素受體的作用劑或部分作用劑效果，讓子宮產生持續的強直性收縮，子宮上段與下段都會收縮。（[仿單](https://www.medicines.org.uk/emc/product/6265/smpc)）
- 這種持續收縮能控制子宮出血；和 oxytocin 不同，它對未懷孕的子宮也有作用。（[仿單](https://www.medicines.org.uk/emc/product/6265/smpc)）
- 它會抑制泌乳素分泌，因此可能減少乳汁分泌。（[仿單](https://www.medicines.org.uk/emc/product/6265/smpc)）
- 肌肉注射後約 7 分鐘內開始刺激子宮，靜脈注射則幾乎立即作用。（[仿單](https://www.medicines.org.uk/emc/product/6265/smpc)）
- 對血管有部分作用劑效果（比 ergotamine 弱），對心血管與中樞神經的影響也比其他麥角生物鹼小；對 α 腎上腺素受體幾乎沒有拮抗作用。（[仿單](https://www.medicines.org.uk/emc/product/6265/smpc)）

**來源**：[英國 emc：Ergometrine Injection BP 0.05% w/v 產品特性摘要（SmPC）§5.1 藥效學](https://www.medicines.org.uk/emc/product/6265/smpc)；查閱日期 2026-10-03。

---

<!-- review:end ergometrine-moa-2026-10-03 -->

## 為什麼這個預測合理？

目前 Ergometrine 的詳細作用機轉（MOA）資料尚有缺口。根據現有藥理學文獻，Ergometrine 為麥角生物鹼（ergot alkaloid），具備與同類藥物一致的受體藥理特性：透過激動 **5-HT1B/1D 受體**使顱內異常擴張的血管收縮，並作用於 **α-腎上腺素受體**抑制三叉神經源性炎症反應。這正是麥角類藥物治療偏頭痛的核心機轉。

<!-- review:begin ergometrine-alpha-premise-2026-10-03 -->

> **查核加註（2026-10-03）**：此前提與仿單不符。仿單所載 ergometrine 的受體作用是子宮肌層 5-HT2 與 α 腎上腺素受體的作用劑／部分作用劑效果，並寫明它對 α 腎上腺素受體幾乎沒有拮抗作用；仿單沒有提到 5-HT1B/1D，也沒有提到經 α 受體抑制三叉神經源性炎症。上段原文保留未改。依據：[emc：Ergometrine Injection BP 0.05% w/v SmPC §5.1](https://www.medicines.org.uk/emc/product/6265/smpc)。

<!-- review:end ergometrine-alpha-premise-2026-10-03 -->

子宮收縮與偏頭痛治療看似毫無關聯，但 Ergometrine 的效用根本都來自相同的**血管收縮特性**。偏頭痛急性發作時顱內血管異常擴張，麥角生物鹼恰好能透過上述受體機轉逆轉此病理狀態。與 Ergometrine 結構相近的半合成同系物 methylergonovine 已有多項觀察性研究直接用於月經性偏頭痛預防及頑固性偏頭痛急性治療。

<!-- review:begin ergometrine-methylergonovine-not-metabolite-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「Ergometrine 的活性代謝物 methylergonovine」。Methylergonovine 不是 ergometrine 的代謝物：它是 ergometrine（ergonovine）多一個 CH2 的同系物，屬半合成麥角生物鹼；ergometrine 仿單所載的代謝途徑是羥化、葡萄糖醛酸結合（可能還有 N-去甲基），主要排出物為 12-hydroxyergometrine glucuronide。本次只更正這個藥理事實，引用的研究、證據等級與結論未改。依據：[NLM MeSH：Methylergonovine（D008755）](https://meshb.nlm.nih.gov/record/ui?ui=D008755)；[DailyMed：Methylergonovine Maleate Tablets, USP 仿單（Teva）](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d8e4b8ed-3289-4611-8a61-2392a4bf6072)；[emc：Ergometrine Injection BP 0.05% w/v SmPC §5.2](https://www.medicines.org.uk/emc/product/6265/smpc)。

<!-- review:end ergometrine-methylergonovine-not-metabolite-2026-10-03 -->

更值得關注的是，**台灣部分核准仿單已明列「偏頭痛」為適應症**（如「分娩後之子宮弛緩⋯⋯偏頭痛」），代表此一用途在台灣監理層面已有前例，大幅降低法規再申請的障礙。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [2759844](https://pubmed.ncbi.nlm.nih.gov/2759844/) | 1989 | Cohort | Headache | 40 名月經性偏頭痛患者接受間歇性 ergonovine maleate 預防治療，6 個月觀察顯示療效顯著 |
| [23432443](https://pubmed.ncbi.nlm.nih.gov/23432443/) | 2013 | Cohort | Headache | 口服 methylergonovine maleate 用於頑固性偏頭痛及叢發性頭痛預防，報告臨床觀察結果 |
| [19895705](https://pubmed.ncbi.nlm.nih.gov/19895705/) | 2009 | Cohort | Head & Face Medicine | 急診靜脈注射 methylergonovine 用於嚴重偏頭痛女性患者的療效與耐受性初探試驗 |
| [7216754](https://pubmed.ncbi.nlm.nih.gov/7216754/) | 1980 | Cohort | Headache | 偏頭痛長期間歇預防療法的結果追蹤研究 |
| [5761912](https://pubmed.ncbi.nlm.nih.gov/5761912/) | 1969 | Cohort | BMJ | 復發性頭痛預防療法的比較研究，包含麥角衍生物組別 |
| [9793694](https://pubmed.ncbi.nlm.nih.gov/9793694/) | 1998 | Review | Cephalalgia | Methysergide（ergometrine 衍生物）作為特異性 5-HT 受體拮抗劑/激動劑用於偏頭痛預防，對高頻率頑固案例尤為有效 |
| [556819](https://pubmed.ncbi.nlm.nih.gov/556819/) | 1977 | Case series | Neurology | 8 名女性頸動脈痛（carotidynia）患者以偏頭痛預防藥物（含麥角衍生物）成功治療 |
| [23216317](https://pubmed.ncbi.nlm.nih.gov/23216317/) | 2013 | Case series | Headache | 審視偏頭痛藥物的心臟血管副作用，指出麥角生物鹼使用時需注意冠狀動脈痙攣風險 |
| [13306339](https://pubmed.ncbi.nlm.nih.gov/13306339/) | 1955 | Review | Int Arch Allergy | 麥角療法治療偏頭痛的歷史發展與機轉文獻回顧 |
| [15293589](https://pubmed.ncbi.nlm.nih.gov/15293589/) | 2004 | Review | Am J Crit Care | 探討 Prinzmetal 心絞痛與偏頭痛的血管痙攣共同病理機轉；涉及 ergonovine 誘發試驗 |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Ergometrine 的不重複許可證共 **101 張**：有效單方 17 張、有效複方 1 張、已註銷 83 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（17 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 內衛藥製字第001749號 | “強生”縮水蘋果酸麥角新鹼膜衣錠０．２毫克 | 膜衣錠 | 強生化學製藥廠股份有限公司 | 2029/05/25 | 產褥期之出血、流產後之出血、分娩時之子宮弛緩出血、不正常出血、分娩第三期陣痛微弱。 |
| 內衛藥製字第007872號 | "尼斯可"縮水蘋果酸麥角新鹼片 | 錠劑 | 尼斯可生技股份有限公司 | 2029/05/25 | 弛緩性子宮出血、分娩後出血、子宮收縮不全、流產出血 |
| 內衛藥製字第009702號 | "新喜"美宮錠０．２公絲 | 錠劑 | 新喜國際企業股份有限公司 | 2028/05/25 | 產褥期出血、分娩時子宮弛緩出血、產後防止出血、產後子宮收縮不全 |
| 內衛藥製字第009847號 | 縮水蘋果酸麥角新鹼錠 | 錠劑 | 人人化學製藥股份有限公司 | 2027/12/31 | 產科用於產後促使子宮復原及預防出血過多、偏頭痛 |
| 內衛藥製字第009850號 | 〝人人〞縮水蘋果酸麥角新鹼注射液 | 注射劑 | 人人化學製藥股份有限公司 | 2029/12/31 | 產後或流產後促進子宮之復元及預防出血過多 |
| 內衛藥製字第012732號 | 縮水蘋果酸麥角新鹼片 | 錠劑 | 中生生技製藥股份有限公司淡水廠 | 2028/05/25 | 產後子宮肌張力弛緩而致之血崩症、偏頭痛 |
| 內衛藥製字第013083號 | 爾可利錠 | 錠劑 | 豐田藥品股份有限公司 | 2027/08/20 | 產褥期之出血、子宮內膜搔爬後之出血、流產後之出血、子宮弛緩之出血、子宮不正常出血、分娩第三期陣痛微弱 |
| 衛署藥製字第001605號 | 縮水蘋果酸麥角新/片 | 錠劑 | 中美兄弟製藥股份有限公司 | 2028/05/25 | 一般婦產科之出血（如分娩時子宮弛緩性出血、產褥期之出血、流產後出血、子宮內膜搔爬後之出血） |
| 衛署藥製字第003786號 | 麥角新 生僉 注射液 | 注射劑 | 安星製藥股份有限公司 | 2028/05/25 | 產後出血、子宮異常出血、流產後出血、分娩時子宮弛緩出血、分娩第三期陣痛微弱 |
| 衛署藥製字第014363號 | 縮水蘋果酸麥角新注射液 | 注射劑 | 台裕化學製藥廠股份有限公司 | 2030/02/27 | 分娩後之子宮弛緩、子宮收縮不全、弛緩性出血之預防及止血 |
| 衛署藥製字第015273號 | "應元"縮水蘋果酸麥角新鹼注射液 | 注射劑 | 應元化學製藥股份有限公司 | 2028/07/13 | 產褥期出血、促進產後子宮之復元及預防出血過多 |
| 衛署藥製字第017720號 | "優良"優復安錠（縮水蘋果酸麥角新鹼） | 錠劑 | 優良化學製藥股份有限公司 | 2029/06/01 | 預防及治療產後子宮出血 |
| 衛署藥製字第018516號 | "優良"優復安注射液（縮水蘋果酸麥角新鹼） | 注射劑 | 優良化學製藥股份有限公司 | 2028/08/31 | 生產後及流產後出血 |
| 衛署藥製字第024272號 | "正和"益兒宮糖衣錠（縮蘋果酸麥角新生僉） | 糖衣錠 | 正和製藥股份有限公司新營廠 | 2028/05/25 | 促進子宮收縮及治療子宮出血 |
| 衛署藥製字第029626號 | 意如宮注射液（縮水蘋果酸麥角新/） | 注射劑 | 永信藥品工業股份有限公司 | 2030/02/13 | 分娩後之子宮弛緩、子宮弛緩性出血、流產後出血、產褥期出血、子宮內膜刮除後出血之預防及治療、偏頭痛。 |
| 衛部藥輸字第027396號 | 縮蘋酸麥角新鹼 | （粉） | 新雙隆生技股份有限公司 | 2028/03/01 | 子宮收縮藥 |
| 衛部藥輸字第027478號 | 縮蘋酸麥角新生僉 | 粉劑 | 仁友興業股份有限公司 | 2028/07/26 | 子宮收縮藥 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（1 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 內衛藥製字第002200號 | 益兒可針 | ERGONOVINE MALEATE、ASCORBIC ACID (VIT C) | 注射劑 | 產褥期之出血、流產後之出血、分娩時之子宮弛緩性出血、不正常出血等 |

<details><summary><strong>已註銷</strong>（83 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第000046號</td><td>麥角新/錠</td><td>ERGONOVINE MALEATE</td><td>2002/09/02</td></tr><tr><td>內衛藥製字第000287號</td><td>益妳好－甲糖衣錠</td><td>MENADIONE (VIT K3)、CARBAZOCHROME、ERGONOVINE MALEATE、BENACTYZ…</td><td>1989/11/25</td></tr><tr><td>內衛藥製字第000390號</td><td>催娩糖衣錠</td><td>QUININE HCL、ERGONOVINE MALEATE、PAPAVERINE HCL</td><td>1993/07/29</td></tr><tr><td>內衛藥製字第001793號</td><td>保美通針</td><td>ERGONOVINE MALEATE、SPARTEINE SULFATE、ASCORBIC ACID (VIT C)</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第002701號</td><td>縮水蘋果酸麥角新/注射液０．０２％</td><td>ERGONOVINE MALEATE</td><td>2013/10/15</td></tr><tr><td>內衛藥製字第002908號</td><td>蘋果酸麥角新/注射液</td><td>ERGONOVINE MALEATE</td><td>2013/04/08</td></tr><tr><td>內衛藥製字第003182號</td><td>麥角蘋注射液</td><td>ERGONOVINE MALEATE</td><td>2016/01/19</td></tr><tr><td>內衛藥製字第003242號</td><td>安產糖衣錠</td><td>ETHAVERINE HCL (eq to BALBONIN) (eq to Ethylpapaverine HCl)、…</td><td>2000/08/04</td></tr><tr><td>內衛藥製字第004304號</td><td>縮水蘋果酸麥角新/糖衣片</td><td>ERGONOVINE MALEATE</td><td>2015/04/15</td></tr><tr><td>內衛藥製字第004784號</td><td>縮水蘋果酸麥角新鹼錠０．２公絲</td><td>ERGONOVINE MALEATE</td><td>1998/03/31</td></tr><tr><td>內衛藥製字第005085號</td><td>益婦明注</td><td>ERGONOVINE MALEATE</td><td>1998/12/24</td></tr><tr><td>內衛藥製字第005177號</td><td>縮水蘋果酸麥角新/錠</td><td>ERGONOVINE MALEATE</td><td>2013/10/01</td></tr><tr><td>內衛藥製字第006364號</td><td>麥托年錠</td><td>ERGONOVINE MALEATE</td><td>1993/07/20</td></tr><tr><td>內衛藥製字第006925號</td><td>益婦明片</td><td>ERGONOVINE MALEATE</td><td>2013/06/10</td></tr><tr><td>內衛藥製字第007126號</td><td>益爾康美得林注射液</td><td>ASCORBIC ACID (VIT C)、ERGONOVINE MALEATE</td><td>1991/06/05</td></tr><tr><td>內衛藥製字第009320號</td><td>娩可敏糖衣錠</td><td>ERGONOVINE MALEATE</td><td>2010/11/18</td></tr><tr><td>內衛藥製字第013362號</td><td>誘娩膠囊</td><td>ERGONOVINE MALEATE、QUININE HCL、PAPAVERINE HCL</td><td>2013/07/11</td></tr><tr><td>內衛藥製字第013372號</td><td>益爾可錠</td><td>ERGONOVINE MALEATE</td><td>2013/10/07</td></tr><tr><td>內衛藥製字第013902號</td><td>縮水蘋果酸麥角新鹼片</td><td>ERGONOVINE MALEATE</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第015148號</td><td>蘋果酸麥角新鹼片</td><td>ERGONOVINE MALEATE</td><td>2013/10/07</td></tr><tr><td>內衛藥輸字第002548號</td><td>美生露</td><td>ERGONOVINE MALEATE</td><td>2000/10/20</td></tr><tr><td>內衛藥輸字第002635號</td><td>美生露片</td><td>ERGONOVINE MALEATE</td><td>2000/10/20</td></tr><tr><td>內衛藥輸字第002865號</td><td>新多美定</td><td>ERGONOVINE MALEATE、OXYTOCIN</td><td>1985/12/26</td></tr><tr><td>內衛藥輸字第004358號</td><td>蘋果酸麥角新鹼注射液</td><td>ERGONOVINE MALEATE</td><td>1984/06/05</td></tr><tr><td>內衛藥輸字第004803號</td><td>蘋果酸麥角新鹼針</td><td>ERGONOVINE MALEATE</td><td>1986/06/20</td></tr><tr><td>內衛藥輸字第005356號</td><td>斯肯麥角新鹼針</td><td>ERGONOVINE MALEATE</td><td>1986/01/16</td></tr><tr><td>內衛藥輸字第005357號</td><td>斯肯麥角新鹼片</td><td>ERGONOVINE MALEATE</td><td>1987/03/24</td></tr><tr><td>內衛藥輸字第005361號</td><td>雅克麥角新鹼片</td><td>ERGONOVINE MALEATE</td><td>2000/10/16</td></tr><tr><td>內衛藥輸字第005918號</td><td>歐葛百新</td><td>ERGONOVINE MALEATE</td><td>1991/02/01</td></tr><tr><td>內衛藥輸字第006176號</td><td>歐葛百新</td><td>ERGONOVINE MALEATE</td><td>1991/02/01</td></tr><tr><td>內衛藥輸字第006507號</td><td>縮水蘋果酸麥角新/</td><td>ERGONOVINE MALEATE</td><td>1985/09/17</td></tr><tr><td>內衛藥輸字第007931號</td><td>速把得寧</td><td>CARBAZOCHROME、METHYL HESPERIDIN、SPARTEINE SULFATE、ERGONOVINE…</td><td>1991/01/31</td></tr><tr><td>內衛藥輸字第008322號</td><td>蘋果酸麥角新/注射液</td><td>ERGONOVINE MALEATE</td><td>2000/10/20</td></tr><tr><td>衛署藥製字第000295號</td><td>易爾果速注射液</td><td>SPARTEINE SULFATE、ERGONOVINE MALEATE、ASCORBATE (SODIUM)</td><td>1991/05/06</td></tr><tr><td>衛署藥製字第000360號</td><td>易生注射液</td><td>OXYTOCIN、ERGONOVINE MALEATE</td><td>1991/05/20</td></tr><tr><td>衛署藥製字第002549號</td><td>意如宮錠</td><td>ERGONOVINE MALEATE</td><td>1987/08/21</td></tr><tr><td>衛署藥製字第004289號</td><td>娩朗糖衣錠</td><td>PAPAVERINE HCL、QUININE HCL、ERGONOVINE MALEATE</td><td>2023/07/03</td></tr><tr><td>衛署藥製字第005278號</td><td>縮水蘋果酸麥角新鹼注射液０．２公絲</td><td>ERGONOVINE MALEATE</td><td>2009/10/21</td></tr><tr><td>衛署藥製字第005279號</td><td>伊舒宮錠</td><td>ERGONOVINE MALEATE</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第005426號</td><td>縮水蘋果酸麥角新/錠</td><td>ERGONOVINE MALEATE</td><td>1988/12/31</td></tr><tr><td>衛署藥製字第005992號</td><td>能利娩膠囊</td><td>ERGONOVINE MALEATE、QUININE HCL、PAPAVERINE HCL</td><td>1999/08/23</td></tr><tr><td>衛署藥製字第006003號</td><td>"大豐"麥角新鹼膜衣錠</td><td>ERGONOVINE MALEATE</td><td>2025/05/29</td></tr><tr><td>衛署藥製字第008916號</td><td>意如宮注射液</td><td>ERGONOVINE MALEATE</td><td>1987/06/19</td></tr><tr><td>衛署藥製字第010370號</td><td>醫宮能錠</td><td>ERGONOVINE MALEATE</td><td>2000/08/04</td></tr><tr><td>衛署藥製字第010664號</td><td>益護注射液</td><td>SPARTEINE SULFATE、ERGONOVINE MALEATE</td><td>2007/05/09</td></tr><tr><td>衛署藥製字第013503號</td><td>縮水蘋果酸麥角新/錠</td><td>ERGONOVINE MALEATE</td><td>2014/06/11</td></tr><tr><td>衛署藥製字第013714號</td><td>縮水蘋果酸麥角新鹼糖衣錠</td><td>ERGONOVINE MALEATE</td><td>2014/11/19</td></tr><tr><td>衛署藥製字第014299號</td><td>縮水蘋果酸麥角新/糖衣錠</td><td>ERGONOVINE MALEATE</td><td>1989/08/17</td></tr><tr><td>衛署藥製字第014317號</td><td>縮免停注射液</td><td>ERGONOVINE MALEATE、SPARTEINE SULFATE</td><td>2007/05/09</td></tr><tr><td>衛署藥製字第014426號</td><td>娩可敏錠０．２公絲</td><td>ERGONOVINE MALEATE</td><td>2010/11/18</td></tr><tr><td>衛署藥製字第015117號</td><td>縮水蘋果酸麥角新/錠</td><td>ERGONOVINE MALEATE</td><td>2013/10/15</td></tr><tr><td>衛署藥製字第015831號</td><td>縮水蘋果酸麥角新/注射液</td><td>ERGONOVINE MALEATE</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第015832號</td><td>縮水蘋果酸麥角新/錠</td><td>ERGONOVINE MALEATE</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第016941號</td><td>縮水蘋果酸麥角新鹼錠　〝順華〞</td><td>ERGONOVINE MALEATE</td><td>2016/09/12</td></tr><tr><td>衛署藥製字第017820號</td><td>縮水蘋果酸麥角新/錠</td><td>ERGONOVINE MALEATE</td><td>2022/05/05</td></tr><tr><td>衛署藥製字第017980號</td><td>安宮能錠０．５公絲（縮水蘋果酸麥角新鹼）</td><td>ERGONOVINE MALEATE</td><td>2005/11/14</td></tr><tr><td>衛署藥製字第019170號</td><td>縮保宮糖衣錠</td><td>BENACTYZINE HCL、ERGONOVINE MALEATE、SPARTEINE SULFATE、MENADIO…</td><td>1987/06/02</td></tr><tr><td>衛署藥製字第019262號</td><td>縮水蘋果酸麥角新鹼錠</td><td>ERGONOVINE MALEATE</td><td>2013/10/15</td></tr><tr><td>衛署藥製字第023151號</td><td>縮蘋果酸麥角新鹼糖衣錠</td><td>ERGONOVINE MALEATE</td><td>2024/01/04</td></tr><tr><td>衛署藥製字第023727號</td><td>益婦康糖衣錠</td><td>METHYL HESPERIDIN、CARBAZOCHROME、SPARTEINE SULFATE、ERGONOVINE…</td><td>2007/05/09</td></tr><tr><td>衛署藥製字第024528號</td><td>縮蘋果酸麥角新鹼注射液０．２公絲/公撮</td><td>ERGONOVINE MALEATE</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第024674號</td><td>益宮縮注射液</td><td>ERGONOVINE MALEATE、SPARTEINE SULFATE</td><td>2007/05/09</td></tr><tr><td>衛署藥製字第026113號</td><td>樂你康錠</td><td>ERGONOVINE MALEATE、SPARTEINE SULFATE、MENADIONE (VIT K3)、ETHE…</td><td>2007/05/09</td></tr><tr><td>衛署藥製字第033769號</td><td>易爾果速注射液</td><td>ASCORBIC ACID (VIT C)、ERGONOVINE MALEATE、SPARTEINE SULFATE</td><td>2000/08/04</td></tr><tr><td>衛署藥製字第033875號</td><td>易生注射液</td><td>ERGONOVINE MALEATE、OXYTOCIN</td><td>1998/03/02</td></tr><tr><td>衛署藥輸字第001981號</td><td>麥角新/片</td><td>ERGONOVINE MALEATE、MAGNESIUM ALUMINUM METASILICATE (NEUSILIN…</td><td>1988/11/08</td></tr><tr><td>衛署藥輸字第002223號</td><td>縮水蘋果酸麥角新/</td><td>ERGONOVINE MALEATE</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第002689號</td><td>縮水蘋果酸麥角新/</td><td>ERGONOVINE MALEATE</td><td>1993/02/16</td></tr><tr><td>衛署藥輸字第002829號</td><td>縮水蘋果酸麥角新/</td><td>ERGONOVINE MALEATE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第003625號</td><td>縮水蘋果酸麥角新/</td><td>ERGONOVINE MALEATE</td><td>2000/09/05</td></tr><tr><td>衛署藥輸字第003728號</td><td>縮水蘋果酸麥角新/</td><td>ERGONOVINE MALEATE</td><td>1990/07/03</td></tr><tr><td>衛署藥輸字第003742號</td><td>保婦針</td><td>SPARTEINE SULFATE、ERGONOVINE MALEATE、ASCORBIC ACID (VIT C)</td><td>1990/10/11</td></tr><tr><td>衛署藥輸字第003755號</td><td>保婦丸</td><td>ERGONOVINE MALEATE、DIMETHYLAMINOETHYL-BETA-BENZILAMIDE HCL、S…</td><td>1990/10/11</td></tr><tr><td>衛署藥輸字第004804號</td><td>縮水蘋果酸麥角新/</td><td>ERGONOVINE MALEATE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第006943號</td><td>縮水蘋果酸麥角新鹼</td><td>ERGONOVINE MALEATE</td><td>1998/06/17</td></tr><tr><td>衛署藥輸字第011359號</td><td>麥角新/糖衣錠０、５公絲</td><td>ERGONOVINE MALEATE</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第011840號</td><td>縮水蘋果酸麥角新/粉劑</td><td>ERGONOVINE MALEATE</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第012615號</td><td>收縮寧錠</td><td>ERGONOVINE MALEATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第012762號</td><td>蘋果酸麥角新鹼</td><td>ERGONOVINE MALEATE</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第014054號</td><td>縮蘋果酸麥角新/粉劑</td><td>ERGONOVINE MALEATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第014478號</td><td>欣多美定注射液５ＩＵ/ＭＬ</td><td>OXYTOCIN、ERGONOVINE MALEATE</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第014603號</td><td>麥角新/注射液０．５公絲/公撮</td><td>ERGONOVINE MALEATE</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第017934號</td><td>縮水蘋果酸麥角新/</td><td>ERGONOVINE MALEATE</td><td>2005/06/16</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

---

## 安全性考量

**藥物交互作用**（資料庫共收錄 83 筆；下表列出 Major 級別交互作用）：

| 交互作用藥物 | 嚴重程度 |
|-------------|---------|
| Isometheptene | Major |
| Epinephrine | Major |
| Epinephrine (topical) | Major |
| Ephedrine | Major |
| Lorcaserin | Major |
| Clarithromycin | Major |
| Cobicistat | Major |

Moderate 級別交互作用包含：Doxycycline、Aprepitant、Dexamethasone、Tetracycline、Cimetidine、Minocycline、Miconazole、Clotrimazole 等（共 76 筆）。

> 安全性警語及禁忌症資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
偏頭痛預測具備 L3 等級觀察性研究證據，多篇臨床觀察研究支持 Ergometrine 及其半合成同系物 methylergonovine 用於月經性偏頭痛預防與頑固性偏頭痛治療；尤其台灣現行仿單已核准「偏頭痛」適應症，法規路徑比一般再利用案例更為順暢。然而，目前仍缺乏高等級 RCT 證據，且血管收縮特性帶來特定族群的安全疑慮，需謹慎規劃。

<!-- review:begin ergometrine-methylergonovine-not-metabolite-conclusion-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「Ergometrine 及其活性代謝物 methylergonovine」。同上，methylergonovine 是 ergometrine 的半合成同系物而非代謝物；結論的判斷未改。依據：[NLM MeSH：Methylergonovine（D008755）](https://meshb.nlm.nih.gov/record/ui?ui=D008755)；[DailyMed：Methylergonovine Maleate Tablets, USP 仿單（Teva）](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d8e4b8ed-3289-4611-8a61-2392a4bf6072)。

<!-- review:end ergometrine-methylergonovine-not-metabolite-conclusion-2026-10-03 -->

**若要推進需要：**
- 補充 DrugBank MOA 詳細資料，確認 5-HT1B/1D 受體及 α-腎上腺素受體作用機轉
- 設計前瞻性 RCT 或登記式觀察研究，填補 L1/L2 級別證據缺口
- 建立心血管安全監測計畫，特別針對 Major DDI 藥物（Epinephrine、Ephedrine、Cobicistat）及合併冠心病、高血壓患者
- **肺動脈高壓患者（TxGNN 第 10 名預測）為明確安全疑慮族群**：Ergometrine 在此族群可能誘發急性肺高壓危象（見文獻 PMID 26050249），應列為禁忌評估
- 評估是否申請「偏頭痛」正式適應症擴充，利用既有台灣仿單先例加速審查

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「methylergonovine 是 ergometrine 的活性代謝物」 | 更正 | [NLM MeSH：Methylergonovine（D008755）](https://meshb.nlm.nih.gov/record/ui?ui=D008755)；[DailyMed：Methylergonovine Maleate Tablets, USP 仿單（Teva）](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d8e4b8ed-3289-4611-8a61-2392a4bf6072)；[emc：Ergometrine Injection BP 0.05% w/v SmPC §5.2](https://www.medicines.org.uk/emc/product/6265/smpc) |
| 2026-10-03 | 結論段「及其活性代謝物 methylergonovine」 | 更正 | [NLM MeSH：Methylergonovine（D008755）](https://meshb.nlm.nih.gov/record/ui?ui=D008755)；[DailyMed：Methylergonovine Maleate Tablets, USP 仿單（Teva）](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d8e4b8ed-3289-4611-8a61-2392a4bf6072) |
| 2026-10-03 | 預測理由「作用於 α-腎上腺素受體抑制三叉神經源性炎症」 | 加註 | [emc：Ergometrine Injection BP 0.05% w/v SmPC §5.1](https://www.medicines.org.uk/emc/product/6265/smpc) |
| 2026-10-03 | 偏頭痛預測標記待重審 | 標記待重審 → 已重審（見下列重審結果） | [emc：Ergometrine Injection BP 0.05% w/v SmPC §5.1](https://www.medicines.org.uk/emc/product/6265/smpc) |
| 2026-10-03 | 新增「作用機轉」段（每點附仿單來源） | 新增附來源段落 | [emc：Ergometrine Injection BP 0.05% w/v SmPC §5.1](https://www.medicines.org.uk/emc/product/6265/smpc) |
| 2026-10-03 | 偏頭痛預測重審結果 | 重審：維持，證據等級 L3 不變 | [PubMed：Menstrual migraine and intermittent ergonovine therapy（PMID 2759844）](https://pubmed.ncbi.nlm.nih.gov/2759844/)；[PubMed：Microiontophoretic application of serotonin (5HT)1B/1D agonists inhibits trigeminal cell firing in the cat（PMID 9448572）](https://pubmed.ncbi.nlm.nih.gov/9448572/)；[PubMed：Oral methylergonovine maleate for refractory migraine and cluster headache prevention（PMID 23432443）](https://pubmed.ncbi.nlm.nih.gov/23432443/)；[PubMed：Efficacy and tolerability of intravenous methylergonovine in migraine female patients attending the emergency department: a pilot open-label study（PMID 19895705）](https://pubmed.ncbi.nlm.nih.gov/19895705/)；[PubMed：QT prolongation, Torsade de Pointes, myocardial ischemia from coronary vasospasm, and headache medications. Part 1: review of serotonergic cardiac adverse events with a triptan case（PMID 23216317）](https://pubmed.ncbi.nlm.nih.gov/23216317/)；[PubMed：Pleural thickening caused by Sansert and Ergotrate in the treatment of migraine（PMID 6773347）](https://pubmed.ncbi.nlm.nih.gov/6773347/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

