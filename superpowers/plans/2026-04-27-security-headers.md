# Security Headers Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 修復 ZAP 掃描的 5 個 Medium finding（CSP 相關），並建立 rules config 降級 GitHub Pages 無法控制的項目。

**Architecture:** 從 head_custom.html 抽出 SGE/AEO 樣式為外部 CSS，加入 CSP meta tag（不含 unsafe-inline），建立 .zap/rules.tsv 給掃描 CI 引用，最後同步到 29 個國家站。

**Tech Stack:** Jekyll / GitHub Pages / OWASP ZAP rules.tsv / Bash sync scripts

---

## File Structure

| 操作 | 檔案 | 用途 |
|------|------|------|
| Create | `docs/assets/css/custom.css` | SGE/AEO 樣式（從 head_custom.html 抽出） |
| Create | `docs/.zap/rules.tsv` | ZAP 掃描規則配置 |
| Create | `.claude/sync_security_headers.sh` | 同步腳本 |
| Modify | `docs/_includes/head_custom.html` | 移除 style block，加 CSP meta + CSS link |

---

### Task 1: 建立外部 CSS 檔案

**Files:**
- Create: `TwTxGNN/docs/assets/css/custom.css`

- [ ] **Step 1: 建立 custom.css**

將 `docs/_includes/head_custom.html` 第 479-932 行（`<!-- SGE/AEO 支援樣式 -->` 開始到 `</style>` 結束）的 CSS 內容抽出，不含 `<style>` 和 `</style>` 標籤本身。

```css
/* SGE/AEO 支援樣式 */
.key-answer {
  background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
  padding: 1rem 1.25rem;
  border-radius: 8px;
  border-left: 4px solid #2E7D32;
  margin: 1rem 0;
  font-size: 1.05rem;
}
/* ... 完整內容從 head_custom.html 第 480-931 行複製 ... */
```

- [ ] **Step 2: 確認檔案存在**

Run: `wc -l TwTxGNN/docs/assets/css/custom.css`
Expected: 約 452 行

- [ ] **Step 3: Commit**

```bash
cd /Users/lightman/yao.care/TxGNN/TwTxGNN
git add docs/assets/css/custom.css
git commit -m "feat(security): extract SGE/AEO styles to external CSS"
```

---

### Task 2: 修改 head_custom.html

**Files:**
- Modify: `TwTxGNN/docs/_includes/head_custom.html`

- [ ] **Step 1: 在檔案最頂部加入 CSP meta tag 和 CSS link**

在現有第 1 行之前插入：

```html
<!-- Security: Content Security Policy -->
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' https://d3js.org https://cdn.jsdelivr.net https://giscus.app; style-src 'self'; img-src 'self' data: https:; connect-src 'self' https://rxnav.nlm.nih.gov https://giscus.app; frame-src https://giscus.app; font-src 'self';">

<!-- Custom styles (extracted from inline) -->
<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

```

- [ ] **Step 2: 刪除 SGE/AEO `<style>` 區塊**

刪除從 `<!-- SGE/AEO 支援樣式 -->` 到對應 `</style>` 的整段（原第 478-932 行，含 `<style>` 和 `</style>` 標籤）。

- [ ] **Step 3: 確認結果**

Run: `grep -c 'unsafe-inline' TwTxGNN/docs/_includes/head_custom.html`
Expected: 0

Run: `grep -c 'Content-Security-Policy' TwTxGNN/docs/_includes/head_custom.html`
Expected: 1

Run: `grep -c 'custom.css' TwTxGNN/docs/_includes/head_custom.html`
Expected: 1

Run: `grep -c '<style>' TwTxGNN/docs/_includes/head_custom.html`
Expected: 0（head_custom.html 中不應再有 style 標籤）

- [ ] **Step 4: Commit**

```bash
cd /Users/lightman/yao.care/TxGNN/TwTxGNN
git add docs/_includes/head_custom.html
git commit -m "feat(security): add CSP meta tag, replace inline styles with external CSS"
```

---

### Task 3: 建立 ZAP rules config

**Files:**
- Create: `TwTxGNN/docs/.zap/rules.tsv`

- [ ] **Step 1: 建立 rules.tsv**

