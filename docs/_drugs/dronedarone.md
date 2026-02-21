---
layout: default
title: Dronedarone
description: "Dronedarone 的老藥新用潛力分析。高證據等級 L2，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 高證據等級 (L1-L2)
nav_order: 63
evidence_level: L1
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
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.97%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p><p class="key-answer" data-question="這個藥物的作用機轉是什麼？"></p>
<p>Dronedarone 是 amiodarone 的衍生物，具有多通道阻斷作用，能維持竇性心律。</p>
<p>心房纖維顫動是中風的主要危險因素，透過維持竇性心律可減少心房血栓形成。</p>
<p>ATHENA 試驗的事後分析顯示 dronedarone 可降低中風和暫時性腦缺血發作風險，</p>
<p>且研究發現其具有獨立於抗心律不整作用之外的抗凝血和抗血小板效應。</p>
<p></p></p>

<p><div class="key-takeaway"></p>
<p>此預測基於藥物的作用機轉，與現有臨床證據方向一致。</p>

<h3>臨床試驗</h3>

<table>
<thead>
<tr>
<th>試驗編號</th>
<th>階段</th>
<th>狀態</th>
<th>人數</th>
<th>主要發現</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://clinicaltrials.gov/study/NCT01151137">NCT01151137</a></td>
<td>Phase 3</td>
<td>TERMINATED</td>
<td>3236</td>
<td>PALLAS 試驗評估 dronedarone 在永久性心房纖維顫動預防主要心血管事件</td>
</tr>
<tr>
<td><a href="https://clinicaltrials.gov/study/NCT01288352">NCT01288352</a></td>
<td>Phase 4</td>
<td>COMPLETED</td>
<td>2789</td>
<td>EAST 試驗證實早期節律控制可預防心血管死亡和中風</td>
</tr>
<tr>
<td><a href="https://clinicaltrials.gov/study/NCT05130268">NCT05130268</a></td>
<td>Phase 4</td>
<td>COMPLETED</td>
<td>339</td>
<td>評估首發心房纖維顫動患者早期使用 dronedarone 的效果</td>
</tr>
<tr>
<td><a href="https://clinicaltrials.gov/study/NCT05293080">NCT05293080</a></td>
<td>Phase 3</td>
<td>NOT_YET_RECRUITING</td>
<td>1746</td>
<td>急性中風合併心房纖維顫動患者的早期節律控制</td>
</tr>
<tr>
<td><a href="https://clinicaltrials.gov/study/NCT00911508">NCT00911508</a></td>
<td>N/A</td>
<td>COMPLETED</td>
<td>2204</td>
<td>CABANA 試驗比較導管消融與抗心律不整藥物治療</td>
</tr>
</tbody>
</table>

<h3>相關文獻</h3>

<table>
<thead>
<tr>
<th>PMID</th>
<th>年份</th>
<th>類型</th>
<th>期刊</th>
<th>主要發現</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/22166900/">22166900</a></td>
<td>2012</td>
<td>Review</td>
<td>Lancet</td>
<td>心房纖維顫動治療進展，包括 dronedarone 的角色</td>
</tr>
<tr>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/28992468/">28992468</a></td>
<td>2017</td>
<td>In vitro</td>
<td>Atherosclerosis</td>
<td>Dronedarone 具有獨立於抗心律不整作用的抗凝血和抗血小板效應</td>
</tr>
<tr>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/40387892/">40387892</a></td>
<td>2025</td>
<td>RCT analysis</td>
<td>Clin Res Cardiol</td>
<td>EAST-AFNET 4 試驗中 amiodarone 和 dronedarone 用於早期節律控制的安全性和療效</td>
</tr>
<tr>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/20730068/">20730068</a></td>
<td>2010</td>
<td>Review</td>
<td>Vasc Health Risk Manag</td>
<td>Dronedarone 獲批及其在心房纖維顫動治療中的療效</td>
</tr>
<tr>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/35293087/">35293087</a></td>
<td>2022</td>
<td>Post-hoc analysis</td>
<td>Eur J Heart Fail</td>
<td>ATHENA 試驗事後分析評估 dronedarone 在 HFpEF/HFmrEF 合併心房纖維顫動的效果</td>
</tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. obsolete susceptibility to ischemic stroke</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.96%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. ABri amyloidosis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.92%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. cerebrovascular disorder</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.71%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（6 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03993119" target="_blank">NCT03993119</a></td><td>N/A</td><td>COMPLETED</td><td>500</td><td>Non-Interventional, Cross-sectional Study to Describe NOACs Management in Elderl...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01288352" target="_blank">NCT01288352</a></td><td>PHASE4</td><td>COMPLETED</td><td>2789</td><td>Early Therapy of Atrial Fibrillation for Stroke Prevention Trial (EAST).</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01856075" target="_blank">NCT01856075</a></td><td>N/A</td><td>COMPLETED</td><td>1015</td><td>Relative Effectiveness of Dronedarone vs. Other Treatments of Atrial Fibrillatio...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06125925" target="_blank">NCT06125925</a></td><td>NA</td><td>RECRUITING</td><td>436</td><td>Catheter Ablation in Atrial Fibrillation Patients With Heart Failure With Preser...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05293080" target="_blank">NCT05293080</a></td><td>PHASE3</td><td>NOT_YET_RECRUITING</td><td>1746</td><td>Early Treatment of Atrial Fibrillation for Stroke Prevention Trial in Acute STRO...</td></tr>
</tbody>
</table>
<p><em>...及其他 1 項試驗</em></p>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/22166900/" target="_blank">22166900</a></td><td>2012</td><td>Article</td><td>Lancet (London, Engl</td><td>Atrial fibrillation.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/22149318/" target="_blank">22149318</a></td><td>2011</td><td>Article</td><td>American journal of </td><td>Dronedarone and the incidence of stroke in patients with par...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/22682206/" target="_blank">22682206</a></td><td>2012</td><td>Article</td><td>Neurologia (Barcelon</td><td>[Prevention of cardioembolic stroke].</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/20396635/" target="_blank">20396635</a></td><td>2010</td><td>Article</td><td>Clinical interventio</td><td>Impact of dronedarone in atrial fibrillation and flutter on ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30528621/" target="_blank">30528621</a></td><td>2019</td><td>Article</td><td>International journa</td><td>Impact of dronedarone on the risk of myocardial infarction a...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. brain stem infarction</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.71%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. sick sinus syndrome 2, autosomal dominant</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.63%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. duodenal obstruction</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.56%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. cerebral artery occlusion</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.44%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（1 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05130268" target="_blank">NCT05130268</a></td><td>PHASE4</td><td>COMPLETED</td><td>339</td><td>Pragmatic Randomized Clinical Trial of Early Dronedarone Versus Usual Care to Ch...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. sarcoglycanopathy</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.43%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. Wildervanck syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.37%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
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

<div class="dfi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**葡萄柚汁** 🟢 Minor
- 影響：影響藥物代謝。可能增加藥物血中濃度。
- 建議：建議避免併用。避免食用葡萄柚或葡萄柚汁。

### 藥物-草藥交互作用 (DHI)

**聖約翰草（貫葉連翹）** 🔴 Major
- 影響：聖約翰草降低 Dronedarone 血中濃度
- 建議：禁止併用


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**Cardiomyopathies** 🟢 Minor
- 本藥物在此情況下禁用。可能有致命風險。

**肝臟疾病** 🟢 Minor
- 本藥物在此情況下禁用。可能需要調整劑量。可能有嚴重不良反應。

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
