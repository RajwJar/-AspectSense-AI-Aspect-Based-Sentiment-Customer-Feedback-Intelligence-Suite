"""
Assignment 2 Solution: Sentiment Lexicon Scoring & Emotion Detection
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from code.core.sentiment_analyzer import SentimentAnalyzer


def run_assignment_2():
    analyzer = SentimentAnalyzer()

    phrases = [
        "The OLED screen is absolutely gorgeous and stunning.",
        "The battery life is not good at all, barely lasts three hours.",
        "Total disaster! Motherboard fried and customer service refused refund.",
        "It is an average laptop with standard basic features."
    ]

    print("=" * 60)
    print("ASSIGNMENT 2: LEXICON POLARITY & EMOTION DETECTION")
    print("=" * 60)

    for i, phrase in enumerate(phrases, 1):
        polarity, subjectivity = analyzer.score_text_fragment(phrase)
        label = analyzer.classify_polarity_label(polarity)
        emotion = analyzer.detect_emotion(phrase, polarity)
        urgency = analyzer.determine_urgency(phrase, polarity)

        print(f"\n[Phrase #{i}]: '{phrase}'")
        print(f"   Polarity Score    : {polarity:+.3f}")
        print(f"   Subjectivity Score: {subjectivity:.3f}")
        print(f"   Sentiment Label   : {label.upper()}")
        print(f"   Detected Emotion  : {emotion}")
        print(f"   Triage Urgency    : {urgency}")


if __name__ == "__main__":
    run_assignment_2()
