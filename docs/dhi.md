---
layout: default
title: 藥物-草藥交互作用
parent: 安全性資料
nav_order: 4
description: "TwTxGNN 藥物-草藥交互作用資料庫，收錄 35 筆 DHI 資料，涵蓋 10 種常見草藥，協助評估草藥對藥效的影響。"
permalink: /dhi/
---

# 藥物-草藥交互作用 (DHI)

<p class="key-answer" data-question="什麼是藥物-草藥交互作用？">
<strong>藥物-草藥交互作用（Drug-Herb Interaction, DHI）</strong> 是指草藥或植物性補充品影響藥物療效或安全性的現象。本平台精選 <strong>35 筆</strong> DHI 資料，涵蓋 <strong>10 種臨床上最重要的草藥</strong>，協助研究人員評估草藥使用對老藥新用的影響。
</p>

<div class="key-takeaway">
許多患者同時使用處方藥和草藥保健品，但不一定會主動告知醫師。評估老藥新用時，需考量目標族群的草藥使用習慣。
</div>

---

## 什麼是 DHI？

草藥雖然是「天然」產品，但含有多種活性成分，可能透過以下機制與藥物產生交互作用：

| 機制 | 說明 | 範例 |
|------|------|------|
| **酵素誘導** | 增加藥物代謝，降低療效 | 聖約翰草誘導 CYP3A4 |
| **酵素抑制** | 減少藥物代謝，增加毒性 | 某些草藥抑制 CYP2D6 |
| **藥效加成** | 增強藥物作用 | 銀杏 + 抗凝血藥 |
| **藥效拮抗** | 減弱藥物作用 | 人參 + 降血糖藥 |

---

## 資料來源

<table class="comparison-table">
<thead>
<tr><th>項目</th><th>資訊</th></tr>
</thead>
<tbody>
<tr>
  <td>資料來源</td>
  <td>精選資料集（臨床文獻整理）</td>
</tr>
<tr>
  <td>DHI 筆數</td>
  <td>35</td>
</tr>
<tr>
  <td>涵蓋草藥種類</td>
  <td>10 種</td>
</tr>
<tr>
  <td>最後更新</td>
  <td>2026-02-21</td>
</tr>
</tbody>
</table>

**說明**：目前公開可下載的 DHI 資料庫非常有限。DDInter 2.0 論文提到未來將支援 DHI 資料，屆時本平台會進行整合更新。

---

## 涵蓋的重要草藥

<p class="key-answer" data-question="哪些草藥與藥物的交互作用最重要？">
以下 10 種草藥在臨床上最常見且交互作用最為顯著，是評估藥物安全性時的重點關注對象。
</p>

### 1. 聖約翰草（St. John's Wort）

| 項目 | 說明 |
|------|------|
| **用途** | 輕度憂鬱、焦慮 |
| **主要機制** | 強效 CYP3A4/P-gp 誘導劑 |
| **重大交互** | 降低多種藥物濃度（免疫抑制劑、口服避孕藥、抗病毒藥） |
| **嚴重程度** | Major |

<div class="key-takeaway">
聖約翰草是最重要的 DHI 來源，可能使許多藥物失效，應列為老藥新用評估的重點項目。
</div>

### 2. 銀杏（Ginkgo biloba）

| 項目 | 說明 |
|------|------|
| **用途** | 改善記憶、血液循環 |
| **主要機制** | 抗血小板作用 |
| **重大交互** | 增加出血風險（與抗凝血藥、NSAIDs 併用） |
| **嚴重程度** | Moderate - Major |

### 3. 人參（Ginseng）

| 項目 | 說明 |
|------|------|
| **用途** | 提神、增強體力 |
| **主要機制** | 多重途徑（血糖、血壓、凝血） |
| **重大交互** | 影響降血糖藥、Warfarin、MAOIs |
| **嚴重程度** | Moderate |

### 4. 大蒜（Garlic）

| 項目 | 說明 |
|------|------|
| **用途** | 降膽固醇、心血管保健 |
| **主要機制** | 抗血小板、輕度 CYP3A4 影響 |
| **重大交互** | 增加出血風險、影響 HIV 蛋白酶抑制劑 |
| **嚴重程度** | Minor - Moderate |

### 5. 紫錐花（Echinacea）

| 項目 | 說明 |
|------|------|
| **用途** | 增強免疫力、預防感冒 |
| **主要機制** | 免疫調節、CYP1A2/CYP3A4 影響 |
| **重大交互** | 可能影響免疫抑制劑效果 |
| **嚴重程度** | Minor - Moderate |

### 6-10. 其他重要草藥

| 草藥 | 主要機制 | 嚴重程度 |
|------|----------|----------|
| **卡瓦（Kava）** | CNS 抑制、肝毒性 | Moderate - Major |
| **纈草（Valerian）** | CNS 抑制 | Minor - Moderate |
| **甘草（Licorice）** | 礦物皮質素作用 | Moderate |
| **當歸（Dong Quai）** | 增強抗凝血作用 | Moderate |
| **綠茶（Green Tea）** | 維生素 K、咖啡因、CYP 影響 | Minor - Moderate |

---

## 在老藥新用中的應用

<blockquote class="expert-quote">
「評估藥物再利用時，需了解目標患者族群的草藥和保健品使用習慣。尤其是腫瘤患者，許多人會使用補充療法，可能與化療藥物產生交互作用。」
<cite>— 藥物安全性評估原則</cite>
</blockquote>

### 高風險族群

<ol class="actionable-steps">
<li><strong>腫瘤患者</strong>：常使用各種補充療法</li>
<li><strong>老年人</strong>：多重用藥且保健品使用率高</li>
<li><strong>慢性病患者</strong>：長期服用多種藥物</li>
<li><strong>特定文化背景</strong>：傳統醫學使用較普遍的族群</li>
</ol>

---

## 評估建議

1. **主動詢問**：在臨床試驗設計時，應主動詢問受試者的草藥使用
2. **排除條件**：考慮將使用高風險草藥（如聖約翰草）列為排除條件
3. **監測計畫**：針對無法排除的草藥使用，設計適當的監測方案
4. **衛教材料**：提供受試者關於 DHI 的衛教資訊

---

## 下載資料

需要進行分析？可從 GitHub 下載精選 DHI 資料：

| 資料 | 說明 | 連結 |
|------|------|------|
| DHI 精選資料 | 結構化 JSON | [GitHub](https://github.com/yao-care/TwTxGNN/tree/main/data/external/dhi) |

---

## 參考資源

- [Natural Medicines Database](https://naturalmedicines.therapeuticresearch.com/)（需訂閱）
- [Memorial Sloan Kettering - About Herbs](https://www.mskcc.org/cancer-care/diagnosis-treatment/symptom-management/integrative-medicine/herbs)
- [NIH - National Center for Complementary and Integrative Health](https://www.nccih.nih.gov/)

---

## 相關資源

| 資源 | 說明 | 連結 |
|------|------|------|
| 藥物-藥物交互作用 | DDI 資料庫 | [前往]({{ '/ddi/' | relative_url }}) |
| 藥物-疾病注意事項 | DDSI 資料庫 | [前往]({{ '/ddsi/' | relative_url }}) |
| 藥物-食物交互作用 | DFI 資料庫 | [前往]({{ '/dfi/' | relative_url }}) |

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本頁面的 DHI 資料僅供研究參考，<strong>不構成用藥或草藥使用建議</strong>。如正在服用處方藥，請諮詢醫師或藥師後再使用任何草藥或保健品。
<br><br>
<small>最後審核：2026-02-21 | 審核者：TwTxGNN Research Team</small>
</div>
