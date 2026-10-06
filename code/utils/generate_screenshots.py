"""
Generates UI screenshots and visual architecture diagrams
for resources/screenshots/.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../resources/screenshots"))
os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_architecture_diagram():
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    fig.patch.set_facecolor("#0b0f19")
    ax.set_facecolor("#0b0f19")

    # Boxes
    boxes = [
        {"x": 0.05, "y": 0.45, "w": 0.16, "h": 0.22, "title": "Customer Review\n(Unstructured)", "color": "#1e293b", "border": "#38bdf8"},
        {"x": 0.26, "y": 0.45, "w": 0.18, "h": 0.22, "title": "Text Preprocessing\n• Contractions\n• Conjunctions\n• Negations", "color": "#1e293b", "border": "#818cf8"},
        {"x": 0.49, "y": 0.60, "w": 0.20, "h": 0.24, "title": "Aspect Extractor\n• Compound Nouns\n• Domain Ontology\n• Clause Attribution", "color": "#1e293b", "border": "#c084fc"},
        {"x": 0.49, "y": 0.25, "w": 0.20, "h": 0.24, "title": "Sentiment Analyzer\n• Tanh Polarity\n• Intensifiers\n• Emotion & Urgency", "color": "#1e293b", "border": "#34d399"},
        {"x": 0.74, "y": 0.40, "w": 0.22, "h": 0.30, "title": "Gemini 3.8 Flash\n• Root Cause Diagnosis\n• Product Actions\n• Support Draft", "color": "#1e293b", "border": "#f59e0b"},
    ]

    for b in boxes:
        rect = patches.FancyBboxPatch(
            (b["x"], b["y"]), b["w"], b["h"],
            boxstyle="round,pad=0.02,rounding_size=0.03",
            facecolor=b["color"], edgecolor=b["border"], linewidth=2
        )
        ax.add_patch(rect)
        ax.text(
            b["x"] + b["w"]/2, b["y"] + b["h"]/2, b["title"],
            ha="center", va="center", color="#f8fafc", fontsize=9.5, fontweight="bold", linespacing=1.3
        )

    # Arrows
    arrows = [
        ((0.21, 0.56), (0.26, 0.56)),
        ((0.44, 0.60), (0.49, 0.68)),
        ((0.44, 0.52), (0.49, 0.40)),
        ((0.69, 0.68), (0.74, 0.60)),
        ((0.69, 0.40), (0.74, 0.50)),
    ]

    for start, end in arrows:
        ax.annotate(
            "", xy=end, xytext=start,
            arrowprops=dict(arrowstyle="->", color="#94a3b8", lw=2)
        )

    ax.set_title("AspectSense AI - System Pipeline Architecture", color="#f8fafc", fontsize=15, pad=15, fontweight="bold")
    ax.set_xlim(0, 1)
    ax.set_ylim(0.15, 0.95)
    ax.axis("off")

    path = os.path.join(OUTPUT_DIR, "architecture_diagram.png")
    plt.savefig(path, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close()
    print(f"Saved: {path}")


def generate_dashboard_mockup():
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    fig.patch.set_facecolor("#0f172a")
    ax.set_facecolor("#1e293b")

    # Header bar
    rect_hdr = patches.Rectangle((0, 0.88), 1, 0.12, facecolor="#1e293b", edgecolor="#334155", linewidth=1)
    ax.add_patch(rect_hdr)
    ax.text(0.04, 0.93, "🔍 AspectSense AI Dashboard | Real-Time Sentiment & LLM Diagnostics", color="#38bdf8", fontsize=13, fontweight="bold")

    # Metrics row
    metrics = [
        {"x": 0.04, "label": "Overall Sentiment", "val": "MIXED", "c": "#f59e0b"},
        {"x": 0.28, "label": "Polarity Score", "val": "+0.15", "c": "#34d399"},
        {"x": 0.52, "label": "Dominant Emotion", "val": "Frustration", "c": "#f87171"},
        {"x": 0.76, "label": "Triage Urgency", "val": "High", "c": "#ef4444"},
    ]
    for m in metrics:
        card = patches.FancyBboxPatch((m["x"], 0.70), 0.20, 0.14, boxstyle="round,pad=0.01", facecolor="#0f172a", edgecolor="#334155")
        ax.add_patch(card)
        ax.text(m["x"] + 0.10, 0.79, m["label"], ha="center", color="#94a3b8", fontsize=8.5)
        ax.text(m["x"] + 0.10, 0.73, m["val"], ha="center", color=m["c"], fontsize=12, fontweight="bold")

    # Aspect Cards
    aspects = [
        {"x": 0.04, "term": "OLED Screen", "sent": "POSITIVE", "c": "#10b981", "quote": "\"screen is absolutely gorgeous\""},
        {"x": 0.36, "term": "Camera", "sent": "POSITIVE", "c": "#10b981", "quote": "\"takes stunning low-light shots\""},
        {"x": 0.68, "term": "Battery Life", "sent": "NEGATIVE", "c": "#ef4444", "quote": "\"barely lasts six hours\""},
    ]
    for a in aspects:
        card = patches.FancyBboxPatch((a["x"], 0.44), 0.28, 0.20, boxstyle="round,pad=0.01", facecolor="#0f172a", edgecolor="#334155")
        ax.add_patch(card)
        ax.text(a["x"] + 0.14, 0.58, a["sent"], ha="center", color=a["c"], fontsize=8.5, fontweight="bold")
        ax.text(a["x"] + 0.14, 0.52, a["term"], ha="center", color="#f8fafc", fontsize=11, fontweight="bold")
        ax.text(a["x"] + 0.14, 0.47, a["quote"], ha="center", color="#94a3b8", fontsize=7.5, style="italic")

    # LLM Box
    llm_box = patches.FancyBboxPatch((0.04, 0.08), 0.92, 0.30, boxstyle="round,pad=0.01", facecolor="#090d16", edgecolor="#818cf8", linewidth=1.5)
    ax.add_patch(llm_box)
    ax.text(0.06, 0.32, "🤖 Google Gemini 3.8 Flash LLM Diagnostics", color="#818cf8", fontsize=11, fontweight="bold")
    ax.text(0.06, 0.26, "Root Cause: Battery cathode chemistry & background app sync causes high standby drain.", color="#cbd5e1", fontsize=8.5)
    ax.text(0.06, 0.20, "Recommendations: • Issue power-profiling firmware update • Audit standby kernel wakelocks", color="#94a3b8", fontsize=8)
    ax.text(0.06, 0.12, "Draft Response: \"Thank you for your feedback! We are thrilled you love the display, but deeply apologize for the battery issue...\"", color="#38bdf8", fontsize=8, style="italic")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    path = os.path.join(OUTPUT_DIR, "dashboard_overview.png")
    plt.savefig(path, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close()
    print(f"Saved: {path}")


def generate_all_mockups():
    generate_architecture_diagram()
    generate_dashboard_mockup()


if __name__ == "__main__":
    generate_all_mockups()
