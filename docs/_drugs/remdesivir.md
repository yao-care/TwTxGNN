---
layout: default
title: Remdesivir
parent: 僅模型預測 (L5)
nav_order: 242
evidence_level: L5
indication_count: 6
monitor_inn: "Remdesivir"
predicted_indications: ["multiple endocrine neoplasia", "HIV infectious disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "homozygous familial hypercholesterolemia"]
last_modified_at: 2026-10-16
description: "Remdesivir：預測新適應症為多發性內分泌腫瘤 (Multiple Endocrine Neoplasia)（證據等級 L5）。原適應症：適用於治療新型冠狀病毒疾病 (COVID-19)：發生肺炎並須給予氧氣治療的成人與 28 天大以上且體重至少 3 公斤之兒童"
---

# Remdesivir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Remdesivir：從重度 COVID-19 到多發性內分泌腫瘤

## 一句話總結

Remdesivir 是一種核苷酸類似物前驅藥，原本用於治療新型冠狀病毒感染症 (COVID-19)。
TxGNN 模型預測它可能對**多發性內分泌腫瘤 (Multiple Endocrine Neoplasia)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 適用於治療新型冠狀病毒疾病 (COVID-19)：發生肺炎並須給予氧氣治療的成人與 28 天大以上且體重至少 3 公斤之兒童；不須氧氣治療但惡化成重度 COVID-19 風險較高的成人與兒童 |
| 預測新適應症 | 多發性內分泌腫瘤 (Multiple Endocrine Neoplasia) |
| TxGNN 預測分數 | 99.50% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 2 張（有效單方 1／有效複方 0／已註銷 1） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知資訊，Remdesivir 是腺苷核苷酸類似物的前驅藥，作用於病毒的 RNA 依賴性 RNA 聚合酶，用於抑制 SARS-CoV-2 複製。

多發性內分泌腫瘤是由 MEN1、RET 等抑癌基因或致癌基因異常所驅動的遺傳性疾病。這條致病路徑與病毒聚合酶抑制之間，沒有已知的合理機轉連結。因此，這項預測較可能來自知識圖譜的網路相似性，而非生物學上的因果關係，應視為低可信度的假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Remdesivir 的不重複許可證共 **2 張**：有效單方 1 張、有效複方 0 張、已註銷 1 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第027899號 | 韋如意凍晶乾燥注射劑100毫克/瓶 | 凍晶乾燥注射劑 | 香港商吉立亞醫藥有限公司台灣分公司 | 2028/06/07 | 適用於治療下列病人的新型冠狀病毒疾病(COVID-19，嚴重特殊傳染性肺炎)：發生肺炎並須給予氧氣治療(開始本品治療時須使用低或高流量氧氣或其他非侵入性呼吸器)的成人與28 天大以… |

<details><summary><strong>已註銷</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛部藥輸字第027898號</td><td>韋如意注射用溶液劑100毫克/20毫升</td><td>Remdesivir</td><td>2021/06/02</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：已查詢到 182 筆交互作用紀錄，以下為部分中度等級項目：
  - Acarbose
  - Doxycycline
  - Pioglitazone
  - Amphotericin B
  - Bupropion
  - Clarithromycin
  - Levofloxacin
  - Vancomycin

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但沒有任何臨床試驗或文獻支持。
- 作用機轉（抑制病毒聚合酶）與多發性內分泌腫瘤的致病機轉（MEN1、RET 路徑）缺乏關聯，不建議投入資源推進。

**若要推進需要：**
- 補充 Remdesivir 的作用機轉資料，並提出具體的生物學假說。
- 進行前臨床研究（如細胞或動物模型），檢視其對相關腫瘤路徑的影響。
- 在取得前臨床證據之前，不建議啟動臨床試驗。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證字號寫成「衛部藥輸字第XXXXXX號」（且該證已註銷） | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

