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
       permalink 含 collection 文件（_drugs/、_news/）：照 _config.yml 的
       `permalink: /drugs/:name/` 樣板＋Jekyll slugify 推導（2026-10-03 補）。
    6. 藥物頁的許可證字號都屬於該藥（TFDA 快照）、許可證表是程式產生的、張數一致、
       沒有產線開場白與「Evidence Pack」用語；被 superseded 的查核紀錄確認屬於本藥的字號
       （asserted_license_ids）必須都在程式表裡（2026-10-03 補）。
    7. 藥物頁頁首等級＝快速總覽證據等級列的最高等級；表格前面不缺空行（2026-10-04 補）。
    5. docs/_data/drug_reviews.json 的人工查核紀錄（更正／加註／待重審／附來源段落）
       都還套在藥物頁上（產線重產會蓋掉；修法：python3 scripts/apply_drug_reviews.py）。

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


def jekyll_slugify(s):
    """Jekyll Utils.slugify 的預設模式：非英數（含底線）連成一個 '-'、去頭尾 '-'、轉小寫。
    實測線上 /drugs/magnesium-sulfate/ 回 200、/drugs/magnesium_sulfate/ 回 404（檔名 magnesium_sulfate.md）。"""
    return re.sub(r"[\W_]+", "-", s).strip("-").lower()


def collection_rules():
    """從 _config.yml 的 collections: 區塊讀 {名稱: permalink 樣板}，只取 output: true 的。
    本機無 PyYAML，用縮排解析；只認得這種兩層結構，讀不到就回空（不影響其他檢查）。"""
    cfg = DOCS / "_config.yml"
    if not cfg.exists():
        return {}
    rules, cur, inside = {}, None, False
    for line in cfg.read_text(encoding="utf-8", errors="replace").splitlines():
        if re.match(r"^collections:\s*$", line):
            inside = True
            continue
        if not inside:
            continue
        if line.strip() == "" or line.lstrip().startswith("#"):
            continue
        if not line.startswith(" "):
            break
        m = re.match(r"^  ([A-Za-z_][\w-]*):\s*$", line)
        if m:
            cur = m.group(1)
            rules[cur] = {}
            continue
        m = re.match(r"^\s{4,}(output|permalink):\s*(\S+)\s*$", line)
        if m and cur:
            rules[cur][m.group(1)] = m.group(2).strip('"').strip("'")
    return {k: v["permalink"] for k, v in rules.items()
            if v.get("output") == "true" and v.get("permalink")}


# collection 文件（_drugs 等）的網址：照 _config.yml 的 permalink 樣板推導，
# 文件自己的 front matter permalink 優先（上面已收）。2026-10-03 補：之前漏掉這塊，
# nct-lookup.md／tw-availability.md 連到 /drugs/* 的 672 條連結全被誤判成斷連結。
for cname, pattern in collection_rules().items():
    if re.search(r":(?!name\b)\w+", pattern):
        errors.append(f"_config.yml collection {cname} 的 permalink {pattern} 含本 gate 不認得的變數（只支援 :name），請擴充 check_seo_docs.py")
        continue
    for f in (DOCS / f"_{cname}").glob("*"):
        if f.suffix not in (".md", ".markdown", ".html"):
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        if front_matter(text).get("permalink"):
            continue
        url = pattern.replace(":name", jekyll_slugify(f.stem))
        permalinks.add(url if url.endswith("/") else url + "/")

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

# 5) 藥物頁人工查核紀錄（docs/_data/drug_reviews.json）都還套在頁面上（2026-10-03 補）：
#    藥物頁是產線重產的，重產會蓋掉更正與加註；沒重套就擋下。
sys.path.insert(0, str(Path(__file__).resolve().parent))
from apply_drug_reviews import check_errors  # noqa: E402
errors.extend(check_errors())

# 6) 藥物頁的許可證字號與張數（2026-10-03 補）：每個許可證字號都必須是該藥主成分相符的 TFDA
#    許可證（依 snapshots/tfda_licenses.json.gz）；許可證表必須是程式產生的區塊、張數與快照一致；
#    不得殘留產線開場白或「Evidence Pack」內部用語。修法：python3 scripts/regenerate_tfda_tables.py
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from twtxgnn.regulatory import tfda_licenses as _T  # noqa: E402
from twtxgnn.regulatory.page_postprocess import strip_preamble as _strip  # noqa: E402
_snap = (_T.load_snapshot().get("drugs") or {})
for md in sorted((DOCS / "_drugs").glob("*.md")):
    text = md.read_text(encoding="utf-8", errors="replace")
    entry = _snap.get(md.stem)
    if entry is None:
        errors.append(f"{md.name}：TFDA 許可證快照沒有這一頁（跑 scripts/regenerate_tfda_tables.py）")
        continue
    lics = entry["licenses"]
    bad = _T.validate_page(text, {x["id"] for x in lics})
    if bad:
        errors.append(f"{md.name}：頁面上有不屬於本藥（或 TFDA 查無）的許可證字號 {bad[:5]}")
    if _T.BEGIN not in text:
        errors.append(f"{md.name}：許可證表不是程式產生的區塊")
    m = re.search(r"^\|\s*許可證數\s*\|([^|\n]*)\|", text, re.M)
    if m and m.group(1).strip() != _T.count_text(_T.summarize(lics)):
        errors.append(f"{md.name}：「許可證數」與 TFDA 快照不符（{m.group(1).strip()}）")
    if _strip(text) != text:
        errors.append(f"{md.name}：報告開頭殘留產線開場白")
    if "Evidence Pack" in text:
        errors.append(f"{md.name}：殘留「Evidence Pack」內部用語")
