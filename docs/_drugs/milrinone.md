---
layout: default
title: Milrinone
description: "Milrinone 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 106
evidence_level: L1
indication_count: 10
---

# Milrinone

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Milrinone 藥師筆記

## 一句話總結

<p class="key-answer" data-question="Milrinone 可以用於治療什麼新適應症？">
Milrinone 是一種磷酸二酯酶抑制劑，TxGNN 預測其對禿髮症及頭痛障礙有潛力，其中頭痛障礙（特別是可逆性腦血管收縮症候群相關頭痛）已有病例報告支持動脈內 Milrinone 的療效。
</p>

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Milrinone（米力心） |
| DrugBank ID | DB00235 |
| 台灣商品名 | 米力心注射劑0.2毫克/毫升 |
| 原核准適應症 | 充血性心衰竭的短期療法 |
| 預測新適應症 | alopecia、hypotrichosis simplex of the scalp、congenital hypotrichosis milia、diffuse alopecia areata、headache disorder、congestive heart failure、migraine disorder、migraine with brainstem aura、trigeminal autonomic cephalalgia、acute pulmonary heart disease |
| 最高預測分數 | 0.9991（禿髮症） |
| 證據等級 | L3（觀察性研究/病例報告 - 頭痛障礙） |

---



## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. alopecia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.91%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>### 藥理機轉分析</p>

<p>Milrinone 是選擇性磷酸二酯酶-3（PDE3）抑制劑，透過增加細胞內 cAMP 濃度發揮作用。其機轉與預測適應症的關聯：</p>

<ol>
<li><strong>禿髮症/毛髮稀疏症</strong>（TxGNN Score: 0.9991）</li>
</ol>
<ul>
<li>PDE 抑制劑（如 minoxidil）已知可促進毛髮生長</li>
<li>Milrinone 作為 PDE3 抑制劑理論上可能有類似作用</li>
<li>但缺乏直接證據</li>

</ul>
<ol>
<li><strong>頭痛障礙</strong>（TxGNN Score: 0.9946）</li>
</ol>
<ul>
<li>Milrinone 具有血管擴張作用</li>
<li>已有病例報告顯示動脈內 Milrinone 可用於治療可逆性腦血管收縮症候群（RCVS）</li>
<li>透過解除腦血管痙攣來緩解頭痛</li>

</ul>
<ol>
<li><strong>充血性心衰竭</strong>（TxGNN Score: 0.9945）</li>
</ol>
<ul>
<li>此為原核准適應症，有豐富臨床試驗證據</li>
</ul>

<h3>臨床試驗</h3>

<table>
<thead>
<tr>
<th>疾病</th>
<th>臨床試驗數量</th>
<th>最高期別</th>
<th>證據等級</th>
</tr>
</thead>
<tbody>
<tr>
<td>頭痛障礙</td>
<td>1</td>
<td>N/A（觀察性）</td>
<td>L3</td>
</tr>
<tr>
<td>充血性心衰竭</td>
<td>30+</td>
<td>Phase 4</td>
<td>L1</td>
</tr>
<tr>
<td>禿髮症</td>
<td>0</td>
<td>-</td>
<td>L5</td>
</tr>
</tbody>
</table>

<h3>相關文獻</h3>

<p>### 頭痛障礙（可逆性腦血管收縮症候群）</p>

<table>
<thead>
<tr>
<th>PMID</th>
<th>標題</th>
<th>年份</th>
<th>類型</th>
<th>證據等級</th>
</tr>
</thead>
<tbody>
<tr>
<td>34784343</td>
<td>Reversible Cerebral Vasoconstriction Syndrome in Eclampsia Responding to Milrinone</td>
<td>2021</td>
<td>病例報告</td>
<td>L3</td>
</tr>
<tr>
<td>25440342</td>
<td>Novel approach to diagnose reversible cerebral vasoconstriction syndrome</td>
<td>2015</td>
<td>病例系列</td>
<td>L3</td>
</tr>
<tr>
<td>18647181</td>
<td>Intra-arterial milrinone for reversible cerebral vasoconstriction syndrome</td>
<td>2009</td>
<td>病例報告</td>
<td>L3</td>
</tr>
</tbody>
</table>

