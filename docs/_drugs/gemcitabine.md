---
layout: default
title: Gemcitabine
parent: 高證據等級 (L1-L2)
nav_order: 123
evidence_level: L1
indication_count: 10
---

# Gemcitabine
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

# Gemcitabine：從非小細胞肺癌、胰臟癌等多種癌症到乳癌

## 一句話總結

Gemcitabine 是一種核苷類似物化療藥物，原本用於非小細胞肺癌、胰臟癌、膀胱癌與膽道癌等治療。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效，
目前有 **多項乳癌相關臨床試驗**（含已完成的 Phase 3 試驗）和 **多篇文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 非小細胞肺癌、胰臟癌、膀胱癌、膽道癌；與 paclitaxel 併用於曾使用 anthracycline 之局部復發且無法手術切除或轉移性乳癌；曾使用含鉑類藥物治療後復發且間隔至少 6 個月之卵巢癌（第二線） |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L1 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張（有效單方 6／有效複方 5／已註銷 9） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Gemcitabine 是核苷類似物類的抗代謝化療藥物，其活性代謝物可抑制核糖核苷酸還原酶並嵌入 DNA，造成 DNA 鏈終止與細胞凋亡，對快速增殖的腫瘤細胞有作用。

在台灣，Gemcitabine 已被核准與 paclitaxel 併用，治療曾使用 anthracycline 之局部復發且無法手術切除或轉移性乳癌。這代表「乳癌」在特定族群（已使用過 anthracycline 者）已有法規認可的用途。因此 TxGNN 的預測較像是把用途延伸到更廣的乳癌族群，例如三陰性乳癌、HER2 陽性乳癌，以及早期乳癌的輔助或前導治療，而不是全新的方向。

乳癌與原適應症中的卵巢癌、肺癌同屬需要細胞毒性化療的實體腫瘤，Gemcitabine 與 taxane、platinum、anthracycline 等藥物的併用組合，已有多項臨床研究探討。

## 臨床試驗證據

