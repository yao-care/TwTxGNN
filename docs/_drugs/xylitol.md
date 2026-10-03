---
layout: default
title: Xylitol
parent: 僅模型預測 (L5)
nav_order: 286
evidence_level: L5
indication_count: 1
---

# Xylitol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Xylitol：從糖尿病代謝異常到腦膜炎球菌感染

## 一句話總結

Xylitol 原本用於糖尿病患者的醣類補充與代謝異常改善。
TxGNN 模型預測它可能對**腦膜炎球菌感染 (meningococcal infection)** 有效，
但目前缺乏臨床試驗和文獻支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 糖尿病代謝異常、醣類補充 |
| 預測新適應症 | 腦膜炎球菌感染 (meningococcal infection) |
| TxGNN 預測分數 | 99.66% |
| 證據等級 | 無臨床證據 |
| 台灣上市 | 有效許可證（xylitol 單方注射液 6 張、含 xylitol 複方輸注液 7 張） |
| 許可證數 | 117 張（有效單方 6／有效複方 7／已註銷 104） |
| 建議決策 | Wait for More Evidence |

<!-- review:begin xylitol-active-licenses-overview-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「台灣上市／僅 1 張有效許可證」。TFDA 資料集中 xylitol 單方注射液有 6 張未註銷（另有 7 張含 xylitol 的複方營養輸注液），不是只有 1 張。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end xylitol-active-licenses-overview-2026-10-03 -->

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Xylitol 是一種五碳糖醇，主要作為糖尿病患者的醣類補充劑使用，
其代謝途徑不依賴胰島素。知識圖譜中將其與腦膜炎球菌感染關聯的原因尚不明確，
可能需要進一步研究其潛在的抗菌或免疫調節特性。

值得注意的是，有研究顯示 xylitol 在口腔和鼻腔中具有抗菌作用，可能抑制細菌生物膜形成。
但這與腦膜炎球菌感染的直接關聯仍待釐清。

## 臨床試驗證據

目前未發現任何 Xylitol 用於腦膜炎球菌感染的臨床試驗。

## 文獻證據

目前未發現任何 Xylitol 用於腦膜炎球菌感染的相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Xylitol 的不重複許可證共 **117 張**：有效單方 6 張、有效複方 7 張、已註銷 104 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（6 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第009683號 | 可樂醣注射液５％ | 注射劑 | 杏林新生製藥股份有限公司 | 2028/05/11 | 糖尿病時醣類之代謝異常及補充 |
| 衛署藥製字第014354號 | "台裕"五碳糖注射液５％ | 注射劑 | 台裕化學製藥廠股份有限公司 | 2030/02/27 | 糖尿病之代謝異常及補充體液 |
| 衛署藥製字第039138號 | 可力醣注射液５％（五碳醣） | 注射劑 | 信東生技股份有限公司 | 2028/05/25 | 糖尿時之不正常代謝作用、醣類利用不良引起之血糖升高或糖尿症、由於水份或電解質代謝作用不良引起之脫水與休克現象、外傷刺激麻醉手術或手術後引起之不正常醣類代謝作用或迷睡疾病之熱能補充 |
| 衛署藥製字第039139號 | 可力醣注射液１０％（五碳醣） | 注射劑 | 信東生技股份有限公司 | 2028/05/25 | 糖尿時之不正常代謝作用、醣類利用不良引起之血糖升高或糖尿症、由於水份或電解質代謝不良引起之脫水與休克現象、外傷刺激麻醉手術或手術後引起之不正常醣類代謝作用或迷睡等疾病熱能之補充 |
| 衛署藥製字第040558號 | 克立注射液 | 注射劑 | 安星製藥股份有限公司 | 2029/05/25 | 糖尿病時代謝異常之營養補給 |
| 衛署藥製字第044066號 | "南光"其西力糖 注射液２０％　(五碳醣) | 注射劑 | 南光化學製藥股份有限公司 | 2030/10/27 | 糖尿病及外傷、麻醉、手術後糖代謝異常時之醣類補充。 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（7 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第011723號 | "信東" 胺美樂瑞注射液 | XYLITOL、L-ISOLEUCINE、L-THREONINE、L-PROLINE、L-PHENYLALANINE、L… | 注射劑 | 手術前後之營養補給、不能經口之補給營養及水分時 |
| 衛署藥製字第019962號 | "台裕 "綜胺酸五碳糖注射液 | L-TYROSINE、LYSINE L- HCL ( EQ TO L-LYSINE HCL)、L-ALANINE、L-T… | 注射劑 | 糖尿病患者或手術後糖利用障害需補充胺基酸及水份者經口服不能攝取營養及水份或手術前後營養補給 |
| 衛署藥製字第021883號 | "信東" 胺美樂舒注射液 | GLUTAMIC ACID L-、CYSTINE L-、L-SERINE、L-PROLINE、L-THREONINE、L… | 注射劑 | 不能攝取適當食物之患者補助治療劑、蛋白質之消化吸收機能及合成利用障礙、嚴重創傷、火傷、骨折時蛋白質之補給、蛋白攝取減少之營養失調症 |
| 衛署藥製字第023312號 | "南光" 安命活源注射液 | SODIUM HYDROXIDE、GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYC… | 注射劑 | 電解質失調、維他命缺乏、蛋白質缺乏等營養不良症狀 |
| 衛署藥製字第032498號 | 安命多－恩注射液 | L-TRYPTOPHAN、L-CYSTEINE HCL MONOHYDRATE、L-ALANINE、L-PHENYLAL… | 注射劑 | 蛋白質消化吸收障礙及其合成利用障礙、其他各種營養補給低蛋白血症 |
| 衛署藥製字第034067號 | 固力醣胺注射液 | LYSINE L- HCL ( EQ TO L-LYSINE HCL)、L-TRYPTOPHAN、ASPARTATE M… | 注射劑 | 手術前後的營養補給，不能經口攝取營養及水分的補給。 |
| 衛署藥製字第045035號 | "南光" 優安命注射液 3% | L-PHENYLALANINE、LYSINE L- HCL ( EQ TO L-LYSINE HCL)、L-ASPART… | 注射劑 | 手術前後之營養補給、低蛋白血症、消化道潰瘍、營養障礙之補給。 |

