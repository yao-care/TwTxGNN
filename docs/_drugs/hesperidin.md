---
layout: default
title: Hesperidin
parent: 中證據等級 (L3-L4)
nav_order: 120
evidence_level: L4
indication_count: 10
---

# Hesperidin
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Hesperidin：從血管強化到骨髓增生性腫瘤

## 一句話總結

Hesperidin（甲基柑橘素）是一種柑橘類黃酮苷，在台灣主要核准用於增強毛細血管、防止出血及維他命 P 缺乏症。
TxGNN 模型預測它可能對**骨髓增生性腫瘤 (Myeloproliferative Neoplasm)** 有效，
目前有 **0 個臨床試驗**和 **2 篇文獻**支持這個方向，證據仍處於前臨床階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 強化血管、末梢血管強化劑（hesperidin 單方許可證，皆已註銷，如衛署藥輸字第013726號）；現行有效許可證均為含 hesperidin 的複方（綜合感冒藥等） |
| 預測新適應症 | 骨髓增生性腫瘤 (Myeloproliferative Neoplasm) |
| TxGNN 預測分數 | 99.47% |
| 證據等級 | L4 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 74 張（有效單方 0／有效複方 10／已註銷 64） |
| 建議決策 | Hold |

<!-- review:begin hesperidin-original-indication-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「原適應症／增強毛細血管」。「增強毛細血管」出自 methyl hesperidin、troxerutin 的已註銷許可證；hesperidin 單方許可證曾載「強化血管」「末梢血管強化劑」，但已全部註銷，現行有效許可證都是複方。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end hesperidin-original-indication-2026-10-03 -->

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Hesperidin 是柑橘類黃酮苷，在人體代謝後轉化為活性苷元 **Hesperetin**，已知具有抗氧化、抗發炎及廣泛的細胞訊號調節特性。

骨髓增生性腫瘤（MPN）涵蓋慢性骨髓白血病（CML）等亞型，其中 CML 的核心驅動突變為 **BCR-ABL 融合蛋白**（一種過度活化的酪胺酸激酶）。計算分子對接研究顯示 Hesperidin 可能針對 BCR 激酶結構域產生抑制效應；另有研究顯示 Hesperetin 可調節骨髓白血病細胞的膜孕激素受體（mPR）表達並降低活性氧（ROS），理論上可干擾腫瘤細胞增殖信號。

