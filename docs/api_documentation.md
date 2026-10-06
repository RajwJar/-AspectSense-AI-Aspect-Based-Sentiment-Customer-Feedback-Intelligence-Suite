# AspectSense AI - REST API Reference

The AspectSense AI REST API exposes high-throughput endpoints for Aspect-Based Sentiment Analysis, emotion classification, customer urgency triage, and Google Gemini LLM diagnostics.

---

## 🌐 Base URL
```
http://localhost:8000
```
Interactive OpenAPI / Swagger Docs: **`http://localhost:8000/docs`**  
ReDoc UI: **`http://localhost:8000/redoc`**

---

## 📌 Endpoints

### 1. Health & Service Metadata
`GET /` & `GET /health`

**Sample Response:**
```json
{
  "service": "AspectSense AI Engine",
  "status": "online",
  "version": "1.0.0",
  "documentation": "/docs",
  "llm_connected": false,
  "model": "gemini-3.8-flash"
}
```

---

### 2. Single Review Analysis
`POST /api/v1/analyze`

**Request Body:**
```json
{
  "review_text": "The OLED screen and camera are stunning, but the battery drains fast and customer support was completely unhelpful.",
  "domain": "Smartphones",
  "include_llm_diagnostics": true
}
```

**Response Body:**
```json
{
  "input_text": "The OLED screen and camera are stunning, but the battery drains fast and customer support was completely unhelpful.",
  "domain": "Smartphones",
  "preprocessing": {
    "cleaned_text": "The OLED screen and camera are stunning, but the battery drains fast and customer support was completely unhelpful.",
    "clause_count": 2,
    "token_count": 18
  },
  "overall_assessment": {
    "sentiment": "mixed",
    "polarity_score": 0.05,
    "subjectivity_score": 0.42,
    "emotion": "frustration",
    "urgency_level": "High"
  },
  "aspect_analysis": {
    "aspect_count": 3,
    "aspects": [
      {
        "aspect_term": "screen",
        "canonical_aspect": "screen_display",
        "clause_context": "The OLED screen and camera are stunning",
        "polarity_score": 0.72,
        "sentiment": "positive"
      },
      {
        "aspect_term": "camera",
        "canonical_aspect": "camera",
        "clause_context": "The OLED screen and camera are stunning",
        "polarity_score": 0.72,
        "sentiment": "positive"
      },
      {
        "aspect_term": "battery",
        "canonical_aspect": "battery",
        "clause_context": "the battery drains fast and customer support was completely unhelpful.",
        "polarity_score": -0.81,
        "sentiment": "negative"
      }
    ]
  },
  "llm_diagnostics": {
    "root_cause_summary": "Customer friction stemmed primarily from battery drain and support unresponsiveness, while appreciating the display and camera.",
    "impact_severity": "High",
    "actionable_recommendations": [
      "Conduct power-profiling telemetry and release a firmware patch to optimize standby background drain.",
      "Implement automated SLA escalation for high-urgency customer tickets."
    ],
    "draft_customer_response": "Hello, thank you for sharing your candid feedback...",
    "source": "AspectSense Heuristic LLM Simulator (Offline Mode)"
  },
  "pipeline_status": "SUCCESS"
}
```

---

### 3. Batch Review Analysis
`POST /api/v1/batch`

**Request Body:**
```json
{
  "reviews": [
    {"review_text": "Unmatched keyboard and smooth trackpad.", "domain": "Laptops"},
    {"review_text": "Overheating issues and loud fan noise.", "domain": "Laptops"}
  ]
}
```

---

### 4. Domain Aspect Categories
`GET /api/v1/aspects`

Returns dictionary mapping supported product domains and aspect categories to seed keyword synonyms.
