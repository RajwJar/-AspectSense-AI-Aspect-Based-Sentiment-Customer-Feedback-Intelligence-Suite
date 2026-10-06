"""
Unit tests for AspectSensePipeline
"""

import pytest
from code.core.pipeline import AspectSensePipeline


@pytest.fixture
def pipeline():
    return AspectSensePipeline()


def test_pipeline_single_review(pipeline):
    review = "The OLED screen is gorgeous, but the battery life is terrible."
    result = pipeline.analyze_review(review, domain="Smartphones", include_llm_diagnostics=True)

    assert result["pipeline_status"] == "SUCCESS"
    assert result["overall_assessment"]["sentiment"] == "mixed"
    assert len(result["aspect_analysis"]["aspects"]) >= 2
    assert result["llm_diagnostics"] is not None


def test_pipeline_batch_analysis(pipeline):
    reviews = [
        {"review_text": "Great laptop, lightning fast M3 processor.", "domain": "Laptops"},
        {"review_text": "Broken keyboard keys and rattles constantly.", "domain": "Laptops"}
    ]
    batch_results = pipeline.analyze_batch(reviews, include_llm=False)
    assert len(batch_results) == 2
    assert batch_results[0]["overall_assessment"]["sentiment"] == "positive"
    assert batch_results[1]["overall_assessment"]["sentiment"] == "negative"
