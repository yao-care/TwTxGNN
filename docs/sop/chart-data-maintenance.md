---
nav_exclude: true
---

# TwTxGNN 首頁圖表資料維護 - 標準作業程序 (SOP)

## 目錄

1. [系統概述](#1-系統概述)
2. [資料來源](#2-資料來源)
3. [更新 drug_stats.json](#3-更新-drug_statsjson)
4. [修改圖表呈現](#4-修改圖表呈現)
5. [驗證與部署](#5-驗證與部署)

---

## 1. 系統概述

### 1.1 架構圖

```
docs/_drugs/*.md (藥物頁面)
         │
         ├─ 提取 NCT ID 數量
         │
         ▼
docs/_data/drug_stats.json
         │
         ├─ all_drugs[]
         │  ├─ name, slug, level
         │  ├─ indication_count
         │  └─ nct_count ← 臨床試驗數量
         │
         ▼
docs/_includes/d3-charts.html
         │
         ├─ 高證據藥物臨床試驗數（L1-L2）長條圖
         └─ 證據等級 vs 適應症數量 散點圖
```

### 1.2 關鍵檔案

| 檔案 | 用途 |
|------|------|
| `docs/_data/drug_stats.json` | D3 圖表資料來源 |
| `docs/_includes/d3-charts.html` | D3 圖表程式碼 |
| `docs/_drugs/*.md` | 藥物頁面（NCT ID 來源） |

---

## 2. 資料來源

### 2.1 drug_stats.json 結構

```json
{
  "total_drugs": 191,
  "level_counts": { "L1": 8, "L2": 12, ... },
  "top_by_indications": [...],
  "all_drugs": [
    {
      "name": "Docetaxel",
      "slug": "docetaxel",
      "level": "L1",
      "indication_count": 10,
      "prediction_score": 0,
      "nct_count": 118
    }
  ]
}
```

### 2.2 NCT 數量來源

NCT 數量從 `docs/_drugs/*.md` 藥物頁面中提取，透過正則表達式 `NCT\d+` 計算唯一 NCT ID 數量。

---

## 3. 更新 drug_stats.json

### 3.1 更新 NCT 數量

當藥物頁面內容更新後，執行以下腳本重新計算 NCT 數量：

```python
import json
import re
from pathlib import Path

# 讀取現有 drug_stats
with open('docs/_data/drug_stats.json') as f:
    drug_stats = json.load(f)

# 計算每個藥物頁面的 NCT ID 數量
drugs_dir = Path('docs/_drugs')
nct_counts = {}

for md_file in drugs_dir.glob('*.md'):
    slug = md_file.stem
    content = md_file.read_text()
    nct_ids = set(re.findall(r'NCT\d+', content))
    nct_counts[slug] = len(nct_ids)

# 更新 all_drugs
for drug in drug_stats['all_drugs']:
    drug['nct_count'] = nct_counts.get(drug['slug'], 0)

# 更新 top_by_indications
for drug in drug_stats['top_by_indications']:
    drug['nct_count'] = nct_counts.get(drug['slug'], 0)

# 儲存
with open('docs/_data/drug_stats.json', 'w') as f:
    json.dump(drug_stats, f, indent=2, ensure_ascii=False)
```

### 3.2 新增其他欄位

若需要新增其他欄位（如文獻數量），依照相同模式：
1. 確定資料來源
2. 撰寫提取腳本
3. 更新 drug_stats.json
4. 修改 d3-charts.html 使用新欄位

---

## 4. 修改圖表呈現

### 4.1 圖表類型

| 圖表 | 用途 | 位置 |
|------|------|------|
| 長條圖 | 高證據藥物臨床試驗數 | `#indication-bar-chart` |
| 散點圖 | 證據等級 vs 適應症數量 | `#evidence-scatter-chart` |

### 4.2 修改長條圖 Y 軸欄位

在 `d3-charts.html` 的 `createBarChart()` 函數中：

```javascript
// 1. 修改資料排序
const highEvidence = drugData
  .filter(d => d.level === 'L1' || d.level === 'L2')
  .filter(d => (d.nct_count || 0) > 0)
  .sort((a, b) => (b.nct_count || 0) - (a.nct_count || 0))
  .slice(0, 15);

// 2. 修改 Y 軸
const y = d3.scaleLinear()
  .domain([0, d3.max(highEvidence, d => d.nct_count || 0) + 5])
  .nice()
  .range([height, 0]);

// 3. 修改長條高度
.attr('y', d => y(d.nct_count || 0))
.attr('height', d => height - y(d.nct_count || 0))

// 4. 修改 Y 軸標籤
.text('臨床試驗數量 (NCT)');
```

### 4.3 修改圖表標題

在 `d3-charts.html` 中修改：

```html
<div class="d3-chart-title">高證據藥物臨床試驗數（L1-L2）</div>
```

---

## 5. 驗證與部署

### 5.1 本地驗證

```bash
# 啟動本地 Jekyll 伺服器
cd docs && bundle exec jekyll serve

# 檢查 http://localhost:4000/ 圖表是否正確顯示
```

### 5.2 部署

```bash
git add docs/_data/drug_stats.json docs/_includes/d3-charts.html
git commit -m "feat(chart): update chart data source"
git push
gh workflow run "Deploy Jekyll to GitHub Pages"
```

---

## 執行紀錄

| 日期 | 修改內容 | 結果 |
|------|----------|------|
| 2026-03-03 | 長條圖改為顯示臨床試驗數量（NCT count） | Top 15 顯示，Docetaxel 118 NCTs 居首 |

---

*建立日期：2026-03-03*
