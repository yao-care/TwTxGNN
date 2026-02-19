# 網站現況盤點報告

> 產出日期：2026-02-19
> 階段：1-Discovery (Writer)

---

## 基本資訊

| 項目 | 內容 |
|------|------|
| 網站 URL | https://twtxgnn.yao.care/ |
| 檢測日期 | 2026-02-19 |
| 託管平台 | GitHub Pages |
| 靜態網站框架 | Jekyll (Just the Docs 主題) |
| 頁面數量 | 約 200 頁（191 藥物報告 + 6 說明頁） |

---

## 1. 技術健檢結果

### 1.1 效能分數

| 項目 | 狀態 | 說明 |
|------|------|------|
| Performance | ⚠️ 待測 | PageSpeed API 未返回數據 |
| SEO | ⚠️ 需改善 | 缺少 Meta Description、OG Tags |
| Accessibility | ⚠️ 待測 | 需進一步檢測 |

> **注意**：PageSpeed Insights API 未返回有效數據，建議手動測試。

### 1.2 Core Web Vitals

| 指標 | 數值 | 標準 | 評價 |
|------|------|------|------|
| LCP | 待測 | < 2.5s | ⚠️ |
| TBT | 待測 | < 200ms | ⚠️ |
| CLS | 待測 | < 0.1 | ⚠️ |

### 1.3 安全性

| 項目 | 結果 | 評價 |
|------|------|------|
| HTTPS | ✅ 啟用 | GitHub Pages 自動提供 SSL |
| SSL 評級 | 待確認 | SSL Labs 掃描中 |
| HTTP Headers | ⚠️ 基本 | 缺少 CSP、X-Frame-Options（GitHub Pages 限制） |

**HTTP Headers 檢測結果**：
```
server: GitHub.com
content-type: text/html; charset=utf-8
access-control-allow-origin: *
cache-control: max-age=600
```

### 1.4 HTML 驗證

| 項目 | 數量 | 評價 |
|------|------|------|
| Errors | 1 | ⚠️ 需修復 |
| Warnings | 0 | ✅ 良好 |

### 1.5 SEO 基礎

| 項目 | 狀態 | 說明 |
|------|------|------|
| robots.txt | ❌ 缺少 | 返回 404，需建立 |
| sitemap.xml | ❌ 缺少 | 返回 404，需建立 |
| Meta Description | ❌ 缺少 | 首頁無 meta description 標籤 |
| OG Tags | ❌ 缺少 | 無 og:title, og:description, og:image |
| Twitter Card | ❌ 缺少 | 無 twitter:card 標籤 |
| Canonical URL | ⚠️ 未確認 | 需檢查 |
| JSON-LD Schema | ✅ 存在 | WebSite 類型（透過 jekyll-seo-tag） |
| H1 標籤 | ✅ 存在 | 「老藥新用，從數據到證據」 |

### 1.6 Jekyll 設定分析

| 項目 | 設定值 | 評價 |
|------|--------|------|
| 主題 | just-the-docs/just-the-docs | ✅ 良好 |
| SEO 插件 | jekyll-seo-tag | ✅ 已啟用 |
| 搜尋功能 | 已啟用 | ✅ 良好 |
| Collections | drugs (191 筆) | ✅ 結構化 |

**問題**：jekyll-seo-tag 插件需要在 front matter 中設定 `description` 才會產生 meta description。

---

## 2. 內容盤點

### 2.1 頁面清單

| 頁面 | URL | 類型 | 狀態 | 優先級 |
|------|-----|------|------|--------|
| 首頁 | / | 首頁 | ✅ | P0 |
| 高證據等級 | /evidence-high | 列表頁 | ✅ | P0 |
| 中證據等級 | /evidence-medium | 列表頁 | ✅ | P1 |
| 低證據等級 | /evidence-low | 列表頁 | ✅ | P1 |
| 方法論 | /methodology | 說明頁 | ✅ | P1 |
| 使用指南 | /guide | 說明頁 | ✅ | P2 |
| 資料來源 | /sources | 說明頁 | ✅ | P2 |
| 藥物報告 x191 | /drugs/{name}/ | 報告頁 | ✅ | P1 |

