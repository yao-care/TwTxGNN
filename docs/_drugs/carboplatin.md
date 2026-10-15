---
layout: default
title: Carboplatin
parent: 高證據等級 (L1-L2)
nav_order: 55
evidence_level: L1
indication_count: 10
---

# Carboplatin
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

# Carboplatin：從 HER2 陽性乳癌與轉移性胃癌（許可證所載適應症）到女性乳癌

## 一句話總結

Carboplatin 是鉑類細胞毒性化療藥物，在台灣許可證資料中，與它相關的適應症主要是 HER2 陽性乳癌及轉移性胃癌（Carboplatin 為併用療法的一環）。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效，目前有**多個臨床試驗**（含 3 項已完成的 Phase 3）和**多篇文獻**（含數項 RCT）支持這個方向。

> **資料提醒：** 本報告所用的台灣許可證資料，列出的是 trastuzumab 與 pembrolizumab 等生物藥品的許可證，其適應症文字只是提到「與 carboplatin 併用」。資料中沒有 carboplatin 本身的單方許可證，下列「原適應症」應理解為 carboplatin 所參與的併用療法適應症，而非 carboplatin 單方的核准適應症。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 卵巢癌（台灣許可證核准適應症） |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L1 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 16 張（有效單方 3／有效複方 0／已註銷 13） |
| 建議決策 | Proceed with Guardrails |

<!-- review:begin carboplatin-original-indication-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「原適應症／HER2 過度表現之早期乳癌、轉移性乳癌，以及未曾接受化療之 HER2 過度表現轉移性胃腺癌（來自許可證文字，carboplatin 為併用藥物）」。2026-10-15 報告重生後，此列改寫成 trastuzumab 許可證中與 carboplatin 併用的適應症，仍不是 carboplatin 本身的核准適應症。原文列的是 trastuzumab、pembrolizumab 等其他藥品許可證中與 carboplatin 併用的適應症；台灣有效的 carboplatin 許可證（衛署藥輸字第024074號佳鉑帝、第024804號爾定康、衛署藥製字第057314號杏輝剋鉑停）核准適應症都是「卵巢癌」。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end carboplatin-original-indication-2026-10-03 -->

由於原適應症本身已含乳癌，這個預測更像是**擴大或釐清使用族群**（例如三陰性乳癌、BRCA 相關乳癌），而不是全新的疾病領域。

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。依本報告彙整的推論，carboplatin 會與 DNA 形成鉑-DNA 加成物與交叉鏈結，阻斷 DNA 複製並誘發細胞凋亡。

這個機轉特別適用於 DNA 修復功能受損的腫瘤，例如三陰性乳癌與 BRCA 缺陷乳癌。另外，carboplatin 已是 TCH 療法（docetaxel + carboplatin + trastuzumab）的一部分，用於 HER2 陽性乳癌，因此原適應症與預測新適應症在臨床上高度相關。

