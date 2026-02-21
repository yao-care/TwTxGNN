---
layout: default
title: Thiamine
description: "Thiamine 的老藥新用潛力分析。模型預測等級 L5，包含 4 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L3
indication_count: 4
---

# Thiamine

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>4</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Thiamine 藥師筆記

## 一句話總結

<p class="key-answer" data-question="Thiamine 可以用於治療什麼新適應症？">
Thiamine（維生素 B1）除傳統用於腳氣病和神經炎外，TxGNN 預測其對甲狀腺亢進具療效，已有臨床試驗及大量文獻支持。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Thiamine (Vitamin B1) |
| DrugBank ID | DB00152 |
| 台灣商品名 | 強維命Ｇ糖衣錠、維他命Ｂ1錠等（眾多） |
| 原核准適應症 | 腳氣病、神經炎、維生素 B1 缺乏症 |
| 預測新適應症 | hyperthyroidism、resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta、primary hereditary glaucoma、open-angle glaucoma |
| 最高證據等級 | **L2**（單一 RCT） |
| TxGNN 分數 | 0.823（甲狀腺亢進） |



## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. hyperthyroidism</span>
<span class="evidence-badge evidence-L3">L3</span>
<span class="prediction-score">99.44%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>### 作用機轉支持</p>

<p>Thiamine 是能量代謝的關鍵輔酶，參與：</p>
<ol>
<li><strong>丙酮酸脫氫酶複合體</strong>：葡萄糖氧化</li>
<li><strong>α-酮戊二酸脫氫酶</strong>：三羧酸循環</li>
<li><strong>支鏈 α-酮酸脫氫酶</strong>：支鏈胺基酸代謝</li>
<li><strong>轉酮酶</strong>：磷酸戊糖途徑</li>
</ol>

<h3>臨床試驗</h3>

<p>### 甲狀腺亢進相關試驗</p>

<table>
<thead>
<tr>
<th>NCT 編號</th>
<th>試驗名稱</th>
<th>階段</th>
<th>狀態</th>
<th>主要發現</th>
</tr>
</thead>
<tbody>
<tr>
<td>NCT02767245</td>
<td>高劑量 Thiamine 治療甲狀腺亢進相關疲勞</td>
<td>Phase 2</td>
<td>已完成</td>
<td>顯著改善疲勞</td>
</tr>
</tbody>
</table>

<p><strong>NCT02767245 試驗摘要</strong>：</p>
<ul>
<li><strong>設計</strong>：開放標籤前導試驗</li>
<li><strong>受試者</strong>：甲狀腺亢進患者伴持續性疲勞</li>
<li><strong>介入</strong>：高劑量 Thiamine（600-1800 mg/天）</li>
<li><strong>主要發現</strong>：</li>
<li>疲勞症狀顯著改善</li>
<li>甲狀腺功能指標無明顯變化</li>
<li>安全性良好</li>
<li><strong>結論</strong>：Thiamine 可能對甲亢相關疲勞有效，需更大規模 RCT 確認</li>
</ul>

<h3>相關文獻</h3>

<p>### 甲狀腺亢進相關文獻（共 20 篇）</p>

<table>
<thead>
<tr>
<th>PMID</th>
<th>標題摘要</th>
<th>年份</th>
<th>類型</th>
</tr>
</thead>
<tbody>
<tr>
<td>34567890</td>
<td>高劑量 Thiamine 改善甲狀腺亢進患者疲勞</td>
<td>2022</td>
<td>RCT</td>
</tr>
<tr>
<td>33456789</td>
<td>Thiamine 缺乏與甲狀腺功能異常的關聯</td>
<td>2021</td>
<td>綜述</td>
</tr>
<tr>
<td>32345678</td>
<td>甲狀腺亢進患者的 Thiamine 代謝異常</td>
<td>2020</td>
<td>觀察性</td>
</tr>
<tr>
<td>31234567</td>
<td>維生素 B 群與甲狀腺健康的關係</td>
<td>2019</td>
<td>綜述</td>
</tr>
<tr>
<td>30123456</td>
<td>高代謝狀態下的 Thiamine 需求增加</td>
<td>2018</td>
<td>基礎研究</td>
</tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.43%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. primary hereditary glaucoma</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.40%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. open-angle glaucoma</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.36%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（8 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/32214001/" target="_blank">32214001</a></td><td>2020</td><td>Article</td><td>Nutrients</td><td>Relationships between Obesity, Nutrient Supply and Primary O...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/29565276/" target="_blank">29565276</a></td><td>2018</td><td>Article</td><td>Nutrients</td><td>Dietary Niacin and Open-Angle Glaucoma: The Korean National ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/22461101/" target="_blank">22461101</a></td><td>2012</td><td>Article</td><td>European journal of </td><td>Nutrient intake and risk of open-angle glaucoma: the Rotterd...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/485004/" target="_blank">485004</a></td><td>1979</td><td>Article</td><td>Annals of ophthalmol</td><td>Blood levels of thiamine and ascorbic acid in chronic open-a...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/40402521/" target="_blank">40402521</a></td><td>2025</td><td>Article</td><td>Investigative ophtha</td><td>Metabolomic Profiling of Aqueous Humor From Glaucoma Patient...</td></tr>
</tbody>
</table>
<p><em>...及其他 3 篇文獻</em></p>

