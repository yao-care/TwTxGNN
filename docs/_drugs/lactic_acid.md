---
layout: default
title: Lactic Acid
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 5
monitor_inn: "Lactic acid"
predicted_indications: ["atypical coarctation of aorta", "aortic malformation", "non-syndromic esophageal malformation", "amenorrhea (disease)", "dry eye syndrome"]
last_modified_at: 2026-11-20
description: "Lactic Acid：預測新適應症為非典型主動脈縮窄 (Atypical coarctation of aorta)（證據等級 L5）。原適應症：婦女陰道及陰部之除臭與洗潔、白帶之預防與治療"
---

# Lactic Acid
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

## Lactic acid：從婦女陰道及陰部洗潔除臭到非典型主動脈縮窄
{: .text-alpha }

## 一句話總結

Lactic acid（乳酸）在台灣主要作為外用婦女陰道及陰部洗潔、除臭、白帶預防與治療用藥，也出現在除疣劑（與 salicylic acid 的複方）中；含「乳酸」字樣的整腸藥主成分是乳酸菌，不是乳酸。
TxGNN 模型預測它可能對**非典型主動脈縮窄 (Atypical coarctation of aorta)** 有效，但目前**無臨床試驗**、**無相關文獻**支持，屬於純模型預測。

<!-- review:begin lactic-acid-summary-oral-uses-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「也出現在部分腸胃藥與除疣劑中」。2026-10-15 報告重生後仍寫乳酸出現在腸胃藥中；現行有效的這類腸胃藥（表飛鳴－樂錠／散）主成分是抗生素耐性乳酸菌。TFDA 資料集中，截至資料集日期，乳酸的有效單方許可證都是外用液劑（陰道及陰部洗潔除臭、白帶）；「整腸」只見於已註銷的複方（「表舒鳴」散劑含比菲德氏菌、糞鏈球菌與乳酸；「寶兒康顆粒」為維生素複方）。含乳酸鹽的口服錠劑是含 calcium lactate（乳酸鈣）的鈣補充劑，用途是補鈣，不是整腸；乳酸鈣、乳酸鈉不算乳酸本身，不列入本頁許可證表。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end lactic-acid-summary-oral-uses-2026-10-03 -->

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 婦女陰道及陰部之除臭與洗潔、白帶之預防與治療 |
| 預測新適應症 | 非典型主動脈縮窄 (Atypical coarctation of aorta) |
| TxGNN 預測分數 | 0.9959 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 16 張／共 31 張） |
| 許可證數 | 31 張（有效單方 9／有效複方 7／已過期 1／已註銷 14） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

ChEMBL（EMBL-EBI）收錄的 Lactic Acid 作用機轉（非官方翻譯）：「pH降低劑」。英文原文："pH lowering agent"（[ChEMBL CHEMBL1200559 (lactic acid): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1200559)，CC BY-SA 3.0；查閱日期 2026-11-19）。Lactic acid 是一種有機酸，在台灣產品中多用於外用洗潔液，用以維持陰道酸性環境、除臭與清潔。

主動脈縮窄是先天性的血管結構缺陷，需靠手術或導管介入矯正，並非藥物可改善的疾病。乳酸（外用酸化劑與腸道輔助用途）與此疾病之間，在機轉上找不到可信的關聯。此預測僅來自 TxGNN 模型（深度學習）的分數，可能反映模型學到的相關疾病間的相似性，並非生物學證據，缺乏任何臨床或文獻佐證。

<!-- review:begin lactic-acid-why-oral-premise-2026-10-03 -->

> **查核加註（2026-10-03）**：台灣截至資料集日期，乳酸的有效單方許可證都是外用液劑（陰道及陰部洗潔除臭、白帶）；「整腸」只見於已註銷的複方（表舒鳴散劑、寶兒康顆粒），目前沒有核准的乳酸口服整腸用途。上段原文保留未改。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end lactic-acid-why-oral-premise-2026-10-03 -->

此外，排名前 10 的預測還包括主動脈畸形、食道畸形、閉經、乾眼症、食道疾病、複雜先天性心臟畸形、淚道異常、眼部疾病及馬尾症候群。其中多數屬於先天結構異常，乳酸沒有合理的治療機轉。乾眼症和眼部疾病雖有間接文獻，但內容多為乳酸菌或材料研究，並非乳酸本身的療效。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對首位預測（非典型主動脈縮窄）：目前無相關文獻。

