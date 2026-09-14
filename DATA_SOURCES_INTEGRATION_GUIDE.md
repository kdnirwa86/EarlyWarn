# Data Sources Integration Guide for Early Warning Analytical Engine

## Executive Summary

The Early Warning Intelligence Engine uses **5 complementary data layers** to provide comprehensive, multi-perspective analysis:

```
┌─────────────────────────────────────────────────────────────────────────┐
│          COMPLETE INTELLIGENCE MODEL - 5 DATA SOURCES                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  Layer 1: OPERATIONAL (Weekly POS)                [GDD Nielsen]          │
│   └─ WHAT happened at retail                                            │
│                           │                                              │
│  Layer 2: DETAILED (Weekly POS - Extended)        [Circana 1000]         │
│   └─ DEEP-DIVE single category analysis                                 │
│                           │                                              │
│  Layer 3: HOUSEHOLD (Monthly)                     [Penetration Panel]    │
│   └─ WHO bought & HOW MUCH loyalty                                      │
│                           │                                              │
│  Layer 4: PERCEPTION (Monthly)                    [BGS Brand Health]     │
│   └─ WHY consumers made choices                                         │
│                           │                                              │
│  Layer 5: CONTEXT (Annual)                        [Category Trended]     │
│   └─ STRUCTURAL long-term trajectory                                    │
│                           │                                              │
│              ↓↓↓ INTEGRATED INTELLIGENCE ENGINE ↓↓↓                     │
│         (Real-time operational + Strategic context)                     │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Part 1: Data Sources Overview

### Source 1: GDD Nielsen POS Data (Multi-Category)

| Attribute | Value |
|-----------|-------|
| **File Name** | `GDD_Dummy_Neilson.xlsx` |
| **Type** | Point-of-Sale transaction data |
| **Rows × Columns** | 281 × 105 |
| **Time Granularity** | Weekly (3 periods: MAT-2, MAT-1, MAT) |
| **Geographic Scope** | North America / United States |
| **Category Coverage** | 6+ categories (Deodorant, Snacks, Cereal, Bread, Beverages, Coffee, Cleaning) |
| **Data Freshness** | Current MAT period |
| **Completeness** | 90%+ |

#### What It Contains
```
Dimensions:
├─ Time: Week ID, Week Ending Date, Fiscal Year/Month/Quarter
├─ Geography: Market, State, Region
├─ Retail: Channel (Supermarket, Hypermarket, Drug, Convenience, Multi-outlet)
├─ Retailer: National vs Regional
├─ Product: Category → SubCategory → Manufacturer → Brand → SKU → UPC
└─ Promotion: Promo flags, lift %, base vs incremental units

Metrics (Level 1-2 KPIs):
├─ Revenue: dollar_sales, base_dollar_sales, promo_dollar_sales
├─ Volume: units_sold, base_units, incremental_units, promo_units
├─ Distribution: distribution_pct (% stores carrying)
├─ Price: average_unit_price, realized_unit_price, price_per_volume_unit
├─ Market Share: market_share_pct (both value and volume implied)
├─ Promotion: is_promoted, promo_lift_pct
└─ Opportunity: (Built-in classifications: Winners, Bleeders, etc.)
```

#### Primary Use Case
**What happened at retail this week/month?**
- Revenue up/down and why (price vs volume)
- Market share movement by channel
- Promotional effectiveness
- Distribution losses or gains
- Competitive pricing dynamics

---

### Source 2: Circana 1000-Row Deodorant Data (Category-Focused)

| Attribute | Value |
|-----------|-------|
| **File Name** | `circana_1000_rows_dummy.csv` |
| **Type** | Point-of-Sale transaction data (synthetic, 1000 rows) |
| **Rows × Columns** | 1,000 × 44 |
| **Time Granularity** | Weekly (distributed across FY2025-2026) |
| **Geographic Scope** | North America / United States |
| **Category Focus** | **Deodorants & Fragrances ONLY** (5 subcategories) |
| **Brand Coverage** | 25 real brands (Dove, Axe, Degree, Rexona, Old Spice, Secret, Nivea, etc.) |
| **Market Coverage** | 10 US cities |
| **Completeness** | 100% (synthetically generated) |

#### What It Contains
```
Same 44 columns as GDD, but focused entirely on Deodorant category:

