# AspectSense AI - Comprehensive Installation & Deployment Guide

This guide provides step-by-step instructions for installing, configuring, testing, and running **AspectSense AI** on local machines (Windows, macOS, Linux) and via Docker.

---

## 📋 System Prerequisites
- **Python:** 3.10, 3.11, or 3.12 (Recommended: Python 3.12)
- **Git:** 2.30+ installed
- **Operating System:** Windows 10/11, Ubuntu 20.04+, or macOS
- **Optional:** Google Gemini API Key (Get free key from [Google AI Studio](https://aistudio.google.com/))
  *Note: AspectSense AI runs completely offline with simulated heuristic LLM mode if no API key is provided!*

---

## 🛠️ Option 1: Standard Python Setup (Recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/RajwJar/-AspectSense-AI-Aspect-Based-Sentiment-Customer-Feedback-Intelligence-Suite.git
cd -AspectSense-AI-Aspect-Based-Sentiment-Customer-Feedback-Intelligence-Suite
```

### Step 2: Create and Activate Virtual Environment
**On Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**On Linux / macOS (Bash):**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables (Optional)
Create a `.env` file in the project root:
```env
# Optional: Provide Google Gemini API Key for live AI calls
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-3.8-flash

# Optional: Server Port Configuration
API_PORT=8000
DASHBOARD_PORT=8501
```

---

## 🧪 Step 5: Verify Installation with Pytest
Run the test suite to verify all modules and endpoints:
```bash
pytest code/tests/ -v
```
*Expected Result: 21 passed tests in < 2 seconds.*

---

## 🚀 Step 6: Running the Applications

### 1. Launch the Interactive Streamlit Web Dashboard
```bash
streamlit run code/web/dashboard.py
```
Open your browser at: **`http://localhost:8501`**

### 2. Launch the FastAPI REST Service
```bash
uvicorn code.api.app:app --host 0.0.0.0 --port 8000 --reload
```
- API Base URL: **`http://localhost:8000`**
- Interactive Swagger / OpenAPI Documentation: **`http://localhost:8000/docs`**
- Alternative ReDoc Documentation: **`http://localhost:8000/redoc`**

### 3. Run Pipeline CLI Sanity Check
```bash
python -m code.core.pipeline --sanity-check
```

---

## 🐳 Option 2: Docker Container Deployment

### Build and Run with Docker Compose
```bash
docker compose up --build
```
- Streamlit Dashboard: `http://localhost:8501`
- FastAPI Documentation: `http://localhost:8000/docs`

### Build and Run Standalone Docker Container
```bash
docker build -t aspectsense-ai .
docker run -p 8501:8501 -p 8000:8000 -e GEMINI_API_KEY="" aspectsense-ai
```

---

## 🔧 Troubleshooting & FAQ

1. **`ValueError: numpy.dtype size changed` on system Python:**
   - Solution: Use a dedicated virtual environment (`.venv`) as detailed in Step 2.
2. **What if I don't have a Gemini API key?**
   - AspectSense AI automatically detects missing keys and activates the offline heuristic reasoning engine without crashing or throwing errors.
3. **PowerShell script execution disabled:**
   - Run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in PowerShell.
