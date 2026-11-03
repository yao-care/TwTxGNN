---
layout: default
title: "僅已知用途／主預測已撤回"
nav_order: 24
permalink: /known-uses/
description: "兩類藥物：TxGNN 模型候選全部屬於已知用途、目前沒有新的預測適應症；或主預測經人工重審確認為已核准用途而撤回、不列證據等級。各頁列出已知用途與本地上市狀況。"
---

# 僅已知用途／主預測已撤回

本頁列出兩類藥物，頁首證據等級都標為 N/A：

- **僅已知用途**：TxGNN 模型候選全部屬於已知用途（已記錄於知識圖譜或藥品許可證），因此目前沒有新的預測適應症。
- **主預測已撤回**：報告快速總覽的主預測經人工重審，確認是任一國官方仿單或許可證已核准的用途（不是新適應症）而撤回；頁面保留模型預測原文與查核紀錄，其餘模型預測未經證據評估，不列證據等級。

各頁列出已知用途與本地上市狀況。

{% assign known_drugs = site.drugs | where: "evidence_level", "N/A" | sort: "title" %}
{% assign withdrawn_files = site.data.drug_reviews.records | where: "action", "header_level" | where: "trigger", "withdraw" | where: "new_level", "N/A" | map: "file" %}

**{{ known_drugs.size }} 個藥物**

| 藥物 | 類別 | 報告 |
|------|------|------|
{% for drug in known_drugs %}{% assign fname = drug.relative_path | split: "/" | last %}| **{{ drug.title }}** | {% if withdrawn_files contains fname %}主預測已撤回{% else %}僅已知用途{% endif %} | [查看]({{ drug.url | relative_url }}) |
{% endfor %}
