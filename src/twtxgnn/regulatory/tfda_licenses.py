"""台灣許可證（TFDA）資料的確定性處理：比對、計數、產表、驗證。

為什麼有這個模組（2026-10-03 建）：
  藥物頁的「許可證數」與許可證表原本交給 LLM 依 Evidence Pack 寫，而 Evidence Pack
  只給前 5 筆（collector 還截在 20 筆）且以資料列數當張數。全站查核發現張數灌水或
  卡在 20、許可證字號是佔位或屬於別的藥。改為：張數與表格一律由這裡從 TFDA
  「全部藥品許可證資料集」確定性產生，LLM 只引用結果，不自行列字號。

比對規則（寧可漏、不可錯）：
  許可證的「主成分略述」以 ;; 切成各成分；沒有主成分欄時用英文品名。某成分符合藥名，
  該證就算這個藥的證。符合＝去掉立體標記（L-／D-／DL-）與鹽類前綴後，成分以藥名開頭；
  或成分括號內「EQ TO …」別名以藥名開頭；或去複數後詞集合相同（處理
  TOCOPHEROL ACETATE ALPHA DL- 這種倒裝）。「…ic acid」另以「…ate」比對。
  PENICILLIN G PROCAINE 不算 procaine、BUTYLSCOPOLAMINE 不算 scopolamine、
  HYDROCORTISONE 不算 cortisone —— 不同藥。

分類：單方＝主成分只有一項；複方＝多項（依許可證主成分欄，賦形劑若被列入也算）；
  已註銷＝註銷狀態欄有值。張數＝不重複許可證字號數。
"""
from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
DATASET = REPO / "data" / "raw" / "tw_fda_drugs.json"
SNAPSHOT = REPO / "snapshots" / "tfda_licenses.json.gz"
SOURCE_LABEL = "衛福部食藥署開放資料「全部藥品許可證資料集」（資料集 36）"
SOURCE_URL = "https://data.fda.gov.tw/data/opendata/export/36/json"

# 字號：衛署／衛部／內衛開頭；號碼可帶英文字首（放射性藥品 R00104 這類）
LICENSE_RE = re.compile(r"(?:衛署|衛部|內衛)[\u4e00-\u9fff]{0,6}字第[A-Z]?\d{5,6}號")
BEGIN = "<!-- tfda-licenses:begin（程式產生，勿手改；scripts/regenerate_tfda_tables.py） -->"
END = "<!-- tfda-licenses:end -->"

SYNONYMS_FILE = REPO / "config" / "tfda_synonyms.json"


def _load_synonym_config() -> tuple[dict, dict]:
    """別名表放在 config/tfda_synonyms.json（可審閱），這裡只讀不寫死。"""
    if not SYNONYMS_FILE.exists():
        return {}, {}
    cfg = json.loads(SYNONYMS_FILE.read_text(encoding="utf-8"))
    syn = {norm(k): [norm(n) for n in v["names"]] for k, v in cfg.get("synonyms", {}).items()}
    slug = {k: v["query"] for k, v in cfg.get("slug_query", {}).items()}
    return syn, slug


STEREO = {"L", "D", "DL"}
SALT_PREFIX = {"SODIUM", "DISODIUM", "POTASSIUM", "MAGNESIUM", "CALCIUM", "ZINC"}


def norm(s: str | None) -> str:
    return re.sub(r"[^A-Z0-9]+", " ", (s or "").upper()).strip()


SYNONYMS, SLUG_QUERY = _load_synonym_config()


def _sing(tok: str) -> str:
    return tok[:-1] if len(tok) > 4 and tok.endswith("S") else tok


def drug_terms(name: str) -> list[str]:
    base = norm(name)
    terms = [base] + SYNONYMS.get(base, [])
    # 「DL-ALPHA-TOCOPHEROL」這類藥名：去掉立體標記的版本也當一個詞
    stripped = " ".join(x for x in base.split() if x not in STEREO)
    if stripped and stripped != base:
        terms.append(stripped)
    if base.endswith("IC ACID"):
        stem = base[: -len("IC ACID")]
        terms.append(stem + "ATE")
    return [norm(t) for t in terms]


def _strip_prefix(tokens: list[str]) -> list[str]:
    while tokens and (tokens[0] in STEREO or tokens[0] in SALT_PREFIX):
        tokens = tokens[1:]
    return tokens


def _ingredient_names(raw: str) -> list[str]:
    """一個成分字串 → 主名稱＋括號內 EQ TO 別名，皆已正規化。"""
    names = []
    main = re.sub(r"\(.*?\)", " ", raw)
    names.append(norm(main))
    names.append(norm(raw))  # 括號內容併入：「MAGNESIUM (SULFATE)」「TOCOPHEROL (ACETATE ALPHA DL-)」
    for alias in re.findall(r"\(\s*(?:EQ TO\s+)?([^()]*)\)", raw, flags=re.I):
        names.append(norm(alias))
    return [n for n in names if n]


