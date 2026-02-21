---
layout: default
title: Milrinone
description: "Milrinone 的老藥新用潛力分析。模型預測等級 L5，包含 10 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 106
evidence_level: L5
indication_count: 10
---

# Milrinone

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>10</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Milrinone 藥師筆記

## 一句話總結

<p class="key-answer" data-question="Milrinone 可以用於治療什麼新適應症？">
Milrinone 是一種磷酸二酯酶抑制劑，TxGNN 預測其對禿髮症及頭痛障礙有潛力，其中頭痛障礙（特別是可逆性腦血管收縮症候群相關頭痛）已有病例報告支持動脈內 Milrinone 的療效。
</p>


---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 藥物名稱 | Milrinone（米力心） |
| DrugBank ID | DB00235 |
| 台灣商品名 | 米力心注射劑0.2毫克/毫升 |
| 原核准適應症 | 充血性心衰竭的短期療法 |
| 預測新適應症 | alopecia、hypotrichosis simplex of the scalp、congenital hypotrichosis milia、diffuse alopecia areata、headache disorder、congestive heart failure、migraine disorder、migraine with brainstem aura、trigeminal autonomic cephalalgia、acute pulmonary heart disease |
| 最高預測分數 | 0.9991（禿髮症） |
| 證據等級 | L3（觀察性研究/病例報告 - 頭痛障礙） |

---


## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. alopecia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.91%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content" markdown="1">

### 為什麼這個預測合理？

### 藥理機轉分析

Milrinone 是選擇性磷酸二酯酶-3（PDE3）抑制劑，透過增加細胞內 cAMP 濃度發揮作用。其機轉與預測適應症的關聯：

1. **禿髮症/毛髮稀疏症**（TxGNN Score: 0.9991）
   - PDE 抑制劑（如 minoxidil）已知可促進毛髮生長
   - Milrinone 作為 PDE3 抑制劑理論上可能有類似作用
   - 但缺乏直接證據

2. **頭痛障礙**（TxGNN Score: 0.9946）
   - Milrinone 具有血管擴張作用
   - 已有病例報告顯示動脈內 Milrinone 可用於治療可逆性腦血管收縮症候群（RCVS）
   - 透過解除腦血管痙攣來緩解頭痛

3. **充血性心衰竭**（TxGNN Score: 0.9945）
   - 此為原核准適應症，有豐富臨床試驗證據

### 臨床試驗

| 疾病 | 臨床試驗數量 | 最高期別 | 證據等級 |
|------|-------------|---------|---------|
| 頭痛障礙 | 1 | N/A（觀察性） | L3 |
| 充血性心衰竭 | 30+ | Phase 4 | L1 |
| 禿髮症 | 0 | - | L5 |

### 重點臨床試驗（心衰竭相關）

| NCT ID | 標題 | 期別 | 狀態 | 國家 |
|--------|------|------|------|------|
| NCT02098629 | Milrinone 與 Esmolol 併用於急性心肌梗塞 | Phase 2 | 已完成 | 新加坡 |
| NCT07186062 | Levosimendan vs Dobutamine vs Milrinone 比較 | N/A | 已完成 | 埃及 |
| NCT04718350 | 靜脈 Levosimendan vs 吸入 Milrinone 比較 | N/A | 已完成 | 希臘 |

### 相關文獻

### 頭痛障礙（可逆性腦血管收縮症候群）

| PMID | 標題 | 年份 | 類型 | 證據等級 |
|------|------|------|------|---------|
| 34784343 | Reversible Cerebral Vasoconstriction Syndrome in Eclampsia Responding to Milrinone | 2021 | 病例報告 | L3 |
| 25440342 | Novel approach to diagnose reversible cerebral vasoconstriction syndrome | 2015 | 病例系列 | L3 |
| 18647181 | Intra-arterial milrinone for reversible cerebral vasoconstriction syndrome | 2009 | 病例報告 | L3 |

**關鍵發現**：
- 多篇病例報告顯示動脈內 Milrinone 可快速改善 RCVS 相關的腦血管痙攣和神經症狀
- 特別適用於鈣離子通道阻斷劑治療無效的病例
- 作為 PDE 抑制劑，可有效鬆弛血管平滑肌

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. hypotrichosis simplex of the scalp</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.90%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.90%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. congenital hypotrichosis milia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.89%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.89%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">4. diffuse alopecia areata</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.88%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.88%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. headache disorder</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.46%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.46%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. congestive heart failure</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.45%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.45%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">7. migraine disorder</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.45%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.45%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">8. migraine with brainstem aura</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.38%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.38%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">9. trigeminal autonomic cephalalgia</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.25%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.25%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">10. acute pulmonary heart disease</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.19%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.19%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>


