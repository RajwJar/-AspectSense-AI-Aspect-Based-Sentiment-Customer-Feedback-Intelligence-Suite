"""
Unit tests for TextPreprocessor
"""

import pytest
from code.core.preprocessor import TextPreprocessor


@pytest.fixture
def preprocessor():
    return TextPreprocessor()


def test_expand_contractions(preprocessor):
    text = "I don't like it and it isn't working."
    expanded = preprocessor.expand_contractions(text)
    assert "do not" in expanded
    assert "is not" in expanded


def test_clean_text(preprocessor):
    dirty = "Great phone! <br> Check https://example.com for info.   Lots    of spaces!!!"
    cleaned = preprocessor.clean_text(dirty)
    assert "<br>" not in cleaned
    assert "https://" not in cleaned
    assert "  " not in cleaned
    assert "!" in cleaned


def test_segment_into_clauses(preprocessor):
    compound = "The screen is wonderful, but the battery drains in four hours; however the camera is good."
    clauses = preprocessor.segment_into_clauses(compound)
    assert len(clauses) >= 2
    assert any("screen" in c.lower() for c in clauses)
    assert any("battery" in c.lower() for c in clauses)


def test_tag_negations(preprocessor):
    tokens = ["the", "battery", "is", "not", "very", "good"]
    tagged = preprocessor.tag_negations(tokens)
    # Tokens after 'not' within window should be flagged as negated
    neg_flags = [is_neg for tok, is_neg in tagged]
    assert True in neg_flags
