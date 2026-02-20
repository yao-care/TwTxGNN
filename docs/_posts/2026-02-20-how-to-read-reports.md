---
layout: default
title: "教學：如何閱讀 TwTxGNN 驗證報告"
description: "一步步教你如何閱讀和理解老藥新用驗證報告，包含證據等級、決策建議的解讀方式。"
date: 2026-02-20
categories: [教學]
tags: [使用指南, 新手入門]
---

# 如何閱讀驗證報告

<p class="key-answer" data-question="報告中最重要的資訊是什麼？">
每份報告最重要的三個資訊：<strong>證據等級</strong>（L1-L5）、<strong>預測分數</strong>（AI 信心）、<strong>決策建議</strong>（Go/Proceed/Hold）。這三者結合，能快速告訴你這個預測的可信度和行動方向。
</p>

---

## 報告結構導覽

### 1. 一句話總結

報告開頭的一句話總結是最重要的快速閱讀區塊：

<div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 1rem; border-radius: 8px; border-left: 4px solid #2E7D32; margin: 1rem 0;">
<strong>範例：</strong>Temozolomide 原本用於治療神經膠母細胞瘤。TxGNN 模型預測它可能對成人星狀細胞瘤有效，目前有 2 個臨床試驗和超過 20 篇文獻支持。
</div>

這告訴你：
- 藥物原本的用途
- AI 預測的新用途
- 有多少證據支持

### 2. 快速總覽表

| 項目 | 如何解讀 |
|------|----------|
| TxGNN 預測分數 | 99%+ 表示 AI 非常有信心 |
| 證據等級 | L1 最強，L5 僅有預測 |
| 建議決策 | Go 可直接推進，Hold 需等待 |
| 台灣上市 | 是否已有核准許可證 |

### 3. 臨床試驗證據

臨床試驗是最重要的證據來源：

| Phase | 說明 | 證據強度 |
|-------|------|----------|
| **Phase 3** | 大規模驗證性試驗 | 最強 |
| **Phase 2** | 探索性試驗 | 中等 |
| **Phase 1** | 安全性試驗 | 較弱 |

### 4. 文獻證據

| 文獻類型 | 說明 | 證據強度 |
|----------|------|----------|
| **RCT** | 隨機對照試驗 | 最高 |
| **Cohort** | 世代研究 | 中等 |
| **Case Report** | 個案報告 | 參考 |

---

## 實際操作步驟

<ol class="actionable-steps">
<li><strong>第一步</strong>：從<a href="/evidence-high/">高證據等級</a>頁面開始瀏覽</li>
<li><strong>第二步</strong>：點擊感興趣的藥物進入報告</li>
<li><strong>第三步</strong>：先看「一句話總結」和「快速總覽表」</li>
<li><strong>第四步</strong>：如需深入了解，閱讀臨床試驗和文獻證據</li>
<li><strong>第五步</strong>：查看「結論與下一步」了解建議行動</li>
</ol>

---

## 常見問題

### Q: 預測分數高但證據等級低，怎麼解讀？

<div class="key-takeaway">
預測分數反映 AI 的信心程度，證據等級反映臨床研究的充分程度。兩者可能不一致。
</div>

例如 Hydroxyurea：預測分數 99.97%，但證據等級是 L2。這表示：
- AI 對預測非常有信心
- 但臨床證據還不夠充分（只有早期研究）
- 這是值得關注的研究方向

### Q: Go 和 Proceed 有什麼差別？

| 決策 | 含義 | 建議行動 |
|------|------|----------|
| **Go** | 證據非常充分 | 可直接進入深入評估 |
| **Proceed** | 證據充分 | 值得進一步評估可行性 |
| **Consider** | 有一定證據 | 需權衡風險再決定 |
| **Explore** | 值得探索 | 先補充更多資料 |
| **Hold** | 證據不足 | 目前暫不建議推進 |

---

## 延伸閱讀

- [證據等級完整說明](/blog/2026/02/21/evidence-levels-explained/)
- [Anastrozole 案例解讀](/blog/2026/02/22/anastrozole-case-study/)
- [使用指南](/guide/)

---

<div class="disclaimer">
<strong>提醒</strong><br>
本報告僅供研究參考，任何臨床應用需諮詢專業醫療人員。
</div>
