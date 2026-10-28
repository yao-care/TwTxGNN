---
layout: default
title: Isosorbide Dinitrate
parent: 僅模型預測 (L5)
nav_order: 157
evidence_level: L5
indication_count: 10
monitor_inn: "Isosorbide dinitrate"
predicted_indications: ["alopecia", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "pulmonary hypertension", "diffuse alopecia areata", "vascular disease", "hypertrichosis (disease)", "kyphoscoliotic heart disease", "visceral calciphylaxis", "arterial thoracic outlet syndrome"]
last_modified_at: 2026-10-29
description: "Isosorbide Dinitrate：預測新適應症為alopecia（禿髮）（證據等級 L5）。原適應症：預防狹心症之發作"
---

# Isosorbide Dinitrate
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

## Isosorbide dinitrate：從狹心症到 alopecia（禿髮）
{: .text-alpha }

## 一句話總結

Isosorbide dinitrate（二硝酸異山梨酯）是一種硝酸酯類血管擴張劑，台灣許可證核准用於預防及治療狹心症發作。
TxGNN 模型預測分數最高的新適應症是 **alopecia（禿髮）**，但目前**沒有任何臨床試驗或文獻**直接支持，僅為模型預測。
在所有預測中，證據相對較多的是**肺動脈高壓**（約 20 篇文獻，無登記試驗）與**血管疾病**（6 個臨床試驗、約 20 篇文獻，但多與冠心症或其他相關疾病有關）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 預防狹心症之發作 |
| 預測新適應症 | alopecia（禿髮） |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 5 張／共 71 張） |
| 許可證數 | 71 張（有效單方 5／有效複方 0／已註銷 66） |
| 建議決策 | Hold |

> 說明：上表以排名第一的預測（禿髮）為主。排名第 4 的肺動脈高壓與排名第 6 的血管疾病證據較多，見後文補充。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Isosorbide dinitrate 屬於一氧化氮（NO）供體，可在血管平滑肌提高 cGMP，使血管擴張、降低前負荷與後負荷，這與其狹心症用途一致。

針對禿髮，唯一的推測是血管擴張可能增加毛囊血流，類似 minoxidil 等血管擴張劑的聯想。但目前沒有任何臨床或前臨床證據支持，此推論屬高度推測，分數僅代表模型預測。

排名前十的預測中，其他毛髮相關疾病（先天性少毛症、頭皮單純性少毛症、瀰漫性斑禿、多毛症）機轉上也缺乏合理連結；斑禿屬自體免疫機轉，與 NO 血管擴張無關。相較之下，肺動脈高壓（NO 降低肺血管阻力）與血管疾病在機轉上較合理，但需注意肺部通氣灌注失衡（尤其 COPD 合併肺高壓）及耐受性風險。

## 臨床試驗證據

預測新適應症「alopecia」目前無相關臨床試驗登記。

