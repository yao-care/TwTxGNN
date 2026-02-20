---
layout: default
title: "教學：證據等級 L1-L5 完整說明"
description: "深入理解 TwTxGNN 的五級證據分類系統，了解每個等級的定義、臨床意義和適用情境。"
date: 2026-02-21
categories: [教學]
tags: [證據等級, 方法論]
---

# 證據等級 L1-L5 完整說明

<p class="key-answer" data-question="TwTxGNN 的證據等級如何分類？">
TwTxGNN 採用五級證據分類系統（L1-L5），從最高的「多個 Phase 3 RCT 支持」到最低的「僅模型預測」。這套分類幫助研究人員快速評估預測的可信度和推進的優先順序。
</p>

---

## 證據等級總覽

| 等級 | 定義 | 臨床試驗要求 | 文獻要求 | 建議行動 |
|------|------|-------------|---------|----------|
| **L1** | 最高證據 | 多個 Phase 3 RCT | 系統性回顧/Meta-analysis | Go |
| **L2** | 高證據 | 單一 RCT 或多個 Phase 2 | 多篇高品質研究 | Proceed |
| **L3** | 中等證據 | 觀察性研究 | 大型病例系列 | Consider |
| **L4** | 初步證據 | 前臨床/機轉研究 | 個案報告 | Explore |
| **L5** | 僅預測 | 無 | 無 | Hold |

---

## L1：最高證據等級

<div style="background: #e8f5e9; padding: 1rem; border-radius: 8px; border-left: 4px solid #2E7D32; margin: 1rem 0;">
<strong>定義：</strong>具有多個大型隨機對照試驗（Phase 3 RCT）支持，或有系統性回顧/Meta-analysis 彙整證據。
</div>

**達標條件**（滿足任一）：
- 2+ 個 Phase 3 RCT 呈現正向結果
- 1 個系統性回顧或 Meta-analysis
- 已被納入臨床指引

**代表案例**：
- [Temozolomide](/drugs/temozolomide/) - 腦瘤藥物用於星狀細胞瘤
- [Anastrozole](/drugs/anastrozole/) - 乳癌輔助治療

**適合行動**：直接進入深入可行性評估

---

## L2：高證據等級

<div style="background: #c8e6c9; padding: 1rem; border-radius: 8px; border-left: 4px solid #66BB6A; margin: 1rem 0;">
<strong>定義：</strong>具有單一 RCT 或多個 Phase 2 試驗支持，臨床證據相當充分。
</div>

**達標條件**（滿足任一）：
- 1 個 Phase 3 RCT
- 2+ 個 Phase 2 試驗
- 多篇高品質臨床研究（非 RCT）

**代表案例**：
- [Vonoprazan](/drugs/vonoprazan/) - 新一代胃藥
- [Hydroxyurea](/drugs/hydroxyurea/) - 血液病藥物

**適合行動**：值得進一步評估可行性，考慮設計驗證試驗

---

## L3：中等證據等級

<div style="background: #fff9c4; padding: 1rem; border-radius: 8px; border-left: 4px solid #FDD835; margin: 1rem 0;">
<strong>定義：</strong>有觀察性研究或大型病例系列支持，但缺乏隨機對照試驗。
</div>

**達標條件**：
- 世代研究（Cohort study）
- 病例對照研究（Case-control study）
- 大型病例系列（>20 例）

**適合行動**：有初步證據，待補充 RCT 後可升級評估

---

## L4：初步證據等級

<div style="background: #ffe0b2; padding: 1rem; border-radius: 8px; border-left: 4px solid #FB8C00; margin: 1rem 0;">
<strong>定義：</strong>有前臨床研究、機轉研究或少數個案報告，但缺乏系統性臨床驗證。
</div>

**達標條件**：
- 動物實驗/體外研究
- 藥理機轉研究
- 個案報告（<20 例）
- 電腦模擬/生物資訊學分析

**適合行動**：機轉合理但需進一步臨床驗證，可作為研究方向

---

## L5：僅模型預測

<div style="background: #f5f5f5; padding: 1rem; border-radius: 8px; border-left: 4px solid #9E9E9E; margin: 1rem 0;">
<strong>定義：</strong>僅有 TxGNN 模型預測，尚無任何直接臨床或前臨床證據。
</div>

**特點**：
- 預測分數可能很高（>99%）
- 但無相關研究文獻
- 可能是尚未被研究的領域

**適合行動**：可作為研究假設的起點，但不建議直接推進

---

## 重要觀念：預測分數 ≠ 證據等級

<div class="key-takeaway">
預測分數是 AI 模型的信心程度，證據等級是臨床研究的充分程度。高預測分數但低證據等級，代表這是一個值得探索但尚未被研究的方向。
</div>

| 情境 | 預測分數 | 證據等級 | 解讀 |
|------|----------|----------|------|
| 情境 A | 99.9% | L1 | 模型準確識別已驗證的用途 |
| 情境 B | 99.9% | L5 | 可能是未被研究的新機會 |
| 情境 C | 95.0% | L2 | 雖然預測信心較低，但有臨床證據 |

---

## 證據等級升級路徑

<ol class="actionable-steps">
<li><strong>L5 → L4</strong>：發表前臨床研究或機轉分析</li>
<li><strong>L4 → L3</strong>：進行觀察性研究或收集大型病例系列</li>
<li><strong>L3 → L2</strong>：完成 Phase 2 臨床試驗</li>
<li><strong>L2 → L1</strong>：完成 Phase 3 RCT 或發表系統性回顧</li>
</ol>

---

## 延伸閱讀

- [如何閱讀報告](/blog/2026/02/20/how-to-read-reports/)
- [Hydroxyurea：99.97% 卻是 L2](/blog/2026/02/23/hydroxyurea-high-score-l2/)
- [方法論](/methodology/)

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
證據等級判定基於公開資料自動化分析，可能存在遺漏或誤判。如有疑問，請以原始文獻為準。
</div>
