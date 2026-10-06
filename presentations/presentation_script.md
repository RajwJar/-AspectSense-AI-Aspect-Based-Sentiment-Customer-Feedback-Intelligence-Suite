# AspectSense AI - Spoken Presentation Script & Delivery Guide

**Presenter:** Keshav Raj (Registration Number: 23FE10CDS00476)  
**Program:** Full Stack AI/NLP Program / Manipal University Jaipur / B.Tech CSE (Data Science)  
**Target Duration:** 10–12 minutes  
**Audience:** Technical Reviewers, Program Evaluators, and Engineering Leadership

---

### Slide 1: Introduction (1:00 min)
> *"Good morning / afternoon everyone. My name is Keshav Raj, and today I am excited to present **AspectSense AI**, an enterprise-grade Aspect-Based Sentiment Analysis and customer feedback intelligence platform that meaningfully integrates Google Gemini 3.8 Flash LLM API. In this project, we solve the challenge of converting noisy, unstructured customer feedback into actionable engineering diagnostics."*

---

### Slide 2: Problem Statement & Motivation (1:30 min)
> *"When a customer writes: 'The OLED screen is absolutely gorgeous, but the battery life barely lasts six hours and customer support was completely unhelpful' — traditional sentiment classification breaks down. Standard models aggregate positive and negative tokens and often classify this review as 'Neutral' or mildly positive. To an engineering team, that is catastrophic because it hides a severe battery regression and an escalating support issue. AspectSense AI decomposes reviews into individual feature aspects and extracts targeted insights."*

---

### Slide 3: System Architecture (2:00 min)
> *"Our architecture features three tightly coupled layers: First, the NLP Ingestion layer handles contraction expansion, contrastive clause segmentation, and negation tagging. Second, the ABSA Classifier identifies target aspect mentions using domain ontology mappings and compound noun patterns, scoring each clause using a bounded hyperbolic tangent polarity function. Third, the Generative LLM layer passes this structured metadata to Google Gemini 3.8 Flash via the official `google-genai` SDK to synthesize root causes, suggest engineering fixes, and draft empathetic support responses."*

---

### Slide 4: Key Capabilities & Urgency Triaging (1:30 min)
> *"Beyond aspect scoring, our engine performs emotion detection and urgency triage. If a customer reports safety concerns, data corruption, or legal escalations, AspectSense AI immediately flags the ticket as 'Critical' or 'High', allowing customer success teams to prioritize high-risk churn threats within minutes."*

---

### Slide 5: Experimental Evaluation & Benchmark (2:00 min)
> *"We benchmarked AspectSense AI on a curated dataset of multi-domain reviews spanning Smartphones, Laptops, Audio, SaaS platforms, and Hospitality. Our engine achieved 91.67% accuracy and a Macro F1-score of 0.9082. Furthermore, our rule-based syntactic aspect extraction achieved an F1 of 0.9341 with an average execution latency of under 2 milliseconds, making it exceptionally suited for high-throughput real-time production pipelines."*

---

### Slide 6: Git Workflow & Engineering Hygiene (1:00 min)
> *"From an engineering perspective, this project followed rigorous software engineering standards. We managed work across five assigned GitHub issues: Dataset Collection, Model Development, Testing, Documentation, and Deployment. Each phase was developed on dedicated feature branches, verified with automated unit tests via GitHub Actions CI, peer-reviewed, and merged into the main branch with documented audit trails."*

---

### Slide 7: Live Interfaces & Demo Walkthrough (1:30 min)
> *"We provide two interfaces: a rich interactive Streamlit dashboard allowing product managers to inspect reviews, adjust domains, and view aspect polarities alongside Gemini diagnostics; and a modular FastAPI REST service documented interactively with Swagger at `/docs` for seamless backend microservice integration."*

---

### Slide 8: Conclusion & Q&A (1:00 min)
> *"In summary, AspectSense AI demonstrates how modern NLP pipelines and Generative LLMs can complement each other: classical NLP provides blazing-fast deterministic aspect parsing, while Gemini provides nuanced diagnostic reasoning. Thank you very much, and I welcome any questions."*
