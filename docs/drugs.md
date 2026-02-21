---
layout: default
title: 藥物列表
parent: 藥物報告
nav_order: 4
description: "TwTxGNN 所有藥物驗證報告列表，支援證據等級篩選和關鍵字搜尋。"
permalink: /drugs/
---

# 藥物列表

共 191 種藥物的老藥新用驗證報告

---

## 進階篩選

<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; margin-bottom: 1.5rem;">
  <!-- 第一行：搜尋和證據等級 -->
  <div style="display: flex; flex-wrap: wrap; gap: 1rem; align-items: center;">
    <div>
      <label for="search-input" style="font-weight: 600; margin-right: 0.5rem;">搜尋：</label>
      <input type="text" id="search-input" placeholder="輸入藥物名稱..." style="padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px; width: 200px;">
    </div>
    <div>
      <label style="font-weight: 600; margin-right: 0.5rem;">證據等級：</label>
      <label style="margin-right: 0.5rem;"><input type="checkbox" class="level-filter" value="L1" checked> L1</label>
      <label style="margin-right: 0.5rem;"><input type="checkbox" class="level-filter" value="L2" checked> L2</label>
      <label style="margin-right: 0.5rem;"><input type="checkbox" class="level-filter" value="L3" checked> L3</label>
      <label style="margin-right: 0.5rem;"><input type="checkbox" class="level-filter" value="L4" checked> L4</label>
      <label style="margin-right: 0.5rem;"><input type="checkbox" class="level-filter" value="L5" checked> L5</label>
    </div>
  </div>

  <!-- 第二行：適應症數量和快速篩選 -->
  <div style="display: flex; flex-wrap: wrap; gap: 1rem; align-items: center; margin-top: 1rem;">
    <div>
      <label for="indication-filter" style="font-weight: 600; margin-right: 0.5rem;">適應症數：</label>
      <select id="indication-filter" style="padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;">
        <option value="all">全部</option>
        <option value="10+">10+ 個</option>
        <option value="5-9">5-9 個</option>
        <option value="1-4">1-4 個</option>
      </select>
    </div>
    <div>
      <label style="font-weight: 600; margin-right: 0.5rem;">快速篩選：</label>
      <button class="quick-filter-btn" data-filter="high" style="padding: 0.4rem 0.8rem; background: #2E7D32; color: white; border: none; border-radius: 4px; cursor: pointer; margin-right: 0.25rem;">高證據 (L1-L2)</button>
      <button class="quick-filter-btn" data-filter="medium" style="padding: 0.4rem 0.8rem; background: #FB8C00; color: white; border: none; border-radius: 4px; cursor: pointer; margin-right: 0.25rem;">中證據 (L3-L4)</button>
      <button class="quick-filter-btn" data-filter="multi" style="padding: 0.4rem 0.8rem; background: #1976D2; color: white; border: none; border-radius: 4px; cursor: pointer;">多適應症 (5+)</button>
    </div>
    <div>
      <button id="reset-filters" style="padding: 0.5rem 1rem; background: #6c757d; color: white; border: none; border-radius: 4px; cursor: pointer;">重置全部</button>
    </div>
  </div>

  <!-- 結果統計 -->
  <div style="margin-top: 1rem; padding-top: 0.75rem; border-top: 1px solid #e0e0e0; font-size: 0.9rem; color: #666;">
    顯示 <strong id="filtered-count">191</strong> / 191 個藥物
    <span id="filter-summary" style="margin-left: 1rem;"></span>
  </div>
</div>

---

## 藥物清單

<table id="drugs-table">
  <thead>
    <tr>
      <th style="cursor: pointer;" onclick="sortTable(0)">藥物名稱 ↕</th>
      <th style="cursor: pointer;" onclick="sortTable(1)">證據等級 ↕</th>
      <th style="cursor: pointer;" onclick="sortTable(2)">適應症數 ↕</th>
      <th>報告連結</th>
    </tr>
  </thead>
  <tbody>
{% assign drugs = site.drugs | sort: 'title' %}
{% for drug in drugs %}
    <tr data-level="{{ drug.evidence_level }}" data-name="{{ drug.title | downcase }}">
      <td><a href="{{ drug.url | relative_url }}">{{ drug.title }}</a></td>
      <td><span class="level-badge level-{{ drug.evidence_level | downcase }}">{{ drug.evidence_level }}</span></td>
      <td>{{ drug.indication_count }}</td>
      <td><a href="{{ drug.url | relative_url }}#pharmacist">藥師報告</a></td>
    </tr>
{% endfor %}
  </tbody>
