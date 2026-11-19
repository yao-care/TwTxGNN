---
layout: default
title: 中證據等級 (L3-L4)
parent: 藥物報告
nav_order: 2
has_children: true
description: "本站（台灣）證據等級 L3–L4 的 24 個藥品，例如 Docetaxel, Eltrombopag, Ethynodiol Diacetate；逐藥列出主要預測新適應症、本地藥品許可證張數與查核紀錄。"
permalink: /evidence-medium/
redirect_from:
  - /evidence-medium.html
---

# 中證據等級藥物

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
本頁列出本站 **{{ site.data.drug_stats.total_drugs }}** 個有公開報告的藥品中的 **{{ site.data.evidence_tier_facts.medium.count }}** 個（占 {{ site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%）：L3 **{{ site.data.evidence_tier_facts.medium.by_level.L3 }}**、L4 **{{ site.data.evidence_tier_facts.medium.by_level.L4 }}**。
30 個 TxGNN 站台 L3–L4 占比的中位數為 {{ site.data.evidence_tier_facts.medium.cross.median_share }}%。 {% if ev_share > site.data.evidence_tier_facts.medium.cross.median_share %}本站高於中位數。{% elsif ev_share < site.data.evidence_tier_facts.medium.cross.median_share %}本站低於中位數。{% else %}本站等於中位數。{% endif %}

{% if site.data.evidence_tier_facts.medium.count > 0 %}
本地資料（藥品許可證）中，這些藥有 **{{ site.data.evidence_tier_facts.medium.with_current }}** 個至少有一筆有效資料、**{{ site.data.evidence_tier_facts.medium.none_current }}** 個有資料但沒有有效的、**{{ site.data.evidence_tier_facts.medium.without_data }}** 個不在本地資料裡。 **{{ site.data.evidence_tier_facts.medium.with_reviews }}** 個在查核紀錄有記載（藥物頁上的許可事實更正）。 **{{ site.data.evidence_tier_facts.medium.cross.unique_drugs }}** 個有其他 TxGNN 站台對同一藥品都沒有的預測適應症。
{% if site.data.evidence_tier_facts.medium.none_current_list.size > 0 %}

有資料但沒有有效的：{% for r in site.data.evidence_tier_facts.medium.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}、{% endunless %}{% endfor %}。{% endif %}
{% endif %}

各等級定義見[方法論]({{ '/methodology/' | relative_url }})。
<!-- tier-facts:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
需補充證據後可進一步評估的候選藥物
</p>

---

## 證據標準

| 等級 | 定義 | 臨床意義 |
|------|------|---------|
| **L3** | 觀察性研究 / 大型病例系列 | 有初步證據，待補件後評估 |
| **L4** | 前臨床 / 機轉研究 / 個案報告 | 機轉合理，缺乏臨床驗證 |

---

## 藥物列表

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | sort: "title" %}

### L3 等級 ({{ site.data.evidence_tier_facts.medium.by_level.L3 }} 個)

<!-- tier-table:start L3（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| 藥品 | 等級 | 主要預測新適應症 | 藥品許可證：有效／全部 | 查核紀錄 | 本站獨有 |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L3" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}是 ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L4 等級 ({{ site.data.evidence_tier_facts.medium.by_level.L4 }} 個)

<!-- tier-table:start L4（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| 藥品 | 等級 | 主要預測新適應症 | 藥品許可證：有效／全部 | 查核紀錄 | 本站獨有 |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L4" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}是 ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

