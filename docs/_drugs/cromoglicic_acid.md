---
layout: default
title: Cromoglicic Acid
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Cromoglicic Acid：從過敏性結膜炎到過敏性蕁麻疹（多適應症評估）

## 一句話總結

Cromoglicic acid（色甘酸）是已知的**肥大細胞穩定劑**，國際上核准用於過敏性結膜炎、氣喘及食物過敏，但台灣目前無任何藥品許可證。TxGNN 模型針對 10 項新適應症進行預測，**過敏性蕁麻疹 (Allergic Urticaria)** 具備最強的機轉合理性，目前有 **19 篇文獻**間接支持，建議列為研究問題；TxGNN 分數最高的**潰瘍性直腸乙狀結腸炎**已有直接 RCT 顯示局部給藥無效，建議暫緩。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 過敏性結膜炎、過敏性鼻炎（台灣有效許可證） |
| 預測適應症數 | 10 項 |
| TxGNN 最高分適應症 | 潰瘍性直腸乙狀結腸炎（99.99%） |
| 最具潛力適應症 | 過敏性蕁麻疹（L3 證據，Research Question） |
| 最佳證據等級 | L3（潰瘍性直腸乙狀結腸炎、過敏性蕁麻疹） |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 46 張（有效單方 14／有效複方 0／已註銷 32） |
| 建議決策 | **Research Question**（2 項）／Hold（8 項） |

<!-- review:begin cromoglicic-acid-original-indication-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「原適應症／過敏性結膜炎、氣喘（台灣未登記）」。台灣有效許可證核准的適應症為過敏性結膜炎（點眼液）與過敏性鼻炎（噴鼻劑）。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end cromoglicic-acid-original-indication-2026-10-03 -->

<!-- review:begin cromoglicic-acid-tw-marketed-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「台灣上市／✗ 未上市」。台灣有主成分為色甘酸鈉的有效許可證，屬已上市。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end cromoglicic-acid-tw-marketed-2026-10-03 -->

---

## 所有預測適應症摘要

| 排名 | 適應症 | TxGNN 分數 | 臨床試驗 | 文獻數 | 證據等級 | 建議決策 |
|------|--------|-----------|---------|-------|---------|---------|
| 1 | 潰瘍性直腸乙狀結腸炎 | 99.99% | 0 | 2 | L3 | Hold |
| 2 | 諾卡氏菌病 | 99.99% | 0 | 0 | L5 | Hold |
| 3 | 玫瑰斑相關結膜炎 | 99.99% | 0 | 1 | L4 | Research Question |
| 4 | Cap 息肉病 | 99.99% | 0 | 0 | L5 | Hold |
| 5 | 皮膚光敏感-致命性結腸炎症候群 | 99.99% | 0 | 0 | L5 | Hold |
| 6 | 不確定性結腸炎 | 99.98% | 0 | 0 | L5 | Hold |
| 7 | 肺孢子菌肺炎 | 99.97% | 0 | 0 | L5 | Hold |
| 8 | 骨關節炎 | 99.96% | 0 | 2 | L4 | Hold |
| **9** | **過敏性蕁麻疹** | **99.95%** | **0** | **19** | **L3** | **Research Question** |
| 10 | 新生兒炎症性皮膚腸道病 | 99.94% | 0 | 0 | L5 | Hold |

---

## 為什麼這個預測合理？

Cromoglicic acid 的核心機轉是**阻斷肥大細胞脫顆粒**：當 IgE 與過敏原交聯後，觸發鈣離子流入肥大細胞，導致組織胺、白三烯等炎症介質釋放。色甘酸透過穩定細胞膜、阻斷此鈣離子通道，在多個已核准適應症（過敏性結膜炎、氣喘、食物過敏）中發揮預防性抗過敏效果。

**過敏性蕁麻疹**的核心病理正是皮膚肥大細胞的 IgE 介導脫顆粒，釋放組織胺導致風疹塊及搔癢，與色甘酸的作用靶點高度一致。已有多篇觀察性研究顯示，口服色甘酸對食物過敏引發之蕁麻疹及血管性水腫具有療效（PMID 3091307、PMID 1708197、PMID 6159572），提供了機轉上的間接臨床佐證。

**玫瑰斑相關結膜炎**（排名第 3）亦具有合理的機轉基礎：色甘酸已核准用於過敏性結膜炎，玫瑰斑相關眼表疾病涉及慢性肥大細胞活化，兩者在眼表炎症路徑上有所重疊，值得進一步探索。相對地，感染性疾病（諾卡氏菌病、肺孢子菌肺炎）及遺傳性屏障缺陷病（新生兒炎症性皮膚腸道病）的預測機轉關聯性不成立，建議維持 Hold。

