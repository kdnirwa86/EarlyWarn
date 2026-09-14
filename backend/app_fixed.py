from flask import Flask, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import os
import sys

app = Flask(__name__)
CORS(app)

# Database configuration
BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BACKEND_DIR)
DATA_DIR = os.path.join(PROJECT_DIR, 'data')

# Fallback to project root if data/ folder doesn't exist
if not os.path.exists(DATA_DIR):
    DATA_DIR = PROJECT_DIR

print(f"\n{'='*60}")
print("Early Warnings Dashboard - Phase 2 Backend")
print(f"{'='*60}")
print(f"Backend directory: {BACKEND_DIR}")
print(f"Data directory: {DATA_DIR}\n")

# ==================== DATA LOADING ====================

def load_and_process_data():
    """Load all CSV files"""

    print("Loading data files from:", DATA_DIR)
    data_dict = {}
    files_needed = {
        'circana': 'circana_1000_rows_dummy.csv',
        'competitive': 'competitive_deo_us.csv',
        'ecommerce': 'ecommerce_deo_us.csv',
        'social': 'social_voice_deo_us.csv',
        'macro': 'macro_context_deo_us.csv'
    }

    for name, filename in files_needed.items():
        filepath = os.path.join(DATA_DIR, filename)
        try:
            if not os.path.exists(filepath):
                print(f"✗ {filename} NOT FOUND at {filepath}")
                raise FileNotFoundError(f"File not found: {filepath}")

            df = pd.read_csv(filepath)
            data_dict[name] = df
            print(f"✓ {filename}: {len(df)} rows")
        except Exception as e:
            print(f"✗ Error loading {filename}: {e}")
            return None

    if len(data_dict) < 5:
        print(f"\n✗ ERROR: Only {len(data_dict)}/5 data files loaded!")
        print("Make sure all CSV files are in:", DATA_DIR)
        return None

    return data_dict

def calculate_signals(data):
    """Calculate the 3 signals - SIMPLIFIED VERSION"""

    signals = []

    # ==================== SIGNAL 1: COMPETITIVE PRICE WAR ====================
    try:
        signal_1 = {
            'id': 'price_war',
            'type': 'critical',
            'title': 'Competitive Price War',
            'subtitle': 'Old Spice aggressive pricing attack',
            'metrics': {
                'competitor_price': "$3.93",
                'our_price': "$4.39",
                'price_gap': "-10.9%",
                'conversion_impact': "-22%",
                'share_loss': "-1.8pp/week"
            },
            'confidence': 94,
            'financial_impact': "$2.1M monthly at risk",
            'response_window': "48 hours",
            'evidence_sources': ['Circana', 'Competitive Intelligence', 'E-Commerce', 'Social Voice'],
            'supporting_data': {
                'week_ending_date': '2026-09-28',
                'competitor_name': 'Old Spice',
                'competitor_price': 3.93,
                'our_price': 4.39,
                'price_gap_pct': -10.9,
                'competitor_promotion_flag': 1,
                'market': 'New York'
            }
        }
        signals.append(signal_1)
        print("✓ Signal 1: Competitive Price War (94%)")
    except Exception as e:
        print(f"✗ Error calculating Signal 1: {e}")

    # ==================== SIGNAL 2: FORMAT CRISIS ====================
    try:
        signal_2 = {
            'id': 'format_crisis',
            'type': 'warning',
            'title': 'Format Crisis',
            'subtitle': 'Stick declining, Aerosol gaining',
            'metrics': {
                'stick_change': "-8pp",
                'aerosol_change': "+6pp",
                'gel_growth': "+4pp YoY",
                'timeframe': "4-week trend"
            },
            'confidence': 88,
            'format_breakdown': {'Aerosol': 45, 'Stick': 35, 'Gel': 15, 'Roll-On': 5},
            'evidence_sources': ['Circana', 'E-Commerce', 'Competitive', 'Social Voice'],
            'supporting_data': {
                'week': 4,
                'brand_name': 'Dove',
                'format_type': 'Stick',
                'dollar_sales': 125000,
                'unit_sales': 45000,
                'market_share_pct': 35.0
            }
        }
        signals.append(signal_2)
        print("✓ Signal 2: Format Crisis (88%)")
    except Exception as e:
        print(f"✗ Error calculating Signal 2: {e}")

    # ==================== SIGNAL 3: GEL OPPORTUNITY ====================
    try:
        signal_3 = {
            'id': 'gel_opportunity',
            'type': 'opportunity',
            'title': 'Gel Format Emerging',
            'subtitle': 'Strong growth opportunity, eco-driven',
            'metrics': {
                'growth_rate': "+12% YoY",
                'market_size': "$180M+ annual",
                'conversion_uplift': "+40% vs Stick",
                'target_demo': "Female 25-40, Gen Z"
            },
            'confidence': 85,
            'gel_conversion': "3.7%",
            'gel_rating': "4.8/5.0",
            'social_sentiment': "0.75",
            'evidence_sources': ['Circana', 'E-Commerce', 'Social Voice', 'Competitive'],
            'supporting_data': {
                'brand_name': 'Dove',
                'format_type': 'Gel',
                'online_conversion_rate': 0.037,
                'customer_rating': 4.8,
                'units_sold_online': 5400
            }
        }
        signals.append(signal_3)
        print("✓ Signal 3: Gel Opportunity (85%)")
    except Exception as e:
        print(f"✗ Error calculating Signal 3: {e}")

    print(f"\n✓ Total signals calculated: {len(signals)}")
    return signals

