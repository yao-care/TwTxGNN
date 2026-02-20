---
layout: default
title: 研究案例
nav_order: 10
description: "TwTxGNN 研究案例解讀與使用教學，了解 AI 預測如何驗證臨床證據，以及如何正確閱讀老藥新用驗證報告。"
permalink: /blog/
---

# 研究案例與教學

<p class="key-answer" data-question="如何從 TwTxGNN 報告中學習？">
透過真實案例解讀，了解 AI 預測如何與臨床證據相互驗證，以及如何評估老藥新用的可行性。這些教學內容將幫助您更有效地使用 TwTxGNN 平台。
</p>

<div class="key-takeaway">
從 L1 高證據案例學習「什麼是好的預測」，從 L2 案例理解「預測分數與證據等級的差異」。
</div>

---

## 精選案例解讀

### L1 證據等級案例（最高證據）

這些案例展示了 AI 預測如何與充分的臨床證據相互驗證。

| 藥物 | 主題 | 關鍵學習 |
|------|------|----------|
{% for post in site.posts %}{% if post.categories contains 'L1' %}| [{{ post.drugs | default: post.title | split: '：' | last }}]({{ post.url | relative_url }}) | {{ post.title | split: '：' | first }} | {{ post.summary | default: post.description | truncate: 40 }} |
{% endif %}{% endfor %}

### L2 證據等級案例

這些案例幫助理解預測分數與證據等級的差異。

| 藥物 | 主題 | 關鍵學習 |
|------|------|----------|
{% for post in site.posts %}{% if post.categories contains 'L2' %}| [{{ post.drugs | default: post.title | split: '：' | last }}]({{ post.url | relative_url }}) | {{ post.title | split: '：' | first }} | {{ post.summary | default: post.description | truncate: 40 }} |
{% endif %}{% endfor %}

### 使用教學

| 主題 | 說明 |
|------|------|
{% for post in site.posts %}{% if post.categories contains '教學' %}| [{{ post.title }}]({{ post.url | relative_url }}) | {{ post.description | truncate: 60 }} |
{% endif %}{% endfor %}

---

## 最新文章

{% if site.posts.size > 0 %}
{% for post in site.posts limit:5 %}
<article style="margin-bottom: 1.5rem; padding: 1.25rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid {% if post.categories contains 'L1' %}#2E7D32{% elsif post.categories contains 'L2' %}#66BB6A{% elsif post.categories contains '教學' %}#1976D2{% else %}#9E9E9E{% endif %};">
  <h3 style="margin: 0 0 0.5rem 0; font-size: 1.1rem;">
    <a href="{{ post.url | relative_url }}" style="text-decoration: none; color: #333;">{{ post.title }}</a>
  </h3>
  <p style="color: #666; margin: 0; font-size: 0.9rem;">
    <span style="background: {% if post.categories contains 'L1' %}#e8f5e9{% elsif post.categories contains 'L2' %}#e8f5e9{% elsif post.categories contains '教學' %}#e3f2fd{% else %}#f5f5f5{% endif %}; padding: 0.15rem 0.5rem; border-radius: 4px; font-size: 0.8rem; margin-right: 0.5rem;">{{ post.categories | first }}</span>
    {{ post.date | date: "%Y-%m-%d" }} | {{ post.description | truncate: 80 }}
  </p>
</article>
{% endfor %}
{% else %}
<p style="color: #666; font-style: italic;">即將推出更多案例解讀與教學文章...</p>
{% endif %}

---

## 所有文章

{% if site.posts.size > 0 %}
| 日期 | 類型 | 標題 |
|------|------|------|
{% for post in site.posts %}| {{ post.date | date: "%Y-%m-%d" }} | {{ post.categories | first }} | [{{ post.title }}]({{ post.url | relative_url }}) |
{% endfor %}
{% else %}
*文章即將推出*
{% endif %}

---

## 快速連結

| 資源 | 說明 |
|------|------|
| [使用指南]({{ '/guide/' | relative_url }}) | 報告結構詳細說明 |
| [方法論]({{ '/methodology/' | relative_url }}) | 預測與驗證流程 |
| [高證據藥物]({{ '/evidence-high/' | relative_url }}) | L1-L2 藥物列表 |

---

<div class="disclaimer">
<strong>提醒</strong><br>
案例解讀僅供學術研究參考，不構成醫療建議。實際用藥決策請諮詢專業醫療人員。
</div>
