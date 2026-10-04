"""藥物頁的確定性格式規則：頁首證據等級、表格前空行（2026-10-03 建）。

產線（page_postprocess.postprocess_with_licenses）與 scripts/apply_drug_reviews.py 都呼叫這裡，
gate（scripts/check_seo_docs.py 第 7 項）用同一套函式檢查，三者規則一致。

頁首等級規則（產線原意，見 sync_notes_to_docs.extract_evidence_level、build_docs.get_evidence_level）：
  頁首（front matter evidence_level、parent、「證據等級: **Lx**」列）＝「快速總覽」表「證據等級」
  儲存格裡的等級；儲存格有多個等級（如「L2 (偏頭痛)、L3 (類風濕)」「L4 至 L5」）取最高（數字最小）。
  儲存格沒有任何 Lx（「不適用」「待評估」等）或沒有這一列：頁首不動。
  舊解析式只認「| 證據等級 | L3 |」這種純值儲存格，帶說明文字就落到預設 L5，造成頁首與總覽表不一致。

表格前空行：kramdown 不把緊接在標題或段落下一行的 `|` 列當表格，整張表會變成一段純文字；
表格第一列的前一行不是空行時補一個空行（程式碼區塊內不動）。
"""
from __future__ import annotations

import re
from pathlib import Path

DOCS = Path(__file__).resolve().parents[3] / "docs"
EVIDENCE_PAGES = ("evidence-high.md", "evidence-medium.md", "evidence-low.md")
OVERVIEW_ROW_RE = re.compile(r"^\|\s*證據等級\s*\|([^|\n]*)\|", re.M)
_PARENTS: dict = {}


def best_level(cell: str) -> str | None:
    lv = re.findall(r"L([1-5])", cell or "")
    return f"L{min(lv)}" if lv else None


def overview_level(text: str) -> str | None:
    """快速總覽「證據等級」列的最高等級；沒有這列或列內沒有 Lx 回 None。"""
    m = OVERVIEW_ROW_RE.search(text)
    return best_level(m.group(1)) if m else None


def parent_titles() -> dict:
    """證據等級 → 列表頁標題（docs/evidence-*.md 的 title，標題裡的 L 範圍決定歸屬）。"""
    if not _PARENTS:
        for fname in EVIDENCE_PAGES:
            p = DOCS / fname
            if not p.exists():
                continue
            m = re.search(r"^title:\s*(.+?)\s*$", p.read_text(encoding="utf-8"), re.M)
            if not m:
                continue
            title = m.group(1).strip().strip('"').strip("'")
            lv = [int(x) for x in re.findall(r"L([1-5])", title)]
            for n in range(min(lv), max(lv) + 1) if lv else []:
                _PARENTS.setdefault(f"L{n}", title)
    return _PARENTS


def _split_fm(text: str):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    return (text[:end], text[end:]) if end >= 0 else (None, text)


def header_state(text: str) -> dict:
    """目前頁首的 evidence_level／parent／頁首列等級（gate 與重算紀錄用）。"""
    fm, rest = _split_fm(text)
    fm = fm or ""
    lv = re.search(r"^evidence_level:[ \t]*(L[1-5])[ \t]*$", fm, re.M)
    par = re.search(r"^parent:[ \t]*(.*?)[ \t]*$", fm, re.M)
    head = re.search(r"^證據等級: \*\*(L[1-5])\*\*", rest, re.M)
    return {"evidence_level": lv.group(1) if lv else None, "parent": par.group(1) if par else None,
            "header": head.group(1) if head else None}


def sync_header_level(text: str) -> str:
    best = overview_level(text)
    fm, rest = _split_fm(text)
    if not best or fm is None:
        return text
    fm = re.sub(r"^(evidence_level:[ \t]*)L[1-5][ \t]*$", lambda x: x.group(1) + best, fm, count=1, flags=re.M)
    parent = parent_titles().get(best)
    if parent:
        fm = re.sub(r"^parent:.*$", lambda x: f"parent: {parent}", fm, count=1, flags=re.M)
    rest = re.sub(r"^(證據等級: \*\*)L[1-5](\*\*)", lambda x: x.group(1) + best + x.group(2), rest, count=1, flags=re.M)
    return fm + rest


def header_problems(text: str) -> list[str]:
    best = overview_level(text)
    if not best:
        return []
    st = header_state(text)
    errs = []
    if st["evidence_level"] != best:
        errs.append(f"front matter evidence_level={st['evidence_level']}，快速總覽最高等級={best}")
    if st["header"] not in (None, best):
        errs.append(f"頁首「證據等級」={st['header']}，快速總覽最高等級={best}")
    want = parent_titles().get(best)
    if want and st["parent"] != want:
        errs.append(f"parent={st['parent']}，應為 {want}")
    return errs


def _table_starts_without_blank(lines: list[str]):
    fence = False
    for i, ln in enumerate(lines):
        if ln.startswith("```"):
            fence = not fence
            continue
        if fence or i == 0:
            continue
        prev = lines[i - 1]
        if ln.startswith("|") and prev.strip() and not prev.startswith("|"):
            yield i


def fix_table_spacing(text: str) -> str:
    lines = text.split("\n")
    for i in reversed(list(_table_starts_without_blank(lines))):
        lines.insert(i, "")
    return "\n".join(lines)


def table_spacing_problems(text: str) -> list[str]:
    lines = text.split("\n")
    return [f"第 {i + 1} 行的表格前面缺空行（前一行：{lines[i - 1][:30]}）"
            for i in _table_starts_without_blank(lines)]
