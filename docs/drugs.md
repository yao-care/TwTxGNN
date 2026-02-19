---
layout: default
title: 藥物列表
nav_order: 5
description: "TwTxGNN 所有藥物驗證報告列表，支援證據等級篩選和關鍵字搜尋。"
permalink: /drugs/
---

# 藥物列表

共 191 種藥物的老藥新用驗證報告

---

## 進階篩選

<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px; margin-bottom: 1.5rem;">
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
    <div>
      <button id="reset-filters" style="padding: 0.5rem 1rem; background: #6c757d; color: white; border: none; border-radius: 4px; cursor: pointer;">重置</button>
    </div>
  </div>
  <div style="margin-top: 0.75rem; font-size: 0.9rem; color: #666;">
    顯示 <span id="filtered-count">191</span> / 191 個藥物
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
  const resetBtn = document.getElementById('reset-filters');
  const filteredCount = document.getElementById('filtered-count');
  const tableRows = document.querySelectorAll('#drugs-table tbody tr');

  function applyFilters() {
    const searchTerm = searchInput.value.toLowerCase();
    const selectedLevels = Array.from(levelFilters)
      .filter(cb => cb.checked)
      .map(cb => cb.value);

    let visibleCount = 0;

    tableRows.forEach(row => {
      const name = row.dataset.name;
      const level = row.dataset.level;

      const matchesSearch = name.includes(searchTerm);
      const matchesLevel = selectedLevels.includes(level);

      if (matchesSearch && matchesLevel) {
        row.classList.remove('hidden');
        visibleCount++;
      } else {
        row.classList.add('hidden');
      }
    });

    filteredCount.textContent = visibleCount;
  }

  searchInput.addEventListener('input', applyFilters);
  levelFilters.forEach(cb => cb.addEventListener('change', applyFilters));

  resetBtn.addEventListener('click', function() {
    searchInput.value = '';
    levelFilters.forEach(cb => cb.checked = true);
    applyFilters();
  });
});

let sortDirection = {};
function sortTable(columnIndex) {
  const table = document.getElementById('drugs-table');
  const tbody = table.querySelector('tbody');
  const rows = Array.from(tbody.querySelectorAll('tr'));

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
| CSV | 適合 Excel | [drugs.csv]({{ '/data/drugs.csv' | relative_url }}) |
| JSON | 適合程式存取 | [drugs.json]({{ '/data/drugs.json' | relative_url }}) |

[前往下載頁面]({{ '/download' | relative_url }})

---

## 證據等級說明

| 等級 | 定義 | 臨床意義 |
|-----|------|---------|
| L1 | 多個 Phase 3 RCT / 系統性回顧 | 可支持臨床使用 |
| L2 | 單一 RCT 或多個 Phase 2 試驗 | 可考慮使用 |
| L3 | 觀察性研究 / 大型病例系列 | 待補件後評估 |
| L4 | 前臨床 / 機轉研究 / 個案報告 | 暫不建議 |
| L5 | 僅模型預測，無臨床證據 | 暫不建議 |
