# Phase 3: Analytical Engines Visualization (Weeks 4-9)

## Overview

**Phase 3** makes the entire analytical pipeline visible and interactive. Users can see exactly how signals are calculated, which engines confirmed them, and where the confidence scores come from.

---

## The 8 Analytical Engines

### 1. KPI Calculator
**Purpose:** Compute weekly/monthly metrics from raw data

**Inputs:**
- Circana raw sales data
- Category trended historical data

**Calculations:**
- Market share ($ and units)
- Growth rates (YoY, WoW, MoM)
- Price realization (ASP)
- Distribution coverage

**Outputs:**
- Weekly KPI dataframe
- Trend direction (+/- YoY)

**Example:** "Market share down 1.8pp WoW" from KPI Calculator

---

### 2. Trend Detector
**Purpose:** Identify direction and velocity of KPI changes

**Inputs:**
- KPI history (4+ weeks)
- Market share over time
- Price trends

**Calculations:**
- Linear regression (trend direction)
- Velocity (change/week)
- Acceleration (velocity change)
- Deviation from baseline

**Outputs:**
- Trend signal (↑ up, ↓ down, → flat)
- Confidence (strength of trend)

**Example:** "Share trend down 0.45pp/week for 4 weeks" = accelerating threat

---

### 3. Anomaly Detector
**Purpose:** Flag statistical outliers

**Inputs:**
- Current week metrics
- Historical average (past 52 weeks)
- Standard deviation

**Calculations:**
- Z-score ((value - mean) / std_dev)
- Threshold: |Z| > 2.5 (99% confidence)

**Outputs:**
- Anomaly flag (yes/no)
- Severity (Z-score magnitude)

**Example:** "Share down 8pp = Z-score -3.2" = severe anomaly

---

### 4. Driver Decomposer
**Purpose:** Break down KPI movement into drivers

**Inputs:**
- Current metrics
- Previous metrics
- Multiple data sources

**Calculations:**
- Price contribution (price × volume elasticity)
- Volume contribution
- Mix contribution (format/segment changes)
- Market contribution (category growth/decline)

**Outputs:**
- Driver attribution (% of change)
- Root cause hypothesis

**Example:** "Share loss is 60% price-driven, 40% format-shift"

---

### 5. Relative Performance
**Purpose:** Compare us vs competitors

**Inputs:**
- Our metrics
- Competitor metrics
- Market benchmarks

**Calculations:**
- Price gap vs each competitor
- Market share vs competitor
- Growth rate comparison
- Promotional intensity ratio

**Outputs:**
- Competitive position (leader/follower)
- Pressure indicator (high/medium/low)

**Example:** "Old Spice 10.9% cheaper, gaining share faster"

---

### 6. Cross-KPI Diagnosis
**Purpose:** Validate signals across multiple KPIs

**Inputs:**
- Market share trend
- Distribution trend
- Brand awareness (BGS)
- Consideration (BGS)
- Social sentiment

**Calculations:**
- Correlation check (do KPIs move together?)
- Conflict check (do metrics contradict?)

**Outputs:**
- Coherence score (1-100)
- Diagnostic verdict

**Example:** "Share down BUT awareness up = distribution issue, not perception"

---

### 7. Threat Classifier
**Purpose:** Categorize threats into types

**Inputs:**
- All engine outputs
- Signal characteristics

**Classification Rules:**
- **Distribution Loss:** If distribution ↓ and share ↓
- **Price Pressure:** If price gap widening and competitor attacking
- **Penetration Erosion:** If HH% declining
- **Format Shift:** If one format declining faster
- **Loyalty Breakdown:** If repeat purchase rate declining
- **Awareness Decline:** If awareness ↓ while consideration ↓

**Outputs:**
- Threat type (one of 6 above)
- Sub-threat (specific market/segment)

**Example:** "Price Pressure in NY market + BOGO promotion active"

---

### 8. Evidence Chain Generator
**Purpose:** Link data sources → calculations → signal

**Inputs:**
- All engine outputs + decisions
- Original data row that triggered

**Creates:**
- Chain of evidence document
- Data lineage (CSV row → calculation → signal)
- Confidence justification

**Outputs:**
- Evidence chain object
- Audit trail for signal

**Example:**
```
Data: competitive_deo_us.csv row 47 (Old Spice -10.9%)
  ↓
Relative Performance: Price gap detected
  ↓
Trend Detector: Gap widening 4 weeks
  ↓
Cross-KPI: Share declining in same markets
  ↓
Threat Classifier: PRICE PRESSURE
  ↓
SIGNAL: Competitive Price War (94% confidence)
```

