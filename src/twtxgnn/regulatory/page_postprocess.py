"""藥物報告的確定性後處理：清理 LLM 開場白／內部用語、替換許可證張數與表格、驗證許可證字號。

產線（sync_notes_to_docs.py、build_docs.py）在把報告寫進 docs/_drugs/ 之前呼叫
postprocess_report()；scripts/regenerate_tfda_tables.py 用同一套函式處理既有頁面。
驗證不過（頁面上出現不屬於這個藥的許可證字號）就不同步，交人工處理。
"""
from __future__ import annotations

import re

from . import tfda_licenses as T

REVIEW_RE = re.compile(r"<!-- review:begin (\S+) -->.*?<!-- review:end \1 -->", re.S)
TFDA_BLOCK_RE = re.compile(re.escape(T.BEGIN) + r".*?" + re.escape(T.END), re.S)

# LLM 開場白的特徵（產線內部用語、技能確認、格式說明）
META_RE = re.compile(
    r"txgnn-pipeline|\bskill\b|技能|Evidence Pack|報告如下|以下是根據|以下根據|以下依|依照.*格式|v5 格式|"
    r"Prompt|系統提示|system prompt|candidate_id|Proceeding|confirms? this", re.I)

# 內文的內部用語 → 中性說法（順序有意義：長的先換）
JARGON = [
    (re.compile(r"本次\s*Evidence Pack"), "本次彙整資料"),
    (re.compile(r"本\s*Evidence Pack"), "本報告彙整的資料"),
    (re.compile(r"Evidence Pack\s*中"), "彙整資料中"),
    (re.compile(r"Evidence Pack"), "彙整資料"),
]


def strip_preamble(report: str) -> str:
    """去掉報告本體（第一個 `# ` 標題）之前、帶有產線內部用語的開場段落。
    report 可以是 notes 原文，也可以是 docs 頁（此時只處理藥師評估報告 div 之後那段）。"""
    anchor = report.find('<div id="pharmacist">')
    start = report.find("</div>", anchor) + len("</div>") if anchor >= 0 else 0
    m = re.compile(r"^# ", re.M).search(report, start)
    if not m:
        return report
    head = report[start:m.start()]
    paras = [p for p in re.split(r"\n\s*\n", head) if p.strip()]
    kept = [p for p in paras if not META_RE.search(p)]
    if len(kept) == len(paras):
        return report
    kept = [p for p in kept if p.strip().strip("-").strip()]  # 開場白後面孤立的 --- 分隔線一併拿掉
    sep = "\n\n" if anchor >= 0 else ""
    body = sep + ("\n\n".join(kept) + "\n\n" if kept else "")
    return report[:start] + body + report[m.start():]


def drop_stale_license_notes(text: str) -> str:
    """刪除「說 Evidence Pack／產線資料的許可證有問題」的引言框——許可證已改由程式產生，這些說明過時。"""
    out, buf = [], []

    def flush():
        block = "\n".join(buf)
        if not (re.search(r"Evidence Pack|taiwan_regulatory|彙整資料", block) and "許可證" in block):
            out.extend(buf)
        buf.clear()

    for line in text.split("\n"):
        if line.startswith(">"):
            buf.append(line)
        else:
            if buf:
                flush()
            out.append(line)
    if buf:
        flush()
    return "\n".join(out)


def replace_jargon(text: str) -> str:
    for rx, rep in JARGON:
        text = rx.sub(rep, text)
    # 原文「目前 Evidence Pack 中」這類中英夾雜的空白，換成中文後收掉
    text = re.sub(r"(?<=[\u4e00-\u9fff（，。、])[ \t]+(?=彙整資料|本報告彙整)", "", text)
    return re.sub(r"(彙整資料|本報告彙整的資料)[ \t]+(?=[\u4e00-\u9fff])", r"\1", text)


def clean_llm_output(text: str) -> str:
    return replace_jargon(drop_stale_license_notes(strip_preamble(text)))


# ---------------- 許可證表與張數 ----------------

def _is_sep(line: str) -> bool:
    return bool(re.match(r"^\|[\s:|-]+\|\s*$", line.strip()))


def _license_tables(lines: list[str]) -> list[tuple[int, int]]:
    """回傳許可證表的 (起, 迄) 行號（表頭含「許可證」的 markdown 表）。"""
    spans, i = [], 0
    while i < len(lines) - 1:
        if lines[i].startswith("|") and _is_sep(lines[i + 1]):
            j = i + 2
            while j < len(lines) and lines[j].startswith("|"):
                j += 1
            rows = lines[i:j]
            first_cells = [r.split("|")[1].strip() if r.count("|") >= 2 else "" for r in rows]
            if "許可證" in lines[i] or any(re.search(r"許可證字號|許可證號", c) for c in first_cells):
                spans.append((i, j))
            i = j
        else:
            i += 1
    return spans


SECTION_RE = re.compile(r"^## .*台灣上市", re.M)
COUNT_PROSE_RE = re.compile(r"(\d[\d,，]*)\s*張(相關|藥品|有效)?許可證(?:（有效 \d+ 張）)?")  # 已改寫過的連同括號一起更新


def rewrite_count_prose(text: str, s: dict) -> str:
    """表格以外的「N 張許可證」敘述：數字改成程式算的不重複張數（查核框與程式區塊內不動）。"""
    pat = re.compile(r"(" + re.escape(T.BEGIN) + r".*?" + re.escape(T.END) +
                     r"|<!-- review:begin (\S+) -->.*?<!-- review:end \2 -->)", re.S)
    out, pos = [], 0
    for m in pat.finditer(text):
        out.append(_prose(text[pos:m.start()], s))
        out.append(m.group(0))
        pos = m.end()
    out.append(_prose(text[pos:], s))
    return "".join(out)


