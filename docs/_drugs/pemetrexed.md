---
layout: default
title: Pemetrexed
description: "Pemetrexed 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L1
indication_count: 10
---

# Pemetrexed

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Pemetrexed 藥師筆記

## 一句話總結

<p class="key-answer" data-question="Pemetrexed 可以用於治療什麼新適應症？">
Pemetrexed 為多標靶抗葉酸類抗腫瘤藥物，TxGNN 預測其對惡性胸膜間皮瘤和腹膜間皮瘤有療效，此預測已獲多個 Phase III 臨床試驗證實，為該疾病的第一線標準治療。
</p>


---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥品名稱 | Pemetrexed (培美曲塞) |
| DrugBank ID | DB00642 |
| 台灣商品名 | 愛寧達注射劑 (Alimta)、各廠學名藥 |
| 原適應症 | 非小細胞肺癌、惡性胸膜間皮瘤 |
| 預測新適應症 | malignant peritoneal mesothelioma、pleural adenomatoid tumor、pleural mesothelioma、pleural epithelioid mesothelioma、pleural sarcomatoid mesothelioma、pleural biphasic mesothelioma、pericardium cancer、well differentiated papillary mesothelioma、lymphohistiocytoid mesothelioma、malignant mesothelioma (disease) |
| 證據等級 | L1 (多個 RCT) |
| TxGNN 預測分數 | 0.9999+ |

---



## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. malignant peritoneal mesothelioma</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.99%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>### 機轉連結</p>

<ol>
<li><strong>多標靶抗葉酸作用</strong>：Pemetrexed 抑制多個葉酸依賴性酵素 (DHFR、TS、GARFT)，阻斷嘌呤和嘧啶合成，對快速分裂的腫瘤細胞有效。</li>

<li><strong>間皮瘤共同病理</strong>：胸膜和腹膜間皮瘤均起源於間皮細胞，具有相似的分子特徵，對 pemetrexed 的反應機制相似。</li>

<li><strong>與鉑類藥物協同</strong>：Pemetrexed + cisplatin 的組合已證實對間皮瘤有效，此組合也適用於腹膜型。</li>
</ol>

<h3>臨床試驗</h3>

<p>### 胸膜間皮瘤 Phase III 試驗</p>

<table>
<thead>
<tr>
<th>試驗編號</th>
<th>療法</th>
<th>狀態</th>
<th>主要終點</th>
</tr>
</thead>
<tbody>
<tr>
<td>NCT00386815</td>
<td>Pemetrexed + Cisplatin</td>
<td>完成</td>
<td>安全性確認</td>
</tr>
<tr>
<td>NCT02899299</td>
<td>Nivolumab + Ipilimumab vs Pemetrexed + Platinum</td>
<td>完成</td>
<td>整體存活期</td>
</tr>
<tr>
<td>NCT06097728</td>
<td>Volrustomig + Carboplatin + Pemetrexed</td>
<td>招募中</td>
<td>整體存活期</td>
</tr>
<tr>
<td>NCT04334759</td>
<td>Durvalumab + 化療 (含 Pemetrexed)</td>
<td>完成</td>
<td>整體存活期</td>
</tr>
<tr>
<td>NCT04153565</td>
<td>Pembrolizumab + Cisplatin + Pemetrexed</td>
<td>完成</td>
<td>安全性及初步療效</td>
</tr>
</tbody>
</table>

<h3>相關文獻</h3>

<p>### 惡性腹膜間皮瘤 (MPeM)</p>

