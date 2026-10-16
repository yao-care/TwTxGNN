---
layout: default
title: Griseofulvin
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 5
monitor_inn: "Griseofulvin"
predicted_indications: ["myiasis", "furuncular myiasis", "wound myiasis", "creeping myiasis", "echinococcus granulosus infectious disease"]
last_modified_at: 2026-10-16
description: "Griseofulvin：預測新適應症為蠅蛆症 (Myiasis)（證據等級 L5）。原適應症：甲癬（Onychomycosis）、髮癬（Tinea capitis），不適宜局部外用治療或局部外用無效的皮膚黴菌感染"
---

# Griseofulvin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Griseofulvin：從皮膚黴菌感染到蠅蛆症（Myiasis）

## 一句話總結

Griseofulvin（灰黴素）是口服抗黴菌藥，原本用於治療甲癬、髮癬等不適宜局部外用或外用無效的皮膚黴菌感染。
TxGNN 模型預測它可能對**蠅蛆症 (Myiasis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測訊號。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 甲癬（Onychomycosis）、髮癬（Tinea capitis），不適宜局部外用治療或局部外用無效的皮膚黴菌感染 |
| 預測新適應症 | 蠅蛆症 (Myiasis) |
| TxGNN 預測分數 | 99.41% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 76 張（有效單方 11／有效複方 0／已過期 2／已註銷 63） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知資訊，Griseofulvin 會干擾黴菌的微管功能與有絲分裂，這是它抗黴菌的基礎。

蠅蛆症是蠅類幼蟲寄生於人體組織所致，與黴菌感染的病原體完全不同。目前沒有已知機轉能把 Griseofulvin 的抗黴菌作用連到幼蟲感染。這個預測很可能來自知識圖譜的網路特徵相似性，而非生物學上的因果關係，因此合理性偏低。

同一批預測中還有三個蠅蛆症相關疾病（皮膚型蠅蛆症 furuncular myiasis、傷口蠅蛆症 wound myiasis、匍行性蠅蛆症 creeping myiasis），以及**細粒棘球蚴感染 (Echinococcus granulosus infection)**，分數皆在 99.3% 以上，且同樣沒有試驗或文獻支持。其中細粒棘球蚴感染有一個較弱的假說：Griseofulvin 作用於黴菌微管蛋白，而苯並咪唑類驅蟲藥作用於寄生蟲微管蛋白。但 Griseofulvin 本身並無已證實的驅蟲活性。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Griseofulvin 的不重複許可證共 **76 張**：有效單方 11 張、有效複方 0 張、已過期 2 張（未註銷但有效日期早於資料集日期）、已註銷 63 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（11 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 內衛藥製字第003414號 | 克黴敏片 | 錠劑 | 中國化學製藥股份有限公司新豐工廠 | 2028/05/09 | 甲癬（ＯＮＹＣＨＯＭＹＯＳＩＳ）、髮癬（ＴＩＮＥＡ ＣＡＰＩＴＩＳ）、不適宜局部外用治療或局部外用無效的皮膚黴菌感染。 |
| 衛署藥製字第007372號 | "生達" 灰黃黴素錠 | 錠劑 | 生達化學製藥股份有限公司 | 2029/09/13 | 甲癬（ＯＮＹＣＨＯＭＹＯＳＩＳ）、髮癬（ＴＩＮＥＡ ＣＡＰＩＴＩＳ），不適宜局部外用治療或局部外用無效的皮膚黴菌感染。 |
| 衛署藥製字第010941號 | "派頓"癬黴淨膠囊 | 膠囊劑 | 臺灣派頓化學製藥股份有限公司 | 2028/05/25 | 甲癬（Onychomyosis）、髮癬（Tinea capitis），不適宜局部外用治療或局部外用無效的皮膚黴菌感染。 |
| 衛署藥製字第019146號 | 格利癬錠（灰黴素） | 錠劑 | 政德製藥股份有限公司 | 2029/10/19 | 甲癬(Onychomyosis)、髮癬(Tinea Capitis)，不適宜局部外用治療或局部外用無效的皮膚黴菌感染。 |
| 衛署藥製字第024375號 | "元宙"灰黴素錠２５０毫克 | 錠劑 | 元宙化學製藥股份有限公司 | 2029/05/25 | 甲癬（ＯＮＹＣＨＯＭＹＳＩＳ）、髮癬（ＴＩＮＥＡ ＣＡＰＩＴＩＳ），不適宜局部外用治療或局部外用無故的皮膚黴菌感染。 |
| 衛署藥製字第025159號 | 克黴星錠５００毫克（灰黴素） | 錠劑 | 嘉林藥品有限公司 | 2029/02/14 | 甲癬 (Onychomyosis)、 髮癬 (Tinea Capitis)，不適宜局部外用治療或局部外用無效的皮膚黴菌感染 |
| 衛署藥製字第026877號 | 灰黴素膠囊２５０公絲 | 膠囊劑 | 嘉信藥品股份有限公司 | 2028/12/31 | 甲癬、髮癬，不適宜局部外用治療或局部外用無效的皮膚黴菌感染。 |
| 衛署藥製字第027109號 | 克膚癬錠５００公絲（灰黴素） | 錠劑 | 中美兄弟製藥股份有限公司 | 2029/05/25 | 甲癬(Onychomyosis)、髮癬(Tinea Capitis)，不適宜局部外用治療或局部外用無效的皮膚黴菌感染。 |
| 衛署藥製字第027776號 | "榮民"克癬錠500毫克(灰黴素) | 錠劑 | 榮民製藥股份有限公司 | 2028/08/15 | 甲癬（ＯＮＹＣＨＯＭＹＯＳＩＳ）、髮癬、（ＴＩＮＥＡ ＣＡＰＩＴＩＳ），不適宜局部外用治療或局部外用無效的皮膚黴菌感染。 |
| 衛署藥製字第028054號 | 膚友錠 | 錠劑 | 瑞士藥廠股份有限公司 | 2028/05/25 | 甲癬（ＯＮＹＣＨＯＭＹＯＳＩＳ）、髮癬（ＴＩＮＥＡ ＣＡＰＩＴＩＳ），不適宜局部外用治療或局部外用無效的皮膚黴菌感染。 |
| 衛署藥製字第028055號 | 膚友錠５００毫克 | 錠劑 | 瑞士藥廠股份有限公司 | 2028/05/25 | 甲癬（ＯＮＹＣＨＯＭＹＯＳＩＳ）、髮癬（ＴＩＮＥＡ ＣＡＰＩＴＩＳ），不適宜局部外用治療或局部外用無效的皮膚黴菌感染。 |

<details><summary><strong>已過期（未註銷但有效日期早於資料集日期 2026-09-29）</strong>（2 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>有效日期</th></tr></thead><tbody><tr><td>衛署藥製字第012523號</td><td>"聯邦" 克制黴錠</td><td>GRISEOFULVIN</td><td>2024/05/25</td></tr><tr><td>衛署藥製字第024572號</td><td>"聯邦"克制黴錠５００公絲（灰黴素）〝聯邦〞</td><td>GRISEOFULVIN</td><td>2024/05/25</td></tr></tbody></table></details>

<details><summary><strong>已註銷</strong>（63 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第007313號</td><td>黴可淨錠</td><td>GRISEOFULVIN</td><td>1998/06/01</td></tr><tr><td>內衛藥輸字第000795號</td><td>護星５００</td><td>GRISEOFULVIN</td><td>1985/10/03</td></tr><tr><td>內衛藥輸字第004556號</td><td>膚爾皮質達新ＵＦ片</td><td>GRISEOFULVIN</td><td>1985/09/26</td></tr><tr><td>內衛藥輸字第005882號</td><td>灰鏈素</td><td>GRISEOFULVIN</td><td>1985/09/23</td></tr><tr><td>內衛藥輸字第006262號</td><td>巴里歐軟膏</td><td>PECILOCIN、HYDROCORTISONE、GRISEOFULVIN、ALLANTOIN、NEOMYCIN (FR…</td><td>1985/12/31</td></tr><tr><td>衛署藥製字第004335號</td><td>克黴敏錠５００公絲</td><td>GRISEOFULVIN</td><td>1999/09/30</td></tr><tr><td>衛署藥製字第009019號</td><td>香港腳敏膠囊</td><td>GRISEOFULVIN</td><td>2002/09/05</td></tr><tr><td>衛署藥製字第011974號</td><td>扶星錠</td><td>GRISEOFULVIN</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第013591號</td><td>灰黴素錠</td><td>GRISEOFULVIN</td><td>2020/10/05</td></tr><tr><td>衛署藥製字第013594號</td><td>灰黴素錠</td><td>GRISEOFULVIN</td><td>2000/06/12</td></tr><tr><td>衛署藥製字第014740號</td><td>灰黴素錠５００公絲</td><td>GRISEOFULVIN</td><td>2010/03/18</td></tr><tr><td>衛署藥製字第015372號</td><td>灰黴素錠</td><td>GRISEOFULVIN</td><td>1990/10/04</td></tr><tr><td>衛署藥製字第016488號</td><td>灰徽素錠</td><td>GRISEOFULVIN</td><td>2000/08/08</td></tr><tr><td>衛署藥製字第016678號</td><td>方克黴錠１２５公絲（灰黴素）</td><td>GRISEOFULVIN</td><td>2015/06/17</td></tr><tr><td>衛署藥製字第017085號</td><td>克癬服錠（灰黴素）</td><td>GRISEOFULVIN</td><td>1991/06/19</td></tr><tr><td>衛署藥製字第017970號</td><td>利癬敏錠（灰黴素）</td><td>GRISEOFULVIN</td><td>1988/12/31</td></tr><tr><td>衛署藥製字第018700號</td><td>方克黴膠囊５００公絲（灰黴素）</td><td>GRISEOFULVIN</td><td>2015/06/17</td></tr><tr><td>衛署藥製字第018870號</td><td>豐癬寧錠（灰黴素）</td><td>GRISEOFULVIN</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第019323號</td><td>可威淨錠（灰黴素）</td><td>GRISEOFULVIN</td><td>2013/10/01</td></tr><tr><td>衛署藥製字第020384號</td><td>"華盛頓"吉膚黴素膠囊125毫克（灰黴素）</td><td>GRISEOFULVIN</td><td>2023/07/03</td></tr><tr><td>衛署藥製字第020385號</td><td>"華盛頓"吉膚黴素膠囊250毫克（灰黴素）</td><td>GRISEOFULVIN</td><td>2023/07/03</td></tr><tr><td>衛署藥製字第021319號</td><td>樂膚佳膠囊（灰黴素）</td><td>GRISEOFULVIN</td><td>1989/03/30</td></tr><tr><td>衛署藥製字第021550號</td><td>灰黴素錠</td><td>GRISEOFULVIN</td><td>1994/01/21</td></tr><tr><td>衛署藥製字第022541號</td><td>克膚鏈素膠囊（灰黴素）</td><td>GRISEOFULVIN</td><td>2012/04/25</td></tr><tr><td>衛署藥製字第023465號</td><td>葛利文錠（灰黴素）</td><td>GRISEOFULVIN</td><td>2016/09/08</td></tr><tr><td>衛署藥製字第024313號</td><td>"應元"護膚黴素膠囊（灰黴素）</td><td>GRISEOFULVIN</td><td>2024/04/19</td></tr><tr><td>衛署藥製字第024767號</td><td>克黴星膜衣錠１２５公絲（灰黴素）</td><td>GRISEOFULVIN</td><td>1991/01/29</td></tr><tr><td>衛署藥製字第025278號</td><td>灰黴素５００公絲膠囊</td><td>GRISEOFULVIN</td><td>2023/08/31</td></tr><tr><td>衛署藥製字第027698號</td><td>灰黴素錠</td><td>GRISEOFULVIN</td><td>1997/08/28</td></tr><tr><td>衛署藥製字第034962號</td><td>格利蘇芬膜衣錠５００公絲（灰黴素）</td><td>GRISEOFULVIN</td><td>2009/03/13</td></tr><tr><td>衛署藥製字第035243號</td><td>格利蘇芬膜衣錠１２５公絲（灰黴素）</td><td>GRISEOFULVIN</td><td>2005/11/08</td></tr><tr><td>衛署藥輸字第000098號</td><td>護星１２５錠</td><td>GRISEOFULVIN</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第000339號</td><td>格利蘇芬錠１２５毫克</td><td>GRISEOFULVIN</td><td>1988/08/17</td></tr><tr><td>衛署藥輸字第000517號</td><td>格利蘇芬錠５００公絲</td><td>GRISEOFULVIN</td><td>1990/02/07</td></tr><tr><td>衛署藥輸字第000728號</td><td>灰鏈素（微粒）</td><td>GRISEOFULVIN</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第002120號</td><td>灰鏈素</td><td>GRISEOFULVIN</td><td>2014/01/28</td></tr><tr><td>衛署藥輸字第002561號</td><td>灰鏈素</td><td>GRISEOFULVIN</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第004465號</td><td>克利斯丁錠１２５公絲</td><td>GRISEOFULVIN</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第004995號</td><td>利膚美錠５００公絲</td><td>GRISEOFULVIN</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第004997號</td><td>利膚美錠２５０公絲</td><td>GRISEOFULVIN</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第004998號</td><td>利膚美錠１２５公絲</td><td>GRISEOFULVIN</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第005295號</td><td>格利蘇芬</td><td>GRISEOFULVIN</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第005500號</td><td>格利文錠</td><td>GRISEOFULVIN</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第006323號</td><td>灰黴素</td><td>GRISEOFULVIN</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第006624號</td><td>灰鏈素</td><td>GRISEOFULVIN</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第009680號</td><td>灰黴素</td><td>GRISEOFULVIN</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第009791號</td><td>灰黴素</td><td>GRISEOFULVIN</td><td>1991/05/14</td></tr><tr><td>衛署藥輸字第010267號</td><td>可利適達錠</td><td>GRISEOFULVIN</td><td>1999/07/16</td></tr><tr><td>衛署藥輸字第010985號</td><td>灰黴素錠１２５公絲</td><td>GRISEOFULVIN</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第012186號</td><td>克灰敏錠５００公絲</td><td>GRISEOFULVIN</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第012885號</td><td>格利蘇芬錠１２５公絲</td><td>GRISEOFULVIN</td><td>1990/02/07</td></tr><tr><td>衛署藥輸字第013673號</td><td>可利適達錠</td><td>GRISEOFULVIN</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第014103號</td><td>灰鏈素</td><td>GRISEOFULVIN</td><td>1998/10/20</td></tr><tr><td>衛署藥輸字第014132號</td><td>膚爾皮質達新錠</td><td>GRISEOFULVIN</td><td>2013/12/05</td></tr><tr><td>衛署藥輸字第014199號</td><td>護星膜衣錠５００公絲</td><td>GRISEOFULVIN</td><td>1998/05/14</td></tr><tr><td>衛署藥輸字第014489號</td><td>巴里歐軟膏</td><td>NEOMYCIN (FRADIOMYCIN)、GRISEOFULVIN、ALLANTOIN、PECILOCIN、HYDR…</td><td>1989/09/11</td></tr><tr><td>衛署藥輸字第015721號</td><td>克黴適錠１２５公絲</td><td>GRISEOFULVIN</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第016852號</td><td>克黴適膜衣錠５００公絲</td><td>GRISEOFULVIN</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第017486號</td><td>格利蘇芬錠１２５公絲</td><td>GRISEOFULVIN</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第017532號</td><td>格利蘇芬錠５００公絲</td><td>GRISEOFULVIN</td><td>2010/05/31</td></tr><tr><td>衛署藥輸字第018557號</td><td>灰黴素</td><td>GRISEOFULVIN</td><td>2005/06/14</td></tr><tr><td>衛署藥輸字第019446號</td><td>灰黴素</td><td>GRISEOFULVIN</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第022110號</td><td>護星錠５００公絲</td><td>GRISEOFULVIN</td><td>2009/12/31</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜關聯，非仿單文字）：肝衰竭、紫質症（含遺傳性紫質症與紫質代謝疾病）、系統性紅斑性狼瘡（含兒童型）、物質濫用/依賴、顆粒球缺乏症、嗜中性白血球低下症（含週期性、先天性等各型）。
- **藥物交互作用**：已查得 234 筆交互作用，以下為部分範例。
  - 抗凝血/抗血小板藥：Warfarin、Apixaban、Rivaroxaban、Dicoumarol、Ticagrelor（中度）
  - 降血糖藥：Saxagliptin、Linagliptin、Repaglinide（中度）；Liraglutide（輕度）
  - 止吐藥：Aprepitant、Rolapitant（中度）
  - 抗瘧/驅蟲藥：Artemether、Mefloquine、Praziquantel（中度）
  - 其他：Eliglustat、Naloxegol、Nitisinone、Macimorelin、Fostamatinib（中度）；Acetylsalicylic acid（輕度）

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自 TxGNN 模型（L5），沒有臨床試驗或文獻佐證。
- Griseofulvin 的抗黴菌機轉與蠅蛆症病因無已知關聯，且藥物交互作用多、有血液學與肝臟相關的潛在風險。

**若要推進需要：**
- 補齊 Griseofulvin 的作用機轉資料（MOA）。
- 檢索是否有體外或動物模型顯示其對蠅蛆幼蟲或寄生蟲的活性。
- 若要探索，優先評估細粒棘球蚴感染的微管蛋白假說，先做體外驗證。
- 確認蠅蛆症現有標準治療（如手術清創、伊維菌素）的優勢，評估再利用的臨床必要性。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「76 筆…多為有效許可證」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

