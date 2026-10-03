"""許可證確定性處理與藥物報告後處理的測試（2026-10-03）。"""
import json
from unittest import mock

import pytest

from twtxgnn.regulatory import tfda_licenses as T
from twtxgnn.regulatory import page_postprocess as P


def rec(lid, ing, zh="品名", en="", ind="適應症", cancelled=False, form="錠劑"):
    return {"許可證字號": lid, "主成分略述": ing, "中文品名": zh, "英文品名": en, "適應症": ind,
            "註銷狀態": "已註銷" if cancelled else "", "註銷日期": "2001/01/01" if cancelled else "",
            "有效日期": "2030/01/01", "劑型": form, "申請商名稱": "某公司"}


@pytest.fixture
def records():
    return [
        rec("衛署藥製字第000001號", "PROCAINE HCL", "普魯卡因注射液"),
        rec("衛署藥製字第000001號", "PROCAINE HCL", "普魯卡因注射液"),  # 資料集重複列
        rec("內衛藥製字第004458號", "PENICILLIN G POTASSIUM BUFFERED;;PENICILLIN G PROCAINE (EQ TO BENZYLPENICILLIN PROCAINE)"),
        rec("衛署藥製字第004771號", "MAGNESIUM SULFATE 7H2O", "硫酸鎂注射液"),
        rec("衛部藥輸字第026388號", "MAGNESIUM SULPHATE HEPTAHYDRATE;;L-LYSINE ACETATE", "營養輸注液"),
        rec("衛署藥製字第026490號", "TOCOPHEROL ACETATE ALPHA DL-", "維他命E"),
        rec("衛署藥製字第004676號", "RIFAMPIN (EQ TO RIFAMPICIN) (EQ TO RIMACTAN)", "立汎黴素"),
        rec("衛部藥製字第061007號", "SODIUM DEOXYCHOLATE", "去氧膽酸鈉"),
        rec("內衛藥製字第003610號", "DEMECLOCYCLINE;;NYSTATIN", "立達泰定膠囊", cancelled=True),
        rec("衛部藥陸輸字第001025號", None, "香葉木素", en="Diosmin"),
    ]


class TestMatching:
    def test_procaine_excludes_penicillin_g_procaine(self, records):
        ids = {x["id"] for x in T.licenses_for_drug("Procaine", records)}
        assert ids == {"衛署藥製字第000001號"}

    def test_distinct_count(self, records):
        assert T.summarize(T.licenses_for_drug("Procaine", records))["total"] == 1

    def test_salt_hydrate_and_combo(self, records):
        lics = T.licenses_for_drug("Magnesium Sulfate", records)
        assert [x["id"] for x in lics] == ["衛署藥製字第004771號"]  # SULPHATE 拼法不同，不硬配

    def test_inverted_name(self, records):
        assert [x["id"] for x in T.licenses_for_drug("Alpha-Tocopherol Acetate", records)] == ["衛署藥製字第026490號"]

    def test_eq_to_alias_and_synonym(self, records):
        assert [x["id"] for x in T.licenses_for_drug("Rifampicin", records)] == ["衛署藥製字第004676號"]

    def test_ic_acid_to_ate(self, records):
        assert [x["id"] for x in T.licenses_for_drug("Deoxycholic Acid", records)] == ["衛部藥製字第061007號"]

    def test_english_name_when_no_ingredient(self, records):
        assert [x["id"] for x in T.licenses_for_drug("Diosmin", records)] == ["衛部藥陸輸字第001025號"]

    def test_kinds_and_status(self, records):
        lics = T.licenses_for_drug("Nystatin", records)
        assert lics[0]["kind"] == "combo" and lics[0]["status"] == "cancelled"
        s = T.summarize(lics)
        assert (s["total"], s["valid_single"], s["valid_combo"], s["cancelled"]) == (1, 0, 0, 1)

    def test_no_cap(self):
        many = [rec(f"衛部藥製字第{i:06d}號", "TESTOLIDE") for i in range(45)]
        assert len(T.licenses_for_drug("Testolide", many)) == 45


