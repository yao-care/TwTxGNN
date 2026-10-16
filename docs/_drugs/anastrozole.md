---
layout: default
title: Anastrozole
parent: 高證據等級 (L1-L2)
nav_order: 29
evidence_level: L1
indication_count: 6
monitor_inn: "Anastrozole"
predicted_indications: ["female breast carcinoma", "neuroblastoma", "vertebral anomalies and variable endocrine and T-cell dysfunction", "ganglioneuroblastoma (disease)", "retroperitoneal neoplasm", "monocytic leukemia"]
last_modified_at: 2026-10-16
description: "Anastrozole：預測新適應症為女性乳癌 (Female Breast Carcinoma)（證據等級 L1）。原適應症：治療停經後婦女晚期乳癌"
---

# Anastrozole
{: .fs-9 }

證據等級: **L1** | 預測適應症: **6** 個
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

# Anastrozole：從停經後乳癌到女性乳癌（ER+ 適應症確認）

## 一句話總結

Anastrozole 是一種非類固醇芳香環轉化酶抑制劑，原本用於治療停經後婦女的晚期與早期荷爾蒙接受器陽性乳癌。
TxGNN 模型預測的首位適應症為**女性乳癌 (female breast carcinoma)**，與既有核准適應症高度重疊，屬於「已上市適應症的再確認」，而非全新的適應症。
目前有 **30 個臨床試驗**和 **20 篇文獻**支持這個方向，其中包含多個已完成的 Phase 3 RCT。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 治療停經後婦女晚期乳癌；輔助治療停經後婦女且荷爾蒙接受器為陽性的早期侵犯性乳癌；輔助治療已使用 tamoxifen 2-3 年之停經後婦女且荷爾蒙接受器為陽性的早期乳癌 |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.68% |
| 證據等級 | L1 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 13 張（有效單方 9／有效複方 0／已註銷 4） |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據已知資訊，Anastrozole 是一種非類固醇芳香環轉化酶抑制劑，可降低停經後婦女周邊組織的雌激素合成，使荷爾蒙接受器陽性的乳癌細胞失去雌激素驅動的生長訊號。

這個預測的疾病（女性乳癌）與原適應症（停經後荷爾蒙接受器陽性乳癌）本質上屬於同一疾病範疇，因此預測合理性很高，也有多個 Phase 3 RCT 與大型文獻佐證。需要注意：這屬於已核准適應症的驗證，不是真正跨疾病領域的再利用。

排名 2–6 的預測（神經母細胞瘤、神經節母細胞瘤、腹膜後腫瘤、單核球性白血病，以及一種罕見的椎體異常合併內分泌與 T 細胞功能異常症候群）缺乏機轉依據，且幾乎沒有臨床證據，僅為模型計算結果，建議列為 Hold。

---

## 臨床試驗證據

