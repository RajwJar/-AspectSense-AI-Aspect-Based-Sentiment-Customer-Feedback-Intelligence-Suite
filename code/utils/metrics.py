"""
Metrics and Evaluation Engine for AspectSense AI
Computes Classification Metrics (Accuracy, Precision, Recall, F1),
Confusion Matrix, and Aspect Extraction IoU / Term Matching metrics.
"""

from typing import List, Dict, Any, Tuple
from collections import defaultdict


def calculate_classification_metrics(y_true: List[str], y_pred: List[str]) -> Dict[str, Any]:
    """
    Computes Accuracy, Precision, Recall, and F1-score per class
    as well as Macro/Weighted averages without strictly requiring sklearn.
    """
    classes = sorted(list(set(y_true + y_pred)))
    tp = defaultdict(int)
    fp = defaultdict(int)
    fn = defaultdict(int)
    support = defaultdict(int)

    for true_lbl, pred_lbl in zip(y_true, y_pred):
        support[true_lbl] += 1
        if true_lbl == pred_lbl:
            tp[true_lbl] += 1
        else:
            fp[pred_lbl] += 1
            fn[true_lbl] += 1

    per_class = {}
    macro_p, macro_r, macro_f1 = 0.0, 0.0, 0.0
    weighted_f1 = 0.0
    total_samples = len(y_true)
    correct_samples = sum(tp.values())

    for cls in classes:
        p = tp[cls] / (tp[cls] + fp[cls]) if (tp[cls] + fp[cls]) > 0 else 0.0
        r = tp[cls] / (tp[cls] + fn[cls]) if (tp[cls] + fn[cls]) > 0 else 0.0
        f1 = (2 * p * r) / (p + r) if (p + r) > 0 else 0.0

        per_class[cls] = {
            "precision": round(p, 4),
            "recall": round(r, 4),
            "f1_score": round(f1, 4),
            "support": support[cls]
        }
        macro_p += p
        macro_r += r
        macro_f1 += f1
        weighted_f1 += f1 * support[cls]

    n_classes = len(classes) if classes else 1
    accuracy = correct_samples / total_samples if total_samples > 0 else 0.0

    # Build confusion matrix
    conf_matrix = {c_true: {c_pred: 0 for c_pred in classes} for c_true in classes}
    for true_lbl, pred_lbl in zip(y_true, y_pred):
        conf_matrix[true_lbl][pred_lbl] += 1

    return {
        "accuracy": round(accuracy, 4),
        "macro_precision": round(macro_p / n_classes, 4),
        "macro_recall": round(macro_r / n_classes, 4),
        "macro_f1": round(macro_f1 / n_classes, 4),
        "weighted_f1": round(weighted_f1 / total_samples, 4) if total_samples > 0 else 0.0,
        "classes": classes,
        "per_class": per_class,
        "confusion_matrix": conf_matrix,
        "total_samples": total_samples
    }


def evaluate_aspect_extraction(true_aspects_list: List[List[str]], pred_aspects_list: List[List[str]]) -> Dict[str, float]:
    """
    Computes Precision, Recall, and F1 for multi-aspect entity identification.
    """
    total_true = 0
    total_pred = 0
    total_correct = 0

    for true_set, pred_set in zip(true_aspects_list, pred_aspects_list):
        t_normalized = set(t.strip().lower() for t in true_set if t.strip())
        p_normalized = set(p.strip().lower() for p in pred_set if p.strip())

        total_true += len(t_normalized)
        total_pred += len(p_normalized)

        # Count partial / fuzzy matches
        matched = 0
        for p in p_normalized:
            for t in t_normalized:
                if p in t or t in p:
                    matched += 1
                    break
        total_correct += matched

    precision = total_correct / total_pred if total_pred > 0 else 0.0
    recall = total_correct / total_true if total_true > 0 else 0.0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0

    return {
        "aspect_precision": round(precision, 4),
        "aspect_recall": round(recall, 4),
        "aspect_f1": round(f1, 4),
        "true_entities_count": total_true,
        "pred_entities_count": total_pred
    }
