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
    7. 藥物頁頁首等級＝快速總覽證據等級列的最高等級（主預測重審撤回時＝其他預測表保留的最高等級，沒有就 N/A，2026-11-03 補）；
       front matter description 提到的「證據等級 Lx」＝頁首等級（2026-11-03 補）；
       重審撤回的預測不在 search-index 與 FHIR（7d，2026-11-03 補）；FHIR 的 MedicationKnowledge 等級＝頁首、
       Bundle／metadata 數字＝實際檔案（7e，2026-11-03 補）；表格前後不缺空行（表格後 2026-11-03 補）；吃等級的衍生檔與頁首一致；
       不能用 Liquid 的寫死藥物數／等級分布等於 drug_stats.json（2026-10-04 補）。
    5. docs/_data/drug_reviews.json 的人工查核紀錄（更正／加註／待重審／附來源段落）
       都還套在藥物頁上（產線重產會蓋掉；修法：python3 scripts/apply_drug_reviews.py）。
    8. docs/nav-*.md、evidence-*.md、drugs.md 不寫死該由 drug_stats.json 來的藥物總數、等級分布條寬度、等級藥物數（2026-11-03）。
    9. llms.txt／llms-full.txt 範例藥物行「名稱 (Lx): 網址」的標籤＝藥物頁 evidence_level，且不指向轉址／noindex／不存在的頁（2026-11-03）。

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
            # 未加引號的 {{ … | jsonify }} 會輸出合法 JSON 值，驗證時以字串代入（2026-10-17）
            json.loads(re.sub(r'(:\s*)\{\{[^}]*\}\}', r'\1"x"', b))
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
    if 'http-equiv="refresh"' in text:
        continue  # 轉址頁（2026-10-17）
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
#    必須等於「快速總覽」證據等級列的最高等級；表格第一列前面、最後一列後面必須是空行（否則 kramdown 排成純文字）。
#    規則與修法都在 src/twtxgnn/regulatory/page_format.py；修法：python3 scripts/regenerate_tfda_tables.py
from twtxgnn.regulatory import page_format as _F  # noqa: E402
for md in sorted((DOCS / "_drugs").glob("*.md")):
    text = md.read_text(encoding="utf-8", errors="replace")
    if 'http-equiv="refresh"' in text:
        continue  # 轉址頁（2026-10-17）
    for e in _F.header_problems(text):
        errors.append(f"{md.name}：頁首等級與快速總覽不一致：{e}")
    for e in _F.description_level_problems(text):  # 2026-11-03：description 的等級＝頁首等級
        errors.append(f"{md.name}：{e}")
    for e in _F.table_spacing_problems(text):
        errors.append(f"{md.name}：{e}")
# 7b) 吃等級的衍生檔要跟頁首一致（重產頁面後忘了重產衍生檔就擋）
_fm_level = {}
for md in (DOCS / "_drugs").glob("*.md"):
    _head = md.read_text(encoding="utf-8", errors="replace")[:2000]
    _m = re.search(r"^evidence_level:[ \t]*(L[1-5]|N/A)", _head, re.M)
    if _m and not re.search(r"^noindex:[ \t]*true", _head, re.M):  # noindex 頁不進衍生檔（2026-10-17）
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

# 7d) 重審撤回的預測（drug_reviews.json verdict=withdraw）不能留在搜尋索引與 FHIR（2026-11-03 用戶決定）
from twtxgnn.regulatory import withdrawn as _Wd  # noqa: E402
_wd = _Wd.load()
_si = DOCS / "data" / "search-index.json"
if _wd and _si.exists():
    _left = sorted((d.get("slug"), i.get("name")) for d in json.loads(_si.read_text(encoding="utf-8")).get("drugs", [])
                   for i in d.get("indications") or [] if _Wd.is_withdrawn(_wd, d.get("slug"), i.get("name")))
    if _left:
        errors.append(f"search-index.json 仍有重審撤回的預測 {_left[:5]}（跑 scripts/generate_search_index.py --levels-from-pages）")
if _wd and (DOCS / "fhir" / "ClinicalUseDefinition").is_dir():
    sys.path.insert(0, str(DOCS.parent / "scripts"))
    from generate_fhir_resources import _cud_key  # noqa: E402
    _left = sorted(f.name for f in (DOCS / "fhir" / "ClinicalUseDefinition").glob("*.json")
                   if _Wd.is_withdrawn(_wd, *_cud_key(json.loads(f.read_text(encoding="utf-8")))))
    _b = DOCS / "fhir" / "Bundle" / "all-predictions.json"
    if _b.exists():
        _left += sorted(e["resource"].get("id", "") for e in json.loads(_b.read_text(encoding="utf-8")).get("entry", [])
                        if e.get("resource", {}).get("resourceType") == "ClinicalUseDefinition"
                        and _Wd.is_withdrawn(_wd, *_cud_key(e["resource"])))
    if _left:
        errors.append(f"FHIR 仍有重審撤回的預測 {_left[:5]}（跑 scripts/generate_fhir_resources.py --prune-withdrawn）")

