---
layout: default
title: Trabectedin
parent: 僅模型預測 (L5)
nav_order: 286
evidence_level: L5
indication_count: 1
monitor_inn: "Trabectedin"
predicted_indications: ["female breast carcinoma"]
last_modified_at: 2026-10-16
description: "Trabectedin：預測新適應症為女性乳癌 (Female Breast Carcinoma)（證據等級 L2）。原適應症：無法切除或轉移性脂肪肉瘤 (liposarcoma) 或平滑肌肉瘤 (leiomyosarcoma)…"
---

# Trabectedin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Trabectedin：從脂肪肉瘤／平滑肌肉瘤到女性乳癌
{: .text-alpha }

## 一句話總結

Trabectedin 原本用於治療曾接受 anthracycline 療程、無法切除或轉移性的脂肪肉瘤與平滑肌肉瘤。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效，
目前有 **1 個臨床試驗**和 **20 篇文獻**支持這個方向，其中包含數項針對乳癌的 Phase 2 研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無法切除或轉移性脂肪肉瘤 (liposarcoma) 或平滑肌肉瘤 (leiomyosarcoma)，且曾接受一種含 anthracycline 療程的病人 |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 0.9973 |
| 證據等級 | L5 |
| 台灣上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效單方 1／有效複方 0／已註銷 0） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏來自 DrugBank 的詳細作用機轉資料，但根據本報告彙整的文獻，Trabectedin 會結合 DNA 小溝，並干擾轉錄偶聯的核苷酸切除修復 (transcription-coupled nucleotide excision repair)，造成 DNA 雙股斷裂。它也會減少腫瘤相關巨噬細胞 (TAM)，進而調節腫瘤微環境。

這個機轉與乳癌有合理的連結。同源重組缺陷 (HR-deficient) 的腫瘤，例如 BRCA 突變者，對 Trabectedin 特別敏感；而三陰性乳癌 (TNBC) 的免疫抑制性骨髓細胞，也可能成為其調節微環境作用的標的。文獻指出，Trabectedin 在 BRCA1/2 種系突變的轉移性乳癌中已有 Phase 2 研究，臨床前研究也顯示它能增強 IL-12 在三陰性乳癌中的抗腫瘤效果。

