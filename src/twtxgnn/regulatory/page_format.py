"""藥物頁的確定性格式規則：頁首證據等級、表格前空行（2026-10-03 建）。

產線（page_postprocess.postprocess_with_licenses）與 scripts/apply_drug_reviews.py 都呼叫這裡，
gate（scripts/check_seo_docs.py 第 7 項）用同一套函式檢查，三者規則一致。

頁首等級規則（產線原意，見 sync_notes_to_docs.extract_evidence_level、build_docs.get_evidence_level）：
  頁首（front matter evidence_level、parent、「證據等級: **Lx**」列）＝「快速總覽」表「證據等級」
  儲存格裡的等級；儲存格有多個等級（如「L2 (偏頭痛)、L3 (類風濕)」「L4 至 L5」）取最高（數字最小）。
  儲存格沒有任何 Lx（「不適用」「待評估」等）或沒有這一列：頁首不動。
  舊解析式只認「| 證據等級 | L3 |」這種純值儲存格，帶說明文字就落到預設 L5，造成頁首與總覽表不一致。
  主預測重審撤回（2026-11-03 用戶決定）：查核紀錄的 table_updates 把總覽「證據等級」格換成「撤回：…」
  （格內不再有 Lx）時，頁首改取本頁其他預測表（表頭有「證據等級」欄的表，如「其他預測適應症概況」
  「附註：其他預測適應症」）裡仍保留的最高等級；沒有就是 N/A，parent 跟既有 N/A 頁一樣歸
  known-uses 列表頁（docs/known-uses.md 的 title，2026-11-03 改為「僅已知用途／主預測已撤回」；head_custom.html 的 breadcrumb：N/A→/known-uses）。
  只看表格裡的等級欄，不解析敘述文字裡提到的等級；被撤回的列在表裡同樣已換成「撤回…」，不會被算進去。

description 的等級（2026-11-03 用戶決定）：front matter description 是產線依報告寫的（「（證據等級 Lx）」），
  主預測撤回或頁首重算後會過期。drug_reviews.json 的 action: description_level 紀錄（記 original_description）
  由 apply_drug_reviews.py 呼叫 sync_description_level，只把 description 裡「證據等級 Lx」換成目前頁首等級
  （N/A 頁換成「僅已知用途」，與 docs/known-uses.md 的用語一致），其他文字一字不動；
  gate 用 description_level_problems 檢查 description 提到的等級與頁首一致。

表格前空行：kramdown 不把緊接在標題或段落下一行的 `|` 列當表格，整張表會變成一段純文字；
表格第一列的前一行不是空行時補一個空行（程式碼區塊內不動）。
表格後空行（2026-11-03 補）：表格最後一列的下一行直接接「## 免責聲明」之類的非表格行，kramdown 同樣把
整張表排成純文字（aliskiren、icatibant 實例）；最後一列以 `|` 收尾、下一行不是空行／`{:` 屬性列／
Liquid `{%` 時補一個空行。最後一列沒以 `|` 收尾（儲存格內含換行，例如 TFDA 適應症原文多行）不是缺空行，
補空行也救不回那張表，這裡不處理。
"""
from __future__ import annotations

import re
from pathlib import Path

DOCS = Path(__file__).resolve().parents[3] / "docs"
EVIDENCE_PAGES = ("evidence-high.md", "evidence-medium.md", "evidence-low.md")
KNOWN_USES_PAGE = "known-uses.md"  # evidence_level N/A 的列表頁
NA = "N/A"
OVERVIEW_ROW_RE = re.compile(r"^\|\s*證據等級\s*\|([^|\n]*)\|", re.M)
WITHDRAWN_CELL_RE = re.compile(r"^\s*(\*\*)?撤回")
REVIEW_BLOCK_RE = re.compile(r"<!-- review:begin (\S+) -->.*?<!-- review:end \1 -->", re.S)
LEVEL_RE = r"(?:L[1-5]|N/A)"
_PARENTS: dict = {}


def best_level(cell: str) -> str | None:
    lv = re.findall(r"L([1-5])", cell or "")
    return f"L{min(lv)}" if lv else None


def overview_level(text: str) -> str | None:
    """快速總覽「證據等級」列的最高等級；沒有這列或列內沒有 Lx 回 None。"""
    m = OVERVIEW_ROW_RE.search(text)
    return best_level(m.group(1)) if m else None


def overview_withdrawn(text: str) -> bool:
    """快速總覽「證據等級」格是重審撤回後的「撤回：…」（格內沒有 Lx）。"""
    m = OVERVIEW_ROW_RE.search(text)
    return bool(m and WITHDRAWN_CELL_RE.match(m.group(1)) and not best_level(m.group(1)))


def other_prediction_levels(text: str) -> list[str]:
    """快速總覽以外、表頭有「證據等級」欄的表格裡，該欄的等級（查核框與程式碼區塊內不算）。"""
    text = REVIEW_BLOCK_RE.sub("", text)
    out, col, fence = [], None, False
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        if ln.startswith("```"):
            fence = not fence
        if fence or not ln.startswith("|"):
            col = None
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        prev = lines[i - 1] if i else ""
        if not prev.startswith("|"):  # 表頭列
            col = cells.index("證據等級") if "證據等級" in cells else None
            continue
        if col is None or set(ln.replace("|", "").strip()) <= set("-: "):
            continue
        if col < len(cells):
            lv = best_level(cells[col])
            if lv:
                out.append(lv)
    return out


