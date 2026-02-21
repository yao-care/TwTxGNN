---
layout: default
title: Gefitinib
description: "Gefitinib 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L3
indication_count: 10
---

# Gefitinib

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Gefitinib (吉非替尼) - 藥師評估報告

## 一句話總結

<p class="key-answer" data-question="Gefitinib 可以用於治療什麼新適應症？">
吉非替尼是一種 EGFR 酪胺酸激酶抑制劑，TxGNN 預測其對多種纖維瘤樣病變和肺部良性腫瘤有潛在療效，這些預測基於 EGFR 訊號傳導在細胞增殖中的角色，但目前缺乏臨床證據支持。
</p>

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物學名 | Gefitinib |
| 台灣商品名 | 基扶能膜衣錠 250 毫克、艾瑞莎 (IRESSA) |
| DrugBank ID | DB00317 |
| 原核准適應症 | EGFR-TK 突變陽性非小細胞肺癌 (NSCLC) |
| 預測新適應症 | fibromatosis, gingival、fibroma of lung、inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia、hamartoma of lung、lung hilum carcinoma、lung benign neoplasm、Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome、lung germ cell tumor、pulmonary sulcus neoplasm、junctional epidermolysis bullosa |
| 最高證據等級 | L4 (前臨床/病例報告) |
| 台灣上市狀態 | 有效許可證 |



## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. fibromatosis, gingival</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.89%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>吉非替尼透過抑制 EGFR 酪胺酸激酶活性來阻斷細胞增殖訊號，其預測適應症可從以下角度理解：</p>

<ol>
<li><strong>牙齦纖維瘤</strong> (TxGNN Score: 0.999, Rank: 2960)：</li>
</ol>
<ul>
<li>EGFR 訊號傳導與纖維母細胞增殖相關</li>
<li>部分牙齦纖維瘤可能由 EGFR 過度活化驅動</li>
<li>值得注意的是，EGFR-TKI 本身可能導致口腔黏膜炎</li>

</ul>
<ol>
<li><strong>肺纖維瘤 / 肺錯構瘤</strong> (TxGNN Score: 0.999, Ranks: 3554, 3683)：</li>
</ol>
<ul>
<li>這些為肺部良性腫瘤</li>
<li>考量到 gefitinib 的肺部組織分佈特性，預測有其合理性</li>
<li>但良性腫瘤通常不需 TKI 治療</li>

</ul>
<ol>
<li><strong>額顳葉失智伴包涵體肌病</strong> (TxGNN Score: 0.999, Rank: 3649)：</li>
</ol>
<ul>
<li>此預測較難解釋</li>
<li>可能與神經保護作用相關的探索性研究有關</li>
</ul>

<h3>臨床試驗</h3>

<p>針對預測的新適應症，<strong>未檢索到直接相關的臨床試驗</strong>。</p>

<p>但存在大量 gefitinib 用於原核准適應症（NSCLC）的臨床試驗。</p>

<p><strong>證據等級：L5</strong> - 預測適應症僅有理論機轉支持，無臨床證據。</p>

<h3>相關文獻</h3>

<p>### 額顳葉失智相關（20 篇文獻）</p>

<p>文獻檢索結果多為額顳葉失智的一般性綜述文章，而非 gefitinib 治療該疾病的研究：</p>

<ol>
<li><strong>Bang J et al. (2015)</strong> - Lancet</li>
</ol>
<ul>
<li>額顳葉失智綜述</li>
<li>討論診斷和治療進展，但未涉及 EGFR-TKI</li>

</ul>
<ol>
<li><strong>Boeve BF et al. (2022)</strong> - Lancet Neurology</li>
</ol>
<ul>
<li>額顳葉失智診斷和生物標記進展</li>
<li>提及分子標靶治療研究方向</li>

