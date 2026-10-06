"""
Assignment 4 Solution: Generative LLM Integration & Root-Cause Diagnosis
"""

import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from code.core.pipeline import AspectSensePipeline


def run_assignment_4():
    pipeline = AspectSensePipeline()

    review = "The phone overheats constantly within ten minutes of video recording, and customer service refused the warranty replacement."
    domain = "Smartphones"

    print("=" * 60)
    print("ASSIGNMENT 4: GEMINI LLM REASONING & ROOT-CAUSE SYNTHESIS")
    print("=" * 60)
    print(f"\nReview Input: \"{review}\"")
    print(f"Domain      : {domain}")
    print(f"LLM Status  : {'🟢 Live Gemini Connected' if pipeline.llm_service.is_live_connected() else '🟡 Offline Heuristic Mode'}\n")

    result = pipeline.analyze_review(review, domain=domain, include_llm_diagnostics=True)

    print("--- Pipeline Assessment ---")
    print(f"Overall Sentiment: {result['overall_assessment']['sentiment'].upper()}")
    print(f"Emotion          : {result['overall_assessment']['emotion']}")
    print(f"Triage Urgency   : {result['overall_assessment']['urgency_level']}")

    print("\n--- Detected Aspects ---")
    for a in result['aspect_analysis']['aspects']:
        print(f"  • {a['aspect_term']} ({a['canonical_aspect']}): {a['sentiment']} (score: {a['polarity_score']})")

    diag = result["llm_diagnostics"]
    print("\n--- LLM Root-Cause & Customer Action Output ---")
    print(f"Source: {diag.get('source')}")
    print(f"Severity: {diag.get('impact_severity')}")
    print(f"Root Cause: {diag.get('root_cause_summary')}")
    print("\nRecommendations:")
    for r in diag.get("actionable_recommendations", []):
        print(f"  [+] {r}")
    print(f"\nDrafted Response:\n\"{diag.get('draft_customer_response')}\"")


if __name__ == "__main__":
    run_assignment_4()
