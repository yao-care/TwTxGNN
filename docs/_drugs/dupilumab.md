---
layout: default
title: Dupilumab
description: "Dupilumab 的老藥新用潛力分析。中等證據等級 L3，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 中證據等級 (L3-L4)
nav_order: 64
evidence_level: L3
indication_count: 10
---

# Dupilumab

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L3</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Dupilumab：從異位性皮膚炎到支氣管炎

## 一句話總結

<p class="key-answer" data-question="Dupilumab 可以用於治療什麼新適應症？">
Dupilumab 原本用於治療中至重度異位性皮膚炎、氣喘及慢性鼻竇炎合併鼻息肉。
TxGNN 模型預測它可能對**支氣管炎 (bronchitis)** 有效，
目前有 **1 個臨床試驗**和 **多篇文獻**支持這個方向。
</p>

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 異位性皮膚炎、氣喘、慢性鼻竇炎合併鼻息肉、嗜伊紅性食道炎 |
| 預測新適應症 | bronchitis、皮膚炎、acne keloid、exanthem (disease)、neonatal dermatomyositis、acrodermatitis chronica atrophicans、amyopathic dermatomyositis、secondary interstitial lung disease specific to childhood associated with a connective tissue disease、hydroa vacciniforme, familial、atopic eczema |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L3 |
| 台灣上市 | 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. bronchitis</span>
<span class="evidence-badge evidence-L3">L3</span>
<span class="prediction-score">99.92%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content" markdown="1">

### 為什麼這個預測合理？

<p class="key-answer" data-question="這個藥物的作用機轉是什麼？">
Dupilumab 是一種人源化單株抗體，可阻斷 IL-4 和 IL-13 的訊號傳遞，
這兩種細胞因子是第二型發炎反應的關鍵介質。支氣管炎，特別是嗜酸性支氣管炎，
涉及類似的發炎機轉。Dupilumab 已核准用於嗜酸性白血球表現型的氣喘，
其對下呼吸道發炎的抑制作用可能延伸至支氣管炎的治療。
</p>

<div class="key-takeaway">
此預測基於藥物的作用機轉，與現有臨床證據方向一致。
</div>

### 臨床試驗

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | COMPLETED | 33 | 評估 dupilumab 在無鼻息肉的慢性鼻竇炎患者的療效 |
| [NCT03346434](https://clinicaltrials.gov/study/NCT03346434) | Phase 2/3 | COMPLETED | 202 | 評估 dupilumab 在 6 個月至 6 歲異位性皮膚炎兒童的藥動學和療效 |
| [NCT01949311](https://clinicaltrials.gov/study/NCT01949311) | Phase 3 | COMPLETED | 2733 | Dupilumab 在異位性皮膚炎成人患者的長期安全性研究 |
| [NCT04287621](https://clinicaltrials.gov/study/NCT04287621) | N/A | ACTIVE_NOT_RECRUITING | 718 | RAPID 登記研究：氣喘患者使用 dupilumab 的真實世界數據 |
| [NCT02277769](https://clinicaltrials.gov/study/NCT02277769) | Phase 3 | COMPLETED | 708 | 確認 dupilumab 單藥治療中至重度異位性皮膚炎的療效 |

### 相關文獻

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | RCT extension | Lancet Respir Med | TRAVERSE 研究：dupilumab 在中至重度氣喘的長期安全性和療效 |
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Meta-analysis | J Asthma | Dupilumab 在控制不佳氣喘的療效和安全性系統性回顧 |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Case report | Pediatr Pulmonol | Dupilumab 用於兒童嗜酸性塑型性支氣管炎的新療法 |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | 吸菸相關氣道疾病合併氣喘的治療挑戰 |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Clinical study | Chest | 抗 T2 生物製劑治療對類固醇依賴型氣喘肺通氣的影響 |

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. dermatitis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.71%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.71%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. acne keloid</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.61%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.61%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. exanthem (disease)</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.57%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.57%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. neonatal dermatomyositis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.56%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.56%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. acrodermatitis chronica atrophicans</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.54%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.54%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. amyopathic dermatomyositis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.53%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.53%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. secondary interstitial lung disease specific to childhood associated with a connective tissue disease</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.52%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.52%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. hydroa vacciniforme, familial</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.50%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.50%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. severe nonproliferative diabetic retinopathy</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.10%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.10%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 2 張許可證 | 杜避炎注射劑300毫克 | 注射劑 | 異位性皮膚炎、氣喘、慢性鼻竇炎合併鼻息肉、嗜伊紅性食道炎、COPD、慢性自發性蕁麻疹 |

## 安全性考量

- **常見不良反應**：注射部位反應、結膜炎、口唇皰疹
- **重要注意事項**：開始治療前應評估寄生蟲感染，不建議與活病毒疫苗同時使用
- **特殊族群**：兒童使用需按體重調整劑量


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**Helminthiasis** 🟡 Moderate
- 請參閱 DDInter 2.0 了解詳情。

**Vision Disorders** 🟡 Moderate
- 需密切監測。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Dupilumab 抑制 IL-4/IL-13 的機轉適用於嗜酸性發炎相關的支氣管炎，
已有病例報告支持其在嗜酸性塑型性支氣管炎的療效。需區分支氣管炎的亞型。

**若要推進需要：**
- 區分嗜酸性與非嗜酸性支氣管炎的生物標記
- 針對慢性支氣管炎患者的前瞻性臨床試驗
- 與 COPD 合併嗜酸性白血球增高患者的治療效益評估

---

## 相關藥物報告

- [Acitretin]({{ "/drugs/acitretin/" | relative_url }}) - 證據等級 L3
- [Propantheline]({{ "/drugs/propantheline/" | relative_url }}) - 證據等級 L3
- [Human Immunoglobulin G]({{ "/drugs/human_immunoglobulin_g/" | relative_url }}) - 證據等級 L3
- [Alfacalcidol]({{ "/drugs/alfacalcidol/" | relative_url }}) - 證據等級 L3
- [Dorzolamide]({{ "/drugs/dorzolamide/" | relative_url }}) - 證據等級 L3

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Dupilumab老藥新用驗證報告. https://twtxgnn.yao.care/drugs/dupilumab/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_dupilumab,
  title = {Dupilumab老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/dupilumab/}
}
```

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>最後審核：2026-02-20 | 審核者：TwTxGNN Research Team</small>
</div>

{% include giscus.html %}
