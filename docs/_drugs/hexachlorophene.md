---
layout: default
title: Hexachlorophene
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 10
---

# Hexachlorophene
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

# Hexachlorophene：從皮膚抑菌清潔到脂漏性角化症

## 一句話總結

Hexachlorophene（六氯酚）是雙酚類外用抗菌劑，原本用於外科擦拭、皮膚抑菌清潔等外用情境（皮膚黴菌感染屬於與 tolnaftate、undecylenic acid 的複方）。
TxGNN 模型預測它可能對**脂漏性角化症 (Seborrheic Keratosis)** 有效，但目前**沒有任何臨床試驗與文獻**直接支持這個方向，僅有模型預測。

<!-- review:begin hexachlorophene-original-indication-summary-2026-10-16 -->

> **查核更正（2026-10-16）**：原寫「，以及皮膚黴菌感染等外用情境。」。TFDA 許可證資料中，hexachlorophene 現行有效單方許可證只有衛署藥製字第000974號「惠民」柔和潔乳白軟膏，核准外科擦拭用、供皮膚抑菌使用目的之清潔劑；寫皮膚黴菌感染（足癬、股癬等）的是 hexachlorophene 與 tolnaftate 或 undecylenic acid 的複方（如衛署藥製字第041482號「井田」除癬乳膏），抗黴菌作用來自 tolnaftate／undecylenic acid。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end hexachlorophene-original-indication-summary-2026-10-16 -->

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 外科擦拭用、供皮膚抑菌使用目的之清潔劑 |
| 預測新適應症 | 脂漏性角化症 (Seborrheic Keratosis) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 86 張（有效單方 1／有效複方 16／已註銷 69） |
| 建議決策 | Hold |

<!-- review:begin hexachlorophene-original-indication-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「原適應症／濕疹、腫痛、皮膚炎、搔癢與蟲咬」。原寫內容取自 prednisolone＋benzocaine＋hexachlorophene 複方「脫濕美軟膏」（已於 1989-12-29 註銷），不是 hexachlorophene 本身的作用；已改為現行有效單方許可證的適應症。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end hexachlorophene-original-indication-2026-10-03 -->

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般藥理認為，Hexachlorophene 是雙酚類抗菌劑，可破壞細菌細胞膜與膜結合酶，因此可降低皮膚細菌負荷。另有研究指出它可能抑制 SHP2，進而影響 RAS/MEK/ERK 與 PI3K/AKT 訊號路徑，在 KRAS 突變癌細胞中產生抗增生效果，但這只是初步證據，並未與皮膚病變連結。

脂漏性角化症是良性的表皮增生性病變，與抗菌作用沒有已知的關聯。因此，目前沒有明確的機轉理由支持這個預測，TxGNN 分數是唯一的支持依據。

另外，這個藥物在台灣同時有單方與複方許可證，原適應症多為抗菌、清潔與皮膚黴菌感染；新預測的適應症與這些用途差距明顯。

<!-- review:begin hexachlorophene-original-indication-why-2026-10-16 -->

> **查核加註（2026-10-16）**：TFDA 許可證資料中，hexachlorophene 現行有效單方許可證只有衛署藥製字第000974號「惠民」柔和潔乳白軟膏，核准外科擦拭用、供皮膚抑菌使用目的之清潔劑；寫皮膚黴菌感染（足癬、股癬等）的是 hexachlorophene 與 tolnaftate 或 undecylenic acid 的複方（如衛署藥製字第041482號「井田」除癬乳膏），抗黴菌作用來自 tolnaftate／undecylenic acid。原文保留。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end hexachlorophene-original-indication-why-2026-10-16 -->

---

## 臨床試驗證據

目前無與脂漏性角化症相關的臨床試驗登記。

---

## 文獻證據

目前無與脂漏性角化症相關的文獻。

---

## 其他預測適應症的參考

TxGNN 排名前 10 的預測中，下列兩項有部分資料可供參考，但均不足以支持推進：