以下列出與 Anastrozole 最相關的 10 個試驗（依相關性分級與研究設計挑選）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00784680](https://clinicaltrials.gov/study/NCT00784680) | Phase 3 | 完成 | 308 | 雙盲 RCT，比較 Arimidex、Nolvadex 及兩者合併輔助治療的生活品質 |
| [NCT00327769](https://clinicaltrials.gov/study/NCT00327769) | Phase 3 | 完成 | 234 | Fulvestrant 與 Arimidex 作為二線治療，ER 陽性晚期乳癌的療效與安全性比較 |
| [NCT00143390](https://clinicaltrials.gov/study/NCT00143390) | Phase 3 | 完成 | 298 | Exemestane 對比 anastrozole 作為晚期/復發乳癌初始荷爾蒙治療的非劣性試驗 |
| [NCT00300508](https://clinicaltrials.gov/study/NCT00300508) | Phase 3 | 完成 | 856 | 完成 5 年輔助荷爾蒙治療後，再用 3 年 anastrozole 對比不治療 |
| [NCT00301457](https://clinicaltrials.gov/study/NCT00301457) | Phase 3 | 完成 | 1914 | 使用 tamoxifen 2–3 年後，比較 6 年與 3 年 anastrozole 的無病存活 |
| [NCT00784940](https://clinicaltrials.gov/study/NCT00784940) | Phase 3 | 完成 | 308 | 評估 Arimidex 與 Nolvadex 對骨密度與骨代謝的影響 |
| [NCT00784862](https://clinicaltrials.gov/study/NCT00784862) | Phase 3 | 完成 | 9358 | 評估 Arimidex 與 tamoxifen 合併使用時的藥物動力學交互作用 |
| [NCT02246621](https://clinicaltrials.gov/study/NCT02246621) | Phase 3 | 進行中 | 493 | 非類固醇芳香環轉化酶抑制劑（anastrozole 或 letrozole）加 abemaciclib 對比安慰劑，用於 HR+/HER2− 晚期乳癌 |
| [NCT00256217](https://clinicaltrials.gov/study/NCT00256217) | Phase 2 | 完成 | 42 | Anastrozole 用於停經後 DCIS 與早期侵犯性乳癌的化學預防 |
| [NCT00437853](https://clinicaltrials.gov/study/NCT00437853) | N/A | 完成 | 30 | Anastrozole 用於停經後 ER 陽性可手術乳癌的新輔助荷爾蒙治療 |

另有多個 anastrozole 與 CDK4/6 抑制劑、AKT 抑制劑等的合併試驗，多數為小規模或已終止。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15639680](https://pubmed.ncbi.nlm.nih.gov/15639680/) | 2005 | RCT | Lancet | ATAC 試驗（9366 人）：anastrozole 相較 tamoxifen 顯著延長無病存活 |
| [31839281](https://pubmed.ncbi.nlm.nih.gov/31839281/) | 2020 | RCT | Lancet | IBIS-II 長期追蹤：anastrozole 可預防高風險女性發生乳癌 |
| [27908454](https://pubmed.ncbi.nlm.nih.gov/27908454/) | 2016 | RCT | Lancet | FALCON：fulvestrant 500 mg 與 anastrozole 1 mg 用於未接受過內分泌治療的 HR+ 晚期乳癌之比較 |
| [41632158](https://pubmed.ncbi.nlm.nih.gov/41632158/) | 2025 | Cohort | JAMA Netw Open | 比較 anastrozole、letrozole、exemestane 在停經後乳癌的真實世界療效 |
| [31615937](https://pubmed.ncbi.nlm.nih.gov/31615937/) | 2020 | Cohort | Clin Cancer Res | neoMONARCH：abemaciclib 加 anastrozole 之新輔助治療抑制細胞週期並提升免疫反應 |
| [20923259](https://pubmed.ncbi.nlm.nih.gov/20923259/) | 2010 | Review | Expert Opin Drug Saf | 第三代芳香環轉化酶抑制劑，輔助治療療效優於 tamoxifen |
| [16034487](https://pubmed.ncbi.nlm.nih.gov/16034487/) | 2005 | Review | Drugs Today | 回顧 anastrozole 作用機轉與主要臨床試驗 |
| [28614542](https://pubmed.ncbi.nlm.nih.gov/28614542/) | 2017 | Review | Rev Assoc Med Bras | Anastrozole 用於乳癌化學預防與治療的文獻回顧 |
| [16439860](https://pubmed.ncbi.nlm.nih.gov/16439860/) | 2006 | Review | Oncology | Anastrozole 涵蓋晚期、早期乳癌至預防的角色回顧 |
| [17033446](https://pubmed.ncbi.nlm.nih.gov/17033446/) | 2006 | Case report | Eur J Gastroenterol Hepatol | 首例通報的 anastrozole 引起肝毒性（高齡女性） |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Anastrozole 的不重複許可證共 **13 張**：有效單方 9 張、有效複方 0 張、已註銷 4 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（9 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第047539號 | 安納柔膜衣錠 | 膜衣錠 | 台灣東洋藥品工業股份有限公司 | 2030/09/21 | 治療停經後婦女晚期乳癌。其療效對於雌激素接受器陰性之病患尚未被證實，除非這些病患曾經對TAMOXIFEN有陽性反應。輔助治療停經後婦女且荷爾蒙接受器為陽性的早期侵犯性乳癌。輔助治療… |
| 衛署藥製字第048627號 | "台灣神隆" 安耐柔 | （粉） | 台灣神隆股份有限公司 | 2027/03/15 | 抗腫瘤原料藥。 |
| 衛署藥製字第048909號 | 安斯如膜衣錠 1 毫克 | 膜衣錠 | 美時化學製藥股份有限公司 | 2027/07/27 | 治療停經後婦女晚期乳癌。其療效對於雌激素接受器陰性之病患尚未被證實，除非這些病患曾經對TAMOXIFEN有陽性反應。輔助治療停經後婦女且荷爾蒙接受器為陽性的早期侵犯性乳癌。輔助治療… |
| 衛署藥製字第055555號 | “培力”安諾妥膜衣錠 1 毫克 | 膜衣錠 | 培力藥品工業股份有限公司 | 2030/11/24 | 治療停經後婦女晚期乳癌。其療效對於雌激素接受器陰性之病患尚未被證實，除非這些病患曾經對TAMOXIFEN有陽性反應。輔助治療停經後婦女且荷爾蒙接受器為陽性的早期侵犯性乳癌。輔助治療… |
| 衛署藥製字第056730號 | "杏輝"安娜斯柔膜衣錠1毫克 | 膜衣錠 | 杏輝藥品工業股份有限公司 | 2026/11/18 | 治療停經後婦女晚期乳癌。其療效對於雌激素接受器陰性之病患尚未被證實，除非這些病患曾經對Tamoxifen有陽性反應。輔助治療停經後婦女且荷爾蒙接受器為陽性的早期侵犯性乳癌。輔助治療… |
| 衛署藥輸字第022282號 | 安美達錠１毫克 | 膜衣錠 | 臺灣阿斯特捷利康股份有限公司 | 2028/08/31 | 治療停經後婦女晚期乳癌。其療效對於雌激素接受器陰性之病人尚未被證實，除非這些病人曾經對TAMOXIFEN有陽性反應。 輔助治療停經後婦女且荷爾蒙接受器為陽性的早期侵犯性乳癌。 輔助… |
| 衛署藥輸字第025251號 | 安滅癌膜衣錠 1 毫克 | 膜衣錠 | 富富企業股份有限公司 | 2030/08/20 | 治療停經後婦女晚期乳癌。其療效對於雌激素接受器陰性之病患尚未被證實，除非這些病患曾經對tamoxifen有陽性反應。輔助治療停經後婦女且荷爾蒙接受器為陽性的早期侵犯性乳癌。輔助治療… |
| 衛署藥輸字第025535號 | 消汝妥1毫克 | 膜衣錠 | 生達化學製藥股份有限公司 | 2026/10/11 | 治療停經後婦女晚期乳癌。其療效對於雌激素接受器陰性之病患尚未被證實，除非這些病患曾經對tamoxifen有陽性反應。輔助治療停經後婦女且荷爾蒙接受器為陽性的早期侵犯性乳癌。輔助治療… |
| 衛部藥輸字第026515號 | 安瑞特膜衣錠1毫克 | 膜衣錠 | 凱沛爾藥品有限公司 | 2030/03/23 | 治療停經後婦女晚期乳癌。其療效對於雌激素接受器陰性之病患尚未被證實，除非這些病患曾經對TAMOXIFEN有陽性反應。輔助治療停經後婦女且荷爾蒙接受器為陽性的早期侵犯性乳癌。輔助治療… |

<details><summary><strong>已註銷</strong>（4 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第057290號</td><td>"台耀"安耐柔</td><td>Anastrozole</td><td>2022/03/28</td></tr><tr><td>衛署藥輸字第025288號</td><td>安適乳膜衣錠 1 毫克</td><td>ANASTROZOLE</td><td>2016/01/19</td></tr><tr><td>衛署藥輸字第025610號</td><td>安耐柔</td><td>Anastrozole USP</td><td>2023/06/20</td></tr><tr><td>衛部藥輸字第027015號</td><td>安納若適膜衣錠1毫克</td><td>ANASTROZOLE</td><td>2022/06/10</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 細胞毒性

Anastrozole 為荷爾蒙類抗腫瘤藥物，不屬於傳統細胞毒性化療藥。請參考原廠仿單的警語與注意事項。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 荷爾蒙治療（非類固醇芳香環轉化酶抑制劑），非傳統細胞毒性藥物 |
| 監測項目 | 骨密度（長期使用有骨質流失風險）、肝功能、血脂 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：心肌缺血、冠狀動脈疾病（來自 TxGNN 知識圖譜的藥物－疾病關聯，並非仿單文字，臨床使用前須以仿單為準）。
- **藥物交互作用**：資料庫共收錄 147 筆可能的交互作用，目前皆未標示嚴重程度分級，部分例子包括 bupropion、pantoprazole、omeprazole、metformin、simvastatin、prednisone、acetylsalicylic acid 等。
- **其他安全訊號**：相關研究提到骨密度與肌肉密度變化（NCT00421447）、血管內皮功能影響（NCT00719966），以及個案通報的肝毒性（PMID 17033446）。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 首位預測（女性乳癌）已是台灣核准適應症，並有多個已完成的 Phase 3 RCT（含 ATAC、FALCON、IBIS-II）支持，證據等級為 L1。
- 這個預測屬於既有適應症的確認，並非新的再利用機會；排名 2–6 的預測缺乏機轉與臨床證據，應維持 Hold。

**若要推進需要：**
- 補充 DrugBank 的作用機轉資料，完善機轉連結分析。
- 若有意探索真正的新適應症，需針對排名 2–6 的候選（如神經母細胞瘤）先建立機轉假說與前臨床證據。
- 制訂長期使用的安全性監測計畫，特別是骨密度、心血管風險（有冠狀動脈疾病者）與肝功能。
- 補齊仿單的警語與禁忌症，並確認 147 筆藥物交互作用的臨床嚴重程度分級。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

