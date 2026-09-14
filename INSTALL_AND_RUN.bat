@echo off
REM Complete setup and run script for Early Warnings Dashboard

echo.
echo =====================================================
echo Early Warnings Dashboard - Complete Setup & Run
echo =====================================================
echo.
echo This script will:
echo  1. Check Python installation
echo  2. Verify CSV data files
echo  3. Install Flask, Pandas, CORS
echo  4. Start the dashboard
echo.
echo =====================================================
echo.

cd /d "%~dp0"

python SETUP_AND_RUN.py

if errorlevel 1 (
    echo.
    echo =====================================================
    echo SETUP FAILED - Check the errors above
    echo =====================================================
    echo.
    pause
)
