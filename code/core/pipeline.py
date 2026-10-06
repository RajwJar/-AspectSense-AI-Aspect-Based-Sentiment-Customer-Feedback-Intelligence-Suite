"""
Main Pipeline Orchestrator for AspectSense AI
Combines text preprocessing, aspect extraction, sentiment analysis,
emotion detection, urgency scoring, and Gemini LLM intelligence.
"""

import os
import sys
import argparse
import json
from typing import Dict, Any, List, Optional

from .preprocessor import TextPreprocessor
from .aspect_extractor import AspectExtractor
from .sentiment_analyzer import SentimentAnalyzer
from .llm_service import LLMService


class AspectSensePipeline:
    """
    Unified end-to-end NLP & LLM processing pipeline.
    """

    def __init__(self, api_key: Optional[str] = None, lexicon_path: Optional[str] = None):
        self.preprocessor = TextPreprocessor()
        self.extractor = AspectExtractor(lexicon_path=lexicon_path)
        self.analyzer = SentimentAnalyzer()
        self.llm_service = LLMService(api_key=api_key)

    def analyze_review(
        self,
        review_text: str,
        domain: str = "Technology",
        include_llm_diagnostics: bool = True
    ) -> Dict[str, Any]:
        """
        Executes end-to-end analysis on an individual customer review.
        """
        # 1. Preprocessing
        prep_result = self.preprocessor.preprocess_pipeline(review_text)

        # 2. Aspect Extraction
        aspect_data = self.extractor.extract_aspects(prep_result["cleaned_text"])

        # 3. Overall Text Polarity & Emotion
        overall_polarity, overall_subjectivity = self.analyzer.score_text_fragment(prep_result["cleaned_text"])
        overall_sentiment_label = self.analyzer.classify_polarity_label(overall_polarity)
        emotion = self.analyzer.detect_emotion(prep_result["cleaned_text"], overall_polarity)
        urgency = self.analyzer.determine_urgency(prep_result["cleaned_text"], overall_polarity)

        # 4. Aspect-Level Sentiment Scoring
        aspect_sentiments = self.analyzer.analyze_aspect_sentiments(
            prep_result["cleaned_text"], aspect_data
        )

        # If aspects have opposing polarities, overall sentiment is 'mixed'
        sentiments_set = {a["sentiment"] for a in aspect_sentiments}
        if "positive" in sentiments_set and "negative" in sentiments_set:
            overall_sentiment_label = "mixed"

        # 5. Gemini LLM Root-Cause Diagnostics & Response Drafting
        llm_output = None
        if include_llm_diagnostics:
            llm_output = self.llm_service.generate_root_cause_analysis(
                review_text=review_text,
                detected_aspects=aspect_sentiments,
                overall_sentiment=overall_sentiment_label,
                domain=domain
            )

        return {
            "input_text": review_text,
            "domain": domain,
            "preprocessing": {
                "cleaned_text": prep_result["cleaned_text"],
                "clause_count": prep_result["clause_count"],
                "token_count": prep_result["token_count"]
            },
            "overall_assessment": {
                "sentiment": overall_sentiment_label,
                "polarity_score": overall_polarity,
                "subjectivity_score": overall_subjectivity,
                "emotion": emotion,
                "urgency_level": urgency
            },
            "aspect_analysis": {
                "aspect_count": len(aspect_sentiments),
                "aspects": aspect_sentiments
            },
            "llm_diagnostics": llm_output,
            "pipeline_status": "SUCCESS"
        }

    def analyze_batch(self, reviews: List[Dict[str, str]], include_llm: bool = False) -> List[Dict[str, Any]]:
        """Analyzes a collection of reviews efficiently."""
        results = []
        for item in reviews:
            text = item.get("review_text", "")
            domain = item.get("domain", "Technology")
            res = self.analyze_review(text, domain=domain, include_llm_diagnostics=include_llm)
            results.append(res)
        return results


def run_sanity_check():
    """CLI sanity check used in automated CI and testing."""
    pipeline = AspectSensePipeline()
    sample = "The OLED screen and camera are stunning, but the battery drains fast and customer service was unhelpful."
    result = pipeline.analyze_review(sample, domain="Smartphones", include_llm_diagnostics=True)
    print("\n--- AspectSense AI Sanity Check ---")
    print(f"Overall Sentiment: {result['overall_assessment']['sentiment']}")
    print(f"Emotion: {result['overall_assessment']['emotion']}")
    print(f"Urgency: {result['overall_assessment']['urgency_level']}")
    print(f"Aspects Found: {len(result['aspect_analysis']['aspects'])}")
    for a in result['aspect_analysis']['aspects']:
        print(f"  • {a['aspect_term']} -> {a['sentiment']} (score: {a['polarity_score']})")
    print(f"LLM Root Cause: {result['llm_diagnostics']['root_cause_summary']}")
    print(f"LLM Source: {result['llm_diagnostics']['source']}")
    print("Sanity check PASSED successfully!\n")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AspectSense AI Pipeline CLI")
    parser.add_argument("--sanity-check", action="store_true", help="Run sanity check")
    parser.add_argument("--text", type=str, help="Text to analyze")
    parser.add_argument("--domain", type=str, default="Technology", help="Product domain")
    args = parser.parse_args()

    if args.sanity_check:
        run_sanity_check()
    elif args.text:
        pipeline = AspectSensePipeline()
        output = pipeline.analyze_review(args.text, domain=args.domain)
        print(json.dumps(output, indent=2))
    else:
        run_sanity_check()
