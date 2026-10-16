---
layout: default
title: Vismodegib
parent: 高證據等級 (L1-L2)
nav_order: 302
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-16
description: "Vismodegib：預測新適應症為皮膚癌 (Skin Cancer)（證據等級 L2）。原適應症：治療轉移性基底細胞癌，或不適合接受手術或放射線治療之局部晚期基底細胞癌成人病患"
---

# Vismodegib
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Vismodegib：從基底細胞癌到皮膚癌

## 一句話總結

Vismodegib 是口服 Hedgehog 路徑抑制劑，原本用於治療轉移性或局部晚期基底細胞癌。
TxGNN 模型預測它可能對**皮膚癌 (Skin Cancer)** 有效，
目前有 **12 個臨床試驗**和 **20 篇文獻**支持這個方向。
需要注意：此預測與現有許可適應症高度重疊，屬於符合仿單的用途，並非真正的新適應症。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 治療轉移性基底細胞癌，或不適合接受手術或放射線治療之局部晚期基底細胞癌成人病患 |
| 預測新適應症 | 皮膚癌 (Skin Cancer) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L2 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 1 張（有效單方 1／有效複方 0／已註銷 0） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據文獻，Vismodegib 是 Smoothened (SMO) 的選擇性抑制劑，可阻斷 Hedgehog 訊號路徑。基底細胞癌多數具有 Hedgehog 路徑的異常活化，抑制 SMO 可降低腫瘤增殖。

