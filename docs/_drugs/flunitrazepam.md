---
layout: default
title: Flunitrazepam
description: "Flunitrazepam 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L3
indication_count: 10
---

# Flunitrazepam

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Flunitrazepam (氟硝西泮) - 藥師評估報告

## 一句話總結

<p class="key-answer" data-question="Flunitrazepam 可以用於治療什麼新適應症？">
氟硝西泮是一種苯二氮平類安眠藥，TxGNN 預測其對失眠（疾病分類）有效，這實際上與其核准適應症完全重疊；另預測對偏頭痛和焦慮有潛在療效，部分有臨床證據支持。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物學名 | Flunitrazepam |
| 台灣商品名 | 氟耐妥眠 |
| DrugBank ID | DB01544 |
| 原核准適應症 | 失眠、安眠、鎮靜 |
| 預測新適應症 | insomnia (disease)、migraine disorder、migraine with brainstem aura、anxiety、焦慮症、alcohol withdrawal delirium、migraine with or without aura, susceptibility to、agoraphobia、benign paroxysmal torticollis of infancy、atrophoderma vermiculata |
| 最高證據等級 | L2 (有臨床試驗) |
| 台灣上市狀態 | 有效許可證（管制藥品） |




## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. insomnia (disease)</span>
<span class="evidence-badge evidence-L3">L3</span>
<span class="prediction-score">99.89%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>氟硝西泮是一種強效苯二氮平類藥物，其預測適應症與其 GABA-A 受體調節機制相關：</p>

<ol>
<li><strong>失眠（疾病）</strong> (TxGNN Score: 0.999, Rank: 2959)：這實際上與原核准適應症相同，是模型準確識別已知適應症的例證。</li>

<li><strong>偏頭痛</strong> (TxGNN Score: 0.997, Rank: 6338)：苯二氮平類藥物可能透過 GABA 能機制調節疼痛傳導，且偏頭痛常與睡眠障礙共病。</li>

<li><strong>焦慮</strong> (TxGNN Score: 0.996, Rank: 7852)：苯二氮平類藥物的抗焦慮作用是其核心藥理特性之一，氟硝西泮確實具有顯著的抗焦慮效果。</li>
</ol>

<h3>臨床試驗</h3>

<p>### 失眠相關試驗</p>

<table>
<thead>
<tr>
<th>試驗編號</th>
<th>標題</th>
<th>階段</th>
<th>狀態</th>
<th>國家</th>
</tr>
</thead>
<tbody>
<tr>
<td>NCT02648776</td>
<td>老年人安眠藥物風險效益評估</td>
<td>N/A</td>
<td>狀態不明</td>
<td>台灣</td>
</tr>
</tbody>
</table>

<p><strong>特別注意：</strong> 此試驗由中國醫藥大學附設醫院執行，專門評估台灣老年人使用安眠藥（包含 flunitrazepam）的用藥模式、療效和安全性。</p>

<h3>相關文獻</h3>

<p>針對失眠適應症，檢索到 11 篇相關 PubMed 文獻：</p>

<p><strong>重點文獻：</strong></p>

<ol>
<li><strong>Murciano D et al. (1993)</strong> - European Respiratory Journal</li>
</ol>
<ul>
<li>比較 zolpidem、triazolam 和 flunitrazepam 對嚴重 COPD 患者的急性效果</li>
<li>顯示各藥物對呼吸功能的影響差異</li>

</ul>
<ol>
<li><strong>Kales A et al. (1979)</strong> - JAMA</li>
</ol>
<ul>
<li>首次描述苯二氮平類藥物的「反跳性失眠」現象</li>
<li>指出 flunitrazepam 因中等半衰期可能引起停藥後反跳性失眠</li>

</ul>
<ol>
<li><strong>Rickels K (1986)</strong> - Acta Psychiatrica Scandinavica</li>
</ol>
<ul>
<li>綜述安眠藥的臨床使用</li>
<li>討論 flunitrazepam 作為長效安眠藥的定位</li>

</ul>
<ol>
<li><strong>Cook PJ (1986)</strong> - Acta Psychiatrica Scandinavica</li>
</ol>
<ul>
<li>探討老年人使用苯二氮平類安眠藥的藥效學變化</li>
<li>發現老年人對 flunitrazepam 反應增加 2-3 倍</li>

