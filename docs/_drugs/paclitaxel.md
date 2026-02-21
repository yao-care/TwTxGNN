---
layout: default
title: Paclitaxel
description: "Paclitaxel 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 122
evidence_level: L1
indication_count: 10
---

# Paclitaxel

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Paclitaxel 藥師筆記

## 一句話總結

<p class="key-answer" data-question="Paclitaxel 可以用於治療什麼新適應症？">
Paclitaxel 為紫杉醇類抗腫瘤藥物，TxGNN 預測其對乳癌 (包括三陰性乳癌、雌激素受體陽性乳癌) 有治療潛力，此預測已獲大量 Phase III 臨床試驗證實，證據等級最高。
</p>


---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥品名稱 | Paclitaxel (紫杉醇) |
| DrugBank ID | DB01229 |
| 台灣商品名 | 曲斯若凍晶注射劑、汰癌勝注射劑等 |
| 原適應症 | 卵巢癌、乳癌、非小細胞肺癌、胃癌、食道癌、頭頸癌、膀胱癌、子宮頸癌 |
| 預測新適應症 | 女性乳腺癌、hereditary breast ovarian cancer syndrome、estrogen-receptor negative breast cancer、hormone-resistant breast carcinoma、estrogen-receptor positive breast cancer、Ehrlich tumor carcinoma、bilateral breast carcinoma、breast carcinoma by gene expression profile、nipple carcinoma、ovarian clear cell adenocarcinoma |
| 證據等級 | L1 (多個 RCT) |
| TxGNN 預測分數 | 0.999+ |

---



## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. female breast carcinoma</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">100.00%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>### 機轉連結</p>

<ol>
<li><strong>微管穩定作用</strong>：Paclitaxel 結合 beta-tubulin 促進微管聚合並穩定微管，抑制有絲分裂，導致細胞凋亡。</li>

<li><strong>免疫調節作用</strong>：最新研究顯示 paclitaxel 可調節腫瘤相關巨噬細胞 (TAM)，增強 PD-1 阻斷劑的療效。</li>

<li><strong>克服荷爾蒙抗性</strong>：對於荷爾蒙治療無效的 ER+ 乳癌，化療仍是重要選項，paclitaxel 透過不依賴荷爾蒙受體的機制發揮作用。</li>
</ol>

<h3>臨床試驗</h3>

<p>### 已完成的 Phase III 試驗</p>

<table>
<thead>
<tr>
<th>試驗編號</th>
<th>疾病</th>
<th>療法</th>
<th>狀態</th>
<th>主要發現</th>
</tr>
</thead>
<tbody>
<tr>
<td>NCT00281658</td>
<td>ErbB2 陽性轉移性乳癌</td>
<td>Lapatinib + Paclitaxel vs Paclitaxel</td>
<td>完成</td>
<td>評估整體存活期</td>
</tr>
<tr>
<td>NCT01583426</td>
<td>早期乳癌</td>
<td>Nab-paclitaxel vs 傳統 Paclitaxel</td>
<td>完成</td>
<td>比較病理完全反應率</td>
</tr>
<tr>
<td>NCT03725059</td>
<td>ER+/HER2- 乳癌</td>
<td>Pembrolizumab + 化療 (含 Paclitaxel)</td>
<td>招募中</td>
<td>評估 pCR 及 EFS</td>
</tr>
</tbody>
</table>

<h3>相關文獻</h3>

