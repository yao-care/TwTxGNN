#!/usr/bin/env python3
"""docs 的 SEO 結構守門 —— 給 seo-ops 反思／大腦的自動改動當 gate。

為什麼需要這支（2026-09-22 建）：
  本站 docs/ 由 GitHub Pages 建置，主機上沒有 ruby／bundler／jekyll，也沒有 lychee，
  所以沒有任何可在本機執行的建置或連結檢查。而 seo-ops 的紅線是「開了自動改動就必須
  有 gates，且 gate 要與該層的 scope 相關」。這支只查「reflect/brain 的 scope 改壞了
  卻不會有畫面症狀」的那幾件事：

    1. 關鍵 permalink 還在（改掉或刪掉 permalink＝該網址靜默 404，站內連結與 llms.txt
       仍指向舊網址，Google 那邊變成整頁消失）。
    2. llms.txt／llms-full.txt 列的自站網址都對得上實際 permalink（AI 引用的入口清單）。
    3. head_custom.html 的 GA4 評量 ID 還在、script 標籤成對、每個 ld+json 區塊仍是
       合法 JSON（結構化資料壞掉不會影響版面，只會讓 rich result 消失）。
    4. docs/*.md 的站內連結指到存在的 permalink 或實際檔案。

用法：python3 scripts/check_seo_docs.py      # 非零＝不通過
"""
import json
import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"
GA4_ID = "G-W7ZNBYKJHJ"
SITE = "https://twtxgnn.yao.care"

# 這些網址是 llms.txt 對外宣告的入口與導覽骨架，少一個就是站台結構被改壞。
CRITICAL = ["/", "/drugs/", "/methodology/", "/guide/", "/sources/", "/downloads/",
            "/about/", "/news/", "/nav-drugs/", "/nav-safety/", "/nav-help/", "/nav-resources/"]

errors = []


def redirect_paths(text):
    """front matter 的 redirect_from 清單（jekyll-redirect-from 產的舊網址，實測線上回 200）。"""
    if not text.startswith("---"):
        return []
    end = text.find("\n---", 3)
    if end < 0:
        return []
    out, collecting = [], False
    for line in text[3:end].splitlines():
        if re.match(r"^redirect_from:\s*$", line):
            collecting = True
            continue
        if collecting:
            m = re.match(r"^\s*-\s*(\S+)\s*$", line)
            if m:
                out.append(m.group(1).strip('"').strip("'"))
                continue
            collecting = False
        m = re.match(r"^redirect_from:\s*(\S+)\s*$", line)
        if m:
            out.append(m.group(1).strip('"').strip("'"))
    return out


def front_matter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    out = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return out


# 收集全站 permalink
permalinks = set()
redirects = set()          # jekyll-redirect-from 的舊網址也是有效目標
for md in DOCS.rglob("*.md"):
    text = md.read_text(encoding="utf-8", errors="replace")
    fm = front_matter(text)
    if fm.get("permalink"):
        permalinks.add(fm["permalink"].rstrip("/") + "/" if fm["permalink"] != "/" else "/")
    redirects.update(redirect_paths(text))

# 1) 關鍵 permalink
for p in CRITICAL:
    if p not in permalinks:
        errors.append(f"關鍵 permalink 消失：{p}（llms.txt 與導覽都指向它）")

# 2) llms.txt 內的自站網址
for name in ("llms.txt", "llms-full.txt"):
    f = DOCS / name
    if not f.exists():
        errors.append(f"{name} 不存在（AI 引用入口清單）")
        continue
    for url in re.findall(r"https?://[^\s)\]]+", f.read_text(encoding="utf-8", errors="replace")):
        if not url.startswith(SITE):
            continue
        path = url[len(SITE):] or "/"
        path = path.split("#")[0].split("?")[0]
        if not path.endswith("/"):
            path += "/"
        if path not in permalinks:
            errors.append(f"{name} 指向不存在的網址：{url}")

# 3) head_custom.html
head = DOCS / "_includes" / "head_custom.html"
if not head.exists():
    errors.append("_includes/head_custom.html 不存在（GA4 與全部結構化資料都在裡面）")
else:
    t = head.read_text(encoding="utf-8", errors="replace")
    if GA4_ID not in t:
        errors.append(f"head_custom.html 不再含 GA4 評量 ID {GA4_ID}（改壞了不會有畫面症狀，數據直接歸零）")
    if t.count("<script") != t.count("</script>"):
        errors.append(f"head_custom.html 的 script 標籤不成對（{t.count('<script')} 開 / {t.count('</script>')} 閉）")
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S)
    if not blocks:
        errors.append("head_custom.html 找不到任何 ld+json 區塊（結構化資料全失）")
    for i, b in enumerate(blocks, 1):
        try:
            json.loads(b)
        except Exception as e:
            errors.append(f"head_custom.html 第 {i} 個 ld+json 不是合法 JSON：{e}")

# 4) docs/*.md 的站內連結
for md in sorted(DOCS.glob("*.md")):
    text = md.read_text(encoding="utf-8", errors="replace")
    for link in re.findall(r"\]\((/[^)\s]*)\)", text):
        path = link.split("#")[0].split("?")[0]
        if not path or path.startswith("/assets/"):
            continue
        if path in permalinks or (path.rstrip("/") + "/") in permalinks:
            continue
        if path in redirects or path.rstrip("/") in redirects:
            continue
        if (DOCS / path.lstrip("/")).exists():
            continue
        errors.append(f"{md.name} 的站內連結指不到東西：{link}")

if errors:
    print(f"docs SEO 守門：✗ {len(errors)} 項")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print(f"docs SEO 守門：✓ {len(permalinks)} 個 permalink、關鍵入口 {len(CRITICAL)} 個齊全、"
      f"llms 清單對得上、head_custom 的 GA4 與 ld+json 完好、"
      f"站內連結無斷點（含 {len(redirects)} 條 redirect_from 舊網址）")
