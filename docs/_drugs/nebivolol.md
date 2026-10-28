---
layout: default
title: Nebivolol
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 4
monitor_inn: "Nebivolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
last_modified_at: 2026-10-29
description: "Nebivolol：預測新適應症為惡性高血壓腎病 (malignant hypertensive renal disease)（證據等級 L5）。原適應症：治療原發性高血壓"
---

# Nebivolol
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

## Nebivolol：β1 選擇性受體阻斷劑 → 惡性高血壓腎病 (malignant hypertensive renal disease)
{: .text-alpha }

## 一句話總結

Nebivolol 是一種具一氧化氮（NO）釋放特性的 β1 選擇性受體阻斷劑。
TxGNN 模型預測它可能對**惡性高血壓腎病 (malignant hypertensive renal disease)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 治療原發性高血壓。 |
| 預測新適應症 | 惡性高血壓腎病 (malignant hypertensive renal disease) |
| TxGNN 預測分數 | 0.9942 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效單方 5／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

<!-- review:begin nebivolol-moa-2026-10-03 -->

## Nebivolol 的作用機轉

<!-- moa-sourced: 2026-10-03 用戶拍板例外，只限附來源的作用機轉段 -->

以下只說明這個藥原本怎麼作用，每一點都摘自官方仿單的藥理段落並附連結；與本頁的老藥新用預測無關，也不構成用藥建議。

- Nebivolol 是 β 腎上腺素受體阻斷劑；在多數人（CYP2D6 廣泛代謝者）且劑量 10 mg 以下時，偏向選擇性阻斷 β1；在慢代謝者或較高劑量時，β1 與 β2 都會被抑制。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8b8ad213-1dc8-454e-a524-075685c0e1a8)）
- 在臨床劑量下，它沒有內在擬交感活性與膜穩定作用，也沒有 α1 受體阻斷作用。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8b8ad213-1dc8-454e-a524-075685c0e1a8)）
- 仿單寫明降血壓的機轉**尚未完全確立**，可能的因素包括：心跳減慢、心肌收縮力下降、腦部血管運動中樞送往周邊的交感神經張力減少、腎素活性受抑制，以及血管擴張使周邊阻力下降。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8b8ad213-1dc8-454e-a524-075685c0e1a8)）

**來源**：[DailyMed：BYSTOLIC（nebivolol）美國仿單（Allergan），§12 Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8b8ad213-1dc8-454e-a524-075685c0e1a8)，版本日期 2024-08-01；查閱日期 2026-10-03。

---

<!-- review:end nebivolol-moa-2026-10-03 -->

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Nebivolol 是 β1 選擇性受體阻斷劑，另具促進內皮型一氧化氮合成酶（eNOS）活化、釋放 NO 的血管擴張作用。

惡性高血壓腎病是嚴重高血壓造成腎臟血管損傷的結果。理論上，Nebivolol 的降血壓作用與內皮 NO 相關效應，可能有助於減輕腎血管傷害。

但這只是機轉上的推論。針對此疾病並沒有臨床試驗或文獻佐證，因此此預測目前僅屬模型層次的假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Nebivolol 的不重複許可證共 **5 張**：有效單方 5 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（5 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥製字第061020號 | 欣倍泰錠5毫克 | 錠劑 | 健喬信元醫藥生技股份有限公司 | 2031/11/08 | 治療原發性高血壓。 |
| 衛部藥製字第061041號 | 舒爾脈錠5毫克 | 錠劑 | 生達化學製藥股份有限公司二廠 | 2031/12/13 | 治療原發性高血壓。 |
| 衛部藥製字第062403號 | 耐洛心 錠5毫克 | 錠劑 | 永信藥品工業股份有限公司 | 2031/08/07 | 治療原發性高血壓。 |
| 衛部藥輸字第026700號 | 耐比洛錠5毫克 | 錠劑 | 新加坡商美納里尼醫藥有限公司台灣分公司 | 2031/01/22 | 治療原發性高血壓。 |
| 衛部藥輸字第028953號 | 氟色原烷洛鹽酸鹽 | （粉） | 盛佳國際股份有限公司 | 2030/05/13 | 治療原發性高血壓。 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：已查得 174 筆交互作用紀錄，其中多數為中度。例如：Epinephrine、Hydrocortisone、Bupropion、Morphine、Dexamethasone、Canagliflozin、Dapagliflozin、Chlorpropamide 等為中度；Acetylsalicylic acid、Magnesium oxide 為輕度。與降血糖藥併用時需留意低血糖症狀可能被掩蓋。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 針對惡性高血壓腎病，目前沒有任何臨床試驗或文獻，證據等級為 L5，僅有模型預測分數。
- 此疾病屬嚴重急症，現階段無依據支持以 Nebivolol 作為治療選項。

**若要推進需要：**
- 補充詳細的作用機轉資料（MOA）
- 進行針對惡性高血壓腎病的文獻回顧，並搜尋相關臨床試驗
- 先以腎損傷動物模型或回溯性觀察研究驗證腎保護效果
- 建立明確的安全性評估，包含腎功能不全與重度高血壓患者的用藥風險

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 新增「作用機轉」段（每點附仿單來源） | 新增附來源段落 | [DailyMed：BYSTOLIC 美國仿單 §12](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8b8ad213-1dc8-454e-a524-075685c0e1a8) |
| 2026-10-04 | 頁首證據等級 | 報告重生後已無此錯誤（2026-10-16：報告重生後頁首依新報告為 L5，此筆記的是舊版報告的重算；原為頁首等級依總覽表重算（原 L5→L3）） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

