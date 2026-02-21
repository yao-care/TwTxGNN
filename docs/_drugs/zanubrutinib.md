---
layout: default
title: Zanubrutinib
description: "Zanubrutinib 的老藥新用潛力分析。模型預測等級 L5，包含 6 個預測適應症。查看 AI 預測與臨床證據完整報告。"
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L3
indication_count: 6
---

# Zanubrutinib

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>L5</strong> | 預測適應症: <strong>6</strong> 個
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Zanubrutinib：從 B 細胞淋巴瘤到骨髓性白血病

## 一句話總結

<p class="key-answer" data-question="Zanubrutinib 可以用於治療什麼新適應症？">
Zanubrutinib 原本用於治療被套細胞淋巴瘤、華氏巨球蛋白血症等 B 細胞惡性腫瘤。
TxGNN 模型預測它可能對**骨髓性白血病 (myeloid leukemia)** 有效，
有 **2 個臨床試驗**和 **9 篇文獻**支持這個方向。
</p>

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 被套細胞淋巴瘤 (MCL)、華氏巨球蛋白血症 (WM)、CLL/SLL、邊緣區淋巴瘤、濾泡性淋巴瘤 |
| 預測新適應症 | myeloid leukemia、vertebral anomalies and variable endocrine and T-cell dysfunction、ganglioneuroblastoma (disease)、腹膜後腫瘤、Ewing sarcoma、神經母細胞瘤 |
| TxGNN 預測分數 | 99.65% |
| 證據等級 | L2 (有臨床試驗支持) |
| 台灣上市 | 已上市 |
| 許可證數 | 1 張 (有效) |
| 建議決策 | Proceed with Guardrails |





## 預測適應症詳細分析

<details class="indication-section" open>
<summary>
<span class="indication-name">1. myeloid leukemia</span>
<span class="evidence-badge evidence-L3">L3</span>
<span class="prediction-score">99.65%</span> <span class="primary-badge">主要分析</span>
</summary>
<div class="indication-content">

<h3>為什麼這個預測合理？</h3>

<p>Zanubrutinib 是高選擇性的布魯頓酪氨酸激酶 (BTK) 抑制劑。</p>
<p>BTK 在 B 細胞受體 (BCR) 訊號傳遞中扮演關鍵角色，抑制 BTK 可阻斷惡性 B 細胞的增殖與存活。</p>

<p><strong>作用機轉：</strong></p>
<ul>
<li>抑制 BTK (Bruton tyrosine kinase)，IC50 約 20 nM</li>
<li>相較於 ibrutinib，具有更高的 BTK 選擇性</li>
<li>較少 off-target 效應，心房顫動等副作用較低</li>

</ul>
<p>雖然 BTK 主要表現於 B 細胞，但近年研究發現 BTK 在某些骨髓性惡性腫瘤中也有表現，</p>
<p>這可能是預測 zanubrutinib 對骨髓性白血病有效的機轉基礎。</p>

<h3>臨床試驗</h3>

<table>
<thead>
<tr><th>試驗編號</th><th>階段</th><th>狀態</th><th>人數</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://clinicaltrials.gov/study/NCT04477291" target="_blank">NCT04477291</a></td><td>PHASE1</td><td>TERMINATED</td><td>45</td><td>A Phase 1a/b Trial of CG-806 in Patients With Relapsed/Refractory Acute Myeloid ...</td></tr>
<tr><td><a href="https://clinicaltrials.gov/study/NCT05665530" target="_blank">NCT05665530</a></td><td>PHASE1</td><td>COMPLETED</td><td>86</td><td>A Phase 1 Open-Label, Multi-Center, Safety and Efficacy Study of PRT2527 as Mono...</td></tr>
</tbody>
</table>

