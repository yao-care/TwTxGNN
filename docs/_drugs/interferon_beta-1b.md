---
layout: default
title: Interferon Beta-1B
parent: 僅模型預測 (L5)
nav_order: 148
evidence_level: L5
indication_count: 2
---

# Interferon Beta-1B
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Interferon beta-1b：從多發性硬化症到毛細胞白血病

## 一句話總結

Interferon beta-1b（台灣商品名：貝他費隆）原本用於治療復發型與續發型多發性硬化症。
TxGNN 模型預測它可能對**毛細胞白血病 (Hairy Cell Leukemia)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 降低反覆發作型多發性硬化症的發作頻率及嚴重度；降低續發型多發性硬化症復發的頻率及嚴重度；延緩單一臨床症狀（疑似多發性硬化症）病患惡化成多發性硬化症 |
| 預測新適應症 | 毛細胞白血病 (Hairy Cell Leukemia) |
| TxGNN 預測分數 | 99.16% |
| 證據等級 | L5 |
| 台灣上市 | 曾上市，唯一許可證已於 2026-06-08 註銷 |
| 許可證數 | 1 張（有效單方 0／有效複方 0／已註銷 1） |
| 建議決策 | Hold |

<!-- review:begin interferon-beta-1b-license-cancelled-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「台灣上市／✓ 已上市」。本頁列的唯一許可證衛署菌疫輸字第000601號「貝他費隆注射劑」已於 2026-06-08 註銷，TFDA 資料集中沒有其他有效的 interferon beta-1b 許可證。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end interferon-beta-1b-license-cancelled-2026-10-03 -->

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Interferon beta-1b 是第一型干擾素，具有免疫調節作用，這也是它用於多發性硬化症的基礎。

Interferon beta 與 interferon alpha 透過同一個第一型干擾素受體（IFNAR）傳遞訊號。Interferon alpha 在毛細胞白血病中已有抗增殖與免疫調節作用的既有知識。因此從受體與訊號路徑來看，這個預測在生物學上有合理性。

不過這只是類別層級的推論。本報告所整理的資料中，沒有 interferon beta-1b 用於此疾病的臨床試驗或文獻，也缺乏藥物自身的作用機轉資料。原適應症（神經免疫疾病）與預測適應症（血液惡性腫瘤）的關聯，目前只能靠受體相同來推論。

另外，模型的第二名預測是**中樞神經系統自體免疫疾病**。這與現有的多發性硬化症適應症基本重疊，屬於已核准用途，不算真正的藥物再利用。該方向有 6 個臨床試驗（含 1 個已完成的 Phase 3 延伸試驗 NCT00185211，納入 468 人）和多篇文獻，但不屬於本報告評估的新適應症。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Interferon Beta-1B 的不重複許可證共 **1 張**：有效單方 0 張、有效複方 0 張、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署菌疫輸字第000601號</td><td>貝他費隆　注射劑</td><td>INTERFERON BETA-1B</td><td>2026/06/08</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：已查詢到 284 筆交互作用。其中 **Bupropion** 為 **Major（重大）**等級，應優先留意。
  - 其餘列出的多為 Moderate（中度），例如 Clarithromycin、Levofloxacin、Minocycline、Naltrexone、Pioglitazone、Rosiglitazone、Rosuvastatin、Simvastatin 等。
  - 若用於血液腫瘤族群，常見的併用藥物需另行評估。

其他安全性資訊（警語、禁忌症）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 毛細胞白血病的預測分數雖高（99.16%），但沒有臨床試驗或文獻支持，證據等級僅 L5。
- 作用機轉資料缺失，僅能靠與 interferon alpha 共用受體的類別推論，不足以直接推進。

**若要推進需要：**
- 補齊 interferon beta-1b 的作用機轉資料，並做機轉層面的比較分析（與 interferon alpha 在毛細胞白血病的作用路徑）。
- 系統性檢索 interferon beta 用於毛細胞白血病的前臨床與臨床資料，確認是否有可支持的證據。
- 與現行毛細胞白血病標準治療做療效與安全性比較，評估是否有臨床價值。
- 若要進一步考慮，需設計前臨床試驗或探索性臨床試驗，並確認劑型與給藥途徑（目前台灣僅有凍晶注射劑）是否適用。

<!-- review:begin interferon-beta-1b-license-cancelled-next-step-2026-10-16 -->

> **查核加註（2026-10-16）**：TFDA 許可證資料中，interferon beta-1b 唯一的許可證（衛署菌疫輸字第000601號「貝他費隆注射劑」）已於 2026-06-08 註銷，台灣目前沒有有效的 interferon beta-1b 製劑；現行有效的是 interferon beta-1a（立比扶、保優利）。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end interferon-beta-1b-license-cancelled-next-step-2026-10-16 -->

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「台灣上市：已上市」 | 更正（2026-10-15 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「Beta 干擾素曾用於 HCL 治療」 | 報告重生後已無此錯誤（2026-10-15：新報告改以 interferon alpha 與同一受體的類別推論說明，未再寫 beta 干擾素曾用於毛細胞白血病；原為加註） | [Drugs@FDA：INTRON A（interferon alfa-2b）仿單，Indications and Usage](https://www.accessdata.fda.gov/drugsatfda_docs/label/2018/103132s5199lbl.pdf)；[DailyMed：BETASERON（interferon beta-1b）仿單（Bayer），1 Indications and Usage](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=66311f74-0472-4fa3-848a-06002ca0def5) |
| 2026-10-16 | 下一步稱目前台灣僅有凍晶注射劑 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

