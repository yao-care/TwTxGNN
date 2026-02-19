---
layout: default
title: 資料來源
nav_order: 7
description: "TwTxGNN 使用的資料來源說明"
permalink: /sources/
---

# 資料來源
{: .fs-9 }

本專案使用的資料庫與來源說明
{: .fs-6 .fw-300 }

---

## 資料來源總覽

| 資料類型 | 來源 | 用途 |
|---------|------|------|
| AI 預測 | TxGNN | 藥物-疾病關聯預測 |
| 臨床試驗 | ClinicalTrials.gov | 驗證臨床證據 |
| 學術文獻 | PubMed | 驗證研究證據 |
| 藥物資訊 | DrugBank | 藥理機轉說明 |
| 台灣許可 | TFDA | 台灣上市資訊 |
| 藥物交互 | DDInter, GtoPdb | DDI 資訊 |

---

## TxGNN 模型

### 簡介

TxGNN 是由哈佛醫學院 Marinka Zitnik 教授團隊開發的藥物再利用預測模型。

### 論文資訊

- **標題**：A foundation model for clinician-centered drug repurposing
- **期刊**：Nature Medicine (2023)
- **DOI**：[10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

### 資料規模

| 項目 | 數量 |
|------|------|
| 節點數 | 17,080 |
| 藥物數 | 4,465 |
| 疾病數 | 2,870 |
| 已知藥物-疾病關聯 | 14,573 |

### 資料下載

- [node.csv](https://dataverse.harvard.edu/api/access/datafile/7144482) - 節點資料
- [kg.csv](https://dataverse.harvard.edu/api/access/datafile/7144484) - 知識圖譜

---

## ClinicalTrials.gov

### 簡介

美國國家衛生研究院 (NIH) 維護的全球最大臨床試驗登記資料庫。

### 網址

[https://clinicaltrials.gov/](https://clinicaltrials.gov/)

### 使用方式

- 透過 API 搜尋藥物名稱 + 疾病名稱
- 收集試驗編號、階段、狀態、人數等資訊

### 收集欄位

| 欄位 | 說明 |
|------|------|
| NCT Number | 試驗唯一識別碼 |
| Phase | 試驗階段 (Phase 1-4) |
| Status | 試驗狀態 |
| Enrollment | 受試者人數 |
| Conditions | 研究的疾病 |
| Interventions | 介入措施（藥物）|

---

## PubMed

### 簡介

美國國家醫學圖書館 (NLM) 維護的生物醫學文獻資料庫。

### 網址

[https://pubmed.ncbi.nlm.nih.gov/](https://pubmed.ncbi.nlm.nih.gov/)

### 使用方式

- 透過 E-utilities API 搜尋
- 藥物名稱 + 疾病名稱作為關鍵字

### 收集欄位

| 欄位 | 說明 |
|------|------|
| PMID | PubMed 唯一識別碼 |
| Title | 文章標題 |
| Year | 發表年份 |
| Journal | 發表期刊 |
| Abstract | 摘要內容 |
| Publication Type | 文獻類型 |

---

## DrugBank

### 簡介

加拿大 OMx Personal Health Analytics 維護的綜合藥物資料庫。

### 網址

[https://go.drugbank.com/](https://go.drugbank.com/)

### 收集欄位

| 欄位 | 說明 |
|------|------|
| DrugBank ID | 藥物唯一識別碼 |
| Name | 藥物名稱 |
| Mechanism of Action | 作用機轉 |
| Pharmacodynamics | 藥效學 |
| Indication | 適應症 |

---

## 衛福部食藥署 (TFDA)

### 簡介

台灣衛生福利部食品藥物管理署，負責藥品許可證管理。

### 資料來源

[政府資料開放平臺 - 藥品許可證資料集](https://data.fda.gov.tw/)

### 收集欄位

| 欄位 | 說明 |
|------|------|
| 許可證號 | 藥品許可證字號 |
| 中文品名 | 藥品中文名稱 |
| 英文品名 | 藥品英文名稱 |
| 劑型 | 藥品劑型 |
| 適應症 | 核准適應症 |
| 許可證狀態 | 有效/註銷 |

---

## 藥物交互作用 (DDI)

### DDInter 2.0

- **網址**：[https://ddinter2.scbdd.com/](https://ddinter2.scbdd.com/)
- **規模**：302,516 DDI 資料、2,310 藥物
- **用途**：藥物-藥物交互作用資訊

### Guide to PHARMACOLOGY (GtoPdb)

- **網址**：[https://www.guidetopharmacology.org/](https://www.guidetopharmacology.org/)
- **維護**：IUPHAR/BPS
- **用途**：核准藥物交互作用

### 資料規模

| 來源 | DDI 數量 | 更新日期 |
|------|---------|----------|
| DDInter | 222,391 筆 | 2026-02-08 |
| GtoPdb | 4,636 筆 | 2026-02-08 |

---

## 資料更新頻率

| 資料類型 | 更新頻率 |
|---------|----------|
| TxGNN 預測 | 模型版本更新時 |
| 臨床試驗 | 報告產出時 |
| PubMed 文獻 | 報告產出時 |
| TFDA 許可證 | 報告產出時 |
| DDI 資料 | 每季建議更新 |

---

## 授權與引用

使用本專案資料時，請同時引用原始資料來源。

### TxGNN 引用

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and others},
  journal={Nature Medicine},
  year={2023},
  doi={10.1038/s41591-023-02233-x}
}
```

### 本專案引用

```bibtex
@misc{twtxgnn2026,
  title={TwTxGNN: Taiwan Drug Repurposing Validation Reports},
  url={https://twtxgnn.yao.care},
  year={2026}
}
```
