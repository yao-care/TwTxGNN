---
layout: default
title: Lorcaserin
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 4
monitor_inn: "lorcaserin"
predicted_indications: ["hypervitaminosis", "proximal 16p11.2 microdeletion syndrome", "obsolete hypertelorism (disease)", "frontorhiny"]
last_modified_at: 2026-10-29
description: "Lorcaserin：預測新適應症為高維生素症 (hypervitaminosis)（證據等級 L5）."
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

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Lorcaserin：5-HT2C 受體致效劑 → 高維生素症 (hypervitaminosis)
{: .text-alpha }

## 一句話總結

Lorcaserin 是一種選擇性血清素 5-HT2C 受體致效劑，屬於抗肥胖類藥物。
TxGNN 模型預測它可能對**高維生素症 (hypervitaminosis)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抗肥胖劑; BELVIQ是血清素5-HT2c受體致效劑，對成人身體質量指數 (BMI) 過高者於飲食和運動控制後之長期體重輔助管理。
 適用之身體質量指數為: (1) BMI ≧ 30 kg/m2 或 (2) BMI ≧ 27 kg/m2 且有一項與體重相關之疾病 (例如: 高血壓、血脂異常或第二型糖尿病)。 
 說明:●BELVIQ 併用其他減重藥物(處方藥、非處方藥及中草藥)之安全性和有效性尚未確立。 
 ●BELVIQ 對於心血管系統之影響(致病率及致死率)尚未確立。 |

| 預測新適應症 | 高維生素症 (hypervitaminosis) |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | L5 |
| 台灣上市 | 未上市（已註銷許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效單方 0／有效複方 0／已過期 1／已註銷 1） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Lorcaserin 為選擇性 5-HT2C 受體致效劑，透過作用於中樞食慾調控路徑來抑制食慾。目前缺乏詳細的作用機轉資料（資料庫中未收錄完整 MOA）。

就現有資訊而言，5-HT2C 致效作用與維生素過量狀態之間，並未找到合理的機轉關聯。此預測僅來自 TxGNN 模型的計算結果，缺乏機轉或臨床層面的支持，應視為低可信度的假說，不宜直接作為研發依據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Lorcaserin 的不重複許可證共 **2 張**：有效單方 0 張、有效複方 0 張、已過期 1 張（未註銷但有效日期早於資料集日期）、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-09-29）</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛部藥輸字第027955號</td><td>半水氯卡色林鹽酸鹽</td><td>Lorcaserin hydrochloride hemihydrate</td><td>2025/09/02</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛部藥輸字第027218號</td><td>沛麗婷膜衣錠10毫克</td><td>Lorcaserin HCl hemihydrate</td><td>2020/07/16</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：本次彙整資料共記錄 190 筆交互作用，其中較重要的 Major 等級包括：
  - Fentanyl
  - Dextromethorphan
  - Tramadol
  - Alfentanil
  - Almotriptan
  - Sumatriptan
  - Amitriptyline
  - Bupropion

  這些多為具血清素或中樞神經作用的藥物，併用時需留意血清素症候群等風險。Moderate 等級包括 Acarbose、Metformin、Pioglitazone、Codeine、Amphetamine、Aripiprazole 等。

其他警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測缺乏任何臨床試驗、文獻或合理的機轉支持，證據等級為 L5。
- 此外，台灣目前沒有有效上市的許可證，推進的實務基礎也不足。

**若要推進需要：**
- 建立 5-HT2C 致效作用與維生素過量狀態之間的機轉假說，並進行前臨床驗證
- 補充完整的作用機轉資料
- 確認該預測疾病的定義與臨床意義，並評估是否有實際的未滿足需求
- 評估血清素相關藥物交互作用的安全性監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

