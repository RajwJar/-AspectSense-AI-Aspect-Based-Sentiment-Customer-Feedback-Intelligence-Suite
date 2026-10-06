---
name: "Task: Deployment, Interactive UI & REST API Service"
about: "Build and deploy the interactive Streamlit dashboard, FastAPI web service, and Docker containerization."
title: "[DEPLOY] Interactive Streamlit Dashboard & FastAPI Deployment"
labels: ["deployment", "fastapi", "streamlit", "docker", "phase-5"]
assignees: ["rajkeshav2324"]
---

### Objective
Deploy user-facing interfaces for real-time aspect analysis, batch CSV processing, interactive sentiment visualizers, and enterprise REST API endpoints.

### Key Deliverables
- [ ] Build interactive web dashboard (`code/web/dashboard.py`) with multi-aspect visualizer, live demo, and Gemini diagnostics.
- [ ] Implement production REST API (`code/api/app.py`) with OpenAPI/Swagger docs at `/docs`.
- [ ] Create `Dockerfile` and `docker-compose.yml` for reproducible container deployment.
- [ ] Author `docs/installation_guide.md` with local, venv, and Docker setup instructions.
- [ ] Capture application screenshots in `resources/screenshots/`.

### Definition of Done
- Dashboard launches cleanly and allows interactive review analysis.
- FastAPI passes health checks and returns JSON payloads.
- Deployment instructions verified on local machine.