</ul>
<p>針對焦慮適應症，檢索到 15 篇相關文獻，多數涉及藥物濫用和法醫毒理學議題。</p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. migraine disorder</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.71%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. migraine with brainstem aura</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.63%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. anxiety</span>
<span class="evidence-badge evidence-L3">L3</span>
<span class="prediction-score">99.63%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（1 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02648776" target="_blank">NCT02648776</a></td><td>N/A</td><td>UNKNOWN</td><td>1400</td><td>Risk and Benefit Assessment of Hypnotic Agents for Sleep Disorders Among Elderly...</td></tr>
</tbody>
</table>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/9475831/" target="_blank">9475831</a></td><td>1998</td><td>Article</td><td>The Annals of pharma</td><td>Use and abuse of flunitrazepam.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/6110431/" target="_blank">6110431</a></td><td>1981</td><td>Article</td><td>British journal of a</td><td>Flunitrazepam.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/9169981/" target="_blank">9169981</a></td><td>1997</td><td>Article</td><td>Journal of clinical </td><td>Abuse liability of flunitrazepam.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/15365913/" target="_blank">15365913</a></td><td>2004</td><td>Article</td><td>Fortschritte der Neu</td><td>[Flunitrazepam and driving ability].</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/9107334/" target="_blank">9107334</a></td><td>1997</td><td>Article</td><td>Academic emergency m</td><td>Flunitrazepam and its involvement in date or acquaintance ra...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. anxiety disorder</span>
<span class="evidence-badge evidence-L3">L3</span>
<span class="prediction-score">99.58%</span>
</summary>
<div class="indication-content">

<h3>臨床試驗（1 項）</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT02648776" target="_blank">NCT02648776</a></td><td>N/A</td><td>UNKNOWN</td><td>1400</td><td>Risk and Benefit Assessment of Hypnotic Agents for Sleep Disorders Among Elderly...</td></tr>
</tbody>
</table>

<h3>相關文獻（20 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/40704033/" target="_blank">40704033</a></td><td>2025</td><td>Article</td><td>Frontiers in psychia</td><td>Adverse events of pharmacological interventions for insomnia...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/9475831/" target="_blank">9475831</a></td><td>1998</td><td>Article</td><td>The Annals of pharma</td><td>Use and abuse of flunitrazepam.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/9169981/" target="_blank">9169981</a></td><td>1997</td><td>Article</td><td>Journal of clinical </td><td>Abuse liability of flunitrazepam.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/11672967/" target="_blank">11672967</a></td><td>2001</td><td>Article</td><td>Forensic science int</td><td>Flunitrazepam: an evaluation of use, abuse and toxicity.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/12063892/" target="_blank">12063892</a></td><td>2002</td><td>Article</td><td>American journal of </td><td>Club drugs: methylenedioxymethamphetamine, flunitrazepam, ke...</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. alcohol withdrawal delirium</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.50%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（6 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/8214408/" target="_blank">8214408</a></td><td>1993</td><td>Article</td><td>Alcoholism, clinical</td><td>Intravenous flunitrazepam in the treatment of alcohol withdr...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/14557857/" target="_blank">14557857</a></td><td>2003</td><td>Article</td><td>Intensive care medic</td><td>Alcohol withdrawal severity is decreased by symptom-orientat...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/1329785/" target="_blank">1329785</a></td><td>1992</td><td>Article</td><td>Alcohol and alcoholi</td><td>Functional alterations in cerebral GABAA receptor complex as...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/8383922/" target="_blank">8383922</a></td><td>1993</td><td>Article</td><td>Alcoholism, clinical</td><td>Chronic ethanol intoxication induces differential effects on...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/42267/" target="_blank">42267</a></td><td>1979</td><td>Article</td><td>Activitas nervosa su</td><td>Flunitrazepam in the treatment of delirium tremens. -- Preli...</td></tr>
</tbody>
</table>
<p><em>...及其他 1 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. migraine with or without aura, susceptibility to</span>
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
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/22938964/" target="_blank">22938964</a></td><td>2012</td><td>Article</td><td>Handbook of clinical</td><td>Animal models.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/16201993/" target="_blank">16201993</a></td><td>2005</td><td>Article</td><td>Epilepsia</td><td>Rearranging receptors.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/22266888/" target="_blank">22266888</a></td><td>2011</td><td>Article</td><td>Seminars in neurolog</td><td>Genetics of epilepsy.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/34575901/" target="_blank">34575901</a></td><td>2021</td><td>Article</td><td>International journa</td><td>Selected Molecular Targets for Antiepileptogenesis.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/34209535/" target="_blank">34209535</a></td><td>2021</td><td>Article</td><td>International journa</td><td>Neuroinflammation: A Signature or a Cause of Epilepsy?</td></tr>
</tbody>
</table>
<p><em>...及其他 15 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. agoraphobia</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.39%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（2 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2836759/" target="_blank">2836759</a></td><td>1987</td><td>Article</td><td>Neuropsychobiology</td><td>A 3H-flunitrazepam binding inhibitor is present in psychiatr...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/2554193/" target="_blank">2554193</a></td><td>1989</td><td>Article</td><td>Neuropsychobiology</td><td>Further investigation on benzodiazepine binding inhibitory a...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. benign paroxysmal torticollis of infancy</span>
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
<span class="indication-name">10. atrophoderma vermiculata</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.20%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>


