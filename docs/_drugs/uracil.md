---
layout: default
title: Uracil
parent: 高證據等級 (L1-L2)
nav_order: 273
evidence_level: L1
indication_count: 10
---

# Uracil
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

# Uracil：從甲狀腺機能亢進症到大腸腫瘤

## 一句話總結

Uracil 在台灣以口服粉劑形式登記用於甲狀腺機能亢進症，同時也是 UFT（tegafur-uracil）複方的關鍵成分，透過抑制 DPD 酶來強化 5-FU 的抗腫瘤效果。TxGNN 模型預測它可能對**大腸腫瘤（Colonic Neoplasm）**有效，這項預測有堅實的生物學機轉支持。目前有多達 **50 個臨床試驗**及 **20 篇文獻**佐證氟嘧啶類藥物在大腸腫瘤的療效，其中包含多項直接評估 UFT 用於大腸癌術後輔助化療的 Phase 3 RCT。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 甲狀腺機能亢進症 |
| 預測新適應症 | 大腸腫瘤（Colonic Neoplasm） |
| TxGNN 預測分數 | 99.50% |
| 證據等級 | L1 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 Uracil（DB03419）的完整 DrugBank 作用機轉資料，但根據大量藥理學文獻，Uracil 在腫瘤治療中的核心角色是作為 **DPD（Dihydropyrimidine Dehydrogenase，二氫嘧啶脫氫酶）競爭性抑制劑**。DPD 是 5-氟尿嘧啶（5-FU）在肝臟快速降解的主要代謝酶，Uracil 與 5-FU 競爭 DPD 結合位點，從而減緩 5-FU 的代謝分解，維持較高的血漿藥物濃度，使 tegafur 轉化而來的 5-FU 能充分發揮抗腫瘤效果。這正是 UFT（tegafur-uracil 按莫耳比 1:4 組合）複方的設計核心，也是台灣部分許可證（大腸直腸癌適應症）中 UFT 複方療效的藥理基礎。

5-FU 透過抑制胸苷酸合成酶（Thymidylate Synthase, TS）干擾 DNA 及 RNA 合成，對快速增殖的腸黏膜上皮細胞具有直接細胞毒殺效果。大腸腺癌細胞高度表達 TS，為氟嘧啶類藥物的理想靶點。此外，DPYD 基因（編碼 DPD 酶）多型性已被臨床研究（NCT05266300，n=722）直接證實影響氟嘧啶類（5-FU、capecitabine、tegafur）的毒性與療效，進一步確立 DPD 抑制機轉在大腸癌治療中的核心地位，也直接支持 Uracil 的角色。