基底細胞癌是最常見的皮膚癌類型，因此「皮膚癌」這個預測，實質上涵蓋了已核准的適應症。
這代表預測方向合理，但目前的證據主要支持基底細胞癌，其他皮膚癌類型（如鱗狀細胞癌）的證據並未呈現。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01543581](https://clinicaltrials.gov/study/NCT01543581) | Phase 2 | 完成 | 3 | 安慰劑對照，評估 Vismodegib 用於 Mohs 手術前基底細胞癌的療效與安全性；樣本數極小 |
| [NCT01835626](https://clinicaltrials.gov/study/NCT01835626) | Phase 2 | 完成 | 24 | 放射線治療合併 Vismodegib 用於頭頸部局部晚期基底細胞癌的安全性與耐受性 |
| [NCT01631331](https://clinicaltrials.gov/study/NCT01631331) | Early Phase 1 | 完成 | 15 | 手術前使用 Vismodegib 治療散發性基底細胞癌的先導研究 |
| [NCT05463757](https://clinicaltrials.gov/study/NCT05463757) | N/A | 招募中 | 80 | 荷蘭 Vismodegib 與 Sonidegib 用於晚期及多發性基底細胞癌的觀察性登錄研究 |
| [NCT05651828](https://clinicaltrials.gov/study/NCT05651828) | Early Phase 1 | 招募中 | 34 | 比較四種給藥時程（含個人化間歇給藥）用於晚期基底細胞癌 |
| [NCT02690948](https://clinicaltrials.gov/study/NCT02690948) | Phase 1/2 | 完成 | 16 | Pembrolizumab 加或不加 Vismodegib 用於無法切除或轉移性基底細胞癌 |
| [NCT06357988](https://clinicaltrials.gov/study/NCT06357988) | Phase 2 | 進行中（不再招募） | 34 | NCI-MATCH 子試驗，用於 SMO 或 PTCH1 突變的非基底細胞皮膚癌腫瘤 |
| [NCT02694224](https://clinicaltrials.gov/study/NCT02694224) | Phase 2 | 未知 | 40 | 標準新輔助化療加入 Vismodegib 用於三陰性乳癌（病灶非皮膚癌） |
| [NCT01071564](https://clinicaltrials.gov/study/NCT01071564) | Phase 1 | 終止 | 13 | Vismodegib 合併 Notch 抑制劑用於晚期乳癌 |
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | 進行中（不再招募） | 6452 | NCI-MATCH 基因導向治療總試驗，Vismodegib 僅為其中一個子組 |

另有 SMMART 平台試驗（NCT03878524、NCT05238831）因提前終止或撤銷，幾乎無可用證據，未列入上表。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36795228](https://pubmed.ncbi.nlm.nih.gov/36795228/) | 2023 | 系統性回顧／統合分析 | Am J Clin Dermatol | 更新評估 Hedgehog 抑制劑用於基底細胞癌的療效與安全性 |
| [37604067](https://pubmed.ncbi.nlm.nih.gov/37604067/) | 2023 | Review（指引） | Eur J Cancer | 歐洲基底細胞癌診療共識指引 2023 更新 |
| [31288208](https://pubmed.ncbi.nlm.nih.gov/31288208/) | 2019 | Review（指引） | Eur J Cancer | 歐洲基底細胞癌診療共識指引，提出「易治療／難治療」分類 |
| [26919418](https://pubmed.ncbi.nlm.nih.gov/26919418/) | 2016 | Review | Cell | Vismodegib 與 Sonidegib 為 SMO 抑制劑，均核准用於局部晚期基底細胞癌，Vismodegib 另核准用於轉移性 |
| [22679179](https://pubmed.ncbi.nlm.nih.gov/22679179/) | 2012 | Review | Clin Cancer Res | FDA 核准主要依據一項非隨機、平行世代的 Phase 2 研究 |
| [22653209](https://pubmed.ncbi.nlm.nih.gov/22653209/) | 2012 | Review | Nat Rev Drug Discov | 說明 Vismodegib 的核准基礎與藥物特性 |
| [24756807](https://pubmed.ncbi.nlm.nih.gov/24756807/) | 2014 | Review | Recent Results Cancer Res | Hedgehog 異常活化見於基底細胞癌，亦見於髓母細胞瘤等多種癌症 |
| [23719880](https://pubmed.ncbi.nlm.nih.gov/23719880/) | 2013 | Review | Am J Health Syst Pharm | 回顧藥理、療效、不良反應與臨床定位 |
| [32759706](https://pubmed.ncbi.nlm.nih.gov/32759706/) | 2020 | Review | Int J Mol Sci | 基底細胞癌的組織學與分子特徵及系統性治療抗藥機轉 |
| [26566923](https://pubmed.ncbi.nlm.nih.gov/26566923/) | 2016 | Review | Int J Dermatol | 口服 SMO 抑制劑用於晚期非黑色素瘤皮膚癌的文獻回顧 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Vismodegib 的不重複許可證共 **1 張**：有效單方 1 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第026444號 | 愛維德膠囊150毫克 | 膠囊劑 | 羅氏大藥廠股份有限公司 | 2030/03/13 | 治療轉移性基底細胞癌，或不適合接受手術或放射線治療之局部晚期(Locally Advanced)基底細胞癌成人病患。 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（Hedgehog／SMO 抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：本報告彙整的資料共收錄 56 項已知交互作用。
  - 中度：Clarithromycin。
  - 輕度：多為制酸劑與胃酸抑制劑，包括 H2 受體拮抗劑（Famotidine、Ranitidine、Cimetidine、Nizatidine）、質子幫浦抑制劑（Omeprazole、Esomeprazole、Lansoprazole、Pantoprazole、Rabeprazole、Dexlansoprazole），以及含鋁、鎂、鈣的制酸劑。
  - 以上僅列出部分項目，完整清單請於處方前查詢。
- **致畸胎性**：評估中的風險控管重點包含懷孕防護措施，詳細警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 皮膚癌預測的證據主要來自基底細胞癌，包括數個已完成的 Phase 2 試驗與多篇指引及回顧，證據等級 L2。
- 但此方向與現有許可適應症重疊，並非真正的新適應症，且對基底細胞癌以外的皮膚癌尚無證據。
- 已完成的 Phase 2 試驗人數很少（3 至 24 人），單獨解讀時需保守。

**若要推進需要：**
- 確認病患為基底細胞癌組織學診斷，並符合許可適應症範圍。
- 若欲擴展到其他皮膚癌類型，需另行蒐集該類型的臨床證據。
- 補齊作用機轉的官方資料（DrugBank）。
- 處方前審查 56 項已知交互作用（特別是 Clarithromycin），並落實致畸胎性防護。
- 補充原廠仿單的警語與禁忌資料。

---

### 附註：其他預測適應症

資料中另有幾項預測，證據都不足以作為推進依據：

- **著色性乾皮症（xeroderma pigmentosum）**：僅有個案報告，顯示 Vismodegib 可治療此類病人的基底細胞癌，並非治療該疾病本身，屬 L4，建議作為研究問題。
- **髓母細胞瘤（極度結節型）**：機轉上合理（SHH 亞群），但無試驗或文獻，屬 L5，建議 Hold。
- **其他**（環狀表皮鬆解性魚鱗癬、單純性大皰性表皮鬆解症、Brenner 瘤等）：僅有模型預測，部分無明確機轉連結，屬 L5，建議 Hold。

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 快速總覽「許可證數：2 張」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

