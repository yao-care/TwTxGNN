---
layout: default
title: Benazepril
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-16
description: "Benazepril：預測新適應症為惡性腎血管性高血壓 (Malignant Renovascular Hypertension)（證據等級 L5）。原適應症：高血壓"
monitor_inn: "Benazepril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Benazepril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Benazepril：從高血壓到惡性腎血管性高血壓
{: .text-alpha }

## 一句話總結

Benazepril（貝那普利）是一種血管收縮素轉化酶（ACE）抑制劑，原本用於治療高血壓。
TxGNN 模型預測它可能對**惡性腎血管性高血壓 (Malignant Renovascular Hypertension)** 有效，
但目前**沒有臨床試驗**，也沒有直接相關的文獻支持，證據僅來自模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓 |
| 預測新適應症 | 惡性腎血管性高血壓 (Malignant Renovascular Hypertension) |
| TxGNN 預測分數 | 99.65% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 8 張（有效單方 1／有效複方 4／已註銷 3） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Benazepril 屬於 ACE 抑制劑類藥物，在高血壓的療效已被證實。ACE 抑制劑可降低血管收縮素 II 與醛固酮，理論上與腎素依賴性的腎血管性高血壓相符。

原適應症（高血壓）與預測的新適應症（惡性腎血管性高血壓）同屬高血壓範疇，差別在於後者由腎動脈狹窄等腎血管病變引起，且病程進展快速、較嚴重。腎臟灌流下降會啟動腎素—血管收縮素系統，因此阻斷此路徑在機轉上有合理性。

不過，這項推論僅建立在藥理學上的合理推測與模型預測上，目前沒有試驗或文獻直接驗證。另外，ACE 抑制劑用於腎血管性高血壓時（特別是雙側腎動脈狹窄）可能影響腎功能，需特別謹慎。

**其他預測適應症（皆為 L5、建議 Hold）：**

| 排名 | 預測適應症 | 預測分數 | 備註 |
|------|-----------|---------|------|
| 2 | 惡性高血壓性腎病 (Malignant Hypertensive Renal Disease) | 99.65% | 機轉上合理（降低腎絲球內壓），但無試驗與文獻 |
| 3 | 機轉不明的多因素肺高壓 | 99.60% | 僅間接關聯，未經證實 |
| 4 | 肺疾病和/或缺氧所致肺高壓 | 99.60% | 檢索到的 3 篇文獻為中藥複方的動物實驗，並未測試 Benazepril 或肺高壓，無直接證據 |
| 5 | Braddock 症候群 | 99.44% | 無法建立機轉關聯，信心低 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無直接相關文獻。

（備註：針對排名第 4 的預測適應症，雖檢索到 3 篇文獻，但皆為中藥複方在腎纖維化或心肌纖維化的動物實驗，並未研究 Benazepril 或肺高壓，因此不列為本預測的證據。）

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Benazepril 的不重複許可證共 **8 張**：有效單方 1 張、有效複方 4 張、已註銷 3 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第025881號 | 鹽酸貝那普利 | （粉） | 鴻傑藥品有限公司 | 2027/12/28 | 血管收縮素轉化每抑制劑 |

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（4 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第046742號 | 諾壓錠 | AMLODIPINE BESYLATE、BENAZEPRIL HYDROCHLORIDE | 錠劑 | 治療高血壓，此複方藥品不適合用於起始治療。 |
| 衛署藥製字第056647號 | 紓心膠囊 | AMLODIPINE BESYLATE、BENAZEPRIL HYDROCHLORIDE | 膠囊劑 | 治療高血壓，此複方藥品不適合用於起始治療 |
| 衛署藥製字第057325號 | 壓諾本錠 | AMLODIPINE BESYLATE、BENAZEPRIL HYDROCHLORIDE | 錠劑 | 治療高血壓，此複方藥品不適合用於起始治療。 |
| 衛部藥製字第059395號 | 可得寧膜衣錠5/10毫克 | AMLODIPINE BESYLATE、BENAZEPRIL HYDROCHLORIDE | 膜衣錠 | 治療高血壓。此複方藥品不適合用於起始治療。 |

<details><summary><strong>已註銷</strong>（3 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第019089號</td><td>汽巴欣膜衣錠5毫克</td><td>BENAZEPRIL HYDROCHLORIDE</td><td>2018/07/13</td></tr><tr><td>衛署藥輸字第019090號</td><td>汽巴欣膜衣錠１０公絲</td><td>BENAZEPRIL HYDROCHLORIDE</td><td>2016/06/03</td></tr><tr><td>衛署藥輸字第019091號</td><td>汽巴欣膜衣錠２０公絲</td><td>BENAZEPRIL HYDROCHLORIDE</td><td>2005/06/03</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自 TxGNN 知識圖譜的藥物—疾病關聯，非仿單文字）：包括血管性水腫（含遺傳性及 ACE 抑制劑誘發型）、腎臟疾病、肝衰竭與肝病、無尿症、低血壓、胰臟炎、糖尿病酮酸中毒、嗜中性白血球低下與顆粒球缺乏症、全身性紅斑性狼瘡、結締組織疾病、低血鉀、副甲狀腺機能亢進、新生兒黃疸等。實際禁忌請以原廠仿單為準。
- **藥物交互作用**：共查得 169 筆交互作用，已列出者多為中度等級，主要涉及降血糖藥物，例如：
  - 胰島素類（human、aspart、degludec、detemir、glargine、glulisine、lispro 等）
  - 磺醯脲類（glimepiride、glipizide、glyburide、chlorpropamide、acetohexamide）
  - 其他降血糖藥（alogliptin、dapagliflozin、exenatide）
  - 其他：hydrocortisone、glycerin

  合併使用時建議監測血糖與血壓。

其他警語與禁忌症的仿單資訊，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（99.65%），但沒有任何臨床試驗或直接文獻支持，證據等級為 L5，僅有模型預測與藥理推論。
- 原始作用機轉資料缺漏，且 ACE 抑制劑用於腎血管性高血壓有腎功能風險，需先釐清再推進。

**若要推進需要：**
- 補齊 Benazepril 的作用機轉資料（如透過 DrugBank 查詢）
- 針對 ACE 抑制劑用於（惡性）腎血管性高血壓的臨床試驗、治療指引與系統性回顧進行文獻檢索
- 評估雙側腎動脈狹窄或單一腎病患者的腎功能與高血鉀風險，並制定監測方案
- 確認此適應症與台灣現行核准「高血壓」適應症的差異，以及是否需要新增適應症申請

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表「衛部藥輸字第025881號 鹽酸貝那普利」字號 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 紓心膠囊許可證效期 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表中 4 張成品許可證皆為 amlodipine＋benazepril 複方 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

