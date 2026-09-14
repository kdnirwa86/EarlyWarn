# REST API Reference

Base URL: `http://localhost:5000`

---

## Endpoints

### Get All Signals
```
GET /api/signals
```

**Response:**
```json
[
  {
    "id": "price_war",
    "type": "critical",
    "title": "Competitive Price War",
    "subtitle": "Old Spice aggressive pricing attack",
    "metrics": {
      "competitor_price": "$3.93",
      "our_price": "$4.39",
      "price_gap": "-10.9%",
      "conversion_impact": "-22%",
      "share_loss": "-1.8pp/week"
    },
    "confidence": 94,
    "financial_impact": "$2.1M monthly at risk",
    "response_window": "48 hours",
    "evidence_sources": ["Circana", "Competitive Intelligence", "E-Commerce", "Social Voice"],
    "supporting_data": {...}
  },
  ...
]
```

**Use Case:** Load all signals for dashboard display

---

### Get Specific Signal
```
GET /api/signal/<signal_id>
```

**Parameters:**
- `signal_id` (string): One of `price_war`, `format_crisis`, `gel_opportunity`

**Response:** Same as individual signal object above

**Example:**
```
GET /api/signal/price_war
```

**Use Case:** Get detailed view of one signal

---

### Get Signal Evidence/Supporting Data
```
GET /api/evidence/<signal_id>
```

**Parameters:**
- `signal_id` (string): One of `price_war`, `format_crisis`, `gel_opportunity`

**Response:**
```json
{
  "signal_id": "price_war",
  "supporting_data": [
    {
      "week_ending_date": "2026-09-28",
      "competitor_name": "Old Spice",
      "competitor_price": 3.93,
      "our_price": 4.39,
      "price_gap_pct": -10.9,
      "competitor_promotion_flag": 1,
      "promo_discount_pct": 25.0,
      ...
    }
  ],
  "metrics": {...},
  "confidence": 94,
  "evidence_sources": [...]
}
```

**Use Case:** Display supporting data table for drill-down

---

### Get Circana Data
```
GET /api/data/circana
```

**Response:**
```json
[
  {
    "week": 1,
    "brand_name": "Dove",
    "format_type": "Aerosol",
    "market": "National",
    "dollar_sales": 125000,
    "unit_sales": 45000,
    "market_share_pct": 18.5,
    "distribution_pct": 92,
    ...
  },
  ...
]
```

**Limit:** First 20 rows only (for inspection)

**Use Case:** View raw Circana data structure

---

### Get Competitive Intelligence Data
```
GET /api/data/competitive
```

**Response:**
```json
[
  {
    "week_ending_date": "2026-09-28",
    "market": "New York",
    "competitor_name": "Old Spice",
    "competitor_price": 3.93,
    "our_price": 4.39,
    "price_gap_pct": -10.9,
    "competitor_promotion_flag": 1,
    "promo_discount_pct": 25.0,
    "competitor_distribution_pct": 85,
    ...
  },
  ...
]
```

**Limit:** First 20 rows only (for inspection)

**Use Case:** View raw competitive intelligence data

---

## HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | ✓ Success - Data returned |
| 404 | ✗ Not Found - Signal ID doesn't exist |
| 500 | ✗ Server Error - Check Flask console for details |

---

## Error Responses

**404 Not Found:**
```json
{
  "error": "Signal not found"
}
```

**500 Server Error:**
```json
{
  "error": "Error message describing what went wrong"
}
```

---

## Usage Examples

### JavaScript / Fetch API

**Load all signals:**
```javascript
fetch('http://localhost:5000/api/signals')
  .then(response => response.json())
  .then(signals => console.log(signals))
  .catch(error => console.error('Error:', error));
```

**Get price war signal details:**
```javascript
fetch('http://localhost:5000/api/signal/price_war')
  .then(response => response.json())
  .then(signal => {
    console.log('Confidence:', signal.confidence);
    console.log('Impact:', signal.financial_impact);
  });
```

**Get evidence for a signal:**
```javascript
fetch('http://localhost:5000/api/evidence/price_war')
  .then(response => response.json())
  .then(evidence => {
    console.log('Supporting data:', evidence.supporting_data);
    console.log('Sources:', evidence.evidence_sources);
  });
```

### Python / Requests

```python
import requests

# Get all signals
response = requests.get('http://localhost:5000/api/signals')
signals = response.json()

# Get specific signal
price_war = requests.get('http://localhost:5000/api/signal/price_war').json()

# Get evidence
evidence = requests.get('http://localhost:5000/api/evidence/price_war').json()
print(evidence['supporting_data'])
```

### cURL

```bash
# Get all signals
curl http://localhost:5000/api/signals

# Get specific signal
curl http://localhost:5000/api/signal/price_war

# Get evidence
curl http://localhost:5000/api/evidence/price_war
```

---

## Data Structure

### Signal Object
```json
{
  "id": "string",                    // Unique identifier
  "type": "critical|warning|opportunity",
  "title": "string",                 // Signal name
  "subtitle": "string",              // Description
  "metrics": {                       // Key metrics
    "key": "value",
    ...
  },
  "confidence": 85,                  // 0-100 percentage
  "evidence_sources": ["string"],    // Data sources that validated
  "supporting_data": {...}           // Sample CSV row
}
```

### Evidence Object
```json
{
  "signal_id": "string",
  "supporting_data": [               // Array of CSV rows
    {
      "column_name": "value",
      ...
    }
  ],
  "metrics": {...},
  "confidence": 85,
  "evidence_sources": ["string"]
}
```

---

## Rate Limits

None - this is a local dashboard. Use freely.

---

## Response Time

- **Signals:** <100ms (pre-calculated)
- **Evidence:** <50ms (from memory)
- **Raw Data:** <200ms (pandas operations)

---

## CORS Support

All endpoints support CORS requests from any origin.

---

## Authentication

None required - this is a local dashboard.

---

## Versioning

Current version: **Phase 2 (1.0)**

Future versions will add:
- `/api/engines/*` - Analytical engine endpoints
- `/api/confidence/<signal_id>` - Confidence breakdown
- `/api/settings/*` - Configuration endpoints
