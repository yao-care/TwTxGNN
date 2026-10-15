---
layout: default
title: Lorcaserin
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 4
---

# Lorcaserin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Lorcaserin：從體重管理到維生素過多症

## 一句話總結

Lorcaserin 是血清素 5-HT2C 受體致效劑，原本用於成人長期體重輔助管理（抗肥胖劑）。
TxGNN 模型預測它可能對**維生素過多症 (Hypervitaminosis)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個預測，僅為模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抗肥胖劑 |
| 預測新適應症 | 維生素過多症 (Hypervitaminosis) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 2 張（有效單方 1／有效複方 0／已註銷 1） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，lorcaserin 是選擇性 5-HT2C 受體致效劑，透過作用於中樞食慾調控路徑來輔助體重管理。

就機轉而言，5-HT2C 受體的作用與維生素過量狀態之間，目前沒有找到合理的生物學關聯。這個預測只來自 TxGNN 知識圖譜的推論，分數雖高（99.97%），但缺乏任何機轉或臨床佐證，應視為低可信度的假說。

資料中另有三個預測，其中「近端 16p11.2 微缺失症候群」在機轉上較合理：該症候群與食慾過盛、肥胖相關，5-HT2C 介導的食慾抑制具生物學上的可能性，但同樣沒有臨床證據。另外兩個（過時的眼距過寬、frontorhiny）屬顱顏結構異常，與 5-HT2C 訊號無已知關聯，且前者的疾病名稱已過時，預測品質偏低。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Lorcaserin 的不重複許可證共 **2 張**：有效單方 1 張、有效複方 0 張、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第027955號 | 半水氯卡色林鹽酸鹽 | （粉） | 丞泰企業有限公司 | 2025/09/02 | 抗肥胖劑 |

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛部藥輸字第027218號</td><td>沛麗婷膜衣錠10毫克</td><td>Lorcaserin HCl hemihydrate</td><td>2020/07/16</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：資料庫共收錄 190 筆交互作用，以下為部分重要項目：
  - **嚴重（Major）**：Fentanyl、Dextromethorphan、Tramadol、Alfentanil、Almotriptan、Sumatriptan、Amitriptyline、Bupropion
  - **中度（Moderate）**：Acarbose、Chlorpheniramine、Codeine、Albiglutide、Alogliptin、Metformin、Pioglitazone、Alprostadil、Amphetamine、Aripiprazole、Asenapine、Atomoxetine
  - 嚴重交互作用多涉及血清素或中樞神經系統藥物（如鴉片類、triptan 類、抗憂鬱劑），合併使用時需特別留意血清素症候群風險。降血糖藥物則需留意低血糖。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型，沒有臨床試驗與文獻，證據等級為 L5，且機轉上找不到合理關聯。
- 該藥的血清素類交互作用多，安全性管理負擔不低，在缺乏效益證據下不宜推進。

**若要推進需要：**
- 補充詳細的作用機轉資料（MOA），評估與維生素代謝或毒性的關聯
- 進行系統性文獻檢索與前臨床研究，確認有無生物學依據
- 建議優先評估排名第 2 的「近端 16p11.2 微缺失症候群」，其機轉較合理，可先做文獻回顧與前臨床驗證
- 確認藥品在台灣的許可證與供應現況（其中一張許可證已註銷）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

