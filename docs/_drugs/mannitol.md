---
layout: default
title: Mannitol
description: "Mannitol 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L1
indication_count: 10
---

# Mannitol

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Mannitol (甘露醇) - 藥師筆記

## 一句話總結

<p class="key-answer" data-question="Mannitol 可以用於治療什麼新適應症？">
Mannitol 為滲透性利尿劑，TxGNN 預測其可用於多種罕見疾病如惡性高熱、週期性麻痺及腎源性尿崩症等，部分預測有文獻支持 (低血鉀週期性麻痺 L3)，其他為純預測階段 (L5)。
</p>

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Mannitol (甘露醇、木密醇) |
| DrugBank ID | DB00742 |
| 台灣商品名 | 信東美立妥、滿乃通、濟生邁尼妥等 |
| 原核准適應症 | 利尿、降顱內壓、腦水腫、促進毒物排除、腎小球過濾速率測定 |
| 預測新適應症 | nephrogenic syndrome of inappropriate antidiuresis、congestive heart failure、acute pulmonary heart disease、exercise-induced malignant hyperthermia、malignant hyperthermia, susceptibility to、familial periodic paralysis、hypokalemic periodic paralysis、congenital multicore myopathy with external ophthalmoplegia、moderate multiminicore disease with hand involvement、pseudotumor cerebri |
| TxGNN 預測分數 | 0.997-0.999 |
| 證據等級 | **L3** (低血鉀週期性麻痺)、**L5** (其他 - 僅預測或文獻薄弱) |
| 臨床試驗 | 無直接相關 |
| PubMed 文獻 | 部分有 |

---


## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. nephrogenic syndrome of inappropriate antidiuresis</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.97%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content" markdown="1">

### 為什麼這個預測合理？

### 機轉推論

1. **滲透性利尿作用**：Mannitol 為滲透性利尿劑，可增加血漿滲透壓，促進水分從組織轉移至血管內，並增加腎臟水分排泄。

2. **各預測適應症分析**：

| 預測適應症 | 機轉關聯性 | 說明 |
|-----------|-----------|------|
| 腎源性抗利尿不當症候群 (NSIAD) | 低 | 此為遺傳性 V2 受體突變，Mannitol 理論上可對抗水分滯留，但非根本治療 |
| 急性肺心病 | 中 | 有文獻支持 Mannitol 可降低肺血管阻力，但非標準治療 |
| 惡性高熱 | 低-中 | 文獻提及 Mannitol 作為輔助治療使用，但 Dantrolene 為首選 |
| 家族性週期性麻痺 | 中 | 作為靜脈輸注溶劑，避免葡萄糖誘發發作 |
| 低血鉀週期性麻痺 | 中-高 | **有文獻直接支持**作為 KCl 靜脈給藥的溶劑 |
| 腎源性尿崩症 | 低 | 機轉不合理，可能加重脫水 |
| King-Denborough 症候群 | 低 | 與惡性高熱相關的罕見疾病 |

### 臨床試驗

### 與預測適應症相關的臨床試驗

**無直接針對預測適應症的臨床試驗**

但資料庫中存在多項 Mannitol 相關試驗，主要集中於：
- 顱內壓控制 (原適應症)
- 腸道通透性測試 (診斷用途)
- COVID-19 相關研究 (ACTT-2, ACTT-3, ACTT-4 試驗中作為對照組溶劑)

### 相關文獻

### 低血鉀週期性麻痺 (HypoPP) - 證據等級 L3

| PMID | 標題 | 年份 | 重點發現 |
|------|------|------|---------|
| **6412669** | 低血鉀週期性麻痺的靜脈治療 | 1983 | **關鍵文獻**：研究確認使用 5% 葡萄糖稀釋 KCl 反而使症狀惡化並降低血鉀；改用 **5% Mannitol 作為溶劑**則可使血鉀上升並改善肌力 |
| 18426576 | 低血鉀週期性麻痺的實務管理 | 2008 | 回顧提及若需靜脈給藥，可使用 **mannitol 溶劑**代替葡萄糖 |
| 32585385 | 術後首發低血鉀週期性麻痺 | 2020 | 病例報告 |

