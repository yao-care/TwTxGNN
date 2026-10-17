---
layout: default
title: Cromoglicic Acid
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-16
description: "Cromoglicic Acid：預測新適應症為潰瘍性直腸乙狀結腸炎 (Ulcerative Proctosigmoiditis)（證據等級 L5）。原適應症：過敏性結膜炎、過敏性鼻炎"
monitor_inn: "Cromoglicic acid"
predicted_indications: ["ulcerative proctosigmoiditis", "nocardiosis", "cap polyposis", "cutaneous photosensitivity-lethal colitis syndrome", "undetermined colitis", "pneumocystosis", "osteoarthritis", "allergic urticaria", "neonatal inflammatory skin and bowel disease"]
---

# Cromoglicic Acid
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

# Cromoglicic acid：從過敏性結膜炎與過敏性鼻炎到潰瘍性直腸乙狀結腸炎

<!-- review:begin cromoglicic-acid-original-indication-title-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「# Cromoglicic acid：從氣喘與過敏性鼻炎到潰瘍性直腸乙狀結腸炎」。TFDA 許可證資料中，cromolyn sodium（sodium cromoglicate，色甘酸鈉）截至資料集日期有效的單方許可證共 13 張（另 1 張衛署藥製字第051028號舒治敏鼻用噴液劑已過期）：其中 11 張是製劑，都是過敏性結膜炎點眼液（如衛署藥製字第049351號、衛部藥製字第059380號）與過敏性鼻炎噴鼻劑（如衛署藥輸字第021824號）；另 2 張是原料藥，衛署藥輸字第025831號「果莫喘鈉」登載適應症為「支氣管擴張劑」、衛部藥輸字第029058號「色甘酸鈉鹽」為「過敏症用藥」。台灣沒有有效的氣喘吸入劑或口服製劑許可證，肥大細胞增生症也不在有效許可證的適應症內。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end cromoglicic-acid-original-indication-title-2026-10-16 -->

## 一句話總結

Cromoglicic acid（色甘酸）是一種肥大細胞穩定劑，在台灣的有效製劑許可證用於過敏性結膜炎（點眼液）與過敏性鼻炎（噴鼻劑）；氣喘吸入劑與肥大細胞增生症用的口服劑型在台灣沒有有效製劑許可證。
TxGNN 模型預測它可能對**潰瘍性直腸乙狀結腸炎 (Ulcerative Proctosigmoiditis)** 有效（預測分數 99.99%），
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅為模型預測。

<!-- review:begin cromoglicic-acid-original-indication-summary-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「原本用於氣喘、過敏性鼻炎、過敏性結膜炎及肥大細胞增生症等過敏相關疾病。」。TFDA 許可證資料中，cromolyn sodium（sodium cromoglicate，色甘酸鈉）截至資料集日期有效的單方許可證共 13 張（另 1 張衛署藥製字第051028號舒治敏鼻用噴液劑已過期）：其中 11 張是製劑，都是過敏性結膜炎點眼液（如衛署藥製字第049351號、衛部藥製字第059380號）與過敏性鼻炎噴鼻劑（如衛署藥輸字第021824號）；另 2 張是原料藥，衛署藥輸字第025831號「果莫喘鈉」登載適應症為「支氣管擴張劑」、衛部藥輸字第029058號「色甘酸鈉鹽」為「過敏症用藥」。台灣沒有有效的氣喘吸入劑或口服製劑許可證，肥大細胞增生症也不在有效許可證的適應症內。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end cromoglicic-acid-original-indication-summary-2026-10-16 -->

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 過敏性結膜炎、過敏性鼻炎（台灣有效單方製劑許可證）；原料藥許可證另登載支氣管擴張劑、過敏症用藥；肥大細胞增生症為知識圖譜的適應症關聯 |
| 預測新適應症 | 潰瘍性直腸乙狀結腸炎 (Ulcerative Proctosigmoiditis) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 46 張（有效單方 13／有效複方 0／已過期 1／已註銷 32） |
| 建議決策 | Hold |

<!-- review:begin cromoglicic-acid-tw-marketed-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「台灣上市／✗ 未上市」。台灣有主成分為色甘酸鈉的有效許可證，屬已上市。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end cromoglicic-acid-tw-marketed-2026-10-03 -->

