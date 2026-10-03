---
layout: default
title: Hexachlorophene
parent: 中證據等級 (L3-L4)
nav_order: 121
evidence_level: L3
indication_count: 10
---

# Hexachlorophene
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Hexachlorophene：從皮膚抑菌消毒到廣義皮膚病 (Skin Disease)

## 一句話總結

Hexachlorophene（六氯酚）是歷史悠久的外用廣效抗菌劑，台灣核准用於皮膚消毒殺菌、外科擦拭、以及濕疹與皮膚炎等皮膚症狀。TxGNN 模型在 10 個預測適應症中，以**廣義皮膚病 (Skin Disease)** 的臨床證據最為充分，目前有 **2 個臨床試驗**和 **20 篇文獻**支持這個方向，建議在嚴格安全條件下推進評估。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 外科擦拭用、供皮膚抑菌使用目的之清潔劑 |
| 預測新適應症 | 廣義皮膚病 (Skin Disease) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 86 張（有效單方 1／有效複方 16／已註銷 69） |
| 建議決策 | Proceed with Guardrails |

<!-- review:begin hexachlorophene-original-indication-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「原適應症／濕疹、腫痛、皮膚炎、搔癢與蟲咬」。原寫內容取自 prednisolone＋benzocaine＋hexachlorophene 複方「脫濕美軟膏」（已於 1989-12-29 註銷），不是 hexachlorophene 本身的作用；已改為現行有效單方許可證的適應症。依據：[衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)。

<!-- review:end hexachlorophene-original-indication-2026-10-03 -->

---

## 為什麼這個預測合理？

目前缺乏正式記錄的作用機轉資料（MOA 資料缺口）。根據現有資訊，Hexachlorophene 是一種有機氯類外用抗菌劑，歷史應用中以**干擾革蘭氏陽性菌細胞膜通透性、抑制膜結合酶系統**為主要殺菌途徑，對金黃色葡萄球菌（包括 MRSA）和鏈球菌具有強效活性。此外，Guide to PHARMACOLOGY 資料庫顯示，Hexachlorophene 可能抑制 N-Acylphosphatidylethanolamine-phospholipase D（NAPEPLD），並有初步文獻提示可透過 SHP2 抑制路徑干擾 RAS/MEK/ERK 及 PI3K/AKT 訊號（PMID: 32284327），後者屬藥理學靶點資料，臨床意義尚待釐清。

原核准用途（皮膚消毒、外科擦拭、嬰兒室葡萄球菌去定植）與「廣義皮膚病」的關聯性相當直接——臨床試驗 NCT01049438 直接以 Hexachlorophene 全身洗浴作為 MRSA 皮膚去定植的核心干預，明確支持其對細菌性皮膚感染的管理能力。多項文獻亦顯示，停用 Hexachlorophene 沐浴後新生兒葡萄球菌皮膚感染率顯著上升，反向驗證了其皮膚防護效果。

