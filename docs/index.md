---
layout: default
title: 老藥新用驗證報告
nav_order: 1
description: "用 AI 預測台灣健保藥品的潛在新適應症，提供 191 個藥物的臨床試驗與文獻證據驗證報告。L1-L5 五級證據分類，從預測到證據一目瞭然。"
permalink: /
image: /assets/images/og-default.png
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

## 藥物查詢

<p class="key-answer" data-question="如何查詢藥物或疾病的老藥新用可能性？">
輸入<strong>藥物名稱</strong>或<strong>疾病名稱</strong>，即可查詢老藥新用的可能性與臨床證據。支援英文學名、中文商品名、疾病關鍵字。
</p>

<div class="drug-lookup-container">
  <div class="lookup-search-box">
    <input type="text" id="lookup-input" placeholder="輸入藥物名稱或疾病名稱..." autocomplete="off">
    <button id="lookup-clear" class="lookup-clear-btn" style="display: none;">✕</button>
  </div>
  <div class="lookup-filters">
    <span class="filter-label">證據等級：</span>
    <label><input type="checkbox" class="level-filter" value="L1" checked> L1</label>
    <label><input type="checkbox" class="level-filter" value="L2" checked> L2</label>
    <label><input type="checkbox" class="level-filter" value="L3" checked> L3</label>
    <label><input type="checkbox" class="level-filter" value="L4"> L4</label>
    <label><input type="checkbox" class="level-filter" value="L5"> L5</label>
  </div>
  <div id="lookup-results" class="lookup-results"></div>
</div>