</table>

<style>
.level-badge {
  display: inline-block;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-weight: 600;
  font-size: 0.85rem;
}
.level-l1 { background: #2E7D32; color: white; }
.level-l2 { background: #66BB6A; color: white; }
.level-l3 { background: #FDD835; color: #333; }
.level-l4 { background: #FB8C00; color: white; }
.level-l5 { background: #9E9E9E; color: white; }

#drugs-table {
  width: 100%;
  border-collapse: collapse;
}
#drugs-table th, #drugs-table td {
  padding: 0.75rem;
  text-align: left;
  border-bottom: 1px solid #ddd;
}
#drugs-table th {
  background: #f5f5f5;
  font-weight: 600;
}
#drugs-table tr:hover {
  background: #f8f9fa;
}
#drugs-table tr.hidden {
  display: none;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('search-input');
  const levelFilters = document.querySelectorAll('.level-filter');
  const indicationFilter = document.getElementById('indication-filter');
  const quickFilterBtns = document.querySelectorAll('.quick-filter-btn');
  const resetBtn = document.getElementById('reset-filters');
  const filteredCount = document.getElementById('filtered-count');
  const filterSummary = document.getElementById('filter-summary');
  const tableRows = document.querySelectorAll('#drugs-table tbody tr');

  // 從 URL hash 載入篩選條件
  function loadFiltersFromHash() {
    const hash = window.location.hash.substring(1);
    if (!hash) return;

    const params = new URLSearchParams(hash);

    if (params.has('search')) {
      searchInput.value = params.get('search');
    }
    if (params.has('levels')) {
      const levels = params.get('levels').split(',');
      levelFilters.forEach(cb => {
        cb.checked = levels.includes(cb.value);
      });
    }
    if (params.has('indication')) {
      indicationFilter.value = params.get('indication');
    }
  }

  // 儲存篩選條件到 URL hash
  function saveFiltersToHash() {
    const params = new URLSearchParams();

    if (searchInput.value) {
      params.set('search', searchInput.value);
    }

    const selectedLevels = Array.from(levelFilters).filter(cb => cb.checked).map(cb => cb.value);
    if (selectedLevels.length < 5) {
      params.set('levels', selectedLevels.join(','));
    }

    if (indicationFilter.value !== 'all') {
      params.set('indication', indicationFilter.value);
    }

    const hashString = params.toString();
    if (hashString) {
      history.replaceState(null, '', '#' + hashString);
    } else {
      history.replaceState(null, '', window.location.pathname);
    }
  }

  function applyFilters() {
    const searchTerm = searchInput.value.toLowerCase();
    const selectedLevels = Array.from(levelFilters)
      .filter(cb => cb.checked)
      .map(cb => cb.value);
    const indicationRange = indicationFilter.value;

    let visibleCount = 0;
    const summaryParts = [];

    tableRows.forEach(row => {
      const name = row.dataset.name;
      const level = row.dataset.level;
      const indicationCount = parseInt(row.cells[2].textContent.trim()) || 0;

      const matchesSearch = name.includes(searchTerm);
      const matchesLevel = selectedLevels.includes(level);

      let matchesIndication = true;
      if (indicationRange === '10+') {
        matchesIndication = indicationCount >= 10;
      } else if (indicationRange === '5-9') {
        matchesIndication = indicationCount >= 5 && indicationCount <= 9;
      } else if (indicationRange === '1-4') {
        matchesIndication = indicationCount >= 1 && indicationCount <= 4;
      }

      if (matchesSearch && matchesLevel && matchesIndication) {
        row.classList.remove('hidden');
        visibleCount++;
      } else {
        row.classList.add('hidden');
      }
    });

    // 更新篩選摘要
    if (searchTerm) summaryParts.push('搜尋: "' + searchTerm + '"');
    if (selectedLevels.length < 5) summaryParts.push('等級: ' + selectedLevels.join(', '));
    if (indicationRange !== 'all') summaryParts.push('適應症: ' + indicationRange);

    filteredCount.textContent = visibleCount;
    filterSummary.textContent = summaryParts.length > 0 ? '(' + summaryParts.join(' | ') + ')' : '';

    saveFiltersToHash();
  }

  // 快速篩選按鈕
  quickFilterBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      const filter = this.dataset.filter;

      if (filter === 'high') {
        levelFilters.forEach(cb => {
          cb.checked = ['L1', 'L2'].includes(cb.value);
        });
        indicationFilter.value = 'all';
      } else if (filter === 'medium') {
        levelFilters.forEach(cb => {
          cb.checked = ['L3', 'L4'].includes(cb.value);
        });
        indicationFilter.value = 'all';
      } else if (filter === 'multi') {
        levelFilters.forEach(cb => cb.checked = true);
        indicationFilter.value = '5-9';
        // 也包含 10+
        const indicationCount = indicationFilter.value;
      }

      // 高亮選中的按鈕
      quickFilterBtns.forEach(b => b.style.opacity = '0.6');
      this.style.opacity = '1';

      applyFilters();
    });
  });

  searchInput.addEventListener('input', applyFilters);
  levelFilters.forEach(cb => cb.addEventListener('change', applyFilters));
  indicationFilter.addEventListener('change', applyFilters);

  resetBtn.addEventListener('click', function() {
    searchInput.value = '';
    levelFilters.forEach(cb => cb.checked = true);
    indicationFilter.value = 'all';
    quickFilterBtns.forEach(b => b.style.opacity = '1');
    applyFilters();
  });

  // 載入 URL hash 的篩選條件
  loadFiltersFromHash();
  applyFilters();
});

