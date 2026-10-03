---
layout: default
title: Cefoperazone
parent: 高證據等級 (L1-L2)
nav_order: 57
evidence_level: L2
indication_count: 10
---

# Cefoperazone
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Cefoperazone：從廣譜細菌感染到肺炎（Pneumonia）

## 一句話總結

Cefoperazone 是第三代頭孢菌素類抗生素，原本用於治療感受性細菌引起的廣譜感染（呼吸道、泌尿道、腹腔內感染、敗血病等）。
TxGNN 模型預測它可能對**肺炎（Pneumonia）** 具有更系統性的應用價值，尤其是院內肺炎及多重抗藥性（MDR）肺炎，
目前有 **2 個臨床試驗**和 **20 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 廣譜細菌感染（上下呼吸道感染、泌尿道感染、腹膜炎、敗血病等） |
| 預測新適應症 | 肺炎（Pneumonia） |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L2 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 43 張（有效單方 11／有效複方 7／已註銷 25） |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏完整的作用機轉資料（DrugBank 尚未回傳詳細 MOA）。根據已知資訊，Cefoperazone 屬第三代頭孢菌素，透過與細菌青黴素結合蛋白（PBP）共價結合、抑制肽聚醣交叉連結，破壞細胞壁合成而達到殺菌效果。與 Sulbactam 組合後，可抑制細菌產生的 β-lactamase 酶，有效擴展對多重抗藥性病株（包括鮑曼不動桿菌）的抗菌覆蓋範圍。

原適應症（廣譜細菌感染）與肺炎之間的關聯性極為直接。肺炎鏈球菌（*Streptococcus pneumoniae*）、克雷伯氏肺炎桿菌（*Klebsiella pneumoniae*）、假單胞菌（*Pseudomonas* spp.）及鮑曼不動桿菌等均為 Cefoperazone 的主要抗菌目標，同時也是院內肺炎（HAP）與呼吸器相關肺炎（VAP）的常見致病菌。

<!-- review:begin cefoperazone-acinetobacter-2026-10-03 -->

> **查核加註（2026-10-03）**：Cefoperazone 單方仿單列出的活性菌種有肺炎鏈球菌、克雷伯氏菌、假單胞菌等，沒有不動桿菌，且把 Acinetobacter 列為排除菌屬；對鮑曼不動桿菌的活性主要來自與 sulbactam 的複方。原文保留。依據：[Drugs@FDA：CEFOBID（cefoperazone）仿單（2017），Microbiology](https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/050551s045lbl.pdf)。

<!-- review:end cefoperazone-acinetobacter-2026-10-03 -->

