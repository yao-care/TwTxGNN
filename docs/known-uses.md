---
layout: default
title: "僅已知用途（無新預測）"
nav_order: 24
permalink: /known-uses/
description: "這些藥物的 TxGNN 模型候選全部屬於已知用途（已記錄於知識圖譜或藥品許可證），因此目前沒有新的預測適應症。各頁列出已知用途與本地上市狀況。"
---

# 僅已知用途（無新預測）

這些藥物的 TxGNN 模型候選全部屬於已知用途（已記錄於知識圖譜或藥品許可證），因此目前沒有新的預測適應症。各頁列出已知用途與本地上市狀況。

{% assign known_drugs = site.drugs | where: "evidence_level", "N/A" | sort: "title" %}

**{{ known_drugs.size }} 個藥物**

| 藥物 | 報告 |
|------|------|
{% for drug in known_drugs %}| **{{ drug.title }}** | [查看]({{ drug.url | relative_url }}) |
{% endfor %}
