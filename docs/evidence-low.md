---
layout: default
title: 僅模型預測 (L5)
nav_order: 4
has_children: true
description: "L5 等級的老藥新用候選藥物，目前僅有 AI 模型預測，尚無臨床證據，可作為研究方向參考。"
---

# 僅模型預測藥物
{: .fs-9 }

TxGNN 模型預測但尚無臨床證據支持的候選藥物
{: .fs-6 .fw-300 }

---

## 證據標準

| 等級 | 定義 | 臨床意義 |
|------|------|---------|
| **L5** | 僅模型預測，無臨床證據 | 可作為研究假設，需進一步驗證 |

{: .warning }
> L5 等級藥物僅基於知識圖譜預測，尚無直接臨床證據支持。
> 不建議直接用於臨床決策，可作為研究方向參考。

---

## 藥物列表

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | sort: "title" %}

### L5 等級 ({{ l5_drugs.size }} 個)

| 藥物名稱 | 適應症數 | 連結 |
|---------|---------|------|
{% for drug in l5_drugs %}| {{ drug.title }} | {{ drug.indication_count }} | [查看報告]({{ drug.url | relative_url }}) |
{% endfor %}
