"""
FastAPI REST Service for AspectSense AI
Provides endpoints for real-time aspect-based sentiment analysis,
batch text processing, ontology discovery, and Gemini LLM diagnostics.
"""

from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from code.core.pipeline import AspectSensePipeline
from code.core.aspect_extractor import DEFAULT_ASPECT_CATEGORIES

app = FastAPI(
    title="AspectSense AI - API",
    description="Enterprise Aspect-Based Sentiment Analysis & LLM Root-Cause Diagnostics Service",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Enable CORS for external frontends or integrations
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pipeline = AspectSensePipeline()


class ReviewRequest(BaseModel):
    review_text: str = Field(..., example="The camera and display are stunning, but the battery drains fast and customer support was completely unhelpful.")
    domain: Optional[str] = Field("Smartphones", example="Smartphones")
    include_llm_diagnostics: Optional[bool] = Field(True, description="Whether to invoke Gemini LLM for root cause diagnosis and reply drafting")


class BatchReviewRequest(BaseModel):
    reviews: List[ReviewRequest]


@app.get("/")
def root():
    return {
        "service": "AspectSense AI Engine",
        "status": "online",
        "version": "1.0.0",
        "documentation": "/docs",
        "llm_connected": pipeline.llm_service.is_live_connected(),
        "model": pipeline.llm_service.model_name
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "llm_live_mode": pipeline.llm_service.is_live_connected(),
        "model": pipeline.llm_service.model_name
    }


@app.get("/api/v1/aspects")
def get_supported_aspects():
    """Returns supported aspect categories and seed terms."""
    return {
        "aspect_categories": DEFAULT_ASPECT_CATEGORIES
    }


@app.post("/api/v1/analyze")
def analyze_review_endpoint(request: ReviewRequest):
    """
    Performs full ABSA, emotion detection, urgency scoring,
    and LLM root-cause synthesis on a customer review.
    """
    if not request.review_text.strip():
        raise HTTPException(status_code=400, detail="review_text cannot be empty.")

    try:
        result = pipeline.analyze_review(
            review_text=request.review_text,
            domain=request.domain or "Technology",
            include_llm_diagnostics=request.include_llm_diagnostics
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


@app.post("/api/v1/batch")
def analyze_batch_endpoint(request: BatchReviewRequest):
    """
    Processes multiple reviews in batch mode.
    """
    if not request.reviews:
        raise HTTPException(status_code=400, detail="reviews list cannot be empty.")

    formatted_inputs = [
        {"review_text": r.review_text, "domain": r.domain or "Technology"}
        for r in request.reviews
    ]

    results = pipeline.analyze_batch(formatted_inputs, include_llm=False)
    return {
        "total_processed": len(results),
        "results": results
    }