```tsv
# ZAP Rules Configuration for TwTxGNN (GitHub Pages)
# 以下項目因 GitHub Pages 無法設定 HTTP 回應標頭，降為 WARN
# 參考：https://www.zaproxy.org/docs/docker/baseline-scan/#rules-file-format
#
# 格式：<rule_id>\t<action>\t<description>
# WARN = 報告但不算 failure

10020	WARN	(X-Frame-Options Header - GitHub Pages cannot set HTTP headers)
10021	WARN	(X-Content-Type-Options Header - GitHub Pages cannot set HTTP headers)
10027	WARN	(Information Disclosure - Suspicious Comments - normal code comments)
10035	WARN	(Strict-Transport-Security - GitHub Pages cannot set HTTP headers)
10063	WARN	(Permissions Policy Header - GitHub Pages cannot set HTTP headers)
10098	WARN	(Cross-Domain Misconfiguration - CORS controlled by GitHub CDN)
90004	WARN	(Cross-Origin-Embedder-Policy - GitHub Pages cannot set HTTP headers)
90005	WARN	(Cross-Origin-Opener-Policy - GitHub Pages cannot set HTTP headers)
```

- [ ] **Step 2: 確認格式（tab-separated）**

Run: `cat -A TwTxGNN/docs/.zap/rules.tsv | grep '^10020'`
Expected: 含 `^I`（tab character）分隔欄位

- [ ] **Step 3: Commit**

```bash
cd /Users/lightman/yao.care/TxGNN/TwTxGNN
git add docs/.zap/rules.tsv
git commit -m "feat(security): add ZAP rules config for GitHub Pages limitations"
```

---

### Task 4: Push TwTxGNN 並驗證

**Files:** 無新建

- [ ] **Step 1: Push**

```bash
cd /Users/lightman/yao.care/TxGNN/TwTxGNN
git push
```

- [ ] **Step 2: 等待 GitHub Pages 部署完成**

Run: `gh -R yao-care/TwTxGNN run list --workflow=pages.yml --limit=1`
Expected: 顯示最新一次 run，狀態為 completed/success

- [ ] **Step 3: 測試頁面（瀏覽器 Console 檢查）**

手動開啟以下 URL，F12 開 Console 確認無 CSP violation：
1. https://twtxgnn.yao.care/
2. https://twtxgnn.yao.care/drugs/acebutolol/
3. https://twtxgnn.yao.care/smart/standalone.html
4. 首頁捲到底部確認 Giscus 載入

如果有 CSP violation：
- 記錄被阻擋的來源
- 回到 Task 2 Step 1 修改 CSP 政策加入該來源
- 若是 just-the-docs 主題的 inline style，改為 `style-src 'self' 'unsafe-inline'`

- [ ] **Step 4: 確認 CSP header 存在**

Run: `curl -sI https://twtxgnn.yao.care/ | grep -i content-security`
Expected: 無輸出（因為是 meta tag，不是 HTTP header）

Run: `curl -s https://twtxgnn.yao.care/ | grep -o 'Content-Security-Policy'`
Expected: `Content-Security-Policy`

---

### Task 5: 建立同步腳本並執行

**Files:**
- Create: `/Users/lightman/yao.care/TxGNN/.claude/sync_security_headers.sh`

- [ ] **Step 1: 建立同步腳本**