# 6b) 被 superseded 的查核紀錄寫明「屬於本藥」的字號，程式表必須包含（防比對漏同義名把錯寫回去）
_rev = DOCS / "_data" / "drug_reviews.json"
if _rev.exists():
    for _r in json.loads(_rev.read_text(encoding="utf-8"))["records"]:
        _ids = set(_r.get("asserted_license_ids") or [])
        _entry = _snap.get(_r["file"][:-3])
        if _ids and _entry is not None:
            _miss = _ids - {x["id"] for x in _entry["licenses"]}
            if _miss:
                errors.append(f"{_r['file']}：查核紀錄 {_r['id']} 確認屬於本藥的字號 {sorted(_miss)} 不在程式產生的許可證表裡"
                              "（比對規則漏了同義名？補 config/tfda_synonyms.json 後重跑 scripts/regenerate_tfda_tables.py）")

# 7) 藥物頁格式（2026-10-04 補）：頁首等級（front matter evidence_level、parent、頁首「證據等級」列）
#    必須等於「快速總覽」證據等級列的最高等級；表格第一列前面必須是空行（否則 kramdown 排成純文字）。
#    規則與修法都在 src/twtxgnn/regulatory/page_format.py；修法：python3 scripts/regenerate_tfda_tables.py
from twtxgnn.regulatory import page_format as _F  # noqa: E402
for md in sorted((DOCS / "_drugs").glob("*.md")):
    text = md.read_text(encoding="utf-8", errors="replace")
    for e in _F.header_problems(text):
        errors.append(f"{md.name}：頁首等級與快速總覽不一致：{e}")
    for e in _F.table_spacing_problems(text):
        errors.append(f"{md.name}：{e}")
# 7b) 吃等級的衍生檔要跟頁首一致（重產頁面後忘了重產衍生檔就擋）
_fm_level = {}
for md in (DOCS / "_drugs").glob("*.md"):
    _m = re.search(r"^evidence_level:[ \t]*(L[1-5])", md.read_text(encoding="utf-8", errors="replace")[:2000], re.M)
    if _m:
        _fm_level[md.stem] = _m.group(1)
_DERIVED = [("_data/drug_stats.json", "all_drugs", "level", "scripts/generate_drug_stats.py"),
            ("data/drugs.json", "drugs", "evidence_level", "scripts/generate_data_exports.py"),
            ("downloads/twtxgnn_drugs_summary.json", "drugs", "evidence_level", "scripts/generate_download_data.py"),
            ("data/search-index.json", "drugs", "level", "scripts/generate_search_index.py --levels-from-pages")]
def _slug_of(r):
    if r.get("slug"):
        return r["slug"]
    _u = re.match(r"/drugs/([^/]+)/", r.get("url") or "")
    return _u.group(1) if _u else None


for _rel, _key, _fld, _fix in _DERIVED:
    _f = DOCS / _rel
    if not _f.exists():
        continue
    _rows = {_slug_of(r): r for r in (json.loads(_f.read_text(encoding="utf-8")).get(_key) or [])}
    _bad = sorted(s for s, r in _rows.items() if s in _fm_level and r.get(_fld) != _fm_level[s])
    _missing = sorted(set(_fm_level) - set(_rows))
    if _bad or _missing:
        errors.append(f"{_rel}：等級與藥物頁頁首不一致 {_bad[:5]}、缺 {_missing[:5]}（跑 {_fix}）")

if errors:
    print(f"docs SEO 守門：✗ {len(errors)} 項")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print(f"docs SEO 守門：✓ {len(permalinks)} 個 permalink、關鍵入口 {len(CRITICAL)} 個齊全、"
      f"llms 清單對得上、head_custom 的 GA4 與 ld+json 完好、"
      f"站內連結無斷點（含 {len(redirects)} 條 redirect_from 舊網址）")
