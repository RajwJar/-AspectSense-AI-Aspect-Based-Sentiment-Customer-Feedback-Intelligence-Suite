@echo off
title AspectSense AI - Streamlit Dashboard
echo ========================================================
echo   Launching AspectSense AI Interactive Dashboard
echo   Author: Keshav Raj (23FE10CDS00476)
echo ========================================================
cd /d "%~dp0"
.\.venv\Scripts\streamlit.exe run code/web/dashboard.py
pause