Subcategories:
├─ Aerosol Deodorant
├─ Stick Deodorant
├─ Roll-On Deodorant
├─ Gel Deodorant
└─ Antiperspirant

Manufacturers: 5 (Unilever, P&G, Henkel, Church & Dwight, Colgate)

Markets: 10 US cities (New York, LA, Chicago, Houston, etc.)

Channels: 5 (Grocery, Drug, Mass Merch, E-Commerce, Club)
```

#### Primary Use Case
**Deep-dive analysis on a single category**
- Subcategory performance trends (Aerosol vs Stick vs Roll-On)
- Brand-level competitive dynamics within deodorants
- Format/type preferences by market/channel
- Detailed scenario testing (what if Aerosol declines 10%?)
- Validation of analytical engines with known patterns
- Root cause analysis at granular brand level

---

### Source 3: Penetration Panel Data (Household Level)

| Attribute | Value |
|-----------|-------|
| **File Name** | `Penetreation _Data_Deo_US.xlsx` |
| **Type** | Household panel survey data (Worldpanel/Kantar) |
| **Rows × Columns** | 2,129 × 61 |
| **Time Granularity** | Monthly (3 periods: MAT-2, MAT-1, MAT) |
| **Geographic Scope** | North America / United States |
| **Category Coverage** | Deodorants (focus) + other tracked categories |
| **Data Freshness** | May 2026 monthly snapshot |
| **Completeness** | 85%+ (some metrics legitimately null) |

#### What It Contains
```
Dimensions:
├─ Household Universe (% of population)
├─ Brand × Gender × Segment
├─ Time: MAT periods + Last 12 Weeks variants
└─ Significance flags (1=significant, 0=flat, -1=decline)

Metrics (Consumer Behavior Level):
├─ Penetration: % households buying
├─ Buyers: # of households
├─ Trips: Purchase occasions
├─ Frequency: Purchases per buyer
├─ Repeat Rate: % of buyers who repeat purchase
├─ Value: Total $ spent (HH universe basis)
├─ Volume: Total units (HH universe basis)
├─ Spend per Buyer: $ per household
├─ Spend per Trip: $ per purchase occasion
├─ Relative Penetration: Brand vs Category index
└─ Loyalty Trips: Repeat purchase occasions
```

#### Primary Use Case
**Who is buying and with what loyalty?**
- Household penetration reach (% of HH buying brand)
- Customer retention (repeat rate trends)
- Purchase intensity (frequency per buyer)
- Acquisition vs retention diagnosis
  - Penetration ↓ + Repeat → lost customers
  - Penetration → + Frequency ↑ → deeper loyalty
- Validate POS revenue changes with household data
- Segment performance by consumer type

---

### Source 4: BGS Brand Health Data (Perception Level)

| Attribute | Value |
|-----------|-------|
| **File Name** | `BGS data_dummy.xlsx` |
| **Type** | Brand health tracking (Kantar consumer survey) |
| **Rows × Columns** | 1,074 × 53 |
| **Time Granularity** | Monthly (single snapshot: May 2026) |
| **Geographic Scope** | North America / United States |
| **Category Coverage** | Deodorants (focus) |
| **Data Freshness** | Q2 2026 snapshot |
| **Completeness** | ~50% (many diagnostic fields unpopulated) |

#### What It Contains
```
Dimensions:
├─ Brand × Gender (Female/Male split)
├─ Unilever vs Competitor
├─ Power Brands flag
└─ Time: MAT periods with significance flags

