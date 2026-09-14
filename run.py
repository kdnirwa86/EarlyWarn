#!/usr/bin/env python
"""
Simple launcher for Early Warnings Dashboard
Just run this with: python run.py
"""

import os
import sys
import subprocess

# Change to backend directory
backend_dir = os.path.join(os.path.dirname(__file__), 'backend')
os.chdir(backend_dir)

print("\n" + "="*60)
print("Early Warnings Dashboard Launcher")
print("="*60 + "\n")

# Check if Flask is installed
try:
    import flask
    print("✓ Flask found")
except ImportError:
    print("Installing Flask...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "flask", "flask-cors", "pandas"])
    print("✓ Flask installed")

# Run the app
print("\nStarting dashboard...\n")
sys.path.insert(0, backend_dir)

try:
    from app import app
    print("\n" + "="*60)
    print("✓ Dashboard started successfully!")
    print("="*60)
    print("\nOpen your browser: http://localhost:5000")
    print("Press CTRL+C to stop\n")
    app.run(debug=False, port=5000, host='127.0.0.1')
except Exception as e:
    print(f"\n✗ ERROR: {e}")
    print("\nTroubleshooting:")
    print("1. Make sure data/*.csv files exist")
    print("2. Check that you're in the right directory")
    print("3. Run: pip install flask flask-cors pandas")
    input("\nPress Enter to close...")
    sys.exit(1)
