---
layout: default
title: Dehydrocholic Acid
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 10
---

# Dehydrocholic Acid
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

# Dehydrocholic Acid (去氫膽酸) - 藥師評估報告

## 一句話總結

Dehydrocholic acid 是一種傳統利膽劑，TxGNN 預測其可能對膽道疾病和腎結石有潛在療效，但這些預測與其原有膽道適應症高度重疊，缺乏真正的新適應症發現價值。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Dehydrocholic acid (去氫膽酸/脫氫膽酸) |
| DrugBank ID | DB11622 |
| 台灣商品名 | 得利膽錠、派頓去氫膽酸錠 |
| 原適應症 | 利膽劑、膽石症、膽囊炎、膽道炎、肝硬化、黃疸 |
| 預測新適應症 | 急性尿酸腎病、腎結石、膽道疾病、膽管腫瘤 |
| 最高 TxGNN 分數 | 0.9999 (急性尿酸腎病) |
| 臨床試驗支持 | 無 |
| 文獻支持 | 部分 (膽道疾病相關) |

## 為什麼預測合理

### 機轉分析

1. **膽道疾病 (bile duct disease)**：TxGNN 分數 0.9999，但這與藥物原有的利膽適應症完全重疊，不具新藥再利用價值。

2. **腎結石 (nephrolithiasis)**：TxGNN 分數 0.9999。理論上，dehydrocholic acid 可增加膽汁流動，可能影響膽固醇和膽鹽代謝，間接影響某些類型結石的形成。但目前無直接機轉證據支持其用於腎結石治療。

3. **急性尿酸腎病 (acute urate nephropathy)**：TxGNN 分數最高 (0.9999)，但無任何文獻或臨床試驗支持，機轉連結薄弱。

### 預測品質評估

- 預測多集中於膽道相關疾病，與原適應症高度重疊
- 新預測適應症（如尿酸腎病、牙周炎）缺乏機轉支持
- 整體而言，此藥物的老藥新用潛力有限

## 臨床試驗

**無相關臨床試驗**

目前 ClinicalTrials.gov 和 WHO ICTRP 均未發現 dehydrocholic acid 用於預測新適應症的臨床試驗。

## 文獻證據

### 膽道疾病相關文獻

1. **Ratan J et al. (1997)** - Tohoku J Exp Med
   - 比較 Livzon 和 dehydrocholic acid 在阻塞性黃疸大鼠模型中的保肝和利膽作用
   - 結論：Dehydrocholic acid 主要表現利膽作用

2. **Sakai Y et al. (2008)** - Hepato-gastroenterology
   - 研究 dehydrocholic acid 在 MRCP 檢查中增強膽道顯影的潛在用途

3. **Martinez-Gili L et al. (2023)** - Gut Microbes
   - 研究原發性膽道膽汁淤積症患者對 UDCA 治療反應不佳的細菌和代謝表型
   - dehydrocholic acid 作為相關代謝物被提及

### 腎結石相關文獻

- **Fletcher DL et al. (1967)** - J Can Assoc Radiol
  - 僅為影像診斷相關報告，非治療研究

