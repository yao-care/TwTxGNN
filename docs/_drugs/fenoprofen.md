---
layout: default
title: Fenoprofen
description: "Fenoprofen 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L4
indication_count: 10
---

# Fenoprofen

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Fenoprofen 藥師評估筆記

## 一句話總結

<p class="key-answer" data-question="Fenoprofen 可以用於治療什麼新適應症？">
Fenoprofen 是一種 NSAID 類止痛藥，TxGNN 預測其可用於多種骨骼肌肉疾病，其中僵直性脊椎炎的預測具有多項臨床試驗支持。
</p>

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Fenoprofen (芬諾普芬) |
| DrugBank ID | DB00573 |
| 台灣商品名 | 風諾保膠囊 |
| 原核准適應症 | 風濕性關節炎、骨關節炎、急性痛風、鎮痛、解熱 |
| 預測新適應症 | osteoarthritis susceptibility、osteoarthritis、rheumatoid arthritis、acromesomelic dysplasia, Hunter-Thompson type、brachyolmia-amelogenesis imperfecta syndrome、myosclerosis、brachyolmia、brachydactyly-syndactyly syndrome、colobomatous microphthalmia-rhizomelic dysplasia syndrome、arthropathy |
| 最高預測分數 | 0.9999 (acromesomelic dysplasia) |
| 證據等級 | L2 (僵直性脊椎炎有多個臨床試驗) |



## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. acromesomelic dysplasia, Hunter-Thompson type</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">100.00%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>Fenoprofen 作為丙酸類 NSAID，其對預測適應症的機轉如下：</p>

<ol>
<li><strong>COX 抑制作用</strong>：同時抑制 COX-1 和 COX-2，減少前列腺素合成</li>
<li><strong>抗發炎效果</strong>：對關節炎和脊椎炎的發炎有效</li>
<li><strong>止痛作用</strong>：中樞和周邊的止痛機轉</li>
<li><strong>同類藥物比較</strong>：屬於與 naproxen、ibuprofen 同類的丙酸類 NSAID</li>
</ol>

<h3>臨床試驗</h3>

<p>### 僵直性脊椎炎相關試驗</p>

<p>雖然 ClinicalTrials.gov 未找到近期試驗，但 PubMed 文獻記載了多項歷史臨床試驗：</p>

<table>
<thead>
<tr>
<th>研究</th>
<th>設計</th>
<th>關鍵發現</th>
</tr>
</thead>
<tbody>
<tr>
<td>Wordsworth 1980</td>
<td>雙盲交叉試驗</td>
<td>Fenoprofen 600mg tid vs Phenylbutazone 100mg tid；Phenylbutazone 較優</td>
</tr>
<tr>
<td>Wasner 1981</td>
<td>雙盲隨機試驗</td>
<td>比較 6 種 NSAIDs，fenoprofen 為僵直性脊椎炎的有效選擇之一</td>
</tr>
<tr>
<td>Shipley 1980</td>
<td>雙盲交叉試驗</td>
<td>Fenoprofen vs Indomethacin vs 安慰劑比較</td>
</tr>
</tbody>
</table>

<p><strong>證據等級：L2 (多個臨床試驗)</strong></p>

<h3>相關文獻</h3>

<p>### 僵直性脊椎炎</p>

<table>
<thead>
<tr>
<th>PMID</th>
<th>年份</th>
<th>研究類型</th>
<th>關鍵發現</th>
</tr>
</thead>
<tbody>
<tr>
<td>7010512</td>
<td>1980</td>
<td>RCT</td>
<td>30 位患者；fenoprofen 改善胸廓擴張，但整體效果不如 phenylbutazone</td>
</tr>
<tr>
<td>7026817</td>
<td>1981</td>
<td>RCT</td>
<td>32 位患者；naproxen、indomethacin、fenoprofen 為最有效的三種 NSAIDs</td>
</tr>
<tr>
<td>6996071</td>
<td>1980</td>
<td>RCT</td>
<td>Fenoprofen 優於安慰劑，但不如 indomethacin</td>
</tr>
<tr>
<td>324748</td>
<td>1977</td>
<td>綜述</td>
<td>Fenoprofen 2.4g/day 用於僵直性脊椎炎的療效與安全性回顧</td>
</tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. brachyolmia-amelogenesis imperfecta syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">100.00%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. myosclerosis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">100.00%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. brachyolmia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">100.00%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. brachydactyly-syndactyly syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.99%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. colobomatous microphthalmia-rhizomelic dysplasia syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.99%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. pseudoachondroplasia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.99%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. spondyloarthropathy, susceptibility to</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.99%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. WHIM syndrome</span>
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
<span class="indication-name">10. ankylosing spondylitis</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.94%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（9 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/391117/" target="_blank">391117</a></td><td>1979</td><td>Article</td><td>Annals of internal m</td><td>Ibuprofen.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/7010512/" target="_blank">7010512</a></td><td>1980</td><td>Article</td><td>Rheumatology and reh</td><td>A double-blind cross-over trial of fenoprofen and phenylbuta...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36583943/" target="_blank">36583943</a></td><td>2023</td><td>Article</td><td>ChemMedChem</td><td>Carborane Analogues of Fenoprofen Exhibit Improved Antitumor...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/324748/" target="_blank">324748</a></td><td>1977</td><td>Article</td><td>Drugs</td><td>Fenoprofen: a review of its pharmacological properties and t...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/7026817/" target="_blank">7026817</a></td><td>1981</td><td>Article</td><td>JAMA</td><td>Nonsteroidal anti-inflammatory agents in rheumatoid arthriti...</td></tr>
</tbody>
</table>
<p><em>...及其他 4 篇文獻</em></p>

