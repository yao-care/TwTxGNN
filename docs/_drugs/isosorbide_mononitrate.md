---
layout: default
title: Isosorbide Mononitrate
parent: 僅模型預測 (L5)
nav_order: 147
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

# Isosorbide mononitrate：從狹心症到多毛症

## 一句話總結

Isosorbide mononitrate（單硝酸異山梨酯）是長效有機硝酸酯類藥物，原本用於預防狹心症發作。
TxGNN 模型預測它可能對**多毛症 (Hypertrichosis)** 有效，
目前**無臨床試驗**、**無文獻**直接支持這個方向，預測純粹來自模型拓樸推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 預防狹心症發作 |
| 預測新適應症 | 多毛症 (Hypertrichosis) |
| TxGNN 預測分數 | 99.995% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 30 張（有效單方 11／有效複方 0／已註銷 19） |
| 建議決策 | Hold |

<!-- review:begin isosorbide-mononitrate-hypertrichosis-rereview-2026-10-03 -->

> **待重審（2026-10-03）**：多毛症這筆預測的機轉討論有一項前提與仿單不符（見下方「為什麼這個預測合理」的查核加註），已標記待重審；證據等級、文獻與決策在重審完成前不更動。依據：[emc：Regaine for Men Extra Strength Scalp Solution 5% w/v SmPC §5.1](https://www.medicines.org.uk/emc/product/5765/smpc)。

<!-- review:end isosorbide-mononitrate-hypertrichosis-rereview-2026-10-03 -->

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA）。根據已知資訊，Isosorbide mononitrate 屬於有機硝酸酯類藥物，以 NO 供體角色釋放一氧化氮（NO），透過 **NO → cGMP → PKG** 路徑促進血管平滑肌舒張，用於預防狹心症的療效已被廣泛驗證。

從概念上推測，NO 引發的局部血管舒張理論上可改善毛囊微循環，與 minoxidil 誘發多毛症的現象有一定相似性。然而，minoxidil 促進毛髮生長的機轉主要透過開放 K⁺ 通道（而非 NO/cGMP），兩條路徑本質不同，機轉類比十分間接。

<!-- review:begin isosorbide-mononitrate-minoxidil-k-channel-premise-2026-10-03 -->

> **查核加註（2026-10-03）**：此前提與仿單不符。Minoxidil 外用製劑仿單寫明它促進毛髮生長的機轉尚未完全了解，只列出增加毛幹直徑、刺激並延長生長期等作用，沒有把生髮機轉歸於開放鉀離子通道。上段原文保留未改。依據：[emc：Regaine for Men Extra Strength Scalp Solution 5% w/v SmPC §5.1](https://www.medicines.org.uk/emc/product/5765/smpc)。

<!-- review:end isosorbide-mononitrate-minoxidil-k-channel-premise-2026-10-03 -->

目前對於 Isosorbide mononitrate 用於多毛症，**無任何前臨床、臨床試驗或文獻支持**。此預測純粹基於 TxGNN 圖神經網路的知識圖譜拓樸關聯，尚需前臨床實驗驗證其生物學合理性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

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

---

## 安全性考量

**藥物交互作用**：共收錄 **189 筆**交互作用記錄（來源：DDInter），以下列出主要交互藥物：

| 交互藥物 | 嚴重程度 | 備註 |
|---------|---------|------|
| Bupropion | 中度 (Moderate) | 抗憂鬱/戒菸用藥 |
| Morphine | 中度 (Moderate) | 鴉片類止痛藥 |
| Canagliflozin | 中度 (Moderate) | SGLT2 抑制劑（糖尿病） |
| Dapagliflozin | 中度 (Moderate) | SGLT2 抑制劑（糖尿病） |
| Empagliflozin | 中度 (Moderate) | SGLT2 抑制劑（糖尿病） |
| Ertugliflozin | 中度 (Moderate) | SGLT2 抑制劑（糖尿病） |
| Dronabinol | 中度 (Moderate) | 大麻素類 |
| Nabilone | 中度 (Moderate) | 大麻素類 |
| Opium | 中度 (Moderate) | 鴉片類 |
| Rosiglitazone | 中度 (Moderate) | TZD 類降血糖藥 |
| Omeprazole | 輕度 (Minor) | 質子幫浦抑制劑 |

> ⚠️ **特別提醒**：Isosorbide mononitrate 與 PDE5 抑制劑（sildenafil、tadalafil 等）合併使用為**已知臨床禁忌**，可能導致嚴重低血壓，規劃任何再利用研究時需嚴格排除此用藥組合。

---

## 結論與下一步

**決策：Hold**

**理由：**
目前僅有 TxGNN 模型預測（L5），完全無前臨床或臨床研究支持 Isosorbide mononitrate 用於多毛症治療。機轉連結（NO 血管舒張 → 毛囊微循環）屬於間接推論，且與已知促毛髮生長機轉（K⁺ 通道）不同，生物學合理性待驗證。

**若要推進需要：**
- 補充完整 MOA 資料（從 DrugBank API 查詢 DB01020）
- 執行前臨床毛囊細胞模型研究（毛乳頭細胞體外 NO 刺激實驗）
- 驗證 NO/cGMP 路徑對毛囊生長週期的直接影響
- 評估外用劑型可行性（現有許可劑型為口服及原料藥，全身性低血壓風險限制口服用於皮膚科適應症的可行性）
- 若機轉驗證成功，考慮與 IND 申請前顧問會議（Pre-IND meeting）確認監管路徑

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 預測理由「minoxidil 促進毛髮生長主要透過開放 K⁺ 通道」 | 加註 | [emc：Regaine for Men Extra Strength Scalp Solution 5% w/v SmPC §5.1](https://www.medicines.org.uk/emc/product/5765/smpc) |
| 2026-10-03 | 多毛症預測標記待重審 | 標記待重審 | [emc：Regaine for Men Extra Strength Scalp Solution 5% w/v SmPC §5.1](https://www.medicines.org.uk/emc/product/5765/smpc) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