</ul>
<p><strong>注意：</strong> 這些文獻的關聯性較低，反映的是知識圖譜中疾病的連結而非直接的治療證據。</p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. fibroma of lung</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.86%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.86%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/26595641/" target="_blank">26595641</a></td><td>2015</td><td>Article</td><td>Lancet (London, Engl</td><td>Frontotemporal dementia.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28410663/" target="_blank">28410663</a></td><td>2017</td><td>Article</td><td>Neurologic clinics</td><td>Frontotemporal Dementia.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35182511/" target="_blank">35182511</a></td><td>2022</td><td>Article</td><td>The Lancet. Neurolog</td><td>Advances and controversies in frontotemporal dementia: diagn...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/21810890/" target="_blank">21810890</a></td><td>2011</td><td>Article</td><td>Brain : a journal of</td><td>Sensitivity of revised diagnostic criteria for the behaviour...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35678399/" target="_blank">35678399</a></td><td>2022</td><td>Article</td><td>Continuum (Minneapol</td><td>Behavioral Variant Frontotemporal Dementia.</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. hamartoma of lung</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.86%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. lung hilum carcinoma</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.86%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（1 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/22688581/" target="_blank">22688581</a></td><td>2012</td><td>Article</td><td>General thoracic and</td><td>Salvage surgery for a super-responder by gefitinib therapy f...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. lung benign neoplasm</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.85%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/32778129/" target="_blank">32778129</a></td><td>2020</td><td>Article</td><td>Respiratory research</td><td>FGL1 regulates acquired resistance to Gefitinib by inhibitin...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/24794908/" target="_blank">24794908</a></td><td>2014</td><td>Article</td><td>Profiles of drug sub</td><td>Gefitinib.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/37057810/" target="_blank">37057810</a></td><td>2023</td><td>Article</td><td>The Kaohsiung journa</td><td>Dihydroartemisinin enhances gefitinib cytotoxicity against l...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/23140355/" target="_blank">23140355</a></td><td>2014</td><td>Article</td><td>Anti-cancer agents i</td><td>Erlotinib and gefitinib for elderly patients with advanced n...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38967523/" target="_blank">38967523</a></td><td>2024</td><td>Article</td><td>Cancer medicine</td><td>METTL1/FOXM1 promotes lung adenocarcinoma progression and ge...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.84%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38288441/" target="_blank">38288441</a></td><td>2024</td><td>Article</td><td>Frontiers in pharmac</td><td>Valsartan attenuates LPS-induced ALI by modulating NF-κB and...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39281285/" target="_blank">39281285</a></td><td>2024</td><td>Article</td><td>Frontiers in pharmac</td><td>Gastrointestinal tract organoids as novel tools in drug disc...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30033041/" target="_blank">30033041</a></td><td>2019</td><td>Article</td><td>The lancet. Diabetes</td><td>Advances in the medical treatment of Cushing&#x27;s syndrome.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/18931563/" target="_blank">18931563</a></td><td>2008</td><td>Article</td><td>Gan to kagaku ryoho.</td><td>[Cutaneous toxicities].</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/34474028/" target="_blank">34474028</a></td><td>2021</td><td>Article</td><td>European journal of </td><td>Mechanisms of gefitinib-induced QT prolongation.</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. lung germ cell tumor</span>
<span class="evidence-badge evidence-L3">L3</span>
<span class="prediction-score">99.84%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（1 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT00068497" target="_blank">NCT00068497</a></td><td>NA</td><td>COMPLETED</td><td>40</td><td>Single Agent ZD-1839 (NSC-715055, IND-61187) in Patients With Advanced Head and ...</td></tr>
</tbody>
</table>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/22588876/" target="_blank">22588876</a></td><td>2012</td><td>Article</td><td>Cancer discovery</td><td>Occupy EGFR.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/21485758/" target="_blank">21485758</a></td><td>2011</td><td>Article</td><td>Acta clinica Belgica</td><td>Epidermal growth factor receptor targeted therapies for soli...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38261467/" target="_blank">38261467</a></td><td>2024</td><td>Article</td><td>Clinical cancer rese</td><td>Germline USP36 Mutation Confers Resistance to EGFR-TKIs by U...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/16330971/" target="_blank">16330971</a></td><td>2005</td><td>Article</td><td>Cancer nursing</td><td>Gefitinib (Iressa, ZD1839) and tyrosine kinase inhibitors: t...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/24618893/" target="_blank">24618893</a></td><td>2014</td><td>Article</td><td>Cancer biology &amp; the</td><td>Met in lung cancer.</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. pulmonary sulcus neoplasm</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.84%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（2 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/16015545/" target="_blank">16015545</a></td><td>2005</td><td>Article</td><td>Seminars in oncology</td><td>An overview of Eastern Cooperative Oncology Group stage III ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/21441747/" target="_blank">21441747</a></td><td>2011</td><td>Article</td><td>Neurologia medico-ch</td><td>Focal leptomeningeal metastasis following curative surgery f...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. junctional epidermolysis bullosa</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.84%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>


## 台灣上市資訊

**有效許可證：**

| 許可證字號 | 商品名 | 許可證持有者 |
|------------|--------|--------------|
| 衛署藥輸字第024308號 | 艾瑞莎膜衣錠 250 毫克 | 台灣阿斯乙利康 |
| 衛部藥製字第059XXX號 | 基扶能膜衣錠 250 毫克 | 多家學名藥廠 |

**核准適應症：**
- 具有 EGFR-TK 突變之局部侵犯性或轉移性非小細胞肺癌 (NSCLC) 病患之第一線治療
- 先前已接受化學治療後仍局部惡化或轉移之肺腺癌病患之第二線用藥

## 安全性考量