特別是 Cefoperazone/Sulbactam 組合，因 Sulbactam 對鮑曼不動桿菌具天然固有抑制活性，使其成為應對廣泛耐藥（XDR）院內肺炎的重要選擇。現有一項已發表的隨機非劣性試驗支持其療效，機轉上的合理性充分。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01280461](https://clinicaltrials.gov/study/NCT01280461) | Phase 3 | 未知 | 142 | 開放性隨機比較試驗，直接評估 Cefoperazone/Sulbactam vs Cefepime 用於院內肺炎（HAP）及醫療相關肺炎（HCAP）之療效與安全性，療程 7–21 天，已有對應發表論文（PMID 31138577） |
| [NCT02060149](https://clinicaltrials.gov/study/NCT02060149) | Phase 1/2 | 未知 | 90 | 多中心隨機研究，探討霧化鹼性溶液合併 Cefoperazone-Sulbactam 及 Minocycline，用於廣泛耐藥鮑曼不動桿菌（XDRAB）肺炎之療效，假說為改變氣道 pH 環境可抑制 XDRAB 生物活性 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31138577](https://pubmed.ncbi.nlm.nih.gov/31138577/) | 2019 | RCT | Antimicrobial Agents and Chemotherapy | 隨機非劣性試驗顯示 Cefoperazone-Sulbactam 治療 HAP/HCAP 不劣於 Cefepime，為迄今最重要的直接比較證據 |
| [1643821](https://pubmed.ncbi.nlm.nih.gov/1643821/) | 1992 | RCT | Diagnostic Microbiology and Infectious Disease | 多中心隨機前瞻試驗比較 Cefoperazone vs Ceftriaxone 治療院內肺炎，整體成功率分別為 80% vs 70%，療效相當 |
| [34168466](https://pubmed.ncbi.nlm.nih.gov/34168466/) | 2021 | Cohort | Infection and Drug Resistance | 比較 Cefoperazone-Sulbactam vs Piperacillin-Tazobactam 用於 HAP/VAP 治療的臨床療效 |
| [34871744](https://pubmed.ncbi.nlm.nih.gov/34871744/) | 2022 | Cohort | International Journal of Antimicrobial Agents | 比較 Cefoperazone-Sulbactam vs Piperacillin-Tazobactam 用於老年肺炎患者，分析臨床有效性與安全性 |
| [41368483](https://pubmed.ncbi.nlm.nih.gov/41368483/) | 2025 | Cohort | Infection and Drug Resistance | 多中心回溯研究評估高劑量 vs 標準劑量 Cefoperazone-Sulbactam 用於嚴重感染（含多重抗藥性菌株）之效果與安全性 |
| [24726664](https://pubmed.ncbi.nlm.nih.gov/24726664/) | 2014 | Cohort | International Journal of Infectious Diseases | 分析老年碳青黴烯耐藥鮑曼不動桿菌（CRAB）院內肺炎之臨床特徵，並評估 Cefoperazone/Sulbactam 組合療法的體外抗菌活性 |
| [6456894](https://pubmed.ncbi.nlm.nih.gov/6456894/) | 1981 | Cohort | Drugs | Cefoperazone 肺炎臨床試驗（n=15），分離菌株包括金黃色葡萄球菌、克雷伯菌、肺炎雙球菌及假單胞菌，均對 Cefoperazone 敏感 |
| [35924047](https://pubmed.ncbi.nlm.nih.gov/35924047/) | 2022 | Review | Frontiers in Pharmacology | 以模型引導藥物開發（MIDD）方法評估新 Cefoperazone/Sulbactam 3:1 組合對腸桿菌科感染之 PK/PD 分析及殺菌效果 |
| [2671141](https://pubmed.ncbi.nlm.nih.gov/2671141/) | 1989 | Review | Infectious Disease Clinics of North America | 第三代頭孢菌素類藥物綜合評述，說明 Cefoperazone 對假單胞菌具活性，為該亞群中廣譜抗菌代表 |
| [17120738](https://pubmed.ncbi.nlm.nih.gov/17120738/) | 2006 | Cohort | Journal of Huazhong University of Science and Technology | 比較 Moxifloxacin vs Cefoperazone + Azithromycin 用於社區獲得性肺炎（CAP）靜脈治療之療效與耐受性 |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Cefoperazone 的不重複許可證共 **43 張**：有效單方 11 張、有效複方 7 張、已註銷 25 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（11 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第028538號 | "生達"綠膿黴素注射劑１公克（西弗匹拉隆） | 注射劑 | 生達化學製藥股份有限公司 | 2030/03/17 | 適用於治療感受性細菌所引起的下列感染：上下呼吸道感染、上下泌尿道感染、腹膜炎、膽囊炎、膽管炎及其他腹腔內感染、敗血病、腦膜炎皮膚及軟組織感染、骨關節感染、骨盆發炎、子宮內膜炎、淋病… |
| 衛署藥製字第028539號 | "生達"綠膿黴素注射劑５００公絲（西弗匹拉隆） | 注射劑 | 生達化學製藥股份有限公司 | 2030/03/17 | 適用於治療由感受性細菌所引起的下列感染：上下呼吸道感染、上下泌尿道感染、腹膜炎、膽囊炎、膽管炎、及其他腹腔內感染、敗血病、腦膜炎、皮膚及軟組織感染、骨關節感染、骨盆發炎、淋病及其他… |
| 衛署藥製字第029351號 | "優良"優頌黴素注射劑１公克（西弗匹拉隆） | 注射劑 | 優良化學製藥股份有限公司 | 2029/01/07 | 治療具有感受性細菌所引起之感染症、如呼吸道器官感染、腹膜炎及腹腔內感染、細菌性敗血症、皮膚及皮膚組織感染、泌尿器官感染、骨盆炎症、子宮內膜炎及其他女性生殖器官感染症 |
| 衛署藥製字第034331號 | "瑞安"速妥注射劑（西弗匹拉隆） | 乾粉注射劑 | 瑞安大藥廠股份有限公司 | 2031/09/13 | 由感受性細菌所引起之下列感染症：呼吸道感染症、腹膜炎及其他腹腔內感染症、細菌性敗血症、皮膚及皮膚組織之感染症、骨盆炎症性疾患、子宮內膜炎及其他女性生殖道感染症。 |
| 衛署藥製字第036763號 | 清華注射劑（西弗匹拉隆） | 注射劑 | 瑞士藥廠股份有限公司 | 2028/09/21 | 葡萄球菌、鏈球菌、肺炎雙球菌、腦膜炎球菌及其他具有感受性細菌引起之感染性。 |
| 衛署藥製字第039078號 | 歐寶賜福注射劑（西弗匹拉隆） | 乾粉注射劑 | 中國化學製藥股份有限公司台南三廠 | 2030/07/22 | 適用於治療由感受性細菌所引起的下列感染：上、下呼吸道感染、上、泌尿道感染、腹膜炎、膽囊炎、膽管炎及其它腹腔內感染、敗血病、腦膜炎、皮膚及軟組織感染、骨關節感染、骨盆發炎、淋病及其它… |
| 衛部藥陸輸字第000909號 | 頭孢匹拉腙鈉 | （粉） | 龍大生技股份有限公司 | 2029/12/09 | 抗生素 |
| 衛部藥陸輸字第001007號 | 頭孢哌𠯤酮鈉鹽-碸丙內醯胺鈉鹽 | （粉） | 宇直泰貿易股份有限公司 | 2031/08/11 | 抗生素 |
| 衛部藥陸輸字第001008號 | 頭孢哌𠯤酮鈉鹽-碸丙內醯胺鈉鹽 | （粉） | 龍大生技股份有限公司 | 2026/08/11 | 抗生素。 |
| 衛部藥陸輸字第001241號 | 頭孢匹拉腙納鹽 | （粉） | 台灣荃新股份有限公司 | 2030/11/05 | 抗生素 |
| 衛部藥陸輸字第001273號 | 頭孢哌𠯤酮鈉鹽-碸丙內醯胺鈉鹽 | （粉） | 台灣荃新股份有限公司 | 2031/04/27 | 抗生素 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（7 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第029078號 | "永信"信福黴素注射劑（西弗匹拉隆） | CEFOPERAZONE(AS SODIUM)STERILE、CEFOPERAZONE(AS SODIUM)STERIL… | 乾粉注射劑 | 由感受性細菌所引起的下列感染症：呼吸道感染症、腹膜炎及其他腹腔內感染症、細菌性敗血症、皮膚及皮膚組織之感染症、骨盆炎症性疾患、子宮內膜炎及其他女性生殖道感染症 |
| 衛署藥製字第035473號 | "政德" 歐力隆乾粉注射劑 | CEFOPERAZONE (SODIUM)、CEFOPERAZONE (SODIUM) | 乾粉注射劑 | 由感受性細菌所引起的下列感染症：呼吸道感染症、腹膜炎及其他 腹腔內感染症、細菌性敗血症、皮膚及皮膚組織之感染症、骨盆炎 症性疾患、子宮內膜炎及其他女性生殖道感染症。 |
| 衛署藥製字第036510號 | 安治妥肌肉/靜脈乾粉注射劑 | CEFOPERAZONE (SODIUM)、CEFOPERAZONE (SODIUM) | 乾粉注射劑 | 適用於治療由感受性細菌所引起的下列感染：上下呼吸道感染、上下泌尿道感染、腹膜炎、膽囊炎、膽管炎、及其他腹腔內感染、敗血病、腦膜炎、皮膚及軟組織感染、骨關節感染、骨盆發炎、淋病及其他… |
| 衛署藥製字第039094號 | "榮民"舒復得注射劑(西弗匹拉隆) | CEFOPERAZONE(AS SODIUM)STERILE、CEFOPERAZONE(AS SODIUM)STERIL… | 乾粉注射劑 | 葡萄球菌、鏈球菌、肺炎雙球菌、腦膜炎球菌及其他具有感受性細菌引起之感染性。 |
| 衛部藥製字第058156號 | 博益欣注射劑 | SULBACTAM(AS SODIUM)STERILE、SULBACTAM(AS SODIUM)STERILE、SULB… | 乾粉注射劑 | 適用於治療由感受性細菌所引起的下列感染：上、下呼吸道感染、上、下泌尿道感染、腹膜炎、膽囊炎、膽管炎及其他腹腔內感染、骨盆發炎、子宮內膜炎及其他生殖道感染、以及創傷燙傷、手術後之二次… |
| 衛部藥製字第060278號 | 賜復坦乾粉靜脈注射劑 | SULBACTAM(AS SODIUM)STERILE、SULBACTAM(AS SODIUM)STERILE、SULB… | 乾粉注射劑 | 適用於治療由感受性細菌所引起的下列感染：上、下呼吸道感染、上、下泌尿道感染、腹膜炎、膽囊炎、膽管炎及其它腹腔內感染、骨盆發炎、子宮內膜炎及其它生殖道感染、以及創傷燙傷、手術後之二次… |
| 衛部藥製字第061039號 | 布洛坦乾粉注射劑 | SULBACTAM(AS SODIUM)STERILE、CEFOPERAZONE SODIUM、CEFOPERAZONE… | 乾粉注射劑 | 適用於治療由感受性細菌所引起的下列感染：上、下呼吸道感染、上、下泌尿道感染、腹膜炎、膽囊炎、膽管炎及其他腹腔內感染、骨盆發炎、子宮內膜炎及其他生殖道感染、以及創傷燙傷、手術後之二次… |

<details><summary><strong>已註銷</strong>（25 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第025325號</td><td>先復癒黴素肌肉及靜脈注射劑１公克（西弗匹拉隆）</td><td>CEFOPERAZONE (SODIUM)</td><td>2013/10/08</td></tr><tr><td>衛署藥製字第025397號</td><td>先復癒黴素肌肉及靜脈注射劑２公克（西弗匹拉隆）</td><td>CEFOPERAZONE (SODIUM)</td><td>2013/10/08</td></tr><tr><td>衛署藥製字第025398號</td><td>先復癒黴素肌肉及靜脈注射劑０．５公克（西弗匹拉隆）</td><td>CEFOPERAZONE (SODIUM)</td><td>2013/10/08</td></tr><tr><td>衛署藥製字第029093號</td><td>欣朗注射劑５００公絲（西弗匹拉隆）</td><td>CEFOPERAZONE (SODIUM)</td><td>1996/04/27</td></tr><tr><td>衛署藥製字第030625號</td><td>西弗宗注射劑０．５公克、１公克（西弗拉隆）</td><td>CEFAZOLIN (SODIUM)、CEFOPERAZONE (SODIUM)</td><td>2015/04/21</td></tr><tr><td>衛署藥製字第030781號</td><td>"聯邦" 優榮注射劑０．５公克、１公克（西弗匹拉隆）</td><td>CEFOPERAZONE (SODIUM)、CEFOPERAZONE (SODIUM)</td><td>2023/08/15</td></tr><tr><td>衛署藥製字第032061號</td><td>賜復壯注射劑（西弗匹拉隆）</td><td>CEFOPERAZONE (SODIUM)、CEFOPERAZONE (SODIUM)</td><td>2015/01/09</td></tr><tr><td>衛署藥製字第039084號</td><td>喜龍乾粉注射劑（西弗匹拉隆）</td><td>CEFOPERAZONE (SODIUM)、CEFOPERAZONE (SODIUM)</td><td>2016/09/19</td></tr><tr><td>衛署藥製字第039714號</td><td>欣朗注射劑５００公絲（西弗匹拉隆）</td><td>CEFOPERAZONE (SODIUM)</td><td>2016/09/07</td></tr><tr><td>衛署藥輸字第010404號</td><td>西弗匹拉隆鈉</td><td>CEFOPERAZONE SODIUM</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第015658號</td><td>西弗匹拉隆鈉注射用</td><td>CEFOPERAZONE SODIUM</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第016255號</td><td>西弗匹拉隆</td><td>CEFOPERAZONE (SODIUM)</td><td>2000/10/20</td></tr><tr><td>衛署藥輸字第016385號</td><td>西佛朗黴素注射劑２公克</td><td>CEFOPERAZONE (SODIUM)</td><td>1994/03/11</td></tr><tr><td>衛署藥輸字第016565號</td><td>西佛朗黴素注射劑１公克</td><td>CEFOPERAZONE SODIUM</td><td>1994/03/11</td></tr><tr><td>衛署藥輸字第017034號</td><td>達得肌肉注射劑１０００公絲</td><td>CEFOPERAZONE (SODIUM)</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第018246號</td><td>西弗匹拉隆鈉</td><td>CEFOPERAZONE SODIUM</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第019790號</td><td>西弗匹拉隆鈉</td><td>CEFOPERAZONE SODIUM</td><td>2003/03/03</td></tr><tr><td>衛署藥輸字第020357號</td><td>先復癒黴素肌肉及靜脈注射劑１公克</td><td>CEFOPERAZONE SODIUM</td><td>2010/08/24</td></tr><tr><td>衛署藥輸字第020358號</td><td>先復癒黴素肌肉疾靜脈注射劑０．５公克</td><td>CEFOPERAZONE SODIUM</td><td>2010/08/24</td></tr><tr><td>衛署藥輸字第020359號</td><td>先復癒黴素肌肉疾靜脈注射劑二公克</td><td>CEFOPERAZONE SODIUM</td><td>2010/08/24</td></tr><tr><td>衛署藥輸字第020491號</td><td>"艾施多華" 無菌西福博拉樂鈉</td><td>CEFOPERAZONE(AS SODIUM)STERILE</td><td>2009/12/21</td></tr><tr><td>衛署藥輸字第021013號</td><td>斯服幸肌肉注射劑１０００公絲</td><td>LIDOCAINE HCL、CEFOPERAZONE SODIUM</td><td>2005/06/03</td></tr><tr><td>衛署藥陸輸字第000570號</td><td>西弗匹拉隆鈉</td><td>Cefoperazone Sodium</td><td>2024/05/06</td></tr><tr><td>衛部藥製字第060979號</td><td>雪服安注射劑</td><td>CEFOPERAZONE (SODIUM)、CEFOPERAZONE (SODIUM)、CEFOPERAZONE (SO…</td><td>2024/12/18</td></tr><tr><td>衛部藥陸輸字第000837號</td><td>頭孢匹拉腙鈉舒巴坦鈉</td><td>Cefoperazone Sodium &amp; Sulbactam Sodium 1：1 sterile mixture</td><td>2024/05/06</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

---

## 安全性考量

**藥物交互作用**（共 14 項，均為中度，資料來源：DDInter）：

| 交互藥物 | 等級 | 臨床意義 |
|---------|------|---------|
| Ethanol | Moderate | 可能引發 disulfiram-like 反應（潮紅、噁心、心悸），使用期間及停藥後 48–72 小時內應避免飲酒 |
| Warfarin | Moderate | 可能增強抗凝效果，合用時需監測 INR/PT |
| Heparin | Moderate | 與抗凝藥物合用需謹慎，注意出血風險 |
| Amikacin／Amikacin（脂質體） | Moderate | 合用可能增加腎毒性，需監測腎功能及藥物濃度 |
| Gentamicin | Moderate | 同上，氨基糖苷類合用腎毒性風險 |
| Kanamycin / Neomycin / Streptomycin | Moderate | 同上，氨基糖苷類合用注意腎毒性 |
| Chloramphenicol | Moderate | 可能產生拮抗作用，影響抗菌效果 |
| Pemetrexed | Moderate | 影響 Pemetrexed 腎臟清除 |
| Mycophenolic acid | Moderate | 可能影響免疫抑制劑血中濃度 |
| Ethinylestradiol | Moderate | 可能降低口服避孕藥效果 |
| Picosulfuric acid | Moderate | 腸道菌叢改變可能影響藥效 |

安全性警語及禁忌症詳細資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
已有 1 個 Phase 3 隨機比較試驗（NCT01280461，已發表為 PMID 31138577）顯示 Cefoperazone-Sulbactam 治療院內肺炎不劣於 Cefepime，輔以多項世代研究支持其用於 HAP、VAP 及 MDR 肺炎的療效；藥物在台灣擁有 43 張許可證（有效 18 張）且已上市，臨床可及性高，整體證據達 L2 等級。

**若要推進需要：**
- 補充完整的作用機轉資料（查詢 DrugBank API，確認 MOA 及藥物分類）
- 追蹤 NCT01280461 在 ClinicalTrials.gov 的最終狀態（目前顯示「未知」，建議確認是否為 PMID 31138577 之登記試驗）
- 建立 MDR 肺炎患者的安全監測計畫，特別注意與氨基糖苷類（Amikacin、Gentamicin 等）合用時的腎毒性監測
- 補充正式警語、禁忌症及劑量調整資訊（目前資料缺口，需查閱台灣核准仿單）
- 若考慮高劑量方案用於 XDR 菌株，可參考 2025 年多中心回溯研究（PMID 41368483）的安全性數據

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 許可證表中 4 列為 cefoperazone＋sulbactam 複方 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 把鮑曼不動桿菌列為 cefoperazone 主要抗菌目標 | 加註 | [Drugs@FDA：CEFOBID（cefoperazone）仿單（2017），Microbiology](https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/050551s045lbl.pdf) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

