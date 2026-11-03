# Security Headers 修復設計

**日期**: 2026-04-27
**目標**: 解決 ZAP 掃描報告中 16 個 finding（5 Medium / 5 Low / 6 Info）
**範圍**: TwTxGNN + 其他 29 個國家站同步

---

## 背景

- 網站架構：GitHub Pages（Jekyll + GitHub Actions 部署）
- 限制：GitHub Pages 無法設定 HTTP 回應標頭
- 掃描方式：每日 zaproxy/action-baseline@v0.14.0、每月 zap-full-scan.py
- 目前設定：無 rules config，所有規則為預設值

## 策略

| 分類 | 數量 | 處理方式 |
|------|------|----------|
| 能修的 Medium（CSP） | 3 | 加 CSP meta tag + 抽出外部 CSS |
| 不能修的 Medium/Low（HTTP 標頭） | 7 | ZAP rules config 降為 WARN |
| Informational | 6 | 待定（5 個 cache 相關 + 1 個加 CSP 後自動消失） |

---

## 第一手：真修

### 1. 抽出 CSS 為外部檔案

**新建** `docs/assets/css/custom.css`

將 `docs/_includes/head_custom.html` 第 479-932 行的 `<style>` 區塊移入外部 CSS 檔案。

**理由**：消除 `style-src 'unsafe-inline'` 的需求，讓 CSP 更嚴格。

### 2. 修改 head_custom.html

- 刪除 `<style>...</style>` 區塊
- 加入 `<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">`
- 加入 CSP meta tag

### 3. CSP 政策

```html
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' https://d3js.org https://cdn.jsdelivr.net https://giscus.app; style-src 'self'; img-src 'self' data: https:; connect-src 'self' https://rxnav.nlm.nih.gov https://giscus.app; frame-src https://giscus.app; font-src 'self';">
```

**允許的外部來源**：

| 指令 | 來源 | 用途 |
|------|------|------|
| script-src | https://d3js.org | D3.js 圖表 |
| script-src | https://cdn.jsdelivr.net | fuse.js、fhirclient |
| script-src | https://giscus.app | 留言系統 |
| connect-src | https://rxnav.nlm.nih.gov | SMART App RxNorm API |
| connect-src | https://giscus.app | Giscus API |
| frame-src | https://giscus.app | Giscus iframe |

**注意**：`style-src 'self'` 不含 `'unsafe-inline'`。部署後需測試：
- 首頁 D3 圖表
- 任一藥物頁面樣式
- SMART standalone
- Giscus 留言區
- 搜尋功能

若 just-the-docs 主題注入了 inline style 導致壞掉，fallback 方案是加回 `'unsafe-inline'` 並在 rules config 中將 10055 CSP style-src 降為 WARN。

---

## 第二手：ZAP Rules Config

**新建** `docs/.zap/rules.tsv`

```tsv
# ZAP Rules Configuration for TwTxGNN
# GitHub Pages 無法設定 HTTP 回應標頭，以下項目降為 WARN
# 參考：https://www.zaproxy.org/docs/docker/baseline-scan/#rules-file-format

10020	WARN	(X-Frame-Options Header - GitHub Pages 無法設定)
10021	WARN	(X-Content-Type-Options Header - GitHub Pages 無法設定)
10027	WARN	(Information Disclosure - Suspicious Comments - 正常程式碼註解)
10035	WARN	(Strict-Transport-Security - GitHub Pages 無法設定)
10063	WARN	(Permissions Policy Header - GitHub Pages 無法設定)
10098	WARN	(Cross-Domain Misconfiguration - GitHub CDN 控制 CORS)
90004	WARN	(Cross-Origin-Embedder-Policy - GitHub Pages 無法設定)
90005	WARN	(Cross-Origin-Opener-Policy - GitHub Pages 無法設定)
```

提供給掃描單位在 CI 中引用：
```yaml
# zaproxy/action-baseline 或 action-full-scan
with:
  rules_file_name: "docs/.zap/rules.tsv"
```

---

## 第三手：同步到 30 個國家站

使用 `sync_shared_code.sh` 模式，同步以下檔案：
- `docs/assets/css/custom.css`
- `docs/_includes/head_custom.html`
- `docs/.zap/rules.tsv`

同步腳本中新增這三個檔案的路徑。

---

## 預期結果

修復前：5 Medium / 5 Low / 6 Info = 16 findings

修復後（CSP meta tag 成功、style-src 'self' 無問題）：
- Medium: 0（CSP 3 個消除 + Anti-clickjacking 和 CORS 降為 WARN）
- Low: 0（全部降為 WARN）
- Info: 5（cache 相關，待定）
- WARN: 8（不 fail、報告中可見但不計為 finding）

修復後（若需要加回 unsafe-inline）：
- Medium: 1（CSP style-src unsafe-inline）
- 其餘同上

---

## 驗證計畫

1. 修改 TwTxGNN，push 後等 GitHub Pages 部署
2. 手動開啟以下頁面，檢查 Console 無 CSP violation 錯誤：
   - https://twtxgnn.yao.care/
   - https://twtxgnn.yao.care/drugs/acebutolol/
   - https://twtxgnn.yao.care/smart/standalone.html
   - 任一有 Giscus 留言的頁面
3. 通過後執行同步腳本推送到 29 個國家站
4. 通知掃描單位在 CI 中引用 `docs/.zap/rules.tsv`
