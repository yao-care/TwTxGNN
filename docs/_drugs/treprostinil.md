---
layout: default
title: Treprostinil
description: "Treprostinil 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
---

# Treprostinil

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Treprostinil：從肺動脈高壓到相關併發症

## 一句話總結

<p class="key-answer" data-question="Treprostinil 可以用於治療什麼新適應症？">
Treprostinil (勵脈展素) 原本用於治療特發性或遺傳性肺動脈高壓。
TxGNN 模型預測它可能對**多種肺動脈高壓相關疾病**有效，
其中**結締組織疾病相關肺動脈高壓**有最強的臨床證據支持。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 特發性或遺傳性肺動脈高壓 (WHO functional class III/IV) |
| 預測新適應症 | pulmonary arteriovenous malformation (disease)、pulmonary arterial hypertension、pulmonary arterial hypertension associated with congenital heart disease、pulmonary arterial hypertension associated with HIV infection、pulmonary arterial hypertension associated with chronic hemolytic anemia、pulmonary arterial hypertension associated with connective tissue disease、pulmonary arterial hypertension associated with schistosomiasis、hypotrichosis simplex of the scalp、congenital hypotrichosis milia、malformation syndrome with odontal and/or periodontal component |
| TxGNN 最高預測分數 | 99.70% (肺動靜脈畸形) |
| 證據等級 | L2 (結締組織疾病相關 PAH) |
| 台灣上市 | 已上市 |
| 許可證數 | 25 張 |
| 建議決策 | Proceed with Guardrails |

## 預測新適應症一覽

| 疾病名稱 | TxGNN 分數 | 臨床試驗 | 文獻數 |
|---------|-----------|---------|-------|
| 肺動靜脈畸形 | 99.70% | 0 | 0 |
| 先天性心臟病相關 PAH | 99.60% | 2 | 20+ |
| HIV 感染相關 PAH | 99.55% | 1 | 5 |
| 結締組織疾病相關 PAH | 99.55% | 2 | 20+ |
| 慢性溶血性貧血相關 PAH | 99.55% | 0 | 0 |
| 血吸蟲病相關 PAH | 99.55% | 0 | 0 |


## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. pulmonary arteriovenous malformation (disease)</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.70%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content" markdown="1">

### 為什麼這個預測合理？

Treprostinil 是一種前列環素類似物，其作用機轉支持在各類肺動脈高壓中的應用：

1. **血管擴張**：直接擴張肺血管及全身血管
2. **抗血小板作用**：抑制血小板聚集
3. **抗增殖作用**：抑制血管平滑肌細胞增殖
4. **細胞保護作用**：保護內皮細胞功能

這些機轉適用於各種病因導致的肺動脈高壓，包括結締組織疾病、先天性心臟病、HIV 感染等。

### 臨床試驗

### 結締組織疾病相關 PAH
| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| 相關試驗 | Phase 2/3 | COMPLETED | N/A | Treprostinil 可改善 CTD-PAH 患者的運動耐力及血流動力學參數 |

### 先天性心臟病相關 PAH
| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| 相關試驗 | Phase 2 | COMPLETED | N/A | 評估 Treprostinil 在艾森曼格症候群患者中的療效 |