# 7e) FHIR 不能跟頁面、實際檔案脫節（2026-11-03 用戶決定）：MedicationKnowledge 等級＝藥物頁頁首（含 N/A）、不含 noindex／轉址頁的藥、
#     Bundle 與資源檔一致且 total＝entry 數、metadata 的藥物數／適應症數＝檔案數
if (DOCS / "fhir" / "MedicationKnowledge").is_dir():
    sys.path.insert(0, str(DOCS.parent / "scripts"))
    from generate_fhir_resources import fhir_problems as _fhir_problems  # noqa: E402
    errors.extend(f"FHIR：{e}（跑 scripts/generate_fhir_resources.py --sync-from-files）"
                  for e in _fhir_problems(DOCS / "fhir", DOCS / "_drugs"))

# 7c) 不能用 Liquid 的寫死藥物數／等級分布（front matter description、ld+json numberOfItems、README、CITATION…）
#     必須等於 drug_stats.json（2026-10-04 補）。清單與修法：scripts/generate_drug_stats.py 的 COUNT_SPOTS。
from generate_drug_stats import count_spot_problems as _count_spots  # noqa: E402
_stats_path = DOCS / "_data" / "drug_stats.json"
if _stats_path.exists():
    _stats = json.loads(_stats_path.read_text(encoding="utf-8"))
    # 2026-10-28：已知用途頁（evidence_level N/A）也是公開藥物報告，總數要算進去
    # 2026-11-03：_fm_level 已含 N/A 頁（主預測重審撤回的頁也是 N/A），衍生檔一併比對
    _n_public = len(_fm_level)
    if _stats.get("total_drugs") != _n_public:
        errors.append(f"drug_stats.json total_drugs={_stats.get('total_drugs')}，藥物頁 {_n_public} 頁（跑 scripts/generate_drug_stats.py）")
    errors.extend(f"寫死的藥物數：{e}（跑 scripts/generate_drug_stats.py）" for e in _count_spots(_stats))
# 8) 導覽頁與等級列表頁不得寫死該由 docs/_data/drug_stats.json 來的數字（2026-11-03 補）：
#    docs/nav-*.md 的藥物／報告總數、等級分布條（dist-high／dist-medium／dist-low）的寬度、等級卡片的藥物數，
#    以及 nav-*.md、evidence-*.md、drugs.md 等級表（| L1-L2 | 數字 |）的藥物數。nav-*.md 曾被自動化層寫入
#    寫死的數字後過期（MyTxGNN 2026-11-03：寫 799 份、14%／5%／81%，實際 606 份）。
#    修法：內文改用 Liquid 讀 site.data.drug_stats（total_drugs、level_counts，百分比在 Liquid 裡算）；
#    front matter description 不能用 Liquid，不寫數字（非寫不可就列進 scripts/generate_drug_stats.py 的 COUNT_SPOTS 由它同步）。
import generate_drug_stats as _gds_nav  # noqa: E402
_NAV_W = (r"(?:drugs?|medicines?|medications?|ubat|medicamentos?|fármacos?|farmacos?|arzneimittel\w*|lægemidl\w*|"
          r"geneesmiddel\w*|läkemed\w*|legemid\w*|lääk\w*|médicaments?|farmaci|藥物?|药物?|薬|医薬品|약물|의약품|ยา|أدوية|دواء|"
          r"reports?|relatórios?|informes?|rapports?|berichte\w*|rapporter|rapporten|rapporti|laporan|รายงาน|レポート|報告|报告|보고서)")
_NAV_N = r"(?<![A-Za-z\d.,/#:\-])(\d{1,3}(?:[,.]\d{3})+|\d{2,5})(?![A-Za-z\d%.,/])"
_NAV_HARD = re.compile(_NAV_N + r"[^\d\n]{0,12}?" + _NAV_W + "|" + _NAV_W + r"[^\d\n]{0,40}?" + _NAV_N, re.I)
_NAV_MASK = re.compile(r"\{\{.*?\}\}|\{%.*?%\}|<[^>\n]*>|https?://\S+|&#?\w+;", re.S)
_NAV_BAR = re.compile(r"<[^>]*\bdist-(?:high|medium|low|l[1-5])\b[^>]*>", re.I)
_NAV_CARD = re.compile(r'class="drug-card-count">\s*([\d][\d,.]*)\s*<', re.I)
_NAV_LVROW = re.compile(r"^\|\s*\**L[1-5](?:\s*[-–~]\s*L[1-5])?\**\s*\|\s*\**(\d[\d,.]*)\**\s*\|", re.M)
_nav_spots = {}
for _sp in _gds_nav.COUNT_SPOTS:
    _nav_spots.setdefault(_sp[0], []).append(_sp[1])
