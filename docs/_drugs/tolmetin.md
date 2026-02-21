---
layout: default
title: Tolmetin
description: "Tolmetin 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
---

# Tolmetin

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Tolmetin (妥美汀) - 藥師評估報告

## 一句話總結

<p class="key-answer" data-question="Tolmetin 可以用於治療什麼新適應症？">
Tolmetin 是一種非類固醇抗發炎藥 (NSAID)，TxGNN 預測多項罕見骨骼發育疾病，但均缺乏臨床試驗與文獻支持，不建議用於這些預測適應症。
</p>


---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Tolmetin (妥美汀) |
| DrugBank ID | DB00500 |
| 原適應症 | 類風濕性關節炎、骨關節炎、僵直性脊椎炎、急性痛風 |
| 預測新適應症 | osteoarthritis susceptibility、osteoarthritis、acromesomelic dysplasia, Hunter-Thompson type、brachyolmia-amelogenesis imperfecta syndrome、myosclerosis、brachyolmia、arthropathy、pseudoachondroplasia、rheumatoid arthritis、rheumatoid nodulosis |
| 最高 TxGNN 分數 | 0.9998 (Hunter-Thompson 型肢端中段發育不全，排名 887) |
| 證據等級 | 所有預測適應症均無臨床試驗與文獻支持 |
| 台灣上市狀態 | 有效許可證（利達、恆信、應元等廠） |

---


## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. acromesomelic dysplasia, Hunter-Thompson type</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.98%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content" markdown="1">

### 為什麼這個預測合理？

### 機轉分析

Tolmetin 是非選擇性 COX 抑制劑，具有抗發炎、鎮痛、解熱作用。TxGNN 預測的適應症多為罕見骨骼發育異常疾病：

| 預測適應症 | TxGNN 分數 | 疾病特性 |
|-----------|-----------|---------|
| Hunter-Thompson 型肢端中段發育不全 | 0.9998 | GDF5 基因突變，軟骨發育異常 |
| 短軀幹發育不良-牙釉質發育不全症候群 | 0.9998 | LTBP3 基因突變 |
| 肌硬化症 | 0.9998 | 肌肉進行性纖維化 |
| 假性軟骨發育不全 | 0.9995 | COMP 基因突變 |

### 預測限制

1. **機轉不符**：NSAID 無法修正基因突變導致的發育異常
2. **疾病本質**：這些疾病是結構性/發育性問題，非發炎性疾病
3. **可能原因**：這些疾病常伴有關節疼痛，可能造成知識圖譜關聯

### 合理的症狀緩解應用

部分預測可能反映的是：
- 骨骼發育異常患者常有關節疼痛
- NSAID 可用於這些患者的症狀緩解
- 但這不等於「治療」該疾病本身

### 相關文獻

**所有預測適應症均無相關 PubMed 文獻**

未發現任何探討 Tolmetin 用於這些罕見骨骼發育疾病的學術文獻。

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. brachyolmia-amelogenesis imperfecta syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.98%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.98%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. myosclerosis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.98%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.98%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. brachyolmia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.97%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.97%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. pseudoachondroplasia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.95%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.95%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. rheumatoid nodulosis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.76%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.76%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. rheumatoid factor-positive polyarticular juvenile idiopathic arthritis</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.75%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.75%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. spondyloarthropathy, susceptibility to</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.75%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.75%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. colobomatous microphthalmia-rhizomelic dysplasia syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.72%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.72%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. WHIM syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.71%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.71%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>


## 台灣上市情形

Tolmetin 在台灣有有效許可證，但多數已註銷：

### 有效許可證

| 許可證字號 | 品名 | 劑量 | 許可證持有者 | 效期 |
|-----------|------|------|-------------|------|
| 衛署藥製字第025549號 | 痛必定錠 | 200mg | 利達製藥 | 2028/05/25 |
| 衛署藥製字第022712號 | 妥美定錠 | - | 恆信藥品 | 2029/12/30 |
| 衛署藥製字第055941號 | 遠痛錠 | 200mg | 應元化學製藥 | 2031/02/21 |

