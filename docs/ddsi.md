---
layout: default
title: 藥物-疾病注意事項
parent: 安全性資料
nav_order: 2
description: "TwTxGNN 藥物-疾病注意事項資料庫，收錄 8,359 筆 DDSI 資料，協助評估藥物用於特定疾病患者的安全風險。"
permalink: /ddsi/
---

# 藥物-疾病注意事項 (DDSI)

<p class="key-answer" data-question="什麼是藥物-疾病注意事項？">
<strong>藥物-疾病注意事項（Drug-Disease Safety Information, DDSI）</strong> 是指某些藥物在特定疾病患者身上可能加重病情或造成不良反應的警示資訊。本平台整合 DDInter 2.0 的 <strong>8,359 筆</strong> DDSI 資料，涵蓋 <strong>115 種藥物</strong>的禁忌症與注意事項。
</p>

<div class="key-takeaway">
老藥新用時，需特別注意目標患者群體常見的共病。例如：將某藥物用於癌症患者時，需考量這些患者常見的肝腎功能異常等狀況。
</div>

---

## 什麼是 DDSI？

當藥物用於某些特定疾病的患者時，可能會：

| 情況 | 說明 | 範例 |
|------|------|------|
| **病情惡化** | 藥物可能加重原有疾病 | NSAIDs 惡化腎功能不全 |
| **藥效改變** | 疾病狀態影響藥物代謝 | 肝硬化影響藥物清除率 |
| **毒性增加** | 疾病使器官更易受損 | 心衰竭患者對強心配醣體更敏感 |
| **症狀遮蔽** | 藥物可能掩蓋疾病徵兆 | β-阻斷劑掩蓋低血糖症狀 |

---

## 資料來源

<table class="comparison-table">
<thead>
<tr><th>項目</th><th>資訊</th></tr>
</thead>
<tbody>
<tr>
  <td>資料來源</td>
  <td><a href="https://ddinter2.scbdd.com/" target="_blank" rel="noopener">DDInter 2.0</a></td>
</tr>
<tr>
  <td>DDSI 筆數</td>
  <td>8,359</td>
</tr>
<tr>
  <td>涵蓋藥物</td>
  <td>115 種</td>
</tr>
<tr>
  <td>最後更新</td>
  <td>2026-02-21</td>
</tr>
<tr>
  <td>授權</td>
  <td>CC BY-NC-SA 4.0</td>
</tr>
</tbody>
</table>

---

## DDSI 等級說明

<p class="key-answer" data-question="DDSI 有哪些嚴重程度等級？">
藥物-疾病注意事項依嚴重程度分為三級，從嚴重（Major）到輕微（Minor），每個等級有不同的臨床處置建議。
</p>

| 等級 | 英文 | 說明 | 建議處置 |
|------|------|------|----------|
| **嚴重** | Major | 絕對禁忌或可能危及生命 | 避免使用，尋找替代藥物 |
| **中度** | Moderate | 可能需要調整劑量或密切監測 | 謹慎使用，加強監測 |
| **輕微** | Minor | 臨床意義較低 | 一般可使用，必要時監測 |

---

## 常見的藥物-疾病注意事項

### 肝臟疾病相關

<ol class="actionable-steps">
<li><strong>肝毒性藥物禁忌</strong>：嚴重肝功能不全患者應避免使用肝毒性藥物</li>
<li><strong>劑量調整需求</strong>：主要經肝臟代謝的藥物需減量</li>
<li><strong>凝血功能考量</strong>：肝硬化患者使用抗凝血藥物風險增加</li>
</ol>

### 腎臟疾病相關

- 腎功能不全時需調整經腎排泄藥物劑量
- 腎毒性藥物應避免或謹慎使用
- 需監測電解質變化

### 心血管疾病相關

- 心衰竭患者對某些藥物更敏感
- QT 延長風險藥物需注意心律不整病史
- 低血壓風險藥物需評估現有心血管狀態

---

## 在老藥新用中的應用

<blockquote class="expert-quote">
「當評估藥物再利用時，不僅要考慮藥物是否對新適應症有效，更要考量目標患者群體的共病特徵，避免因共病而產生的安全性問題。」
<cite>— 藥物安全性評估原則</cite>
</blockquote>

### 評估流程建議

1. **確認目標族群**：了解新適應症患者的常見共病
2. **比對 DDSI 資料**：檢查藥物是否對這些共病有禁忌
3. **風險效益評估**：權衡療效與潛在風險
4. **監測計畫制定**：針對高風險族群設計監測方案

---

## 下載資料

需要進行大規模分析？可從 GitHub 下載原始 DDSI 資料：

| 資料 | 說明 | 連結 |
|------|------|------|
| DDSI 原始資料 | DDInter API 回應 | [GitHub](https://github.com/yao-care/TwTxGNN/tree/main/data/external/ddsi) |
| 處理後資料 | 結構化 JSON | [GitHub](https://github.com/yao-care/TwTxGNN/tree/main/data/external/ddsi) |

---

## 相關資源

| 資源 | 說明 | 連結 |
|------|------|------|
| 藥物-藥物交互作用 | DDI 資料庫 | [前往]({{ '/ddi/' | relative_url }}) |
| 藥物-食物交互作用 | DFI 資料庫 | [前往]({{ '/dfi/' | relative_url }}) |
| 藥物-草藥交互作用 | DHI 資料庫 | [前往]({{ '/dhi/' | relative_url }}) |

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本頁面的 DDSI 資料僅供研究參考，<strong>不構成用藥建議</strong>。實際用藥決策請諮詢專業藥師或醫師。藥物對特定疾病的影響會因個人因素而異。
<br><br>
<small>最後審核：2026-02-21 | 審核者：TwTxGNN Research Team</small>
</div>
