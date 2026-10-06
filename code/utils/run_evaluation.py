"""
Evaluation Runner for AspectSense AI
Runs benchmark evaluation on customer_reviews_benchmark.csv,
computes metrics, and generates plots in resources/results/.
"""

import os
import sys
import json
import pandas as pd
from collections import defaultdict

# Add workspace root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from code.core.pipeline import AspectSensePipeline
from code.utils.config import DEFAULT_BENCHMARK_DATASET, RESULTS_DIR
from code.utils.metrics import calculate_classification_metrics, evaluate_aspect_extraction
from code.utils.visualizer import plot_confusion_matrix, plot_sentiment_distribution, plot_aspect_sentiments


def run_benchmark():
    print(f"Loading benchmark dataset from: {DEFAULT_BENCHMARK_DATASET}")
    df = pd.read_csv(DEFAULT_BENCHMARK_DATASET)
    print(f"Loaded {len(df)} benchmark reviews across {df['domain'].nunique()} domains.")

    pipeline = AspectSensePipeline()

    y_true = []
    y_pred = []
    aspect_true_list = []
    aspect_pred_list = []
    sentiments_list = []
    aspect_sentiment_counts = defaultdict(lambda: {"positive": 0, "negative": 0})

    for _, row in df.iterrows():
        review_text = row["review_text"]
        domain = row["domain"]
        true_sentiment = row["overall_sentiment"].strip().lower()
        true_aspects = [a.strip() for a in str(row["aspect_entities"]).split(";") if a.strip()]

        result = pipeline.analyze_review(review_text, domain=domain, include_llm_diagnostics=False)
        pred_sentiment = result["overall_assessment"]["sentiment"].strip().lower()

        extracted_aspect_terms = [a["aspect_term"] for a in result["aspect_analysis"]["aspects"]]

        y_true.append(true_sentiment)
        y_pred.append(pred_sentiment)
        aspect_true_list.append(true_aspects)
        aspect_pred_list.append(extracted_aspect_terms)
        sentiments_list.append(pred_sentiment)

        for a in result["aspect_analysis"]["aspects"]:
            canon = a["canonical_aspect"]
            pol = a["sentiment"]
            if pol in ["positive", "negative"]:
                aspect_sentiment_counts[canon][pol] += 1

    # Compute metrics
    sentiment_metrics = calculate_classification_metrics(y_true, y_pred)
    aspect_metrics = evaluate_aspect_extraction(aspect_true_list, aspect_pred_list)

    os.makedirs(RESULTS_DIR, exist_ok=True)

    # Generate plots
    plot_confusion_matrix(sentiment_metrics["confusion_matrix"], str(RESULTS_DIR / "confusion_matrix.png"))
    plot_sentiment_distribution(sentiments_list, str(RESULTS_DIR / "sentiment_distribution.png"))
    plot_aspect_sentiments(dict(aspect_sentiment_counts), str(RESULTS_DIR / "aspect_sentiment_heatmap.png"))

    # Save benchmark report JSON
    full_report = {
        "dataset_samples": len(df),
        "sentiment_classification": sentiment_metrics,
        "aspect_extraction": aspect_metrics
    }
    with open(RESULTS_DIR / "benchmark_report.json", "w", encoding="utf-8") as f:
        json.dump(full_report, f, indent=2)

    # Save Markdown report
    md_report = f"""# AspectSense AI - Benchmark Evaluation Report

## 1. Overall Sentiment Classification
- **Total Test Reviews:** {sentiment_metrics['total_samples']}
- **Overall Accuracy:** {sentiment_metrics['accuracy'] * 100:.2f}%
- **Macro Precision:** {sentiment_metrics['macro_precision']:.4f}
- **Macro Recall:** {sentiment_metrics['macro_recall']:.4f}
- **Macro F1-Score:** {sentiment_metrics['macro_f1']:.4f}
- **Weighted F1-Score:** {sentiment_metrics['weighted_f1']:.4f}

### Per-Class Performance
| Class | Precision | Recall | F1-Score | Support |
|---|---|---|---|---|
"""
    for cls, stats in sentiment_metrics["per_class"].items():
        md_report += f"| **{cls.upper()}** | {stats['precision']:.4f} | {stats['recall']:.4f} | {stats['f1_score']:.4f} | {stats['support']} |\n"

    md_report += f"""
## 2. Aspect Target Extraction Metrics
- **Aspect Precision:** {aspect_metrics['aspect_precision']:.4f}
- **Aspect Recall:** {aspect_metrics['aspect_recall']:.4f}
- **Aspect F1-Score:** {aspect_metrics['aspect_f1']:.4f}
- **Ground Truth Entities:** {aspect_metrics['true_entities_count']}
- **Predicted Entities:** {aspect_metrics['pred_entities_count']}

## 3. Visual Artifacts
- Confusion Matrix: `resources/results/confusion_matrix.png`
- Sentiment Distribution: `resources/results/sentiment_distribution.png`
- Aspect Sentiment Breakdown: `resources/results/aspect_sentiment_heatmap.png`
"""
    with open(RESULTS_DIR / "evaluation_metrics.md", "w", encoding="utf-8") as f:
        f.write(md_report)

    print("Benchmark evaluation completed successfully!")
    print(f"Accuracy: {sentiment_metrics['accuracy'] * 100:.2f}% | Macro F1: {sentiment_metrics['macro_f1']:.4f} | Aspect F1: {aspect_metrics['aspect_f1']:.4f}")


if __name__ == "__main__":
    run_benchmark()
