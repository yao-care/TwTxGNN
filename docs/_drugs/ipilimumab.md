---
layout: default
title: Ipilimumab
description: "Ipilimumab 的老藥新用潛力分析。模型預測等級 L5，包含 2 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 91
evidence_level: L1
indication_count: 2
---

# Ipilimumab

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>2</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ipilimumab (易乳莫單抗) - 藥師評估報告

## 一句話總結

<p class="key-answer" data-question="Ipilimumab 可以用於治療什麼新適應症？">
易乳莫單抗是一種抗 CTLA-4 免疫檢查點抑制劑，TxGNN 預測其對非皮膚黑色素瘤有療效，這項預測獲得大量臨床試驗支持，展現了極高的轉譯價值。
</p>

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物學名 | Ipilimumab |
| 台灣商品名 | 益伏注射劑 5 毫克/毫升 (YERVOY) |
| DrugBank ID | DB06186 |
| 原核准適應症 | 無法切除或轉移性黑色素瘤、腎細胞癌、NSCLC、肝細胞癌、大腸直腸癌、食道癌等（多與 nivolumab 併用） |
| 預測新適應症 | metastatic melanoma、choroideremia |
| 最高證據等級 | L1/L2 (多項 RCT 研究) |
| 台灣上市狀態 | 有效許可證 |





## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. choroideremia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.06%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>Ipilimumab 透過阻斷 CTLA-4 來增強 T 細胞活化，解除免疫系統對腫瘤的抑制：</p>

<ol>
<li><strong>非皮膚黑色素瘤</strong> (TxGNN Score: 0.990, Rank: 16733)：</li>
</ol>
<ul>
<li>包括黏膜黑色素瘤、眼部黑色素瘤（葡萄膜黑色素瘤）等</li>
<li>這些亞型較皮膚黑色素瘤少見，但具有相似的免疫原性</li>
<li>Ipilimumab（特別是與 nivolumab 併用）已在這些亞型中顯示療效</li>

</ul>
<ol>
<li><strong>脈絡膜無虹膜症 (Choroideremia)</strong> (TxGNN Score: 0.991, Rank: 16090)：</li>
</ol>
<ul>
<li>這是一種遺傳性視網膜退化疾病，非腫瘤性</li>
<li>此預測的機轉關聯不明，可能為偽陽性</li>
</ul>

<h3>臨床試驗</h3>