<p>### 三陰性乳癌 (TNBC)</p>

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
<td>31783552</td>
<td>2019</td>
<td>綜述</td>
<td>Paclitaxel 是 TNBC 第一線治療藥物，nab-PTX 可提高療效並降低副作用</td>
</tr>
<tr>
<td>39009452</td>
<td>2024</td>
<td>基礎研究</td>
<td>Paclitaxel 透過 TLR4 調節 TAM，增強 PD-1 阻斷劑療效</td>
</tr>
<tr>
<td>35795050</td>
<td>2022</td>
<td>綜述</td>
<td>TNBC 免疫療法進展，Pembrolizumab + 化療已成為標準治療</td>
</tr>
<tr>
<td>35976445</td>
<td>2023</td>
<td>綜述</td>
<td>三陰性乳癌核准治療選項及其作用機轉</td>
</tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. estrogen-receptor negative breast cancer</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.91%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（50 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01777932" target="_blank">NCT01777932</a></td><td>N/A</td><td>COMPLETED</td><td>220</td><td>A Multicenter, Single-arm, Observational Study Describing the Clinical Benefits ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04132817" target="_blank">NCT04132817</a></td><td>PHASE1</td><td>COMPLETED</td><td>12</td><td>A Phase 1 Multi-Targeted Study to Promote Anti-Tumor Immunity in ER Positive, HE...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02734290" target="_blank">NCT02734290</a></td><td>PHASE1, PHASE2</td><td>ACTIVE_NOT_RECRUITING</td><td>29</td><td>A Pilot and Phase II Study to Assess the Safety, Tolerability and Efficacy of Pe...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04152057" target="_blank">NCT04152057</a></td><td>PHASE1, PHASE2</td><td>UNKNOWN</td><td>20</td><td>A Single-arm, Exploratory Clinical Study of Pyrotinib Maleate Tablets Combined W...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01897441" target="_blank">NCT01897441</a></td><td>NA</td><td>TERMINATED</td><td>31</td><td>Prospective Tissue Collection in Breast Cancer Patients Receiving Preoperative S...</td></tr>
</tbody>
</table>
<p><em>...及其他 45 項試驗</em></p>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38771995/" target="_blank">38771995</a></td><td>2024</td><td>Article</td><td>Journal of clinical </td><td>Final Results of RIGHT Choice: Ribociclib Plus Endocrine The...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/33015734/" target="_blank">33015734</a></td><td>2021</td><td>Article</td><td>Cancer immunology, i</td><td>Pembrolizumab and atezolizumab in triple-negative breast can...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/37440239/" target="_blank">37440239</a></td><td>2023</td><td>Article</td><td>JAMA oncology</td><td>Efficacy of Metronomic Oral Vinorelbine, Cyclophosphamide, a...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/37526149/" target="_blank">37526149</a></td><td>2023</td><td>Article</td><td>Future oncology (Lon</td><td>TROPION-Breast02: Datopotamab deruxtecan for locally recurre...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39838117/" target="_blank">39838117</a></td><td>2025</td><td>Article</td><td>Nature medicine</td><td>Pembrolizumab and chemotherapy in high-risk, early-stage, ER...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. hormone-resistant breast carcinoma</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.91%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（14 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03285607" target="_blank">NCT03285607</a></td><td>PHASE1</td><td>WITHDRAWN</td><td>0</td><td>Phase I Study of MCS110 Combined With Neoadjuvant Dose-Dense Doxorubicin, Cyclop...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02616848" target="_blank">NCT02616848</a></td><td>PHASE1</td><td>UNKNOWN</td><td>1</td><td>Safety and Tolerability of Everolimus in Combination With Eribulin in Triple-neg...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04771871" target="_blank">NCT04771871</a></td><td>PHASE2</td><td>UNKNOWN</td><td>42</td><td>Treatment Response and microRNA Profiles in Triple Negative Breast Cancer Patien...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02603679" target="_blank">NCT02603679</a></td><td>PHASE2</td><td>ACTIVE_NOT_RECRUITING</td><td>181</td><td>PREDIX Luminal B - Neoadjuvant Response-guided Treatment of ER Positive Tumors W...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01031446" target="_blank">NCT01031446</a></td><td>PHASE1, PHASE2</td><td>COMPLETED</td><td>55</td><td>A Phase Ib/II Study of Cisplatin, Paclitaxel, and RAD001 in Patients With Metast...</td></tr>
</tbody>
</table>
<p><em>...及其他 9 項試驗</em></p>

<h3>相關文獻（9 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/9071337/" target="_blank">9071337</a></td><td>1997</td><td>Article</td><td>Seminars in oncology</td><td>Response to estramustine phosphate and paclitaxel in patient...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/8091238/" target="_blank">8091238</a></td><td>1994</td><td>Article</td><td>Seminars in oncology</td><td>Salvage chemotherapy of breast cancer.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/34781168/" target="_blank">34781168</a></td><td>2021</td><td>Article</td><td>European journal of </td><td>TAKTIC: A prospective, multicentre, uncontrolled, phase IB/I...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/7481851/" target="_blank">7481851</a></td><td>1995</td><td>Article</td><td>Seminars in oncology</td><td>Management of breast cancer: status and future trends.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/9374083/" target="_blank">9374083</a></td><td>1997</td><td>Article</td><td>Seminars in oncology</td><td>Chemotherapy of breast cancer: a historical perspective.</td></tr>
</tbody>
</table>
<p><em>...及其他 4 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. estrogen-receptor positive breast cancer</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.91%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（50 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01777932" target="_blank">NCT01777932</a></td><td>N/A</td><td>COMPLETED</td><td>220</td><td>A Multicenter, Single-arm, Observational Study Describing the Clinical Benefits ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06202261" target="_blank">NCT06202261</a></td><td>PHASE1, PHASE2</td><td>RECRUITING</td><td>154</td><td>A Phase Ib/II Clinical Trial to Evaluate the Safety and Efficacy of TQB2930 for ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04132817" target="_blank">NCT04132817</a></td><td>PHASE1</td><td>COMPLETED</td><td>12</td><td>A Phase 1 Multi-Targeted Study to Promote Anti-Tumor Immunity in ER Positive, HE...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04152057" target="_blank">NCT04152057</a></td><td>PHASE1, PHASE2</td><td>UNKNOWN</td><td>20</td><td>A Single-arm, Exploratory Clinical Study of Pyrotinib Maleate Tablets Combined W...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01897441" target="_blank">NCT01897441</a></td><td>NA</td><td>TERMINATED</td><td>31</td><td>Prospective Tissue Collection in Breast Cancer Patients Receiving Preoperative S...</td></tr>
</tbody>
</table>
<p><em>...及其他 45 項試驗</em></p>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38771995/" target="_blank">38771995</a></td><td>2024</td><td>Article</td><td>Journal of clinical </td><td>Final Results of RIGHT Choice: Ribociclib Plus Endocrine The...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/37440239/" target="_blank">37440239</a></td><td>2023</td><td>Article</td><td>JAMA oncology</td><td>Efficacy of Metronomic Oral Vinorelbine, Cyclophosphamide, a...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30413379/" target="_blank">30413379</a></td><td>2018</td><td>Article</td><td>The Lancet. Oncology</td><td>Neoadjuvant chemotherapy with or without anthracyclines in t...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39838117/" target="_blank">39838117</a></td><td>2025</td><td>Article</td><td>Nature medicine</td><td>Pembrolizumab and chemotherapy in high-risk, early-stage, ER...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39631485/" target="_blank">39631485</a></td><td>2024</td><td>Article</td><td>Pharmacological rese</td><td>Targeted and cytotoxic inhibitors used in the treatment of b...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. Ehrlich tumor carcinoma</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.91%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（1 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04885270" target="_blank">NCT04885270</a></td><td>PHASE3</td><td>UNKNOWN</td><td>50</td><td>Phase III Clinical Trial of Intravenous Paclitaxel Plus Intraperitoneal Cisplati...</td></tr>
</tbody>
</table>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30342146/" target="_blank">30342146</a></td><td>2019</td><td>Article</td><td>International journa</td><td>Acylated chitosan anchored paclitaxel loaded liposomes: Phar...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/31002367/" target="_blank">31002367</a></td><td>2019</td><td>Article</td><td>Oncology reports</td><td>Dietary baker&#x27;s yeast sensitizes Ehrlich mammary adenocarcin...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/27426109/" target="_blank">27426109</a></td><td>2016</td><td>Article</td><td>International journa</td><td>Heparin modification enhances the delivery and tumor targeti...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26500095/" target="_blank">26500095</a></td><td>2016</td><td>Article</td><td>Tumour biology : the</td><td>The combination of thymoquinone and paclitaxel shows anti-tu...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/17385543/" target="_blank">17385543</a></td><td>2007</td><td>Article</td><td>Acta biologica Hunga</td><td>Evaluation of the effect of paclitaxel, epirubicin and tamox...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. bilateral breast carcinoma</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.89%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（5 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02364726" target="_blank">NCT02364726</a></td><td>NA</td><td>COMPLETED</td><td>28</td><td>Acupuncture to Reduce Chemotherapy-induced Peripheral Neuropathy Severity During...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04461977" target="_blank">NCT04461977</a></td><td>NA</td><td>COMPLETED</td><td>60</td><td>Acupuncture for Treatment of Peripheral Neuropathy Induced by Neoadjuvant or Adj...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02457039" target="_blank">NCT02457039</a></td><td>NA</td><td>COMPLETED</td><td>93</td><td>An Assessor-Blinded, Randomised Controlled Trial of Acupuncture to Prevent Chemo...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03873272" target="_blank">NCT03873272</a></td><td>NA</td><td>COMPLETED</td><td>63</td><td>Randomized Controlled Selection Trial of Cryotherapy vs. Compression Therapy for...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05861830" target="_blank">NCT05861830</a></td><td>PHASE3</td><td>RECRUITING</td><td>80</td><td>An Exploratory Study on Predicting the Efficacy of Dalpiciclib in Combination Wi...</td></tr>
</tbody>
</table>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/40690248/" target="_blank">40690248</a></td><td>2025</td><td>Article</td><td>JAMA</td><td>Ovarian Cancer: A Review.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36068624/" target="_blank">36068624</a></td><td>2022</td><td>Article</td><td>International journa</td><td>Bilateral intermediate uveitis following treatment with pacl...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36335424/" target="_blank">36335424</a></td><td>2022</td><td>Article</td><td>The American journal</td><td>Gynecomastia and Malignancy: A Case of Male Invasive Ductal ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/25978147/" target="_blank">25978147</a></td><td>2017</td><td>Article</td><td>Journal of chemother</td><td>Paclitaxel-induced pneumonitis in patients with breast cance...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/11876386/" target="_blank">11876386</a></td><td>2002</td><td>Article</td><td>European journal of </td><td>Primary breast carcinoma of the vulva: case report and revie...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. breast carcinoma by gene expression profile</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.89%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（45 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02628132" target="_blank">NCT02628132</a></td><td>PHASE1, PHASE2</td><td>COMPLETED</td><td>22</td><td>Study of the Safety, Tolerability and Efficacy of the Investigational Anti PD-L1...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00589238" target="_blank">NCT00589238</a></td><td>PHASE2</td><td>TERMINATED</td><td>16</td><td>Randomised Phase II Trial of Neoadjuvant Weekly Paclitaxel Plus Carboplatin Comp...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03725436" target="_blank">NCT03725436</a></td><td>PHASE1</td><td>ACTIVE_NOT_RECRUITING</td><td>35</td><td>A Phase 1b Study of ALRN-6924 in Combination With Paclitaxel in Wild-Type TP53 A...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01722968" target="_blank">NCT01722968</a></td><td>PHASE2</td><td>COMPLETED</td><td>33</td><td>A Prospective Randomized Phase II Study to Identify Predictive Biomarkers and Me...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00499291" target="_blank">NCT00499291</a></td><td>NA</td><td>WITHDRAWN</td><td>0</td><td>Pharmacokinetic, Pharmacodynamic and Pharmacogenetic Study of Nab-Paclitaxel (Na...</td></tr>
</tbody>
</table>
<p><em>...及其他 40 項試驗</em></p>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26372358/" target="_blank">26372358</a></td><td>2016</td><td>Article</td><td>Molecular oncology</td><td>Genomic signatures for paclitaxel and gemcitabine resistance...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39400682/" target="_blank">39400682</a></td><td>2024</td><td>Article</td><td>Medical oncology (No</td><td>Glycolytic pathway analysis and gene expression profiles of ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30426838/" target="_blank">30426838</a></td><td>2018</td><td>Article</td><td>Molecular pain</td><td>Expression of mitochondrial dysfunction-related genes and pa...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36602784/" target="_blank">36602784</a></td><td>2023</td><td>Article</td><td>JAMA oncology</td><td>Prognostic and Predictive Value of Immune-Related Gene Expre...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/27094684/" target="_blank">27094684</a></td><td>2016</td><td>Article</td><td>Scientific reports</td><td>Genome-wide profiles of methylation, microRNAs, and gene exp...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. nipple carcinoma</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.89%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（2 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03875573" target="_blank">NCT03875573</a></td><td>PHASE2</td><td>ACTIVE_NOT_RECRUITING</td><td>147</td><td>Neo-adjuvant Chemotherapy Combined With Stereotactic Body Radiotherapy to the Pr...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00616967" target="_blank">NCT00616967</a></td><td>PHASE2</td><td>ACTIVE_NOT_RECRUITING</td><td>68</td><td>A Multi-Institutional Double-Blind Phase II Study Evaluating Response and Surrog...</td></tr>
</tbody>
</table>

<h3>相關文獻（10 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39233823/" target="_blank">39233823</a></td><td>2024</td><td>Article</td><td>Oncology letters</td><td>Neoadjuvant chemotherapy for primary invasive ductal carcino...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/33827325/" target="_blank">33827325</a></td><td>2021</td><td>Article</td><td>International journa</td><td>Acinic Cell Carcinoma of the Breast: Report of a Case With I...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/37064212/" target="_blank">37064212</a></td><td>2023</td><td>Article</td><td>Case reports in wome</td><td>Ovarian high-grade serous carcinoma with estrogenic manifest...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/29514832/" target="_blank">29514832</a></td><td>2018</td><td>Article</td><td>BMJ case reports</td><td>Rare case of metaplastic breast cancer in a man.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38741768/" target="_blank">38741768</a></td><td>2024</td><td>Article</td><td>Frontiers in medicin</td><td>Untypical bilateral breast cancer with peritoneal fibrosis o...</td></tr>
</tbody>
</table>
<p><em>...及其他 5 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. parameningeal embryonal rhabdomyosarcoma</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.73%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. botryoid-type embryonal rhabdomyosarcoma of the vagina</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.73%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>


## 台灣上市資訊

Paclitaxel 在台灣有多種製劑核准上市，包括：

- 傳統溶劑型 Paclitaxel 注射劑
- Nab-paclitaxel (白蛋白結合型)
- Paclitaxel 微脂粒注射劑

原適應症已涵蓋乳癌的多種類型。

---

## 安全性考量

### 重要警語

- **過敏反應**：傳統製劑含 Cremophor EL，可能導致嚴重過敏反應，需預防給藥
- **骨髓抑制**：嗜中性球低下為劑量限制毒性
- **周邊神經病變**：累積劑量相關，可能不可逆
- **心臟毒性**：與 anthracycline 併用時需注意

### 常見副作用

| 副作用 | 發生率 |
|--------|--------|
| 骨髓抑制 | 非常常見 |
| 周邊神經病變 | 常見 |
| 肌肉關節痛 | 常見 |
| 噁心嘔吐 | 常見 |
| 掉髮 | 非常常見 |

### 藥物交互作用

- **CYP3A4 及 CYP2C8 抑制劑**：可能增加 paclitaxel 血中濃度
- **CYP3A4 誘導劑**：可能降低療效
- **Anthracyclines**：建議先給 paclitaxel 再給 anthracycline

### 特殊族群

- **肝功能不全**：需根據膽紅素及 AST 調整劑量
- **孕婦**：禁忌使用
- **老年人**：周邊神經病變風險較高

---




### 藥物-食物交互作用 (DFI)

<div class="dfi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**葡萄柚汁** 🟡 Moderate
- 影響：影響藥物代謝。可能增加藥物血中濃度。
- 建議：需監測療效或不良反應。可能需調整劑量。避免食用葡萄柚或葡萄柚汁。

### 藥物-草藥交互作用 (DHI)

**聖約翰草（貫葉連翹）** 🔴 Major
- 影響：聖約翰草降低化療藥物療效
- 建議：化療期間禁用所有草藥補充品


## 結論與下一步

### 整體評估

Paclitaxel 對乳癌的預測已獲得最高等級的臨床證據支持：

1. **證據等級最高 (L1)**：多個 Phase III 臨床試驗證實療效
2. **機轉清晰**：微管穩定及免疫調節雙重作用
3. **臨床應用成熟**：已是乳癌標準治療的重要組成部分
4. **持續創新**：與免疫療法併用的新組合正在研究中

### 目前臨床定位

| 乳癌亞型 | Paclitaxel 在治療中的角色 |
|----------|---------------------------|
| 三陰性乳癌 | 第一線化療核心藥物，常與免疫療法併用 |
| HER2+ 乳癌 | 與 trastuzumab 併用的標準方案 |
| ER+/HER2- 乳癌 | 荷爾蒙治療無效後的化療選項 |
| 發炎性乳癌 | 前導化療的重要成分 |

### 建議行動

- **持續作為標準治療**：Paclitaxel 在乳癌治療中的地位已確立
- **關注新組合療法**：與 PD-1/PD-L1 抑制劑的併用研究
- **個人化醫療**：根據生物標記選擇最適合的治療組合

---

*本報告由 TxGNN 預測系統生成，僅供研究參考，不構成醫療建議。*


---

## 相關藥物報告

- [Benzylpenicillin]({{ "/drugs/benzylpenicillin/" | relative_url }}) - 證據等級 L5
- [Allopurinol]({{ "/drugs/allopurinol/" | relative_url }}) - 證據等級 L5
- [Cerliponase Alfa]({{ "/drugs/cerliponase_alfa/" | relative_url }}) - 證據等級 L5
- [Thiamine]({{ "/drugs/thiamine/" | relative_url }}) - 證據等級 L5
- [Buprenorphine]({{ "/drugs/buprenorphine/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Paclitaxel老藥新用驗證報告. https://twtxgnn.yao.care/drugs/paclitaxel/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_paclitaxel,
  title = {Paclitaxel老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/paclitaxel/}
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
