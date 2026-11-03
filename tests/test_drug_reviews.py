"""scripts/apply_drug_reviews.py：重審結果（rereview_result）、同 id 重發的 history、頁首等級同步。"""
import json
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


def test_table_spacing_after():
    page = "## 表\n\n| a | b |\n|---|---|\n| 1 | 2 |\n## 免責聲明\n\n| c |\n|---|\n| 3 |\n{: .x }\n"
    assert len(F.table_spacing_problems(page)) == 1
    out = F.fix_table_spacing(page)
    assert "| 1 | 2 |\n\n## 免責聲明" in out and "| 3 |\n{: .x }" in out and F.table_spacing_problems(out) == []
    assert F.fix_table_spacing(out) == out
    # 儲存格內含換行（最後一列沒以 | 收尾）不是缺空行，不動
    multi = "\n| 項目 | 內容 |\n|---|---|\n| 原適應症 | 1、甲\n 2、乙 |\n"
    assert F.table_spacing_problems(multi) == [] and F.fix_table_spacing(multi) == multi


def test_pipeline_parsers_read_annotated_cells():
    import build_docs
    import sync_notes_to_docs
    txt = "| 證據等級 | **L2** (偏頭痛)、**L3** (類風濕) |\n"
    assert sync_notes_to_docs.extract_evidence_level(txt) == "L2"
    assert build_docs.get_evidence_level(txt) == "L2"


# ---- 主預測重審撤回 → 頁首 N/A（2026-11-03 用戶決定）----
WITHDRAW_CELL = "| 證據等級 | 撤回：甲病是已核准用途，不列新適應症證據等級（原值見查核紀錄） |"
OTHER_TABLE = """
## 附註：其他預測適應症

| 預測適應症 | TxGNN 分數 | 證據等級 | 說明 | 決策 |
|-----------|-----------|---------|------|------|
| 乙病 | 0.99 | L4 | 動物研究 | Research Question |
| 丙病 | 0.98 | 撤回（已核准用途，不列新適應症等級） | 已核准 | 撤回 |
| 丁病 | 0.97 | L5 | 僅模型預測 | Hold |
"""


def withdraw_recs():
    rs = recs(verdict="withdraw", new="撤回（已核准用途，不列新適應症等級）", updates=False)
    rs[2]["table_updates"] = [{"label": "快速總覽「證據等級」", "claim": "| 證據等級 | L3 (觀察性研究) |",
                               "replacement": WITHDRAW_CELL}]
    return rs


def test_withdrawn_main_prediction_header_na():
    out, problems = render(withdraw_recs())
    assert problems == []
    assert F.overview_withdrawn(out) and F.target_level(out) == "N/A"
    assert "evidence_level: N/A" in out and "證據等級: **N/A**" in out
    assert "parent: 僅已知用途（無新預測）" in out
    assert F.header_problems(out) == []
    assert F.sync_header_level(out) == out


def test_withdrawn_main_prediction_keeps_other_table_level():
    page = PAGE.replace("## 免責聲明", OTHER_TABLE.strip() + "\n\n## 免責聲明")
    out, problems = render(withdraw_recs(), page)
    assert problems == []
    assert F.other_prediction_levels(out) == ["L4", "L5"]  # 撤回的丙病列不算
    assert "evidence_level: L4" in out and "parent: 中證據等級 (L3-L4)" in out and "證據等級: **L4**" in out
    assert F.header_problems(out) == []


def test_non_withdrawn_cell_without_level_leaves_header():
    page = PAGE.replace("| 證據等級 | L3 (觀察性研究) |", "| 證據等級 | 待評估 |")
    assert F.target_level(page) is None and F.sync_header_level(page) == page and F.header_problems(page) == []


def test_gate_flags_stale_header_after_withdraw():
    page = PAGE.replace("| 證據等級 | L3 (觀察性研究) |", WITHDRAW_CELL)
    assert any("N/A" in e for e in F.header_problems(page))


