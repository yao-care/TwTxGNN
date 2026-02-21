---
layout: default
title: Dupilumab
description: "Dupilumab 的老藥新用潛力分析。中等證據等級 L3，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 中證據等級 (L3-L4)
nav_order: 64
evidence_level: L1
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
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p><p class="key-answer" data-question="這個藥物的作用機轉是什麼？"></p>
<p>Dupilumab 是一種人源化單株抗體，可阻斷 IL-4 和 IL-13 的訊號傳遞，</p>
<p>這兩種細胞因子是第二型發炎反應的關鍵介質。支氣管炎，特別是嗜酸性支氣管炎，</p>
<p>涉及類似的發炎機轉。Dupilumab 已核准用於嗜酸性白血球表現型的氣喘，</p>
<p>其對下呼吸道發炎的抑制作用可能延伸至支氣管炎的治療。</p>
<p></p></p>

<p><div class="key-takeaway"></p>
<p>此預測基於藥物的作用機轉，與現有臨床證據方向一致。</p>

<h3>臨床試驗</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04362501" target="_blank">NCT04362501</a></td><td>PHASE2</td><td>COMPLETED</td><td>33</td><td>Efficacy of Dupilumab for Patients With Chronic Rhinosinusitis Without Nasal Pol...</td></tr>
</tbody>
</table>

