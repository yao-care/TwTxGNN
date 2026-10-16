---
layout: default
title: Clomipramine
parent: 高證據等級 (L1-L2)
nav_order: 70
evidence_level: L1
indication_count: 10
---

# Clomipramine
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

# Clomipramine：從憂鬱病到焦慮症

## 一句話總結

Clomipramine（可洛米普明）是三環抗憂鬱劑，在台灣原本核准用於憂鬱病（部分舊證另核准強迫症、恐懼症等）。
TxGNN 模型預測它可能對**焦慮症 (Anxiety Disorder)** 有效，
目前有 **8 個臨床試驗**和 **20 篇文獻**支持這個方向，其中以強迫症與恐慌症的證據最具體。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 憂鬱病 |
| 預測新適應症 | 焦慮症 (Anxiety Disorder) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L1 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 14 張（有效單方 4／有效複方 0／已過期 1／已註銷 9） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位無資料）。根據已知藥理，Clomipramine 是三環類抗憂鬱劑，能強力抑制血清素再回收，並有次要的正腎上腺素作用。這種血清素系統的調節，是它在強迫症與恐慌／畏懼型焦慮中發揮療效的基礎。

憂鬱與焦慮常合併出現，且共享血清素與正腎上腺素神經傳導的失衡，因此抗憂鬱劑常被用於焦慮相關疾患。強迫症屬於焦慮譜系疾病，Clomipramine 在其中有長期的臨床使用歷史；文獻也顯示它對伴有懼曠症的恐慌症有效。

