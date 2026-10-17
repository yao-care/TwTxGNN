---
layout: default
title: Nebivolol
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-16
description: "Nebivolol：預測新適應症為惡性腎血管性高血壓 (Malignant Renovascular Hypertension)（證據等級 L5）。原適應症：治療原發性高血壓"
monitor_inn: "Nebivolol"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Nebivolol
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

# Nebivolol：從原發性高血壓到惡性腎血管性高血壓

## 一句話總結

Nebivolol 是一種 β1 選擇性阻斷劑，原本用於治療原發性高血壓。
TxGNN 模型預測它可能對**惡性腎血管性高血壓 (Malignant Renovascular Hypertension)** 有效，
但目前**沒有臨床試驗**，也**沒有直接相關的文獻**支持，證據僅來自模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 治療原發性高血壓 |
| 預測新適應症 | 惡性腎血管性高血壓 (Malignant Renovascular Hypertension) |
| TxGNN 預測分數 | 99.42% |
| 證據等級 | L5 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 5 張（有效單方 5／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

<!-- review:begin nebivolol-moa-2026-10-03 -->

## Nebivolol 的作用機轉

<!-- moa-sourced: 2026-10-03 用戶拍板例外，只限附來源的作用機轉段 -->

以下只說明這個藥原本怎麼作用，每一點都摘自官方仿單的藥理段落並附連結；與本頁的老藥新用預測無關，也不構成用藥建議。

- Nebivolol 是 β 腎上腺素受體阻斷劑；在多數人（CYP2D6 廣泛代謝者）且劑量 10 mg 以下時，偏向選擇性阻斷 β1；在慢代謝者或較高劑量時，β1 與 β2 都會被抑制。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8b8ad213-1dc8-454e-a524-075685c0e1a8)）
- 在臨床劑量下，它沒有內在擬交感活性與膜穩定作用，也沒有 α1 受體阻斷作用。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8b8ad213-1dc8-454e-a524-075685c0e1a8)）
- 仿單寫明降血壓的機轉**尚未完全確立**，可能的因素包括：心跳減慢、心肌收縮力下降、腦部血管運動中樞送往周邊的交感神經張力減少、腎素活性受抑制，以及血管擴張使周邊阻力下降。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8b8ad213-1dc8-454e-a524-075685c0e1a8)）

**來源**：[DailyMed：BYSTOLIC（nebivolol）美國仿單（Allergan），§12 Clinical Pharmacology](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8b8ad213-1dc8-454e-a524-075685c0e1a8)，版本日期 2024-08-01；查閱日期 2026-10-03。

---

<!-- review:end nebivolol-moa-2026-10-03 -->

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Nebivolol 是 β1 選擇性阻斷劑，並可透過一氧化氮 (NO) 機制產生血管擴張，在原發性高血壓的降壓療效已獲核准。機轉上，這種降壓作用可能適用於嚴重的高血壓狀態。

不過，惡性腎血管性高血壓是由腎素驅動的高血壓急症，與原發性高血壓的病理機制不同。目前沒有任何臨床或文獻證據直接驗證 Nebivolol 在此情境的效果，支持僅來自 TxGNN 預測。

TxGNN 另外預測的其他適應症包括惡性高血壓性腎病變、肺高壓（肺部疾病或缺氧所致，以及機轉不明的多因素型）與 Braddock 症候群。其中多數同樣沒有直接研究；Braddock 症候群在機轉上更缺乏明確關聯。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對首要預測（惡性腎血管性高血壓），目前無相關文獻。

