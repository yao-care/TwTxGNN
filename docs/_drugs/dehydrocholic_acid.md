---
layout: default
title: Dehydrocholic Acid
description: "Dehydrocholic Acid 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L4
indication_count: 10
---

# Dehydrocholic Acid

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Dehydrocholic Acid (去氫膽酸) - 藥師評估報告

## 一句話總結

<p class="key-answer" data-question="Dehydrocholic Acid 可以用於治療什麼新適應症？">
Dehydrocholic acid 是一種傳統利膽劑，TxGNN 預測其可能對膽道疾病和腎結石有潛在療效，但這些預測與其原有膽道適應症高度重疊，缺乏真正的新適應症發現價值。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Dehydrocholic acid (去氫膽酸/脫氫膽酸) |
| DrugBank ID | DB11622 |
| 台灣商品名 | 得利膽錠、派頓去氫膽酸錠 |
| 原適應症 | 利膽劑、膽石症、膽囊炎、膽道炎、肝硬化、黃疸 |
| 預測新適應症 | 急性尿酸腎病、腎結石、膽道疾病、膽管腫瘤 |
| 最高 TxGNN 分數 | 0.9999 (急性尿酸腎病) |
| 臨床試驗支持 | 無 |
| 文獻支持 | 部分 (膽道疾病相關) |



## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. acute urate nephropathy</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">100.00%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>### 機轉分析</p>

<ol>
<li><strong>膽道疾病 (bile duct disease)</strong>：TxGNN 分數 0.9999，但這與藥物原有的利膽適應症完全重疊，不具新藥再利用價值。</li>

<li><strong>腎結石 (nephrolithiasis)</strong>：TxGNN 分數 0.9999。理論上，dehydrocholic acid 可增加膽汁流動，可能影響膽固醇和膽鹽代謝，間接影響某些類型結石的形成。但目前無直接機轉證據支持其用於腎結石治療。</li>

<li><strong>急性尿酸腎病 (acute urate nephropathy)</strong>：TxGNN 分數最高 (0.9999)，但無任何文獻或臨床試驗支持，機轉連結薄弱。</li>
</ol>

<h3>臨床試驗</h3>

<p>目前無針對此特定適應症的臨床試驗登記。</p>

<h3>相關文獻</h3>

<p>### 膽道疾病相關文獻</p>

<ol>
<li><strong>Ratan J et al. (1997)</strong> - Tohoku J Exp Med</li>
</ol>
<ul>
<li>比較 Livzon 和 dehydrocholic acid 在阻塞性黃疸大鼠模型中的保肝和利膽作用</li>
<li>結論：Dehydrocholic acid 主要表現利膽作用</li>

</ul>
<ol>
<li><strong>Sakai Y et al. (2008)</strong> - Hepato-gastroenterology</li>
</ol>
<ul>
<li>研究 dehydrocholic acid 在 MRCP 檢查中增強膽道顯影的潛在用途</li>