Metrics (Brand Perception - Level 3):
├─ Brand Awareness: % aware of brand
├─ Brand Consideration: % considering purchase
├─ Brand Preference: % preferring over alternatives
├─ Purchase Behavior: Recent/regular purchase
├─ Penetration (from awareness): Household % reached
├─ Loyalty Trips: Repeat purchase occasions
├─ Frequency: Purchases per buyer
├─ Spend per Buyer: $ per customer
├─ Repeat Rate: % of buyers repeating
├─ Relative Penetration: vs category average
├─ Value: Total $ by brand
├─ Volume: Total units by brand
├─ Trips: Total occasions
└─ Buyers: Total households
```

#### Primary Use Case
**Why are consumers making purchase choices?**
- Brand awareness trends (awareness ↓ explains volume ↓?)
- Preference vs penetration gap (aware but not buying?)
- Emotional connection & brand equity
- Power brand performance tracking (Unilever portfolio)
- Competitive benchmarking (Brand A vs Competitor B brand health)
- Root cause analysis: Sales ↓ due to awareness loss vs choice shift?

---

### Source 5: Category Trended Data (Historical Context)

| Attribute | Value |
|-----------|-------|
| **File Name** | `Category_Deo_Dummy.xlsx` |
| **Type** | Historical category performance (10-year annual data) |
| **Rows × Columns** | 1,277 × 24 |
| **Time Granularity** | Annual (Fiscal Years 2016-2025) |
| **Geographic Scope** | North America / United States |
| **Category Coverage** | Deodorants & Fragrances |
| **Time Span** | 10 years of history |
| **Data Freshness** | June 2026 report (FY2025 complete) |
| **Completeness** | 100% (all years populated) |

#### What It Contains
```
Dimensions:
├─ Time: 10 fiscal years (FY2016 - FY2025)
├─ Aggregation Level: ALL MANUFACTURERS → Individual Manufacturer → Brand
└─ Hierarchy: Category → SubCategory → Manufacturer → Brand

Metrics (Structural Trends):
├─ Revenue:
│  ├─ Value (k EUR)
│  ├─ Value Growth vs PY (%)
│  ├─ Value Share (%)
│  └─ Value Share Development (bps)
├─ Volume:
│  ├─ Volume (units)
│  ├─ Volume Growth vs PY (%)
│  ├─ Volume Share (%)
│  └─ Volume Share Development (bps)
├─ Price:
│  ├─ Average Price (EUR/unit)
│  ├─ Average Price Growth vs PY (%)
│  └─ Average Price Index (indexed to base)
└─ Positioning: Competitive pricing strategy over time
```

#### Key Insights (10-Year Patterns)
```
Category Trajectory (FY2016 → FY2025):
├─ Revenue: €2.77B → €5.43B (+96%, CAGR 7.8%)
├─ Volume: 811M → 868M units (+7%, CAGR 0.7%)
├─ Price: €3.42 → €6.25 (+83%, CAGR 7.0%)
└─ Trend: PRICE-DRIVEN GROWTH, volume flat (mature market)

