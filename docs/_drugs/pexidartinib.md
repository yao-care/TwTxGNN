---
layout: default
title: Pexidartinib
parent: 僅模型預測 (L5)
nav_order: 215
evidence_level: L5
indication_count: 10
monitor_inn: "Pexidartinib"
predicted_indications: ["HER2 positive breast carcinoma", "normal breast-like subtype of breast carcinoma", "progesterone-receptor positive breast cancer", "progesterone-receptor negative breast cancer", "breast tumor luminal A or B", "synovium cancer", "synovium disease", "dermatofibrosarcoma protuberans", "multifocal choroiditis", "malignant giant cell tumor"]
last_modified_at: 2026-10-27
description: "Pexidartinib：預測新適應症為HER2 陽性乳癌 (HER2 positive breast carcinoma)（證據等級 L5）。原適應症：無法透過手術或其他治療(如局部放射線治療)改善，且具嚴重後遺症或嚴重功能受限的症狀性腱鞘巨細胞瘤(TGCT)成人病人"
---

# Pexidartinib
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

## Pexidartinib：CSF1R/KIT/FLT3 酪胺酸激酶抑制劑 → HER2 陽性乳癌 (HER2 positive breast carcinoma)
{: .text-alpha }

## 一句話總結

Pexidartinib 是一種口服的 CSF1R、KIT 與 FLT3 酪胺酸激酶抑制劑。
TxGNN 模型預測它可能對 **HER2 陽性乳癌 (HER2 positive breast carcinoma)** 有效，
但目前沒有臨床試驗，僅有 **1 篇**動物研究文獻與機轉推論，且該文獻探討的是 HR+/HER2- 乳癌，並非 HER2 陽性乳癌本身。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無法透過手術或其他治療(如局部放射線治療)改善，且具嚴重後遺症或嚴重功能受限的症狀性腱鞘巨細胞瘤(TGCT)成人病人。 |
| 預測新適應症 | HER2 陽性乳癌 (HER2 positive breast carcinoma) |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5 |
| 台灣上市 | 未上市（已註銷許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效單方 0／有效複方 0／已註銷 1） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Pexidartinib 抑制 CSF1R，可能減少腫瘤相關巨噬細胞所造成的免疫抑制。這種機轉在乳癌的腫瘤微環境中理論上可能有意義。

唯一相關的文獻是一項動物研究，探討 CSF1R 抑制劑如何減輕 CDK4/6 抑制劑引起的免疫抑制，對象為 HR+/HER2- 乳癌。這項研究並未直接以 HER2 陽性乳癌為研究對象，也沒有任何 HER2 相關的臨床資料。因此本預測目前僅屬前臨床層級的機轉推論，不能視為已有直接證據。

依據嚴格的證據等級規則，沒有任何研究直接針對預測疾病本身，證據等級只能列為 L5。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41986650](https://pubmed.ncbi.nlm.nih.gov/41986650/) | 2026 | 動物研究 | Oncogene | CSF1R 抑制劑可減輕 CDK4/6 抑制劑引起的免疫抑制，提升 HR+/HER2- 乳癌的抗腫瘤免疫（研究對象並非 HER2 陽性乳癌） |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Pexidartinib 的不重複許可證共 **1 張**：有效單方 0 張、有效複方 0 張、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛部藥輸字第028293號</td><td>圖拉留膠囊200毫克</td><td>Pexidartinib HCl</td><td>2026/02/03</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 肝功能（文獻指出長期使用需留意肝臟安全性）、血液學參數 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：共查得 262 項交互作用，負擔偏高。主要者包括：
  - 重大 (Major)：Acarbose、Rabeprazole、Omeprazole、Dexlansoprazole、Doxycycline、Tetracycline、Minocycline、Pioglitazone、Bupropion、Aprepitant、Clarithromycin、Chenodeoxycholic acid
  - 中等 (Moderate)：Famotidine、Ranitidine、Cimetidine、Metformin、Dexamethasone、Budesonide、Magnesium oxide、Saxagliptin
- **肝臟安全性**：已有文獻專門評估本藥在腱鞘巨細胞瘤病人的長期肝臟安全性，使用時須嚴密監測肝功能。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有任何臨床試驗，唯一相關文獻為 HR+/HER2- 乳癌的動物研究，並非 HER2 陽性乳癌，證據等級僅為 L5。
- 藥物有肝毒性疑慮與高度藥物交互作用負擔，在缺乏療效證據下，不宜直接推進。

**若要推進需要：**
- 針對 HER2 陽性乳癌的前臨床研究（細胞株或動物模型），驗證 CSF1R 抑制的效果
- 與 HER2 標靶藥物併用的機轉與安全性評估
- 詳細的藥物作用機轉資料（MOA）
- 評估肝毒性風險與乳癌病人用藥的風險效益
- 確認台灣許可證現況與可及性

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「台灣上市 ✓ 已上市」（唯一許可證已註銷） | 報告重生後已無此錯誤（2026-10-28：報告重產與事實層改寫後，本紀錄指出的錯誤原文已不在正文（僅見於本頁查核紀錄表或程式產生的許可證表）（2026-10-28 用戶核准的處理方案）；原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證數寫 2 張 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

