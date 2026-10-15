---
layout: default
title: Isosorbide Mononitrate
parent: 僅模型預測 (L5)
nav_order: 158
evidence_level: L5
indication_count: 10
---

# Isosorbide Mononitrate
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

# Isosorbide mononitrate：從狹心症預防到毛髮過多症（TxGNN 首位預測）

## 一句話總結

Isosorbide mononitrate（單硝酸異山梨酯）是一種一氧化氮（NO）供體，原本用於預防狹心症發作。
TxGNN 模型預測分數最高的新適應症是**毛髮過多症 (Hypertrichosis)**，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型運算結果。
在所有預測中，只有**肺動脈高壓 (Pulmonary Arterial Hypertension)** 有間接文獻（2 篇），較值得後續研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 預防狹心症之發作 |
| 預測新適應症 | 毛髮過多症 (Hypertrichosis) |
| TxGNN 預測分數 | 99.995% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 30 張（有效單方 11／有效複方 0／已註銷 19） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未收錄）。依一般藥理知識，Isosorbide mononitrate 會釋放 NO，活化可溶性鳥苷酸環化酶（sGC），使 cGMP 上升，進而舒張血管平滑肌，這也是它預防狹心症的基礎。

就毛髮過多症而言，NO/cGMP 血管舒張作用與毛髮過度生長之間沒有已知的關聯，這個預測目前純屬計算結果，機轉上缺乏支持。排名前 9 的預測（毛髮過多症、Ambras 症候群、齒或牙周畸形症候群、Dandy-Walker 畸形症候群、落髮、遺傳性毛幹異常、頭皮單純性毛髮稀少症、先天性毛髮稀少伴粟粒疹、瀰漫性斑禿）多屬遺傳性或結構性疾病，或自體免疫疾病，同樣沒有任何證據。落髮一項僅能類比 minoxidil 這類血管舒張劑，屬於推測。