### 已註銷許可證

多數進口製劑（嬌生妥力定系列）已於 2000 年代初期陸續註銷。

---

## 安全性考量

### 藥物交互作用

| 嚴重度 | 交互作用藥物 | 臨床意義 |
|--------|-------------|---------|
| Moderate | Acetylsalicylic acid | 增加胃腸道出血風險 |
| Moderate | 類固醇類 | 增加胃腸道副作用 |
| Moderate | Metformin | 可能影響腎功能 |
| Moderate | Vancomycin | 增加腎毒性風險 |
| Moderate | Warfarin | 增強抗凝血作用 |
| Minor | H2 受體拮抗劑 | 可能降低 Tolmetin 吸收 |

### NSAID 類別警告

1. **心血管風險**：
   - 增加心肌梗塞、中風風險
   - 長期使用風險更高

2. **胃腸道風險**：
   - 潰瘍、出血、穿孔
   - 老年人風險較高

3. **腎臟風險**：
   - 可能導致急性腎損傷
   - 慢性使用可能影響腎功能

### 使用注意事項

1. 有心血管疾病史者慎用
2. 有消化道潰瘍史者慎用
3. 腎功能不全者需調整劑量
4. 避免與其他 NSAID 併用

---

## 結論

### 預測適應症評估

| 適應症 | TxGNN 分數 | 臨床試驗 | 文獻 | 建議 |
|-------|-----------|---------|------|------|
| Hunter-Thompson 型肢端中段發育不全 | 0.9998 | 無 | 無 | **不建議** |
| 短軀幹發育不良-牙釉質發育不全 | 0.9998 | 無 | 無 | **不建議** |
| 肌硬化症 | 0.9998 | 無 | 無 | **不建議** |
| 假性軟骨發育不全 | 0.9995 | 無 | 無 | **不建議** |
| 類風濕結節症 | 0.9976 | 無 | 無 | 可考慮（症狀緩解） |
| RF 陽性多關節型幼年特發性關節炎 | 0.9975 | 無 | 無 | 可考慮（同類藥物有證據） |

### 臨床建議

1. **不建議用於預測的罕見骨骼發育疾病**：
   - 這些疾病無法被 NSAID「治療」
   - 缺乏任何臨床證據支持

2. **維持現有適應症使用**：
   - 類風濕性關節炎
   - 骨關節炎
   - 僵直性脊椎炎
   - 急性痛風

3. **症狀緩解考量**：
   - 骨骼發育異常患者若有關節疼痛，可考慮使用 NSAID 類藥物緩解症狀
   - 但這屬於一般止痛用途，非針對疾病本身

4. **TxGNN 預測解讀**：
   - 高分數可能反映疾病與藥物在知識圖譜中的關聯（如共同的疼痛症狀）
   - 不等於治療效果的預測
   - 罕見疾病的預測需更謹慎解讀

---

*報告產生日期：2026-02-11*
*資料來源：TxGNN 知識圖譜預測、ClinicalTrials.gov、PubMed、台灣 FDA*


---

## 相關藥物報告

- [Pitolisant]({{ "/drugs/pitolisant/" | relative_url }}) - 證據等級 L5
- [Salicylic Acid]({{ "/drugs/salicylic_acid/" | relative_url }}) - 證據等級 L5
- [Tyrosine]({{ "/drugs/tyrosine/" | relative_url }}) - 證據等級 L5
- [Caspofungin]({{ "/drugs/caspofungin/" | relative_url }}) - 證據等級 L5
- [Benzylpenicillin]({{ "/drugs/benzylpenicillin/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Tolmetin老藥新用驗證報告. https://twtxgnn.yao.care/drugs/tolmetin/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_tolmetin,
  title = {Tolmetin老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/tolmetin/}
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