<!-- review:begin cromoglicic-acid-original-indication-row-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「原適應症／氣喘、過敏性鼻炎、過敏性結膜炎、肥大細胞增生症（來自知識圖譜的適應症關聯，非台灣許可證）」。TFDA 許可證資料中，cromolyn sodium（sodium cromoglicate，色甘酸鈉）截至資料集日期有效的單方許可證共 13 張（另 1 張衛署藥製字第051028號舒治敏鼻用噴液劑已過期）：其中 11 張是製劑，都是過敏性結膜炎點眼液（如衛署藥製字第049351號、衛部藥製字第059380號）與過敏性鼻炎噴鼻劑（如衛署藥輸字第021824號）；另 2 張是原料藥，衛署藥輸字第025831號「果莫喘鈉」登載適應症為「支氣管擴張劑」、衛部藥輸字第029058號「色甘酸鈉鹽」為「過敏症用藥」。台灣沒有有效的氣喘吸入劑或口服製劑許可證，肥大細胞增生症也不在有效許可證的適應症內。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end cromoglicic-acid-original-indication-row-2026-10-16 -->

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Cromoglicic acid 屬於肥大細胞穩定劑，已用於多種過敏性疾病，其機轉上可能是抑制肥大細胞釋放發炎介質。

潰瘍性直腸乙狀結腸炎是發生在直腸與乙狀結腸的黏膜發炎。理論上，若肥大細胞釋放的介質參與腸黏膜發炎，穩定肥大細胞或許能減輕發炎反應。

不過，這只是推測性的機轉連結。目前僅有 TxGNN 預測支持此適應症，沒有臨床或文獻證據，也尚無法確認與原適應症的相似性及給藥途徑是否相容。

### 其他預測適應症的參考

TxGNN 另預測了多個適應症，整體證據同樣停留在模型預測階段：