### 2.2 藥物報告結構

每個藥物報告包含：
- Front matter (layout, title, parent, evidence_level)
- 藥師評估報告
- 快速總覽表格
- 預測合理性說明
- 臨床試驗/文獻證據
- 安全性資訊
- 決策建議

### 2.3 內容問題

| 頁面 | 問題 | 嚴重度 |
|------|------|--------|
| 所有頁面 | 使用 Kramdown 語法 `{: .fs-9 }` | P1 |
| 所有頁面 | 缺少 description front matter | P0 |
| 首頁 | 免責聲明不夠醒目 | P1 |
| 藥物報告 | 缺少作者/審核者資訊 | P1 |

---

## 3. 結構分析（無 GA 數據）

| 分析項目 | 結果 | 建議 |
|----------|------|------|
| 導航結構 | ✅ 清晰 | 三層分類（等級 → 藥物 → 報告） |
| CTA 明確度 | ⚠️ 一般 | 首頁有 CTA 按鈕，報告頁缺乏下一步引導 |
| 內容完整度 | ✅ 良好 | 191 份報告完整產出 |
| 內部連結 | ⚠️ 不足 | 報告間缺乏相互連結 |
| 搜尋功能 | ✅ 已啟用 | Just the Docs 內建搜尋 |

---

## 4. 建議 KPI

基於現況，建議追蹤以下 KPI：

| KPI | 當前基準 | 目標 | 測量方式 |
|-----|----------|------|----------|
| 自然搜尋曝光 | 未知 | 月曝光 10,000+ | Search Console |
| 自然搜尋點擊 | 未知 | 月點擊 1,000+ | Search Console |
| 索引頁面數 | 未知 | 197 頁 (全部) | Search Console |
| 頁面停留時間 | 未知 | > 2 分鐘 | GA |
| 跳出率 | 未知 | < 60% | GA |

---

## 5. 關鍵發現摘要

### 優勢

1. **內容完整**：191 份藥物報告已完成，結構化良好
2. **技術架構現代**：Jekyll + GitHub Pages，維護成本低
3. **搜尋功能內建**：Just the Docs 提供站內搜尋
4. **證據分級系統**：L1-L5 分級清晰，便於用戶判斷

### 問題（按嚴重度排序）

| 優先級 | 問題 | 影響 | 建議行動 |
|--------|------|------|----------|
| **P0** | 缺少 robots.txt | 搜尋引擎爬蟲無指引 | 建立 robots.txt |
| **P0** | 缺少 sitemap.xml | 搜尋引擎無法有效索引 | 使用 jekyll-sitemap 插件 |
| **P0** | 缺少 meta description | SEO 嚴重不足 | 為每頁加入 description |
| **P0** | 缺少 OG Tags | 社群分享效果差 | 設定 og:image 等標籤 |
| **P1** | Kramdown 語法殘留 | 可能顯示原始碼 | 改用標準 HTML |
| **P1** | 缺少作者資訊 | E-E-A-T 信號不足 | 加入作者/機構資訊 |
| **P1** | 免責聲明不醒目 | YMYL 合規風險 | 增加視覺強調 |
| **P2** | 報告間缺乏連結 | 內部連結不足 | 加入相關藥物推薦 |

---

## 6. 數據來源

| 檢測項目 | 工具 | 時間 |
|----------|------|------|
| HTTP Headers | curl | 2026-02-19 14:32 |
| robots.txt | curl | 2026-02-19 14:32 |
| sitemap.xml | curl | 2026-02-19 14:32 |
| HTML Validation | W3C Validator API | 2026-02-19 14:33 |
| SEO 元素 | WebFetch | 2026-02-19 14:33 |
| Jekyll 設定 | 本地檔案 | 2026-02-19 14:34 |

---

## 下一步

1. 進入 **階段 2：競品分析 (Competitive)**
2. 或直接開始修復 P0 問題