def _prose(seg: str, s: dict) -> str:
    return "\n".join(
        ln if ln.startswith("|") else COUNT_PROSE_RE.sub(
            lambda m: f"{s['total']} 張{m.group(2) or ''}許可證（有效 {s['valid']} 張）", ln)
        for ln in seg.split("\n"))


def replace_tfda(text: str, display_name: str, lics: list[dict], data_date: str) -> str:
    s = T.summarize(lics)
    block = T.render_block(display_name, lics, data_date)
    if TFDA_BLOCK_RE.search(text):  # 已有程式區塊：原地更新，位置不動
        text = TFDA_BLOCK_RE.sub(lambda m: block, text, count=1)
        return _count_row(text, s)
    lines = text.split("\n")
    spans = _license_tables(lines)
    sec = SECTION_RE.search(text)
    sec_line = text[:sec.start()].count("\n") if sec else None
    sec_end = None
    if sec_line is not None:
        sec_end = next((k for k in range(sec_line + 1, len(lines)) if lines[k].startswith("## ")), len(lines))
    insert_at = None
    for a, b in reversed(spans):
        if insert_at is None or a < insert_at:
            insert_at = a
        del lines[a:b]
        if sec_end is not None and a < sec_end:
            sec_end -= (b - a)
    if sec_line is not None:
        if insert_at is None or not (sec_line < insert_at <= sec_end):
            insert_at = sec_line + 1
        # 區段內的張數敘述、「精選／部分」說明一律移除（已由程式化區塊取代）
        k = sec_line + 1
        while k < sec_end:
            ln = lines[k]
            if (COUNT_PROSE_RE.search(ln) or re.search(r"精選|部分許可證|以下為部分|僅列出", ln)) and not ln.startswith("#"):
                if k < insert_at:
                    insert_at -= 1
                del lines[k]
                sec_end -= 1
                continue
            k += 1
    else:
        tgt = re.compile(r"^## (安全|結論|查核紀錄|免責)")
        idx = next((k for k, ln in enumerate(lines) if tgt.match(ln)), len(lines))
        lines[idx:idx] = ["## 台灣上市資訊", ""]
        insert_at = idx + 2
    lines[insert_at:insert_at] = ["", block, ""]
    text = "\n".join(lines)
    # 已空掉的小標（下一個非空行就是同級或更高標題／區塊）
    text = re.sub(r"^### [^\n]*許可證[^\n]*\n\s*\n(?=(### |## |<!-- tfda-licenses:begin))", "", text, flags=re.M)
    text = _count_row(text, s)
    return re.sub(r"\n{3,}", "\n\n", text)


def _count_row(text: str, s: dict) -> str:
    """快速總覽的「許可證數」列改成程式算的張數與分類。"""
    return re.sub(r"^(\|\s*許可證數\s*\|)[^|\n]*(\|)", lambda m: f"{m.group(1)} {T.count_text(s)} {m.group(2)}",
                  text, flags=re.M)


def postprocess_with_licenses(text: str, display_name: str, lics: list[dict], data_date: str,
                              slug: str | None = None):
    """清理 → 程式化許可證表與「許可證數」列 → 套人工查核紀錄 → 改寫其他張數敘述 → 驗證。
    回傳 (新內容, 不符字號)。slug 給了才套查核紀錄（docs/_data/drug_reviews.json）。"""
    new = replace_tfda(clean_llm_output(text), display_name, lics, data_date)
    if slug:
        new, _ = _apply_reviews(new, f"{slug}.md")
    new = re.sub(r"\n{3,}", "\n\n", rewrite_count_prose(new, T.summarize(lics)))
    bad = T.validate_page(new, {x["id"] for x in lics})
    return new, bad


def _apply_reviews(text: str, fname: str):
    import sys
    sd = str(T.REPO / "scripts")
    if sd not in sys.path:
        sys.path.insert(0, sd)
    import apply_drug_reviews as A
    return A.apply_text(text, fname)


def postprocess_report(text: str, query_name: str, display_name: str, by_id: dict, data_date: str):
    lics = T.licenses_for_drug(query_name, by_id)
    new, bad = postprocess_with_licenses(text, display_name, lics, data_date)
    return new, lics, bad


_SOURCE: dict = {}


def site_licenses(slug: str, title: str) -> tuple[list[dict], str]:
    """產線用：有 data/raw/tw_fda_drugs.json 就從資料集算；沒有就用 repo 內快照。"""
    if "by_id" not in _SOURCE:
        recs = T.load_records()
        _SOURCE["by_id"] = T.dedupe(recs) if recs else None
        snap = T.load_snapshot()
        _SOURCE["snap"] = snap
        _SOURCE["date"] = (snap.get("meta") or {}).get("data_date", "")
    query = T.SLUG_QUERY.get(slug, title)
    if _SOURCE["by_id"] is not None:
        return T.licenses_for_drug(query, _SOURCE["by_id"]), _SOURCE["date"]
    entry = (_SOURCE["snap"].get("drugs") or {}).get(slug)
    if entry is None:
        raise LookupError(f"{slug}：沒有 TFDA 資料集也沒有快照，無法產生許可證表")
    return entry["licenses"], _SOURCE["date"]


def process_for_site(text: str, slug: str, title: str):
    """sync_notes_to_docs.py／build_docs.py 寫頁前呼叫。回傳 (新內容, 不符字號)；不符就不要寫。"""
    lics, date = site_licenses(slug, title)
    return postprocess_with_licenses(text, title, lics, date, slug=slug)
