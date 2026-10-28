---
layout: default
title: Nepafenac
parent: 高證據等級 (L1-L2)
nav_order: 192
evidence_level: L2
indication_count: 10
monitor_inn: "Nepafenac"
predicted_indications: ["eye disease", "optic papillitis", "hypotrichosis simplex of the scalp", "seborrheic keratosis", "von Hippel anomaly", "congenital hypotrichosis milia", "mcpherson robertson cammarano syndrome", "lagophthalmos", "vulvar inverted follicular keratosis", "vitreous detachment"]
last_modified_at: 2026-10-16
description: "Nepafenac：預測新適應症為眼部疾病 (Eye Disease)（證據等級 L2）。原適應症：治療白內障手術引起之疼痛與發炎"
---

# Nepafenac
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Nepafenac：從白內障術後疼痛與發炎到眼部疾病
{: .text-alpha }

## 一句話總結

Nepafenac 是一種局部眼用非類固醇消炎藥（NSAID），原本用於治療白內障手術後的疼痛與發炎。
TxGNN 模型預測它可能對**眼部疾病 (Eye Disease)** 有效，
目前有 **40 個臨床試驗**和 **20 篇文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 治療白內障手術引起之疼痛與發炎 |
| 預測新適應症 | 眼部疾病 (Eye Disease) |
| TxGNN 預測分數 | 0.9985 |
| 證據等級 | L2 |
| 台灣上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效單方 2／有效複方 0／已註銷 0） |
| 建議決策 | Proceed with Guardrails |

<!-- review:begin nepafenac-moa-2026-10-03 -->

## Nepafenac（納衛視）的作用機轉

<!-- moa-sourced: 2026-10-03 用戶拍板例外，只限附來源的作用機轉段 -->

以下只說明這個藥原本怎麼作用，每一點都摘自官方仿單的藥理段落並附連結；與本頁的老藥新用預測無關，也不構成用藥建議。

- 點眼後，nepafenac 會穿透角膜，被眼內組織的水解酶轉換成 amfenac，amfenac 是一種非類固醇抗發炎藥（NSAID）。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a2909252-c5f1-421f-9073-b7be90b45b51)）
- Amfenac 被認為會抑制前列腺素 H 合成酶（也就是環氧化酶，COX），這個酶是身體製造前列腺素必需的。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a2909252-c5f1-421f-9073-b7be90b45b51)）
- 雙眼每天點 3 次的試驗中，多數受試者血中只測到很低的 nepafenac 與 amfenac 濃度。（[仿單](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a2909252-c5f1-421f-9073-b7be90b45b51)）

**來源**：[DailyMed：NEVANAC（nepafenac ophthalmic suspension）0.1% 美國仿單（Novartis）§12.1、§12.3](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a2909252-c5f1-421f-9073-b7be90b45b51)，版本日期 2023-04-19；查閱日期 2026-10-03。

---

<!-- review:end nepafenac-moa-2026-10-03 -->

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫未收錄）。根據已知資訊，Nepafenac 是一種前驅藥，點眼後滲入眼內並轉換為活性代謝物 amfenac。Amfenac 可抑制 COX-1 與 COX-2，減少前列腺素介導的眼部發炎、疼痛及血液-眼球屏障破壞。

原適應症屬於眼前節的術後發炎，而「眼部疾病」是範圍較廣的類別。臨床試驗與文獻顯示，nepafenac 也被研究用於白內障術後囊樣黃斑水腫、糖尿病視網膜病變相關黃斑水腫、視網膜前膜手術後恢復，以及屈光雷射術後疼痛等。動物研究也指出，它的活性代謝物可到達後段眼組織。

需要注意的是，「眼部疾病」是很泛的預測。這項預測較適合視為「在術後及視網膜發炎性眼疾中延伸使用」的方向，而非單一明確的新適應症。

## 臨床試驗證據

