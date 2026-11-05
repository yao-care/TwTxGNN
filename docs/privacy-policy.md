---
layout: default
title: 隱私權政策
parent: 說明
nav_order: 5
description: "TwTxGNN SMART on FHIR 應用程式隱私權政策，說明資料收集、使用、儲存與安全措施。"
permalink: /privacy-policy/
---

# 隱私權政策

**最後更新日期**：2026 年 11 月 5 日

---

## 概述

<p class="key-answer" data-question="TwTxGNN 如何處理我的資料？">
TwTxGNN SMART App 是一個<strong>純前端應用程式</strong>，本站沒有後端伺服器處理病患資料。我們<strong>不收集、不儲存、不傳輸</strong>任何病患的個人健康資訊 (PHI) 到我們的伺服器；但為了對應藥名，App 會把藥品的 RxNorm 代碼送到美國國家醫學圖書館（NLM）的 RxNav，這個代碼不含病患身分。
</p>

---

## 資料收集與使用

### 我們不收集的資料

| 資料類型 | 收集情形 |
|----------|----------|
| 病患姓名、生日、聯絡資訊 | **不收集** |
| 病患用藥記錄 | **不收集** |
| 診斷紀錄 | **不收集** |
| 任何個人健康資訊 (PHI) | **不收集** |

### 應用程式如何運作

<ol class="actionable-steps">
<li><strong>EHR 授權</strong>：您從電子病歷系統 (EHR) 啟動 TwTxGNN SMART App</li>
<li><strong>本地處理</strong>：應用程式在您的瀏覽器中讀取用藥資料</li>
<li><strong>本地查詢與藥名對應</strong>：老藥新用查詢在瀏覽器中完成；藥物映射會把藥品的 RxNorm 代碼送到 NLM 的 RxNav 查成分名稱（不含病患身分）</li>
<li><strong>不送到本站伺服器</strong>：病患身分與電子病歷資料不會送到本站伺服器（本站是靜態網站，沒有後端）；您要求查詢臨床試驗時，送到 ClinicalTrials.gov 的是藥名與適應症名稱</li>
</ol>

---

## 技術架構與安全措施

### 純前端架構

<p class="key-answer" data-question="TwTxGNN 的技術架構是什麼？">
TwTxGNN SMART App 採用<strong>純前端（Client-Side Only）</strong>架構：所有程式碼都在使用者的瀏覽器中執行，不需要後端伺服器處理病患資料。
</p>

| 項目 | 說明 |
|------|------|
| 伺服器端處理 | 無 |
| 資料庫 | 無（使用靜態 JSON 檔案） |
| 病患資料儲存 | 無 |
| Session 儲存 | 僅在瀏覽器（記憶體與 sessionStorage），關閉分頁即清除 |

### OAuth 2.0 安全授權

本應用程式使用 **OAuth 2.0 with PKCE**（Proof Key for Code Exchange）進行授權：

- **PKCE 保護**：防止授權碼攔截攻擊
- **最小權限原則**：只請求必要的讀取權限
- **無長期憑證**：不儲存 refresh token

### 請求的權限範圍

```
launch                          - EHR 啟動上下文
patient/MedicationRequest.read  - 讀取用藥處方
patient/MedicationStatement.read - 讀取用藥陳述
openid                          - OpenID Connect 身份驗證
fhirUser                        - 使用者資訊
```

---

## 第三方服務

### 使用的外部服務

| 服務 | 用途 | 資料傳輸 |
|------|------|----------|
| **RxNorm API**（rxnav.nlm.nih.gov） | SMART App 查藥品成分名稱 | 僅傳送從電子病歷讀到的藥品 RxCUI 代碼（不含病患身分資料） |
| **CDN (jsDelivr)**（cdn.jsdelivr.net） | 程式庫：每頁的 d3 圖表；SMART 頁面與首頁藥物查詢的 Fuse.js、SMART on FHIR 用戶端 | 無病患資料 |
| **ClinicalTrials.gov API**（clinicaltrials.gov） | SMART 頁面的臨床試驗查詢 | 只在您要求查詢時，傳送藥名與適應症名稱 |
| **Google Analytics 4**（www.googletagmanager.com、google-analytics.com） | 網站瀏覽統計 | 瀏覽頁面、來源網站，使用分析 Cookie；不傳送搜尋字詞、表單內容與網址查詢參數 |