需要注意，這項預測的證據主要來自強迫症與恐慌症，不一定能直接推論到所有焦慮症亞型。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00004310](https://clinicaltrials.gov/study/NCT00004310) | Phase 2 | 未知 | 76 | 比較靜脈與口服 Clomipramine 負荷給藥，後續 12 週維持治療用於強迫症（直接相關） |
| [NCT00564564](https://clinicaltrials.gov/study/NCT00564564) | Phase 4 | 完成 | 21 | 對 SSRI 無反應的強迫症，比較 Quetiapine 與 Clomipramine 加成治療（開放試驗） |
| [NCT00466609](https://clinicaltrials.gov/study/NCT00466609) | Phase 4 | 完成 | 54 | 對第一線治療無反應的強迫症，比較 Fluoxetine 單用、加 Quetiapine、加 Clomipramine（雙盲） |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | 完成 | 124 | 兒童強迫症 SRI 部分反應者，評估認知行為治療的加成效果（Clomipramine 非試驗藥物） |
| [NCT00254735](https://clinicaltrials.gov/study/NCT00254735) | Phase 3 | 完成 | 44 | 嚴重強迫症在 SSRI／Clomipramine 基礎治療上加用 Quetiapine（試驗藥物為 Quetiapine） |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | 完成 | 26 | 強迫症患者隨機接受 Clomipramine 或 Escitalopram，探討藥物反應預測因子 |
| [NCT05737511](https://clinicaltrials.gov/study/NCT05737511) | Phase 4 | 尚未招募 | 80 | Hydroxyzine 對比常規治療用於恐慌症（Clomipramine 至多屬常規治療） |
| [NCT02374567](https://clinicaltrials.gov/study/NCT02374567) | Phase 3 | 已終止 | 407 | 老年精神科住院病人的藥物不良反應監測（僅提供一般安全性參考） |

多數試驗的對象是強迫症，且 Clomipramine 常為背景或對照用藥；以 Clomipramine 為直接研究對象的試驗只有 NCT00004310 與 NCT00564564，且規模小。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | 統合分析 | Cochrane Database Syst Rev | 成人恐慌症藥物治療的網絡統合分析 |
| [40788541](https://pubmed.ncbi.nlm.nih.gov/40788541/) | 2026 | 統合分析 | Eur Arch Psychiatry Clin Neurosci | 抗焦慮藥物治療焦慮症的療效與可接受性比較 |
| [40946318](https://pubmed.ncbi.nlm.nih.gov/40946318/) | 2026 | 系統性回顧 | Psychother Psychosom | 難治型焦慮症的藥物、心理與神經刺激治療選項 |
| [35900217](https://pubmed.ncbi.nlm.nih.gov/35900217/) | 2023 | 指引 | World J Biol Psychiatry | WFSBP 焦慮、強迫症與創傷後壓力症治療指引 |
| [41978943](https://pubmed.ncbi.nlm.nih.gov/41978943/) | 2026 | 系統性回顧 | Acta Neuropsychiatr | 注射型 Clomipramine 用於憂鬱症或強迫症的統合分析 |
| [27663940](https://pubmed.ncbi.nlm.nih.gov/27663940/) | 2016 | 統合分析 | J Am Acad Child Adolesc Psychiatry | 兒童強迫症中 SSRI 與 Clomipramine 的早期療效比較 |
| [2021107](https://pubmed.ncbi.nlm.nih.gov/2021107/) | 1991 | Review | Am Fam Physician | Clomipramine 治療強迫症；療效在三環類中獨特，癲癇發生率約 0.4% |
| [18849910](https://pubmed.ncbi.nlm.nih.gov/18849910/) | 2008 | Review | CNS Spectrums | Clomipramine 對強迫症有效，但不良反應較多 |
| [34582562](https://pubmed.ncbi.nlm.nih.gov/34582562/) | 2021 | 統合分析 | Cochrane Database Syst Rev | 拔毛症的藥物治療 |
| [3887445](https://pubmed.ncbi.nlm.nih.gov/3887445/) | 1985 | 雙盲試驗 | Psychiatry Res | Clomipramine 與 Imipramine 用於強迫症，兩者均僅有中等程度改善 |

此外，針對恐慌症／懼曠症（預測排名第 7）另有 RCT 與開放試驗，例如 Clomipramine 對比 Diazepam（PMID 6373161）及對比 Imipramine（PMID 22290995），以及多項低劑量與劑量探索研究。整體而言，統合分析層級的證據多為藥物類別比較，直接針對 Clomipramine 的對照試驗多為小型研究。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Clomipramine 的不重複許可證共 **14 張**：有效單方 4 張、有效複方 0 張、已過期 1 張（未註銷但有效日期已過）、已註銷 9 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（4 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第040205號 | "約克"克爾鬱膠囊25毫克（可洛米普明） | 膠囊劑 | 約克製藥股份有限公司 | 2031/08/15 | 憂鬱症 |
| 衛署藥製字第040356號 | 解鬱膠囊２５公絲（可洛米普明） | 膠囊劑 | 井田國際醫藥廠股份有限公司 | 2031/09/21 | 憂鬱症 |
| 衛署藥製字第040544號 | "瑞士" 可必安膜衣錠２５毫克（可洛米普明） | 膜衣錠 | 瑞士藥廠股份有限公司 | 2026/11/07 | 憂鬱病。。 |
| 衛部藥製字第058145號 | "強生"可使寧膜衣錠25毫克 | 膜衣錠 | 強生化學製藥廠股份有限公司 | 2028/12/10 | 憂鬱病。 |

<details><summary><strong>已過期（未註銷但有效日期已過）</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛署藥製字第039220號</td><td>倍欣膜衣錠２５公絲（可洛米普明）</td><td>CLOMIPRAMINE HCL</td><td>2025/08/24</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（9 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第039691號</td><td>解夏寧膠囊２５公絲（可洛米普明）</td><td>CLOMIPRAMINE HCL</td><td>2013/11/04</td></tr><tr><td>衛署藥製字第041051號</td><td>〝新東〞可欣喜錠２５公絲</td><td>CLOMIPRAMINE HCL</td><td>2009/10/21</td></tr><tr><td>衛署藥製字第041427號</td><td>可落眠錠２５公絲（可洛米普明）</td><td>CLOMIPRAMINE HCL</td><td>2016/09/07</td></tr><tr><td>衛署藥製字第042463號</td><td>伏憂糖衣錠２５公絲（可洛米普明）〝溫士頓〞</td><td>CLOMIPRAMINE HCL</td><td>2018/11/07</td></tr><tr><td>衛署藥輸字第004186號</td><td>安納福寧注射液</td><td>CLOMIPRAMINE HCL</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第012536號</td><td>安納福寧２５公絲糖衣錠</td><td>CLOMIPRAMINE HCL</td><td>2004/11/09</td></tr><tr><td>衛署藥輸字第012692號</td><td>安納福寧１０公絲糖衣錠</td><td>CLOMIPRAMINE HCL</td><td>2004/11/09</td></tr><tr><td>衛署藥輸字第022028號</td><td>鹽酸可洛米普明　〝維士〞</td><td>CLOMIPRAMINE HCL</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第022176號</td><td>鹽酸可洛米普明</td><td>CLOMIPRAMINE HCL</td><td>2010/05/31</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的相關禁忌疾病**（來自模型知識圖譜，並非仿單文字）：癲癇、躁型雙相情感障礙、肝病、膽囊疾病、物質濫用／依賴、惡性高熱、嗜鉻細胞瘤、青光眼、甲狀腺功能亢進（含 Graves 病）、神經母細胞瘤等。
- **藥物交互作用**：共收錄 318 筆，主要（Major）等級包括 Epinephrine、Bupropion、Lorcaserin、Potassium citrate、Cisapride；中度（Moderate）包括 Famotidine、Cimetidine、Clarithromycin、Morphine、Acetylsalicylic acid 及多種抗膽鹼藥物（Atropine、Hyoscyamine 等）。
- **文獻中的安全訊號**：個案報告曾見 Clomipramine 相關全血球減少（PMID 3572384）與誘發抽動症（PMID 9316681）；文獻亦提到抗膽鹼作用、心臟風險與癲癇風險。

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- Clomipramine 在強迫症與恐慌症／懼曠症已有多年臨床證據，並有直接以它為研究對象的試驗與統合分析，支持焦慮症方向。
- 但相關直接試驗規模小，且 Clomipramine 的不良反應與藥物交互作用負擔高於 SSRI，因此需要設置安全防護。

**若要推進需要：**
- 補充詳細的作用機轉（MOA）資料
- 明確界定目標焦慮症亞型（強迫症、恐慌症／懼曠症等），並與現行第一線 SSRI 做比較
- 建立高風險族群（癲癇、心臟疾病、青光眼、肝病、老年人）的篩檢與監測計畫
- 制定交互作用審查流程，尤其是 Bupropion、Epinephrine 及其他血清素類藥物
- 取得仿單中的警語與禁忌資料，以補足目前的資料缺口

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 原核准適應症列入強迫症、恐懼症、驚懼發作 | 報告重生後已無此錯誤（2026-10-15：新報告「原適應症」列為「憂鬱病」；原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表核准適應症 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 備註「台灣核准適應症已包含恐懼症及驚懼發作」 | 報告重生後已無此錯誤（2026-10-15：新報告改寫為「原本核准用於憂鬱病（部分舊證另核准強迫症、恐懼症等）」，與許可證資料相符；原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-04 | 頁首證據等級 | 頁首等級依總覽表重算（原 L5→L1） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