<p><strong>關鍵發現</strong>：</p>
<ul>
<li>多篇病例報告顯示動脈內 Milrinone 可快速改善 RCVS 相關的腦血管痙攣和神經症狀</li>
<li>特別適用於鈣離子通道阻斷劑治療無效的病例</li>
<li>作為 PDE 抑制劑，可有效鬆弛血管平滑肌</li>
</ul>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. hypotrichosis simplex of the scalp</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.90%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. congenital hypotrichosis milia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.89%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. diffuse alopecia areata</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.88%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. headache disorder</span>
<span class="evidence-badge evidence-L3">L3</span>
<span class="prediction-score">99.46%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（1 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06205758" target="_blank">NCT06205758</a></td><td>N/A</td><td>UNKNOWN</td><td>1600</td><td>Efficacy and Safety Prediction of Milrinone or Levosimendan as Initial Inotropic...</td></tr>
</tbody>
</table>

<h3>相關文獻（3 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/34784343/" target="_blank">34784343</a></td><td>2021</td><td>Article</td><td>The American journal</td><td>Reversible Cerebral Vasoconstriction Syndrome in a Backgroun...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/25440342/" target="_blank">25440342</a></td><td>2015</td><td>Article</td><td>Journal of stroke an</td><td>A novel approach to diagnose reversible cerebral vasoconstri...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/18647181/" target="_blank">18647181</a></td><td>2009</td><td>Article</td><td>Headache</td><td>Intra-arterial milrinone for reversible cerebral vasoconstri...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. congestive heart failure</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.45%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（50 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01301313" target="_blank">NCT01301313</a></td><td>PHASE2</td><td>TERMINATED</td><td>116</td><td>Phase II Study to Evaluate the Efficacy and Safety of Levosimendan in Severe Acu...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02098629" target="_blank">NCT02098629</a></td><td>PHASE2</td><td>COMPLETED</td><td>25</td><td>Concomitant Milrinone and Esmolol Treatment in Patients with Acute Myocardial In...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04369573" target="_blank">NCT04369573</a></td><td>PHASE4</td><td>TERMINATED</td><td>100</td><td>Early Intra-aortic Balloon Pump Placement in Acute Decompensated Heart Failure C...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06522594" target="_blank">NCT06522594</a></td><td>PHASE2</td><td>RECRUITING</td><td>20</td><td>Randomized Embedded Multifactorial Adaptive Platform in ExtraCorporeal Membrane ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03071835" target="_blank">NCT03071835</a></td><td>N/A</td><td>COMPLETED</td><td>47</td><td>A Comparative Study of Subjects tHree to Thirteen Years Past thEiR fInal Follow-...</td></tr>
</tbody>
</table>
<p><em>...及其他 45 項試驗</em></p>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35545181/" target="_blank">35545181</a></td><td>2023</td><td>Article</td><td>Current problems in </td><td>Meta-analysis Comparing the Efficacy of Dobutamine Versus Mi...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/3012226/" target="_blank">3012226</a></td><td>1986</td><td>Article</td><td>The Medical clinics </td><td>Congestive heart failure.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/31865433/" target="_blank">31865433</a></td><td>2020</td><td>Article</td><td>Heart and vessels</td><td>Comparing the effects of milrinone and olprinone in patients...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36122816/" target="_blank">36122816</a></td><td>2022</td><td>Article</td><td>Journal of cardiac f</td><td>Palliative Inotropes in Advanced Heart Failure: Comparing Ou...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/22664586/" target="_blank">22664586</a></td><td>2012</td><td>Article</td><td>Circulation journal </td><td>Combination of β-blocker and milrinone for acute heart failu...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. migraine disorder</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.45%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. migraine with brainstem aura</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.38%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. trigeminal autonomic cephalalgia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.25%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. acute pulmonary heart disease</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.19%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（27 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05049590" target="_blank">NCT05049590</a></td><td>PHASE3</td><td>COMPLETED</td><td>63</td><td>Acute Normovolemic Hemodilution (ANH) in Complex Cardiac Surgery</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05194514" target="_blank">NCT05194514</a></td><td>NA</td><td>COMPLETED</td><td>20</td><td>Randomized Trial to Compare the SherpaPak™ Device vs Cold Storage of Donor Heart...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04092855" target="_blank">NCT04092855</a></td><td>N/A</td><td>RECRUITING</td><td>112</td><td>Early Identification and Prediction of Right Ventricular Dysfunction and Failure...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01971944" target="_blank">NCT01971944</a></td><td>N/A</td><td>COMPLETED</td><td>50</td><td>The Influence of Beta Blocker Therapy on the Hemodynamic Response to Inotrope In...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04694092" target="_blank">NCT04694092</a></td><td>NA</td><td>UNKNOWN</td><td>40</td><td>Landiolol for Rate Control in Decompensated Heart Failure Due to Atrial Fibrilla...</td></tr>
</tbody>
</table>
<p><em>...及其他 22 項試驗</em></p>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/8659556/" target="_blank">8659556</a></td><td>1996</td><td>Article</td><td>The American journal</td><td>Milrinone: basic and clinical pharmacology and acute and chr...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/11096492/" target="_blank">11096492</a></td><td>1999</td><td>Article</td><td>Current treatment op</td><td>Acute Pulmonary Edema.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/16582544/" target="_blank">16582544</a></td><td>2006</td><td>Article</td><td>Cardiology</td><td>Medical and ventilatory treatment of acute heart failure: ne...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/16541166/" target="_blank">16541166</a></td><td>2006</td><td>Article</td><td>Tidsskrift for den N</td><td>[Medical and ventilatory treatment of acute heart failure].</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/21678708/" target="_blank">21678708</a></td><td>2011</td><td>Article</td><td>Prescrire internatio</td><td>Acute heart failure with dyspnoea: initial treatment. Furose...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>