| 預測適應症 | 分數 | 機轉合理性簡評 |
|-----------|------|---------------|
| 蕁麻疹（過敏性） | 99.95% | 肥大細胞脫顆粒與組織胺釋放是蕁麻疹的核心機轉，生物學上合理，可列為研究問題 |
| 酒糟性結膜炎 | 99.99% | 藥物已用於過敏性與春季結膜炎，眼表發炎機轉可能相通，但無直接證據 |
| 未確定型結腸炎 | 99.98% | 肥大細胞介質可能參與腸道發炎，僅屬理論推測 |
| 骨關節炎 | 99.96% | 僅有一篇與藥物無關的類風濕性關節炎生物標記文獻，不構成支持 |
| 奴卡氏菌病、肺囊蟲肺炎 | 99.99%、99.97% | 屬細菌／黴菌感染，肥大細胞穩定無已知抗微生物作用，高分疑為模型假象 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無針對潰瘍性直腸乙狀結腸炎的相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Cromoglicic Acid 的不重複許可證共 **46 張**：有效單方 13 張、有效複方 0 張、已過期 1 張（未註銷但有效日期早於資料集日期）、已註銷 32 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（13 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第039964號 | 信妥單劑量點眼液2% | 點眼液劑 | 麥迪森醫藥股份有限公司 | 2031/05/06 | 過敏性結膜炎 |
| 衛署藥製字第047622號 | "應元" 療敏眼藥水2% | 點眼液劑 | 應元化學製藥股份有限公司 | 2030/11/03 | 過敏性結膜炎。 |
| 衛署藥製字第047809號 | "黃氏" 敏保鼻用噴液劑 | 鼻用噴液劑 | 黃氏製藥股份有限公司 | 2031/02/10 | 各種過敏性鼻炎、季節性及全年性的鼻炎、乾草熱。 |
| 衛署藥製字第047990號 | 樂舒敏點眼液 | 點眼液劑 | 溫士頓醫藥股份有限公司 | 2031/05/23 | 過敏性結膜炎。 |
| 衛署藥製字第048900號 | “麥迪森”麥敏眼藥水 2% | 點眼液劑 | 麥迪森醫藥股份有限公司 | 2027/07/19 | 過敏性結膜炎。 |
| 衛署藥製字第049351號 | “派頓”克樂敏眼藥水 2% | 點眼液劑 | 臺灣派頓化學製藥股份有限公司 | 2028/03/31 | 過敏性結膜炎。 |
| 衛署藥製字第057329號 | "杏輝"眸朗明眼藥水 | 點眼液劑 | 杏輝藥品工業股份有限公司 | 2027/08/15 | 過敏性結膜炎。 |
| 衛署藥輸字第020121號 | 唯敏準眼用液劑 | 點眼液劑 | 武昌貿易有限公司 | 2028/10/07 | 暫時緩解已經醫師診斷之過敏性結膜炎、枯草熱所引起的相關症狀(流淚、搔癢、充血)。 |
| 衛署藥輸字第021824號 | 艾麗鼻用噴液劑２．８ＭＧ/ＳＰＲＡＹ | 鼻用噴液劑 | 吉富貿易有限公司 | 2027/07/24 | 過敏性鼻炎 |
| 衛署藥輸字第023892號 | 悅力舒點眼液 | 點眼液劑 | 吉富貿易有限公司 | 2028/12/09 | 過敏性結膜炎 |
| 衛署藥輸字第025831號 | 果莫喘鈉 | （粉） | 新雙隆生技股份有限公司 | 2027/10/04 | 支氣管擴張劑 |
| 衛部藥製字第059380號 | 舒敏眼藥水2% | 點眼液劑 | 健喬信元醫藥生技股份有限公司 | 2026/11/15 | 過敏性結膜炎。 |
| 衛部藥輸字第029058號 | 色甘酸鈉鹽 | （粉） | 商鶴藥品有限公司 | 2030/11/03 | 過敏症用藥 |

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-09-29）</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛署藥製字第051028號</td><td>舒治敏鼻用噴液劑</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2024/09/18</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（32 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第013937號</td><td>可樂得利噴鼻液</td><td>CROMOLYN</td><td>1997/04/08</td></tr><tr><td>衛署藥製字第040642號</td><td>優鼻噴鼻液（可樂得利）</td><td>CROMOLYN</td><td>2015/06/29</td></tr><tr><td>衛署藥製字第043819號</td><td>"瑞安" 睛爽達點眼液４０公絲/公撮</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2017/02/06</td></tr><tr><td>衛署藥輸字第001244號</td><td>可樂得利二鈉鹽</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>1991/08/19</td></tr><tr><td>衛署藥輸字第001654號</td><td>咽達永樂膠囊</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第004554號</td><td>弗喘膠囊吸入劑</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>1987/03/27</td></tr><tr><td>衛署藥輸字第006109號</td><td>弗喘複合膠囊</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第006802號</td><td>果莫喘鈉</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第013242號</td><td>咽達永樂吸入用膠囊劑</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第016115號</td><td>敏鼻速樂噴鼻液</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第016116號</td><td>敏眼速樂點眼液</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第016829號</td><td>喘可免吸入用膠囊</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2000/10/20</td></tr><tr><td>衛署藥輸字第017027號</td><td>果莫喘鈉</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第017129號</td><td>可樂得利二鈉鹽</td><td>CROMOLYN</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第017522號</td><td>維眼康眼藥水</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第018628號</td><td>咽達永樂吸入劑</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第018783號</td><td>可舒噴鼻劑</td><td>CROMOLYN SODIUM MONOHYDRATE</td><td>2018/03/15</td></tr><tr><td>衛署藥輸字第018908號</td><td>果莫喘鈉</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第019076號</td><td>可舒眼藥水</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2008/07/16</td></tr><tr><td>衛署藥輸字第019270號</td><td>果莫喘鈉</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2014/01/28</td></tr><tr><td>衛署藥輸字第019410號</td><td>艾麗點眼液</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2019/03/28</td></tr><tr><td>衛署藥輸字第020344號</td><td>諾視朗鼻用噴液劑２．６ＭＧ/ＤＯＳＥ</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2004/09/22</td></tr><tr><td>衛署藥輸字第020546號</td><td>克喘乾粉吸入用膠囊劑</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第020632號</td><td>微微準鼻用噴液劑</td><td>CROMOLYN</td><td>2016/06/01</td></tr><tr><td>衛署藥輸字第021066號</td><td>諾目朗點眼液</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2004/09/22</td></tr><tr><td>衛署藥輸字第021402號</td><td>平克癒吸入劑５ＭＧ﹨ＤＯＳＥ</td><td>CROMOLYN</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第022224號</td><td>克視敏點眼液２％</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2016/05/31</td></tr><tr><td>衛署藥輸字第022275號</td><td>克視敏點眼液４％</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2016/05/31</td></tr><tr><td>衛署藥輸字第022341號</td><td>鼻恩通鼻用噴液劑２．８ＭＧ/ＳＰＲＡＹ</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第022922號</td><td>克鼻敏２％鼻用噴液劑</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2013/01/08</td></tr><tr><td>衛署藥輸字第023115號</td><td>克鼻敏４％鼻用噴液劑</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2017/06/05</td></tr><tr><td>衛署藥輸字第024572號</td><td>悅鼻康鼻用噴液劑</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2018/02/12</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的禁忌疾病（非仿單內容）**：肝衰竭、腎臟疾病、輸尿管積膿、肝臟疾病、膽囊疾病、鼻腔息肉。此資訊來自知識圖譜關聯，須以正式仿單核對。
- **藥物交互作用**：已查得 100 筆交互作用紀錄。目前列出的資料中，Insulin human（吸入型速效胰島素）為中度（Moderate）；其餘如 Theophylline、Valproic acid、Topiramate、Erythromycin、Fluconazole、Metoprolol 等，嚴重度分級為未知，需進一步確認。