原適應症（軟組織肉瘤）與乳癌的相似性目前尚無明確評估，因此這項預測較偏向以機轉為基礎的假說，尚需臨床資料驗證。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00786838](https://clinicaltrials.gov/study/NCT00786838) | Phase 2 | 完成 | 76 | 單盲、安慰劑對照的 QT 間期研究，評估單次給予 Trabectedin 對晚期實體腫瘤病人心電圖 QT/QTc 的影響；屬安全性研究，並非乳癌專屬的療效試驗 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25239225](https://pubmed.ncbi.nlm.nih.gov/25239225/) | 2014 | Phase 2 | Clin Breast Cancer | 多中心隨機 Phase 2 研究，比較兩種給藥方案，評估 Trabectedin 單藥用於 anthracycline 與 taxane 治療後晚期乳癌的療效與安全性 |
| [24692579](https://pubmed.ncbi.nlm.nih.gov/24692579/) | 2014 | Phase 2 | Ann Oncol | 評估 Trabectedin 用於 BRCA1/2 種系突變、已接受過治療的轉移性乳癌的療效與安全性 |
| [27266804](https://pubmed.ncbi.nlm.nih.gov/27266804/) | 2016 | Phase 2 | Clin Breast Cancer | 依 XPG 基因表現，評估 Trabectedin 用於 HR 陽性、HER2 陰性晚期乳癌的療效 |
| [19114300](https://pubmed.ncbi.nlm.nih.gov/19114300/) | 2009 | Phase 1 | Eur J Cancer | Trabectedin 合併 doxorubicin 用於晚期軟組織肉瘤與乳癌的可行性及藥動學研究（38 位病人，其中 9 位為乳癌） |
| [26592307](https://pubmed.ncbi.nlm.nih.gov/26592307/) | 2016 | Review | Expert Opin Investig Drugs | 回顧 Trabectedin 用於乳癌的機轉與潛力，包括減少腫瘤相關巨噬細胞的作用 |
| [27710871](https://pubmed.ncbi.nlm.nih.gov/27710871/) | 2016 | Review | Cancer Treat Rev | 探討 Trabectedin 作為 BRCA 缺陷病人化療選項的角色 |
| [18410797](https://pubmed.ncbi.nlm.nih.gov/18410797/) | 2008 | Review | Semin Oncol | 回顧 anthracycline 及 taxane 難治性轉移性乳癌的新興藥物 |
| [19496709](https://pubmed.ncbi.nlm.nih.gov/19496709/) | 2009 | Review | Expert Rev Anticancer Ther | 回顧 Trabectedin 在軟組織肉瘤的應用，並提及其在卵巢癌與乳癌的單藥活性；常見毒性為血液學與肝臟毒性 |
| [39777457](https://pubmed.ncbi.nlm.nih.gov/39777457/) | 2025 | 動物研究 | Cancer Immunol Res | Trabectedin 可增強 IL-12 對三陰性乳癌的抗腫瘤效果 |
| [24941346](https://pubmed.ncbi.nlm.nih.gov/24941346/) | 2014 | 細胞研究 | Eur Cytokine Netw | Trabectedin 對乳癌細胞株及血管內皮細胞具抗血管新生作用 |
| [23792433](https://pubmed.ncbi.nlm.nih.gov/23792433/) | 2013 | 細胞研究 | Toxicol Lett | Trabectedin 在不同基因型的乳癌細胞株中誘導細胞凋亡的情形不同 |

## 台灣上市資訊

<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->

### 台灣許可證（依 TFDA 資料集自動產生）

依衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）（檔案日期 2026-09-29），主成分含 Trabectedin 的不重複許可證共 **1 張**：有效單方 1 張、有效複方 0 張、已註銷 0 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。資料來源：[TFDA 開放資料](https://data.fda.gov.tw/data/opendata/export/36/json)。

**有效・單方（截至資料集日期 2026-09-29）**（1 張）

| 許可證字號 | 品名 | 劑型 | 申請商 | 有效日期 | 核准適應症 |
|------|------|------|------|------|------|
| 衛部藥輸字第027370號 | "友待" 凍晶注射劑1毫克 | 凍晶注射劑 | 台灣東洋藥品工業股份有限公司 | 2028/01/09 | 適用於治療患有無法切除或轉移性脂肪肉瘤(liposarcoma)或平滑肌肉瘤(leiomyosarcoma)，且曾接受一種含anthracycline療程的病人。 |

<!-- tfda-licenses:end -->

<!-- TFDA_LICENSE_TABLE -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（海洋來源的 DNA 結合型烷化類抗腫瘤藥物） |
| 骨髓抑制風險 | 中至高（文獻指出約 50% 病人出現 3–4 級嗜中性白血球減少，約 20% 出現血小板減少） |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | CBC（含分類）、肝功能（文獻指出毒性以血液學與肝臟為主） |
| 處置防護 | 請參考原廠仿單，並依細胞毒性藥物處置規範操作 |

## 安全性考量

- **藥物交互作用**：本報告彙整的資料顯示共有 450 筆潛在交互作用。其中被列為 **Major** 的包括 Clarithromycin；其餘多為 Moderate，例如 Aprepitant、Dexamethasone、Cimetidine、Metronidazole、Levofloxacin、Simvastatin、Rosuvastatin 等。使用時須留意併用藥物，尤其是會影響肝臟代謝酵素的藥物。
- **心臟安全性**：已有專門的 QT 間期研究（NCT00786838、PMID 21739119），可作為心電圖安全性評估的參考。

其餘警語與禁忌症資料不足，請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有數項針對乳癌的 Phase 2 研究（含 BRCA1/2 突變族群與 anthracycline／taxane 治療後的晚期乳癌），機轉上也有合理依據，TxGNN 分數很高（0.9973）。但缺乏已完成的 Phase 3 RCT，且唯一登記的臨床試驗屬 QT 安全性研究，並非乳癌療效試驗，因此證據等級為 L2，宜在限定族群與嚴格監測下推進。

**若要推進需要：**
- 取得並確認各 Phase 2 乳癌研究的主要療效數據（反應率、無惡化存活期），並與現行標準治療比較
- 鎖定最可能受益的族群（如 BRCA1/2 突變、HR 缺陷或三陰性乳癌）
- 補充 DrugBank 的作用機轉資料及原廠仿單的警語與禁忌症
- 規劃骨髓抑制與肝毒性的監測計畫，並審視與 CYP3A4 相關藥物（如 Clarithromycin）的併用風險
- 評估是否需設計前瞻性的隨機對照試驗，以取得更高等級的證據

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

