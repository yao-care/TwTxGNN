---
layout: default
title: Cabazitaxel
parent: 高證據等級 (L1-L2)
nav_order: 48
evidence_level: L2
indication_count: 1
---

# Cabazitaxel
{: .fs-9 }

證據等級: **L2** | 預測適應症: **1** 個
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

# Cabazitaxel：從去勢抗性前列腺癌到女性乳癌

## 一句話總結

Cabazitaxel（去癌達）是第二代 taxane 類化療藥物，原本核准與 prednisone 併用，治療 docetaxel 治療後仍進展的去勢抗性轉移性前列腺癌。TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效，目前有 **1 個 Phase II RCT** 及 **20 篇文獻**（含多項臨床及臨床前研究）支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 與 prednisone 或 prednisolone 併用，治療去勢抗性轉移性前列腺癌（已接受過 docetaxel 治療者） |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L2 |
| 台灣上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Cabazitaxel 是第二代半合成 taxane 類藥物。作為微管穩定劑，它透過阻止微管去聚合，使腫瘤細胞停滯於有絲分裂的 G2/M 期並誘導細胞凋亡。其最關鍵的藥理特性在於對 P-糖蛋白（MDR1/P-gp）的親和性遠低於 paclitaxel 和 docetaxel，使其能突破 P-gp 過度表現所造成的多重藥物耐藥性（MDR）——這正是它在 docetaxel 失敗後仍能發揮療效的核心機轉。

乳癌是 taxane 類藥物最主要的傳統適應症之一。Paclitaxel 和 docetaxel 早已是早期及轉移性乳癌化療方案的核心成員。同屬 taxane 家族的 cabazitaxel，其機轉對乳癌（尤其是快速增殖的三陰性乳癌）高度合理，且低 P-gp 親和性的特性使其在 taxane 耐藥患者族群中更具潛力。

臨床層面，已有 Phase II RCT（GENEVIEVE 研究，PMID 28768217）直接將 cabazitaxel 與 paclitaxel 比較，評估其作為 HER2 陰性乳癌新輔助化療的病理完全緩解率；另有 Phase I/II 多中心劑量遞增研究（PMID 21339064）評估 cabazitaxel 聯合 capecitabine 用於 taxane 及 anthracycline 治療後復發的轉移性乳癌，均提供了直接的臨床依據，大幅增強預測的可信度。

---

## 臨床試驗證據

ClinicalTrials.gov 查詢（2026-03-04）未檢索到以「female breast carcinoma」為適應症的正式登錄試驗結果，但以下研究已作為文獻發表並包含可供參考的試驗資訊：

