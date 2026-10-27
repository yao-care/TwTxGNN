---
layout: default
title: Cobimetinib
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
monitor_inn: "cobimetinib"
predicted_indications: ["amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "axial spondylometaphyseal dysplasia", "Mills syndrome", "amyotrophic lateral sclerosis, susceptibility to", "lower motor neuron syndrome with late-adult onset", "trichomegaly-retina pigmentary degeneration-dwarfism syndrome", "lethal arthrogryposis-anterior horn cell disease syndrome", "amyotrohpic lateral sclerosis type 22", "monomelic amyotrophy"]
last_modified_at: 2026-10-16
description: "Cobimetinib：預測新適應症為肌萎縮性側索硬化症 (Amyotrophic Lateral Sclerosis)（證據等級 L5）。原適應症：Cotellic 與 vemurafenib 併用於治療 BRAF V600 突變陽性且無法以手術切除或轉移性的黑色素瘤"
---

# Cobimetinib
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

## Cobimetinib：從 BRAF V600 突變黑色素瘤到肌萎縮性側索硬化症
{: .text-alpha }

## 一句話總結

Cobimetinib 是 MEK 抑制劑，原本與 vemurafenib 併用於治療 BRAF V600 突變陽性、無法手術切除或轉移性的黑色素瘤。
TxGNN 模型預測它可能對**肌萎縮性側索硬化症 (Amyotrophic Lateral Sclerosis, ALS)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | Cotellic 與 vemurafenib 併用於治療 BRAF V600 突變陽性且無法以手術切除或轉移性的黑色素瘤 |
| 預測新適應症 | 肌萎縮性側索硬化症 (Amyotrophic Lateral Sclerosis) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 1 張（有效單方 1／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏完整的作用機轉資料。根據已知資訊，cobimetinib 是 MEK1/2 抑制劑，會阻斷 RAS-RAF-MEK-ERK 訊號路徑，這也是它在 BRAF V600 突變黑色素瘤中發揮療效的基礎。

ERK 訊號失調曾被提出與運動神經元退化及神經發炎有關，因此從機轉上推測，抑制此路徑理論上可能影響 ALS 的病程。不過這只是理論推測，目前沒有臨床或文獻證據顯示 cobimetinib 對 ALS 有效，這個連結僅來自 TxGNN 的預測。

值得注意的是，排名前 10 的預測中，多數為運動神經元疾病（如 ALS 各亞型、Mills 症候群、單肢肌萎縮症等），另有少數罕見發育或骨骼異常，這些預測同樣都缺乏實證支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Cobimetinib 的不重複許可證共 **1 張**：有效單方 1 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第026916號 | 可泰利 膜衣錠20毫克 | 膜衣錠 | 羅氏大藥廠股份有限公司 | 2031/11/22 | Cotellic與vemurafenib併用於治療BRAF V600突變陽性且無法以手術切除或轉移性的黑色素瘤患者。 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（MEK 抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：本report 彙整的資料顯示共有 266 筆交互作用紀錄，以下為部分重要項目：
  - **嚴重 (Major)**：Aprepitant、Dexamethasone、Clarithromycin、Cobicistat、Samarium (153Sm) lexidronam
  - **中度 (Moderate)**：Cimetidine、Clotrimazole、Miconazole、Eliglustat、Naltrexone、Ticagrelor、Quinine、Ivacaftor 等

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自 TxGNN 模型（證據等級 L5），沒有臨床試驗或文獻佐證，機轉連結也只是理論推測。
- 此藥為抗腫瘤標靶藥物，且有多項嚴重藥物交互作用，在缺乏任何實證下，不宜推進到神經退化性疾病。

**若要推進需要：**
- 補充詳細的作用機轉資料，並以 ERK 路徑與運動神經元退化的關聯進行文獻回顧
- 進行 ALS 細胞或動物模型的前臨床研究，驗證 MEK 抑制的效果
- 評估藥物能否通過血腦障壁，以及長期使用於神經退化性疾病的安全性
- 完整整理原廠仿單中的警語與禁忌症
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

