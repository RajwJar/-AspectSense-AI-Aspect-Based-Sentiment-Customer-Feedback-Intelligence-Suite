"""
Configuration and constants for AspectSense AI
"""

import os
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
RESOURCES_DIR = BASE_DIR / "resources"
DATA_DIR = RESOURCES_DIR / "data"
RESULTS_DIR = RESOURCES_DIR / "results"
SCREENSHOTS_DIR = RESOURCES_DIR / "screenshots"

DEFAULT_BENCHMARK_DATASET = DATA_DIR / "customer_reviews_benchmark.csv"
DEFAULT_ASPECT_LEXICON = DATA_DIR / "aspect_lexicon.json"

# API & LLM Settings
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Server Ports
API_PORT = int(os.getenv("API_PORT", "8000"))
DASHBOARD_PORT = int(os.getenv("DASHBOARD_PORT", "8501"))

# Thresholds
POLARITY_POS_THRESHOLD = 0.15
POLARITY_NEG_THRESHOLD = -0.15
URGENCY_CRITICAL_THRESHOLD = -0.75
URGENCY_HIGH_THRESHOLD = -0.45
