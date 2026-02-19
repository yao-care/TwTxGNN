---
layout: default
title: 首頁
nav_order: 1
description: "用 AI 預測台灣健保藥品的潛在新適應症，提供 191 個藥物的臨床試驗與文獻證據驗證報告。L1-L5 五級證據分類，從預測到證據一目瞭然。"
permalink: /
---

# 老藥新用，從數據到證據

<p class="key-answer" data-question="什麼是 TwTxGNN 老藥新用驗證報告？">
<strong>TwTxGNN</strong> 是基於哈佛 TxGNN 模型的老藥新用預測平台。我們用 AI 預測了 <strong>142,328</strong> 個老藥新用候選，並為 <strong>191</strong> 種台灣健保藥物完成臨床證據驗證，提供從預測到證據的完整報告。
</p>

<div class="key-takeaway">
不只告訴你「可能有效」，還告訴你「證據在哪裡」。L1-L5 五級證據分類，讓研究人員快速評估預測的可信度。
</div>

<p style="margin-top: 1.5rem;">
  <a href="{{ '/evidence-high' | relative_url }}" style="display: inline-block; padding: 0.75rem 1.5rem; background: #2E7D32; color: white; text-decoration: none; border-radius: 4px; font-weight: 600; margin-right: 0.5rem;">瀏覽高證據藥物</a>
  <a href="{{ '/methodology' | relative_url }}" style="display: inline-block; padding: 0.75rem 1.5rem; background: #f5f5f5; color: #333; text-decoration: none; border-radius: 4px; font-weight: 500;">了解方法論</a>
</p>

---

## 我們的差異化

<p class="key-answer" data-question="TwTxGNN 和其他預測工具有什麼不同？">
TwTxGNN 不只提供 AI 預測分數，更整合多來源臨床證據，讓研究人員能快速評估預測的可信度。
</p>

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

<p class="key-answer" data-question="目前證據最充分的老藥新用案例有哪些？">
以下是經過臨床證據驗證、證據等級達 L1-L2 的老藥新用案例，可優先考慮進入臨床評估：
</p>

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

