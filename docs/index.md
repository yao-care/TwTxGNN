---
layout: default
title: 首頁
nav_order: 1
description: "TwTxGNN 台灣健保藥品老藥新用驗證報告"
permalink: /
---

# 老藥新用，從數據到證據
{: .fs-9 }

我們用 AI 預測了 **142,328** 個老藥新用候選，並為 **191** 種藥物完成了臨床證據驗證。
{: .fs-6 .fw-300 }

[瀏覽藥物列表]({{ '/drugs/' | relative_url }}){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[了解方法論](#關於本專案){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## 亮點發現

以下是證據最充分的老藥新用案例：

| 藥物 | 證據等級 | 預測適應症 | 說明 |
|------|---------|-----------|------|
| **[Temozolomide]({{ '/drugs/temozolomide/' | relative_url }})** | L1 / Go | 星狀細胞瘤 | 口服腦瘤藥物，能穿透血腦屏障。20+ 篇文獻、2 個臨床試驗支持，已在台灣核准適應症範圍內。 |
| **[Vonoprazan]({{ '/drugs/vonoprazan/' | relative_url }})** | L2 / Strong Proceed | 活動性消化性潰瘍 | 新一代胃藥，抑酸效力是傳統 PPI 的 350 倍。16 篇文獻支持。 |
| **[Icatibant]({{ '/drugs/icatibant/' | relative_url }})** | L1 / Proceed | C1 Inhibitor Deficiency | 罕病藥物新機會，22 項臨床試驗、13 篇文獻支持。 |

---

## 證據等級分布

<style>
.evidence-bar {
  display: flex;
  height: 48px;
  border-radius: 8px;
  overflow: hidden;
  margin: 1.5rem 0;
  font-size: 0.85rem;
}
.bar-segment {
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  transition: all 0.3s ease;
}
.bar-segment:hover {
  filter: brightness(1.1);
}
.l1 { background: #2E7D32; }
.l2 { background: #66BB6A; }
.l3 { background: #FDD835; color: #333; }
.l4 { background: #FB8C00; }
.l5 { background: #9E9E9E; }
</style>

<div class="evidence-bar">
  <a href="{{ '/evidence-high' | relative_url }}" class="bar-segment l1" style="width: 3.1%" title="L1: 6 個藥物">L1: 6</a>
  <a href="{{ '/evidence-high' | relative_url }}" class="bar-segment l2" style="width: 6.3%" title="L2: 12 個藥物">L2: 12</a>
  <a href="{{ '/evidence-medium' | relative_url }}" class="bar-segment l3" style="width: 8.4%" title="L3: 16 個藥物">L3: 16</a>
  <a href="{{ '/evidence-medium' | relative_url }}" class="bar-segment l4" style="width: 9.9%" title="L4: 19 個藥物">L4: 19</a>
  <a href="{{ '/evidence-low' | relative_url }}" class="bar-segment l5" style="width: 72.3%" title="L5: 138 個藥物">L5: 138</a>
</div>

| 等級 | 定義 | 藥物數 |
|:----:|------|:------:|
| **L1** | 多個 Phase 3 RCT / 系統性回顧 | 6 |
| **L2** | 單一 RCT 或多個 Phase 2 試驗 | 12 |
| **L3** | 觀察性研究 / 大型病例系列 | 16 |
| **L4** | 前臨床 / 機轉研究 / 個案報告 | 19 |
| **L5** | 僅模型預測，無臨床證據 | 138 |

---

## 快速導航

| 分類 | 說明 | 連結 |
|------|------|------|
| **高證據等級** | L1-L2，可優先評估 | [查看 18 個藥物]({{ '/evidence-high' | relative_url }}) |
| **中證據等級** | L3-L4，需補充證據 | [查看 35 個藥物]({{ '/evidence-medium' | relative_url }}) |
| **僅模型預測** | L5，研究方向參考 | [查看 138 個藥物]({{ '/evidence-low' | relative_url }}) |
| **完整列表** | 所有 191 個藥物 | [藥物列表]({{ '/drugs/' | relative_url }}) |

---

## 關於本專案

本系統使用 [TxGNN](https://www.nature.com/articles/s41591-023-02233-x) 深度學習模型預測台灣健保藥品的潛在新適應症，並透過自動化流程收集臨床試驗、文獻、安全性等證據，產生結構化的驗證報告。

### 資料規模

| 項目 | 數量 |
|------|------|
| 藥物報告 | 191 份 |
| 老藥新用候選 | 142,328 筆 |
| DDI 資料 | 222,391 筆 |

### 驗證流程

```
TxGNN 預測 → 資料收集 (Bundle) → 證據整理 (Evidence Pack) → 報告產出 (Notes)
```

---

{: .warning }
> **免責聲明**：本報告僅供研究參考，**不構成醫療建議**。任何老藥新用決策需經過完整的臨床驗證與法規審查。
