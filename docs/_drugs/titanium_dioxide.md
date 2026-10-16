---
layout: default
title: Titanium Dioxide
parent: 僅模型預測 (L5)
nav_order: 281
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-16
description: "Titanium Dioxide：預測新適應症為藥物誘發性骨質疏鬆 (Drug-induced Osteoporosis)（證據等級 L5）。原適應症：外用抗刺激劑"
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Titanium dioxide：從外用抗刺激劑／局部保護劑到藥物誘發性骨質疏鬆

## 一句話總結

二氧化鈦（Titanium dioxide）是一種惰性的外用物理性保護劑，在台灣原本以糊劑或粉劑用於皮膚的局部保護與抗刺激，也出現在數種複方製劑中。
TxGNN 模型預測它可能對**藥物誘發性骨質疏鬆 (Drug-induced Osteoporosis)** 有效，但目前**沒有任何臨床試驗與相關文獻**支持這個方向，預測僅來自模型分數。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 外用抗刺激劑（單方許可證，已註銷） |
| 預測新適應症 | 藥物誘發性骨質疏鬆 (Drug-induced Osteoporosis) |
| TxGNN 預測分數 | 99.9998% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市（僅複方仍有效） |
| 許可證數 | 7 張（有效單方 0／有效複方 1／已過期 1／已註銷 5） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。二氧化鈦是一種惰性色素與外用物理性保護劑，其已知用途是在皮膚表面形成屏障、保護並減少刺激，並非透過特定的藥理標的發揮作用。

原適應症（皮膚局部保護）與骨代謝之間，在現有資料中找不到已建立的藥理關聯。這項預測目前只建立在 TxGNN 知識圖譜的模型分數上，無法從機轉角度解釋為何二氧化鈦可能影響骨質流失。

其他排名靠前的預測（糖尿病視網膜病變與各類白內障）同樣沒有機轉或臨床依據。針對糖尿病視網膜病變檢索到的 5 篇文獻，內容都是把二氧化鈦當作分析或影像材料（如細胞外囊泡純化、螢光素奈米粒子視網膜造影、眼球模型），而不是治療用途。因此，本報告將這些預測視為模型假說，而非有根據的再利用機會。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前針對「藥物誘發性骨質疏鬆」無相關文獻。

---

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

---

## 安全性考量

安全性資訊請參考原廠仿單。本次整理的資料中，藥物交互作用查詢未找到紀錄，知識圖譜亦無禁忌症連結。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數（證據等級 L5），沒有臨床試驗、文獻或任何機轉支持。二氧化鈦是惰性外用保護劑，與骨代謝缺乏合理關聯，且原始作用機轉資料也缺漏。
- 現有單方許可證皆已註銷，仍有效的許可證都是口服複方，與外用的原用途不同，也無法歸因於二氧化鈦本身。

**若要推進需要：**
- 補齊作用機轉（MOA）資料，並釐清二氧化鈦是否有任何全身性生物活性。
- 以文獻與前臨床研究檢視二氧化鈦與骨代謝（成骨／蝕骨細胞）的關聯。
- 評估給藥途徑的可行性：外用惰性物質難以達到治療骨質疏鬆所需的全身暴露。
- 在投入資源前，先由專家審視 TxGNN 預測是否為知識圖譜的人為關聯。

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

