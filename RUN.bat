@echo off
echo.
echo =========================================================
echo Early Warnings Dashboard - Simple Launcher
echo =========================================================
echo.

cd /d "%~dp0"

REM Try to run with Python directly
python run.py

if errorlevel 1 (
    echo.
    echo ERROR: Failed to start dashboard
    echo.
    echo Troubleshooting:
    echo 1. Make sure Python is installed
    echo 2. Run: pip install flask flask-cors pandas
    echo 3. Check data/*.csv files exist in this folder
    echo.
    pause
)
