# Phase 2: SGE/AEO 標記批量更新計畫

**建立日期**: 2026-02-20
**執行者**: Claude Code
**狀態**: 執行中

---

## 1. 背景與問題

### 1.1 現況分析

| 指標 | 現況 | 目標 |
|------|------|------|
| 藥物頁面總數 | 191 | 191 |
| 已有 SGE/AEO 標記 | 1 (temozolomide.md) | 191 |
| 使用 Kramdown 語法 | 190 | 0 |
| 有 YMYL 免責聲明 | 1 | 191 |

### 1.2 識別的問題

1. **SGE/AEO 標記缺失**
   - `.key-answer` 標記：僅 1 頁
   - `.key-takeaway` 標記：僅 1 頁
   - `data-question` 屬性：僅 1 頁

2. **Kramdown 語法問題**
   ```markdown
   # 標題
   {: .fs-9 }

   {: .no_toc .text-delta }
   ```
   這些語法在某些環境下不會正確渲染。

3. **YMYL 合規問題**
   - 缺少免責聲明
   - 缺少審核日期
   - 缺少審核者資訊

---

## 2. 解決方案

### 2.1 範本結構

參考 `temozolomide.md` 建立標準藥物頁面結構：

```markdown
---
layout: default
title: {藥物名稱}
description: "{藥物名稱} 的老藥新用潛力分析。最高證據等級 {L1-L5}..."
parent: {父分類}
nav_order: {序號}
evidence_level: {L1-L5}
indication_count: {數量}
---

# {藥物名稱}

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
證據等級: <strong>{L1-L5}</strong> | 預測適應症: <strong>{N}</strong> 個 | 建議決策: <strong style="color: #2E7D32;">{決策}</strong>
</p>

---

<div id="pharmacist">

## 藥師評估報告

</div>

## 一句話總結

<p class="key-answer" data-question="{藥物名稱} 可以用於治療什麼新適應症？">
<strong>{藥物名稱}</strong> 是{藥物描述}...
</p>

<div class="key-takeaway">
{重點摘要}
</div>

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | {原適應症} |
| 預測新適應症 | {新適應症} |
| TxGNN 預測分數 | {分數}% |
| 證據等級 | {L1-L5} |
| 台灣上市 | {已上市/未上市} |

... (其他章節)

---

<div class="disclaimer">
<strong>免責聲明</strong><br>
本報告僅供學術研究參考，<strong>不構成醫療建議</strong>。藥物使用請遵循醫師指示，切勿自行調整用藥。任何老藥新用決策需經過完整的臨床驗證與法規審查。
<br><br>
<small>最後審核：2026-02-20 | 審核者：TwTxGNN Research Team</small>
</div>
```

### 2.2 更新策略

| 步驟 | 動作 | 說明 |
|------|------|------|
| 1 | 移除 Kramdown 語法 | 刪除所有 `{: .xxx }` 格式 |
| 2 | 更新標題區塊 | 使用內嵌 HTML/CSS 樣式 |
| 3 | 包裝關鍵內容 | 加入 `.key-answer` 和 `data-question` |
| 4 | 加入重點摘要 | 加入 `.key-takeaway` 區塊 |
| 5 | 加入免責聲明 | 加入 `.disclaimer` 區塊 |

---

## 3. 執行計畫

### 3.1 腳本開發

建立 `scripts/update_drug_pages.py`：

- 讀取所有 `docs/_drugs/*.md` 檔案
- 解析 front matter 和內容
- 移除 Kramdown 語法
- 套用新模板格式
- 寫入更新後的檔案

### 3.2 執行順序

1. **備份現有檔案**（透過 git）
2. **執行批量更新腳本**
3. **驗證更新結果**
4. **本地測試 Jekyll 建置**
5. **提交並推送至 GitHub**

### 3.3 驗證標準

- [ ] 所有 191 個藥物頁面都有 `.key-answer` 標記
- [ ] 所有頁面都有 `data-question` 屬性
- [ ] 所有頁面都有 `.disclaimer` 區塊
- [ ] 無 Kramdown 語法殘留
- [ ] Jekyll 建置成功
- [ ] GitHub Pages 部署成功

---

## 4. 風險與緩解

| 風險 | 影響 | 緩解措施 |
|------|------|----------|
| 內容解析錯誤 | 頁面內容遺失 | Git 版本控制可回滾 |
| 模板套用不一致 | 格式混亂 | 逐一檢查 L1-L2 頁面 |
| Jekyll 建置失敗 | 網站無法部署 | 本地預先測試 |

---

## 5. 預期成果

完成後：

- ✅ 191 個藥物頁面符合 SGE/AEO 規範
- ✅ AI 搜尋引擎可有效提取頁面重點
- ✅ YMYL 合規（所有頁面有免責聲明）
- ✅ 統一的視覺風格（無 Kramdown 語法問題）

---

## 6. 附錄

### 6.1 受影響檔案清單

共 190 個檔案需更新（排除已符合規範的 temozolomide.md）。

### 6.2 相關文件

- 範本參考：`docs/_drugs/temozolomide.md`
- SEO 規則：`CLAUDE.md` > docs/ 目錄 SEO/AEO 完整規則
- 樣式定義：`docs/_includes/head_custom.html`
