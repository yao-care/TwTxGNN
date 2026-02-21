---
layout: default
title: Pitolisant
description: "Pitolisant 的老藥新用潛力分析。模型預測等級 L5，包含 3 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 129
evidence_level: L3
indication_count: 3
---

# Pitolisant

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>3</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Pitolisant 藥師筆記

## 一句話總結

<p class="key-answer" data-question="Pitolisant 可以用於治療什麼新適應症？">
Pitolisant 為選擇性組織胺 H3 受體反向激動劑，TxGNN 預測對失眠及 ADHD 有潛在療效，已有文獻支持其促醒及認知增強作用。
</p>

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥品學名 | Pitolisant (唯醒) |
| DrugBank ID | DB11642 |
| 原核准適應症 | 猝睡症（伴隨或未伴隨猝倒）、阻塞性睡眠呼吸中止引起的日間過度嗜睡 |
| TxGNN 預測新適應症 | insomnia (disease)、attention deficit-hyperactivity disorder、faciodigitogenital syndrome |
| 台灣許可證數 | 4 張 |
| 最高證據等級 | L3 (觀察性研究/文獻回顧) |



## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. insomnia (disease)</span>
<span class="evidence-badge evidence-L3">L3</span>
<span class="prediction-score">99.71%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>Pitolisant 作為 H3 受體反向激動劑，其預測的新適應症在機轉上具有合理性：</p>

<ol>
<li><strong>失眠 (Insomnia)</strong>：H3 受體阻斷可增加腦內組織胺釋放，促進覺醒。雖看似矛盾，但改善睡眠-覺醒週期調控可能對某些失眠類型有益</li>
<li><strong>注意力不足過動症 (ADHD)</strong>：組織胺系統參與注意力及認知功能調控，H3 受體拮抗劑可增強覺醒及注意力</li>
<li><strong>Aarskog 症候群</strong>：預測機轉不明確，可能為模型假陽性</li>
</ol>

<h3>臨床試驗</h3>

<table>
<thead>
<tr>
<th>預測適應症</th>
<th>臨床試驗數</th>
<th>代表性試驗</th>
</tr>
</thead>
<tbody>
<tr>
<td>失眠</td>
<td>1 (間接)</td>
<td>NCT02800083: Pitolisant 治療酒精使用障礙（評估睡眠作為次要指標）</td>
</tr>
<tr>
<td>ADHD</td>
<td>0</td>
<td>直接試驗無，但有相關文獻討論</td>
</tr>
</tbody>
</table>

<h3>相關文獻</h3>

<p>### 失眠 (Insomnia)</p>
<p><strong>證據等級：L3 (觀察性研究/回顧性文獻)</strong></p>

<table>
<thead>
<tr>
<th>PMID</th>
<th>標題</th>
<th>年份</th>
<th>重點發現</th>
</tr>
</thead>
<tbody>
<tr>
<td>34225942</td>
<td>Histamine receptors in health and disease</td>
<td>2021</td>
<td>綜述 H3 受體在睡眠-覺醒調控中的角色，Pitolisant 為治療猝睡症的新選項</td>
</tr>
<tr>
<td>36169322</td>
<td>Real-life WAKE study in narcolepsy with pitolisant</td>
<td>2022</td>
<td>觀察性研究顯示 Pitolisant 對既往治療無效的猝睡症患者有效，提及失眠評估</td>
</tr>
<tr>
<td>30214155</td>
<td>Profile of pitolisant in narcolepsy management</td>
<td>2018</td>
<td>系統性回顧 Pitolisant 的藥效學與藥動學特性</td>
</tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. attention deficit-hyperactivity disorder</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.36%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（7 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/32882898/" target="_blank">32882898</a></td><td>2020</td><td>Article</td><td>Medicines (Basel, Sw</td><td>Pitolisant and Other Histamine-3 Receptor Antagonists-An Upd...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/34534876/" target="_blank">34534876</a></td><td>2021</td><td>Article</td><td>Epilepsy &amp; behavior </td><td>Drugs for patients with epilepsy and excessive daytime sleep...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/24122734/" target="_blank">24122734</a></td><td>2013</td><td>Article</td><td>Drugs</td><td>Current and emerging options for the drug treatment of narco...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/27363923/" target="_blank">27363923</a></td><td>2016</td><td>Article</td><td>Behavioural brain re</td><td>Histamine H3 receptor as a potential target for cognitive sy...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30359639/" target="_blank">30359639</a></td><td>2019</td><td>Article</td><td>Neuropharmacology</td><td>Drug-receptor kinetics and sigma-1 receptor affinity differe...</td></tr>
</tbody>
</table>
<p><em>...及其他 2 篇文獻</em></p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. faciodigitogenital syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.29%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>


