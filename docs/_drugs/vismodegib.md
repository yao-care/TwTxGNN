---
layout: default
title: Vismodegib
parent: 僅模型預測 (L5)
nav_order: 302
evidence_level: L5
indication_count: 8
monitor_inn: "Vismodegib"
predicted_indications: ["medulloblastoma with extensive nodularity", "xeroderma pigmentosum", "annular epidermolytic ichthyosis", "epidermolysis bullosa simplex with mottled pigmentation", "Brenner tumor", "cutaneous adenocystic carcinoma", "prostate leiomyoma", "benign neoplasm of sweat gland"]
last_modified_at: 2026-10-29
description: "Vismodegib：預測新適應症為伴有廣泛結節的髓母細胞瘤 (medulloblastoma with extensive nodularity)（證據等級 L5）。原適應症：治療轉移性基底細胞癌，或不適合接受手術或放射線治療之局部晚期(Locally Advanced)基底細胞癌成人病患"
---

# Vismodegib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

## Vismodegib：Hedgehog 訊號路徑（SMO）抑制劑 → 伴有廣泛結節的髓母細胞瘤 (medulloblastoma with extensive nodularity)
{: .text-alpha }

## 一句話總結

Vismodegib 是口服 Hedgehog 訊號路徑抑制劑，作用於 Smoothened (SMO)。
TxGNN 模型預測它可能對**伴有廣泛結節的髓母細胞瘤 (medulloblastoma with extensive nodularity)** 有效，
但目前本報告彙整的資料中**沒有臨床試驗與文獻**直接支持此預測，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 治療轉移性基底細胞癌，或不適合接受手術或放射線治療之局部晚期(Locally Advanced)基底細胞癌成人病患。 |
| 預測新適應症 | 伴有廣泛結節的髓母細胞瘤 (medulloblastoma with extensive nodularity) |
| TxGNN 預測分數 | 0.9993 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效單方 1／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未收錄 MOA）。依本報告彙整的資料，Vismodegib 為 SMO 抑制劑，可阻斷 Hedgehog 訊號路徑。

髓母細胞瘤中的 SHH 亞型依賴 Hedgehog 路徑的異常活化，因此在機轉上，抑制 SMO 有可能對此類腫瘤產生作用。不過，針對此特定亞型（廣泛結節型），目前沒有任何臨床試驗或文獻被納入，支持僅來自 TxGNN 模型預測，尚無法視為已被驗證。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Vismodegib 的不重複許可證共 **1 張**：有效單方 1 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第026444號 | 愛維德膠囊150毫克 | 膠囊劑 | 羅氏大藥廠股份有限公司 | 2030/03/13 | 治療轉移性基底細胞癌，或不適合接受手術或放射線治療之局部晚期(Locally Advanced)基底細胞癌成人病患。 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（Hedgehog 路徑／SMO 抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：本次共查得 56 筆交互作用紀錄，以下為部分重點：
  - **中度**：Clarithromycin
  - **輕微**：制酸劑與胃酸抑制劑類，例如 Famotidine、Ranitidine、Cimetidine、Nizatidine、Omeprazole、Esomeprazole、Lansoprazole、Pantoprazole、Rabeprazole、Dexlansoprazole，以及 Calcium carbonate、Aluminum hydroxide、Magnesium oxide、Sodium bicarbonate 等

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自 TxGNN 模型（分數 0.9993），沒有直接針對伴有廣泛結節的髓母細胞瘤的臨床試驗或文獻，證據等級為 L5。
- 雖然 SMO 抑制在 SHH 亞型髓母細胞瘤上有機轉上的合理性，但此特定亞型尚未被驗證。

**若要推進需要：**
- 補充 Vismodegib 的作用機轉資料（MOA）
- 檢索並評估 SHH 亞型髓母細胞瘤相關的臨床試驗與文獻，確認是否涵蓋廣泛結節型
- 取得完整的仿單警語與禁忌症資料，並評估對兒童族群（髓母細胞瘤好發族群）的安全性顧慮
- 規劃前臨床或早期探索性研究，驗證此亞型對 SMO 抑制的反應

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 快速總覽「許可證數：2 張」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