for _f in sorted(DOCS.glob("nav-*.md")) + sorted(DOCS.glob("evidence-*.md")) + [DOCS / "drugs.md"]:
    if not _f.exists():
        continue
    _t = _f.read_bytes().decode("utf-8", errors="replace")
    _ln = lambda i: _t.count("\n", 0, i) + 1  # noqa: E731
    _bad = []
    for _m in _NAV_BAR.finditer(_t):
        _w = re.search(r"width:\s*([^;\"']+)", _m.group(0))
        if _w and "{{" not in _w.group(1):
            _bad.append(f"{_ln(_m.start())} 行等級分布條寬度寫死 {_w.group(1).strip()}")
    _bad += [f"{_ln(_m.start())} 行等級卡片寫死 {_m.group(1)}" for _m in _NAV_CARD.finditer(_t)]
    _bad += [f"{_ln(_m.start())} 行等級表寫死 {_m.group(1)}" for _m in _NAV_LVROW.finditer(_t)]
    if _f.name.startswith("nav-") and _f.name != "nav-safety.md":  # nav-safety 的數字是 DDInter 等安全性資料集的規模，不是 drug_stats
        _skip = [(_m.start(), _m.end()) for _p in _nav_spots.get(f"docs/{_f.name}", [])
                 for _m in re.finditer(_p, _t, re.M)]  # COUNT_SPOTS 管的位置（腳本同步）不算
        _masked = _NAV_MASK.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), _t)
        for _m in _NAV_HARD.finditer(_masked):
            _num = (_m.group(1) or _m.group(2)).replace(",", "").replace(".", "")
            if int(_num) < 50 or 1990 <= int(_num) <= 2099 or any(a <= _m.start() < b for a, b in _skip):
                continue  # 個位數／每藥前 N 筆之類的小數字、年份不是藥物總數
            _bad.append(f"{_ln(_m.start())} 行寫死的藥物／報告數「{' '.join(_m.group(0).split())}」")
    errors.extend(f"{_f.name}：{b}（改用 site.data.drug_stats 的 Liquid；description 不寫數字）" for b in _bad)

# 9) llms.txt／llms-full.txt 的範例藥物行「- 名稱 (Lx): 網址」（2026-11-03 補）：標籤＝該藥物頁 front matter 的
#    evidence_level，且網址指到存在的藥物頁、不是 ID 轉址頁、不是 noindex 頁（藥物頁重新評級後標籤會過期，
#    NZTxGNN 等站曾發生）。修法：母目錄 python3 .claude/sync_llms_descriptions.py <站> 會依頁面同步標籤；
#    指到轉址／noindex／不存在頁的行要人工換一個藥。
_LLM_LINE = re.compile(r"^\s*[-*]\s*(.+?)\s*\((L[1-5]|N/A)\)\s*:\s*(https?://\S+?)\s*$", re.M)
_llm_pages, _llm_prefix = {}, []
for _cn, _pat in collection_rules().items():
    if _cn != "drugs":
        continue
    _llm_prefix.append(_pat.split(":")[0])
    for _f in (DOCS / "_drugs").glob("*.md"):
        _t = _f.read_text(encoding="utf-8", errors="replace")
        _fm = front_matter(_t)
        _u = _fm.get("permalink") or re.sub(r":(name|slug|title)\b", jekyll_slugify(_fm.get("slug") or _f.stem), _pat)
        _llm_pages[_u.rstrip("/") + "/"] = (_fm, 'http-equiv="refresh"' in _t)
for _name in ("llms.txt", "llms-full.txt"):
    _f = DOCS / _name
    if not _f.exists():
        continue
    for _m in _LLM_LINE.finditer(_f.read_text(encoding="utf-8", errors="replace")):
        _url, _lv = _m.group(3), _m.group(2)
        if not _url.startswith(SITE):
            continue
        _path = (_url[len(SITE):].split("#")[0].split("?")[0] or "/").rstrip("/") + "/"
        if not any(_path.startswith(p) for p in _llm_prefix):
            continue  # 不是藥物頁（如 /evidence-low/ 的等級說明行）
        if _path not in _llm_pages:
            errors.append(f"{_name}：「{_m.group(1)} ({_lv})」指到不存在的藥物頁 {_url}（換一個藥）")
            continue
        _fm, _refresh = _llm_pages[_path]
        if _fm.get("layout") == "id_redirect" or _refresh or _fm.get("redirect_to"):
            errors.append(f"{_name}：「{_m.group(1)} ({_lv})」指到轉址頁 {_url}（換一個藥）")
        elif _fm.get("noindex", "").lower() == "true":
            errors.append(f"{_name}：「{_m.group(1)} ({_lv})」指到 noindex 頁 {_url}（換一個藥）")
        elif _fm.get("evidence_level", "") != _lv:
            errors.append(f"{_name}：「{_m.group(1)} ({_lv})」標籤與頁面 evidence_level {_fm.get('evidence_level') or '（無）'} 不符"
                          f"（跑母目錄 .claude/sync_llms_descriptions.py）")

if errors:
    print(f"docs SEO 守門：✗ {len(errors)} 項")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print(f"docs SEO 守門：✓ {len(permalinks)} 個 permalink、關鍵入口 {len(CRITICAL)} 個齊全、"
      f"llms 清單對得上、head_custom 的 GA4 與 ld+json 完好、"
      f"站內連結無斷點（含 {len(redirects)} 條 redirect_from 舊網址）")
