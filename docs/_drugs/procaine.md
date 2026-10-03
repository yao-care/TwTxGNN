---
layout: default
title: Procaine
parent: 中證據等級 (L3-L4)
nav_order: 217
evidence_level: L4
indication_count: 10
---

# Procaine
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

# Procaine：從局部麻醉到高鐵血紅蛋白血症

## 一句話總結

Procaine（普魯卡因）是一種酯類局部麻醉藥，台灣核准用於局部麻醉及作為青黴素注射的載體。
TxGNN 模型預測與 Procaine 關聯性最高的適應症為**高鐵血紅蛋白血症 (Methemoglobinemia)**，
然而現有 **8 篇文獻**顯示此關聯源自 Procaine 代謝物 PABA 誘發此病的**已知不良反應機轉**，而非治療機轉，目前亦無相關臨床試驗登記。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 局部麻醉 |
| 預測新適應症 | 高鐵血紅蛋白血症 (Methemoglobinemia) |
| TxGNN 預測分數 | 99.50% |
| 證據等級 | L4 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 90 張（有效單方 4／有效複方 9／已註銷 77） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏完整的 DrugBank 作用機轉資料（高嚴重度資料缺口 DG001）。根據已知藥理，Procaine 是一種酯類局部麻醉藥（代表性商品名：Novocaine），透過**阻斷電壓門控鈉離子通道（Na⁺ channel）**，抑制神經元動作電位的產生與傳導，達到局部麻醉效果。此外，Guide to Pharmacology 資料庫指出 Procaine 與 ryanodine receptor（RyR1、RyR2）存在潛在交互作用，但目前缺乏量化生物活性數據加以支撐。

Procaine 在體內由血漿假性膽鹼酯酶（pseudocholinesterase）快速水解，主要代謝物為**對胺基苯甲酸（PABA）**。PABA 能將血紅素中的亞鐵（Fe²⁺）氧化為高鐵（Fe³⁺），導致血紅蛋白失去攜氧能力，引發高鐵血紅蛋白血症。TxGNN 的知識圖譜因此在 Procaine 節點與此疾病節點之間建立了強連結。