</ul>
<ol>
<li><strong>Martinez-Gili L et al. (2023)</strong> - Gut Microbes</li>
</ol>
<ul>
<li>研究原發性膽道膽汁淤積症患者對 UDCA 治療反應不佳的細菌和代謝表型</li>
<li>dehydrocholic acid 作為相關代謝物被提及</li>
</ul>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. nephrolithiasis</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">100.00%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（1 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/6080021/" target="_blank">6080021</a></td><td>1967</td><td>Article</td><td>Journal of the Canad</td><td>Nephrotomography in various renal disorders.</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. bile duct disease</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.99%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/9149351/" target="_blank">9149351</a></td><td>1997</td><td>Article</td><td>The Tohoku journal o</td><td>A controlled trial of choleretic and hepatoprotective action...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/4947701/" target="_blank">4947701</a></td><td>1971</td><td>Article</td><td>Postgraduate medical</td><td>Primary sclerosing cholangitis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/839737/" target="_blank">839737</a></td><td>1977</td><td>Article</td><td>Laboratory investiga</td><td>Subcellular pathology of rat liver in cholestasis and choler...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/37191344/" target="_blank">37191344</a></td><td>2023</td><td>Article</td><td>Gut microbes</td><td>Bacterial and metabolic phenotypes associated with inadequat...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/21010742/" target="_blank">21010742</a></td><td>1945</td><td>Article</td><td>The Journal of pharm</td><td>The choleretic action of dehydrocholic acid (decholin) and d...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. bile duct neoplasm</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.98%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（1 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2919585/" target="_blank">2919585</a></td><td>1989</td><td>Article</td><td>The American journal</td><td>The biotransformed metabolite profiles in blood after intrav...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. apical periodontitis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.98%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. suppurative periapical periodontitis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.98%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. periapical granuloma</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.98%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. disorder of phenylalanine metabolism</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.96%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. urolithiasis</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.96%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（1 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/6080021/" target="_blank">6080021</a></td><td>1967</td><td>Article</td><td>Journal of the Canad</td><td>Nephrotomography in various renal disorders.</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. disorder of tyrosine metabolism</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.94%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>


## 台灣上市狀態

| 許可證號 | 商品名 | 劑型 | 狀態 |
|----------|--------|------|------|
| 衛署藥製字第014319號 | 派頓去氫膽酸錠 | 錠劑 | **有效** (至2028/05/25) |
| 內衛藥製字第004206號 | 得利膽錠 | 錠劑 | 已註銷 |
| 其他多項 | - | 粉劑/注射劑 | 已註銷 |

**現況**：台灣目前僅剩派頓去氫膽酸錠一項有效許可證。

## 安全性

### 藥物交互作用

| 併用藥物 | 嚴重程度 | 來源 |
|----------|----------|------|
| Cyclosporine | Minor | DDInter |

### 警語與禁忌

- 仿單詳細資訊未提供完整警語資料
- 一般禁忌：完全膽道阻塞時禁用

## 結論

### 整體評估：低優先級

Dehydrocholic acid 的 TxGNN 預測新適應症主要集中在膽道相關疾病，與其原有適應症高度重疊，不具真正的老藥新用價值。對於腎臟相關預測（如急性尿酸腎病、腎結石），缺乏機轉支持和臨床證據。

### 建議

1. **不建議**進一步投入資源研究此藥物的新適應症
2. 維持其作為傳統利膽劑的角色
3. 台灣目前僅剩一項有效許可證，市場重要性已大幅下降

### 證據等級總結

| 預測適應症 | TxGNN 分數 | 臨床試驗 | 文獻支持 | 機轉合理性 | 綜合評估 |
|------------|------------|----------|----------|------------|----------|
| 急性尿酸腎病 | 0.9999 | 無 | 無 | 低 | 不推薦 |
| 腎結石 | 0.9999 | 無 | 極弱 | 低 | 不推薦 |
| 膽道疾病 | 0.9999 | 無 | 有 | 高 | 已為適應症 |
| 膽管腫瘤 | 0.9998 | 無 | 極弱 | 低 | 不推薦 |

---
*報告產生日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、台灣 FDA*


---

## 相關藥物報告

- [Theophylline]({{ "/drugs/theophylline/" | relative_url }}) - 證據等級 L5
- [Scopolamine]({{ "/drugs/scopolamine/" | relative_url }}) - 證據等級 L5
- [Fenoprofen]({{ "/drugs/fenoprofen/" | relative_url }}) - 證據等級 L5
- [Sodium Citrate]({{ "/drugs/sodium_citrate/" | relative_url }}) - 證據等級 L5
- [Belimumab]({{ "/drugs/belimumab/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Dehydrocholic Acid老藥新用驗證報告. https://twtxgnn.yao.care/drugs/dehydrocholic_acid/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_dehydrocholic_acid,
  title = {Dehydrocholic Acid老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/dehydrocholic_acid/}
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