資料中共有 40 個相關試驗，以下列出最相關的 10 個：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Phase 3 | 完成 | 2120 | 0.3% 懸液用於白內障術後眼部發炎與疼痛的安全性與療效 |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | 完成 | 881 | 0.3% 每日一次 vs 載體，用於糖尿病患者白內障術後 |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Phase 3 | 完成 | 819 | 同上設計之重複試驗，評估糖尿病患者術後臨床結果 |
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Phase 2 | 完成 | 1342 | 0.3% vs 0.1% vs 載體，用於預防與治療白內障術後發炎與疼痛 |
| [NCT00782717](https://clinicaltrials.gov/study/NCT00782717) | Phase 2 | 完成 | 263 | Nevanac 0.1% vs 載體，用於糖尿病視網膜病變患者白內障術後黃斑水腫 |
| [NCT00333255](https://clinicaltrials.gov/study/NCT00333255) | Phase 3 | 完成 | 267 | Nevanac 0.1% 對比 Acular LS，用於白內障術後發炎 |
| [NCT01426854](https://clinicaltrials.gov/study/NCT01426854) | Phase 3 | 完成 | 260 | 0.1% 對比安慰劑，於中國成人白內障術後的療效 |
| [NCT01021761](https://clinicaltrials.gov/study/NCT01021761) | Phase 4 | 完成 | 126 | 比較 Acuvail、Xibrom、Nevanac 對 PGE2 的抑制 |
| [NCT07736690](https://clinicaltrials.gov/study/NCT07736690) | Phase 4 | 完成 | 60 | 圍手術期使用於視網膜前膜手術後的解剖與功能恢復 |
| [NCT03025945](https://clinicaltrials.gov/study/NCT03025945) | N/A | 完成 | 662 | 0.3% 每日一次 vs 安慰劑，預防人工水晶體眼囊樣黃斑水腫 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34120417](https://pubmed.ncbi.nlm.nih.gov/34120417/) | 2021 | RCT | Korean J Ophthalmol | 比較 0.1% nepafenac 與 1% prednisolone 於微切口白內障術後發炎控制 |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | RCT | Ophthalmol Glaucoma | 雷射周邊虹膜切開術後，nepafenac 與 prednisolone 的安全性與療效比較 |
| [41039316](https://pubmed.ncbi.nlm.nih.gov/41039316/) | 2025 | RCT | BMC Ophthalmol | 比較 7 種局部 NSAID 對全視網膜光凝疼痛的止痛效果 |
| [39095467](https://pubmed.ncbi.nlm.nih.gov/39095467/) | 2024 | 統合分析 | Eye (Lond) | 局部 NSAID 對白內障術後黃斑水腫與視力結果影響的網絡統合分析 |
| [34210237](https://pubmed.ncbi.nlm.nih.gov/34210237/) | 2022 | Review | Clin Exp Optom | 回顧 nepafenac 在白內障手術的角色，高眼內穿透且副作用低 |
| [26502088](https://pubmed.ncbi.nlm.nih.gov/26502088/) | 2016 | Review | Dev Ophthalmol | NSAID 在視網膜疾病治療的應用回顧 |
| [25686158](https://pubmed.ncbi.nlm.nih.gov/25686158/) | 2015 | Review | Cochrane Database Syst Rev | 局部 NSAID 用於糖尿病囊樣黃斑水腫的系統性回顧 |
| [26474497](https://pubmed.ncbi.nlm.nih.gov/26474497/) | 2016 | 動物研究 | Exp Eye Res | nepafenac 及其活性代謝物 amfenac 可分布至眼後段 |
| [17259381](https://pubmed.ncbi.nlm.nih.gov/17259381/) | 2007 | 動物研究 | Diabetes | 局部 nepafenac 抑制糖尿病大鼠視網膜微血管病變 |
| [17964407](https://pubmed.ncbi.nlm.nih.gov/17964407/) | 2007 | 病例報告 | J Cataract Refract Surg | 通報一例 nepafenac 相關角膜融解（患者有移植物抗宿主病） |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Nepafenac 的不重複許可證共 **2 張**：有效單方 2 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第024795號 | 納衛視點眼懸液劑 0.1% | 點眼懸液劑 | 台灣諾華股份有限公司 | 2028/03/03 | 治療白內障手術引起之疼痛與發炎。 |
| 衛部藥輸字第026743號 | 以利視點眼懸液劑0.3% | 無菌眼耳鼻用液劑 | 台灣諾華股份有限公司 | 2031/04/15 | 用於成人患者預防及治療白內障手術相關的術後疼痛及發炎 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **知識圖譜標示的潛在禁忌疾病**（來自藥物-疾病關聯資料，並非仿單原文）：類風濕性關節炎、糖尿病、糖尿病酮酸中毒、凝血疾病、角膜炎、角結膜炎、乾眼症、眼乾燥症、角膜潰瘍。
- **文獻提示的風險**：已有病例報告指出，高風險患者（如移植物抗宿主病）使用 nepafenac 後發生角膜融解，角膜上皮缺損或眼表疾病患者需特別留意。
- **藥物交互作用**：目前查無相關資料。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多項已完成的 Phase 2/3 試驗，且 nepafenac 在白內障術後疼痛與發炎已在台灣取得核准，證據等級為 L2。
- 「眼部疾病」過於籠統，現有證據主要集中在白內障術後、糖尿病患者術後黃斑水腫及視網膜手術等具體情境，需先界定明確的目標適應症。

**若要推進需要：**
- 選定具體的目標疾病（例如白內障術後囊樣黃斑水腫預防、視網膜手術後黃斑水腫），並設計對應的確認性試驗
- 補充詳細的作用機轉資料（MOA）
- 針對角膜炎、乾眼症、角膜潰瘍及糖尿病患者建立角膜安全性監測計畫
- 確認台灣現有許可適應症與擬擴充適應症之間的差距，評估是否需申請適應症變更

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 新增「作用機轉」段（每點附仿單來源） | 新增附來源段落 | [DailyMed：NEVANAC 美國仿單 §12.1](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a2909252-c5f1-421f-9073-b7be90b45b51) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