**關鍵發現**：低血鉀週期性麻痺患者靜脈補充 KCl 時，**禁用葡萄糖溶液**（會誘發發作），應使用 **Mannitol 溶液**稀釋。

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. acute pulmonary heart disease</span>
<span class="evidence-badge evidence-L1">L1</span>
<span class="prediction-score">99.88%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.88%
- **證據等級**：L1（多個大型 RCT 支持）

### 臨床證據

**臨床試驗**：共 7 項

- 試驗階段分布：N/A: 2項, NA: 1項, PHASE2: 1項, PHASE3: 3項

**相關文獻**：共 6 篇


</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. exercise-induced malignant hyperthermia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.86%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.86%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. malignant hyperthermia, susceptibility to</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.80%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.80%
- **證據等級**：L4（有文獻支持）

### 臨床證據

**相關文獻**：共 3 篇


</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. familial periodic paralysis</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.75%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.75%
- **證據等級**：L4（有文獻支持）

### 臨床證據

**相關文獻**：共 2 篇


</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. hypokalemic periodic paralysis</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.72%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.72%
- **證據等級**：L4（有文獻支持）

### 臨床證據

**相關文獻**：共 3 篇


</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. congenital multicore myopathy with external ophthalmoplegia</span>
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
<span class="indication-name">8. moderate multiminicore disease with hand involvement</span>
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

<details class="indication-section">
<summary>
<span class="indication-name">9. nephrogenic diabetes insipidus</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.70%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.70%
- **證據等級**：L4（有文獻支持）

### 臨床證據

**相關文獻**：共 2 篇


</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. King-Denborough syndrome</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.69%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.69%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>


## 台灣上市資訊

### 許可證狀態 (精選有效許可證)

| 許可證字號 | 商品名 | 濃度 | 持證商 | 效期 |
|-----------|--------|------|--------|------|
| 內衛藥製字第012343號 | 信東 美立妥注射劑 | 20% | 信東生技 | 2028/05/25 |
| 衛署藥製字第009633號 | 滿乃通注射液 | 20% | 杏林新生製藥 | 2028/05/10 |
| 衛署藥製字第013354號 | 濟生邁尼妥注射液 | 20% | 濟生醫藥生技 | 2028/05/25 |
| 衛署藥製字第043768號 | 滿乃通注射液 | 15% | 杏林新生製藥 | 2030/05/26 |

### 核准適應症

1. **利尿**
2. **降顱內壓**
3. **腦水腫**
4. **促進毒物之尿中排除**
5. **腎小球過濾速率之測定（診斷用）**
6. **降低眼壓**
7. **防止溶血**

---

## 安全性考量

### 藥物交互作用 (DDI)

#### 嚴重 (Major) 交互作用

| 併用藥物 | 影響說明 |
|---------|---------|
| Amikacin | 增強耳毒性與腎毒性風險 |
| 其他氨基糖苷類抗生素 | 增強耳毒性與腎毒性風險 |

#### 中度 (Moderate) 交互作用

| 併用藥物類別 | 代表藥物 | 影響 |
|-------------|---------|------|
| 抗凝血劑 | Lamivudine | 可能影響藥物排泄 |
| beta-2 促效劑 | Salbutamol, Formoterol | 低血鉀風險 |
| ACE 抑制劑 | Captopril, Benazepril | 電解質異常風險 |
| 瀉劑 | Bisacodyl | 電解質流失加劇 |
| 抗癲癇藥 | Carbamazepine | 低血鈉風險增加 |
| SSRI | Citalopram | 低血鈉風險增加 |
| 顯影劑 | Diatrizoate, Iothalamic acid | 腎毒性風險 |
| 神經肌肉阻斷劑 | Cisatracurium | 電解質影響神經肌肉功能 |
| SGLT2 抑制劑 | Canagliflozin | 電解質異常與滲透性利尿加成 |

