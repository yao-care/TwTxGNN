---
layout: default
title: 關於專案
nav_order: 10
description: "TwTxGNN 是基於哈佛 TxGNN 模型的老藥新用預測平台，整合臨床試驗、文獻等多來源證據，提供 191 個台灣健保藥品的完整驗證報告。"
permalink: /about/
---

# 關於本專案

<div class="key-takeaway">
用 AI 加速老藥新用的證據驗證，從預測到證據一目瞭然。
</div>

---

## 專案背景

<p class="key-answer" data-question="TwTxGNN 是什麼？">
<strong>TwTxGNN</strong> 是一個藥物再利用（Drug Repurposing）研究輔助平台，基於哈佛大學 Zitnik Lab 發表於 <em>Nature Medicine</em> 的 TxGNN 模型，針對台灣健保核准藥品進行適應症擴展預測。不同於其他預測工具，本平台不僅提供 AI 預測分數，更整合 ClinicalTrials.gov、PubMed 等來源的臨床證據，讓研究人員能快速評估預測的可信度。
</p>

---

## 作者與團隊

| 項目 | 資訊 |
|------|------|
| 專案維護 | Yao.Care |
| 模型基礎 | Harvard TxGNN (Zitnik Lab) |
| 最後更新 | 2026 年 2 月 |

### 學術依據

本專案的 AI 預測模型基於以下論文：

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## 什麼是老藥新用？

<p class="key-answer" data-question="什麼是老藥新用？">
<strong>老藥新用（Drug Repurposing）</strong> 是指發現現有藥物的新治療用途。相較於從頭開發新藥需要 10-15 年和 10-20 億美元，老藥新用只需 3-5 年和 1-3 億美元，且已有人體安全性資料，失敗風險較低。
</p>

<table class="comparison-table">
<thead>
<tr><th>比較項目</th><th>新藥開發</th><th>老藥新用</th></tr>
</thead>
<tbody>
<tr><td>開發時間</td><td>10-15 年</td><td>3-5 年</td></tr>
<tr><td>開發成本</td><td>10-20 億美元</td><td>1-3 億美元</td></tr>
<tr><td>安全性資料</td><td>需重新建立</td><td>已有人體資料</td></tr>
<tr><td>失敗風險</td><td>極高 (>90%)</td><td>較低</td></tr>
</tbody>
</table>

<div class="key-takeaway">
老藥新用的優勢在於：藥物的安全性、藥物動力學、製程都已經過驗證，可以直接進入臨床療效試驗。
</div>

---

## 什麼是 TxGNN？

<p class="key-answer" data-question="什麼是 TxGNN？">
<a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a> 是由哈佛醫學院 Zitnik Lab 團隊開發的深度學習模型，發表於 <em>Nature Medicine</em>，專門用於預測藥物與疾病的新關聯，是首個專為臨床醫師設計的老藥新用基礎模型。
</p>

<blockquote class="expert-quote">
「TxGNN 整合了 17,080 個生物醫學實體的知識圖譜，使用圖神經網路學習節點間的複雜關聯，能預測藥物對罕見疾病的潛在療效。」
<cite>— Huang et al., Nature Medicine (2023)</cite>
</blockquote>

### 技術特點

<ol class="actionable-steps">
<li><strong>知識圖譜</strong>：整合藥物、疾病、基因、蛋白質等 17,080 個節點</li>
<li><strong>圖神經網路</strong>：學習節點間的複雜關聯</li>
<li><strong>預測能力</strong>：可預測藥物對哪些疾病可能有效</li>
</ol>

---

## 資料來源

<p class="key-answer" data-question="TwTxGNN 的資料來源有哪些？">
本平台整合六大公開資料來源，包括 AI 預測、臨床試驗、學術文獻、藥物資訊、台灣上市資訊和藥物交互作用資料。
</p>

<table class="comparison-table">
<thead>
<tr><th>資料類型</th><th>來源</th><th>說明</th></tr>
</thead>
<tbody>
<tr><td>AI 預測</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>哈佛大學知識圖譜預測模型</td></tr>
<tr><td>臨床試驗</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>全球臨床試驗登記資料庫</td></tr>
<tr><td>學術文獻</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>生物醫學文獻資料庫</td></tr>
<tr><td>藥物資訊</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>藥物與靶點資料庫</td></tr>
<tr><td>台灣上市</td><td><a href="https://data.fda.gov.tw/">TFDA</a></td><td>衛福部食藥署開放資料</td></tr>
<tr><td>藥物交互作用</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>藥物交互作用資料庫</td></tr>
</tbody>
</table>

---

## 專案規模

| 項目 | 數量 |
|------|------|
| 藥物報告 | 191 份 |
| 老藥新用候選 | 142,328 筆 |
| DDI 資料 | 222,391 筆 |

---

## 如何引用

如需引用本平台資料，請使用以下格式：

### APA 格式

```
TwTxGNN. (2026). TwTxGNN 老藥新用驗證報告. https://twtxgnn.yao.care/
```

### BibTeX 格式

```bibtex
@misc{twtxgnn2026,
  title = {TwTxGNN 老藥新用驗證報告},
  author = {TwTxGNN Team},
  year = {2026},
  url = {https://twtxgnn.yao.care/},
  note = {Accessed: 2026-02-19}
}
```

### 引用原始模型

如使用 TxGNN 預測結果，請同時引用原始論文：

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and others},
  journal={Nature Medicine},
  year={2023},
  doi={10.1038/s41591-023-02233-x}
}
```

---

## 聯絡與回饋

如有問題或建議，歡迎透過以下管道聯繫：

- **GitHub Issues**: [https://github.com/yao-care/TwTxGNN/issues](https://github.com/yao-care/TwTxGNN/issues)
- **專案首頁**: [https://twtxgnn.yao.care/](https://twtxgnn.yao.care/)

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>最後審核：2026-02-19 | 審核者：TwTxGNN Research Team</small>
</div>
