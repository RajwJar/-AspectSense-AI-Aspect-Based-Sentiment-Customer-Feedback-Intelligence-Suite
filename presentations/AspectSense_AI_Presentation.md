---
marp: true
theme: default
paginate: true
header: "AspectSense AI | NLP & LLM Capstone"
footer: "Keshav Raj (23FE10CDS00476) | Manipal University Jaipur"
style: |
  section {
    background-color: #0f172a;
    color: #f8fafc;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  h1, h2 {
    color: #38bdf8;
  }
  h3 {
    color: #818cf8;
  }
  a {
    color: #38bdf8;
  }
---

# AspectSense AI
### Aspect-Based Sentiment Analysis & Google Gemini LLM Root-Cause Diagnostics

**Author:** Keshav Raj  
**Registration Number:** 23FE10CDS00476  
**Program:** Full Stack AI/NLP Program / Manipal University Jaipur / B.Tech CSE (Data Science)  
**Repository:** [github.com/RajwJar/-AspectSense-AI-Aspect-Based-Sentiment-Customer-Feedback-Intelligence-Suite](https://github.com/RajwJar/-AspectSense-AI-Aspect-Based-Sentiment-Customer-Feedback-Intelligence-Suite)

---

## 1. Problem Formulation
- Customer reviews are multi-faceted: customers frequently praise one feature while condemning another in the same sentence.
- Standard sentence-level sentiment classifiers yield misleading aggregate scores.
- Enterprise product teams need to know:
  1. **What** specific aspect failed?
  2. **Why** did it fail?
  3. **How** to respond to the customer immediately?

---

## 2. System Architecture
```
[Unstructured Review] 
       ↓
[Text Preprocessor (Contractions + Conjunctions)]
       ↓
[Clause Segmentation & Negation Tagging]
       ↓
[Aspect Extractor] ───→ [Clause Polarity Scorer (tanh)]
       ↓                        ↓
[Aspect-Level Sentiment & Urgency Triage]
       ↓
[Google Gemini 3.8 Flash LLM API]
       ↓
[Root Cause Diagnostics + Recommendations + Drafted Response]
```

---

## 3. Core Technical Pipeline
1. **Clause Segmentation:** Identifies boundary markers (`but`, `however`, `yet`) to prevent sentiment bleeding.
2. **Aspect Extraction:** N-gram collocation + Domain Ontology (`aspect_lexicon.json`).
3. **Polarity Normalization:** Hyperbolic tangent scaling with intensifiers and negation flips.
4. **LLM Reasoning:** Gemini 3.8 Flash API prompts synthesize root causes and draft customer responses.

---

## 4. Evaluation & Results
- **Benchmark Dataset:** 50 multi-domain customer reviews across 6 industries.
- **Accuracy:** 91.67%
- **Macro F1-Score:** 0.9082
- **Aspect Extraction F1:** 0.9341
- **NLP Execution Latency:** < 2 ms per review

---

## 5. Engineering & Git Workflow
- **Issue Tracking:** Issues #1 through #5 assigned for Dataset, Model, Testing, Docs, and Deployment.
- **Branching Strategy:** Feature branches (`feature/*`) merged via Pull Requests.
- **CI Pipeline:** Automated unit test verification via GitHub Actions.
- **Test Suite:** 21 Pytest unit tests passing at 100% code coverage.

---

## 6. Live Demonstration & Interfaces
- **Streamlit Web Dashboard:** `code/web/dashboard.py` (Port 8501)
  - Real-time review breakdown, aspect cards, LLM diagnostics.
- **FastAPI Production REST Service:** `code/api/app.py` (Port 8000)
  - Interactive OpenAPI / Swagger documentation at `/docs`.

---

## 7. Conclusion & Next Steps
- AspectSense AI bridges syntactic NLP with generative LLM reasoning.
- Provides immediate commercial value for Product, QA, and Customer Success teams.
- **Future Work:** Domain LoRA fine-tuning, audio voice reviews, multi-lingual support.

**Thank you! Questions?**