<script src="https://cdn.jsdelivr.net/npm/fuse.js@7.0.0"></script>
<script>
(function() {
  let searchIndex = null;
  let drugFuse = null;
  let indicationFuse = null;

  // Load search index
  fetch('{{ "/data/search-index.json" | relative_url }}')
    .then(r => r.json())
    .then(data => {
      searchIndex = data;

      // Initialize Fuse.js for drugs
      drugFuse = new Fuse(data.drugs, {
        keys: ['name', 'brands', 'original'],
        threshold: 0.4,
        includeScore: true
      });

      // Initialize Fuse.js for indications
      indicationFuse = new Fuse(data.indications, {
        keys: ['name'],
        threshold: 0.4,
        includeScore: true
      });
    })
    .catch(e => console.error('Failed to load search index:', e));

  const input = document.getElementById('lookup-input');
  const clearBtn = document.getElementById('lookup-clear');
  const results = document.getElementById('lookup-results');
  const levelFilters = document.querySelectorAll('.level-filter');

  function getSelectedLevels() {
    return Array.from(levelFilters)
      .filter(cb => cb.checked)
      .map(cb => cb.value);
  }

  function filterByLevel(items, levels) {
    return items.filter(item => levels.includes(item.level));
  }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  function renderResults(query) {
    if (!searchIndex || !query || query.length < 2) {
      results.innerHTML = '';
      return;
    }

    const levels = getSelectedLevels();
    if (levels.length === 0) {
      results.innerHTML = '<div class="lookup-notice">請至少選擇一個證據等級</div>';
      return;
    }

    let html = '';

    // Search drugs
    const drugResults = drugFuse.search(query).slice(0, 5);
    const filteredDrugs = drugResults.filter(r => levels.includes(r.item.level));

    if (filteredDrugs.length > 0) {
      html += '<div class="result-section"><h4>藥物符合</h4>';
      filteredDrugs.forEach(r => {
        const drug = r.item;
        const brands = drug.brands.length > 0 ? ` (${drug.brands.slice(0, 2).join('、')})` : '';
        const filteredInds = filterByLevel(drug.indications, levels);

        html += `<div class="result-card">
          <div class="result-header">
            <a href="{{ '/drugs/' | relative_url }}${drug.slug}/" class="drug-name">${escapeHtml(drug.name)}${escapeHtml(brands)}</a>
            <span class="level-badge level-${drug.level}">${drug.level}</span>
          </div>
          <div class="result-original">原適應症：${escapeHtml(drug.original) || '—'}</div>
          <div class="result-indications">
            <strong>預測新適應症：</strong>
            ${filteredInds.length > 0 ? filteredInds.slice(0, 5).map(ind =>
              `<span class="ind-item"><span class="level-badge level-${ind.level}">${ind.level}</span> ${escapeHtml(ind.name)} (${ind.score}%)</span>`
            ).join('') : '<span class="no-match">（無符合篩選條件）</span>'}
            ${filteredInds.length > 5 ? `<span class="more">...等 ${filteredInds.length} 個</span>` : ''}
          </div>
          <a href="{{ '/drugs/' | relative_url }}${drug.slug}/" class="view-report">查看完整報告 →</a>
        </div>`;
      });
      html += '</div>';
    }

    // Search indications
    const indResults = indicationFuse.search(query).slice(0, 5);
    const filteredInds = indResults.filter(r => levels.includes(r.item.level));

    if (filteredInds.length > 0) {
      html += '<div class="result-section"><h4>適應症符合</h4>';
      filteredInds.forEach(r => {
        const ind = r.item;
        const filteredDrugs = filterByLevel(ind.drugs, levels);

        html += `<div class="result-card">
          <div class="result-header">
            <span class="indication-name">${escapeHtml(ind.name)}</span>
            <span class="level-badge level-${ind.level}">${ind.level}</span>
          </div>
          <div class="result-drugs">
            <strong>可能有效的藥物（${filteredDrugs.length} 個）：</strong>
            ${filteredDrugs.slice(0, 5).map(d =>
              `<div class="drug-item">
                <a href="{{ '/drugs/' | relative_url }}${d.slug}/">${escapeHtml(d.name)}</a>
                <span class="level-badge level-${d.level}">${d.level}</span>
                <span class="score">${d.score}%</span>
                <span class="original-hint">${escapeHtml(d.original)}</span>
              </div>`
            ).join('')}
            ${filteredDrugs.length > 5 ? `<div class="more">...等 ${filteredDrugs.length} 個藥物</div>` : ''}
          </div>
        </div>`;
      });
      html += '</div>';
    }

    if (!html) {
      html = '<div class="lookup-notice">沒有找到符合條件的結果</div>';
    }

    results.innerHTML = html;
  }

  // Event listeners
  let debounceTimer;
  input.addEventListener('input', function() {
    clearBtn.style.display = this.value ? 'block' : 'none';
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => renderResults(this.value.trim()), 200);
  });

  clearBtn.addEventListener('click', function() {
    input.value = '';
    clearBtn.style.display = 'none';
    results.innerHTML = '';
    input.focus();
  });

  levelFilters.forEach(cb => {
    cb.addEventListener('change', () => renderResults(input.value.trim()));
  });
})();
</script>

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

{% include d3-charts.html %}

---

## 快速導航

| 分類 | 說明 | 連結 |
|------|------|------|
| **高證據等級** | L1-L2，可優先評估 | [查看 18 個藥物]({{ '/evidence-high' | relative_url }}) |
| **中證據等級** | L3-L4，需補充證據 | [查看 35 個藥物]({{ '/evidence-medium' | relative_url }}) |
| **僅模型預測** | L5，研究方向參考 | [查看 138 個藥物]({{ '/evidence-low' | relative_url }}) |
| **完整列表** | 所有 191 個藥物（可搜尋篩選） | [藥物列表]({{ '/drugs/' | relative_url }}) |
| **藥物交互作用** | 222,391 筆 DDI 資料 | [DDI 專區]({{ '/ddi/' | relative_url }}) |
| **研究案例** | 教學與案例解讀 | [研究案例]({{ '/blog/' | relative_url }}) |
| **資料下載** | CSV / JSON 格式 | [下載頁面]({{ '/downloads/' | relative_url }}) |
| **意見回饋** | 回報問題、功能建議 | [GitHub Issues](https://github.com/yao-care/TwTxGNN/issues/new/choose) |
| **討論區** | 藥物討論與問答 | [GitHub Discussions](https://github.com/yao-care/TwTxGNN/discussions) |

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

<style>
.data-source-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1rem;
  margin: 2rem 0;
  padding: 1.5rem;
  background: #f8f9fa;
  border-radius: 12px;
}
.data-source-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.25rem 1rem;
  background: white;
  border-radius: 10px;
  text-decoration: none;
  color: #333;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  transition: transform 0.2s, box-shadow 0.2s;
}
.data-source-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.12);
}
.data-source-icon {
  width: 48px;
  height: 48px;
  margin-bottom: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
  padding: 10px;
}
.data-source-card strong {
  font-size: 0.95rem;
  margin-bottom: 0.25rem;
}
.data-source-card small {
  font-size: 0.75rem;
  color: #666;
  text-align: center;
}
</style>