⚠️ **重要臨床解讀**：此高分預測反映的是 Procaine 與高鐵血紅蛋白血症之間的**不良反應因果關聯**，而非治療潛力。現有所有文獻均記錄 Procaine（或其複方）**導致**此病症的案例，而非治療案例。對高鐵血紅蛋白血症患者使用 Procaine 實際上構成臨床用藥禁忌，此預測方向不具再利用價值。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [3691245](https://pubmed.ncbi.nlm.nih.gov/3691245/) | 1987 | Cohort | Chinese Journal of Surgery | 靜脈 Procaine 麻醉確認可升高患者血中高鐵血紅蛋白濃度 |
| [6705717](https://pubmed.ncbi.nlm.nih.gov/6705717/) | 1984 | Review | Drugs | 局部麻醉藥合理使用綜述，涵蓋神經阻斷技術與毒性風險評估 |
| [5118947](https://pubmed.ncbi.nlm.nih.gov/5118947/) | 1971 | Review | Laval Medical | 局部麻醉藥藥理特性全面綜述，含代謝途徑與不良反應描述 |
| [6745527](https://pubmed.ncbi.nlm.nih.gov/6745527/) | 1984 | Review | Fundam Appl Toxicol | 有機磷殺蟲劑抑制非關鍵組織酯酶，間接改變 Procaine 等酯類藥物代謝速率與毒性 |
| [5529388](https://pubmed.ncbi.nlm.nih.gov/5529388/) | 1970 | Case series | Acta Physiol Lat Am | 靜脈注射 Procaine 直接導致高鐵血紅蛋白血症之病案系列報告 |
| [14246695](https://pubmed.ncbi.nlm.nih.gov/14246695/) | 1965 | Case series | Lancet | Lignocaine 引發高鐵血紅蛋白血症，機轉與 Procaine 代謝物氧化作用類似 |
| [705003](https://pubmed.ncbi.nlm.nih.gov/705003/) | 1978 | Case series | Rev Esp Anestesiol Reanim | 全身麻醉中使用 Novocaine 皮下浸潤後，新生兒發生高鐵血紅蛋白血症 |
| [5644303](https://pubmed.ncbi.nlm.nih.gov/5644303/) | 1968 | In vitro | Am J Obstet Gynecol | Procaine HCl 及代謝物 PABA 均可穿越人類胎盤屏障，具胎兒暴露風險 |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Procaine 的不重複許可證共 **90 張**：有效單方 4 張、有效複方 9 張、已註銷 77 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（4 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 內衛藥製字第002992號 | 鹽酸普魯卡因注射液２％ | 注射劑 | 信東生技股份有限公司 | 2028/05/25 | 局部麻醉 |
| 內衛藥製字第002996號 | 鹽酸普魯卡因注射液１％ | 注射劑 | 信東生技股份有限公司 | 2028/05/25 | 局部麻醉用 |
| 內衛藥製字第004913號 | "濟生"鹽酸普魯卡因注射液 | 注射劑 | 濟生醫藥生技股份有限公司 | 2028/05/25 | 局部麻醉 |
| 衛署藥製字第009699號 | 鹽酸普魯卡因注射液１％２公撮 | 注射劑 | 榮民製藥股份有限公司 | 2028/05/13 | 局部麻醉 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（9 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 內衛藥製字第011125號 | 〝人人〞鹽酸四環素肌肉注射劑 | TETRACYCLINE HCL (EQ TO TETRACYCLINE HYDROCHLORIDE)、PROCAINE… | 注射劑 | 支氣管炎、扁桃腺炎、肺炎、急性心內膜炎、膽道炎、急性胃腸炎、膀胱炎、腎盂炎、淋菌性尿道炎、子宮炎、乳房炎、產褥熱、腹膜炎、中耳炎、眼部感染症、癤病、敗血症、蜂窩織炎 |
| 內衛藥製字第015192號 | 明晶可寧點眼劑 | PROCAINE HCL、TAURINE (EQ TO 2-AMINOETHANE SULFONIC ACID)、HOM… | 點眼液劑 | 急慢性結膜炎、眼瞼緣炎、麥粒腫、急性淚腺炎、角膜潰瘍 |
| 衛署藥製字第016222號 | "溫士頓"舒鼻喜噴鼻液 | DIPHENHYDRAMINE HCL、NAPHAZOLINE HCL、PROCAINE HCL | 鼻用噴液劑 | 鼻炎、副鼻腔炎、過敏性鼻炎及流鼻水、鼻塞、鼻出血 |
| 衛署藥製字第019585號 | "長安"汎鼻寧噴劑 | DIPHENHYDRAMINE HCL、NAPHAZOLINE HCL、PROCAINE HCL | 鼻用氣化噴霧劑 | 鼻炎、副鼻腔炎、過敏性鼻炎（鼻塞、流鼻水）鼻出血 |
| 衛署藥製字第023380號 | "健康"宜鼻噴鼻液 | NAPHAZOLINE HCL、DIPHENHYDRAMINE HCL、PROCAINE HCL | 鼻用噴液劑 | 急慢性鼻炎、過敏性鼻炎、副鼻腔炎、鼻塞、鼻充血 |
| 衛署藥製字第025931號 | "成大" 愛鼻爽點鼻液 | DIPHENHYDRAMINE HCL、NAPHAZOLINE HCL、PROCAINE HCL | 外用液劑 | 鼻炎、副鼻腔炎、過敏性鼻炎所引起之鼻塞、流鼻水、鼻出血 |
| 衛署藥製字第027760號 | 舒敏明眼藥水 | ZINC SULFATE、MAFENIDE (HOMOSULFAMINE)、TAURINE (EQ TO 2-AMINO… | 點眼液劑 | 急性結膜炎、眼瞼緣炎、麥粒腫、急性淚腺炎、角膜潰瘍。 |
| 衛署藥製字第043489號 | "約克" 舒鼻爽噴鼻液 | PROCAINE HCL、DIPHENHYDRAMINE HCL、NAPHAZOLINE HCL | 鼻用噴液劑 | 鼻炎、副鼻腔炎、過敏性鼻炎所引起之流鼻水、鼻塞及鼻出血。 |
| 衛署藥製字第049759號 | “中美”鼻舒康噴鼻液 | PROCAINE HCL、NAPHAZOLINE HCL、DIPHENHYDRAMINE HCL | 鼻用噴液劑 | 鼻炎、副鼻腔炎、過敏性鼻炎所引起之流鼻水、鼻塞及鼻出血。 |

<details><summary><strong>已註銷</strong>（77 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第000477號</td><td>鹽酸普魯卡因注射液２％</td><td>PROCAINE HCL</td><td>2013/10/15</td></tr><tr><td>內衛藥製字第002081號</td><td>特得素針</td><td>PROCAINE HCL、TETRACYCLINE HCL (EQ TO TETRACYCLINE HYDROCHLOR…</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第002299號</td><td>鹽酸普魯卡因注射液</td><td>PROCAINE HCL</td><td>2013/10/03</td></tr><tr><td>內衛藥製字第002557號</td><td>鎮吐能注射液</td><td>PROCAINE HCL、PHENOL (CARBOLIC ACID)、BROMISOVALUM ( EQ TO BRO…</td><td>2023/07/21</td></tr><tr><td>內衛藥製字第002997號</td><td>鹽酸普魯卡因注射液０．５％</td><td>PROCAINE HCL</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第003291號</td><td>普魯卡因針</td><td>PROCAINE HCL</td><td>2013/04/08</td></tr><tr><td>內衛藥製字第003539號</td><td>痔莫痛坐劑</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、BENZOCAINE (ET…</td><td>1989/06/15</td></tr><tr><td>內衛藥製字第006179號</td><td>齒痛可癒注射液２公撮</td><td>PROCAINE HCL、TETRACAINE HCL、EPINEPHRINE HCL、SODIUM BISULFITE…</td><td>1989/12/31</td></tr><tr><td>內衛藥製字第006644號</td><td>補祿卡因注射液</td><td>PROCAINE HCL</td><td>1991/06/05</td></tr><tr><td>內衛藥製字第007470號</td><td>安治吐寧注射液</td><td>BROMISOVALUM ( EQ TO BROMOVALERYLUREA) ( EQ TO BROMVALETONE)…</td><td>1997/12/22</td></tr><tr><td>內衛藥製字第010191號</td><td>目藥水”金馬”　　　　　　　　　　　　　　　　　　　　　　　 G</td><td>PROCAINE HCL、EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、M…</td><td>1989/08/17</td></tr><tr><td>內衛藥製字第013333號</td><td>鹽酸普魯卡因腎上腺素注射液</td><td>EPINEPHRINE (ADRENALINEPIRENAMINE)、PROCAINE HCL</td><td>1989/12/31</td></tr><tr><td>內衛藥輸字第001412號</td><td>兩黴素目藥水</td><td>PROCAINE HCL、TYROTHRICIN、CHLORAMPHENICOL</td><td>1999/09/22</td></tr><tr><td>內衛藥輸字第001414號</td><td>沙克鼻塞Ｃ</td><td>PROCAINE HCL、OCTODRINE PHOSPHATE、CHLORAMPHENICOL</td><td>1999/09/22</td></tr><tr><td>內衛藥輸字第001415號</td><td>沙克鼻塞</td><td>PYRILAMINE MALEATE (MEPYRAMINE MALEATE)、PROCAINE HCL、OCTODRI…</td><td>1999/09/22</td></tr><tr><td>內衛藥輸字第001853號</td><td>鹽酸普魯卡因</td><td>PROCAINE HCL</td><td>1986/01/17</td></tr><tr><td>內衛藥輸字第001930號</td><td>複合維他命Ｂ注射劑</td><td>RIBOFLAVIN (VIT B2)、PYRIDOXINE HCL、NIACINAMIDE (NICOTINAMIDE…</td><td>1986/04/30</td></tr><tr><td>內衛藥輸字第002394號</td><td>痔良軟膏</td><td>PHENOL (CARBOLIC ACID)、PROCAINE HCL、CETYL ALCOHOL (CETANOL)(…</td><td>1986/07/11</td></tr><tr><td>內衛藥輸字第002516號</td><td>格路比路針</td><td>SULPYRINE (EQ TO DIPYRONE )、PROCAINE HCL、MONOSODIUM GLUTAMAT…</td><td>1984/12/31</td></tr><tr><td>內衛藥輸字第002845號</td><td>痔良栓劑</td><td>PROCAINE HCL、COLON BACILLI KILLED</td><td>1986/07/11</td></tr><tr><td>內衛藥輸字第002999號</td><td>因普里托</td><td>CAFFEINE、PROCAINE HCL</td><td>1990/09/13</td></tr><tr><td>內衛藥輸字第003110號</td><td>速定痛針</td><td>PROCAINE (P-AMINOBENZOYL-DIETHYLAMINOETHANOL)、NIACIN (NICOTI…</td><td>1986/04/30</td></tr><tr><td>內衛藥輸字第003514號</td><td>撲痛針</td><td>CAMPHOR、SODIUM SALICYLATE、SODIUM CHLORIDE、PROCAINE HCL</td><td>1986/02/12</td></tr><tr><td>內衛藥輸字第003709號</td><td>鹽酸普羅加因</td><td>PROCAINE HCL</td><td>1986/03/15</td></tr><tr><td>內衛藥輸字第004202號</td><td>鹽酸普魯卡因</td><td>PROCAINE HCL</td><td>1985/08/02</td></tr><tr><td>內衛藥輸字第004347號</td><td>康壽寧針</td><td>BETA-NAPHTHOQUINONE SEMICARBAZONE (NAFTAZONE)、PROCAINE HCL</td><td>1987/03/24</td></tr><tr><td>內衛藥輸字第004587號</td><td>特製普魯卡因</td><td>SODIUM CHLORIDE、PROCAINE HCL</td><td>2000/10/16</td></tr><tr><td>內衛藥輸字第004722號</td><td>牙保安</td><td>PROPOXYCAINE HCL、LEVO NORDEFRIN (L-NORDEFRIN HCL)、PROCAINE H…</td><td>1986/01/18</td></tr><tr><td>內衛藥輸字第005872號</td><td>懸濁水性盤尼西林</td><td>PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)、PROC…</td><td>1988/11/08</td></tr><tr><td>內衛藥輸字第006184號</td><td>服斯　針</td><td>POTASSIUM GUAIACOLSULFONATE、DL-METHYLEPHEDRINE HCL、CAFFEINE…</td><td>1986/06/02</td></tr><tr><td>內衛藥輸字第006245號</td><td>必拉啥通西</td><td>IODOPYRACET、PROCAINE HCL</td><td>1999/10/25</td></tr><tr><td>內衛藥輸字第006980號</td><td>痔樂保命</td><td>DIPHENHYDRAMINE HCL、ORONINE-D、ALUMINUM、EPHEDRINE HCL (EQ TO…</td><td>1999/09/22</td></tr><tr><td>衛署成製字第006559號</td><td>噴腳好液</td><td>ETHACRIDINE LACTATE MONOHYDRATE (ACRINOL)、ASPIRIN、PROCAINE H…</td><td>2013/10/03</td></tr><tr><td>衛署藥製字第000230號</td><td>蒙汝康恩須古布羅命注射液</td><td>EPINEPHRINE HCL、DIMETHYLAMINOETHYL-BETA-BENZILAMIDE HCL、SCOP…</td><td>1991/05/06</td></tr><tr><td>衛署藥製字第000395號</td><td>蒙汝康恩注射液</td><td>PROCAINE HCL、PYRABITAL (AMINOPYRINE+BARBITAL)、DIMETHYLAMINOE…</td><td>1991/05/06</td></tr><tr><td>衛署藥製字第007386號</td><td>鹽酸普魯卡因注射液</td><td>PROCAINE HCL</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第011456號</td><td>"德星" 佛賜佳因注射液</td><td>CAFFEINE、SCOPOLAMINE HBR、PROCAINE HCL、ATROPINE SULFATE、PYRAB…</td><td>1997/12/22</td></tr><tr><td>衛署藥製字第013982號</td><td>鹽酸普魯卡因腎上腺注射液</td><td>EPINEPHRINE (ADRENALINEPIRENAMINE)、PROCAINE HCL</td><td>2016/09/08</td></tr><tr><td>衛署藥製字第014304號</td><td>止咳注射液</td><td>DL-METHYLEPHEDRINE HCL、POTASSIUM GUAIACOLSULFONATE、CAFFEINE…</td><td>2014/07/18</td></tr><tr><td>衛署藥製字第027422號</td><td>痔安軟膏</td><td>GLYCYRRHETIC ACID (EQ TO GLYCYRRHETINIC ACID)、BENZOCAINE (ET…</td><td>1994/08/17</td></tr><tr><td>衛署藥製字第033759號</td><td>蒙汝康恩須古布羅命注射液</td><td>EPINEPHRINE HCL、DIMETHYLAMINOETHYL-BETA-BENZILAMIDE HCL、PROC…</td><td>1992/01/13</td></tr><tr><td>衛署藥製字第033770號</td><td>蒙汝康恩注射液</td><td>DIMETHYLAMINOETHYL-BETA-BENZILAMIDE HCL、EPINEPHRINE HCL、PROC…</td><td>1992/01/13</td></tr><tr><td>衛署藥輸字第000239號</td><td>鹽酸普魯卡因</td><td>PROCAINE HCL</td><td>2014/01/28</td></tr><tr><td>衛署藥輸字第002594號</td><td>格如科</td><td>GLUTAMIC ACID L-、THIAMINE HYDROCHLORIDE、PROCAINE HCL、GONADOT…</td><td>1986/11/06</td></tr><tr><td>衛署藥輸字第003370號</td><td>樂拔齒２％</td><td>EPINEPHRINE (ADRENALINEPIRENAMINE)、PROCAINE HCL</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第003371號</td><td>樂拔齒４％</td><td>EPINEPHRINE (ADRENALINEPIRENAMINE)、PROCAINE HCL</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第003830號</td><td>克瀾新胃針</td><td>SOLUTION OF TOTAL HYDROLYSATE OF VENTRICULAR &amp; DU*、PROCAINE…</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第004166號</td><td>福樂補滋注射液</td><td>NIACINAMIDE (NICOTINAMIDE)、PROCAINE (P-AMINOBENZOYL-DIETHYLA…</td><td>1986/02/21</td></tr><tr><td>衛署藥輸字第005815號</td><td>羅佛卡因</td><td>PROCAINE HCL、L-NOREPINEPHRINE BITARTRATE、PROPOXYCAINE HCL</td><td>1992/11/11</td></tr><tr><td>衛署藥輸字第006423號</td><td>優體素膠囊</td><td>HEMATOPORPHYRIN、GINSENG EXTRACT SICC.、PROCAINE HCL</td><td>1990/10/08</td></tr><tr><td>衛署藥輸字第006885號</td><td>菩樂薩注射液</td><td>PROCAINE HCL、SODIUM SALICYLATE</td><td>1994/01/27</td></tr><tr><td>衛署藥輸字第007166號</td><td>捷力旺錠</td><td>TOCOPHEROL-ALPHA-D ACID SUCCINATE、NYLIDRIN (SULFONATED STYRO…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第007669號</td><td>維我百達膠囊</td><td>TOCOPHEROL ACETATE ALPHA (EQ TO VIT E ACETATE) (EQ TO VITAMI…</td><td>1996/01/11</td></tr><tr><td>衛署藥輸字第007892號</td><td>保樂得華膠囊</td><td>HEMATOPORPHYRIN、PROCAINE HCL</td><td>1988/05/07</td></tr><tr><td>衛署藥輸字第008964號</td><td>安得痔栓劑</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、BENZOCAINE (ET…</td><td>1986/01/17</td></tr><tr><td>衛署藥輸字第009004號</td><td>安痔軟膏</td><td>PROCAINE HCL、DIPHENHYDRAMINE、EPHEDRINE HCL (EQ TO EPHEDRINE…</td><td>1986/01/17</td></tr><tr><td>衛署藥輸字第009063號</td><td>生多派爾軟膏</td><td>ZINC OXIDE、DIPHENHYDRAMINE HCL、PROCAINE (P-AMINOBENZOYL-DIET…</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第009427號</td><td>益得康糖衣錠</td><td>HYDROXOCOBALAMIN ACETATE、NIACIN (NICOTINIC ACID)、PROCAINE HC…</td><td>1987/11/06</td></tr><tr><td>衛署藥輸字第009486號</td><td>療痔栓劑</td><td>ALLANTOIN、ZINC OXIDE、GLYCYRRHETIC ACID (EQ TO GLYCYRRHETINIC…</td><td>2000/08/11</td></tr><tr><td>衛署藥輸字第009573號</td><td>百賜隆軟膠囊</td><td>HEMATOPORPHYRIN HCL、PROCAINE HCL</td><td>1987/02/27</td></tr><tr><td>衛署藥輸字第010391號</td><td>利達平６：３：３注射劑</td><td>PENICILLIN G (BENZATHINE)、PENICILLIN G (SODIUM)、PENICILLIN G…</td><td>1984/12/31</td></tr><tr><td>衛署藥輸字第010518號</td><td>安明眼藥水</td><td>CHONDROITIN SULFATE、D-BORNEOL、PROCAINE HCL、TAURINE (EQ TO 2-…</td><td>1986/12/17</td></tr><tr><td>衛署藥輸字第010685號</td><td>愛樂目藥水</td><td>NAPHAZOLINE HCL、CHLOROBUTANOL (TRICHLORISOBUTYLIC ALCOHOL)、Z…</td><td>1993/03/17</td></tr><tr><td>衛署藥輸字第011828號</td><td>舒樂目藥</td><td>CHONDROITIN SULFATE SODIUM (EQ TO SODIUM CHONDROITIN SULFATE…</td><td>1989/01/05</td></tr><tr><td>衛署藥輸字第011849號</td><td>痔瘡克軟膏</td><td>PROCAINE (P-AMINOBENZOYL-DIETHYLAMINOETHANOL)、ZINC OXIDE、BEN…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第011850號</td><td>痔瘡克栓劑</td><td>ZINC OXIDE、BENZOCAINE (ETHYL AMINOBENZOATE)、PROCAINE (P-AMIN…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第011935號</td><td>複方維他命Ｂ注射液</td><td>THIAMINE(HCL)、NIACINAMIDE (NICOTINAMIDE)、VITAMIN B6 (HCL)、RI…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第013769號</td><td>鹽酸普魯卡因粉劑</td><td>PROCAINE HCL</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第014640號</td><td>鹽酸普卡因</td><td>PROCAINE HCL</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第014656號</td><td>安痔軟膏</td><td>DIPHENHYDRAMINE、PROCAINE HCL、BENZOCAINE (ETHYL AMINOBENZOATE…</td><td>1998/01/06</td></tr><tr><td>衛署藥輸字第014659號</td><td>安得痔栓劑</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、ZINC OXIDE、BEN…</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第014678號</td><td>牙保安注射液</td><td>PROPOXYCAINE HCL、LEVO NORDEFRIN (L-NORDEFRIN HCL)、PROCAINE H…</td><td>1992/11/11</td></tr><tr><td>衛署藥輸字第018329號</td><td>普魯卡因/基素黴素鉀合劑注射用粉劑</td><td>PENICILLIN G (PROCAINE)</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第019992號</td><td>鹽酸普魯卡因</td><td>PROCAINE HCL</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第021044號</td><td>維我百達膠囊</td><td>INOSITOL (MESO-INOSITOL)、LYSINE L- HCL H2O、HEMATOPORPHYRIN、V…</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第021920號</td><td>安痔軟膏</td><td>EPHEDRINE HCL (EQ TO EPHEDRINE HYDROCHLORIDE)、BENZOCAINE (ET…</td><td>2009/12/10</td></tr><tr><td>衛署藥陸輸字第000287號</td><td>鹽酸普魯卡因</td><td>Procaine Hydrochloride</td><td>2019/03/12</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

---

## 安全性考量

**藥物交互作用（共 15 筆，依嚴重程度排列）：**

| 交互藥物 | 嚴重程度 |
|---------|---------|
| Nitrous acid | ⚠️ Major |
| Sulfasalazine | Moderate |
| Lidocaine（局部）、Lidocaine（眼科） | Moderate |
| Benzocaine（局部） | Moderate |
| Cocaine（局部）、Cocaine（鼻腔） | Moderate |
| Tetracaine（眼科）、Tetracaine（局部） | Moderate |
| Oxybuprocaine（眼科） | Moderate |
| Cinchocaine（局部） | Moderate |
| Laronidase | Minor |
| Hyaluronidase | Minor |
| Doxorubicin、Doxorubicin（liposomal） | Minor |

> Nitrous acid 與 Procaine 合用具重大交互作用（Major），需特別注意。多種局部麻醉藥合用（同類疊加效應）均列 Moderate 級別，臨床上應避免同時使用多種酯類或醯胺類局部麻醉藥。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 最高分預測適應症（高鐵血紅蛋白血症）是 Procaine 代謝物 PABA 的**已知毒性機轉**，所有相關文獻一致記錄為不良反應，而非治療效益；對高鐵血紅蛋白血症患者使用 Procaine 構成用藥禁忌，此方向完全不具再利用價值。

**若要推進需要：**
- **優先轉向評估 Rank 8（肌腱炎，Tendinitis，L3 證據，建議 Proceed with Guardrails）**：有 1 篇 RCT（PMID [23494116](https://pubmed.ncbi.nlm.nih.gov/23494116/)，2013）及 1 篇 2022 年 Cohort 研究（PMID [35480510](https://pubmed.ncbi.nlm.nih.gov/35480510/)）支持 1% Procaine 局部注射（神經療法）用於棘上肌肌腱病變的止痛效益，是目前最具現代臨床根據的再利用方向
- 同步評估 **Rank 7（纖維肌痛症，Fibromyalgia）**：有歷史性觸發點注射文獻，但需新的現代 RCT 驗證
- 補充完整 DrugBank MOA 資料（資料缺口 DG001），強化後續機轉關聯分析
- 針對肌腱病變適應症設計現代雙盲 RCT，確立 Procaine 神經療法注射的療效與最適劑量、頻次及安全監測標準

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表中三張 procaine penicillin 製劑 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

