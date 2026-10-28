---
layout: default
title: Mannitol
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 9
monitor_inn: "Mannitol"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "acute pulmonary heart disease", "exercise-induced malignant hyperthermia", "familial periodic paralysis", "hypokalemic periodic paralysis", "congenital multicore myopathy with external ophthalmoplegia", "moderate multiminicore disease with hand involvement", "nephrogenic diabetes insipidus", "central core myopathy"]
last_modified_at: 2026-10-23
description: "Mannitol：預測新適應症為腎因性抗利尿不適當綜合症 (nephrogenic syndrome of inappropriate antidiuresis)（證據等級 L5）。原適應症：利尿、降顱內壓、腦水腫、促進毒物之尿中排除、腎小球過濾速率之測定（診斷用）"
---

# Mannitol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Mannitol：腎因性抗利尿不適當綜合症
{: .text-alpha }

## 一句話總結

Mannitol（甘露醇）是一種滲透性利尿劑，在台灣核准用於利尿、降顱內壓、腦水腫、促進毒物經尿排除，以及腎絲球過濾率測定（診斷用）。
TxGNN 模型預測它可能對**腎因性抗利尿不適當綜合症 (nephrogenic syndrome of inappropriate antidiuresis)** 有效，但目前**沒有臨床試驗**，僅有 **1 篇**一般性的低血鈉綜述，且未提及甘露醇的實際療效，屬於僅有模型預測的階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 利尿、降顱內壓、腦水腫、促進毒物之尿中排除、腎小球過濾速率之測定（診斷用） |
| 預測新適應症 | 腎因性抗利尿不適當綜合症 (nephrogenic syndrome of inappropriate antidiuresis) |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 8 張／共 83 張） |
| 許可證數 | 83 張（有效單方 8／有效複方 0／已過期 2／已註銷 73） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知甘露醇是滲透性利尿劑，經腎小球過濾後不易被再吸收，使腎小管內滲透壓升高而增加尿量與溶質排出，這也是它用於降顱內壓與腦水腫的基礎。

從理論上看，腎因性抗利尿不適當綜合症是一種水分滯留、容易低血鈉的疾病，而滲透性利尿能增加排尿，因此模型可能因此建立關聯。不過，這個連結相當間接：滲透性負荷本身也可能擾動鈉的平衡，反而使電解質問題更複雜。

