# Troubleshooting Guide

## Issue: "ERR_CONNECTION_REFUSED" when accessing http://localhost:5000

### Quick Fixes (try in order)

#### Fix #1: Run the diagnostic tool
```bash
DIAGNOSE.bat
```
This checks:
- ✓ Python is installed
- ✓ All CSV files exist
- ✓ Flask is installed
- ✓ Port 5000 is available

#### Fix #2: Use the simplified starter script
```bash
START.bat
```
This is simpler than RUN_DASHBOARD.bat and handles most issues.

#### Fix #3: Check if Flask is running
Open a NEW command prompt and type:
```bash
netstat -ano | findstr :5000
```
- If you see a result, port 5000 is in use
- If nothing shows, Flask isn't running

#### Fix #4: Verify CSV files are in correct location
```bash
dir /b *.csv
```
You should see:
- circana_1000_rows_dummy.csv
- competitive_deo_us.csv
- ecommerce_deo_us.csv
- social_voice_deo_us.csv
- macro_context_deo_us.csv

If any are missing, the dashboard won't work.

---

## Detailed Troubleshooting

### Scenario 1: "Port 5000 in use"

**Symptoms:** Dashboard won't start, says port 5000 in use

**Solution:**
```bash
REM Find process using port 5000
netstat -ano | findstr :5000

REM You'll see output like:
REM   TCP    127.0.0.1:5000         0.0.0.0:0              LISTENING    12345

REM Kill the process (replace 12345 with actual PID)
taskkill /PID 12345 /F

REM Or change Flask to use a different port
REM Edit backend/app.py, change: app.run(debug=False, port=5000, ...)
REM To: app.run(debug=False, port=5001, ...)
REM Then access http://localhost:5001
```

### Scenario 2: "CSV files not found"

**Symptoms:** Error says "CSV file not found" when you start Flask

**Solution:**
```bash
REM Check you're in the right directory
cd D:\LangGraph\EarlyWarning_OPFIN

REM Verify files exist
dir *.csv

REM All 5 should appear. If not:
REM 1. Check file names exactly (case-sensitive on some systems)
REM 2. Make sure files aren't in a subfolder
REM 3. Files should be in root directory, not in \backend
```

### Scenario 3: "ModuleNotFoundError: No module named 'flask'"

**Symptoms:** Error says Flask, pandas, or flask_cors not installed

**Solution:**
```bash
REM Install dependencies manually
pip install flask flask-cors pandas

REM Or use the requirements file
pip install -r backend/requirements.txt
```

### Scenario 4: "Python not found"

**Symptoms:** Says "python: command not found" or similar

**Solution:**
1. Download Python from https://www.python.org/downloads/
2. During installation, **CHECK** "Add Python to PATH"
3. Restart command prompt after installing
4. Verify: `python --version`

### Scenario 5: Browser shows blank page or "Cannot GET /"

**Symptoms:** Flask running but page is blank

**Solution:**
1. Check Flask console for errors
2. Open browser's developer tools (F12)
3. Check Console tab for JavaScript errors
4. Try different browser (Chrome, Firefox, Edge)
5. Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)

---

## Manual Start (if scripts don't work)

**Step 1: Open Command Prompt**
```
Press Windows+R, type "cmd", press Enter
```

**Step 2: Navigate to project folder**
```bash
cd D:\LangGraph\EarlyWarning_OPFIN
```

**Step 3: Install dependencies**
```bash
pip install flask flask-cors pandas
```

**Step 4: Start Flask**
```bash
cd backend
python app.py
```

**Step 5: Open browser**
```
http://localhost:5000
```

---

## What You Should See

### When Flask starts correctly:
```
============================================================
Early Warnings Dashboard - Phase 2 Backend
============================================================
Backend directory: D:\LangGraph\EarlyWarning_OPFIN\backend
Data directory: D:\LangGraph\EarlyWarning_OPFIN
Database path: D:\LangGraph\EarlyWarning_OPFIN\dashboard.db

Loading data files from: D:\LangGraph\EarlyWarning_OPFIN
✓ circana_1000_rows_dummy.csv: 1000 rows
✓ competitive_deo_us.csv: 110 rows
✓ ecommerce_deo_us.csv: 505 rows
✓ social_voice_deo_us.csv: 300 rows
✓ macro_context_deo_us.csv: 100 rows

============================================================
INITIALIZING DASHBOARD
============================================================

[1/3] Loading data files...
✓ All data files loaded successfully!

[2/3] Initializing database...
✓ Database initialized

[3/3] Starting Flask server...

============================================================
✓ DASHBOARD READY!
============================================================

📊 Open your browser and go to:
   http://localhost:5000

Press CTRL+C to stop the server
============================================================
```

### When you access http://localhost:5000:
- Header: "Early Warnings Dashboard - Phase 2"
- Left panel: List of signals (Competitive Price War, Format Crisis, Gel Opportunity)
- Right panel: "Click a signal to see supporting data"
- Click any signal → see evidence

---

## Common Error Messages

### Error: "FileNotFoundError: [Errno 2] No such file or directory: 'circana_1000_rows_dummy.csv'"

**Cause:** CSV files not found in the data directory

**Fix:**
```bash
REM List files in current directory
dir

REM Make sure you see all 5 CSV files
REM If missing, they may be in a different folder
REM Move them to: D:\LangGraph\EarlyWarning_OPFIN\
```

### Error: "Address already in use"

**Cause:** Another process is using port 5000

**Fix:**
```bash
REM Find what's using port 5000
netstat -ano | findstr :5000

REM Kill it (replace PID number)
taskkill /PID 1234 /F
```

### Error: "No module named 'flask'"

**Cause:** Flask not installed in your Python environment

**Fix:**
```bash
pip install flask
pip install flask-cors
pip install pandas
```

### Error: "Connection refused" when accessing http://localhost:5000

**Cause:** Flask server is not running

**Fix:**
1. Check command prompt window - is Flask running?
2. Look for error messages in the console
3. Try running START.bat instead
4. Try manual steps above

---

## Browser Access

### Works:
- http://localhost:5000
- http://127.0.0.1:5000
- http://[your-computer-name]:5000

### Doesn't work:
- http://0.0.0.0:5000 (use 127.0.0.1 instead)
- https://localhost:5000 (not HTTPS, just HTTP)

---

## Still Having Issues?

1. **Run the diagnostic:**
   ```bash
   DIAGNOSE.bat
   ```

2. **Check the Flask console** for actual error messages (not just connection refused)

3. **Verify file locations:**
   ```bash
   cd D:\LangGraph\EarlyWarning_OPFIN
   dir *.csv
   ```

4. **Try manual startup** (Step-by-step above)

5. **Check Windows Defender/Antivirus** - may be blocking port 5000

---

## Getting Help

If the above doesn't work:

1. **Save the error message** from the Flask console
2. **Check Flask is actually running** (should show "Running on http://localhost:5000")
3. **Verify all CSV files exist** with: `dir *.csv`
4. **Try a different port** if 5000 is blocked
5. **Restart your computer** (sometimes fixes port conflicts)

Most common cause: **CSV files are in wrong location or Flask isn't actually running.**

Run `DIAGNOSE.bat` first - it will tell you exactly what's wrong.
