---
layout: default
title: Ergometrine
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 10
monitor_inn: "Ergometrine"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "nephrogenic syndrome of inappropriate antidiuresis", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "migraine disorder", "migraine with brainstem aura", "leprosy", "pulmonary hypertension"]
last_modified_at: 2026-10-29
description: "Ergometrine：預測新適應症為毛髮過多症 (Hypertrichosis)（證據等級 L5）。原適應症：產褥期之出血、流產後之出血、分娩時之子宮弛緩出血、不正常出血、分娩第三期陣痛微弱"
---

# Ergometrine
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

## Ergometrine：從產後子宮出血到毛髮過多症（Hypertrichosis）
{: .text-alpha }

## 一句話總結

Ergometrine（麥角新鹼）是麥角生物鹼類子宮收縮劑，原本用於產後出血、流產後出血及子宮收縮不全；台灣現行有效許可證也核准偏頭痛。
TxGNN 模型預測它可能對**毛髮過多症 (Hypertrichosis)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 產褥期之出血、流產後之出血、分娩時之子宮弛緩出血、不正常出血、分娩第三期陣痛微弱 |
| 預測新適應症 | 毛髮過多症 (Hypertrichosis) |
| TxGNN 預測分數 | 0.9996 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 18 張／共 101 張） |
| 許可證數 | 101 張（有效單方 17／有效複方 1／已註銷 83） |
| 建議決策 | Hold |

<!-- review:begin ergometrine-moa-2026-10-03 -->

## Ergometrine 的作用機轉

<!-- moa-sourced: 2026-10-03 用戶拍板例外，只限附來源的作用機轉段 -->

以下只說明這個藥原本怎麼作用，每一點都摘自官方仿單的藥理段落並附連結；與本頁的老藥新用預測無關，也不構成用藥建議。

