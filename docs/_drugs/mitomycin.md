---
layout: default
title: Mitomycin
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
monitor_inn: "mitomycin"
predicted_indications: ["solid pseudopapillary carcinoma of pancreas", "osteoclastic giant cell tumor of pancreas", "pancreatic carcinoma with mixed differentiation", "pancreatic intraductal papillary-mucinous carcinoma", "mixed ductal-endocrine carcinoma of pancreas", "pancreatic signet ring cell adenocarcinoma", "undifferentiated pancreatic carcinoma", "malignant exocrine pancreas neoplasm", "pancreatic intraductal papillary-mucinous neoplasm", "pancreatic acinar cell cystadenocarcinoma"]
last_modified_at: 2026-10-16
description: "Mitomycin：預測新適應症為胰臟實體假乳突癌 (Solid Pseudopapillary Carcinoma of Pancreas)（證據等級 L5）。原適應症：胃癌、膀胱癌（灌注使用）、肺癌、肉瘤、白血病等症狀之緩解"
---

# Mitomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Mitomycin：從胃癌、膀胱癌到胰臟實體假乳突癌
{: .text-alpha }

## 一句話總結

Mitomycin（密多邁杏）是一種 DNA 交聯型的細胞毒性抗腫瘤藥物，在台灣核准用於胃癌、膀胱癌（灌注使用）、肺癌、肉瘤、白血病等症狀的緩解。
TxGNN 模型預測它可能對**胰臟實體假乳突癌 (Solid Pseudopapillary Carcinoma of Pancreas)** 有效，但目前**沒有相關臨床試驗與文獻**支持，證據僅來自模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃癌、膀胱癌（灌注使用）、肺癌、肉瘤、白血病等症狀之緩解 |
| 預測新適應症 | 胰臟實體假乳突癌 (Solid Pseudopapillary Carcinoma of Pancreas) |
| TxGNN 預測分數 | 0.9986 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 1 張／共 9 張） |
| 許可證數 | 9 張（有效單方 1／有效複方 0／已註銷 8） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Mitomycin 屬於 DNA 交聯型烷化劑，是一種需經生物還原活化的細胞毒性藥物，能抑制增生中腫瘤細胞的 DNA 複製。這類廣譜的抗增生作用，在機轉上有可能延伸到胰臟上皮來源的腫瘤。

本次 TxGNN 模型（深度學習）的前 10 名預測皆為胰臟腫瘤，主要預測為胰臟實體假乳突癌（胰臟實體假乳突癌，solid pseudopapillary carcinoma of pancreas），分數 0.9986；其餘分數介於 0.9982 至 0.9986。這些分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據。

不過，這些連結目前只建立在模型預測上。就實體假乳突癌而言，沒有任何臨床或文獻證據顯示 Mitomycin 對其有效，因此只能視為待驗證的假說。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首位預測（實體假乳突癌）目前無相關文獻。