---

## 臨床試驗證據

目前無相關臨床試驗登記（10 項預測適應症均未找到已登記的臨床試驗）。

---

## 文獻證據（重點適應症：過敏性蕁麻疹）

以下為與過敏性蕁麻疹及 Cromoglicic acid 最相關的文獻（共 19 篇，列出前 10 篇最相關者）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [3091307](https://pubmed.ncbi.nlm.nih.gov/3091307/) | 1986 | Case series | Clin Immunol Immunopathol | 口服色甘酸對 IgE 介導食物過敏（蕁麻疹／血管性水腫）患者顯示顯著症狀改善，安慰劑組無效 |
| [1708197](https://pubmed.ncbi.nlm.nih.gov/1708197/) | 1990 | Case series | Allergologia et immunopathologia | 兒童食物過敏（含蕁麻疹）以口服 Sodium cromoglycate 治療，提供診斷與療效評估架構 |
| [6159572](https://pubmed.ncbi.nlm.nih.gov/6159572/) | 1980 | — | La Nouvelle presse medicale | 口服 DSCG 對 I 型食物過敏引發蕁麻疹及血管性水腫者的療效比較（vs 假性過敏組） |
| [3135820](https://pubmed.ncbi.nlm.nih.gov/3135820/) | 1988 | — | Allergie et immunologie | 多中心研究：口服 NALCRON（色甘酸）對食物過敏（蕁麻疹／濕疹）配合排除飲食有效 |
| [11761817](https://pubmed.ncbi.nlm.nih.gov/11761817/) | 2001 | — | Polski merkuriusz lekarski | 3 歲以下嬰幼兒食物過敏：口服色甘酸療效與安全性評估，支持抗過敏藥物的預防性應用 |
| [6405650](https://pubmed.ncbi.nlm.nih.gov/6405650/) | 1983 | — | Allergy | 雙盲交叉試驗：口服 DSCG 對異位性皮膚炎（與蕁麻疹共享 IgE/肥大細胞路徑）6 週後顯著改善 |
| [6194502](https://pubmed.ncbi.nlm.nih.gov/6194502/) | 1983 | — | Pediatr Clin North Am | Cromolyn 完整回顧：過去、現在與未來，涵蓋各給藥途徑及適應症的臨床應用 |
| [2226222](https://pubmed.ncbi.nlm.nih.gov/2226222/) | 1990 | Review | Drugs | Ketotifen 評論：與色甘酸在過敏性疾病（含蕁麻疹相關IgE路徑）的療效比較 |
| [8146811](https://pubmed.ncbi.nlm.nih.gov/8146811/) | 1994 | Review | Therapeutische Umschau | 食物過敏（含蕁麻疹）機轉、診斷與治療全面回顧，IgE 介導路徑為主 |
| [6152751](https://pubmed.ncbi.nlm.nih.gov/6152751/) | 1984 | Review | Tokai J Exp Clin Med | 眼科搔癢的治療：INTAL（色甘酸）作為化學介質抑制劑的臨床應用，肥大細胞脫顆粒路徑 |

---

## 文獻證據（重點適應症：潰瘍性直腸乙狀結腸炎）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [3090860](https://pubmed.ncbi.nlm.nih.gov/3090860/) | 1986 | **RCT** | Acta Med Scand | **雙盲試驗（n=43）：DSCG 600 mg 直腸灌腸 8 週，與安慰劑相比無任何顯著差異，局部給藥無效** |
| [1967326](https://pubmed.ncbi.nlm.nih.gov/1967326/) | 1990 | Review | Med Clin North Am | 潰瘍性直腸乙狀結腸炎局部治療回顧；5-ASA 灌腸優於類固醇，色甘酸未獲推薦 |

---

## 文獻證據（重點適應症：玫瑰斑相關結膜炎）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [2154106](https://pubmed.ncbi.nlm.nih.gov/2154106/) | 1990 | Review | Am J Ophthalmol | 慢性結膜炎系統性診斷與治療方法；INTAL（色甘酸）列為化學介質抑制劑的選項之一 |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Cromoglicic Acid 的不重複許可證共 **46 張**：有效單方 14 張、有效複方 0 張、已註銷 32 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（14 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第039964號 | 信妥單劑量點眼液2% | 點眼液劑 | 麥迪森醫藥股份有限公司 | 2031/05/06 | 過敏性結膜炎 |
| 衛署藥製字第047622號 | "應元" 療敏眼藥水2% | 點眼液劑 | 應元化學製藥股份有限公司 | 2030/11/03 | 過敏性結膜炎。 |
| 衛署藥製字第047809號 | "黃氏" 敏保鼻用噴液劑 | 鼻用噴液劑 | 黃氏製藥股份有限公司 | 2031/02/10 | 各種過敏性鼻炎、季節性及全年性的鼻炎、乾草熱。 |
| 衛署藥製字第047990號 | 樂舒敏點眼液 | 點眼液劑 | 溫士頓醫藥股份有限公司 | 2031/05/23 | 過敏性結膜炎。 |
| 衛署藥製字第048900號 | “麥迪森”麥敏眼藥水 2% | 點眼液劑 | 麥迪森醫藥股份有限公司 | 2027/07/19 | 過敏性結膜炎。 |
| 衛署藥製字第049351號 | “派頓”克樂敏眼藥水 2% | 點眼液劑 | 臺灣派頓化學製藥股份有限公司 | 2028/03/31 | 過敏性結膜炎。 |
| 衛署藥製字第051028號 | 舒治敏鼻用噴液劑 | 點鼻液劑 | 廣欣藥品股份有限公司 | 2024/09/18 | 急性鼻炎、過敏性鼻炎、鼻竇炎、鼻咽炎。 |
| 衛署藥製字第057329號 | "杏輝"眸朗明眼藥水 | 點眼液劑 | 杏輝藥品工業股份有限公司 | 2027/08/15 | 過敏性結膜炎。 |
| 衛署藥輸字第020121號 | 唯敏準眼用液劑 | 點眼液劑 | 武昌貿易有限公司 | 2028/10/07 | 暫時緩解已經醫師診斷之過敏性結膜炎、枯草熱所引起的相關症狀(流淚、搔癢、充血)。 |
| 衛署藥輸字第021824號 | 艾麗鼻用噴液劑２．８ＭＧ/ＳＰＲＡＹ | 鼻用噴液劑 | 吉富貿易有限公司 | 2027/07/24 | 過敏性鼻炎 |
| 衛署藥輸字第023892號 | 悅力舒點眼液 | 點眼液劑 | 吉富貿易有限公司 | 2028/12/09 | 過敏性結膜炎 |
| 衛署藥輸字第025831號 | 果莫喘鈉 | （粉） | 新雙隆生技股份有限公司 | 2027/10/04 | 支氣管擴張劑 |
| 衛部藥製字第059380號 | 舒敏眼藥水2% | 點眼液劑 | 健喬信元醫藥生技股份有限公司 | 2026/11/15 | 過敏性結膜炎。 |
| 衛部藥輸字第029058號 | 色甘酸鈉鹽 | （粉） | 商鶴藥品有限公司 | 2030/11/03 | 過敏症用藥 |

<details><summary><strong>已註銷</strong>（32 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第013937號</td><td>可樂得利噴鼻液</td><td>CROMOLYN</td><td>1997/04/08</td></tr><tr><td>衛署藥製字第040642號</td><td>優鼻噴鼻液（可樂得利）</td><td>CROMOLYN</td><td>2015/06/29</td></tr><tr><td>衛署藥製字第043819號</td><td>"瑞安" 睛爽達點眼液４０公絲/公撮</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2017/02/06</td></tr><tr><td>衛署藥輸字第001244號</td><td>可樂得利二鈉鹽</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>1991/08/19</td></tr><tr><td>衛署藥輸字第001654號</td><td>咽達永樂膠囊</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第004554號</td><td>弗喘膠囊吸入劑</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>1987/03/27</td></tr><tr><td>衛署藥輸字第006109號</td><td>弗喘複合膠囊</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第006802號</td><td>果莫喘鈉</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第013242號</td><td>咽達永樂吸入用膠囊劑</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第016115號</td><td>敏鼻速樂噴鼻液</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第016116號</td><td>敏眼速樂點眼液</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第016829號</td><td>喘可免吸入用膠囊</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2000/10/20</td></tr><tr><td>衛署藥輸字第017027號</td><td>果莫喘鈉</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第017129號</td><td>可樂得利二鈉鹽</td><td>CROMOLYN</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第017522號</td><td>維眼康眼藥水</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第018628號</td><td>咽達永樂吸入劑</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第018783號</td><td>可舒噴鼻劑</td><td>CROMOLYN SODIUM MONOHYDRATE</td><td>2018/03/15</td></tr><tr><td>衛署藥輸字第018908號</td><td>果莫喘鈉</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第019076號</td><td>可舒眼藥水</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2008/07/16</td></tr><tr><td>衛署藥輸字第019270號</td><td>果莫喘鈉</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2014/01/28</td></tr><tr><td>衛署藥輸字第019410號</td><td>艾麗點眼液</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2019/03/28</td></tr><tr><td>衛署藥輸字第020344號</td><td>諾視朗鼻用噴液劑２．６ＭＧ/ＤＯＳＥ</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2004/09/22</td></tr><tr><td>衛署藥輸字第020546號</td><td>克喘乾粉吸入用膠囊劑</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第020632號</td><td>微微準鼻用噴液劑</td><td>CROMOLYN</td><td>2016/06/01</td></tr><tr><td>衛署藥輸字第021066號</td><td>諾目朗點眼液</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2004/09/22</td></tr><tr><td>衛署藥輸字第021402號</td><td>平克癒吸入劑５ＭＧ﹨ＤＯＳＥ</td><td>CROMOLYN</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第022224號</td><td>克視敏點眼液２％</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2016/05/31</td></tr><tr><td>衛署藥輸字第022275號</td><td>克視敏點眼液４％</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2016/05/31</td></tr><tr><td>衛署藥輸字第022341號</td><td>鼻恩通鼻用噴液劑２．８ＭＧ/ＳＰＲＡＹ</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第022922號</td><td>克鼻敏２％鼻用噴液劑</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2013/01/08</td></tr><tr><td>衛署藥輸字第023115號</td><td>克鼻敏４％鼻用噴液劑</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2017/06/05</td></tr><tr><td>衛署藥輸字第024572號</td><td>悅鼻康鼻用噴液劑</td><td>CROMOLYN SODIUM (EQ TO SODIUM CROMOGLICATE)(EQ TO SODIUM CRO…</td><td>2018/02/12</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

Cromoglicic acid 在台灣目前**無任何藥品許可證**，屬未上市藥物。若有研究需求，需透過 TFDA 專案核准（專案進口）管道取得。

---

## 安全性考量

**藥物交互作用（共 100 筆，列出主要 10 筆）：**

| 相互作用藥物 | 等級 | 說明 |
|------------|------|------|
| Insulin human（吸入型速效） | **中度 (Moderate)** | 與色甘酸合用可能影響血糖調控，需監測 |
| Theophylline | 未知 | 同為呼吸道用藥，合用交互作用程度待確認 |
| Erythromycin | 未知 | 可能影響代謝，程度待確認 |
| Moxifloxacin | 未知 | 程度待確認 |
| Fluconazole | 未知 | 程度待確認 |
| Citalopram | 未知 | 程度待確認 |
| Valproic acid | 未知 | 程度待確認 |
| Metoprolol | 未知 | 程度待確認 |
| Omeprazole | 未知 | 程度待確認 |
| Pantoprazole | 未知 | 程度待確認 |

> 共 99 筆交互作用等級為「未知」；**唯一確認中度交互作用**為吸入型速效胰島素（Insulin human）。建議就重要合用藥物個別查閱最新文獻或諮詢臨床藥師。

安全性警語及禁忌症資料尚未收錄，請參考原廠仿單。

---

## 結論與下一步

**決策：Research Question（過敏性蕁麻疹）／Hold（其餘 9 項）**

**理由：**

10 項預測適應症中，TxGNN 最高分的潰瘍性直腸乙狀結腸炎已遭直接 RCT 否定，不建議進一步投入。**過敏性蕁麻疹**與色甘酸的作用機轉高度吻合（IgE/肥大細胞脫顆粒路徑），雖目前僅有觀察性研究與個案系列，但機轉合理性與間接臨床佐證足以支持提出正式研究假說；**玫瑰斑相關結膜炎**因原適應症（過敏性結膜炎）的延伸合理性，亦值得納入眼科研究規劃。

**若要推進「過敏性蕁麻疹」研究需要：**
- 設計以過敏性蕁麻疹為主要終點的前瞻性 RCT，確認口服色甘酸劑量與療程
- 釐清適用族群（IgE 介導型 vs. 慢性自發性蕁麻疹）
- 補充完整 TFDA 仿單資料，完成安全性初評（Data Gap DG001）
- 查詢 DrugBank API 補充完整作用機轉資料（Data Gap DG002）
- 評估台灣 TFDA 引進路徑（目前 46 張許可證（有效 14 張），需確認專案進口或新申請可行性）

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「台灣目前無任何藥品許可證」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 原適應症「（台灣未登記）」 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 台灣上市「未上市」 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證數「0 張」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「在台灣目前無任何藥品許可證，屬未上市藥物」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 下一步「目前 0 張許可證」 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

