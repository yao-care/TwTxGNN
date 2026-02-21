---
layout: default
title: Acebutolol
description: "Acebutolol 的老藥新用潛力分析。初步證據等級 L4，包含 2 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 中證據等級 (L3-L4)
nav_order: 11
evidence_level: L4
indication_count: 2
---

# Acebutolol

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L4</strong> | 預測適應症: <strong>2</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Acebutolol：從高血壓心律不整到惡性腎血管高血壓

## 一句話總結

<p class="key-answer" data-question="Acebutolol 可以用於治療什麼新適應症？">
Acebutolol 原本用於高血壓、狹心症及心律不整。
TxGNN 模型預測它可能對**惡性腎血管高血壓 (malignant renovascular hypertension)** 有效，
目前有 **1 篇文獻**支持這個方向。
</p>


## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓、狹心症、心律不整 |
| 預測新適應症 | malignant hypertensive renal disease、malignant renovascular hypertension |
| TxGNN 預測分數 | 99.10% |
| 證據等級 | L4 |
| 台灣上市 | 已上市 |
| 許可證數 | 27 張（部分已註銷） |
| 建議決策 | Hold |


## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. malignant hypertensive renal disease</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.10%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content" markdown="1">

### 為什麼這個預測合理？

Acebutolol 是一種選擇性 beta-1 交感神經阻斷劑，具有內在擬交感活性 (ISA)。其降壓機轉包括減少心輸出量、抑制腎素釋放，以及中樞性降壓作用。

在腎血管性高血壓的病理機轉中，腎素-血管張力素系統 (RAS) 過度活化扮演關鍵角色。Beta 阻斷劑能抑制腎素分泌，理論上可能對腎血管性高血壓有輔助療效。1975 年的法國研究 (PMID: 768911) 指出，acebutolol 在血漿腎素活性增高的腎血管性高血壓患者中展現良好療效。

然而，目前臨床上對於惡性腎血管高血壓的一線治療仍以血管介入或手術為主，藥物治療多以 ACE 抑制劑或 ARB 為首選。

### 臨床試驗

目前無針對 acebutolol 與惡性腎血管高血壓的註冊臨床試驗。

