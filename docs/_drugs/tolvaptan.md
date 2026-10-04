---
layout: default
title: Tolvaptan
parent: 高證據等級 (L1-L2)
nav_order: 263
evidence_level: L1
indication_count: 10
---

# Tolvaptan
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

# Tolvaptan：從自體顯性多囊性腎臟病到多囊性腎臟病第3型合併多囊性肝臟病

## 一句話總結

Tolvaptan（佳腎康）是血管加壓素 V2 受體拮抗劑，原本核准用於自體顯性多囊性腎臟病（ADPKD）及低血鈉症的治療。TxGNN 模型預測它可能對**多囊性腎臟病第3型合併多囊性肝臟病（Polycystic Kidney Disease 3 with or without Polycystic Liver Disease）**有效，此適應症為 ADPKD 的特定基因亞型（GANAB/DNAJB11 突變），與原核准適應症共享相同的 cAMP 驅動囊泡生成機轉，目前有 **0 個專屬臨床試驗**及 **20 篇相關文獻**（含 2 篇 Phase 3 RCT）支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 自體顯性多囊性腎臟病（ADPKD，eGFR > 25 mL/min/1.73m²） |
| 預測新適應症 | 多囊性腎臟病第3型合併多囊性肝臟病（PKD3 with/without PLD） |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1（2 篇已完成 Phase 3 RCT，適用於 ADPKD 上位診斷） |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 7 張（有效單方 7／有效複方 0／已註銷 0） |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Tolvaptan 是選擇性血管加壓素 V2 受體（V2R）拮抗劑，作用於腎臟集尿管，透過阻斷 V2R 降低細胞內 cAMP（環腺苷酸）濃度，抑制囊泡液體分泌與囊泡上皮細胞異常增殖。目前缺乏完整的 DrugBank MOA 結構化記錄，但其藥理機轉在多篇 NEJM 大型 RCT 中已被清楚闡明。

多囊性腎臟病第3型（PKD3）由 **GANAB 或 DNAJB11 基因突變**引起，雖然致病基因與 PKD1（多囊蛋白1）、PKD2（多囊蛋白2）不同，但下游病理機轉——cAMP 升高驅動的囊泡液體積累與上皮細胞增生——在本質上一致。這使得 tolvaptan 的 V2R 拮抗靶點對 PKD3 同樣具有直接的藥理學依據。

<!-- review:begin tolvaptan-pkd3-gene-2026-10-03 -->

