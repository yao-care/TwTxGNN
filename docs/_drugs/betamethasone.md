---
layout: default
title: Betamethasone
parent: 高證據等級 (L1-L2)
nav_order: 42
evidence_level: L1
indication_count: 10
---

# Betamethasone
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Betamethasone：從皮膚炎到圓禿 (Alopecia Areata)

## 一句話總結

Betamethasone（臨得隆錠）是強效合成糖皮質激素，原本廣泛用於皮膚炎、濕疹、風濕病及自體免疫疾病的抗炎治療。
TxGNN 模型預測它可能對**圓禿 (Alopecia Areata)** 有效，
目前有 **7 個臨床試驗**和 **20 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 原發性腎上腺皮質機能不全症（安迪生氏病）、風濕熱、關節風濕症、全身性紅斑狼瘡、支氣管氣喘、腎病、濕疹、皮膚炎、藥疹 |
| 預測新適應症 | 圓禿 (Alopecia Areata) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L1 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Betamethasone 是強效合成糖皮質激素，其作用機轉與圓禿的核心病理直接對應。根據現有機轉資料，Betamethasone 透過結合糖皮質激素受體，強力抑制 **CD8+ T 細胞**介導的毛囊自體免疫攻擊，並下調 IFN-γ、IL-2 等促炎細胞因子的表達。

圓禿（Alopecia Areata）的發病核心是 T 細胞入侵毛囊「免疫豁免區」（immune privilege zone），造成毛囊週期停滯而引發非瘢痕性脫髮。這正是糖皮質激素受體路徑可直接介入的靶點，使機轉推論具有充分的科學合理性。

