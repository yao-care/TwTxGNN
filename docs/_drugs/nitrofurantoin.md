---
layout: default
title: Nitrofurantoin
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
---

# Nitrofurantoin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Nitrofurantoin：從 尿路感染 到 類風濕性關節炎

## 一句話總結

Nitrofurantoin（淋可輸）是一種合成抗菌劑，專門用於治療尿路感染。TxGNN 模型預測它對**類風濕性關節炎 (rheumatoid arthritis)** 有潛在關聯，但文獻證據顯示這主要是共病關係或藥物不良反應報告，而非治療效果。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 尿路感染（膀胱炎、腎盂炎、尿道炎） |
| 預測新適應症 | 類風濕性關節炎 (rheumatoid arthritis) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L5 |
| 台灣上市 | 已上市 |
| 許可證數 | 75 張（有效單方 4／有效複方 4／已註銷 67） |
| 建議決策 | Hold |

## 為什麼這個預測可能是偽相關？

Nitrofurantoin 通過損傷細菌 DNA 和抑制酶活性發揮殺菌作用，對革蘭氏陽性和陰性菌均有效。其作用局限於尿路，全身吸收有限。

**文獻回顧顯示：**
- 多篇文獻提及 nitrofurantoin 與類風濕性關節炎的關係，但主要是：
  1. **藥物性肺纖維化**：Nitrofurantoin 是已知可導致肺纖維化的藥物，這也是類風濕性關節炎的併發症
  2. **共病報告**：類風濕性關節炎患者使用 nitrofurantoin 治療尿路感染的病例報告
  3. **抗生素與 RA 惡化**：研究顯示某些抗生素可能觸發 RA 惡化

**缺乏治療證據：**
- 無證據顯示 nitrofurantoin 對 RA 有抗發炎或免疫調節作用
- Nitrofurantoin 主要局限於尿路，不適合全身性疾病治療

## 臨床試驗證據

無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 主要發現 |
|------|-----|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Journal Article | 抗生素使用與 RA 惡化的關係，nitrofurantoin 被列為研究藥物之一 |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case Report | Methotrexate 和 nitrofurantoin 交互作用導致不可逆肺纖維化 |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Journal Article | RA 患者住院治療間質性肺纖維化，部分與 nitrofurantoin 相關 |

這些文獻顯示 nitrofurantoin 與 RA 的關聯主要是**不良反應**（肺纖維化）或**共病治療**，而非治療效果。

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Nitrofurantoin 的不重複許可證共 **75 張**：有效單方 4 張、有效複方 4 張、已註銷 67 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（4 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第003893號 | 硝弗侖陶因錠１００公絲 | 錠劑 | 榮民製藥股份有限公司 | 2030/01/16 | 尿道感染、膀胱炎 |
| 衛署藥製字第010246號 | 汝路朗腸溶錠 | 腸溶錠 | 永信藥品工業股份有限公司 | 2028/05/25 | 尿路感染症、腎盂炎、腎盂腎炎、膀胱炎 |
| 衛署藥製字第023320號 | 裕免淋錠（硝基/喃妥因） | 錠劑 | 台裕化學製藥廠股份有限公司 | 2028/05/25 | 尿道炎、腎盂炎、膀胱炎、前列腺炎、淋病 |
| 衛署藥製字第030312號 | 尼卜魯富蘭脫寧膠囊１００公絲（耐挫敷妥因） | 膠囊劑 | 明大化學製藥股份有限公司 | 2028/12/31 | 腎盂炎、腎盂腎炎、膀胱炎、尿道炎、淋病。 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（4 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 內衛藥製字第008536號 | "美"克淨淋膠囊 | SULFAMETHOXYPYRIDAZINE、NITROFURANTOIN | 膠囊劑 | 淋病、急慢性尿道炎、膀胱炎、腎盂炎、扁桃腺炎、咽喉炎、中耳炎、鼻腔炎、口腔炎、腸炎 |
| 內衛藥製字第012890號 | 可安淋膠囊 | NITROFURANTOIN、SULFAMETHOXYPYRIDAZINE | 膠囊劑 | 淋病、急、慢性尿道炎、膀胱炎、腎盂炎、肩桃腺炎、口腔炎、咽喉炎、中耳炎、腸炎、腸內異常醱酵 |
| 內衛藥製字第013750號 | "約克"力克林膠囊 | NITROFURANTOIN、SULFAMETHOXYPYRIDAZINE | 膠囊劑 | 尿路感染症、腎盂炎、膀胱炎、淋病、子宮內膜炎、軟性下疳、痢疾、腸炎、肺炎、支氣管炎、猩紅熱、丹毒、中耳炎、扁桃腺炎、咽喉炎 |
| 內衛藥製字第014465號 | 服樂克淋片 | SULFAMETHOXYPYRIDAZINE、NITROFURANTOIN | 錠劑 | 淋病、梅毒、尿道炎、腎臟炎、腎盂炎、前列腺炎、軟性下疳、開刀前後的感染、子宮內膜炎、子宮附屬器炎、乳腺炎、子宮周圍炎。 |