def ingredient_matches(raw: str, terms: list[str]) -> bool:
    for name in _ingredient_names(raw):
        full = name.split()
        for toks in (full, _strip_prefix(full)):
            joined = " ".join(toks)
            core = [x for x in toks if x not in STEREO]
            for t in terms:
                if joined == t or joined.startswith(t + " "):
                    return True
                if core and sorted(_sing(x) for x in core) == sorted(_sing(x) for x in t.split() if x not in STEREO):
                    return True
    return False


def ingredients_of(rec: dict) -> list[str]:
    s = rec.get("主成分略述")
    if s:
        return [i.strip() for i in s.split(";;") if i.strip()]
    en = rec.get("英文品名")
    return [en.strip()] if en else []


def load_records(path: Path | None = None) -> list[dict]:
    p = Path(path) if path else DATASET
    if not p.exists():
        return []
    return json.loads(p.read_text(encoding="utf-8"))


def dedupe(records: list[dict]) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for r in records:
        lid = r.get("許可證字號")
        if lid and lid not in out:
            out[lid] = r
    return out


def to_license(rec: dict) -> dict:
    ings = ingredients_of(rec)
    cancelled = bool((rec.get("註銷狀態") or "").strip())
    return {
        "id": rec["許可證字號"],
        "name_zh": (rec.get("中文品名") or "").strip(),
        "name_en": (rec.get("英文品名") or "").strip(),
        "ingredients": ings,
        "kind": "single" if len(ings) <= 1 else "combo",
        "status": "cancelled" if cancelled else "valid",
        "cancel_date": rec.get("註銷日期") or "",
        "expiry": rec.get("有效日期") or "",
        "form": (rec.get("劑型") or "").strip(),
        "applicant": (rec.get("申請商名稱") or "").strip(),
        "indication": re.sub(r"\s+", " ", rec.get("適應症") or "").strip(),
    }


_INDEX_CACHE: dict[int, tuple] = {}


def _index(by_id: dict[str, dict]) -> tuple:
    """成分名稱變體的倒排索引（首詞 → 證、詞集合 → 證），讓全站比對在數秒內完成。"""
    key = id(by_id)
    if key in _INDEX_CACHE:
        return _INDEX_CACHE[key]
    first: dict[str, list] = {}
    tset: dict[tuple, set] = {}
    for lid, r in by_id.items():
        for raw in ingredients_of(r):
            for name in _ingredient_names(raw):
                full = name.split()
                for toks in (full, _strip_prefix(full)):
                    if not toks:
                        continue
                    first.setdefault(toks[0], []).append((" ".join(toks), lid))
                    core = tuple(sorted(_sing(x) for x in toks if x not in STEREO))
                    if core:
                        tset.setdefault(core, set()).add(lid)
    _INDEX_CACHE[key] = (first, tset)
    return first, tset


def licenses_for_drug(name: str, records: list[dict] | dict[str, dict]) -> list[dict]:
    """藥名 → 該藥的不重複許可證（已排序：有效單方、有效複方、已註銷；同類依字號）。
    與 ingredient_matches() 同一套規則，只是走索引。"""
    by_id = records if isinstance(records, dict) else dedupe(records)
    first, tset = _index(by_id)
    hit: set[str] = set()
    for t in drug_terms(name):
        tt = t.split()
        if not tt:
            continue
        for joined, lid in first.get(tt[0], []):
            if joined == t or joined.startswith(t + " "):
                hit.add(lid)
        hit |= tset.get(tuple(sorted(_sing(x) for x in tt if x not in STEREO)), set())
    out = [to_license(by_id[lid]) for lid in hit]
    order = {("valid", "single"): 0, ("valid", "combo"): 1}
    out.sort(key=lambda x: (order.get((x["status"], x["kind"]), 2), x["id"]))
    return out


def summarize(lics: list[dict]) -> dict:
    s = {"total": len(lics), "valid_single": 0, "valid_combo": 0, "cancelled": 0}
    for x in lics:
        if x["status"] == "cancelled":
            s["cancelled"] += 1
        elif x["kind"] == "single":
            s["valid_single"] += 1
        else:
            s["valid_combo"] += 1
    s["valid"] = s["valid_single"] + s["valid_combo"]
    return s


def count_text(s: dict) -> str:
    if s["total"] == 0:
        return "0 張（TFDA 資料集查無主成分相符的許可證）"
    return (f"{s['total']} 張（有效單方 {s['valid_single']}／有效複方 {s['valid_combo']}／"
            f"已註銷 {s['cancelled']}）")


def _cell(s: str, limit: int = 90) -> str:
    s = (s or "").replace("|", "／").replace("\n", " ").strip()
    return s if len(s) <= limit else s[:limit].rstrip() + "…"


