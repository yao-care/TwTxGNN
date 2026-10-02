#!/usr/bin/env python3
"""由 docs/_drugs/*.md 產生兩頁索引（只讀藥物頁，不改動）：
  docs/nct-lookup.md      NCT 編號 → 出現在哪顆藥的報告
  docs/tw-availability.md 英文藥名 → 報告記載的台灣上市狀態與商品名
用法：uv run python scripts/build_lookup_pages.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRUGS = ROOT / "docs" / "_drugs"
NCT_RE = re.compile(r"NCT\d{8}")


def front(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    return meta


def cell(s):
    return re.sub(r"\s+", " ", s.replace("|", "／")).strip()


def collect():
    drugs = []
    for f in sorted(DRUGS.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        meta = front(text)
        if meta.get("search_exclude") == "true":
            continue
        name = meta.get("title", f.stem)
        slug = f.stem.replace("_", "-")
        drugs.append((f, text, name, slug, meta.get("evidence_level", "")))
    return drugs


def nct_rows(drugs):
    rows = {}
    for f, text, name, slug, lvl in drugs:
        for line in text.splitlines():
            if not line.startswith("|"):
                continue
            cols = [c.strip() for c in line.strip().strip("|").split("|")]
            m = NCT_RE.search(cols[0]) if cols else None
            if not m or len(cols) < 3:
                continue
            nct = m.group(0)
            desc = max(cols[1:], key=len)
            if len(desc) < 8:
                desc = ""
            rows.setdefault(nct, []).append((name, slug, lvl, cell(desc)))
    return rows


def avail_rows(drugs):
    out = []
    for f, text, name, slug, lvl in drugs:
        status = brand = ""
        for line in text.splitlines():
            if line.startswith("| 台灣上市 ") and not status:
                status = cell(line.split("|")[2])
            elif re.match(r"\| 台灣(商品名|品牌名) ", line) and not brand:
                brand = cell(line.split("|")[2])
        out.append((name, slug, lvl, status, brand))
    return out


def write_nct(rows):
    lines = ["""---
layout: default
title: 用 NCT 編號找藥
parent: 資源
nav_order: 3
description: "手上只有一組 NCT 試驗編號，想知道它出現在 TwTxGNN 哪顆藥的報告裡。本頁依編號列出對應藥物與試驗摘要，並連到 ClinicalTrials.gov 原始登記。"
permalink: /nct-lookup/
---

# 用 NCT 編號找藥

<p class="key-answer" data-question="拿到一組 NCT 編號，怎麼知道它對應哪個藥？">
下表把 TwTxGNN 藥物報告引用到的 ClinicalTrials.gov 試驗編號（共 %d 組）反查回藥物。找到編號後，點藥名看完整報告，點編號看 ClinicalTrials.gov 的原始登記。
</p>

用瀏覽器的頁內搜尋（Ctrl+F 或 Cmd+F）貼上編號即可。

編號後面的「藥物」欄，意思是「該藥的報告有引用這個試驗」。試驗本身不一定只測那一顆藥，有些是複方、比較藥或同類藥的研究。要確認受試藥物與適應症，請以 ClinicalTrials.gov 登記頁為準。

編號不在表中，代表本站報告沒引用它，不代表試驗不存在。請直接到 [ClinicalTrials.gov](https://clinicaltrials.gov/) 輸入編號查詢。

試驗摘要欄文字取自各藥物報告，是本站整理的簡述，不是登記頁的原文。

| NCT 編號 | 藥物 | 證據等級 | 報告中的試驗摘要 |
|----------|------|:--------:|------------------|""" % len(rows)]
    for nct in sorted(rows):
        for name, slug, lvl, desc in sorted(rows[nct]):
            lines.append(
                f"| [{nct}](https://clinicaltrials.gov/study/{nct}) | [{name}](/drugs/{slug}/) | {lvl} | {desc} |"
            )
    lines.append("""
---

## 出處

- 試驗登記：[ClinicalTrials.gov](https://clinicaltrials.gov/)（美國國家醫學圖書館）
- 證據等級（L1 到 L5）的定義見[使用指南](/guide/)與[方法論](/methodology/)

<div class="disclaimer">
<strong>免責聲明</strong><br>
本頁是研究資料的查找索引，不構成醫療建議。藥物使用請遵循醫師與藥師指示。
</div>
""")
    (ROOT / "docs" / "nct-lookup.md").write_text("\n".join(lines), encoding="utf-8")


def write_avail(rows):
    n_status = sum(1 for r in rows if r[3])
    n_brand = sum(1 for r in rows if r[4])
    lines = ["""---
layout: default
title: 台灣有沒有這個藥
parent: 資源
nav_order: 4
description: "看到外文藥名，想知道台灣有沒有上市、中文商品名叫什麼。本頁列出 TwTxGNN 報告記載的各藥台灣上市狀態與商品名，並說明如何到食藥署核對許可證。"
permalink: /tw-availability/
---

# 台灣有沒有這個藥

<p class="key-answer" data-question="外文藥名在台灣有沒有上市？中文商品名是什麼？">
下表依英文藥名列出 TwTxGNN 報告（共 %d 份）記載的台灣上市狀態；其中 %d 份記有商品名。每一列都連到該藥的完整報告，報告內有許可證號、劑型與效期。
</p>

用瀏覽器的頁內搜尋（Ctrl+F 或 Cmd+F）貼上英文藥名即可。

## 怎麼讀這張表

「台灣上市狀態」是各份報告撰寫當下，依衛福部食藥署公開的藥品許可證資料整理的結果。許可證會到期、註銷或新核發，所以這欄會落後於現況。要確認某個藥現在能不能在台灣買到，請到[衛生福利部食品藥物管理署](https://www.fda.gov.tw/)的藥品許可證查詢，用許可證號或成分名核對。資料集本身可在[食藥署開放資料平臺](https://data.fda.gov.tw/)取得。

商品名欄空白，代表那份報告沒有記錄商品名，要看許可證號請點進報告。商品名欄寫「等」的，是只列出部分。

有許可證不等於適合自己使用。本站只整理研究資料，用藥請問醫師或藥師。

| 英文藥名 | 台灣上市狀態（報告記載） | 台灣商品名（報告記載） | 證據等級 |
|----------|--------------------------|------------------------|:--------:|""" % (len(rows), n_brand)]
    for name, slug, lvl, status, brand in sorted(rows, key=lambda r: r[0].lower()):
        lines.append(f"| [{name}](/drugs/{slug}/) | {status or '見報告'} | {brand} | {lvl} |")
    lines.append("""
---

## 出處

- 許可證資料：衛生福利部食品藥物管理署，[食藥署開放資料平臺](https://data.fda.gov.tw/)
- 各藥的許可證號、劑型與效期，請見該藥報告的「台灣上市狀態」一節

<div class="disclaimer">
<strong>免責聲明</strong><br>
本頁是研究資料的查找索引，不構成醫療建議。藥物使用請遵循醫師與藥師指示。
</div>
""")
    (ROOT / "docs" / "tw-availability.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    d = collect()
    write_nct(nct_rows(d))
    write_avail(avail_rows(d))
    print("ok")
