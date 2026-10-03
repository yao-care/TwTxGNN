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
