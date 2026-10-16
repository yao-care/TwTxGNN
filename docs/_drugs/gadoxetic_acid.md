---
layout: default
title: Gadoxetic Acid
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
monitor_inn: "gadoxetic acid"
predicted_indications: ["hyperthyroidism", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "hyperthyroxinemia", "Prinzmetal angina", "infectious bovine rhinotracheitis", "malignant catarrh", "conjunctivitis", "cytomegalovirus infection", "conjunctivitis (disease)", "thrombotic disease"]
last_modified_at: 2026-10-16
description: "Gadoxetic Acid：預測新適應症為甲狀腺機能亢進 (Hyperthyroidism)（證據等級 L5）。原適應症：適用於 T1 加權掃描核磁造影時，偵測肝臟局部病灶及提供病灶特性資訊"
---

# Gadoxetic Acid
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

# Gadoxetic acid：從肝臟局部病灶造影到甲狀腺機能亢進（預測）

## 一句話總結

Gadoxetic acid（釓塞酸）是肝臟特異性的 MRI 對比劑，原本用於 T1 加權核磁造影，偵測肝臟局部病灶並提供病灶特性資訊。
TxGNN 模型預測它可能對**甲狀腺機能亢進 (Hyperthyroidism)** 有效，但目前**沒有任何臨床試驗與文獻**支持這個方向，僅有模型預測，且缺乏機轉依據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 適用於 T1 加權掃描核磁造影時，偵測肝臟局部病灶及提供病灶特性資訊 |
| 預測新適應症 | 甲狀腺機能亢進 (Hyperthyroidism) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 1 張（有效單方 1／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 gadoxetic acid 是肝細胞特異性 MRI 對比劑，主要經 OATP1B1/1B3 轉運體被肝細胞攝取，用於肝臟病灶的診斷造影，並沒有已知的抗甲狀腺活性。

原適應症（肝臟病灶影像診斷）與預測的新適應症（甲狀腺機能亢進）在疾病領域與藥理作用上並無明顯關聯。此外，這是一個診斷用的釓類對比劑，以治療目的使用並不合理。

因此，這個高分預測較可能來自知識圖譜的關聯結構，而非真實的藥理關係。同一份預測清單中的其他項目（如甲狀腺素抗性症候群、高甲狀腺素血症、牛傳染性鼻氣管炎、結膜炎、巨細胞病毒感染等）同樣缺乏機轉與臨床支持，也顯示這批預測的可信度有限。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對首要預測（甲狀腺機能亢進）目前無相關文獻。

補充說明：在排名第 10 的預測「血栓性疾病」下，有 2 篇世代研究，但內容皆是將 gadoxetic acid 當作**診斷影像工具**，並非治療證據，因此不支持藥物再利用：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37246973](https://pubmed.ncbi.nlm.nih.gov/37246973/) | 2023 | Cohort | Abdominal Radiology | 評估 LI-RADS v2018 在 gadoxetic acid MRI 上區分腫瘤性靜脈栓塞與良性血栓的觀察者間一致性與準確度 |
| [39809606](https://pubmed.ncbi.nlm.nih.gov/39809606/) | 2025 | Cohort | Academic Radiology | 以 gadoxetic acid MRI 與肝功能影像評分建立並驗證經動脈化療栓塞後肝衰竭的預測模型 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Gadoxetic Acid 的不重複許可證共 **1 張**：有效單方 1 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第024676號 | 卜邁維斯 | 注射劑 | 台灣拜耳股份有限公司 | 2027/08/06 | 適用於T1 加權掃描核磁造影時，偵測肝臟局部病灶及提供病灶特性資訊。. |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：資料庫共收錄 33 筆交互作用（本次列出 20 筆，皆為中度）。主要涉及：
  - β 受體阻斷劑：acebutolol、atenolol、betaxolol、bisoprolol、carvedilol、nadolol、labetalol 及多種眼用製劑（timolol、carteolol、levobunolol、metipranolol 等）
  - 鈣離子通道阻斷劑：nifedipine、amlodipine、levamlodipine、diltiazem、verapamil、clevidipine、isradipine
  - 其他：rifabutin

其他警語與禁忌症資料不足，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有臨床試驗、文獻或機轉支持，證據等級為 L5。
- Gadoxetic acid 是診斷用對比劑，沒有抗甲狀腺作用，以治療目的使用並不合理。

**若要推進需要：**
- 取得明確的作用機轉資料，並說明與甲狀腺病理的生物學關聯
- 進行前臨床研究，驗證是否有任何抗甲狀腺相關活性
- 評估釓類對比劑作為治療用途的安全性與可行性
- 目前不建議投入進一步開發資源，維持現有的診斷用途即可
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