Competitive Shift (Beiersdorf/Nivea):
├─ FY2016: Premium positioning (€7.21, 210% index)
├─ FY2025: Value positioning (€3.65, 58% index)
├─ Movement: Downward price strategy, declining share
└─ Implication: Market consolidation at price-based competition
```

#### Primary Use Case
**Is this structural change or tactical noise?**
- 10-year baseline for anomaly detection
- Category maturity assessment (growth → plateau → decline?)
- Cyclical pattern identification
- Competitive positioning trajectory
- Long-term sustainability signals
- Context for interpreting recent short-term moves

---

## Part 2: Analytical Engine Architecture

### Engine Processing Pipeline

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    RAW DATA INGESTION (5 Sources)                        │
├─────────────────────────────────────────────────────────────────────────┤
│  GDD (281 rows)  |  Circana 1K (1000 rows)  |  Panel (2129)  |  BGS  │  │
│  Brands Multi    |  Deodorant Focus         |  Household     |  Perception
└─────────────┬───────────────────────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                   LAYER 1: DATA PREPARATION                              │
├─────────────────────────────────────────────────────────────────────────┤
│  • Normalize column names across sources                                 │
│  • Handle missing/null values                                           │
│  • Standardize units (€ → $, units, volumes)                           │
│  • Align time periods (weekly → monthly → annual)                       │
│  • Create master dimension tables (Brand, Channel, Market, etc.)        │
└─────────────┬───────────────────────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────────────────────┐
│           LAYER 2: POS ENGINE (GDD + Circana 1K)                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  [Engine 1] KPI Calculation                                             │
│  ├─ Revenue = Units × ASP                                               │
│  ├─ Market Share = Brand Value / Category Value                         │
│  ├─ Distribution normalized                                             │
│  └─ Price decomposition                                                 │
│         │                                                                │
│         ▼                                                                │
│  [Engine 2] Trend Detection                                             │
│  ├─ MoM / QoQ / YoY growth                                              │
│  ├─ Direction flagging (↑↓→)                                            │
│  ├─ Significance thresholds (±5% material)                             │
│  └─ Output: Trend signals                                               │
│         │                                                                │
│         ▼                                                                │
│  [Engine 3] Anomaly Detection                                           │
│  ├─ Historical baseline (12-week rolling)                               │
│  ├─ Z-score calculation (|Z| > 2 = anomaly)                            │
│  ├─ Confidence scoring                                                  │
│  └─ Output: Anomaly flags                                               │
│         │                                                                │
│         ▼                                                                │
│  [Engine 4] Driver Decomposition                                        │
│  ├─ Revenue = Volume Effect + Price Effect                             │
│  ├─ Market Share = Distribution + Price + Volume                       │
│  ├─ Attribution to each factor                                         │
│  └─ Output: Driver contribution %                                       │
│                                                                           │
│  INPUT SOURCES:                                                         │
│  ├─ GDD (281 rows): Multi-category operational data                    │
│  │  └─ Use: Immediate signals, competitive benchmarking                │
│  └─ Circana 1K (1000 rows): Deep deodorant focus                       │
│     └─ Use: Scenario testing, subcategory analysis                     │
│                                                                           │
└─────────────┬───────────────────────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────────────────────┐
│        LAYER 3: HOUSEHOLD VALIDATION ENGINE (Penetration Panel)         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  [Validation] Cross-Check POS Findings                                  │
│  ├─ POS Revenue ↓ → Panel Penetration ↓? OR Frequency ↓?               │
│  ├─ POS Volume ↓ → Panel Repeat Rate ↓? (Loyalty issue)                │
│  ├─ POS Market Share → Panel Relative Penetration trend                │
│  └─ OUTPUT: Corroborated/Contradicted signals                           │
│         │                                                                │
│         ▼                                                                │
│  [Hypothesis Refinement]                                                │
│  ├─ If Revenue ↓ + Penetration ↓ → Lost customer acquisition           │
│  ├─ If Revenue ↓ + Frequency ↓ → Lost loyalty/retention issue          │
│  ├─ If Revenue → + Penetration ↓ + Frequency ↑ → Trading up/mix        │
│  └─ OUTPUT: Refined diagnostic                                          │
│                                                                           │
│  INPUT SOURCE: Penetration Panel (2129 rows)                            │
│  └─ Use: Household behavior validation, loyalty signals                 │
│                                                                           │
└─────────────┬───────────────────────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────────────────────┐
│      LAYER 4: PERCEPTION ENGINE (BGS Brand Health)                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  [Root Cause Analysis]                                                  │
│  ├─ POS + Panel suggest Volume Loss                                     │
│  ├─ BGS shows Awareness ↓ 5%                                            │
│  ├─ Conclusion: Brand awareness driving loss                            │
│  └─ Recommendation: Invest in awareness campaign                        │
│         │                                                                │
│         ▼                                                                │
│  [Competitive Context]                                                  │
│  ├─ Brand A awareness ↓ while Competitor B awareness ↑                 │
│  ├─ Suggests share loss to competitor (not category decline)           │
│  └─ Strategy: Differentiation vs price-based response                  │
│                                                                           │
│  INPUT SOURCE: BGS (1074 rows)                                          │
│  └─ Use: Brand perception, root cause WHY                               │
│                                                                           │
└─────────────┬───────────────────────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────────────────────┐
│    LAYER 5: STRUCTURAL CONTEXT (Category Trended - 10 Years)            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  [Baseline Normalization]                                               │
│  ├─ Recent 3% revenue decline vs 10-year CAGR 7.8%                     │
│  ├─ Is this normal variance or anomaly?                                │
│  ├─ Answer: ANOMALY (worse than historical trend)                      │
│  └─ Action: Escalate from normal monitoring                             │
│         │                                                                │
│         ▼                                                                │
│  [Market Structure Assessment]                                          │
│  ├─ 10-year data shows: Price-driven growth, volume flat                │
│  ├─ Category maturity assessment: ENTERING SATURATION                   │
│  ├─ Implication: Future growth harder to come by                        │
│  └─ Strategy: Share gains more valuable than category growth            │
│         │                                                                │
│         ▼                                                                │
│  [Competitive Positioning]                                              │
│  ├─ Beiersdorf: Premium → Value repositioning over 10 years             │
│  ├─ Market consolidation evident                                        │
│  └─ Forecast: Continued price-based competition                         │
│                                                                           │
│  INPUT SOURCE: Category Trended (1277 rows, 10 years)                   │
│  └─ Use: Historical baseline, market maturity context                   │
│                                                                           │
└─────────────┬───────────────────────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                  FINAL INSIGHT OUTPUT                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  COMPLETE EVIDENCE CHAIN:                                               │
│  ├─ What Happened (GDD/Circana): Revenue ↓ 3%                          │
│  ├─ Why (Decomposition): Volume ↓ 5%, Price ↑ 2%                       │
│  ├─ Who (Penetration Panel): Penetration ↓ 2.5pp (lost customers)      │
│  ├─ Why They Left (BGS): Awareness ↓ 5% (mental availability issue)    │
│  ├─ Is This Normal (Category Trended): NO - below historical trend     │
│  │                                                                       │
│  └─ INSIGHT:                                                            │
│     "Revenue decline driven by lost household penetration (-2.5pp),      │
│      with volume declining 5% despite stable ASP (+2%). Brand awareness │
│      deteriorating (-5%), suggesting reduced mental availability as     │
│      root cause. While 3% revenue decline appears modest, relative to  │
│      10-year category CAGR (7.8%), this signals acceleration of market │
│      maturity. Recommendation: Launch brand awareness campaign to       │
│      rebuild consideration and re-acquire lapsed households."          │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Part 3: Data Source Sequence & Phasing

### Phase 1: MVP - Engines 1-4 (Weeks 1-3)

**Primary Data**: GDD Nielsen (281 rows) + Circana 1000 (1000 rows)

```
Week 1: Setup & Data Ingestion
├─ Load GDD into SQLite
├─ Load Circana 1000 into SQLite
├─ Create master dimension tables
└─ Validate data quality

