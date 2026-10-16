---
layout: default
title: Nystatin
parent: 中證據等級 (L3-L4)
nav_order: 198
evidence_level: L3
indication_count: 10
---

# Nystatin
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

# Nystatin：從念珠菌感染到外陰陰道炎 (Vulvovaginitis)

## 一句話總結

Nystatin（耐絲菌素）是一種多烯類抗黴菌藥物，原本用於念珠菌引起的口腔、腸道、皮膚及陰道感染。
TxGNN 模型預測它可能對**外陰陰道炎 (Vulvovaginitis)** 有效，
目前**無臨床試驗登記**，但有 **20 篇文獻**支持這個方向（多為綜述）。
需注意：念珠菌性陰道炎本來就是已核准的適應症，因此這並非真正的「新」適應症。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抗生素（單方有效許可證中第一個非空的核准適應症文字；其他單方許可證另載有念珠菌引起之口腔、皮膚、腸道及陰道感染） |
| 預測新適應症 | 外陰陰道炎 (Vulvovaginitis) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 126 張（有效單方 11／有效複方 28／已註銷 87） |
| 建議決策 | Proceed with Guardrails |

<!-- review:begin nystatin-moa-2026-10-03 -->

## Nystatin 的作用機轉

<!-- moa-sourced: 2026-10-03 用戶拍板例外，只限附來源的作用機轉段 -->

以下只說明這個藥原本怎麼作用，每一點都摘自官方仿單的藥理段落並附連結；與本頁的老藥新用預測無關，也不構成用藥建議。

- Nystatin 是抗真菌藥，會與易感念珠菌（Candida）細胞膜上的固醇結合，改變細胞膜的通透性，讓細胞內的成分漏出。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=28b4e26e-206a-4e8a-abfe-774b780e91c3)）
- 體外試驗中，它對多種酵母菌與類酵母菌同時有抑制生長與殺菌的作用。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=28b4e26e-206a-4e8a-abfe-774b780e91c3)）
- 口服時腸胃道幾乎不吸收，大部分以原形隨糞便排出。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=28b4e26e-206a-4e8a-abfe-774b780e91c3)）

**來源**：[DailyMed：Nystatin Oral Suspension USP 仿單（PAI Pharma），Clinical Pharmacology／Microbiology 段](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=28b4e26e-206a-4e8a-abfe-774b780e91c3)，版本日期 2026-07-21；查閱日期 2026-10-03。

---

<!-- review:end nystatin-moa-2026-10-03 -->

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫中未收錄）。依一般藥理知識，Nystatin 會結合念珠菌細胞膜上的麥角固醇 (ergosterol)，形成孔洞造成細胞內容物滲漏而致菌體死亡。

外陰陰道炎中最常見的病因即為念珠菌感染，白色念珠菌約占 85–90%。Nystatin 的作用標的正是這類致病菌，因此機轉上高度吻合。

台灣已有多張陰道錠、陰道用製劑核准用於陰道念珠菌感染，所以這個預測更接近「既有適應症的確認」，而非跨疾病的藥物再利用。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

