#!/usr/bin/env python3
"""Run the complete validation pipeline for a drug-disease candidate."""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from twtxgnn.collectors import (
    BundleAggregator,
    CandidateInfo,
    ClinicalTrialsCollector,
    ICTRPCollector,
    KnownRelationsChecker,
    UnifiedDDICollector,
    PubMedCollector,
    TFDACollector,
)
from twtxgnn.reviewer import EvidencePackGenerator
from twtxgnn.writer import PharmacistNotesWriter, SponsorNotesWriter
from twtxgnn.paths import get_evidence_packs_dir, get_notes_dir, slugify


def run_pipeline(
    drug: str,
    disease: str,
    drugbank_id: str | None = None,
    txgnn_score: float | None = None,
    skip_collection: bool = False,
    skip_evidence_pack: bool = False,
    skip_known: bool = False,
) -> dict[str, Path] | None:
    """Run the complete validation pipeline.

    Args:
        drug: Drug name (INN)
        disease: Disease/indication name
        drugbank_id: Optional DrugBank ID
        txgnn_score: Optional TxGNN score
        skip_collection: Skip data collection (use existing bundle)
        skip_evidence_pack: Skip evidence pack generation (use existing)
        skip_known: Skip candidates that are known indications/contraindications

    Returns:
        Dict with paths to all generated files, or None if skipped
    """
    results = {}

    # Create candidate info
    candidate = CandidateInfo(
        inn=drug,
        drugbank_id=drugbank_id,
        indication_raw=disease,
        txgnn_score=txgnn_score,
    )

    # Check known relations first
    checker = KnownRelationsChecker()
    kg_status = checker.check(drug, disease)

    drug_slug = slugify(drug)
    disease_slug = slugify(disease)
    candidate_dir = f"{drug_slug}_{disease_slug}"

    print("=" * 60)
    print(f"TxGNN Validation Pipeline")
    print("=" * 60)
    print(f"Drug: {drug}")
    print(f"Disease: {disease}")
    print(f"DrugBank ID: {drugbank_id or 'N/A'}")
    print(f"TxGNN Score: {txgnn_score or 'N/A'}")
    print("-" * 60)
    print(f"Knowledge Graph Status:")
    if kg_status["is_novel"]:
        print(f"  ✓ Novel prediction (not in KG)")
    else:
        print(f"  ✗ Known relation: {kg_status['relation_type']}")
        print(f"    {kg_status['reason']}")
    print("=" * 60)

    # Skip if known and skip_known is True
    if skip_known and not kg_status["is_novel"]:
        print(f"\n⚠ Skipping: This is a known {kg_status['relation_type']} in the knowledge graph.")
        return None

    # Update candidate with KG status
    candidate.is_novel = kg_status["is_novel"]
    candidate.kg_relation_type = kg_status["relation_type"]
    candidate.kg_relation_note = kg_status["reason"]

    # Step 1: Data Collection
    if not skip_collection:
        print("\n[Step 1] Collecting data...")

        aggregator = BundleAggregator()

        # Register all collectors
        aggregator.register_collector('unified_ddi', UnifiedDDICollector())
        aggregator.register_collector('clinicaltrials', ClinicalTrialsCollector())
        aggregator.register_collector('pubmed', PubMedCollector())
        aggregator.register_collector('tfda', TFDACollector())
        aggregator.register_collector('ictrp', ICTRPCollector())

        bundle = aggregator.collect(candidate)

        # Report collected data
        print(f"  - DDI entries: {len(bundle.safety.get('ddi', []))}")
        print(f"  - Clinical trials: {len(bundle.trials.get('clinicaltrials_gov', []))}")
        print(f"  - ICTRP trials: {len(bundle.trials.get('who_ictrp', []))}")
        print(f"  - PubMed articles: {len(bundle.pubmed.get('results', []))}")
        print(f"  - TFDA found: {bundle.tfda.get('found', False)}")
        if bundle.tfda.get('found'):
            print(f"    - TFDA records: {len(bundle.tfda.get('records', []))}")
        print(f"  - Bundle saved: {bundle.metadata.get('bundle_path')}")
        results['bundle'] = Path(bundle.metadata.get('bundle_path'))
    else:
        print("\n[Step 1] Skipping data collection (using existing bundle)")
        from twtxgnn.collectors import EvidenceBundle
        from twtxgnn.paths import get_bundles_dir
        bundle_path = get_bundles_dir() / candidate_dir / "bundle.json"
        bundle = EvidenceBundle.load(bundle_path)
        results['bundle'] = bundle_path

    # Step 2: Evidence Pack Generation
    evidence_pack_dir = get_evidence_packs_dir() / candidate_dir
    evidence_pack_json = evidence_pack_dir / "evidence_pack.json"
    evidence_pack_md = evidence_pack_dir / "evidence_pack.md"

    if not skip_evidence_pack:
        print("\n[Step 2] Generating Evidence Pack (calling LLM)...")

        generator = EvidencePackGenerator()
        json_path, md_path = generator.generate_and_save(
            bundle=bundle,
            output_dir=evidence_pack_dir,
        )

        print(f"  - JSON: {json_path}")
        print(f"  - Markdown: {md_path}")
        results['evidence_pack_json'] = json_path
        results['evidence_pack_md'] = md_path
    else:
        print("\n[Step 2] Skipping Evidence Pack generation (using existing)")
        results['evidence_pack_json'] = evidence_pack_json
        results['evidence_pack_md'] = evidence_pack_md

    # Step 3: Notes Generation
    print("\n[Step 3] Generating Notes (calling LLM)...")

    notes_dir = get_notes_dir() / candidate_dir
    notes_dir.mkdir(parents=True, exist_ok=True)

    # Load evidence pack for notes generation
    import json
    with open(results['evidence_pack_json'], 'r', encoding='utf-8') as f:
        evidence_pack = json.load(f)

    # Generate Pharmacist Notes
    print("  - Generating Pharmacist Notes...")
    pharmacist_writer = PharmacistNotesWriter()
    pharmacist_path = notes_dir / "pharmacist_notes.md"
    pharmacist_writer.generate_and_save(evidence_pack, pharmacist_path)
    print(f"    Saved: {pharmacist_path}")
    results['pharmacist_notes'] = pharmacist_path

    # Generate Sponsor Notes
    print("  - Generating Sponsor Notes...")
    sponsor_writer = SponsorNotesWriter()
    sponsor_path = notes_dir / "sponsor_notes.md"
    sponsor_writer.generate_and_save(evidence_pack, sponsor_path)
    print(f"    Saved: {sponsor_path}")
    results['sponsor_notes'] = sponsor_path

    print("\n" + "=" * 60)
    print("Pipeline completed!")
    print("=" * 60)
    print("\nGenerated files:")
    for name, path in results.items():
        print(f"  - {name}: {path}")

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Run the TxGNN validation pipeline for a drug-disease candidate"
    )
    parser.add_argument("--drug", required=True, help="Drug name (INN)")
    parser.add_argument("--disease", required=True, help="Disease/indication name")
    parser.add_argument("--drugbank-id", help="DrugBank ID")
    parser.add_argument("--txgnn-score", type=float, help="TxGNN prediction score")
    parser.add_argument("--skip-collection", action="store_true",
                       help="Skip data collection, use existing bundle")
    parser.add_argument("--skip-evidence-pack", action="store_true",
                       help="Skip evidence pack generation, use existing")
    parser.add_argument("--skip-known", action="store_true",
                       help="Skip known indications/contraindications in KG")

    args = parser.parse_args()

    run_pipeline(
        drug=args.drug,
        disease=args.disease,
        drugbank_id=args.drugbank_id,
        txgnn_score=args.txgnn_score,
        skip_collection=args.skip_collection,
        skip_evidence_pack=args.skip_evidence_pack,
        skip_known=args.skip_known,
    )


if __name__ == "__main__":
    main()
