---
layout: default
title: Disopyramide
description: "Disopyramide 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L4
indication_count: 10
---

# Disopyramide

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Disopyramide (待索匹拉邁) - 藥師評估報告

## 一句話總結

<p class="key-answer" data-question="Disopyramide 可以用於治療什麼新適應症？">
Disopyramide 是一種 Class Ia 抗心律不整藥物，TxGNN 預測其可能對妥瑞症、ADHD 和拔毛症等神經精神疾病有療效，但這些預測缺乏機轉支持和臨床證據，可能是知識圖譜中的假陽性關聯。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Disopyramide (待索匹拉邁/二索匹拉麥) |
| DrugBank ID | DB00280 |
| 台灣商品名 | 福元心達寧膠囊 100mg |
| 原適應症 | 心室性不整律、心律不整 |
| 預測新適應症 | Tourette syndrome、attention deficit-hyperactivity disorder、trichotillomania、attention deficit hyperactivity disorder, inattentive type、faciodigitogenital syndrome、specific developmental disorder、idiopathic neonatal atrial flutter、chondromyxoid fibroma、multifocal atrial tachycardia (disease)、trigeminal nerve neoplasm |
| 最高 TxGNN 分數 | 0.9986 (妥瑞症) |
| 臨床試驗支持 | 無 |
| 文獻支持 | 極弱（僅心律不整相關） |


## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. Tourette syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.86%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content" markdown="1">

### 為什麼這個預測合理？

### 機轉分析

1. **妥瑞症 (Tourette syndrome)** - TxGNN 分數 0.9986：
   - Disopyramide 具有抗膽鹼作用
   - 妥瑞症涉及多巴胺系統異常
   - 但 disopyramide 主要作用於心臟鈉離子通道，對中樞神經系統的直接影響有限
   - **機轉連結薄弱**

2. **注意力不足過動症 (ADHD)** - TxGNN 分數 0.9982：
   - ADHD 主要與多巴胺和正腎上腺素通路相關
   - Disopyramide 無已知的中樞神經系統活性
   - **機轉連結極為薄弱**

3. **拔毛症 (trichotillomania)** - TxGNN 分數 0.9981：
   - 這是一種強迫相關障礙
   - 與 disopyramide 的藥理作用無關
   - **機轉連結極為薄弱**

4. **新生兒心房撲動 / 多灶性心房頻脈**：
   - 這些預測與原適應症（心律不整）直接相關
   - Disopyramide 作為 Class Ia 抗心律不整藥確實可能用於某些心房心律不整
   - **但已在原適應症範圍內**

### 預測品質評估

- 神經精神疾病預測（妥瑞症、ADHD、拔毛症）可能是知識圖譜中的假陽性關聯
- 這些預測可能源於藥物的抗膽鹼作用與某些神經疾病的間接關聯
- 心律不整相關預測與原適應症重疊

### 相關文獻

### 多灶性心房頻脈相關文獻

1. **Somani P et al. (1980)** - Chest
   - 報告一例難治性心室和心房心律不整患者
   - 患者對多種藥物（包括 disopyramide）無效
   - 最終使用 lorcainide 成功治療
   - 相關性：僅提及 disopyramide 為失敗治療選項之一

### 神經精神疾病相關文獻

**無相關文獻**

未發現任何將 disopyramide 用於妥瑞症、ADHD 或拔毛症治療的文獻。

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. attention deficit-hyperactivity disorder</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.82%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.82%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. trichotillomania</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.81%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.81%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. attention deficit hyperactivity disorder, inattentive type</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.74%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.74%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. faciodigitogenital syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.66%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.66%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. specific developmental disorder</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.54%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.54%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. idiopathic neonatal atrial flutter</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.42%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.42%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. chondromyxoid fibroma</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.41%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.41%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. multifocal atrial tachycardia (disease)</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.21%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.21%
- **證據等級**：L4（有文獻支持）

### 臨床證據

**相關文獻**：共 1 篇


