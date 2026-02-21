---
layout: default
title: Cytarabine
description: "Cytarabine 的老藥新用潛力分析。模型預測等級 L5，包含 9 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L2
indication_count: 9
---

# Cytarabine

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>9</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Cytarabine 藥師筆記

## 一句話總結

<p class="key-answer" data-question="Cytarabine 可以用於治療什麼新適應症？">
Cytarabine (Ara-C) 是治療急性白血病的核心化療藥物，TxGNN 預測其對小細胞肺癌及原發性肺淋巴瘤有療效，這些預測有歷史臨床研究支持，但療效有限且非現代標準治療。
</p>

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Cytarabine (阿糖胞苷, Ara-C) |
| DrugBank ID | DB00987 |
| 台灣商品名 | 複方製劑中的成分，如 Midostaurin 併用方案 |
| 原核准適應症 | 急性骨髓性白血病 (AML)、慢性淋巴球性白血病 (CLL)、與其他藥物併用 |
| 預測新適應症 | small cell lung carcinoma、primary pulmonary lymphoma、well-differentiated fetal adenocarcinoma of the lung、pulmonary blastoma、myeloid leukemia、upper aerodigestive tract neoplasm、ganglioneuroblastoma (disease)、vertebral anomalies and variable endocrine and T-cell dysfunction、腹膜後腫瘤 |
| 最高預測分數 | 0.998 (small cell lung carcinoma) |
| 證據等級 | L3 (歷史臨床研究，非現代標準) |

---



## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. small cell lung carcinoma</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.78%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>Cytarabine 的抗腫瘤機轉支持其對多種惡性腫瘤的潛在活性：</p>

<ol>
<li><strong>核苷類似物</strong>：Cytarabine 是胞嘧啶核苷的類似物，干擾 DNA 合成</li>
<li><strong>S 期特異性</strong>：主要作用於 DNA 合成期，對快速分裂的腫瘤細胞有選擇性</li>
<li><strong>廣譜活性</strong>：歷史上曾用於多種惡性腫瘤的探索性治療</li>
</ol>

<h3>臨床試驗</h3>

<p>### 小細胞肺癌相關試驗</p>

<table>
<thead>
<tr>
<th>試驗編號</th>
<th>標題</th>
<th>階段</th>
<th>狀態</th>
<th>相關性</th>
</tr>
</thead>
<tbody>
<tr>
<td>NCT03507244</td>
<td>鞘內 Pemetrexed 治療腦膜轉移</td>
<td>Phase 1/2</td>
<td>已完成</td>
<td>提及 cytarabine 作為對照</td>
</tr>
<tr>
<td>NCT03101579</td>
<td>鞘內 Pemetrexed 治療 NSCLC 腦膜轉移</td>
<td>Phase 1</td>
<td>已完成</td>
<td>Cytarabine 作為傳統鞘內治療比較</td>
</tr>
</tbody>
</table>

<h3>相關文獻</h3>

<p>### 小細胞肺癌</p>

<table>
<thead>
<tr>
<th>PMID</th>
<th>標題</th>
<th>年份</th>
<th>主要發現</th>
</tr>
</thead>
<tbody>
<tr>
<td>232239</td>
<td>Combination radiotherapy and chemotherapy for SCLC</td>
<td>1979</td>
<td>Ara-C 併用方案有效但無優勢</td>
</tr>
<tr>
<td>3030547</td>
<td>High-dose cytarabine in SCLC</td>
<td>1987</td>
<td>高劑量 Ara-C 單獨使用反應有限</td>
</tr>
<tr>
<td>6095640</td>
<td>Intensive cytosine arabinoside therapy in SCLC</td>
<td>1984</td>
<td>Ara-C 加入 CAV 方案無額外益處</td>
</tr>
<tr>
<td>2841844</td>
<td>VP-16 and Ara-C for relapsed SCLC</td>
<td>1988</td>
<td>復發 SCLC 治療，毒性高但活性有限</td>
</tr>
</tbody>
</table>

