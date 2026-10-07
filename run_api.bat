@echo off
title AspectSense AI - FastAPI REST Server
echo ========================================================
echo   Launching AspectSense AI FastAPI REST Server
echo   Docs: http://localhost:8000/docs
echo ========================================================
cd /d "%~dp0"
.\.venv\Scripts\uvicorn.exe code.api.app:app --host 0.0.0.0 --port 8000 --reload
pause