let sortDirection = {};
function sortTable(columnIndex) {
  const table = document.getElementById('drugs-table');
  const tbody = table.querySelector('tbody');
  const rows = Array.from(tbody.querySelectorAll('tr'));
  const headers = table.querySelectorAll('th');

  sortDirection[columnIndex] = !sortDirection[columnIndex];
  const dir = sortDirection[columnIndex] ? 1 : -1;

  rows.sort((a, b) => {
    let aVal = a.cells[columnIndex].textContent.trim();
    let bVal = b.cells[columnIndex].textContent.trim();

    // 數字排序
    if (columnIndex === 2) {
      return (parseInt(aVal) - parseInt(bVal)) * dir;
    }

    return aVal.localeCompare(bVal) * dir;
  });

  rows.forEach(row => tbody.appendChild(row));

  // 更新排序箭頭
  headers.forEach((h, i) => {
    let text = h.textContent.replace(/ [↕▲▼]$/, '');
    if (i === columnIndex) {
      text += sortDirection[columnIndex] ? ' ▲' : ' ▼';
    } else if (i < 3) {
      text += ' ↕';
    }
    h.textContent = text;
  });
}
</script>

---

## 快速導航

| 證據等級 | 報告數 | 說明 | 連結 |
|---------|-------|------|------|
| **L1-L2** | 18 | 可優先評估 | [高證據等級]({{ '/evidence-high' | relative_url }}) |
| **L3-L4** | 35 | 需補充證據 | [中證據等級]({{ '/evidence-medium' | relative_url }}) |
| **L5** | 138 | 研究方向參考 | [僅模型預測]({{ '/evidence-low' | relative_url }}) |

---

## 資料下載

需要完整資料集？

| 格式 | 說明 | 下載 |
|------|------|------|
| CSV | 藥物摘要（適合 Excel） | [下載 CSV]({{ '/downloads/twtxgnn_drugs_summary.csv' | relative_url }}) |
| JSON | 藥物摘要（含統計） | [下載 JSON]({{ '/downloads/twtxgnn_drugs_summary.json' | relative_url }}) |
| CSV | 高證據藥物 (L1-L2) | [下載 CSV]({{ '/downloads/twtxgnn_high_evidence.csv' | relative_url }}) |

[前往下載頁面]({{ '/downloads/' | relative_url }}) &#124; [GitHub 完整資料](https://github.com/yao-care/TwTxGNN/tree/main/data/processed)

---

## 證據等級說明

| 等級 | 定義 | 臨床意義 |
|-----|------|---------|
| L1 | 多個 Phase 3 RCT / 系統性回顧 | 可支持臨床使用 |
| L2 | 單一 RCT 或多個 Phase 2 試驗 | 可考慮使用 |
| L3 | 觀察性研究 / 大型病例系列 | 待補件後評估 |
| L4 | 前臨床 / 機轉研究 / 個案報告 | 暫不建議 |
| L5 | 僅模型預測，無臨床證據 | 暫不建議 |
