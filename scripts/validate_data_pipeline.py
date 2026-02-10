#!/usr/bin/env python3
"""Validation pipeline for TwTxGNN drug repurposing workflow.

This script validates data integrity across the pipeline:
1. DrugBundle -> Evidence Pack: Ensures 100% data fidelity
2. Evidence Pack -> Notes: Ensures status markers are correct

Usage:
    # Validate single drug
    uv run python scripts/validate_data_pipeline.py --drug minoxidil

    # Validate all drugs
    uv run python scripts/validate_data_pipeline.py --all

    # Validate specific stage
    uv run python scripts/validate_data_pipeline.py --drug aspirin --stage bundle-to-ep
"""

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ValidationResult:
    """Result of a validation check."""

    stage: str
    drug: str
    passed: bool
    errors: list[str]
    warnings: list[str]


def get_data_dir() -> Path:
    """Get the data directory."""
    return Path(__file__).parent.parent / "data"


def validate_bundle_to_evidence_pack(drug_name: str) -> ValidationResult:
    """Validate that Evidence Pack correctly reflects Bundle data.

    Checks:
    - Indication count matches
    - Clinical trial count per indication matches
    - Literature count per indication matches
    - query_log has entries for collection_log items

    Args:
        drug_name: Name of the drug to validate

    Returns:
        ValidationResult with findings
    """
    errors = []
    warnings = []
    data_dir = get_data_dir()

    # Load bundle
    bundle_path = data_dir / "bundles" / drug_name / "drug_bundle.json"
    if not bundle_path.exists():
        return ValidationResult(
            stage="bundle-to-ep",
            drug=drug_name,
            passed=False,
            errors=[f"Bundle not found: {bundle_path}"],
            warnings=[],
        )

    with open(bundle_path) as f:
        bundle = json.load(f)

    # Load evidence pack
    ep_dir = data_dir / "evidence_packs" / drug_name
    ep_files = list(ep_dir.glob("*_drug_evidence_pack.json"))
    if not ep_files:
        return ValidationResult(
            stage="bundle-to-ep",
            drug=drug_name,
            passed=False,
            errors=[f"Evidence Pack not found in: {ep_dir}"],
            warnings=[],
        )

    ep_path = ep_files[0]
    with open(ep_path) as f:
        ep = json.load(f)

    # Check indication count
    bundle_indications = bundle.get("drug", {}).get("predicted_indications", [])
    ep_indications = ep.get("predicted_indications", [])

    if len(bundle_indications) != len(ep_indications):
        errors.append(
            f"Indication count mismatch: Bundle={len(bundle_indications)}, EP={len(ep_indications)}"
        )

    # Check each indication's evidence count
    for i, (b_ind, e_ind) in enumerate(zip(bundle_indications, ep_indications)):
        disease = b_ind.get("disease_name", f"indication_{i}")

        # Clinical trials
        b_trials = [
            t for t in b_ind.get("clinical_trials", [])
            if isinstance(t, dict) and not t.get("error")
        ]
        e_trials = e_ind.get("evidence", {}).get("clinical_trials", [])

        if len(b_trials) != len(e_trials):
            errors.append(
                f"{disease}: trial count mismatch (Bundle={len(b_trials)}, EP={len(e_trials)})"
            )

        # Literature
        b_lit = [
            a for a in b_ind.get("pubmed_articles", [])
            if isinstance(a, dict) and not a.get("error")
        ]
        e_lit = e_ind.get("evidence", {}).get("literature", [])

        if len(b_lit) != len(e_lit):
            errors.append(
                f"{disease}: literature count mismatch (Bundle={len(b_lit)}, EP={len(e_lit)})"
            )

    # Check query_log
    collection_log = bundle.get("collection_log", [])
    query_log = ep.get("query_log", [])

    if collection_log and not query_log:
        errors.append("query_log is empty but collection_log has entries")

    if len(collection_log) != len(query_log):
        warnings.append(
            f"Log count mismatch: collection_log={len(collection_log)}, query_log={len(query_log)}"
        )

    return ValidationResult(
        stage="bundle-to-ep",
        drug=drug_name,
        passed=len(errors) == 0,
        errors=errors,
        warnings=warnings,
    )


def validate_evidence_pack_status(drug_name: str) -> ValidationResult:
    """Validate that Evidence Pack query_log has correct status values.

    Checks:
    - Each query_log entry has result_status
    - result_status is one of: success, error, not_found
    - result_count is present for success status

    Args:
        drug_name: Name of the drug to validate

    Returns:
        ValidationResult with findings
    """
    errors = []
    warnings = []
    data_dir = get_data_dir()

    # Load evidence pack
    ep_dir = data_dir / "evidence_packs" / drug_name
    ep_files = list(ep_dir.glob("*_drug_evidence_pack.json"))
    if not ep_files:
        return ValidationResult(
            stage="ep-status",
            drug=drug_name,
            passed=False,
            errors=[f"Evidence Pack not found in: {ep_dir}"],
            warnings=[],
        )

    ep_path = ep_files[0]
    with open(ep_path) as f:
        ep = json.load(f)

    query_log = ep.get("query_log", [])

    if not query_log:
        warnings.append("query_log is empty")

    valid_statuses = {"success", "error", "not_found"}

    for entry in query_log:
        source = entry.get("source", "unknown")
        status = entry.get("result_status")

        if not status:
            errors.append(f"{source}: missing result_status")
            continue

        if status not in valid_statuses:
            errors.append(f"{source}: invalid status '{status}' (expected: {valid_statuses})")

        if status == "success" and "result_count" not in entry:
            warnings.append(f"{source}: success status but no result_count")

    return ValidationResult(
        stage="ep-status",
        drug=drug_name,
        passed=len(errors) == 0,
        errors=errors,
        warnings=warnings,
    )