PAGE = """---
title: Procaine
---

<div id="pharmacist">

## 藥師評估報告

</div>

使用 `txgnn-pipeline` 技能確認任務範圍後，以下根據 Evidence Pack 產生評估報告：

---

# Procaine：測試

## 一句話總結

Procaine 是局部麻醉藥，台灣已有 20 張許可證。目前 Evidence Pack 中缺乏資料。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 許可證數 | 20 張 |

## 台灣上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| 內衛藥製字第004458號 | 博西林 | 注射劑 | 感染症 |
| （待確認） | 其他 | 注射劑 | - |

**台灣共有 40 張相關許可證，目前有效者約 6 張。**

| 欄位 | 內容 |
|------|------|
| 許可證字號 | 衛署藥製字第999999號 |

## 安全性考量

無。
"""


class TestPostprocess:
    def lics(self, records):
        return T.licenses_for_drug("Procaine", records)

    def test_full_pipeline(self, records):
        new, bad = P.postprocess_with_licenses(PAGE, "Procaine", self.lics(records), "2026-09-29")
        assert bad == []
        assert "txgnn-pipeline" not in new and "Evidence Pack" not in new
        assert "目前彙整資料中缺乏資料" in new
        assert "004458" not in new and "待確認" not in new and "999999" not in new  # 別藥、佔位、垂直表都被取代
        assert "| 許可證數 | 1 張（有效單方 1／有效複方 0／已註銷 0） |" in new
        assert "台灣已有 1 張許可證（有效 1 張）" in new
        assert "40 張相關許可證" not in new
        assert new.count(T.BEGIN) == 1 and "衛署藥製字第000001號" in new

    def test_idempotent(self, records):
        once, _ = P.postprocess_with_licenses(PAGE, "Procaine", self.lics(records), "2026-09-29")
        twice, _ = P.postprocess_with_licenses(once, "Procaine", self.lics(records), "2026-09-29")
        assert once == twice

    def test_validate_flags_foreign_license(self, records):
        text = "見 內衛藥製字第004458號 與 衛署藥製字第000001號"
        assert T.validate_page(text, {x["id"] for x in self.lics(records)}) == ["內衛藥製字第004458號"]

    def test_validate_ignores_review_boxes(self, records):
        text = "<!-- review:begin x -->\n內衛藥製字第004458號\n<!-- review:end x -->"
        assert T.validate_page(text, set()) == []

    def test_fold_large_tables(self):
        many = [T.to_license(rec(f"衛部藥製字第{i:06d}號", "TESTOLIDE")) for i in range(T.FOLD_AT + 1)]
        block = T.render_block("Testolide", many, "2026-09-29")
        assert "<details>" in block and "| 許可證字號 |" not in block

    def test_preamble_english(self):
        text = "The `txgnn-pipeline` skill confirms this is TxGNN context work.\n\n---\n\n# 標題\n\n內文"
        assert P.strip_preamble(text) == "# 標題\n\n內文"

    def test_no_preamble_untouched(self):
        text = "# 標題\n\n內文提到技能也不動"
        assert P.strip_preamble(text) == text


class TestSnapshot:
    def test_roundtrip(self, tmp_path, records):
        lics = [T.compact(x) for x in T.licenses_for_drug("Procaine", records)]
        p = T.write_snapshot({"procaine": {"query": "Procaine", "licenses": lics}}, "2026-09-29", tmp_path / "s.json.gz")
        snap = T.load_snapshot(p)
        assert snap["meta"]["data_date"] == "2026-09-29"
        assert snap["drugs"]["procaine"]["licenses"][0]["id"] == "衛署藥製字第000001號"

    def test_deterministic_bytes(self, tmp_path):
        a = T.write_snapshot({"x": {"query": "X", "licenses": []}}, "d", tmp_path / "a.gz").read_bytes()
        b = T.write_snapshot({"x": {"query": "X", "licenses": []}}, "d", tmp_path / "b.gz").read_bytes()
        assert a == b


class TestLLMClient:
    def test_disables_skills_and_settings_and_cleans(self):
        from twtxgnn.reviewer import llm_client
        client = llm_client.LLMClient() if hasattr(llm_client, "LLMClient") else None
        if client is None:
            pytest.skip("LLMClient not found")
        out = mock.Mock(returncode=0, stdout="使用 `txgnn-pipeline` 技能確認後：\n\n# 報告\n\n依 Evidence Pack 撰寫", stderr="")
        with mock.patch.object(llm_client.subprocess, "run", return_value=out) as run:
            text = client.chat("hi")
        cmd = run.call_args[0][0]
        assert "--disable-slash-commands" in cmd
        i = cmd.index("--setting-sources")
        assert cmd[i + 1] == ""
        assert text == "# 報告\n\n依彙整資料撰寫"
