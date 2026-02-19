---
layout: default
title: 首頁
nav_order: 1
description: "用 AI 預測台灣健保藥品的潛在新適應症，提供 191 個藥物的臨床試驗與文獻證據驗證報告。L1-L5 五級證據分類，從預測到證據一目瞭然。"
permalink: /
---

# 老藥新用，從數據到證據

**不只告訴你「可能有效」，還告訴你「證據在哪裡」**

我們用 AI 預測了 **142,328** 個老藥新用候選，並為 **191** 種藥物完成了臨床證據驗證。

<p style="margin-top: 1.5rem;">
  <a href="{{ '/evidence-high' | relative_url }}" style="display: inline-block; padding: 0.75rem 1.5rem; background: #2E7D32; color: white; text-decoration: none; border-radius: 4px; font-weight: 600; margin-right: 0.5rem;">瀏覽高證據藥物</a>
  <a href="{{ '/methodology' | relative_url }}" style="display: inline-block; padding: 0.75rem 1.5rem; background: #f5f5f5; color: #333; text-decoration: none; border-radius: 4px; font-weight: 500;">了解方法論</a>
</p>

---

## 我們的差異化

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px;">
    <strong style="font-size: 1.1rem;">AI 預測 + 證據驗證</strong><br>
    <span style="color: #666;">使用哈佛 TxGNN 模型預測，並整合 ClinicalTrials.gov 和 PubMed 證據</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px;">
    <strong style="font-size: 1.1rem;">五級證據分類</strong><br>
    <span style="color: #666;">L1-L5 證據等級，從臨床試驗到僅模型預測，一目瞭然</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px;">
    <strong style="font-size: 1.1rem;">台灣健保藥品</strong><br>
    <span style="color: #666;">聚焦 TFDA 核准藥品，具有在地研究實用性</span>
  </div>
</div>

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

[了解更多]({{ '/about' | relative_url }}) | [查看方法論]({{ '/methodology' | relative_url }}) | [資料來源]({{ '/sources' | relative_url }})

---

<div style="background: #fff3cd; padding: 1rem; margin-top: 2rem; border-left: 4px solid #ffc107; border-radius: 4px;">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
</div>
