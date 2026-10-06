"""
Assignment 3 Solution: Aspect Extraction & Canonical Ontology Mapping
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from code.core.aspect_extractor import AspectExtractor


def run_assignment_3():
    extractor = AspectExtractor()

    reviews = [
        "The active noise cancellation creates pure silence, but the battery life is subpar.",
        "The tactile keyboard and mini-LED display are unmatched, though fan noise is annoying.",
        "Our cloud ETL pipelines are rock solid, but billing charges were quadruple our quota."
    ]

    print("=" * 60)
    print("ASSIGNMENT 3: ASPECT TARGET EXTRACTION & MAPPING")
    print("=" * 60)

    for i, rev in enumerate(reviews, 1):
        extracted = extractor.extract_aspects(rev)
        print(f"\n[Review #{i}]: \"{rev}\"")
        print(f"   Aspect Count: {extracted['aspect_count']}")
        print(f"   Categories  : {', '.join(extracted['unique_categories'])}")
        print("   Detailed Mentions:")
        for m in extracted["aspect_mentions"]:
            print(f"     • Term: '{m['term']}' | Canonical: '{m['canonical_aspect']}' | Clause: \"{m['clause']}\"")


if __name__ == "__main__":
    run_assignment_3()
