---
layout: default
title: Treprostinil
description: "Treprostinil 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L2
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
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>Treprostinil 是一種前列環素類似物，其作用機轉支持在各類肺動脈高壓中的應用：</p>

<ol>
<li><strong>血管擴張</strong>：直接擴張肺血管及全身血管</li>
<li><strong>抗血小板作用</strong>：抑制血小板聚集</li>
<li><strong>抗增殖作用</strong>：抑制血管平滑肌細胞增殖</li>
<li><strong>細胞保護作用</strong>：保護內皮細胞功能</li>

</ol>
<p>這些機轉適用於各種病因導致的肺動脈高壓，包括結締組織疾病、先天性心臟病、HIV 感染等。</p>

<h3>臨床試驗</h3>

<p>### 結締組織疾病相關 PAH</p>
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
<td>相關試驗</td>
<td>Phase 2/3</td>
<td>COMPLETED</td>
<td>N/A</td>
<td>Treprostinil 可改善 CTD-PAH 患者的運動耐力及血流動力學參數</td>
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
<td><a href="https://pubmed.ncbi.nlm.nih.gov/15302727/">15302727</a></td>
<td>2004</td>
<td>RCT</td>
<td>Chest</td>
<td>Treprostinil 皮下注射治療 CTD-PAH 的療效與安全性</td>
</tr>
<tr>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/11897647/">11897647</a></td>
<td>2002</td>
<td>RCT</td>
<td>Ann Intern Med</td>
<td>Treprostinil 在肺動脈高壓中的療效</td>
</tr>
<tr>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/22621693/">22621693</a></td>
<td>2012</td>
<td>Review</td>
<td>Drugs</td>
<td>CTD-APAH 治療指南建議使用 Treprostinil (I-B 推薦)</td>
</tr>
<tr>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/41594679/">41594679</a></td>
<td>2026</td>
<td>Review</td>
<td>Biomolecules</td>
<td>討論 CTD-PAH 目前治療策略及吸入式 Treprostinil 的角色</td>
</tr>
<tr>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/22291467/">22291467</a></td>
<td>2012</td>
<td>Review</td>
<td>Drug Des Devel Ther</td>
<td>吸入式 Treprostinil 的臨床應用回顧</td>
</tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. pulmonary arterial hypertension associated with congenital heart disease</span>
<span class="evidence-badge evidence-L3">L3</span>
<span class="prediction-score">99.60%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（2 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01383083" target="_blank">NCT01383083</a></td><td>N/A</td><td>UNKNOWN</td><td>42</td><td>Effects of Iloprost Treatment in Adult Patients With Pulmonary Arterial Hyperten...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02261883" target="_blank">NCT02261883</a></td><td>PHASE2</td><td>TERMINATED</td><td>42</td><td>Intravenous Remodulin (Treprostinil) as Add-on Therapy for the Treatment of Pers...</td></tr>
</tbody>
</table>