def test_header_level_withdraw_log_text():
    rec = {"id": "demo-h", "file": "demo.md", "checked": "2026-11-03", "action": "header_level", "trigger": "withdraw",
           "summary": "頁首證據等級", "original_level": "L3", "new_level": "N/A", "sources": SRC}
    out = A.log_md(withdraw_recs() + [rec])
    assert "主預測重審撤回，頁首等級重算（原 L3→N/A），改列「僅已知用途（無新預測）」" in out


def test_extract_drug_list_skips_withdrawn(tmp_path):
    import extract_drug_list as X
    f = tmp_path / "r.json"
    f.write_text(json.dumps({"records": [
        {"action": "rereview_result", "verdict": "withdraw", "file": "a.md",
         "known_use_exclusion": [{"predicted": "Obstructive Lung Disease"}]},
        {"action": "rereview_result", "verdict": "withdraw", "file": "b.md", "withdrawn_predictions": ["alopecia"]},
        {"action": "rereview_result", "verdict": "withdraw", "file": "c.md", "status": "withdrawn",
         "withdrawn_predictions": ["x"]},
        {"action": "rereview_result", "verdict": "downgrade", "file": "d.md", "withdrawn_predictions": ["y"]},
    ]}), encoding="utf-8")
    assert X.withdrawn_predictions(f) == {"a.md": {"obstructive lung disease"}, "b.md": {"alopecia"}}


# ---- description 的等級跟頁首（2026-11-03 用戶決定）----
def desc_rec(lv_old, lv_new):
    return {"id": "demo-desc", "file": "demo.md", "checked": "2026-11-03", "action": "description_level",
            "summary": "頁面描述（description）的證據等級", "original_description": "x",
            "original_level": lv_old, "new_level": lv_new, "note": "n", "sources": SRC}


def test_description_level_follows_header_na():
    page = PAGE.replace("evidence_level: L5\n", 'evidence_level: L5\ndescription: "Demo：預測新適應症為甲病（證據等級 L3）。原適應症：舊"\n')
    assert F.description_level_problems(page)
    out, problems = render(withdraw_recs() + [desc_rec("L3", "N/A")], page)
    assert problems == []
    assert 'description: "Demo：預測新適應症為甲病（僅已知用途）。原適應症：舊"' in out
    assert F.description_level_problems(out) == []
    assert "「證據等級 L3」改為「僅已知用途」" in out


def test_description_level_follows_header_level():
    page = PAGE.replace("evidence_level: L5\n", 'evidence_level: L5\ndescription: "Demo（甲病，證據等級 L2）。"\n')
    out, _ = render(recs(verdict="maintain", new="L3", updates=False) + [desc_rec("L2", "L3")], page)
    assert 'description: "Demo（甲病，證據等級 L3）。"' in out
    # 沒有紀錄就不動 description（gate 會擋）
    out2, _ = render(recs(verdict="maintain", new="L3", updates=False), page)
    assert "證據等級 L2" in out2 and F.description_level_problems(out2)


# ---- 撤回的預測不進搜尋索引／FHIR（2026-11-03 用戶決定）----
def test_withdrawn_name_matching():
    from twtxgnn.regulatory import withdrawn as W
    t = {"camphor": {"erectile dysfunction (disease)"}, "terbutaline": {"obstructive lung disease"}}
    assert W.is_withdrawn(t, "terbutaline", "Obstructive Lung Disease")
    assert W.is_withdrawn(t, "camphor", "勃起功能障礙 (Erectile Dysfunction) (erectile dysfunction (disease))")
    assert W.is_withdrawn(t, "terbutaline", "阻塞性肺病（obstructive lung disease）")
    assert not W.is_withdrawn(t, "terbutaline", "respiratory malformation")
    assert not W.is_withdrawn(t, "omalizumab", "obstructive lung disease")


def test_fhir_cud_key():
    import generate_fhir_resources as G
    res = G.create_clinical_use_definition({"slug": "terbutaline", "name": "Terbutaline"},
                                           {"name": "obstructive lung disease", "score": 99.0}, "https://x")
    assert G._cud_key(res) == ("terbutaline", "obstructive lung disease")
