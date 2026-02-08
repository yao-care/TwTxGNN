#!/usr/bin/env python3
"""Demo script for DDInter collector usage."""

from twtxgnn.collectors import DDInterCollector


def main():
    """Demonstrate DDInter collector functionality."""
    print("=== DDInter Collector Demo ===\n")

    # Initialize collector
    collector = DDInterCollector()
    print(f"Data directory: {collector.data_dir}\n")

    # Example 1: Search for a drug
    drug = "Dolutegravir"
    print(f"Example 1: Searching for '{drug}'")
    result = collector.search(drug)

    if result.success and result.data:
        print(f"Found {len(result.data)} interactions for {drug}:")
        for interaction in result.data[:5]:  # Show first 5
            print(
                f"  - {interaction['interacting_drug']}: "
                f"{interaction['level']} severity"
            )
        if len(result.data) > 5:
            print(f"  ... and {len(result.data) - 5} more interactions")
    else:
        print(f"No interactions found for {drug}")
    print()

    # Example 2: Case-insensitive search
    drug_lower = "naltrexone"
    print(f"Example 2: Case-insensitive search for '{drug_lower}'")
    result = collector.search(drug_lower)
    print(f"Found {len(result.data)} interactions\n")

    # Example 3: Get severe interactions only
    print(f"Example 3: Major interactions for '{drug}'")
    severe = collector.get_severe_interactions(drug, min_level="Major")
    print(f"Found {len(severe)} major interactions:")
    for interaction in severe[:5]:
        print(f"  - {interaction['interacting_drug']}")
    if len(severe) > 5:
        print(f"  ... and {len(severe) - 5} more")
    print()

    # Example 4: Get interaction statistics
    print("Example 4: Interaction statistics")
    drugs_to_check = ["Dolutegravir", "Naltrexone", "Abacavir"]
    for drug in drugs_to_check:
        count = collector.get_interaction_count(drug)
        severe = len(collector.get_severe_interactions(drug, min_level="Major"))
        print(f"{drug}: {count} total interactions ({severe} major)")
    print()

    # Example 5: Available drugs
    print("Example 5: Number of drugs in database")
    available = collector.get_available_drugs()
    print(f"Total drugs with DDI data: {len(available)}")
    print(f"Sample drugs: {', '.join(available[:10])}")
    print()

    # Example 6: Result structure
    print("Example 6: Result structure")
    result = collector.search("Naltrexone")
    print(f"Source: {result.source}")
    print(f"Query: {result.query}")
    print(f"Success: {result.success}")
    print(f"Timestamp: {result.timestamp}")
    print(f"Data type: {type(result.data)}")
    if result.data:
        print(f"First interaction structure: {result.data[0]}")


if __name__ == "__main__":
    main()
