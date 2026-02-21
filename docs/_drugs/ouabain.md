---
layout: default
title: Ouabain
description: "Ouabain 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L4
indication_count: 10
---

# Ouabain

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ouabain 藥師筆記

## 一句話總結

<p class="key-answer" data-question="Ouabain 可以用於治療什麼新適應症？">
Ouabain 為強心配醣體類藥物，TxGNN 預測其可能對鐮刀型紅血球貧血和心肌梗塞有治療潛力，但目前僅有前臨床研究支持，需謹慎評估其治療窗口極窄的安全性問題。
</p>


---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥品名稱 | Ouabain (歐巴因) |
| DrugBank ID | DB01092 |
| 台灣商品名 | 安保心注射液 |
| 原適應症 | 心臟衰竭、心房撲動、心房纖維顫動、陣發性上室性心搏過速 |
| 預測新適應症 | Prinzmetal angina、hemoglobinopathy、myocardial infarction、thrombotic disease、hyperthyroidism、homozygous familial hypercholesterolemia、partial deletion of the short arm of chromosome 16、beta-thalassemia with other manifestations、brain small vessel disease 1 with or without ocular anomalies、autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome |
| 證據等級 | L4 (前臨床研究) |
| TxGNN 預測分數 | 0.995 (鐮刀型紅血球貧血)、0.994 (心肌梗塞) |

---



## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. Prinzmetal angina</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.69%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>### 機轉連結</p>

<ol>
<li><strong>鐮刀型紅血球貧血</strong>：Ouabain 作為 Na+/K+-ATPase 抑制劑，可調節紅血球陽離子運輸。研究顯示鐮刀型紅血球的陽離子通透性異常，ouabain 敏感性的 ATPase 活性在這些細胞中呈現特殊表現，可能有助於調節細胞膜穩定性。</li>

<li><strong>心肌梗塞</strong>：腦內類 ouabain 化合物 (ouabain-like compounds) 與腎素-血管張力素系統在心肌梗塞後的交感神經過度活化中扮演關鍵角色。低劑量 ouabain 可能透過 Na/K-ATPase 訊號傳導途徑產生心臟保護作用。</li>
</ol>

<h3>臨床試驗</h3>

<p>目前無針對上述預測適應症的已完成臨床試驗。</p>

<h3>相關文獻</h3>

<p>### 鐮刀型紅血球貧血相關研究</p>

<table>
<thead>
<tr>
<th>PMID</th>
<th>發表年份</th>
<th>主要發現</th>
</tr>
</thead>
<tbody>
<tr>
<td>149799</td>
<td>1978</td>
<td>發現不可逆鐮刀型細胞的主動陽離子運輸下降，但膜 Na,K-ATPase 活性正常</td>
</tr>
<tr>
<td>2213597</td>
<td>1990</td>
<td>脫氧使鐮刀型貧血紅血球對鎂離子通透化，可能影響離子梯度</td>
</tr>
<tr>
<td>7204577</td>
<td>1981</td>
<td>地中海型貧血和骨髓應激狀態下紅血球陽離子通透性增加</td>
</tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. hemoglobinopathy</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.48%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/1891492/" target="_blank">1891492</a></td><td>1991</td><td>Article</td><td>Planta medica</td><td>The in vitro effects of griffonin and ouabain on erythrocyte...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/3026473/" target="_blank">3026473</a></td><td>1987</td><td>Article</td><td>Biochimica et biophy</td><td>Furosemide-sensitive Na+ and K+ transport and human erythroc...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/3034977/" target="_blank">3034977</a></td><td>1987</td><td>Article</td><td>The Journal of clini</td><td>Sodium-potassium pump, ion fluxes, and cellular dehydration ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2947642/" target="_blank">2947642</a></td><td>1987</td><td>Article</td><td>Blood</td><td>The xerocytosis of Hb SC disease.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/3961486/" target="_blank">3961486</a></td><td>1986</td><td>Article</td><td>Science (New York, N</td><td>Regulation of erythrocyte cation and water content in sickle...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. myocardial infarction</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.42%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/10564131/" target="_blank">10564131</a></td><td>1999</td><td>Article</td><td>The American journal</td><td>Brain &quot;ouabain&quot; and angiotensin II contribute to cardiac dys...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/99072/" target="_blank">99072</a></td><td>1977</td><td>Article</td><td>Annals of clinical r</td><td>Pump failure in acute myocardial infarction. Fluid and drug ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/767015/" target="_blank">767015</a></td><td>1976</td><td>Article</td><td>Circulation</td><td>Effects of metabolic and pharmacologic interventions on myoc...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/19486591/" target="_blank">19486591</a></td><td>2009</td><td>Article</td><td>Current heart failur</td><td>The brain renin-angiotensin-aldosterone system: a major mech...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/19787147/" target="_blank">19787147</a></td><td>2009</td><td>Article</td><td>Brazilian journal of</td><td>Ventricular performance and Na+-K+ ATPase activity are reduc...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. thrombotic disease</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.33%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（4 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/41118620/" target="_blank">41118620</a></td><td>2025</td><td>Article</td><td>Blood advances</td><td>The Na/K-ATPase Alpha-1 Subunit Fine-Tunes Platelet P2Y12 Fu...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/6137280/" target="_blank">6137280</a></td><td>1983</td><td>Article</td><td>Cardiovascular clini</td><td>Acute myocardial infarction--coronary thrombosis and salvage...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/1305429/" target="_blank">1305429</a></td><td>1992</td><td>Article</td><td>Eksperimental&#x27;naia i</td><td>[The increased sensitivity of rats to ouabain in the acute s...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/8324469/" target="_blank">8324469</a></td><td>1993</td><td>Article</td><td>Eksperimental&#x27;naia i</td><td>[The effect of ouabain on the cardiovascular system of rats ...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. hyperthyroidism</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.26%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/130826/" target="_blank">130826</a></td><td>1976</td><td>Article</td><td>Annual review of phy</td><td>Cellular thermogenesis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2168011/" target="_blank">2168011</a></td><td>1990</td><td>Article</td><td>Metabolism: clinical</td><td>Erythrocyte sodium fluxes, ouabain binding sites, and Na+,K(...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/1324264/" target="_blank">1324264</a></td><td>1992</td><td>Article</td><td>Journal of endocrino</td><td>Na+K+ATPase activity and ouabain binding sites in erythrocyt...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2370297/" target="_blank">2370297</a></td><td>1990</td><td>Article</td><td>The Journal of clini</td><td>The effect of hyperthyroidism on in vivo aging of erythrocyt...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/4108576/" target="_blank">4108576</a></td><td>1970</td><td>Article</td><td>Klinische Wochenschr</td><td>Serum concentration and urinary excretion of 3 H-ouabain and...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. homozygous familial hypercholesterolemia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.19%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. partial deletion of the short arm of chromosome 16</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.17%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. beta-thalassemia with other manifestations</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.17%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. brain small vessel disease 1 with or without ocular anomalies</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.17%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（19 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/35882526/" target="_blank">35882526</a></td><td>2023</td><td>Article</td><td>Journal of medical g</td><td>Axenfeld-Rieger syndrome: more than meets the eye.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30182440/" target="_blank">30182440</a></td><td>2018</td><td>Article</td><td>American journal of </td><td>Neuropathology of holoprosencephaly.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/33870948/" target="_blank">33870948</a></td><td>2022</td><td>Article</td><td>Journal of neuro-oph</td><td>Optic Nerve Aplasia.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/11941259/" target="_blank">11941259</a></td><td>2002</td><td>Article</td><td>Journal francais d&#x27;o</td><td>[Congenital megalocornea].</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/6390155/" target="_blank">6390155</a></td><td>1983</td><td>Article</td><td>Neurologic clinics</td><td>Optic disk abnormalities.</td></tr>
</tbody>
</table>
<p><em>...及其他 14 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.15%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>