以下為與外陰陰道炎及相關外陰炎最相關的文獻（資料中多為綜述，未見 RCT）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7282789](https://pubmed.ncbi.nlm.nih.gov/7282789/) | 1981 | 雙盲比較（分類為 Cohort） | Am J Obstet Gynecol | 硼酸粉對比 Nystatin 陰道膠囊：硼酸治癒率 92%（7–10 天）、72%（30 天）；Nystatin 為 64% 與 50% |
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Review | Pharmaceutics | 回顧抗氟康唑外陰陰道念珠菌症的替代療法，包括硼酸、Nystatin 與新藥 |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Womens Health | 復發性外陰陰道念珠菌症的硼酸臨床證據，非白色念珠菌對唑類較不敏感 |
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Review | BMJ Clin Evid | 外陰陰道念珠菌症為陰道炎第二常見原因，白色念珠菌占 85–90% |
| [1436934](https://pubmed.ncbi.nlm.nih.gov/1436934/) | 1992 | Review | Obstet Gynecol Clin North Am | Nystatin 1950 年代起用於陰道念珠菌症，後來首選已被咪唑類與三唑類取代 |
| [18729533](https://pubmed.ncbi.nlm.nih.gov/18729533/) | 2008 | 文獻回顧 | Drugs | 局部治療與口服治療對單純性感染療效相當，局部治療有其獨特優勢 |
| [10796183](https://pubmed.ncbi.nlm.nih.gov/10796183/) | 2000 | 系統性回顧 (Cochrane) | Cochrane Database Syst Rev | 孕期陰道念珠菌症的局部治療 |
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | 臨床研究 | Mycoses | 針對 287 株複雜型外陰陰道念珠菌症分離株，比較氟康唑與 Nystatin 的體外敏感性與臨床結果 |
| [16047929](https://pubmed.ncbi.nlm.nih.gov/16047929/) | 2005 | 臨床研究 | Ceska Gynekol | 評估 Nystatin 與 nifuratel 複方陰道製劑治療混合型外陰陰道感染 |
| [25711406](https://pubmed.ncbi.nlm.nih.gov/25711406/) | 2015 | 臨床指引 | Mycoses | 德語系外陰陰道念珠菌症診療指引（S2k） |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Nystatin 的不重複許可證共 **126 張**：有效單方 11 張、有效複方 28 張、已註銷 87 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（11 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第014596號 | "永信"寧司泰定陰道錠 | 陰道錠 | 永信藥品工業股份有限公司 | 2030/04/03 | 念珠菌所引起之陰道感染症 |
| 衛署藥製字第018895號 | "永信"寧司泰定膠囊 | 膠囊劑 | 永信藥品工業股份有限公司 | 2029/09/26 | 腸道念珠菌感染症之預防與治療、當廣效性抗生素或類固醇療法時併用為念珠菌過度增殖之預防療法。 |
| 衛署藥製字第025025號 | "元宙" 妮泰錠 50 萬單位（耐絲菌素） | 錠劑 | 元宙化學製藥股份有限公司 | 2029/05/25 | 白色念珠菌引起之感染症 |
| 衛署藥製字第026035號 | 耐斯特淨膠囊５００，０００國際單位（耐斯菌素） | 膠囊劑 | 中美兄弟製藥股份有限公司 | 2028/05/25 | 腸道念珠菌感染症 |
| 衛署藥製字第027557號 | "生達" 速淨陰道錠１０萬單位（耐絲菌素） | 外用錠劑 | 生達化學製藥股份有限公司 | 2030/02/10 | 陰道念珠菌感染症 |
| 衛署藥製字第034585號 | "衛達"妳達新陰道栓劑 | 栓劑 | 衛達化學製藥股份有限公司 | 2026/11/19 | 念珠菌感染引起之陰道炎。 |
| 衛署藥製字第034904號 | 滅菌靈懸液用粉劑１０萬單位/毫升（耐絲菌素） | 懸液用粉劑 | 健亞生物科技股份有限公司 | 2029/09/21 | 預防和治療由白色念珠菌所引起之口腔、皮膚及腸內諸感染 |
| 衛署藥製字第040573號 | "井田"尼斯菌膠囊５０萬單位（耐絲菌素） | 膠囊劑 | 井田國際醫藥廠股份有限公司 | 2031/11/15 | 腸道念珠菌感染症。 |
| 衛署藥製字第057924號 | 婦可安陰道錠10萬單位(耐絲菌素) | 陰道錠 | 井田國際醫藥廠股份有限公司 | 2028/05/09 | 陰道念珠菌感染症。 |
| 衛署藥輸字第021661號 | 耐絲菌素 | （粉） | 東信化學藥品有限公司 | 2027/04/22 | 對念珠菌具有感受性之細菌感染症。 |
| 衛部藥輸字第027982號 | 耐絲菌素 | 粉劑 | 仁友興業股份有限公司 | 2030/10/27 | 抗生素 |

**有效・複方（截至資料集日期 2026-09-29；適應症屬整個複方，不是本藥單獨的適應症）**（28 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第018023號 | "優良"優膚力霜劑 | NYSTATIN、TRIAMCINOLONE ACETONIDE | 乳膏劑 | 過敏性、發炎性與念珠菌黴菌及酵母菌之皮膚感染 |
| 衛署藥製字第018053號 | 膚可爽霜膏 | NYSTATIN、NEOMYCIN SULFATE、GRAMICIDIN、TRIAMCINOLONE ACETONIDE | 乳膏劑 | 濕疹、外耳炎、皮膚搔癢症、神經性皮膚炎、牛皮癬、頑癬、香港腳、外傷、火傷、化膿性皮膚病。 |
| 衛署藥製字第020102號 | "人人"三用親水性軟膏 | TRIAMCINOLONE ACETONIDE、TRIAMCINOLONE ACETONIDE、TRIAMCINOLON… | 乳膏劑 | 濕疹(異位性、接觸性、脂漏性、毛囊性、彎曲處、創傷後感染性、錢幣形、壅滯性及嬰兒濕疹)、外陰搔癢、神經性皮炎、外耳炎、肛門搔癢及牛皮癬 |
| 衛署藥製字第021924號 | "杏輝"美康乳膏 | GRAMICIDIN、GRAMICIDIN、NEOMYCIN (SULFATE)、NEOMYCIN (SULFATE)、… | 乳膏劑 | 濕疹、過敏性和發炎性皮膚病、續發性細菌或黴菌感染（念珠菌感染） |
| 衛署藥製字第022078號 | "人人"制黴乳膏 | NYSTATIN、TOLNAFTATE | 乳膏劑 | 治療皮膚表淺性黴菌感染，如足癬（香港腳）、體癬、股癬、汗斑。 |
| 衛署藥製字第022867號 | "杏輝"美康耳用滴劑 | NYSTATIN、NEOMYCIN (SULFATE)、GRAMICIDIN、TRIAMCINOLONE ACETONI… | 滴劑 | 外耳道念珠菌感染、表面細菌感染、異位性皮膚炎、濕疹性皮膚炎、過敏接觸性皮膚炎、原發刺激性接觸皮膚炎、皮脂溢出性皮膚炎、溢出性皮膚炎、神經性皮膚炎 |
| 衛署藥製字第023133號 | 康可麗乳膏 | NEOMYCIN (SULFATE)、GRAMICIDIN、GRAMICIDIN、NEOMYCIN (SULFATE)、… | 乳膏劑 | 濕疹、過敏性和發炎性皮膚病、細菌、黴菌之感染症 |
| 衛署藥製字第031063號 | 康淨膚軟膏 | NEOMYCIN (SULFATE)、GRAMICIDIN、NYSTATIN、TRIAMCINOLONE ACETONI… | 乳膏劑 | 溼疹(異位性、接觸性、濕脂性、毛囊性、彎曲性、創傷後感染性、錢幣形、壅滯性及嬰兒性濕疹)、外陰搔癢、神經性皮炎、外耳炎、肛門搔癢及牛皮癬。 |
| 衛署藥製字第033074號 | "大豐"抗黴康免乳膏 | TRIAMCINOLONE ACETONIDE、NYSTATIN、NEOMYCIN (SULFATE)、GRAMICID… | 乳膏劑 | 細菌或念珠菌感染引起之各類濕疹症狀，癬症或皮膚炎 |
| 衛署藥製字第033381號 | 卡耐乳膏 | TRIAMCINOLONE ACETONIDE、NYSTATIN、NEOMYCIN (SULFATE)、GRAMICID… | 乳膏劑 | 濕疹（異位性、接觸性、脂漏性、毛囊性、彎曲處、創傷後感染性錢幣形、壅滯性及嬰兒濕疹），外陰瘙癢，神經性皮炎、外耳炎、肛門瘙癢及牛皮癬。 |
| 衛署藥製字第033943號 | "井田"真好乳膏 | NEOMYCIN (SULFATE)、NEOMYCIN (SULFATE)、GRAMICIDIN、GRAMICIDIN、… | 乳膏劑 | 濕疹（異位性、接觸性、脂漏性、毛囊性、彎曲處、創傷後感染性、錢幣形、壅滯性及嬰兒濕疹），外陰搔癢、神經性皮炎、外耳炎、肛門搔癢及牛皮癬。 |
| 衛署藥製字第035788號 | 納新淨乳膏 | TRIAMCINOLONE (ACETONIDE)、TRIAMCINOLONE (ACETONIDE)、NYSTATIN… | 乳膏劑 | 淺表性細菌感染、淺性念珠菌及（或）細菌感染、或併發之皮膚炎（如異位性、濕疹樣、錢幣形、接觸性、滲出性、皮脂溢出性、濕疹、神經性皮膚炎）、外耳炎、創傷後感染性濕疹、牛皮癬、靜脈瘤濕疹… |
| 衛署藥製字第038712號 | 妥膚定乳膏 | TRIAMCINOLONE ACETONIDE、GRAMICIDIN、NYSTATIN、NEOMYCIN SULFATE | 乳膏劑 | 濕疹、（異位性、接觸性、脂漏性、毛囊性、彎曲處、創傷後感染性錢幣形、壅滯性及嬰兒濕疹）、外陰瘙癢、神經性皮炎、外耳炎、肛門瘙癢及牛皮癬 |
| 衛署藥製字第041437號 | "生達"雅膚乳膏 | GRAMICIDIN、NEOMYCIN (SULFATE)、NYSTATIN、TRIAMCINOLONE ACETONI… | 乳膏劑 | 異位性濕疹、錢幣形濕疹、外耳炎、接觸性濕疹、創傷後感染性濕疹、肛門搔癢、毛囊性濕疹、漏脂性濕疹、牛皮癬、外陰搔癢、神經性皮炎、彎曲處濕疹、壅滯性濕疹。 |
| 衛署藥製字第043981號 | 欣膚淨乳膏 | NYSTATIN、NYSTATIN、TRIAMCINOLONE ACETONIDE、TRIAMCINOLONE ACET… | 乳膏劑 | 濕疹、（異位性、接觸性、脂漏性、毛囊性、彎曲處、創傷後感染性錢幣形、壅滯性及嬰兒濕疹）、外陰瘙癢、神經性皮炎、外耳炎、肛門瘙癢及牛皮癬。 |
| 衛署藥製字第043983號 | 吉時乳膏〝溫士頓〞 | NYSTATIN、TRIAMCINOLONE ACETONIDE、GRAMICIDIN、NEOMYCIN (SULFAT… | 乳膏劑 | 濕疹（異位性、接觸性、脂漏性、毛囊性、彎曲處、創傷後感染性、錢幣形、壅滯性及嬰兒濕疹）、外陰搔癢、神經性皮炎、外耳炎、肛門搔癢及牛皮癬。 |
| 衛署藥製字第044089號 | 福聯乳膏 | NEOMYCIN SULFATE、NYSTATIN、GRAMICIDIN、TRIAMCINOLONE ACETONIDE | 乳膏劑 | 濕疹（異位性、接觸性、脂漏性、毛囊性、彎曲處、創傷後感染性錢幣形、壅滯性及嬰兒濕疹）、外陰瘙癢、神經性皮炎、外耳炎、肛門瘙癢及牛皮癬 |
| 衛署藥製字第045228號 | "明德" 敏治菌 乳膏 | NYSTATIN、NYSTATIN、NYSTATIN、TRIAMCINOLONE ACETONIDE、TRIAMCINO… | 乳膏劑 | 濕疹、外耳炎、皮膚搔癢症、神經性皮膚炎、牛皮癬、頑癬、香港腳、外傷、化膿性皮膚病。 |
| 衛署藥製字第045851號 | 益四聯乳膏 | TRIAMCINOLONE ACETONIDE、TRIAMCINOLONE ACETONIDE、TRIAMCINOLON… | 乳膏劑 | 溼疹(異位性、接觸性、脂漏性、毛囊性、彎曲性、創傷後感染性、錢幣形、壅滯性及嬰兒濕疹)、外陰搔癢、神經性皮炎、外耳炎、肛門搔癢及牛皮癬。 |
| 衛署藥製字第046485號 | "黃氏" 膚炎寧乳膏 | HALCINONIDE MICRO、NEOMYCIN SULFATE、NYSTATIN | 乳膏劑 | 異位性濕疹、濕疹樣濕疹、壅滯性濕疹、接觸性濕疹、脂漏性濕疹、錢幣形濕疹、嬰兒濕疹、神經性皮炎、牛皮癬。 |
| 衛署藥製字第049418號 | 保康美乳膏 | TRIAMCINOLONE ACETONIDE、GRAMICIDIN、NEOMYCIN (SULFATE)、NYSTAT… | 乳膏劑 | 濕疹：(異位性、接觸性、脂漏性、毛囊性、彎曲處、創傷後感染、錢幣型、壅滯性及嬰兒濕疹)、外陰搔癢、神經性皮膚炎、外耳炎、肛門搔癢及牛皮癬。 |
| 衛署藥製字第050141號 | 四寧乳膏 | TRIAMCINOLONE ACETONIDE、NYSTATIN、GRAMICIDIN、NEOMYCIN (SULFAT… | 乳膏劑 | 異位性濕疹、錢幣形濕疹、外耳炎、接觸性濕疹、創傷後感染性濕疹、肛門搔癢、毛囊性濕疹、漏脂性濕疹、牛皮癬、外陰搔癢、神經性皮炎、彎曲處濕疹、壅滯性濕疹。 |
| 衛署藥製字第057113號 | "仙台"康適研乳膏 | GRAMICIDIN、NEOMYCIN SULFATE、TRIAMCINOLONE ACETONIDE、NYSTATIN | 乳膏劑 | 異位性濕疹、錢幣形濕疹、外耳炎、接觸性濕疹、創傷後感染性濕疹、肛門搔癢、毛囊性濕疹、漏脂性濕疹、牛皮癬、外陰搔癢、神經性皮炎、彎曲處濕疹、壅滯性濕疹。 |
| 衛署藥輸字第022648號 | 得克膚軟膏 | TRIAMCINOLONE ACETONIDE、GRAMICIDIN、NEOMYCIN (SULFATE)、NYSTAT… | 軟膏劑 | 異位性濕疹、接觸性濕疹、毛囊性濕疹、外陰瘙癢、錢幣形濕疹、創傷後感染性濕疹、漏脂性濕疹、神經性皮炎、嬰兒濕疹、外耳炎、肛門瘙癢、牛皮癬、彎曲處濕疹、壅滯性濕疹。 |
| 衛部藥製字第058318號 | 耳得康耳滴劑 | GRAMICIDIN、NEOMYCIN SULFATE、TRIAMCINOLONE ACETONIDE、NYSTATIN | 點耳液劑 | 外耳道念珠菌感染、表面細菌感染、異位性皮膚炎、濕疹性皮膚炎、過敏接觸性皮膚炎、原發刺激性接觸皮膚炎、皮脂溢出性皮膚炎、溢出性皮膚炎、神經性皮膚炎。 |
| 衛部藥製字第058828號 | ''嘉林''抑黴舒乳膏 | TRIAMCINOLONE ACETONIDE、NYSTATIN、NEOMYCIN SULFATE、GRAMICIDIN | 乳膏劑 | 細菌或念珠菌感染引起之各類濕疹症狀、癬症或皮膚炎。 |
| 衛部藥製字第058944號 | "元福"吉時康乳膏 | NEOMYCIN SULFATE、GRAMICIDIN、NYSTATIN、TRIAMCINOLONE ACETONIDE | 乳膏劑 | 濕疹(異位性、接觸性、脂漏性、毛囊性、彎曲處、創傷後感染性、錢幣形、壅滯性及嬰兒濕疹)、外陰搔癢、神經性皮炎、外耳炎、肛門搔癢及牛皮癬。 |
| 衛部藥製字第059069號 | 寶耳康耳用滴劑 | NYSTATIN、TRIAMCINOLONE ACETONIDE、GRAMICIDIN、NEOMYCIN (SULFAT… | 滴劑 | 外耳道念珠菌感染、表面細菌感染、異位性皮膚炎、濕疹性皮膚炎、過敏接觸性皮膚炎、原發刺激性接觸皮膚炎、皮脂溢出性皮膚炎、溢出性皮膚炎、神經性皮膚炎。 |

<details><summary><strong>已註銷</strong>（87 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>內衛藥製字第003610號</td><td>立達泰定膠囊</td><td>DEMECLOCYCLINE、NYSTATIN</td><td>1995/07/11</td></tr><tr><td>內衛藥輸字第003045號</td><td>尼斯塔汀</td><td>NYSTATIN</td><td>1986/01/16</td></tr><tr><td>衛署藥製字第004069號</td><td>尼爾斯泰外用軟膏</td><td>NYSTATIN</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第004070號</td><td>尼爾斯泰外用水溶性軟膏</td><td>NYSTATIN</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第006513號</td><td>都愛淨口服錠</td><td>NYSTATIN</td><td>2013/10/08</td></tr><tr><td>衛署藥製字第006963號</td><td>都愛淨陰道錠</td><td>NYSTATIN</td><td>2013/10/08</td></tr><tr><td>衛署藥製字第013808號</td><td>脫黴－念親水性軟膏</td><td>TOLNAFTATE、NYSTATIN</td><td>2025/07/29</td></tr><tr><td>衛署藥製字第014219號</td><td>寧司泰定錠</td><td>NYSTATIN</td><td>1988/07/19</td></tr><tr><td>衛署藥製字第014858號</td><td>保好爽水溶性軟膏</td><td>TRIAMCINOLONE ACETONIDE、NYSTATIN、NEOMYCIN (SULFATE)、GRAMICID…</td><td>2007/01/11</td></tr><tr><td>衛署藥製字第015759號</td><td>尼爾斯泰陰道錠（寧司泰定）</td><td>NYSTATIN</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第021405號</td><td>帝黴素乳膏</td><td>IODOCHLORHYDROXYQUIN、NYSTATIN</td><td>1989/03/30</td></tr><tr><td>衛署藥製字第022035號</td><td>康膚軟膚</td><td>TRIAMCINOLONE ACETONIDE、NYSTATIN、NEOMYCIN (SULFATE)、GRAMICID…</td><td>1988/08/10</td></tr><tr><td>衛署藥製字第024959號</td><td>潔克寧乳膏</td><td>TOLNAFTATE、NYSTATIN</td><td>2007/01/11</td></tr><tr><td>衛署藥製字第026913號</td><td>泰司寧錠（寧司泰定）</td><td>NYSTATIN</td><td>1988/12/31</td></tr><tr><td>衛署藥製字第029912號</td><td>滴達膠囊（耐絲菌素）</td><td>NYSTATIN</td><td>2016/09/07</td></tr><tr><td>衛署藥製字第029958號</td><td>康納可軟膏</td><td>NYSTATIN、TRIAMCINOLONE ACETONIDE、GRAMICIDIN、NEOMYCIN (SULFAT…</td><td>1992/06/17</td></tr><tr><td>衛署藥製字第030303號</td><td>滅菌靈懸液用粉劑（耐絲菌素）</td><td>NYSTATIN</td><td>1992/06/02</td></tr><tr><td>衛署藥製字第030316號</td><td>滅菌靈錠（耐絲菌素）</td><td>NYSTATIN</td><td>1988/12/31</td></tr><tr><td>衛署藥製字第030736號</td><td>康納可乳膏</td><td>NEOMYCIN (SULFATE)、GRAMICIDIN、NYSTATIN、TRIAMCINOLONE ACETONI…</td><td>1992/06/17</td></tr><tr><td>衛署藥製字第030744號</td><td>紐黴素軟膏（耐絲菌素）</td><td>NYSTATIN</td><td>1992/07/02</td></tr><tr><td>衛署藥製字第030761號</td><td>紐黴素發泡陰道錠（耐絲菌素）</td><td>NYSTATIN</td><td>1992/06/17</td></tr><tr><td>衛署藥製字第031328號</td><td>紐黴素糖衣錠（耐絲菌素）</td><td>NYSTATIN</td><td>1992/05/21</td></tr><tr><td>衛署藥製字第032012號</td><td>"杏輝"耐適妥乳膏</td><td>TOLNAFTATE、NYSTATIN</td><td>2026/09/07</td></tr><tr><td>衛署藥製字第034746號</td><td>康納可乳膏</td><td>TRIAMCINOLONE ACETONIDE、NEOMYCIN (SULFATE)、GRAMICIDIN、NYSTAT…</td><td>2016/09/20</td></tr><tr><td>衛署藥製字第034747號</td><td>紐黴素軟膏１００，０００單位/公克（耐絲菌素）</td><td>NYSTATIN</td><td>2010/03/01</td></tr><tr><td>衛署藥製字第034755號</td><td>康納可軟膏</td><td>TRIAMCINOLONE ACETONIDE、GRAMICIDIN、NEOMYCIN (SULFATE)、NYSTAT…</td><td>2016/09/20</td></tr><tr><td>衛署藥製字第034756號</td><td>紐黴素糖衣錠５００，０００單位（耐絲菌素）</td><td>NYSTATIN</td><td>2013/01/24</td></tr><tr><td>衛署藥製字第034795號</td><td>紐黴素發泡陰道錠１０萬單位（耐絲菌素）</td><td>NYSTATIN</td><td>2013/01/24</td></tr><tr><td>衛署藥製字第035457號</td><td>保康美乳膏</td><td>GRAMICIDIN、NEOMYCIN (SULFATE)、NYSTATIN、TRIAMCINOLONE ACETONI…</td><td>1998/06/29</td></tr><tr><td>衛署藥製字第035558號</td><td>新四聯親水性軟膏</td><td>TRIAMCINOLONE ACETONIDE、NYSTATIN、GRAMICIDIN、NEOMYCIN (SULFAT…</td><td>1995/10/09</td></tr><tr><td>衛署藥製字第036793號</td><td>復彼寧軟膏</td><td>GRAMICIDIN、NEOMYCIN (SULFATE)、NYSTATIN、TRIAMCINOLONE ACETONI…</td><td>2006/05/09</td></tr><tr><td>衛署藥製字第038947號</td><td>欣四聯親水性軟膏</td><td>TRIAMCINOLONE ACETONIDE、NYSTATIN、GRAMICIDIN、NEOMYCIN (SULFAT…</td><td>2014/08/15</td></tr><tr><td>衛署藥製字第041981號</td><td>保康美乳膏</td><td>NYSTATIN、NEOMYCIN (SULFATE)、GRAMICIDIN、TRIAMCINOLONE ACETONI…</td><td>2008/05/12</td></tr><tr><td>衛署藥輸字第002453號</td><td>敵他種卵型陰道錠</td><td>DIIODOHYDROXYQUIN、DEXAMETHASONE (TERT-BUTYLACETATE)、NYSTATIN</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第003026號</td><td>紐黴素發泡陰道錠</td><td>NYSTATIN</td><td>1988/06/03</td></tr><tr><td>衛署藥輸字第003706號</td><td>念珠速淨陰道錠</td><td>NYSTATIN</td><td>1987/03/20</td></tr><tr><td>衛署藥輸字第003814號</td><td>念珠速淨外用軟膏</td><td>NYSTATIN</td><td>1988/03/05</td></tr><tr><td>衛署藥輸字第003815號</td><td>念珠速淨陰道水溶性軟膏</td><td>NYSTATIN</td><td>1988/03/05</td></tr><tr><td>衛署藥輸字第003839號</td><td>寧司泰定</td><td>NYSTATIN</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第003899號</td><td>念珠速淨外用水溶性軟膏</td><td>NYSTATIN</td><td>1988/03/05</td></tr><tr><td>衛署藥輸字第004070號</td><td>寧司泰定</td><td>NYSTATIN</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第004222號</td><td>寧司泰定</td><td>NYSTATIN</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第005103號</td><td>史耐陰道錠１０００００國際單位</td><td>NYSTATIN</td><td>2009/01/06</td></tr><tr><td>衛署藥輸字第005372號</td><td>念珠速淨口服錠</td><td>NYSTATIN</td><td>1988/09/19</td></tr><tr><td>衛署藥輸字第007583號</td><td>康適膚軟膏</td><td>NYSTATIN、NEOMYCIN (SULFATE)、HALCINONIDE</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第008012號</td><td>康適膚乳膏</td><td>HALCINONIDE、NYSTATIN、NEOMYCIN (SULFATE)</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第008107號</td><td>爽膚特乳膏</td><td>NYSTATIN、CHLORHEXIDINE HCL、DEXAMETHASONE</td><td>1995/02/15</td></tr><tr><td>衛署藥輸字第008295號</td><td>康納可耳滴液０．１％</td><td>GRAMICIDIN、NEOMYCIN (SULFATE)、TRIAMCINOLONE ACETONIDE、NYSTAT…</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第008462號</td><td>紐黴素嬰兒軟膏</td><td>NYSTATIN</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第008626號</td><td>複方美明樂陰道軟膏</td><td>NYSTATIN、NIFURATEL</td><td>2010/12/06</td></tr><tr><td>衛署藥輸字第008704號</td><td>克菌好糊劑</td><td>NYSTATIN</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第009109號</td><td>福爾西得軟膏</td><td>NYSTATIN、BUFEXAMAC、NEOMYCIN (SULFATE)</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第009681號</td><td>尼司他定</td><td>NYSTATIN</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第009741號</td><td>克膚達軟膏</td><td>POLYMYXIN B SULFATE、NEOMYCIN (SULFATE)、HYDROCORTISONE、NYSTAT…</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第010933號</td><td>帶淨陰道錠</td><td>NYSTATIN</td><td>1993/03/17</td></tr><tr><td>衛署藥輸字第010970號</td><td>耐絲菌素外用乳膏</td><td>NYSTATIN</td><td>1993/06/19</td></tr><tr><td>衛署藥輸字第011054號</td><td>黴可淨糖衣錠</td><td>NYSTATIN</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第011616號</td><td>黴克消陰道用軟膠囊</td><td>NYSTATIN</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第011884號</td><td>寧司泰定粉劑</td><td>NYSTATIN</td><td>1999/10/26</td></tr><tr><td>衛署藥輸字第011991號</td><td>康納可</td><td>TRIAMCINOLONE ACETONIDE、NYSTATIN、NEOMYCIN SULFATE、GRAMICIDIN</td><td>1989/03/06</td></tr><tr><td>衛署藥輸字第011992號</td><td>康納可軟膏</td><td>GRAMICIDIN、NEOMYCIN SULFATE、NYSTATIN、TRIAMCINOLONE ACETONIDE</td><td>1987/12/23</td></tr><tr><td>衛署藥輸字第012061號</td><td>瑪宜淨</td><td>NYSTATIN</td><td>1987/03/03</td></tr><tr><td>衛署藥輸字第012261號</td><td>滅菌寧混懸劑</td><td>NYSTATIN</td><td>1988/02/02</td></tr><tr><td>衛署藥輸字第012262號</td><td>紐黴素陰道片</td><td>NYSTATIN</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第012264號</td><td>紐黴素軟膏</td><td>NYSTATIN</td><td>1989/03/06</td></tr><tr><td>衛署藥輸字第012305號</td><td>滅菌靈</td><td>NYSTATIN</td><td>1988/02/02</td></tr><tr><td>衛署藥輸字第012630號</td><td>黴可淨陰道發泡片</td><td>NYSTATIN</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第013474號</td><td>黴克消陰道用軟膠囊</td><td>NYSTATIN</td><td>1993/06/14</td></tr><tr><td>衛署藥輸字第014492號</td><td>耐絲菌素</td><td>NYSTATIN</td><td>1994/03/14</td></tr><tr><td>衛署藥輸字第014981號</td><td>耐絲菌素糖衣錠</td><td>NYSTATIN</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第015489號</td><td>複方美明樂陰道栓劑</td><td>NIFURATEL、NYSTATIN</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第015536號</td><td>耐絲菌素陰道錠１０００００國際單位</td><td>NYSTATIN</td><td>2009/12/30</td></tr><tr><td>衛署藥輸字第015539號</td><td>妮康健陰道錠</td><td>NYSTATIN</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第015556號</td><td>瑪宜淨陰道錠</td><td>NYSTATIN</td><td>2000/10/16</td></tr><tr><td>衛署藥輸字第015712號</td><td>念珠速淨陰道錠</td><td>NYSTATIN</td><td>2001/08/13</td></tr><tr><td>衛署藥輸字第015713號</td><td>念珠速淨口服錠</td><td>NYSTATIN</td><td>2001/08/02</td></tr><tr><td>衛署藥輸字第016279號</td><td>念珠速淨外用軟膏</td><td>NYSTATIN</td><td>2001/08/02</td></tr><tr><td>衛署藥輸字第016280號</td><td>念珠速淨外用水溶性軟膏</td><td>NYSTATIN</td><td>2001/08/02</td></tr><tr><td>衛署藥輸字第016281號</td><td>念珠速淨陰道水溶性軟膏</td><td>NYSTATIN</td><td>2001/08/02</td></tr><tr><td>衛署藥輸字第017753號</td><td>德邁耐絲菌素陰道錠</td><td>NYSTATIN</td><td>1996/07/16</td></tr><tr><td>衛署藥輸字第019561號</td><td>耐絲菌素</td><td>NYSTATIN</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第021629號</td><td>康納可軟膏</td><td>NYSTATIN、TRIAMCINOLONE ACETONIDE、GRAMICIDIN、NEOMYCIN SULFATE</td><td>2008/12/22</td></tr><tr><td>衛署藥輸字第021640號</td><td>紐黴素軟膏１０００００單位/公克</td><td>NYSTATIN</td><td>2007/05/28</td></tr><tr><td>衛署藥輸字第021660號</td><td>口服滴劑</td><td>NYSTATIN</td><td>2013/01/24</td></tr><tr><td>衛署藥輸字第021771號</td><td>耐絲菌素</td><td>NYSTATIN</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第022169號</td><td>德邁耐絲菌素陰道錠</td><td>NYSTATIN</td><td>2013/11/26</td></tr><tr><td>衛署藥輸字第022993號</td><td>耐絲菌乳膏</td><td>NYSTATIN</td><td>2004/05/19</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的潛在禁忌相關疾病**（來自知識圖譜關聯，非仿單文字）：腎上腺皮質功能不全、愛迪生氏症、皮膚萎縮、微血管擴張、微血管疾病、遺傳性出血性微血管擴張症。這些可能反映含類固醇複方（如乳膏）的特性，需對照實際仿單確認。
- **藥物交互作用**：資料庫收錄 347 筆交互作用，但目前皆未標示嚴重度，例如與 Cyclosporine、Fluconazole、Erythromycin、Azithromycin、Bortezomib 等。臨床使用時應逐項查核。

主要警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Nystatin 對念珠菌性外陰陰道炎的機轉直接相關，且台灣已有陰道劑型核准此類適應症。但現有證據以綜述和較舊的研究為主，沒有臨床試驗登記，且 Nystatin 在現行指引中已非首選（唑類藥物取代），因此證據等級為 L3。

**若要推進需要：**
- 補充詳細的作用機轉資料（MOA）
- 與唑類藥物的直接比較研究，特別是氟康唑抗藥或非白色念珠菌的情境
- 確認各製劑的實際仿單警語、禁忌症與交互作用嚴重度
- 釐清是否需要新的適應症，或僅是既有適應症的證據補強

**其他預測適應症備註：** 排名第 2 至第 10 的預測中，除外陰炎（vulvitis，L3，與念珠菌感染相關，同樣可 Proceed with Guardrails）外，其餘如眼眶疾病、囊性畸胎瘤、脊髓皮樣囊腫、生物素代謝疾病、停經後萎縮性陰道炎等，皆缺乏機轉依據與研究證據（L5），建議暫緩（Hold）。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「原適應症」寫細菌感染 | 報告重生後已無此錯誤（2026-10-15：新報告「原適應症」列未再引用 demeclocycline 複方的細菌感染適應症；原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json)；[DailyMed：Nystatin Oral Suspension USP 仿單（PAI）](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=28b4e26e-206a-4e8a-abfe-774b780e91c3) |
| 2026-10-03 | 台灣上市資訊表第一列（立達泰定膠囊） | 已由程式化許可證表取代（原為加註） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 新增「作用機轉」段（每點附仿單來源） | 新增附來源段落 | [DailyMed：Nystatin Oral Suspension USP 仿單（PAI）](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=28b4e26e-206a-4e8a-abfe-774b780e91c3) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

