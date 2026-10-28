---
layout: default
title: Propantheline
parent: 僅模型預測 (L5)
nav_order: 236
evidence_level: L5
indication_count: 1
monitor_inn: "Propantheline"
predicted_indications: ["irritable bowel syndrome"]
last_modified_at: 2026-10-29
description: "Propantheline：預測新適應症為腸躁症 (Irritable Bowel Syndrome)（證據等級 L5）。原適應症：胃、十二指腸潰瘍、幽門痙攣、胃炎、胃酸過多、結腸痙攣、輸尿道及膀胱痙攣"
---

# Propantheline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Propantheline：從消化性潰瘍到腸躁症
{: .text-alpha }

## 一句話總結

Propantheline（普泮夕林，台灣商品名如益胃寧）是一種副交感神經遮斷劑（抗膽鹼藥），原本用於胃、十二指腸潰瘍與腸胃痙攣。
TxGNN 模型預測它可能對**腸躁症 (Irritable Bowel Syndrome)** 有效，
目前**無臨床試驗登記**，有 **3 篇文獻**與此方向相關，其中直接研究腸躁症的人體研究為 2 篇（1 篇 RCT、1 篇世代研究），且兩篇均為合併用藥設計。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃、十二指腸潰瘍、幽門痙攣、胃炎、胃酸過多、結腸痙攣、輸尿道及膀胱痙攣 |
| 預測新適應症 | 腸躁症 (Irritable Bowel Syndrome) |
| TxGNN 預測分數 | 0.9916 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 9 張／共 53 張） |
| 許可證數 | 53 張（有效單方 4／有效複方 5／已註銷 44） |
| 建議決策 | Hold |

**證據等級說明：**文獻中雖有直接研究腸躁症的 RCT（1989 年），但該研究為 ispaghula husk（洋車前子殼）加 propantheline 的合併治療，無法單獨歸因於 propantheline；另一篇為 bromazepam 合併 propantheline 的研究，同樣屬合併用藥，且無摘要可供查核。依證據上限規則與保守原則，本報告判定為 L5。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為空缺）。根據已知藥理，Propantheline 屬周邊作用的抗毒蕈鹼（抗膽鹼）藥物，可減少胃腸道平滑肌痙攣與蠕動亢進。