### 黑框警語
- **間質性肺病 (ILD)**：可能發生致命性間質性肺病，發生率約 1-3%
- 出現呼吸困難、咳嗽或發燒時應立即停藥並評估

### 常見不良反應

| 不良反應 | 發生率 |
|----------|--------|
| 皮疹 | 40-50% |
| 腹瀉 | 30-40% |
| 皮膚乾燥 | 20-30% |
| 噁心 | 15-25% |
| 甲溝炎 | 10-20% |

### 藥物交互作用

| 交互作用藥物 | 嚴重程度 | 說明 |
|--------------|----------|------|
| CYP3A4 誘導劑 | Major | Rifampicin 等可降低 gefitinib 濃度 |
| CYP3A4 抑制劑 | Moderate | Ketoconazole 等可增加 gefitinib 濃度 |
| Warfarin | Moderate | 可能增加出血風險 |
| PPI/H2 blocker | Moderate | 可能降低 gefitinib 吸收 |

### 特殊族群
- **肝功能不全**：中重度肝功能不全患者需謹慎使用
- **孕婦**：禁用，為 FDA 懷孕分類 D 級

### 藥物-食物交互作用 (DFI)

**葡萄柚** 🔴 Major
- 影響：葡萄柚顯著增加 Gefitinib 血中濃度和毒性
- 建議：避免葡萄柚

### 藥物-草藥交互作用 (DHI)

**聖約翰草（貫葉連翹）** 🔴 Major
- 影響：聖約翰草顯著降低 Gefitinib 血中濃度
- 建議：禁止併用


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**腎臟疾病** 🟡 Moderate
- 可能有嚴重不良反應。

**Stevens-Johnson Syndrome** 🟢 Minor
- 需定期監測。可能危及生命。必要時應停止治療。

**Gastrointestinal Diseases** 🟢 Minor
- 可能有致命風險。必要時應停止治療。

**Eye Diseases** 🟢 Minor
- 必要時應停止治療。

**Lung Diseases** 🟢 Minor
- 應謹慎使用本藥物。可能有致命風險。出現症狀時應考慮停藥。

**肝臟疾病** 🟢 Minor
- 需定期監測。可能有嚴重不良反應。必要時應停止治療。

## 結論與下一步

### 預測評估結論

Gefitinib 的預測新適應症（纖維瘤樣病變、良性肺腫瘤、神經退化性疾病）目前**缺乏臨床證據支持**。雖然 EGFR 訊號傳導在細胞增殖中扮演重要角色，但：

1. 良性腫瘤通常不需要使用具有顯著毒性的 TKI
2. 神經退化性疾病的預測缺乏明確機轉基礎
3. 現有證據等級僅停留在理論推測

### 證據等級總結

| 預測適應症 | TxGNN Score | 證據等級 | 評估 |
|------------|-------------|----------|------|
| 牙齦纖維瘤 | 0.999 | L5 | 僅機轉推測 |
| 肺纖維瘤 | 0.999 | L5 | 僅機轉推測 |
| 額顳葉失智伴肌病 | 0.999 | L5 | 關聯性不明 |
| 肺錯構瘤 | 0.999 | L5 | 僅機轉推測 |
| 肺門癌 | 0.999 | L4 | 有病例報告（與原適應症相近）|

### 建議

1. **不建議優先開發預測適應症**：
   - 缺乏臨床前證據
   - 藥物毒性與良性疾病不匹配
   - 神經退化性疾病預測機轉不明

2. **可能的研究方向**：
   - 若有新的機轉證據支持 EGFR 在纖維化疾病中的角色，可考慮前臨床研究
   - 額顳葉失智與包涵體肌病的預測需更多基礎研究支持

3. **現有適應症優化**：
   - 持續優化 NSCLC 治療方案
   - 探索與其他 TKI 或免疫療法的組合策略

---

*報告生成日期：2026-02-11*
*資料來源：TxGNN 知識圖譜預測、ClinicalTrials.gov、PubMed、台灣 FDA*

---

## 相關藥物報告

- [Raloxifene]({{ "/drugs/raloxifene/" | relative_url }}) - 證據等級 L5
- [Berberine]({{ "/drugs/berberine/" | relative_url }}) - 證據等級 L5
- [Tenofovir Alafenamide]({{ "/drugs/tenofovir_alafenamide/" | relative_url }}) - 證據等級 L5
- [Cerliponase Alfa]({{ "/drugs/cerliponase_alfa/" | relative_url }}) - 證據等級 L5
- [Pemetrexed]({{ "/drugs/pemetrexed/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Gefitinib老藥新用驗證報告. https://twtxgnn.yao.care/drugs/gefitinib/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_gefitinib,
  title = {Gefitinib老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/gefitinib/}
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
