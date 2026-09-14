go and
@echo off
REM Simple starter script - runs Flask directly

echo.
echo Starting Early Warnings Dashboard...
echo.

REM Make sure we're in the right directory
cd /d "%~dp0"

REM Install Flask if not already installed
echo Checking dependencies...
pip install -q flask flask-cors pandas 2>nul

REM Run Flask
echo.
cd backend
python app.py
