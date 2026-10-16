---
layout: default
title: Propantheline
parent: 中證據等級 (L3-L4)
nav_order: 236
evidence_level: L3
indication_count: 2
---

# Propantheline
{: .fs-9 }

證據等級: **L3** | 預測適應症: **2** 個
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

# Propantheline：從胃、十二指腸潰瘍到胃十二指腸炎

## 一句話總結

Propantheline（溴化丙烷體林）是一種四級銨類抗毒蕈鹼藥物（副交感神經遮斷劑），在台灣原本用於胃、十二指腸潰瘍與腸胃痙攣。
TxGNN 模型預測它可能對**胃十二指腸炎 (Gastroduodenitis)** 有效，目前**無臨床試驗登記**，但有 **3 篇文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃、十二指腸潰瘍、幽門痙攣、胃炎、胃酸過多、結腸痙攣、輸尿道及膀胱痙攣 |
| 預測新適應症 | 胃十二指腸炎 (Gastroduodenitis) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 53 張（有效單方 4／有效複方 5／已註銷 44） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。不過依藥理分類，Propantheline 是四級銨類抗毒蕈鹼藥物，可阻斷胃壁細胞與平滑肌上的 M3 受體，降低胃酸分泌與胃十二指腸的過度蠕動。

胃十二指腸炎與消化性潰瘍同屬上消化道的酸相關疾病，病理上有重疊。Propantheline 在台灣已核准用於胃炎與胃、十二指腸潰瘍，因此預測的新適應症與既有適應症高度相近，更像是原適應症的延伸，而非全新的治療領域。

需要注意：這是一個相當「貼近原適應症」的預測，新意有限。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [6342335](https://pubmed.ncbi.nlm.nih.gov/6342335/) | 1983 | 雙盲試驗（58 位門診病人） | Acta Med Scand | Cimetidine 加低劑量 propantheline 與 cimetidine 加安慰劑相比，治療 3 週和 6 週後，潰瘍癒合與症狀緩解皆無顯著差異（約 79% vs 83%） |
| [761954](https://pubmed.ncbi.nlm.nih.gov/761954/) | 1979 | 世代研究 | Int J Clin Pharmacol Biopharm | 比較 trithiozine 與 propantheline 對胃液分泌的影響；兩者皆可減少基礎狀態下的胃液量，組織胺刺激後 propantheline 降低胃液量與胃酸分泌的效果優於 trithiozine |
| [13392433](https://pubmed.ncbi.nlm.nih.gov/13392433/) | 1956 | 回顧 | Vie Med | 以 propantheline 進行胃十二指腸潰瘍抗膽鹼治療的應用（無摘要） |

整體而言文獻年代較早，且唯一的對照試驗顯示 propantheline 併用 cimetidine 並未帶來額外療效。

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

- **禁忌／需謹慎的疾病（來自 TxGNN 知識圖譜，非仿單內容）：** 閉角型青光眼、重症肌無力、麻痺性腸阻塞與腸阻塞、幽門狹窄、巨結腸症（中毒性）、潰瘍性結腸炎與發炎性腸道疾病、賁門失弛緩症、良性攝護腺肥大與膀胱頸阻塞、甲狀腺功能亢進、冠狀動脈疾病、高血壓、肝臟與腎臟疾病、食道裂孔疝等。
- **藥物交互作用：** 共記錄 203 筆。已列出的多為中度，例如其他抗膽鹼藥物（hyoscyamine、homatropine、aclidinium）、鴉片類藥物（fentanyl、codeine、tramadol）、抗組織胺（chlorpheniramine）、三環抗憂鬱劑（amitriptyline）、amantadine、loperamide、酒精與 botulinum toxin type A；與 acetaminophen、hydrochlorothiazide 為輕度。疊加抗膽鹼作用可能增加口乾、便秘、尿滯留等副作用。
- 其他警語與正式禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測的胃十二指腸炎與既有適應症（胃炎、胃與十二指腸潰瘍）高度重疊，新增價值有限。
- 目前沒有臨床試驗，僅有少量老舊文獻，其中唯一的對照試驗未顯示額外療效。

**若要推進需要：**
- 補齊作用機轉資料（MOA）。
- 確認台灣現有適應症文字是否已涵蓋胃十二指腸炎，以判斷是否真有必要另行申請。
- 在現代標準治療（如質子幫浦抑制劑）背景下，評估 propantheline 的臨床定位與相對效益。
- 針對老年人及有上述禁忌疾病的族群，擬定抗膽鹼副作用與藥物交互作用的監測計畫。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

