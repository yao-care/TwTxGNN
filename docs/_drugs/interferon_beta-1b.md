---
layout: default
title: Interferon Beta-1B
parent: 僅模型預測 (L5)
nav_order: 148
evidence_level: L5
indication_count: 2
monitor_inn: "Interferon beta-1b"
predicted_indications: ["hairy cell leukemia", "autoimmune disease of central nervous system"]
last_modified_at: 2026-10-29
description: "Interferon Beta-1B：預測新適應症為毛細胞白血病 (hairy cell leukemia)（證據等級 L5）。原適應症：降低反覆發作型多發性硬化症的發作頻率及嚴重度。降低續發型多發性硬化症(secondary progressive multiple scl…"
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

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Interferon beta-1b：免疫調節型 I 型干擾素 → 毛細胞白血病 (hairy cell leukemia)
{: .text-alpha }

## 一句話總結

Interferon beta-1b 是一種 I 型干擾素，具免疫調節作用。
TxGNN 模型預測它可能對**毛細胞白血病 (hairy cell leukemia)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 降低反覆發作型多發性硬化症的發作頻率及嚴重度。降低續發型多發性硬化症(secondary progressive multiple sclerosis)復發的頻率及嚴重度。發生單一臨床症狀(Clinically Isolated Syndrome)疑似多發性硬化症的病患，可延緩其惡化成多發性硬化症。 |
| 預測新適應症 | 毛細胞白血病 (hairy cell leukemia) |
| TxGNN 預測分數 | 0.9916 |
| 證據等級 | L5 |
| 台灣上市 | 未上市（已註銷許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效單方 0／有效複方 0／已註銷 1） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供 MOA）。根據已知的藥物類別，Interferon beta-1b 與干擾素 alpha 同樣透過 I 型干擾素受體（IFNAR）傳遞訊號。干擾素 alpha 在毛細胞白血病中具有已確立的抗增殖與免疫調節作用，因此從受體路徑來看，此預測在生物學上有其合理性。

不過，這個推論建立在藥物類別的一般知識上，並非來自本報告所整理的直接研究。目前沒有任何針對 Interferon beta-1b 用於毛細胞白血病的臨床試驗或文獻，β 型與 α 型干擾素在此疾病中的療效是否相當，仍需驗證。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Interferon Beta-1B 的不重複許可證共 **1 張**：有效單方 0 張、有效複方 0 張、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署菌疫輸字第000601號</td><td>貝他費隆　注射劑</td><td>INTERFERON BETA-1B</td><td>2026/06/08</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：資料共收錄 284 筆交互作用，其中較重要的包括：
  - 重度：Bupropion
  - 中度：Acarbose、Pioglitazone、Rosiglitazone、Clarithromycin、Levofloxacin、Minocycline、Naltrexone、Rosuvastatin、Simvastatin 等

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅有模型分數（0.9916）與受體層級的機轉推論支持，沒有針對此疾病的臨床試驗或文獻，證據等級為 L5。
- 在毛細胞白血病已有其他成熟治療選擇的情況下，目前不足以支持推進。

**若要推進需要：**
- 系統性檢索 Interferon beta-1b 用於毛細胞白血病的前臨床與臨床研究
- 補齊詳細的作用機轉資料（MOA），並比較 β 型與 α 型干擾素在此疾病中的作用差異
- 若有初步證據，再設計小規模探索性研究並擬定安全性監測計畫

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「台灣上市：已上市」 | 報告重生後已無此錯誤（2026-10-28：報告重產與事實層改寫後，本紀錄指出的錯誤原文已不在正文（僅見於本頁查核紀錄表或程式產生的許可證表）（2026-10-28 用戶核准的處理方案）；原為更正（2026-10-15 修訂，前版保留於紀錄）） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「Beta 干擾素曾用於 HCL 治療」 | 報告重生後已無此錯誤（2026-10-15：新報告改以 interferon alpha 與同一受體的類別推論說明，未再寫 beta 干擾素曾用於毛細胞白血病；原為加註） | [Drugs@FDA：INTRON A（interferon alfa-2b）仿單，Indications and Usage](https://www.accessdata.fda.gov/drugsatfda_docs/label/2018/103132s5199lbl.pdf)；[DailyMed：BETASERON（interferon beta-1b）仿單（Bayer），1 Indications and Usage](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=66311f74-0472-4fa3-848a-06002ca0def5) |
| 2026-10-16 | 下一步稱目前台灣僅有凍晶注射劑 | 報告重生後已無此錯誤（2026-10-28：報告重產與事實層改寫後，本紀錄指出的錯誤原文已不在正文（僅見於本頁查核紀錄表或程式產生的許可證表）（2026-10-28 用戶核准的處理方案）；原為加註（2026-10-16 修訂，前版保留於紀錄）） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

