---
layout: default
title: 健康新聞
nav_order: 2
description: "自動監測 191 種藥物與適應症的最新健康新聞報導，連結到藥物報告頁面。"
permalink: /news/
---

# 健康新聞監測

<p class="key-answer" data-question="TwTxGNN 健康新聞監測是什麼？">
<strong>自動追蹤 191 種藥物與適應症的最新報導</strong>，當新聞提到 TwTxGNN 資料庫中的藥物或適應症時，系統會自動收集並整理，提供快速連結到對應的藥物報告頁面。
</p>

---

<div id="news-list">
<p>正在載入新聞...</p>
</div>

---

## 熱門關鍵字

<div id="keyword-cloud">
<p>正在載入關鍵字...</p>
</div>

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本頁新聞由系統自動收集，<strong>僅供研究參考</strong>，不構成醫療建議。新聞內容來自各媒體，TwTxGNN 不對新聞內容負責。藥物使用請遵循醫師指示。
<br><br>
<small>資料來源：Google News、嘉義慈濟醫院 | 更新頻率：每小時</small>
</div>

<style>
.news-card {
  border: 1px solid #e1e4e8;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
  background: #fff;
}

.news-card:hover {
  border-color: #0366d6;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.news-title {
  font-size: 1.1em;
  font-weight: 600;
  margin-bottom: 8px;
  color: #24292e;
}

.news-meta {
  font-size: 0.85em;
  color: #586069;
  margin-bottom: 8px;
}

.news-sources {
  font-size: 0.85em;
}

.news-sources a {
  color: #0366d6;
  margin-right: 8px;
}

.news-keywords {
  margin-top: 8px;
}

.keyword-tag {
  display: inline-block;
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 0.8em;
  margin-right: 4px;
  margin-bottom: 4px;
  text-decoration: none;
}

.keyword-drug {
  background: #e3f2fd;
  color: #1565c0;
}

.keyword-indication {
  background: #f3e5f5;
  color: #7b1fa2;
}

.keyword-cloud-item {
  display: inline-block;
  padding: 4px 12px;
  margin: 4px;
  border-radius: 16px;
  background: #f0f0f0;
  color: #333;
  text-decoration: none;
  font-size: 0.9em;
}

.keyword-cloud-item:hover {
  background: #e0e0e0;
}

.no-news {
  text-align: center;
  padding: 40px;
  color: #586069;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  fetch('{{ "/data/news-index.json" | relative_url }}')
    .then(response => response.json())
    .then(data => {
      renderNews(data.news);
      renderKeywordCloud(data.news);
    })
    .catch(err => {
      document.getElementById('news-list').innerHTML =
        '<p class="no-news">無法載入新聞資料</p>';
    });
});

function renderNews(newsItems) {
  const container = document.getElementById('news-list');

  if (!newsItems || newsItems.length === 0) {
    container.innerHTML = '<p class="no-news">目前沒有匹配的新聞</p>';
    return;
  }

  // 按時間排序
  newsItems.sort((a, b) => new Date(b.published) - new Date(a.published));

  let html = '';

  newsItems.forEach(item => {
    // 格式化日期
    const date = new Date(item.published);
    const dateStr = date.toLocaleDateString('zh-TW', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });

    // 來源連結
    const sources = item.sources.map(s =>
      `<a href="${s.link}" target="_blank" rel="noopener">${s.name} ↗</a>`
    ).join(' ');

    // 關鍵字標籤
    let keywords = '';
    if (item.keywords && item.keywords.length > 0) {
      keywords = item.keywords.map(k => {
        if (k.type === 'drug') {
          return `<a href="{{ '' | relative_url }}drugs/${k.slug}/" class="keyword-tag keyword-drug">${k.name} →</a>`;
        } else {
          return `<span class="keyword-tag keyword-indication">${k.name}</span>`;
        }
      }).join('');
    }

    html += `
      <div class="news-card">
        <div class="news-title">${item.title}</div>
        <div class="news-meta">${dateStr}</div>
        <div class="news-sources">來源：${sources}</div>
        ${keywords ? `<div class="news-keywords">${keywords}</div>` : ''}
      </div>
    `;
  });

  container.innerHTML = html;
}

function renderKeywordCloud(newsItems) {
  const container = document.getElementById('keyword-cloud');

  if (!newsItems || newsItems.length === 0) {
    container.innerHTML = '<p>目前沒有關鍵字資料</p>';
    return;
  }

  // 統計關鍵字出現次數
  const keywordCounts = {};

  newsItems.forEach(item => {
    if (item.keywords) {
      item.keywords.forEach(k => {
        const key = k.type === 'drug' ? k.slug : k.name;
        const label = k.type === 'drug' ? k.name : k.name;
        if (!keywordCounts[key]) {
          keywordCounts[key] = { label, count: 0, type: k.type, slug: k.slug };
        }
        keywordCounts[key].count++;
      });
    }
  });

  // 轉換為陣列並排序
  const sortedKeywords = Object.values(keywordCounts)
    .sort((a, b) => b.count - a.count)
    .slice(0, 20);

  if (sortedKeywords.length === 0) {
    container.innerHTML = '<p>目前沒有關鍵字資料</p>';
    return;
  }

  let html = sortedKeywords.map(k => {
    if (k.type === 'drug') {
      return `<a href="{{ '' | relative_url }}drugs/${k.slug}/" class="keyword-cloud-item">${k.label} (${k.count})</a>`;
    } else {
      return `<span class="keyword-cloud-item">${k.label} (${k.count})</span>`;
    }
  }).join('');

  container.innerHTML = html;
}
</script>