def render_block(display_name: str, lics: list[dict], data_date: str) -> str:
    """產生「台灣許可證」區塊（markdown；已註銷者收在 <details> 的 HTML 表）。"""
    s = summarize(lics)
    lines = [BEGIN, "", "### 台灣許可證（依 TFDA 資料集自動產生）", ""]
    lines.append(
        f"依{SOURCE_LABEL}（檔案日期 {data_date}），主成分含 {display_name} 的不重複許可證共 "
        f"**{s['total']} 張**：有效單方 {s['valid_single']} 張、有效複方 {s['valid_combo']} 張、"
        f"已註銷 {s['cancelled']} 張。本表由程式依主成分比對產生，適應症為許可證原文（過長者截斷）。"
        f"資料來源：[TFDA 開放資料]({SOURCE_URL})。"
    )
    lines.append("")
    singles = [x for x in lics if x["status"] == "valid" and x["kind"] == "single"]
    combos = [x for x in lics if x["status"] == "valid" and x["kind"] == "combo"]
    cancelled = [x for x in lics if x["status"] == "cancelled"]
    s_head = ["許可證字號", "品名", "劑型", "申請商", "有效日期", "核准適應症"]
    s_rows = [[x["id"], _cell(x["name_zh"], 40), _cell(x["form"], 16), _cell(x["applicant"], 24),
               x["expiry"], _cell(x["indication"])] for x in singles]
    c_head = ["許可證字號", "品名", "主成分", "劑型", "核准適應症"]
    c_rows = [[x["id"], _cell(x["name_zh"], 40), _cell("、".join(x["ingredients"]), 60),
               _cell(x["form"], 16), _cell(x["indication"])] for x in combos]
    x_head = ["許可證字號", "品名", "主成分", "註銷日期"]
    x_rows = [[x["id"], _cell(x["name_zh"], 40), _cell("、".join(x["ingredients"]), 60), x["cancel_date"]]
              for x in cancelled]
    if singles:
        lines += _table("有效・單方", s_head, s_rows, fold=len(s_rows) > FOLD_AT)
    if combos:
        lines += _table("有效・複方（適應症屬整個複方，不是本藥單獨的適應症）", c_head, c_rows,
                        fold=len(c_rows) > FOLD_AT)
    if cancelled:
        lines += _table("已註銷", x_head, x_rows, fold=True)
    if not lics:
        lines += ["TFDA 資料集查無主成分與本藥相符的許可證。", ""]
    lines.append(END)
    return "\n".join(lines)


FOLD_AT = 30  # 超過這麼多列就收進 <details>，避免頁面被上百列許可證淹沒


def _table(title: str, head: list[str], rows: list[list[str]], fold: bool) -> list[str]:
    if not fold:
        out = [f"**{title}**（{len(rows)} 張）", "", "| " + " | ".join(head) + " |",
               "|" + "|".join("------" for _ in head) + "|"]
        out += ["| " + " | ".join(r) + " |" for r in rows]
        return out + [""]
    th = "".join(f"<th>{h}</th>" for h in head)
    body = "".join("<tr>" + "".join(f"<td>{_html(c)}</td>" for c in r) + "</tr>" for r in rows)
    return [f"<details><summary><strong>{title}</strong>（{len(rows)} 張，展開）</summary>",
            f"<table><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></details>", ""]


def _html(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def license_ids_in(text: str) -> list[str]:
    return LICENSE_RE.findall(text)


def validate_page(text: str, allowed_ids: set[str]) -> list[str]:
    """頁面（不含查核框與程式產生區塊以外的地方也一樣檢查）上每個許可證字號，
    都必須是這個藥主成分相符的 TFDA 許可證。回傳不符的字號。"""
    body = re.sub(r"<!-- review:begin (\S+) -->.*?<!-- review:end \1 -->", "", text, flags=re.S)
    return sorted({n for n in license_ids_in(body) if n not in allowed_ids})


def compact(lic: dict) -> dict:
    """快照用：只留產表與驗證需要的欄位，長文字截在產表用得到的長度內。"""
    c = dict(lic)
    c.pop("name_en", None)
    c["indication"] = c["indication"][:200]
    return c


def load_snapshot(path: Path | None = None) -> dict:
    import gzip
    p = Path(path) if path else SNAPSHOT
    if not p.exists():
        return {}
    with gzip.open(p, "rt", encoding="utf-8") as f:
        return json.load(f)


def write_snapshot(drugs: dict, data_date: str, path: Path | None = None) -> Path:
    import gzip
    p = Path(path) if path else SNAPSHOT
    p.parent.mkdir(parents=True, exist_ok=True)
    doc = {"meta": {"source": SOURCE_LABEL, "url": SOURCE_URL, "data_date": data_date,
                    "rule": "主成分比對，見 src/twtxgnn/regulatory/tfda_licenses.py"},
           "drugs": drugs}
    raw = json.dumps(doc, ensure_ascii=False, sort_keys=True, indent=0).encode("utf-8")
    with open(p, "wb") as fh:
        with gzip.GzipFile(fileobj=fh, mode="wb", mtime=0, filename="") as gz:
            gz.write(raw)
    return p