## 台灣上市資訊

| 許可證字號 | 商品名 | 劑型 | 許可證持有者 | 狀態 |
|-----------|--------|------|-------------|------|
| （待確認） | 米力心注射劑0.2毫克/毫升 | 注射劑 | （待確認） | 有效 |

**適應症**：充血性心衰竭的短期療法。需在有適當心電圖監測設備的環境下使用。

---

## 安全性考量

### 使用注意事項

1. **心律不整風險**
   - 可能引起危及生命的室性心律不整
   - 需持續心電圖監測

2. **使用限制**
   - 目前無使用超過 48 小時的對照試驗經驗
   - 建議僅作為短期療法

3. **藥物交互作用**
   - 常與 digoxin 和利尿劑併用
   - 與其他強心藥物併用時需謹慎

### 給藥途徑考量

- **靜脈注射**：心衰竭標準給藥方式
- **動脈內注射**：RCVS 治療的研究給藥方式，需專業介入設備
- **吸入給藥**：肺高壓治療的研究給藥方式

---


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**肝臟疾病** 🟡 Moderate
- 需定期監測。風險包括：肝毒性。

**低血壓** 🟡 Moderate
- 需定期監測。

**Thrombocytopenia** 🟡 Moderate
- 風險包括：血栓。出現症狀時應考慮停藥。

**Arrhythmias, Cardiac** 🟢 Minor
- 需密切監測。風險包括：心律不整。可能有致命風險。

**Heart Valve Diseases** 🟢 Minor
- 不應使用本藥物。可能有嚴重不良反應。

**Myocardial Infarction** 🟢 Minor
- 不建議使用本藥物。

## 結論與下一步

### 評估結論

| 預測適應症 | 證據等級 | 臨床轉譯可行性 | 建議優先順序 |
|-----------|---------|---------------|-------------|
| 頭痛障礙（RCVS） | L3 | 中等 | 建議進一步研究 |
| 禿髮症 | L5 | 低 | 不建議優先開發 |
| 心衰竭 | L1 | 高（已核准） | 不適用 |

### 建議

1. **可逆性腦血管收縮症候群（RCVS）**
   - 目前已有多篇病例報告支持動脈內 Milrinone 的療效
   - 建議設計前瞻性研究評估安全性和有效性
   - 可考慮作為鈣離子通道阻斷劑無效時的救援治療

2. **禿髮症**
   - 雖然 PDE 抑制劑理論上可能有效
   - 但 Milrinone 為注射劑型，不適合局部外用治療禿髮
   - 不建議進一步開發

### 後續行動

- [x] 確認頭痛障礙文獻證據（已有 3 篇病例報告）
- [ ] 監測 RCVS 治療的新臨床試驗
- [ ] 評估是否有可能開發局部外用劑型用於禿髮（可行性低）

---

*報告產生日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、台灣 FDA*

---

## 相關藥物報告

- [Nitrofurantoin]({{ "/drugs/nitrofurantoin/" | relative_url }}) - 證據等級 L5
- [Trabectedin]({{ "/drugs/trabectedin/" | relative_url }}) - 證據等級 L5
- [Zanubrutinib]({{ "/drugs/zanubrutinib/" | relative_url }}) - 證據等級 L5
- [Remdesivir]({{ "/drugs/remdesivir/" | relative_url }}) - 證據等級 L5
- [Cladribine]({{ "/drugs/cladribine/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Milrinone老藥新用驗證報告. https://twtxgnn.yao.care/drugs/milrinone/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_milrinone,
  title = {Milrinone老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/milrinone/}
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