### 相關文獻

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15302727](https://pubmed.ncbi.nlm.nih.gov/15302727/) | 2004 | RCT | Chest | Treprostinil 皮下注射治療 CTD-PAH 的療效與安全性 |
| [11897647](https://pubmed.ncbi.nlm.nih.gov/11897647/) | 2002 | RCT | Ann Intern Med | Treprostinil 在肺動脈高壓中的療效 |
| [22621693](https://pubmed.ncbi.nlm.nih.gov/22621693/) | 2012 | Review | Drugs | CTD-APAH 治療指南建議使用 Treprostinil (I-B 推薦) |
| [41594679](https://pubmed.ncbi.nlm.nih.gov/41594679/) | 2026 | Review | Biomolecules | 討論 CTD-PAH 目前治療策略及吸入式 Treprostinil 的角色 |
| [22291467](https://pubmed.ncbi.nlm.nih.gov/22291467/) | 2012 | Review | Drug Des Devel Ther | 吸入式 Treprostinil 的臨床應用回顧 |

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. pulmonary arterial hypertension associated with congenital heart disease</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.60%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.60%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. pulmonary arterial hypertension associated with HIV infection</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.55%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.55%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. pulmonary arterial hypertension associated with chronic hemolytic anemia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.55%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.55%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. pulmonary arterial hypertension associated with connective tissue disease</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.55%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.55%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. pulmonary arterial hypertension associated with schistosomiasis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.55%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.55%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. hypotrichosis simplex of the scalp</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.48%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.48%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. congenital hypotrichosis milia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.30%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.30%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. malformation syndrome with odontal and/or periodontal component</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.21%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.21%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. Ambras type hypertrichosis universalis congenita</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.17%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.17%
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
| 衛部罕藥輸字第000071號 | 勵脈展素注射劑1毫克/毫升 | 注射劑 | 特發性或遺傳性肺動脈高壓 (WHO class III/IV) |
| 衛部罕藥輸字第000072號 | 勵脈展素注射劑2.5毫克/毫升 | 注射劑 | 特發性或遺傳性肺動脈高壓 (WHO class III/IV) |
| 衛部罕藥輸字第000074號 | 勵脈展素注射劑10毫克/毫升 | 注射劑 | 特發性或遺傳性肺動脈高壓 (WHO class III/IV) |
| 衛部罕藥輸字第000096號 | 泰肺舒口腔吸入液 | 口腔吸入劑 | 特發性或遺傳性肺動脈高壓 (NYHA class III) |
| 衛部藥輸字第029038號 | 拓肺鬆口腔吸入液 | 口腔吸入劑 | 間質性肺病造成的肺高壓 |

## 安全性考量

- **給藥途徑**：皮下注射可能引起注射部位疼痛及反應
- **血壓影響**：可能引起低血壓
- **出血風險**：抗血小板作用可能增加出血風險
- **主要交互作用 (Moderate)**：
  - Acetylsalicylic acid（增加出血風險）
  - SGLT2 抑制劑（Canagliflozin、Dapagliflozin、Empagliflozin）
  - Epinephrine（可能影響血壓調節）


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a></div>

**Hemorrhage** 🟡 Moderate
- Treprostinil injection inhibits platelet aggregation and increases the risk of bleeding.  Close monitoring is recommended when using this agent in patients with bleeding disorders.

**Diverticulum** 🟡 Moderate
- The tablet shell of the manufactured form of treprostinil, Orenitram does not dissolve and can lodge in the diverticulum of patients with diverticulosis.  Care should be exercised when using this drug in patient with diverticulosis.

**低血壓 (Hypotension)** 🟡 Moderate
- Treprostinil is a pulmonary and systemic vasodilator.  In patients with low systemic arterial pressure, treatment with treprostinil injection may produce symptomatic hypotension.  Care should be exercised when using this agent in patients at risk.

**肝臟疾病 (Liver Diseases)** 🟡 Moderate
- Severe hepatic impairment (Child Pugh Class C) is a contraindication in patients taking the oral presentation of treprostinil.  Treprostinil is substantially metabolized by the liver, primarily by CYP450 2C8.  Treprostinil injection clearance is redu...

**Pneumonia** 🟡 Moderate
- The efficacy of treprostinil inhalant has not been established in patients with significant underlying lung disease.  Patients with acute pulmonary infections should be carefully monitored to detect any worsening of lung disease and loss of drug effe...

*另有 2 項疾病注意事項，詳見 [DDInter 2.0](https://ddinter2.scbdd.com/)*

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Treprostinil 在結締組織疾病相關肺動脈高壓中已有充分的臨床證據支持，歐洲治療指南已將其列為 I-B 等級推薦。對於其他預測的適應症（如先天性心臟病相關 PAH），也有臨床試驗和文獻支持。

**若要推進需要：**
- 針對特定亞型（如 HIV 相關 PAH）的進一步研究
- 吸入式劑型在不同 PAH 亞型中的療效評估
- 與其他 PAH 治療藥物的比較研究


---

## 相關藥物報告

- [Povidone]({{ "/drugs/povidone/" | relative_url }}) - 證據等級 L5
- [Irbesartan]({{ "/drugs/irbesartan/" | relative_url }}) - 證據等級 L5
- [Cytarabine]({{ "/drugs/cytarabine/" | relative_url }}) - 證據等級 L5
- [Atezolizumab]({{ "/drugs/atezolizumab/" | relative_url }}) - 證據等級 L5
- [Remdesivir]({{ "/drugs/remdesivir/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Treprostinil老藥新用驗證報告. https://twtxgnn.yao.care/drugs/treprostinil/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_treprostinil,
  title = {Treprostinil老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/treprostinil/}
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
