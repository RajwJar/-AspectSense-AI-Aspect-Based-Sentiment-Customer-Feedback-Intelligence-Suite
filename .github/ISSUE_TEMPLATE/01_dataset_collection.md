---
name: "Task: Dataset Collection & Exploratory Data Analysis"
about: "Track dataset acquisition, cleaning, preprocessing, and EDA for multi-domain customer feedback."
title: "[DATASET] Collection, Preprocessing & EDA Pipeline"
labels: ["dataset", "nlp-preprocessing", "phase-1"]
assignees: ["rajkeshav2324"]
---

### Objective
Collect, annotate, and preprocess high-quality multi-domain customer feedback and product review datasets for Aspect-Based Sentiment Analysis (ABSA).

### Key Deliverables
- [ ] Curate benchmark reviews dataset across domains (Smartphones, SaaS, Laptops, Hospitality).
- [ ] Implement text normalization, contraction expansion, and tokenization.
- [ ] Perform Exploratory Data Analysis (EDA): word frequencies, sentiment distribution, review length metrics.
- [ ] Save processed dataset to `resources/data/customer_reviews_benchmark.csv`.
- [ ] Document findings in `notebooks/01_dataset_collection_and_eda.ipynb`.

### Definition of Done
- Dataset contains multi-aspect sentences with ground-truth sentiment labels.
- EDA notebook generates summary statistics and visualizations.
- Code reviewed and merged into `main` via Pull Request.
