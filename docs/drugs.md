---
layout: default
title: 藥物列表
nav_order: 5
description: "TwTxGNN 所有藥物驗證報告列表"
permalink: /drugs/
---

# 藥物列表
{: .fs-9 }

共 115 種藥物的老藥新用驗證報告
{: .fs-6 .fw-300 }

---

## 快速篩選

| 證據等級 | 報告數 | 連結 |
|---------|-------|------|
| **L1** 強力證據 | 6 | [高證據等級]({{ '/evidence-high' | relative_url }}) |
| **L2** 中等證據 | 11 | [高證據等級]({{ '/evidence-high' | relative_url }}) |
| **L3** 觀察性研究 | 15 | [中證據等級]({{ '/evidence-medium' | relative_url }}) |
| **L4** 前臨床研究 | 19 | [中證據等級]({{ '/evidence-medium' | relative_url }}) |
| **L5** 僅模型預測 | 64 | [僅模型預測]({{ '/evidence-low' | relative_url }}) |

---

## 完整列表

{% assign drugs = site.drugs | sort: 'title' %}

| 藥物名稱 | 證據等級 | 適應症數 | 報告連結 |
|---------|---------|---------|---------|
{% for drug in drugs %}| [{{ drug.title }}]({{ drug.url | relative_url }}) | {{ drug.evidence_level }} | {{ drug.indication_count }} | [藥師報告]({{ drug.url | relative_url }}#pharmacist) |
{% endfor %}

---

## 證據等級說明

| 等級 | 定義 | 臨床意義 |
|-----|------|---------|
| L1 | 多個 Phase 3 RCT / 系統性回顧 | 可支持臨床使用 |
| L2 | 單一 RCT 或多個 Phase 2 試驗 | 可考慮使用 |
| L3 | 觀察性研究 / 大型病例系列 | 待補件後評估 |
| L4 | 前臨床 / 機轉研究 / 個案報告 | 暫不建議 |
| L5 | 僅模型預測，無臨床證據 | 暫不建議 |