腸躁症的核心症狀為腹痛、絞痛與腸蠕動異常。Propantheline 在台灣已核准的適應症包含結腸痙攣、腸道運動亢進與幽門痙攣，這些症狀與腸躁症高度重疊，因此機轉上可能緩解腸躁症的腹痛與絞痛。另有一篇動物研究（YM905，另一種 M3 受體拮抗劑）顯示，抗 M3 受體可改善腸躁症模型的腸道功能異常，間接支持此機轉方向，但該研究並未使用 propantheline。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2697886](https://pubmed.ncbi.nlm.nih.gov/2697886/) | 1989 | RCT | The Quarterly Journal of Medicine | 28 名腸躁症患者先以 ispaghula husk 加 propantheline 治療 4–6 週後完全緩解，再隨機分組，比較安慰劑與持續治療的長期復發情形；為合併用藥，無法單獨評估 propantheline |
| [2888056](https://pubmed.ncbi.nlm.nih.gov/2888056/) | 1987 | 世代研究 | Minerva Dietologica e Gastroenterologica | 多中心研究，評估 bromazepam 加 propantheline 複方用於腸躁症的療效與耐受性（無摘要，細節不明） |
| [11488427](https://pubmed.ncbi.nlm.nih.gov/11488427/) | 2001 | 動物研究 | Japanese Journal of Pharmacology | 新型 M3 受體拮抗劑 YM905 可抑制大鼠壓力誘發的排便與腹瀉，支持抗膽鹼機轉於腸躁症模型的合理性 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Propantheline 的不重複許可證共 **53 張**：有效單方 4 張、有效複方 5 張、已註銷 44 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（4 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 內衛藥製字第002613號 | 補潰寧糖衣錠 | 糖衣錠 | 天下生物科技股份有限公司 | 2029/05/25 | 消化性潰瘍、胃炎、幽門痙攣、腸管之疝痛、腸管運動亢進、膽囊疝痛、子宮或膀胱痙攣、唾液過多症、多汗症 |
| 內衛藥製字第013679號 | "人生"溴化普盤林糖衣錠１５公絲 | 糖衣錠 | 人生製藥股份有限公司 | 2029/05/25 | 胃、十二指腸潰瘍、幽門痙攣、胃炎、胃酸過多、結腸痙攣、輸尿道及膀胱痙攣 |
| 衛署藥製字第010279號 | 溴化普魯派西林糖衣錠１５公絲 | 糖衣錠 | 榮民製藥股份有限公司 | 2028/07/07 | 胃腸炎、膽管及尿道痙攣、胰腺炎 |
| 衛署藥製字第040704號 | "紐約"溴化普泮夕林糖衣錠１５公絲 | 糖衣錠 | 人人化學製藥股份有限公司 | 2029/12/31 | 胃、十二指腸潰瘍、胃酸過多、幽門痙攣、結腸過敏及痙攣、膽囊痙攣、輸尿管及膀胱痙攣、多汗症、節制涎液分泌 |

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（5 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 內衛藥製字第002251號 | 胃治平散 | SODIUM BICARBONATE ( EQ TO SODIUM HYDROGEN CARBONATE)、BENZOC… | 散劑 | 胃十二指腸潰瘍、胃酸過多、急性慢性胃炎、胃痛 |
| 內衛藥製字第002596號 | 胃治平錠 | CALCIUM CARBONATE、SCOPOLIA EXTRACT POWDER、MAGNESIUM TRISILIC… | 錠劑 | 胃、十二指腸潰瘍、胃酸過多、急慢性胃炎、胃痛等胃腸障礙 |
| 衛署藥製字第008462號 | 胃錠 | PROPANTHELINE BROMIDE、BENZOCAINE (ETHYL AMINOBENZOATE)、MAGNE… | 錠劑 | 緩解胃部不適或灼熱感、胃酸過多、消化不良。 |
| 衛署藥製字第035954號 | 胃得好錠 | PROPANTHELINE BROMIDE、MAGNESIUM OXIDE (MG. TRISILICATE)、ALUM… | 錠劑 | 胃、十二指腸潰瘍、潰瘍痛、胃酸過多、胃炎、胃痛、迴腸炎、結腸炎 |
| 衛部藥製字第060967號 | "國際"幫息力膠囊 | PROPANTHELINE BROMIDE、ALUMINUM HYDROXIDE DRIED GEL、SIMETHICO… | 膠囊劑 | 消化性潰瘍、胃酸過多、胃炎、胃痛、幽門痙攣、異常醱酵、氣脹、結腸痙攣。 |

<details><summary><strong>已註銷</strong>（44 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第000138號</td><td>溴化普盤林糖衣錠１５公絲</td><td>PROPANTHELINE BROMIDE</td><td>2010/03/05</td></tr><tr><td>內衛藥製字第001973號</td><td>胃百康片</td><td>CHLOROPHYLL SODIUM COPPER、PROPANTHELINE BROMIDE、MAGNESIUM AL…</td><td>2000/08/04</td></tr><tr><td>內衛藥製字第004186號</td><td>克胃生錠</td><td>MAGNESIUM ALUMINUM METASILICATE (NEUSILIN)、CHLOROPHYLL SODIU…</td><td>1989/11/27</td></tr><tr><td>內衛藥製字第005670號</td><td>"威力"胃康寧錠</td><td>PHENOBARBITAL、PROPANTHELINE BROMIDE</td><td>2023/07/07</td></tr><tr><td>內衛藥製字第009652號</td><td>溴化丙烷體林片</td><td>PROPANTHELINE BROMIDE</td><td>1997/04/07</td></tr><tr><td>內衛藥製字第010474號</td><td>"華盛頓牌"溴化丙烷體林糖衣錠１５公絲</td><td>PROPANTHELINE BROMIDE</td><td>2023/07/03</td></tr><tr><td>內衛藥製字第012722號</td><td>複方舒胃寧片</td><td>ALUMINUM HYDROXIDE GEL、PROPANTHELINE BROMIDE、BELLADONNA EXTR…</td><td>2024/05/16</td></tr><tr><td>內衛藥製字第013656號</td><td>安治胃錠</td><td>SYNTHETIC ALUMINUM SILICATE、PROPANTHELINE BROMIDE、MAGNESIUM…</td><td>2015/07/01</td></tr><tr><td>內衛藥輸字第001185號</td><td>綠胃素錠</td><td>CHLOROPHYLL SODIUM COPPER、MAGNESIUM ALUMINUM HYDROXIDE、PROPA…</td><td>1986/01/06</td></tr><tr><td>內衛藥輸字第001949號</td><td>綠胃素</td><td>PROPANTHELINE BROMIDE、CHLOROPHYLL SODIUM COPPER、MAGNESIUM AL…</td><td>1987/04/08</td></tr><tr><td>內衛藥輸字第002640號</td><td>益胃寧</td><td>DIHYDROXYALUMINUM AMINOACETATE、PROPANTHELINE BROMIDE</td><td>1986/10/20</td></tr><tr><td>內衛藥輸字第002650號</td><td>新益胃寧</td><td>PROPANTHELINE BROMIDE、PHENOBARBITAL、DIHYDROXYALUMINUM AMINOA…</td><td>1986/10/20</td></tr><tr><td>內衛藥輸字第005242號</td><td>健胃新</td><td>PHENOBARBITAL、PROPANTHELINE BROMIDE、BELLADONNA LEAF ALKALOID…</td><td>1986/05/12</td></tr><tr><td>內衛藥輸字第005890號</td><td>好胃寧</td><td>MAGNESIUM TRISILICATE、MAGNESIUM ALUMINUM HYDROXIDE MONOHYDRA…</td><td>1986/06/16</td></tr><tr><td>衛署藥製字第005012號</td><td>永舒胃錠</td><td>GLYCYRRHIZA EXTRACT、MAGNESIUM ALUMINUM HYDROXIDE CO-DRIED GE…</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第005219號</td><td>永舒胃顆粒</td><td>BENZOCAINE (ETHYL AMINOBENZOATE)、ALUMINUM SILICATE、PROPANTHE…</td><td>2016/09/19</td></tr><tr><td>衛署藥製字第005408號</td><td>胃滋錠</td><td>ALUMINUM MAGNESIUM SILICATE、PROPANTHELINE BROMIDE</td><td>2002/04/18</td></tr><tr><td>衛署藥製字第007983號</td><td>凱胃糖衣錠</td><td>PROPANTHELINE BROMIDE</td><td>2011/02/22</td></tr><tr><td>衛署藥製字第008291號</td><td>表胃平優錠</td><td>ALUMINUM MAGNESIUM SILICATE、PROPANTHELINE BROMIDE</td><td>2023/07/27</td></tr><tr><td>衛署藥製字第008538號</td><td>潰克舒錠</td><td>CALCIUM CARBONATE、ALUMINUM MAGNESIUM SILICATE、PROPANTHELINE…</td><td>2017/03/15</td></tr><tr><td>衛署藥製字第015357號</td><td>"國際" 幫息力膠囊</td><td>ALUMINUM HYDROXIDE DRIED GEL、SIMETHICONE (ACTIVE DIMETHICONE…</td><td>2022/04/21</td></tr><tr><td>衛署藥製字第016310號</td><td>保胃能錠</td><td>GLYCYRRHIZA EXTRACT、PROPANTHELINE BROMIDE、MAGNESIUM TRISILIC…</td><td>1999/12/10</td></tr><tr><td>衛署藥製字第017143號</td><td>胃舒錠</td><td>MAGNESIUM OXIDE、PROPANTHELINE BROMIDE、BROMISOVALUM ( EQ TO B…</td><td>2023/06/30</td></tr><tr><td>衛署藥製字第017909號</td><td>佳胃素錠</td><td>PROPANTHELINE BROMIDE、CHLOROPHYLL SODIUM COPPER、MAGNESIUM AL…</td><td>2013/07/11</td></tr><tr><td>衛署藥製字第019489號</td><td>胃寶能顆粒</td><td>CHLOROPHYLL SODIUM COPPER、ALUMINUM HYDROXIDE MAGNESIUM CARBO…</td><td>2004/10/06</td></tr><tr><td>衛署藥製字第021925號</td><td>治胃腸錠</td><td>MAGNESIUM OXIDE、BROMISOVALUM ( EQ TO BROMOVALERYLUREA) ( EQ…</td><td>2000/08/04</td></tr><tr><td>衛署藥製字第025710號</td><td>胃得好錠</td><td>MAGNESIUM OXIDE (MG. TRISILICATE)、PROPANTHELINE BROMIDE、BROM…</td><td>1993/03/31</td></tr><tr><td>衛署藥製字第026339號</td><td>佑爾健錠</td><td>ALUMINUM HYDROXIDE DRIED GEL、BROMISOVALUM ( EQ TO BROMOVALER…</td><td>2016/09/07</td></tr><tr><td>衛署藥輸字第000243號</td><td>普魯萬胃聖</td><td>PROPANTHELINE BROMIDE</td><td>2014/01/28</td></tr><tr><td>衛署藥輸字第000334號</td><td>溴化丙烷體林</td><td>PROPANTHELINE BROMIDE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第000353號</td><td>溴化丙烷西林</td><td>PROPANTHELINE BROMIDE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第002394號</td><td>溴化丙烷體林</td><td>PROPANTHELINE BROMIDE</td><td>1988/09/02</td></tr><tr><td>衛署藥輸字第004028號</td><td>溴化丙烷基林</td><td>PROPANTHELINE BROMIDE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第005055號</td><td>溴化丙烷體林</td><td>PROPANTHELINE BROMIDE</td><td>1995/04/06</td></tr><tr><td>衛署藥輸字第005636號</td><td>普邦生錠</td><td>PROPANTHELINE BROMIDE</td><td>1993/12/03</td></tr><tr><td>衛署藥輸字第006206號</td><td>溴化丙烷體林</td><td>PROPANTHELINE BROMIDE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第006756號</td><td>溴化丙烷體林</td><td>PROPANTHELINE BROMIDE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第009550號</td><td>美得寧錠</td><td>PROPANTHELINE BROMIDE、MAGNESIUM OXIDE (MG. TRISILICATE)、CHLO…</td><td>1988/03/12</td></tr><tr><td>衛署藥輸字第012166號</td><td>美效胃齡片</td><td>CHLOROPHYLL SODIUM COPPER、PROPANTHELINE BROMIDE、MAGNESIUM SI…</td><td>1988/09/02</td></tr><tr><td>衛署藥輸字第014569號</td><td>綠胃素錠</td><td>PROPANTHELINE BROMIDE、CHLOROPHYLL SODIUM COPPER、MAGNESIUM AL…</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第016135號</td><td>美得寧錠</td><td>CALCIUM PHOSPHATE DIBASIC、CHLOROPHYLL SODIUM COPPER、PROPANTH…</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第017134號</td><td>溴化普泮夕林</td><td>PROPANTHELINE BROMIDE</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第020088號</td><td>普邦生錠</td><td>PROPANTHELINE BROMIDE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第021246號</td><td>溴化普泮夕林</td><td>PROPANTHELINE BROMIDE</td><td>2013/12/16</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（來自知識圖譜，非仿單內容）：閉鎖角青光眼、重症肌無力、麻痺性腸阻塞與腸道阻塞、幽門狹窄、巨結腸症、潰瘍性大腸炎、良性攝護腺肥大與膀胱頸阻塞、甲狀腺機能亢進、冠狀動脈疾病、高血壓、肝臟與腎臟疾病、食道弛緩不能、裂孔疝等。
  - 其中潰瘍性大腸炎、腸道阻塞與毒性巨結腸，與腸躁症的鑑別診斷相關，用藥前須先排除。
- **藥物交互作用**：共查得 203 筆交互作用，以下為部分例子：
  - 中度：其他抗膽鹼藥（hyoscyamine、homatropine、aclidinium）、amitriptyline、amantadine、抗組織胺（chlorpheniramine、acrivastine）、鴉片類（fentanyl、codeine、tramadol、alfentanil、dihydrocodeine）、loperamide、肉毒桿菌毒素 A、乙醇、acebutolol。
  - 輕度：acetaminophen、hydrochlorothiazide。
  - 多重抗膽鹼作用疊加，可能增加口乾、便秘、尿滯留等風險。

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 預測分數高，且機轉與台灣核准的結腸痙攣、腸道運動亢進適應症合理相符；但直接的腸躁症人體證據僅有合併用藥的小型研究（含 1989 年 RCT，無單獨 propantheline 的對照），也沒有任何臨床試驗登記，目前僅屬研究假說階段。

**若要推進需要：**
- 取得 propantheline 單藥用於腸躁症的對照試驗證據，或設計單藥 vs 安慰劑的隨機試驗。
- 補充 DrugBank 的作用機轉資料，並釐清與現有抗膽鹼類腸躁症用藥（如 hyoscyamine）的相對定位。
- 取得原廠仿單中的警語與禁忌資訊，並針對老年人、便秘型腸躁症患者與多重抗膽鹼用藥者制定安全監測計畫。
- 評估是否需要申請腸躁症適應症的擴增，以及台灣有效單方許可證（4 張）的適用範圍。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