### 靜態資源

藥物預測資料庫（`search-index.json`）是靜態檔案，不包含任何使用者或病患資訊。

---

## 網站分析

### 我們的網站

TwTxGNN 網站（twtxgnn.yao.care）使用 Google Analytics 4 分析 Cookie 統計使用情況：

- **流量統計**：頁面瀏覽數、訪客來源、捲動深度、停留時間，以及點擊藥物報告與引用來源的次數
- **分析 Cookie**：載入頁面時設定 GA4 的分析 Cookie（如 `_ga`）；不傳送搜尋字詞、表單內容與網址查詢參數

### SMART App

SMART App 頁面和網站其他頁面一樣載入 Google Analytics 4，記錄頁面瀏覽與捲動、停留時間等使用情況；病患資料、搜尋字詞與網址查詢參數不會送出。

---

## 資料儲存

### 本地儲存

| 儲存位置 | 內容 | 存續時間 |
|----------|------|----------|
| 瀏覽器記憶體 | 用藥資料 | 關閉分頁即清除 |
| Local Storage | 無 | 不使用 |
| Session Storage | SMART App 的 EHR 授權狀態（含 OAuth token，由 SMART on FHIR 用戶端程式庫寫入） | 關閉分頁即清除 |
| Cookies | Google Analytics 4 分析 Cookie（如 `_ga`） | 依 GA4 預設，最長 2 年 |

### 伺服器端儲存

**無**。我們沒有後端伺服器，不儲存任何使用者或病患資料。網站使用統計由 Google Analytics 4 保存，見「網站分析」。

---

## HIPAA 合規聲明

雖然 TwTxGNN 主要針對台灣健保藥品，本應用程式的設計符合 HIPAA 隱私規則的精神：

<div class="key-takeaway">
<strong>隱私保護措施</strong>
<ul>
<li>不把病患身分傳到外部伺服器：送到外部服務的只有藥品 RxNorm 代碼（RxNav），以及您要求查詢時的藥名與適應症名稱（ClinicalTrials.gov）</li>
<li>純前端處理，本站沒有後端伺服器接收病患資料</li>
<li>使用加密連線 (HTTPS)</li>
<li>OAuth 2.0 + PKCE 安全授權</li>
<li>最小權限原則</li>
</ul>
</div>

---

## 開源透明

TwTxGNN 是開源專案，您可以檢視完整的程式碼：

- **GitHub**: [https://github.com/yao-care/TwTxGNN](https://github.com/yao-care/TwTxGNN)
- **SMART App 程式碼**: `docs/smart/` 目錄

<p>透明度是建立信任的基礎。開源程式碼允許任何人驗證我們的隱私聲明。</p>

---

## 兒童隱私

本應用程式不特別針對 13 歲以下兒童設計，但作為醫療輔助工具，可能用於顯示兒科病患的用藥資訊。無論使用者年齡，我們都不收集病患的個人資料；網站使用統計見「網站分析」。

---

## 政策變更

如果本隱私權政策有重大變更，我們將：

1. 更新本頁面的「最後更新日期」
2. 在 GitHub 專案中記錄變更
3. 保持變更的透明度

---

## 聯絡我們

如有隱私相關問題，請透過以下方式聯繫：

- **GitHub Issues**: [https://github.com/yao-care/TwTxGNN/issues](https://github.com/yao-care/TwTxGNN/issues)
- **專案首頁**: [https://twtxgnn.yao.care/](https://twtxgnn.yao.care/)

---

## 相關連結

- [SMART on FHIR 技術文件](/smart/)
- [關於專案](/about/)
- [資料來源](/sources/)

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本隱私權政策僅適用於 TwTxGNN SMART App 和 twtxgnn.yao.care 網站。當您使用第三方 EHR 系統時，該系統的隱私政策可能另有規定。
<br><br>
<small>最後審核：2026-02-27 | 審核者：藥提醒科技有限公司 (yao.care)</small>
</div>
