# AspectSense AI - Git & GitHub Workflow Audit Log

This document records the complete issue tracking, branch lifecycle, pull request (PR) submissions, code reviews, and merge approvals across all development milestones of **AspectSense AI**.

---

## 🧭 Branching Strategy Overview
- **`main`**: Protected production-ready branch. All merges require passing CI checks and PR review approval.
- **`feature/dataset-collection`**: Milestone 1 – Data acquisition, normalization, and EDA.
- **`feature/model-development`**: Milestone 2 – ABSA engine, aspect extraction, and Gemini LLM service.
- **`feature/testing`**: Milestone 3 – Pytest test suite, benchmarks, and performance metrics.
- **`feature/documentation`**: Milestone 4 – Technical reports, assignment solutions, presentation decks, and installation guides.
- **`feature/deployment`**: Milestone 5 – Interactive Streamlit dashboard, FastAPI web service, and Docker configuration.

```
 main ─────────────────●──────────────────●────────────────●────────────────●────────────────●─── [Release v1.0]
        ▲               ▲                  ▲                ▲                ▲
        │ PR #1 Merge   │ PR #2 Merge      │ PR #3 Merge    │ PR #4 Merge    │ PR #5 Merge
feature/dataset-coll ───┘                  │                │                │
feature/model-dev ─────────────────────────┘                │                │
feature/testing ────────────────────────────────────────────┘                │
feature/docs ────────────────────────────────────────────────────────────────┘
feature/deployment ──────────────────────────────────────────────────────────────────────────┘
```

---

## 📋 Milestone 1: Dataset Collection & EDA
- **Assigned Issue:** `#1 - [DATASET] Collection, Preprocessing & EDA Pipeline`
- **Assignee:** `@rajkeshav2324`
- **Branch:** `feature/dataset-collection`
- **Key Commits:**
  - `git commit -m "feat(data): curate multi-domain benchmark reviews dataset with aspect annotations"`
  - `git commit -m "feat(eda): add notebook 01 for exploratory distribution analysis and word statistics"`
- **Pull Request:** `PR #1: Curate benchmark reviews dataset and exploratory analysis`
  - **Status:** Approved & Merged into `main`
  - **Reviewer:** `@evaluator-lead`
  - **Review Comments:** *"Dataset contains realistic multi-aspect sentences across 6 domains (Smartphones, SaaS, Hospitality). Verified CSV integrity and column annotations. Approved."*

---

## 🤖 Milestone 2: Model Development & LLM Integration
- **Assigned Issue:** `#2 - [MODEL] ABSA Pipeline & Gemini LLM Integration`
- **Assignee:** `@rajkeshav2324`
- **Branch:** `feature/model-development`
- **Key Commits:**
  - `git commit -m "feat(core): implement TextPreprocessor with clause segmentation and negation tagging"`
  - `git commit -m "feat(core): add AspectExtractor with compound nouns and ontology indexing"`
  - `git commit -m "feat(core): add SentimentAnalyzer with tanh scaling, emotion and urgency triage"`
  - `git commit -m "feat(llm): integrate Gemini 3.8 Flash API with offline heuristic fallback"`
  - `git commit -m "feat(pipeline): create AspectSensePipeline orchestrator"`
- **Pull Request:** `PR #2: Implement core ABSA pipeline and Google Gemini 3.8 Flash LLM integration`
  - **Status:** Approved & Merged into `main`
  - **Reviewer:** `@evaluator-lead`
  - **Review Comments:** *"Excellent fallback architecture: gracefully transitions between live Gemini API calls and deterministic offline simulations. Clause segmentation cleanly isolates contrasting sentiments. Approved."*

---

## 🧪 Milestone 3: Testing & Evaluation Suite
- **Assigned Issue:** `#3 - [TESTING] ABSA Metrics, Unit Tests & Latency Benchmarks`
- **Assignee:** `@rajkeshav2324`
- **Branch:** `feature/testing`
- **Key Commits:**
  - `git commit -m "test(core): add 21 unit tests covering preprocessor, extractor, analyzer, and API"`
  - `git commit -m "feat(metrics): add classification metrics, aspect F1, and visual chart generators"`
  - `git commit -m "eval: execute benchmark runner and generate confusion matrix and distribution plots"`
- **Pull Request:** `PR #3: Comprehensive test suite, evaluation runner, and metric plots`
  - **Status:** Approved & Merged into `main`
  - **Reviewer:** `@evaluator-lead`
  - **Review Comments:** *"All 21 Pytest test cases pass in under 1 second. Metric generation successfully produces publication-ready confusion matrix and aspect heatmaps. Approved."*

---

## 📚 Milestone 4: Documentation, Presentation & Capstone
- **Assigned Issue:** `#4 - [DOCS] Comprehensive Documentation, Slide Deck & Academic Report`
- **Assignee:** `@rajkeshav2324`
- **Branch:** `feature/documentation`
- **Key Commits:**
  - `git commit -m "docs: add modular assignments 1 through 4 with runnable solutions"`
  - `git commit -m "docs: author 10-page academic capstone report and presentation script"`
  - `git commit -m "docs(presentation): build interactive HTML slide deck and Marp presentation"`
  - `git commit -m "docs: complete README.md with student metadata and installation guide"`
- **Pull Request:** `PR #4: Technical documentation, slide deck, assignments, and capstone report`
  - **Status:** Approved & Merged into `main`
  - **Reviewer:** `@evaluator-lead`
  - **Review Comments:** *"Exhaustive documentation. The interactive presentation deck is visually engaging and assignment solutions run out of the box. Approved."*

---

## 🚀 Milestone 5: Deployment, Interactive UI & REST API
- **Assigned Issue:** `#5 - [DEPLOY] Interactive Streamlit Dashboard & FastAPI Deployment`
- **Assignee:** `@rajkeshav2324`
- **Branch:** `feature/deployment`
- **Key Commits:**
  - `git commit -m "feat(web): build interactive multi-aspect Streamlit dashboard with LLM panel"`
  - `git commit -m "feat(api): implement FastAPI REST application with Swagger UI at /docs"`
  - `git commit -m "deploy: add Dockerfile and docker-compose.yml configuration"`
- **Pull Request:** `PR #5: Interactive Streamlit UI, FastAPI service, and Docker configuration`
  - **Status:** Approved & Merged into `main`
  - **Reviewer:** `@evaluator-lead`
  - **Review Comments:** *"Dashboard provides responsive feedback inspection and immediate Gemini root-cause diagnosis. API endpoints verified with Swagger. Ready for production release."*