然而，原適應症（血管強化、止血）屬於平滑肌與微血管壁藥理，與 MPN 的骨髓異常增殖機轉在生物學路徑上缺乏直接連結。TxGNN 的預測很可能反映知識圖譜中黃酮類廣泛抗增殖節點與 MPN 節點的拓撲鄰近性，現有生物學理據仍屬初探，需要更多前臨床驗證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [31759365](https://pubmed.ncbi.nlm.nih.gov/31759365/) | 2019 | In vitro | Asian Pacific Journal of Cancer Prevention | 以計算方法重新定位藥物靶向 BCR 激酶結構域，探索克服 TKI 耐藥性的新策略，Hesperidin 列為候選分子之一 |
| [40751800](https://pubmed.ncbi.nlm.nih.gov/40751800/) | 2025 | In vitro | Medical Oncology | Hesperetin 可上調人類骨髓白血病細胞膜孕激素受體表達，並顯著降低 CML 特徵性高 ROS 水平，顯示抗氧化與細胞訊號雙重效應 |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Hesperidin 的不重複許可證共 **74 張**：有效單方 0 張、有效複方 10 張、已註銷 64 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（10 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 內衛成製字第000141號 | 益風糖衣錠 | THIAMINE MONONITRATE、GUAIACOL GLYCERYL ETHER (EQ TO GUAIFENE… | 糖衣錠 | 四季感冒、發熱、咳嗽、鼻涕、流行性感冒症狀之治療、過敏性鼻炎、氣喘、頭痛、齒痛等 |
| 內衛藥製字第000977號 | 小兒寶理熱顆粒 | BROMISOVALUM ( EQ TO BROMOVALERYLUREA) ( EQ TO BROMVALETONE)… | 內服顆粒劑 | 緩解感冒之各種症狀（咽喉痛、發燒、頭痛、關節痛、肌肉痛、流鼻水、鼻塞、打噴嚏）。 |
| 內衛藥製字第001097號 | "生達" 克風膠囊 | THIAMINE MONONITRATE、DEXTROMETHORPHAN HBR、SALICYLAMIDE、CHLOR… | 膠囊劑 | 緩解感冒之各種症狀（咽喉痛、發燒、頭痛、關節痛、肌肉痛、流鼻水、鼻塞、打噴嚏、咳嗽）。 |
| 衛署藥製字第019401號 | 咳熱愛兒康顆粒 | CAFFEINE ANHYDROUS、HESPERIDIN (VIT P)、DIPHENHYDRAMINE TANNAT… | 內服顆粒劑 | 緩解感冒之各種症狀（流鼻水、鼻塞、打噴嚏、咽喉痛、畏寒、發燒、頭痛、關節痛、肌肉酸痛）。 |
| 衛署藥製字第027833號 | 佈血康膠囊 | FERROUS FUMARATE、FOLIC ACID、OROTIC ACID (VIT B13)、PYRIDOXINE… | 膠囊劑 | 鐵缺乏性貧血、惡性貧血及因貧血所引起之貧血症狀之改善 |
| 衛署藥製字第031051號 | 頓風寧顆粒 | HESPERIDIN (VIT P)、DIPHENHYDRAMINE TANNATE、ACETAMINOPHEN (EQ… | 內服顆粒劑 | 緩解感冒之各種症狀（咽喉痛、畏寒、發燒、頭痛、關節痛、肌肉酸痛、流鼻水、鼻塞、打噴嚏）。 |
| 衛署藥製字第041687號 | 衛格維他命感冒錠 | NOSCAPINE、HESPERIDIN (VIT P)、CAFFEINE、RIBOFLAVIN (VIT B2)、PA… | 錠劑 | 感冒諸症狀（畏寒、發燒、頭痛、咳嗽、鼻塞、流鼻水、打噴嚏、咽喉痛、關節痛、肌肉痛等）。 |
| 衛署藥製字第046051號 | 衛格維他命感冒膠囊 | HESPERIDIN (VIT P)、RIBOFLAVIN (VIT B2)、ETHENZAMIDE (ETHOXYBE… | 膠囊劑 | 緩解感冒之各種症狀(畏寒、發燒、頭痛、咳嗽、鼻塞、流鼻水、打噴嚏、咽喉痛、關節痛、肌肉酸痛)。 |
| 衛署藥製字第055050號 | 小兒用利撒爾感冒顆粒 | ACETAMINOPHEN (EQ TO PARACETAMOL)、DIPHENHYDRAMINE TANNATE、HE… | 內服顆粒劑 | 緩解感冒之各種症狀(流鼻水、鼻塞、打噴嚏、咽喉痛、畏寒、發燒、頭痛、關節痛、肌肉酸痛)。 |
| 衛部藥製字第059659號 | 風治樂膠囊 | NOSCAPINE、DL-METHYLEPHEDRINE HCL、THIAMINE MONONITRATE、HESPER… | 膠囊劑 | 緩解感冒之各種症狀(咽喉痛、畏寒、發燒、頭痛、關節痛、肌肉酸痛、流鼻水、鼻塞、打噴嚏、咳嗽、喀痰)。 |

<details><summary><strong>已註銷</strong>（64 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第000868號</td><td>咳哪糖衣錠</td><td>HESPERIDIN (VIT P)、CHLORPHENIRAMINE MALEATE、DL-METHYLEPHEDRI…</td><td>2000/08/04</td></tr><tr><td>內衛藥製字第009188號</td><td>小兒風哪顆粒</td><td>CHLORPHENIRAMINE MALEATE、THIAMINE HYDROCHLORIDE、DL-METHYLEPH…</td><td>2015/06/18</td></tr><tr><td>內衛藥製字第010101號</td><td>非必林膠囊</td><td>THIAMINE NITRATE、CAFFEINE、HESPERIDIN (VIT P)、RIBOFLAVIN (VIT…</td><td>2010/02/08</td></tr><tr><td>內衛藥製字第011537號</td><td>非必林糖衣錠</td><td>CHLORPHENIRAMINE MALEATE、SODIUM ASCORBATE、NOSCAPINE HCL、ALUM…</td><td>2010/02/08</td></tr><tr><td>內衛藥製字第013179號</td><td>必止血膠囊</td><td>HESPERIDIN (VIT P)、1-NAPHTHYLAMINE-4-SULFONATE SODIUM GLYCOS…</td><td>1990/09/10</td></tr><tr><td>內衛藥製字第013895號</td><td>育寶Ｆ膠囊</td><td>INOSITOL NIACINATE、CYANOCOBALAMIN (VIT B12)、ERGOCALCIFEROL (…</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第013997號</td><td>"東光吉華"欣兒顆粒</td><td>CAFFEINE ANHYDROUS、DIPHENHYDRAMINE TANNATE、HESPERIDIN (VIT P…</td><td>2005/01/17</td></tr><tr><td>內衛藥輸字第002546號</td><td>去水腫腸衣錠</td><td>3-(A-METHYLBENZYL)-HYDROCHLOROTHIAZIDE、THIAMINE MONONITRATE、…</td><td>2000/10/20</td></tr><tr><td>內衛藥輸字第003189號</td><td>血利通錠</td><td>INOSITOL (MESO-INOSITOL)、THIAMINE MONONITRATE、PENTAERYTHRITO…</td><td>1986/01/15</td></tr><tr><td>內衛藥輸字第003355號</td><td>愛爾體</td><td>VITAMIN A、LINOLEATE CALCIUM、LECITHIN(LECITHOL)、CHOLINE BITAR…</td><td>1990/09/13</td></tr><tr><td>內衛藥輸字第003464號</td><td>喜壽達膠囊</td><td>VITAMIN C FROM ROSE HIPS、MENADIONE (VIT K3)、HESPERIDIN (VIT…</td><td>1988/09/05</td></tr><tr><td>內衛藥輸字第003751號</td><td>可培得力針劑</td><td>HESPERIDIN (VIT P)、FOLIC ACID、RIBOFLAVIN PHOSPHATE、PYRIDOXIN…</td><td>1988/11/15</td></tr><tr><td>內衛藥輸字第004152號</td><td>安治血管</td><td>TOCOPHEROL ACETATE ALPHA DL-、RUTIN、HESPERIDIN (VIT P)、PYRIDO…</td><td>1990/08/18</td></tr><tr><td>內衛藥輸字第004284號</td><td>降血平片</td><td>PENTAERYTHRITOL TETRANITRATE (PENTHROL)、BEZOAR ORIENTALE、BRO…</td><td>1990/08/18</td></tr><tr><td>內衛藥輸字第004546號</td><td>永沛力膠囊</td><td>ASCORBIC ACID (VIT C)、ERGOCALCIFEROL IN GELATIN、PYRIDOXINE H…</td><td>1990/08/18</td></tr><tr><td>內衛藥輸字第004577號</td><td>中新血壓錠</td><td>INOSITOL (MESO-INOSITOL)、THIAMINE MONONITRATE、PENTAERYTHRITO…</td><td>1990/07/20</td></tr><tr><td>內衛藥輸字第004786號</td><td>血平鎮</td><td>HESPERIDIN (VIT P)</td><td>1985/08/09</td></tr><tr><td>內衛藥輸字第005705號</td><td>喝斯百靈</td><td>HESPERIDIN (VIT P)</td><td>1985/08/14</td></tr><tr><td>內衛藥輸字第006162號</td><td>悠捷露</td><td>THIAMINE MONONITRATE、TOCOPHEROL ALPHA DL- (EQ TO DL-ALPHA TO…</td><td>1986/06/16</td></tr><tr><td>內衛藥輸字第006364號</td><td>橙醣</td><td>HESPERIDIN (VIT P)</td><td>1985/09/10</td></tr><tr><td>內衛藥輸字第007393號</td><td>橙/</td><td>HESPERIDIN (VIT P)</td><td>1985/12/30</td></tr><tr><td>衛署藥製字第000785號</td><td>兒下熱顆粒</td><td>ACETAMINOPHEN (EQ TO PARACETAMOL)、DIPHENHYDRAMINE TANNATE、HE…</td><td>1991/01/02</td></tr><tr><td>衛署藥製字第001441號</td><td>金字傷風克片</td><td>ACETAMINOPHEN (EQ TO PARACETAMOL)、CHLORPHENIRAMINE MALEATE、A…</td><td>1998/02/25</td></tr><tr><td>衛署藥製字第004139號</td><td>舒你康膠囊</td><td>GELATIN、POTASSIUM GUAIACOLSULFONATE、ALUMINUM BIS(ACETYLSALIC…</td><td>2010/11/03</td></tr><tr><td>衛署藥製字第007052號</td><td>小兒消除熱嗽顆粒</td><td>ACETAMINOPHEN (EQ TO PARACETAMOL)、HESPERIDIN (VIT P)、CAFFEIN…</td><td>1989/12/31</td></tr><tr><td>衛署藥製字第007249號</td><td>小兒祝爾康顆粒</td><td>HESPERIDIN (VIT P)、CHLORPHENIRAMINE MALEATE、ACETAMINOPHEN (E…</td><td>2005/05/04</td></tr><tr><td>衛署藥製字第008103號</td><td>小兒用利熱寧顆粒</td><td>CAFFEINE ANHYDROUS、ACETAMINOPHEN (EQ TO PARACETAMOL)、HESPERI…</td><td>2012/09/14</td></tr><tr><td>衛署藥製字第009960號</td><td>"富生"感冒顆粒</td><td>CAFFEINE ANHYDROUS、CHLORPHENIRAMINE MALEATE、HESPERIDIN (VIT…</td><td>2017/01/25</td></tr><tr><td>衛署藥製字第010817號</td><td>利兒風顆粒</td><td>ACETAMINOPHEN (EQ TO PARACETAMOL)、CHLORPHENIRAMINE MALEATE、H…</td><td>2005/03/08</td></tr><tr><td>衛署藥製字第014301號</td><td>司風糖衣錠</td><td>DL-METHYLEPHEDRINE HCL、THIAMINE MONONITRATE、NOSCAPINE、GUAIAC…</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第022311號</td><td>克冒平糖衣錠</td><td>CAFFEINE ANHYDROUS、GLYCYRRHIZA (LIQUORICE)、ACETAMINOPHEN (EQ…</td><td>2000/08/08</td></tr><tr><td>衛署藥製字第024879號</td><td>舒必通膠囊</td><td>GLYCYRRHETIC ACID (EQ TO GLYCYRRHETINIC ACID)、BELLADONNA EXT…</td><td>1997/01/07</td></tr><tr><td>衛署藥製字第026092號</td><td>鼻能通膠囊</td><td>BELLADONNA EXTRACT、PHENYLPROPANOLAMINE HCL (DL-NOREPHEDRINE…</td><td>1988/12/31</td></tr><tr><td>衛署藥製字第027216號</td><td>舒感平顆粒</td><td>CAFFEINE ANHYDROUS、ACETAMINOPHEN (EQ TO PARACETAMOL)、HESPERI…</td><td>2014/10/08</td></tr><tr><td>衛署藥製字第028287號</td><td>小兒用安可感冒顆粒</td><td>DIPHENHYDRAMINE TANNATE、ACETAMINOPHEN (EQ TO PARACETAMOL)、CA…</td><td>2013/10/02</td></tr><tr><td>衛署藥製字第029946號</td><td>兒感熱顆粒</td><td>CHLORPHENIRAMINE MALEATE、HESPERIDIN (VIT P)、ACETAMINOPHEN (E…</td><td>1988/08/20</td></tr><tr><td>衛署藥製字第030359號</td><td>速治感冒錠</td><td>DL-METHYLEPHEDRINE HCL、OXELADIN、ALUMINUM BIS(ACETYLSALICYLAT…</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第031074號</td><td>兒感熱顆粒</td><td>HESPERIDIN (VIT P)、CAFFEINE ANHYDROUS、ACETAMINOPHEN (EQ TO P…</td><td>2010/12/28</td></tr><tr><td>衛署藥製字第031077號</td><td>感風錠</td><td>DL-METHYLEPHEDRINE HCL、CAFFEINE ANHYDROUS、HYDROXYBUTYRIC ACI…</td><td>2010/12/28</td></tr><tr><td>衛署藥製字第031752號</td><td>必止血膠囊</td><td>ASCORBIC ACID (VIT C)、MENADIONE (VIT K3)、1-NAPHTHYLAMINE-4-S…</td><td>1997/08/28</td></tr><tr><td>衛署藥製字第033169號</td><td>兒下熱顆粒</td><td>ACETAMINOPHEN (EQ TO PARACETAMOL)、HESPERIDIN (VIT P)、DIPHENH…</td><td>2023/07/03</td></tr><tr><td>衛署藥製字第034897號</td><td>利康兒顆粒</td><td>ACETAMINOPHEN (EQ TO PARACETAMOL)、CAFFEINE ANHYDROUS、HESPERI…</td><td>2013/10/14</td></tr><tr><td>衛署藥製字第035189號</td><td>舒涕克膠囊</td><td>ASCORBIC ACID (VIT C)、CARBINOXAMINE MALEATE、PHENYLPROPANOLAM…</td><td>2007/03/28</td></tr><tr><td>衛署藥製字第035642號</td><td>甜安熱感冒顆粒</td><td>CAFFEINE ANHYDROUS、ACETAMINOPHEN (EQ TO PARACETAMOL)、DIPHENH…</td><td>2013/07/18</td></tr><tr><td>衛署藥製字第036520號</td><td>“龍德”鼻通寧感冒膠囊</td><td>PSEUDOEPHEDRINE HCL、ACETAMINOPHEN (EQ TO PARACETAMOL)、DEXTRO…</td><td>2017/08/24</td></tr><tr><td>衛署藥製字第037678號</td><td>利特顆粒</td><td>ACETAMINOPHEN (EQ TO PARACETAMOL)、CAFFEINE、HESPERIDIN (VIT P…</td><td>2023/07/21</td></tr><tr><td>衛署藥輸字第000399號</td><td>治咳寧膠囊</td><td>HESPERIDIN (VIT P)、DIBUNATE SODIUM (CORTEMIN SSODIUM 2,6-DI-…</td><td>1985/07/05</td></tr><tr><td>衛署藥輸字第001841號</td><td>小兒用利撒爾感冒顆粒</td><td>ACETAMINOPHEN (EQ TO PARACETAMOL)、HESPERIDIN (VIT P)、DIPHENH…</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第007081號</td><td>佳維他命膜衣錠</td><td>INOSITOL (MESO-INOSITOL)、GLUTAMIC ACID、VITAMIN D、ALFALFA LEA…</td><td>2003/12/05</td></tr><tr><td>衛署藥輸字第007096號</td><td>祈得補膜衣錠</td><td>HESPERIDIN COMPLEX、PYRIDOXINE(VITAMIN B6)、VIT E (TOCOPHEROL…</td><td>1999/01/12</td></tr><tr><td>衛署藥輸字第007219號</td><td>命倍得錠</td><td>CALCIUM、CYANOCOBALAMIN (VIT B12)、CHOLINE、ASCORBIC ACID (VIT…</td><td>1995/05/12</td></tr><tr><td>衛署藥輸字第010543號</td><td>安汝錠</td><td>PARA-AMINOBENZOIC ACID (VIT H1)、NIACINAMIDE (NICOTINAMIDE)、C…</td><td>2002/07/09</td></tr><tr><td>衛署藥輸字第011483號</td><td>美佳多士膜衣錠</td><td>VITAMIN A (FISH LIVER OIL)、FERROUS GLUCONATE、BIOFLAVINOIDS (…</td><td>2004/12/08</td></tr><tr><td>衛署藥輸字第011510號</td><td>舒好維持續膜衣錠</td><td>NIACINAMIDE (NICOTINAMIDE)、ZINC (OXIDE)、POTASSIUM (CHLORIDE)…</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第012213號</td><td>利康維錠</td><td>PYRIDOXINE(VITAMIN B6)、HESPERIDIN COMPLEX、TOCOPHEROL ALPHA-、…</td><td>2002/02/26</td></tr><tr><td>衛署藥輸字第012666號</td><td>鼻能健膠囊</td><td>HESPERIDIN (VIT P)、PHENYLPROPANOLAMINE HCL (DL-NOREPHEDRINE…</td><td>1985/12/26</td></tr><tr><td>衛署藥輸字第013205號</td><td>小兒用利撒爾感冒顆粒</td><td>DIPHENHYDRAMINE TANNATE、HESPERIDIN (VIT P)、ACETAMINOPHEN (EQ…</td><td>1991/11/15</td></tr><tr><td>衛署藥輸字第013726號</td><td>血平鎮粉劑</td><td>HESPERIDIN (VIT P)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第014541號</td><td>橙/</td><td>HESPERIDIN (VIT P)</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第014550號</td><td>鼻能健膠囊</td><td>GLYCYRRHETIC ACID (EQ TO GLYCYRRHETINIC ACID)、BELLADONNA EXT…</td><td>2004/05/21</td></tr><tr><td>衛署藥輸字第018027號</td><td>小兒用理研感冒顆粒</td><td>GLYCYRRHIZATE AMMONIUM SALT (GLYCAMIL)、CAFFEINE ANHYDROUS、AC…</td><td>2013/12/31</td></tr><tr><td>衛署藥輸字第018820號</td><td>小兒用利撒爾感冒顆粒</td><td>ACETAMINOPHEN (EQ TO PARACETAMOL)、HESPERIDIN (VIT P)、DIPHENH…</td><td>2011/02/24</td></tr><tr><td>衛署藥輸字第019874號</td><td>"阿爾卑斯 " 橙苷</td><td>HESPERIDIN</td><td>2019/03/14</td></tr><tr><td>衛署藥輸字第023240號</td><td>嘉佑感冒膠囊</td><td>CHLORPHENIRAMINE MALEATE、DL-METHYLEPHEDRINE HCL、CAFFEINE ANH…</td><td>2017/08/18</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
目前僅有 2 篇體外實驗研究（均為 In vitro），且研究對象多為 Hesperidin 的代謝物 Hesperetin 而非 Hesperidin 本身，活性形式與劑量轉化關係尚未釐清；無臨床試驗數據支持，現有證據不足以進入開發階段。

**若要推進需要：**
- 補充 Hesperidin 的完整作用機轉資料（DrugBank MOA）
- 建立 Hesperidin 於骨髓增生性腫瘤動物模型的體內（in vivo）前臨床實驗
- 釐清 Hesperidin → Hesperetin 的代謝轉化率與腫瘤組織生物可用性
- 評估與現有 TKI（如 Imatinib）的協同或拮抗效應
- 確認口服劑型的血漿藥物濃度是否達到體外實驗有效濃度

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表 5 張全數已註銷 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 原適應症「增強毛細血管」取自其他成分 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

