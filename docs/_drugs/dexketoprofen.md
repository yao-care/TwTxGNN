---
layout: default
title: Dexketoprofen
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
monitor_inn: "dexketoprofen"
predicted_indications: ["tendinitis", "fibromyalgia", "myositis fibrosa", "idiopathic granulomatous myositis", "rheumatoid arthritis", "migraine disorder", "headache disorder", "migraine with brainstem aura", "exostosis", "congenital hypotrichosis milia"]
last_modified_at: 2026-10-29
description: "Dexketoprofen：預測新適應症為肌腱炎 (tendinitis)（證據等級 L5）。原適應症：治療輕度至中等強度疼痛症狀，如肌肉骨骼疼痛、經痛、牙痛"
---

# Dexketoprofen
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

## Dexketoprofen：COX 抑制型非類固醇消炎止痛藥 → 肌腱炎 (tendinitis)
{: .text-alpha }

## 一句話總結

Dexketoprofen 是一種非類固醇消炎止痛藥（NSAID），透過抑制 COX-1/COX-2 來減少前列腺素介導的發炎與疼痛。
TxGNN 模型預測它可能對**肌腱炎 (tendinitis)** 有效，但目前沒有針對肌腱炎的臨床試驗，僅有 **1 篇**間接相關的文獻（非創傷性肌肉骨骼疼痛的急診 RCT）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 治療輕度至中等強度疼痛症狀，如肌肉骨骼疼痛、經痛、牙痛。; 須使用dexketoprofen及tramadol合併療法之成人中度至重度急性疼痛短期治療 |
| 預測新適應症 | 肌腱炎 (tendinitis) |
| TxGNN 預測分數 | 0.9990 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效單方 1／有效複方 1／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉登錄資料。依一般藥理知識，dexketoprofen 屬於 COX-1/COX-2 抑制劑，可降低前列腺素合成，進而減輕發炎與疼痛。肌腱炎的症狀以局部發炎與疼痛為主，因此機轉上有其合理性。

不過，目前唯一的相關文獻是一項在急診比較靜脈注射 dexketoprofen 與 paracetamol 治療非創傷性肌肉骨骼疼痛的隨機試驗。該研究只在背景說明中提到肌腱炎是肌肉骨骼疼痛的成因之一，並非直接以肌腱炎病人為對象。因此證據屬間接推論，依規則證據等級只能判為 L5。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30744914](https://pubmed.ncbi.nlm.nih.gov/30744914/) | 2019 | RCT | The American Journal of Emergency Medicine | 比較靜脈注射 dexketoprofen 與 paracetamol 於急診非創傷性肌肉骨骼疼痛的緩解效果；研究對象並非特定肌腱炎病人 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Dexketoprofen 的不重複許可證共 **2 張**：有效單方 1 張、有效複方 1 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第026487號 | 克痛停錠25毫克 | 膜衣錠 | 裕利股份有限公司 | 2030/03/26 | 治療輕度至中等強度疼痛症狀，如肌肉骨骼疼痛、經痛、牙痛。 |

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（1 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛部藥輸字第027628號 | 舒宜達膜衣錠75毫克/25毫克 | Dexketoprofen trometamol、TRAMADOL HCL | 膜衣錠 | 須使用dexketoprofen及tramadol合併療法之成人中度至重度急性疼痛短期治療 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何直接研究肌腱炎的臨床試驗或文獻，支持僅來自模型預測與間接的肌肉骨骼疼痛研究，證據等級為 L5。

**若要推進需要：**
- 針對肌腱炎族群的臨床試驗或回溯性研究，比較 dexketoprofen 與其他 NSAID 或安慰劑。
- 補充詳細的作用機轉資料。
- 確認劑量、療程與腸胃道、心血管、腎臟風險的監測計畫。
- 取得完整的仿單安全性資訊（警語、禁忌與藥物交互作用）。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

