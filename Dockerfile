FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose Streamlit (8501) and FastAPI (8000)
EXPOSE 8501 8000

# Set environment
ENV PYTHONUNBUFFERED=1

# Start entrypoint script
CMD ["sh", "-c", "uvicorn code.api.app:app --host 0.0.0.0 --port 8000 & streamlit run code/web/dashboard.py --server.port 8501 --server.address 0.0.0.0"]
