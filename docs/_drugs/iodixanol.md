---
layout: default
title: Iodixanol
description: "Iodixanol 的老藥新用潛力分析。模型預測等級 L5，包含 3 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L4
indication_count: 3
---

# Iodixanol

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>3</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Iodixanol：從 X光對比劑 到 骨關節炎

## 一句話總結

<p class="key-answer" data-question="Iodixanol 可以用於治療什麼新適應症？">
Iodixanol（易渠派克）是一種等滲透壓的碘化X光對比劑，用於心血管、腦血管及泌尿道造影。TxGNN 模型預測它可能對**骨關節炎 (osteoarthritis)** 有潛在關聯，目前有 **7 篇文獻**探討相關機制，但無臨床試驗支持。
</p>

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | X光對比劑：心臟血管、腦血管、周邊動脈造影等 |
| 預測新適應症 | osteoarthritis susceptibility、osteoarthritis、rheumatoid arthritis |
| TxGNN 預測分數 | 99.07% |
| 證據等級 | L5 |
| 台灣上市 | 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |





## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. osteoarthritis susceptibility</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.16%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>Iodixanol 是一種非離子型等滲透壓的碘化對比劑，主要用於影像學檢查。目前缺乏直接的藥理機轉資料說明其對骨關節炎的治療潛力。</p>

<p>然而，從文獻證據來看，Iodixanol 作為顯影劑被用於關節軟骨的 CT 造影研究。多篇研究使用對比增強電腦斷層（CECT）技術結合 iodixanol 來評估軟骨結構和成分變化，這些變化與早期骨關節炎相關。這種應用主要是診斷性質，而非治療性質。</p>

<p>TxGNN 的預測可能反映了藥物與疾病在知識圖譜中的共現關係（如文獻中同時提及），而非直接的治療效果。</p>

<h3>臨床試驗</h3>

<p>目前無針對此特定適應症的臨床試驗登記。</p>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. osteoarthritis</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.07%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（7 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/40155520/" target="_blank">40155520</a></td><td>2025</td><td>Article</td><td>Annals of biomedical engineeri</td><td>Dual-Contrast Agent with Nanoparticle and Molecular Components in Photon-Countin...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28063646/" target="_blank">28063646</a></td><td>2017</td><td>Article</td><td>Journal of biomechanics</td><td>Solute transport at the interface of cartilage and subchondral bone plate: Effec...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30145230/" target="_blank">30145230</a></td><td>2018</td><td>Article</td><td>Osteoarthritis and cartilage</td><td>Aging does not change the compressive stiffness of mandibular condylar cartilage...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39012563/" target="_blank">39012563</a></td><td>2024</td><td>Article</td><td>Annals of biomedical engineeri</td><td>Revealing Detailed Cartilage Function Through Nanoparticle Diffusion Imaging: A ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/27793406/" target="_blank">27793406</a></td><td>2016</td><td>Article</td><td>Journal of biomechanics</td><td>Neutral solute transport across osteochondral interface: A finite element approa...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/30374787/" target="_blank">30374787</a></td><td>2018</td><td>Article</td><td>Journal of experimental orthop</td><td>Iodine contrast agents do not influence Platelet-Rich Plasma function at an earl...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/28518064/" target="_blank">28518064</a></td><td>2017</td><td>Article</td><td>Journal of visualized experime</td><td>An Experimental and Finite Element Protocol to Investigate the Transport of Neut...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. rheumatoid arthritis</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.00%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（1 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36628042/" target="_blank">36628042</a></td><td>2022</td><td>Article</td><td>Cureus</td><td>Successful Desensitization to the Radiocontrast Material Iohexol (Omnipaque™).</td></tr>
</tbody>
</table>

</div>
</details>


## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 衛署藥輸字第023365號 | 易渠派克 注射劑 270公絲碘/公撮 | 注射劑 | X光對比劑：用於心臟血管、腦血管、周邊動脈造影... |
| 衛署藥輸字第023367號 | 易渠派克 注射劑 320毫克碘/毫升 | 注射劑 | X光對比劑：用於心臟血管、腦血管、周邊動脈造影... |

## 安全性考量

**藥物交互作用**：

主要交互作用（Major）：
- Metformin：可能增加乳酸酸中毒風險
- Amphotericin B：可能增加腎毒性
- Vancomycin、Aminoglycosides（Amikacin, Gentamicin, Kanamycin）：可能增加腎毒性
- Cyclosporine、Tacrolimus：可能增加腎毒性
- NSAIDs（Ketorolac, Ibuprofen, Naproxen, Celecoxib）：可能增加腎毒性
- Cisplatin：可能增加腎毒性

中度交互作用（Moderate）：
- Beta-blockers（Metoprolol, Atenolol 等）
- 利尿劑（Furosemide, Hydrochlorothiazide 等）


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**Anemia, Sickle Cell** 🟡 Moderate
- 應謹慎使用本藥物。

**Multiple Myeloma** 🟡 Moderate
- 不建議使用本藥物。可能有致命風險。

**重症肌無力** 🟡 Moderate
- 應謹慎使用本藥物。

**腎臟疾病** 🟡 Moderate
- 應謹慎使用本藥物。可能有嚴重不良反應。

**Hypersensitivity** 🟡 Moderate
- 需定期監測。可能有致命風險。

**甲狀腺機能亢進** 🟢 Minor
- 本藥物在此情況下禁用。

**Pheochromocytoma** 🟢 Minor
- 應謹慎使用本藥物。

## 結論與下一步

**決策：Hold**

**理由：**
文獻中 iodixanol 與骨關節炎的關聯主要來自診斷性應用（顯影劑用於軟骨造影），而非治療效果。缺乏機轉支持和臨床試驗證據表明這個預測可能是知識圖譜中的偽相關。

**若要推進需要：**
- 明確的藥理機轉研究支持治療潛力
- 體外/體內實驗驗證 iodixanol 對軟骨的直接效果
- 目前不建議進一步探索此適應症

---

## 相關藥物報告

- [Deoxycholic Acid]({{ "/drugs/deoxycholic_acid/" | relative_url }}) - 證據等級 L5
- [Brivaracetam]({{ "/drugs/brivaracetam/" | relative_url }}) - 證據等級 L5
- [Sacituzumab Govitecan]({{ "/drugs/sacituzumab_govitecan/" | relative_url }}) - 證據等級 L5
- [Dipyridamole]({{ "/drugs/dipyridamole/" | relative_url }}) - 證據等級 L5
- [Oxytetracycline]({{ "/drugs/oxytetracycline/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Iodixanol老藥新用驗證報告. https://twtxgnn.yao.care/drugs/iodixanol/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_iodixanol,
  title = {Iodixanol老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/iodixanol/}
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