仿單中的警語與禁忌資料尚未取得，其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 潰瘍性直腸乙狀結腸炎的預測僅來自 TxGNN 模型，沒有任何臨床試驗或文獻佐證（證據等級 L5）。
- 台灣已有色甘酸鈉的有效許可證（點眼液、噴鼻劑），但作用機轉與仿單安全性資料皆缺漏。

<!-- review:begin cromoglicic-acid-original-indication-conclusion-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「- 台灣目前無上市許可證，且作用機轉與仿單安全性資料皆缺漏。」。TFDA 許可證資料中，cromolyn sodium（sodium cromoglicate，色甘酸鈉）截至資料集日期有效的單方許可證共 13 張（另 1 張衛署藥製字第051028號舒治敏鼻用噴液劑已過期）：其中 11 張是製劑，都是過敏性結膜炎點眼液（如衛署藥製字第049351號、衛部藥製字第059380號）與過敏性鼻炎噴鼻劑（如衛署藥輸字第021824號）；另 2 張是原料藥，衛署藥輸字第025831號「果莫喘鈉」登載適應症為「支氣管擴張劑」、衛部藥輸字第029058號「色甘酸鈉鹽」為「過敏症用藥」。台灣沒有有效的氣喘吸入劑或口服製劑許可證，肥大細胞增生症也不在有效許可證的適應症內。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end cromoglicic-acid-original-indication-conclusion-2026-10-16 -->

**若要推進需要：**
- 補齊作用機轉（MOA）資料，並評估肥大細胞在潰瘍性結腸炎的角色
- 系統性檢索色甘酸用於發炎性腸病的既有文獻與臨床試驗
- 取得仿單的警語與禁忌資料，並釐清交互作用的嚴重度分級
- 評估給藥途徑（如直腸給藥或口服）與腸道局部作用的可行性
- 若需優先探索，蕁麻疹因機轉較合理，可作為另一個研究問題一併評估

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「台灣目前無任何藥品許可證」 | 報告重生後已無此錯誤（2026-10-15：新報告一句話總結未再寫「台灣目前無任何藥品許可證」；原為更正（2026-10-16 修訂，前版保留於紀錄）） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 原適應症「（台灣未登記）」 | 報告重生後已無此錯誤（2026-10-15：新報告「原適應症」列未再寫「台灣未登記」；同一份報告的「台灣上市」列仍寫未上市、結論仍寫無上市許可證，另有查核紀錄更正；原為更正（2026-10-16 修訂，前版保留於紀錄）） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 台灣上市「未上市」 | 更正（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證數「0 張」 | 已由程式化許可證表取代（原為更正（2026-10-16 修訂，前版保留於紀錄）） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「在台灣目前無任何藥品許可證，屬未上市藥物」 | 報告重生後已無此錯誤（2026-10-15：新報告「台灣上市資訊」未再寫「無任何藥品許可證，屬未上市藥物」；原為更正（2026-10-16 修訂，前版保留於紀錄）） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 下一步「目前 0 張許可證」 | 已由程式化許可證表取代（原為加註（2026-10-16 修訂，前版保留於紀錄）） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 結論稱台灣目前無上市許可證 | 更正（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 原適應症列氣喘、肥大細胞增生症 | 更正（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 標題以氣喘為原用途 | 更正（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 一句話總結以氣喘、肥大細胞增生症為原用途 | 更正（2026-10-16 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

