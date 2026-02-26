---
layout: default
title: 📰 健康新聞
nav_order: 3
description: "自動監測 191 種藥物與適應症的最新健康新聞報導，連結到藥物報告頁面。"
permalink: /news/
---

# 📰 健康新聞監測

<p class="key-answer" data-question="TwTxGNN 健康新聞監測是什麼？">
<strong>自動追蹤 191 種藥物與適應症的最新報導</strong>，當新聞提到 TwTxGNN 資料庫中的藥物或適應症時，系統會自動收集並整理，提供快速連結到對應的藥物報告頁面。
</p>

---

## 最新新聞

<div id="news-list">
<p>正在載入新聞...</p>
</div>

---

## 熱門關鍵字

<div id="keyword-cloud">
<p>正在載入關鍵字...</p>
</div>

---

## 瀏覽所有藥物

<p>點擊藥物名稱查看相關新聞報導：</p>

<div id="drug-list">
<p>正在載入藥物清單...</p>
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
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-items: center;
  gap: 6px;
}

.keyword-tag {
  display: inline-flex;
  align-items: center;
  padding: 4px 10px;
  border-radius: 14px;
  font-size: 0.85em;
  text-decoration: none;
  white-space: nowrap;
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

.drug-list-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 8px;
  margin-top: 16px;
}

.drug-list-item {
  display: block;
  padding: 8px 12px;
  background: #f6f8fa;
  border-radius: 6px;
  text-decoration: none;
  color: #24292e;
  font-size: 0.9em;
  transition: background 0.2s;
}

.drug-list-item:hover {
  background: #e1e4e8;
  text-decoration: none;
}

.drug-list-item.has-news {
  background: #e3f2fd;
  color: #1565c0;
}

.drug-list-item.has-news:hover {
  background: #bbdefb;
}
</style>

<script>
// 將名稱轉換為 URL slug（與 Python 版本一致）
function slugify(text) {
  return text.toLowerCase()
    .replace(/[\s_]+/g, '-')              // 空格和底線轉換為連字號
    .replace(/[^\w\u4e00-\u9fff-]/g, '')  // 移除特殊字元
    .replace(/-+/g, '-')                   // 多個連字號合併
    .replace(/^-|-$/g, '');                // 移除首尾連字號
}

document.addEventListener('DOMContentLoaded', function() {
  // 載入新聞索引
  fetch('{{ "/data/news-index.json" | relative_url }}')
    .then(response => response.json())
    .then(data => {
      renderNews(data.news);
      renderKeywordCloud(data.news);
      // 載入藥物清單
      loadDrugList(data.news);
    })
    .catch(err => {
      console.error('載入新聞失敗:', err);
      document.getElementById('news-list').innerHTML =
        '<p class="no-news">無法載入新聞資料</p>';
    });
});

function loadDrugList(newsItems) {
  fetch('{{ "/data/drugs.json" | relative_url }}')
    .then(response => response.json())
    .then(data => {
      // 找出有新聞的藥物
      const drugsWithNews = new Set();
      if (newsItems) {
        newsItems.forEach(item => {
          if (item.keywords) {
            item.keywords.forEach(k => {
              if (k.type === 'drug' && k.slug) {
                drugsWithNews.add(k.slug);
              }
            });
          }
        });
      }
      renderDrugList(data.drugs, drugsWithNews);
    })
    .catch(err => {
      console.error('載入藥物清單失敗:', err);
      document.getElementById('drug-list').innerHTML =
        '<p>無法載入藥物清單</p>';
    });
}

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

    // 關鍵字標籤（去重）
    let keywords = '';
    const baseUrl = '{{ "/" | relative_url }}';
    if (item.keywords && item.keywords.length > 0) {
      // 去重：使用 keyword 作為 key
      const seenKeywords = new Set();
      const uniqueKeywords = item.keywords.filter(k => {
        const key = k.keyword || k.name;
        if (seenKeywords.has(key)) return false;
        seenKeywords.add(key);
        return true;
      });

      keywords = uniqueKeywords.map(k => {
        if (k.type === 'drug') {
          return `<a href="${baseUrl}news/${k.slug}/" class="keyword-tag keyword-drug">${k.name} →</a>`;
        } else {
          // 適應症：顯示關鍵字名稱（連結到適應症頁面）+ 相關藥物連結
          const indSlug = slugify(k.name);
          const indLabel = k.keyword || k.name;
          let html = `<a href="${baseUrl}news/${indSlug}/" class="keyword-tag keyword-indication">${indLabel} →</a>`;
          if (k.related_drugs && k.related_drugs.length > 0) {
            const drugLinks = k.related_drugs.slice(0, 3).map(drug =>
              `<a href="${baseUrl}news/${drug.slug}/" class="keyword-tag keyword-drug">${drug.name} →</a>`
            ).join(' ');
            html += ' ' + drugLinks;
          }
          return html;
        }
      }).join(' ');
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
        const key = k.type === 'drug' ? k.slug : (k.keyword || k.name);
        const label = k.type === 'drug' ? k.name : (k.keyword || k.name);
        const slug = k.type === 'drug' ? k.slug : slugify(k.name);
        if (!keywordCounts[key]) {
          keywordCounts[key] = { label, count: 0, type: k.type, slug: slug };
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

  const baseUrl = '{{ "/" | relative_url }}';
  let html = sortedKeywords.map(k => {
    return `<a href="${baseUrl}news/${k.slug}/" class="keyword-cloud-item">${k.label} (${k.count})</a>`;
  }).join('');

  container.innerHTML = html;
}

function renderDrugList(drugs, drugsWithNews) {
  const container = document.getElementById('drug-list');

  if (!drugs || drugs.length === 0) {
    container.innerHTML = '<p>無法載入藥物清單</p>';
    return;
  }

  // 按藥物名稱排序
  drugs.sort((a, b) => a.name.localeCompare(b.name));

  const baseUrl = '{{ "/" | relative_url }}';
  let html = '<div class="drug-list-grid">';

  drugs.forEach(drug => {
    const hasNews = drugsWithNews.has(drug.slug);
    const className = hasNews ? 'drug-list-item has-news' : 'drug-list-item';
    html += `<a href="${baseUrl}news/${drug.slug}/" class="${className}">${drug.name}</a>`;
  });

  html += '</div>';
  container.innerHTML = html;
}
</script>