作為參考，第 3 名預測「肺高壓」有一批間接文獻，但**均非直接研究肺高壓**：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23506636](https://pubmed.ncbi.nlm.nih.gov/23506636/) | 2013 | RCT | Int J Cardiol | CARNEBI 試驗：比較 carvedilol、nebivolol、bisoprolol 在中度心衰竭的多參數表現 |
| [21045724](https://pubmed.ncbi.nlm.nih.gov/21045724/) | 2011 | RCT | J Hypertens | 比較選擇性與非選擇性 β 阻斷劑在高海拔缺氧下的 24 小時血壓影響 |
| [21883997](https://pubmed.ncbi.nlm.nih.gov/21883997/) | 2012 | 隨機對照試驗 | Cardiovasc Ther | 比較 nebivolol 與 carvedilol 對健康受試者高海拔運動表現的影響 |
| [19789971](https://pubmed.ncbi.nlm.nih.gov/19789971/) | 2009 | Review | Cardiovasc Drugs Ther | 回顧 β 阻斷劑對心衰竭患者肺功能的影響 |
| [36947849](https://pubmed.ncbi.nlm.nih.gov/36947849/) | 2023 | 動物研究 | Can J Physiol Pharmacol | Nebivolol 透過 AKT1/Hif-1α/eNOS 路徑減輕大鼠 methotrexate 腎毒性 |
| [32128711](https://pubmed.ncbi.nlm.nih.gov/32128711/) | 2020 | 動物研究 | Pharmacol Rep | Nebivolol 對大鼠急性腎損傷具保護作用，可能與 SGLT2 相關 |
| [34693844](https://pubmed.ncbi.nlm.nih.gov/34693844/) | 2022 | 動物研究 | Drug Chem Toxicol | Nebivolol 經 AKT1/Hif1α/eNOS 減輕 methotrexate 肝毒性 |
| [35202159](https://pubmed.ncbi.nlm.nih.gov/35202159/) | 2022 | 體外研究 | Toxins | Nebivolol 對馬兜鈴酸誘發的內皮細胞氧化壓力具保護作用 |
| [23400988](https://pubmed.ncbi.nlm.nih.gov/23400988/) | 2013 | 動物研究 | Anesth Analg | 高選擇性 β1 阻斷在大鼠血液稀釋後造成腦灌流劑量依賴性受損（安全性警訊） |
| [42264321](https://pubmed.ncbi.nlm.nih.gov/42264321/) | 2026 | 體外研究 | Life Sci | Nebivolol 對子癇前症體外模型的內皮反應之藥理作用 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Nebivolol 的不重複許可證共 **5 張**：有效單方 5 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（5 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥製字第061020號 | 欣倍泰錠5毫克 | 錠劑 | 健喬信元醫藥生技股份有限公司 | 2031/11/08 | 治療原發性高血壓。 |
| 衛部藥製字第061041號 | 舒爾脈錠5毫克 | 錠劑 | 生達化學製藥股份有限公司二廠 | 2031/12/13 | 治療原發性高血壓。 |
| 衛部藥製字第062403號 | 耐洛心 錠5毫克 | 錠劑 | 永信藥品工業股份有限公司 | 2031/08/07 | 治療原發性高血壓。 |
| 衛部藥輸字第026700號 | 耐比洛錠5毫克 | 錠劑 | 新加坡商美納里尼醫藥有限公司台灣分公司 | 2031/01/22 | 治療原發性高血壓。 |
| 衛部藥輸字第028953號 | 氟色原烷洛鹽酸鹽 | （粉） | 盛佳國際股份有限公司 | 2030/05/13 | 治療原發性高血壓。 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **禁忌症（知識圖譜資料，非仿單內容）**：知識圖譜列出的相關疾病包括肝衰竭、肝病、膽囊疾病、糖尿病、糖尿病酮酸中毒、周邊血管疾病、間歇性跛行、周邊動脈疾病、低血糖、房室傳導阻滯、支氣管疾病、病態竇症候群與家族性病態竇症候群。
- **藥物交互作用**：共查得 174 筆交互作用。列出的項目多為中度，例如 epinephrine、hydrocortisone、hyoscyamine、bupropion、triamcinolone、morphine、atropine、dexamethasone、canagliflozin、chlorpropamide、dapagliflozin 等；aspirin 與氧化鎂為輕度。
- **特別提醒**：支氣管疾病與缺氧情境下使用 β 阻斷劑須留意呼吸安全，這與肺高壓的預測方向直接相關。

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都沒有臨床試驗，且沒有直接研究該疾病的文獻，證據等級為 L5（僅模型預測）。
- 惡性腎血管性高血壓是腎素驅動的高血壓急症，與 Nebivolol 原適應症的病理機制不同；口服 β 阻斷劑是否適合急症處置仍缺乏依據。

**若要推進需要：**
- 補充 Nebivolol 的作用機轉資料（MOA）。
- 針對惡性腎血管性高血壓進行系統性文獻回顧，並檢索臨床試驗登記。
- 評估口服劑型與高血壓急症情境的相容性（給藥途徑）。
- 若考慮肺高壓方向，需先釐清 β 阻斷劑在肺部疾病、缺氧情境的呼吸安全性。
- 進行更完整的安全性評估，涵蓋知識圖譜列出的相關疾病與主要藥物交互作用。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 新增「作用機轉」段（每點附仿單來源） | 新增附來源段落 | [DailyMed：BYSTOLIC 美國仿單 §12](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8b8ad213-1dc8-454e-a524-075685c0e1a8) |
| 2026-10-04 | 頁首證據等級 | 報告重生後已無此錯誤（2026-10-16：報告重生後頁首依新報告為 L5，此筆記的是舊版報告的重算；原為頁首等級依總覽表重算（原 L5→L3）） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

