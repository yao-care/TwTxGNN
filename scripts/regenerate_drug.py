#!/usr/bin/env python3
"""Regenerate Bundle, Evidence Pack, and Notes for a single drug.

This script tests the complete v4 pipeline:
1. Collect DrugBundle with CollectionStatus tracking
2. Generate Evidence Pack with v4 architecture (100% data fidelity)
3. Generate Notes using the new query_log interpretation

Usage:
    uv run python scripts/regenerate_drug.py minoxidil
    uv run python scripts/regenerate_drug.py --drug minoxidil --top-n 5
"""

import argparse
import json
import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def regenerate_drug(
    drug_name: str,
    top_n: int = 5,
    min_score: float = 0.99,
    skip_bundle: bool = False,
    skip_ep: bool = False,
    skip_notes: bool = False,
) -> dict:
    """Regenerate all outputs for a single drug.

    Args:
        drug_name: Name of the drug
        top_n: Number of top indications to include
        min_score: Minimum TxGNN score threshold
        skip_bundle: Skip bundle collection
        skip_ep: Skip Evidence Pack generation
        skip_notes: Skip Notes generation

    Returns:
        Dict with results and validation status
    """
    from twtxgnn.collectors import DrugBundleAggregator
    from twtxgnn.reviewer import DrugEvidencePackGenerator
    from twtxgnn.writer import DrugPharmacistNotesWriter, DrugSponsorNotesWriter

    data_dir = Path(__file__).parent.parent / "data"
    results = {
        "drug": drug_name,
        "bundle": None,
        "evidence_pack": None,
        "notes": None,
        "validation": None,
    }

    # Step 1: Collect Bundle
    if not skip_bundle:
        print(f"\n{'='*60}")
        print(f"Step 1: Collecting DrugBundle for {drug_name}")
        print(f"{'='*60}")

        aggregator = DrugBundleAggregator(save_collected=True)
        bundle = aggregator.collect(
            drug_name=drug_name,
            top_n=top_n,
            min_score=min_score,
        )

        # Save the bundle
        bundle_path = bundle.save()

        print(f"\n  Bundle saved: {bundle_path}")
        print(f"  Collection log entries: {len(bundle.collection_log)}")
        print(f"  Predicted indications: {len(bundle.drug.predicted_indications)}")

        # Show collection log summary
        print("\n  Collection Log:")
        for cs in bundle.collection_log:
            status_icon = "✅" if cs.status == "success" else "❌"
            print(f"    {status_icon} {cs.source}: {cs.status} ({cs.result_count} results)")

        results["bundle"] = {
            "path": str(bundle_path),
            "collection_log_count": len(bundle.collection_log),
            "indication_count": len(bundle.drug.predicted_indications),
        }
    else:
        # Load existing bundle
        bundle_path = data_dir / "bundles" / drug_name / "drug_bundle.json"
        if not bundle_path.exists():
            raise FileNotFoundError(f"Bundle not found: {bundle_path}")

        # Use DrugBundle.load() method
        from twtxgnn.collectors.drug_bundle import DrugBundle

        bundle = DrugBundle.load(bundle_path)
        print(f"\n  Loaded existing bundle: {bundle_path}")
        print(f"  Collection log entries: {len(bundle.collection_log)}")

    # Step 2: Generate Evidence Pack
    if not skip_ep:
        print(f"\n{'='*60}")
        print(f"Step 2: Generating Evidence Pack for {drug_name}")
        print(f"{'='*60}")

        # Check for API key
        if not os.environ.get("OPENAI_API_KEY"):
            print("  ⚠️  OPENAI_API_KEY not set, skipping Evidence Pack generation")
            results["evidence_pack"] = {"skipped": "No API key"}
        else:
            ep_generator = DrugEvidencePackGenerator()
            ep_dir = data_dir / "evidence_packs" / drug_name

            try:
                json_path, md_path = ep_generator.generate_and_save(
                    bundle=bundle,
                    output_dir=ep_dir,
                    validate=True,
                )

                print(f"\n  Evidence Pack saved:")
                print(f"    - JSON: {json_path}")
                print(f"    - MD: {md_path}")

                # Load and show summary
                with open(json_path) as f:
                    ep = json.load(f)

                print(f"\n  query_log entries: {len(ep.get('query_log', []))}")
                print(f"  predicted_indications: {len(ep.get('predicted_indications', []))}")

                results["evidence_pack"] = {
                    "json_path": str(json_path),
                    "md_path": str(md_path),
                    "query_log_count": len(ep.get("query_log", [])),
                    "indication_count": len(ep.get("predicted_indications", [])),
                }

            except Exception as e:
                print(f"\n  ❌ Error generating Evidence Pack: {e}")
                results["evidence_pack"] = {"error": str(e)}
    else:
        print("\n  Skipping Evidence Pack generation")

    # Step 3: Generate Notes
    if not skip_notes:
        print(f"\n{'='*60}")
        print(f"Step 3: Generating Notes for {drug_name}")
        print(f"{'='*60}")

        # Check for API key
        if not os.environ.get("OPENAI_API_KEY"):
            print("  ⚠️  OPENAI_API_KEY not set, skipping Notes generation")
            results["notes"] = {"skipped": "No API key"}
        else:
            # Load Evidence Pack
            ep_dir = data_dir / "evidence_packs" / drug_name
            ep_files = list(ep_dir.glob("*_drug_evidence_pack.json"))

            if not ep_files:
                print(f"  ⚠️  Evidence Pack not found, skipping Notes generation")
                results["notes"] = {"skipped": "No Evidence Pack"}
            else:
                ep_path = ep_files[0]
                with open(ep_path) as f:
                    ep_data = json.load(f)

                notes_dir = data_dir / "notes" / drug_name

                try:
                    # Generate Pharmacist Notes
                    print("\n  Generating Pharmacist Notes...")
                    pharmacist_writer = DrugPharmacistNotesWriter()
                    pharmacist_path = notes_dir / "drug_pharmacist_notes.md"
                    pharmacist_writer.generate_and_save(ep_data, pharmacist_path)
                    print(f"    ✅ {pharmacist_path}")

                    # Generate Sponsor Notes
                    print("\n  Generating Sponsor Notes...")
                    sponsor_writer = DrugSponsorNotesWriter()
                    sponsor_path = notes_dir / "drug_sponsor_notes.md"
                    sponsor_writer.generate_and_save(ep_data, sponsor_path)
                    print(f"    ✅ {sponsor_path}")

                    results["notes"] = {
                        "pharmacist": str(pharmacist_path),
                        "sponsor": str(sponsor_path),
                    }

                except Exception as e:
                    print(f"\n  ❌ Error generating Notes: {e}")
                    results["notes"] = {"error": str(e)}
    else:
        print("\n  Skipping Notes generation")

    # Step 4: Validate
    print(f"\n{'='*60}")
    print(f"Step 4: Validating outputs for {drug_name}")
    print(f"{'='*60}")

    # Import validate_drug from the same directory
    import importlib.util
    validate_script = Path(__file__).parent / "validate_data_pipeline.py"
    spec = importlib.util.spec_from_file_location("validate_data_pipeline", validate_script)
    validate_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(validate_module)

    validation_results = validate_module.validate_drug(drug_name)
    all_passed = all(r.passed for r in validation_results)

    for result in validation_results:
        status = "✅ PASS" if result.passed else "❌ FAIL"
        print(f"  [{result.stage}] {status}")
        for error in result.errors:
            print(f"    ❌ {error}")

    results["validation"] = {
        "all_passed": all_passed,
        "stages": [
            {
                "stage": r.stage,
                "passed": r.passed,
                "errors": r.errors,
            }
            for r in validation_results
        ],
    }

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Regenerate Bundle, Evidence Pack, and Notes for a drug"
    )
    parser.add_argument(
        "drug",
        nargs="?",
        help="Drug name to regenerate",
    )
    parser.add_argument(
        "--drug",
        dest="drug_alt",
        help="Drug name (alternative syntax)",
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=5,
        help="Number of top indications (default: 5)",
    )
    parser.add_argument(
        "--min-score",
        type=float,
        default=0.99,
        help="Minimum TxGNN score (default: 0.99)",
    )
    parser.add_argument(
        "--skip-bundle",
        action="store_true",
        help="Skip bundle collection (use existing)",
    )
    parser.add_argument(
        "--skip-ep",
        action="store_true",
        help="Skip Evidence Pack generation",
    )
    parser.add_argument(
        "--skip-notes",
        action="store_true",
        help="Skip Notes generation",
    )

    args = parser.parse_args()

    drug_name = args.drug or args.drug_alt
    if not drug_name:
        parser.error("Please specify a drug name")

    results = regenerate_drug(
        drug_name=drug_name,
        top_n=args.top_n,
        min_score=args.min_score,
        skip_bundle=args.skip_bundle,
        skip_ep=args.skip_ep,
        skip_notes=args.skip_notes,
    )

    print(f"\n{'='*60}")
    print("Summary")
    print(f"{'='*60}")
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
