# Assignment 3: Fine-Grained Aspect Extraction & Mapping

## 🎯 Objective
Extract explicit and implicit aspect entity targets from multi-sentence feedback using:
1. Syntactic compound noun collocation patterns (e.g., *"battery life"*, *"fan noise"*, *"screen resolution"*).
2. Domain ontology graph traversal (`aspect_lexicon.json`).
3. Local clause context attribution for targeted sentiment polarity mapping.

---

## 📚 Methodology
Aspect extraction identifies what product feature or service touchpoint is being discussed. Rather than naive single-word matching, we utilize:
- Ordered N-gram search (preferring longer multi-word expressions like *"noise cancellation"* over isolated *"noise"*).
- Canonical ontology normalization (mapping *"OLED"*, *"AMOLED"*, *"retina"* $\to$ `screen_display`).
- Boundary span tracking to avoid duplicate or overlapping matches.

---

## 🛠️ Execution
Run `python solution.py` to extract aspects from compound reviews.