---

## Phase 3 Implementation

### Architecture

```
CSV Data Files
    ↓
[1] KPI Calculator → Weekly metrics
    ↓
[2] Trend Detector → Direction + velocity
    ↓
[3] Anomaly Detector → Outlier detection
    ↓
[4] Driver Decomposer → Root cause
    ↓
[5] Relative Performance → Competitive view
    ↓
[6] Cross-KPI Diagnosis → Coherence check
    ↓
[7] Threat Classifier → Category
    ↓
[8] Evidence Chain → Audit trail
    ↓
Signal Output (94% confidence)
```

### Frontend: Pipeline Visualization

**Interactive Flow View:**
- Horizontal flow: Data → Engine 1 → Engine 2 → ... → Signal
- Each engine is a clickable node
- Click engine → see calculations step-by-step

**Example Pipeline View:**
```
circana.csv
    ↓
┌─────────────────────┐
│  KPI Calculator     │  Market share: 18.5%
│  (sales → metrics)  │  Growth: -1.8pp WoW
└─────────────────────┘
    ↓
┌─────────────────────┐
│  Trend Detector     │  Velocity: -0.45pp/week
│  (4-week trend)     │  Confidence: HIGH
└─────────────────────┘
    ↓
   ...
    ↓
┌─────────────────────┐
│  Signal Output      │  🔴 CRITICAL
│  Price War (94%)    │  Action: Review pricing
└─────────────────────┘
```

### Features

**1. Engine Drill-Down**
- Click any engine → see input data
- See calculations step-by-step
- Show intermediate outputs
- Explain decisions

**2. Confidence Breakdown**
- Show which engines CONFIRMED signal
- Show which engines had doubts
- Display Z-scores and calculations
- Explain why confidence is 94%

**3. Data Lineage**
- Trace signal back to CSV row
- Show timestamp of data
- Link to raw data table
- Show data quality score

**4. Sensitivity Analysis**
- "What if X changed by Y%?"
- How much would confidence change?
- Which engine is most sensitive?

**5. Alternative Explanations**
- Could this be caused by something else?
- Cross-KPI check finds contradictions
- Driver decomposer shows distribution

---

## Implementation Plan (Weeks 4-9)

### Week 1-2: Engine Implementation
- [ ] Build 8 engine modules
- [ ] Each returns JSON with calculations
- [ ] Unit test each engine
- [ ] Validate outputs with sample data

### Week 2-3: API Layer
- [ ] `/api/engines/<type>` endpoints
- [ ] `/api/engine/<id>/details` details view
- [ ] `/api/confidence/<signal_id>` breakdown
- [ ] `/api/lineage/<signal_id>` data trace

### Week 3-4: Frontend Visualization
- [ ] Pipeline flow view (SVG/Canvas)
- [ ] Engine detail panels
- [ ] Confidence breakdown chart
- [ ] Data lineage display

### Week 4: Integration & Testing
- [ ] Connect frontend to API
- [ ] End-to-end testing
- [ ] Performance optimization
- [ ] Documentation

### Week 5: Polish & Deploy
- [ ] UI refinement
- [ ] Edge case handling
- [ ] Production deployment
- [ ] Client demo

---

## Code Structure (Phase 3)

```
backend/
├── analytics/
│   ├── __init__.py
│   ├── engines/
│   │   ├── __init__.py
│   │   ├── kpi_calculator.py
│   │   ├── trend_detector.py
│   │   ├── anomaly_detector.py
│   │   ├── driver_decomposer.py
│   │   ├── relative_performance.py
│   │   ├── cross_kpi_diagnosis.py
│   │   ├── threat_classifier.py
│   │   └── evidence_chain.py
│   ├── signal_pipeline.py
│   └── confidence_model.py
├── app.py (updated)
└── templates/
    ├── dashboard.html (updated)
    └── pipeline.html (new)
```

---

## Example: Price War Signal Pipeline (Detailed)

### Input Data
```
competitive_deo_us.csv row 47:
  competitor_name: "Old Spice"
  competitor_price: $3.93
  our_price: $4.39
  price_gap_pct: -10.9
  competitor_promotion_flag: 1
  week_ending_date: 2026-09-28
```

### Engine 1: KPI Calculator
```json
{
  "engine": "KPI Calculator",
  "input": "circana data week 4",
  "calculations": {
    "our_share": "18.5%",
    "our_price": "$4.39",
    "volume": "450,000 units"
  },
  "output": {
    "market_share_pct": 18.5,
    "asp": 4.39
  }
}
```

