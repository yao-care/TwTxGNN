---
layout: default
title: Larotrectinib
parent: 中證據等級 (L3-L4)
nav_order: 151
evidence_level: L3
indication_count: 10
---

# Larotrectinib
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

The txgnn-pipeline skill covers pipeline management; the report format is fully defined in the system prompt. Proceeding to generate the report from the Evidence Pack.

---

# Larotrectinib：從 NTRK 融合實體腫瘤 到 多發性內分泌腺瘤病

## 一句話總結

Larotrectinib（維泰凱）是第一代選擇性 TRK 激酶抑制劑，原本以「腫瘤不可知（tumor-agnostic）」方式核准用於具 NTRK 基因融合的實體腫瘤。
TxGNN 模型預測它可能對**多發性內分泌腺瘤病（Multiple Endocrine Neoplasia, MEN）**有效，
目前有 **1 個臨床試驗**和 **2 篇文獻**提供間接支持。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 具 NTRK 基因融合之轉移性實體腫瘤（成人及兒童，無後天阻抗性突變） |
| 預測新適應症 | 多發性內分泌腺瘤病（Multiple Endocrine Neoplasia） |
| TxGNN 預測分數 | 99.24% |
| 證據等級 | L3 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Larotrectinib 詳細的作用機轉原始資料。根據已知資訊，Larotrectinib 是高度選擇性的 TRK 激酶抑制劑，可抑制 NTRK1、NTRK2、NTRK3 基因融合所產生的異常 TRK 融合蛋白，進而阻斷腫瘤細胞的增殖與存活訊號（MAPK/ERK 及 PI3K/AKT 路徑）。其核准機制為「腫瘤不可知」，亦即療效由基因驅動突變決定，而非由腫瘤組織起源決定。

多發性內分泌腺瘤病（MEN）是一群遺傳性內分泌腫瘤症候群。其中 MEN2 型主要由 **RET** 基因突變驅動（甲狀腺髓樣癌），但 MEN 譜系中的**乳突狀甲狀腺癌**亞型已有文獻記載可攜帶 **NTRK 基因融合**。此外，MEN1 型胰臟神經內分泌腫瘤等也屬實體腫瘤範疇，理論上亦可能出現 NTRK 融合事件。

因此，TxGNN 的預測邏輯具一定生物合理性：若 MEN 相關腫瘤攜帶 NTRK 融合，Larotrectinib 即可透過其 tumor-agnostic 機轉發揮作用。然而，MEN 族群中 NTRK 融合的實際盛行率仍屬未知，目前尚無直接針對 MEN 患者的臨床試驗，屬需進一步探索的研究假說。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | 招募結束・進行中 | 6,452 | NCI-MATCH 跨瘤種籃型試驗，含 NTRK1/2/3 融合臂（Arm Z1A），可能納入 MEN 相關實體腫瘤；惟試驗設計並非針對 MEN，為間接相關 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31322645](https://pubmed.ncbi.nlm.nih.gov/31322645/) | 2019 | Review | Endocrine Reviews | 甲狀腺癌標靶治療综述；涵蓋 NTRK 融合在乳突狀甲狀腺癌（MEN 相關亞型）的角色，及 TRK 抑制劑的臨床應用 |
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | In vitro | NPJ Precision Oncology | RET TKI（selpercatinib）治療甲狀腺髓樣癌（MTC）耐藥機轉分析；NTRK 融合作為替代致癌訊號的潛在意義，與 MEN2 相關 MTC 間接相關 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部藥輸字第027746號 | 維泰凱 20毫克/毫升口服溶液 | 口服液劑 | 適用於有NTRK 基因融合的實體腫瘤之成人和兒童病人，須符合：具融合且無後天阻抗性突變、轉移性或手術風險高、無合適替代治療... |
| 衛部藥輸字第027747號 | 維泰凱 膠囊25毫克 | 膠囊劑 | 適用於有NTRK 基因融合的實體腫瘤之成人和兒童病人，須符合：具融合且無後天阻抗性突變、轉移性或手術風險高、無合適替代治療... |
| 衛部藥輸字第027748號 | 維泰凱 膠囊100毫克 | 膠囊劑 | 適用於有NTRK 基因融合的實體腫瘤之成人和兒童病人，須符合：具融合且無後天阻抗性突變、轉移性或手術風險高、無合適替代治療... |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | **標靶藥物**（TRK 激酶選擇性抑制劑，非傳統細胞毒性化療） |
| 骨髓抑制風險 | **低**（標靶機轉，較傳統化療骨髓毒性低；偶見白血球/中性球輕度下降） |
| 致吐性分級 | **低**（口服標靶藥物，致吐性低） |
| 監測項目 | CBC（含分類）、ALT/AST（肝功能）、神經系統評估（TRK 訊號與神經發育相關）、體重與生長指標（兒童族群） |
| 處置防護 | 依口服抗腫瘤藥物（Oral Antineoplastic）處置規範操作；孕婦照護者需注意接觸防護 |

---

## 安全性考量

**藥物交互作用（共 427 筆，以下列出主要項目）：**

| 交互藥物 | 嚴重程度 | 備註 |
|---------|---------|------|
| Clarithromycin | **Major（重大）** | 強效 CYP3A4 抑制劑，可能顯著升高 Larotrectinib 血中濃度 |
| Omeprazole | Moderate（中度） | CYP2C19 抑制，潛在藥動學交互作用 |
| Dexamethasone | Moderate（中度） | CYP3A4 誘導，可能降低 Larotrectinib 療效 |
| Hydrocortisone | Moderate（中度） | CYP3A4 誘導，同類影響 |
| Betamethasone | Moderate（中度） | CYP3A4 誘導，同類影響 |
| Budesonide | Moderate（中度） | CYP3A4 誘導，同類影響 |
| Aprepitant | Moderate（中度） | CYP3A4 調節劑，影響程度視劑量而定 |
| Cisapride | Moderate（中度） | 潛在 QT 延長風險，需特別留意 |

> 其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測具一定生物合理性（MEN 相關腫瘤可攜帶 NTRK 融合），但目前僅有一個 NCI-MATCH 跨瘤種間接試驗與兩篇間接相關的回顧文獻，尚無針對 MEN 族群的直接臨床證據；在 MEN 中 NTRK 融合盛行率未明前，此預測仍屬假說階段。

**若要推進需要：**
- 盤查 MEN 患者腫瘤組織的 NTRK 融合盛行率（分子流行病學資料）
- 確認 NCI-MATCH Arm Z1A 中是否有 MEN 相關亞型患者的亞組分析
- 補充 Larotrectinib 完整 MOA 資料（DrugBank API 查詢）
- 評估 MEN 患者接受 TRK 抑制劑的安全性，尤其是兒童族群的神經發育影響
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