<details><summary><strong>已註銷</strong>（104 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第000705號</td><td>克力醣注射液２０％</td><td>XYLITOL</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第000706號</td><td>克力醣注射液５０％</td><td>XYLITOL</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第000707號</td><td>克力醣注射液３０％</td><td>XYLITOL</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第002321號</td><td>其西力醣注射液５％</td><td>XYLITOL</td><td>1993/03/11</td></tr><tr><td>內衛藥製字第002322號</td><td>其西力醣注射液１０％</td><td>XYLITOL</td><td>2013/10/03</td></tr><tr><td>內衛藥製字第003131號</td><td>吉爾通注射液５％</td><td>XYLITOL</td><td>2013/10/14</td></tr><tr><td>內衛藥製字第003132號</td><td>吉爾通注射液２０％</td><td>XYLITOL</td><td>2009/12/30</td></tr><tr><td>內衛藥製字第008046號</td><td>克力醣注射液１０％</td><td>XYLITOL</td><td>1995/11/23</td></tr><tr><td>內衛藥製字第008066號</td><td>克力醣注射液５％</td><td>XYLITOL</td><td>1995/11/23</td></tr><tr><td>內衛藥製字第015347號</td><td>宜糖注射液５％</td><td>XYLITOL</td><td>2016/09/08</td></tr><tr><td>內衛藥輸字第004165號</td><td>特美醣注射液５</td><td>XYLITOL</td><td>1990/12/05</td></tr><tr><td>內衛藥輸字第004671號</td><td>五炭醣５</td><td>XYLITOL</td><td>1988/11/08</td></tr><tr><td>內衛藥輸字第004672號</td><td>五炭醣１０</td><td>XYLITOL</td><td>1988/11/08</td></tr><tr><td>內衛藥輸字第005480號</td><td>基力糖２公克注射劑</td><td>XYLITOL</td><td>2010/09/21</td></tr><tr><td>內衛藥輸字第005780號</td><td>基力糖２５公克注射劑</td><td>XYLITOL</td><td>2010/09/21</td></tr><tr><td>內衛藥輸字第006919號</td><td>１０％康力得針</td><td>XYLITOL</td><td>1999/09/22</td></tr><tr><td>內衛藥輸字第007960號</td><td>可樂醣注射液１０％</td><td>XYLITOL</td><td>1994/02/01</td></tr><tr><td>衛署藥製字第004718號</td><td>適治醣注射液１０％</td><td>XYLITOL</td><td>2023/09/21</td></tr><tr><td>衛署藥製字第004753號</td><td>適治醣注射液５％</td><td>XYLITOL</td><td>2023/09/21</td></tr><tr><td>衛署藥製字第006572號</td><td>永安命舒注射液</td><td>L-METHIONINE、GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOL…</td><td>2023/10/02</td></tr><tr><td>衛署藥製字第006789號</td><td>祈立糖注射液５％</td><td>XYLITOL</td><td>1988/12/31</td></tr><tr><td>衛署藥製字第009505號</td><td>溫利醣注射液</td><td>XYLITOL</td><td></td></tr><tr><td>衛署藥製字第009676號</td><td>奇醣注射液</td><td>XYLITOL</td><td>1999/08/20</td></tr><tr><td>衛署藥製字第013964號</td><td>"壽元"五碳糖注射液</td><td>XYLITOL</td><td>2023/07/21</td></tr><tr><td>衛署藥製字第014700號</td><td>五碳糖注射液５％</td><td>XYLITOL</td><td>1997/02/12</td></tr><tr><td>衛署藥製字第016400號</td><td>能安命注射液</td><td>L-SERINE、L-ISOLEUCINE、LYSINE HCL、XYLITOL、L-LEUCINE、L-THREONI…</td><td>1989/12/31</td></tr><tr><td>衛署藥製字第020551號</td><td>五碳醣注射液</td><td>XYLITOL</td><td>1988/12/31</td></tr><tr><td>衛署藥製字第024557號</td><td>"壽元"西力安命注射液</td><td>L-SERINE、XYLITOL、L-ISOLEUCINE、L-LEUCINE、HISTIDINE L- HCL (EQ…</td><td>2023/07/21</td></tr><tr><td>衛署藥製字第029426號</td><td>能安命注射液</td><td>GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOLL)、ARGININE H…</td><td>1990/07/11</td></tr><tr><td>衛署藥製字第030627號</td><td>輸樂注射液２號</td><td>POTASSIUM PHOSPHATE MONOBASIC(EQ TO POTASSIUM BIPHOSPHATE)(E…</td><td>2013/10/03</td></tr><tr><td>衛署藥製字第035893號</td><td>"南光"其西力糖注射液５％（五碳醣）</td><td>XYLITOL</td><td>2023/07/03</td></tr><tr><td>衛署藥輸字第000254號</td><td>祈士得針劑５％</td><td>XYLITOL</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第000256號</td><td>祈士得針劑１０％</td><td>XYLITOL</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第000520號</td><td>代謝療糖注射液５％</td><td>XYLITOL</td><td>1985/06/24</td></tr><tr><td>衛署藥輸字第000598號</td><td>五碳糖</td><td>XYLITOL</td><td>1999/12/02</td></tr><tr><td>衛署藥輸字第001612號</td><td>固力醣胺注射液</td><td>L-SERINE、L-VALINE、LYSINE HCL、XYLITOL、CYSTEINE L- HCL (EQ TO…</td><td>1988/03/02</td></tr><tr><td>衛署藥輸字第002395號</td><td>可理醣</td><td>XYLITOL</td><td>1988/09/02</td></tr><tr><td>衛署藥輸字第002517號</td><td>百糖立舒注射液２０％</td><td>XYLITOL</td><td>1986/05/26</td></tr><tr><td>衛署藥輸字第003416號</td><td>卡羅里路靜脈滴注液</td><td>XYLITOL、FRUCTOSE (LAEVULOSE)</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第003522號</td><td>５％木糖醇注射液</td><td>XYLITOL</td><td>1985/11/22</td></tr><tr><td>衛署藥輸字第003657號</td><td>五炭醣注射液２０％</td><td>XYLITOL</td><td>1990/12/04</td></tr><tr><td>衛署藥輸字第003658號</td><td>五炭醣注射液１０％</td><td>XYLITOL</td><td>1990/12/04</td></tr><tr><td>衛署藥輸字第003679號</td><td>五炭醣注射液５％</td><td>XYLITOL</td><td>1990/12/04</td></tr><tr><td>衛署藥輸字第003698號</td><td>保體安民注射液</td><td>L-SERINE、NITROGEN、CYSTINE L-、SODIUM CITRATE (SODIUM CITRATE…</td><td>1988/04/02</td></tr><tr><td>衛署藥輸字第004389號</td><td>壽爾明靜脈注射液</td><td>L-SERINE、SODIUM ION、NITROGEN、ACETATE、GLUTAMIC ACID L-、LYSINE…</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第004428號</td><td>蒙諾安敏注射液</td><td>SODIUM ION、INOSITOL (MESO-INOSITOL)、ACETATE、L-LEUCINE、MALIC…</td><td>1987/03/24</td></tr><tr><td>衛署藥輸字第004651號</td><td>可喜得利注射液</td><td>XYLITOL</td><td>1986/05/12</td></tr><tr><td>衛署藥輸字第004662號</td><td>木糖醇無熱原</td><td>XYLITOL</td><td>1990/04/11</td></tr><tr><td>衛署藥輸字第005301號</td><td>保體安民濃氨基酸注射液</td><td>L-PROLINE、L-THREONINE、L-TYROSINE、HISTIDINE L- HCL (EQ TO L-H…</td><td>1988/03/16</td></tr><tr><td>衛署藥輸字第005608號</td><td>喜加力五碳糖５Ｗ/Ｖ％注射液</td><td>XYLITOL</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第006984號</td><td>五碳糖</td><td>XYLITOL</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第007235號</td><td>五碳醣注射液５Ｗ/Ｖ％</td><td>XYLITOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第008010號</td><td>木糖醇</td><td>XYLITOL D-</td><td>2014/01/28</td></tr><tr><td>衛署藥輸字第008050號</td><td>德泰固命注射液</td><td>GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOLL)、ASPARTATE…</td><td>1990/02/26</td></tr><tr><td>衛署藥輸字第008051號</td><td>德泰復生注射液</td><td>ARGININE HCL L-、PANTHENOL、L-ARGININE、NIACINAMIDE (NICOTINAMI…</td><td>1990/02/26</td></tr><tr><td>衛署藥輸字第008052號</td><td>德泰利多注射液</td><td>ORNITHINE L- ASPARTATE L-、SODIUM CHLORIDE、CYANOCOBALAMIN (VI…</td><td>1988/01/28</td></tr><tr><td>衛署藥輸字第008053號</td><td>德泰安命注射液</td><td>CYSTINE L-、GLUTAMIC ACID L-、SODIUM CARBONATE MONOHYDRATE、SOR…</td><td>1990/02/26</td></tr><tr><td>衛署藥輸字第008054號</td><td>德泰氨美注射液</td><td>L-ARGININE、NIACINAMIDE (NICOTINAMIDE)、PANTHENOL、L-TRYPTOPHAN…</td><td>1990/02/26</td></tr><tr><td>衛署藥輸字第008286號</td><td>德泰固心注射液</td><td>ASPARTATE MAGNESIUM DL- 4H2O、EDETATE DISODIUM DIHYDRATE (EQ…</td><td>1988/08/05</td></tr><tr><td>衛署藥輸字第008362號</td><td>氨基酸電解質糖類點滴注射液</td><td>L-ARGININE、L-TYROSINE、L-ASPARTIC ACID、LYSINE L- HCL ( EQ TO…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第008421號</td><td>德士糖注射液５％</td><td>XYLITOL</td><td>1987/12/22</td></tr><tr><td>衛署藥輸字第008477號</td><td>安美若胖得注射液２．５％</td><td>XYLITOL、L-HISTIDINE、L-ISOLEUCINE、L-LEUCINE、TYROSINE L-(N-ACE…</td><td>1997/11/22</td></tr><tr><td>衛署藥輸字第009068號</td><td>能使安寧注射液</td><td>L-VALINE、ASPARTATE SODIUM L-、L-PHENYLALANINE、L-LEUCINE、L-ALA…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第009094號</td><td>輸樂注射液（開始液）</td><td>SODIUM ACETATE、XYLITOL、SODIUM CHLORIDE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第009096號</td><td>輸樂注射液（維持液）</td><td>SODIUM ACETATE、POTASSIUM CHLORIDE、MAGNESIUM CHLORIDE、XYLITOL…</td><td>1988/06/16</td></tr><tr><td>衛署藥輸字第009281號</td><td>其士得注射液</td><td>XYLITOL</td><td>1988/04/30</td></tr><tr><td>衛署藥輸字第009917號</td><td>基實寧糖１０％注射液</td><td>XYLITOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第009922號</td><td>基實寧糖２０％注射液</td><td>XYLITOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第009967號</td><td>基實寧糖５％注射液</td><td>XYLITOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第010402號</td><td>舒補胺基注射液</td><td>L-LEUCINE、HISTIDINE L- HCL (EQ TO L-HISTIDINE HYDROCHLORIDE)…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第010920號</td><td>１２％喜加力安命－愛克注射液</td><td>L-SERINE、GLUTAMIC ACID L-、CYSTINE L-、L-THREONINE、L-PROLINE、L…</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第010925號</td><td>３％喜加力安命－愛克注射液</td><td>GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOLL)、L-METHIONI…</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第011503號</td><td>阿美諾愛克斯注射液</td><td>L-PROLINE、L-THREONINE、L-ISOLEUCINE、LYSINE HCL、L-LEUCINE、XYLI…</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第011982號</td><td>康脈得注射液</td><td>L-ISOLEUCINE、L-VALINE、POTASSIUM CHLORIDE、L-PHENYLALANINE、L-A…</td><td>1988/01/18</td></tr><tr><td>衛署藥輸字第012002號</td><td>喜加力安命－愛克注射液１２％</td><td>GLUTAMIC ACID L-、CYSTINE L-、L-SERINE、XYLITOL、L-ISOLEUCINE、HI…</td><td>1988/04/11</td></tr><tr><td>衛署藥輸字第012005號</td><td>喜加力安命－愛克注射液３％</td><td>L-SERINE、GLUTAMIC ACID L-、CYSTINE L-、L-ISOLEUCINE、L-LEUCINE、…</td><td>1988/04/11</td></tr><tr><td>衛署藥輸字第012088號</td><td>喜巴胺美舒注射液</td><td>ASPARTATE ZINC-BIS HYDROGEN DL-、EACH SOLVENT CONTAINS、L-ISOL…</td><td>1988/03/21</td></tr><tr><td>衛署藥輸字第014380號</td><td>５％木糖醇注射液</td><td>XYLITOL</td><td>2002/12/20</td></tr><tr><td>衛署藥輸字第014843號</td><td>固力醣鹽－二號注射液</td><td>MAGNESIUM CHLORIDE、SODIUM ACETATE、SODIUM CHLORIDE、POTASSIUM…</td><td>1988/03/25</td></tr><tr><td>衛署藥輸字第014844號</td><td>固力醣鹽－一號注射液</td><td>SODIUM ACETATE、SODIUM CHLORIDE、XYLITOL</td><td>1988/03/01</td></tr><tr><td>衛署藥輸字第015075號</td><td>安命納精注射液５％</td><td>L-METHIONINE、SODIUM HYDROXIDE、GLYCINE (EQ TO AMINOACETIC ACI…</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第015662號</td><td>安命注射液６００卡路里</td><td>NIACINAMIDE (NICOTINAMIDE)、L-ALANINE、L-TRYPTOPHAN、GLYCINE (E…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第015663號</td><td>安命注射液</td><td>L-TRYPTOPHAN、L-ALANINE、POTASSIUM HYDROXIDE、LYSINE L- HCL ( E…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第015894號</td><td>營全注射液３．５％</td><td>GLUTAMIC ACID L-、SODIUM GLYCEROPHOSPHATE 5H2O、MONOSODIUM GLU…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第016125號</td><td>德士糖注射液５％</td><td>XYLITOL</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第016134號</td><td>康脈得注射液</td><td>L-VALINE、HISTIDINE L- HCL (EQ TO L-HISTIDINE HYDROCHLORIDE)、…</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第016254號</td><td>喜巴胺美舒注射液</td><td>POTASSIUM CARBONATE、INOSITOL (MESO-INOSITOL)、SORBITOL、GLUTAM…</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第016288號</td><td>固力醣鹽一號注射液</td><td>SODIUM ACETATE、XYLITOL、SODIUM CHLORIDE</td><td>1998/09/16</td></tr><tr><td>衛署藥輸字第016300號</td><td>固力醣胺注射液</td><td>SODIUM GLUTAMATE L-、L-LEUCINE、LYSINE HCL、L-ISOLEUCINE、L-PROL…</td><td>1992/08/13</td></tr><tr><td>衛署藥輸字第016337號</td><td>保體安民注射液</td><td>L-ASPARTIC ACID、LYSINE L- HCL ( EQ TO L-LYSINE HCL)、L-PHENYL…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第016342號</td><td>保體安民濃氨基酸注射液</td><td>XYLITOL、L-ISOLEUCINE、L-PROLINE、L-THREONINE、ELECTROLYTE、L-SER…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第016411號</td><td>固力醣鹽二號注射液</td><td>XYLITOL、SODIUM CHLORIDE、POTASSIUM PHOSPHATE MONOBASIC(EQ TO…</td><td>1998/09/16</td></tr><tr><td>衛署藥輸字第016433號</td><td>喜加力安命－愛克注射液３％</td><td>CYSTINE L-、GLUTAMIC ACID L-、L-SERINE、HISTIDINE L- HCL (EQ TO…</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第016437號</td><td>喜加力安命－愛克注射液１２％</td><td>XYLITOL、L-ISOLEUCINE、LYSINE HCL、L-VALINE、L-THREONINE、L-PROLI…</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第016506號</td><td>其士得注射液</td><td>XYLITOL</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第017489號</td><td>愛克依注射液</td><td>SODIUM CHLORIDE、SORBITOL、SODIUM ACETATE TRIHYDRATE (EQ TO SO…</td><td>1995/06/16</td></tr><tr><td>衛署藥輸字第017704號</td><td>德泰氨美注射液</td><td>XYLITOL、THIAMINE HYDROCHLORIDE、RIBOFLAVIN PHOSPHATE SODIUM、L…</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第017706號</td><td>德泰固命注射液</td><td>SODIUM CHLORIDE、GLUTAMIC ACID L-、SORBITOL、INOSITOL (MESO-INO…</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第017726號</td><td>德泰安命注射液</td><td>L-ARGININE、L-TYROSINE、L-TRYPTOPHAN、MAGNESIUM CHLORIDE、PYRIDO…</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第017727號</td><td>德泰復生注射液</td><td>CYANOCOBALAMIN (VIT B12)、ORNITHINE L- ASPARTATE L-、GLUTAMIC…</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第020814號</td><td>喜加力安命－愛克注射液３％</td><td>L-SERINE、GLUTAMIC ACID L-、CYSTINE L-、XYLITOL、L-ISOLEUCINE、L-…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第020885號</td><td>愛克依注射液</td><td>GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO GLYCOCOLL)、POTASSIUM…</td><td>2004/10/26</td></tr><tr><td>衛署藥輸字第020983號</td><td>木糖醇〝羅貴特〞</td><td>XYLITOL</td><td>2014/01/24</td></tr><tr><td>衛署藥輸字第022505號</td><td>木糖醇〝東和〞</td><td>XYLITOL</td><td>2014/01/24</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

## 安全性考量

- **藥物交互作用**：目前資料庫中未發現已知的藥物交互作用記錄。
- **警語與禁忌**：未檢索到詳細仿單資訊。

## 結論與下一步

**決策：Wait for More Evidence**

**理由：**
Xylitol 與腦膜炎球菌感染之間的關聯缺乏任何臨床試驗或文獻支持。
預測分數雖高 (99.66%)，但排名較低 (7287)，且缺乏機轉上的合理解釋。

**若要推進需要：**
- 基礎研究確認 Xylitol 的抗菌或免疫調節機轉
- 體外或動物模型研究驗證對腦膜炎球菌的抑制效果
- 進一步了解知識圖譜中此預測的推論路徑

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 快速總覽「僅 1 張有效許可證」 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 台灣上市資訊「僅剩 1 張仍有效」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

