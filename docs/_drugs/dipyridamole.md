---
layout: default
title: Dipyridamole
description: "Dipyridamole 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L1
indication_count: 10
---

# Dipyridamole

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Dipyridamole (待乙妥) - 藥師評估報告

## 一句話總結

<p class="key-answer" data-question="Dipyridamole 可以用於治療什麼新適應症？">
Dipyridamole 是一種磷酸二酯酶抑制劑和腺苷再攝取抑制劑，用於心絞痛和血栓預防；TxGNN 預測其對變異型心絞痛和中風有潛在療效，有豐富的臨床試驗和文獻支持，但變異型心絞痛預測與原適應症高度重疊。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Dipyridamole (待乙妥/雙乙妥) |
| DrugBank ID | DB00975 |
| 台灣商品名 | 百心康、Aggrenox（與 aspirin 複方） |
| 原適應症 | 慢性狹心症、冠狀動脈不全、血小板凝集降低、心肌灌流造影替代運動試驗 |
| 預測新適應症 | Prinzmetal angina、stroke disorder、thrombotic disease、atrial fibrillation (disease)、sick sinus syndrome 2, autosomal dominant、transient ischemic attack (disease)、sarcoglycanopathy、Wildervanck syndrome、macrocephaly, dysmorphic facies, and psychomotor retardation、lateral sinus thrombosis |
| 最高 TxGNN 分數 | 0.9999 (Prinzmetal angina) |
| 臨床試驗支持 | **豐富** (中風預防) |
| 文獻支持 | **豐富** |



## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. Prinzmetal angina</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.99%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>### 機轉分析</p>

<ol>
<li><strong>變異型心絞痛 (Prinzmetal angina)</strong>：</li>
</ol>
<ul>
<li>TxGNN 分數 0.9999，排名 438</li>
<li>Dipyridamole 是冠狀動脈血管擴張劑</li>
<li>理論上可緩解冠狀動脈痙攣</li>
<li>但文獻顯示其對變異型心絞痛的效果不一，部分研究甚至指出無效或可能加重症狀</li>
<li><strong>注意</strong>：此預測與原適應症「慢性狹心症」高度重疊</li>

</ul>
<ol>
<li><strong>中風 (stroke disorder)</strong>：</li>
</ol>
<ul>
<li>TxGNN 分數 0.9995，排名 1695</li>
<li>Dipyridamole 抑制血小板凝集</li>
<li>與 aspirin 合用已被廣泛用於缺血性中風的二級預防</li>
<li><strong>重要</strong>：Aggrenox (dipyridamole + aspirin) 已是核准適應症</li>
</ul>

<h3>臨床試驗</h3>

<p>目前無針對此特定適應症的臨床試驗登記。</p>

<h3>相關文獻</h3>

<p>### 變異型心絞痛相關文獻</p>

<ol>
<li><strong>Yasue H et al. (1978)</strong> - Jpn Circ J</li>
</ol>
<ul>
<li>研究各種藥物對靜止型心絞痛的效果</li>
<li>發現：Dipyridamole 對 Prinzmetal 變異型心絞痛<strong>無效</strong></li>
<li>相對而言，Diltiazem 對所有病例都有效</li>

</ul>
<ol>
<li><strong>Picano E et al. (1988)</strong> - Am J Cardiol</li>
</ol>
<ul>
<li>報告 aminophylline 終止 dipyridamole 壓力測試可能誘發變異型心絞痛患者的冠狀動脈痙攣</li>
<li>警示：使用 dipyridamole 進行壓力測試時需注意</li>

</ul>
<ol>
<li><strong>多項 dipyridamole 壓力測試研究</strong></li>
</ol>
<ul>
<li>Dipyridamole 主要作為診斷工具而非治療藥物用於變異型心絞痛</li>
</ul>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. stroke disorder</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.95%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（31 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02966119" target="_blank">NCT02966119</a></td><td>PHASE3</td><td>TERMINATED</td><td>23</td><td>Evaluation of the Benefit/Risk Ratio of Restarting or Avoiding Antiplatelet Drug...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01781611" target="_blank">NCT01781611</a></td><td>NA</td><td>TERMINATED</td><td>18</td><td>Dipyridamole Assessment for Flare Reduction in SLE</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06983795" target="_blank">NCT06983795</a></td><td>N/A</td><td>NOT_YET_RECRUITING</td><td>1000</td><td>Pioneering Advancements in Cardiocerebrovascular Interactions in the Asia pacFIC...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01528800" target="_blank">NCT01528800</a></td><td>PHASE2</td><td>COMPLETED</td><td>85</td><td>Inhibit Progression of Coronary Artery Calcification With Vitamin K in HemoDialy...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03993119" target="_blank">NCT03993119</a></td><td>N/A</td><td>COMPLETED</td><td>500</td><td>Non-Interventional, Cross-sectional Study to Describe NOACs Management in Elderl...</td></tr>
</tbody>
</table>
<p><em>...及其他 26 項試驗</em></p>

