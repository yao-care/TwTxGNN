---
layout: default
title: Axitinib
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 10
---

# Axitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Axitinib：從晚期腎細胞癌到未分類腎細胞癌

## 一句話總結

Axitinib 是口服的 VEGFR 酪胺酸激酶抑制劑，原本用於曾接受 sunitinib 或 cytokine 治療失敗的晚期腎細胞癌。
TxGNN 模型預測它可能對**未分類腎細胞癌 (unclassified renal cell carcinoma)** 有效，分數為 99.90%。
但這個首位預測目前**沒有任何臨床試驗或文獻**直接支持，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 治療已接受過 sunitinib 或 cytokine 治療失敗的晚期腎細胞癌病患 |
| 預測新適應症 | 未分類腎細胞癌 (unclassified renal cell carcinoma) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 2 張（有效單方 2／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

> 補充：排名前 10 的預測中，「腎細胞癌 (renal carcinoma)」一項證據最完整（L1），但那屬於已核准的適應症，不算真正的藥物再利用。詳見下方「其他預測的證據概況」。

---

## 為什麼這個預測合理？

Axitinib 是選擇性的 VEGFR-1、-2、-3 抑制劑，透過阻斷腫瘤血管新生來抑制腫瘤生長。腎細胞癌（尤其是透明細胞型）的生長高度依賴 VEGF 訊號，因此 VEGFR 抑制劑是此類癌症的核心治療。目前缺乏 DrugBank 的詳細作用機轉資料，以上機轉說明來自本次整理的文獻與預測資料。

「未分類腎細胞癌」同屬腎細胞癌大類，原適應症與新適應症在疾病生物學上高度相關，所以模型給出高分並不意外。不過，這類亞型的腫瘤生物學差異大，已核准適應症的證據不能直接套用。

目前沒有針對此亞型的試驗或文獻，這個預測只能視為假說。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 其他預測的證據概況

以下是排名前 10 的其他預測中，具有證據者：

| 預測適應症 | 證據等級 | 主要證據 | 建議 |
|-----------|---------|---------|------|
| 腎細胞癌 (renal carcinoma) | L1 | [AXIS（NCT00678392）](https://clinicaltrials.gov/study/NCT00678392) 與 [KEYNOTE-426（NCT02853331）](https://clinicaltrials.gov/study/NCT02853331) 等已完成 Phase 3 試驗；[PMID 30779529](https://pubmed.ncbi.nlm.nih.gov/30779529/)、[30779531](https://pubmed.ncbi.nlm.nih.gov/30779531/) 等 RCT | Proceed with Guardrails（屬已核准範圍） |
| TFE3 轉位型腎細胞癌 | L3 | [NCT03595124](https://clinicaltrials.gov/study/NCT03595124)：Phase 2，axitinib+nivolumab，僅 15 人，進行中 | Research Question |
| 集尿管癌 (collecting duct carcinoma) | L4 | [NCT06211114](https://clinicaltrials.gov/study/NCT06211114)：Phase 2，30 人，招募中；病例報告 [PMID 36341193](https://pubmed.ncbi.nlm.nih.gov/36341193/) | Research Question |
| 兒童腎細胞癌 | L4 | 一篇回顧 [PMID 31012542](https://pubmed.ncbi.nlm.nih.gov/31012542/) 與一則病例 [PMID 26279736](https://pubmed.ncbi.nlm.nih.gov/26279736/) | Research Question |
| 脂肪肉瘤 | L4 | 僅體外研究 [PMID 27822137](https://pubmed.ncbi.nlm.nih.gov/27822137/) | Hold |
| 腎細胞癌合併神經母細胞瘤、卵巢黏液樣脂肪肉瘤、血管脂肪瘤、家族性自發性氣胸 | L5 | 無 | Hold |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Axitinib 的不重複許可證共 **2 張**：有效單方 2 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第025853號 | 抑癌特膜衣錠 1 毫克 | 膜衣錠 | 輝瑞大藥廠股份有限公司 | 2027/11/13 | 治療已接受過sunitinib或cytokine治療失敗的晚期腎細胞癌病患。 |
| 衛署藥輸字第025854號 | 抑癌特膜衣錠 5 毫克 | 膜衣錠 | 輝瑞大藥廠股份有限公司 | 2027/11/13 | 治療已接受過sunitinib或cytokine治療失敗的晚期腎細胞癌病患。 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（VEGFR 酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 高血壓、肝功能（依本次整理資料所列風險） |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**：共記錄 178 筆交互作用。Axitinib 為 CYP3A4/5 受質，需特別留意強效抑制劑或誘導劑。主要例子如下：
  - **重大（Major）**：Clarithromycin、Dexamethasone
  - **中度（Moderate）**：Aprepitant、Clotrimazole、Miconazole、Naltrexone
  - **輕微（Minor）**：Famotidine、Ranitidine、Cimetidine、Rabeprazole、Esomeprazole、Lansoprazole 及多種制酸劑（氫氧化鋁、碳酸鈣、氫氧化鎂等）
- **需留意的不良反應**：高血壓與肝毒性（來自本次整理的評估資料）。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測「未分類腎細胞癌」只有模型分數支持，沒有任何試驗或文獻，證據等級為 L5。
- 腎細胞癌大類已是核准適應症，並有多項 Phase 3 RCT（AXIS、KEYNOTE-426、JAVELIN Renal 101 等）支持，但這是既有用途，不是新的再利用機會。

**若要推進需要：**
- 針對未分類腎細胞癌的回顧性病例資料或小型前瞻性研究，確認 axitinib 的療效訊號。
- 補充作用機轉資料（MOA）。
- 若考慮罕見亞型（如 TFE3 轉位型、集尿管癌），可追蹤 NCT03595124 與 NCT06211114 的結果。
- 擬定 CYP3A4 交互作用管理，以及高血壓與肝功能的監測計畫。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | Axitinib 台灣中文品名寫成「英利達」 | 報告重生後已無此錯誤（2026-10-15：新報告正文未再出現中文品名「英利達」；原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表只列出 pembrolizumab（吉舒達）的許可證 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

