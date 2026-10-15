---
layout: default
title: Buprenorphine
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 6
---

# Buprenorphine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Buprenorphine：從鴉片類物質成癮與疼痛到急性間歇性紫質症

## 一句話總結

Buprenorphine（丁基原啡因）是部分 mu 類鴉片受體促效劑，在台灣原本用於鴉片類物質成癮的替代療法，以及中重度疼痛（含癌症疼痛）的治療。
TxGNN 模型預測它可能對**急性間歇性紫質症 (Acute Intermittent Porphyria)** 有效，但目前**無臨床試驗**，僅有 **1 篇**麻醉處置個案報告，證據非常薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 麻醉性鎮痛藥（單方有效許可證之核准適應症） |
| 預測新適應症 | 急性間歇性紫質症 (Acute Intermittent Porphyria) |
| TxGNN 預測分數 | 99.41% |
| 證據等級 | L5（僅有模型預測，實質上無支持療效的研究） |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 19 張（有效單方 4／有效複方 5／已註銷 10） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Buprenorphine 是部分 mu 類鴉片受體促效劑，作用於疼痛與成癮治療；它與急性間歇性紫質症的血紅素生合成缺陷之間，並無已知的機轉關聯。

目前唯一的文獻是一篇 1993 年的麻醉處置個案報告，討論的是紫質症患者手術時的圍手術期安全，而非藥物對疾病本身的治療效果。因此，這項預測主要來自知識圖譜的統計關聯，機轉上的合理性不足。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | 病例系列 | Masui | 一名疑似急性間歇性紫質症的患者接受婦科腫瘤手術，文中討論麻醉處置；內容為圍手術期安全，並非治療效果 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Buprenorphine 的不重複許可證共 **19 張**：有效單方 4 張、有效複方 5 張、已註銷 10 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（4 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥製字第049689號 | 比普利注射劑 0.3 毫克/毫升 | 注射劑 | 歐舒邁克有限公司 | 2028/09/30 | 中、重度疼痛。 |
| 衛署藥製字第050250號 | 解佳 舌下錠8毫克 | 舌下錠 | 美時化學製藥股份有限公司 | 2029/07/22 | 鴉片類物質成癮之替代療法。 |
| 衛部藥輸字第027727號 | 鹽酸丁基原啡因 | （粉） | 如山藥業有限公司 | 2024/08/21 | 麻醉性鎮痛藥 |
| 衛部藥輸字第028483號 | 丁基原啡因鹽酸鹽 | （粉） | 恒亞貿易股份有限公司 | 2028/05/22 | 麻醉性鎮痛藥。 |

**有效・複方（適應症屬整個複方，不是本藥單獨的適應症）**（5 張）

| 許可證字號 | 品名 | 主成分 | 劑型 | 核准適應症 |
|------|------|------|------|------|
| 衛署藥製字第050251號 | 解佳益 舌下錠 | BUPRENORPHINE HYDROCHLORIDE、NALOXONE HCL DIHYDRATE | 舌下錠 | 鴉片類物質成癮之替代療法。 |
| 衛署藥輸字第024951號 | 舒倍生 2 毫克 | BUPRENORPHINE HYDROCHLORIDE、NALOXONE HCL DIHYDRATE | 舌下錠 | 鴉片類物質成癮之替代療法。 |
| 衛署藥輸字第024952號 | 舒倍生 8 毫克 | BUPRENORPHINE HYDROCHLORIDE、NALOXONE HCL DIHYDRATE | 舌下錠 | 鴉片類物質成癮之替代療法。 |
| 衛部藥製字第058289號 | 解佳益 4/1毫克 舌下錠 | BUPRENORPHINE HYDROCHLORIDE、NALOXONE HCL DIHYDRATE | 舌下錠 | 鴉片類物質成癮之替代療法 |
| 衛部藥製字第058395號 | 解佳益2/0.5毫克舌下錠 | BUPRENORPHINE HYDROCHLORIDE、NALOXONE HCL DIHYDRATE | 舌下錠 | 鴉片類物質成癮之替代療法。 |

<details><summary><strong>已註銷</strong>（10 張，展開）</summary>
<table><thead><tr><th>許可證字號</th><th>品名</th><th>主成分</th><th>註銷日期</th></tr></thead><tbody><tr><td>衛署藥輸字第021625號</td><td>丁基原啡因舌下錠０．２毫克</td><td>BUPRENORPHINE (AS HYDROCHLORIDE)</td><td>2024/01/03</td></tr><tr><td>衛署藥輸字第021626號</td><td>丁基原啡因注射液０．３毫克/毫升</td><td>BUPRENORPHINE HYDROCHLORIDE</td><td>2023/12/26</td></tr><tr><td>衛署藥輸字第024949號</td><td>速百騰 2 毫克</td><td>BUPRENORPHINE HYDROCHLORIDE</td><td>2021/11/12</td></tr><tr><td>衛署藥輸字第024950號</td><td>速百騰 8 毫克</td><td>BUPRENORPHINE HYDROCHLORIDE</td><td>2021/11/12</td></tr><tr><td>衛部藥輸字第026280號</td><td>舒免疼穿皮貼片劑5微公克/小時</td><td>BUPRENORPHINE</td><td>2022/01/27</td></tr><tr><td>衛部藥輸字第026281號</td><td>舒免疼穿皮貼片劑10微公克/小時</td><td>BUPRENORPHINE</td><td>2022/01/28</td></tr><tr><td>衛部藥輸字第026282號</td><td>舒免疼穿皮貼片劑20微公克/小時</td><td>BUPRENORPHINE</td><td>2022/01/27</td></tr><tr><td>衛部藥輸字第026740號</td><td>鹽酸丁基原啡因</td><td>Buprenorphine HCL</td><td>2023/06/16</td></tr><tr><td>衛部藥輸字第026935號</td><td>全克痛穿皮貼片劑35微克/小時</td><td>BUPRENORPHINE</td><td>2023/09/07</td></tr><tr><td>衛部藥輸字第026936號</td><td>全克痛穿皮貼片劑52.5微克/小時</td><td>BUPRENORPHINE</td><td>2023/08/21</td></tr></tbody></table></details>

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**（來自知識圖譜，非仿單內容）：包括長 QT 症候群與尖端扭轉型心律不整、慢性阻塞性肺病與呼吸衰竭、肝病與慢性 B/C 型肝炎、腎上腺皮質功能不全、甲狀腺功能低下、麻痺性腸阻塞與腸阻塞、良性攝護腺增生、顱內高壓、藥物依賴與物質濫用等。
- **藥物交互作用**：共查得 264 筆，主要的「嚴重 (Major)」交互作用包括 Morphine、Alvimopan、Bupropion、Cisapride、Dolasetron；中度交互作用包括 Famotidine、Loperamide、Clarithromycin、Dexamethasone 等。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這項預測僅來自模型，沒有臨床試驗，文獻也只是麻醉處置個案報告，機轉上看不出治療關聯。
- 此外，Buprenorphine 的安全性考量（呼吸抑制、肝病、QT 延長等）也使缺乏證據的新用途更難推進。

**若要推進需要：**
- 補充詳細的作用機轉資料，並評估與血紅素生合成途徑是否有任何關聯。
- 進行系統性文獻回顧，確認是否有紫質症患者使用 Buprenorphine 的安全性或療效資料。
- 在有任何前臨床或機轉證據之前，不建議啟動臨床開發。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「速必治舌下錠 (含 naloxone)」 | 更正 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「舒免疼貼片」許可證已註銷 | 加註 | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-04 | 頁首證據等級 | 頁首等級依總覽表重算（原 L5→L4） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