目前唯一連結的文獻是低血鈉評估的通論性綜述，並未提到甘露醇，因此這項預測目前只能視為假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | 說明評估低血鈉病人時常見的十個陷阱，強調正確診斷病因的重要性，以及治療不足或矯正過度的風險；未涉及甘露醇的療效 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Mannitol 的不重複許可證共 **83 張**：有效單方 8 張、有效複方 0 張、已過期 2 張（未註銷但有效日期早於資料集日期）、已註銷 73 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（8 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 內衛藥製字第012343號 | "信東" 美立妥注射劑 | 注射劑 | 信東生技股份有限公司 | 2028/05/25 | 利尿、降顱內壓、腦水腫、促進毒物之尿中排除、腎小球過濾速率之測定(診斷用) |
| 衛署藥製字第009633號 | 滿乃通注射液 | 注射劑 | 杏林新生製藥股份有限公司 | 2028/05/10 | 利尿、降顱內壓、腦水腫、促進毒物之尿中排除、腎小球過濾速率之測定（診斷用） |
| 衛署藥製字第013354號 | "濟生"邁尼妥注射液２０％ | 注射劑 | 濟生醫藥生技股份有限公司 | 2028/05/25 | 利尿、降顱內壓、腦水腫、促進毒物之尿中排除、腎小球過濾速率之測定（診斷用） |
| 衛署藥製字第015561號 | 邁尼妥注射液２０％　〝順華〞 | 注射劑 | 順華藥品工業股份有限公司 | 2028/05/25 | 利尿、降顱內壓、腦水腫、促進毒物之尿中排除、腎小球過濾速率之測定（診斷用） |
| 衛署藥製字第016476號 | "台裕"甘露醇注射液（邁尼妥） | 注射劑 | 台裕化學製藥廠股份有限公司 | 2030/05/25 | 利尿、降顱內壓、腦水腫、促進毒物之尿中排除、腎小球過濾速率之測定（診斷用） |
| 衛署藥製字第042601號 | 〝安星〞安露注射液２００毫克/毫升（甘露醇） | 注射劑 | 安星製藥股份有限公司 | 2028/09/30 | 利尿、降顱內壓、腦水腫，促進毒物之尿中排除、腎小球過濾速率之測定(診斷用)。 |
| 衛署藥製字第043768號 | 滿乃通　注射液　１５Ｗ／Ｖ％ | 注射劑 | 杏林新生製藥股份有限公司 | 2030/05/26 | 利尿、降顱內壓、腦水腫、促進毒物之尿中排除、腎小球過濾速率之測定（診斷用）。 |
| 衛署藥輸字第016930號 | "羅貴特" 甘露醇 | （粉） | 法台化學股份有限公司 | 2028/11/23 | 利尿劑 |

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-09-29）</strong>（2 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛署藥製字第033425號</td><td>"南光"舒而通輸注液20%(甘露醇)</td><td>D-MANNITOL</td><td>2025/12/21</td></tr><tr><td>衛署藥輸字第022202號</td><td>舒得寧長效凍晶注射劑30公絲</td><td>MANNITOL、LANREOTIDE (ACETATE)、WATER FOR INJECTION</td><td>2013/06/05</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（73 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第003275號</td><td>得利通注射液</td><td>MANNITOL</td><td>1989/01/24</td></tr><tr><td>內衛藥製字第006610號</td><td>凍結輔/美達民針５公絲</td><td>COCARBOXYLASE (THIAMINE PYROPHOSPHATE)、MANNITOL</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第006612號</td><td>凍結輔/美達民針２０公絲</td><td>COCARBOXYLASE (THIAMINE PYROPHOSPHATE)、MANNITOL</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第006617號</td><td>凍結輔/美達民針１０公絲</td><td>MANNITOL、COCARBOXYLASE (THIAMINE PYROPHOSPHATE)</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第006619號</td><td>旅爽片</td><td>DIPHENHYDRAMINE HCL、MANNITOL、CHLORPHENIRAMINE MALEATE、DYPHYL…</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第007899號</td><td>木蜜醇注射液５％</td><td>D-MANNITOL、GLUCOSE、CALCIUM CHLORIDE、SODIUM CHLORIDE</td><td>2013/10/03</td></tr><tr><td>內衛藥輸字第000441號</td><td>木蜜醇注</td><td>D-MANNITOL</td><td>1988/09/05</td></tr><tr><td>內衛藥輸字第000881號</td><td>奧斯莫斯他利２０％</td><td>MANNITOL</td><td>1986/10/17</td></tr><tr><td>內衛藥輸字第002102號</td><td>木密醇</td><td>MANNITOL</td><td>1988/09/05</td></tr><tr><td>內衛藥輸字第004205號</td><td>甘露醇</td><td>MANNITOL</td><td>1985/08/02</td></tr><tr><td>內衛藥輸字第005218號</td><td>望你通針</td><td>MANNITOL</td><td>1999/10/25</td></tr><tr><td>內衛藥輸字第008242號</td><td>滿汝託注射液</td><td>D-MANNITOL</td><td>1990/12/05</td></tr><tr><td>衛署藥製字第004997號</td><td>"壽元"壽力醣注射液</td><td>D-MANNITOL</td><td>2025/04/29</td></tr><tr><td>衛署藥製字第006512號</td><td>壽力醣注射液</td><td>D-MANNITOL</td><td>2023/07/21</td></tr><tr><td>衛署藥製字第009345號</td><td>利斯妥－利注射液</td><td>SODIUM CHLORIDE、CALCIUM CHLORIDE、DEXTRAN 70、GLUCOSE、MANNITOL</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第009745號</td><td>"永豐"邁力通注射液</td><td>MANNITOL</td><td>2023/09/19</td></tr><tr><td>衛署藥製字第009996號</td><td>利斯妥－優注射液</td><td>SODIUM CHLORIDE、GLUCOSE、CALCIUM CHLORIDE、MANNITOL</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第012532號</td><td>血清哥娜荷爾蒙注射劑</td><td>MANNITOL、GONADOTROPIN SERUM</td><td></td></tr><tr><td>衛署藥製字第015562號</td><td>邁尼妥舒注射液　〝順華〞</td><td>SORBITOL、MANNITOL</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第028498號</td><td>克酸胃寧－鎂錠</td><td>MANNITOL、ALUMINUM HYDROXIDE (ALUMINA HYDRATED)、MAGNESIUM HYD…</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第031033號</td><td>福樂滿注射液</td><td>D-MANNITOL、FRUCTOSE (LAEVULOSE)</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第031387號</td><td>甘露醇注射液２００公絲/公撮</td><td>MANNITOL</td><td>2006/04/19</td></tr><tr><td>衛署藥製字第035943號</td><td>維喜鈣錠</td><td>PANTOTHENATE CALCIUM、MANNITOL、ASCORBIC ACID (VIT C)、SODIUM A…</td><td>2013/04/08</td></tr><tr><td>衛署藥製字第041553號</td><td>維達豪錠</td><td>CYANOCOBALAMIN (VIT B12)、VITAMIN A、NICOTINAMIDE、VITAMIN A (V…</td><td>2016/09/19</td></tr><tr><td>衛署藥輸字第000638號</td><td>腦能寧－果注射液</td><td>FRUCTOSE (LAEVULOSE)、MANNITOL</td><td>1985/06/24</td></tr><tr><td>衛署藥輸字第001387號</td><td>甘露糖醇</td><td>MANNITOL</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第002038號</td><td>木蜜醇</td><td>MANNITOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第002633號</td><td>每益多１５％注射液</td><td>D-MANNITOL</td><td>1985/11/22</td></tr><tr><td>衛署藥輸字第002690號</td><td>木蜜醇</td><td>MANNITOL</td><td>1993/02/16</td></tr><tr><td>衛署藥輸字第003208號</td><td>安世木蜜醇</td><td>MANNITOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第003419號</td><td>木蜜醇</td><td>MANNITOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第003483號</td><td>越速明診斷用注射劑</td><td>BENZALKONIUM CHLORIDE、GIRACTIDE ACETATE、MANNITOL</td><td>1986/02/13</td></tr><tr><td>衛署藥輸字第003847號</td><td>甘露醇１０％</td><td>MANNITOL</td><td>1988/07/06</td></tr><tr><td>衛署藥輸字第003979號</td><td>木蜜醇</td><td>MANNITOL</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第004563號</td><td>木蜜醇</td><td>MANNITOL</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第004665號</td><td>木蜜醇</td><td>MANNITOL</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第004802號</td><td>木蜜醇</td><td>MANNITOL</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第005552號</td><td>木蜜醇</td><td>D-MANNITOL</td><td>1990/07/03</td></tr><tr><td>衛署藥輸字第005753號</td><td>木蜜醇</td><td>MANNITOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第006028號</td><td>甘露醇</td><td>MANNITOL</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第006159號</td><td>表使得利注射液</td><td>MANNITOL</td><td>1986/04/30</td></tr><tr><td>衛署藥輸字第007303號</td><td>甘露醇２０％注射液</td><td>MANNITOL</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第007304號</td><td>甘露醇２５％注射液</td><td>MANNITOL</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第009214號</td><td>德達滿通注射液</td><td>EDETATE DISODIUM DIHYDRATE (EQ TO DISODIUM EDETATE DIHYDRATE…</td><td>1988/03/09</td></tr><tr><td>衛署藥輸字第009513號</td><td>貝樂斯發泡顆粒</td><td>MANNITOL、SORBITAN FATTY ACID ESTERS、SODIUM BICARBONATE ( EQ…</td><td>1988/03/01</td></tr><tr><td>衛署藥輸字第009936號</td><td>曼寧脫兒注射液</td><td>MANNITOL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第012025號</td><td>邁力多果糖注射液</td><td>D-MANNITOL、FRUCTOSE (LAEVULOSE)</td><td>1988/04/11</td></tr><tr><td>衛署藥輸字第012548號</td><td>木蜜醇</td><td>D-MANNITOL</td><td>1999/12/02</td></tr><tr><td>衛署藥輸字第012778號</td><td>木蜜醇</td><td>MANNITOL</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第013768號</td><td>甘露醇粉劑</td><td>MANNITOL</td><td>1993/08/12</td></tr><tr><td>衛署藥輸字第014379號</td><td>每益多１５％注射液</td><td>D-MANNITOL</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第014508號</td><td>速必瑞１０公絲咀嚼錠</td><td>MANNITOL MIXTURE 25% ISND</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第014841號</td><td>安痛速注射液</td><td>COCARBOXYLASE (THIAMINE PYROPHOSPHATE)、PYRIDOXINE HCL、CYANOC…</td><td>1997/01/09</td></tr><tr><td>衛署藥輸字第014868號</td><td>敏立舒注射液</td><td>NITROGLYCERIN、D-MANNITOL</td><td>1992/03/12</td></tr><tr><td>衛署藥輸字第014880號</td><td>莫拿克錠</td><td>ALLOPURINOL、D-MANNITOL</td><td>1999/09/28</td></tr><tr><td>衛署藥輸字第016289號</td><td>貝樂斯發泡顆粒</td><td>MANNITOL、SORBITAN FATTY ACID ESTERS、SODIUM BICARBONATE ( EQ…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第016302號</td><td>德達滿通注射液</td><td>EDETATE DISODIUM DIHYDRATE (EQ TO DISODIUM EDETATE DIHYDRATE…</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第016432號</td><td>邁力多果糖注射液</td><td>D-MANNITOL、FRUCTOSE (LAEVULOSE)</td><td>1993/07/29</td></tr><tr><td>衛署藥輸字第016697號</td><td>甘露醇１０％</td><td>MANNITOL</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第016905號</td><td>甘露醇注射液２０％</td><td>MANNITOL</td><td>2000/10/20</td></tr><tr><td>衛署藥輸字第016923號</td><td>"辛法" 甘露醇注射液１５％</td><td>MANNITOL</td><td>2000/10/20</td></tr><tr><td>衛署藥輸字第017170號</td><td>郝士曼木蜜醇注射液２０％</td><td>MANNITOL</td><td>1994/03/24</td></tr><tr><td>衛署藥輸字第017374號</td><td>安舒明注射液</td><td>D-MANNITOL、MECOBALAMIN</td><td>1991/08/05</td></tr><tr><td>衛署藥輸字第017923號</td><td>木蜜醇</td><td>D-MANNITOL</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第019837號</td><td>樂免敏點眼液　〝愛爾康〞</td><td>MANNITOL、LODOXAMIDE TROMETHAMINE、CITRIC ACID MONOHYDRATE、TYL…</td><td>2010/09/21</td></tr><tr><td>衛署藥輸字第019862號</td><td>邁力多果糖注射液</td><td>D-MANNITOL、FRUCTOSE (LAEVULOSE)</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第020322號</td><td>木蜜醇注射液２０％</td><td>MANNITOL</td><td>2014/04/28</td></tr><tr><td>衛署藥輸字第021130號</td><td>速挺欣注射劑１００國際單位</td><td>MANNITOL、SALCATONIN</td><td>2004/05/19</td></tr><tr><td>衛署藥輸字第023308號</td><td>達菲林長效注射劑３．７５毫克</td><td>TRIPTORELIN ACETATE、WATER FOR INJECTION、MANNITOL</td><td>2014/10/13</td></tr><tr><td>衛署藥輸字第025971號</td><td>甘露醇</td><td>Pearlitol PF (Mannitol)</td><td>2024/07/17</td></tr><tr><td>衛署藥輸字第R00082號</td><td>普特幽門螺旋桿菌測試劑</td><td>C-13 UREA、CITRIC ACID ANHYDROUS、MANNITOL、ORANGE FLAVOR</td><td>2004/12/20</td></tr><tr><td>衛署藥輸字第R00083號</td><td>大塚優比特顆粒100毫克</td><td>D-MANNITOL、C-13 UREA</td><td>2016/02/23</td></tr><tr><td>衛署藥陸輸字第000401號</td><td>甘露醇</td><td>Mannitol</td><td>2017/04/14</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜中的禁忌關聯**（來自知識圖譜的疾病關聯，並非仿單文字）：肝衰竭、肝性腦病變、無尿症、腎功能不全、肺水腫、顱內出血、貧血、血小板減少、嗜中性球減少、顆粒球缺乏症、紫質症、睡眠呼吸中止症、物質濫用或依賴等。
- **與預測適應症相關的安全疑慮**：滲透性利尿可能加重水與電解質失衡，用於水分滯留或低血鈉族群時，需特別留意血鈉變化。
- **藥物交互作用**：資料庫共記錄 249 筆交互作用。其中較需注意的包括與 Amikacin 的**嚴重 (Major)** 交互作用；另有多項中度交互作用，例如 Lamivudine、Formoterol、Salbutamol、Benazepril、Captopril、Carbamazepine、Citalopram、Dapagliflozin、Canagliflozin 等。

## 結論與下一步

**決策：Hold**

**理由：**
此預測僅來自模型分數，沒有任何臨床試驗，唯一的文獻也與甘露醇無直接關聯，證據等級為 L5。再加上滲透性利尿在理論上可能擾亂鈉平衡，不建議推進。

**若要推進需要：**
- 補齊甘露醇的作用機轉資料，並釐清其在抗利尿相關疾病中的生理效應
- 檢索並評估甘露醇用於此疾病的病例報告或機轉研究
- 評估對血鈉、血鉀與容積狀態的風險，並設計安全性監測計畫
- 確認此罕見疾病族群是否有可行的臨床研究設計

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄；頁首證據等級依本頁「快速總覽」的證據等級列重算，模型預測、總覽表與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-04 | 頁首證據等級 | 報告重生後已無此錯誤（2026-10-16：報告重生後頁首依新報告為 L5，此筆記的是舊版報告的重算；原為頁首等級依總覽表重算（原 L5→L3）） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