以下為同屬胰臟腫瘤的其他預測項目所檢索到的文獻，僅供背景參考，均未直接證明 Mitomycin 的療效：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15983445](https://pubmed.ncbi.nlm.nih.gov/15983445/) | 2005 | Case series | Pancreatology | 偽黏液性腹膜瘤合併胰臟導管內乳突黏液性腫瘤的個案，以腹腔內溫熱化療灌注處理；並未提供 Mitomycin 對該疾病的療效證據 |
| [8361472](https://pubmed.ncbi.nlm.nih.gov/8361472/) | 1993 | Cohort | Nihon Geka Gakkai Zasshi | 胰臟癌切除後，在免疫化學療法（含 Tegafur、Mitomycin 等）上加用 Tamoxifen；重點在荷爾蒙治療，不能直接支持 Mitomycin |
| [10897253](https://pubmed.ncbi.nlm.nih.gov/10897253/) | 2000 | Review | Strahlenther Onkol | 導管型胰臟癌的術後輔助與術前放化療回顧 |
| [2695183](https://pubmed.ncbi.nlm.nih.gov/2695183/) | 1989 | Review | Bull Cancer | 原發部位不明腫瘤的診斷與治療，與 Mitomycin 無特定關聯 |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Mitomycin 的不重複許可證共 **9 張**：有效單方 1 張、有效複方 0 張、已註銷 8 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第028315號 | 密多邁杏凍晶注射劑 | 凍晶注射劑 | 韋淳貿易股份有限公司 | 2027/05/26 | 胃癌、膀胱癌（灌注使用）、肺癌、肉瘤、白血病等症狀之緩解。 |

<details><summary><strong>已註銷</strong>（8 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥輸字第003510號</td><td>排多癌錠</td><td>MITOMYCIN C</td><td>1999/09/22</td></tr><tr><td>內衛藥輸字第003756號</td><td>排多癌針</td><td>MITOMYCIN C</td><td>1985/08/09</td></tr><tr><td>衛署藥輸字第008190號</td><td>排多癌注射劑１０公絲</td><td>MITOMYCIN C</td><td>1988/03/25</td></tr><tr><td>衛署藥輸字第013731號</td><td>排多癌注射劑</td><td>MITOMYCIN C</td><td>1988/03/25</td></tr><tr><td>衛署藥輸字第016381號</td><td>排多癌注射劑１０公絲</td><td>MITOMYCIN C</td><td>1995/12/08</td></tr><tr><td>衛署藥輸字第016382號</td><td>排多癌注射劑</td><td>MITOMYCIN C</td><td>1995/12/08</td></tr><tr><td>衛署藥輸字第021025號</td><td>排多癌注射劑</td><td>MITOMYCIN C</td><td>2016/05/30</td></tr><tr><td>衛署藥輸字第021026號</td><td>"協和" 排多癌注射劑１０公絲</td><td>MITOMYCIN C</td><td>2025/06/11</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（DNA 交聯烷化劑，抗腫瘤抗生素類） |
| 骨髓抑制風險 | 高（知識圖譜顯示與血小板低下、白血球低下、貧血等血液學疾病有禁忌關聯） |
| 致吐性分級 | 中度 |
| 監測項目 | CBC（含血小板與分類）、腎功能、肝功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

詳細警語請參考原廠仿單。

---

## 安全性考量

- **知識圖譜標示的禁忌關聯疾病**（來自 TxGNN 知識圖譜，並非仿單內容）：腎臟疾病、膿尿輸尿管、血小板低下、凝血疾病、貧血、巨球性貧血、白血球低下、溶血尿毒症候群（含典型）、充血性心衰竭、心臟衰竭、口腔炎。
- **藥物交互作用**：共查得 193 筆，主要例子如下：
  - **Major**：Deferiprone、Samarium (153Sm) lexidronam
  - **Moderate**：Palifermin、Strontium chloride Sr-89、Fostamatinib
  - **Minor**：Levofloxacin
  - 其餘（如 Warfarin、Dexamethasone、Ondansetron 等）等級未知，需進一步確認。

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（0.9986），但沒有任何臨床試驗或直接文獻支持，證據等級為 L5。
- 實體假乳突癌通常以手術為主，Mitomycin 的角色缺乏依據；同時 Mitomycin 骨髓抑制風險高、安全性負擔大，現階段不宜推進。

**若要推進需要：**
- 補齊作用機轉（MOA）資料，釐清與胰臟腫瘤的機轉連結。
- 系統性搜尋 Mitomycin 用於各類胰臟腫瘤（特別是胰臟腺癌、胰臟印戒細胞腺癌）的臨床與前臨床證據。
- 進行前臨床研究（如細胞株或類器官試驗）驗證對實體假乳突癌的敏感性。
- 取得完整的仿單警語、禁忌症與血液毒性監測計畫。
- 評估各預測項目的優先順序，並考慮改以證據較多的胰臟癌亞型作為驗證起點。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

