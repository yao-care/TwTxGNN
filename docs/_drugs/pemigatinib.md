---
layout: default
title: Pemigatinib
parent: 僅模型預測 (L5)
nav_order: 209
evidence_level: L5
indication_count: 10
monitor_inn: "Pemigatinib"
predicted_indications: ["multiple endocrine neoplasia", "amenorrhea (disease)", "HER2 positive breast carcinoma", "cytomegalovirus infection", "infectious bovine rhinotracheitis", "malignant catarrh", "amyotrophic lateral sclerosis", "amyotrohpic lateral sclerosis type 22", "amyotrophic lateral sclerosis, susceptibility to", "axial spondylometaphyseal dysplasia"]
last_modified_at: 2026-10-16
description: "Pemigatinib：預測新適應症為多發性內分泌腫瘤 (Multiple Endocrine Neoplasia)（證據等級 L5）。原適應症：適用於成人接受過全身性藥物治療、腫瘤具有 FGFR2 融合或重排、不可手術切除的局部晚期或轉移性膽管癌"
---

# Pemigatinib
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

# Pemigatinib：從膽管癌到多發性內分泌腫瘤

## 一句話總結

Pemigatinib（達伯坦）是一種口服 FGFR 抑制劑，原本用於治療具 FGFR2 融合或重排的晚期膽管癌。
TxGNN 模型預測它可能對**多發性內分泌腫瘤 (Multiple Endocrine Neoplasia)** 有效，
但目前**沒有任何臨床試驗與文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 適用於成人接受過全身性藥物治療、腫瘤具有 FGFR2 融合或重排、不可手術切除的局部晚期或轉移性膽管癌 |
| 預測新適應症 | 多發性內分泌腫瘤 (Multiple Endocrine Neoplasia) |
| TxGNN 預測分數 | 99.71% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 3 張（有效單方 3／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Pemigatinib 是選擇性 FGFR1–3 激酶抑制劑，在 FGFR2 融合或重排的膽管癌中療效已被證實。

然而，多發性內分泌腫瘤通常由 MEN1 或 RET 等基因變異驅動，與 FGFR 訊號並無已知的因果關聯。因此，這項預測目前只建立在 TxGNN 知識圖譜的推論上，缺乏機轉面的支持。

另外值得留意的是，同一份預測清單中的其他項目（例如巨細胞病毒感染、牛傳染性鼻氣管炎、惡性卡他熱、肌萎縮性側索硬化症等），同樣沒有機轉或臨床證據支持，部分疑為知識圖譜的衍生假象。其中 HER2 陽性乳癌雖有 FGFR 訊號與抗 HER2 治療抗藥性相關的推測性理由，但目前僅有一篇泛論激酶抑制劑的文獻，並無針對 Pemigatinib 的直接證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Pemigatinib 的不重複許可證共 **3 張**：有效單方 3 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（3 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第028063號 | 達伯坦錠4.5毫克 | 錠劑 | 台灣東洋藥品工業股份有限公司 | 2031/04/23 | 適用於成人接受過全身性藥物治療、腫瘤具有FGFR2融合或重排、不可手術切除的局部晚期或轉移性膽管癌。 |
| 衛部藥輸字第028064號 | 達伯坦錠9毫克 | 錠劑 | 台灣東洋藥品工業股份有限公司 | 2031/04/23 | 適用於成人接受過全身性藥物治療、腫瘤具有FGFR2融合或重排、不可手術切除的局部晚期或轉移性膽管癌。 |
| 衛部藥輸字第028065號 | 達伯坦錠13.5毫克 | 錠劑 | 台灣東洋藥品工業股份有限公司 | 2031/04/23 | 適用於成人接受過全身性藥物治療、腫瘤具有FGFR2融合或重排、不可手術切除的局部晚期或轉移性膽管癌。 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（FGFR 激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：本報告彙整的資料共記錄 50 筆交互作用，以下為其中主要項目：
  - **嚴重（Major）**：Aprepitant、Dexamethasone、Clarithromycin、Cobicistat、Lumacaftor、Chloramphenicol、Erythromycin、Ketoconazole、Fluconazole
  - **中度（Moderate）**：Cimetidine、Metreleptin、Clotrimazole、Glycerol phenylbutyrate、Troglitazone、Deferasirox、Ivacaftor、Zafirlukast、Griseofulvin、Elagolix、Osilodrostat
  - 多數嚴重交互作用藥物為 CYP3A4 抑制劑或誘導劑，併用時需謹慎評估（此為依藥物類別的一般推論，請以仿單為準）。

其他警語與禁忌症資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這項預測沒有任何臨床試驗或文獻支持，證據等級為 L5，僅有模型分數。
- 多發性內分泌腫瘤的致病機轉（MEN1、RET 變異）與 FGFR 抑制無已知關聯，機轉上缺乏合理性。

**若要推進需要：**
- 補充 Pemigatinib 的完整作用機轉資料，並釐清 FGFR 訊號是否參與多發性內分泌腫瘤的病理。
- 進行前臨床研究（如細胞或動物模型）驗證 FGFR 抑制對相關腫瘤的作用。
- 系統性檢索文獻與試驗登記，確認是否有任何間接證據。
- 在證據出現前，建議將資源優先放在已有機轉或初步文獻支持的候選適應症上（例如 HER2 陽性乳癌的 FGFR 相關抗藥性假說），並先補足安全性（警語、禁忌症）資料。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證數寫 6 張 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

