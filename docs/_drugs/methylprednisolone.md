---
layout: default
title: Methylprednisolone
parent: 中證據等級 (L3-L4)
nav_order: 164
evidence_level: L3
indication_count: 10
---

# Methylprednisolone
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

使用 `txgnn-pipeline` 確認脈絡後，以下依照評估報告 Prompt v5 格式產出完整報告。

---

# Methylprednisolone：從抗炎性皮質固醇到圓禿症

## 一句話總結

Methylprednisolone（甲基培尼皮質醇）是廣泛使用的合成糖皮質固醇，原本核准用於風濕性關節炎、氣喘、過敏性疾患等抗炎與免疫抑制治療。TxGNN 模型預測它可能對**圓禿症 (Alopecia Areata)** 有效，目前有 **1 個直接相關的 Phase 4 臨床試驗**及多項觀察性研究，加上 **20 篇文獻**（含多篇直接研究 methylprednisolone 脈衝療法用於圓禿症）支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抗炎性皮質固醇（風濕性關節炎、氣喘、過敏性疾患） |
| 預測新適應症 | 圓禿症 (Alopecia Areata) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Methylprednisolone 是強效合成糖皮質固醇，透過與細胞內糖皮質固醇受體（GR）結合後，抑制 NF-κB 和 AP-1 等促炎轉錄因子，廣泛下調 IL-1、IL-6、TNF-α 等多種細胞激素，同時抑制 T 細胞活化與增殖。其抗炎效價約為 hydrocortisone 的 5 倍，可口服或靜脈給藥，適合需要快速系統性免疫抑制的急性病程。

圓禿症的核心病理為自體免疫性毛囊破壞：CD8⁺ NKG2D⁺ T 細胞失去對毛囊的「免疫豁免（follicular immune privilege）」，浸潤並攻擊生長期毛囊髮母細胞，導致毛囊微型化與非疤痕性脫髮。Methylprednisolone 的免疫抑制機轉直接針對這條病理路徑——透過抑制 T 細胞媒介的自體免疫浸潤，減少毛囊周圍的炎症環境，脈衝給藥（pulse therapy）可快速阻斷正在進行的活動性免疫攻擊，避免長期低劑量類固醇帶來的全身副作用。