</div>
</details>


## 台灣上市資訊

| 許可證字號 | 中文品名 | 劑量 | 許可證持有者 | 狀態 |
|-----------|---------|------|-------------|------|
| 衛署藥製字第041435號 | 應元炎普朗膠囊 | 200mg | 應元化學製藥 | 有效 |
| 衛署藥製字第037862號 | 伏炎痛膠囊 | - | 西德有機化學藥品 | 有效 |
| 衛署藥製字第011765號 | 風諾保膠囊 | 300mg | 臺灣禮來 | 已註銷 |

**注意**：多數 fenoprofen 製劑已註銷，目前在台灣取得較困難。

## 安全性考量

### 已知風險
- **胃腸道風險**：潰瘍、出血、穿孔
- **心血管風險**：NSAIDs 類效應，可能增加心血管事件風險
- **腎臟風險**：可能導致急性腎損傷，尤其在脫水狀態
- **過敏反應**：aspirin 過敏者可能交叉過敏

### 藥物交互作用

根據 DDInter 資料庫：

| 交互作用藥物 | 嚴重度 | 說明 |
|-------------|--------|------|
| Acetylsalicylic acid | Moderate | 增加胃腸道出血風險 |
| Hydrocortisone | Moderate | 增加胃腸道副作用 |
| Metformin | Moderate | 可能增加乳酸中毒風險 |
| Triamcinolone | Moderate | 增加胃腸道副作用 |
| Famotidine | Minor | 可降低 NSAIDs 相關潰瘍風險 |
| Ranitidine | Minor | 可降低 NSAIDs 相關潰瘍風險 |

### 禁忌症
- 活動性胃腸道潰瘍或出血
- 嚴重心衰竭
- 冠狀動脈繞道手術前後
- 對 NSAIDs 或 aspirin 過敏

### 特殊族群
- **孕婦**：C 級(第三孕期 D 級)，避免使用
- **哺乳**：分泌至乳汁，不建議使用
- **老年人**：增加胃腸道出血風險，建議最低有效劑量
- **腎功能不全**：避免使用或減量


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**Anemia** 🟡 Moderate
- 需定期監測。風險包括：出血、貧血。

**心臟衰竭** 🟡 Moderate
- 應避免使用本藥物。需定期監測。可能有嚴重不良反應。

**肝臟疾病** 🟡 Moderate
- 需定期監測。風險包括：肝毒性。可能有致命風險。

**Hyperkalemia** 🟡 Moderate
- 應謹慎使用本藥物。

**高血壓** 🟡 Moderate
- 應謹慎使用本藥物。需密切監測。

**Blood Platelet Disorders** 🟡 Moderate
- 風險包括：出血、血栓。可能有嚴重不良反應。

**氣喘** 🟢 Minor
- 本藥物在此情況下禁用。需定期監測。可能有致命風險。

**Water-Electrolyte Imbalance** 🟢 Minor
- 需密切監測。

**消化性潰瘍** 🟢 Minor
- 應謹慎使用本藥物。風險包括：出血。可能有致命風險。特別注意族群：老年人。

**Exanthema** 🟢 Minor
- 本藥物在此情況下禁用。可能有致命風險。必要時應停止治療。

**腎臟疾病** 🟢 Minor
- 應避免使用本藥物。需定期監測。特別注意族群：老年人。

**Thrombosis** 🟢 Minor
- 本藥物在此情況下禁用。需定期監測。風險包括：血栓。可能有致命風險。

### 藥物-食物交互作用 (DFI)

<div class="dfi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**酒精** 🟡 Moderate
- 影響：產生協同作用。可能降低藥效。
- 建議：請諮詢醫師或藥師了解詳細建議。


## 結論與下一步

### 整體評估
僵直性脊椎炎的預測**具有臨床價值**，原因如下：
1. 多個歷史 RCT 支持 fenoprofen 對僵直性脊椎炎的療效
2. NSAIDs 是僵直性脊椎炎的一線治療藥物
3. 部分原核准適應症已涵蓋此用途

其他預測（如罕見骨骼發育異常）缺乏證據，不建議應用。

### 建議行動
- [x] 僵直性脊椎炎可作為 fenoprofen 的合理使用適應症
- [ ] 考量到 fenoprofen 在台灣取得困難，可優先選用其他同類 NSAIDs
- [ ] 其他預測的罕見疾病需要進一步研究

### 臨床建議
對於僵直性脊椎炎患者：
1. NSAIDs 仍是一線藥物選擇
2. Fenoprofen 是有效選項之一，但療效可能不如 indomethacin 或 naproxen
3. 若 fenoprofen 不可得，可選用其他丙酸類 NSAIDs

### 風險等級
**中等風險** - 僵直性脊椎炎使用有證據支持，但需注意 NSAIDs 通用風險

---

*報告生成日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、TFDA*

---

## 相關藥物報告

- [Dipyridamole]({{ "/drugs/dipyridamole/" | relative_url }}) - 證據等級 L5
- [Travoprost]({{ "/drugs/travoprost/" | relative_url }}) - 證據等級 L5
- [Pemetrexed]({{ "/drugs/pemetrexed/" | relative_url }}) - 證據等級 L5
- [Polysorbate 80]({{ "/drugs/polysorbate_80/" | relative_url }}) - 證據等級 L5
- [Ferrous Gluconate]({{ "/drugs/ferrous_gluconate/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Fenoprofen老藥新用驗證報告. https://twtxgnn.yao.care/drugs/fenoprofen/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_fenoprofen,
  title = {Fenoprofen老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/fenoprofen/}
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