Betamethasone 原有的皮膚炎與自體免疫適應症，與圓禿同屬皮膚免疫失調疾患；且 Betamethasone 已在臨床實踐中透過**局部塗抹**、**病灶內注射**及**口服 mini-pulse** 等多種途徑應用於圓禿，對應台灣現有的多元劑型（錠劑、軟膏、懸液注射劑），進一步支持了 TxGNN 預測的合理性。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02350023](https://clinicaltrials.gov/study/NCT02350023) | Phase 4 | 完成 | 50 | 隨機比較局部 betamethasone 與 latanoprost 於局限性圓禿的療效與安全性，為局部皮質類固醇治療圓禿的頭對頭比較 |
| [NCT06786689](https://clinicaltrials.gov/study/NCT06786689) | Phase 2 | 完成 | 60 | 直接比較 betamethasone 口服 mini-pulse（BOMP）與 azathioprine 週脈衝療法治療中至重度圓禿之療效 |
| [NCT03535233](https://clinicaltrials.gov/study/NCT03535233) | Phase 4 | 完成 | 40 | 強效局部皮質類固醇聯合 minoxidil 5% 對比病灶內三安西諾龍注射於圓禿的隨機對照試驗 |
| [NCT06087796](https://clinicaltrials.gov/study/NCT06087796) | Phase 1 | 狀態不明 | 60 | 以 betamethasone valerate 0.1% 霜為主動對照，比較 pentoxifylline 2% 及 metformin 10% 凝膠治療斑塊型圓禿 |
| [NCT05803070](https://clinicaltrials.gov/study/NCT05803070) | N/A | 狀態不明 | 59 | 評估並比較局部 cetirizine 1% 與局部 betamethasone valerate 0.1% 治療局限性圓禿之療效與安全性 |
| [NCT04207931](https://clinicaltrials.gov/study/NCT04207931) | Phase 4 | 招募中 | 250 | 中心性離心性瘢痕性脫髮（CCCA）多中心前瞻性治療結果研究，皮質類固醇應用具間接參考價值 |
| [NCT01111981](https://clinicaltrials.gov/study/NCT01111981) | Phase 4 | 狀態不明 | 30 | clobetasol propionate 0.05% 泡沫劑於中心性離心性瘢痕性脫髮的安全性與療效，提供同類藥物的間接機轉佐證 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Meta-analysis | Cochrane Database Syst Rev | 圓禿治療網絡統合分析，含免疫抑制劑、生長刺激劑及接觸免疫療法的全面比較，為類固醇療效定位提供最高等級證據 |
| [39393548](https://pubmed.ncbi.nlm.nih.gov/39393548/) | 2025 | RCT | J Am Acad Dermatol | 微針透皮給藥複方 betamethasone 於圓禿之隨機對照試驗，驗證新型給藥途徑可達病灶內注射相近療效且減少疼痛 |
| [38623137](https://pubmed.ncbi.nlm.nih.gov/38623137/) | 2024 | RCT | Cureus | 比較局部 betamethasone dipropionate 與 minoxidil 於圓禿患者之療效，提供兩種一線外用藥的直接比較數據 |
| [34400956](https://pubmed.ncbi.nlm.nih.gov/34400956/) | 2021 | RCT | Iran J Pharm Res | 雙盲安慰劑對照 RCT（36 例重度圓禿），比較口服 betamethasone pulse、methotrexate 及二者聯合之療效 |
| [36114868](https://pubmed.ncbi.nlm.nih.gov/36114868/) | 2023 | RCT | Arch Dermatol Res | 評估分段 CO₂ 雷射單獨或聯合 betamethasone valerate 霜治療圓禿的療效與安全性（30 例患者） |
| [36257912](https://pubmed.ncbi.nlm.nih.gov/36257912/) | 2022 | RCT | Dermatol Ther | 多組盲法 RCT（108 例），比較 latanoprost、minoxidil 及 betamethasone 單用與組合用於圓禿的療效與患者滿意度 |
| [40510104](https://pubmed.ncbi.nlm.nih.gov/40510104/) | 2025 | RCT | Cureus | 非盲隨機平行對照試驗（60 例），比較口服 cyclosporine 與 betamethasone mini-pulse 治療圓禿的療效與安全性 |
| [40519428](https://pubmed.ncbi.nlm.nih.gov/40519428/) | 2025 | Cohort | Cureus | 口服 betamethasone mini-pulse 治療中至重度圓禿的療效與安全性世代研究，評估復發率與長期耐受性 |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatol Pract Conceptual | 皮質類固醇脈衝療法（含 betamethasone 方案）於圓禿的療效、復發率、副作用及預後因子的系統性回顧 |
| [28521549](https://pubmed.ncbi.nlm.nih.gov/28521549/) | 2018 | — | J Dermatol Treat | 比較局部 latanoprost 與 minoxidil 及 betamethasone valerate 治療圓禿的療效，提供多藥物比較的臨床數據 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 內衛藥製字第004123號 | 臨得隆錠 | 錠劑 | 原發性腎上腺皮質機能不全症（安迪生氏病）、風濕熱、關節風濕症、全身性紅斑狼瘡、支氣管氣喘、腎病、濕疹、皮膚炎、藥疹 |
| 內衛藥輸字第000938號 | 纈草酸倍他美素松 | （粉） | 濕疹，皮膚疾患 |
| 內衛藥輸字第000939號 | 磷酸二鈉倍他美素松 | （粉） | 抗炎症 |
| 內衛藥輸字第000947號 | 必乃膚通－Ｎ藥膏 | 軟膏劑 | 牛皮癬、嬰兒濕疹、雍滯等各類型濕疹、外耳炎、神經皮膚炎、皮脂溢出 |
| 內衛藥輸字第003941號 | 臨得隆懸濁液 | 滅菌懸液注射劑 | 慢性關節炎、骨關節炎、滑液囊炎、腱鞘炎 |

---

## 安全性考量

**藥物交互作用（資料庫共收錄 451 筆，以下列出代表性案例）：**

| 交互藥物 | 嚴重程度 |
|---------|---------|
| Adalimumab | 重度（Major）|
| Ibuprofen | 中度（Moderate）|
| Ketorolac | 中度（Moderate）|
| Isotretinoin | 中度（Moderate）|
| Nifedipine | 中度（Moderate）|
| Ethinylestradiol | 中度（Moderate）|
| Acarbose | 中度（Moderate）|
| Fluvoxamine | 中度（Moderate）|
| Formoterol | 輕度（Minor）|
| Salbutamol | 輕度（Minor）|

> 警語、禁忌症及完整藥物交互作用清單請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
圓禿的核心病理機制（T 細胞毛囊免疫攻擊）與 Betamethasone 糖皮質激素機轉直接對應，多項已完成的 Phase 2/4 隨機對照試驗及 Cochrane 統合分析均支持其療效；台灣現有多種劑型（口服、外用、注射），具備局部與全身應用的完整臨床基礎，可依嚴重度分層使用。

**若要推進需要：**
- 補充正式 MOA 文件（DrugBank API 查詢），以強化機轉分析的完整性
- 針對不同疾病嚴重度（局限型 vs. 全禿/普禿）制定最佳給藥途徑與劑量方案
- 建立長期安全性監測計畫，特別關注系統性使用的 HPA 軸抑制、血糖影響及骨質流失風險
- 評估與台灣現行皮膚科圓禿治療（JAK 抑制劑核准後）的定位整合與競爭優勢
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

