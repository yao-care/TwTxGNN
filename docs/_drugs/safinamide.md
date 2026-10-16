---
layout: default
title: Safinamide
parent: 僅模型預測 (L5)
nav_order: 252
evidence_level: L5
indication_count: 3
monitor_inn: "safinamide"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration"]
last_modified_at: 2026-10-16
description: "Safinamide：預測新適應症為Rasmussen 亞急性腦炎 (Rasmussen subacute encephalitis)（證據等級 L5）。原適應症：用於改善以含有 levodopa 製劑治療的帕金森氏症之藥效漸退現象"
---

# Safinamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Safinamide：從帕金森氏症藥效漸退現象到 Rasmussen 亞急性腦炎

## 一句話總結

Safinamide 是一種用於帕金森氏症的藥物，原本用來改善以 levodopa 製劑治療時出現的藥效漸退現象（wearing-off phenomenon）。
TxGNN 模型預測它可能對 **Rasmussen 亞急性腦炎 (Rasmussen subacute encephalitis)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 用於改善以含有 levodopa 製劑治療的帕金森氏症之藥效漸退現象 |
| 預測新適應症 | Rasmussen 亞急性腦炎 (Rasmussen subacute encephalitis) |
| TxGNN 預測分數 | 99.63% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 1 張（有效單方 1／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位尚未收錄）。根據本報告所整理的資料，safinamide 被認為是可逆性 MAO-B 抑制劑，同時具有鈉離子通道阻斷及抑制麩胺酸釋放的作用。理論上，這些特性可能減緩神經興奮性毒性與神經元過度興奮。

Rasmussen 腦炎主要由 T 細胞介導的自體免疫發炎所驅動，會造成單側大腦半球進行性萎縮與難治型癲癇。Safinamide 的機轉並未針對這個免疫病理過程，因此兩者的關聯**純屬推測**，沒有臨床或前臨床證據支持。

其他同時被預測的疾病包括脊髓炎（myelitis，分數 99.46%）與 PLA2G6 相關神經退化症（PLA2G6-associated neurodegeneration，分數 99.22%）。後者與帕金森症狀有部分重疊，機轉上相對較合理，但同樣沒有直接證據，且藥物預期無法改變疾病本身的進程。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Safinamide 的不重複許可證共 **1 張**：有效單方 1 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第028061號 | 愛可穩錠50毫克 | 膜衣錠 | 衛采製藥股份有限公司 | 2031/05/03 | 用於改善以含有levodopa製劑治療的帕金森氏症之藥效漸退現象(wearing-off phenomenon)。 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：資料庫共查得 110 筆交互作用，其中較需注意的是：
  - **重大 (Major)**：Bupropion
  - **中度 (Moderate)**：Isometheptene、Diethylpropion、Phentermine、Metoclopramide、Rosuvastatin，以及多種降血糖藥物（如 Glimepiride、Chlorpropamide、Nateglinide、Repaglinide、Empagliflozin 與各類胰島素）

其餘警語與禁忌症資料請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型，沒有任何臨床試驗或文獻佐證（證據等級 L5）。
- 機轉上與疾病的免疫病理缺乏關聯，屬於推測性連結。

**若要推進需要：**
- 補齊 safinamide 的作用機轉資料。
- 進行文獻與前臨床研究回顧，確認是否有動物模型或病例報告支持。
- 評估 PLA2G6 相關神經退化症等機轉上較合理的替代候選適應症。
- 補充仿單中的警語與禁忌症，並完整審視藥物交互作用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

