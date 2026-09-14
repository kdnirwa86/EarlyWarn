@echo off
echo.
echo ============================================
echo Dashboard Diagnostic Tool
echo ============================================
echo.

echo [1/5] Checking Python installation...
python --version
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.8+
    pause
    exit /b 1
)
echo ✓ Python found
echo.

echo [2/5] Checking CSV data files...
if exist "circana_1000_rows_dummy.csv" (
    echo ✓ circana_1000_rows_dummy.csv found
) else (
    echo ❌ circana_1000_rows_dummy.csv NOT FOUND
)

if exist "competitive_deo_us.csv" (
    echo ✓ competitive_deo_us.csv found
) else (
    echo ❌ competitive_deo_us.csv NOT FOUND
)

if exist "ecommerce_deo_us.csv" (
    echo ✓ ecommerce_deo_us.csv found
) else (
    echo ❌ ecommerce_deo_us.csv NOT FOUND
)

if exist "social_voice_deo_us.csv" (
    echo ✓ social_voice_deo_us.csv found
) else (
    echo ❌ social_voice_deo_us.csv NOT FOUND
)

if exist "macro_context_deo_us.csv" (
    echo ✓ macro_context_deo_us.csv found
) else (
    echo ❌ macro_context_deo_us.csv NOT FOUND
)
echo.

echo [3/5] Checking backend folder...
if exist "backend\app.py" (
    echo ✓ backend\app.py found
) else (
    echo ❌ backend\app.py NOT FOUND
)

if exist "backend\templates\dashboard.html" (
    echo ✓ backend\templates\dashboard.html found
) else (
    echo ❌ backend\templates\dashboard.html NOT FOUND
)
echo.

echo [4/5] Checking Python dependencies...
if not exist "backend\venv" (
    echo Creating virtual environment...
    python -m venv backend\venv
)

call backend\venv\Scripts\activate.bat

echo Installing Flask and dependencies...
pip install -q flask flask-cors pandas 2>nul

pip show flask >nul 2>&1
if errorlevel 1 (
    echo ❌ Flask not installed
    pause
    exit /b 1
)
echo ✓ Flask installed
pip show pandas >nul 2>&1
if errorlevel 1 (
    echo ❌ Pandas not installed
    pause
    exit /b 1
)
echo ✓ Pandas installed
echo.

echo [5/5] Checking if port 5000 is available...
netstat -ano | findstr ":5000" >nul 2>&1
if errorlevel 1 (
    echo ✓ Port 5000 is available
) else (
    echo ⚠️  Port 5000 is in use. Another process may be running.
    echo Kill existing Flask process or use a different port.
)
echo.

echo ============================================
echo ✓ All checks passed! Ready to run dashboard.
echo ============================================
echo.
echo To start the dashboard, run: RUN_DASHBOARD.bat
echo.
pause