<h3>相關文獻（18 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/11786451/" target="_blank">11786451</a></td><td>2002</td><td>Article</td><td>BMJ (Clinical resear</td><td>Collaborative meta-analysis of randomised trials of antiplat...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/27816341/" target="_blank">27816341</a></td><td>2016</td><td>Article</td><td>Presse medicale (Par</td><td>Stroke prevention.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/4119751/" target="_blank">4119751</a></td><td>1973</td><td>Article</td><td>Lancet (London, Engl</td><td>Glycerol and stroke.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/9064773/" target="_blank">9064773</a></td><td>1997</td><td>Article</td><td>Science (New York, N</td><td>Aspirin and stroke.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/16102029/" target="_blank">16102029</a></td><td>2005</td><td>Article</td><td>Journal of thrombosi</td><td>Preventable stroke and stroke prevention.</td></tr>
</tbody>
</table>
<p><em>...及其他 13 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. thrombotic disease</span>
<span class="evidence-badge evidence-L2">L2</span>
<span class="prediction-score">99.94%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（2 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01528800" target="_blank">NCT01528800</a></td><td>PHASE2</td><td>COMPLETED</td><td>85</td><td>Inhibit Progression of Coronary Artery Calcification With Vitamin K in HemoDialy...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01661322" target="_blank">NCT01661322</a></td><td>PHASE3</td><td>TERMINATED</td><td>3096</td><td>Safety and Efficacy of Intensive Versus Guideline Antiplatelet Therapy in High R...</td></tr>
</tbody>
</table>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26719230/" target="_blank">26719230</a></td><td>2016</td><td>Article</td><td>Lancet (London, Engl</td><td>Bevacizumab for newly diagnosed pleural mesothelioma in the ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36696191/" target="_blank">36696191</a></td><td>2023</td><td>Article</td><td>Journal of thrombosi</td><td>Targeting thromboinflammation in antiphospholipid syndrome.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2107174/" target="_blank">2107174</a></td><td>1990</td><td>Article</td><td>Hematology/oncology </td><td>Thrombotic thrombocytopenic purpura and related disorders.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/382146/" target="_blank">382146</a></td><td>1979</td><td>Article</td><td>Postgraduate medicin</td><td>Antiplatelet drugs in thromboembolism.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/32574107/" target="_blank">32574107</a></td><td>2020</td><td>Article</td><td>Emerging microbes &amp; </td><td>Kawasaki-like diseases and thrombotic coagulopathy in COVID-...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. sick sinus syndrome 2, autosomal dominant</span>
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
<span class="indication-name">5. transient ischemic attack (disease)</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.87%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（15 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT06983795" target="_blank">NCT06983795</a></td><td>N/A</td><td>NOT_YET_RECRUITING</td><td>1000</td><td>Pioneering Advancements in Cardiocerebrovascular Interactions in the Asia pacFIC...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00027170" target="_blank">NCT00027170</a></td><td>N/A</td><td>COMPLETED</td><td>8781</td><td>Technical Development of Cardiovascular Magnetic Resonance Imaging</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01528800" target="_blank">NCT01528800</a></td><td>PHASE2</td><td>COMPLETED</td><td>85</td><td>Inhibit Progression of Coronary Artery Calcification With Vitamin K in HemoDialy...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT03993119" target="_blank">NCT03993119</a></td><td>N/A</td><td>COMPLETED</td><td>500</td><td>Non-Interventional, Cross-sectional Study to Describe NOACs Management in Elderl...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00738894" target="_blank">NCT00738894</a></td><td>NA</td><td>COMPLETED</td><td>664</td><td>GORE® HELEX® Septal Occluder / GORE® CARDIOFORM Septal Occluder and Antiplatelet...</td></tr>
</tbody>
</table>
<p><em>...及其他 10 項試驗</em></p>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/11786451/" target="_blank">11786451</a></td><td>2002</td><td>Article</td><td>BMJ (Clinical resear</td><td>Collaborative meta-analysis of randomised trials of antiplat...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35470408/" target="_blank">35470408</a></td><td>2022</td><td>Article</td><td>Acta neurologica Tai</td><td>Antiplatelets and Anticoagulants in Ischemic Stroke,Transien...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26304937/" target="_blank">26304937</a></td><td>2015</td><td>Article</td><td>Journal of the Ameri</td><td>Long-Term Antiplatelet Mono- and Dual Therapies After Ischem...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/17389280/" target="_blank">17389280</a></td><td>2007</td><td>Article</td><td>Circulation</td><td>Secondary prevention of stroke and transient ischemic attack...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/24157563/" target="_blank">24157563</a></td><td>2014</td><td>Article</td><td>Frontiers of neurolo</td><td>Antithrombotic therapy in transient ischemic attack patients...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. sarcoglycanopathy</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.82%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. Wildervanck syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.78%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. macrocephaly, dysmorphic facies, and psychomotor retardation</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.77%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. cavernous sinus thrombosis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.72%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. lateral sinus thrombosis</span>
<span class="evidence-badge evidence-L3">L3</span>
<span class="prediction-score">99.72%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（1 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT01528800" target="_blank">NCT01528800</a></td><td>PHASE2</td><td>COMPLETED</td><td>85</td><td>Inhibit Progression of Coronary Artery Calcification With Vitamin K in HemoDialy...</td></tr>
</tbody>
</table>

</div>
</details>


## 台灣上市狀態

| 許可證號 | 商品名 | 劑型 | 適應症 | 狀態 |
|----------|--------|------|--------|------|
| 多項 | 百心康等 | 錠劑/膠囊 | 慢性狹心症、血小板凝集降低 | 部分有效 |

**備註**：Aggrenox（dipyridamole + aspirin 複方）國際上用於中風預防，台灣需確認是否有上市。

## 安全性

### 藥物交互作用

Dipyridamole 的主要交互作用與其腺苷再攝取抑制作用相關：

| 併用藥物 | 注意事項 |
|----------|----------|
| Adenosine | 增強腺苷作用，需調整劑量 |
| 抗凝血劑 | 增加出血風險 |
| 抗血小板藥物 | 出血風險加成 |

### 重要警語

- 不穩定型心絞痛或急性心肌梗塞期間應謹慎使用
- 低血壓風險
- 可能引起頭痛、頭暈

## 結論

### 整體評估：已有成熟適應症

Dipyridamole 的 TxGNN 預測雖然分數很高，但兩項主要預測都與現有適應症高度重疊：

1. **變異型心絞痛**：文獻證據矛盾，且部分研究顯示無效
2. **中風預防**：Dipyridamole + aspirin 複方已是確立的二級預防方案

### 建議

1. **不需要**進行新適應症研究，因為預測的適應症已是現有用途或其延伸
2. 對於變異型心絞痛，現有證據不支持將 dipyridamole 作為首選治療
3. 中風預防應優先考慮 Aggrenox 複方或其他已證實有效的抗血小板方案

### 證據等級總結

| 預測適應症 | TxGNN 分數 | 臨床試驗 | 文獻支持 | 機轉合理性 | 綜合評估 |
|------------|------------|----------|----------|------------|----------|
| Prinzmetal angina | 0.9999 | 診斷用途 | 有（但矛盾） | 中等 | 與原適應症重疊，效果存疑 |
| 中風 | 0.9995 | **豐富** | **豐富** | 高 | 已為適應症（複方） |

---
*報告產生日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、台灣 FDA*


---

## 相關藥物報告

- [Tenofovir Alafenamide]({{ "/drugs/tenofovir_alafenamide/" | relative_url }}) - 證據等級 L5
- [Titanium Dioxide]({{ "/drugs/titanium_dioxide/" | relative_url }}) - 證據等級 L5
- [Berberine]({{ "/drugs/berberine/" | relative_url }}) - 證據等級 L5
- [Sodium Citrate]({{ "/drugs/sodium_citrate/" | relative_url }}) - 證據等級 L5
- [Mannitol]({{ "/drugs/mannitol/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Dipyridamole老藥新用驗證報告. https://twtxgnn.yao.care/drugs/dipyridamole/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_dipyridamole,
  title = {Dipyridamole老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/dipyridamole/}
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
