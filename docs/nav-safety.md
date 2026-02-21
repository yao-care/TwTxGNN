---
layout: default
title: 安全性資料
nav_order: 4
has_children: true
description: "四大交互作用資料庫：DDI、DDSI、DFI、DHI，評估老藥新用安全風險。"
---

# 安全性資料

<p style="font-size: 1.1rem; color: #666; margin-bottom: 1.5rem;">
整合 <strong>4 種交互作用資料</strong>，評估老藥新用的安全性風險
</p>

<style>
.safety-dist-container {
  margin: 2rem 0;
}
.safety-dist-bar {
  display: flex;
  height: 32px;
  border-radius: 16px;
  overflow: hidden;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
.safety-dist-bar a {
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 0.75rem;
  text-decoration: none;
  transition: filter 0.2s, transform 0.2s;
}
.safety-dist-bar a:hover {
  filter: brightness(1.1);
  transform: scaleY(1.1);
}
.dist-ddi { background: linear-gradient(135deg, #1565C0, #42A5F5); }
.dist-ddsi { background: linear-gradient(135deg, #7B1FA2, #BA68C8); }
.dist-dfi { background: linear-gradient(135deg, #388E3C, #66BB6A); }
.dist-dhi { background: linear-gradient(135deg, #E65100, #FF9800); }

.safety-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1rem;
}
.safety-card {
  display: flex;
  align-items: center;
  padding: 1.25rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.08);
  text-decoration: none;
  color: inherit;
  transition: transform 0.2s, box-shadow 0.2s;
  border-left: 5px solid;
}
.safety-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.12);
}
.safety-card.ddi { border-color: #1565C0; }
.safety-card.ddsi { border-color: #7B1FA2; }
.safety-card.dfi { border-color: #388E3C; }
.safety-card.dhi { border-color: #E65100; }

.safety-card-icon {
  width: 56px;
  height: 56px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 1rem;
  flex-shrink: 0;
  font-size: 1.5rem;
}
.safety-card.ddi .safety-card-icon { background: #E3F2FD; }
.safety-card.ddsi .safety-card-icon { background: #F3E5F5; }
.safety-card.dfi .safety-card-icon { background: #E8F5E9; }
.safety-card.dhi .safety-card-icon { background: #FFF3E0; }

.safety-card-count {
  font-size: 1.25rem;
  font-weight: 700;
  line-height: 1;
}
.safety-card.ddi .safety-card-count { color: #1565C0; }
.safety-card.ddsi .safety-card-count { color: #7B1FA2; }
.safety-card.dfi .safety-card-count { color: #388E3C; }
.safety-card.dhi .safety-card-count { color: #E65100; }

.safety-card-info {
  flex: 1;
}
.safety-card-title {
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
  color: #333;
}
.safety-card-desc {
  font-size: 0.8rem;
  color: #666;
}
.safety-card-badge {
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.7rem;
  font-weight: 600;
  margin-left: auto;
  white-space: nowrap;
}
.safety-card.ddi .safety-card-badge { background: #E3F2FD; color: #1565C0; }
.safety-card.ddsi .safety-card-badge { background: #F3E5F5; color: #7B1FA2; }
.safety-card.dfi .safety-card-badge { background: #E8F5E9; color: #388E3C; }
.safety-card.dhi .safety-card-badge { background: #FFF3E0; color: #E65100; }
</style>

<div class="safety-dist-container">
  <div class="safety-dist-bar">
    <a href="{{ '/ddi/' | relative_url }}" class="dist-ddi" style="width: 97%;" title="藥物-藥物交互作用：302,516 筆">DDI 30萬</a>
    <a href="{{ '/ddsi/' | relative_url }}" class="dist-ddsi" style="width: 2.7%;" title="藥物-疾病注意事項：8,359 筆"></a>
    <a href="{{ '/dfi/' | relative_url }}" class="dist-dfi" style="width: 0.3%;" title="藥物-食物交互作用：857 筆"></a>
  </div>

  <div class="safety-cards">
    <a href="{{ '/ddi/' | relative_url }}" class="safety-card ddi">
      <div class="safety-card-icon">
        <span class="safety-card-count">30萬</span>
      </div>
      <div class="safety-card-info">
        <div class="safety-card-title">藥物-藥物交互作用</div>
        <div class="safety-card-desc">2,310 種藥物的併用風險</div>
      </div>
      <span class="safety-card-badge">DDI</span>
    </a>

    <a href="{{ '/ddsi/' | relative_url }}" class="safety-card ddsi">
      <div class="safety-card-icon">
        <span class="safety-card-count">8,359</span>
      </div>
      <div class="safety-card-info">
        <div class="safety-card-title">藥物-疾病注意事項</div>
        <div class="safety-card-desc">115 種藥物的禁忌症</div>
      </div>
      <span class="safety-card-badge">DDSI</span>
    </a>

    <a href="{{ '/dfi/' | relative_url }}" class="safety-card dfi">
      <div class="safety-card-icon">
        <span class="safety-card-count">857</span>
      </div>
      <div class="safety-card-info">
        <div class="safety-card-title">藥物-食物交互作用</div>
        <div class="safety-card-desc">29 種常見食物的影響</div>
      </div>
      <span class="safety-card-badge">DFI</span>
    </a>

    <a href="{{ '/dhi/' | relative_url }}" class="safety-card dhi">
      <div class="safety-card-icon">
        <span class="safety-card-count">35</span>
      </div>
      <div class="safety-card-info">
        <div class="safety-card-title">藥物-草藥交互作用</div>
        <div class="safety-card-desc">10 種常見草藥的風險</div>
      </div>
      <span class="safety-card-badge">DHI</span>
    </a>
  </div>
</div>

---

## 資料來源

所有交互作用資料主要來自 [DDInter 2.0](https://ddinter2.scbdd.com/)，這是目前最完整的公開藥物交互作用資料庫。

| 類型 | 資料來源 | 記錄數 | 最後更新 |
|------|----------|--------|----------|
| DDI | DDInter 2.0 | 302,516 | 2026-02-08 |
| DDSI | DDInter 2.0 | 8,359 | 2026-02-21 |
| DFI | DDInter 2.0 | 857 | 2026-02-21 |
| DHI | 精選資料集 | 35 | 2026-02-21 |

