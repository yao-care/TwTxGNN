#!/usr/bin/env python3
"""把人工查核紀錄（docs/_data/drug_reviews.json）套用到 docs/_drugs/*.md。

為什麼要有這支（2026-10-03 建）：
  藥物頁是產線生成的（data/notes/ → sync_notes_to_docs.py 或 build_docs.py 覆寫整頁）。
  人工查核後的更正、加註、待重審標記、附來源的作用機轉段，如果只改在頁面上，
  下次重產就會被蓋掉。所以查核結果一律記在 docs/_data/drug_reviews.json（機器可讀、
  之後補的藥沿用同一份），再由這支套到頁面上；產線兩支生成腳本結尾都會呼叫它，
  scripts/check_seo_docs.py 也會檢查每筆紀錄都還在頁面上（被蓋掉＝gate 不過）。

紀錄的 action：
  correct   基本藥理事實照仿單／許可證更正：頁面上的 claim 換成 replacement，
            並在該段落後加「查核更正」說明（原句、依據、日期）。
  annotate  原文不動，在 claim 所在段落（或表格）後加「查核加註」。
  rereview  在 anchor 所在段落後加「待重審」標記（預測本身與證據等級不改）。
  section   在 before 指定的標題前插入一整段 markdown（附來源的作用機轉段）。
每頁另在「免責聲明」前產生「查核紀錄」表，列出該頁全部紀錄。

用法：
  python3 scripts/apply_drug_reviews.py           # 套用（可重複執行，結果相同）
  python3 scripts/apply_drug_reviews.py --check   # 只檢查，有未套用的紀錄就 exit 1
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
DATA = DOCS / "_data" / "drug_reviews.json"
DRUGS = DOCS / "_drugs"

LABEL = {"correct": "查核更正", "annotate": "查核加註", "rereview": "待重審"}
ACTION_ZH = {"correct": "更正", "annotate": "加註", "rereview": "標記待重審", "section": "新增附來源段落"}


def load():
    return json.loads(DATA.read_text(encoding="utf-8"))["records"]


def begin(rid):
    return f"<!-- review:begin {rid} -->"


def end(rid):
    return f"<!-- review:end {rid} -->"


def strip_block(text, rid):
    """移除先前產生的同 id 區塊（連同前後空行），讓套用可重複執行。"""
    pat = re.compile(r"\n*" + re.escape(begin(rid)) + r".*?" + re.escape(end(rid)) + r"\n*", re.S)
    return pat.sub("\n\n", text)


def sources_md(rec):
    return "；".join(f"[{s['title']}]({s['url']})" for s in rec["sources"])


def display(s):
    """表格列原句改成「格／格」顯示，避免引言框裡的 | 被當成表格。"""
    s = s.strip()
    if s.startswith("|"):
        s = "／".join(c.strip() for c in s.strip("|").split("|"))
    return s.replace("|", "&#124;")


def note_md(rec):
    label = LABEL[rec["action"]]
    head = f"> **{label}（{rec['checked']}）**："
    if rec["action"] == "correct":
        body = f"原寫「{display(rec['claim'])}」。{rec['note']}"
    else:
        body = rec["note"]
    return f"{begin(rec['id'])}\n\n{head}{body}依據：{sources_md(rec)}。\n\n{end(rec['id'])}"


def block_end(text, pos):
    """pos 所在段落／表格／清單的結尾（下一個空行的位置）。"""
    m = re.compile(r"\n[ \t]*\n").search(text, pos)
    return m.start() if m else len(text)


def apply_record(text, rec, problems):
    rid = rec["id"]
    text = strip_block(text, rid)
    act = rec["action"]
    if act == "section":
        m = re.search(rec["before"], text, re.M)
        if not m:
            problems.append(f"{rid}：找不到插入位置 {rec['before']}")
            return text
        block = f"{begin(rid)}\n\n{rec['markdown'].strip()}\n\n{end(rid)}\n\n"
        return text[:m.start()] + block + text[m.start():]
    if act == "correct":
        if rec["claim"] in text:
            text = text.replace(rec["claim"], rec["replacement"], 1)
        anchor = rec["replacement"]
    else:
        anchor = rec.get("anchor") or rec["claim"]
    i = text.find(anchor)
    if i < 0:
        problems.append(f"{rid}：頁面上找不到 {'replacement' if act == 'correct' else 'anchor'}「{anchor[:40]}…」（頁面可能被重產改寫，需人工重查）")
        return text
    e = block_end(text, i)
    # 同一段後面已有別筆紀錄的框，就接在它們後面，讓顯示順序跟紀錄順序一致
    nxt = re.compile(r"\s*<!-- review:begin (\S+) -->.*?<!-- review:end \1 -->", re.S)
    while True:
        m = nxt.match(text, e)
        if not m or m.group(1) == "log":
            break
        e = m.end()
    return text[:e] + "\n\n" + note_md(rec) + text[e:]


def log_md(recs):
    rows = ["| 查核日期 | 項目 | 處理 | 依據 |", "|---------|------|------|------|"]
    for r in recs:
        item = r.get("summary") or display(r["claim"])
        rows.append(f"| {r['checked']} | {item} | {ACTION_ZH[r['action']]} | {sources_md(r)} |")
    intro = ("以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；"
             "更正只限基本藥理事實，模型預測、證據等級與結論未改寫。")
    return f"{begin('log')}\n\n## 查核紀錄\n\n{intro}\n\n" + "\n".join(rows) + f"\n\n{end('log')}\n\n"


def apply_page(path, recs, problems):
    """套到不再變動為止（空行正規化在第一次套用時可能多收斂一輪），確保重跑結果相同。"""
    orig = path.read_text(encoding="utf-8")
    text = orig
    for _ in range(4):
        local = []
        nxt = render_page(text, recs, local)
        if nxt == text:
            break
        text = nxt
    problems.extend(local)
    return text, text != orig


def render_page(text, recs, problems):
    # 先清掉本頁所有先前產生的區塊，再依序重套；否則 A 紀錄的說明文字裡引用的原句
    # 會被 B 紀錄誤認成頁面原文。
    text = re.sub(r"\n*<!-- review:begin (\S+) -->.*?<!-- review:end \1 -->\n*", "\n\n", text, flags=re.S)
    for r in recs:
        text = apply_record(text, r, problems)
    m = re.search(r"^## 免責聲明", text, re.M)
    log = log_md(recs)
    text = text[:m.start()] + log + text[m.start():] if m else text.rstrip() + "\n\n" + log
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def run(check=False):
    recs = load()
    by_file = {}
    for r in recs:
        by_file.setdefault(r["file"], []).append(r)
    problems, changed = [], []
    for fname, rs in sorted(by_file.items()):
        path = DRUGS / fname
        if not path.exists():
            problems.append(f"{fname}：藥物頁不存在")
            continue
        new, diff = apply_page(path, rs, problems)
        if diff:
            changed.append(fname)
            if not check:
                path.write_text(new, encoding="utf-8")
    return problems, changed


def check_errors():
    """給 check_seo_docs.py 用：回傳錯誤字串清單（空＝全部紀錄都已套用在頁面上）。"""
    if not DATA.exists():
        return []
    problems, changed = run(check=True)
    errs = [f"藥物頁查核紀錄：{p}" for p in problems]
    errs += [f"藥物頁查核紀錄未套用（或被重產蓋掉）：{f}，請跑 python3 scripts/apply_drug_reviews.py" for f in changed]
    return errs


if __name__ == "__main__":
    check = "--check" in sys.argv
    problems, changed = run(check=check)
    for p in problems:
        print("  ✗", p)
    if check:
        print(f"查核紀錄：{'✗' if (problems or changed) else '✓'} 待套用 {len(changed)} 頁、問題 {len(problems)} 項")
        sys.exit(1 if (problems or changed) else 0)
    print(f"查核紀錄：已套用 {len(changed)} 頁、問題 {len(problems)} 項")
    sys.exit(1 if problems else 0)
