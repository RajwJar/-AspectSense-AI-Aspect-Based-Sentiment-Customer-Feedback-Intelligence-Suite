"""
Unit tests for SentimentAnalyzer
"""

import pytest
from code.core.sentiment_analyzer import SentimentAnalyzer
from code.core.aspect_extractor import AspectExtractor


@pytest.fixture
def analyzer():
    return SentimentAnalyzer()


@pytest.fixture
def extractor():
    return AspectExtractor()


def test_positive_scoring(analyzer):
    text = "The screen is absolutely stunning and flawless."
    polarity, subjectivity = analyzer.score_text_fragment(text)
    assert polarity > 0.3
    assert analyzer.classify_polarity_label(polarity) == "positive"


def test_negative_scoring(analyzer):
    text = "Total disaster. Motherboard fried and customer service was terrible."
    polarity, subjectivity = analyzer.score_text_fragment(text)
    assert polarity < -0.3
    assert analyzer.classify_polarity_label(polarity) == "negative"


def test_emotion_detection(analyzer):
    joy_text = "The audio quality is stunning, a pure delight!"
    assert analyzer.detect_emotion(joy_text, 0.8) == "joy"

    anger_text = "Unacceptable nightmare, they laughed at my complaint!"
    assert analyzer.detect_emotion(anger_text, -0.9) in ["anger", "frustration"]


def test_urgency_triage(analyzer):
    urgent_text = "Zero support response during critical production outage, data corrupted!"
    assert analyzer.determine_urgency(urgent_text, -0.85) in ["Critical", "High"]

    low_urgency_text = "Lightweight laptop, great keyboard for typing."
    assert analyzer.determine_urgency(low_urgency_text, 0.6) == "Low"


def test_aspect_sentiments(analyzer, extractor):
    text = "The camera is stunning, but the battery life is terrible."
    aspect_data = extractor.extract_aspects(text)
    aspect_sentiments = analyzer.analyze_aspect_sentiments(text, aspect_data)

    assert len(aspect_sentiments) >= 2
    sent_dict = {a["canonical_aspect"]: a["sentiment"] for a in aspect_sentiments}
    assert sent_dict.get("camera") == "positive"
    assert sent_dict.get("battery") == "negative"
