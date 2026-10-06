"""
Script to generate the 4 standard Jupyter Notebooks for AspectSense AI.
"""

import json
import os
from pathlib import Path


def make_notebook(cells):
    return {
        "cells": cells,
        "metadata": {
            "language_info": {"name": "python", "version": "3.12.6"},
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }


def md_cell(text):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in text.strip().split("\n")]
    }


def code_cell(code):
    return {
        "cell_type": "code",
        "execution_count": 1,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in code.strip().split("\n")]
    }


def generate_all_notebooks():
    nb_dir = Path("notebooks")
    nb_dir.mkdir(exist_ok=True)

    # 1. Dataset Collection and EDA
    nb1_cells = [
        md_cell("""# Notebook 01: Dataset Collection & Exploratory Data Analysis (EDA)
### Project: AspectSense AI - Multi-Aspect Customer Feedback Intelligence
**Author:** Raj Keshav | **Track:** NLP & LLM Capstone 2026

This notebook covers:
1. Multi-domain benchmark customer review acquisition and structure.
2. Distribution of reviews across product categories (Smartphones, SaaS, Laptops, Hospitality, Audio).
3. Sentiment and star rating correlations.
4. Review length analysis and vocabulary sparsity."""),
        code_cell("""import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure paths
sys.path.insert(0, os.path.abspath(".."))
DATA_PATH = "../resources/data/customer_reviews_benchmark.csv"

df = pd.read_csv(DATA_PATH)
print(f"Dataset shape: {df.shape}")
df.head()"""),
        md_cell("### 1.1 Category Distribution"),
        code_cell("""print("Domain counts:")
print(df["domain"].value_counts())

plt.figure(figsize=(8, 4))
sns.countplot(data=df, x="domain", palette="viridis")
plt.title("Review Distribution Across Product Domains")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()"""),
        md_cell("### 1.2 Sentiment Breakdown and Review Lengths"),
        code_cell("""df["char_length"] = df["review_text"].apply(len)
df["word_count"] = df["review_text"].apply(lambda x: len(x.split()))

print(df.groupby("overall_sentiment")[["word_count", "rating"]].mean())

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
sns.histplot(df["word_count"], kde=True, color="purple")
plt.title("Review Word Count Distribution")

plt.subplot(1, 2, 2)
sns.countplot(data=df, x="overall_sentiment", palette="Set2")
plt.title("Overall Sentiment Counts")
plt.tight_layout()
plt.show()""")
    ]

    with open(nb_dir / "01_dataset_collection_and_eda.ipynb", "w", encoding="utf-8") as f:
        json.dump(make_notebook(nb1_cells), f, indent=2)

    # 2. NLP Preprocessing and Aspect Extraction
    nb2_cells = [
        md_cell("""# Notebook 02: NLP Preprocessing & Aspect Extraction
### Project: AspectSense AI
**Author:** Raj Keshav | **Track:** NLP & LLM Capstone 2026

This notebook walks through:
1. Normalization, contraction expansion, and HTML/URL cleaning.
2. Contrastive clause segmentation using syntactic markers (`but`, `however`, `although`).
3. Negation tagging.
4. Aspect candidate extraction via compound noun matching and domain ontology lookup."""),
        code_cell("""import sys
import os
sys.path.insert(0, os.path.abspath(".."))

from code.core.preprocessor import TextPreprocessor
from code.core.aspect_extractor import AspectExtractor

preprocessor = TextPreprocessor()
extractor = AspectExtractor("../resources/data/aspect_lexicon.json")

sample = "The OLED screen is absolutely gorgeous, but the battery life barely lasts five hours!"
cleaned = preprocessor.clean_text(sample)
clauses = preprocessor.segment_into_clauses(sample)

print("Original:", sample)
print("Cleaned :", cleaned)
print("Clauses :", clauses)"""),
        md_cell("### 2.2 Aspect Extraction & Clause Mapping"),
        code_cell("""extracted = extractor.extract_aspects(cleaned)
print(f"Aspect count: {extracted['aspect_count']}")
for mention in extracted["aspect_mentions"]:
    print(f"Term: {mention['term']} | Category: {mention['canonical_aspect']} | Clause: '{mention['clause']}'")""")
    ]

    with open(nb_dir / "02_nlp_preprocessing_and_aspect_extraction.ipynb", "w", encoding="utf-8") as f:
        json.dump(make_notebook(nb2_cells), f, indent=2)

    # 3. ABSA Model Training and Evaluation
    nb3_cells = [
        md_cell("""# Notebook 03: ABSA Model Evaluation & Benchmarking
### Project: AspectSense AI
**Author:** Raj Keshav | **Track:** NLP & LLM Capstone 2026

This notebook covers:
1. Aspect-level polarity scoring with hyperbolic tangent normalization.
2. Emotion classification and urgency triage.
3. Confusion matrix, Precision, Recall, and Macro F1 evaluation across the benchmark set."""),
        code_cell("""import sys
import os
import pandas as pd
sys.path.insert(0, os.path.abspath(".."))

from code.core.pipeline import AspectSensePipeline
from code.utils.metrics import calculate_classification_metrics

pipeline = AspectSensePipeline()
df = pd.read_csv("../resources/data/customer_reviews_benchmark.csv")

y_true = []
y_pred = []

for _, row in df.iterrows():
    res = pipeline.analyze_review(row["review_text"], domain=row["domain"], include_llm_diagnostics=False)
    y_true.append(row["overall_sentiment"].strip().lower())
    y_pred.append(res["overall_assessment"]["sentiment"].strip().lower())

metrics = calculate_classification_metrics(y_true, y_pred)
print("Accuracy   :", metrics["accuracy"])
print("Macro F1   :", metrics["macro_f1"])
print("Weighted F1:", metrics["weighted_f1"])"""),
        md_cell("### 3.2 Confusion Matrix Heatmap"),
        code_cell("""import matplotlib.pyplot as plt
import numpy as np

classes = metrics["classes"]
matrix = np.zeros((len(classes), len(classes)))
for i, c1 in enumerate(classes):
    for j, c2 in enumerate(classes):
        matrix[i, j] = metrics["confusion_matrix"][c1].get(c2, 0)

plt.figure(figsize=(6, 5))
plt.imshow(matrix, cmap="Blues")
plt.colorbar()
plt.xticks(range(len(classes)), classes)
plt.yticks(range(len(classes)), classes)
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("ABSA Sentiment Confusion Matrix")
plt.show()""")
    ]

    with open(nb_dir / "03_absa_model_training_and_evaluation.ipynb", "w", encoding="utf-8") as f:
        json.dump(make_notebook(nb3_cells), f, indent=2)

    # 4. LLM Gemini Integration and Diagnostics
    nb4_cells = [
        md_cell("""# Notebook 04: Gemini LLM Integration & Root-Cause Diagnostics
### Project: AspectSense AI
**Author:** Raj Keshav | **Track:** NLP & LLM Capstone 2026

This notebook demonstrates:
1. Google Gemini 3.8 Flash LLM integration (`google-genai` SDK).
2. Structured JSON generation for root-cause diagnosis.
3. Actionable strategic recommendations for product engineering.
4. Automated empathetic customer support email drafting.
5. Graceful offline heuristic fallback execution."""),
        code_cell("""import sys
import os
sys.path.insert(0, os.path.abspath(".."))

from code.core.pipeline import AspectSensePipeline

pipeline = AspectSensePipeline()
print(f"Live Gemini Connected: {pipeline.llm_service.is_live_connected()}")
print(f"Target Model: {pipeline.llm_service.model_name}")"""),
        md_cell("### 4.2 End-to-End LLM Root Cause Diagnosis"),
        code_cell("""sample_review = "The OLED screen is gorgeous, but the phone overheats during 4K video recording and customer service was dismissive."
result = pipeline.analyze_review(sample_review, domain="Smartphones", include_llm_diagnostics=True)

print("=== PIPELINE OUTPUT ===")
print("Overall Sentiment:", result["overall_assessment"]["sentiment"])
print("Triage Urgency   :", result["overall_assessment"]["urgency_level"])
print("\\n=== GEMINI LLM SYNTHESIS ===")
llm_out = result["llm_diagnostics"]
print("Root Cause :", llm_out.get("root_cause_summary"))
print("Severity   :", llm_out.get("impact_severity"))
print("\\nRecommendations:")
for r in llm_out.get("actionable_recommendations", []):
    print("  •", r)

print("\\nDrafted Response:")
print(llm_out.get("draft_customer_response"))""")
    ]

    with open(nb_dir / "04_llm_gemini_integration_and_diagnostics.ipynb", "w", encoding="utf-8") as f:
        json.dump(make_notebook(nb4_cells), f, indent=2)

    print("Successfully generated all 4 Jupyter Notebooks in notebooks/")


if __name__ == "__main__":
    generate_all_notebooks()
