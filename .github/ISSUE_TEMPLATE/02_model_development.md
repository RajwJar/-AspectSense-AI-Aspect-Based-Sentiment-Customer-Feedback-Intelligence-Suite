---
name: "Task: Model Development & LLM Integration"
about: "Develop Aspect-Based Sentiment Analysis (ABSA) model and integrate Gemini LLM API."
title: "[MODEL] ABSA Pipeline & Gemini LLM Integration"
labels: ["model-development", "llm-api", "phase-2"]
assignees: ["rajkeshav2324"]
---

### Objective
Build the core NLP pipeline for aspect extraction, sentiment scoring, and integrate Google Gemini LLM API for root-cause diagnosis and automated response generation.

### Key Deliverables
- [ ] Implement rule-based & syntactic dependency aspect extraction (`code/core/aspect_extractor.py`).
- [ ] Build multi-aspect sentiment and emotion classifier (`code/core/sentiment_analyzer.py`).
- [ ] Integrate Google Gemini 3.8 Flash LLM client (`code/core/llm_service.py`) for root cause insights & customer response drafting.
- [ ] Create orchestrator pipeline (`code/core/pipeline.py`).
- [ ] Document training/modeling pipeline in `notebooks/03_absa_model_training_and_evaluation.ipynb`.

### Definition of Done
- Aspect extraction identifies target entities (e.g., "battery", "customer support", "camera").
- LLM API call produces structured diagnostic JSON and empathetic response.
- Offline fallback supported when API key is unavailable.
- Pull request submitted, reviewed, and merged.
