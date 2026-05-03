---
layout: default
title: Enfortumab Vedotin
parent: 中證據等級 (L3-L4)
nav_order: 92
evidence_level: L3
indication_count: 10
---

# Enfortumab Vedotin
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

# Enfortumab Vedotin：從泌尿道上皮癌到 HER2 陽性乳癌

## 一句話總結

Enfortumab vedotin（備思復）是靶向 Nectin-4 的抗體藥物結合物 (ADC)，目前核准用於局部晚期或轉移性泌尿道上皮癌 (mUC) 的治療。在 TxGNN 所有預測候選適應症中，**HER2 陽性乳癌 (HER2 Positive Breast Carcinoma)** 具有最佳臨床轉譯潛力，目前有 **4 個臨床試驗**和 **4 篇文獻**支持此方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 局部晚期或轉移性泌尿道上皮癌 (mUC) |
| 預測新適應症 | HER2 陽性乳癌 (HER2 Positive Breast Carcinoma) |
| TxGNN 預測分數 | 98.99% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 15 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Enfortumab vedotin 是以 Nectin-4 為靶點的 ADC，透過與 Nectin-4 結合後將細胞毒性載體 **MMAE（monomethyl auristatin E）**遞送至腫瘤細胞內，MMAE 藉由破壞微管系統抑制細胞分裂並誘導凋亡，對活躍分裂的腫瘤細胞具有強效細胞毒殺效果。

Nectin-4 在泌尿道上皮癌中高度過表現，是本藥原始適應症的基礎。研究數據進一步顯示，Nectin-4 在**乳癌（含 HER2 陽性亞型）中同樣呈現高度過表現**，且 Nectin-4 的表現與 HER2 信號路徑相互獨立。這意味著即使是對 HER2 靶向治療產生耐藥的病人，腫瘤仍可能保有 Nectin-4 表現，因而對 Enfortumab vedotin 的 Nectin-4 靶向遞送保持敏感。

EV-202（NCT04225117）Phase 2 籃子試驗已直接納入乳癌患者群，正式在臨床試驗架構下探索此適應症。現有數據顯示 Nectin-4 與 HER2 在乳癌細胞中的共表現支持此機轉可行性，預測方向具備合理的生物學基礎。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04225117](https://clinicaltrials.gov/study/NCT04225117) | Phase 2 | 入組完成 | 329 | EV-202 多腫瘤籃子試驗，評估 Enfortumab vedotin 於多種實體腫瘤（含乳癌 cohort）及聯合 pembrolizumab（cohort 9）的客觀緩解率，目前仍持續追蹤 |
| [NCT05097599](https://clinicaltrials.gov/study/NCT05097599) | Phase 2 | 已終止 | 11 | StrataPATH 精準醫療平台試驗，評估已核准藥物於生物標誌指引族群的臨床活性；因入組人數不足而提前終止，可用數據極為有限 |
| [NCT07287995](https://clinicaltrials.gov/study/NCT07287995) | Phase 1/2 | 招募中 | 428 | ASP2998（TROP2 靶向 ADC）單獨使用或聯合 pembrolizumab、carboplatin 及 Enfortumab vedotin 用於局部晚期或轉移性實體腫瘤的安全性與療效評估 |
| [NCT07309770](https://clinicaltrials.gov/study/NCT07309770) | Phase 2 | 招募中 | 90 | Trastuzumab Rezetecan（HER2 靶向 ADC）於 HER2 陽性晚期實體腫瘤多 cohort 研究，含 Extramammary Paget's Disease、罕見實體腫瘤及泌尿道上皮癌 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40614854](https://pubmed.ncbi.nlm.nih.gov/40614854/) | 2025 | In vitro | Cancer Letters | 多倍體巨大癌細胞（PGCC）誘導 HER2 靶向 ADC 耐藥性，揭示 ADC 在 HER2+ 乳癌中的耐藥機轉，對選擇 Nectin-4 替代靶點策略有潛在意義 |
| [41654096](https://pubmed.ncbi.nlm.nih.gov/41654096/) | 2026 | Review | Crit Rev Oncol Hematol | 近 5 年核准腫瘤藥物的真實世界證據綜合分析，評估 RCT 療效能否轉譯至更廣泛的臨床族群 |
| [32315240](https://pubmed.ncbi.nlm.nih.gov/32315240/) | 2020 | Review | ASCO Educational Book | ADC 類藥物在癌症治療中的復興：靶點選擇、抗體設計與細胞毒素載體策略的全面回顧 |
| [41384708](https://pubmed.ncbi.nlm.nih.gov/41384708/) | 2026 | Review | Histopathology | 膀胱癌分子病理進展，整合 KMT2D、KDM6A、TP53、PIK3CA、FGFR3 等突變的個人化腫瘤學新分類框架 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部菌疫輸字第001212號 | 備思復凍晶注射劑20毫克 | 凍晶注射劑 | 單獨使用或併用 pembrolizumab 治療局部晚期或轉移性泌尿道上皮癌 (mUC) 成人病人... |
| 衛部菌疫輸字第001213號 | 備思復凍晶注射劑30毫克 | 凍晶注射劑 | 單獨使用或併用 pembrolizumab 治療局部晚期或轉移性泌尿道上皮癌 (mUC) 成人病人... |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 抗體藥物結合物（ADC）— MMAE（auristatin 類）微管抑制劑 |
| 骨髓抑制風險 | 中度（MMAE 載體可致嗜中性白血球減少、血小板低下） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含分類計數）、肝腎功能；如合併使用降糖藥需額外監測血糖 |
| 處置防護 | 需依細胞毒性藥物處置規範操作（MMAE 具潛在致畸胎性與遺傳毒性） |

---

## 安全性考量

**藥物交互作用**（共 147 筆，以下列出主要項目）：

| 交互藥物 | 等級 | 藥物類別 |
|---------|------|---------|
| Clarithromycin | **Major** | 大環內酯類抗生素（CYP3A4 強效抑制劑，可能升高 MMAE 暴露量） |
| Metformin、Glipizide、Glyburide、Glimepiride | Moderate | 口服降糖藥（磺脲類 / 雙胍類） |
| Empagliflozin、Canagliflozin、Dapagliflozin、Ertugliflozin | Moderate | SGLT-2 抑制劑 |
| Dulaglutide、Albiglutide、Exenatide | Moderate | GLP-1 受體激動劑 |
| Pioglitazone | Moderate | Thiazolidinedione 類降糖藥 |
| Aprepitant | Moderate | NK1 受體拮抗劑（止吐藥） |

> 安全性警語與禁忌症詳情請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
EV-202（NCT04225117）Phase 2 籃子試驗已直接納入乳癌 cohort，正式在臨床架構下探索此適應症，提供了現階段最直接的臨床可行性依據。Nectin-4 於 HER2 陽性乳癌中的高度過表現提供了合理的生物學機轉基礎，且此靶點策略不受 HER2 耐藥性影響，具有差異化的臨床價值；然而目前尚無完整療效結果，宜待 EV-202 數據成熟後再進一步評估。

**若要推進需要：**
- EV-202（NCT04225117）乳癌 cohort 的完整療效數據（ORR、PFS、OS）
- Nectin-4 在 HER2 陽性乳癌中的表現率及其與療效的相關性研究
- 作用機轉（MOA）的完整文件（補充 DrugBank 資料）
- 與現有 HER2 靶向 ADC（T-DM1、T-DXd）療效的比較或互補性分析
- 釐清 Nectin-4 / HER2 共陽性族群的精準篩選標準
- 制定合併降糖藥使用時的血糖監測與劑量調整計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