### 重要警語

1. **體液與電解質失衡**：
   - 可導致嚴重脫水與電解質紊亂
   - 需監測血清電解質、滲透壓、腎功能

2. **循環超負荷**：
   - 給藥初期因血漿滲透壓增加，可能導致血容量擴張
   - 心臟衰竭患者需謹慎

3. **腎功能**：
   - 可能導致急性腎損傷
   - 腎功能不全者需調整劑量或避免使用

4. **顱內出血風險**：
   - 腦外傷患者若血腦屏障破損，可能加重腦水腫

### 禁忌症

- 無尿
- 嚴重脫水
- 進行性心衰竭
- 活動性顱內出血（除手術中使用外）
- 嚴重肺水腫或充血

### 特殊族群

- **孕婦**：Category C，權衡利弊使用
- **哺乳婦女**：資料不足，謹慎使用
- **腎功能不全**：可能需避免使用或減量
- **老年人**：需密切監測體液狀態

---


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**Dehydration** 🟡 Moderate
- 可能有嚴重不良反應。

**Dehydration** 🟢 Minor
- 本藥物在此情況下禁用。可能有嚴重不良反應。

## 結論與下一步

### 藥師評估

| 預測適應症 | 預測可信度 | 機轉合理性 | 證據等級 | 建議優先度 |
|-----------|-----------|-----------|---------|-----------|
| 低血鉀週期性麻痺 | 高 | 高 | **L3** | 建議追蹤 |
| 惡性高熱 | 低 | 低 (僅輔助) | L5 | 不建議 |
| 腎源性抗利尿不當症候群 | 中 | 中 | L5 | 可考慮研究 |
| 急性肺心病 | 低 | 中 | L5 | 不建議 |
| 腎源性尿崩症 | 低 | 低 | L5 | 不建議 |
| 週期性麻痺家族性 | 高 | 高 | L3 | 建議追蹤 |

### 建議

1. **低血鉀週期性麻痺** (建議追蹤)：
   - **臨床應用價值明確**：作為靜脈補充 KCl 的溶劑
   - **重要提醒**：禁用葡萄糖溶液稀釋 KCl
   - 可納入醫院處方建議或臨床指引

2. **惡性高熱** (不建議優先探索)：
   - Mannitol 僅為輔助支持治療
   - **Dantrolene 為首選治療**
   - 無需針對此適應症進行老藥新用

3. **其他預測適應症** (不建議)：
   - 腎源性尿崩症：機轉不合理，可能有害
   - 急性肺心病：證據過於老舊且不足

4. **藥師臨床提醒**：
   - 低血鉀週期性麻痺患者若需靜脈補鉀，建議使用 **Mannitol 或生理食鹽水**稀釋，**避免葡萄糖溶液**

### 證據等級說明

- **L3 (低血鉀週期性麻痺)**：有多篇文獻直接支持使用 Mannitol 作為 KCl 靜脈給藥的溶劑
- **L5 (其他適應症)**：僅有間接文獻提及或純粹預測，缺乏直接臨床證據

---

*本筆記由 TxGNN 老藥新用預測系統生成，僅供研究參考，不構成醫療建議。*

*生成日期：2026-02-11*

---

## 相關藥物報告

- [Pitavastatin]({{ "/drugs/pitavastatin/" | relative_url }}) - 證據等級 L5
- [Buprenorphine]({{ "/drugs/buprenorphine/" | relative_url }}) - 證據等級 L5
- [Inclisiran]({{ "/drugs/inclisiran/" | relative_url }}) - 證據等級 L5
- [Warfarin]({{ "/drugs/warfarin/" | relative_url }}) - 證據等級 L5
- [Levamisole]({{ "/drugs/levamisole/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Mannitol老藥新用驗證報告. https://twtxgnn.yao.care/drugs/mannitol/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_mannitol,
  title = {Mannitol老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/mannitol/}
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