| 預測適應症 | 證據等級 | 現有證據 |
|-----------|---------|---------|
| 皮膚疾病 (Skin disease) | L4 | 1 個小型試驗 [NCT01049438](https://clinicaltrials.gov/study/NCT01049438)（Phase NA、已完成、31 人）：以鼻用 mupirocin、六氯酚沐浴及全身性抗生素合併預防復發性 MRSA 感染，無法分離出六氯酚本身的效果；另有多篇年代久遠的回顧與新生兒護理研究，其中包含六氯酚毒性的討論 |
| 脂漏性皮膚炎 (Seborrheic dermatitis) | L4 | 僅有 1 篇 1960 年的兒童病例系列 [PMID 13853303](https://pubmed.ncbi.nlm.nih.gov/13853303/)，且嬰兒使用有神經毒性與吸收疑慮 |

其餘預測（外陰倒置性毛囊角化症、網狀色素異常、黏液性苔癬、成人硬腫病等）均為 L5，無實際研究，亦無機轉依據。

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Hexachlorophene 的不重複許可證共 **86 張**：有效單方 1 張、有效複方 16 張、已註銷 69 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第000974號 | "惠民" 柔和潔乳白軟膏（六氯酚） | 軟膏劑 | 惠民製藥股份有限公司 | 2029/10/16 | 外科擦拭用、供皮膚抑菌使用目的之清潔劑 |

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（16 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 內衛藥製字第002746號 | 可麗藥膏 | PREDNISOLONE、HEXACHLOROPHENE、PANTHENOL、ZINC OXIDE、SULFUR | 軟膏劑 | 尋常性痤瘡、尋常性毛瘡 |
| 內衛藥製字第003521號 | 好皮Ｐ．Ｔ．軟膏（外用） | CHLORPHENIRAMINE MALEATE、VITAMIN A、HEXACHLOROPHENE、TOCOPHERO… | 軟膏劑 | 濕疹、藥物疹、過敏性皮膚炎、蕁麻疹、皮膚搔癢症、一般創傷、蟲剌傷、擦傷、痤傷 |
| 內衛藥製字第003537號 | 新痔莫痛藥膏 | HEXACHLOROPHENE、TOCOPHEROL ACETATE ALPHA DL-、BISMUTH SUBNITR… | 軟膏劑 | 內外痔、核痔疼痛、痔出血、肛門裂傷、痔？、肛門搔癢症、脫肛、肛門周圍炎、肛門部手術後之疼痛及其他一般肛門疼痛 |
| 內衛藥製字第006268號 | "健康" 害可消軟膏 | HEXACHLOROPHENE、HYDROCORTISONE、CLEMIZOLE HCL、CLEMIZOLE HCL | 軟膏劑 | 濕疹或皮膚炎． |
| 衛署成製字第008542號 | "井田"腋香外用液 | HEXACHLOROPHENE、ALUMINUM HYDROXYCHLORIDE | 外用液劑 | 止汗，殺菌 |
| 衛署成製字第008658號 | 立夫爽液 | HEXACHLOROPHENE、ALUMINUM HYDROXYCHLORIDE | 外用液劑 | 止汗、殺菌。 |
| 衛署藥製字第008444號 | 安的新藥膏 | UNDECYLENIC ACID、UNDECYLENATE ZINC、PREDNISOLONE、BENZOCAINE (… | 軟膏劑 | 香港腳、頑癬（繡球瘋）頭部白癬、顏面白癬、皮膚搔？症、皮膚黴菌病 |
| 衛署藥製字第022340號 | 脫足癬軟膏 | TOLNAFTATE、HEXACHLOROPHENE | 軟膏劑 | 香港腳、汗？狀白癬、頑癬、斑狀小水？性白癬、足癬、股癬、髮癬、錢癬 |
| 衛署藥製字第023979號 | 止癢懸浮液 | CALAMINE、DIPHENHYDRAMINE、BENZOCAINE (ETHYL AMINOBENZOATE)、ZI… | 外用懸液劑 | 皮膚炎、皮膚搔癢症、皮膚過敏、痱子、濕疹 |
| 衛署藥製字第027999號 | 富癬康乳膏 | HEXACHLOROPHENE、TOLNAFTATE | 乳膏劑 | 汗？狀白癬（香港腳）斑狀小水泡性白癬、頑癬 |
| 衛署藥製字第028612號 | 癬益寧軟膏 | HEXACHLOROPHENE、TOLNAFTATE | 軟膏劑 | 香港腳（足癬）股癬、金錢癬、手癬、禿髮癬、花斑癬、膿？癬、毛囊炎性鬚癬、汗？狀白癬、頑癬、斑狀小水？狀白癬 |
| 衛署藥製字第033290號 | 脫癬軟膏 | HEXACHLOROPHENE、TOLNAFTATE | 軟膏劑 | 治療皮膚表淺性黴菌感染，如：足癬（香港腳）、股癬、汗斑 |
| 衛署藥製字第037071號 | 髮而滋液 | ESTRADIOL BENZOATE、CHLORPHENIRAMINE MALEATE、PANTHENOL D- (EQ… | 外用液劑 | 頭髮保護、頭髮稀疏。 |
| 衛署藥製字第040475號 | 祛癢舒軟膏 | LIDOCAINE、HEXACHLOROPHENE、PREDNISOLONE、CHLORPHENIRAMINE MALE… | 軟膏劑 | 蕁麻疹、濕疹、過敏性皮膚炎。 |
| 衛署藥製字第041206號 | 膚爽得軟膏 | DIPHENHYDRAMINE HCL、HEXACHLOROPHENE、PREDNISOLONE | 軟膏劑 | 濕疹樣症候群（乳兒濕疹、貨幣狀濕疹、脂漏性濕疹、急慢性濕疹、皮膚搔癢症、蕁痲疹）。 |
| 衛署藥製字第041482號 | "井田"除癬乳膏 | HEXACHLOROPHENE、TOLNAFTATE | 乳膏劑 | 治療皮膚表淺性黴菌感染、如足癬（香港腳），股癬，汗斑。 |

<details><summary><strong>已註銷</strong>（69 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛成製字第000292號</td><td>藥用養髮液</td><td>ESTRADIOL BENZOATE、CHLORPHENIRAMINE MALEATE、PYRIDOXINE HCL、2…</td><td>2025/01/09</td></tr><tr><td>內衛成製字第000716號</td><td>“川田”治癢軟膏</td><td>CAMPHOR、BENZOCAINE (ETHYL AMINOBENZOATE)、ZINC OXIDE、MENTHOL、…</td><td>2025/05/15</td></tr><tr><td>內衛成製字第000918號</td><td>泰康藥膏</td><td>ZINC OXIDE、CAMPHOR、DIPHENHYDRAMINE HCL、HEXACHLOROPHENE</td><td>2009/07/22</td></tr><tr><td>內衛成製字第000982號</td><td>癢得寧藥膏</td><td>DIPHENHYDRAMINE HCL、DIBUCAINE HCL、ZINC OXIDE、HEXACHLOROPHENE…</td><td>2009/12/09</td></tr><tr><td>內衛成製字第001091號</td><td>諾德露</td><td>HEXACHLOROPHENE、ALUMINUM HYDROXYCHLORIDE-PROPYLENE GLYCOL CO…</td><td>1990/05/16</td></tr><tr><td>內衛成製字第001093號</td><td>諾德露</td><td>HEXACHLOROPHENE、ALUMINUM HYDROXYCHLORIDE-PROPYLENE GLYCOL CO…</td><td>1989/12/31</td></tr><tr><td>內衛成製字第001201號</td><td>皮寶粉末</td><td>DIETHYLTOLUAMIDE、N-OCTYL BICYCLOHEPTENE DICARBOXYIMIDE、TETRA…</td><td>1988/07/19</td></tr><tr><td>內衛藥製字第000358號</td><td>得撫敏藥膏</td><td>CHLORPHENIRAMINE MALEATE、VITAMIN A PALMITATE、TOCOPHEROL ACET…</td><td>2023/07/24</td></tr><tr><td>內衛藥製字第005724號</td><td>安的新藥膏</td><td>BENZOCAINE (ETHYL AMINOBENZOATE)、UNDECYLENIC ACID、UNDECYLENA…</td><td>2013/10/02</td></tr><tr><td>內衛藥製字第005781號</td><td>康速龍痔根膏</td><td>BENZOCAINE (ETHYL AMINOBENZOATE)、MENTHOL、PREDNISOLONE、HEXACH…</td><td>1990/05/07</td></tr><tr><td>內衛藥製字第005793號</td><td>康速龍軟膏</td><td>HEXACHLOROPHENE、PREDNISOLONE</td><td>1989/11/28</td></tr><tr><td>內衛藥製字第005804號</td><td>康益敏液</td><td>PHENOL (CARBOLIC ACID)、HEXACHLOROPHENE、CALAMINE、MENTHOL、ZINC…</td><td>1990/03/21</td></tr><tr><td>內衛藥製字第005898號</td><td>菲克斯潔膚消毒漿</td><td>HEXACHLOROPHENE</td><td>1998/01/12</td></tr><tr><td>內衛藥製字第006130號</td><td>複方康速龍軟膏</td><td>PREDNISOLONE、TAR、HEXACHLOROPHENE</td><td>2000/08/08</td></tr><tr><td>內衛藥製字第006173號</td><td>美膚健藥膏</td><td>CHLORPHENIRAMINE MALEATE、MENTHOL、CAMPHOR、LIDOCAINE、METHYL SA…</td><td>2015/09/03</td></tr><tr><td>內衛藥製字第007861號</td><td>治傷寧藥膏</td><td>DIPHENHYDRAMINE HCL、LIDOCAINE、SALICYLIC ACID、HEXACHLOROPHENE</td><td>1989/12/31</td></tr><tr><td>內衛藥製字第008452號</td><td>莉那藥膏</td><td>CHLORPHENIRAMINE MALEATE、VITAMIN A、HEXACHLOROPHENE、TOCOPHERO…</td><td>1991/07/08</td></tr><tr><td>內衛藥製字第009203號</td><td>敏能軟膏</td><td>LIDOCAINE、CHLORPHENIRAMINE MALEATE、HEXACHLOROPHENE、PREDNISOL…</td><td>1997/07/26</td></tr><tr><td>內衛藥製字第009478號</td><td>安癬脫軟膏</td><td>UNDECYLENIC ACID、UNDECYLENATE ZINC、HEXACHLOROPHENE</td><td>1990/03/21</td></tr><tr><td>內衛藥製字第011769號</td><td>可利身軟膏</td><td>HEXACHLOROPHENE、CLEMIZOLE、HYDROCORTISONE</td><td>1989/11/29</td></tr><tr><td>內衛藥製字第012461號</td><td>脫濕美軟膏</td><td>PREDNISOLONE、BENZOCAINE (ETHYL AMINOBENZOATE)、HEXACHLOROPHEN…</td><td>1989/12/29</td></tr><tr><td>內衛藥輸字第004247號</td><td>安汗疹軟膏</td><td>DIPHENHYDRAMINE、PHENOL (CARBOLIC ACID)、ZINC OXIDE、L-MENTHOL、…</td><td>1990/08/18</td></tr><tr><td>內衛藥輸字第004720號</td><td>愛貴/藥膏</td><td>BENZOIC ACID、ALLANTOIN、HEXACHLOROPHENE、MALIC ACID、BENZYL SAL…</td><td>1990/12/05</td></tr><tr><td>衛署成製字第007344號</td><td>瑪莉Ｇ－１１藥皂</td><td>TRICLOCARBAN、METHYL SALICYLATE、SOAP、HEXACHLOROPHENE</td><td>2016/06/02</td></tr><tr><td>衛署成製字第008210號</td><td>諾德露洗劑</td><td>HEXACHLOROPHENE、ALUMINUM HYDROXYCHLORIDE-PROPYLENE GLYCOL CO…</td><td>2016/06/23</td></tr><tr><td>衛署成製字第008446號</td><td>〝杏輝〞治汗樂液</td><td>HEXACHLOROPHENE、ALUMINUM HYDROXYCHLORIDE</td><td>2023/07/07</td></tr><tr><td>衛署成製字第009887號</td><td>聖婓蘭外用液</td><td>ALUMINUM CHLOROHYDROXIDE、HEXACHLOROPHENE</td><td>2016/06/15</td></tr><tr><td>衛署成製字第013456號</td><td>"溫士頓" 舒香外用液劑</td><td>HEXACHLOROPHENE、ALUMINUM HYDROXYCHLORIDE</td><td>2012/03/20</td></tr><tr><td>衛署藥製字第003027號</td><td>愛膚康軟膏</td><td>CAMPHOR、HEXACHLOROPHENE、METHYL SALICYLATE、PREDNISOLONE、DIPHE…</td><td>2013/10/02</td></tr><tr><td>衛署藥製字第004470號</td><td>舒維特乳液</td><td>HEXACHLOROPHENE</td><td>2013/10/02</td></tr><tr><td>衛署藥製字第006879號</td><td>養髮液</td><td>HEXACHLOROPHENE、CHLORPHENIRAMINE MALEATE、PREDNISOLONE、PYRIDO…</td><td>1994/04/15</td></tr><tr><td>衛署藥製字第007265號</td><td>苦息樂軟膏</td><td>HEXACHLOROPHENE、LIDOCAINE、CALCITRIOL (DIHYDROXYCHOLECALCIFER…</td><td>2006/11/13</td></tr><tr><td>衛署藥製字第011028號</td><td>命多磺淨軟膏</td><td>HEXACHLOROPHENE、LIDOCAINE、SULFAMETHOMIDINE</td><td>2010/03/18</td></tr><tr><td>衛署藥製字第013510號</td><td>滅癬淨軟膏</td><td>HEXACHLOROPHENE、TOLNAFTATE</td><td>2020/10/05</td></tr><tr><td>衛署藥製字第013522號</td><td>己氯酚乳液</td><td>HEXACHLOROPHENE</td><td>1999/09/30</td></tr><tr><td>衛署藥製字第014001號</td><td>"人生"脫拿癬軟膏</td><td>TOLNAFTATE、HEXACHLOROPHENE</td><td>2026/08/17</td></tr><tr><td>衛署藥製字第015998號</td><td>脫癬軟膏</td><td>TOLNAFTATE、HEXACHLOROPHENE</td><td>1991/04/26</td></tr><tr><td>衛署藥製字第016370號</td><td>安膚除癢軟膏</td><td>TOLNAFTATE、HEXACHLOROPHENE</td><td>2013/10/11</td></tr><tr><td>衛署藥製字第018225號</td><td>通克癬軟膏</td><td>HEXACHLOROPHENE、TOLNAFTATE</td><td>2016/09/08</td></tr><tr><td>衛署藥製字第019473號</td><td>“川田”敏答隆軟膏</td><td>DIPHENHYDRAMINE HCL、HYDROCORTISONE ACETATE、HEXACHLOROPHENE</td><td>2025/05/15</td></tr><tr><td>衛署藥製字第019886號</td><td>安那膚軟膏</td><td>TOLNAFTATE、HEXACHLOROPHENE</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第021371號</td><td>癬益寧軟膏</td><td>HEXACHLOROPHENE、TOLNAFTATE</td><td>1989/11/28</td></tr><tr><td>衛署藥製字第021739號</td><td>克異香</td><td>HEXACHLOROPHENE、ALUMINUM HYDROXYCHLORIDE</td><td>2013/10/03</td></tr><tr><td>衛署藥製字第023989號</td><td>癢得治軟膏</td><td>PREDNISOLONE、HEXACHLOROPHENE、MENTHOL、CAMPHOR、DIPHENHYDRAMINE…</td><td>2010/03/18</td></tr><tr><td>衛署藥製字第024650號</td><td>菲蘇海克乳劑</td><td>ENTSUFON SODIUM、HEXACHLOROPHENE</td><td>1988/12/31</td></tr><tr><td>衛署藥製字第024752號</td><td>"美西"脫癬軟膏</td><td>HEXACHLOROPHENE、TOLNAFTATE</td><td>2023/07/24</td></tr><tr><td>衛署藥製字第027533號</td><td>可膚淨乳劑</td><td>HEXACHLOROPHENE</td><td>2013/10/03</td></tr><tr><td>衛署藥製字第028088號</td><td>沐亦康液</td><td>POTASSIUM SOAP (SOFT SOAP)、HEXACHLOROPHENE</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第028261號</td><td>菲蘇海克乳劑</td><td>HEXACHLOROPHENE、ENTSUFON SODIUM</td><td>2010/03/05</td></tr><tr><td>衛署藥製字第029553號</td><td>樟芝高軟膏</td><td>HEXACHLOROPHENE、HYDROCORTISONE ACETATE、DIPHENHYDRAMINE HCL</td><td>2011/02/22</td></tr><tr><td>衛署藥製字第031674號</td><td>安癬脫乳霜</td><td>HEXACHLOROPHENE、UNDECYLENATE ZINC、UNDECYLENIC ACID</td><td>2013/09/23</td></tr><tr><td>衛署藥製字第031678號</td><td>康益敏液</td><td>ZINC OXIDE、MENTHOL、PHENOL (CARBOLIC ACID)、HEXACHLOROPHENE、CA…</td><td>2013/09/23</td></tr><tr><td>衛署藥製字第031772號</td><td>複方康速龍軟膏</td><td>PREDNISOLONE、HEXACHLOROPHENE</td><td>2013/09/23</td></tr><tr><td>衛署藥製字第031926號</td><td>康速龍痔根膏</td><td>ZINC OXIDE、BENZOCAINE (ETHYL AMINOBENZOATE)、HEXACHLOROPHENE、…</td><td>2017/02/06</td></tr><tr><td>衛署藥製字第033520號</td><td>"杏輝"莉那藥膏</td><td>VITAMIN A、CHLORPHENIRAMINE MALEATE、TOCOPHEROL ACETATE ALPHA…</td><td>2023/07/07</td></tr><tr><td>衛署藥製字第043047號</td><td>沐亦康液</td><td>HEXACHLOROPHENE、TRICLOCARBAN</td><td>2023/07/07</td></tr><tr><td>衛署藥輸字第001026號</td><td>六氯酚</td><td>HEXACHLOROPHENE</td><td>1991/04/03</td></tr><tr><td>衛署藥輸字第004516號</td><td>百特靈噴霧劑</td><td>HEXACHLOROPHENE、BENZOCAINE (ETHYL AMINOBENZOATE)、UNDECYLENIC…</td><td>1986/06/20</td></tr><tr><td>衛署藥輸字第004617號</td><td>己氯酚</td><td>HEXACHLOROPHENE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第005390號</td><td>汗士求美液</td><td>HEXACHLOROPHENE</td><td>1999/09/28</td></tr><tr><td>衛署藥輸字第007507號</td><td>體舒隆殺菌消毒液（外用）</td><td>HEXACHLOROPHENE</td><td>1986/06/02</td></tr><tr><td>衛署藥輸字第007808號</td><td>利痔良軟膏</td><td>BENZOCAINE (ETHYL AMINOBENZOATE)、HEXACHLOROPHENE、HYDROCORTIS…</td><td>1992/07/01</td></tr><tr><td>衛署藥輸字第008312號</td><td>登得潔乳膏</td><td>CHLOROCRESOL (4-CHLORO-M-CRESOL)、HEXACHLOROPHENE</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第008319號</td><td>姍拉娜糊劑</td><td>VEEGUM、SULFUR COLLOIDAL、HEXACHLOROPHENE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第009516號</td><td>百樂軟膏</td><td>FORMALDEHYDE SOLUTION (FORMALIN)、UNDECYLENATE MONOETHANOLAMI…</td><td>2000/09/05</td></tr><tr><td>衛署藥輸字第010676號</td><td>為痔好栓劑</td><td>HEXACHLOROPHENE、O-(BETA-HYDROXY O-(BETA-HYDRXYETHYL)ETHYL)-R…</td><td>1991/04/22</td></tr><tr><td>衛署藥輸字第010687號</td><td>己氯酚</td><td>HEXACHLOROPHENE</td><td>1999/09/28</td></tr><tr><td>衛署藥輸字第011313號</td><td>為痔好軟膏</td><td>PREDNISOLONE TRIMETHYLACETATE、HEXACHLOROPHENE、TROXERUTIN</td><td>1991/04/22</td></tr><tr><td>衛署藥輸字第012151號</td><td>必克爛軟膏</td><td>TIOXOLONE、HEXACHLOROPHENE、HYDROCORTISONE ACETATE</td><td>1988/09/02</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：燒傷 (burn)（來自 TxGNN 知識圖譜的藥物－疾病禁忌關聯，並非仿單內容）
- **藥物交互作用**：資料庫僅記錄 1 筆藥理學層面的交互作用，標靶為 N-醯基磷脂醯乙醇胺磷脂酶 D (NAPEPLD)，無臨床嚴重度分級。
- **文獻提及的風險**：多篇文獻指出六氯酚用於早產兒或新生兒全身沐浴時，可能造成中樞神經系統空泡化，而外用藥物也可能經皮吸收，因此嬰幼兒使用須特別謹慎。美國 FDA 已終止其核准用途。

<!-- review:begin hexachlorophene-fda-discontinued-tw-2026-10-03 -->

> **查核加註（2026-10-03）**：Drugs@FDA 裡 hexachlorophene 外用品多數已標示停售（Discontinued），但 NDA 017433 的 PRE-OP／PRE-OP II 外用海綿仍登載為處方藥（Prescription），並非全面停用。原文保留。依據：[Drugs@FDA：NDA 017433（PRE-OP／PRE-OP II，hexachlorophene 480MG sponge;topical）](https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=017433)；[openFDA Drugs@FDA API：主成分 HEXACHLOROPHENE 的申請案（查詢 products.active_ingredients.name:"HEXACHLOROPHENE"）](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22HEXACHLOROPHENE%22&limit=100)。

<!-- review:end hexachlorophene-fda-discontinued-tw-2026-10-03 -->

其餘警語與禁忌資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 脂漏性角化症的預測沒有任何臨床試驗或文獻支持，且機轉上找不到合理關聯，只有 TxGNN 分數 (L5)。
- 六氯酚有已知的經皮吸收與神經毒性疑慮，風險效益比不利於推進新用途。

**若要推進需要：**
- 補齊作用機轉資料，並釐清 SHP2 抑制等機轉是否與良性角化性病變有關
- 進行前臨床研究（如細胞或皮膚模型），驗證對角化細胞增生的作用
- 若研究顯示有效，需評估局部用藥的經皮吸收與長期安全性
- 若要轉向證據稍多的方向，可優先考慮縮小「皮膚疾病」範圍，例如細菌性皮膚感染或去菌落化，並重新評估風險效益

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 原適應症取自已註銷的類固醇複方 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表含複方且多數已註銷 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | FDA 核准外用品「已全面停用」 | 報告重生後已無此錯誤（2026-10-15：預測理由段已無此說；新報告改在「安全性考量」寫「美國 FDA 已終止其核准用途」，由 hexachlorophene-fda-discontinued-tw 紀錄處理；原為加註） | [Drugs@FDA：NDA 017433（PRE-OP／PRE-OP II，hexachlorophene 480MG sponge;topical）](https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=017433)；[openFDA Drugs@FDA API：主成分 HEXACHLOROPHENE 的申請案（查詢 products.active_ingredients.name:"HEXACHLOROPHENE"）](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22HEXACHLOROPHENE%22&limit=100) |
| 2026-10-03 | 安全性段稱美國 FDA 已終止核准用途 | 加註（2026-10-16 修訂，前版保留於紀錄） | [Drugs@FDA：NDA 017433（PRE-OP／PRE-OP II，hexachlorophene 480MG sponge;topical）](https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=017433)；[openFDA Drugs@FDA API：主成分 HEXACHLOROPHENE 的申請案（查詢 products.active_ingredients.name:"HEXACHLOROPHENE"）](https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22HEXACHLOROPHENE%22&limit=100) |
| 2026-10-16 | 一句話總結把皮膚黴菌感染列為原用途 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-16 | 預測理由稱原適應症含皮膚黴菌感染 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案日期 2026-09-29；2026-10-16 逐號程式核對）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

