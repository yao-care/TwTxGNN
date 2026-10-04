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
  rereview_result  重審結論（2026-10-03 起）：用 resolves 指回一筆 rereview 紀錄。被指到的
            rereview 不再顯示「待重審」框，同一位置改顯示「重審結果」框（維持／降級／撤回、
            原等級→新等級、理由與文獻）；rereview 紀錄本身保留，查核紀錄表兩筆都列。
            table_updates（[{label, claim, replacement}]）把頁面上該適應症的證據等級／決策
            儲存格換成重審後的值（降級、撤回時才用）；原值留在紀錄的 claim，查核紀錄表列出變更。
  header_level  頁首等級重算的留存紀錄（2026-10-04 起）：頁首等級依快速總覽重算（全站規則，
            見 src/twtxgnn/regulatory/page_format.py）後與原值不同的頁，各記一筆 original_level／
            new_level／original_parent／new_parent。不顯示框，只在查核紀錄表列「頁首等級依總覽表重算（原 Lx→Ly）」。
            頁首重算本身每頁都做（有沒有紀錄都一樣），產線寫頁前也做。
紀錄可帶 history：同 id 重發時的前版（整筆前版內容＋retired 日期＋reason）。correct 紀錄
在頁面上找不到 claim 時，會改找 history 裡前版的 replacement 換成新版（頁面停在前版時用）。
紀錄的 status 為 superseded（錨點落在已改由程式產生的許可證表或張數上）時：紀錄保留、
頁面不再顯示它的框，查核紀錄表仍列出並註明「已由程式化許可證表取代」。
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
sys.path.insert(0, str(ROOT / "src"))
from twtxgnn.regulatory import page_format as F  # noqa: E402
DOCS = ROOT / "docs"
DATA = DOCS / "_data" / "drug_reviews.json"
DRUGS = DOCS / "_drugs"

LABEL = {"correct": "查核更正", "annotate": "查核加註", "rereview": "待重審", "rereview_result": "重審結果"}
ACTION_ZH = {"correct": "更正", "annotate": "加註", "rereview": "標記待重審", "section": "新增附來源段落",
             "rereview_result": "重審完成", "header_level": "頁首等級依總覽表重算"}
VERDICT_ZH = {"maintain": "維持", "downgrade": "降級", "withdraw": "撤回"}


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
    """同一筆紀錄裡重複的來源網址只顯示一次（紀錄本身不動，逐字摘錄仍全部留在 JSON）。"""
    seen, out = set(), []
    for s in rec["sources"]:
        if s["url"] in seen:
            continue
        seen.add(s["url"])
        out.append(f"[{s['title']}]({s['url']})")
    return "；".join(out)


BLOCK_RE = re.compile(r"<!-- review:begin (\S+) -->.*?<!-- review:end \1 -->", re.S)


def find_outside(text, needle):
    """找 needle 在頁面原文中的位置，跳過已插入的查核框（框裡會引用原句，不能當定位點）。"""
    spans = [m.span() for m in BLOCK_RE.finditer(text)]
    start = 0
    while True:
        i = text.find(needle, start)
        if i < 0:
            return -1
        hit = next((s for s in spans if s[0] <= i < s[1]), None)
        if not hit:
            return i
        start = hit[1]


def display(s):
    """表格列原句改成「格／格」顯示，避免引言框裡的 | 被當成表格。"""
    s = s.strip()
    if s.startswith("|"):
        s = "／".join(c.strip() for c in s.strip("|").split("|"))
    return s.replace("|", "&#124;")


def level_text(lv):
    """new_level 可以是字串或 {適應症: 等級}；後者顯示成「頭痛疾患 L4；A、B L5」（同等級併列）。"""
    if isinstance(lv, str):
        return lv
    groups = {}
    for k, v in lv.items():
        groups.setdefault(v, []).append(k)
    return "；".join(f"{'、'.join(ks)} {v}" for v, ks in groups.items())


def level_change(rec):
    o, n = rec["original_level"], level_text(rec["new_level"])
    return f"證據等級 {o} 不變" if n == o else f"證據等級 {o}→{n}"


