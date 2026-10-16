---
layout: default
title: Metoprolol
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
---

# Metoprolol
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

# Metoprolol：從高血壓、狹心症到惡性高血壓性腎病變

## 一句話總結

Metoprolol（美托普洛）是 β1 選擇性阻斷劑，在台灣原本核准用於高血壓與狹心症。
TxGNN 模型預測它可能對**惡性高血壓性腎病變 (Malignant Hypertensive Renal Disease)** 有效，
但目前**沒有臨床試驗與文獻**直接支持這個預測，僅有模型分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓、狹心症 |
| 預測新適應症 | 惡性高血壓性腎病變 (Malignant Hypertensive Renal Disease) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 46 張（有效單方 8／有效複方 0／已註銷 38） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Metoprolol 是 β1 選擇性腎上腺素阻斷劑，已在高血壓與狹心症中確立療效。其降血壓作用部分來自減少腎素（renin）釋放，因此機轉上可能與腎素相關的高血壓病變有關。

惡性高血壓性腎病變和原適應症同屬高血壓相關疾病，這是模型給出高分的合理背景。不過，惡性高血壓通常需要快速起效的注射藥物處理，口服 β 阻斷劑並非典型首選，因此臨床上能否取代或輔助現行治療仍屬未知。

此外，同一份預測清單中的其他候選適應症，證據略多的是心肌梗塞次型（間隔、後側壁）與慢性肺心病（均為 L3），但它們不是本報告的主要預測項目，僅供後續評估參考。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

（備註：同一疾病族群中的「惡性腎血管性高血壓」僅有一篇嗜鉻細胞瘤診斷標記的文獻，與 Metoprolol 的療效無關，因此不列入。）

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Metoprolol 的不重複許可證共 **46 張**：有效單方 8 張、有效複方 0 張、已註銷 38 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（8 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第029301號 | "明德" 心壓暢錠100毫克（美托普洛） | 錠劑 | 明德製藥股份有限公司 | 2029/11/28 | 高血壓、狹心症 |
| 衛署藥製字第029313號 | “成大”貝他寧錠１００毫克（美托普洛） | 錠劑 | 成大藥品股份有限公司 | 2028/12/10 | 高血壓、狹心症 |
| 衛署藥製字第031032號 | “健喬”心舒寧錠１００毫克（美托普洛） | 錠劑 | 健喬信元醫藥生技股份有限公司 | 2028/08/30 | 高血壓、狹心症。 |
| 衛署藥製字第036844號 | 速暢壓錠100毫克 | 錠劑 | 約克製藥股份有限公司 | 2028/10/20 | 高血壓、狹心症。 |
| 衛署藥製字第048912號 | “生泰”琥珀酸美托普洛 | 原料藥結晶性粉末 | 生泰合成工業股份有限公司 | 2027/07/30 | 降血壓劑。 |
| 衛署藥製字第057407號 | "永日"琥珀酸美托普洛 | 原料藥粉末 | 永日化學工業股份有限公司台中幼獅廠 | 2027/10/18 | 降血壓劑。 |
| 衛部藥輸字第026220號 | 酒石酸美托普洛 | （粉） | 新雙隆生技股份有限公司 | 2028/12/16 | 降壓劑 |
| 衛部藥輸字第026617號 | 琥珀酸美托普洛 | （粉） | 新雙隆生技股份有限公司 | 2030/09/03 | 降血壓劑 |

