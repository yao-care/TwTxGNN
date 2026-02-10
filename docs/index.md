---
layout: default
title: 首頁
nav_order: 1
description: "TwTxGNN 台灣健保藥品老藥新用驗證報告"
permalink: /
---

# TwTxGNN 老藥新用驗證報告
{: .fs-9 }

基於 TxGNN 知識圖譜的台灣健保藥品 Drug Repurposing 預測與驗證系統
{: .fs-6 .fw-300 }

---

## 專案概述

本系統使用 TxGNN 深度學習模型預測台灣健保藥品的潛在新適應症，並透過自動化流程收集臨床試驗、文獻、安全性等證據，產生結構化的驗證報告。

### 驗證流程

```
TxGNN 預測 → 資料收集 (Bundle) → 證據整理 (Evidence Pack) → 報告產出 (Notes)
```

### 報告類型

| 報告類型 | 目標讀者 | 內容重點 |
|---------|---------|---------|
| **藥師評估報告** | 臨床藥師 | 安全性、DDI、監測計畫 |
| **贊助商報告** | 藥廠/研究者 | 商業潛力、法規路徑 |

---

## 藥物列表

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

---

## 免責聲明

{: .warning }
> 本報告僅供研究參考，**不構成醫療建議**。
> 任何老藥新用決策需經過完整的臨床驗證與法規審查。