為提供參考，以下為排名第 2 的「主動脈畸形」所檢索到的文獻。這些研究並未直接證明乳酸有效：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23791497](https://pubmed.ncbi.nlm.nih.gov/23791497/) | 2013 | RCT | J Cardiothorac Vasc Anesth | 小兒心臟手術中合併超濾策略的臨床效果，與乳酸治療無關 |
| [3367436](https://pubmed.ncbi.nlm.nih.gov/3367436/) | 1988 | 動物研究 | J Vasc Surg | 兔子主動脈縮窄後的動脈壁代謝與動脈粥樣硬化易感性，非乳酸療法 |
| [25157439](https://pubmed.ncbi.nlm.nih.gov/25157439/) | 2015 | 動物研究 | Catheter Cardiovasc Interv | 聚乳酸可降解支架用於兔降主動脈，屬材料研究 |
| [32382764](https://pubmed.ncbi.nlm.nih.gov/32382764/) | 2020 | 病例系列 | Pediatr Cardiol | 聚乳酸材料微板用於先天性心臟病嬰兒支氣管軟化，屬材料應用 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-11-24），主成分含 Lactic Acid 的不重複許可證共 **31 張**：有效單方 9 張、有效複方 7 張、已過期 1 張（未註銷但有效日期早於資料集日期）、已註銷 14 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-11-24）**（9 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第006636號 | 婦必寧濃縮液 | 外用液劑 | 歐文藥品股份有限公司 | 2029/04/15 | 婦女陰道及陰部之除臭與洗潔、白帶之預防與治療 |
| 衛署藥製字第017736號 | "久松"夢香縮潔液 | 外用液劑 | 久松化學企業股份有限公司 | 2028/05/25 | 婦女陰道及陰部之除臭與洗潔、白帶之預防與治療 |
| 衛署藥製字第019202號 | 婦寧濃縮液（乳酸） | 外用液劑 | 新喜國際企業股份有限公司 | 2028/05/25 | 婦女陰道及陰部之除臭及清潔、白帶之預防與治療 |
| 衛署藥製字第022462號 | 柔美濃縮洗液（乳酸） | 外用液劑 | 惠民製藥股份有限公司 | 2028/10/16 | 經期後婦女陰道及陰部之洗潔、除臭及日常洗潔、治療及預防陰道滴蟲性？炎、白帶、外陰搔癢 |
| 衛署藥製字第022957號 | 婦佳爽液（乳酸） | 外用液劑 | 理想藥品股份有限公司 | 2031/03/25 | 婦女陰道及陰部之洗潔與除臭、白帶之預防與治療 |
| 衛署藥製字第023755號 | 佳樂濃縮液（外用）（乳酸） | 外用液劑 | 成大藥品股份有限公司 | 2028/05/25 | 婦女陰道及陰部之除臭與洗潔、白帶之預防與治療 |
| 衛署藥製字第047838號 | ”華琳”舒潔婦女洗潔濃縮液 | 外用液劑 | 華琳實業有限公司 | 2031/02/22 | 經期後婦女陰道及陰部之洗潔、除臭及日常洗潔、治療及預防陰道滴蟲性膣炎、白帶、外陰搔癢。 |
| 衛署藥製字第048008號 | 新歡婦女洗潔濃縮液 | 外用液劑 | 天良生物科技企業股份有限公司 | 2031/06/07 | 婦女陰道及陰部之洗潔、除臭及日常洗潔、治療及預防陰道滴蟲性膣炎、白帶、外陰搔癢。 |
| 衛署藥製字第048338號 | 恆婦佳液 | 外用液劑 | 健康化學製藥股份有限公司 | 2031/10/27 | 婦女陰道及陰部之洗潔與除臭、白帶之預防與治療。 |

**有效・複方（截至資料集日期 2026-11-24；適應症屬整個複方，不是本藥單獨的適應症）**（7 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第009474號 | 啟力多注射液 | LACTIC ACID、SODIUM CHLORIDE、POTASSIUM CHLORIDE、GLUCOSE | 注射劑 | 大量出血、心臟衰弱、虛脫、大手術時之出血時用以補給水分電解質 |
| 衛署藥製字第020252號 | 洗汝潔濃縮殺菌液（乳酸） | LACTIC ACID、L-MENTHOL | 外用液劑 | 婦女陰道及陰部之洗潔與除臭、白帶之預防與治療、膀胱洗淨、皮膚腫瘍 |
| 衛署藥製字第030547號 | 利夫妥注射液 | POTASSIUM CHLORIDE、POTASSIUM PHOSPHATE ( eq to POTASSIUM PHO… | 注射劑 | 取代含有葡萄糖或轉化糖液劑之治療及其他非經口的水、電解質之補給 |
| 衛署藥輸字第017603號 | 史達德 治疣液 | LACTIC ACID、SALICYLIC ACID | 外用液劑 | 除疣劑 |
| 衛署藥輸字第025386號 | 補利壽血液過濾及血液透析液 (4mmol/l鉀) | MAGNESIUM CHLORIDE HEXAHYDRATE (EQ TO MAGNESIUM CHLORIDE 6H2… | 透析用液劑 | 連續性血液過濾或連續性血液透析過濾所使用的補充液,連續性血液透析或連續性血液透析過濾所使用之透析液。 |
| 衛署藥輸字第025387號 | 補利壽B0血液過濾及血液透析液 | MAGNESIUM CHLORIDE HEXAHYDRATE (EQ TO MAGNESIUM CHLORIDE 6H2… | 透析用液劑 | 連續性血液過濾或連續性血液透析過濾所使用的補充液,連續性血液透析或連續性血液透析過濾所使用之透析液。 |
| 衛署藥輸字第025388號 | 補利壽血液過濾及血液透析液 (2mmol/l鉀) | MAGNESIUM CHLORIDE HEXAHYDRATE (EQ TO MAGNESIUM CHLORIDE 6H2… | 透析用液劑 | 連續性血液過濾或連續性血液透析過濾所使用的補充液,連續性血液透析或連續性血液透析過濾所使用之透析液。 |

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-11-24）</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛署藥製字第048269號</td><td>健婦友液</td><td>LACTIC ACID</td><td>2026/09/25</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（14 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥輸字第001404號</td><td>表舒鳴</td><td>BIFIDOBACTERIUM、STREPTOCOCCUS FAECALIS、LACTIC ACID</td><td>1986/04/10</td></tr><tr><td>內衛藥輸字第002646號</td><td>乳鉀寧</td><td>POTASSIUM、LACTIC ACID</td><td>1986/10/20</td></tr><tr><td>內衛藥輸字第005381號</td><td>腹膜灌流液二號</td><td>CALCIUM CHLORIDE、MAGNESIUM CHLORIDE、LACTIC ACID、SODIUM CHLOR…</td><td>1985/06/24</td></tr><tr><td>內衛藥輸字第006168號</td><td>喜多納</td><td>CALCIUM LACTATE、METHIONINE DL-、AMINO ACID L-、THIAMINE (VITAM…</td><td>1986/03/01</td></tr><tr><td>衛署藥製字第002997號</td><td>寶兒康顆粒</td><td>NIACINAMIDE (NICOTINAMIDE)、PANTOTHENATE CALCIUM、PYRIDOXINE H…</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第012856號</td><td>蓋寧妥滴劑</td><td>HALOPERIDOL、LACTIC ACID</td><td>1999/08/23</td></tr><tr><td>衛署藥製字第027078號</td><td>複方乳酸鈉注射液</td><td>LACTIC ACID、SODIUM CHLORIDE、POTASSIUM CHLORIDE、CALCIUM CHLOR…</td><td>1987/09/14</td></tr><tr><td>衛署藥製字第047719號</td><td>立可潔婦女洗潔濃縮液</td><td>LACTIC ACID</td><td>2017/07/10</td></tr><tr><td>衛署藥輸字第005862號</td><td>乳酸８５－９０％</td><td>LACTIC ACID</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第009620號</td><td>體維素液</td><td>GLUCOSE、NIACINAMIDE (NICOTINAMIDE)、SORBITOL D- SOLUTION、PYRI…</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第014810號</td><td>喜多納內服液</td><td>AMINO ACID、METHIONINE DL-、ETHANOL ( EQ TO ETHYL ALCOHOL) (EQ…</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第016478號</td><td>洗腎液Ｄ—０１型</td><td>POTASSIUM CHLORIDE、MAGNESIUM CHLORIDE、SODIUM CHLORIDE、LACTIC…</td><td>1990/03/27</td></tr><tr><td>衛署藥輸字第017660號</td><td>洗腎液Ｄ—０１型</td><td>LACTIC ACID、SODIUM CHLORIDE、POTASSIUM CHLORIDE、ACETIC ACID、C…</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第025101號</td><td>立朵舒潔浴露</td><td>ATOMIZED LACTOSERUM (SPRAY DRIED LACTOSERUM)、LACTIC ACID</td><td>2018/07/03</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

**藥物交互作用：** 已查得 17 項交互作用紀錄，以中度與輕度為主。

- **中度：** Doxycycline、Tetracycline、Minocycline、Demeclocycline、Oxytetracycline、Acetylsalicylic acid、Salicylic acid (sodium)、Ephedrine、Pseudoephedrine
- **輕度：** Chlorpropamide、Tolazamide、Glipizide、Glyburide、Acetohexamide、Tolbutamide、Methotrexate

其他警語與禁忌資料，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，無臨床試驗，也無直接文獻支持。
- 主動脈縮窄是結構性先天缺陷，與乳酸之間無合理機轉。

**若要推進需要：**
- 補齊乳酸的作用機轉資料。
- 重新檢視 TxGNN 預測，優先評估機轉較合理的方向，例如陰道微生態相關適應症。
- 在確認機轉與臨床需求前，不建議投入資源於此預測。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯與英文原文）。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 一句話總結稱乳酸見於腸胃藥 | 更正（2026-11-25 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 預測理由稱乳酸有腸道輔助用途 | 加註（2026-11-25 修訂，前版保留於紀錄） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表「蓋寧妥滴劑」一列 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國仿單節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄（2026-11-20 修訂，前版保留於紀錄） | [ChEMBL CHEMBL1200559 (lactic acid): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1200559) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