Week 2: Engines 1-3
├─ Engine 1: KPI Calculator
│  ├─ Revenue = Units × ASP
│  ├─ Market Share calculations
│  └─ Validate against GDD built-in metrics
├─ Engine 2: Trend Detector
│  ├─ MoM/QoQ/YoY calculations
│  └─ Test against GDD "Growing/Declining" flags
└─ Engine 3: Anomaly Detector
   ├─ Z-score calculations
   └─ Test against GDD cell movement flags

Week 3: Engine 4 + Validation
├─ Engine 4: Driver Decomposer
│  ├─ Revenue = Volume + Price decomposition
│  └─ Test against known scenarios
├─ Test Scenario 1: Distribution-Driven Decline
├─ Test Scenario 2: Competitive Price Pressure
└─ Test Scenario 3: Category Downturn

OUTPUT: Working Engines 1-4 validated on GDD + Circana
```

**Data Not Used Yet**:
- ⏸️ Penetration Panel (reserved for Phase 2 validation)
- ⏸️ BGS (reserved for Phase 2 root cause)
- ⏸️ Category Trended (reserved for Phase 3 baseline)

---

### Phase 2: Cross-Source Validation (Weeks 4-6)

**Add Data**: Penetration Panel (2129 rows) + BGS (1074 rows)

```
Week 4-5: Household-Level Validation
├─ Load Penetration Panel
├─ Engine 5: Relative Performance (brand vs category)
├─ Cross-Check:
│  ├─ GDD Revenue ↓ → Panel Penetration ↓?
│  ├─ GDD Volume ↓ → Panel Frequency ↓?
│  └─ GDD Share trends → Panel Relative Penetration
└─ VALIDATE: All 3 sources agree on direction?