<h3>相關文獻</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/34597534/" target="_blank">34597534</a></td><td>2022</td><td>Article</td><td>The Lancet. Respiratory medici</td><td>Long-term safety and efficacy of dupilumab in patients with moderate-to-severe a...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30273510/" target="_blank">30273510</a></td><td>2019</td><td>Article</td><td>The Journal of asthma : offici</td><td>Dupilumab safety and efficacy in uncontrolled asthma: a systematic review and me...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39904363/" target="_blank">39904363</a></td><td>2025</td><td>Article</td><td>Tuberculosis and respiratory d</td><td>Pharmacologic Therapies for Preventing Chronic Obstructive Pulmonary Disease Exa...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30196731/" target="_blank">30196731</a></td><td>2018</td><td>Article</td><td>Expert opinion on pharmacother</td><td>Challenges in the management of asthma associated with smoking-induced airway di...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38488768/" target="_blank">38488768</a></td><td>2024</td><td>Article</td><td>Pediatric pulmonology</td><td>Novel therapies for eosinophilic pediatric plastic bronchitis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/32428511/" target="_blank">32428511</a></td><td>2020</td><td>Article</td><td>Chest</td><td>Effects of Anti-T2 Biologic Treatment on Lung Ventilation Evaluated by MRI in Ad...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. dermatitis</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.71%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（50 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03884842" target="_blank">NCT03884842</a></td><td>PHASE3</td><td>COMPLETED</td><td>24</td><td>A Two-arm, Placebo-controlled Randomized Clinical Trial to Evaluate the Effect o...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03346434" target="_blank">NCT03346434</a></td><td>PHASE2, PHASE3</td><td>COMPLETED</td><td>202</td><td>A Phase 2/3 Study Investigating the Pharmacokinetics, Safety, and Efficacy of Du...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05268107" target="_blank">NCT05268107</a></td><td>PHASE4</td><td>RECRUITING</td><td>30</td><td>Ethnic Differences in Mechanisms of Action of Dupilumab</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04183335" target="_blank">NCT04183335</a></td><td>PHASE3</td><td>COMPLETED</td><td>151</td><td>A Randomized, Double Blind, Placebo-controlled, Multi-center, Parallel Group Stu...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05527964" target="_blank">NCT05527964</a></td><td>N/A</td><td>COMPLETED</td><td>146</td><td>The Influence of Specific Targeted Therapy on Subject and Family Quality of Life...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04244006" target="_blank">NCT04244006</a></td><td>PHASE2, PHASE3</td><td>UNKNOWN</td><td>24</td><td>A Randomized Double-blinded Pilot Study of the Efficacy and Safety of Dupilumab ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06193434" target="_blank">NCT06193434</a></td><td>PHASE1</td><td>COMPLETED</td><td>99</td><td>A Phase 1 FIH, Randomized, Double Blind, Placebo Controlled, SAD/MAD Study to As...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02407756" target="_blank">NCT02407756</a></td><td>PHASE2</td><td>COMPLETED</td><td>78</td><td>A Phase 2a Study Investigating the Safety, Pharmacokinetics, Immunogenicity, and...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05128383" target="_blank">NCT05128383</a></td><td>PHASE2</td><td>COMPLETED</td><td>20</td><td>An Open-label Proof of Concept Study Regarding the Efficacy and Safety of Dupilu...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06687980" target="_blank">NCT06687980</a></td><td>PHASE3</td><td>ACTIVE_NOT_RECRUITING</td><td>138</td><td>A Phase 3, Randomized, Double-blind, Placebo-controlled, Parallel-group Study to...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04066998" target="_blank">NCT04066998</a></td><td>NA</td><td>UNKNOWN</td><td>15</td><td>Cytokine Profile of Conjunctivitis, Performed Through Tears Analysis Among Patie...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03057860" target="_blank">NCT03057860</a></td><td>N/A</td><td>RECRUITING</td><td>2800</td><td>TREATgermany: German National Clinical Registry: Treatment and Medical Care of P...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04306965" target="_blank">NCT04306965</a></td><td>PHASE2</td><td>COMPLETED</td><td>10</td><td>Apremilast 30 mg BID Combined With Dupilumab for the Treatment of Recalcitrant M...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03411837" target="_blank">NCT03411837</a></td><td>N/A</td><td>TERMINATED</td><td>46</td><td>Dupilumab Registry Study</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05203380" target="_blank">NCT05203380</a></td><td>N/A</td><td>COMPLETED</td><td>45</td><td>Neuropsychologic Assessments of Dupilumab-Treated Adolescents With Moderate-to-S...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05197023" target="_blank">NCT05197023</a></td><td>PHASE1</td><td>UNKNOWN</td><td>20</td><td>A RANDOMIZED, DOUBLE-BLIND, DOSE-ESCALATION, PLACEBO-CONTROLLED PHASE I CLINICAL...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06136767" target="_blank">NCT06136767</a></td><td>N/A</td><td>RECRUITING</td><td>400</td><td>Registry for Systemic Eczema Treatments</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04345367" target="_blank">NCT04345367</a></td><td>PHASE3</td><td>COMPLETED</td><td>727</td><td>A PHASE 3B RANDOMIZED, DOUBLE-BLIND, DOUBLE-DUMMY, ACTIVE CONTROLLED MULTI-CENTE...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06884891" target="_blank">NCT06884891</a></td><td>PHASE3</td><td>NOT_YET_RECRUITING</td><td>520</td><td>A Multicenter Randomized, Double-blinded, Parallel, Positive-controlled, Phase Ⅲ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04447417" target="_blank">NCT04447417</a></td><td>PHASE4</td><td>COMPLETED</td><td>52</td><td>Open Label Exploratory Study to Evaluate the Effect of Dupilumab on Skin Barrier...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06099704" target="_blank">NCT06099704</a></td><td>N/A</td><td>ACTIVE_NOT_RECRUITING</td><td>305</td><td>A Prospective, Observational Study of Canadian Patients Receiving Dupixent® for ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT07187089" target="_blank">NCT07187089</a></td><td>PHASE4</td><td>WITHDRAWN</td><td>0</td><td>An Open-Label, Single-Arm Study to Assess Growth and Bone Mineral Density in Chi...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05649098" target="_blank">NCT05649098</a></td><td>EARLY_PHASE1</td><td>RECRUITING</td><td>30</td><td>Repurposing Dupilumab for Management of Pruritic Genetic Inflammatory Skin Disor...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06169527" target="_blank">NCT06169527</a></td><td>N/A</td><td>ACTIVE_NOT_RECRUITING</td><td>303</td><td>French Prospective Observational Study of Patients Receiving Dupilumab for Atopi...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05070663" target="_blank">NCT05070663</a></td><td>N/A</td><td>COMPLETED</td><td>105</td><td>National, Multicentre, Non-interventional, Prospective and Retrospective Study i...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03345914" target="_blank">NCT03345914</a></td><td>PHASE3</td><td>COMPLETED</td><td>367</td><td>A Randomized, Double-blind, Placebo-controlled Study to Investigate the Efficacy...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03389893" target="_blank">NCT03389893</a></td><td>PHASE4</td><td>TERMINATED</td><td>72</td><td>Effect of Dupilumab (Anti-IL4Rα) on the Host-Microbe Interface in Atopic Dermati...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05442645" target="_blank">NCT05442645</a></td><td>N/A</td><td>COMPLETED</td><td>80</td><td>Observational Study of Atopic Dermatitis Patients Treated With Dupilumab in Taiw...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06687967" target="_blank">NCT06687967</a></td><td>PHASE3</td><td>ACTIVE_NOT_RECRUITING</td><td>142</td><td>A Phase 3, Randomized, Double-blind, Placebo-controlled, Parallel-group Study to...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06004986" target="_blank">NCT06004986</a></td><td>PHASE4</td><td>RECRUITING</td><td>216</td><td>DUPI REDUCE Trial (DUPIlumab Dose REDUCtion in Patients With Controlled Atopic E...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01949311" target="_blank">NCT01949311</a></td><td>PHASE3</td><td>COMPLETED</td><td>2733</td><td>An Open-label Study of Dupilumab in Patients With Atopic Dermatitis Who Particip...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05602207" target="_blank">NCT05602207</a></td><td>PHASE4</td><td>COMPLETED</td><td>24</td><td>Clinical and Molecular Effects of Abrocitinib in Subjects With Atopic Dermatitis...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05436535" target="_blank">NCT05436535</a></td><td>PHASE4</td><td>COMPLETED</td><td>433</td><td>Longitudinal Endotyping Of Atopic Dermatitis Through Transcriptomic Skin Analysi...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06477653" target="_blank">NCT06477653</a></td><td>PHASE2</td><td>RECRUITING</td><td>30</td><td>A Pilot Phase 2 Study of the Safety and Efficacy of Dupilumab as Add-on Therapy ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05674695" target="_blank">NCT05674695</a></td><td>N/A</td><td>RECRUITING</td><td>2500</td><td>Spanish Academy of Dermatology and Venereology Registry of Atopic Dermatitis The...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04718870" target="_blank">NCT04718870</a></td><td>PHASE4</td><td>COMPLETED</td><td>41</td><td>Open-label Exploratory Study to Evaluate the Effect of Dupilumab on Skin Barrier...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT07098000" target="_blank">NCT07098000</a></td><td>N/A</td><td>ACTIVE_NOT_RECRUITING</td><td>40</td><td>The Role of Confocal Microscopy in Estimating Dupilumab Treatment Response for M...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05858619" target="_blank">NCT05858619</a></td><td>PHASE4</td><td>RECRUITING</td><td>15</td><td>Molecular Signatures of Cutaneous Dupilumab Response</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06192563" target="_blank">NCT06192563</a></td><td>N/A</td><td>RECRUITING</td><td>150</td><td>A Prospective Observational Study of Adolescent Patients With Severe Atopic Derm...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05394792" target="_blank">NCT05394792</a></td><td>N/A</td><td>COMPLETED</td><td>111</td><td>CANadian Effectiveness of UPadacitinib in Adult Moderate-to-severe aTopIc derMat...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04287621" target="_blank">NCT04287621</a></td><td>N/A</td><td>ACTIVE_NOT_RECRUITING</td><td>718</td><td>Registry of Asthma Patients Initiating DUPIXENT® (RAPID)</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02277769" target="_blank">NCT02277769</a></td><td>PHASE3</td><td>COMPLETED</td><td>708</td><td>A Phase 3 Confirmatory Study Investigating the Efficacy and Safety of Dupilumab ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05694884" target="_blank">NCT05694884</a></td><td>PHASE2</td><td>UNKNOWN</td><td>75</td><td>A Randomized, Double-Blind, Placebo-Controlled, Multicenter Trial to Evaluate th...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05624112" target="_blank">NCT05624112</a></td><td>PHASE4</td><td>COMPLETED</td><td>44</td><td>Open-label Exploratory Study to Evaluate the Effect of Dupilumab on Skin Barrier...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02647086" target="_blank">NCT02647086</a></td><td>PHASE1</td><td>COMPLETED</td><td>14</td><td>An Open-Label, Drug-Drug Interaction Study to Examine the Effects of Dupilumab o...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01385657" target="_blank">NCT01385657</a></td><td>PHASE1</td><td>COMPLETED</td><td>37</td><td>A Randomized, Double-Blind, Placebo-Controlled, Sequential Ascending, Repeated-D...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05682976" target="_blank">NCT05682976</a></td><td>N/A</td><td>NOT_YET_RECRUITING</td><td>100</td><td>Prospective Multicentre Study on Ophthalmological Adverse Events of Tralokinumab...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03736967" target="_blank">NCT03736967</a></td><td>PHASE2</td><td>TERMINATED</td><td>206</td><td>A Randomized, Double-Blind, Placebo-Controlled, Phase 2a Study to Assess the Eff...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05331755" target="_blank">NCT05331755</a></td><td>N/A</td><td>COMPLETED</td><td>120</td><td>Real Life Experience Survey of Dupilumab in the Netherlands</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT07352566" target="_blank">NCT07352566</a></td><td>PHASE4</td><td>NOT_YET_RECRUITING</td><td>10</td><td>Utilization of a Cutaneous Therapy In Situ Microdevice</td></tr>
</tbody>
</table>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36214355/" target="_blank">36214355</a></td><td>2022</td><td>Article</td><td>Journal of cutaneous medicine </td><td>Treatment With Dupilumab in Patients With Atopic Dermatitis: Systematic Review a...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30194992/" target="_blank">30194992</a></td><td>2019</td><td>Article</td><td>The Journal of allergy and cli</td><td>Dupilumab progressively improves systemic and cutaneous abnormalities in patient...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/34126094/" target="_blank">34126094</a></td><td>2022</td><td>Article</td><td>Journal of the American Academ</td><td>Management of inadequate response and adverse effects to dupilumab in atopic der...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38560522/" target="_blank">38560522</a></td><td>2024</td><td>Article</td><td>Drug design, development and t</td><td>A Review of Dupilumab in the Treatment of Atopic Dermatitis in Infants and Child...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39588375/" target="_blank">39588375</a></td><td>2024</td><td>Article</td><td>Frontiers in immunology</td><td>Immunogenicity of dupilumab in adult and pediatric patients with atopic dermatit...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28478972/" target="_blank">28478972</a></td><td>2017</td><td>Article</td><td>Lancet (London, England)</td><td>Long-term management of moderate-to-severe atopic dermatitis with dupilumab and ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36705657/" target="_blank">36705657</a></td><td>2023</td><td>Article</td><td>Dermatitis : contact, atopic, </td><td>Dupilumab for Atopic Dermatitis-From Clinical Trials to Molecular and Cellular M...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/32892674/" target="_blank">32892674</a></td><td>2020</td><td>Article</td><td>Immunotherapy</td><td>Dupilumab use in atopic dermatitis and beyond in skin diseases.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35567671/" target="_blank">35567671</a></td><td>2022</td><td>Article</td><td>American journal of clinical d</td><td>Long-Term Efficacy and Safety of Dupilumab in Adolescents with Moderate-to-Sever...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/40246083/" target="_blank">40246083</a></td><td>2025</td><td>Article</td><td>Journal of the American Academ</td><td>Abrocitinib versus dupilumab: Impact on skin barrier function and proteomics in ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/37100035/" target="_blank">37100035</a></td><td>2023</td><td>Article</td><td>Dermatology (Basel, Switzerlan</td><td>Dupilumab-Associated Psoriasis and Psoriasiform Manifestations: A Scoping Review...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/33428978/" target="_blank">33428978</a></td><td>2021</td><td>Article</td><td>Journal of the American Academ</td><td>Facial and neck erythema associated with dupilumab treatment: A systematic revie...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39818381/" target="_blank">39818381</a></td><td>2025</td><td>Article</td><td>International journal of biolo</td><td>AP2M1 as the potential biomarker for prediction of the response of atopic dermat...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/25006719/" target="_blank">25006719</a></td><td>2014</td><td>Article</td><td>The New England journal of med</td><td>Dupilumab treatment in adults with moderate-to-severe atopic dermatitis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/31109652/" target="_blank">31109652</a></td><td>2019</td><td>Article</td><td>Journal of dermatological scie</td><td>Efficacy and safety of dupilumab monotherapy in adults with moderate-to-severe a...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/32822798/" target="_blank">32822798</a></td><td>2021</td><td>Article</td><td>Journal of the American Academ</td><td>Real-world evidence of dupilumab efficacy and risk of adverse events: A systemat...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38588818/" target="_blank">38588818</a></td><td>2024</td><td>Article</td><td>Journal of the American Academ</td><td>Dupilumab therapy for atopic dermatitis is associated with increased risk of cut...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35439608/" target="_blank">35439608</a></td><td>2022</td><td>Article</td><td>Journal of the American Academ</td><td>Phase 3 efficacy and safety of abrocitinib in adults with moderate-to-severe ato...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35503163/" target="_blank">35503163</a></td><td>2022</td><td>Article</td><td>American journal of clinical d</td><td>Dupilumab Provides Acceptable Safety and Sustained Efficacy for up to 4 Years in...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/29471919/" target="_blank">29471919</a></td><td>2018</td><td>Article</td><td>Journal of the American Academ</td><td>Dupilumab: A review of its use in the treatment of atopic dermatitis.</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. acne keloid</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.61%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（1 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/37360650/" target="_blank">37360650</a></td><td>2023</td><td>Article</td><td>JAAD case reports</td><td>Effects of dupilumab on keloid stabilization and prevention.</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. exanthem (disease)</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.57%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（10 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04447417" target="_blank">NCT04447417</a></td><td>PHASE4</td><td>COMPLETED</td><td>52</td><td>Open Label Exploratory Study to Evaluate the Effect of Dupilumab on Skin Barrier...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06012448" target="_blank">NCT06012448</a></td><td>PHASE4</td><td>COMPLETED</td><td>10</td><td>The Immunologic Effects of Dupilumab in the Treatment of Dermal Hypersensitivity...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04718870" target="_blank">NCT04718870</a></td><td>PHASE4</td><td>COMPLETED</td><td>41</td><td>Open-label Exploratory Study to Evaluate the Effect of Dupilumab on Skin Barrier...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05394792" target="_blank">NCT05394792</a></td><td>N/A</td><td>COMPLETED</td><td>111</td><td>CANadian Effectiveness of UPadacitinib in Adult Moderate-to-severe aTopIc derMat...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT07352566" target="_blank">NCT07352566</a></td><td>PHASE4</td><td>NOT_YET_RECRUITING</td><td>10</td><td>Utilization of a Cutaneous Therapy In Situ Microdevice</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06461897" target="_blank">NCT06461897</a></td><td>PHASE3</td><td>RECRUITING</td><td>675</td><td>A Phase 3, Open-label, Efficacy-Assessor-Blinded Study, Comparing the Safety and...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05601882" target="_blank">NCT05601882</a></td><td>PHASE3</td><td>COMPLETED</td><td>920</td><td>A Phase 3b/4 Randomized, Open-label, Efficacy Assessor Blinded Study, Comparing ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04988022" target="_blank">NCT04988022</a></td><td>PHASE4</td><td>COMPLETED</td><td>44</td><td>Defining Reversal of Keloid Lesions by Th2 Targeting With Dupilumab Treatment</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT07021495" target="_blank">NCT07021495</a></td><td>N/A</td><td>RECRUITING</td><td>840</td><td>A Prospective, Multi-Center, Observational Biomarker Real-World Evidence Study f...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06389136" target="_blank">NCT06389136</a></td><td>PHASE3</td><td>RECRUITING</td><td>200</td><td>A Phase 3b/4 Randomized, Open-label, Efficacy Assessor-Blinded Study, to Evaluat...</td></tr>
</tbody>
</table>

<h3>相關文獻（11 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/40375468/" target="_blank">40375468</a></td><td>2025</td><td>Article</td><td>International journal of derma</td><td>Dupilumab for the Treatment of Cutaneous Immune-Related Adverse Events: A System...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/33207021/" target="_blank">33207021</a></td><td>2021</td><td>Article</td><td>Clinical and experimental derm</td><td>Skin manifestations of COVID-19 in children: Part 3.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/40507326/" target="_blank">40507326</a></td><td>2025</td><td>Article</td><td>Cancers</td><td>Interleukin-4 and -13 Gene Expression Profiles in Immune-Related Bullous Pemphig...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38008067/" target="_blank">38008067</a></td><td>2023</td><td>Article</td><td>Respiration; international rev</td><td>Adverse Effects Under Th2 Biologics (Dupilumab and Tezepelumab) in a Patient wit...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/37203799/" target="_blank">37203799</a></td><td>2023</td><td>Article</td><td>International journal of derma</td><td>Detection of novel therapies using a multi-national, multi-institutional registr...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36610660/" target="_blank">36610660</a></td><td>2023</td><td>Article</td><td>The Journal of investigative d</td><td>IL-4/IL-13 Inhibitors for Atopic Dermatitis Induce Psoriatic Rash Transcriptiona...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38013381/" target="_blank">38013381</a></td><td>2023</td><td>Article</td><td>Medicine</td><td>The effect of atopic dermatitis in pediatric patients on height: Reflections tri...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35986706/" target="_blank">35986706</a></td><td>2022</td><td>Article</td><td>Dermatologic therapy</td><td>Successful treatment of secukinumab-resistant palmoplantar pustulosis by Dupilum...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35194901/" target="_blank">35194901</a></td><td>2022</td><td>Article</td><td>Dermatologic therapy</td><td>De novo pustular psoriasis associated with dupilumab therapy in a young male wit...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35796728/" target="_blank">35796728</a></td><td>2022</td><td>Article</td><td>Dermatologic therapy</td><td>An uncommon case of lichen spinulosus induced by dupilumab in a patient treated ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36153663/" target="_blank">36153663</a></td><td>2022</td><td>Article</td><td>Dermatologic therapy</td><td>Pustular psoriasis appearing in a Chinese woman treated with dupilumab for atopi...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. neonatal dermatomyositis</span>
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
<span class="indication-name">6. acrodermatitis chronica atrophicans</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.54%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. amyopathic dermatomyositis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.53%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. secondary interstitial lung disease specific to childhood associated with a connective tissue disease</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.52%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. hydroa vacciniforme, familial</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.50%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. severe nonproliferative diabetic retinopathy</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.10%</span>
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
| 2 張許可證 | 杜避炎注射劑300毫克 | 注射劑 | 異位性皮膚炎、氣喘、慢性鼻竇炎合併鼻息肉、嗜伊紅性食道炎、COPD、慢性自發性蕁麻疹 |

## 安全性考量

- **常見不良反應**：注射部位反應、結膜炎、口唇皰疹
- **重要注意事項**：開始治療前應評估寄生蟲感染，不建議與活病毒疫苗同時使用
- **特殊族群**：兒童使用需按體重調整劑量


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**Helminthiasis** 🟡 Moderate
- 風險包括：感染。必要時應停止治療。

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
