---
layout: default
title: Dupilumab
parent: 中證據等級 (L3-L4)
nav_order: 89
evidence_level: L3
indication_count: 10
---

# Dupilumab
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

# Dupilumab：從異位性皮膚炎到支氣管炎

## 一句話總結

Dupilumab 原本用於治療中至重度異位性皮膚炎、氣喘及慢性鼻竇炎合併鼻息肉。
TxGNN 模型預測它可能對**支氣管炎 (bronchitis)** 有效，
目前有 **1 個臨床試驗**和 **多篇文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 異位性皮膚炎、氣喘、慢性鼻竇炎合併鼻息肉、嗜伊紅性食道炎 |
| 預測新適應症 | 支氣管炎 (bronchitis) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L3 |
| 台灣上市 | 已上市 |
| 許可證數 | 2 張（有效單方 2／有效複方 0／已註銷 0） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Dupilumab 是一種全人類（human）IgG4 單株抗體，可阻斷 IL-4 和 IL-13 的訊號傳遞，
這兩種細胞因子是第二型發炎反應的關鍵介質。支氣管炎，特別是嗜酸性支氣管炎，
涉及類似的發炎機轉。Dupilumab 已核准用於嗜酸性白血球表現型的氣喘，
其對下呼吸道發炎的抑制作用可能延伸至支氣管炎的治療。

<!-- review:begin dupilumab-human-antibody-2026-10-03 -->

> **查核更正（2026-10-03）**：原寫「Dupilumab 是一種人源化單株抗體」。仿單載明 dupilumab 是全人類（human）IgG4 單株抗體，不是人源化（humanized）抗體；它與 IL-4、IL-13 受體共用的 IL-4Rα 次單元結合而抑制兩者的訊號。本次只更正這個藥理事實，推論與結論未改。依據：[DailyMed：DUPIXENT（dupilumab）injection 美國仿單 §12.1](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=595f437d-2729-40bb-9c62-c8ece1f82780)。

<!-- review:end dupilumab-human-antibody-2026-10-03 -->

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | COMPLETED | 33 | 評估 dupilumab 在無鼻息肉的慢性鼻竇炎患者的療效 |
| [NCT03346434](https://clinicaltrials.gov/study/NCT03346434) | Phase 2/3 | COMPLETED | 202 | 評估 dupilumab 在 6 個月至 6 歲異位性皮膚炎兒童的藥動學和療效 |
| [NCT01949311](https://clinicaltrials.gov/study/NCT01949311) | Phase 3 | COMPLETED | 2733 | Dupilumab 在異位性皮膚炎成人患者的長期安全性研究 |
| [NCT04287621](https://clinicaltrials.gov/study/NCT04287621) | N/A | ACTIVE_NOT_RECRUITING | 718 | RAPID 登記研究：氣喘患者使用 dupilumab 的真實世界數據 |
| [NCT02277769](https://clinicaltrials.gov/study/NCT02277769) | Phase 3 | COMPLETED | 708 | 確認 dupilumab 單藥治療中至重度異位性皮膚炎的療效 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | RCT extension | Lancet Respir Med | TRAVERSE 研究：dupilumab 在中至重度氣喘的長期安全性和療效 |
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Meta-analysis | J Asthma | Dupilumab 在控制不佳氣喘的療效和安全性系統性回顧 |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Case report | Pediatr Pulmonol | Dupilumab 用於兒童嗜酸性塑型性支氣管炎的新療法 |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | 吸菸相關氣道疾病合併氣喘的治療挑戰 |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Clinical study | Chest | 抗 T2 生物製劑治療對類固醇依賴型氣喘肺通氣的影響 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Dupilumab 的不重複許可證共 **2 張**：有效單方 2 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部菌疫輸字第001082號 | 杜避炎注射劑300毫克 | 預充填式注射劑 | 賽諾菲股份有限公司 | 2028/05/10 | 1、異位性皮膚炎：可用於治療患有中度至重度異位性皮膚炎且對局部處方治療控制不佳或不適合使用該療法的成人病人及6個月以上的兒童病人。可併用或不併用局部皮質類固醇治療。 2、氣喘：可作… |
| 衛部菌疫輸字第001133號 | 杜避炎注射劑200毫克 | 預充填式注射劑 | 賽諾菲股份有限公司 | 2030/07/20 | 1. 異位性皮膚炎：可用於治療患有中度至重度異位性皮膚炎且對局部處方治療控制不佳或不適合使用該療法的成人病人及6個月以上的兒童病人。可併用或不併用局部皮質類固醇治療。 2. 氣喘：… |

<!-- tfda-licenses:end -->

## 安全性考量

- **常見不良反應**：注射部位反應、結膜炎、口唇皰疹
- **重要注意事項**：開始治療前應評估寄生蟲感染，不建議與活病毒疫苗同時使用
- **特殊族群**：兒童使用需按體重調整劑量

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Dupilumab 抑制 IL-4/IL-13 的機轉適用於嗜酸性發炎相關的支氣管炎，
已有病例報告支持其在嗜酸性塑型性支氣管炎的療效。需區分支氣管炎的亞型。

**若要推進需要：**
- 區分嗜酸性與非嗜酸性支氣管炎的生物標記
- 針對慢性支氣管炎患者的前瞻性臨床試驗
- 與 COPD 合併嗜酸性白血球增高患者的治療效益評估

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「Dupilumab 是一種人源化單株抗體」 | 更正 | [DailyMed：DUPIXENT（dupilumab）injection 美國仿單 §12.1](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=595f437d-2729-40bb-9c62-c8ece1f82780) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

