---
layout: default
title: 藥物交互作用
parent: 安全性資料
nav_order: 1
description: "TwTxGNN 藥物交互作用資料：DDInter 下載檔共 222,383 筆藥物-藥物交互作用，另附 Guide to PHARMACOLOGY 的藥物標靶資料，協助評估老藥新用的安全性。"
permalink: /ddi/
---

# 藥物交互作用 (DDI)

<p class="key-answer" data-question="TwTxGNN 有哪些藥物交互作用資料？">
本平台的藥物-藥物交互作用（DDI）資料來自 <strong>DDInter</strong> 的 <code>ddinter_code_*.csv</code> 下載檔，共 <strong>222,383 筆</strong>（160,235 組不重複藥物配對），涵蓋 1,939 個藥物名稱。藥物報告另外列出 <strong>Guide to PHARMACOLOGY</strong> 的核准藥物標靶資料（藥物-標靶，不是藥物-藥物交互作用，也沒有嚴重度分級），協助研究人員在評估老藥新用時考量安全性因素。
</p>

<div class="key-takeaway">
藥物交互作用是老藥新用評估的關鍵考量。當藥物用於新適應症時，可能需要與該疾病的標準治療藥物併用，了解潛在的 DDI 風險至關重要。
</div>

---

## 資料來源

<table class="comparison-table">
<thead>
<tr><th>資料來源</th><th>筆數</th><th>涵蓋藥物</th><th>版本／下載日期</th></tr>
</thead>
<tbody>
<tr>
  <td><a href="https://ddinter2.scbdd.com/" target="_blank" rel="noopener">DDInter</a> 下載檔（<code>ddinter_code_*.csv</code>，藥物-藥物交互作用）</td>
  <td>222,383</td>
  <td>1,939 個藥物名稱</td>
  <td>2026-02-08 下載</td>
</tr>
<tr>
  <td><a href="https://www.guidetopharmacology.org/" target="_blank" rel="noopener">Guide to PHARMACOLOGY</a>（核准藥物的藥物-標靶資料，不是 DDI）</td>
  <td>4,799</td>
  <td>2,248 個藥物（ligand）</td>
  <td>GtoPdb 2026.3（2026-09-16 發布）</td>
</tr>
</tbody>
</table>

---

## DDI 等級說明

<p class="key-answer" data-question="藥物交互作用有哪些等級？">
藥物交互作用依嚴重程度分為三級，從嚴重（Major）到輕微（Minor），每個等級有不同的臨床處置建議。
</p>

| 等級 | 英文 | 說明 | 建議處置 |
|------|------|------|----------|
| **嚴重** | Major | 可能危及生命或造成永久傷害 | 避免併用，需尋找替代藥物 |
| **中度** | Moderate | 可能需要調整劑量或密切監測 | 謹慎使用，監測不良反應 |
| **輕微** | Minor | 臨床意義較低 | 一般可併用，必要時監測 |

---

## 如何使用 DDI 資料

### 在藥物報告中查看

每份藥物報告的「安全性考量」區塊都包含重要的藥物交互作用資訊。

<ol class="actionable-steps">
<li>前往<a href="{{ '/drugs/' | relative_url }}">藥物列表</a>找到目標藥物</li>
<li>滾動到報告中的「安全性考量」區塊</li>
<li>查看該藥物的 DDI 警示和禁忌</li>
</ol>

### 下載完整資料集

需要進行大規模分析？原始資料不在 git repo 裡，而是放在 GitHub Release 的資料壓縮檔中（解開後在 <code>data/external/ddi/</code>）：

| 資料 | 說明 | 連結 |
|------|------|------|
| DDInter 資料 | 完整 DDI 對照表（`ddinter/ddinter_code_*.csv`） | [GitHub Releases](https://github.com/yao-care/TwTxGNN/releases) |
| Pharmacology 資料 | 核准藥物的藥物-標靶資料（`pharmacology/approved_drug_detailed_interactions.csv`） | [GitHub Releases](https://github.com/yao-care/TwTxGNN/releases) |

---

## 為什麼 DDI 很重要？

<p>藥物再利用研究不僅要評估療效，更要考量新適應症情境下的藥物交互作用。新適應症的患者常同時使用該疾病的標準治療藥物，交互作用風險需要一併評估。</p>

### 老藥新用情境下的 DDI 考量

1. **疾病標準治療**：新適應症通常有既有的標準治療藥物，需評估併用風險
2. **患者族群差異**：不同疾病的患者可能有不同的共病和用藥習慣
3. **劑量調整需求**：某些 DDI 可透過劑量調整來管理，而非完全禁用

---

## 相關資源

| 資源 | 說明 | 連結 |
|------|------|------|
| 藥物列表 | 查看個別藥物報告 | [前往]({{ '/drugs/' | relative_url }}) |
| 方法論 | 了解證據等級判定 | [前往]({{ '/methodology/' | relative_url }}) |
| 資料來源 | 完整資料來源說明 | [前往]({{ '/sources/' | relative_url }}) |

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本頁面的 DDI 資料僅供研究參考，<strong>不構成用藥建議</strong>。實際用藥決策請諮詢專業藥師或醫師。藥物交互作用的臨床影響會因個人因素而異。
<br><br>
<small>最後審核：2026-02-20 | 審核者：藥提醒科技有限公司 (yao.care)</small>
</div>
