---
layout: default
title: "案例解讀：Hydroxyurea — 99.97% 預測分數卻是 L2"
description: "透過 Hydroxyurea 案例，理解預測分數與證據等級的差異，以及如何正確解讀這類「高分數低等級」的預測。"
date: 2026-02-23
categories: [案例解讀, L2]
tags: [hydroxyurea, 乳癌, 證據等級]
drugs: Hydroxyurea
summary: "預測分數 ≠ 證據等級，高分數低等級代表未被充分研究的機會"
---

# 案例解讀：99.97% 卻是 L2

<p class="key-answer" data-question="預測分數和證據等級有什麼差異？">
<strong>預測分數</strong>反映 AI 模型的信心程度，<strong>證據等級</strong>反映臨床研究的充分程度。Hydroxyurea 以 99.97% 的預測分數卻只有 L2 證據等級，正是這種差異的最佳說明。
</p>

---

## 案例概覽

| 項目 | 內容 |
|------|------|
| 藥物 | Hydroxyurea（羥基脲） |
| 原適應症 | 慢性骨髓性白血病、骨髓纖維化、真性紅血球增多症 |
| 預測適應症 | 女性乳腺癌 |
| 預測分數 | **99.97%**（接近滿分） |
| 證據等級 | **L2** |
| 決策建議 | Proceed with Guardrails |

<div class="key-takeaway">
這是一個典型的「AI 很有信心，但臨床研究不足」的案例。高預測分數意味著值得關注，但 L2 等級提醒我們需要更多驗證。
</div>

---

## 為什麼預測分數這麼高？

### AI 模型看到了什麼

TxGNN 知識圖譜中，Hydroxyurea 與乳癌之間存在多條關聯路徑：

<ol class="actionable-steps">
<li><strong>DNA 合成抑制</strong>：Hydroxyurea 是核糖核苷酸還原酶抑制劑，阻斷 DNA 合成</li>
<li><strong>廣譜抗腫瘤活性</strong>：已被證實對多種實體腫瘤有效（頭頸癌、卵巢癌）</li>
<li><strong>細胞週期阻斷</strong>：阻斷 S 期，與其他化療藥物有協同效應</li>
</ol>

基於這些藥理特性，模型認為 Hydroxyurea 對乳癌有效的可能性極高。

---

## 為什麼證據等級只有 L2？

### 現有臨床證據

| 證據類型 | 數量 | 內容 |
|----------|------|------|
| Phase I/II 試驗 | 數個 | 安全性和初步療效 |
| 體外研究 | 多篇 | 細胞株實驗證實活性 |
| 聯合用藥研究 | 數篇 | 與其他化療藥物併用 |

### 缺少什麼

- **無大型 Phase 3 RCT**：缺乏高品質驗證性試驗
- **非標準治療**：未被納入乳癌治療指引
- **樣本數有限**：現有研究規模較小

---

## 這類案例的價值

<blockquote class="expert-quote">
「高預測分數 + 中低證據等級 = 潛在研究機會。這些案例特別適合學術研究者探索新方向，或藥廠評估再開發價值。」
<cite>— 藥物再利用研究原則</cite>
</blockquote>

### 適合的應用情境

| 角色 | 可能的行動 |
|------|------------|
| **學術研究者** | 以此作為研究假設，申請研究計畫 |
| **藥廠 BD** | 評估專利佈局和競爭格局 |
| **臨床試驗設計** | 考慮納入 Phase II 探索性試驗 |

---

## 對比：高分數 + 高等級 vs 高分數 + 低等級

| 案例 | 預測分數 | 證據等級 | 解讀 |
|------|----------|----------|------|
| Anastrozole | 99.68% | L1 | AI 正確識別已驗證用途 |
| **Hydroxyurea** | **99.97%** | **L2** | **值得研究但尚待驗證** |
| 某 L5 藥物 | 99.5% | L5 | 純粹是研究方向 |

---

## 決策建議解讀

**Proceed with Guardrails** 意思是：

<div style="background: #fff3cd; padding: 1rem; border-radius: 8px; border-left: 4px solid #ffc107; margin: 1rem 0;">
<strong>可以推進，但需要額外保護措施：</strong>
<ul style="margin: 0.5rem 0 0 0;">
<li>需要更多前臨床數據支持</li>
<li>考慮小規模 Phase I/II 試驗</li>
<li>密切監測安全性指標</li>
<li>可能需要 IRB 額外審查</li>
</ul>
</div>

---

## 如果您對這個案例感興趣

<ol class="actionable-steps">
<li>閱讀<a href="/drugs/hydroxyurea/">完整 Hydroxyurea 報告</a>中的文獻清單</li>
<li>查詢 ClinicalTrials.gov 是否有進行中的相關試驗</li>
<li>評估是否有足夠的前臨床數據支持您的研究假設</li>
<li>諮詢專業團隊評估可行性</li>
</ol>

---

## 學習重點

從 Hydroxyurea 案例，我們學到：

1. **預測分數 ≠ 證據等級**：兩者反映不同面向
2. **高分數低等級 = 機會**：代表值得研究但尚未被充分探索
3. **謹慎推進**：有條件推進的決策需要額外保護措施

---

## 延伸閱讀

- [查看完整 Hydroxyurea 報告](/drugs/hydroxyurea/)
- [Anastrozole：高分數高等級案例](/blog/2026/02/22/anastrozole-case-study/)
- [證據等級完整說明](/blog/2026/02/21/evidence-levels-explained/)

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本文僅供研究教學參考，不構成醫療建議。Hydroxyurea 用於乳癌的臨床應用需經過完整驗證。
</div>