/* Donut Chart Styles */
.chart-container {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  align-items: center;
  justify-content: center;
  margin: 2rem 0;
}
.donut-chart {
  position: relative;
  width: 200px;
  height: 200px;
}
.donut-chart svg {
  transform: rotate(-90deg);
}
.donut-segment {
  fill: none;
  stroke-width: 40;
  transition: stroke-width 0.3s ease;
  cursor: pointer;
}
.donut-segment:hover {
  stroke-width: 45;
}
.donut-center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}
.donut-center .number {
  font-size: 2.5rem;
  font-weight: 700;
  color: #333;
  line-height: 1;
}
.donut-center .label {
  font-size: 0.9rem;
  color: #666;
}
.chart-legend {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}
.legend-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem 1rem;
  background: #f8f9fa;
  border-radius: 8px;
  text-decoration: none;
  color: #333;
  transition: transform 0.2s, box-shadow 0.2s;
}
.legend-item:hover {
  transform: translateX(4px);
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
.legend-color {
  width: 16px;
  height: 16px;
  border-radius: 4px;
}
.legend-text {
  flex: 1;
}
.legend-count {
  font-weight: 700;
  font-size: 1.1rem;
}
</style>

<div class="chart-container">
  <div class="donut-chart">
    <svg viewBox="0 0 200 200">
      <!-- L5: 138/191 = 72.3% -->
      <circle class="donut-segment" cx="100" cy="100" r="80" stroke="#9E9E9E" stroke-dasharray="362.7 502.65" stroke-dashoffset="0" onclick="location.href='{{ '/evidence-low' | relative_url }}'"/>
      <!-- L4: 19/191 = 9.9% -->
      <circle class="donut-segment" cx="100" cy="100" r="80" stroke="#FB8C00" stroke-dasharray="49.7 502.65" stroke-dashoffset="-362.7" onclick="location.href='{{ '/evidence-medium' | relative_url }}'"/>
      <!-- L3: 16/191 = 8.4% -->
      <circle class="donut-segment" cx="100" cy="100" r="80" stroke="#FDD835" stroke-dasharray="42.1 502.65" stroke-dashoffset="-412.4" onclick="location.href='{{ '/evidence-medium' | relative_url }}'"/>
      <!-- L2: 12/191 = 6.3% -->
      <circle class="donut-segment" cx="100" cy="100" r="80" stroke="#66BB6A" stroke-dasharray="31.6 502.65" stroke-dashoffset="-454.5" onclick="location.href='{{ '/evidence-high' | relative_url }}'"/>
      <!-- L1: 6/191 = 3.1% -->
      <circle class="donut-segment" cx="100" cy="100" r="80" stroke="#2E7D32" stroke-dasharray="15.6 502.65" stroke-dashoffset="-486.1" onclick="location.href='{{ '/evidence-high' | relative_url }}'"/>
    </svg>
    <div class="donut-center">
      <div class="number">191</div>
      <div class="label">藥物報告</div>
    </div>
  </div>

  <div class="chart-legend">
    <a href="{{ '/evidence-high' | relative_url }}" class="legend-item">
      <span class="legend-color" style="background: #2E7D32;"></span>
      <span class="legend-text">L1 多個 Phase 3 RCT</span>
      <span class="legend-count">6</span>
    </a>
    <a href="{{ '/evidence-high' | relative_url }}" class="legend-item">
      <span class="legend-color" style="background: #66BB6A;"></span>
      <span class="legend-text">L2 單一 RCT / Phase 2</span>
      <span class="legend-count">12</span>
    </a>
    <a href="{{ '/evidence-medium' | relative_url }}" class="legend-item">
      <span class="legend-color" style="background: #FDD835;"></span>
      <span class="legend-text">L3 觀察性研究</span>
      <span class="legend-count">16</span>
    </a>
    <a href="{{ '/evidence-medium' | relative_url }}" class="legend-item">
      <span class="legend-color" style="background: #FB8C00;"></span>
      <span class="legend-text">L4 前臨床 / 機轉研究</span>
      <span class="legend-count">19</span>
    </a>
    <a href="{{ '/evidence-low' | relative_url }}" class="legend-item">
      <span class="legend-color" style="background: #9E9E9E;"></span>
      <span class="legend-text">L5 僅模型預測</span>
      <span class="legend-count">138</span>
    </a>
  </div>
</div>

<div class="evidence-bar">
  <a href="{{ '/evidence-high' | relative_url }}" class="bar-segment l1" style="width: 3.1%" title="L1: 6 個藥物">L1</a>
  <a href="{{ '/evidence-high' | relative_url }}" class="bar-segment l2" style="width: 6.3%" title="L2: 12 個藥物">L2</a>
  <a href="{{ '/evidence-medium' | relative_url }}" class="bar-segment l3" style="width: 8.4%" title="L3: 16 個藥物">L3</a>
  <a href="{{ '/evidence-medium' | relative_url }}" class="bar-segment l4" style="width: 9.9%" title="L4: 19 個藥物">L4</a>
  <a href="{{ '/evidence-low' | relative_url }}" class="bar-segment l5" style="width: 72.3%" title="L5: 138 個藥物">L5: 138</a>
</div>

---

## 快速導航

| 分類 | 說明 | 連結 |
|------|------|------|
| **高證據等級** | L1-L2，可優先評估 | [查看 18 個藥物]({{ '/evidence-high' | relative_url }}) |
| **中證據等級** | L3-L4，需補充證據 | [查看 35 個藥物]({{ '/evidence-medium' | relative_url }}) |
| **僅模型預測** | L5，研究方向參考 | [查看 138 個藥物]({{ '/evidence-low' | relative_url }}) |
| **完整列表** | 所有 191 個藥物（可搜尋篩選） | [藥物列表]({{ '/drugs/' | relative_url }}) |
| **資料下載** | CSV / JSON 格式 | [下載頁面]({{ '/downloads/' | relative_url }}) |

---

## 關於本專案

<p class="key-answer" data-question="TwTxGNN 使用什麼技術進行預測？">
本系統使用哈佛大學 Zitnik Lab 發表於 <em>Nature Medicine</em> 的 <a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a> 深度學習模型，預測台灣健保藥品的潛在新適應症，並透過自動化流程收集臨床試驗、文獻、安全性等證據，產生結構化的驗證報告。
</p>

<blockquote class="expert-quote">
「TxGNN 是首個專為臨床醫師設計的老藥新用基礎模型，整合知識圖譜與深度學習，能預測藥物對罕見疾病的潛在療效。」
<cite>— Huang et al., Nature Medicine (2023)</cite>
</blockquote>

### 資料規模

| 項目 | 數量 |
|------|------|
| 藥物報告 | 191 份 |
| 老藥新用候選 | 142,328 筆 |
| DDI 資料 | 222,391 筆 |

### 驗證流程

<ol class="actionable-steps">
<li><strong>TxGNN 預測</strong>：使用知識圖譜與深度學習預測藥物-疾病關係</li>
<li><strong>資料收集 (Bundle)</strong>：自動收集 ClinicalTrials.gov、PubMed 等來源的證據</li>
<li><strong>證據整理 (Evidence Pack)</strong>：判定 L1-L5 證據等級</li>
<li><strong>報告產出 (Notes)</strong>：產生結構化的驗證報告</li>
</ol>

[了解更多]({{ '/about' | relative_url }}) | [查看方法論]({{ '/methodology' | relative_url }}) | [資料來源]({{ '/sources' | relative_url }})

---

## 資料來源與合作夥伴

<p class="key-answer" data-question="TwTxGNN 的資料來源有哪些？">
本平台整合多個權威公開資料來源，確保預測結果具有可追溯性與學術價值。
</p>

<div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; align-items: center; margin: 2rem 0; padding: 1.5rem; background: #f8f9fa; border-radius: 12px;">
  <a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/" target="_blank" rel="noopener" style="display: flex; flex-direction: column; align-items: center; padding: 1rem 1.5rem; background: white; border-radius: 8px; text-decoration: none; color: #333; box-shadow: 0 2px 4px rgba(0,0,0,0.1); transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'">
    <strong style="font-size: 1.1rem; color: #A51C30;">TxGNN</strong>
    <small style="color: #666;">Harvard Zitnik Lab</small>
  </a>
  <a href="https://clinicaltrials.gov/" target="_blank" rel="noopener" style="display: flex; flex-direction: column; align-items: center; padding: 1rem 1.5rem; background: white; border-radius: 8px; text-decoration: none; color: #333; box-shadow: 0 2px 4px rgba(0,0,0,0.1); transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'">
    <strong style="font-size: 1.1rem; color: #205493;">ClinicalTrials.gov</strong>
    <small style="color: #666;">NIH 臨床試驗</small>
  </a>
  <a href="https://pubmed.ncbi.nlm.nih.gov/" target="_blank" rel="noopener" style="display: flex; flex-direction: column; align-items: center; padding: 1rem 1.5rem; background: white; border-radius: 8px; text-decoration: none; color: #333; box-shadow: 0 2px 4px rgba(0,0,0,0.1); transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'">
    <strong style="font-size: 1.1rem; color: #326599;">PubMed</strong>
    <small style="color: #666;">生物醫學文獻</small>
  </a>
  <a href="https://go.drugbank.com/" target="_blank" rel="noopener" style="display: flex; flex-direction: column; align-items: center; padding: 1rem 1.5rem; background: white; border-radius: 8px; text-decoration: none; color: #333; box-shadow: 0 2px 4px rgba(0,0,0,0.1); transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'">
    <strong style="font-size: 1.1rem; color: #E74C3C;">DrugBank</strong>
    <small style="color: #666;">藥物資料庫</small>
  </a>
  <a href="https://data.fda.gov.tw/" target="_blank" rel="noopener" style="display: flex; flex-direction: column; align-items: center; padding: 1rem 1.5rem; background: white; border-radius: 8px; text-decoration: none; color: #333; box-shadow: 0 2px 4px rgba(0,0,0,0.1); transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'">
    <strong style="font-size: 1.1rem; color: #00A651;">TFDA</strong>
    <small style="color: #666;">衛福部食藥署</small>
  </a>
  <a href="https://ddinter2.scbdd.com/" target="_blank" rel="noopener" style="display: flex; flex-direction: column; align-items: center; padding: 1rem 1.5rem; background: white; border-radius: 8px; text-decoration: none; color: #333; box-shadow: 0 2px 4px rgba(0,0,0,0.1); transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'">
    <strong style="font-size: 1.1rem; color: #9B59B6;">DDInter</strong>
    <small style="color: #666;">藥物交互作用</small>
  </a>
</div>

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>最後審核：2026-02-19 | 審核者：TwTxGNN Research Team</small>
</div>