Week 6: Perception Analysis
├─ Load BGS
├─ Engine 6: Cross-KPI Diagnosis (with LLM)
├─ Link:
│  ├─ GDD drivers → BGS perception drivers
│  ├─ Volume loss → Awareness decline?
│  └─ Market share loss → Preference decline?
└─ OUTPUT: Root cause hypotheses with evidence chains

OUTPUT: Engines 1-6 validated with 3 data sources
```

---

### Phase 3: Structural Context (Weeks 7+)

**Add Data**: Category Trended (1277 rows, 10-year history)

```
Week 7+: Strategic Context
├─ Load Category Trended
├─ Create 10-year baselines
├─ Calculate:
│  ├─ Historical volatility for anomaly thresholds
│  ├─ Growth trend decomposition (price vs volume CAGR)
│  └─ Market maturity indicators
├─ Re-calibrate Engines 2-3 with historical context
└─ Enable long-term trend identification

INTEGRATION:
├─ Short-term anomalies (Engine 3) vs long-term trends
├─ Price growth sustainability
├─ Volume stagnation implications
└─ Competitive positioning trajectory (Beiersdorf case)

OUTPUT: Complete intelligence engine with strategic + operational layers
```

---

## Part 4: Data Flow Specification for Each Engine

### Engine 1: KPI Calculator

```
INPUT SOURCES:
├─ Primary: GDD (weekly POS)
├─ Validation: Circana 1000 (weekly POS)
└─ Context: Category Trended (annual)

CALCULATION LOGIC:
├─ Revenue = Units × ASP
├─ Market Share = Brand Value / (Sum of all brands in category)
├─ Distribution % = (Stores carrying / Total stores) × 100
├─ Price Premium Index = Brand ASP / Category Average ASP × 100
└─ Relative Growth = Brand Growth % - Category Growth %

OUTPUT:
└─ KPI Table (SQLite):
   ├─ kpi_id
   ├─ week_ending_date
   ├─ brand_id, category_id, geography_id
   ├─ revenue, units, asp, market_share_pct, distribution_pct
   └─ price_premium_index

VALIDATION:
├─ Spot-check 10 brands against source values
├─ Cross-verify with GDD built-in calculations
└─ Flag any discrepancies > 1%
```

### Engine 2: Trend Detection

```
INPUT SOURCES:
├─ Primary: KPI Table (from Engine 1)
├─ Comparison: GDD "Growing/Declining" flags
└─ History: Category Trended for baselines

CALCULATION LOGIC:
├─ MoM Growth = (Current - Prior Month) / Prior Month × 100
├─ Direction = IF Growth > +5% THEN "Growing"
│            ELSE IF Growth < -5% THEN "Declining"
│            ELSE "Flat"
└─ Significance = Compared to historical volatility (from Cat Trended)

OUTPUT:
└─ Trend Table (SQLite):
   ├─ signal_id
   ├─ kpi_id
   ├─ direction (↑/↓/→)
   ├─ magnitude_pct
   ├─ timeframe (MoM/QoQ/YoY)
   └─ confidence_level (High/Medium/Low)

VALIDATION:
├─ Compare all "Growing" flags vs GDD = 100% match?
├─ Compare "Declining" flags vs GDD = 95%+ match?
└─ Reconcile discrepancies
```

### Engine 3: Anomaly Detection

```
INPUT SOURCES:
├─ Primary: KPI Table (from Engine 1)
├─ Historical: Category Trended (10-year baseline)
└─ Recent: Last 12 weeks rolling stats

