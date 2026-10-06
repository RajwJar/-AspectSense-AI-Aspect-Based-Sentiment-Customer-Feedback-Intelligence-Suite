---
name: "Task: Testing & Evaluation Suite"
about: "Construct unit tests, performance benchmarks, and evaluation metrics for ABSA & LLM pipeline."
title: "[TESTING] ABSA Metrics, Unit Tests & Latency Benchmarks"
labels: ["testing", "evaluation", "qa", "phase-3"]
assignees: ["rajkeshav2324"]
---

### Objective
Ensure robustness, numerical correctness, and evaluation integrity across all NLP modules and LLM API integrations.

### Key Deliverables
- [ ] Implement unit test suite with `pytest` covering preprocessor, aspect extractor, sentiment analyzer, LLM service, and API endpoints.
- [ ] Compute Precision, Recall, Macro F1-score, and Confusion Matrix on the benchmark test set.
- [ ] Measure API latency, tokens per second, and error handling for missing/malformed inputs.
- [ ] Generate visual metric plots in `resources/results/`.
- [ ] Document test execution in `capstone/rubric_compliance_matrix.md`.

### Definition of Done
- Test suite achieves >90% code coverage.
- ABSA Accuracy and F1-score benchmarks logged in `resources/results/benchmark_report.json`.
- All tests pass cleanly in automated CI.
