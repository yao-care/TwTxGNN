#!/usr/bin/env python3
"""
Pre-flight 檢查清單腳本。

在產生報告前驗證所有必要資料來源是否已查詢。
"""

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class CheckItem:
    """檢查項目"""
    name: str
    description: str
    blocking: bool
    status: str = "unchecked"  # unchecked, passed, failed, skipped
    message: str = ""


class PreflightChecker:
    """Pre-flight 檢查器"""

    def __init__(self, evidence_pack: dict[str, Any]):
        self.evidence_pack = evidence_pack
        self.checks: list[CheckItem] = []
        self._init_checks()

    def _init_checks(self):
        """初始化檢查項目"""
        # 資料來源查核
        self.checks.extend([
            CheckItem(
                name="tfda_license",
                description="TFDA 許可證查詢完成",
                blocking=True,
            ),
            CheckItem(
                name="tfda_label",
                description="TFDA 仿單 PDF 下載/解析完成",
                blocking=True,
            ),
            CheckItem(
                name="ddi_database",
                description="DDI 資料庫查詢完成",
                blocking=True,
            ),
            CheckItem(
                name="clinicaltrials",
                description="ClinicalTrials.gov 查詢完成",
                blocking=False,
            ),
            CheckItem(
                name="pubmed",
                description="PubMed 查詢完成",
                blocking=False,
            ),
            CheckItem(
                name="drugbank_moa",
                description="DrugBank MOA 查詢完成",
                blocking=False,
            ),
        ])

        # 必要欄位檢核
        self.checks.extend([
            CheckItem(
                name="drug_basic_info",
                description="藥物基本資訊完整",
                blocking=True,
            ),
            CheckItem(
                name="indication_icd10",
                description="每個適應症有 ICD-10",
                blocking=False,
            ),
            CheckItem(
                name="indication_evidence_level",
                description="每個適應症有證據等級",
                blocking=True,
            ),
            CheckItem(
                name="data_gap_unlock",
                description="每個 Data Gap 有解鎖條件",
                blocking=True,
            ),
        ])

    def run_all_checks(self) -> bool:
        """執行所有檢查"""
        self._check_tfda_license()
        self._check_tfda_label()
        self._check_ddi_database()
        self._check_clinicaltrials()
        self._check_pubmed()
        self._check_drugbank_moa()
        self._check_drug_basic_info()
        self._check_indication_icd10()
        self._check_indication_evidence_level()
        self._check_data_gap_unlock()

        # 檢查是否有 blocking 項目失敗
        blocking_failed = any(
            c.status == "failed" and c.blocking
            for c in self.checks
        )

        return not blocking_failed

    def _check_tfda_license(self):
        """檢查 TFDA 許可證"""
        check = self._get_check("tfda_license")

        taiwan_reg = self.evidence_pack.get("local_regulatory", {})
        if taiwan_reg.get("license_numbers"):
            check.status = "passed"
            check.message = f"找到 {len(taiwan_reg['license_numbers'])} 個許可證"
        elif taiwan_reg.get("market_status") == "已上市":
            check.status = "failed"
            check.message = "已上市但無許可證號"
        else:
            check.status = "skipped"
            check.message = "未上市藥品"

    def _check_tfda_label(self):
        """檢查 TFDA 仿單"""
        check = self._get_check("tfda_label")

        safety = self.evidence_pack.get("safety_profile", {})

        has_contraindications = safety.get("contraindications") not in [None, [], "[未檢索]", "[Data Gap]"]
        has_warnings = safety.get("warnings") not in [None, [], "[未檢索]", "[Data Gap]"]

        if has_contraindications and has_warnings:
            check.status = "passed"
            check.message = "禁忌症和警語已解析"
        elif has_contraindications or has_warnings:
            check.status = "failed"
            check.message = "仿單解析不完整"
        else:
            check.status = "failed"
            check.message = "仿單未取得或未解析"

    def _check_ddi_database(self):
        """檢查 DDI 資料庫"""
        check = self._get_check("ddi_database")

        safety = self.evidence_pack.get("safety_profile", {})
        ddi = safety.get("drug_interactions", {})

        if isinstance(ddi, dict) and ddi.get("interactions"):
            check.status = "passed"
            check.message = f"找到 {len(ddi['interactions'])} 筆 DDI"
        elif isinstance(ddi, dict) and ddi.get("query_status") == "completed":
            check.status = "passed"
            check.message = "已查詢，無相關 DDI"
        else:
            check.status = "failed"
            check.message = "DDI 資料庫未查詢"

    def _check_clinicaltrials(self):
        """檢查 ClinicalTrials.gov"""
        check = self._get_check("clinicaltrials")

        indications = self.evidence_pack.get("indications", [])
        total_trials = sum(
            len(ind.get("clinical_trials", []))
            for ind in indications
        )

        if total_trials > 0:
            check.status = "passed"
            check.message = f"找到 {total_trials} 項臨床試驗"
        else:
            check.status = "passed"
            check.message = "已查詢，無相關試驗"

    def _check_pubmed(self):
        """檢查 PubMed"""
        check = self._get_check("pubmed")

        indications = self.evidence_pack.get("indications", [])
        total_papers = sum(
            len(ind.get("literature", []))
            for ind in indications
        )

        if total_papers > 0:
            check.status = "passed"
            check.message = f"找到 {total_papers} 篇文獻"
        else:
            check.status = "passed"
            check.message = "已查詢，無相關文獻"

    def _check_drugbank_moa(self):
        """檢查 DrugBank MOA"""
        check = self._get_check("drugbank_moa")

        drug_info = self.evidence_pack.get("drug_info", {})
        moa = drug_info.get("mechanism_of_action", "")

        if moa and moa not in ["[Data Gap]", "[未檢索]", ""]:
            check.status = "passed"
            check.message = "MOA 已取得"
        else:
            check.status = "failed"
            check.message = "MOA 未取得"

    def _check_drug_basic_info(self):
        """檢查藥物基本資訊"""
        check = self._get_check("drug_basic_info")

        drug_info = self.evidence_pack.get("drug_info", {})
        required_fields = ["name", "drugbank_id"]

        missing = [f for f in required_fields if not drug_info.get(f)]

        if not missing:
            check.status = "passed"
            check.message = "基本資訊完整"
        else:
            check.status = "failed"
            check.message = f"缺少欄位: {missing}"

    def _check_indication_icd10(self):
        """檢查適應症 ICD-10"""
        check = self._get_check("indication_icd10")

        indications = self.evidence_pack.get("indications", [])
        missing_icd = []

        for ind in indications:
            if not ind.get("icd10_code"):
                missing_icd.append(ind.get("disease_name", "未知"))

        if not missing_icd:
            check.status = "passed"
            check.message = "所有適應症都有 ICD-10"
        else:
            check.status = "failed"
            check.message = f"{len(missing_icd)} 個適應症缺少 ICD-10"

    def _check_indication_evidence_level(self):
        """檢查適應症證據等級"""
        check = self._get_check("indication_evidence_level")

        indications = self.evidence_pack.get("indications", [])
        missing_level = []

        for ind in indications:
            if not ind.get("evidence_level"):
                missing_level.append(ind.get("disease_name", "未知"))

        if not missing_level:
            check.status = "passed"
            check.message = "所有適應症都有證據等級"
        else:
            check.status = "failed"
            check.message = f"{len(missing_level)} 個適應症缺少證據等級"

    def _check_data_gap_unlock(self):
        """檢查 Data Gap 解鎖條件"""
        check = self._get_check("data_gap_unlock")

        data_gaps = self.evidence_pack.get("data_gaps", [])
        missing_unlock = []

        for gap in data_gaps:
            if gap.get("blocking") and not gap.get("unlock_condition"):
                missing_unlock.append(gap.get("name", "未知"))

        if not missing_unlock:
            check.status = "passed"
            check.message = "所有 Blocking Gap 都有解鎖條件"
        else:
            check.status = "failed"
            check.message = f"{len(missing_unlock)} 個 Blocking Gap 缺少解鎖條件"

    def _get_check(self, name: str) -> CheckItem:
        """取得指定的檢查項目"""
        for check in self.checks:
            if check.name == name:
                return check
        raise ValueError(f"Unknown check: {name}")

    def get_report(self) -> str:
        """產生檢查報告"""
        lines = [
            "# Pre-flight 檢查報告",
            "",
            "## 資料來源查核",
            "",
        ]

        # 資料來源
        source_checks = [
            "tfda_license", "tfda_label", "ddi_database",
            "clinicaltrials", "pubmed", "drugbank_moa"
        ]

        for name in source_checks:
            check = self._get_check(name)
            status_icon = {
                "passed": "✅",
                "failed": "❌",
                "skipped": "⏭️",
                "unchecked": "⬜",
            }.get(check.status, "⬜")

            blocking_mark = "🛑" if check.blocking else ""
            lines.append(f"- [{status_icon}] {check.description} {blocking_mark}")
            if check.message:
                lines.append(f"  - {check.message}")

        lines.extend([
            "",
            "## 必要欄位檢核",
            "",
        ])

        # 必要欄位
        field_checks = [
            "drug_basic_info", "indication_icd10",
            "indication_evidence_level", "data_gap_unlock"
        ]

        for name in field_checks:
            check = self._get_check(name)
            status_icon = {
                "passed": "✅",
                "failed": "❌",
                "skipped": "⏭️",
                "unchecked": "⬜",
            }.get(check.status, "⬜")

            blocking_mark = "🛑" if check.blocking else ""
            lines.append(f"- [{status_icon}] {check.description} {blocking_mark}")
            if check.message:
                lines.append(f"  - {check.message}")

        lines.extend([
            "",
            "## 總結",
            "",
        ])

        passed = sum(1 for c in self.checks if c.status == "passed")
        failed = sum(1 for c in self.checks if c.status == "failed")
        blocking_failed = sum(1 for c in self.checks if c.status == "failed" and c.blocking)

        lines.append(f"- 通過: {passed}/{len(self.checks)}")
        lines.append(f"- 失敗: {failed}/{len(self.checks)}")

        if blocking_failed > 0:
            lines.append(f"- **阻斷性失敗: {blocking_failed}** 🛑")
            lines.append("")
            lines.append("⚠️ 存在阻斷性檢查失敗，建議先補齊資料再產生報告。")
        else:
            lines.append("")
            lines.append("✅ 無阻斷性檢查失敗，可以產生報告。")

        return "\n".join(lines)


def main():
    """主函數"""
    if len(sys.argv) < 2:
        print("用法: python preflight_check.py <evidence_pack.json>")
        sys.exit(1)

    evidence_path = Path(sys.argv[1])

    if not evidence_path.exists():
        print(f"錯誤: 找不到檔案 {evidence_path}")
        sys.exit(1)

    # 支援 JSON 和 Markdown 格式
    if evidence_path.suffix == ".json":
        evidence_pack = json.loads(evidence_path.read_text(encoding="utf-8"))
    else:
        # 簡化處理：從 Markdown 提取資訊（需要更完整的解析）
        print("警告: Markdown 格式支援有限，建議使用 JSON 格式")
        evidence_pack = {}

    checker = PreflightChecker(evidence_pack)
    can_proceed = checker.run_all_checks()

    print(checker.get_report())

    sys.exit(0 if can_proceed else 1)


if __name__ == "__main__":
    main()
