---
layout: default
title: Felodipine
parent: 僅模型預測 (L5)
nav_order: 106
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-16
description: "Felodipine：預測新適應症為因肺部疾病和/或缺氧引起的肺高壓 (pulmonary hypertension owing to lung disease and/or…（證據等級 L4）。原適應症：高血壓、心絞痛"
monitor_inn: "Felodipine"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome", "chronic pulmonary heart disease"]
---

# Felodipine
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

## Felodipine：從高血壓、心絞痛到肺疾病及（或）缺氧所致的肺高壓
{: .text-alpha }

## 一句話總結

Felodipine（非洛地平）是一種鈣離子拮抗劑，原本用於治療高血壓與心絞痛。
TxGNN 模型預測它可能對**因肺部疾病和/或缺氧引起的肺高壓 (pulmonary hypertension owing to lung disease and/or hypoxia)** 有效，
目前**沒有臨床試驗**，僅有 **9 篇文獻**（皆為動物或體外研究），證據屬於早期階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓、心絞痛 |
| 預測新適應症 | 因肺部疾病和/或缺氧引起的肺高壓 (pulmonary hypertension owing to lung disease and/or hypoxia) |
| TxGNN 預測分數 | 0.9991 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 15 張／共 26 張） |
| 許可證數 | 26 張（有效單方 14／有效複方 1／已過期 1／已註銷 10） |
| 建議決策 | Hold |

<!-- review:begin felodipine-moa-2026-10-03 -->

## Felodipine 的作用機轉

<!-- moa-sourced: 2026-10-03 用戶拍板例外，只限附來源的作用機轉段 -->

以下只說明這個藥原本怎麼作用，每一點都摘自官方仿單的藥理段落並附連結；與本頁的老藥新用預測無關，也不構成用藥建議。

- Felodipine 屬二氫吡啶類鈣離子通道阻斷劑，會可逆地與其他鈣離子通道阻斷劑競爭二氫吡啶結合位，阻斷血管平滑肌的電位依賴性鈣離子電流。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a6560584-e39f-47b3-84db-95da1f90fd40)）
- 體外試驗中，它對血管平滑肌的作用大於對心肌的作用。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a6560584-e39f-47b3-84db-95da1f90fd40)）
- 它降血壓主要是因為依劑量降低周邊血管阻力，同時伴隨輕度的反射性心跳加快。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a6560584-e39f-47b3-84db-95da1f90fd40)）

**來源**：[DailyMed：Felodipine Extended-Release Tablets, USP 仿單（Westminster Pharmaceuticals），Clinical Pharmacology／Mechanism of Action 段](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a6560584-e39f-47b3-84db-95da1f90fd40)，版本日期 2023-07-17；查閱日期 2026-10-03。

---

<!-- review:end felodipine-moa-2026-10-03 -->

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為空）。根據已知資訊，Felodipine 屬於二氫吡啶類（dihydropyridine）L 型鈣離子通道阻斷劑，會造成血管平滑肌鬆弛與血管擴張，這也是它在高血壓與心絞痛中的療效基礎。

肺高壓的特徵是肺血管阻力上升，因此從機轉上看，血管擴張作用有可能降低肺血管阻力。前臨床研究也顯示，Felodipine 在缺氧與再氧合模型中具有保護作用，例如保護大鼠近端腎小管免於缺氧損傷、保護人類心房肌免於缺氧再氧合功能障礙。

