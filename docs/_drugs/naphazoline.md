---
layout: default
title: Naphazoline
description: "Naphazoline 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L4
indication_count: 10
---

# Naphazoline

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Naphazoline 藥師筆記

## 一句話總結

<p class="key-answer" data-question="Naphazoline 可以用於治療什麼新適應症？">
Naphazoline 是一種 alpha 腎上腺素受體致效劑，主要用於鼻塞和眼部充血，TxGNN 預測其對毛髮相關疾病（如禿髮症）和青光眼有治療潛力，但缺乏臨床證據支持這些新適應症。
</p>


---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Naphazoline（萘唑啉） |
| DrugBank ID | DB06711 |
| 台灣商品名 | 噴速點鼻液、各類眼藥水 |
| 原核准適應症 | 過敏性鼻炎、鼻塞、結膜炎、眼充血 |
| 預測新適應症 | hypotrichosis simplex of the scalp、congenital hypotrichosis milia、diffuse alopecia areata、alopecia、primary hereditary glaucoma、hypertrichosis (disease)、Ambras type hypertrichosis universalis congenita、open-angle glaucoma、malformation syndrome with odontal and/or periodontal component、syndrome with a Dandy-Walker malformation as major feature |
| 最高預測分數 | 0.9983（頭皮毛髮稀疏症） |
| 證據等級 | L5（僅預測） |

---




## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. hypotrichosis simplex of the scalp</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.83%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>### 藥理機轉分析</p>

<p>Naphazoline 是一種 alpha-1 和 alpha-2 腎上腺素受體致效劑，主要作用是血管收縮。其機轉與預測適應症的關聯：</p>

<ol>
<li><strong>毛髮相關疾病</strong>（TxGNN Score: 0.9983-0.9976）</li>
</ol>
<ul>
<li>包括頭皮毛髮稀疏症、禿髮症等</li>
<li>血管收縮劑通常不利於毛髮生長（減少血流供應）</li>
<li>與已知促進毛髮生長的血管擴張劑（如 minoxidil）機轉相反</li>
<li><strong>預測合理性低</strong></li>

</ul>
<ol>
<li><strong>青光眼</strong>（TxGNN Score: 0.9962-0.9959）</li>
</ol>
<ul>
<li>Alpha 腎上腺素致效劑可減少房水生成</li>
<li>但 Naphazoline 主要用於短期局部血管收縮</li>
<li>眼科用 alpha 致效劑（如 brimonidine）才是青光眼治療選擇</li>
<li>Naphazoline 可能加重某些類型青光眼</li>
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
<td>頭皮毛髮稀疏症</td>
<td>0</td>
<td>-</td>
<td>L5</td>
</tr>
<tr>
<td>禿髮症</td>
<td>0</td>
<td>-</td>
<td>L5</td>
</tr>
<tr>
<td>開角型青光眼</td>
<td>0</td>
<td>-</td>
<td>L5</td>
</tr>
</tbody>
</table>

<p><strong>結論：目前無任何預測適應症進入臨床試驗階段。</strong></p>

<h3>相關文獻</h3>

<p>### 開角型青光眼相關文獻</p>

<table>
<thead>
<tr>
<th>PMID</th>
<th>標題</th>
<th>年份</th>
<th>相關性</th>
</tr>
</thead>
<tbody>
<tr>
<td>1295525</td>
<td>Effect of topical corticosteroids on laser-induced peripheral anterior synechiae</td>
<td>1992</td>
<td>間接相關（雷射治療後藥物使用）</td>
</tr>
</tbody>
</table>

<p><strong>文獻評估</strong>：此文獻並非直接研究 Naphazoline 用於青光眼治療，僅為研究雷射小樑整形術後的藥物使用。Naphazoline 與青光眼治療的直接證據不足。</p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. congenital hypotrichosis milia</span>
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
<span class="indication-name">3. diffuse alopecia areata</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.79%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. alopecia</span>
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
<span class="indication-name">5. primary hereditary glaucoma</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.62%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. hypertrichosis (disease)</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.60%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. Ambras type hypertrichosis universalis congenita</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.60%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. open-angle glaucoma</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.59%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（1 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/1295525/" target="_blank">1295525</a></td><td>1992</td><td>Article</td><td>Australian and New Z</td><td>The effect of topical corticosteroids on laser-induced perip...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. malformation syndrome with odontal and/or periodontal component</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.57%</span>
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
<span class="indication-name">10. syndrome with a Dandy-Walker malformation as major feature</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.52%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>


## 台灣上市資訊

### 鼻用製劑

| 許可證字號 | 商品名 | 劑型 | 適應症 | 狀態 |
|-----------|--------|------|--------|------|
| （多張許可證） | 噴速點鼻液 | 點鼻液 | 過敏性鼻炎、鼻塞 | 有效 |

### 眼用製劑

| 許可證字號 | 商品名 | 劑型 | 適應症 | 狀態 |
|-----------|--------|------|--------|------|
| （多張許可證） | 各類眼藥水 | 點眼液 | 結膜炎、眼充血 | 有效 |

**台灣有多張相關許可證，涵蓋鼻用和眼用劑型。**

---

## 安全性考量

### 主要警告

1. **反跳性充血**
   - 長期使用鼻用製劑可能導致藥物性鼻炎
   - 建議使用不超過 3-5 天

2. **眼科使用禁忌**
   - 閉角型青光眼患者禁用
   - 可能加重眼壓升高

3. **全身性吸收風險**
   - 過度使用可能導致心血管副作用
   - 兒童和老年人需謹慎使用

4. **特殊族群**
   - 高血壓、心臟病患者需謹慎
   - 甲狀腺功能亢進患者需謹慎
   - 糖尿病患者需謹慎

### 藥物交互作用

- 與 MAO 抑制劑併用可能增加高血壓危機風險
- 與其他血管收縮劑併用可能增加心血管風險

---

## 結論與下一步

### 評估結論

| 預測適應症 | 證據等級 | 臨床轉譯可行性 | 建議優先順序 |
|-----------|---------|---------------|-------------|
| 毛髮稀疏症/禿髮症 | L5 | 極低 | 不建議開發 |
| 青光眼 | L5 | 極低 | 不建議開發 |

### 建議

1. **毛髮相關疾病**
   - 藥理機轉不支持（血管收縮劑不利於毛髮生長）
   - TxGNN 預測可能為假陽性
   - **不建議**進一步研究

2. **青光眼**
   - 已有更適合的 alpha 致效劑（如 brimonidine）用於青光眼
   - Naphazoline 的短效性和安全性問題不適合長期使用
   - **不建議**作為青光眼治療開發

3. **整體評估**
   - 本藥物的預測適應症與其藥理機轉不符
   - 建議將資源投入其他更有潛力的候選藥物

### 後續行動

- [ ] 無需進一步追蹤
- [x] 標記為低優先順序候選藥物

---

*報告產生日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、台灣 FDA*


---

## 相關藥物報告

- [Cytarabine]({{ "/drugs/cytarabine/" | relative_url }}) - 證據等級 L5
- [Iodixanol]({{ "/drugs/iodixanol/" | relative_url }}) - 證據等級 L5
- [Cerliponase Alfa]({{ "/drugs/cerliponase_alfa/" | relative_url }}) - 證據等級 L5
- [Warfarin]({{ "/drugs/warfarin/" | relative_url }}) - 證據等級 L5
- [Raloxifene]({{ "/drugs/raloxifene/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Naphazoline老藥新用驗證報告. https://twtxgnn.yao.care/drugs/naphazoline/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_naphazoline,
  title = {Naphazoline老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/naphazoline/}
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