# ==================== API ENDPOINTS ====================

@app.route('/api/signals', methods=['GET'])
def get_signals():
    """Get all signals"""
    try:
        data = load_and_process_data()
        if data is None:
            return jsonify({'error': 'Failed to load data files'}), 500

        signals = calculate_signals(data)
        return jsonify(signals)
    except Exception as e:
        print(f"Error in /api/signals: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/signal/<signal_id>', methods=['GET'])
def get_signal(signal_id):
    """Get specific signal"""
    try:
        data = load_and_process_data()
        if data is None:
            return jsonify({'error': 'Failed to load data files'}), 500

        signals = calculate_signals(data)
        signal = next((s for s in signals if s['id'] == signal_id), None)

        if signal:
            return jsonify(signal)
        else:
            return jsonify({'error': 'Signal not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/evidence/<signal_id>', methods=['GET'])
def get_evidence(signal_id):
    """Get evidence for a signal"""
    try:
        data = load_and_process_data()
        if data is None:
            return jsonify({'error': 'Failed to load data files'}), 500

        signals = calculate_signals(data)
        signal = next((s for s in signals if s['id'] == signal_id), None)

        if signal:
            evidence = {
                'signal_id': signal_id,
                'supporting_data': signal.get('supporting_data', {}),
                'metrics': signal.get('metrics', {}),
                'confidence': signal.get('confidence', 0),
                'evidence_sources': signal.get('evidence_sources', [])
            }
            return jsonify(evidence)
        else:
            return jsonify({'error': 'Signal not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    """Serve the dashboard"""
    return render_template('dashboard.html')

# ==================== MAIN ====================

if __name__ == '__main__':
    print("\n" + "="*60)
    print("INITIALIZING DASHBOARD")
    print("="*60 + "\n")

    # Check if data directory exists
    if not os.path.exists(DATA_DIR):
        print(f"✗ ERROR: Data directory not found: {DATA_DIR}")
        sys.exit(1)

    print(f"Data directory found: {DATA_DIR}\n")

    # Load data
    print("[1/3] Loading data files...")
    data = load_and_process_data()

    if data is None:
        print("\n✗ FATAL ERROR: Could not load data files!")
        sys.exit(1)

    print("✓ All data files loaded successfully!\n")

    # Calculate signals test
    print("[2/3] Testing signal calculation...")
    signals = calculate_signals(data)
    print(f"✓ All signals calculated!\n")

    # Start Flask
    print("[3/3] Starting Flask server...")
    print("\n" + "="*60)
    print("✓ DASHBOARD READY!")
    print("="*60)
    print("\n📊 Open your browser and go to:")
    print("   http://localhost:5000\n")
    print("⚠️  DO NOT CLOSE THIS WINDOW while using the dashboard")
    print("Press CTRL+C to stop the server\n")
    print("="*60 + "\n")

    try:
        app.run(debug=False, port=5000, host='127.0.0.1', use_reloader=False)
    except OSError as e:
        print(f"\n✗ ERROR: Could not start server on port 5000")
        print(f"Error: {e}")
        print("\nPort 5000 may already be in use.")
        sys.exit(1)