def validate_notes_exist(drug_name: str) -> ValidationResult:
    """Validate that Notes files exist and are non-empty.

    Args:
        drug_name: Name of the drug to validate

    Returns:
        ValidationResult with findings
    """
    errors = []
    warnings = []
    data_dir = get_data_dir()

    notes_dir = data_dir / "notes" / drug_name

    if not notes_dir.exists():
        return ValidationResult(
            stage="notes-exist",
            drug=drug_name,
            passed=False,
            errors=[f"Notes directory not found: {notes_dir}"],
            warnings=[],
        )

    pharmacist_notes = notes_dir / "drug_pharmacist_notes.md"
    sponsor_notes = notes_dir / "drug_sponsor_notes.md"

    for notes_path, name in [
        (pharmacist_notes, "Pharmacist Notes"),
        (sponsor_notes, "Sponsor Notes"),
    ]:
        if not notes_path.exists():
            errors.append(f"{name} not found: {notes_path}")
        elif notes_path.stat().st_size < 100:
            errors.append(f"{name} is too small ({notes_path.stat().st_size} bytes)")
        elif notes_path.stat().st_size < 1000:
            warnings.append(f"{name} is unusually small ({notes_path.stat().st_size} bytes)")

    return ValidationResult(
        stage="notes-exist",
        drug=drug_name,
        passed=len(errors) == 0,
        errors=errors,
        warnings=warnings,
    )


def validate_drug(drug_name: str, stages: list[str] | None = None) -> list[ValidationResult]:
    """Run all validation checks for a single drug.

    Args:
        drug_name: Name of the drug to validate
        stages: Optional list of stages to validate. If None, validates all stages.

    Returns:
        List of ValidationResults
    """
    all_stages = {
        "bundle-to-ep": validate_bundle_to_evidence_pack,
        "ep-status": validate_evidence_pack_status,
        "notes-exist": validate_notes_exist,
    }

    if stages is None:
        stages = list(all_stages.keys())

    results = []
    for stage in stages:
        if stage in all_stages:
            result = all_stages[stage](drug_name)
            results.append(result)

    return results


def validate_all_drugs(stages: list[str] | None = None) -> dict[str, list[ValidationResult]]:
    """Validate all drugs in the data directory.

    Args:
        stages: Optional list of stages to validate

    Returns:
        Dict mapping drug name to list of ValidationResults
    """
    data_dir = get_data_dir()
    results = {}

    # Find all drugs (from bundles, evidence_packs, or notes)
    drugs = set()

    bundles_dir = data_dir / "bundles"
    if bundles_dir.exists():
        for d in bundles_dir.iterdir():
            if d.is_dir():
                drugs.add(d.name)

    ep_dir = data_dir / "evidence_packs"
    if ep_dir.exists():
        for d in ep_dir.iterdir():
            if d.is_dir():
                drugs.add(d.name)

    notes_dir = data_dir / "notes"
    if notes_dir.exists():
        for d in notes_dir.iterdir():
            if d.is_dir():
                drugs.add(d.name)

    for drug in sorted(drugs):
        results[drug] = validate_drug(drug, stages)

    return results


def print_result(result: ValidationResult, verbose: bool = False) -> None:
    """Print a validation result."""
    status = "✅ PASS" if result.passed else "❌ FAIL"
    print(f"  [{result.stage}] {status}")

    if result.errors:
        for error in result.errors:
            print(f"    ❌ {error}")

    if verbose and result.warnings:
        for warning in result.warnings:
            print(f"    ⚠️  {warning}")


def main():
    parser = argparse.ArgumentParser(
        description="Validate TwTxGNN data pipeline integrity"
    )
    parser.add_argument(
        "--drug",
        type=str,
        help="Drug name to validate",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Validate all drugs",
    )
    parser.add_argument(
        "--stage",
        type=str,
        choices=["bundle-to-ep", "ep-status", "notes-exist"],
        help="Validate specific stage only",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show warnings in addition to errors",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Show summary only",
    )

    args = parser.parse_args()

    if not args.drug and not args.all:
        parser.error("Please specify --drug or --all")

    stages = [args.stage] if args.stage else None

    if args.drug:
        print(f"\n{'=' * 60}")
        print(f"Validating: {args.drug}")
        print(f"{'=' * 60}")

        results = validate_drug(args.drug, stages)

        all_passed = True
        for result in results:
            print_result(result, args.verbose)
            if not result.passed:
                all_passed = False

        sys.exit(0 if all_passed else 1)

    elif args.all:
        print(f"\n{'=' * 60}")
        print("Validating all drugs")
        print(f"{'=' * 60}")

        all_results = validate_all_drugs(stages)

        total_passed = 0
        total_failed = 0
        failed_drugs = []

        for drug, results in all_results.items():
            drug_passed = all(r.passed for r in results)

            if args.summary:
                status = "✅" if drug_passed else "❌"
                print(f"  {status} {drug}")
            else:
                print(f"\n{drug}:")
                for result in results:
                    print_result(result, args.verbose)

            if drug_passed:
                total_passed += 1
            else:
                total_failed += 1
                failed_drugs.append(drug)

        print(f"\n{'=' * 60}")
        print(f"Summary: {total_passed} passed, {total_failed} failed")

        if failed_drugs:
            print(f"\nFailed drugs: {', '.join(failed_drugs)}")

        sys.exit(0 if total_failed == 0 else 1)


if __name__ == "__main__":
    main()