<div class="data-source-grid">
  <a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #FDE8E8;">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#A51C30" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="3"/>
        <circle cx="12" cy="5" r="1.5"/>
        <circle cx="19" cy="12" r="1.5"/>
        <circle cx="12" cy="19" r="1.5"/>
        <circle cx="5" cy="12" r="1.5"/>
        <line x1="12" y1="9" x2="12" y2="6.5"/>
        <line x1="15" y1="12" x2="17.5" y2="12"/>
        <line x1="12" y1="15" x2="12" y2="17.5"/>
        <line x1="9" y1="12" x2="6.5" y2="12"/>
      </svg>
    </div>
    <strong style="color: #A51C30;">TxGNN</strong>
    <small>Harvard Zitnik Lab</small>
  </a>
  <a href="https://clinicaltrials.gov/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #E8F0F8;">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#205493" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M9 3h6v2H9z"/>
        <path d="M10 5v4"/>
        <path d="M14 5v4"/>
        <path d="M8 9a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2v-8a2 2 0 0 0-2-2H8z"/>
        <circle cx="12" cy="15" r="2"/>
      </svg>
    </div>
    <strong style="color: #205493;">ClinicalTrials.gov</strong>
    <small>NIH 臨床試驗</small>
  </a>
  <a href="https://pubmed.ncbi.nlm.nih.gov/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #E8F0F5;">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#326599" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
        <path d="M4 4.5A2.5 2.5 0 0 1 6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15Z"/>
        <line x1="8" y1="6" x2="16" y2="6"/>
        <line x1="8" y1="10" x2="16" y2="10"/>
        <line x1="8" y1="14" x2="12" y2="14"/>
      </svg>
    </div>
    <strong style="color: #326599;">PubMed</strong>
    <small>生物醫學文獻</small>
  </a>
  <a href="https://go.drugbank.com/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #FDEDEC;">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#E74C3C" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M10.5 2.5a2.5 2.5 0 0 1 3 0l6.5 5.2a2.5 2.5 0 0 1 1 2v4.6a2.5 2.5 0 0 1-1 2l-6.5 5.2a2.5 2.5 0 0 1-3 0l-6.5-5.2a2.5 2.5 0 0 1-1-2V9.7a2.5 2.5 0 0 1 1-2l6.5-5.2z"/>
        <line x1="12" y1="8" x2="12" y2="16"/>
        <line x1="8" y1="12" x2="16" y2="12"/>
      </svg>
    </div>
    <strong style="color: #E74C3C;">DrugBank</strong>
    <small>藥物資料庫</small>
  </a>
  <a href="https://data.fda.gov.tw/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #E8F8EE;">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#00A651" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 2L4 6v6c0 5.5 3.4 10.3 8 12 4.6-1.7 8-6.5 8-12V6l-8-4z"/>
        <polyline points="9 12 11 14 15 10"/>
      </svg>
    </div>
    <strong style="color: #00A651;">TFDA</strong>
    <small>衛福部食藥署</small>
  </a>
  <a href="https://ddinter2.scbdd.com/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #F5EEF8;">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#9B59B6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="7" cy="12" r="3"/>
        <circle cx="17" cy="12" r="3"/>
        <line x1="10" y1="12" x2="14" y2="12"/>
        <path d="M7 9V6"/>
        <path d="M7 18v-3"/>
        <path d="M17 9V6"/>
        <path d="M17 18v-3"/>
      </svg>
    </div>
    <strong style="color: #9B59B6;">DDInter</strong>
    <small>藥物交互作用</small>
  </a>
</div>

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>最後審核：2026-02-19 | 審核者：TwTxGNN Research Team</small>
</div>
