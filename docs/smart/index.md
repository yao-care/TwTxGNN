---
layout: default
title: SMART on FHIR 技術文件
nav_order: 8
description: TwTxGNN SMART on FHIR 應用程式技術規格，包含 OAuth 配置、FHIR API 端點、藥物映射流程
---

# SMART on FHIR 應用程式

TwTxGNN 提供 SMART on FHIR 整合，讓醫療機構可以從電子病歷系統（EHR）讀取病患用藥資料，自動查詢相關的老藥新用候選。

---

## 什麼是 SMART on FHIR？

SMART on FHIR 是一個開放標準，讓醫療應用程式可以安全地存取電子病歷系統中的資料。透過這個標準：

- 應用程式可以從 EHR 系統獲取授權
- 讀取病患的用藥記錄、診斷等資料
- 在 EHR 工作流程中無縫整合

---

## 功能特色

| 功能 | 說明 |
|------|------|
| **病患用藥讀取** | 自動從 EHR 獲取病患目前的用藥清單 |
| **藥物映射** | 將 RxNorm 藥物代碼映射到 TwTxGNN 資料庫 |
| **老藥新用查詢** | 顯示每個藥物的預測新適應症候選 |
| **證據等級標示** | 清楚標示每個預測的證據等級（L1-L5） |

---

## 使用方式

### 方式一：從 EHR 啟動（正式使用）

1. 在您的 EHR 系統中配置 TwTxGNN SMART App
2. 從病患病歷中啟動應用程式
3. 應用程式會自動讀取病患用藥並顯示老藥新用候選

**啟動端點**：`https://twtxgnn.yao.care/smart/launch.html`

### 方式二：獨立測試模式

不需要連接 EHR 系統，可以直接測試功能：

<div style="margin: 20px 0;">
  <a href="standalone.html" style="display: inline-block; padding: 12px 24px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; text-decoration: none; border-radius: 8px; font-weight: 500;">開啟獨立測試模式</a>
</div>

---

## 技術規格

### SMART on FHIR 配置

| 項目 | 值 |
|------|------|
| FHIR 版本 | R4 |
| Client ID | `twtxgnn-smart-app` |
| Launch URI | `/smart/launch.html` |
| Redirect URI | `/smart/app.html` |
| 授權方式 | OAuth 2.0 with PKCE |

### 請求的權限範圍（Scopes）

```
launch
patient/MedicationRequest.read
patient/MedicationStatement.read
openid
fhirUser
```

### 藥物映射流程

```
EHR MedicationRequest
       │
       ├─ 提取 RxCUI（RxNorm 代碼）
       │
       ├─ 呼叫 RxNorm API 取得成分名
       │
       ├─ 藥物名稱正規化
       │   （移除鹽類後綴、同義詞對照）
       │
       └─ 模糊比對 TwTxGNN 資料庫
              │
              ▼
       顯示老藥新用候選
```

---

## 測試環境

### 使用 SMART Health IT Launcher 測試

1. 前往 [SMART Launcher](https://launch.smarthealthit.org/)
2. 設定：
   - **Launch Type**: Provider EHR Launch
   - **FHIR Version**: R4
   - **App Launch URL**: `https://twtxgnn.yao.care/smart/launch.html`
3. 選擇測試病患
4. 點擊 Launch 開始測試

### 支援的 EHR 系統

理論上支援所有符合 SMART on FHIR R4 標準的 EHR 系統，包括：

- Epic
- Cerner (Oracle Health)
- Allscripts
- 其他 FHIR R4 相容系統

---

## FHIR API

TwTxGNN 也提供靜態 FHIR API，讓其他系統可以查詢藥物預測資料。

### 端點

| 端點 | 說明 |
|------|------|
| `/fhir/metadata` | CapabilityStatement |
| `/fhir/MedicationKnowledge/{id}.json` | 單一藥物資源 |
| `/fhir/Bundle/all-predictions.json` | 全部預測結果 |

### 範例

```bash
# 取得 Warfarin 的藥物知識資源
curl https://twtxgnn.yao.care/fhir/MedicationKnowledge/warfarin.json
```

---

## 隱私與安全

- **無資料儲存**：應用程式不會在伺服器端儲存任何病患資料
- **純前端處理**：所有資料處理都在瀏覽器中進行
- **PKCE 保護**：使用 OAuth 2.0 PKCE 流程確保授權安全
- **最小權限**：只請求必要的讀取權限

---

## 免責聲明

<div style="background: #fff3cd; border: 1px solid #ffc107; border-radius: 8px; padding: 16px; margin: 20px 0;">
<strong>重要提醒</strong><br>
本網站內容僅供研究參考，不能取代專業醫療建議。所有藥物再利用預測結果需經過臨床驗證才能應用。如有健康問題，請諮詢合格醫療人員。
</div>

---

## 相關連結

- [SMART on FHIR 官方文件](http://docs.smarthealthit.org/)
- [HL7 FHIR 規範](https://www.hl7.org/fhir/)
- [RxNorm API 文件](https://lhncbc.nlm.nih.gov/RxNav/APIs/RxNormAPIs.html)