但這些研究多半是動物或體外實驗，並非直接針對肺高壓病人。尚無臨床證據支持 Felodipine 用於缺氧性肺高壓，目前僅屬於機轉上合理的假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9431863](https://pubmed.ncbi.nlm.nih.gov/9431863/) | 1997 | 體外研究 | Int J Cardiol | Felodipine 可保護人類心房肌，減輕缺氧再氧合造成的功能障礙 |
| [8584414](https://pubmed.ncbi.nlm.nih.gov/8584414/) | 1995 | 體外研究 | Pflugers Arch | Felodipine 透過非鈣依賴機制，保護大鼠近端腎小管免於缺氧損傷 |
| [8394565](https://pubmed.ncbi.nlm.nih.gov/8394565/) | 1993 | 體外研究 | Pflugers Arch | L 型鈣通道阻斷劑影響缺氧誘發的兔近端腎小管細胞內鈣濃度上升 |
| [8160846](https://pubmed.ncbi.nlm.nih.gov/8160846/) | 1994 | 動物研究 | Am J Physiol | 先前的缺氧發作會減弱大鼠主動脈環後續缺氧引起的血管舒張 |
| [8110031](https://pubmed.ncbi.nlm.nih.gov/8110031/) | 1993 | 動物研究 | Arch Int Pharmacodyn Ther | 比較 nicardipine、felodipine、nifedipine 對正常與缺氧大鼠被動迴避行為的影響 |
| [3961832](https://pubmed.ncbi.nlm.nih.gov/3961832/) | 1986 | 動物研究 | Stroke | Nifedipine 與 felodipine 可抑制大鼠缺氧時腦血流的增加 |
| [3343292](https://pubmed.ncbi.nlm.nih.gov/3343292/) | 1988 | 動物研究 | J Cereb Blood Flow Metab | 兩種藥物皆抑制缺氧誘發的大鼠大腦皮質腺苷與肌苷釋放 |
| [3142891](https://pubmed.ncbi.nlm.nih.gov/3142891/) | 1988 | 體外研究 | J Cereb Blood Flow Metab | 血管擴張劑對犬腦動脈再氧合與鈣誘發收縮的影響 |
| [9864178](https://pubmed.ncbi.nlm.nih.gov/9864178/) | 1999 | 體外研究 | Blood | 一氧化氮促進缺氧再氧合後多形核白血球自由基生成 |

以上文獻皆為前臨床研究，沒有 RCT 或針對肺高壓病人的研究。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Felodipine 的不重複許可證共 **26 張**：有效單方 14 張、有效複方 1 張、已過期 1 張（未註銷但有效日期早於資料集日期）、已註銷 10 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（14 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第043724號 | 非洛地平 | （粉） | 臺灣永光化學工業股份有限公司第二廠 | 2030/05/03 | 鈣離子拮抗劑。 |
| 衛署藥製字第043931號 | "十全" 紛落持續釋放膜衣錠１０公絲 | 持續性釋放錠 | 十全實業股份有限公司 | 2030/08/24 | 高血壓、心絞痛。 |
| 衛署藥製字第044098號 | "生達"順壓樂持續釋放錠５毫克 | 持續性釋放錠 | 生達化學製藥股份有限公司 | 2030/11/10 | 高血壓、心絞痛。 |
| 衛署藥製字第044468號 | 紛落持續釋放膜衣錠５毫克 | 持續性釋放錠 | 十安藥品股份有限公司 | 2031/05/25 | 高血壓、心絞痛。 |
| 衛署藥製字第044575號 | "惠勝"費平持續釋放錠５毫克 | 持續性釋放錠 | 惠勝藥品股份有限公司 | 2031/08/02 | 高血壓、心絞痛。 |
| 衛署藥製字第045392號 | "信東" 菲可平持續釋放膜衣錠５毫克 | 持續釋放膜衣錠 | 信東生技股份有限公司 | 2028/03/04 | 高血壓、心絞痛。 |
| 衛署藥製字第045510號 | "南光" 非洛緩釋錠１０公絲 | 持續性釋放錠 | 南光化學製藥股份有限公司 | 2028/04/30 | 高血壓、心絞痛。 |
| 衛署藥製字第047536號 | 菲迪欣 持續性藥效膜衣錠5毫克 | 持續性釋放錠 | 健喬信元醫藥生技股份有限公司 | 2030/09/19 | 高血壓、心絞痛。 |
| 衛署藥製字第049376號 | “永勝”費落持續性藥效錠 2.5 毫克 | 持續性藥效錠 | 永勝藥品工業股份有限公司 | 2028/04/24 | 高血壓、心絞痛。 |
| 衛署藥製字第050138號 | 〝永勝〞費落持續釋放膜衣錠 10 毫克 | 持續釋放膜衣錠 | 永勝藥品工業股份有限公司 | 2029/05/12 | 高血壓、心絞痛。 |
| 衛署藥製字第055896號 | “永勝”費落持續釋放錠 5 毫克 | 持續性釋放錠 | 永勝藥品工業股份有限公司 | 2030/12/28 | 高血壓、心絞痛。 |
| 衛署藥輸字第017469號 | 普心寧持續性藥效錠１０公絲 | 持續性釋放錠 | 裕利股份有限公司 | 2029/10/09 | 高血壓、心絞痛。 |
| 衛署藥輸字第017488號 | 普心寧持續性藥效錠５公絲 | 持續性釋放錠 | 裕利股份有限公司 | 2029/10/13 | 高血壓、心絞痛。 |
| 衛部藥陸輸字第000747號 | 非洛地平 | （粉） | 漢旭股份有限公司 | 2031/10/12 | 鈣離子拮抗劑。 |

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（1 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第049516號 | 菲洛安 持續性藥效膜衣錠 | ENALAPRIL MALEATE、FELODIPINE | 持續性藥效膜衣錠 | 治療高血壓。此複方藥品不適合用於起始治療。 |

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-09-29）</strong>（1 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛署藥製字第046480號</td><td>安壓定持續釋放錠5公絲</td><td>FELODIPINE</td><td>2024/09/01</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（10 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第044631號</td><td>撫樂平持續性藥效錠５公絲</td><td>FELODIPINE</td><td>2020/07/15</td></tr><tr><td>衛署藥製字第046021號</td><td>"南光" 非洛緩釋放錠５公絲</td><td>FELODIPINE</td><td>2013/12/17</td></tr><tr><td>衛署藥製字第049876號</td><td>允降 持續釋放膜衣錠 5 毫克</td><td>FELODIPINE</td><td>2023/12/12</td></tr><tr><td>衛署藥製字第049963號</td><td>允降持續釋放膜衣錠 10 毫克</td><td>FELODIPINE</td><td>2024/01/23</td></tr><tr><td>衛署藥輸字第020949號</td><td>寧壓持續性藥效錠２．５公絲</td><td>FELODIPINE</td><td>1996/05/20</td></tr><tr><td>衛署藥輸字第021149號</td><td>普心寧持續性藥效錠２．５公絲</td><td>FELODIPINE</td><td>2020/06/12</td></tr><tr><td>衛署藥輸字第024544號</td><td>采心平5毫克緩釋錠</td><td>RAMIPRIL、FELODIPINE</td><td>2020/11/06</td></tr><tr><td>衛署藥輸字第025565號</td><td>菲洛的平</td><td>Felodipine</td><td>2018/03/09</td></tr><tr><td>衛署藥陸輸字第000454號</td><td>非洛地平</td><td>Felodipine</td><td>2017/04/14</td></tr><tr><td>衛部藥製字第058208號</td><td>"十全"壓落持續釋放膜衣錠5毫克</td><td>FELODIPINE</td><td>2026/09/07</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：資料庫共收錄 246 筆交互作用。其中列為嚴重（Major）的有 Dolasetron；中度（Moderate）者包括 Hydrocortisone、Bupropion、Aprepitant、Cimetidine、Clarithromycin、Acetylsalicylic acid、Morphine，以及 Dexamethasone 等類固醇。
- **知識圖譜標示的禁忌疾病**（來自知識圖譜的藥物-疾病關聯，並非仿單內容）：包括肝病、腎病、主動脈瓣狹窄、肥厚性心肌病變、低血壓、心肌梗塞、冠狀動脈疾病、血管性水腫、嗜中性白血球低下等。實際禁忌請以原廠仿單為準。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數與前臨床研究支持，沒有臨床試驗，也沒有針對肺高壓病人的研究，證據等級僅為 L4。
- 此外，作用機轉資料缺失，且低血壓等狀況可能構成風險，目前不宜推進。

**若要推進需要：**
- 補齊 Felodipine 的作用機轉資料（DrugBank MOA）。
- 針對缺氧性肺高壓進行系統性文獻回顧，並評估是否有人體血流動力學資料。
- 設計小規模探索性臨床研究（例如肺血管阻力、肺動脈壓的血流動力學試驗），並規劃低血壓、周邊水腫等安全性監測。

### 其他預測適應症備註

- **Prinzmetal 心絞痛**（證據等級 L2，建議為研究問題）：已有 3 項 RCT（含與 nifedipine 的比較）顯示 Felodipine 對變異型心絞痛有抗缺血效果，且與其已核准的心絞痛適應症屬同一類機轉，是證據較強的方向，可優先考慮後續評估。
- **慢性肺心症**：僅有小型血流動力學研究（Felodipine 輸注可降低肺與全身血管阻力），建議為 Hold。
- 其餘預測（不明機轉的肺高壓、惡性高血壓腎病變、Braddock 症候群）僅有模型預測，無試驗或文獻，建議為 Hold。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 新增「作用機轉」段（每點附仿單來源） | 新增附來源段落 | [DailyMed：Felodipine Extended-Release Tablets, USP 仿單（Westminster）](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a6560584-e39f-47b3-84db-95da1f90fd40) |
| 2026-10-04 | 頁首證據等級 | 頁首等級依總覽表重算（原 L5→L4） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