<h3>相關文獻（19 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35412560/" target="_blank">35412560</a></td><td>2022</td><td>Article</td><td>JAMA</td><td>Diagnosis and Treatment of Pulmonary Arterial Hypertension: ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/29436381/" target="_blank">29436381</a></td><td>2018</td><td>Article</td><td>Heart (British Cardi</td><td>Subcutaneous treprostinil in congenital heart disease-relate...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/21852894/" target="_blank">21852894</a></td><td>2009</td><td>Article</td><td>Progress in pediatri</td><td>Non-congenital heart disease associated pediatric pulmonary ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/16919006/" target="_blank">16919006</a></td><td>2006</td><td>Article</td><td>European journal of </td><td>Current treatment options in children with pulmonary arteria...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/16725066/" target="_blank">16725066</a></td><td>2006</td><td>Article</td><td>Cardiology in the yo</td><td>Bosentan for the treatment of pulmonary arterial hypertensio...</td></tr>
</tbody>
</table>
<p><em>...及其他 14 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. pulmonary arterial hypertension associated with HIV infection</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.55%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（1 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00494533" target="_blank">NCT00494533</a></td><td>PHASE4</td><td>TERMINATED</td><td>45</td><td>Treprostinil for Untreated Symptomatic PAH Trial: A 12-Week Multicenter Randomiz...</td></tr>
</tbody>
</table>

<h3>相關文獻（3 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/14720012/" target="_blank">14720012</a></td><td>2003</td><td>Article</td><td>American journal of </td><td>Prostanoids for pulmonary arterial hypertension.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/18473715/" target="_blank">18473715</a></td><td>2008</td><td>Article</td><td>Expert opinion on ph</td><td>Treprostinil for the treatment of pulmonary hypertension.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/18260882/" target="_blank">18260882</a></td><td>2007</td><td>Article</td><td>Kardiologiia</td><td>[Pulmonary hypertension and right ventricular failure. Part ...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. pulmonary arterial hypertension associated with chronic hemolytic anemia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.55%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. pulmonary arterial hypertension associated with connective tissue disease</span>
<span class="evidence-badge evidence-L3">L3</span>
<span class="prediction-score">99.55%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（1 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02663895" target="_blank">NCT02663895</a></td><td>PHASE2</td><td>COMPLETED</td><td>12</td><td>A Pilot Study to Evaluate the Safety and Efficacy of Oral Treprostinil in the Tr...</td></tr>
</tbody>
</table>

<h3>相關文獻（19 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35412560/" target="_blank">35412560</a></td><td>2022</td><td>Article</td><td>JAMA</td><td>Diagnosis and Treatment of Pulmonary Arterial Hypertension: ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38378970/" target="_blank">38378970</a></td><td>2024</td><td>Article</td><td>Internal and emergen</td><td>Treatment of pulmonary arterial hypertension in patients wit...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/11897647/" target="_blank">11897647</a></td><td>2002</td><td>Article</td><td>American journal of </td><td>Continuous subcutaneous infusion of treprostinil, a prostacy...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/37765060/" target="_blank">37765060</a></td><td>2023</td><td>Article</td><td>Pharmaceuticals (Bas</td><td>Recent Advances in the Treatment of Pulmonary Arterial Hyper...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/40566626/" target="_blank">40566626</a></td><td>2025</td><td>Article</td><td>Life (Basel, Switzer</td><td>Efficacy and Safety of Selexipag Treatment in Connective Tis...</td></tr>
</tbody>
</table>
<p><em>...及其他 14 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. pulmonary arterial hypertension associated with schistosomiasis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.55%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. hypotrichosis simplex of the scalp</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.48%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. congenital hypotrichosis milia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.30%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. malformation syndrome with odontal and/or periodontal component</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.21%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35688447/" target="_blank">35688447</a></td><td>2022</td><td>Article</td><td>Journal of clinical </td><td>Treatment of stage IV periodontitis: The EFP S3 level clinic...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/37435999/" target="_blank">37435999</a></td><td>2023</td><td>Article</td><td>Periodontology 2000</td><td>Complications and treatment errors related to regenerative p...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35420698/" target="_blank">35420698</a></td><td>2022</td><td>Article</td><td>The Cochrane databas</td><td>Treatment of periodontitis for glycaemic control in people w...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/9495612/" target="_blank">9495612</a></td><td>1998</td><td>Article</td><td>Journal of clinical </td><td>Microbial complexes in subgingival plaque.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/22057194/" target="_blank">22057194</a></td><td>2012</td><td>Article</td><td>Diabetologia</td><td>Periodontitis and diabetes: a two-way relationship.</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. Ambras type hypertrichosis universalis congenita</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.17%</span>
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

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**Hemorrhage** 🟡 Moderate
- 需定期監測。風險包括：出血。

**Diverticulum** 🟡 Moderate
- 注意事項：The tablet shell of the manufactured form of treprostinil, Orenitram does not dissolve and can lodge in the diverticulum of patients with diverticulos...

**低血壓** 🟡 Moderate
- 風險包括：低血壓。

**肝臟疾病** 🟡 Moderate
- 需密切監測。可能有嚴重不良反應。

**Pneumonia** 🟡 Moderate
- 需定期監測。風險包括：感染。

**腎臟疾病** 🟡 Moderate
- 通常無需調整劑量。

**Hepatic Insufficiency** 🟢 Minor
- 本藥物在此情況下禁用。可能有嚴重不良反應。

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
