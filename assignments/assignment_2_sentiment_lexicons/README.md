# Assignment 2: Sentiment Lexicons & Polarity Scoring

## 🎯 Objective
Implement lexicon-based sentiment polarity and subjectivity scoring with:
1. Continuous polarity normalization using hyperbolic tangent (`tanh`) scaling.
2. Intensifier propagation (e.g., *"extremely"*, *"absolutely"* multiplier).
3. Negation sign inversion with damping factors.
4. Discrete sentiment classification and emotional tone detection.

---

## 📚 Mathematical Formulation
The normalized sentiment polarity score $S(C)$ for a clause $C$ is computed as:

$$S(C) = \tanh\left( \frac{\sum_{i=1}^{N} w(t_i) \cdot \mu(t_{i-1}) \cdot \nu(t_i)}{3.0} \right)$$

Where:
- $w(t_i)$ is the lexicon base weight of token $t_i$
- $\mu(t_{i-1})$ is the intensifier multiplier of the preceding token
- $\nu(t_i) \in \{1.0, -0.85\}$ is the negation inversion coefficient
- $\tanh(\cdot)$ bounds the result within $[-1.0, +1.0]$

---

## 🛠️ Execution
Run `python solution.py` to observe sentiment score calculations on contrasting phrases.