## 台灣上市資訊

**管制藥品注意事項：**
氟硝西泮在台灣屬於第三級管制藥品，使用需特別謹慎。

**原核准適應症：**
- 失眠
- 安眠、鎮靜
- 失眠症
- 寧神藥

## 安全性考量

### 重要警語

1. **濫用潛力**：氟硝西泮具有高度濫用潛力，曾被媒體報導與「約會強暴藥」相關
2. **順行性遺忘**：可能導致服藥後的記憶空白
3. **呼吸抑制**：與酒精或其他中樞神經抑制劑併用時風險增加
4. **依賴性**：長期使用可能產生身體依賴

### 特殊族群注意事項

| 族群 | 注意事項 |
|------|----------|
| 老年人 | 反應增強，建議減量 |
| COPD 患者 | 可能加重呼吸抑制 |
| 肝功能不全 | 代謝減慢，需調整劑量 |
| 孕婦 | 可能致畸，懷孕期間禁用 |

### 藥物交互作用

苯二氮平類藥物的常見交互作用：
- CYP3A4 抑制劑可能增加血中濃度
- 與酒精、鴉片類藥物併用增加呼吸抑制風險
- 與其他 CNS 抑制劑有加成效果

### 藥物-食物交互作用 (DFI)

**酒精** 🔴 Major
- 影響：酒精顯著增強鎮靜作用，可能導致呼吸抑制
- 建議：絕對禁止飲酒

### 藥物-草藥交互作用 (DHI)

**卡瓦** 🔴 Major
- 影響：嚴重增強中樞神經抑制
- 建議：禁止併用

**纈草** 🟡 Moderate
- 影響：增強鎮靜作用
- 建議：避免併用


## 結論與下一步

### 預測評估結論

氟硝西泮的預測適應症中，「失眠」實際上是原核准適應症，驗證了 TxGNN 模型能正確識別已知藥物-疾病關係。「焦慮」的預測也與苯二氮平類藥物的已知藥理作用一致。「偏頭痛」的預測較為新穎，但缺乏直接證據。

### 證據等級總結

| 預測適應症 | TxGNN Score | 證據等級 | 評估 |
|------------|-------------|----------|------|
| 失眠（疾病） | 0.999 | L2 | 已核准適應症，有台灣臨床試驗 |
| 偏頭痛 | 0.997 | L5 | 機轉可能相關，缺乏直接證據 |
| 焦慮 | 0.996 | L2 | 藥理作用支持，有臨床試驗 |

### 建議

1. **失眠**：此預測確認已知療效，無需額外研究
2. **焦慮**：雖然機轉支持療效，但考量管制藥品身份和濫用風險，不建議優先開發此適應症
3. **偏頭痛**：缺乏直接證據，且有更安全的替代藥物

### 整體評估

由於氟硝西泮的管制藥品地位和濫用風險，不建議將其作為老藥新用的優先候選藥物。預測的「新」適應症實際上多為已知或可預期的藥理作用延伸。

---

*報告生成日期：2026-02-11*
*資料來源：TxGNN 知識圖譜預測、ClinicalTrials.gov、PubMed、台灣 FDA*


---

## 相關藥物報告

- [Naproxen]({{ "/drugs/naproxen/" | relative_url }}) - 證據等級 L5
- [Salicylic Acid]({{ "/drugs/salicylic_acid/" | relative_url }}) - 證據等級 L5
- [Alprostadil]({{ "/drugs/alprostadil/" | relative_url }}) - 證據等級 L5
- [Cerliponase Alfa]({{ "/drugs/cerliponase_alfa/" | relative_url }}) - 證據等級 L5
- [Simoctocog Alfa]({{ "/drugs/simoctocog_alfa/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Flunitrazepam老藥新用驗證報告. https://twtxgnn.yao.care/drugs/flunitrazepam/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_flunitrazepam,
  title = {Flunitrazepam老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/flunitrazepam/}
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
