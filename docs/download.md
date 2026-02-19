---
layout: default
title: 資料下載
nav_order: 10
description: "下載 TwTxGNN 老藥新用驗證報告的完整資料集，提供 CSV 和 JSON 格式。"
permalink: /download/
---

# 資料下載

下載完整的藥物報告資料集

---

## 可下載檔案

| 檔案 | 格式 | 說明 | 下載 |
|------|------|------|------|
| 完整資料集 | JSON | 191 個藥物的完整資料 | [drugs.json]({{ '/data/drugs.json' | relative_url }}) |
| 完整資料集 | CSV | 適合 Excel / 試算表 | [drugs.csv]({{ '/data/drugs.csv' | relative_url }}) |
| 證據等級分組 | JSON | 按 L1-L5 分組的摘要 | [drugs-by-level.json]({{ '/data/drugs-by-level.json' | relative_url }}) |

---

## 資料欄位說明

| 欄位 | 說明 |
|------|------|
| `name` | 藥物名稱 |
| `slug` | URL 識別碼 |
| `evidence_level` | 證據等級 (L1-L5) |
| `indication_count` | 預測適應症數量 |
| `original_indication` | 原適應症 |
| `predicted_indication` | 預測新適應症 |
| `txgnn_score` | TxGNN 預測分數 |
| `taiwan_approved` | 是否已在台灣上市 |
| `decision` | 建議決策 (Go/Proceed/Consider/Hold) |
| `url` | 報告頁面 URL |

---

## 使用條款

- 資料僅供**學術研究**使用
- 引用時請註明來源：`TwTxGNN - https://twtxgnn.yao.care/`
- 不得用於商業目的或醫療決策

### 建議引用格式

```
TwTxGNN. (2026). TwTxGNN 老藥新用驗證報告資料集. https://twtxgnn.yao.care/download/
```

---

## 程式存取

### Python 範例

```python
import pandas as pd

# 讀取 CSV
df = pd.read_csv('https://twtxgnn.yao.care/data/drugs.csv')

# 篩選高證據等級
high_evidence = df[df['evidence_level'].isin(['L1', 'L2'])]
print(high_evidence)
```

### JavaScript 範例

```javascript
fetch('https://twtxgnn.yao.care/data/drugs.json')
  .then(res => res.json())
  .then(data => {
    // 篩選高證據等級
    const highEvidence = data.drugs.filter(d =>
      ['L1', 'L2'].includes(d.evidence_level)
    );
    console.log(highEvidence);
  });
```

---

<div style="background: #fff3cd; padding: 1rem; margin-top: 2rem; border-left: 4px solid #ffc107; border-radius: 4px;">
<strong>免責聲明</strong><br>
本資料僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示。
</div>
