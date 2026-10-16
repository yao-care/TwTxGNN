---
layout: default
title: Letrozole
parent: 高證據等級 (L1-L2)
nav_order: 165
evidence_level: L1
indication_count: 10
---

# Letrozole
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

# Letrozole：從乳癌到女性乳癌（荷爾蒙受體陽性）

## 一句話總結

Letrozole 是非固醇類芳香環轉化酶（aromatase）抑制劑，原本用於停經後荷爾蒙受體陽性乳癌的治療。
TxGNN 模型預測它對**女性乳癌 (Female Breast Carcinoma)** 有效，目前有 **41 個臨床試驗**和 **19 篇文獻**支持這個方向，其中包含多項 Phase 3 試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 接受抗動情激素治療失敗的自然或人工停經後之末期乳癌病人之治療；停經後之局部晚期或轉移性乳癌婦女患者之第一線治療；荷爾蒙接受器呈陽性及淋巴結轉移陽性之乳癌病人作為 Tamoxifen 輔助療法之後的延伸治療；停經後荷爾蒙接受器呈陽性之初期乳癌病人之輔助治療 |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L1 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 16 張（有效單方 9／有效複方 0／已註銷 7） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）原始資料。就已知資訊，Letrozole 是非固醇類芳香環轉化酶抑制劑，能阻斷雄激素轉化為雌激素，使依賴雌激素生長的荷爾蒙敏感型乳癌失去生長訊號。這也是它現有乳癌適應症的核心機轉。

需要說明的是：「女性乳癌」本質上與 Letrozole 現有適應症高度重疊，屬於同一疾病領域。因此這項預測較接近「確認並涵蓋既有用途」，而非跨疾病的全新用途。

另外，此預測成立的前提是腫瘤為荷爾蒙受體陽性。支持證據幾乎都來自 ER+/HR+ 的族群，對受體陰性的乳癌，機轉上不預期有效。

## 臨床試驗證據