CALCULATION LOGIC:
├─ Mean = Average of last 12 weeks
├─ StdDev = Standard deviation of last 12 weeks
├─ Z-Score = (Current - Mean) / StdDev
├─ Anomaly Flag = IF |Z-Score| > 2 THEN "Yes"
└─ Severity = |Z-Score| value (Higher = More extreme)

OUTPUT:
└─ Anomaly Table (SQLite):
   ├─ anomaly_id
   ├─ kpi_id
   ├─ z_score
   ├─ mean_historical
   ├─ current_value
   ├─ is_anomaly (Yes/No)
   └─ confidence_pct (95% for Z>2)

VALIDATION:
├─ Compare to GDD cell movement flags (Green/Red)
├─ "Cell to Red" should match high Z-scores
├─ "Cell to Green" should match low Z-scores
└─ Test on known scenario patterns
```

### Engine 4: Driver Decomposition

```
INPUT SOURCES:
├─ Primary: KPI Table (from Engine 1)
├─ Reference: Category Tranded (for context)
└─ Validation: Penetration Panel (Phase 2)

CALCULATION LOGIC:
├─ Revenue Change = (Volume Change × Prior ASP) + (ASP Change × Current Units)
├─ Volume Effect % = Volume Change / Revenue Change × 100
├─ Price Effect % = Price Change / Revenue Change × 100
├─ Market Share Change = Volume Share Change + Price Mix Effect
└─ Primary Driver = Whichever effect has largest |magnitude|

EXAMPLE:
│ Revenue: -8%
│ ├─ Volume Effect: -10% (Primary)
│ ├─ Price Effect: +2% (Offsetting)
│ └─ Interpretation: VOLUME-DRIVEN DECLINE

OUTPUT:
└─ Attribution Table (SQLite):
   ├─ attribution_id
   ├─ kpi_id
   ├─ revenue_change_pct
   ├─ volume_effect_pct
   ├─ price_effect_pct
   ├─ primary_driver (Volume/Price/Mix)
   └─ confidence_level

VALIDATION:
├─ Manual spot-checks on 5-10 brands
├─ Verify math: Volume + Price ≈ Revenue
├─ Compare decomposition to Circana 1000 known patterns
└─ Test Scenario 2 (Price Pressure): Should show Price Effect > Volume
```

### Engine 5: Relative Performance (Phase 2)

```
INPUT SOURCES:
├─ Primary: KPI Table (from Engine 1)
├─ Benchmark: Category totals
└─ Validation: Penetration Panel

CALCULATION LOGIC:
├─ Brand Growth = (Current Brand Value - Prior) / Prior × 100
├─ Category Growth = (Current Category Total - Prior) / Prior × 100
├─ Relative Growth = Brand Growth - Category Growth
├─ Competitive Momentum = IF Relative Growth > +5pp THEN "Gaining"
│                       ELSE IF Relative Growth < -5pp THEN "Losing"
│                       ELSE "In-line"
└─ Market Share Trend = Current Share - Prior Share (in basis points)

OUTPUT:
└─ Relative Performance Table (SQLite):
   ├─ perf_id
   ├─ brand_id
   ├─ brand_growth_pct
   ├─ category_growth_pct
   ├─ relative_growth_pct
   ├─ momentum (Gaining/In-line/Losing)
   └─ share_trend_bps

VALIDATION:
├─ Validate against GDD "Consistent Winners" classification
├─ Cross-check with Penetration Panel relative penetration index
└─ Confirm direction alignment across sources
```

### Engine 6: Cross-KPI Diagnosis (Phase 2, with LLM)

```
INPUT SOURCES:
├─ Primary: All Engines 1-5 outputs
├─ LLM Input: Claude (hypothesis generation)
└─ Validation: BGS Brand Health data

