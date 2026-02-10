#!/usr/bin/env python3
"""
報告輸出後完整驗證腳本。

驗證項目：
1. 禁止語句檢查
2. 必要章節檢查
3. Data Gap 格式檢查
4. 來源標註檢查
5. 一致性檢查
"""

import json
import re
import sys
from pathlib import Path
from typing import Any


class ReportValidator:
    """報告驗證器"""

    # 禁止語句（無來源時）
    FORBIDDEN_PHRASES = [
        "可能", "或許", "應該",
        "一般認為", "通常", "據了解",
        "建議參考",
    ]

    # 絕對禁止語句
    ABSOLUTE_FORBIDDEN = [
        "無特別",
        "無風險",
    ]

    # 必要章節
    REQUIRED_SECTIONS = [
        "資料完整性與可用性聲明",
        "阻斷性缺口摘要",
        "補件追蹤表",
    ]

    # 來源標記模式
    SOURCE_PATTERNS = [
        r"\[來源：.*?\]",
        r"\[Data Gap\]",
        r"\[未檢索\]",
        r"\[未找到\]",
        r"\[不適用\]",
    ]

    def __init__(self, content: str, doc_type: str = "Pharmacist"):
        self.content = content
        self.doc_type = doc_type
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def validate_all(self) -> bool:
        """執行所有驗證"""
        self._check_absolute_forbidden()
        self._check_forbidden_without_source()
        self._check_required_sections()
        self._check_data_gap_format()
        self._check_blocking_gaps_unlock()
        self._check_decision_conclusion()

        return len(self.errors) == 0

    def _check_absolute_forbidden(self):
        """檢查絕對禁止語句"""
        for phrase in self.ABSOLUTE_FORBIDDEN:
            if phrase in self.content:
                # 找出行號
                lines = self.content.split("\n")
                for i, line in enumerate(lines, 1):
                    if phrase in line:
                        self.errors.append(
                            f"第 {i} 行發現絕對禁止語句「{phrase}」"
                        )

    def _check_forbidden_without_source(self):
        """檢查無來源的禁止語句"""
        lines = self.content.split("\n")

        for i, line in enumerate(lines, 1):
            # 跳過模板行、程式碼區塊、表格標題
            if (line.strip().startswith("```") or
                line.strip().startswith("|--") or
                line.strip().startswith("| 欄位") or
                line.strip().startswith("❌") or
                line.strip().startswith("✅")):
                continue

            for phrase in self.FORBIDDEN_PHRASES:
                if phrase in line:
                    # 檢查是否有來源標記
                    has_source = any(
                        re.search(pattern, line)
                        for pattern in self.SOURCE_PATTERNS
                    )

                    if not has_source:
                        self.warnings.append(
                            f"第 {i} 行：「{phrase}」無來源標記"
                        )

    def _check_required_sections(self):
        """檢查必要章節"""
        for section in self.REQUIRED_SECTIONS:
            if section not in self.content:
                self.errors.append(f"缺少必要章節：{section}")

    def _check_data_gap_format(self):
        """檢查 Data Gap 格式"""
        # 匹配 Data Gap 區塊
        pattern = r"### Data Gap #(\d+) — (.+?)（(🛑 Blocking|⚠️ Non-blocking)）"
        matches = list(re.finditer(pattern, self.content))

        if not matches:
            # 檢查是否有 Data Gap 但格式不正確
            if "Data Gap" in self.content and "### Data Gap #" not in self.content:
                self.warnings.append("發現 Data Gap 但格式可能不正確")

        # 檢查 ID 連續性
        ids = [int(m.group(1)) for m in matches]
        if ids and ids != list(range(1, len(ids) + 1)):
            self.warnings.append(f"Data Gap ID 不連續: {ids}")

    def _check_blocking_gaps_unlock(self):
        """檢查 Blocking Gap 是否有解鎖條件"""
        # 找出所有 Blocking Gap
        pattern = r"### Data Gap #(\d+) — (.+?)（🛑 Blocking）"
        matches = re.finditer(pattern, self.content)

        for match in matches:
            gap_id = match.group(1)
            gap_name = match.group(2)

            # 檢查解鎖條件
            unlock_pattern = rf"Data Gap #{gap_id}.*?解鎖條件\s*\|\s*(.+?)\s*\|"
            unlock_match = re.search(unlock_pattern, self.content, re.DOTALL)

            if not unlock_match:
                self.errors.append(
                    f"Blocking Gap #{gap_id}「{gap_name}」缺少解鎖條件"
                )
            elif not unlock_match.group(1).strip() or unlock_match.group(1).strip() == "{需要哪種資料、補到哪個欄位後才可升級階段}":
                self.errors.append(
                    f"Blocking Gap #{gap_id}「{gap_name}」解鎖條件為空"
                )

    def _check_decision_conclusion(self):
        """檢查決策結論"""
        valid_decisions = [
            "決策結論：Hold",
            "決策結論：Research Question",
            "決策結論：Proceed with Guardrails",
        ]

        has_decision = any(d in self.content for d in valid_decisions)

        if not has_decision:
            self.errors.append("缺少有效的決策結論（Hold/Research Question/Guardrails）")

    def get_report(self) -> str:
        """產生驗證報告"""
        lines = [
            f"# {self.doc_type} Notes 驗證報告",
            "",
            "## 驗證結果",
            "",
        ]

        if self.errors:
            lines.append(f"❌ **錯誤**：{len(self.errors)} 個")
            lines.append("")
            for error in self.errors:
                lines.append(f"- {error}")
            lines.append("")
        else:
            lines.append("✅ **無錯誤**")
            lines.append("")

        if self.warnings:
            lines.append(f"⚠️ **警告**：{len(self.warnings)} 個")
            lines.append("")
            for warning in self.warnings[:20]:
                lines.append(f"- {warning}")
            if len(self.warnings) > 20:
                lines.append(f"- ... 還有 {len(self.warnings) - 20} 個警告")
            lines.append("")

        return "\n".join(lines)