目前文獻中已有多篇臨床研究直接評估 methylprednisolone 口服或靜脈脈衝療法治療廣泛型、難治型圓禿症，顯示此預測並非純粹的演算法推論，而是有臨床實踐基礎的老藥新用候選。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | 完成 | 42 | 直接研究口服大劑量脈衝 methylprednisolone 用於重度難治性圓禿症，探討更高劑量、更高頻率脈衝方案是否能改善全頭禿及全身禿的療效 |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | 觀察性 | 完成 | 296 | Tofacitinib（JAK 抑制劑，±輔助 prednisolone）用於圓禿症的真實世界安全性與療效評估 |
| [NCT03616964](https://clinicaltrials.gov/study/NCT03616964) | Phase 3 | 完成 | 778 | Baricitinib（JAK1/2 抑制劑）用於圓禿症疾病族群的雙盲安慰劑對照大型 RCT，代表同疾病領域最高等級試驗背景 |
| [NCT03845517](https://clinicaltrials.gov/study/NCT03845517) | Phase 2b | 完成 | 350 | PF-06700841（TYK2/JAK1 抑制劑）用於中重度活躍性圓禿症族群的雙盲隨機劑量探索研究 |
| [NCT05162586](https://clinicaltrials.gov/study/NCT05162586) | Phase 2 | 完成 | 456 | Enpatoran 用於圓禿症族群的隨機雙盲安慰劑對照劑量探索平行研究 |
| [NCT04680637](https://clinicaltrials.gov/study/NCT04680637) | Phase 2b | 終止 | 168 | Efavaleukin alfa（IL-2 路徑免疫調節劑）用於圓禿症族群的有效性與安全性研究 |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | N/A | 未知 | 20 | 比較 DERMOJET 與傳統注射針用於圓禿症局部類固醇（皮內注射）給藥方式的療效與便利性 |
| [NCT04582136](https://clinicaltrials.gov/study/NCT04582136) | Phase 3 | 進行中 | 146 | Sirolimus 加上背景類固醇治療活躍性自體免疫疾患的 Phase 3 雙盲 RCT，提供類固醇聯合免疫抑制劑的設計參考 |
| [NCT06046534](https://clinicaltrials.gov/study/NCT06046534) | N/A | 完成 | 46 | Anifrolumab 早期使用計畫的回顧性病歷審查，評估真實世界系統性免疫抑制治療的用藥型態與患者經驗 |
| [NCT06653556](https://clinicaltrials.gov/study/NCT06653556) | Early Phase 1 | 招募中 | 34 | LCAR-AIO 用於復發/難治性重度自體免疫疾患的開放標籤安全性、耐受性、PK/PD 探索研究 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32270396](https://pubmed.ncbi.nlm.nih.gov/32270396/) | 2020 | Meta-analysis | Dermatology and Therapy | 系統性回顧 Cyclosporine ± 系統性皮質固醇治療圓禿症，評估不同組合方案的療效與安全性 |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Cohort | Dermatologic Therapy | 26 例廣泛型圓禿症回顧性分析：比較 methylprednisolone 單藥 vs. 合併 methotrexate 的療效 |
| [25566921](https://pubmed.ncbi.nlm.nih.gov/25566921/) | 2015 | Cohort | Indian J Dermatol Venereol Leprol | 靜脈脈衝 methylprednisolone 用於重度圓禿症的臨床療效與安全性評估 |
| [36865845](https://pubmed.ncbi.nlm.nih.gov/36865845/) | 2022 | Cohort | Indian J Dermatology | 回顧性研究：類固醇脈衝療法治療圓禿症的性別差異分析，評估復發與預後因子 |
| [30745958](https://pubmed.ncbi.nlm.nih.gov/30745958/) | 2019 | Cohort | Open Access Macedonian J Med Sci | Methotrexate 合併 mini-pulse methylprednisolone 治療重度圓禿症（含全頭禿、全身禿）的越南臨床經驗 |
| [22426909](https://pubmed.ncbi.nlm.nih.gov/22426909/) | 2012 | Cohort | Saudi Medical Journal | 口服大劑量脈衝 methylprednisolone 用於重度難治性圓禿症：強化療程方案的有效性系列評估 |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatology Practical & Conceptual | 皮質固醇脈衝療法治療圓禿症的療效、復發率、副作用及預後因子綜合文獻回顧 |
| [18608727](https://pubmed.ncbi.nlm.nih.gov/18608727/) | 2008 | Case series | J Dermatological Treatment | Cyclosporine 合併 methylprednisolone 用於重度慢性圓禿症，兼顧療效與控制單藥復發率 |
| [28378336](https://pubmed.ncbi.nlm.nih.gov/28378336/) | 2017 | Review | Int J Dermatology | 全頭禿（AT）與全身禿（AU）治療選項系統性回顧，涵蓋脈衝糖皮質固醇療法的地位評估 |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatric Dermatology | 兒童圓禿症使用脈衝劑量皮質固醇療法（PDCT）的劑量方案、療效與副作用文獻彙整 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部藥陸輸字第000824號 | 甲基培尼皮質醇 | 原料藥（粉） | 抗炎性皮質固醇 |
| 內衛藥輸字第003631號 | 歐巴生結晶性懸濁液注射劑 | 滅菌懸液注射劑 | 風溼性關節炎、骨關節炎、骨膜炎 |
| 內衛藥輸字第003634號 | 歐巴生錠劑 | 錠劑 | 風溼性熱、風溼樣關節炎及過敏性症狀 |
| 內衛藥輸字第003391號 | 歐巴生針劑４０公絲 | 乾粉注射劑 | 急性病症（氣喘、休克、虛脫、過敏性疾患） |

---

## 安全性考量

**藥物交互作用（資料庫共 688 筆，以下列出代表性項目）：**

| 交互藥物 | 等級 | 臨床意義 |
|---------|------|---------|
| Bupropion | **Major** | 合用可能降低癲癇發作閾值，需高度警惕 |
| Clarithromycin | **Major** | CYP3A4 強效抑制劑，可顯著提升 methylprednisolone 血中濃度 |
| Metformin | Moderate | 皮質固醇可拮抗降血糖效果，合用需監測血糖 |
| Acarbose | Moderate | 同上，需監測血糖控制 |
| Pioglitazone | Moderate | 同上，需監測血糖控制 |
| Canagliflozin / Dapagliflozin / Empagliflozin | Moderate | 皮質固醇可降低 SGLT2 抑制劑療效，需加強監測 |
| Amphotericin B | Moderate | 合用增加低鉀血症風險，需監測電解質 |
| Acetylsalicylic acid | Moderate | 合用可能增加消化道潰瘍及出血風險 |

> 完整 688 筆 DDI 清單請查閱 DDInter 資料庫。主要警語、禁忌症及用藥監測詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Methylprednisolone 脈衝療法治療圓禿症已有多項臨床觀察性研究、1 個已完成的 Phase 4 直接試驗（NCT01167946）及 1 篇 meta-analysis 支持，藥物免疫抑制機轉與圓禿症的自體免疫發病路徑高度吻合，生物學合理性充分；加上台灣現有多種劑型（口服錠劑、注射劑）上市，可及性高。

**若要推進需要：**
- 補充 DrugBank MOA 詳細資料（目前為資料缺口），以強化機轉關聯性分析
- 訂定標準化脈衝給藥方案（oral mega-pulse vs. IV pulse：劑量、頻率、療程週數）
- 規劃亞洲族群（含台灣患者）的安全性監測計畫，重點關注：血糖上升、骨質疏鬆、感染風險及腎上腺抑制
- 設計前瞻性觀察研究或隨機對照試驗，以填補 Phase 2/3 RCT 層級的關鍵證據缺口
- 若目標為取得台灣核准適應症，需準備完整有效性與安全性資料，依藥品查驗登記流程提交衛福部審查
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

