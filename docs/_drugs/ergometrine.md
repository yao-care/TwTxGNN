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

Ergometrine 是麥角生物鹼類藥物，原本作為子宮收縮劑用於產後出血與相關出血症狀，台灣已有 20 張許可證。TxGNN 模型對其預測了 10 個潛在新適應症；其中 **偏頭痛 (Migraine Disorder)** 是最具臨床意義的預測，目前有 **20 篇文獻**支持，且部分台灣核准仿單已明列「偏頭痛」，具備監理先例。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 產後出血、子宮血崩、月經過多 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

<!-- review:begin ergometrine-migraine-rereview-2026-10-03 -->

> **待重審（2026-10-03）**：偏頭痛這筆預測的機轉理由前提與仿單不符（見下方「為什麼這個預測合理」的查核加註），已標記待重審；證據等級、文獻與決策在重審完成前不更動。依據：[emc：Ergometrine Injection BP 0.05% w/v SmPC §5.1](https://www.medicines.org.uk/emc/product/6265/smpc)。

<!-- review:end ergometrine-migraine-rereview-2026-10-03 -->

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

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 內衛藥製字第004304號 | 縮水蘋果酸麥角新/糖衣片 | 糖衣錠 | 產後出血、子宮血崩、月經過多 |
| 內衛藥製字第004784號 | 縮水蘋果酸麥角新鹼錠０．２公絲 | 錠劑 | 子宮弛緩、胎盤剝離後之出血、子宮收縮不全、第３期陣痛微弱、子宮出血、流產 |
| 內衛藥輸字第004803號 | 蘋果酸麥角新鹼針 | 注射劑 | 產後促進子宮收縮、分娩後出血、剖腹取兒手術時之出血 |
| 內衛藥輸字第005918號 | 歐葛百新 | 注射劑 | 產後子宮收縮劑 |
| 內衛藥製字第001749號 | "強生"縮水蘋果酸麥角新鹼膜衣錠０．２毫克 | 膜衣錠 | 產褥期之出血、流產後之出血、分娩時之子宮弛緩出血、不正常出血、分娩第三期陣痛微弱 |

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
| 2026-10-03 | 偏頭痛預測標記待重審 | 標記待重審 | [emc：Ergometrine Injection BP 0.05% w/v SmPC §5.1](https://www.medicines.org.uk/emc/product/6265/smpc) |
| 2026-10-03 | 新增「作用機轉」段（每點附仿單來源） | 新增附來源段落 | [emc：Ergometrine Injection BP 0.05% w/v SmPC §5.1](https://www.medicines.org.uk/emc/product/6265/smpc) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