<p>目前無針對此特定適應症的臨床試驗登記。</p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. non-cutaneous melanoma</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.02%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（50 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05302921" target="_blank">NCT05302921</a></td><td>PHASE2</td><td>COMPLETED</td><td>5</td><td>Phase II Study Investigating the Efficacy of Neoadjuvant Dual Checkpoint Inhibit...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01827111" target="_blank">NCT01827111</a></td><td>PHASE2</td><td>COMPLETED</td><td>21</td><td>Phase II Study of Abraxane Plus Ipilimumab in Patients With Metastatic Melanoma</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01621490" target="_blank">NCT01621490</a></td><td>PHASE1</td><td>COMPLETED</td><td>170</td><td>An Exploratory Study of the Biologic Effects of Nivolumab and Ipilimumab Monothe...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04074967" target="_blank">NCT04074967</a></td><td>PHASE1, PHASE2</td><td>ACTIVE_NOT_RECRUITING</td><td>70</td><td>A Phase Ib/II Study of ARRY-614 Plus Either Nivolumab or Nivolumab+Ipilimumab in...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01940809" target="_blank">NCT01940809</a></td><td>PHASE1</td><td>TERMINATED</td><td>15</td><td>A Sequential Safety and Biomarker Study of BRAF-MEK Inhibition on the Immune Res...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02659540" target="_blank">NCT02659540</a></td><td>PHASE1</td><td>COMPLETED</td><td>20</td><td>A Pilot (Phase 1) Study to Evaluate the Safety and Efficacy of Combination Check...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04107168" target="_blank">NCT04107168</a></td><td>N/A</td><td>UNKNOWN</td><td>1800</td><td>An Observational Study to Evaluate the Microbiome as a Biomarker of Efficacy and...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02992912" target="_blank">NCT02992912</a></td><td>PHASE2</td><td>ACTIVE_NOT_RECRUITING</td><td>138</td><td>A Phase II Study to Assess the Efficacy of the Anti-PD-L1 Antibody Atezolizumab ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01840007" target="_blank">NCT01840007</a></td><td>PHASE2</td><td>COMPLETED</td><td>20</td><td>Pilot Study Evaluating the Efficacy and Safety of Metformin in Melanoma</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05584670" target="_blank">NCT05584670</a></td><td>PHASE1, PHASE2</td><td>RECRUITING</td><td>542</td><td>A Phase 1/2, Open Label, First-in-human, Dose Escalation and Expansion Study for...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04418167" target="_blank">NCT04418167</a></td><td>PHASE1</td><td>SUSPENDED</td><td>71</td><td>A Phase 1 Study of ERK1/2 Inhibitor JSI-1187 Administered as Monotherapy and in ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03999749" target="_blank">NCT03999749</a></td><td>PHASE2</td><td>ACTIVE_NOT_RECRUITING</td><td>71</td><td>A Phase II Study of the Interleukin-6 Receptor Inhibitor Tocilizumab in Combinat...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06880198" target="_blank">NCT06880198</a></td><td>NA</td><td>RECRUITING</td><td>20</td><td>An Interventional, Not Pharmacological Study to Evaluate Impact® as Support to A...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01838200" target="_blank">NCT01838200</a></td><td>PHASE1</td><td>TERMINATED</td><td>5</td><td>A Phase I Study of Intralesional Bacillus Calmette-Guerin (BCG) and Followed by ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02073123" target="_blank">NCT02073123</a></td><td>PHASE1, PHASE2</td><td>COMPLETED</td><td>132</td><td>A Phase 1/2 Study of the Concomitant Administration of Indoximod Plus Immune Che...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03509584" target="_blank">NCT03509584</a></td><td>PHASE1</td><td>TERMINATED</td><td>6</td><td>Phase I Multicenter Trial Combining Nivolumab, Alone or With Ipilimumab, Plus Hy...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02224768" target="_blank">NCT02224768</a></td><td>N/A</td><td>COMPLETED</td><td>158</td><td>YERVOY Risk Minimisation Tool Evaluation Survey</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01608594" target="_blank">NCT01608594</a></td><td>PHASE1</td><td>COMPLETED</td><td>30</td><td>Neoadjuvant Combination Biotherapy With Ipilimumab (3 mg/kg or 10 mg/kg) and Hig...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03618641" target="_blank">NCT03618641</a></td><td>PHASE2</td><td>COMPLETED</td><td>34</td><td>Neoadjuvant Phase II Study of TLR9 Agonist CMP-001 in Combination With Nivolumab...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03220009" target="_blank">NCT03220009</a></td><td>PHASE2</td><td>WITHDRAWN</td><td>0</td><td>A Randomized Phase II Trial of Adjuvant Nivolumab or Expectant Observation Follo...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04988841" target="_blank">NCT04988841</a></td><td>PHASE2</td><td>COMPLETED</td><td>70</td><td>Prospective randomIzed Clinical Trial Assessing the Tolerance and Clinical Benef...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06581406" target="_blank">NCT06581406</a></td><td>PHASE2, PHASE3</td><td>RECRUITING</td><td>280</td><td>A Randomized, Phase 2/3, Open-Label Study to Investigate the Efficacy and Safety...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04605146" target="_blank">NCT04605146</a></td><td>NA</td><td>RECRUITING</td><td>100</td><td>Impact of Telemonitoring for the Management of Side Effects in Patients with Mel...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04899921" target="_blank">NCT04899921</a></td><td>PHASE2</td><td>TERMINATED</td><td>1</td><td>A Blinded, Randomized Phase 2 Study of Troriluzole in Combination With Ipilimuma...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00796991" target="_blank">NCT00796991</a></td><td>PHASE1</td><td>COMPLETED</td><td>72</td><td>A Randomized, Parallel, 3-arm Study to Characterize the Effect of Ipilimumab + C...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01973608" target="_blank">NCT01973608</a></td><td>PHASE2</td><td>TERMINATED</td><td>12</td><td>A Safety Study for MSB0010445 in Combination With Stereotactic Body Radiation in...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04860076" target="_blank">NCT04860076</a></td><td>N/A</td><td>UNKNOWN</td><td>400</td><td>Open-label, Uncontrolled, Non-Interventional, Retrospective Study to Evaluate Mo...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00972933" target="_blank">NCT00972933</a></td><td>EARLY_PHASE1</td><td>COMPLETED</td><td>59</td><td>Neoadjuvant Anti-CTLA4 Blockade With Ipilimumab in Patients With AJCC Stage IIIB...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04940299" target="_blank">NCT04940299</a></td><td>PHASE2</td><td>ACTIVE_NOT_RECRUITING</td><td>35</td><td>A Phase II Study to Assess the Safety and Efficacy of Tocilizumab in Combination...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01363206" target="_blank">NCT01363206</a></td><td>PHASE2</td><td>COMPLETED</td><td>29</td><td>GM-CSF and Ipilimumab as Therapy in Metastatic Melanoma, a Phase II Study</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04866810" target="_blank">NCT04866810</a></td><td>NA</td><td>SUSPENDED</td><td>24</td><td>The Effect of Diet and Exercise on ImmuNotherapy and the Microbiome (EDEN)</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00871481" target="_blank">NCT00871481</a></td><td>PHASE1, PHASE2</td><td>COMPLETED</td><td>10</td><td>Laboratory-Treated T Cells and Ipilimumab in Treating Patients With Metastatic M...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06999980" target="_blank">NCT06999980</a></td><td>PHASE2</td><td>NOT_YET_RECRUITING</td><td>494</td><td>A Phase II, Multicentre, Parallel Group, Open Label, Randomised Clinical Trial o...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01323517" target="_blank">NCT01323517</a></td><td>PHASE2</td><td>COMPLETED</td><td>26</td><td>A Phase II Trial of The Addition of Ipilimumab (MDX-010) To Isolated Limb Infusi...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06295159" target="_blank">NCT06295159</a></td><td>PHASE2</td><td>RECRUITING</td><td>90</td><td>Neoadjuvant and Adjuvant Anti-PD1 or Combinations for Locoregionally Advanced Me...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01496807" target="_blank">NCT01496807</a></td><td>PHASE1</td><td>COMPLETED</td><td>31</td><td>A Phase Ib Study of Yervoy With Sylatron for Patients With Unresectable Stages I...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03348891" target="_blank">NCT03348891</a></td><td>NA</td><td>COMPLETED</td><td>60</td><td>TNF in Melanoma Patients Treated With Immunotherapy</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02009384" target="_blank">NCT02009384</a></td><td>PHASE2</td><td>TERMINATED</td><td>2</td><td>A Phase II Open-Label Study of Ipilimumab Administered to Stage IIIC and Stage I...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03126110" target="_blank">NCT03126110</a></td><td>PHASE1, PHASE2</td><td>COMPLETED</td><td>145</td><td>A Phase 1/2 Study Exploring the Safety, Tolerability, and Efficacy of INCAGN0187...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03458455" target="_blank">NCT03458455</a></td><td>N/A</td><td>UNKNOWN</td><td>200</td><td>Improved Therapy Response Assessment in Metastatic Brain Tumors</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05428007" target="_blank">NCT05428007</a></td><td>PHASE2</td><td>RECRUITING</td><td>105</td><td>A Phase II Study of the Interleukin-6 Receptor Inhibitor Sarilumab in Combinatio...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04951583" target="_blank">NCT04951583</a></td><td>PHASE2</td><td>ACTIVE_NOT_RECRUITING</td><td>45</td><td>Phase II Trial of Fecal Microbial Transplantation in Patients With Advanced Non-...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05384496" target="_blank">NCT05384496</a></td><td>PHASE2</td><td>RECRUITING</td><td>20</td><td>Phase 2 Study of Axitinib + PD-1 Blockade in Mucosal Melanoma With Pilot Additio...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03469960" target="_blank">NCT03469960</a></td><td>PHASE3</td><td>COMPLETED</td><td>265</td><td>A Randomized Phase 3 Trial Comparing Continuation Nivolumab-Ipilimumab Doublet I...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06116461" target="_blank">NCT06116461</a></td><td>PHASE4</td><td>RECRUITING</td><td>34</td><td>Nivolumab Dose Optimization in Patients With a Complete, Partial or Stable Respo...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00162123" target="_blank">NCT00162123</a></td><td>PHASE2</td><td>COMPLETED</td><td>248</td><td>A Multi-Center, Open-Label, Phase II Study of Ipilimumab (MDX-010 Extended-Treat...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01708941" target="_blank">NCT01708941</a></td><td>PHASE2</td><td>ACTIVE_NOT_RECRUITING</td><td>88</td><td>A Randomized Phase II Study of Ipilimumab at 3 mg/kg or 10 mg/kg Alone or in Com...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02626962" target="_blank">NCT02626962</a></td><td>PHASE2</td><td>COMPLETED</td><td>52</td><td>Phase II Multicenter, Non Randomized, Open Label Trial of Nivolumab in Combinati...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01709162" target="_blank">NCT01709162</a></td><td>PHASE2</td><td>TERMINATED</td><td>31</td><td>A Randomized, Open-Label, Multicenter Phase II Study of Ipilimumab Retreatment V...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01844505" target="_blank">NCT01844505</a></td><td>PHASE3</td><td>COMPLETED</td><td>945</td><td>A Phase 3, Randomized, Double-Blind Study of Nivolumab Monotherapy or Nivolumab ...</td></tr>
</tbody>
</table>

<h3>相關文獻（5 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/24999899/" target="_blank">24999899</a></td><td>2014</td><td>Article</td><td>The Medical journal of Austral</td><td>Ipilimumab in pretreated patients with unresectable or metastatic cutaneous, uve...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28183255/" target="_blank">28183255</a></td><td>2018</td><td>Article</td><td>Current cancer drug targets</td><td>Melanoma Adjuvant Treatment: Current Insight and Clinical Features.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/29466692/" target="_blank">29466692</a></td><td>2018</td><td>Article</td><td>Discovery medicine</td><td>Anti-programmed cell death-1 (PD-1) monoclonal antibodies in treating advanced m...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/37887546/" target="_blank">37887546</a></td><td>2023</td><td>Article</td><td>Current oncology (Toronto, Ont</td><td>Effectiveness of Immune Checkpoint Inhibitor with Anti-PD-1 Monotherapy or in Co...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/40236344/" target="_blank">40236344</a></td><td>2025</td><td>Article</td><td>Cureus</td><td>A Case Report of Metastatic Melanoma in the Transverse Colon.</td></tr>
</tbody>
</table>

</div>
</details>


## 台灣上市資訊

**有效許可證：**

| 許可證字號 | 商品名 | 許可證持有者 | 效期 |
|------------|--------|--------------|------|
| 衛部菌疫輸字第000958號 | 益伏注射劑 5 毫克/毫升 | 台灣必治妥施貴寶 | 2029/08/18 |

**核准適應症（與 nivolumab 併用）：**
1. 無法切除或轉移性黑色素瘤（12 歲以上）
2. 晚期腎細胞癌（中度/重度風險）
3. MSI-H/dMMR 轉移性大腸直腸癌
4. 肝細胞癌（第一線和 sorafenib 失敗後）
5. 轉移性或復發性非小細胞肺癌
6. 惡性肋膜間皮瘤
7. 食道鱗狀細胞癌

## 安全性考量

### 免疫相關不良事件 (irAEs)

Ipilimumab + Nivolumab 併用療法的 Grade 3-4 irAEs 發生率約 50-60%：

| 不良反應類型 | 常見表現 | 管理重點 |
|--------------|----------|----------|
| 腸炎 | 腹瀉、血便 | 可能需 corticosteroids |
| 肝炎 | 轉氨酶升高 | 監測肝功能 |
| 皮膚炎 | 皮疹、搔癢 | 外用/全身性 steroids |
| 內分泌病變 | 甲狀腺/腎上腺功能異常 | 荷爾蒙補充 |
| 肺炎 | 呼吸困難、咳嗽 | 停藥並給予 steroids |
| 腸穿孔 | 罕見但致命 | 緊急外科介入 |

### 主要藥物交互作用

| 交互作用藥物 | 嚴重程度 | 說明 |
|--------------|----------|------|
| Corticosteroids | Moderate | 可能降低免疫治療效果 |
| Hydrocortisone | Moderate | 用於 irAEs 管理時需權衡 |
| Dexamethasone | Moderate | 同上 |
| 其他免疫抑制劑 | Moderate | 可能影響療效 |

### 特殊族群
- **肝功能不全**：輕度肝功能不全不需調整劑量
- **腎功能不全**：不需調整劑量
- **孕婦**：禁用，可能致畸
- **老年患者**：毒性可能增加，需密切監測


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**Hepatic Insufficiency** 🟡 Moderate
- 可能有嚴重不良反應。

**Pneumonia** 🟡 Moderate
- 必要時應停止治療。

**Colitis** 🟢 Minor
- 風險包括：感染。可能有致命風險。必要時應停止治療。

**Dermatitis** 🟢 Minor
- 出現症狀時應考慮停藥。

**Endocrine System Diseases** 🟢 Minor
- 需定期監測。可能危及生命。出現症狀時應考慮停藥。

**Hepatitis** 🟢 Minor
- 需定期監測。可能有致命風險。出現症狀時應考慮停藥。

**Graft vs Host Disease** 🟢 Minor
- 需密切監測。可能有致命風險。

**Immune System Diseases** 🟢 Minor
- 需定期監測。可能有致命風險。出現症狀時應考慮停藥。

**Eye Diseases** 🟢 Minor
- 需定期監測。可能有致命風險。出現症狀時應考慮停藥。

## 結論與下一步

### 預測評估結論

Ipilimumab 對非皮膚黑色素瘤的預測是**高度有價值的發現**：

1. **葡萄膜黑色素瘤**：已有 Phase 2 試驗數據，顯示與 nivolumab 併用的療效
2. **黏膜黑色素瘤**：多項進行中的臨床試驗正在評估
3. **脈絡膜無虹膜症**：此預測缺乏機轉支持，可能為偽陽性

### 證據等級總結

| 預測適應症 | TxGNN Score | 證據等級 | 評估 |
|------------|-------------|----------|------|
| 非皮膚黑色素瘤 | 0.990 | **L1/L2** | 多項 RCT 支持，極高價值 |
| 脈絡膜無虹膜症 | 0.991 | L5 | 機轉不明，可能偽陽性 |

### 建議

1. **非皮膚黑色素瘤**：
   - **強烈建議持續追蹤臨床試驗進展**
   - 現有 Phase 2 試驗（NCT02626962）結果已發表
   - 可作為臨床決策參考
   - 部分亞型可能已可在仿單外使用條件下應用

2. **適應症擴增建議**：
   - 葡萄膜黑色素瘤和黏膜黑色素瘤的證據已相對成熟
   - 可考慮向 TFDA 提交適應症擴增申請

3. **臨床應用注意事項**：
   - 非皮膚黑色素瘤預後通常較皮膚型差
   - 需謹慎評估病患狀況和 irAEs 風險
   - 建議在有免疫治療經驗的中心使用

---

*報告生成日期：2026-02-11*
*資料來源：TxGNN 知識圖譜預測、ClinicalTrials.gov、PubMed、台灣 FDA*

---

## 相關藥物報告

- [Buprenorphine]({{ "/drugs/buprenorphine/" | relative_url }}) - 證據等級 L5
- [Famotidine]({{ "/drugs/famotidine/" | relative_url }}) - 證據等級 L5
- [Loteprednol Etabonate]({{ "/drugs/loteprednol_etabonate/" | relative_url }}) - 證據等級 L5
- [Ouabain]({{ "/drugs/ouabain/" | relative_url }}) - 證據等級 L5
- [Aspirin]({{ "/drugs/aspirin/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Ipilimumab老藥新用驗證報告. https://twtxgnn.yao.care/drugs/ipilimumab/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_ipilimumab,
  title = {Ipilimumab老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/ipilimumab/}
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