<p><strong>文獻結論</strong>：1980 年代的研究顯示 cytarabine 對 SCLC 有一定活性，但並未優於當時的標準方案，且毒性顯著。</p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. primary pulmonary lymphoma</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.78%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（7 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00345865" target="_blank">NCT00345865</a></td><td>PHASE2</td><td>COMPLETED</td><td>473</td><td>Autologous Peripheral Blood Stem Cell Transplant for Patients With Lymphoma</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01476839" target="_blank">NCT01476839</a></td><td>PHASE1</td><td>COMPLETED</td><td>25</td><td>Phase I Study of Yttrium-90 Labeled Anti-CD25 (a-Tac) Monoclonal Antibody Plus B...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02356159" target="_blank">NCT02356159</a></td><td>PHASE1, PHASE2</td><td>COMPLETED</td><td>34</td><td>A Phase I/II Open Label, Dose Escalation Study of Palifermin (Kepivance) in Pers...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00013533" target="_blank">NCT00013533</a></td><td>EARLY_PHASE1</td><td>COMPLETED</td><td>30</td><td>Pilot Study of Non-Myeloablative, HLA-Matched Allogeneic Stem Cell Transplantati...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00452374" target="_blank">NCT00452374</a></td><td>PHASE1, PHASE2</td><td>COMPLETED</td><td>48</td><td>A Phase I-II Study of Oxaliplatin, Fludarabine, Cytarabine and Rituximab in Pati...</td></tr>
</tbody>
</table>
<p><em>...及其他 2 項試驗</em></p>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26256690/" target="_blank">26256690</a></td><td>2017</td><td>Article</td><td>The clinical respira</td><td>Synchronous mantle cell lymph node lymphoma and pulmonary ad...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/15957966/" target="_blank">15957966</a></td><td>2005</td><td>Article</td><td>Expert opinion on ph</td><td>Management of leptomeningeal malignancy.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/12860951/" target="_blank">12860951</a></td><td>2003</td><td>Article</td><td>Journal of clinical </td><td>Chemotherapy alone as initial treatment for primary CNS lymp...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/11244328/" target="_blank">11244328</a></td><td>2001</td><td>Article</td><td>Oncology</td><td>Combined treatment with high-dose methotrexate, vincristine ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38555923/" target="_blank">38555923</a></td><td>2024</td><td>Article</td><td>The Lancet. Haematol</td><td>Anti-CD30 CAR T cells as consolidation after autologous haem...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. well-differentiated fetal adenocarcinoma of the lung</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.76%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. pulmonary blastoma</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.76%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. upper aerodigestive tract neoplasm</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.49%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/32183950/" target="_blank">32183950</a></td><td>2020</td><td>Article</td><td>Cancer cell</td><td>ADORA1 Inhibition Promotes Tumor Immune Evasion by Regulatin...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/16041392/" target="_blank">16041392</a></td><td>2005</td><td>Article</td><td>The pharmacogenomics</td><td>Genetic factors influencing pyrimidine-antagonist chemothera...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36656600/" target="_blank">36656600</a></td><td>2023</td><td>Article</td><td>JAMA oncology</td><td>Malignant Neoplasms of the Gastrointestinal Tract After Bloo...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2589230/" target="_blank">2589230</a></td><td>1989</td><td>Article</td><td>American journal of </td><td>Combination chemotherapy with cytosine arabinoside (Ara-C) a...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/15548350/" target="_blank">15548350</a></td><td>2004</td><td>Article</td><td>Neoplasia (New York,</td><td>Chemotherapy-induced and/or radiation therapy-induced oral m...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. ganglioneuroblastoma (disease)</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.36%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. vertebral anomalies and variable endocrine and T-cell dysfunction</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.32%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. retroperitoneal neoplasm</span>
<span class="evidence-badge evidence-L3">L3</span>
<span class="prediction-score">99.23%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（1 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01468311" target="_blank">NCT01468311</a></td><td>PHASE1, PHASE2</td><td>TERMINATED</td><td>6</td><td>Phase I/II Trial of Yttrium-90-labeled Daclizumab (Anti-CD25) Radioimmunotherapy...</td></tr>
</tbody>
</table>

<h3>相關文獻（14 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/34733617/" target="_blank">34733617</a></td><td>2021</td><td>Article</td><td>World journal of cli</td><td>Gastric myeloid sarcoma: A case report.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/12656749/" target="_blank">12656749</a></td><td>2003</td><td>Article</td><td>European journal of </td><td>Acute myeloid leukemia mimicking primary testicular neoplasm...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/16632190/" target="_blank">16632190</a></td><td>2007</td><td>Article</td><td>European urology</td><td>Retroperitoneal fibrosis after chemotherapy.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28579851/" target="_blank">28579851</a></td><td>2017</td><td>Article</td><td>Clinical medicine in</td><td>Transformation of Follicular Lymphoma to a High-Grade B-Cell...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2049752/" target="_blank">2049752</a></td><td>1991</td><td>Article</td><td>Cancer</td><td>Improved treatment results in boys with overt testicular rel...</td></tr>
</tbody>
</table>
<p><em>...及其他 9 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. neuroblastoma</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.19%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（5 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04029688" target="_blank">NCT04029688</a></td><td>PHASE1, PHASE2</td><td>TERMINATED</td><td>38</td><td>A Phase I/II, Multicenter, Open-Label, Multi-Arm Study Evaluating the Safety, To...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03236857" target="_blank">NCT03236857</a></td><td>PHASE1</td><td>COMPLETED</td><td>143</td><td>A Phase 1 Study of the Safety and Pharmacokinetics of Venetoclax in Pediatric an...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02130869" target="_blank">NCT02130869</a></td><td>PHASE1</td><td>COMPLETED</td><td>8</td><td>A Pilot Study of Immunotherapy Including Haploidentical NK Cell Infusion Followi...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01546038" target="_blank">NCT01546038</a></td><td>PHASE2</td><td>COMPLETED</td><td>255</td><td>A PHASE 1B/2 STUDY TO EVALUATE THE SAFETY AND EFFICACY OF PF-04449913, AN ORAL H...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06942039" target="_blank">NCT06942039</a></td><td>EARLY_PHASE1</td><td>RECRUITING</td><td>15</td><td>A Pilot Study of Intrathecal Topotecan and Maintenance Chemotherapy in the Post-...</td></tr>
</tbody>
</table>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36688816/" target="_blank">36688816</a></td><td>2023</td><td>Article</td><td>ACS applied material</td><td>Green Light-Triggerable Chemo-Photothermal Activity of Cytar...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/15867251/" target="_blank">15867251</a></td><td>2005</td><td>Article</td><td>Clinical cancer rese</td><td>Sensitivity to gemcitabine and its metabolizing enzymes in n...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/31681584/" target="_blank">31681584</a></td><td>2019</td><td>Article</td><td>Frontiers in oncolog</td><td>Two Receptors, Two Isoforms, Two Cancers: Comprehensive Anal...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/7529082/" target="_blank">7529082</a></td><td>1993</td><td>Article</td><td>Cancer biotherapy</td><td>Sensitivity to bleomycin and arabinoside cytosine in lymphoc...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2917605/" target="_blank">2917605</a></td><td>1989</td><td>Article</td><td>Experimental cell re</td><td>Morphologic and phenotypic changes of human neuroblastoma ce...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>


## 台灣上市資訊

Cytarabine 在台灣主要以下列形式使用：

| 用途 | 藥品 | 說明 |
|------|------|------|
| AML 前導治療 | Midostaurin (彌多妥) 併用 | FLT3 突變陽性 AML |
| AML 鞏固治療 | 高劑量 Ara-C | 標準方案 |
| CLL 治療 | Venetoclax 併用低劑量 Ara-C | 不適合強化化療的患者 |

---

## 安全性考量

### 主要毒性

| 毒性類型 | 表現 | 管理 |
|----------|------|------|
| 骨髓抑制 | 嚴重嗜中性球低下、血小板低下 | 監測 CBC，預防性使用 G-CSF |
| 感染 | 機會性感染風險高 | 預防性抗生素、抗黴菌藥 |
| 神經毒性 | 高劑量時可能出現小腦症狀 | 監測神經功能，調整劑量 |
| 消化道 | 黏膜炎、噁心嘔吐 | 止吐藥、口腔護理 |
| Ara-C 症候群 | 發燒、肌痛、骨痛、皮疹 | 類固醇預防 |

### 藥物交互作用注意

- **其他骨髓抑制藥物**：毒性疊加
- **Digoxin**：可能降低 digoxin 吸收
- **Flucytosine**：競爭性拮抗

---


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**肝臟疾病** 🟡 Moderate
- 注意事項：Cytarabine is extensively metabolized by the liver...

**腎臟疾病** 🟡 Moderate
- 注意事項：Cytarabine is primarily eliminated by the kidney...

**Infections** 🟢 Minor
- 本藥物在此情況下禁用。需定期監測。風險包括：骨髓抑制、感染。

**Bone Marrow Failure Disorders** 🟢 Minor
- 風險包括：骨髓抑制、出血、感染。可能有嚴重不良反應。

## 結論與下一步

### 預測評估

| 評估項目 | 小細胞肺癌 | 原發性肺淋巴瘤 |
|----------|------------|----------------|
| 機轉合理性 | 高 | 高 |
| 臨床證據 | L3 (歷史研究) | L2 (CNS 淋巴瘤有 RCT) |
| 文獻支持 | 中等但過時 | 較強（用於 CNS 淋巴瘤） |

### 臨床意義評估

#### 小細胞肺癌

- **不建議臨床使用**：現代 SCLC 治療已不包含 cytarabine
- **現代標準**：Cisplatin/Carboplatin + Etoposide，免疫治療 (如 atezolizumab)
- **歷史價值**：反映了知識圖譜能捕捉歷史用藥關聯

#### 原發性肺淋巴瘤/CNS 淋巴瘤

- **有臨床價值**：高劑量 Ara-C 是 CNS 淋巴瘤治療的重要成分
- **現代方案**：通常與 MTX、rituximab 併用
- **注意事項**：「原發性肺淋巴瘤」較罕見，治療通常參考全身性淋巴瘤方案

### 建議

1. **SCLC**：不建議使用 cytarabine，應依循現代治療指引
2. **CNS 淋巴瘤**：高劑量 cytarabine 仍有其角色，需由血液腫瘤專科評估
3. **腦膜轉移**：鞘內 cytarabine 或 liposomal cytarabine 為可選方案

### 整體證據等級

**L3 (觀察性研究/歷史臨床經驗)** - 有文獻支持但非現代標準治療

---

*本筆記僅供研究參考，不構成醫療建議。任何用藥決策應諮詢專業醫療人員。*

*最後更新：2026-02-11*

---

## 相關藥物報告

- [Raloxifene]({{ "/drugs/raloxifene/" | relative_url }}) - 證據等級 L5
- [Brivaracetam]({{ "/drugs/brivaracetam/" | relative_url }}) - 證據等級 L5
- [Flunitrazepam]({{ "/drugs/flunitrazepam/" | relative_url }}) - 證據等級 L5
- [Clomipramine]({{ "/drugs/clomipramine/" | relative_url }}) - 證據等級 L5
- [Tenofovir Alafenamide]({{ "/drugs/tenofovir_alafenamide/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Cytarabine老藥新用驗證報告. https://twtxgnn.yao.care/drugs/cytarabine/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_cytarabine,
  title = {Cytarabine老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/cytarabine/}
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