相對地，排名第 10 的**肺動脈高壓**與原機轉較一致：NO→sGC→cGMP 正是 PAH 治療（PDE5 抑制劑、sGC 刺激劑）的核心路徑，具生物學合理性。不過現有證據只是間接的，故建議以此作為研究問題，而非首位預測。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下為排名第 10 的預測（肺動脈高壓）的文獻；排名第 1 的毛髮過多症無任何文獻。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16422873](https://pubmed.ncbi.nlm.nih.gov/16422873/) | 2005 | Cohort | The Journal of Sexual Medicine | 探討 sildenafil 與 isosorbide mononitrate 在合併勃起功能障礙的冠心病男性中的血行動力學效應（研究對象並非 PAH 病人，屬間接證據） |
| [29705351](https://pubmed.ncbi.nlm.nih.gov/29705351/) | 2018 | 動物研究 | Life Sciences | 在 monocrotaline 誘發肺高壓的大鼠中，探討 NO 敏感型與不敏感型 sGC 的失衡，以及增強 NO 的藥物能否延緩疾病進展 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Isosorbide Mononitrate 的不重複許可證共 **30 張**：有效單方 11 張、有效複方 0 張、已註銷 19 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（11 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第031168號 | 愛速脈錠２０毫克（伊速必得） | 錠劑 | 東生華製藥股份有限公司 | 2028/12/21 | 預防狹心症之發作 |
| 衛署藥製字第033999號 | "優良"優舒錠２０毫克（伊速必得） | 錠劑 | 優良化學製藥股份有限公司 | 2031/05/14 | 預防狹心症之發作。 |
| 衛署藥製字第034312號 | "安成" 伊速必得錠40毫克 | 錠劑 | 保盛藥業股份有限公司 | 2026/09/09 | 預防狹心症之發作。 |
| 衛署藥製字第043364號 | 冠欣錠２０公毫克 | 錠劑 | 健喬信元醫藥生技股份有限公司 | 2029/11/09 | 預防狹心症之發作。 |
| 衛署藥製字第044597號 | 冠欣　持續性藥效錠４０毫克 | 持續性藥效錠 | 健喬信元醫藥生技股份有限公司 | 2031/08/20 | 預防狹心症發作。 |
| 衛署藥製字第049018號 | 冠欣持續性藥效膜衣錠 60 毫克 | 持續性藥效膜衣錠 | 健喬信元醫藥生技股份有限公司 | 2027/09/12 | 預防狹心症發作。 |
| 衛署藥製字第049372號 | 圓心 持續性藥效錠 60 毫克 | 持續性藥效錠 | 瑩碩生技醫藥股份有限公司 | 2028/04/18 | 預防狹心症發作。 |
| 衛署藥製字第049514號 | “十全”愛彼脈持續性藥效膜衣錠 60 毫克 | 持續性藥效膜衣錠 | 十全實業股份有限公司 | 2028/06/18 | 預防狹心症發作。 |
| 衛署藥製字第049522號 | 恩舒率持續性藥效錠 60 毫克 | 持續性藥效錠 | 永茂藥業股份有限公司 | 2028/06/20 | 預防狹心症發作。 |
| 衛署藥輸字第020554號 | 寬心持續性藥效錠６０公絲 | 持續性藥效錠 | 裕利股份有限公司 | 2029/07/25 | 預防狹心症發作。 |
| 衛部藥輸字第026499號 | 稀硝酸異山梨酯 | （粉） | 東譽興業股份有限公司 | 2030/02/06 | 預防狹心症之發作。 |

<details><summary><strong>已註銷</strong>（19 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第011212號</td><td>愛舒脈錠20毫克</td><td>ISOSORBIDE 5-MONONITRATE</td><td>2025/06/16</td></tr><tr><td>衛署藥輸字第011213號</td><td>愛舒脈錠４０公絲</td><td>ISOSORBIDE 5-MONONITRATE</td><td>1999/10/25</td></tr><tr><td>衛署藥輸字第016855號</td><td>益朗痛錠４０公絲</td><td>ISOSORBIDE 5-MONONITRATE</td><td>2009/12/30</td></tr><tr><td>衛署藥輸字第016864號</td><td>益朗痛錠２０公絲</td><td>ISOSORBIDE 5-MONONITRATE</td><td>2009/12/30</td></tr><tr><td>衛署藥輸字第017278號</td><td>平多克錠２０公絲</td><td>ISOSORBIDE 5-MONONITRATE</td><td>1992/10/15</td></tr><tr><td>衛署藥輸字第017405號</td><td>康汝欣持續性藥效錠６０公絲</td><td>ISOSORBIDE 5-MONONITRATE</td><td>1995/07/03</td></tr><tr><td>衛署藥輸字第017408號</td><td>康汝欣持續性藥效錠４０公絲</td><td>ISOSORBIDE 5-MONONITRATE</td><td>1997/03/17</td></tr><tr><td>衛署藥輸字第018594號</td><td>愛心錠－４０公絲</td><td>ISOSORBIDE 5-MONONITRATE</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第018595號</td><td>愛心錠２０公絲</td><td>ISOSORBIDE 5-MONONITRATE</td><td>2010/08/16</td></tr><tr><td>衛署藥輸字第018600號</td><td>舒心錠劑２０公絲</td><td>ISOSORBIDE 5-MONONITRATE</td><td>2000/10/21</td></tr><tr><td>衛署藥輸字第018904號</td><td>單硝酸伊速必得</td><td>ISOSORBIDE 5-MONONITRATE</td><td>2000/10/18</td></tr><tr><td>衛署藥輸字第018953號</td><td>循脈克錠２０公絲</td><td>ISOSORBIDE 5-MONONITRATE、LACTOSE (MILK SUGAR)</td><td>2005/06/14</td></tr><tr><td>衛署藥輸字第019111號</td><td>循脈克錠４０公絲</td><td>ISOSORBIDE 5-MONONITRATE</td><td>2005/06/14</td></tr><tr><td>衛署藥輸字第019423號</td><td>平多克錠２０公絲</td><td>ISOSORBIDE 5-MONONITRATE</td><td>2005/06/03</td></tr><tr><td>衛署藥輸字第021505號</td><td>康汝欣持續性藥效錠４０公絲</td><td>ISOSORBIDE 5-MONONITRATE</td><td>2014/04/03</td></tr><tr><td>衛署藥輸字第022617號</td><td>樂心得持續性藥效錠６０公絲</td><td>ISOSORBIDE 5-MONONITRATE</td><td>2022/07/04</td></tr><tr><td>衛署藥輸字第022812號</td><td>史達德愛舒脈錠２０毫克</td><td>ISOSORBIDE 5-MONONITRATE</td><td>2022/06/10</td></tr><tr><td>衛署藥輸字第024730號</td><td>愛心明持續性藥效錠 60 毫克</td><td>ISOSORBIDE-5-MONONITRATE/ LACTOSE BLEND 90/10</td><td>2017/01/06</td></tr><tr><td>衛部藥陸輸字第000756號</td><td>單硝酸異山梨酯</td><td>Isosorbide Mononitrate</td><td>2022/01/03</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的疾病禁忌關聯**（來自 TxGNN 知識圖譜，非仿單內容）：低血壓、肥厚性心肌病變、心肌梗塞、冠狀動脈血栓、血紅素病變、貧血（含大球性貧血）、甲狀腺機能亢進（含 Graves 病、甲狀腺毒症）、腦內出血。
- **藥物交互作用**：共查得 189 筆。中度交互作用包括 Bupropion、Morphine、Canagliflozin、Dapagliflozin、Empagliflozin、Ertugliflozin、Dronabinol、Nabilone、Opium、Rosiglitazone、Sapropterin；Omeprazole 為輕度。

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測（毛髮過多症）及排名第 2–9 的預測皆無臨床試驗或文獻，機轉上也無合理連結，證據等級為 L5，不建議推進。
- 肺動脈高壓雖有生物學合理性，但現有證據僅為間接的血行動力學研究與動物實驗（L4），且該領域已有 PDE5 抑制劑、sGC 刺激劑等標準藥物。

**若要推進需要：**
- 補齊 Isosorbide mononitrate 的作用機轉資料。
- 若聚焦肺動脈高壓，需進行系統性文獻回顧，並評估相對於現有標準治療的價值。
- 評估低血壓等風險，以及與 PDE5 抑制劑併用時的安全性（併用有顯著降壓風險，須嚴格評估）。
- 就落髮等皮膚毛髮適應症，需先有前臨床研究，並確認給藥途徑（外用或口服）的可行性。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 預測理由「minoxidil 促進毛髮生長主要透過開放 K⁺ 通道」 | 加註 | [emc：Regaine for Men Extra Strength Scalp Solution 5% w/v SmPC §5.1](https://www.medicines.org.uk/emc/product/5765/smpc) |
| 2026-10-03 | 多毛症預測標記待重審 | 標記待重審 → 已重審（見下列重審結果） | [emc：Regaine for Men Extra Strength Scalp Solution 5% w/v SmPC §5.1](https://www.medicines.org.uk/emc/product/5765/smpc) |
| 2026-10-03 | 多毛症預測重審結果 | 重審：維持，證據等級 L5 不變 | [PubMed：Novel and established potassium channel openers stimulate hair growth in vitro: implications for their modes of action in hair follicles（PMID 15816824）](https://pubmed.ncbi.nlm.nih.gov/15816824/)；[PubMed：Human hair follicles contain two forms of ATP-sensitive potassium channels, only one of which is sensitive to minoxidil（PMID 18258787）](https://pubmed.ncbi.nlm.nih.gov/18258787/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

