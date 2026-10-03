"""TFDA collector - fetches Taiwan FDA drug data."""

import json
import re
from pathlib import Path
from typing import Any

from .base import BaseCollector, CollectorResult


class TFDACollector(BaseCollector):
    """Collector for Taiwan FDA (TFDA) drug data.

    Reads from local tw_fda_drugs.json file that was processed
    from the FDA open data.
    """

    source_name = "tfda"

    def __init__(self, data_path: str | Path | None = None):
        """Initialize the collector.

        Args:
            data_path: Path to tw_fda_drugs.json file.
                      Defaults to data/raw/tw_fda_drugs.json
        """
        if data_path is None:
            self.data_path = (
                Path(__file__).parent.parent.parent.parent
                / "data"
                / "raw"
                / "tw_fda_drugs.json"
            )
        else:
            self.data_path = Path(data_path)

        self._data: list[dict] | None = None

    def _load_data(self) -> list[dict]:
        """Load FDA data from JSON file."""
        if self._data is not None:
            return self._data

        if not self.data_path.exists():
            self._data = []
            return self._data

        with open(self.data_path, "r", encoding="utf-8") as f:
            self._data = json.load(f)

        return self._data

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        """Search for TFDA records matching a drug name.

        Args:
            drug: Drug name (INN or brand name, Chinese or English)
            disease: Disease/indication name (used for filtering if provided)

        Returns:
            CollectorResult with TFDA data
        """
        query = {"drug": drug, "disease": disease}

        try:
            data = self._load_data()

            # Search for matching records
            matches = self._find_matches(drug, data)

            # If disease is provided, further filter by indication
            if disease and matches:
                matches = self._filter_by_indication(matches, disease)

            # Format the result
            result = self._format_result(matches)

            return self._make_result(
                query=query,
                data=result,
                success=True,
            )

        except Exception as e:
            return self._make_result(
                query=query,
                data={"found": False, "records": []},
                success=False,
                error_message=str(e),
            )

    def _find_matches(self, drug: str, data: list[dict]) -> list[dict]:
        """Find records for a drug, one per license ID.

        2026-10-03 起：英文藥名走 twtxgnn.regulatory.tfda_licenses 的主成分比對（確定性、
        不再用全文子字串，避免把 penicillin G procaine 算成 procaine、把適應症裡提到藥名的
        別藥算進來）；中文查詢才比對中文品名。同一字號在資料集重複多列時只留一筆。
        """
        from ..regulatory.tfda_licenses import dedupe, licenses_for_drug

        by_id = dedupe(data)
        if re.search(r"[A-Za-z]", drug):
            return [by_id[x["id"]] for x in licenses_for_drug(drug, by_id)]
        return [r for r in by_id.values() if drug and drug in (r.get("中文品名") or "")]

    def _filter_by_indication(
        self, records: list[dict], disease: str
    ) -> list[dict]:
        """Filter records by indication/disease.

        Args:
            records: List of FDA records
            disease: Disease/indication to filter by

        Returns:
            Filtered list of records
        """
        disease_lower = disease.lower()
        filtered = []

        for record in records:
            indication = record.get("適應症", "").lower()
            if disease_lower in indication:
                filtered.append(record)

        # If no matches with indication filter, return original
        return filtered if filtered else records

    def _format_result(self, records: list[dict]) -> dict:
        """Format the result for the bundle.

        Args:
            records: List of matching FDA records

        Returns:
            Formatted result dictionary
        """
        if not records:
            return {"found": False, "records": []}

        formatted_records = []
        # 2026-10-03：拿掉 records[:20] 上限，張數＝不重複字號數，並標示單方／複方／已註銷
        from ..regulatory.tfda_licenses import summarize, to_license

        for record in records:
            formatted = {
                "license_id": record.get("許可證字號", ""),
                "brand_name_zh": record.get("中文品名", ""),
                "brand_name_en": record.get("英文品名", ""),
                "ingredients": record.get("主成分略述", ""),
                "indication": record.get("適應症", ""),
                "dosage_form": record.get("劑型", ""),
                "manufacturer": record.get("製造廠名稱", ""),
                "license_holder": record.get("申請商名稱", ""),
                "approval_date": record.get("發證日期", ""),
                "expiry_date": record.get("有效日期", ""),
                "status": record.get("註銷狀態", ""),
            }
            lic = to_license(record) if record.get("許可證字號") else None
            if lic:
                formatted["kind"] = lic["kind"]
                formatted["license_status"] = lic["status"]
            formatted_records.append(formatted)
        summary = summarize([to_license(r) for r in records if r.get("許可證字號")])

        # Create package insert summary from first record
        first_record = records[0]
        package_insert = {
            "warnings": [],  # Would need additional data source
            "contraindications": [],
            "dosage": first_record.get("用法用量", ""),
            "special_populations": [],
        }

        return {
            "found": True,
            "records": formatted_records,
            "total_matches": len(records),
            "summary": summary,
            "package_insert": package_insert,
        }

    def get_by_license_id(self, license_id: str) -> dict | None:
        """Get a specific record by license ID.

        Args:
            license_id: Taiwan FDA license ID (e.g., "衛部藥製字第000001號")

        Returns:
            Record dictionary or None if not found
        """
        data = self._load_data()

        for record in data:
            if record.get("許可證字號") == license_id:
                return record

        return None