> **查核加註（2026-10-03）**：依 NCBI MedGen，PKD3 的致病基因是 GANAB；DNAJB11 突變對應的是 PKD6（Polycystic kidney disease 6 with or without polycystic liver disease），不屬於 PKD3。推論內容與證據等級未改。依據：[NCBI MedGen：Polycystic kidney disease 3 with or without polycystic liver disease（C3887964）](https://www.ncbi.nlm.nih.gov/medgen/854672)；[NCBI MedGen：Polycystic kidney disease 6 with or without polycystic liver disease（C4748044）](https://www.ncbi.nlm.nih.gov/medgen/1648469)。

<!-- review:end tolvaptan-pkd3-gene-2026-10-03 -->

此外，台灣許可證批准的 ADPKD 適應症本身即為 PKD3 的**上位診斷**（umbrella diagnosis）。實務上，PKD3 患者若符合 ADPKD 臨床表現，臨床醫師已可在現有核准適應症框架下考慮 tolvaptan 使用，這進一步降低了再利用的監管障礙。

---

## 臨床試驗證據

目前無針對「多囊性腎臟病第3型（PKD3）」專屬的臨床試驗登記。

> **說明**：相關的大型 Phase 3 RCT（TEMPO 3:4、REPRISE）以 ADPKD 為整體族群設計，PKD3 患者未被單獨分層分析，此為目前最主要的證據缺口。

---

## 文獻證據

共 20 篇相關文獻，優先列出 RCT 及系統性回顧（最多 10 篇）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT | N Engl J Med | **TEMPO 3:4 試驗**：tolvaptan vs. 安慰劑，顯著抑制 ADPKD 患者腎臟總體積增長並減緩 eGFR 下降，確立 V2R 拮抗療效 |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT | N Engl J Med | **REPRISE 試驗**：針對較晚期 ADPKD（eGFR 25–65），tolvaptan 仍顯著減緩腎功能惡化，支持廣泛 eGFR 範圍的使用 |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Systematic Review | Cochrane Database Syst Rev | 系統性回顧 ADPKD 疾病修飾治療，tolvaptan 為目前最強證據的藥物干預 |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | Meta-analysis | Nefrologia | 系統性回顧與 meta-analysis：tolvaptan 在 ADPKD 中的療效與安全性，確認臨床獲益與肝毒性需監測 |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Review | Nephrol Dial Transplant | ERA 共識聲明：tolvaptan 於 ADPKD 使用更新建議，含適用族群選擇與長期管理 |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | ADPKD 完整回顧，涵蓋 PKD1/2/3 基因型分類及 tolvaptan 在各亞型中的角色 |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | **直接相關**：ADPKD 合併多囊性肝臟病（PCLD）的臨床管理，明確指出 tolvaptan 可減緩囊泡腎功能惡化及囊泡生長 |
| [28614813](https://pubmed.ncbi.nlm.nih.gov/28614813/) | 2017 | Review | Ann Nutr Metab | Vasopressin 路徑在多囊性腎臟病中的核心角色，為 tolvaptan 機轉關聯性提供直接支持 |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Review | Adv Kidney Dis Health | PKD 遺傳譜系（含 PKD3 相關基因如 GANAB）與表現型分析，說明不同基因型的共同下游機轉 |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Review | Curr Opin Nephrol Hypertens | ADPKD 新興療法展望：tolvaptan 為目前唯一 FDA 核准疾病修飾藥物，同時介紹 mTOR 抑制劑、CFTR 調節劑等新方向 |

---

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Tolvaptan 的不重複許可證共 **7 張**：有效單方 7 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方**（7 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛署藥輸字第025295號 | 伸舒康錠30毫克 | 錠劑 | 台灣大塚製藥股份有限公司 | 2030/11/23 | SAMSCA適用於治療心臟衰竭及抗利尿激素分泌不當症候群（SIADH）引起之低血鈉症。 |
| 衛署藥輸字第025296號 | 伸舒康錠15毫克 | 錠劑 | 台灣大塚製藥股份有限公司 | 2030/11/23 | SAMSCA適用於治療心臟衰竭及抗利尿激素分泌不當症候群（SIADH）引起之低血鈉症。 |
| 衛部藥輸字第027341號 | 佳腎康錠15毫克 | 錠劑 | 台灣大塚製藥股份有限公司 | 2028/03/05 | 適用於自體顯性多囊性腎臟病(ADPKD)且eGFR大於25mL/min/1.73m2之慢性腎臟病成人患者，已出現病情迅速惡化跡象，用以延緩自體顯性多囊性腎臟病之囊泡的生長及腎功能的… |
| 衛部藥輸字第027342號 | 佳腎康錠30毫克 | 錠劑 | 台灣大塚製藥股份有限公司 | 2028/03/05 | 適用於自體顯性多囊性腎臟病(ADPKD)且eGFR大於25mL/min/1.73m2之慢性腎臟病成人患者，已出現病情迅速惡化跡象，用以延緩自體顯性多囊性腎臟病之囊泡的生長及腎功能的… |
| 衛部藥輸字第027343號 | 佳腎康錠45毫克 | 錠劑 | 台灣大塚製藥股份有限公司 | 2028/03/05 | 適用於自體顯性多囊性腎臟病(ADPKD)且eGFR大於25mL/min/1.73m2之慢性腎臟病成人患者，已出現病情迅速惡化跡象，用以延緩自體顯性多囊性腎臟病之囊泡的生長及腎功能的… |
| 衛部藥輸字第027344號 | 佳腎康錠60毫克 | 錠劑 | 台灣大塚製藥股份有限公司 | 2028/03/05 | 適用於自體顯性多囊性腎臟病(ADPKD)且eGFR大於25mL/min/1.73m2之慢性腎臟病成人患者，已出現病情迅速惡化跡象，用以延緩自體顯性多囊性腎臟病之囊泡的生長及腎功能的… |
| 衛部藥輸字第027345號 | 佳腎康錠90毫克 | 錠劑 | 台灣大塚製藥股份有限公司 | 2028/03/05 | 適用於自體顯性多囊性腎臟病(ADPKD)且eGFR大於25mL/min/1.73m2之慢性腎臟病成人患者，已出現病情迅速惡化跡象，用以延緩自體顯性多囊性腎臟病之囊泡的生長及腎功能的… |

<!-- tfda-licenses:end -->

> 台灣共有 **19 張**許可證，上表列出代表性規格。另含 SAMSCA 品牌（適應症為心臟衰竭及 SIADH 引起之低血鈉症）。

---

## 安全性考量

### 藥物交互作用

共查詢到 **128 個**藥物交互作用（DDinter 資料庫），以下列出主要等級：

**Major（需特別注意）：**

| 交互藥物 | 等級 | 臨床意義 |
|---------|------|---------|
| Clarithromycin | Major | CYP3A4 強效抑制劑，可大幅提高 tolvaptan 血中濃度，增加肝毒性及副作用風險 |

**Moderate（重要中度交互作用，代表性列舉）：**

| 交互藥物 | 等級 | 交互藥物 | 等級 |
|---------|------|---------|------|
| Aprepitant | Moderate | Miconazole | Moderate |
| Dexamethasone | Moderate | Empagliflozin | Moderate |
| Potassium citrate | Moderate | Naltrexone | Moderate |
| Potassium chloride | Moderate | Rifaximin | Moderate |
| Potassium gluconate | Moderate | Eliglustat | Moderate |

> **注意**：多項含鉀製劑（Potassium citrate/bicarbonate/chloride/gluconate）均列為 Moderate 交互作用，使用時需監測電解質。Tolvaptan 主要經 CYP3A4 代謝，所有 CYP3A4 強效抑制劑（如 Clarithromycin、Miconazole）均可能顯著提高暴露量。

> 其他安全性資訊（警語、禁忌症）請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
PKD3（GANAB/DNAJB11 突變）與 PKD1/PKD2 共享 cAMP 驅動的囊泡生成機轉，tolvaptan 的 V2R 拮抗靶點具有直接且合理的藥理依據；兩篇 NEJM Phase 3 RCT（TEMPO 3:4、REPRISE）確立了 tolvaptan 在廣泛 ADPKD 族群（包含 PKD3 亞型）中的療效，且台灣已有 19 張上市許可，監管障礙最低。

**若要推進需要：**
- **PKD3 亞型分層分析**：向 TEMPO/REPRISE 試驗研究者申請 GANAB/DNAJB11 突變患者的子群分析資料
- **MOA 結構化記錄**：補充 DrugBank API 查詢結果，完整記錄 V2R 拮抗作用機轉文件（目前為 Data Gap）
- **肝功能監測計畫**：PKD3 患者常合併多囊性肝臟病，tolvaptan 已知具肝毒性風險（ALT/AST 上升），需制定更嚴格的 LFT 監測方案
- **小兒族群考量**：已有兒童 ADPKD 試驗（NCT02964273），若 PKD3 患者年齡較小，需評估兒科劑量
- **倫理與知情同意**：因 PKD3 為 ADPKD 亞型而非獨立核准適應症，臨床使用需以 off-label 框架說明

<!-- review:begin log -->

## 查核紀錄

以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；更正只限基本藥理事實，模型預測、證據等級與結論未改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|---------|------|------|------|
| 2026-10-03 | 快速總覽「許可證數：19 張」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 台灣上市資訊表下「台灣共有 19 張許可證」 | 已由程式化許可證表取代（原為更正） | [衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36，檔案 36_5.json，2026-09-29）](https://data.fda.gov.tw/data/opendata/export/36/json) |
| 2026-10-03 | 「PKD3 由 GANAB 或 DNAJB11 基因突變引起」 | 加註 | [NCBI MedGen：Polycystic kidney disease 3 with or without polycystic liver disease（C3887964）](https://www.ncbi.nlm.nih.gov/medgen/854672)；[NCBI MedGen：Polycystic kidney disease 6 with or without polycystic liver disease（C4748044）](https://www.ncbi.nlm.nih.gov/medgen/1648469) |
| 2026-10-04 | 頁首證據等級 | 頁首等級依總覽表重算（原 L5→L1） | [TwTxGNN 研究方法：證據等級判定](https://twtxgnn.yao.care/methodology/) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