- Ergometrine 屬麥角生物鹼，透過對子宮肌層 5-HT2 受體與 α 腎上腺素受體的作用劑或部分作用劑效果，讓子宮產生持續的強直性收縮，子宮上段與下段都會收縮。（[仿單](https://www.medicines.org.uk/emc/product/6265/smpc)）
- 這種持續收縮能控制子宮出血；和 oxytocin 不同，它對未懷孕的子宮也有作用。（[仿單](https://www.medicines.org.uk/emc/product/6265/smpc)）
- 它會抑制泌乳素分泌，因此可能減少乳汁分泌。（[仿單](https://www.medicines.org.uk/emc/product/6265/smpc)）
- 肌肉注射後約 7 分鐘內開始刺激子宮，靜脈注射則幾乎立即作用。（[仿單](https://www.medicines.org.uk/emc/product/6265/smpc)）
- 對血管有部分作用劑效果（比 ergotamine 弱），對心血管與中樞神經的影響也比其他麥角生物鹼小；對 α 腎上腺素受體幾乎沒有拮抗作用。（[仿單](https://www.medicines.org.uk/emc/product/6265/smpc)）

**來源**：[英國 emc：Ergometrine Injection BP 0.05% w/v 產品特性摘要（SmPC）§5.1 藥效學](https://www.medicines.org.uk/emc/product/6265/smpc)；查閱日期 2026-10-03。

---

<!-- review:end ergometrine-moa-2026-10-03 -->

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Ergometrine 是麥角生物鹼類的子宮收縮劑，一般認為作用於血清素、α-腎上腺素與多巴胺受體，藉此收縮子宮平滑肌與血管，達到止血效果。

原適應症（產後與流產後出血）和毛髮過多症在病理上沒有明顯關聯。已知資訊中，沒有任何機轉可說明 Ergometrine 能促進或調節毛髮生長，此預測目前只是模型的關聯性輸出。

此外，TxGNN 其他排名較高的預測（如 Ambras 型先天性全身性多毛症、腎因性抗利尿不適當症候群、Dandy-Walker 畸形相關症候群等）同樣缺乏機轉依據。這顯示高分預測不等於有生物學合理性。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Ergometrine 的不重複許可證共 **101 張**：有效單方 17 張、有效複方 1 張、已註銷 83 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（17 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 內衛藥製字第001749號 | “強生”縮水蘋果酸麥角新鹼膜衣錠０．２毫克 | 膜衣錠 | 強生化學製藥廠股份有限公司 | 2029/05/25 | 產褥期之出血、流產後之出血、分娩時之子宮弛緩出血、不正常出血、分娩第三期陣痛微弱。 |
| 內衛藥製字第007872號 | "尼斯可"縮水蘋果酸麥角新鹼片 | 錠劑 | 尼斯可生技股份有限公司 | 2029/05/25 | 弛緩性子宮出血、分娩後出血、子宮收縮不全、流產出血 |
| 內衛藥製字第009702號 | "新喜"美宮錠０．２公絲 | 錠劑 | 新喜國際企業股份有限公司 | 2028/05/25 | 產褥期出血、分娩時子宮弛緩出血、產後防止出血、產後子宮收縮不全 |
| 內衛藥製字第009847號 | 縮水蘋果酸麥角新鹼錠 | 錠劑 | 人人化學製藥股份有限公司 | 2027/12/31 | 產科用於產後促使子宮復原及預防出血過多、偏頭痛 |
| 內衛藥製字第009850號 | 〝人人〞縮水蘋果酸麥角新鹼注射液 | 注射劑 | 人人化學製藥股份有限公司 | 2029/12/31 | 產後或流產後促進子宮之復元及預防出血過多 |
| 內衛藥製字第012732號 | 縮水蘋果酸麥角新鹼片 | 錠劑 | 中生生技製藥股份有限公司淡水廠 | 2028/05/25 | 產後子宮肌張力弛緩而致之血崩症、偏頭痛 |
| 內衛藥製字第013083號 | 爾可利錠 | 錠劑 | 豐田藥品股份有限公司 | 2027/08/20 | 產褥期之出血、子宮內膜搔爬後之出血、流產後之出血、子宮弛緩之出血、子宮不正常出血、分娩第三期陣痛微弱 |
| 衛署藥製字第001605號 | 縮水蘋果酸麥角新/片 | 錠劑 | 中美兄弟製藥股份有限公司 | 2028/05/25 | 一般婦產科之出血（如分娩時子宮弛緩性出血、產褥期之出血、流產後出血、子宮內膜搔爬後之出血） |
| 衛署藥製字第003786號 | 麥角新 生僉 注射液 | 注射劑 | 安星製藥股份有限公司 | 2028/05/25 | 產後出血、子宮異常出血、流產後出血、分娩時子宮弛緩出血、分娩第三期陣痛微弱 |
| 衛署藥製字第014363號 | 縮水蘋果酸麥角新注射液 | 注射劑 | 台裕化學製藥廠股份有限公司 | 2030/02/27 | 分娩後之子宮弛緩、子宮收縮不全、弛緩性出血之預防及止血 |
| 衛署藥製字第015273號 | "應元"縮水蘋果酸麥角新鹼注射液 | 注射劑 | 應元化學製藥股份有限公司 | 2028/07/13 | 產褥期出血、促進產後子宮之復元及預防出血過多 |
| 衛署藥製字第017720號 | "優良"優復安錠（縮水蘋果酸麥角新鹼） | 錠劑 | 優良化學製藥股份有限公司 | 2029/06/01 | 預防及治療產後子宮出血 |
| 衛署藥製字第018516號 | "優良"優復安注射液（縮水蘋果酸麥角新鹼） | 注射劑 | 優良化學製藥股份有限公司 | 2028/08/31 | 生產後及流產後出血 |
| 衛署藥製字第024272號 | "正和"益兒宮糖衣錠（縮蘋果酸麥角新生僉） | 糖衣錠 | 正和製藥股份有限公司新營廠 | 2028/05/25 | 促進子宮收縮及治療子宮出血 |
| 衛署藥製字第029626號 | 意如宮注射液（縮水蘋果酸麥角新/） | 注射劑 | 永信藥品工業股份有限公司 | 2030/02/13 | 分娩後之子宮弛緩、子宮弛緩性出血、流產後出血、產褥期出血、子宮內膜刮除後出血之預防及治療、偏頭痛。 |
| 衛部藥輸字第027396號 | 縮蘋酸麥角新鹼 | （粉） | 新雙隆生技股份有限公司 | 2028/03/01 | 子宮收縮藥 |
| 衛部藥輸字第027478號 | 縮蘋酸麥角新生僉 | 粉劑 | 仁友興業股份有限公司 | 2028/07/26 | 子宮收縮藥 |

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（1 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 內衛藥製字第002200號 | 益兒可針 | ERGONOVINE MALEATE、ASCORBIC ACID (VIT C) | 注射劑 | 產褥期之出血、流產後之出血、分娩時之子宮弛緩性出血、不正常出血等 |

<details><summary><strong>已註銷</strong>（83 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第000046號</td><td>麥角新/錠</td><td>ERGONOVINE MALEATE</td><td>2002/09/02</td></tr><tr><td>內衛藥製字第000287號</td><td>益妳好－甲糖衣錠</td><td>MENADIONE (VIT K3)、CARBAZOCHROME、ERGONOVINE MALEATE、BENACTYZ…</td><td>1989/11/25</td></tr><tr><td>內衛藥製字第000390號</td><td>催娩糖衣錠</td><td>QUININE HCL、ERGONOVINE MALEATE、PAPAVERINE HCL</td><td>1993/07/29</td></tr><tr><td>內衛藥製字第001793號</td><td>保美通針</td><td>ERGONOVINE MALEATE、SPARTEINE SULFATE、ASCORBIC ACID (VIT C)</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第002701號</td><td>縮水蘋果酸麥角新/注射液０．０２％</td><td>ERGONOVINE MALEATE</td><td>2013/10/15</td></tr><tr><td>內衛藥製字第002908號</td><td>蘋果酸麥角新/注射液</td><td>ERGONOVINE MALEATE</td><td>2013/04/08</td></tr><tr><td>內衛藥製字第003182號</td><td>麥角蘋注射液</td><td>ERGONOVINE MALEATE</td><td>2016/01/19</td></tr><tr><td>內衛藥製字第003242號</td><td>安產糖衣錠</td><td>ETHAVERINE HCL (eq to BALBONIN) (eq to Ethylpapaverine HCl)、…</td><td>2000/08/04</td></tr><tr><td>內衛藥製字第004304號</td><td>縮水蘋果酸麥角新/糖衣片</td><td>ERGONOVINE MALEATE</td><td>2015/04/15</td></tr><tr><td>內衛藥製字第004784號</td><td>縮水蘋果酸麥角新鹼錠０．２公絲</td><td>ERGONOVINE MALEATE</td><td>1998/03/31</td></tr><tr><td>內衛藥製字第005085號</td><td>益婦明注</td><td>ERGONOVINE MALEATE</td><td>1998/12/24</td></tr><tr><td>內衛藥製字第005177號</td><td>縮水蘋果酸麥角新/錠</td><td>ERGONOVINE MALEATE</td><td>2013/10/01</td></tr><tr><td>內衛藥製字第006364號</td><td>麥托年錠</td><td>ERGONOVINE MALEATE</td><td>1993/07/20</td></tr><tr><td>內衛藥製字第006925號</td><td>益婦明片</td><td>ERGONOVINE MALEATE</td><td>2013/06/10</td></tr><tr><td>內衛藥製字第007126號</td><td>益爾康美得林注射液</td><td>ASCORBIC ACID (VIT C)、ERGONOVINE MALEATE</td><td>1991/06/05</td></tr><tr><td>內衛藥製字第009320號</td><td>娩可敏糖衣錠</td><td>ERGONOVINE MALEATE</td><td>2010/11/18</td></tr><tr><td>內衛藥製字第013362號</td><td>誘娩膠囊</td><td>ERGONOVINE MALEATE、QUININE HCL、PAPAVERINE HCL</td><td>2013/07/11</td></tr><tr><td>內衛藥製字第013372號</td><td>益爾可錠</td><td>ERGONOVINE MALEATE</td><td>2013/10/07</td></tr><tr><td>內衛藥製字第013902號</td><td>縮水蘋果酸麥角新鹼片</td><td>ERGONOVINE MALEATE</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第015148號</td><td>蘋果酸麥角新鹼片</td><td>ERGONOVINE MALEATE</td><td>2013/10/07</td></tr><tr><td>內衛藥輸字第002548號</td><td>美生露</td><td>ERGONOVINE MALEATE</td><td>2000/10/20</td></tr><tr><td>內衛藥輸字第002635號</td><td>美生露片</td><td>ERGONOVINE MALEATE</td><td>2000/10/20</td></tr><tr><td>內衛藥輸字第002865號</td><td>新多美定</td><td>ERGONOVINE MALEATE、OXYTOCIN</td><td>1985/12/26</td></tr><tr><td>內衛藥輸字第004358號</td><td>蘋果酸麥角新鹼注射液</td><td>ERGONOVINE MALEATE</td><td>1984/06/05</td></tr><tr><td>內衛藥輸字第004803號</td><td>蘋果酸麥角新鹼針</td><td>ERGONOVINE MALEATE</td><td>1986/06/20</td></tr><tr><td>內衛藥輸字第005356號</td><td>斯肯麥角新鹼針</td><td>ERGONOVINE MALEATE</td><td>1986/01/16</td></tr><tr><td>內衛藥輸字第005357號</td><td>斯肯麥角新鹼片</td><td>ERGONOVINE MALEATE</td><td>1987/03/24</td></tr><tr><td>內衛藥輸字第005361號</td><td>雅克麥角新鹼片</td><td>ERGONOVINE MALEATE</td><td>2000/10/16</td></tr><tr><td>內衛藥輸字第005918號</td><td>歐葛百新</td><td>ERGONOVINE MALEATE</td><td>1991/02/01</td></tr><tr><td>內衛藥輸字第006176號</td><td>歐葛百新</td><td>ERGONOVINE MALEATE</td><td>1991/02/01</td></tr><tr><td>內衛藥輸字第006507號</td><td>縮水蘋果酸麥角新/</td><td>ERGONOVINE MALEATE</td><td>1985/09/17</td></tr><tr><td>內衛藥輸字第007931號</td><td>速把得寧</td><td>CARBAZOCHROME、METHYL HESPERIDIN、SPARTEINE SULFATE、ERGONOVINE…</td><td>1991/01/31</td></tr><tr><td>內衛藥輸字第008322號</td><td>蘋果酸麥角新/注射液</td><td>ERGONOVINE MALEATE</td><td>2000/10/20</td></tr><tr><td>衛署藥製字第000295號</td><td>易爾果速注射液</td><td>SPARTEINE SULFATE、ERGONOVINE MALEATE、ASCORBATE (SODIUM)</td><td>1991/05/06</td></tr><tr><td>衛署藥製字第000360號</td><td>易生注射液</td><td>OXYTOCIN、ERGONOVINE MALEATE</td><td>1991/05/20</td></tr><tr><td>衛署藥製字第002549號</td><td>意如宮錠</td><td>ERGONOVINE MALEATE</td><td>1987/08/21</td></tr><tr><td>衛署藥製字第004289號</td><td>娩朗糖衣錠</td><td>PAPAVERINE HCL、QUININE HCL、ERGONOVINE MALEATE</td><td>2023/07/03</td></tr><tr><td>衛署藥製字第005278號</td><td>縮水蘋果酸麥角新鹼注射液０．２公絲</td><td>ERGONOVINE MALEATE</td><td>2009/10/21</td></tr><tr><td>衛署藥製字第005279號</td><td>伊舒宮錠</td><td>ERGONOVINE MALEATE</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第005426號</td><td>縮水蘋果酸麥角新/錠</td><td>ERGONOVINE MALEATE</td><td>1988/12/31</td></tr><tr><td>衛署藥製字第005992號</td><td>能利娩膠囊</td><td>ERGONOVINE MALEATE、QUININE HCL、PAPAVERINE HCL</td><td>1999/08/23</td></tr><tr><td>衛署藥製字第006003號</td><td>"大豐"麥角新鹼膜衣錠</td><td>ERGONOVINE MALEATE</td><td>2025/05/29</td></tr><tr><td>衛署藥製字第008916號</td><td>意如宮注射液</td><td>ERGONOVINE MALEATE</td><td>1987/06/19</td></tr><tr><td>衛署藥製字第010370號</td><td>醫宮能錠</td><td>ERGONOVINE MALEATE</td><td>2000/08/04</td></tr><tr><td>衛署藥製字第010664號</td><td>益護注射液</td><td>SPARTEINE SULFATE、ERGONOVINE MALEATE</td><td>2007/05/09</td></tr><tr><td>衛署藥製字第013503號</td><td>縮水蘋果酸麥角新/錠</td><td>ERGONOVINE MALEATE</td><td>2014/06/11</td></tr><tr><td>衛署藥製字第013714號</td><td>縮水蘋果酸麥角新鹼糖衣錠</td><td>ERGONOVINE MALEATE</td><td>2014/11/19</td></tr><tr><td>衛署藥製字第014299號</td><td>縮水蘋果酸麥角新/糖衣錠</td><td>ERGONOVINE MALEATE</td><td>1989/08/17</td></tr><tr><td>衛署藥製字第014317號</td><td>縮免停注射液</td><td>ERGONOVINE MALEATE、SPARTEINE SULFATE</td><td>2007/05/09</td></tr><tr><td>衛署藥製字第014426號</td><td>娩可敏錠０．２公絲</td><td>ERGONOVINE MALEATE</td><td>2010/11/18</td></tr><tr><td>衛署藥製字第015117號</td><td>縮水蘋果酸麥角新/錠</td><td>ERGONOVINE MALEATE</td><td>2013/10/15</td></tr><tr><td>衛署藥製字第015831號</td><td>縮水蘋果酸麥角新/注射液</td><td>ERGONOVINE MALEATE</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第015832號</td><td>縮水蘋果酸麥角新/錠</td><td>ERGONOVINE MALEATE</td><td>2009/12/30</td></tr><tr><td>衛署藥製字第016941號</td><td>縮水蘋果酸麥角新鹼錠　〝順華〞</td><td>ERGONOVINE MALEATE</td><td>2016/09/12</td></tr><tr><td>衛署藥製字第017820號</td><td>縮水蘋果酸麥角新/錠</td><td>ERGONOVINE MALEATE</td><td>2022/05/05</td></tr><tr><td>衛署藥製字第017980號</td><td>安宮能錠０．５公絲（縮水蘋果酸麥角新鹼）</td><td>ERGONOVINE MALEATE</td><td>2005/11/14</td></tr><tr><td>衛署藥製字第019170號</td><td>縮保宮糖衣錠</td><td>BENACTYZINE HCL、ERGONOVINE MALEATE、SPARTEINE SULFATE、MENADIO…</td><td>1987/06/02</td></tr><tr><td>衛署藥製字第019262號</td><td>縮水蘋果酸麥角新鹼錠</td><td>ERGONOVINE MALEATE</td><td>2013/10/15</td></tr><tr><td>衛署藥製字第023151號</td><td>縮蘋果酸麥角新鹼糖衣錠</td><td>ERGONOVINE MALEATE</td><td>2024/01/04</td></tr><tr><td>衛署藥製字第023727號</td><td>益婦康糖衣錠</td><td>METHYL HESPERIDIN、CARBAZOCHROME、SPARTEINE SULFATE、ERGONOVINE…</td><td>2007/05/09</td></tr><tr><td>衛署藥製字第024528號</td><td>縮蘋果酸麥角新鹼注射液０．２公絲/公撮</td><td>ERGONOVINE MALEATE</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第024674號</td><td>益宮縮注射液</td><td>ERGONOVINE MALEATE、SPARTEINE SULFATE</td><td>2007/05/09</td></tr><tr><td>衛署藥製字第026113號</td><td>樂你康錠</td><td>ERGONOVINE MALEATE、SPARTEINE SULFATE、MENADIONE (VIT K3)、ETHE…</td><td>2007/05/09</td></tr><tr><td>衛署藥製字第033769號</td><td>易爾果速注射液</td><td>ASCORBIC ACID (VIT C)、ERGONOVINE MALEATE、SPARTEINE SULFATE</td><td>2000/08/04</td></tr><tr><td>衛署藥製字第033875號</td><td>易生注射液</td><td>ERGONOVINE MALEATE、OXYTOCIN</td><td>1998/03/02</td></tr><tr><td>衛署藥輸字第001981號</td><td>麥角新/片</td><td>ERGONOVINE MALEATE、MAGNESIUM ALUMINUM METASILICATE (NEUSILIN…</td><td>1988/11/08</td></tr><tr><td>衛署藥輸字第002223號</td><td>縮水蘋果酸麥角新/</td><td>ERGONOVINE MALEATE</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第002689號</td><td>縮水蘋果酸麥角新/</td><td>ERGONOVINE MALEATE</td><td>1993/02/16</td></tr><tr><td>衛署藥輸字第002829號</td><td>縮水蘋果酸麥角新/</td><td>ERGONOVINE MALEATE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第003625號</td><td>縮水蘋果酸麥角新/</td><td>ERGONOVINE MALEATE</td><td>2000/09/05</td></tr><tr><td>衛署藥輸字第003728號</td><td>縮水蘋果酸麥角新/</td><td>ERGONOVINE MALEATE</td><td>1990/07/03</td></tr><tr><td>衛署藥輸字第003742號</td><td>保婦針</td><td>SPARTEINE SULFATE、ERGONOVINE MALEATE、ASCORBIC ACID (VIT C)</td><td>1990/10/11</td></tr><tr><td>衛署藥輸字第003755號</td><td>保婦丸</td><td>ERGONOVINE MALEATE、DIMETHYLAMINOETHYL-BETA-BENZILAMIDE HCL、S…</td><td>1990/10/11</td></tr><tr><td>衛署藥輸字第004804號</td><td>縮水蘋果酸麥角新/</td><td>ERGONOVINE MALEATE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第006943號</td><td>縮水蘋果酸麥角新鹼</td><td>ERGONOVINE MALEATE</td><td>1998/06/17</td></tr><tr><td>衛署藥輸字第011359號</td><td>麥角新/糖衣錠０、５公絲</td><td>ERGONOVINE MALEATE</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第011840號</td><td>縮水蘋果酸麥角新/粉劑</td><td>ERGONOVINE MALEATE</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第012615號</td><td>收縮寧錠</td><td>ERGONOVINE MALEATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第012762號</td><td>蘋果酸麥角新鹼</td><td>ERGONOVINE MALEATE</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第014054號</td><td>縮蘋果酸麥角新/粉劑</td><td>ERGONOVINE MALEATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第014478號</td><td>欣多美定注射液５ＩＵ/ＭＬ</td><td>OXYTOCIN、ERGONOVINE MALEATE</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第014603號</td><td>麥角新/注射液０．５公絲/公撮</td><td>ERGONOVINE MALEATE</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第017934號</td><td>縮水蘋果酸麥角新/</td><td>ERGONOVINE MALEATE</td><td>2005/06/16</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜中記錄的禁忌關聯**（來自 TxGNN 知識圖譜，並非仿單文字）：高血壓、癲癇、腎臟疾病、肝臟疾病、膽囊疾病、腦中風與腦血管疾患、腦梗塞、閉塞性動脈硬化症、HELLP 症候群等。
- **藥物交互作用**：資料庫共記錄 83 項，其中列為嚴重（Major）的包括 Isometheptene、Epinephrine、Ephedrine、Lorcaserin、Clarithromycin、Cobicistat；中度的包括 Doxycycline、Tetracycline、Aprepitant、Dexamethasone、Cimetidine、Minocycline、Miconazole、Clotrimazole 等。
- 麥角類藥物具血管收縮作用，與 CYP3A4 抑制劑（如 Clarithromycin、Cobicistat）併用時，有血管缺血風險。

其他安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 針對毛髮過多症沒有任何臨床試驗或文獻，機轉上也缺乏合理性，僅有 TxGNN 模型分數支持，證據等級為 L5。
- Ergometrine 具血管收縮作用，且知識圖譜記錄多項心腦血管相關禁忌，用於非危及生命的美容或皮膚問題，風險效益比不佳。

**若要推進需要：**
- 補齊詳細的作用機轉資料，並釐清是否有任何與毛囊或毛髮週期相關的路徑。
- 進行系統性文獻檢索與前臨床研究（如毛囊細胞或動物模型），先驗證是否存在生物效應。
- 若有任何訊號，再評估局部給藥等低全身暴露方案的可行性與安全性。
- 附帶說明：排名第 7 的偏頭痛 (migraine disorder) 在機轉上較為合理（麥角類具血清素受體活性，部分台灣許可證適應症也列有偏頭痛），但目前文獻僅有綜述與個案報告，且有腦血管風險，可作為另行評估的研究問題。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測原文未改寫；證據等級與決策只依重審結果（降級、升級或撤回）更新，原值列在下表。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「methylergonovine 是 ergometrine 的活性代謝物」 | 報告重生後已無此錯誤（2026-10-15：新報告未再稱 methylergonovine 為 ergometrine 的活性代謝物；原為更正） | [NLM MeSH：Methylergonovine（D008755）](https://meshb.nlm.nih.gov/record/ui?ui=D008755)；[DailyMed：Methylergonovine Maleate Tablets, USP 仿單（Teva）](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d8e4b8ed-3289-4611-8a61-2392a4bf6072)；[emc：Ergometrine Injection BP 0.05% w/v SmPC §5.2](https://www.medicines.org.uk/emc/product/6265/smpc) |
| 2026-10-03 | 結論段「及其活性代謝物 methylergonovine」 | 報告重生後已無此錯誤（2026-10-15：新報告結論未再提及 methylergonovine 為代謝物；原為更正） | [NLM MeSH：Methylergonovine（D008755）](https://meshb.nlm.nih.gov/record/ui?ui=D008755)；[DailyMed：Methylergonovine Maleate Tablets, USP 仿單（Teva）](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d8e4b8ed-3289-4611-8a61-2392a4bf6072) |
| 2026-10-03 | 預測理由稱 ergometrine 作用於 5-HT1B/1D（仿單未載） | 報告重生後已無此錯誤（2026-10-28：報告重產與事實層改寫後，本紀錄指出的錯誤原文已不在正文（僅見於本頁查核紀錄表或程式產生的許可證表）（2026-10-28 用戶核准的處理方案）；原為加註（2026-10-16 修訂，前版保留於紀錄）） | [emc：Ergometrine Injection BP 0.05% w/v SmPC §5.1](https://www.medicines.org.uk/emc/product/6265/smpc) |
| 2026-10-03 | 偏頭痛預測標記待重審 | 標記待重審 → 已重審（見下列重審結果） | [emc：Ergometrine Injection BP 0.05% w/v SmPC §5.1](https://www.medicines.org.uk/emc/product/6265/smpc) |
| 2026-10-03 | 新增「作用機轉」段（每點附仿單來源） | 新增附來源段落 | [emc：Ergometrine Injection BP 0.05% w/v SmPC §5.1](https://www.medicines.org.uk/emc/product/6265/smpc) |
| 2026-10-16 | 偏頭痛預測重審結果 | 報告重生後已無此錯誤（2026-10-28：報告重產與事實層改寫後，本紀錄指出的錯誤原文已不在正文（僅見於本頁查核紀錄表或程式產生的許可證表）（2026-10-28 用戶核准的處理方案）；原為重審：升級，證據等級 L4→L3；證據等級：原「證據等級／L5（多毛症）；L4（偏頭痛）」→「證據等級／L5（多毛症）；L3（偏頭痛）」（2026-10-16 修訂，前版保留於紀錄）） | [PubMed：Menstrual migraine and intermittent ergonovine therapy（PMID 2759844）](https://pubmed.ncbi.nlm.nih.gov/2759844/)；[PubMed：Microiontophoretic application of serotonin (5HT)1B/1D agonists inhibits trigeminal cell firing in the cat（PMID 9448572）](https://pubmed.ncbi.nlm.nih.gov/9448572/)；[PubMed：Oral methylergonovine maleate for refractory migraine and cluster headache prevention（PMID 23432443）](https://pubmed.ncbi.nlm.nih.gov/23432443/)；[PubMed：Efficacy and tolerability of intravenous methylergonovine in migraine female patients attending the emergency department: a pilot open-label study（PMID 19895705）](https://pubmed.ncbi.nlm.nih.gov/19895705/)；[PubMed：QT prolongation, Torsade de Pointes, myocardial ischemia from coronary vasospasm, and headache medications. Part 1: review of serotonergic cardiac adverse events with a triptan case（PMID 23216317）](https://pubmed.ncbi.nlm.nih.gov/23216317/)；[PubMed：Pleural thickening caused by Sansert and Ergotrate in the treatment of migraine（PMID 6773347）](https://pubmed.ncbi.nlm.nih.gov/6773347/) |
| 2026-10-16 | 標題把多毛症寫成「猖毛症」，並把已核准的偏頭痛寫成新用途 | 報告重生後已無此錯誤（2026-10-28：報告重產與事實層改寫後，本紀錄指出的錯誤原文已不在正文（僅見於本頁查核紀錄表或程式產生的許可證表）（2026-10-28 用戶核准的處理方案）；原為更正（2026-10-16 修訂，前版保留於紀錄）） | [本頁快速總覽「預測新適應症」列](https://twtxgnn.yao.care/drugs/ergometrine/)；[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 偏頭痛評為 L4，未納入本藥觀察性研究 | 查核撤回（2026-10-16：重審結果已改為升級並把快速總覽的偏頭痛等級改成 L3，本筆加註不再需要；原為加註（2026-10-16 修訂，前版保留於紀錄）） | [PubMed：Menstrual migraine and intermittent ergonovine therapy（PMID 2759844）](https://pubmed.ncbi.nlm.nih.gov/2759844/) |
| 2026-10-16 | 一句話總結稱偏頭痛僅有 2 篇間接文獻 | 報告重生後已無此錯誤（2026-10-28：報告重產與事實層改寫後，本紀錄指出的錯誤原文已不在正文（僅見於本頁查核紀錄表或程式產生的許可證表）（2026-10-28 用戶核准的處理方案）；原為加註（2026-10-16 修訂，前版保留於紀錄）） | [PubMed：Menstrual migraine and intermittent ergonovine therapy（PMID 2759844）](https://pubmed.ncbi.nlm.nih.gov/2759844/) |
| 2026-10-16 | 結論稱偏頭痛只有間接回顧與個案報告 | 報告重生後已無此錯誤（2026-10-28：報告重產與事實層改寫後，本紀錄指出的錯誤原文已不在正文（僅見於本頁查核紀錄表或程式產生的許可證表）（2026-10-28 用戶核准的處理方案）；原為加註（2026-10-16 修訂，前版保留於紀錄）） | [PubMed：Menstrual migraine and intermittent ergonovine therapy（PMID 2759844）](https://pubmed.ncbi.nlm.nih.gov/2759844/) |
| 2026-10-16 | 稱只有一張許可證列有偏頭痛 | 報告重生後已無此錯誤（2026-10-28：報告重產與事實層改寫後，本紀錄指出的錯誤原文已不在正文（僅見於本頁查核紀錄表或程式產生的許可證表）（2026-10-28 用戶核准的處理方案）；原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 原適應症取自已註銷許可證 | 報告重生後已無此錯誤（2026-10-28：報告重產與事實層改寫後，本紀錄指出的錯誤原文已不在正文（僅見於本頁查核紀錄表或程式產生的許可證表）（2026-10-28 用戶核准的處理方案）；原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 一句話總結的原用途漏列偏頭痛 | 許可證表程式修正後已無此錯誤（2026-10-28：一句話總結依本紀錄更正，補上現行有效許可證核准的偏頭痛（2026-10-28 用戶核准的處理方案）；原為更正（2026-10-16 修訂，前版保留於紀錄）） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 一句話總結把偏頭痛當成新的再利用方向 | 查核撤回（2026-10-16：與相鄰的「一句話總結的原用途漏列偏頭痛」更正說明相同，已併入該筆；原為加註（2026-10-16 修訂，前版保留於紀錄）） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 頁首證據等級 | 頁首等級依總覽表重算（原 L4→L3） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