## 台灣上市資訊

| 許可證字號 | 商品名 | 劑型 | 許可證持有者 | 狀態 |
|-----------|--------|------|-------------|------|
| （待確認） | 米力心注射劑0.2毫克/毫升 | 注射劑 | （待確認） | 有效 |

**適應症**：充血性心衰竭的短期療法。需在有適當心電圖監測設備的環境下使用。

---

## 安全性考量

### 使用注意事項

1. **心律不整風險**
   - 可能引起危及生命的室性心律不整
   - 需持續心電圖監測

2. **使用限制**
   - 目前無使用超過 48 小時的對照試驗經驗
   - 建議僅作為短期療法

3. **藥物交互作用**
   - 常與 digoxin 和利尿劑併用
   - 與其他強心藥物併用時需謹慎

### 給藥途徑考量

- **靜脈注射**：心衰竭標準給藥方式
- **動脈內注射**：RCVS 治療的研究給藥方式，需專業介入設備
- **吸入給藥**：肺高壓治療的研究給藥方式

---


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a></div>

**肝臟疾病 (Liver Diseases)** 🟡 Moderate
- The use of inamrinone (former amrinone) has been associated with hepatotoxicity, manifested as marked alterations in liver function tests and clinical symptoms suggestive of idiosyncratic hypersensitivity.  This especially after long-term use.  Thera...

**低血壓 (Hypotension)** 🟡 Moderate
- The use of amrinone or milrinone is associated with a fall in blood pressure.  Some patients have required correction by intravenous infusion of plasma.  Therapy with amrinone or milrinone should be administered cautiously in hypotensive patients.  M...

**Thrombocytopenia** 🟡 Moderate
- The use of amrinone, and infrequently, milrinone, can cause thrombocytopenia.  This appears to be dose-dependent and usually occurs during prolonged therapy.  Therapy with amrinone and milrinone should be administered cautiously in patients with thro...

**Arrhythmias, Cardiac** 🟢 Minor
- The use of milrinone both intravenously and orally has been associated with increased frequency of ventricular arrhythmias, including nonsustained ventricular tachycardia.  Long-term oral use has been associated with an increased risk of sudden death...

**Heart Valve Diseases** 🟢 Minor
- Milrinone should not be used in patients with severe obstructive aortic or pulmonic valvular disease in lieu of surgical relief of the obstruction.  Like other inotropic agents, it may aggravate outflow tract obstruction in hypertrophic subaortic ste...

*另有 1 項疾病注意事項，詳見 [DDInter 2.0](https://ddinter2.scbdd.com/)*

## 結論與下一步

### 評估結論

| 預測適應症 | 證據等級 | 臨床轉譯可行性 | 建議優先順序 |
|-----------|---------|---------------|-------------|
| 頭痛障礙（RCVS） | L3 | 中等 | 建議進一步研究 |
| 禿髮症 | L5 | 低 | 不建議優先開發 |
| 心衰竭 | L1 | 高（已核准） | 不適用 |

### 建議

1. **可逆性腦血管收縮症候群（RCVS）**
   - 目前已有多篇病例報告支持動脈內 Milrinone 的療效
   - 建議設計前瞻性研究評估安全性和有效性
   - 可考慮作為鈣離子通道阻斷劑無效時的救援治療

2. **禿髮症**
   - 雖然 PDE 抑制劑理論上可能有效
   - 但 Milrinone 為注射劑型，不適合局部外用治療禿髮
   - 不建議進一步開發

### 後續行動

- [x] 確認頭痛障礙文獻證據（已有 3 篇病例報告）
- [ ] 監測 RCVS 治療的新臨床試驗
- [ ] 評估是否有可能開發局部外用劑型用於禿髮（可行性低）

---

*報告產生日期：2026-02-11*
*資料來源：TxGNN 預測、ClinicalTrials.gov、PubMed、台灣 FDA*


---

## 相關藥物報告

- [Nitrofurantoin]({{ "/drugs/nitrofurantoin/" | relative_url }}) - 證據等級 L5
- [Trabectedin]({{ "/drugs/trabectedin/" | relative_url }}) - 證據等級 L5
- [Zanubrutinib]({{ "/drugs/zanubrutinib/" | relative_url }}) - 證據等級 L5
- [Remdesivir]({{ "/drugs/remdesivir/" | relative_url }}) - 證據等級 L5
- [Cladribine]({{ "/drugs/cladribine/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Milrinone老藥新用驗證報告. https://twtxgnn.yao.care/drugs/milrinone/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_milrinone,
  title = {Milrinone老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/milrinone/}
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
