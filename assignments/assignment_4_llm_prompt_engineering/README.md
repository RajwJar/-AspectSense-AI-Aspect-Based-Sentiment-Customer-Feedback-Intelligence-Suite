# Assignment 4: Generative LLM Integration & Root-Cause Diagnosis

## 🎯 Objective
Integrate Large Language Model API (Google Gemini 3.8 Flash via `google-genai` SDK) into the NLP feedback intelligence workflow to:
1. Synthesize multi-aspect sentiments into root-cause engineering diagnostics.
2. Generate executive-level strategic recommendations for Product Managers.
3. Automatically draft personalized, empathetic customer support replies.
4. Ensure graceful degradation through deterministic fallback heuristic simulation when API keys are absent.

---

## 📚 Structured Prompting Architecture
The prompt instructs the LLM with a strict persona (*"AspectSense AI Enterprise Product Intelligence Assistant"*), feeding detected aspect extractions as contextual metadata:
```text
System Context: Enterprise Product Intelligence
Input Review: "The camera is stunning, but the battery drains fast and customer support was completely unhelpful."
Extracted Aspects: camera (positive), battery (negative), customer support (negative)
Target: JSON-only output with root_cause_summary, impact_severity, actionable_recommendations, and draft_customer_response.
```

---

## 🛠️ Execution
Run `python solution.py` to trigger LLM synthesis (live if `GEMINI_API_KEY` is set, or offline simulation mode).