以下列出與 Letrozole 最相關的試驗（依相關性與階段挑選，共 10 項）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02941926](https://clinicaltrials.gov/study/NCT02941926) | Phase 3 | 完成 | 3246 | Ribociclib 併用 Letrozole 用於 HR+/HER2- 晚期乳癌的安全性與療效（含男性及停經前後女性） |
| [NCT02600923](https://clinicaltrials.gov/study/NCT02600923) | Phase 3 | 完成 | 131 | Palbociclib 併用 Letrozole 用於停經後 HR+/HER2- 晚期乳癌（拉丁美洲用藥可近性研究） |
| [NCT01740427](https://clinicaltrials.gov/study/NCT01740427) | Phase 3 | 完成 | 666 | PALOMA-2：Palbociclib + Letrozole 對比安慰劑 + Letrozole，用於未接受過晚期治療的 ER+/HER2- 乳癌 |
| [NCT00382070](https://clinicaltrials.gov/study/NCT00382070) | Phase 3 | 狀態未知 | 3966 | 完成 5 年荷爾蒙治療後，延長 5 年 Letrozole 對比安慰劑，評估無病存活期 |
| [NCT00908531](https://clinicaltrials.gov/study/NCT00908531) | Phase 3 | 提前終止 | 123 | 術前 4 個月 Letrozole 對比先手術，用於停經後可手術的 HR+ 腫瘤 |
| [NCT03425838](https://clinicaltrials.gov/study/NCT03425838) | Phase 3 | 進行中 | 1050 | SONIA：芳香環轉化酶抑制劑加 CDK4/6 抑制劑用於第一線或第二線的順序比較 |
| [NCT04272801](https://clinicaltrials.gov/study/NCT04272801) | Phase 2 | 進行中 | 84 | 老年早期 ER+ 乳癌病人術前荷爾蒙治療窗口期研究 |
| [NCT04568616](https://clinicaltrials.gov/study/NCT04568616) | Phase 2 | 進行中 | 178 | NAOMI：停經後 ER+/HER2- 乳癌術前 Letrozole 4–24 週的分子分析 |
| [NCT01439711](https://clinicaltrials.gov/study/NCT01439711) | Phase 2 | 完成 | 108 | 停經後 ER+ 乳管原位癌術前 Letrozole |
| [NCT02344550](https://clinicaltrials.gov/study/NCT02344550) | Phase 2 | 完成 | 137 | 停經前轉移性乳癌：卵巢抑制 + Letrozole + Everolimus |

> 說明：上述多數試驗是以 Letrozole 作為荷爾蒙治療主幹，搭配 CDK4/6 抑制劑等新藥，因此提供的是「Letrozole 為標準治療基礎」的間接支持。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35263519](https://pubmed.ncbi.nlm.nih.gov/35263519/) | 2022 | RCT | N Engl J Med | MONALEESA-2：Ribociclib + Letrozole 用於 HR+/HER2- 晚期乳癌的整體存活分析 |
| [29718092](https://pubmed.ncbi.nlm.nih.gov/29718092/) | 2018 | RCT | Ann Oncol | MONALEESA-2 更新：第一線 Ribociclib + Letrozole 延長無惡化存活期，毒性可控 |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | Review | Life Sci | Letrozole 的藥理、毒性與潛在治療效果 |
| [20095792](https://pubmed.ncbi.nlm.nih.gov/20095792/) | 2010 | Review | Expert Opin Drug Metab Toxicol | 第三代芳香環轉化酶抑制劑 Letrozole 的藥效、藥動、療效與安全性 |
| [21364577](https://pubmed.ncbi.nlm.nih.gov/21364577/) | 2011 | Review | Br J Cancer | 比較 Anastrozole 與 Letrozole 的臨床差異 |
| [30632023](https://pubmed.ncbi.nlm.nih.gov/30632023/) | 2019 | Cohort | Breast Cancer Res Treat | PALOMA-2 延長追蹤：Palbociclib + Letrozole 的持續獲益 |
| [31190621](https://pubmed.ncbi.nlm.nih.gov/31190621/) | 2019 | Cohort | Pharmacogenomics | SLCO1B1 多型性與接受 Letrozole／Exemestane 病人血漿雌激素濃度的關聯 |
| [19380449](https://pubmed.ncbi.nlm.nih.gov/19380449/) | 2009 | Phase 2 隨機試驗 | J Clin Oncol | 術前 Everolimus + Letrozole 對比安慰劑 + Letrozole 用於 ER+ 乳癌 |
| [16621229](https://pubmed.ncbi.nlm.nih.gov/16621229/) | 2006 | Review | Eur J Obstet Gynecol Reprod Biol | Tamoxifen 後延長使用 Letrozole 的原因、對象與期間 |
| [12113048](https://pubmed.ncbi.nlm.nih.gov/12113048/) | 2002 | Review | Expert Rev Anticancer Ther | Letrozole 作為轉移性停經後乳癌第一線治療，優於 Tamoxifen |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Letrozole 的不重複許可證共 **16 張**：有效單方 9 張、有效複方 0 張、已註銷 7 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（9 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第048901號 | “台灣神隆”立妥柔 | （粉） | 台灣神隆股份有限公司 | 2027/07/19 | 轉移性乳癌。 |
| 衛署藥製字第057732號 | 萊諾妥膜衣錠2.5毫克 | 膜衣錠 | 培力藥品工業股份有限公司 | 2027/11/05 | 接受抗動情激素治療失敗的自然或人工停經後之末期乳癌病人之治療，停經後之局部晚期或轉移性乳癌婦女患者之第一線治療用藥。荷爾蒙接受器呈陽性及LN metastasis positive… |
| 衛署藥輸字第022462號 | 復乳納膜衣錠2.5毫克 | 膜衣錠 | 台灣諾華股份有限公司 | 2029/04/20 | 接受抗動情激素治療失敗的自然或人工停經後之末期乳癌病人之治療。停經後之局部晚期或轉移性乳癌婦女患者之第一線治療用藥。荷爾蒙接受器呈陽性及LN METASTASIS POSITIVE… |
| 衛部藥製字第058819號 | 輔適納膜衣錠2.5毫克 | 膜衣錠 | 中國化學製藥股份有限公司新豐工廠 | 2030/08/24 | 接受抗動情激素治療失敗的自然或人工停經後之末期乳癌病人之治療。停經後之局部晚期或轉移性乳癌婦女患者之第一線治療用藥。荷爾蒙接受器呈陽性及LN METASTASIS POSITIVE… |
| 衛部藥輸字第026206號 | 利妥柔膜衣錠2.5毫克 | 膜衣錠 | 美時化學製藥股份有限公司 | 2028/12/02 | 接受抗動情激素治療失敗的自然或人工停經後之末期乳癌病人之治療。停經後之局部晚期或轉移性乳癌婦女患者之第一線治療用藥。荷爾蒙接受器呈陽性及LN METASTASIS POSITIVE… |
| 衛部藥輸字第026313號 | 萊特汝膜衣錠2.5毫克 | 膜衣錠 | 凱沛爾藥品有限公司 | 2029/05/12 | 接受抗動情激素治療失敗的自然或人工停經後之末期乳癌病人之治療。停經後之局部晚期或轉移性乳癌婦女患者之第一線治療用藥。荷爾蒙接受器呈陽性及LN METASTASIS POSITIVE… |
| 衛部藥輸字第026581號 | 利乳寧膜衣錠2.5毫克 | 膜衣錠 | 昱泰藥品股份有限公司 | 2030/08/05 | 接受抗動情激素治療失敗的自然或人工停經後之末期乳癌病人之治療。停經後之局部晚期或轉移性乳癌婦女患者之第一線治療用藥。荷爾蒙接受器呈陽性及LN METASTASIS POSITIVE… |
| 衛部藥輸字第027485號 | 利妥唑 | （粉） | 恒亞貿易股份有限公司 | 2028/07/31 | 非固醇性抗雌激素藥 |
| 衛部藥輸字第028712號 | 立妥芙膜衣錠2.5毫克 | 膜衣錠 | 毅有生技醫藥股份有限公司 | 2029/06/21 | 接受抗動情激素治療失敗的自然或人工停經後之末期乳癌病人之治療。停經後之局部晚期或轉移性乳癌婦女患者之第一線治療用藥。 荷爾蒙接受器呈陽性及LN METASTASIS POSITIV… |

<details><summary><strong>已註銷</strong>（7 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第025143號</td><td>特羅捷膜衣錠2.5毫克</td><td>LETROZOLE</td><td>2022/07/06</td></tr><tr><td>衛部藥輸字第026108號</td><td>益乳寧膜衣錠2.5毫克</td><td>LETROZOLE</td><td>2025/06/09</td></tr><tr><td>衛部藥輸字第026127號</td><td>蕾卓洛膜衣錠2.5毫克</td><td>LETROZOLE</td><td>2025/04/29</td></tr><tr><td>衛部藥輸字第026333號</td><td>艾爾芬膜衣錠2.5毫克</td><td>LETROZOLE</td><td>2020/04/10</td></tr><tr><td>衛部藥輸字第026564號</td><td>"精金"蕾乳妥膜衣錠2.5毫克</td><td>LETROZOLE</td><td>2022/06/16</td></tr><tr><td>衛部藥輸字第027448號</td><td>法萌樂膜衣錠</td><td>LETROZOLE</td><td>2026/02/11</td></tr><tr><td>衛部藥輸字第027594號</td><td>利妥唑</td><td>Letrozole</td><td>2025/04/24</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

Letrozole 為荷爾蒙治療藥物（芳香環轉化酶抑制劑），不屬於傳統細胞毒性化療藥。本次資料中缺乏細胞毒性相關資訊，請參考原廠仿單的警語與注意事項。

## 安全性考量

- **知識圖譜標示的潛在禁忌／風險疾病**（來自藥物－疾病關聯資料，並非仿單文字，需與仿單核對）：肝衰竭、肝硬化、骨質疏鬆（含停經後骨質疏鬆）、高膽紅素血症（含遺傳性高膽紅素血症、Gilbert 症候群）、腦血管疾病。
- **藥物交互作用**：資料庫共記錄 259 筆交互作用。其中明確分級為中度者包括 Aprepitant；其餘列出的（如 Calcitriol、Glimepiride、Lansoprazole、Metformin、Omeprazole、Prednisone、Simvastatin 等）等級為未知，需進一步評估。
- 臨床試驗與文獻中也曾提及芳香環轉化酶抑制劑相關的關節痛／肌痛、骨骼不良反應，以及個案報告中的黃斑部病變。

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- Letrozole 在女性乳癌（荷爾蒙受體陽性）有多項已完成的 Phase 3 試驗及高等級文獻支持，且已在台灣取得相同領域的核准適應症，證據充分。
- 但此預測與既有適應症高度重疊，且僅適用於 HR+ 族群，需設下適用範圍的護欄。

**若要推進需要：**
- 明確限定適用族群：荷爾蒙受體陽性、停經後（或停經前併用卵巢抑制）；不應推廣至 ER 陰性乳癌。
- 補齊作用機轉（MOA）資料與仿單警語、禁忌的正式內容。
- 建立骨密度、肝功能與心血管風險的監測計畫（對照知識圖譜所列風險疾病）。
- 審視 DDI 清單，確認併用藥物（特別是中度交互作用藥物）的處置原則。
- 其他預測（如 ER 陰性乳癌、Ehrlich 腫瘤、纖維囊腫等）證據薄弱或機轉不支持，不建議納入本次推進範圍。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「雌激素降幅超過 95%」 | 報告重生後已無此錯誤（2026-10-15：新報告未再寫雌激素降幅超過 95%；原為更正） | [DailyMed：Femara (letrozole) tablets 仿單（Novartis），Pharmacodynamics](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=82b77d74-085f-45ac-a7dd-1f5c038bf406) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