def note_md(rec):
    label = LABEL[rec["action"]]
    head = f"> **{label}（{rec['checked']}）**："
    if rec["action"] == "correct":
        body = f"原寫「{display(rec['claim'])}」。{rec['note']}"
    elif rec["action"] == "rereview_result":
        body = f"**{VERDICT_ZH[rec['verdict']]}**（{level_change(rec)}）。{rec['note']}"
        ups = rec.get("table_updates") or []
        if ups:
            body += f"本頁{'、'.join(u['label'] for u in ups)}已依重審結果更新，原值列在下方查核紀錄。"
    else:
        body = rec["note"]
    tail = ""
    if rec["action"] == "rereview_result" and rec.get("decision_note"):
        tail = f"\n>\n> 決策建議另議：{rec['decision_note']}"
    return f"{begin(rec['id'])}\n\n{head}{body}依據：{sources_md(rec)}。{tail}\n\n{end(rec['id'])}"


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
        # 頁面上是原句就換；頁面停在前版更正（同 id 重發）就把前版換成新版
        olds = [rec["claim"]] + [h["replacement"] for h in rec.get("history") or []
                                 if h.get("replacement") and h["replacement"] != rec["replacement"]]
        for old in olds:
            j = find_outside(text, old)
            if j >= 0:
                text = text[:j] + rec["replacement"] + text[j + len(old):]
                break
        anchor = rec["replacement"]
    else:
        anchor = rec.get("anchor") or rec["claim"]
    i = find_outside(text, anchor)
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
    resolved = {r["resolves"] for r in recs if r["action"] == "rereview_result"}
    for r in recs:
        item = r.get("summary") or display(r["claim"])
        act = ACTION_ZH[r["action"]]
        if r["action"] == "rereview" and r["id"] in resolved:
            act = "標記待重審 → 已重審（見下列重審結果）"
        if r["action"] == "header_level":
            act = f"頁首等級依總覽表重算（原 {r['original_level']}→{r['new_level']}）"
        if r["action"] == "rereview_result":
            act = f"重審：{VERDICT_ZH[r['verdict']]}，{level_change(r)}"
            for u in r.get("table_updates") or []:
                act += f"；{u['label']}：原「{display(u['claim'])}」→「{display(u['replacement'])}」"
        if r.get("history"):
            act += f"（{r['history'][-1]['retired']} 修訂，前版保留於紀錄）"
        if r.get("status") == "superseded":
            act = f"已由程式化許可證表取代（原為{act}）"
        rows.append(f"| {r['checked']} | {item} | {act} | {sources_md(r)} |")
    intro = ("以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；"
             "更正只限基本藥理事實，模型預測、證據等級與結論未改寫。")
    if all(r["action"] == "header_level" for r in recs):
        intro = ("以下是本頁的查核紀錄；頁首證據等級依本頁「快速總覽」的證據等級列重算，"
                 "模型預測、總覽表與結論未改寫。")
    elif any(r["action"] == "rereview_result" and r.get("table_updates") for r in recs):
        intro = ("以下是本頁經人工對照官方仿單或衛福部食藥署許可證的查核紀錄；"
                 "更正只限基本藥理事實，模型預測原文未改寫；證據等級與決策只依重審結果（降級或撤回）更新，原值列在下表。")
    return f"{begin('log')}\n\n## 查核紀錄\n\n{intro}\n\n" + "\n".join(rows) + f"\n\n{end('log')}\n\n"


def apply_text(text, fname):
    """記憶體內套用某頁的紀錄（產線寫頁前用）。回傳 (新內容, 問題清單)。"""
    recs = [r for r in load() if r["file"] == fname]
    if not recs:
        return text, []
    problems = []
    for _ in range(4):
        local = []
        nxt = render_page(text, recs, local)
        if nxt == text:
            break
        text = nxt
    problems.extend(local)
    return text, problems


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


def apply_result(text, rereview, res, problems):
    """重審結果：先把該適應症的等級／決策儲存格換成重審後的值，再在原「待重審」框的位置放結果框。"""
    for u in res.get("table_updates") or []:
        j = find_outside(text, u["claim"])
        if j >= 0:
            text = text[:j] + u["replacement"] + text[j + len(u["claim"]):]
        elif find_outside(text, u["replacement"]) < 0:
            problems.append(f"{res['id']}：頁面上找不到要更新的「{u['claim'][:40]}…」（頁面可能被重產改寫，需人工重查）")
    rec = dict(res, anchor=res.get("anchor") or rereview.get("anchor") or rereview["claim"])
    return apply_record(text, rec, problems)


def validate(recs):
    """rereview_result 的結構檢查：resolves 要指到同頁的 rereview、一筆 rereview 最多一筆結果、
    verdict 合法、降級時新等級要低於原等級。"""
    errs, by_id, seen = [], {r["id"]: r for r in recs}, {}
    if len(by_id) != len(recs):
        errs.append("drug_reviews.json 有重複的 id")
    for r in recs:
        if r["action"] != "rereview_result":
            continue
        tgt = by_id.get(r.get("resolves"))
        if not tgt or tgt["action"] != "rereview" or tgt["file"] != r["file"]:
            errs.append(f"{r['id']}：resolves 指向不存在或不是同頁 rereview 的紀錄 {r.get('resolves')}")
        if r.get("resolves") in seen:
            errs.append(f"{r['id']}：{r['resolves']} 已有重審結果 {seen[r['resolves']]}")
        seen[r.get("resolves")] = r["id"]
        if r.get("verdict") not in VERDICT_ZH:
            errs.append(f"{r['id']}：verdict 必須是 {sorted(VERDICT_ZH)}")
        if r.get("verdict") == "downgrade":
            o = [int(x) for x in re.findall(r"L([1-5])", r["original_level"])]
            n = [int(x) for x in re.findall(r"L([1-5])", level_text(r["new_level"]))]
            if not (o and n and min(n) > min(o)):
                errs.append(f"{r['id']}：verdict=downgrade 但新等級沒有低於原等級")
    return errs


def render_page(text, recs, problems):
    # 先清掉本頁所有先前產生的區塊，再依序重套；否則 A 紀錄的說明文字裡引用的原句
    # 會被 B 紀錄誤認成頁面原文。
    text = re.sub(r"\n*<!-- review:begin (\S+) -->.*?<!-- review:end \1 -->\n*", "\n\n", text, flags=re.S)
    text = F.fix_table_spacing(text)  # 先補表格前空行，查核框的插入位置才與產線一致
    results = {r["resolves"]: r for r in recs if r["action"] == "rereview_result"}
    for r in recs:
        if r.get("status") == "superseded":
            continue  # 錨點所在的許可證表／張數已由程式化區塊取代：紀錄保留、頁面不再顯示框
        if r["action"] in ("rereview_result", "header_level"):
            continue  # rereview_result 在它 resolves 的那筆 rereview 位置渲染；header_level 只進查核紀錄表
        if r["action"] == "rereview" and r["id"] in results:
            text = apply_result(text, r, results[r["id"]], problems)
            continue
        text = apply_record(text, r, problems)
    text = F.sync_header_level(text)  # 頁首等級依快速總覽重算（全站規則，見 page_format）
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
    problems, changed = validate(recs), []
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