然而需特別留意：Hexachlorophene 在 FDA 的核准外用用途**已全面停用**，主要原因是早產兒皮膚吸收所致的中樞神經系統空泡化病變。任何新適應症的推進，都必須嚴格界定安全的目標族群，並排除神經毒性高風險族群（早產兒、新生兒）。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01049438](https://clinicaltrials.gov/study/NCT01049438) | N/A | 完成 | 31 | 前瞻性試驗：鼻腔 Mupirocin＋Hexachlorophene 全身洗浴＋全身性抗生素三聯療法，驗證對社區型 MRSA 復發性皮膚感染去定植的效果 |
| [NCT00532324](https://clinicaltrials.gov/study/NCT00532324) | N/A | 完成 | 107 | 前瞻性世代研究：評估孕婦金黃色葡萄球菌（含 CA-MRSA）的臨床與分子流行病學，提供皮膚病原菌背景資料 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [958762](https://pubmed.ncbi.nlm.nih.gov/958762/) | 1976 | 世代研究 | Pediatrics | 五期序列研究：3% Hexachlorophene 全身沐浴期間金黃色葡萄球菌定植率最低；停用後定植率升至 80%、感染率 9.5% |
| [1143981](https://pubmed.ncbi.nlm.nih.gov/1143981/) | 1975 | 世代研究 | Pediatrics | 停用 Hexachlorophene 後嬰兒室爆發鏈球菌／葡萄球菌皮膚感染；嚴格無菌技術比恢復使用 Hexachlorophene 更具長期控制效果 |
| [958085](https://pubmed.ncbi.nlm.nih.gov/958085/) | 1976 | 世代研究 | Med J Australia | 81,756 例出生分析：早產兒使用 3% Hexachlorophene 乳劑洗浴可發生中樞神經系統空泡化病變；足月兒長期追蹤未見神經後遺症 |
| [4834430](https://pubmed.ncbi.nlm.nih.gov/4834430/) | 1974 | 對照研究 | Can Med Assoc J | 158 對 156 例新生兒比較：Hexachlorophene vs Lactacyd 洗浴對鼻腔及臍帶金黃色葡萄球菌定植率的差異 |
| [25017526](https://pubmed.ncbi.nlm.nih.gov/25017526/) | 2014 | 其他 | J Allergy Clin Immunol Pract | 異位性皮膚炎合併反覆 MRSA 皮膚感染管理回顧，涵蓋 S. aureus 去定植治療策略（含 Hexachlorophene 洗浴） |
| [6643773](https://pubmed.ncbi.nlm.nih.gov/6643773/) | 1983 | 回顧 | J Am Acad Dermatol | 手術抗菌劑回顧：比較 Hexachlorophene、Chlorhexidine、Benzalkonium chloride 及 Povidone-iodine 的皮膚消毒效果 |
| [12418624](https://pubmed.ncbi.nlm.nih.gov/12418624/) | 2002 | 回顧 | MMWR | CDC/HICPAC 醫療場所手部衛生指引；含 Hexachlorophene 手術抗菌應用的歷史評估與現行建議 |
| [15060207](https://pubmed.ncbi.nlm.nih.gov/15060207/) | 2004 | 回顧 | Pediatrics | 兒童皮膚屏障與環境暴露回顧；涵蓋 Hexachlorophene 新生兒皮膚護理的毒性疑慮及監管歷史 |
| [123433](https://pubmed.ncbi.nlm.nih.gov/123433/) | 1975 | 病例系列 | Arch Dermatol | 皂類粉刺原性評估：含 Hexachlorophene 的殺菌皂具輕度粉刺原性，可能加重痤瘡患者皮膚狀況 |
| [2235790](https://pubmed.ncbi.nlm.nih.gov/2235790/) | 1990 | 其他 | Postgrad Med | 陰囊搔癢症鑑別診斷與治療，涵蓋外用抑菌劑在皮膚炎症及感染症狀管理中的應用場景 |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Hexachlorophene 的不重複許可證共 **86 張**：有效單方 1 張、有效複方 16 張、已註銷 69 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第000974號 | "惠民" 柔和潔乳白軟膏（六氯酚） | 軟膏劑 | 惠民製藥股份有限公司 | 2029/10/16 | 外科擦拭用、供皮膚抑菌使用目的之清潔劑 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（16 張）

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

---

## 安全性考量

**藥物-靶點交互作用：**
根據 Guide to PHARMACOLOGY 資料庫，Hexachlorophene 可抑制人類 N-Acylphosphatidylethanolamine-phospholipase D（NAPEPLD，Ensembl: ENSG00000161048），並有初步文獻（PMID: 32284327）提示可能透過 SHP2 抑制途徑，干擾 RAS/MEK/ERK 及 PI3K/AKT 訊號路徑，在 KRAS 突變癌細胞中產生抗增殖效果。此為藥理學靶點資料，臨床藥物交互作用意義尚待進一步評估。

**重要安全背景：**
FDA 核准的 Hexachlorophene 外用品已全面停用（discontinued）。主要安全疑慮為**新生兒（尤其早產兒）透過皮膚吸收導致中樞神經系統空泡化病變**（見 PMID: 958085），黃疸為早產兒的加重因子。台灣現有 86 張許可證（有效 17 張）均為外用劑型，應嚴格遵守核准適應症及濃度限制，不得用於新生兒全身性洗浴。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Hexachlorophene 在細菌性皮膚感染（尤其 MRSA 皮膚去定植）方面有歷史應用紀錄及前瞻性臨床試驗直接支持，機轉基礎明確；惟 FDA 已停用其核准用途，已知神經毒性安全疑慮（特別針對早產兒／新生兒族群）構成顯著限制，須在嚴格安全監控框架下方可推進。

**若要推進需要：**
- 補充完整的作用機轉資料（DrugBank MOA 查詢 DB00756）
- 明確界定安全的目標族群（成人為主，排除早產兒、新生兒），建立神經毒性監測計畫
- 聚焦具明確機轉依據的皮膚病亞型（如 MRSA 相關復發性皮膚感染、外科部位皮膚去定植），避免機轉不明的廣義適應症申請
- 進行台灣法規可行性評估：在 FDA 已停用背景下，現有台灣許可證的延伸使用路徑及監管策略
- 確認現有製劑濃度、劑型是否符合擬議新適應症的藥學需求

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 原適應症取自已註銷的類固醇複方 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 許可證表含複方且多數已註銷 | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