## 台灣上市資訊

| 許可證字號 | 商品名 | 劑型 | 適應症 | 狀態 |
|-----------|--------|------|--------|------|
| 內衛藥製字第001934號 | 安保心注射液 | 注射劑 | 心臟衰竭、心房撲動、心房纖維顫動、陣發性上室性心博過速 | 有效 |
| 內衛藥製字第007192號 | 哇巴因注射液 | 注射劑 | 心臟衰竭、心房撲動 | 已註銷 |
| 衛署藥製字第033771號 | 吾安保因注射液 | 注射劑 | 心臟衰竭、心房撲動 | 已註銷 |

---

## 安全性考量

### 重要警語

- **治療窗口極窄**：Ouabain 屬於強心配醣體，治療劑量與中毒劑量接近
- **心律不整風險**：可能誘發嚴重心律不整，包括心室顫動
- **電解質監測**：低血鉀會增加毒性風險，需密切監測電解質

### 藥物交互作用

目前資料庫中無記載重大藥物交互作用，但臨床上應注意：
- 利尿劑（可能導致低血鉀，增加毒性）
- 其他抗心律不整藥物
- 鈣離子補充劑

### 特殊族群

- 腎功能不全患者需調整劑量
- 老年人對強心配醣體更敏感
- 孕婦及哺乳婦女使用安全性未確立

---

## 結論與下一步

### 整體評估

Ouabain 對鐮刀型紅血球貧血和心肌梗塞的老藥新用預測在機轉上具有合理性，但：

1. **證據等級偏低 (L4)**：目前僅有基礎研究和動物實驗支持
2. **安全性疑慮重大**：治療窗口極窄，臨床應用風險高
3. **臨床可行性有限**：需要開發更安全的給藥方式或找到更安全的類似物

### 建議行動

- **不建議直接進行臨床試驗**：需先進行更多前臨床安全性和有效性研究
- **探索替代策略**：考慮研究其他 Na/K-ATPase 調節劑或開發 ouabain 衍生物
- **持續關注文獻**：追蹤相關基礎研究進展

---

*本報告由 TxGNN 預測系統生成，僅供研究參考，不構成醫療建議。*


---

## 相關藥物報告

- [Clomipramine]({{ "/drugs/clomipramine/" | relative_url }}) - 證據等級 L5
- [Gefitinib]({{ "/drugs/gefitinib/" | relative_url }}) - 證據等級 L5
- [Terbutaline]({{ "/drugs/terbutaline/" | relative_url }}) - 證據等級 L5
- [Remdesivir]({{ "/drugs/remdesivir/" | relative_url }}) - 證據等級 L5
- [Tyrosine]({{ "/drugs/tyrosine/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Ouabain老藥新用驗證報告. https://twtxgnn.yao.care/drugs/ouabain/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_ouabain,
  title = {Ouabain老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/ouabain/}
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