def validate_evidence_pack_consistency(
    notes_content: str,
    evidence_pack: dict[str, Any]
) -> list[str]:
    """驗證 Notes 與 Evidence Pack 的一致性"""
    errors = []

    # 檢查藥物名稱
    drug_name = evidence_pack.get("drug_info", {}).get("name", "")
    if drug_name and drug_name not in notes_content:
        errors.append(f"藥物名稱「{drug_name}」未出現在 Notes 中")

    # 檢查適應症數量
    indications = evidence_pack.get("indications", [])
    for indication in indications[:5]:  # 檢查前 5 個
        disease = indication.get("disease_name", "")
        if disease and disease not in notes_content:
            errors.append(f"適應症「{disease}」未出現在 Notes 中")

    return errors


def main():
    """主函數"""
    if len(sys.argv) < 2:
        print("用法: python validate_report.py <report.md> [evidence_pack.json]")
        sys.exit(1)

    report_path = Path(sys.argv[1])

    if not report_path.exists():
        print(f"錯誤: 找不到檔案 {report_path}")
        sys.exit(1)

    content = report_path.read_text(encoding="utf-8")

    # 判斷文件類型
    doc_type = "Pharmacist" if "Pharmacist" in content else "Sponsor"

    # 驗證報告
    validator = ReportValidator(content, doc_type)
    is_valid = validator.validate_all()

    # 輸出結果
    print(validator.get_report())

    # 如果有 Evidence Pack，也驗證一致性
    if len(sys.argv) >= 3:
        evidence_path = Path(sys.argv[2])
        if evidence_path.exists():
            evidence_pack = json.loads(evidence_path.read_text(encoding="utf-8"))
            errors = validate_evidence_pack_consistency(content, evidence_pack)

            if errors:
                print("## Evidence Pack 一致性檢查")
                print("")
                for error in errors:
                    print(f"- {error}")
                print("")

    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