</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. trigeminal nerve neoplasm</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.16%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.16%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>


## 台灣上市狀態

| 許可證號 | 商品名 | 劑型 | 適應症 | 狀態 |
|----------|--------|------|--------|------|
| 衛署藥製字第025427號 | 福元心達寧膠囊 100mg | 膠囊 | 心室性不整律 | 有效 (至2028) |

**現況**：台灣僅剩一項有效許可證，其他製劑均已註銷。市場供應有限。

## 安全性

### 重要藥物交互作用

| 併用藥物 | 嚴重程度 | 臨床意義 |
|----------|----------|----------|
| Clarithromycin | **Major** | QT 延長風險 |
| Cisapride | **Major** | QT 延長風險 |
| Granisetron | **Major** | QT 延長風險 |
| Dolasetron | **Major** | QT 延長風險 |
| Potassium citrate | **Major** | 低血鉀增加心律不整風險 |
| Eliglustat | **Major** | QT 延長風險 |
| 多種降血糖藥 | Moderate | 可能增強降血糖效果 |
| 抗膽鹼藥物 | Moderate | 抗膽鹼作用加成 |
| 類固醇 | Moderate | 電解質異常風險 |

### 重要警語

- **QT 延長**：可能引起尖端扭轉型室速 (Torsades de pointes)
- **負性肌力作用**：心衰竭患者禁用或謹慎使用
- **抗膽鹼作用**：尿滯留、口乾、便秘、視力模糊
- **低血糖**：可能增強胰島素和口服降血糖藥的作用
- **心臟傳導阻滯**：需監測心電圖

## 結論

### 整體評估：不推薦

Disopyramide 的 TxGNN 預測新適應症主要為神經精神疾病（妥瑞症、ADHD、拔毛症），這些預測極有可能是知識圖譜中的假陽性關聯，完全缺乏機轉支持和臨床證據。考慮到 disopyramide 的心臟毒性風險，將其用於神經精神疾病治療是不合理的。

### 建議

1. **強烈不建議**研究 disopyramide 用於神經精神疾病
2. 心律不整相關預測已在原適應症範圍內
3. 此藥物因安全性顧慮，使用已大幅減少，不適合老藥新用研究
4. TxGNN 對此藥物的預測可能反映了知識圖譜的限制

### 證據等級總結

| 預測適應症 | TxGNN 分數 | 臨床試驗 | 文獻支持 | 機轉合理性 | 綜合評估 |
|------------|------------|----------|----------|------------|----------|
| 妥瑞症 | 0.9986 | 無 | 無 | 極低 | **不推薦** |
| ADHD | 0.9982 | 無 | 無 | 極低 | **不推薦** |
| 拔毛症 | 0.9981 | 無 | 無 | 極低 | **不推薦** |
| 新生兒心房撲動 | 0.9942 | 無 | 無 | 中等 | 已為適應症範疇 |
| 多灶性心房頻脈 | 0.9920 | 無 | 極弱 | 中等 | 已為適應症範疇 |

### 安全性警示

即使未來有任何研究興趣，disopyramide 的嚴重心臟毒性（QT 延長、負性肌力作用）使其成為高風險藥物，不適合用於非致命性神經精神疾病的治療。

---
*報告產生日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、台灣 FDA*


---

## 相關藥物報告

- [Gefitinib]({{ "/drugs/gefitinib/" | relative_url }}) - 證據等級 L5
- [Berberine]({{ "/drugs/berberine/" | relative_url }}) - 證據等級 L5
- [Diosmin]({{ "/drugs/diosmin/" | relative_url }}) - 證據等級 L5
- [Paclitaxel]({{ "/drugs/paclitaxel/" | relative_url }}) - 證據等級 L5
- [Pipemidic Acid]({{ "/drugs/pipemidic_acid/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Disopyramide老藥新用驗證報告. https://twtxgnn.yao.care/drugs/disopyramide/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_disopyramide,
  title = {Disopyramide老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/disopyramide/}
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
