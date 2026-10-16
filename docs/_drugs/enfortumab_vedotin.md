---
layout: default
title: Enfortumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 99
evidence_level: L5
indication_count: 10
---

# Enfortumab Vedotin
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

# Enfortumab vedotin：從泌尿道上皮癌到痲瘋病（Leprosy）

## 一句話總結

Enfortumab vedotin 是一種靶向 Nectin-4 的抗體藥物複合體（ADC），原本用於局部晚期或轉移性泌尿道上皮癌，並可與 pembrolizumab 併用於不適合含 cisplatin 化療之肌肉侵犯性膀胱癌的前導性及術後輔助治療。
TxGNN 模型預測它可能對**痲瘋病 (Leprosy)** 有效，但目前**沒有任何臨床試驗與文獻**支持這個方向，僅有模型預測。

<!-- review:begin enfortumab-vedotin-original-indication-summary-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「原本用於局部晚期或轉移性泌尿道上皮癌。」。TFDA 許可證（衛部菌疫輸字第001212號、第001213號）第三項適應症為與 pembrolizumab 併用，治療不適合接受含 cisplatin 化療的肌肉侵犯性膀胱癌（MIBC），作為根治性膀胱切除術的前導性與術後輔助治療。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end enfortumab-vedotin-original-indication-summary-2026-10-16 -->

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 單獨使用治療局部晚期或轉移性泌尿道上皮癌（mUC）成人病人：（1）先前接受過 PD-1/PD-L1 抑制劑和含鉑化學治療；或（2）不適合接受含 cisplatin 化學治療，且先前接受過一線以上治療；另可併用 pembrolizumab 治療局部晚期或轉移性泌尿道上皮癌；另與 pembrolizumab 併用於不適合含 cisplatin 化療之肌肉侵犯性膀胱癌（MIBC）的前導性及術後輔助治療（衛部菌疫輸字第001212號） |
| 預測新適應症 | 痲瘋病 (Leprosy) |
| TxGNN 預測分數 | 99.53% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 2 張（有效單方 2／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

<!-- review:begin enfortumab-vedotin-original-indication-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「原適應症／單獨使用治療局部晚期或轉移性泌尿道上皮癌（mUC）成人病人：（1）先前接受過 PD-1/PD-L1 抑制劑和含鉑化學治療；或（2）不適合接受含 cisplatin 化學治療，且先前接受過一線以上治療；另可併用 pembrolizumab 治療局部晚期或轉移性泌尿道上皮癌」。台灣許可證另核准與 pembrolizumab 併用於不適合含 cisplatin 化療之肌肉侵犯性膀胱癌（MIBC）的前導性及術後輔助治療，頁面原只列 mUC。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end enfortumab-vedotin-original-indication-2026-10-03 -->

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Enfortumab vedotin 是一種靶向 Nectin-4 的抗體藥物複合體，透過抗體將細胞毒性載荷 MMAE（微管抑制劑）送入表現 Nectin-4 的腫瘤細胞。

痲瘋病是由麻風分枝桿菌感染所致，與 Nectin-4 陽性的泌尿道上皮癌在疾病本質上差異很大。目前沒有已知的機轉可將 Nectin-4 導向的細胞毒性藥物與麻風分枝桿菌感染連結起來，這個預測完全建立在 TxGNN 模型分數上。

因此，本預測的合理性很低，較可能是知識圖譜的關聯性推論，而非有生物學依據的訊號。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

目前無相關文獻

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Enfortumab Vedotin 的不重複許可證共 **2 張**：有效單方 2 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部菌疫輸字第001212號 | 備思復凍晶注射劑20毫克 | 凍晶注射劑 | 台灣安斯泰來製藥股份有限公司 | 2027/12/28 | １、單獨使用適用於治療患有局部晚期或轉移性泌尿道上皮癌（mUC）的成人病人： (１)先前接受過PD-1（programmed death receptor-1）或PDL1（prog… |
| 衛部菌疫輸字第001213號 | 備思復凍晶注射劑30毫克 | 凍晶注射劑 | 台灣安斯泰來製藥股份有限公司 | 2027/12/28 | １、單獨使用適用於治療患有局部晚期或轉移性泌尿道上皮癌（mUC）的成人病人： (１)先前接受過PD-1（programmed death receptor-1）或PDL1（prog… |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 抗體藥物複合體（ADC），載荷 MMAE 為微管抑制劑，屬細胞毒性藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項（一般包含血液學與肝腎功能監測） |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

---

## 安全性考量

- **藥物交互作用**：資料庫共查得 147 筆交互作用紀錄，其中標示為 Major 的有 Clarithromycin；其餘多為 Moderate，主要涉及降血糖藥物，例如 Acarbose、Metformin、Pioglitazone、Glimepiride、Glipizide、Glyburide、Dapagliflozin、Empagliflozin、Canagliflozin、Linagliptin、Saxagliptin、Exenatide、Dulaglutide，另有 Aprepitant。

其他警語與禁忌症請參考原廠仿單。

此外，若用於痲瘋病或其他感染症族群，細胞毒性的 MMAE 暴露會增加安全性疑慮，需特別審慎。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（99.53%），但沒有任何臨床試驗或文獻支持，證據等級僅為 L5。
- 機轉上，Nectin-4 導向的細胞毒性 ADC 與麻風分枝桿菌感染之間沒有已知關聯，且潛在毒性不利於感染症病人。

**若要推進需要：**
- 完整的作用機轉資料（MOA），並釐清 Nectin-4 與痲瘋病病理之間是否有任何關聯
- 前臨床研究（如痲瘋病相關細胞或組織模型）提供生物學依據
- 重新審視預測排序：同一份預測清單中，HER2 陽性乳癌因有 Nectin-4 表現的生物學基礎與相關 Phase 2 多癌別試驗（EV-202），證據等級為 L4，較值得優先評估

<!-- review:begin enfortumab-vedotin-original-indication-ev202-2026-10-16 -->

> **查核加註（2026-10-16）**：EV-202（NCT04225117）的乳癌分組是 HR 陽性／HER2 陰性乳癌與三陰性乳癌，沒有 HER2 陽性乳癌分組。原文保留。依據：[ClinicalTrials.gov：NCT04225117（EV-202）](https://clinicaltrials.gov/study/NCT04225117)。

<!-- review:end enfortumab-vedotin-original-indication-ev202-2026-10-16 -->

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 原適應症漏列肌肉侵犯性膀胱癌（MIBC） | 更正（2026-10-15 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 一句話總結漏列肌肉侵犯性膀胱癌 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 稱 EV-202 有 HER2 陽性乳癌依據 | 加註 | [ClinicalTrials.gov：NCT04225117（EV-202）](https://clinicaltrials.gov/study/NCT04225117) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

