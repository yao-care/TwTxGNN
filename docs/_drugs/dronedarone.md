---
layout: default
title: Dronedarone
description: "Dronedarone 的老藥新用潛力分析。高證據等級 L2，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 高證據等級 (L1-L2)
nav_order: 63
evidence_level: L2
indication_count: 10
---

# Dronedarone

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L2</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Dronedarone：從心房纖維顫動到中風疾病

## 一句話總結

<p class="key-answer" data-question="Dronedarone 可以用於治療什麼新適應症？">
Dronedarone 原本用於治療陣發性或持續性心房纖維顫動/心房撲動。
TxGNN 模型預測它可能對**中風疾病 (stroke disorder)** 有效，
目前有 **多個臨床試驗**和 **多篇文獻**支持這個方向。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 心房纖維顫動、心房撲動 |
| 預測新適應症 | stroke disorder、obsolete susceptibility to ischemic stroke、ABri amyloidosis、cerebrovascular disorder、brain stem infarction、atrial fibrillation (disease)、sick sinus syndrome 2, autosomal dominant、duodenal obstruction、cerebral artery occlusion、sarcoglycanopathy |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L2 |
| 台灣上市 | 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |


## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. stroke disorder</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.97%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content" markdown="1">

### 為什麼這個預測合理？

<p class="key-answer" data-question="這個藥物的作用機轉是什麼？">
Dronedarone 是 amiodarone 的衍生物，具有多通道阻斷作用，能維持竇性心律。
心房纖維顫動是中風的主要危險因素，透過維持竇性心律可減少心房血栓形成。
ATHENA 試驗的事後分析顯示 dronedarone 可降低中風和暫時性腦缺血發作風險，
且研究發現其具有獨立於抗心律不整作用之外的抗凝血和抗血小板效應。
</p>

<div class="key-takeaway">
此預測基於藥物的作用機轉，與現有臨床證據方向一致。
</div>

### 臨床試驗

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01151137](https://clinicaltrials.gov/study/NCT01151137) | Phase 3 | TERMINATED | 3236 | PALLAS 試驗評估 dronedarone 在永久性心房纖維顫動預防主要心血管事件 |
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | COMPLETED | 2789 | EAST 試驗證實早期節律控制可預防心血管死亡和中風 |
| [NCT05130268](https://clinicaltrials.gov/study/NCT05130268) | Phase 4 | COMPLETED | 339 | 評估首發心房纖維顫動患者早期使用 dronedarone 的效果 |
| [NCT05293080](https://clinicaltrials.gov/study/NCT05293080) | Phase 3 | NOT_YET_RECRUITING | 1746 | 急性中風合併心房纖維顫動患者的早期節律控制 |
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | N/A | COMPLETED | 2204 | CABANA 試驗比較導管消融與抗心律不整藥物治療 |

### 相關文獻

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22166900](https://pubmed.ncbi.nlm.nih.gov/22166900/) | 2012 | Review | Lancet | 心房纖維顫動治療進展，包括 dronedarone 的角色 |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | In vitro | Atherosclerosis | Dronedarone 具有獨立於抗心律不整作用的抗凝血和抗血小板效應 |
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | RCT analysis | Clin Res Cardiol | EAST-AFNET 4 試驗中 amiodarone 和 dronedarone 用於早期節律控制的安全性和療效 |
| [20730068](https://pubmed.ncbi.nlm.nih.gov/20730068/) | 2010 | Review | Vasc Health Risk Manag | Dronedarone 獲批及其在心房纖維顫動治療中的療效 |
| [35293087](https://pubmed.ncbi.nlm.nih.gov/35293087/) | 2022 | Post-hoc analysis | Eur J Heart Fail | ATHENA 試驗事後分析評估 dronedarone 在 HFpEF/HFmrEF 合併心房纖維顫動的效果 |

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. obsolete susceptibility to ischemic stroke</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.96%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.96%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. ABri amyloidosis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.92%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.92%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. cerebrovascular disorder</span>
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
<span class="indication-name">5. brain stem infarction</span>
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
<span class="indication-name">6. sick sinus syndrome 2, autosomal dominant</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.63%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.63%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. duodenal obstruction</span>
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
<span class="indication-name">8. cerebral artery occlusion</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.44%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.44%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. sarcoglycanopathy</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.43%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.43%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. Wildervanck syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.37%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.37%
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
| 1 張許可證 | 決奈達隆鹽酸鹽 | 口服劑型 | 陣發性或持續性心房纖維顫動/心房撲動，降低心房顫動住院風險 |

## 安全性考量

- **黑框警告**：永久性心房纖維顫動、嚴重心衰竭患者禁用
- **主要不良反應**：腹瀉、噁心、腹痛、血清肌酐升高
- **肝毒性**：罕見但嚴重，需監測肝功能
- **藥物交互作用**：與 digoxin 併用時會增加 digoxin 血中濃度

### 藥物-食物交互作用 (DFI)

<div class="dfi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a></div>

**葡萄柚汁 (grapefruit juice)** 🟢 Minor
- 影響：Grapefruit juice may increase the plasma concentrations of dronedarone.  The proposed mechanism is inhibition of CYP450 3A4-mediated first-pass metabolism in the gut wall by certain compounds present ...
- 建議：Patients treated with dronedarone should avoid consumption of grapefruit, grapefruit juice, and any supplement containing grapefruit extract.  Dronedarone should be taken twice daily with the morning ...

### 藥物-草藥交互作用 (DHI)

**聖約翰草（貫葉連翹）** 🔴 Major
- 影響：聖約翰草降低 Dronedarone 血中濃度
- 建議：禁止併用



### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a></div>

**Cardiomyopathies** 🟢 Minor
- Dronedarone has shown to double the risk of death in patients with symptomatic heart failure and recent decompensation requiring hospitalization or NYHA Class IV heart failure.  It has also shown to double the risk of stroke and death and hospitaliza...

**肝臟疾病 (Liver Diseases)** 🟢 Minor
- Dronedarone is extensively metabolized by the liver.  There is little clinical experience with moderate hepatic impairment and none in patients with severe hepatic impairment.  No dosage adjustment is recommended for patients with moderate hepatic im...

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Dronedarone 透過維持竇性心律和潛在的抗血栓機制，可能對中風預防有效。
ATHENA 試驗已顯示其在中風/TIA 預防方面的益處，但需注意適應症限制。

**若要推進需要：**
- 排除永久性心房纖維顫動和嚴重心衰竭患者
- 嚴格的肝功能監測計畫
- 與抗凝血藥物併用策略的優化研究


---

## 相關藥物報告

- [Carboplatin]({{ "/drugs/carboplatin/" | relative_url }}) - 證據等級 L2
- [Hydroxyurea]({{ "/drugs/hydroxyurea/" | relative_url }}) - 證據等級 L2
- [Hydroxyprogesterone Caproate]({{ "/drugs/hydroxyprogesterone_caproate/" | relative_url }}) - 證據等級 L2
- [Oteracil]({{ "/drugs/oteracil/" | relative_url }}) - 證據等級 L2
- [Prednisone]({{ "/drugs/prednisone/" | relative_url }}) - 證據等級 L2

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Dronedarone老藥新用驗證報告. https://twtxgnn.yao.care/drugs/dronedarone/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_dronedarone,
  title = {Dronedarone老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/dronedarone/}
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
