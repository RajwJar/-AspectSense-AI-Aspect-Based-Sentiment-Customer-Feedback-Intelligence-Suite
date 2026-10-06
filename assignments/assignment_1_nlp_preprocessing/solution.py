"""
Assignment 1 Solution: NLP Preprocessing & Clause Segmentation
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from code.core.preprocessor import TextPreprocessor


def run_assignment_1():
    preprocessor = TextPreprocessor()

    test_reviews = [
        "The screen is absolutely gorgeous, but the battery life barely lasts six hours!",
        "Don't buy this laptop; it's overpriced and customer support isn't helpful at all.",
        "Unbeatable noise cancellation and crisp sound, however the ear pads make my ears sweat."
    ]

    print("=" * 60)
    print("ASSIGNMENT 1: NLP TEXT NORMALIZATION & CLAUSE SEGMENTATION")
    print("=" * 60)

    for i, review in enumerate(test_reviews, 1):
        print(f"\n[Test Review #{i}]")
        print(f"Original: {review}")
        result = preprocessor.preprocess_pipeline(review)
        print(f"Cleaned Text: {result['cleaned_text']}")
        print(f"Segmented Clauses ({result['clause_count']}):")
        for j, c in enumerate(result['clauses'], 1):
            print(f"   Clause {j}: '{c}'")
        print(f"Tokens: {result['tokens'][:8]}... (Total: {result['token_count']})")


if __name__ == "__main__":
    run_assignment_1()
