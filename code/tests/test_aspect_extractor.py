"""
Unit tests for AspectExtractor
"""

import pytest
from code.core.aspect_extractor import AspectExtractor


@pytest.fixture
def extractor():
    return AspectExtractor()


def test_extract_compound_nouns(extractor):
    text = "The battery life is exceptional, but the customer support is slow."
    compounds = extractor.extract_compound_nouns(text)
    assert any("battery life" in c for c in compounds) or any("customer support" in c for c in compounds)


def test_extract_aspects_single(extractor):
    text = "The OLED screen is gorgeous."
    res = extractor.extract_aspects(text)
    assert res["aspect_count"] >= 1
    terms = [m["term"] for m in res["aspect_mentions"]]
    assert any("screen" in t or "oled" in t for t in terms)


def test_extract_aspects_multiple(extractor):
    text = "The camera is stunning, but the battery life is terrible."
    res = extractor.extract_aspects(text)
    categories = res["unique_categories"]
    assert "camera" in categories
    assert "battery" in categories