PROCESS:
├─ Step 1: Compile KPI movements
│  ├─ Revenue ↓ 8%
│  ├─ Volume ↓ 10%
│  ├─ ASP ↑ 2%
│  ├─ Distribution ↓ 5 pts
│  └─ Market Share ↓ 2.5 pts
├─ Step 2: Apply deterministic rules
│  ├─ IF (Revenue ↓ AND Volume ↓ AND Distribution ↓) THEN "Distribution-driven"
│  ├─ IF (Price Premium ↑ AND Competitor Price ↓) THEN "Price pressure"
│  └─ [10 more rules]
├─ Step 3: Score driver candidates
│  ├─ Distribution: HIGH confidence
│  ├─ Competitor Price: MEDIUM confidence
│  └─ Promo Reduction: LOW confidence
└─ Step 4: Invoke Claude for narrative
   └─ "Based on these KPI movements, the most likely drivers are..."

OUTPUT:
└─ Diagnosis Table (SQLite):
   ├─ diagnosis_id
   ├─ kpi_id
   ├─ primary_driver (driver name)
   ├─ confidence_level (High/Med/Low)
   ├─ supporting_indicators (list)
   ├─ claude_narrative (text from LLM)
   └─ alternative_hypotheses

VALIDATION:
├─ Compare Claude narrative to BGS perception data
├─ Cross-check if Awareness ↓ explains Volume ↓
├─ Validate against Penetration Panel loyalty signals
└─ Incorporate into evidence chain
```

---

## Part 5: Data Integration Summary Table

| Engine | Primary Data | Secondary Data | Validation Data | Output | Confidence |
|--------|---|---|---|---|---|
| **1: KPI Calc** | GDD (281) | Circana 1K (1K) | None | Standardized KPIs | High |
| **2: Trend** | KPI Table | Cat Trended (10yr) | GDD flags | Trend signals | High |
| **3: Anomaly** | KPI Table | Cat Trended (10yr) | GDD cell flags | Anomaly flags | High |
| **4: Driver** | KPI Table | Circana 1K | None | Driver attribution | High |
| **5: Relative** | KPI Table | Cat Trended | Panel index | Competitive momentum | Medium |
| **6: Diagnosis** | Engines 1-5 | BGS (1K) | Panel behavior | Root causes + Narrative | Medium |
| **7: Threat Class** | Engine 6 | BGS trends | GDD classifications | Signal classification | Medium |
| **8: Evidence Chain** | All outputs | BGS + Panel | Cat Trended context | Structured insight JSON | Medium |

---

## Part 6: MVP Success Criteria

### Data Processing
- ✓ All 5 sources loaded into SQLite
- ✓ Master dimensions created (Brand, Channel, Market, Category)
- ✓ Column naming standardized across sources
- ✓ Time periods aligned (weekly → monthly → annual)

### Engine Validation
- ✓ Engine 1: KPI calculations spot-check within 1% of source
- ✓ Engine 2: Trend detection matches GDD "Growing/Declining" 95%+
- ✓ Engine 3: Anomaly detection matches GDD "Cell to Red/Green" 90%+
- ✓ Engine 4: Driver decomposition verified on 5+ scenarios

### Scenario Testing
- ✓ Scenario 1 (Distribution Decline): Detected correctly
- ✓ Scenario 2 (Price Pressure): Detected correctly
- ✓ Scenario 3 (Category Downturn): Detected correctly
- ✓ No false positives on 10 control scenarios

### Evidence Chains
- ✓ Insights include source evidence
- ✓ Confidence levels reflect data quality
- ✓ Alternative hypotheses considered
- ✓ Narrative synthesizes multiple signals

---

## Conclusion

The **5-layer data model** provides:

1. **Operational Intelligence** (GDD, Circana): Real-time what/where/when
2. **Deep-Dive Analysis** (Circana 1K): Subcategory scenarios
3. **Household Truth** (Penetration Panel): WHO and LOYALTY
4. **Perception Context** (BGS): WHY consumers decided
5. **Structural Baseline** (Category Trended): Is this normal or structural?

Together, they enable **early warning detection with confidence**, not just noise.