| 研究 | 期別 | 族群 | 主要重點 |
|------|------|------|---------|
| GENEVIEVE（PMID 28768217） | Phase II RCT | HER2 陰性乳癌（TNBC 或 Luminal B） | Cabazitaxel vs. paclitaxel 新輔助化療，評估病理完全緩解率 |
| Villanueva 等（PMID 21339064） | Phase I/II | Taxane + anthracycline 後進展的轉移性乳癌 | Cabazitaxel + capecitabine 劑量遞增及療效 |
| Yardley 等（PMID 29678476，NCT01934894） | Phase II | HER2+ 轉移性乳癌合併腦轉移 | Cabazitaxel + lapatinib 穿越血腦屏障的療效 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | RCT | European Journal of Cancer | GENEVIEVE 研究：cabazitaxel vs. paclitaxel 新輔助化療用於 HER2 陰性乳癌，直接比較兩者病理完全緩解率 |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Cohort | European Journal of Cancer | Phase I/II 多中心研究：cabazitaxel + capecitabine 用於 taxane/anthracycline 後復發的轉移性乳癌，評估最大耐受劑量及初步療效 |
| [29678476](https://pubmed.ncbi.nlm.nih.gov/29678476/) | 2018 | Phase II | Clinical Breast Cancer | Cabazitaxel + lapatinib 用於 HER2+ 轉移性乳癌合併腦轉移（NCT01934894），利用 cabazitaxel 穿越血腦屏障的特性 |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | In vitro | Journal for Immunotherapy of Cancer | Cabazitaxel 重塑腫瘤相關巨噬細胞（TAMs），協同 CD47 標靶免疫療法對抗三陰性乳癌（TNBC），提示免疫調節潛力 |
| [38562610](https://pubmed.ncbi.nlm.nih.gov/38562610/) | 2024 | In vitro | International Journal of Nanomedicine | PACA 奈米粒子載 cabazitaxel 在 TNBC PDX 模型中的臨床前療效，並伴隨 M2 巨噬細胞減少 |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | In vitro | Journal of Controlled Release | PEBCA 奈米粒子載 cabazitaxel 在 PDX basal-like 乳癌模型達完全緩解（8 中 6），療效顯著優於游離藥物 |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Review | Molecular Cancer Therapeutics | 使用 MCF-7 乳癌細胞建立 cabazitaxel 耐藥模型，顯示其對 MDR 變體的交叉耐藥倍數遠低於 paclitaxel/docetaxel |
| [26651178](https://pubmed.ncbi.nlm.nih.gov/26651178/) | 2016 | Review | Expert Opinion on Therapeutic Patents | Taxane 類抗癌藥物專利綜述，確認 cabazitaxel 對多種癌症（含乳癌及激素難治性前列腺癌）的適用性 |
| [33247980](https://pubmed.ncbi.nlm.nih.gov/33247980/) | 2021 | Review | British Journal of Clinical Pharmacology | Taxane 類藥物（含 cabazitaxel）藥物動力學與治療藥物濃度監測（TDM）回顧，評估個體化給藥的價值 |
| [30521787](https://pubmed.ncbi.nlm.nih.gov/30521787/) | 2019 | In vitro | Chemistry and Physics of Lipids | Cabazitaxel + thymoquinone 共載脂質球體協同作用，透過 p53、STAT3、Bax/BCL-2、NF-κB 等路徑抑制乳癌腫瘤生長 |

---

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部藥製字第060198號 | "永信"卡巴紫杉醇 | （粉） | 抗腫瘤藥及免疫製劑 |
| 衛署藥輸字第025633號 | 去癌達注射劑 | 注射劑 | 與 prednisone 或 prednisolone 併用治療去勢抗性轉移性前列腺癌且已接受過 docetaxel 治療者 |
| 衛部藥輸字第028989號 | 卡巴瑞德注射劑 | 注射劑 | 與 prednisone 或 prednisolone 併用治療去勢抗性轉移性前列腺癌且已接受過 docetaxel 治療者 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Taxane 類，微管穩定劑） |
| 骨髓抑制風險 | **高**（嗜中性白血球減少症為主要劑量限制毒性，發熱性嗜中性白血球減少症風險顯著） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含分類計數）、肝功能（AST/ALT/膽紅素）、腎功能（肌酸酐）、周邊神經病變評估 |
| 處置防護 | 需依細胞毒性藥物處置規範操作；依 ASCO/ESMO 指引評估是否預防性給予 G-CSF |

---

## 安全性考量

**藥物交互作用（資料庫共計 276 筆，以下列出重大及代表性中度交互作用）：**

| 交互作用藥物 | 嚴重程度 | 臨床意義 |
|-------------|---------|---------|
| Deferiprone | **重大 (Major)** | 鐵螯合劑，可能加重骨髓抑制，骨髓毒性風險疊加 |
| Samarium (153Sm) lexidronam | **重大 (Major)** | 骨靶向放射性藥物，可能嚴重加重骨髓毒性 |
| Clarithromycin | 中度 (Moderate) | CYP3A4 強效抑制劑，可能顯著增加 cabazitaxel 血中濃度 |
| Cobicistat | 中度 (Moderate) | CYP3A4 抑制劑，影響 cabazitaxel 代謝 |
| Simvastatin / Rosuvastatin | 中度 (Moderate) | Statin 類，需監測肌肉毒性風險 |
| Chloroquine | 中度 (Moderate) | 需監測 QTc 間期延長 |
| Aprepitant | 中度 (Moderate) | 止吐藥（NK1 拮抗劑），可能影響 cabazitaxel 藥物動力學 |

> 完整 276 筆交互作用資料請查閱 DDInter 2.0 資料庫及原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Cabazitaxel 的微管穩定機轉與乳癌的藥理關聯性強，已有 Phase II RCT（GENEVIEVE 研究）直接在乳癌患者中評估療效，且其對 P-gp 的低親和性為 taxane 耐藥族群提供了明確的理論優勢。20 篇文獻涵蓋 RCT、Phase I/II 研究、耐藥機轉及臨床前 PDX 模型，整體達 L2 證據等級。

**若要推進需要：**
- 補充完整的 cabazitaxel 作用機轉（MOA）資料（建議查詢 DrugBank API：DB06772）
- 界定目標適應症族群：優先考慮三陰性乳癌（TNBC）或 taxane 治療後復發的轉移性乳癌
- 制定骨髓抑制管理計畫（G-CSF 使用時機、CBC 監測頻率）
- 評估與乳癌常用藥物（如 pembrolizumab、CDK4/6 抑制劑）的交互作用安全性
- 若計畫申請台灣新適應症，需有 Phase II/III 隨機對照試驗資料支持

---

