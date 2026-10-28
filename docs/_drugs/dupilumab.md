---
layout: default
title: Dupilumab
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 9
monitor_inn: "Dupilumab"
predicted_indications: ["bronchitis", "acne keloid", "exanthem (disease)", "neonatal dermatomyositis", "acrodermatitis chronica atrophicans", "amyopathic dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "hydroa vacciniforme, familial", "severe nonproliferative diabetic retinopathy"]
last_modified_at: 2026-10-27
description: "Dupilumab：預測新適應症為支氣管炎 (bronchitis)（證據等級 L5）。原適應症：1. 異位性皮膚炎：可用於治療患有中度至重度異位性皮膚炎且對局部處方治療控制不佳或不適合使用該療法的成人病人及6個月以上的兒童病人。可併用…"
---

# Dupilumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Dupilumab：IL-4Rα 單株抗體 → 支氣管炎 (bronchitis)
{: .text-alpha }

## 一句話總結

Dupilumab 是一種阻斷 IL-4 受體 α 次單位的單株抗體，可抑制 IL-4/IL-13 的第 2 型發炎訊號。
TxGNN 模型預測它可能對**支氣管炎 (bronchitis)** 有效。
目前有 **1 個相關臨床試驗**（針對相鄰疾病，並非支氣管炎本身）和 **11 篇文獻**，但沒有任何研究直接針對一般支氣管炎，證據屬於模型預測層級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 1. 異位性皮膚炎：可用於治療患有中度至重度異位性皮膚炎且對局部處方治療控制不佳或不適合使用該療法的成人病人及6個月以上的兒童病人。可併用或不併用局部皮質類固醇治療。 ２.氣喘：可作為6歲以上患有嗜伊紅性白血球表現型或口服皮質類固醇依賴型之中度至重度氣喘病人，在已接受中劑量或高劑量吸入性皮質類固醇(ICS)及第2種控制藥物(如，LABA, LTRA, LAMA或methylxanthines)治療，或單獨接受高劑量ICS治療，仍有氣喘控制不佳現象時的附加維持治療(add-on maintenance therapy)。 ３.慢性鼻竇炎合併鼻息肉：可作為患有慢性鼻竇炎合併鼻息肉(CRSwNP)之 |
| 預測新適應症 | 支氣管炎 (bronchitis) |
| TxGNN 預測分數 | 0.9992 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效單方 2／有效複方 0／已註銷 0） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供）。就已知的藥理特性，dupilumab 阻斷 IL-4Rα，抑制 IL-4/IL-13 驅動的第 2 型發炎，這類發炎與嗜伊紅性氣道發炎及黏液栓塞有關。

因此，在嗜伊紅性氣道疾病（如氣喘、慢性阻塞性肺病）以及嗜伊紅性塑型性支氣管炎的個案報告中，可看到此機轉被討論。但一般支氣管炎多為感染性或吸菸相關的嗜中性發炎，並非以第 2 型發炎為主，因此機轉上的適用性有限。

必須強調：目前沒有任何研究直接評估 dupilumab 用於一般支氣管炎。現有資料僅支持相鄰的嗜伊紅性氣道疾病，不能直接推論至支氣管炎。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | 完成 | 33 | 以隨機、雙盲、安慰劑對照設計評估 dupilumab 用於無鼻息肉的慢性鼻竇炎；屬不同疾病，僅反映上、下呼吸道第 2 型發炎的共通機轉 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | 統合分析 | J Asthma | 彙整隨機對照試驗，評估 dupilumab 用於未控制氣喘的安全性與療效 |
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | 世代研究 | Lancet Respir Med | TRAVERSE 開放標籤延伸研究，評估中重度氣喘的長期安全性與療效 |
| [42617837](https://pubmed.ncbi.nlm.nih.gov/42617837/) | 2026 | 世代研究 | Chest | 配對調整間接比較：mepolizumab 與 dupilumab 在嗜伊紅性 COPD 減少急性惡化上無顯著差異 |
| [42839285](https://pubmed.ncbi.nlm.nih.gov/42839285/) | 2026 | 世代研究 | Respir Res | 德國多中心真實世界資料，探討 dupilumab 用於 COPD |
| [42511891](https://pubmed.ncbi.nlm.nih.gov/42511891/) | 2026 | 世代研究 | Biomedicines | 12 例第 2 型發炎 COPD 的恩慈使用病例系列，涵蓋以慢性支氣管炎表現型為主的older 病人 |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | 回顧 | Pediatr Pulmonol | 嗜伊紅性兒童塑型性支氣管炎的新療法回顧 |
| [42773542](https://pubmed.ncbi.nlm.nih.gov/42773542/) | 2026 | 回顧 | Eur J Clin Invest | COPD 從發炎路徑到標靶治療的處置進展 |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | 回顧 | Tuberc Respir Dis | 預防 COPD 急性惡化的藥物治療綜述 |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | 回顧 | Expert Opin Pharmacother | 氣喘合併吸菸相關氣道疾病（含慢性支氣管炎）的處置挑戰 |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | 世代研究 | Chest | 以 MRI 評估抗第 2 型生物製劑對類固醇依賴型氣喘肺通氣的影響 |
| [41672525](https://pubmed.ncbi.nlm.nih.gov/41672525/) | 2026 | 病例報告 | Intern Med | 兩例嗜伊紅性細支氣管炎經 dupilumab 等生物製劑成功治療 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Dupilumab 的不重複許可證共 **2 張**：有效單方 2 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（2 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部菌疫輸字第001082號 | 杜避炎注射劑300毫克 | 預充填式注射劑 | 賽諾菲股份有限公司 | 2028/05/10 | 1、異位性皮膚炎：可用於治療患有中度至重度異位性皮膚炎且對局部處方治療控制不佳或不適合使用該療法的成人病人及6個月以上的兒童病人。可併用或不併用局部皮質類固醇治療。 2、氣喘：可作… |
| 衛部菌疫輸字第001133號 | 杜避炎注射劑200毫克 | 預充填式注射劑 | 賽諾菲股份有限公司 | 2030/07/20 | 1. 異位性皮膚炎：可用於治療患有中度至重度異位性皮膚炎且對局部處方治療控制不佳或不適合使用該療法的成人病人及6個月以上的兒童病人。可併用或不併用局部皮質類固醇治療。 2. 氣喘：… |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 安全性考量

- **藥物交互作用**：資料庫共記錄 53 項交互作用，其中較需留意的重度（Major）項目包括 adalimumab、baricitinib、certolizumab pegol 與 cladribine；中度項目包括 warfarin、roflumilast、cyclosporine、azathioprine、denosumab 等；鋅鹽類（醋酸鋅、葡萄糖酸鋅、硫酸鋅、氯化鋅）為輕度。

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何已列出的研究直接針對一般支氣管炎，現有資料僅涉及氣喘、COPD、鼻竇炎等相鄰疾病，因此證據等級只能判定為 L5，僅為模型預測。
- 一般支氣管炎多非第 2 型發炎驅動，機轉上的支持度有限。

**若要推進需要：**
- 補齊詳細的作用機轉資料
- 界定可能受益的次族群（如嗜伊紅性支氣管炎、第 2 型發炎的慢性支氣管炎表現型），並針對該族群設計研究
- 取得直接以支氣管炎為對象的臨床或前瞻性觀察研究證據
- 評估與免疫抑制劑等藥物併用時的交互作用風險

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 「Dupilumab 是一種人源化單株抗體」 | 報告重生後已無此錯誤（2026-10-15：新報告未再稱 dupilumab 為人源化抗體；原為更正） | [DailyMed：DUPIXENT（dupilumab）injection 美國仿單 §12.1](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=595f437d-2729-40bb-9c62-c8ece1f82780) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