### 相關文獻

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [768911](https://pubmed.ncbi.nlm.nih.gov/768911/) | 1975 | Clinical Trial | La Nouvelle presse medicale | 50 例高血壓患者使用 acebutolol，74% 效果良好；研究指出腎血管性高血壓伴隨高腎素活性者為良好適應症 |

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. malignant renovascular hypertension</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.10%</span>
</summary>
<div class="indication-content" markdown="1">

### TxGNN 預測資訊

- **預測分數**：99.10%
- **證據等級**：L5（僅模型預測）

### 臨床證據

<div class="no-evidence-warning">
目前尚無針對此適應症的直接臨床試驗或文獻證據。此為 AI 模型預測結果，需進一步研究驗證。
</div>

</div>
</details>


## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛部藥輸字第026664號 | 鹽酸阿西布特洛 | 粉劑 | Beta 交感神經遮斷劑 |
| 衛署藥製字第041669號 | "生達" 舒爾心膜衣錠 400mg | 膜衣錠 | 高血壓、狹心症、心律不整 |
| 衛署藥製字第047472號 | 順律膜衣錠 400mg | 膜衣錠 | 心律不整、狹心症、高血壓 |

## 安全性考量

### 重要藥物交互作用

**Major 交互作用：**
- Dolasetron：可能增加 QT 延長風險

**Moderate 交互作用：**
- 降血糖藥物（Glimepiride、Glipizide、Glyburide、各類胰島素）：可能掩蓋低血糖症狀
- 類固醇（Betamethasone、Dexamethasone、Hydrocortisone、Prednisolone、Prednisone）：可能減弱降壓效果
- 鈣離子補充劑：可能影響心臟傳導
- 腎上腺素（Epinephrine）：可能產生嚴重高血壓反應
- Bupropion：可能增加降壓效果
- Cimetidine：可能增加 acebutolol 血中濃度

**Minor 交互作用：**
- 制酸劑（Aluminum hydroxide、Magnesium hydroxide）：可能減少吸收
- Aspirin：輕微影響降壓效果

### 禁忌症
- 竇性心搏過緩
- 二度或三度房室傳導阻滯
- 明顯心衰竭
- 心因性休克

安全性資訊請參考原廠仿單。

### 藥物-食物交互作用 (DFI)

<div class="dfi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a></div>

**酒精 (alcohol)** 🟡 Moderate
- 影響：Many psychotherapeutic and CNS-active agents (e.g., anxiolytics, sedatives, hypnotics, antidepressants, antipsychotics, opioids, alcohol, muscle relaxants) exhibit hypotensive effects, especially duri...
- 建議：Caution and close monitoring for development of hypotension is advised during coadministration of these agents.  Some authorities recommend avoiding alcohol in patients receiving vasodilating antihype...



### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a></div>

**Hepatic Insufficiency** 🟡 Moderate
- Acebutolol should be used cautiously in patients with impaired hepatic function.

**Cerebrovascular Disorders** 🟡 Moderate
- Beta-adrenergic blocking agents (beta-blockers), should be used with caution in patients with cerebrovascular insufficiency because of their potential effects relative to blood pressure and pulse.  If signs or symptoms suggesting reduced cerebral blo...

**青光眼 (Glaucoma)** 🟡 Moderate
- Systemic beta-adrenergic receptor blocking agents (aka beta-blockers) may lower intraocular pressure.  Therefore, patients with glaucoma or intraocular hypertension may require adjustments in their ophthalmic regimen following a dosing change or disc...

**Hyperlipidemias** 🟡 Moderate
- Beta-adrenergic receptor blocking agents (aka beta-blockers) may alter serum lipid profiles.  Increases in serum VLDL and LDL cholesterol and triglycerides, as well as decreases in HDL cholesterol, have been reported with some beta-blockers.  Patient...

**甲狀腺機能亢進 (Hyperthyroidism)** 🟡 Moderate
- When beta-adrenergic receptor blocking agents (aka beta-blockers) are used to alleviate symptoms of hyperthyroidism such as tachycardia, anxiety, tremor and heat intolerance, abrupt withdrawal can exacerbate thyrotoxicosis or precipitate a thyroid st...

*另有 14 項疾病注意事項，詳見 [DDInter 2.0](https://ddinter2.scbdd.com/)*

## 結論與下一步

**決策：Hold**

**理由：**
雖然 acebutolol 的藥理機轉（抑制腎素釋放）理論上可能對腎血管性高血壓有益，但目前僅有 1 篇 1975 年的文獻支持，且現行臨床指引對於惡性腎血管高血壓優先推薦介入治療及 RAS 阻斷劑。

**若要推進需要：**
- 設計前瞻性臨床試驗，比較 acebutolol 與標準治療在腎血管性高血壓的療效
- 進行更多機轉研究，探討 beta 阻斷劑在高腎素狀態下的角色
- 與血管介入或手術治療的併用策略研究


---

## 相關藥物報告

- [Cisatracurium]({{ "/drugs/cisatracurium/" | relative_url }}) - 證據等級 L4
- [Salicylamide]({{ "/drugs/salicylamide/" | relative_url }}) - 證據等級 L4
- [Dl-Alpha-Tocopherol]({{ "/drugs/dl-alpha-tocopherol/" | relative_url }}) - 證據等級 L4
- [Brodalumab]({{ "/drugs/brodalumab/" | relative_url }}) - 證據等級 L4
- [Hydroquinone]({{ "/drugs/hydroquinone/" | relative_url }}) - 證據等級 L4

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Acebutolol老藥新用驗證報告. https://twtxgnn.yao.care/drugs/acebutolol/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_acebutolol,
  title = {Acebutolol老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/acebutolol/}
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