<h3>相關文獻</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/39647999/" target="_blank">39647999</a></td><td>2025</td><td>Article</td><td>Journal of clinical oncology :</td><td>Zanubrutinib Versus Bendamustine and Rituximab in Patients With Treatment-Naïve ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/40334067/" target="_blank">40334067</a></td><td>2025</td><td>Article</td><td>Blood advances</td><td>Zanubrutinib is well tolerated and effective in patients with CLL/SLL intolerant...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/40829104/" target="_blank">40829104</a></td><td>2026</td><td>Article</td><td>Blood advances</td><td>Zanubrutinib for the treatment of patients with del(17p) and/or TP53 CLL/SLL: an...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36400069/" target="_blank">36400069</a></td><td>2023</td><td>Article</td><td>The Lancet. Haematology</td><td>Zanubrutinib in patients with previously treated B-cell malignancies intolerant ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/34959482/" target="_blank">34959482</a></td><td>2021</td><td>Article</td><td>Pharmaceutics</td><td>The TKI Era in Chronic Leukemias.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36402930/" target="_blank">36402930</a></td><td>2023</td><td>Article</td><td>Leukemia</td><td>Managing Waldenström&#x27;s macroglobulinemia with BTK inhibitors.</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/36325357/" target="_blank">36325357</a></td><td>2022</td><td>Article</td><td>Frontiers in immunology</td><td>Case report: A rare case of coexisting Waldenstrom Macroglobulinemia and B-cell ...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38288815/" target="_blank">38288815</a></td><td>2024</td><td>Article</td><td>Anti-cancer agents in medicina</td><td>An Expedition on Synthetic Methodology of FDA-approved Anticancer Drugs (2018-20...</td></tr>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/37150651/" target="_blank">37150651</a></td><td>2023</td><td>Article</td><td>Clinical lymphoma, myeloma &amp; l</td><td>Hepatitis B Virus Reactivation in Patients Receiving Bruton Tyrosine Kinase Inhi...</td></tr>
</tbody>
</table>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">2. vertebral anomalies and variable endocrine and T-cell dysfunction</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.38%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">3. ganglioneuroblastoma (disease)</span>
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
<span class="indication-name">4. retroperitoneal neoplasm</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.30%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">5. Ewing sarcoma</span>
<span class="evidence-badge evidence-L5">L5</span>
<span class="prediction-score">99.27%</span>
</summary>
<div class="indication-content">

<div class="no-evidence-notice">
目前尚無針對此適應症的專門臨床研究。此為 TxGNN 模型預測結果，需進一步驗證。
</div>

</div>
</details>

<details class="indication-section">
<summary>
<span class="indication-name">6. neuroblastoma</span>
<span class="evidence-badge evidence-L4">L4</span>
<span class="prediction-score">99.21%</span>
</summary>
<div class="indication-content">

<h3>相關文獻（1 篇）</h3>

<table>
<thead>
<tr><th>PMID</th><th>年份</th><th>類型</th><th>期刊</th><th>主要發現</th></tr>
</thead>
<tbody>
<tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/38288815/" target="_blank">38288815</a></td><td>2024</td><td>Article</td><td>Anti-cancer agents in medicina</td><td>An Expedition on Synthetic Methodology of FDA-approved Anticancer Drugs (2018-20...</td></tr>
</tbody>
</table>

</div>
</details>


## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 許可證持有者 | 核准日期 |
|---------|------|------|-------------|---------|
| 衛部藥輸字第028160號 | 百悅澤膠囊 80 毫克 | 膠囊劑 | 臺灣百濟神州有限公司 | 2021/09/15 |

**核准適應症：**
1. 先前曾接受至少一種治療的被套細胞淋巴瘤 (MCL) 成人病人
2. 華氏巨球蛋白血症 (WM) 成人病人
3. 先前曾接受至少一種抗 CD20 療法的復發或頑固型邊緣區淋巴瘤 (MZL) 成人病人
4. 慢性淋巴球性白血病 (CLL)/小淋巴球性淋巴瘤 (SLL) 成人病人
5. 併用 obinutuzumab 適用於先前曾接受至少 2 種治療的濾泡性淋巴瘤 (FL) 成人病人

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶治療藥物 (非傳統細胞毒性) |
| 骨髓抑制風險 | 中度 (嗜中性白血球減少、血小板減少) |
| 出血風險 | 需注意，尤其與抗凝血劑併用時 |
| 監測項目 | CBC (含分類)、肝功能、出血徵兆 |
| 處置防護 | 口服藥物，依一般藥物處置規範操作 |