## 台灣上市資訊

### 上市狀態
台灣已核准上市，共有 4 張許可證（2 種劑量規格各 2 張）。

### 代表性產品

| 許可證字號 | 商品名 | 劑型 | 許可證持有者 | 效期 |
|------------|--------|------|--------------|------|
| 衛部藥輸字第028103號 | 唯醒膜衣錠4.5毫克 (Wakix) | 膜衣錠 | 信東生技股份有限公司 | 2026/07/13 |
| 衛部藥輸字第028104號 | 唯醒膜衣錠18毫克 (Wakix) | 膜衣錠 | 信東生技股份有限公司 | 2026/07/13 |

### 核准適應症
1. 治療 6 歲以上猝睡症（伴隨或未伴隨猝倒現象）
2. 改善阻塞性睡眠呼吸中止 (OSA) 成人病人的覺醒狀態並減少日間過度嗜睡 (EDS)

## 安全性考量

### 藥物交互作用

DDInter 資料庫顯示 Pitolisant 與多種藥物有交互作用：

**嚴重交互作用 (Major)**：
- Bupropion：降低 Pitolisant 代謝，增加血中濃度
- Dolasetron：可能延長 QT 間距

**中度交互作用 (Moderate)**：
- H2 受體阻斷劑：Famotidine, Cimetidine
- 皮質類固醇：Hydrocortisone, Triamcinolone, Dexamethasone, Betamethasone, Budesonide
- 其他：Metformin, Morphine, Clarithromycin, Levofloxacin
- 瀉劑：Bisacodyl, Polyethylene glycol

### 注意事項
1. **QT 延長風險**：避免與其他延長 QT 藥物併用
2. **CYP3A4 誘導**：可能降低併用藥物血中濃度（如口服避孕藥）
3. **肝腎功能不全**：中重度肝功能不全需減量
4. **懷孕/哺乳**：不建議使用


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**躁鬱症** 🟡 Moderate
- 需定期監測。

**Psychotic Disorders** 🟡 Moderate
- 需定期監測。

**Arrhythmias, Cardiac** 🟡 Moderate
- 應避免使用本藥物。需定期監測。風險包括：心律不整。可能有致命風險。

**腎臟疾病** 🟡 Moderate
- 不建議使用本藥物。可能有嚴重不良反應。

**Hepatic Insufficiency** 🟢 Minor
- 本藥物在此情況下禁用。需定期監測。可能需要調整劑量。可能有嚴重不良反應。

## 結論與下一步

### 預測價值評估

| 預測適應症 | 證據等級 | 文獻支持 | 臨床試驗 | 總評 |
|------------|----------|----------|----------|------|
| 失眠 | L3 | 8 篇 | 1 (間接) | 中度支持 |
| ADHD | L3-L4 | 7 篇 | 0 | 輕度支持 |
| Aarskog 症候群 | L5 | 0 | 0 | 無支持 |

### 建議
1. **ADHD**：基於 H3 受體在認知功能的角色，值得進一步探索，但目前缺乏直接臨床試驗
2. **失眠**：看似矛盾但改善睡眠-覺醒週期調控可能對某些睡眠障礙有益，需更多研究
3. Pitolisant 相對新穎（台灣 2021 年核准），臨床經驗仍在累積中

---
*本筆記由 TwTxGNN 系統自動產生，僅供研究參考，不構成醫療建議。*
*產生日期：2026-02-11*

---

## 相關藥物報告

- [Titanium Dioxide]({{ "/drugs/titanium_dioxide/" | relative_url }}) - 證據等級 L5
- [Metoprolol]({{ "/drugs/metoprolol/" | relative_url }}) - 證據等級 L5
- [Atezolizumab]({{ "/drugs/atezolizumab/" | relative_url }}) - 證據等級 L5
- [Etanercept]({{ "/drugs/etanercept/" | relative_url }}) - 證據等級 L5
- [Brivaracetam]({{ "/drugs/brivaracetam/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Pitolisant老藥新用驗證報告. https://twtxgnn.yao.care/drugs/pitolisant/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_pitolisant,
  title = {Pitolisant老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/pitolisant/}
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
