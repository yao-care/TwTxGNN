---
layout: default
title: 藥物-食物交互作用
parent: 安全性資料
nav_order: 3
description: "TwTxGNN 藥物-食物交互作用資料庫，收錄 857 筆 DFI 資料，涵蓋 29 種常見食物，協助評估飲食對藥效的影響。"
permalink: /dfi/
---

# 藥物-食物交互作用 (DFI)

<p class="key-answer" data-question="什麼是藥物-食物交互作用？">
<strong>藥物-食物交互作用（Drug-Food Interaction, DFI）</strong> 是指食物成分影響藥物吸收、代謝或療效的現象。本平台整合 DDInter 2.0 的 <strong>857 筆</strong> DFI 資料，涵蓋 <strong>29 種常見食物</strong>，幫助研究人員了解飲食對藥物的影響。
</p>

<div class="key-takeaway">
藥物-食物交互作用常被忽視，但對老藥新用研究非常重要。不同疾病的患者可能有不同的飲食習慣，需考量這些因素對藥效的影響。
</div>

---

## 什麼是 DFI？

食物與藥物的交互作用主要透過以下機制發生：

| 機制 | 說明 | 範例 |
|------|------|------|
| **吸收影響** | 食物改變藥物在腸道的吸收 | 鈣質降低某些抗生素吸收 |
| **代謝影響** | 食物成分影響肝臟酵素活性 | 葡萄柚抑制 CYP3A4 |
| **協同作用** | 食物增強藥物效果 | 高鉀食物 + 保鉀利尿劑 |
| **拮抗作用** | 食物減弱藥物效果 | 維生素 K + Warfarin |

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
  <td>DFI 筆數</td>
  <td>857</td>
</tr>
<tr>
  <td>涵蓋食物種類</td>
  <td>29 種</td>
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

## DFI 等級說明

| 等級 | 英文 | 說明 | 建議處置 |
|------|------|------|----------|
| **嚴重** | Major | 顯著影響藥效或造成毒性 | 避免同時攝取，需衛教 |
| **中度** | Moderate | 可能需要調整用藥時間或劑量 | 建議分開服用 |
| **輕微** | Minor | 臨床意義較低 | 一般可同時攝取 |

---

## 常見的藥物-食物交互作用

### 葡萄柚（Grapefruit）

<p class="key-answer" data-question="葡萄柚如何影響藥物？">
葡萄柚含有呋喃香豆素（furanocoumarins），會抑制腸道的 CYP3A4 酵素，導致多種藥物血中濃度升高，可能增加副作用風險。
</p>

受影響的常見藥物：
- Statins（降膽固醇藥）
- 鈣離子阻斷劑
- 某些免疫抑制劑
- 部分抗心律不整藥

### 高維生素 K 食物

<ol class="actionable-steps">
<li>深綠色蔬菜（菠菜、甘藍）含高量維生素 K</li>
<li>會減弱 Warfarin 等抗凝血藥的效果</li>
<li>建議維持穩定的維生素 K 攝取量，而非完全避免</li>
</ol>

### 乳製品

- 鈣質會與某些抗生素（如 Fluoroquinolones）結合
- 降低藥物吸收
- 建議間隔 2 小時服用

### 酒精

- 增強中樞神經抑制劑效果
- 可能增加肝毒性藥物的風險
- 某些藥物會產生雙硫侖樣反應（Disulfiram-like reaction）

---

## 在老藥新用中的應用

<blockquote class="expert-quote">
「藥物再利用研究需考量目標患者族群的飲食習慣。例如，若新適應症患者常需攝取特定營養品，需評估這些食物與候選藥物的交互作用。」
<cite>— 藥物安全性評估原則</cite>
</blockquote>

### 評估要點

1. **目標族群飲食特徵**：了解新適應症患者的常見飲食習慣
2. **營養補充品使用**：許多慢性病患者會服用保健食品
3. **特殊飲食需求**：如糖尿病患者的低糖飲食、腎病患者的低鉀飲食
4. **文化因素**：不同地區的飲食習慣差異

---

## 涵蓋的食物類別

本資料庫涵蓋以下 29 種常見食物/食物成分：

| 類別 | 食物 |
|------|------|
| **水果** | 葡萄柚、柑橘類、蔓越莓 |
| **蔬菜** | 菠菜、甘藍、綠花椰菜 |
| **乳製品** | 牛奶、起司、優格 |
| **飲料** | 咖啡、茶、酒精 |
| **其他** | 高纖食物、高脂食物、海鮮 |

---

## 下載資料

需要進行大規模分析？可從 GitHub 下載原始 DFI 資料：

| 資料 | 說明 | 連結 |
|------|------|------|
| DFI 原始資料 | DDInter API 回應 | [GitHub](https://github.com/yao-care/TwTxGNN/tree/main/data/external/dfi) |
| 處理後資料 | 結構化 JSON | [GitHub](https://github.com/yao-care/TwTxGNN/tree/main/data/external/dfi) |

---

## 相關資源

| 資源 | 說明 | 連結 |
|------|------|------|
| 藥物-藥物交互作用 | DDI 資料庫 | [前往]({{ '/ddi/' | relative_url }}) |
| 藥物-疾病注意事項 | DDSI 資料庫 | [前往]({{ '/ddsi/' | relative_url }}) |
| 藥物-草藥交互作用 | DHI 資料庫 | [前往]({{ '/dhi/' | relative_url }}) |

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本頁面的 DFI 資料僅供研究參考，<strong>不構成飲食或用藥建議</strong>。實際用藥期間的飲食注意事項請諮詢專業藥師或醫師。藥物與食物的交互作用會因個人因素而異。
<br><br>
<small>最後審核：2026-02-21 | 審核者：TwTxGNN Research Team</small>
</div>