def target_level(text: str) -> str | None:
    """頁首應有的等級：總覽列最高等級；總覽主預測已撤回時取其他預測表保留的最高等級，沒有就 N/A；
    其餘情況（總覽列沒有 Lx 也不是撤回、或沒有總覽列）回 None＝頁首不動。"""
    best = overview_level(text)
    if best:
        return best
    if overview_withdrawn(text):
        return best_level(" ".join(other_prediction_levels(text))) or NA
    return None


def parent_titles() -> dict:
    """證據等級 → 列表頁標題（docs/evidence-*.md 的 title，標題裡的 L 範圍決定歸屬；N/A → known-uses.md）。"""
    if not _PARENTS:
        p = DOCS / KNOWN_USES_PAGE
        if p.exists():
            m = re.search(r"^title:\s*(.+?)\s*$", p.read_text(encoding="utf-8"), re.M)
            if m:
                _PARENTS[NA] = m.group(1).strip().strip('"').strip("'")
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
    lv = re.search(rf"^evidence_level:[ \t]*({LEVEL_RE})[ \t]*$", fm, re.M)
    par = re.search(r"^parent:[ \t]*(.*?)[ \t]*$", fm, re.M)
    head = re.search(rf"^證據等級: \*\*({LEVEL_RE})\*\*", rest, re.M)
    return {"evidence_level": lv.group(1) if lv else None, "parent": par.group(1) if par else None,
            "header": head.group(1) if head else None}


def sync_header_level(text: str) -> str:
    best = target_level(text)
    fm, rest = _split_fm(text)
    if not best or fm is None:
        return text
    fm = re.sub(rf"^(evidence_level:[ \t]*){LEVEL_RE}[ \t]*$", lambda x: x.group(1) + best, fm, count=1, flags=re.M)
    parent = parent_titles().get(best)
    if parent:
        fm = re.sub(r"^parent:.*$", lambda x: f"parent: {parent}", fm, count=1, flags=re.M)
    rest = re.sub(rf"^(證據等級: \*\*){LEVEL_RE}(\*\*)", lambda x: x.group(1) + best + x.group(2), rest, count=1, flags=re.M)
    return fm + rest


DESC_LEVEL_RE = re.compile(r"證據等級 (L[1-5]|N/A)")
NA_DESC = "僅已知用途"


def _desc_line(fm: str):
    return re.search(r"^description:.*$", fm, re.M)


def description_level_text(level: str) -> str:
    return NA_DESC if level == NA else f"證據等級 {level}"


def sync_description_level(text: str) -> str:
    """description 裡的「證據等級 Lx」換成目前頁首等級（N/A→「僅已知用途」）；其他文字不動。"""
    fm, rest = _split_fm(text)
    lv = header_state(text)["evidence_level"]
    m = _desc_line(fm or "")
    if not m or not lv:
        return text
    line = DESC_LEVEL_RE.sub(lambda _: description_level_text(lv), m.group(0))
    return fm[:m.start()] + line + fm[m.end():] + rest


def description_level_problems(text: str) -> list[str]:
    fm, _ = _split_fm(text)
    lv = header_state(text)["evidence_level"]
    m = _desc_line(fm or "")
    if not m or not lv:
        return []
    bad = sorted({x for x in DESC_LEVEL_RE.findall(m.group(0)) if x != lv})
    return [f"description 寫「證據等級 {x}」，頁首等級={lv}（加 description_level 查核紀錄後跑 scripts/apply_drug_reviews.py）"
            for x in bad]


def header_problems(text: str) -> list[str]:
    best = target_level(text)
    if not best:
        # 已知用途頁（N/A、沒有總覽等級）：parent 也要等於 known-uses 列表頁標題（改標題時一起改，2026-11-03）
        st = header_state(text)
        want = parent_titles().get(NA)
        if st["evidence_level"] == NA and want and st["parent"] != want:
            return [f"parent={st['parent']}，N/A 頁應為 {want}（docs/known-uses.md 的 title）"]
        return []
    st = header_state(text)
    errs = []
    if st["evidence_level"] != best:
        errs.append(f"front matter evidence_level={st['evidence_level']}，快速總覽最高等級（主預測撤回時為其他預測表最高等級或 N/A）={best}")
    if st["header"] not in (None, best):
        errs.append(f"頁首「證據等級」={st['header']}，快速總覽最高等級（主預測撤回時為其他預測表最高等級或 N/A）={best}")
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


def _table_ends_without_blank(lines: list[str]):
    """表格最後一列的下一行不是空行（回傳下一行的索引，也就是要在它前面補空行的位置）。"""
    fence = False
    for i, ln in enumerate(lines[:-1]):
        if ln.startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        nxt = lines[i + 1]
        if (ln.startswith("|") and ln.rstrip().endswith("|") and nxt.strip() and not nxt.startswith("|")
                and not nxt.lstrip().startswith(("{:", "{%"))):
            yield i + 1


def fix_table_spacing(text: str) -> str:
    lines = text.split("\n")
    for i in sorted(set(_table_starts_without_blank(lines)) | set(_table_ends_without_blank(lines)), reverse=True):
        lines.insert(i, "")
    return "\n".join(lines)


def table_spacing_problems(text: str) -> list[str]:
    lines = text.split("\n")
    return ([f"第 {i + 1} 行的表格前面缺空行（前一行：{lines[i - 1][:30]}）"
             for i in _table_starts_without_blank(lines)]
            + [f"第 {i} 行的表格後面缺空行（下一行：{lines[i][:30]}）"
               for i in _table_ends_without_blank(lines)])