```bash
#!/bin/bash
# Sync security headers (CSP + external CSS + ZAP rules) from TwTxGNN to all country projects.
# Usage:
#   bash .claude/sync_security_headers.sh            # sync all
#   bash .claude/sync_security_headers.sh UsTxGNN    # sync one
#   bash .claude/sync_security_headers.sh --dry-run  # preview

set -euo pipefail
cd /Users/lightman/yao.care/TxGNN

REF_DIR="TwTxGNN"
DRY_RUN=false

# Parse args
TARGETS=()
for arg in "$@"; do
    if [[ "$arg" == "--dry-run" ]]; then
        DRY_RUN=true
    else
        TARGETS+=("$arg")
    fi
done

# If no targets specified, discover all projects
if [[ ${#TARGETS[@]} -eq 0 ]]; then
    for proj in $(ls -d *TxGNN 2>/dev/null | sort); do
        [[ "$proj" == "$REF_DIR" ]] && continue
        TARGETS+=("$proj")
    done
fi

echo "=== Sync Security Headers ($(date '+%Y-%m-%d %H:%M')) ==="
echo "Reference: $REF_DIR"
echo "Targets: ${#TARGETS[@]} projects"
echo "Dry run: $DRY_RUN"
echo "------------------------------------------------------------"

synced=0
skipped=0

for proj in "${TARGETS[@]}"; do
    docs_dir="$proj/docs"
    if [[ ! -d "$docs_dir" ]]; then
        echo "  [SKIP] $proj — docs/ not found"
        ((skipped++))
        continue
    fi

    changed=0

    # --- 1. Copy custom.css ---
    css_dir="$docs_dir/assets/css"
    css_file="$css_dir/custom.css"
    ref_css="$REF_DIR/docs/assets/css/custom.css"
    if [[ -f "$ref_css" ]]; then
        if [[ ! -f "$css_file" ]] || ! diff -q "$ref_css" "$css_file" > /dev/null 2>&1; then
            if $DRY_RUN; then
                echo "  [dry-run] $proj: Would copy custom.css"
            else
                mkdir -p "$css_dir"
                cp "$ref_css" "$css_file"
            fi
            ((changed++))
        fi
    fi

    # --- 2. Copy .zap/rules.tsv ---
    zap_dir="$docs_dir/.zap"
    zap_file="$zap_dir/rules.tsv"
    ref_zap="$REF_DIR/docs/.zap/rules.tsv"
    if [[ -f "$ref_zap" ]]; then
        if [[ ! -f "$zap_file" ]] || ! diff -q "$ref_zap" "$zap_file" > /dev/null 2>&1; then
            if $DRY_RUN; then
                echo "  [dry-run] $proj: Would copy .zap/rules.tsv"
            else
                mkdir -p "$zap_dir"
                cp "$ref_zap" "$zap_file"
            fi
            ((changed++))
        fi
    fi

    # --- 3. Update head_custom.html ---
    head_file="$docs_dir/_includes/head_custom.html"
    if [[ -f "$head_file" ]]; then
        # 3a. Add CSP meta tag if not present
        if ! grep -q 'Content-Security-Policy' "$head_file" 2>/dev/null; then
            if $DRY_RUN; then
                echo "  [dry-run] $proj: Would add CSP meta tag"
            else
                sed -i '' '1i\
<!-- Security: Content Security Policy -->\
<meta http-equiv="Content-Security-Policy" content="default-src '"'"'self'"'"'; script-src '"'"'self'"'"' https://d3js.org https://cdn.jsdelivr.net https://giscus.app; style-src '"'"'self'"'"'; img-src '"'"'self'"'"' data: https:; connect-src '"'"'self'"'"' https://rxnav.nlm.nih.gov https://giscus.app; frame-src https://giscus.app; font-src '"'"'self'"'"';">\
\
<!-- Custom styles (extracted from inline) -->\
<link rel="stylesheet" href="{{ '"'"'/assets/css/custom.css'"'"' | relative_url }}">\
' "$head_file"
            fi
            ((changed++))
        fi

        # 3b. Remove SGE/AEO <style> block if present
        if grep -q 'SGE/AEO' "$head_file" 2>/dev/null; then
            if $DRY_RUN; then
                echo "  [dry-run] $proj: Would remove SGE/AEO style block"
            else
                sed -i '' '/<!-- SGE\/AEO 支援樣式 -->/,/<\/style>/d' "$head_file"
            fi
            ((changed++))
        fi
    fi

    # --- Summary ---
    if [[ $changed -gt 0 ]]; then
        echo "  [SYNC] $proj — $changed change(s)"
        ((synced++))
    else
        echo "  [ OK ] $proj — already up to date"
    fi
done

echo "------------------------------------------------------------"
echo "Done: $synced synced, $skipped skipped (total ${#TARGETS[@]} projects)"
echo ""
echo "Next steps:"
echo "  1. Review changes: cd /Users/lightman/yao.care/TxGNN && for p in *TxGNN; do echo \"--- \$p ---\"; cd \$p; git diff --stat; cd ..; done"
echo "  2. Commit all: for p in *TxGNN; do cd \$p; git add -A && git commit -m 'feat(security): add CSP + external CSS + ZAP rules' && git push; cd ..; done"
```

- [ ] **Step 2: Dry run 測試**

Run: `bash .claude/sync_security_headers.sh --dry-run`
Expected: 列出 29 個項目，每個顯示 would copy/add/remove

- [ ] **Step 3: 正式執行**

Run: `bash .claude/sync_security_headers.sh`
Expected: 29 個項目全部 SYNC

- [ ] **Step 4: 批次 commit + push**

```bash
cd /Users/lightman/yao.care/TxGNN
for proj in $(ls -d *TxGNN | sort); do
    [[ "$proj" == "TwTxGNN" ]] && continue
    cd "$proj"
    git add docs/assets/css/custom.css docs/.zap/rules.tsv docs/_includes/head_custom.html
    git commit -m "feat(security): add CSP meta tag, external CSS, ZAP rules config" || true
    git push || true
    cd ..
done
```

- [ ] **Step 5: Commit 同步腳本本身**

```bash
cd /Users/lightman/yao.care/TxGNN
git add .claude/sync_security_headers.sh
git commit -m "feat: add security headers sync script"
```
