"""scripts/apply_drug_reviews.py：重審結果（rereview_result）、同 id 重發的 history、頁首等級同步。"""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import apply_drug_reviews as A  # noqa: E402

PAGE = """---
layout: default
title: Demo
parent: 僅模型預測 (L5)
evidence_level: L5
---

# Demo

證據等級: **L5** | 預測適應症: **1** 個

## 快速總覽
| 項目 | 內容 |
|------|------|
| 原適應症 | 舊版更正文字 |
| 預測新適應症 | 甲病 |
| 證據等級 | L3 (觀察性研究) |
| 建議決策 | Consider |

## 為什麼這個預測合理？
理由。

## 免責聲明
僅供研究。
"""

SRC = [{"title": "來源", "url": "https://example.org/a", "excerpt": "x", "accessed": "2026-10-03"}]


def recs(verdict="downgrade", new="L5", updates=True):
    rr = {"id": "demo-rr", "file": "demo.md", "checked": "2026-10-03", "action": "rereview",
          "summary": "甲病預測標記待重審", "claim": "| 預測新適應症 | 甲病 |", "note": "待重審。", "sources": SRC}
    res = {"id": "demo-rr-result", "file": "demo.md", "checked": "2026-10-03", "action": "rereview_result",
           "resolves": "demo-rr", "summary": "甲病預測重審結果", "claim": rr["claim"], "verdict": verdict,
           "original_level": "L3", "new_level": new, "note": "理由。", "sources": SRC}
    if updates:
        res["table_updates"] = [
            {"label": "快速總覽「證據等級」", "claim": "| 證據等級 | L3 (觀察性研究) |",
             "replacement": f"| 證據等級 | {new}（2026-10-03 重審降級） |"},
            {"label": "快速總覽「建議決策」", "claim": "| 建議決策 | Consider |",
             "replacement": "| 建議決策 | Hold（2026-10-03 重審調整） |"}]
    fix = {"id": "demo-fix", "file": "demo.md", "checked": "2026-10-03", "action": "correct",
           "summary": "原適應症", "claim": "| 原適應症 | 原句 |", "replacement": "| 原適應症 | 新版 |",
           "note": "更正。", "sources": SRC,
           "history": [{"replacement": "| 原適應症 | 舊版更正文字 |", "retired": "2026-10-03"}]}
    return [fix, rr, res]


def render(rs, text=PAGE):
    problems = []
    for _ in range(4):
        nxt = A.render_page(text, rs, problems)
        if nxt == text:
            break
        text = nxt
    return text, problems


def test_result_replaces_pending_box_and_updates_cells():
    out, problems = render(recs())
    assert problems == []
    assert "待重審（" not in out and "重審結果（2026-10-03）" in out
    assert "**降級**（證據等級 L3→L5）" in out
    assert "| 證據等級 | L5（2026-10-03 重審降級） |" in out
    assert "| 建議決策 | Hold（2026-10-03 重審調整） |" in out
    # 原值留在查核紀錄表
    assert "原「建議決策／Consider」" in out and "標記待重審 → 已重審" in out


def test_header_follows_overview_level():
    out, _ = render(recs(verdict="maintain", new="L3", updates=False))
    assert "evidence_level: L3" in out and "證據等級: **L3**" in out
    assert "parent: 中證據等級 (L3-L4)" in out


def test_history_replacement_swapped_to_new_version():
    out, problems = render(recs())
    assert problems == []
    assert "| 原適應症 | 新版 |" in out and "舊版更正文字 |\n" not in out


def test_idempotent():
    once, _ = render(recs())
    twice, _ = render(recs(), once)
    assert once == twice


@pytest.mark.parametrize("bad,msg", [
    ({"resolves": "nope"}, "resolves"),
    ({"verdict": "maybe"}, "verdict"),
    ({"new_level": "L2"}, "沒有低於"),
])
def test_validate(bad, msg):
    rs = recs()
    rs[2].update(bad)
    assert any(msg in e for e in A.validate(rs))


# ---- page_format：頁首等級與表格空行（2026-10-04）----
from twtxgnn.regulatory import page_format as F  # noqa: E402


@pytest.mark.parametrize("cell,want", [
    ("L3 (觀察性研究/文獻支持)", "L3"),
    ("**L2** (偏頭痛)、**L3** (類風濕)", "L2"),
    ("L4 (前臨床) 至 L5 (僅預測)", "L4"),
    ("不適用", None),
])
def test_overview_level(cell, want):
    assert F.overview_level(f"| 證據等級 | {cell} |\n") == want


def test_sync_header_and_gate():
    page = PAGE.replace("| 證據等級 | L3 (觀察性研究) |", "| 證據等級 | **L1** (多個 RCT) |")
    assert F.header_problems(page)
    out = F.sync_header_level(page)
    assert "evidence_level: L1" in out and "parent: 高證據等級 (L1-L2)" in out and "證據等級: **L1**" in out
    assert F.header_problems(out) == []
    assert F.sync_header_level(out) == out


def test_table_spacing():
    page = "## 快速總覽\n| a | b |\n|---|---|\n| 1 | 2 |\n\n```\n說明\n| 不是表格 |\n```\n"
    assert len(F.table_spacing_problems(page)) == 1
    out = F.fix_table_spacing(page)
    assert "## 快速總覽\n\n| a | b |" in out and F.table_spacing_problems(out) == []
    assert F.fix_table_spacing(out) == out


def test_pipeline_parsers_read_annotated_cells():
    import build_docs
    import sync_notes_to_docs
    txt = "| 證據等級 | **L2** (偏頭痛)、**L3** (類風濕) |\n"
    assert sync_notes_to_docs.extract_evidence_level(txt) == "L2"
    assert build_docs.get_evidence_level(txt) == "L2"