<details><summary><strong>已註銷</strong>（38 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥製字第035842號</td><td>美托普洛錠１００公絲</td><td>METOPROLOL TARTRATE</td><td>2010/02/08</td></tr><tr><td>衛署藥製字第040476號</td><td>"生泰"酒石酸美托普洛</td><td>METOPROLOL TARTRATE</td><td>2019/05/16</td></tr><tr><td>衛署藥製字第040547號</td><td>"壽元"滅得錠１００公絲/（美托普洛）</td><td>METOPROLOL TARTRATE</td><td>2023/07/21</td></tr><tr><td>衛署藥製字第041956號</td><td>"十全"心達樂錠100毫克(酒石酸美托普洛)</td><td>METOPROLOL TARTRATE</td><td>2025/05/14</td></tr><tr><td>衛署藥輸字第009358號</td><td>舒壓寧錠１００公絲</td><td>METOPROLOL TARTRATE</td><td>1989/07/25</td></tr><tr><td>衛署藥輸字第012933號</td><td>倍舒壓錠</td><td>HYDROCHLOROTHIAZIDE (EQ TO 3,4-DIHYDROCHLOROTHIAZIDE)、METOPR…</td><td>1985/11/15</td></tr><tr><td>衛署藥輸字第013519號</td><td>舒壓寧注射液１公絲/公撮</td><td>METOPROLOL TARTRATE</td><td>1989/05/03</td></tr><tr><td>衛署藥輸字第013672號</td><td>舒壓寧持效錠２００公絲</td><td>METOPROLOL TARTRATE</td><td>1989/05/03</td></tr><tr><td>衛署藥輸字第014370號</td><td>倍舒壓錠</td><td>HYDROCHLOROTHIAZIDE (EQ TO 3,4-DIHYDROCHLOROTHIAZIDE)、METOPR…</td><td>1989/05/03</td></tr><tr><td>衛署藥輸字第015811號</td><td>美托普洛酒石酸鹽</td><td>METOPROLOL</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第015962號</td><td>樂華寧錠</td><td>METOPROLOL TARTRATE</td><td>1991/12/18</td></tr><tr><td>衛署藥輸字第016210號</td><td>"合吉" 酒石酸美托普洛</td><td>METOPROLOL TARTRATE</td><td>2013/12/16</td></tr><tr><td>衛署藥輸字第016503號</td><td>美得寧錠１００公絲</td><td>METOPROLOL TARTRATE</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第016564號</td><td>康達心錠</td><td>METOPROLOL TARTRATE</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第016585號</td><td>美得寧錠５０公絲</td><td>METOPROLOL TARTRATE</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第016649號</td><td>可達平錠５０公絲</td><td>METOPROLOL TARTRATE</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第016888號</td><td>得耐舒錠１００公絲</td><td>METOPROLOL TARTRATE</td><td>2025/06/03</td></tr><tr><td>衛署藥輸字第017200號</td><td>舒壓寧錠１００公絲</td><td>METOPROLOL TARTRATE</td><td>2013/12/16</td></tr><tr><td>衛署藥輸字第017202號</td><td>舒壓寧持效錠２００公絲</td><td>METOPROLOL TARTRATE</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第017205號</td><td>舒壓寧注射液１公絲/公撮</td><td>METOPROLOL TARTRATE</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第017228號</td><td>倍舒壓錠</td><td>HYDROCHLOROTHIAZIDE (EQ TO 3,4-DIHYDROCHLOROTHIAZIDE)、METOPR…</td><td>2005/06/15</td></tr><tr><td>衛署藥輸字第017477號</td><td>酒石酸美托普洛</td><td>METOPROLOL TARTRATE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第017837號</td><td>美托普洛醇酒石酸酯</td><td>METOPROLOL TARTRATE</td><td>2004/12/23</td></tr><tr><td>衛署藥輸字第018751號</td><td>酒石酸美托普洛</td><td>METOPROLOL TARTRATE</td><td>2005/06/16</td></tr><tr><td>衛署藥輸字第018794號</td><td>樂華寧錠</td><td>METOPROLOL TARTRATE</td><td>1993/06/14</td></tr><tr><td>衛署藥輸字第018891號</td><td>酒石酸美托普洛</td><td>METOPROLOL TARTRATE</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第019044號</td><td>酒石酸鹽美托普洛</td><td>METOPROLOL TARTRATE</td><td>1999/09/22</td></tr><tr><td>衛署藥輸字第019507號</td><td>敏樂舒錠５０公絲</td><td>METOPROLOL TARTRATE</td><td>2019/03/14</td></tr><tr><td>衛署藥輸字第019508號</td><td>敏樂舒錠１００公絲</td><td>METOPROLOL TARTRATE</td><td>2019/03/14</td></tr><tr><td>衛署藥輸字第020097號</td><td>酒石酸美托普洛</td><td>METOPROLOL TARTRATE</td><td>1999/03/11</td></tr><tr><td>衛署藥輸字第020173號</td><td>舒壓寧控釋錠２００公絲</td><td>METOPROLOL SUCCINATE</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第020174號</td><td>舒壓寧控釋錠１００公絲</td><td>METOPROLOL SUCCINATE</td><td>2025/10/07</td></tr><tr><td>衛署藥輸字第020175號</td><td>舒壓寧控釋錠５０公絲</td><td>METOPROLOL SUCCINATE</td><td>2009/12/31</td></tr><tr><td>衛署藥輸字第020540號</td><td>樂必舒緩釋錠１９０公絲</td><td>METOPROLOL</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第021187號</td><td>脈妥普樂注射液１公絲－公撮</td><td>METOPROLOL TARTRATE</td><td>1997/12/10</td></tr><tr><td>衛署藥輸字第021835號</td><td>"莫伊士" 酒石酸美托普洛</td><td>METOPROLOL TARTRATE</td><td>2016/05/30</td></tr><tr><td>衛署藥輸字第021955號</td><td>脈妥普樂注射液１公絲－公撮</td><td>METOPROLOL TARTRATE</td><td>2002/03/29</td></tr><tr><td>衛署藥輸字第023799號</td><td>舒壓寧控釋錠２５公絲</td><td>METOPROLOL SUCCINATE</td><td>2025/03/18</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：資料庫共收錄 337 筆交互作用。部分為中度等級，例如 Epinephrine、Bupropion、Cimetidine、Morphine、Canagliflozin、Dapagliflozin、Chlorpropamide 及多種皮質類固醇（Hydrocortisone、Dexamethasone 等）；Acetylsalicylic acid 與 Magnesium oxide 為輕度。
- **知識圖譜標示的禁忌相關疾病**（來自模型知識圖譜，非仿單文字）：包含糖尿病與酮酸中毒、肝病與肝性腦病變、胰臟炎、痛風、重症肌無力、嗜鉻細胞瘤、低血壓、無尿、全身性紅斑狼瘡、乾癬等。實際禁忌請以原廠仿單為準。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（99.91%），但沒有任何臨床試驗或文獻支持，屬於僅有模型預測的 L5 證據。
- 惡性高血壓通常需要快速降壓的注射藥物，口服 Metoprolol 在此情境的角色不明。

**若要推進需要：**
- 補充 Metoprolol 的作用機轉資料（MOA），並釐清腎素抑制在此疾病的實際角色
- 進行系統性文獻回顧，確認 β 阻斷劑在惡性高血壓腎病變的既有臨床資料
- 若有初步證據，設計小規模探索性研究，並明確界定其與現行標準治療的關係
- 評估腎功能受損族群的劑量與安全性監測計畫

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄；頁首證據等級依本頁「快速總覽」的證據等級列重算，模型預測、總覽表與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-04 | 頁首證據等級 | 報告重生後已無此錯誤（2026-10-16：報告重生後頁首依新報告為 L5，此筆記的是舊版報告的重算；原為頁首等級依總覽表重算（原 L5→L2）） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

