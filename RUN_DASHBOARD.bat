@echo off
echo ============================================
echo Early Warnings Dashboard - Phase 2
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from python.org
    pause
    exit /b 1
)

echo Python found. Checking dependencies...
echo.

REM Check if venv exists, if not create it
if not exist "backend\venv" (
    echo Creating virtual environment...
    python -m venv backend\venv
)

REM Activate venv
call backend\venv\Scripts\activate.bat

REM Install requirements
echo Installing dependencies...
pip install -q -r backend\requirements.txt

if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ============================================
echo Starting Dashboard...
echo ============================================
echo.
echo Dashboard will open at: http://localhost:5000
echo Press CTRL+C to stop the server
echo.

cd backend
python app.py
