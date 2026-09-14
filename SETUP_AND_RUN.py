#!/usr/bin/env python
"""
Complete setup and run script for Early Warnings Dashboard
Installs all dependencies and starts the Flask server
"""

import os
import sys
import subprocess
import time

def print_header(text):
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70 + "\n")

def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"[*] {description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[✓] {description} - SUCCESS")
            return True
        else:
            print(f"[✗] {description} - FAILED")
            if result.stderr:
                print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"[✗] {description} - ERROR: {e}")
        return False

def main():
    print_header("EARLY WARNINGS DASHBOARD - COMPLETE SETUP")

    # Get current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.join(current_dir, 'backend')

    print(f"Project folder: {current_dir}\n")

    # Step 1: Check Python
    print("[Step 1/5] Checking Python Installation...")
    result = subprocess.run([sys.executable, '--version'], capture_output=True, text=True)
    print(f"  Python version: {result.stdout.strip()}")
    print("  [✓] Python found\n")

    # Step 2: Verify CSV files
    print("[Step 2/5] Verifying Data Files...")
    csv_files = [
        'circana_1000_rows_dummy.csv',
        'competitive_deo_us.csv',
        'ecommerce_deo_us.csv',
        'social_voice_deo_us.csv',
        'macro_context_deo_us.csv'
    ]

    missing_files = []
    for csv_file in csv_files:
        path = os.path.join(current_dir, csv_file)
        if os.path.exists(path):
            print(f"  [✓] {csv_file}")
        else:
            print(f"  [✗] {csv_file} - NOT FOUND")
            missing_files.append(csv_file)

    if missing_files:
        print(f"\n[✗] ERROR: Missing {len(missing_files)} CSV files!")
        print(f"Expected location: {current_dir}")
        print(f"Missing files: {', '.join(missing_files)}\n")
        input("Press Enter to exit...")
        sys.exit(1)

    print("  [✓] All data files found\n")

    # Step 3: Install dependencies
    print("[Step 3/5] Installing Python Dependencies...")

    packages = ['flask', 'flask-cors', 'pandas']
    for package in packages:
        print(f"  Installing {package}...")
        cmd = f"{sys.executable} -m pip install -q {package}"
        result = subprocess.run(cmd, shell=True, capture_output=True)
        if result.returncode == 0:
            print(f"  [✓] {package} installed")
        else:
            print(f"  [✗] {package} - trying again...")
            subprocess.run(f"{sys.executable} -m pip install {package}", shell=True)

    print()

    # Step 4: Verify imports
    print("[Step 4/5] Verifying Imports...")
    try:
        import flask
        print("  [✓] Flask import successful")
    except ImportError as e:
        print(f"  [✗] Flask import failed: {e}")
        sys.exit(1)

    try:
        import pandas
        print("  [✓] Pandas import successful")
    except ImportError as e:
        print(f"  [✗] Pandas import failed: {e}")
        sys.exit(1)

    print()

    # Step 5: Run Flask
    print("[Step 5/5] Starting Flask Server...")
    print("\n" + "="*70)
    print("  DASHBOARD STARTING - READ BELOW")
    print("="*70 + "\n")

    # Change to backend directory
    os.chdir(backend_dir)

    # Add backend to path
    sys.path.insert(0, backend_dir)

    # Import and run Flask app
    try:
        print("Importing Flask app...")
        from app import app

        print("\n" + "="*70)
        print("  ✓ DASHBOARD READY!")
        print("="*70)
        print("\n📊 Open your browser and go to:")
        print("   http://localhost:5000\n")
        print("⚠️  DO NOT CLOSE THIS WINDOW while using the dashboard")
        print("Press CTRL+C to stop the server\n")
        print("="*70 + "\n")

        # Start Flask
        app.run(debug=False, port=5000, host='127.0.0.1', use_reloader=False)

    except Exception as e:
        print(f"\n[✗] ERROR starting Flask: {e}\n")
        print("Troubleshooting steps:")
        print("1. Make sure all CSV files are in the main folder")
        print("2. Verify Flask is installed: pip install flask")
        print("3. Check if port 5000 is available")
        print("4. Try: netstat -ano | findstr :5000\n")
        input("Press Enter to exit...")
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[*] Dashboard stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n[✗] Unexpected error: {e}")
        input("Press Enter to exit...")
        sys.exit(1)