多項新輔助化療試驗也在測試，於標準治療中加入 carboplatin 能否提高病理完全緩解率 (pCR)。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Phase 3 | 完成 | 3222 | 比較 AC-T、AC-TH 與 TCH（docetaxel + carboplatin + trastuzumab）用於 HER2 陽性可手術乳癌的輔助治療 |
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Phase 3 | 完成 | 263 | 比較 docetaxel + trastuzumab 加或不加 carboplatin，用於 HER2 基因擴增的晚期乳癌第一線治療 |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | 完成 | 961 | GeparOcto：比較兩種劑量密集方案（含 carboplatin 的 PM(Cb)）用於高風險早期乳癌新輔助治療 |
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Phase 2 | 完成 | 148 | 隨機試驗，比較 carboplatin 與 docetaxel 用於轉移性遺傳性（BRCA）乳癌 |
| [NCT00316407](https://clinicaltrials.gov/study/NCT00316407) | Phase 1/2 | 完成 | 30 | Lapatinib 併用 carboplatin/paclitaxel，用於復發卵巢癌或 IV 期乳癌 |
| [NCT00003612](https://clinicaltrials.gov/study/NCT00003612) | Phase 2 | 完成 | 92 | Paclitaxel + carboplatin + Herceptin 用於 HER2 過度表現轉移性乳癌第一線治療 |
| [NCT01208480](https://clinicaltrials.gov/study/NCT01208480) | Phase 2 | 完成 | 45 | 新輔助 bevacizumab + docetaxel + carboplatin 用於三陰性乳癌 |
| [NCT00616967](https://clinicaltrials.gov/study/NCT00616967) | Phase 2 | 進行中（不再招募） | 68 | Carboplatin + nab-paclitaxel 加或不加 vorinostat，用於 HER2 陰性可手術乳癌的術前化療，評估療效與生物標記 |
| [NCT00025688](https://clinicaltrials.gov/study/NCT00025688) | Phase 3 | 未知 | 未提供 | 每週 paclitaxel 加或不加 carboplatin，用於 65 歲以上轉移性乳癌第一線治療 |
| [NCT00118053](https://clinicaltrials.gov/study/NCT00118053) | Phase 2 | 提前終止 | 5 | Docetaxel + carboplatin + Herceptin 用於局部晚期或發炎性乳癌 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24794243](https://pubmed.ncbi.nlm.nih.gov/24794243/) | 2014 | RCT（Phase 2） | The Lancet Oncology | GeparSixto：評估在新輔助治療中加入 carboplatin 用於三陰性與 HER2 陽性早期乳癌 |
| [29501363](https://pubmed.ncbi.nlm.nih.gov/29501363/) | 2018 | RCT（Phase 3） | The Lancet Oncology | BrighTNess：在三陰性乳癌新輔助化療中加入 veliparib + carboplatin 或單用 carboplatin |
| [35044810](https://pubmed.ncbi.nlm.nih.gov/35044810/) | 2022 | RCT（Phase 2） | J Clin Oncol | CALGB 40603 長期追蹤：加入 carboplatin 或 bevacizumab 提高 II-III 期三陰性乳癌的 pCR，本文報告長期結果 |
| [33208340](https://pubmed.ncbi.nlm.nih.gov/33208340/) | 2021 | RCT（Phase 2） | Clin Cancer Res | NeoSTOP：比較不含與含 anthracycline 的新輔助 carboplatin 方案用於三陰性乳癌 |
| [41436191](https://pubmed.ncbi.nlm.nih.gov/41436191/) | 2025 | RCT（Phase 3） | BMJ | CITRINE：高風險早期三陰性乳癌輔助治療，評估加入 carboplatin 對存活的影響 |
| [41115255](https://pubmed.ncbi.nlm.nih.gov/41115255/) | 2026 | Phase 3 RCT | J Clin Oncol | 在三陰性乳癌的 taxane-anthracycline 新輔助化療中加入鉑類，評估對存活的影響 |
| [29175149](https://pubmed.ncbi.nlm.nih.gov/29175149/) | 2018 | RCT（Phase 3） | The Lancet Oncology | KRISTINE：HER2 陽性乳癌新輔助治療，比較含化療方案與 T-DM1 + pertuzumab |
| [40593759](https://pubmed.ncbi.nlm.nih.gov/40593759/) | 2025 | RCT（Phase 2b） | Nature Communications | 以標準新輔助 TCbHP 方案（含 carboplatin）作為對照，比較 ARX788 + pyrotinib |
| [38492276](https://pubmed.ncbi.nlm.nih.gov/38492276/) | 2024 | 系統性回顧 | The Breast | 早期三陰性乳癌的鉑類化療：可提高 pCR，對長期存活的影響尚待釐清 |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Review | Pharmacological Research | 乳癌標靶與細胞毒性抑制劑的治療概述 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Carboplatin 的不重複許可證共 **16 張**：有效單方 3 張、有效複方 0 張、已註銷 13 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（3 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第057314號 | "杏輝"剋鉑停靜脈注射液10毫克/毫升 | 注射劑 | 杏輝藥品工業股份有限公司 | 2027/07/30 | 卵巢癌。 |
| 衛署藥輸字第024074號 | 佳鉑帝靜脈注射液 | 注射液劑 | 台灣大昌華嘉股份有限公司 | 2029/09/29 | 卵巢癌。 |
| 衛署藥輸字第024804號 | 爾定康靜脈注射液 | 注射劑 | 台灣費森尤斯卡比股份有限公司 | 2028/03/17 | 卵巢癌。 |

<details><summary><strong>已註銷</strong>（13 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第017782號</td><td>佳鉑帝注射液</td><td>CARBOPLATIN、CARBOPLATIN</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第018696號</td><td>佳鉑帝凍晶注射劑</td><td>CARBOPLATIN、CARBOPLATIN、CARBOPLATIN</td><td>2008/12/22</td></tr><tr><td>衛署藥輸字第018768號</td><td>佳鉑帝注射液</td><td>CARBOPLATIN、WATER DISTILLED FOR INJECTION</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第020725號</td><td>卡伯拉丁注射液</td><td>CARBOPLATIN</td><td>1997/09/01</td></tr><tr><td>衛署藥輸字第020966號</td><td>克本瘤注射液</td><td>CARBOPLATIN</td><td>2013/12/31</td></tr><tr><td>衛署藥輸字第021047號</td><td>克本瘤注射液１０公絲/公撮</td><td>CARBOPLATIN</td><td>2016/06/03</td></tr><tr><td>衛署藥輸字第021701號</td><td>卡伯拉丁注射液</td><td>CARBOPLATIN</td><td>2022/09/22</td></tr><tr><td>衛署藥輸字第023368號</td><td>克鉑定 "立可用安全型注射液"</td><td>CARBOPLATIN</td><td>2022/06/30</td></tr><tr><td>衛署藥輸字第024591號</td><td>貝福卡鉑靜脈注射液10毫克/毫升</td><td>CARBOPLATIN</td><td>2014/04/08</td></tr><tr><td>衛署藥輸字第025626號</td><td>卡蒲鉑定"山德士"注射劑10毫克/毫升</td><td>CARBOPLATIN</td><td>2021/07/05</td></tr><tr><td>衛部藥輸字第026387號</td><td>艾鉑霆靜脈注射液10毫克/毫升</td><td>CARBOPLATIN</td><td>2026/08/12</td></tr><tr><td>衛部藥輸字第027083號</td><td>可鉑注射液10毫克/毫升</td><td>CARBOPLATIN</td><td>2026/02/02</td></tr><tr><td>衛部藥陸輸字第000936號</td><td>卡鉑定</td><td>Carboplatin</td><td>2026/06/03</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（鉑類，DNA 烷化樣交叉鏈結） |
| 骨髓抑制風險 | 高（劑量限制性毒性，常見血小板減少、嗜中性白血球減少與貧血；知識圖譜亦列有相關禁忌疾病） |
| 致吐性分級 | 中至高度（視劑量而定） |
| 監測項目 | CBC（含分類與血小板）、腎功能、肝功能、電解質、聽力與周邊神經症狀 |
| 處置防護 | 需依細胞毒性藥物處置規範配製與給藥 |

細部警語與劑量調整，請參考原廠仿單。

## 安全性考量

- **知識圖譜標示的潛在禁忌疾病**（來自藥物-疾病關聯資料，並非仿單文字）：腎臟疾病、肝臟疾病、膽囊疾病、血小板減少、嗜中性白血球減少、顆粒球缺乏症、白血球減少、貧血、血液凝固疾病、周邊神經病變、聽力障礙。
- **藥物交互作用**：資料庫共收錄 488 筆。主要為中度等級，例如：
  - 氫離子幫浦抑制劑（rabeprazole、omeprazole、esomeprazole、lansoprazole、pantoprazole、dexlansoprazole）
  - 胺基糖苷類抗生素（kanamycin、neomycin、streptomycin）與 vancomycin（可能加重腎毒性或耳毒性）
  - Metronidazole、tinidazole
  - Statin 類（rosuvastatin、simvastatin）
  - Levofloxacin 為輕度交互作用

仿單中的正式警語與禁忌症，請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有 3 項已完成的 Phase 3 試驗（NCT00021255、NCT00047255、NCT02125344），並有多項 RCT 探討 carboplatin 用於乳癌，證據等級為 L1。
- Carboplatin 的骨髓抑制風險高。同時，乳癌原本就在許可證的併用適應症內，因此重點是確認適用的亞型與劑量，而非開發全新適應症。

**若要推進需要：**
- 釐清台灣許可證資料：目前沒有 carboplatin 單方許可證，需確認其在台灣的實際核准適應症。
- 補充 DrugBank 的詳細作用機轉資料。
- 針對三陰性、BRCA 相關與 HER2 陽性亞型，整理 carboplatin 對長期存活（而非僅 pCR）的獲益與風險。
- 建立血液學毒性、腎功能與聽力、神經毒性的監測計畫，並檢視併用藥物（如 PPI、胺基糖苷類）的交互作用。
- 補充其他預測方向（如成人生殖細胞腫瘤，目前證據等級 L2）的評估，以供後續排序。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「原適應症」列成 trastuzumab／pembrolizumab 等併用方案的適應症 | 更正（2026-10-15 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「許可證數」寫成其他藥品適應症中的併用藥物 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表「衛部藥輸字第027591號」列 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表「衛署藥輸字第027591號」列 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表「衛部藥輸字第028264號」列 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

