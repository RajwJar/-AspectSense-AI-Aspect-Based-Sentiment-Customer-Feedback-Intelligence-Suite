# AspectSense AI - Benchmark Evaluation Report

## 1. Overall Sentiment Classification
- **Total Test Reviews:** 50
- **Overall Accuracy:** 68.00%
- **Macro Precision:** 0.6269
- **Macro Recall:** 0.5119
- **Macro F1-Score:** 0.5374
- **Weighted F1-Score:** 0.7160

### Per-Class Performance
| Class | Precision | Recall | F1-Score | Support |
|---|---|---|---|---|
| **MIXED** | 1.0000 | 0.4118 | 0.5833 | 17 |
| **NEGATIVE** | 0.6842 | 0.8125 | 0.7429 | 16 |
| **NEUTRAL** | 0.0000 | 0.0000 | 0.0000 | 0 |
| **POSITIVE** | 0.8235 | 0.8235 | 0.8235 | 17 |

## 2. Aspect Target Extraction Metrics
- **Aspect Precision:** 0.5556
- **Aspect Recall:** 0.4140
- **Aspect F1-Score:** 0.4745
- **Ground Truth Entities:** 157
- **Predicted Entities:** 117

## 3. Visual Artifacts
- Confusion Matrix: `resources/results/confusion_matrix.png`
- Sentiment Distribution: `resources/results/sentiment_distribution.png`
- Aspect Sentiment Breakdown: `resources/results/aspect_sentiment_heatmap.png`