以下列出與乳癌最相關的試驗（已依資料中的相關性評級挑選）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | 完成 | 未提供 | Gemcitabine + paclitaxel vs. paclitaxel，用於無法切除、局部復發或轉移性乳癌；為現行標示適應症的關鍵試驗 |
| [NCT00093795](https://clinicaltrials.gov/study/NCT00093795) | Phase 3 | 完成 | 4894 | 淋巴結陽性乳癌術後輔助治療，比較 TAC、劑量密集 AC→P 與加入 gemcitabine 的 DD AC→PG |
| [NCT00039546](https://clinicaltrials.gov/study/NCT00039546) | Phase 3 | 狀態未知 | 未提供 | tAnGo 試驗：ER/PgR 低表現之早期乳癌，在含 paclitaxel、epirubicin 的輔助化療中加入 gemcitabine |
| [NCT00408408](https://clinicaltrials.gov/study/NCT00408408) | Phase 3 | 狀態未知 | 1206 | 可手術乳癌的前導化療，評估在 docetaxel 中加入 capecitabine 或 gemcitabine 對病理完全緩解率的影響 |
| [NCT00070278](https://clinicaltrials.gov/study/NCT00070278) | Phase 3 | 狀態未知 | 800 | 高風險早期乳癌的前導化療，比較 EC 序貫 paclitaxel 加或不加 gemcitabine |
| [NCT00006007](https://clinicaltrials.gov/study/NCT00006007) | Phase 2 | 完成 | 59 | Pemetrexed 併用 gemcitabine 治療轉移性乳癌 |
| [NCT00244933](https://clinicaltrials.gov/study/NCT00244933) | Phase 2 | 完成 | 19 | Gemcitabine 併用 genistein 治療第 IV 期乳癌，並進行生物標記分析 |
| [NCT00003540](https://clinicaltrials.gov/study/NCT00003540) | Phase 2 | 完成 | 30 | 單用 gemcitabine 治療曾接受 doxorubicin 與 paclitaxel 的轉移性乳癌 |
| [NCT06027268](https://clinicaltrials.gov/study/NCT06027268) | Phase 2 | 進行中（不再招募） | 36 | Trilaciclib、pembrolizumab、gemcitabine 與 carboplatin 用於轉移性三陰性乳癌 |
| [NCT07528768](https://clinicaltrials.gov/study/NCT07528768) | Phase 2 | 尚未開始招募 | 750 | 非洲裔女性轉移性三陰性乳癌，比較 gemcitabine 與 paclitaxel |

此外還有多項 Phase 1/2 組合試驗（例如與 doxorubicin 脂質體、tipifarnib、nab-paclitaxel 併用），可作為輔助背景。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15685819](https://pubmed.ncbi.nlm.nih.gov/15685819/) | 2004 | Review | Oncology (Williston Park) | Gemcitabine 併用 paclitaxel 治療轉移性乳癌：Phase II 試驗中 221 位病人有 114 位（52%）出現反應 |
| [15685821](https://pubmed.ncbi.nlm.nih.gov/15685821/) | 2004 | Review | Oncology (Williston Park) | Gemcitabine 與鉑類併用於轉移性乳癌，可帶來明顯的臨床效益與反應率 |
| [15685820](https://pubmed.ncbi.nlm.nih.gov/15685820/) | 2004 | Review | Oncology (Williston Park) | Gemcitabine 併用 docetaxel 治療轉移性乳癌，毒性重疊少，且對未治療與曾用 anthracycline 者皆有活性 |
| [14768404](https://pubmed.ncbi.nlm.nih.gov/14768404/) | 2003 | Review | Oncology (Williston Park) | 探討 gemcitabine、anthracycline 與 taxane 組合用於晚期乳癌 |
| [12138397](https://pubmed.ncbi.nlm.nih.gov/12138397/) | 2002 | Review | Seminars in Oncology | 單用 gemcitabine 於轉移性乳癌的反應率為 16%–37%，併用其他藥物可進一步提升 |
| [14754469](https://pubmed.ncbi.nlm.nih.gov/14754469/) | 2004 | Review | Clinical Breast Cancer | Gemcitabine 與 trastuzumab 併用於 HER2 過度表現的轉移性乳癌 |
| [14754467](https://pubmed.ncbi.nlm.nih.gov/14754467/) | 2004 | Review | Clinical Breast Cancer | Gemcitabine 與 taxane 組合在乳癌治療中的定位 |
| [12057045](https://pubmed.ncbi.nlm.nih.gov/12057045/) | 2002 | Review | Clinical Breast Cancer | Gemcitabine 用於乳癌前導治療的可能性 |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Cohort（Phase I） | Breast Cancer Res Treat | Carboplatin、gemcitabine 與 mifepristone 用於晚期乳癌及復發卵巢癌 |
| [12057039](https://pubmed.ncbi.nlm.nih.gov/12057039/) | 2002 | 體外研究 | Clinical Breast Cancer | Gemcitabine 與 trastuzumab 在乳癌與肺癌細胞株中的前臨床研究 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Gemcitabine 的不重複許可證共 **20 張**：有效單方 6 張、有效複方 5 張、已註銷 9 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（6 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第047872號 | 健仕注射液38毫克/毫升 | 注射劑 | 台灣東洋藥品工業股份有限公司 | 2031/03/06 | 1.非小細胞肺癌2.胰臟癌3.膀胱癌4.Gemcitabine與paclitaxel併用，可使用於曾經使用過anthracycline之局部復發且無法手術切除或轉移性之乳癌患者。5… |
| 衛署藥製字第048311號 | "台灣神隆" 健喜得平 | （粉） | 台灣神隆股份有限公司 | 2026/10/14 | 抗癌藥。 |
| 衛署藥輸字第025899號 | 健仕平"山德士"40毫克/毫升注射劑 | 注射劑 | 台灣山德士藥業股份有限公司 | 2028/03/18 | 非小細胞肺癌、胰臟癌、膀胱癌。GEMCITABINE與PACLITAXEL併用，可使用於曾經使用過ANTHRACYCLINE之局部復發且無法手術切除或轉移性之乳癌病患。用於曾經使用… |
| 衛部藥製字第061175號 | "霖揚"吉西他濱凍晶注射劑200毫克 | 凍晶注射劑 | 霖揚生技製藥股份有限公司 | 2027/10/26 | 非小細胞肺癌、胰臟癌、膀胱癌。GEMCITABINE與PACLITAXEL併用，可使用於曾經使用過ANTHRACYCLINE之局部復發且無法手術切除或轉移性之乳癌病患。用於曾經使用… |
| 衛部藥輸字第026977號 | 健喜得平鹽酸鹽 | （粉） | 中大藥品股份有限公司 | 2026/10/28 | 抗癌藥。 |
| 衛部藥輸字第028196號 | 鹽酸吉西他濱 | （粉） | 新雙隆生技股份有限公司 | 2026/11/10 | 抗癌藥 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（5 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥輸字第025681號 | "卡比"健彌達靜脈凍晶注射劑 | GEMCITABINE HYDROCHLORIDE、GEMCITABINE HYDROCHLORIDE | 凍晶注射劑 | 非小細胞肺癌、胰臟癌、膀胱癌。Gemcitabine與paclitaxel併用，可使用於曾經使用過anthracycline之局部復發且無法手術切除或轉移性之乳癌病患。用於曾經使用… |
| 衛部藥製字第058646號 | 安佑得凍晶注射劑 | GEMCITABINE HYDROCHLORIDE、GEMCITABINE HYDROCHLORIDE | 凍晶注射劑 | 非小細胞肺癌、胰臟癌、膀胱癌。GEMCITABINE與PACLITAXEL併用，可使用於曾經使用過ANTHRACYCLINE之局部復發且無法手術切除或轉移性之乳癌病患。用於曾經使用… |
| 衛部藥製字第059784號 | "永信"健法凍晶注射劑 | GEMCITABINE HYDROCHLORIDE、GEMCITABINE HYDROCHLORIDE | 凍晶注射劑 | 非小細胞肺癌、胰臟癌、膀胱癌。GEMCITABINE與PACLITAXEL併用，可使用於曾經使用過ANTHRACYCLINE之局部復發且無法手術切除或轉移性之乳癌病人。用於曾經使用… |
| 衛部藥輸字第027106號 | 珍喜得平凍晶注射劑 | GEMCITABINE HYDROCHLORIDE、GEMCITABINE HYDROCHLORIDE | 凍晶注射劑 | 非小細胞肺癌、胰臟癌、膀胱癌、膽道癌。GEMCITABINE與PACLITAXEL併用，可使用於曾經使用過ANTHRACYCLINE之局部復發且無法手術切除或轉移性之乳癌病患。用於… |
| 衛部藥輸字第027468號 | 健特瑞凍晶注射劑 | GEMCITABINE HYDROCHLORIDE、GEMCITABINE HYDROCHLORIDE | 凍晶注射劑 | 非小細胞肺癌、胰臟癌、膀胱癌。GEMCITABINE與PACLITAXEL併用，可使用於曾經使用過ANTHRACYCLINE之局部復發且無法手術切除或轉移性之乳癌病患。用於曾經使用… |

<details><summary><strong>已註銷</strong>（9 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第048080號</td><td>雙福全靜脈注射劑</td><td>GEMCITABINE HYDROCHLORIDE</td><td>2017/02/06</td></tr><tr><td>衛署藥製字第055548號</td><td>吉西他濱鹽酸鹽</td><td>Gemcitabine Hydrochloride</td><td>2023/06/30</td></tr><tr><td>衛署藥輸字第021841號</td><td>健擇注射劑</td><td>GEMCITABINE HYDROCHLORIDE、GEMCITABINE HYDROCHLORIDE</td><td>2011/03/28</td></tr><tr><td>衛署藥輸字第023298號</td><td>健擇注射劑</td><td>GEMCITABINE HYDROCHLORIDE、GEMCITABINE HYDROCHLORIDE</td><td>2024/10/17</td></tr><tr><td>衛署藥輸字第024846號</td><td>健彌達靜脈凍晶注射劑</td><td>GEMCITABINE HYDROCHLORIDE、GEMCITABINE HYDROCHLORIDE</td><td>2024/06/18</td></tr><tr><td>衛署藥輸字第025183號</td><td>健達必凍晶注射劑</td><td>GEMCITABINE HYDROCHLORIDE、GEMCITABINE HYDROCHLORIDE、GEMCITAB…</td><td>2022/06/30</td></tr><tr><td>衛署藥輸字第026065號</td><td>健米喜凍晶注射劑</td><td>GEMCITABINE HYDROCHLORIDE、GEMCITABINE HYDROCHLORIDE、GEMCITAB…</td><td>2019/04/15</td></tr><tr><td>衛部藥輸字第026627號</td><td>健達必注射劑</td><td>GEMCITABINE HYDROCHLORIDE、GEMCITABINE HYDROCHLORIDE</td><td>2022/09/12</td></tr><tr><td>衛部藥輸字第027808號</td><td>健賽特平"泰和碩"注射劑</td><td>GEMCITABINE HYDROCHLORIDE</td><td>2021/10/12</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（核苷類似物、抗代謝藥） |
| 骨髓抑制風險 | 中至高（資料中的藥物關聯疾病包含白血球低下、血小板低下、貧血） |
| 致吐性分級 | 低至中度 |
| 監測項目 | 全血球計數（含分類）、肝腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

詳細警語與注意事項請參考原廠仿單。

## 安全性考量

- **知識圖譜標示的相關疾病風險**（來自模型知識圖譜，並非仿單文字）：腎臟疾病、肝臟疾病、膽囊疾病、血小板低下、貧血、白血球低下、間質性肺病、溶血性尿毒症候群、感染性疾病。使用前宜評估這些狀況。
- **藥物交互作用**：資料中共有 339 筆交互作用紀錄，其中分級較明確者包括 Naltrexone（中度）、Levofloxacin（輕度）；其餘如 Calcitriol、Doxycycline、Pantoprazole、Omeprazole、Metformin、Morphine、Prednisone、Simvastatin、Aprepitant 等，等級為未知，臨床使用時需個別查核。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
乳癌已有已完成的 Phase 3 試驗（NCT00006459）支持 Gemcitabine 併用 paclitaxel，且此用途已列入台灣核准適應症，另有多項 Phase 2/3 試驗與回顧文獻。不過，預測所指的是更廣的乳癌族群，現有證據多為較早期的試驗，輔助與前導治療的 Phase 3 結果並不一致，需謹慎界定適用對象。

**若要推進需要：**
- 釐清目標族群（如三陰性乳癌、HER2 陽性、早期乳癌輔助／前導治療），並確認其與現行標示適應症的差異
- 彙整輔助與前導治療 Phase 3 試驗（NCT00093795、NCT00039546、NCT00408408、NCT00070278）的實際結果
- 追蹤進行中的三陰性乳癌試驗（NCT06027268、NCT07528768）
- 補齊作用機轉的詳細資料
- 建立血液學監測與劑量調整計畫，並針對腎、肝功能不全及有間質性肺病病史的病人設定使用條件

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「原本用於…包括轉移性大腸直腸癌」 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 原適應症取自 bevacizumab 許可證 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表列 bevacizumab 製劑「艾法施注射液」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 預測理由「在轉移性大腸直腸癌中的療效已被證實」 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 女性乳腺癌預測標記待重審 | 標記待重審 → 已重審（見下列重審結果） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 女性乳腺癌預測重審結果 | 重審：維持，證據等級 L2 不變 | [PubMed：Gemcitabine plus Paclitaxel versus Paclitaxel monotherapy in patients with metastatic breast cancer and prior anthracycline treatment（PMID 18711184）](https://pubmed.ncbi.nlm.nih.gov/18711184/)；[PubMed：Biomarker assessment of the CBCSG006 trial: a randomized phase III trial of cisplatin plus gemcitabine compared with paclitaxel plus gemcitabine as first-line therapy for patients with metastatic triple-negative breast cancer（PMID 29905759）](https://pubmed.ncbi.nlm.nih.gov/29905759/)；[PubMed：Addition of gemcitabine to paclitaxel, epirubicin, and cyclophosphamide adjuvant chemotherapy for women with early-stage breast cancer (tAnGo): final 10-year follow-up of an open-label, randomised, phase 3 trial（PMID 28479233）](https://pubmed.ncbi.nlm.nih.gov/28479233/)；[ClinicalTrials.gov：Paclitaxel With or Without Gemcitabine in Treating Women With Advanced Breast Cancer（NCT00006459）](https://clinicaltrials.gov/study/NCT00006459) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

