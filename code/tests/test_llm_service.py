"""
Unit tests for LLMService
"""

import pytest
from code.core.llm_service import LLMService


@pytest.fixture
def llm_service():
    return LLMService(api_key=None)  # Tests offline mode guaranteed reproducibility


def test_offline_diagnosis_structure(llm_service):
    review = "Overpriced phone with horrible battery life, but beautiful display."
    aspects = [
        {"aspect_term": "battery life", "sentiment": "negative"},
        {"aspect_term": "display", "sentiment": "positive"}
    ]
    diag = llm_service.generate_root_cause_analysis(
        review_text=review,
        detected_aspects=aspects,
        overall_sentiment="mixed",
        domain="Smartphones"
    )

    assert "root_cause_summary" in diag
    assert "impact_severity" in diag
    assert "actionable_recommendations" in diag
    assert len(diag["actionable_recommendations"]) >= 1
    assert "draft_customer_response" in diag
    assert len(diag["draft_customer_response"]) > 10


def test_offline_customer_draft(llm_service):
    review = "Fastest phone I have ever owned, amazing charging speed!"
    aspects = [
        {"aspect_term": "speed", "sentiment": "positive"},
        {"aspect_term": "charging", "sentiment": "positive"}
    ]
    diag = llm_service.generate_root_cause_analysis(
        review_text=review,
        detected_aspects=aspects,
        overall_sentiment="positive",
        domain="Smartphones"
    )

    assert diag["impact_severity"] == "Low"
    assert "thank you" in diag["draft_customer_response"].lower()