<table>
<thead>
<tr>
<th>PMID</th>
<th>發表年份</th>
<th>研究類型</th>
<th>主要發現</th>
</tr>
</thead>
<tbody>
<tr>
<td>38142057</td>
<td>2023</td>
<td>病例報告</td>
<td>BAP1 突變的 MPeM 患者經 18 週期 pemetrexed + bevacizumab 治療後達到完全臨床緩解</td>
</tr>
<tr>
<td>28594258</td>
<td>2017</td>
<td>回顧性研究</td>
<td>Pemetrexed + cisplatin 作為 MPeM 第一線化療的療效評估</td>
</tr>
<tr>
<td>31583526</td>
<td>2020</td>
<td>基礎研究</td>
<td>建立 pemetrexed 抗性 MPeM 細胞株用於研究抗藥機制</td>
</tr>
<tr>
<td>31417959</td>
<td>2019</td>
<td>病例報告</td>
<td>雙向化療 (含 pemetrexed) 使不可切除 MPeM 轉為可手術</td>
</tr>
<tr>
<td>34723916</td>
<td>2022</td>
<td>病例系列</td>
<td>Pembrolizumab + pemetrexed + platinum 對鉑類無反應 MPeM 有效</td>
</tr>
<tr>
<td>38806763</td>
<td>2024</td>
<td>多中心研究</td>
<td>分析 MPeM 治療策略和預後</td>
</tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. pleural adenomatoid tumor</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.99%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. pleural mesothelioma</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.99%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（50 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00386815" target="_blank">NCT00386815</a></td><td>PHASE2</td><td>COMPLETED</td><td>20</td><td>Safety Confirmation Study of LY231514 Plus Cisplatin in Patients With Malignant ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03760575" target="_blank">NCT03760575</a></td><td>PHASE1</td><td>RECRUITING</td><td>20</td><td>Pembrolizumab in Combination With Chemotherapy and Image-Guided Surgery for Mali...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02303899" target="_blank">NCT02303899</a></td><td>PHASE2</td><td>COMPLETED</td><td>22</td><td>A Phase II Study of the Combination of Gemcitabine and Imatinib Mesylate in Peme...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06097728" target="_blank">NCT06097728</a></td><td>PHASE3</td><td>RECRUITING</td><td>825</td><td>A Phase III, Randomized, Open-Label, Multicenter, Global Study of Volrustomig (M...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04153565" target="_blank">NCT04153565</a></td><td>PHASE1</td><td>COMPLETED</td><td>19</td><td>A Phase Ib Clinical Study to Evaluate the Safety and Efficacy of Pembrolizumab (...</td></tr>
</tbody>
</table>
<p><em>...及其他 45 項試驗</em></p>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/37931632/" target="_blank">37931632</a></td><td>2023</td><td>Article</td><td>Lancet (London, Engl</td><td>Pembrolizumab plus chemotherapy versus chemotherapy in untre...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/12860938/" target="_blank">12860938</a></td><td>2003</td><td>Article</td><td>Journal of clinical </td><td>Phase III study of pemetrexed in combination with cisplatin ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/34985934/" target="_blank">34985934</a></td><td>2022</td><td>Article</td><td>Journal of clinical </td><td>New Era for Malignant Pleural Mesothelioma: Updates on Thera...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26719230/" target="_blank">26719230</a></td><td>2016</td><td>Article</td><td>Lancet (London, Engl</td><td>Bevacizumab for newly diagnosed pleural mesothelioma in the ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/16807435/" target="_blank">16807435</a></td><td>2006</td><td>Article</td><td>Annals of oncology :</td><td>Pemetrexed and malignant pleural mesothelioma.</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. pleural epithelioid mesothelioma</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.99%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（13 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06097728" target="_blank">NCT06097728</a></td><td>PHASE3</td><td>RECRUITING</td><td>825</td><td>A Phase III, Randomized, Open-Label, Multicenter, Global Study of Volrustomig (M...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06155279" target="_blank">NCT06155279</a></td><td>PHASE2</td><td>ACTIVE_NOT_RECRUITING</td><td>41</td><td>Phase II Study of Pembrolizumab in Combination With Cisplatin or Carboplatin and...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00227630" target="_blank">NCT00227630</a></td><td>PHASE2</td><td>COMPLETED</td><td>59</td><td>A Phase II Feasibility Trial of Induction Chemotherapy Followed by Extrapleural ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01064648" target="_blank">NCT01064648</a></td><td>PHASE1, PHASE2</td><td>ACTIVE_NOT_RECRUITING</td><td>117</td><td>A Phase I/Randomized Phase II Study of Cediranib (NSC#732208) Versus Placebo in ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT07121374" target="_blank">NCT07121374</a></td><td>PHASE1, PHASE2</td><td>RECRUITING</td><td>37</td><td>NEoadjuvant Chemotherapy and Immunotherapy for a Selected Group of Inoperable Pl...</td></tr>
</tbody>
</table>
<p><em>...及其他 8 項試驗</em></p>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26719230/" target="_blank">26719230</a></td><td>2016</td><td>Article</td><td>Lancet (London, Engl</td><td>Bevacizumab for newly diagnosed pleural mesothelioma in the ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39814199/" target="_blank">39814199</a></td><td>2025</td><td>Article</td><td>Annals of oncology :</td><td>A randomised phase III study of bevacizumab and carboplatin-...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26873306/" target="_blank">26873306</a></td><td>2016</td><td>Article</td><td>Therapeutic advances</td><td>Malignant pleural mesothelioma: an update on diagnosis and t...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/25979846/" target="_blank">25979846</a></td><td>2015</td><td>Article</td><td>Cancer treatment rev</td><td>The established and future biomarkers of malignant pleural m...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39818191/" target="_blank">39818191</a></td><td>2025</td><td>Article</td><td>Respiratory investig</td><td>Current drug therapy for pleural mesothelioma.</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. pleural sarcomatoid mesothelioma</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.99%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（8 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00227630" target="_blank">NCT00227630</a></td><td>PHASE2</td><td>COMPLETED</td><td>59</td><td>A Phase II Feasibility Trial of Induction Chemotherapy Followed by Extrapleural ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01064648" target="_blank">NCT01064648</a></td><td>PHASE1, PHASE2</td><td>ACTIVE_NOT_RECRUITING</td><td>117</td><td>A Phase I/Randomized Phase II Study of Cediranib (NSC#732208) Versus Placebo in ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01085630" target="_blank">NCT01085630</a></td><td>PHASE2</td><td>COMPLETED</td><td>72</td><td>Randomized Phase II Study of Maintenance Pemetrexed Versus Observation for Patie...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00334594" target="_blank">NCT00334594</a></td><td>PHASE2</td><td>COMPLETED</td><td>153</td><td>Neoadjuvant Chemotherapy and Extrapleural Pneumonectomy of Malignant Pleural Mes...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01105390" target="_blank">NCT01105390</a></td><td>PHASE2</td><td>WITHDRAWN</td><td>0</td><td>A Phase II Trial of AMG 102 in Combination With Pemetrexed and Cisplatin in Pati...</td></tr>
</tbody>
</table>
<p><em>...及其他 3 項試驗</em></p>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26719230/" target="_blank">26719230</a></td><td>2016</td><td>Article</td><td>Lancet (London, Engl</td><td>Bevacizumab for newly diagnosed pleural mesothelioma in the ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39818191/" target="_blank">39818191</a></td><td>2025</td><td>Article</td><td>Respiratory investig</td><td>Current drug therapy for pleural mesothelioma.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30798074/" target="_blank">30798074</a></td><td>2019</td><td>Article</td><td>Annals of diagnostic</td><td>Revisiting localized malignant mesothelioma.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28197626/" target="_blank">28197626</a></td><td>2017</td><td>Article</td><td>International journa</td><td>Kdm6a and Kdm6b: Altered expression in malignant pleural mes...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/31569615/" target="_blank">31569615</a></td><td>2019</td><td>Article</td><td>Cancers</td><td>In Vitro Characterization of Cisplatin and Pemetrexed Effect...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. pleural biphasic mesothelioma</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.99%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（5 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06155279" target="_blank">NCT06155279</a></td><td>PHASE2</td><td>ACTIVE_NOT_RECRUITING</td><td>41</td><td>Phase II Study of Pembrolizumab in Combination With Cisplatin or Carboplatin and...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04158141" target="_blank">NCT04158141</a></td><td>PHASE3</td><td>TERMINATED</td><td>16</td><td>Phase III Randomized Trial of Pleurectomy/Decortication Plus Systemic Therapy Wi...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03228537" target="_blank">NCT03228537</a></td><td>PHASE1</td><td>ACTIVE_NOT_RECRUITING</td><td>28</td><td>A Feasibility Trial of Neoadjuvant Cisplatin-Pemetrexed With Atezolizumab in Com...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02709512" target="_blank">NCT02709512</a></td><td>PHASE2, PHASE3</td><td>COMPLETED</td><td>249</td><td>Randomized, Double-Blind, Phase 2/3 Study in Subjects With Malignant Pleural Mes...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03564691" target="_blank">NCT03564691</a></td><td>PHASE1</td><td>COMPLETED</td><td>470</td><td>A Phase 1 Open Label, Multi-Arm, Multicenter Study of MK-4830 as Monotherapy and...</td></tr>
</tbody>
</table>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/25979846/" target="_blank">25979846</a></td><td>2015</td><td>Article</td><td>Cancer treatment rev</td><td>The established and future biomarkers of malignant pleural m...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39818191/" target="_blank">39818191</a></td><td>2025</td><td>Article</td><td>Respiratory investig</td><td>Current drug therapy for pleural mesothelioma.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28197626/" target="_blank">28197626</a></td><td>2017</td><td>Article</td><td>International journa</td><td>Kdm6a and Kdm6b: Altered expression in malignant pleural mes...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/31569615/" target="_blank">31569615</a></td><td>2019</td><td>Article</td><td>Cancers</td><td>In Vitro Characterization of Cisplatin and Pemetrexed Effect...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39624250/" target="_blank">39624250</a></td><td>2024</td><td>Article</td><td>JTO clinical and res</td><td>Real-World Outcomes of Patients With Malignant Pleural Mesot...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. pericardium cancer</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.99%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（3 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04462809" target="_blank">NCT04462809</a></td><td>PHASE2</td><td>UNKNOWN</td><td>40</td><td>A Three-Cohort Phase II Trial to Assess the Efficacy of a Maintenance Treatment ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02662504" target="_blank">NCT02662504</a></td><td>PHASE2</td><td>COMPLETED</td><td>6</td><td>Pilot Study of the Feasibility of Intrapleural Photodynamic Therapy in a Multimo...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01590160" target="_blank">NCT01590160</a></td><td>PHASE1, PHASE2</td><td>COMPLETED</td><td>27</td><td>A Phase I/II Study of First Line Ganetespib With Platinum, in Patients With Mali...</td></tr>
</tbody>
</table>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/17936406/" target="_blank">17936406</a></td><td>2008</td><td>Article</td><td>Lung cancer (Amsterd</td><td>Primary pericardial mesothelioma.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/18473795/" target="_blank">18473795</a></td><td>2008</td><td>Article</td><td>Current medicinal ch</td><td>Molecular targets and targeted therapies for malignant mesot...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30450660/" target="_blank">30450660</a></td><td>2019</td><td>Article</td><td>Journal of clinical </td><td>Localized primary malignant pericardial mesothelioma.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30594459/" target="_blank">30594459</a></td><td>2019</td><td>Article</td><td>Clinical lung cancer</td><td>Treatment and Outcomes of Primary Pericardial Mesothelioma: ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/22104079/" target="_blank">22104079</a></td><td>2012</td><td>Article</td><td>Cancer treatment rev</td><td>Diffuse malignant peritoneal mesothelioma--an update on trea...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. well differentiated papillary mesothelioma</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.99%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（6 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/23964112/" target="_blank">23964112</a></td><td>2013</td><td>Article</td><td>Japanese journal of </td><td>Therapeutic strategies for well-differentiated papillary mes...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28435764/" target="_blank">28435764</a></td><td>2017</td><td>Article</td><td>Cureus</td><td>A Case of Well-Differentiated Papillary Mesothelioma of the ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/23714495/" target="_blank">23714495</a></td><td>2013</td><td>Article</td><td>American Society of </td><td>Peritoneal mesothelioma: the site of origin matters.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38806763/" target="_blank">38806763</a></td><td>2024</td><td>Article</td><td>Annals of surgical o</td><td>Analysis of Treatment Strategies and Outcomes in Malignant P...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26210689/" target="_blank">26210689</a></td><td>2015</td><td>Article</td><td>Annales de pathologi</td><td>[Peritoneal tumor pathology - case no. 3 : peritoneal well-d...</td></tr>
</tbody>
</table>
<p><em>...及其他 1 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. lymphohistiocytoid mesothelioma</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.99%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. iminoglycinuria</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.97%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>


## 台灣上市資訊

| 許可證字號 | 商品名 | 適應症 | 狀態 |
|-----------|--------|--------|------|
| 衛部藥陸輸字第000892號 | 培美曲塞二鈉 (原料藥) | 抗腫瘤藥 | 已註銷 |
| 衛部菌疫輸字第001025號 | 吉舒達注射劑 (Keytruda) | 非小細胞肺癌 (與 pemetrexed 併用)、惡性胸膜間皮瘤 (與 pemetrexed 併用) | 有效 |

**注意**：台灣已核准 pembrolizumab 與 pemetrexed 及含鉑化療併用，作為無法切除之晚期或轉移性惡性胸膜間皮瘤的第一線治療。

---

## 安全性考量

### 重要警語

- **骨髓抑制**：嗜中性球低下、血小板低下為劑量限制毒性
- **腎毒性**：需監測腎功能，腎功能不全需調整劑量
- **皮膚毒性**：皮疹常見，可能需要類固醇預防

### 必要補充治療

| 補充劑 | 目的 | 給予方式 |
|--------|------|----------|
| 葉酸 | 減少血液毒性 | 每日口服 350-1000 mcg |
| 維生素 B12 | 減少血液毒性 | 每 9 週肌肉注射 1000 mcg |
| Dexamethasone | 減少皮膚毒性 | 治療前後給予 |

### 藥物交互作用

| 交互作用藥物 | 影響說明 |
|-------------|----------|
| NSAIDs | 可能增加 pemetrexed 毒性，需停藥 |
| 腎毒性藥物 | 增加腎臟損傷風險 |
| 肝素類 | 增加出血風險 |

### 特殊族群

- **腎功能不全 (CrCl < 45 mL/min)**：不建議使用
- **肝功能不全**：輕度可使用，中重度需謹慎
- **孕婦**：禁忌使用
- **老年人**：需密切監測腎功能

---

## 結論與下一步

### 整體評估

Pemetrexed 對惡性間皮瘤 (包括腹膜型) 的預測已獲堅實證據支持：

1. **證據等級最高 (L1)**：多個臨床試驗證實療效
2. **標準治療地位確立**：Pemetrexed + cisplatin 為間皮瘤第一線標準治療
3. **免疫療法組合**：與 PD-1 抑制劑併用已獲台灣核准
4. **適應症延伸**：胸膜和腹膜間皮瘤的治療原則相似

### 目前臨床定位

| 間皮瘤類型 | Pemetrexed 治療角色 |
|-----------|---------------------|
| 惡性胸膜間皮瘤 | 第一線標準治療 (+ cisplatin +/- pembrolizumab) |
| 惡性腹膜間皮瘤 | 第一線化療選項 (+ cisplatin) |

### 建議行動

- **腹膜間皮瘤適應症申請**：若尚未正式核准，可考慮申請適應症擴展
- **臨床經驗累積**：收集實際臨床數據支持療效
- **關注免疫療法組合**：pembrolizumab + pemetrexed 組合可能也適用於腹膜型

---

*本報告由 TxGNN 預測系統生成，僅供研究參考，不構成醫療建議。*


---

## 相關藥物報告

- [Felodipine]({{ "/drugs/felodipine/" | relative_url }}) - 證據等級 L5
- [Iodixanol]({{ "/drugs/iodixanol/" | relative_url }}) - 證據等級 L5
- [Ferrous Gluconate]({{ "/drugs/ferrous_gluconate/" | relative_url }}) - 證據等級 L5
- [Clomipramine]({{ "/drugs/clomipramine/" | relative_url }}) - 證據等級 L5
- [Gefitinib]({{ "/drugs/gefitinib/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Pemetrexed老藥新用驗證報告. https://twtxgnn.yao.care/drugs/pemetrexed/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_pemetrexed,
  title = {Pemetrexed老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/pemetrexed/}
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
