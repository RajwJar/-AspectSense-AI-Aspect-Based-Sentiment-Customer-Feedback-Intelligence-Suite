# Assignment 1: NLP Text Normalization, Contractions & Clause Segmentation

## 🎯 Objective
Understand and implement foundational NLP preprocessing pipelines specifically tailored for multi-aspect customer reviews, addressing:
1. Slang, contractions, and noisy web formatting.
2. Contrastive clause segmentation (separating conflicting clauses joined by *but*, *however*, *yet*).
3. Grammatical negation propagation (window-based negation tagging).

---

## 📚 Theoretical Background
In standard NLP sentiment tasks, simple bag-of-words tokenization fails on compound sentences such as:
> *"The screen is gorgeous, but the battery drains fast."*

Without clause segmentation, the positive polarity of *"gorgeous"* cancels out the negative polarity of *"drains"*, yielding an incorrect neutral classification. By segmenting on contrastive conjunctions, each clause can be evaluated in isolation.

---

## 🛠️ Code Structure
- Run `python solution.py` to test the preprocessing pipeline on custom and benchmark sample strings.