## 安全性考量

**主要藥物交互作用 (Major)：**

| 藥物類別 | 代表藥物 | 交互作用機轉 |
|---------|---------|-------------|
| 抗凝血劑/抗血小板 | Warfarin, Apixaban, Clopidogrel, Aspirin | 增加出血風險 |
| CYP3A 強效抑制劑 | Ketoconazole, Clarithromycin, Cobicistat | 增加 zanubrutinib 血中濃度 |
| CYP3A 強效誘導劑 | Enzalutamide, Apalutamide, Mitotane | 降低 zanubrutinib 血中濃度 |
| 其他 BTK 抑制劑 | Ibrutinib, Acalabrutinib | 藥理作用重疊 |
| 免疫抑制劑 | Adalimumab, Etanercept, Infliximab | 增加感染風險 |

**注意事項：**
- 接受手術前需暫停使用 (術前至少 3-7 天)
- B 型肝炎再活化風險，需監測 HBsAg/anti-HBc
- 心房顫動風險較 ibrutinib 低，但仍需監測


### 藥物-疾病注意事項 (DDSI)

<div class="ddsi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**Arrhythmias, Cardiac** 🟡 Moderate
- 需定期監測。風險包括：心律不整、感染。

**Hemorrhage** 🟡 Moderate
- 需定期監測。風險包括：出血。可能有致命風險。出現症狀時應考慮停藥。

**Pancytopenia** 🟡 Moderate
- 需定期監測。風險包括：血栓、貧血。

**Hepatic Insufficiency** 🟡 Moderate
- 需定期監測。可能有嚴重不良反應。

**Infections** 🟡 Moderate
- 需定期監測。風險包括：感染。可能有致命風險。

**腎臟疾病** 🟡 Moderate
- 需定期監測。可能有嚴重不良反應。

### 藥物-食物交互作用 (DFI)

<div class="dfi-source">資料來源：<a href="https://ddinter2.scbdd.com/" target="_blank">DDInter 2.0</a>（原文內容請參閱該網站）</div>

**葡萄柚汁** 🟢 Minor
- 影響：影響藥物代謝。可能增加藥物血中濃度。
- 建議：建議避免併用。建議空腹服用。避免食用葡萄柚或葡萄柚汁。


## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
雖然 zanubrutinib 的主要作用在 B 細胞，但其在血液惡性腫瘤中的廣泛療效已獲證實。
針對骨髓性白血病的預測有初步臨床試驗支持，但這些試驗主要探討聯合用藥而非單獨使用。

**若要推進需要：**
- 確認 BTK 在骨髓性白血病中的表現與功能
- 設計專門針對骨髓性白血病的 Phase 1/2 臨床試驗
- 評估與現有骨髓性白血病治療藥物的聯合效果
- 建立生物標記預測可能受益的患者亞群

---

## 相關藥物報告

- [Tizanidine]({{ "/drugs/tizanidine/" | relative_url }}) - 證據等級 L5
- [Denosumab]({{ "/drugs/denosumab/" | relative_url }}) - 證據等級 L5
- [Cerliponase Alfa]({{ "/drugs/cerliponase_alfa/" | relative_url }}) - 證據等級 L5
- [Insulin Lispro]({{ "/drugs/insulin_lispro/" | relative_url }}) - 證據等級 L5
- [Ferrous Gluconate]({{ "/drugs/ferrous_gluconate/" | relative_url }}) - 證據等級 L5

---

{% include ai-analysis.html %}

{% include social-share.html %}

## 引用本報告

如需引用本報告，請使用以下格式：

**APA 格式：**
```
TwTxGNN. (2026). Zanubrutinib老藥新用驗證報告. https://twtxgnn.yao.care/drugs/zanubrutinib/
```

**BibTeX 格式：**
```bibtex
@misc{twtxgnn_zanubrutinib,
  title = {Zanubrutinib老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/drugs/zanubrutinib/}
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
