---
layout: default
title: Titanium Dioxide
parent: 僅模型預測 (L5)
nav_order: 281
evidence_level: L5
indication_count: 10
monitor_inn: "Titanium dioxide"
predicted_indications: ["drug-induced osteoporosis", "diabetic retinopathy", "diabetic cataract", "severe nonproliferative diabetic retinopathy", "tetanic cataract", "craniostenosis cataract", "diabetes mellitus type 2 associated cataract", "immature cataract", "mature cataract", "nuclear senile cataract"]
last_modified_at: 2026-10-29
description: "Titanium Dioxide：預測新適應症為藥物性骨質疏鬆症 (Drug-induced Osteoporosis)（證據等級 L5）。原適應症：外用抗刺激劑"
---

# Titanium Dioxide
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

## Titanium dioxide（二氧化鈦）：從外用抗刺激／保護劑到藥物性骨質疏鬆症
{: .text-alpha }

## 一句話總結

二氧化鈦在台灣曾以單方作為外用抗刺激劑與局部保護劑，另有數個複方許可證使用其成分。
TxGNN 模型預測它可能對**藥物性骨質疏鬆症 (Drug-induced Osteoporosis)** 有效，但目前**無任何臨床試驗與文獻**直接支持此預測，僅為模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 外用抗刺激劑（單方許可證，已註銷） |
| 預測新適應症 | 藥物性骨質疏鬆症 (Drug-induced Osteoporosis) |
| TxGNN 預測分數 | 1.0000 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 1 張／共 7 張） |
| 許可證數 | 7 張（有效單方 0／有效複方 1／已過期 1／已註銷 5） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。二氧化鈦是一種惰性的無機顏料，臨床上主要作為外用保護劑，使用於皮膚表面以減少刺激。已知資訊中，並無證據顯示它會影響骨重塑（骨吸收或骨生成）。

因此，原適應症（外用保護、抗刺激）與預測的藥物性骨質疏鬆症之間，缺乏已知的機轉關聯。這項預測目前僅來自 TxGNN 模型（深度學習），可能反映模型從相關疾病間學到的相似性，並非生物學證據，無法以藥理學解釋。

其他分數接近的預測（如糖尿病視網膜病變、各型白內障）同樣沒有治療機轉支持。糖尿病視網膜病變相關文獻僅把二氧化鈦當作分析或影像材料使用，並非治療用途。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對預測適應症「藥物性骨質疏鬆症」，目前無相關文獻。

作為參考，排名第二的預測「糖尿病視網膜病變」有 5 篇檢索文獻，但皆未研究二氧化鈦對該疾病的治療效果：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36197877](https://pubmed.ncbi.nlm.nih.gov/36197877/) | 2022 | 體外研究 | Analytical Chemistry | 以二氧化鈦微粒純化血漿胞外囊泡，用於糖尿病視網膜病變的代謝特徵分析（分析工具用途） |
| [41637842](https://pubmed.ncbi.nlm.nih.gov/41637842/) | 2026 | Review | J Trace Elem Med Biol | 金屬奈米粒子於糖尿病的機轉與治療展望（一般性背景） |
| [38078945](https://pubmed.ncbi.nlm.nih.gov/38078945/) | 2023 | 體外研究 | Analytical Chemistry | pH 調控的選擇性系統，用於分析胞外囊泡與脂蛋白攜帶的 RNA |
| [39566751](https://pubmed.ncbi.nlm.nih.gov/39566751/) | 2025 | 體外研究 | Methods | 超小二氧化鈦奈米粒子與螢光素結合物，用於改善眼底螢光血管攝影 |
| [20059246](https://pubmed.ncbi.nlm.nih.gov/20059246/) | 2009 | 體外研究 | J Biomed Optics | 用於視網膜血氧測量的動態眼模型 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Titanium Dioxide 的不重複許可證共 **7 張**：有效單方 0 張、有效複方 1 張、已過期 1 張（未註銷但有效日期早於資料集日期）、已註銷 5 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（1 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第029248號 | 生達綜合感冒膠囊 | NEW COCCINE、DEXTROMETHORPHAN HBR、CHLORPHENIRAMINE MALEATE、TI… | 膠囊劑 | 感冒諸症狀（流鼻水、鼻塞、打噴嚏、咽喉痛、咳嗽、畏寒、發燒、頭痛、關節痛、肌肉痛等）之緩解。 |

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-09-29）</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛署藥輸字第012019號</td><td>欣若維豐膠囊</td><td>RIBOFLAVIN (VIT B2)、WAX WHITE、SOYBEAN OIL ( EQ TO SOYA BEAN…</td><td>2004/12/25</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（5 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥輸字第000504號</td><td>二氧化鈦</td><td>TITANIUM DIOXIDE (EQ TO TITANIUM OXIDE)</td><td>2005/06/16</td></tr><tr><td>內衛藥輸字第000977號</td><td>二氧化鈦糊劑</td><td>TITANIUM DIOXIDE (EQ TO TITANIUM OXIDE)</td><td>1986/03/15</td></tr><tr><td>衛署藥製字第036023號</td><td>多維鋅膜衣錠</td><td>PYRIDOXINE HCL、NIACINAMIDE (NICOTINAMIDE)、FOLIC ACID、RIBOFLA…</td><td>2014/05/15</td></tr><tr><td>衛署藥輸字第012421號</td><td>二氧化鈦</td><td>TITANIUM DIOXIDE (EQ TO TITANIUM OXIDE)</td><td>1994/06/27</td></tr><tr><td>衛署藥輸字第019682號</td><td>達帕氏通膠囊</td><td>LEVODOPA、TITANIUM DIOXIDE (EQ TO TITANIUM OXIDE)</td><td>2000/10/20</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測完全來自模型，沒有任何針對藥物性骨質疏鬆症的臨床試驗或文獻，也無已知機轉，證據等級為 L5。
- 二氧化鈦為惰性外用保護劑，其許可證 7 張中目前仍有 1 張有效（市場上仍有販售），不建議以此預測推進開發。

**若要推進需要：**
- 補齊作用機轉資料，並釐清二氧化鈦是否與骨代謝有任何生物學關聯。
- 進行系統性文獻檢索與前臨床（體外或動物）研究，以驗證對骨質疏鬆的效果。
- 評估給藥途徑的可行性（目前為外用或複方口服成分，與骨質疏鬆治療所需的全身性給藥是否相容尚待確認）。
- 取得完整安全性資料（警語、禁忌、藥物交互作用）。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 台灣上市資訊表的達帕氏通膠囊、富腦膠囊 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