補充：排名第 6 的「血管疾病」有下列試驗，均不直接針對禿髮，且多數與血管疾病的關聯為間接：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02789033](https://clinicaltrials.gov/study/NCT02789033) | Phase 3 | 完成 | 68 | 二硝酸異山梨酯噴劑合併幾丁聚醣用於糖尿病足潰瘍 |
| [NCT01513070](https://clinicaltrials.gov/study/NCT01513070) | Phase 4 | 完成 | 120 | 中藥複方與 isosorbide dinitrate 用於中度冠狀動脈狹窄（藥物可能為對照） |
| [NCT02135315](https://clinicaltrials.gov/study/NCT02135315) | NA | 完成 | 1500 | 非 ST 上升型急性冠心症的強化與標準降壓策略 |
| [NCT00000478](https://clinicaltrials.gov/study/NCT00000478) | Phase 3 | 完成 | 未提供 | 無症狀心肌缺血的先導研究 |
| [NCT00803634](https://clinicaltrials.gov/study/NCT00803634) | Phase 3 | 完成 | 117 | 急性心衰竭合併高血壓的血壓控制（clevidipine） |
| [NCT03011775](https://clinicaltrials.gov/study/NCT03011775) | Phase 4 | 完成 | 43 | Pioglitazone 對冠心症胰島素阻抗與動脈粥樣硬化的影響（非本藥） |

## 文獻證據

預測新適應症「alopecia」目前無相關文獻。

補充：肺動脈高壓的代表性文獻如下（均非禿髮）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39164577](https://pubmed.ncbi.nlm.nih.gov/39164577/) | 2025 | Cohort | Heart and Vessels | 靜脈注射 ISDN 對合併心肺疾病的肺高壓之降壓效果，前毛細血管型可能降低心輸出量與血壓 |
| [373940](https://pubmed.ncbi.nlm.nih.gov/373940/) | 1979 | 隨機雙盲（小型） | Clin Pharmacol Ther | 18 位 COPD 合併肺高壓患者，口服 ISDN 與安慰劑比較血行動力學 |
| [6423015](https://pubmed.ncbi.nlm.nih.gov/6423015/) | 1984 | Case series | Bull Eur Physiopathol Respir | COPD 患者舌下 ISDN 降低肺動脈壓與心輸出量，未降低肺血管阻力 |
| [3409916](https://pubmed.ncbi.nlm.nih.gov/3409916/) | 1988 | 臨床研究 | Eur Heart J | 18 位間質性肺纖維化患者，ISDN 兩年治療持續降低肺高壓 |
| [2868878](https://pubmed.ncbi.nlm.nih.gov/2868878/) | 1986 | Review | Drugs | 原發性肺高壓的藥物治療回顧，ISDN 為報告有益的血管擴張劑之一 |
| [28810603](https://pubmed.ncbi.nlm.nih.gov/28810603/) | 2017 | 動物研究 | Exp Ther Med | 大鼠氣管內給予 ISDN 改善肺動脈壓與心室重塑 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Isosorbide Dinitrate 的不重複許可證共 **71 張**：有效單方 5 張、有效複方 0 張、已註銷 66 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（5 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第027438號 | 易適倍錠１０公絲（伊索倍雷） | 錠劑 | 衛達化學製藥股份有限公司 | 2029/10/17 | 預防狹心症之發作。 |
| 衛署藥製字第044974號 | 怡心通注射液 0.1% | 注射劑 | 健亞生物科技股份有限公司 | 2027/05/13 | 治療狹心症發作。 |
| 衛署藥製字第049260號 | 艾舒心注射液 0.1% | 注射劑 | 瑞士藥廠股份有限公司 | 2028/01/28 | 治療狹心症之發作。 |
| 衛署藥製字第056734號 | 歐舒心注射劑 0.01% | 注射劑 | 歐舒邁克有限公司 | 2026/12/02 | 治療狹心症之發作。 |
| 衛署藥輸字第007324號 | "施福" 二硝酸二脫氫山梨醇粉 | （粉） | 東信化學藥品有限公司 | 2028/07/04 | 冠狀動脈舒張劑 |

<details><summary><strong>已註銷</strong>（66 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥輸字第001205號</td><td>富利心舌下錠</td><td>ISOSORBIDE DINITRATE (TRITURATION WITH LACTOSE)</td><td>1989/11/21</td></tr><tr><td>衛署藥製字第019852號</td><td>優舒心舌下錠（伊速必得）</td><td>ISOSORBIDE DINITRATE</td><td>2002/07/24</td></tr><tr><td>衛署藥製字第020784號</td><td>優舒心錠（伊速必得）</td><td>ISOSORBIDE DINITRATE</td><td>2002/07/24</td></tr><tr><td>衛署藥製字第021396號</td><td>心狹爾錠（伊速必得）</td><td>ISOSORBIDE DINITRATE (DILUTED)</td><td>1989/12/31</td></tr><tr><td>衛署藥製字第022558號</td><td>喜心寧錠１０公絲（伊速必得）</td><td>ISOSORBIDE DINITRATE DILUTED</td><td>2002/07/24</td></tr><tr><td>衛署藥製字第026756號</td><td>心舒錠５公絲（二硝酸二脫氫山梨醇）</td><td>ISOSORBIDE DINITRATE/LACTOSE</td><td>2002/07/24</td></tr><tr><td>衛署藥製字第039209號</td><td>安心樂錠１０公絲（伊速必得）</td><td>ISOSORBIDE DINITRATE DILUTED</td><td>2002/07/24</td></tr><tr><td>衛署藥製字第039210號</td><td>安心樂錠５公絲（伊速必得）</td><td>ISOSORBIDE DINITRATE DILUTED</td><td>2002/07/24</td></tr><tr><td>衛署藥製字第048445號</td><td>通易注射液0.1%</td><td>ISOSORBIDE DINITRATE</td><td>2023/06/30</td></tr><tr><td>衛署藥輸字第000631號</td><td>施必爾錠５公絲</td><td>ISOSORBIDE DINITRATE</td><td>1992/03/16</td></tr><tr><td>衛署藥輸字第004321號</td><td>脈能壓順錠</td><td>ISOSORBIDE DINITRATE</td><td>1988/08/01</td></tr><tr><td>衛署藥輸字第005703號</td><td>聖多克錠</td><td>ISOSORBIDE DINITRATE</td><td>1992/11/13</td></tr><tr><td>衛署藥輸字第005893號</td><td>速必瑞５公絲咀嚼錠</td><td>ISOSORBIDE DINITRATE</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第005894號</td><td>速必瑞５公絲舌下錠</td><td>ISOSORBIDE DINITRATE</td><td>1993/04/15</td></tr><tr><td>衛署藥輸字第005895號</td><td>速必瑞１０公絲錠劑</td><td>ISOSORBIDE DINITRATE/LACTOSE</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第005896號</td><td>速必瑞５公絲錠劑</td><td>ISOSORBIDE DINITRATE</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第006232號</td><td>二硝酸二脫氫山梨醇</td><td>ISOSORBIDE DINITRATE</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第007154號</td><td>心舒速定錠１０公絲</td><td>ISOSORBIDE DINITRATE</td><td>1999/09/28</td></tr><tr><td>衛署藥輸字第007155號</td><td>心舒速定舌下錠５公絲</td><td>ISOSORBIDE DINITRATE</td><td>1999/09/28</td></tr><tr><td>衛署藥輸字第007232號</td><td>益舒百得持續性膠囊</td><td>ISOSORBIDE DINITRATE</td><td>1994/03/11</td></tr><tr><td>衛署藥輸字第009676號</td><td>心多克錠２０公絲</td><td>ISOSORBIDE DINITRATE</td><td>1993/04/01</td></tr><tr><td>衛署藥輸字第009750號</td><td>心力舒樂膠囊</td><td>ISOSORBIDE DINITRATE</td><td>2002/07/24</td></tr><tr><td>衛署藥輸字第009773號</td><td>益舒心持續性藥效膠囊２０公絲〝馬克〞</td><td>ISOSORBIDE DINITRATE</td><td>2002/07/24</td></tr><tr><td>衛署藥輸字第009775號</td><td>益舒心持續性藥效膠囊４０公絲〝馬克〞</td><td>ISOSORBIDE DINITRATE</td><td>2002/07/24</td></tr><tr><td>衛署藥輸字第009832號</td><td>益舒心舌下錠５公絲</td><td>ISOSORBIDE DINITRATE (TRITURATION WITH LACTOSE)</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第009833號</td><td>益舒心錠１０公絲</td><td>ISOSORBIDE DINITRATE (TRITURATION WITH LACTOSE)</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第009835號</td><td>益舒心錠５公絲</td><td>ISOSORBIDE DINITRATE (TRITURATION WITH LACTOSE)</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第009836號</td><td>益舒心舌下錠２．５公絲</td><td>ISOSORBIDE DINITRATE (TRITURATION WITH LACTOSE)</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第010083號</td><td>愛速得５公絲舌下錠</td><td>ISOSORBIDE DINITRATE/LACTOSE</td><td>1986/10/29</td></tr><tr><td>衛署藥輸字第010223號</td><td>愛速得錠１０公絲</td><td>ISOSORBIDE DINITRATE/LACTOSE</td><td>1986/10/24</td></tr><tr><td>衛署藥輸字第011460號</td><td>愛速得錠３０公絲</td><td>ISOSORBIDE DINITRATE</td><td>1986/09/30</td></tr><tr><td>衛署藥輸字第012075號</td><td>寧托樂片</td><td>ISOSORBIDE DINITRATE</td><td>1988/03/01</td></tr><tr><td>衛署藥輸字第012331號</td><td>艾克舒錠</td><td>ISOSORBIDE DINITRATE</td><td>2002/07/24</td></tr><tr><td>衛署藥輸字第012777號</td><td>福朗得特效錠</td><td>ISOSORBIDE DINITRATE</td><td>2002/07/24</td></tr><tr><td>衛署藥輸字第013277號</td><td>心多克延效性錠</td><td>ISOSORBIDE DINITRATE</td><td>1992/11/13</td></tr><tr><td>衛署藥輸字第013462號</td><td>富利心舌下錠</td><td>ISOSORBIDE DINITRATE (DILUTED)</td><td>1992/09/25</td></tr><tr><td>衛署藥輸字第013683號</td><td>使得落錠</td><td>ISOSORBIDE DINITRATE</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第014327號</td><td>速必瑞錠２０公絲</td><td>ISOSORBIDE DINITRATE/LACTOSE</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第014355號</td><td>速必瑞持續錠</td><td>ISOSORBIDE DINITRATE/LACTOSE、ISOSORBIDE DINITRATE/LACTOSE</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第014456號</td><td>心多克點滴注射液</td><td>ISOSORBIDE DINITRATE</td><td>1992/11/13</td></tr><tr><td>衛署藥輸字第015224號</td><td>伊速必得錠</td><td>ISOSORBIDE DINITRATE</td><td>1992/07/01</td></tr><tr><td>衛署藥輸字第015284號</td><td>愛速得錠３０公絲</td><td>ISOSORBIDE DINITRATE</td><td>1989/06/05</td></tr><tr><td>衛署藥輸字第015285號</td><td>愛速得錠１０公絲</td><td>ISOSORBIDE DINITRATE/LACTOSE</td><td>1989/06/05</td></tr><tr><td>衛署藥輸字第015286號</td><td>愛速得５公絲舌下錠</td><td>ISOSORBIDE DINITRATE/LACTOSE</td><td>1989/06/05</td></tr><tr><td>衛署藥輸字第016293號</td><td>寧托樂錠</td><td>ISOSORBIDE DINITRATE</td><td>2002/07/24</td></tr><tr><td>衛署藥輸字第016372號</td><td>心舒錠</td><td>ISOSORBIDE DINITRATE</td><td>1989/08/17</td></tr><tr><td>衛署藥輸字第016761號</td><td>伊斯得恩舌下錠５公絲</td><td>ISOSORBIDE DINITRATE</td><td>2002/07/24</td></tr><tr><td>衛署藥輸字第016811號</td><td>伊斯得恩錠１０毫克</td><td>ISOSORBIDE DINITRATE DILUTED</td><td>2002/07/24</td></tr><tr><td>衛署藥輸字第017051號</td><td>愛速得５公絲舌下錠</td><td>ISOSORBIDE DINITRATE/LACTOSE</td><td>1992/03/31</td></tr><tr><td>衛署藥輸字第017065號</td><td>愛速得錠１０公絲</td><td>ISOSORBIDE DINITRATE/LACTOSE</td><td>1992/03/31</td></tr><tr><td>衛署藥輸字第017066號</td><td>愛速得錠３０公絲</td><td>ISOSORBIDE DINITRATE</td><td>1992/03/31</td></tr><tr><td>衛署藥輸字第017133號</td><td>益舒心噴霧劑</td><td>ISOSORBIDE DINITRATE</td><td>2002/07/24</td></tr><tr><td>衛署藥輸字第017150號</td><td>心多克錠１０公絲</td><td>ISOSORBIDE DINITRATE/LACTOSE</td><td>1992/10/15</td></tr><tr><td>衛署藥輸字第017151號</td><td>益舒心注射液</td><td>ISOSORBIDE DINITRATE</td><td>2013/11/28</td></tr><tr><td>衛署藥輸字第017266號</td><td>心舒錠</td><td>ISOSORBIDE DINITRATE</td><td>1999/06/24</td></tr><tr><td>衛署藥輸字第018315號</td><td>二硝酸二脫氫山梨醇</td><td>ISOSORBIDE DINITRATE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第018510號</td><td>二硝酸伊速必得</td><td>ISOSORBIDE DINITRATE (TRITURATION WITH LACTOSE)</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第018972號</td><td>愛速得５公絲舌下錠</td><td>ISOSORBIDE DINITRATE/LACTOSE</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第018974號</td><td>愛速得錠３０公絲</td><td>ISOSORBIDE DINITRATE</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第018987號</td><td>愛速得錠１０公絲</td><td>ISOSORBIDE DINITRATE</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第019417號</td><td>聖多克錠</td><td>ISOSORBIDE DINITRATE</td><td>2002/07/24</td></tr><tr><td>衛署藥輸字第019424號</td><td>心多克點滴注射液</td><td>ISOSORBIDE DINITRATE</td><td>2002/07/24</td></tr><tr><td>衛署藥輸字第019425號</td><td>心多克持續錠２０公絲</td><td>ISOSORBIDE DINITRATE</td><td>2001/06/11</td></tr><tr><td>衛署藥輸字第019426號</td><td>心多克錠１０公絲</td><td>ISOSORBIDE DINITRATE/LACTOSE</td><td>2000/01/27</td></tr><tr><td>衛署藥輸字第019740號</td><td>心多克錠２０公絲</td><td>ISOSORBIDE DINITRATE</td><td>2002/07/24</td></tr><tr><td>衛署藥輸字第024062號</td><td>舒心痛 0.1% 注射液</td><td>ISOSORBIDE DINITRATE</td><td>2019/08/27</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：資料庫共記錄 141 筆交互作用，其中多為中度，例如 Bupropion、Morphine、Canagliflozin、Dapagliflozin、Empagliflozin、Rosiglitazone 等。
- **知識圖譜中記錄的禁忌關聯（非仿單文字）**：低血壓、肥厚型心肌病變、冠狀動脈疾病、中風與腦血管疾病、心肌梗塞、貧血與血紅素病變、甲狀腺機能亢進、顱內高壓、腦出血等。

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的禿髮預測沒有任何臨床或前臨床證據，機轉僅為推測，證據等級為 L5。
- 其他毛髮相關預測同樣缺乏證據。肺動脈高壓與血管疾病雖有較多研究，但多為老舊、小型的血行動力學研究，且血管疾病範圍過廣，尚不足以支持推進。

**若要推進需要：**
- 取得完整的作用機轉資料，並建立 NO 供體與毛囊血流或毛髮生長之間的前臨床證據。
- 若考慮肺動脈高壓，建議另行評估：收集區分前、後毛細血管型的現代對照試驗，並評估 COPD 患者通氣灌注失衡及硝酸酯耐受性的風險。
- 確認給藥途徑（外用或口服）與目標族群的低血壓風險。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