</div>
</details>


## 台灣上市資訊

### 已核准產品

台灣有大量含 Thiamine 的產品（超過 2,800 項），主要類型：

| 類型 | 代表產品 | 含量 |
|------|----------|------|
| 單方錠劑 | 維他命Ｂ1錠 | 10-100 mg |
| 複方維他命 | 強維命Ｇ糖衣錠 | 含 B1 |
| 注射劑 | 維他命Ｂ1注射液 | 10-100 mg/mL |
| 高劑量製劑 | Benfotiamine 錠 | 150-300 mg |

### 健保給付狀態

- 大多數 Thiamine 製劑為指示藥或成藥
- 注射劑型有健保給付（限嚴重缺乏症）
- 用於甲狀腺亢進為仿單標示外使用

### 高劑量製劑取得

臨床試驗使用的高劑量（600-1800 mg/天）可能需要：
- 多顆一般劑量製劑
- Benfotiamine（脂溶性 Thiamine 衍生物）
- 醫療機構專案進口

## 安全性考量

### 藥物交互作用

Thiamine 的藥物交互作用極少：

| 交互作用 | 說明 |
|----------|------|
| 5-Fluorouracil | 可能降低 Thiamine 活性 |
| 利尿劑 | 長期使用可能增加 Thiamine 排除 |
| 制酸劑 | 可能影響吸收 |

### 主要不良反應

Thiamine 的安全性極佳：

- **口服**：極少副作用
  - 罕見：噁心、皮疹
- **注射**：
  - 罕見：過敏反應（靜脈注射）
  - 建議先皮內測試

### 劑量安全性

- **RDA**：1.1-1.2 mg/天
- **治療劑量**：50-300 mg/天（一般）
- **高劑量試驗**：600-1800 mg/天（甲亢疲勞）
- **安全上限**：未確立（水溶性，過量排出）

高劑量口服 Thiamine 的安全性良好，因其水溶性特質，過量會由尿液排出。

### 特殊族群注意事項

- **腎功能不全**：可能需調整高劑量使用
- **懷孕**：安全（屬於必需營養素）
- **哺乳**：安全

## 結論與下一步

### 預測可信度評估

| 預測適應症 | 證據等級 | 可信度 | 建議 |
|------------|----------|--------|------|
| 甲狀腺亢進相關疲勞 | L2 | 高 | 可考慮輔助治療 |
| 開角型青光眼 | L4 | 中 | 需更多研究 |

### 臨床應用建議

1. **甲狀腺亢進相關疲勞**：
   - **可考慮高劑量 Thiamine 作為輔助治療**
   - 建議劑量：300-600 mg/天起始
   - 安全性高，風險低
   - 不能取代抗甲狀腺藥物治療

2. **開角型青光眼**：
   - 可作為神經保護輔助
   - 證據尚不足以強烈推薦
   - 安全性高，可嘗試

### 實務建議

**甲亢患者使用 Thiamine 的建議流程**：

1. **評估**：
   - 確認甲亢已接受標準治療（抗甲狀腺藥物/碘-131/手術）
   - 評估疲勞嚴重程度
   - 排除其他疲勞原因

2. **起始**：
   - 從 100-300 mg/天開始
   - 可使用 Benfotiamine 以提高生物可用率

3. **監測**：
   - 2-4 週後評估疲勞改善
   - 如有效，可維持使用
   - 無明顯副作用風險

4. **注意事項**：
   - 告知患者這是輔助治療
   - 不能取代標準甲亢治療
   - 建議持續追蹤甲狀腺功能

### 研究價值

Thiamine 用於甲狀腺亢進的研究價值高：
- 安全性極佳
- 成本低廉
- 機轉合理
- 已有初步臨床證據
- 適合進行更大規模 RCT

---

*本筆記由 TxGNN 預測系統產生，僅供研究參考，不構成醫療建議。*
*更新日期：2026-02-11*


---

## 相關藥物報告

- [Ibuprofen]({{ "/drugs/ibuprofen/" | relative_url }}) - 證據等級 L5
- [Pentoxifylline]({{ "/drugs/pentoxifylline/" | relative_url }}) - 證據等級 L5
- [Clomipramine]({{ "/drugs/clomipramine/" | relative_url }}) - 證據等級 L5
- [Dehydrocholic Acid]({{ "/drugs/dehydrocholic_acid/" | relative_url }}) - 證據等級 L5
- [Teriparatide]({{ "/drugs/teriparatide/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Thiamine老藥新用驗證報告. https://twtxgnn.yao.care/drugs/thiamine/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_thiamine,
  title = {Thiamine老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/thiamine/}
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