### Engine 2: Trend Detector
```json
{
  "engine": "Trend Detector",
  "input": "4-week share history: [20.3, 20.1, 19.2, 18.5]",
  "calculations": {
    "regression_slope": -0.45,
    "velocity_pct": "-0.45pp/week",
    "r_squared": 0.95
  },
  "output": {
    "trend": "DECLINING",
    "velocity": -0.45,
    "confidence": "HIGH"
  }
}
```

### Engine 3: Anomaly Detector
```json
{
  "engine": "Anomaly Detector",
  "input": "Current: 18.5%, Historical avg: 19.8%, Std dev: 0.5%",
  "calculations": {
    "z_score": -2.6,
    "threshold": 2.5,
    "severity": "HIGH"
  },
  "output": {
    "is_anomaly": true,
    "z_score": -2.6,
    "flag": "ALERT - Severe drop"
  }
}
```

### Engine 4: Driver Decomposer
```json
{
  "engine": "Driver Decomposer",
  "input": "Share change: -1.8pp, Price gap: -10.9%, Promo competitor: YES",
  "calculations": {
    "price_contribution": 60,
    "volume_contribution": 30,
    "mix_contribution": 10
  },
  "output": {
    "root_cause": "PRICE-DRIVEN (60%)",
    "secondary": "Volume pressure (30%)"
  }
}
```

### Engine 5: Relative Performance
```json
{
  "engine": "Relative Performance",
  "input": "Our: $4.39, Old Spice: $3.93, Our share: 18.5%, Their share: 16.2%",
  "calculations": {
    "price_gap": -10.9,
    "share_gap": 2.3,
    "momentum": "They gaining faster"
  },
  "output": {
    "competitive_threat": "HIGH",
    "pressure_type": "PRICE ATTACK"
  }
}
```

### Engine 6: Cross-KPI Diagnosis
```json
{
  "engine": "Cross-KPI Diagnosis",
  "input": "Share ↓, Distribution →, Awareness →, Consideration ↓",
  "calculations": {
    "coherence_check": "COHERENT",
    "correlation": "Price-driven share loss",
    "contradiction": "None"
  },
  "output": {
    "diagnosis": "External pricing pressure, not internal brand issue"
  }
}
```

### Engine 7: Threat Classifier
```json
{
  "engine": "Threat Classifier",
  "input": "Engines 1-6 outputs",
  "classifications": {
    "primary_threat": "PRICE PRESSURE",
    "secondary_threat": "COMPETITIVE OFFENSIVE",
    "market_scope": "NY, LA, Chicago, Houston, Phoenix"
  },
  "output": {
    "threat_type": "PRICE_PRESSURE",
    "sub_threat": "Competitor BOGO promotion"
  }
}
```

### Engine 8: Evidence Chain
```json
{
  "engine": "Evidence Chain",
  "signal": "Competitive Price War",
  "confidence": 94,
  "chain": [
    {
      "step": 1,
      "source": "competitive_deo_us.csv",
      "data": "Old Spice -10.9%",
      "engine": "KPI Calculator",
      "output": "Price gap confirmed"
    },
    {
      "step": 2,
      "engine": "Trend Detector",
      "output": "Gap widening 4 weeks"
    },
    ...
  ]
}
```

### Final Signal
```json
{
  "id": "price_war",
  "type": "critical",
  "title": "Competitive Price War",
  "confidence": 94,
  "reason": "All 8 engines aligned: price gap detected → widening trend → market share loss → competitor promotion active → external threat confirmed",
  "engines_confirmed": [1,2,3,4,5,6,7,8],
  "action": "Review pricing strategy"
}
```

---

## Success Metrics for Phase 3

✅ Users understand HOW each signal was calculated  
✅ Confidence scores are transparent and explainable  
✅ Data lineage is traceable (CSV row → signal)  
✅ Pipeline view is intuitive and interactive  
✅ No user needs to ask "why did we get this signal?"  
✅ Stakeholders trust signals because they see the evidence

---

## Future Enhancements (Phase 4+)

- Real-time engine updates (refresh data daily)
- Sensitivity analysis (what-if scenarios)
- A/B testing of engine logic
- User-defined thresholds per signal
- Predictive modeling (forecast threats)
- Integration with BI tools (Tableau, Power BI)
- Mobile app for alerts
- Slack/email notifications