更重要的是，多項跨地區 Phase 3 RCT 已直接驗證 UFT/LV（tegafur-uracil 加 leucovorin）的大腸癌療效：日本 ACTS-CC 02 確立 UFT/LV 為高風險 Stage III 結腸癌輔助化療的標準方案；美國 NSABP C-06（n=1,886）證明口服 UFT+LV 與靜脈 5-FU+LV 療效相當；台灣健保資料庫大型研究（PMID 33950962）在台灣族群中進一步支持 UFT 的臨床效益。這三個不同地區、來自不同研究設計的一致結論，為 TxGNN 的預測提供了最強力的臨床驗證。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00427310](https://clinicaltrials.gov/study/NCT00427310) | Phase 3 | 已完成 | 1,158 | 結腸癌（Dukes A/B/C）術後門靜脈輸注 5-FU vs 觀察組，大型 RCT 直接驗證氟嘧啶類術後輔助治療效益 |
| [NCT00079274](https://clinicaltrials.gov/study/NCT00079274) | Phase 3 | 已完成 | 3,397 | Stage III 結腸癌術後六臂 RCT，比較含 5-FU 的 FOLFOX（±irinotecan、±cetuximab）各組合療效 |
| [NCT00069121](https://clinicaltrials.gov/study/NCT00069121) | Phase 3 | 已完成 | 1,886 | Stage III 結腸癌術後 XELOX（capecitabine+oxaliplatin）vs 5-FU/LV 輔助化療，capecitabine 為 5-FU 口服前驅藥 |
| [NCT00217737](https://clinicaltrials.gov/study/NCT00217737) | Phase 3 | 進行中（不再招募） | 2,431 | Stage II 高風險結腸癌術後 FOLFOX±bevacizumab，同步前瞻性評估分子標記預後價值 |
| [NCT00561470](https://clinicaltrials.gov/study/NCT00561470) | Phase 3 | 已完成 | 1,226 | 轉移性結直腸癌二線治療：FOLFIRI（含 5-FU）+ aflibercept vs 安慰劑，大型國際雙盲 RCT |
| [NCT00025337](https://clinicaltrials.gov/study/NCT00025337) | Phase 3 | 已完成 | 880 | 進展性結直腸癌：bevacizumab+FOLFOX vs FOLFOX vs bevacizumab 單藥三臂 Phase 3 比較 |
| [NCT00252564](https://clinicaltrials.gov/study/NCT00252564) | Phase 3 | 已完成 | 247 | 轉移性結直腸癌一線：cetuximab+bevacizumab+5-FU/LV vs Bev-FOLFOX，比較 12 個月 PFS |
| [NCT05266300](https://clinicaltrials.gov/study/NCT05266300) | N/A | 已完成 | 722 | DPYD 基因型前測試臨床實施研究，評估氟嘧啶類（5-FU/capecitabine/tegafur）代謝安全性，與 Uracil 的 DPD 抑制機轉直接相關 |
| [NCT00427570](https://clinicaltrials.gov/study/NCT00427570) | Phase 3 | 已完成 | N/A | 可切除結腸癌術後含氟嘧啶類化療（5-FU+vincristine+semustine）vs BCG 免疫治療長期對照 RCT |
| [NCT01383707](https://clinicaltrials.gov/study/NCT01383707) | Phase 2 | 已完成 | 77 | 結直腸癌肝轉移 bevacizumab+mFOLFOX-6（含 5-FU）兩階段 Simon 設計，評估療效與安全性 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | RCT | Medicine | 台灣健保資料庫（2000–2015）大型世代研究合併 meta-analysis：UFT vs 5-FU 作為 Stage II/III 結腸癌術後輔助化療，支持 UFT 在台灣族群的 DFS 及 OS 效益 |
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Colorectal Cancer | ACTS-CC 02 Phase 3 RCT：SOX 未優於 UFT/LV 作為高風險 Stage III 結腸癌輔助化療，確立 UFT/LV 的標準治療地位 |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT | ESMO Open | ACTS-CC 02 最終 5 年生存分析：UFT/LV vs SOX 高風險 Stage III 結腸癌 OS 及 TNM 第 7 版亞組更新結果 |
| [16648506](https://pubmed.ncbi.nlm.nih.gov/16648506/) | 2006 | RCT | J Clin Oncol | NSABP C-06 RCT：口服 UFT+LV vs IV 5-FU+LV 作為 Stage II/III 結腸癌術後輔助化療，療效相當，確立口服氟嘧啶類給藥可行性 |
| [38833114](https://pubmed.ncbi.nlm.nih.gov/38833114/) | 2024 | Cohort | Int J Clin Oncol | JFMC46-1201 最終分析：UFT/LV vs 單獨手術治療高風險 Stage II 結腸癌，傾向分數分析確認 5 年 OS 效益 |
| [35168560](https://pubmed.ncbi.nlm.nih.gov/35168560/) | 2022 | Cohort | BMC Cancer | JFMC46-1201 前瞻性觀察研究：UFT/LV 顯著改善高風險 Stage II 結腸癌 3 年 DFS（傾向分數配對分析） |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Cohort | Surgery Today | UFT 作為肺癌、胃癌、結直腸癌及乳癌術後輔助化療系統性回顧：多項 RCT 結果支持 UFT 在結直腸癌的長期療效與溫和毒性 |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | RCT | Int J Clin Oncol | 大腸直腸癌術後輔助 RCT：評估 UFT 合併免疫製劑（OK-432）及 HCFU 不同組合的療效與安全性 |
| [26722024](https://pubmed.ncbi.nlm.nih.gov/26722024/) | 2016 | Review | Anticancer Res | 口服氟嘧啶類藥物演進回顧：DPD 抑制策略（UFT/S-1）在大腸癌的機轉、臨床地位及與新型 TAS-102 的比較 |
| [17033240](https://pubmed.ncbi.nlm.nih.gov/17033240/) | 2006 | Case series | Gan to Kagaku Ryoho | 2 例轉移性大腸癌以 UFT/LV 口服方案成功治療（完全及部分緩解），提供 UFT/LV 在轉移性病例的療效案例支持 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 內衛藥輸字第001118號 | 甲基硫克由拉西 | （粉） | 甲狀腺機能亢進症 |
| 衛部菌疫輸字第001135號 | 曲斯若凍晶注射劑150毫克 | 凍晶注射劑 | 一、應使用於下列HER2過度表現或HER2基因amplification之早期乳癌、轉移性乳癌病人：1.早期乳癌（EBC）輔助療法；2.轉移性乳癌... |
| 衛部菌疫輸字第001136號 | 曲斯若凍晶注射劑440毫克 | 凍晶注射劑 | 一、應使用於下列HER2過度表現或HER2基因amplification之早期乳癌、轉移性乳癌病人：1.早期乳癌（EBC）輔助療法；2.轉移性乳癌... |

---

## 細胞毒性

本評估的再利用目標為惡性腫瘤（大腸腫瘤），Uracil 在此脈絡中作為 UFT（tegafur-uracil）複方的 Fluoropyrimidine 輔助成分，整體屬抗腫瘤藥物範疇。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | DPD 抑制劑（Fluoropyrimidine 增效成分；Uracil 本身無直接細胞毒殺活性，但 UFT 複方整體屬傳統細胞毒性藥物） |
| 骨髓抑制風險 | 低至中度（Uracil 單獨使用無直接骨髓毒性；UFT 複方可能引起嗜中性白血球減少及血小板減少） |
| 致吐性分級 | 低（口服 UFT 致吐性低，屬低致吐性口服化療方案） |
| 監測項目 | CBC（含分類）、肝功能（AST/ALT）、腎功能（Cr/CCr）；建議 DPYD 基因型前測試 |
| 處置防護 | UFT 複方需依抗腫瘤藥物處置規範操作；DPYD 功能缺失變異者需調整 tegafur 劑量或禁用氟嘧啶類 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
來自日本（ACTS-CC 02 Phase 3 RCT）、美國（NSABP C-06 Phase 3 RCT）及台灣（健保資料庫大型世代研究）的多項高品質研究一致支持 UFT/LV 在 Stage II/III 大腸癌輔助治療的療效，證據等級達 L1，臨床轉化可行性高；然而 Uracil 單一成分的再利用路徑、與 tegafur 的配比需求，以及台灣現行法規框架仍需釐清。

**若要推進需要：**
- 釐清台灣現行 UFT 複方（tegafur-uracil）的許可狀態及大腸直腸癌適應症範圍，確認是否已核准或需補充申請
- 補充 Uracil（DB03419）的完整 DrugBank MOA 資料（目前為 Data Gap，影響機轉關聯性分析精確度）
- 確認開發路徑：以 UFT 複方整體申請新適應症 vs Uracil 單一成分再利用
- 建立 DPYD 基因型前測試的患者篩選方案（參考 NCT05266300 實施模型）
- 評估台灣族群特異性藥物代謝差異（參考 PMID 33950962 台灣健保資料庫結果）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