## 台灣上市狀態

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Dehydrocholic Acid 的不重複許可證共 **105 張**：有效單方 3 張、有效複方 15 張、已註銷 87 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（3 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第014319號 | "派頓"去氫膽酸錠 | 錠劑 | 臺灣派頓化學製藥股份有限公司 | 2028/05/25 | 膽石症、膽石形成之預防、膽石膽砂之排除、膽囊炎、膽管炎膽汁分泌不全所致之疾患、肝硬化、黃疸 |
| 衛署藥製字第048938號 | 欣肝膽錠250毫克(去氫膽酸) | 錠劑 | 興南實業股份有限公司 | 2027/08/09 | 膽石症、預防膽石症、助長維他命之吸收。 |
| 衛署藥輸字第024606號 | 脫氫膽酸 | （粉） | 新雙隆生技股份有限公司 | 2032/01/30 | 利膽劑。 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（15 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 內衛藥製字第000051號 | 利肝能糖衣錠 | DEHYDROCHOLIC ACID、NIACINAMIDE (NICOTINAMIDE)、PANTOTHENATE C… | 糖衣錠 | 急慢性肝炎、黃疸、脂肪肝、肝硬變、肝性昏睡等之預防、妊娠惡阻、藥物及食物中毒、濕疹、皮膚炎、動脈硬化之預防、營養障礙、食慾不振、神經痛、神經炎、腳氣、乳幼兒之促進發育、消除疲勞等 |
| 內衛藥製字第002608號 | 護肝好糖衣錠 | NIACINAMIDE (NICOTINAMIDE)、THIOCTIC ACID AMIDE (THIOCTAMIDE)… | 糖衣錠 | 肝臟疾病（黃疸、膽道炎、膽囊炎、膽囊之膽汁分泌不全）之預防及治療疲勞、食慾不振、宿醉、酒精中毒 |
| 內衛藥製字第005291號 | "田邊"胃腸藥顆粒 | GENTIAN EXT、SCOPOLIA EXTRACT、CLOVE OIL、CINNAMON (CINNAMON CO… | 內服顆粒劑 | 健胃消化劑、胃痛、腸內異常醱酵、食物中毒、其他因消化不良所引起之胃腸病 |
| 內衛藥製字第007522號 | "明通"悠久樂胃腸藥散 | ALUMINUM HYDROXIDE GEL、CALCIUM CARBONATE、DEHYDROCHOLIC ACID、… | 散劑 | 急、慢性胃腸炎、消化不良、胃痛、胃酸過多 |
| 衛署藥製字第001676號 | "明通"悠久樂胃腸藥顆粒 | SCOPOLIA EXTRACT、SODIUM BICARBONATE ( EQ TO SODIUM HYDROGEN… | 內服顆粒劑 | 急慢性胃腸炎、胃痛、胃酸過多 |
| 衛署藥製字第001996號 | 杏力健糖衣錠 | INOSITOL (MESO-INOSITOL)、THIAMINE MONONITRATE、ASCORBIC ACID… | 糖衣錠 | 皮膚疾患，維生素B、C缺乏症，消除疲勞。 |
| 衛署藥製字第003653號 | 洛肝達錠 | METHIONINE、NIACINAMIDE (NICOTINAMIDE)、DEHYDROCHOLIC ACID | 錠劑 | 利膽（肝臟機能不全、膽囊炎、膽道炎、膽汁阻塞等促進膽汁分泌） |
| 衛署藥製字第020819號 | 祝可定糖衣錠 | THIAMINE MONONITRATE、ASCORBIC ACID (VIT C)、THIOCTIC ACID (VI… | 糖衣錠 | 病中病後之營養補助、虛弱體質之改善。 |
| 衛署藥製字第022502號 | "派頓"肝胃腸顆粒 | OX BILE EXTRACT、DRIED ALUMINUM HYDROXIDE GEL、SCOPOLIA EXTRAC… | 內服顆粒劑 | 急慢性胃腸炎、消化不良、胃痛、腹痛、胃酸過多、膽囊炎、黃疸 |
| 衛署藥製字第027471號 | 〝正和〞滋爾肝糖衣錠 | CYANOCOBALAMIN (VIT B12)、INOSITOL (MESO-INOSITOL)、THIAMINE M… | 糖衣錠 | 消除疲勞、病後恢復期、妊產、授乳婦之營養補給、虛弱體質之改善、維生素缺乏症。 |
| 衛署藥製字第029359號 | "田邊"胃腸藥優錠 | VITAMIN U (METHYLMETHIONINE SULFONIUM CHLORIDE)、HISTIDINE L-… | 錠劑 | 胃痛、胃酸過多、胃灼熱感、打嗝、胸悶、胃部停滯感、胃部膨滿感、噁心、嘔吐、食慾不振、消化不良 |
| 衛署藥製字第032859號 | 得痢寧膠囊 | GENTIAN EXT、DIPHENYLPYRALINE HCL、BERBERINE CHLORIDE、ANACOLIN… | 膠囊劑 | 暫時緩解輕微或中度急性腹瀉 |
| 衛署藥製字第037653號 | 田邊胃保錠 | ATRACTYLODES LANCEA RHIZOME、LIPASE、BIODIASTASE、CINNAMON CORT… | 錠劑 | 緩解胃部不適或灼熱感、或經診斷為胃及十二指腸潰瘍、胃炎、食道炎所伴隨之胃酸過多、食慾不振、胃腹部膨脹感、消化不良、幫助消化。 |
| 衛署藥製字第041904號 | “新喜”治益肝糖衣錠 | CYANOCOBALAMIN (VIT B12)、THIAMINE MONONITRATE、THIOCTIC ACID… | 糖衣錠 | 病後恢復期、妊產授乳婦之營養補給、維他命Ｂ複合體缺乏症 |
| 衛署藥製字第045675號 | 理研胃腸藥三層錠 | DEHYDROCHOLIC ACID、BIODIASTASE、SYNTHETIC HYDROTALCITE、SCOPOL… | 錠劑 | 胃痛、胃酸過多、消化不良、食慾不振、腹部脹氣。 |

<details><summary><strong>已註銷</strong>（87 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第001787號</td><td>強克朗糖衣錠</td><td>PYRIDOXINE HCL、OROTIC ACID (VIT B13)、RIBOFLAVIN (VIT B2)、PAN…</td><td>2013/10/11</td></tr><tr><td>內衛藥製字第002171號</td><td>硫克肝糖衣錠</td><td>DEHYDROCHOLIC ACID、PANTOTHENATE CALCIUM、OROTIC ACID (VIT B13…</td><td>1989/11/03</td></tr><tr><td>內衛藥製字第003248號</td><td>膽源錠</td><td>DEHYDROCHOLIC ACID、CURCUMA</td><td>2023/07/04</td></tr><tr><td>內衛藥製字第004206號</td><td>得利膽錠</td><td>DEHYDROCHOLIC ACID</td><td>2016/09/19</td></tr><tr><td>內衛藥製字第005645號</td><td>"田邊"胃腸藥錠</td><td>CALCIUM CARBONATE、FENNEL OIL、MAGNESIUM ALUMINUM METASILICATE…</td><td>2023/07/19</td></tr><tr><td>內衛藥製字第006876號</td><td>綠胃片</td><td>BENACTYZINE HCL、CHLOROPHYLL SODIUM COPPER、SCOPOLIA EXTRACT、D…</td><td>1998/06/01</td></tr><tr><td>內衛藥製字第008739號</td><td>利膽肝糖衣錠</td><td>RIBOFLAVIN (VIT B2)、NIACINAMIDE (NICOTINAMIDE)、OROTIC ACID (…</td><td>1989/11/21</td></tr><tr><td>內衛藥製字第011048號</td><td>刻顧淳錠</td><td>DEHYDROCHOLIC ACID、METHIONINE、NIACINAMIDE (NICOTINAMIDE)</td><td>2010/02/08</td></tr><tr><td>內衛藥製字第014437號</td><td>"人生"維力肝糖衣錠</td><td>Calcium Pantothenate、PYRIDOXINE HCL、OROTIC ACID (VIT B13)、NI…</td><td>2017/03/07</td></tr><tr><td>內衛藥製字第016659號</td><td>"應元"脫氫膽酸鈉注射液</td><td>DEHYDROCHOLIC ACID</td><td>2024/04/19</td></tr><tr><td>內衛藥輸字第000623號</td><td>脫氫膽酸（注射用）</td><td>DEHYDROCHOLIC ACID</td><td>1984/08/29</td></tr><tr><td>內衛藥輸字第001704號</td><td>得海可利酸</td><td>DEHYDROCHOLIC ACID</td><td>1985/09/13</td></tr><tr><td>內衛藥輸字第001758號</td><td>拉瑪加路</td><td>THIAMINE (VITAMIN B1)、DEHYDROCHOLATE SODIUM、TABLET CORE(CORE…</td><td>1988/10/29</td></tr><tr><td>內衛藥輸字第002380號</td><td>復膽利</td><td>DEHYDROCHOLIC ACID、DEHYDRODEOXYCHOLIC ACID</td><td>1985/08/22</td></tr><tr><td>內衛藥輸字第002505號</td><td>家樂兒－Ｓ片</td><td>DEHYDROCHOLIC ACID、PANTOTHENATE CALCIUM、LILAC BASE、BILE, OX…</td><td>1999/10/25</td></tr><tr><td>內衛藥輸字第003355號</td><td>愛爾體</td><td>VITAMIN A、LINOLEATE CALCIUM、LECITHIN(LECITHOL)、CHOLINE BITAR…</td><td>1990/09/13</td></tr><tr><td>內衛藥輸字第003397號</td><td>養健片</td><td>ASCORBIC ACID (VIT C)、CYANOCOBALAMIN (VIT B12)、THIOCTIC ACID…</td><td>1990/09/13</td></tr><tr><td>內衛藥輸字第003803號</td><td>腹痛錠</td><td>BERBERINE TANNATE、BENZOCAINE (ETHYL AMINOBENZOATE)、SCOPOLIA…</td><td>1990/09/13</td></tr><tr><td>內衛藥輸字第004842號</td><td>強力施度Ｐ錠</td><td>BIOTAMYLASE、AMOMI SEMEN POWDER、GINGER POWDER、PANCREATIN (DIA…</td><td>1990/08/13</td></tr><tr><td>內衛藥輸字第004857號</td><td>脫氫膽酸</td><td>DEHYDROCHOLIC ACID</td><td>1985/08/22</td></tr><tr><td>內衛藥輸字第005217號</td><td>樂朗片</td><td>LIPASE、NIACINAMIDE (NICOTINAMIDE)、DEHYDROCHOLIC ACID、GLUCURO…</td><td>1986/01/17</td></tr><tr><td>內衛藥輸字第005287號</td><td>胃可朗</td><td>BENACTYZINE HCL、SODIUM BICARBONATE ( EQ TO SODIUM HYDROGEN C…</td><td>1991/02/01</td></tr><tr><td>內衛藥輸字第005290號</td><td>得利膽１０％針</td><td>DEHYDROCHOLATE SODIUM</td><td>2004/12/23</td></tr><tr><td>內衛藥輸字第005649號</td><td>去氫膽汁酸</td><td>DEHYDROCHOLIC ACID</td><td>1985/07/10</td></tr><tr><td>內衛藥輸字第006024號</td><td>酵母源</td><td>PROTASE (PROTEOLYTIC ENZYME)、AMYLOLYTIC ENZYME、HYOSCYAMINE H…</td><td>1999/09/22</td></tr><tr><td>內衛藥輸字第006445號</td><td>亞路百朗</td><td>PANTOTHENATE CALCIUM、GLYCINE (EQ TO AMINOACETIC ACID)(EQ TO…</td><td>1987/04/08</td></tr><tr><td>內衛藥輸字第007201號</td><td>脫氫膽酸注射用</td><td>DEHYDROCHOLIC ACID</td><td>1987/05/01</td></tr><tr><td>衛署藥製字第001254號</td><td>敵克膽錠</td><td>DEHYDROCHOLIC ACID</td><td>1999/06/21</td></tr><tr><td>衛署藥製字第004375號</td><td>致可能糖衣錠</td><td>RIBOFLAVIN (VIT B2)、DEHYDROCHOLIC ACID、NIACINAMIDE (NICOTINA…</td><td>2023/09/05</td></tr><tr><td>衛署藥製字第004847號</td><td>醫利肝糖衣錠</td><td>PANTOTHENATE CALCIUM、THIAMINE NITRATE、RIBOFLAVIN (VIT B2)、OR…</td><td>1998/11/10</td></tr><tr><td>衛署藥製字第005673號</td><td>利補肝糖衣錠</td><td>PANTOTHENATE CALCIUM、METHIONINE DL-、PYRIDOXINE HCL、OROTIC AC…</td><td>2016/09/08</td></tr><tr><td>衛署藥製字第006366號</td><td>"全群"立保肝糖衣錠</td><td>RIBOFLAVIN (VIT B2)、OROTIC ACID (VIT B13)、DEHYDROCHOLIC ACID…</td><td>2023/07/04</td></tr><tr><td>衛署藥製字第006561號</td><td>“龍德”活力養糖衣錠</td><td>OROTIC ACID (VIT B13)、RIBOFLAVIN (VIT B2)、NIACINAMIDE (NICOT…</td><td>2017/08/24</td></tr><tr><td>衛署藥製字第006817號</td><td>維干能糖衣錠</td><td>PANTOTHENATE CALCIUM、NIACINAMIDE (NICOTINAMIDE)、DEHYDROCHOLI…</td><td>2015/06/18</td></tr><tr><td>衛署藥製字第008945號</td><td>喜露克勞糖衣錠</td><td>DEHYDROCHOLIC ACID</td><td>2013/10/07</td></tr><tr><td>衛署藥製字第009062號</td><td>溫喜肝錠</td><td>PHENOBARBITAL、HOMATROPINE METHYLBROMIDE、DEHYDROCHOLIC ACID</td><td>2006/04/19</td></tr><tr><td>衛署藥製字第009140號</td><td>溫喜肝注射液</td><td>DEHYDROCHOLATE SODIUM</td><td>2006/04/19</td></tr><tr><td>衛署藥製字第013473號</td><td>明理肝糖衣錠</td><td>OROTIC ACID (VIT B13)、RIBOFLAVIN (VIT B2)、NIACINAMIDE (NICOT…</td><td>2013/10/15</td></tr><tr><td>衛署藥製字第017010號</td><td>愛肝糖衣錠</td><td>THIAMINE MONONITRATE、INOSITOL (MESO-INOSITOL)、CYANOCOBALAMIN…</td><td>1992/02/10</td></tr><tr><td>衛署藥製字第017706號</td><td>滋補克康糖衣錠</td><td>OROTIC ACID (VIT B13)、PYRIDOXINE HCL、NIACINAMIDE (NICOTINAMI…</td><td>2013/10/11</td></tr><tr><td>衛署藥製字第022172號</td><td>保膽清錠（去氫膽酸）</td><td>DEHYDROCHOLIC ACID</td><td>2013/10/15</td></tr><tr><td>衛署藥製字第025951號</td><td>康達速膠囊</td><td>ASCORBIC ACID (VIT C)、THIAMINE HYDROCHLORIDE、CHOLINE BITARTR…</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第026300號</td><td>安胃樂錠</td><td>BENZOCAINE (ETHYL AMINOBENZOATE)、TAURINE (EQ TO AMINOETHYL S…</td><td>2023/07/05</td></tr><tr><td>衛署藥製字第033503號</td><td>可樂秘膠囊</td><td>DIOCTYL SODIUM SULFOSUCCINATE(AEROSOL OT)、DEHYDROCHOLIC ACID…</td><td>2007/11/05</td></tr><tr><td>衛署藥製字第034135號</td><td>懷舒錠</td><td>ANACOLIN、SWERTIAE HERBA POWDER ( POWDERED SWERTIA HERB)、OROT…</td><td>2017/02/06</td></tr><tr><td>衛署藥製字第034295號</td><td>愛肝糖衣錠</td><td>CYANOCOBALAMIN (VIT B12)、ASCORBIC ACID (VIT C)、THIAMINE MONO…</td><td>2014/01/03</td></tr><tr><td>衛署藥製字第041909號</td><td>綠胃錠</td><td>MANGANESE CARBONATE、DEHYDROCHOLIC ACID、ALUMINUM HYDROXIDE DR…</td><td>2010/11/18</td></tr><tr><td>衛署藥製字第044842號</td><td>"亞培" 健得生膜衣錠</td><td>CHOLINE DIHYDROGEN CITRATE、NICOTINAMIDE、THIAMINE HYDROCHLORI…</td><td>2024/04/29</td></tr><tr><td>衛署藥製字第055302號</td><td>益肝寶軟膠囊</td><td>DEHYDROCHOLIC ACID、PYRIDOXINE HCL、METHIONINE DL-、RIBOFLAVIN…</td><td>2023/07/07</td></tr><tr><td>衛署藥輸字第000300號</td><td>妙胃舒錠</td><td>SANALMINE、SODIUM BICARBONATE ( EQ TO SODIUM HYDROGEN CARBONA…</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第000420號</td><td>脫氫膽汁酸</td><td>DEHYDROCHOLIC ACID</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第000696號</td><td>脫氫膽酸</td><td>DEHYDROCHOLIC ACID</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第000707號</td><td>無水膽酸</td><td>DEHYDROCHOLIC ACID</td><td>1993/02/16</td></tr><tr><td>衛署藥輸字第001787號</td><td>胃腸藥三層錠</td><td>DIASTASE BIO-、DEHYDROCHOLIC ACID、SODIUM BICARBONATE ( EQ TO…</td><td>1993/03/19</td></tr><tr><td>衛署藥輸字第001979號</td><td>聖萊因－Ｇ末</td><td>ALUMINUM SILICATE、BENACTYZINE METHOBROMIDE (BENACTYZINE METH…</td><td>1988/11/08</td></tr><tr><td>衛署藥輸字第004952號</td><td>補肚必寧錠</td><td>BERBERINE HCL、BENACTYZINE HCL、ETHACRIDINE LACTATE MONOHYDRAT…</td><td>1987/04/08</td></tr><tr><td>衛署藥輸字第007840號</td><td>胃可舒錠</td><td>AMYLASE、DEHYDROCHOLIC ACID、PANTOTHENATE CALCIUM、CALCIUM CARB…</td><td>1987/09/01</td></tr><tr><td>衛署藥輸字第008643號</td><td>胃恩膠囊</td><td>CELLULASE、METOCLOPRAMIDE HCL MONOHYDRATE、PEPSIN、DIMETHICONE…</td><td>1986/07/10</td></tr><tr><td>衛署藥輸字第008978號</td><td>懷舒顆粒</td><td>HOP EXTRACT、OROTIC ACID (VIT B13)、MAGNESIUM ALUMINUM METASIL…</td><td>1992/06/18</td></tr><tr><td>衛署藥輸字第008980號</td><td>得痢寧膠囊</td><td>GENTIAN EXT、ALUMINUM SILICATE、BERBERINE、DEHYDROCHOLIC ACID、A…</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第009046號</td><td>肝必舒錠</td><td>SODIUM ASCORBATE、BIOTAMYLASE、CYANOCOBALAMIN (VIT B12)、DIISOP…</td><td>1992/06/24</td></tr><tr><td>衛署藥輸字第009083號</td><td>懷舒錠</td><td>PHELLODENDRON、ALUMINUM MAGNESIUM SILICATE、ANACOLIN、DEHYDROCH…</td><td>1992/07/14</td></tr><tr><td>衛署藥輸字第009733號</td><td>達羅明顆粒</td><td>DEHYDROCHOLIC ACID、CINNAMON OIL (OLEUM CINNAMOMI)、FENNEL OIL…</td><td>1986/01/21</td></tr><tr><td>衛署藥輸字第009744號</td><td>普樂喜糖衣錠</td><td>METOCLOPRAMIDE HCL、DIMETHICONE (EQ TO DIMETHYLPOLYSILOXANE O…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第009870號</td><td>力美肝軟膠囊</td><td>INOSITOL (MESO-INOSITOL)、CYANOCOBALAMIN (VIT B12)、THIAMINE M…</td><td>2019/04/26</td></tr><tr><td>衛署藥輸字第010138號</td><td>膽胃欣－抗痙膜衣錠</td><td>DEHYDROCHOLIC ACID、AMYLASE、CURCUM RHIZOMA EXTRACT、LIPASE、PAN…</td><td>1995/05/12</td></tr><tr><td>衛署藥輸字第010161號</td><td>膨苦恩錠</td><td>CALCIUM PHOSPHATE DIBASIC、DIASTASE BIO-、ALUMINUM MAGNESIUM S…</td><td>1991/12/09</td></tr><tr><td>衛署藥輸字第010696號</td><td>健得生膜衣錠</td><td>ALBUMIN、DEHYDROCHOLIC ACID、RIBOFLAVIN (VIT B2)、METHIONINE、PY…</td><td>2002/12/20</td></tr><tr><td>衛署藥輸字第011047號</td><td>"紐西蘭" 托氫膽酸粉</td><td>DEHYDROCHOLIC ACID</td><td>2014/04/14</td></tr><tr><td>衛署藥輸字第012294號</td><td>恩滋腸溶錠</td><td>DEHYDROCHOLIC ACID、PEPSIN、PANCREATIN (DIASTASE VERA)</td><td>1989/10/12</td></tr><tr><td>衛署藥輸字第012911號</td><td>脫氫膽酸（口服用）</td><td>DEHYDROCHOLIC ACID</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第013629號</td><td>去氫膽酸粉劑</td><td>DEHYDROCHOLIC ACID</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第013868號</td><td>脫氫膽酸粉劑</td><td>DEHYDROCHOLIC ACID</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第013913號</td><td>復膽利糖衣錠</td><td>DEHYDRODEOXYCHOLIC ACID、DEHYDROCHOLIC ACID</td><td>2000/09/05</td></tr><tr><td>衛署藥輸字第014049號</td><td>去氫膽酸粉劑</td><td>DEHYDROCHOLIC ACID</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第014674號</td><td>達羅明顆粒</td><td>INOSITOL (MESO-INOSITOL)、GLYCYRRHETATE AMMONIUM、AMYLASE ALPH…</td><td>1993/07/30</td></tr><tr><td>衛署藥輸字第015218號</td><td>適百瘼－見了利膜衣錠</td><td>GLUTAMIC ACID HCL、DEHYDROCHOLATE SODIUM、PANCREATIN (DIASTASE…</td><td>1995/05/29</td></tr><tr><td>衛署藥輸字第015761號</td><td>朗朗健錠</td><td>SODIUM BICARBONATE ( EQ TO SODIUM HYDROGEN CARBONATE)、POTATO…</td><td>1988/03/10</td></tr><tr><td>衛署藥輸字第015921號</td><td>胃可舒錠</td><td>PANTOTHENATE CALCIUM、GLYCYRRHIZA POWDER、DEHYDROCHOLIC ACID、G…</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第017199號</td><td>恩滋腸溶錠</td><td>PANCREATIN (DIASTASE VERA)、PEPSIN、DEHYDROCHOLIC ACID</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第017345號</td><td>脫氫膽酸</td><td>DEHYDROCHOLIC ACID</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第018884號</td><td>膨苦恩錠</td><td>MOLUSIN、CELLULOSINE AP、DIASTASE BIO-、PANCREATIN (DIASTASE VE…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第019031號</td><td>肝必舒錠</td><td>SODIUM ASCORBATE、DIISOPROPYLAMINE DICHLOROACETATE、BIOTAMYLAS…</td><td>2004/05/19</td></tr><tr><td>衛署藥輸字第019048號</td><td>懷舒錠</td><td>SCOPOLIA EXTRACT、MAGNESIUM CARBONATE、ANACHOLINE、NAGASE、BISMU…</td><td>2004/05/19</td></tr><tr><td>衛署藥輸字第019163號</td><td>懷舒顆粒</td><td>SWERTIA HERBA、NAGARSE(PROTEASECRYSTAL)、MAGNESIUM ALUMINUM HY…</td><td>2004/05/19</td></tr><tr><td>衛署藥輸字第019646號</td><td>理研胃腸藥三層錠</td><td>ALUMINUM DIHYDROXYALLANTOINATE (ALDIOXA)、SCOPOLIA EXTRACT、SO…</td><td>2013/12/31</td></tr><tr><td>衛署藥輸字第021196號</td><td>脫氫膽酸</td><td>DEHYDROCHOLIC ACID</td><td>2010/08/16</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

**現況**：台灣目前有效的去氫膽酸單方製劑許可證有「派頓」去氫膽酸錠與欣肝膽錠250毫克兩項（另有原料藥許可證）。

<!-- review:begin dehydrocholic-acid-tw-license-count-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「**現況**：台灣目前僅剩派頓去氫膽酸錠一項有效許可證。」。依 TFDA 許可證資料，去氫膽酸單方製劑目前有效的有「派頓」去氫膽酸錠與欣肝膽錠250毫克兩項，另有原料藥許可證。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end dehydrocholic-acid-tw-license-count-2026-10-03 -->

## 安全性

### 藥物交互作用

| 併用藥物 | 嚴重程度 | 來源 |
|----------|----------|------|
| Cyclosporine | Minor | DDInter |

### 警語與禁忌

- 仿單詳細資訊未提供完整警語資料
- 一般禁忌：完全膽道阻塞時禁用

## 結論

### 整體評估：低優先級

Dehydrocholic acid 的 TxGNN 預測新適應症主要集中在膽道相關疾病，與其原有適應症高度重疊，不具真正的老藥新用價值。對於腎臟相關預測（如急性尿酸腎病、腎結石），缺乏機轉支持和臨床證據。

### 建議

1. **不建議**進一步投入資源研究此藥物的新適應症
2. 維持其作為傳統利膽劑的角色
3. 台灣目前僅剩一項有效許可證，市場重要性已大幅下降

<!-- review:begin dehydrocholic-acid-conclusion-license-count-2026-10-03 -->

> **查核加註（2026-10-03）**：依 TFDA 許可證資料，去氫膽酸單方製劑目前有效的有「派頓」去氫膽酸錠與欣肝膽錠250毫克兩項（另有原料藥許可證），不是只剩一項；建議內容原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end dehydrocholic-acid-conclusion-license-count-2026-10-03 -->

### 證據等級總結

| 預測適應症 | TxGNN 分數 | 臨床試驗 | 文獻支持 | 機轉合理性 | 綜合評估 |
|------------|------------|----------|----------|------------|----------|
| 急性尿酸腎病 | 0.9999 | 無 | 無 | 低 | 不推薦 |
| 腎結石 | 0.9999 | 無 | 極弱 | 低 | 不推薦 |
| 膽道疾病 | 0.9999 | 無 | 有 | 高 | 已為適應症 |
| 膽管腫瘤 | 0.9998 | 無 | 極弱 | 低 | 不推薦 |

---
*報告產生日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、台灣 FDA*

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「台灣目前僅剩派頓去氫膽酸錠一項有效許可證」 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 建議「台灣目前僅剩一項有效許可證」 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

