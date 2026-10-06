"""
Visualization Utility for AspectSense AI
Generates publication-quality charts: Confusion Matrix,
Sentiment Distribution, and Aspect Sentiment Heatmaps.
"""

import os
from typing import Dict, Any, List
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend
import matplotlib.pyplot as plt
import numpy as np


def plot_confusion_matrix(conf_matrix: Dict[str, Dict[str, int]], output_path: str):
    """Generates and saves styled Confusion Matrix heatmap."""
    classes = sorted(list(conf_matrix.keys()))
    matrix_data = np.zeros((len(classes), len(classes)))

    for i, c_true in enumerate(classes):
        for j, c_pred in enumerate(classes):
            matrix_data[i, j] = conf_matrix[c_true].get(c_pred, 0)

    fig, ax = plt.subplots(figsize=(6, 5), dpi=300)
    fig.patch.set_facecolor("#0f172a")
    ax.set_facecolor("#1e293b")

    im = ax.imshow(matrix_data, interpolation='nearest', cmap=plt.cm.Blues)
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.yaxis.set_tick_params(color='white')
    plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white')

    ax.set(
        xticks=np.arange(matrix_data.shape[1]),
        yticks=np.arange(matrix_data.shape[0]),
        xticklabels=classes,
        yticklabels=classes,
        title="AspectSense AI - Sentiment Confusion Matrix",
        ylabel="True Label",
        xlabel="Predicted Label"
    )

    ax.title.set_color("white")
    ax.yaxis.label.set_color("white")
    ax.xaxis.label.set_color("white")
    ax.tick_params(colors="white")

    # Loop over data dimensions and create text annotations
    thresh = matrix_data.max() / 2.0
    for i in range(matrix_data.shape[0]):
        for j in range(matrix_data.shape[1]):
            val = int(matrix_data[i, j])
            color = "white" if matrix_data[i, j] > thresh else "#cbd5e1"
            ax.text(j, i, format(val, 'd'),
                    ha="center", va="center",
                    color=color, fontweight="bold", fontsize=11)

    fig.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches="tight")
    plt.close()


def plot_sentiment_distribution(sentiments: List[str], output_path: str):
    """Plots clean distribution bar chart of overall sentiments."""
    counts = {}
    for s in sentiments:
        counts[s] = counts.get(s, 0) + 1

    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
    fig.patch.set_facecolor("#0f172a")
    ax.set_facecolor("#1e293b")

    labels = list(counts.keys())
    values = [counts[k] for k in labels]
    colors = ["#10b981" if "pos" in l else "#ef4444" if "neg" in l else "#f59e0b" for l in labels]

    bars = ax.bar(labels, values, color=colors, width=0.55, edgecolor="#334155", linewidth=1.2)

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, yval + 0.5, int(yval),
                ha='center', va='bottom', color='white', fontweight='bold')

    ax.set_title("Customer Feedback Sentiment Distribution", color="white", fontsize=13, pad=15)
    ax.set_xlabel("Sentiment Category", color="white", fontsize=11)
    ax.set_ylabel("Review Count", color="white", fontsize=11)
    ax.tick_params(colors="white")
    ax.grid(axis='y', linestyle='--', alpha=0.25, color="white")

    for spine in ax.spines.values():
        spine.set_color("#334155")

    fig.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches="tight")
    plt.close()


def plot_aspect_sentiments(aspect_summary: Dict[str, Dict[str, int]], output_path: str):
    """Plots aspect polarity breakdown (Positive vs Negative counts per aspect)."""
    aspects = list(aspect_summary.keys())
    pos_counts = [aspect_summary[a].get("positive", 0) for a in aspects]
    neg_counts = [aspect_summary[a].get("negative", 0) for a in aspects]

    x = np.arange(len(aspects))
    width = 0.38

    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    fig.patch.set_facecolor("#0f172a")
    ax.set_facecolor("#1e293b")

    ax.bar(x - width/2, pos_counts, width, label='Positive Mentions', color='#10b981')
    ax.bar(x + width/2, neg_counts, width, label='Negative Mentions', color='#ef4444')

    ax.set_title("Aspect-Level Sentiment Breakdown Across Categories", color="white", fontsize=13, pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(aspects, rotation=35, ha='right', color="white")
    ax.set_ylabel("Mention Count", color="white")
    ax.tick_params(colors="white")
    ax.legend(facecolor="#1e293b", edgecolor="#475569", labelcolor="white")
    ax.grid(axis='y', linestyle='--', alpha=0.2, color="white")

    for spine in ax.spines.values():
        spine.set_color("#334155")

    fig.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches="tight")
    plt.close()