<details><summary><strong>已註銷</strong>（67 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第001068號</td><td>舒滿拔膠囊</td><td>SULFAMETHOXYPYRIDAZINE、NITROFURANTOIN</td><td>1993/04/29</td></tr><tr><td>內衛藥製字第001539號</td><td>寧路糖衣錠</td><td>NITROFURANTOIN</td><td>2023/07/14</td></tr><tr><td>內衛藥製字第002916號</td><td>淋得樂淨針</td><td>NITROFURANTOIN SODIUM</td><td>2013/04/08</td></tr><tr><td>內衛藥製字第003501號</td><td>滅淋白膠囊</td><td>NITROFURANTOIN、SULFAMETHOXYPYRIDAZINE</td><td>2005/04/08</td></tr><tr><td>內衛藥製字第004450號</td><td>富可治膠囊</td><td>NITROFURANTOIN、SULFAMETHAZINE (SULFADIMIDINE)</td><td>2013/10/01</td></tr><tr><td>內衛藥製字第005258號</td><td>淋克兒片</td><td>NITROFURANTOIN</td><td>1988/12/31</td></tr><tr><td>內衛藥製字第005901號</td><td>乃可法蘭妥片</td><td>NITROFURANTOIN</td><td>1998/01/12</td></tr><tr><td>內衛藥製字第006324號</td><td>哈朗－Ｓ錠</td><td>NITROFURANTOIN、SULFAMETHOXYPYRIDAZINE</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第008060號</td><td>離禍淋片</td><td>NITROFURANTOIN</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第008062號</td><td>離禍淋針</td><td>NITROFURANTOIN</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第008520號</td><td>清淋淨腸溶錠</td><td>NITROFURANTOIN</td><td>2010/11/18</td></tr><tr><td>內衛藥製字第008594號</td><td>可樂淋膠囊</td><td>ALUMINUM SILICATE、NITROFURANTOIN、SULFAMETHOXYPYRIDAZINE</td><td>2013/03/04</td></tr><tr><td>內衛藥製字第008977號</td><td>淋可輸片１００公絲</td><td>NITROFURANTOIN</td><td>2023/07/03</td></tr><tr><td>內衛藥製字第009835號</td><td>利炎脫淋膠囊</td><td>NITROFURANTOIN、SULFAMETHOXYPYRIDAZINE</td><td>2010/02/08</td></tr><tr><td>內衛藥製字第011765號</td><td>殺克淋膠囊</td><td>ALUMINUM SILICATE、NITROFURANTOIN、SULFAMETHOXYPYRIDAZINE</td><td>1989/08/17</td></tr><tr><td>內衛藥製字第013052號</td><td>富朗音片</td><td>NITROFURANTOIN</td><td>2009/12/30</td></tr><tr><td>內衛藥製字第013054號</td><td>驅淋－Ｓ膠囊</td><td>NITROFURANTOIN、SULFAMETHOXYPYRIDAZINE</td><td>2009/12/30</td></tr><tr><td>內衛藥製字第014370號</td><td>淋可樂膠囊</td><td>NITROFURANTOIN、SULFAMETHOXYPYRIDAZINE</td><td>2004/05/31</td></tr><tr><td>內衛藥製字第016750號</td><td>愛可樂散</td><td>SULFAMETHOXYPYRIDAZINE、NITROFURANTOIN</td><td>2015/06/29</td></tr><tr><td>內衛藥製字第016942號</td><td>蘭鼓樂膠囊１００公絲</td><td>NITROFURANTOIN</td><td>2015/03/03</td></tr><tr><td>內衛藥輸字第001330號</td><td>硝基＊喃妥因</td><td>NITROFURANTOIN</td><td>1985/08/20</td></tr><tr><td>內衛藥輸字第001954號</td><td>尼得魯法蘭得因鈉</td><td>NITROFURANTOIN SODIUM</td><td>1988/09/05</td></tr><tr><td>內衛藥輸字第002153號</td><td>尼得魯法蘭得因</td><td>NITROFURANTOIN</td><td>1988/09/05</td></tr><tr><td>內衛藥輸字第004023號</td><td>賜多福片</td><td>NITROFURANTOIN</td><td>1999/09/22</td></tr><tr><td>內衛藥輸字第004088號</td><td>硝基＊喃多因</td><td>NITROFURANTOIN</td><td>2004/12/23</td></tr><tr><td>內衛藥輸字第005746號</td><td>梅尿淋片５０公絲</td><td>NITROFURANTOIN</td><td>2000/10/16</td></tr><tr><td>內衛藥輸字第005747號</td><td>梅尿淋片１００公絲</td><td>NITROFURANTOIN</td><td>1986/05/29</td></tr><tr><td>內衛藥輸字第005751號</td><td>弗利淋片</td><td>NITROFURANTOIN</td><td>2000/10/16</td></tr><tr><td>內衛藥輸字第005753號</td><td>弗利淋針</td><td>NITROFURANTOIN</td><td>2000/10/16</td></tr><tr><td>內衛藥輸字第006356號</td><td>硝基＊喃乙內醯</td><td>NITROFURANTOIN</td><td>1985/09/10</td></tr><tr><td>內衛藥輸字第007400號</td><td>硝基　喃妥因</td><td>NITROFURANTOIN</td><td>1985/12/30</td></tr><tr><td>衛署藥製字第002984號</td><td>離脫淋膠囊</td><td>NITROFURANTOIN</td><td>1999/08/23</td></tr><tr><td>衛署藥製字第003403號</td><td>"優生"硝基呋喃妥因錠</td><td>NITROFURANTOIN</td><td>2019/05/21</td></tr><tr><td>衛署藥製字第006242號</td><td>乃脫菌錠</td><td>NITROFURANTOIN</td><td>1990/09/18</td></tr><tr><td>衛署藥製字第006739號</td><td>你安因錠”三能”　　　　　　　　　　　　　　　　　　　　　　 N</td><td>NITROFURANTOIN</td><td>1989/01/06</td></tr><tr><td>衛署藥製字第009320號</td><td>腹樂錠</td><td>NITROFURANTOIN</td><td>2010/04/28</td></tr><tr><td>衛署藥製字第014798號</td><td>朗高樂膠囊</td><td>NITROFURANTOIN</td><td>1988/12/31</td></tr><tr><td>衛署藥製字第018139號</td><td>硝弗因錠（耐挫敷妥因）</td><td>NITROFURANTOIN</td><td>2014/01/17</td></tr><tr><td>衛署藥製字第019157號</td><td>"正和"炎服妥錠（耐挫敷妥因）</td><td>NITROFURANTOIN</td><td>2023/05/25</td></tr><tr><td>衛署藥製字第021804號</td><td>立邁康膠囊（耐挫敷妥因）</td><td>NITROFURANTOIN</td><td>2003/11/03</td></tr><tr><td>衛署藥製字第028157號</td><td>悠悠寧錠１００公絲（耐挫敷妥因）</td><td>NITROFURANTOIN</td><td>1999/08/30</td></tr><tr><td>衛署藥製字第029859號</td><td>可治淋膠囊</td><td>SULFAMETHOXYPYRIDAZINE、NITROFURANTOIN</td><td>2019/08/21</td></tr><tr><td>衛署藥製字第032301號</td><td>乃脫菌錠１００公絲（耐挫敷隆）</td><td>NITROFURANTOIN</td><td>2010/02/08</td></tr><tr><td>衛署藥輸字第000447號</td><td>硝基吷喃多因</td><td>NITROFURANTOIN</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第000545號</td><td>拂拉爛丁ＭＣ５０公絲膠囊</td><td>NITROFURANTOIN</td><td>1998/03/05</td></tr><tr><td>衛署藥輸字第000546號</td><td>拂拉爛丁ＭＣ１００公絲膠囊</td><td>NITROFURANTOIN</td><td>1998/03/05</td></tr><tr><td>衛署藥輸字第001070號</td><td>硝基/喃妥因</td><td>NITROFURANTOIN</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第002854號</td><td>硝基＊喃妥因</td><td>NITROFURANTOIN</td><td>1993/02/09</td></tr><tr><td>衛署藥輸字第003881號</td><td>硝基＊喃妥因</td><td>NITROFURANTOIN</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第006354號</td><td>尼特富蘭通</td><td>NITROFURANTOIN</td><td>1995/02/13</td></tr><tr><td>衛署藥輸字第007421號</td><td>硝基吷喃妥膠囊５０公絲</td><td>NITROFURANTOIN</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第007422號</td><td>硝基吷喃妥膠囊１００公絲</td><td>NITROFURANTOIN</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第007815號</td><td>優賜福錠</td><td>PHENAZOPYRIDINE HCL、NITROFURANTOIN、SULFADIAZINE</td><td>1990/11/19</td></tr><tr><td>衛署藥輸字第009944號</td><td>漢福林膠囊</td><td>CHLORAMPHENICOL、NITROFURANTOIN、SULFAMETHOXYPYRIDAZINE</td><td>1986/08/15</td></tr><tr><td>衛署藥輸字第010101號</td><td>益菌淨錠１００公絲</td><td>NITROFURANTOIN</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第012157號</td><td>麥克洛丹丁膠囊１００公絲</td><td>NITROFURANTOIN</td><td>1998/03/05</td></tr><tr><td>衛署藥輸字第012158號</td><td>麥克洛丹丁膠囊５０公絲</td><td>NITROFURANTOIN</td><td>1998/03/05</td></tr><tr><td>衛署藥輸字第012490號</td><td>硝基/喃妥因</td><td>NITROFURANTOIN</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第013789號</td><td>硝基喃妥因粉劑</td><td>NITROFURANTOIN</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第014539號</td><td>硝基/喃妥因</td><td>NITROFURANTOIN</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第014682號</td><td>泌克妥能錠</td><td>NITROFURANTOIN</td><td>2000/09/04</td></tr><tr><td>衛署藥輸字第015030號</td><td>梅尿淋錠１００公絲</td><td>NITROFURANTOIN</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第019517號</td><td>硝基/喃妥因</td><td>NITROFURANTOIN</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第021321號</td><td>硝基/喃妥因</td><td>NITROFURANTOIN</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第022271號</td><td>硝基夫喃妥因</td><td>NITROFURANTOIN</td><td>2003/01/27</td></tr><tr><td>衛署藥陸輸字第000147號</td><td>硝基夫南妥因</td><td>NITROFURANTOIN</td><td>2013/12/31</td></tr><tr><td>衛署藥陸輸字第000265號</td><td>硝基(口夫)喃妥因</td><td>Nitrofurantoin</td><td>2016/05/31</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

## 安全性考量

**重要警告：**
- **肺毒性**：急性、亞急性和慢性肺反應，包括肺纖維化
- 長期使用（>6個月）增加肺纖維化風險
- 肝毒性（罕見）
- 神經病變（長期使用）

**RA 患者注意：**
- RA 本身可導致間質性肺疾病
- 合併使用 methotrexate 會增加肺毒性風險
- 不建議 RA 患者長期使用 nitrofurantoin

## 結論與下一步

**決策：Hold**

**理由：**
文獻分析顯示 nitrofurantoin 與類風濕性關節炎的關聯來自：（1）兩者共同導致肺纖維化的副作用/併發症，（2）RA 患者使用 nitrofurantoin 治療尿路感染的病例報告。這是知識圖譜中的偽相關，而非真正的治療關係。此外，nitrofurantoin 的全身分布有限，不適合用於全身性自體免疫疾病。

**若要推進需要：**
- 不建議進一步探索此適應症
- 此預測反映的是共病/不良反應關係，而非治療潛力

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

