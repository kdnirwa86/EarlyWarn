# Category Trended Data Analysis: 10-Year Historical Category Performance

## Dataset Overview
**File**: Category_Deo_Dummy.xlsx  
**Sheet**: Sheet1  
**Rows**: 1,277  
**Columns**: 24  
**Data Type**: Category-level historical performance data  
**Time Span**: FY 2016 - FY 2025 (10 fiscal years)  
**Grain**: Manufacturer × Brand Position × Measure × Fiscal Year  
**Currency**: EUR (thousands) for value; EUR/unit for price  
**Geography**: United States of America (single market)  
**Latest Report Date**: 46243 (June 2026 data)  
**Completeness**: 100% for all years

---

## Column Structure (24 columns)

### A. Dimensions & Hierarchy (10 columns)
| Column | Type | Sample Values | Cardinality |
|--------|------|---|---|
| **Mgmt Hierarchy Node Name** | Categorical | United States of America | 1 |
| **Mgmt Hierarchy Level** | Numeric | 6 | 1 |
| **Category Node Name** | Categorical | Deodorants | ~5 |
| **Category Level** | Numeric | 5 | 1-5 |
| **Business Group** | Categorical | Personal Care | ~3 |
| **Category** | Categorical | Deodorants & Fragrances | ~5 |
| **Global Manufacturer Name** | Categorical | ALL MANUFACTURERS, Beiersdorf, P&G, etc. | ~15-20 |
| **Brand Position Type** | Categorical | ALL BRAND POSITIONS, Global/Regional | ~5 |
| **Brand Position Name** | Categorical | ALL BRAND POSITIONS, Nivea, Dove, etc. | ~30-40 |
| **Local Brand Name** | Categorical | ALL BRANDS, Nivea, Dove, etc. | ~40-50 |

**Hierarchy Structure**:
```
ALL MANUFACTURERS (category total)
├── Manufacturer 1 (e.g., Beiersdorf)
│   ├── ALL BRAND POSITIONS
│   ├── Global/Regional → ALL BRANDS
│   │   └── Brand 1 (e.g., Nivea)
│   │   └── Brand 2 (e.g., Nivea)
├── Manufacturer 2 (e.g., P&G)
│   └── [Similar structure]
```

### B. Time Dimension (1 column)
| Column | Type | Values | Purpose |
|--------|------|--------|---------|
| **LatestAvailableDate** | Date | 46243 | Report date (meta, same for all rows) |

### C. Metrics Structure (12 columns + 1 completeness flag)

#### Price Metrics (3 columns)
| Metric | Unit | Meaning | FY Range |
|--------|------|---------|----------|
| **Average Price** | EUR/unit | Price per unit | FY2016-FY2025 |
| **Average Price Growth vs. PY** | % | Year-over-year price change | FY2016-FY2025 |
| **Average Price Index** | Index | Price indexed to base | FY2016-FY2025 |

**Example Data**:
```
Category Total (ALL MANUFACTURERS):
FY 2016: €3.42/unit
FY 2017: €3.48/unit  (Growth: +2.16%)
FY 2018: €3.61/unit  (Growth: +1.70%)
FY 2025: €6.25/unit  (Growth: +5.60%)

Index: 100 (constant) = indexed to base year

Beiersdorf (Competing manufacturer):
FY 2016: €7.21/unit  (Premium to category)
FY 2025: €3.65/unit  (Discount to category)
Growth: -10.99% YoY (declining price strategy)
Price Index: 58.3 (down from 210.9 in FY2016)
```

#### Value/Revenue Metrics (4 columns)
| Metric | Unit | Meaning | FY Range |
|--------|------|---------|----------|
| **Value** | k EUR | Total revenue in thousands EUR | FY2016-FY2025 |
| **Value Growth vs. PY** | % | Year-over-year revenue growth | FY2016-FY2025 |
| **Value Share** | % | % of category revenue | FY2016-FY2025 |
| **Value Share Development vs. PY** | bps | Basis points change in share | FY2016-FY2025 |

**Example Data**:
```
Category Total:
FY 2016: €2,771,595k
FY 2025: €5,426,580k
10-Year CAGR: ~7.8%

YoY Growth:
FY 2016-17: +3.9%
FY 2017-18: +5.0%
FY 2019-20: -3.2% (Category contraction - COVID?)
FY 2020-21: +11.5% (Recovery)
FY 2024-25: +6.3% (Slowing growth)

Beiersdorf Share:
FY 2016: 0.0008% (negligible)
FY 2025: 0.0005% (shrinking)
Share Development: -0.02 bps (lost share YoY)
```

#### Volume/Units Metrics (4 columns)
| Metric | Unit | Meaning | FY Range |
|--------|------|---------|----------|
| **Volume** | unit | Total units sold | FY2016-FY2025 |
| **Volume Growth vs. PY** | % | Year-over-year unit growth | FY2016-FY2025 |
| **Volume Share** | % | % of category units | FY2016-FY2025 |
| **Volume Share Development vs. PY** | bps | Basis points change in unit share | FY2016-FY2025 |

**Example Data**:
```
Category Total Volume:
FY 2016: 811M units
FY 2025: 868M units
10-Year Growth: +7.0%

YoY Volume Growth:
FY 2016-17: +2.2%
FY 2016-20: -9.2% (Major decline - pandemic impact)
FY 2020-21: +0.4% (Slow recovery)
FY 2024-25: +0.7% (Mature/saturated market)

Volume vs Value Comparison:
Value Growth (+6.3%) > Volume Growth (+0.7%)
→ Price-driven revenue growth, not unit growth
→ Category experiencing pricing power / inflation pass-through
```

### D. Period Completeness (1 column)
| Column | Type | Values | Purpose |
|--------|------|--------|---------|
| **Period Completeness for FY 2025** | % | 100 | Data freshness indicator |

---

## Long-Term Trend Analysis (10-Year View)

### Category Evolution (FY 2016 - FY 2025)

**Revenue Trajectory**:
```
€2.77B (FY2016) → €2.88B → €3.02B → €3.22B → €3.12B (COVID) 
→ €3.48B (Recovery) → €4.09B → €4.60B → €5.10B → €5.43B (FY2025)

CAGR: +7.8%
Peak-to-Trough: -3.2% (FY2019→FY2020)
```

**Unit Volume Trajectory**:
```
811M (FY2016) → 828M → 839M → 843M → 766M (COVID)
→ 768M → 821M → 840M → 862M → 868M (FY2025)

CAGR: +0.7%
Peak-to-Trough: -9.2% (FY2019→FY2020)
```

**Price Evolution**:
```
€3.42/unit (FY2016) → €3.48 → €3.61 → €3.82 → €4.07 → €4.52
→ €4.98 → €5.47 → €5.92 → €6.25 (FY2025)

CAGR: +7.0%
Consistent inflation: Every year 1.7%-11.1% growth
```

### Key Findings

**1. Divergence: Price-Driven Growth**
```
Revenue CAGR (+7.8%) >> Unit Volume CAGR (+0.7%)
→ Category driving revenue through PRICING, not volume
→ Mature market (units flat/declining)
```

**2. COVID Impact (FY2020)**
```
Revenue: -3.2% (modest decline)
Volume: -9.2% (significant contraction)
Price: Increased (+6.5%)
→ Consumers bought less, but paid more
```

**3. Post-COVID Recovery**
```
FY2020→FY2021: Revenue +11.5%, Volume +0.4%
→ Strong pricing power during recovery
→ Units didn't bounce back; prices did
```

**4. Recent Slowdown (FY2024→FY2025)**
```
Revenue Growth: 8.2% → 6.3% (declining)
Volume Growth: 2.6% → 0.7% (declining)
Price Growth: 5.6% (stable)
→ Growth momentum slowing
→ Category maturity evident
```

---

## Manufacturer-Level Competitive Dynamics

### Example: Beiersdorf (Nivea) Performance

**Price Strategy Over 10 Years**:
```
FY 2016: €7.21/unit (210% of category average)
FY 2025: €3.65/unit (58% of category average)
Change: -49.4% price reduction (10-year decline)

Interpretation:
- Started as ultra-premium (210% premium)
- Now positioning as value/discount (58% of category)
- Aggressive downward pricing strategy
```

**Revenue & Volume**:
```
Value:
FY 2016: €22k EUR
FY 2025: €27k EUR (only +23% growth vs category +96%)
Share: 0.0008% → 0.0005% (LOST SHARE)

Volume:
FY 2016: 3,070 units
FY 2025: 7,480 units (+144% units)
BUT: Revenue only +23%
→ Selling more units at much lower price
→ Not value accretive
```

**Business Model Shift**:
- Premium/specialty → Volume/budget
- Declining market share despite unit growth
- Margin compression evident

---

## Competitive Intensity Metrics

### Value Share Concentration

```
Category TOTAL:
Value Share: 100% (by definition)
Value Share Development: 0 bps (balanced set)

Beiersdorf:
Value Share: 0.0008% (FY2016) → 0.0005% (FY2025)
Trend: DECLINING share

Implication:
- Beiersdorf is a minor player (<0.1% share)
- Other manufacturers (P&G, Unilever, etc.) own ~99.9%
- Highly concentrated market
```

### Price Positioning

```
Category Average: €6.25/unit (FY2025)

Premium Players: € 7-8 (11-28% premium)
Mid-Market Players: € 5-6 (similar to category)
Value Players: € 2-4 (36-68% discount)

Beiersdorf: €3.65 (discount to category average)
→ Competing in value/mass-market segment
```

---

## Data Role in Analytical Engine

### Unique Value: Historical Trend Baseline

**GDD, Penetration Panel, BGS**:
- Recent data (current/recent MAT, monthly)
- Tactical decisions
- Immediate anomaly detection

**Category Trended**:
- 10-year historical context
- Structural trend identification
- Long-term trajectory
- Seasonal/cyclical pattern baseline

### Use Cases

**1. Anomaly Detection with Context**
```
GDD shows: Revenue ↓ 5% YoY

Without Category Trended:
→ Is this an anomaly?

With Category Trended:
→ 10-year CAGR +7.8%, recent slowdown to +6.3%
→ 5% decline is WORSE than trend
→ TRUE ANOMALY: Below historical trajectory
```

**2. Growth Decomposition**
```
Recent Revenue ↓ 3%
Volume ↓ 2%
Price ↓ 1%

Historical Context:
- Category grows 7.8% CAGR through PRICING
- But volume growth slowing (2.6% → 0.7%)
- Unit decline accelerating

Insight: Category entering contraction phase
→ Price increases alone can't offset volume loss
```

**3. Competitive Positioning Over Time**
```
Competitor A gaining share this year

10-Year View:
- FY2016: 15% share
- FY2020: 18% share (peak)
- FY2025: 12% share (declining from peak)

Insight: Recent gains are tactical bounce
→ Long-term position is deteriorating
→ Watch for further declines
```

---

## Data Quality & Characteristics

### Completeness
- **Revenue metrics**: 100% complete (FY2016-FY2025)
- **Volume metrics**: 100% complete
- **Price metrics**: 100% complete
- **All years populated**: No gaps
- **All manufacturers represented**: Comprehensive

### Grain & Coverage
```
Rows: 1,277
Manufacturers: ~15-20 (Beiersdorf, P&G, Unilever, etc.)
Brand Positions: ~5 global/regional
Brands: ~40-50 individual brands
Metrics: 12 (price, value, volume + growth + share + change)
Years: 10 (FY2016-FY2025)

Estimated: 20 × 5 × 50 × 12 = 60,000 potential cells
Actual: 1,277 rows

Reason: Only key hierarchy levels tracked
(All Mfg, Mfg only, Mfg+Brand Position, Mfg+Brand)
```

### Data Freshness
- **Report Date**: June 2026
- **Latest Year Populated**: FY 2025 (100% complete)
- **Lag**: ~6 months from FY end

---

## Alignment with Analytical Engine

### Can Provide
✓ **Historical baseline** for anomaly thresholds
✓ **10-year trend** for pattern identification
✓ **Structural growth decomposition** (price vs. volume)
✓ **Competitive benchmarking** over long term
✓ **Cyclical/seasonal patterns** (though annual granularity limits seasonality)

### Cannot Provide (by Design)
✗ **Weekly/monthly granularity** (annual data only)
✗ **Distribution/channel detail** (category-level only)
✗ **Household penetration** (not panel data)
✗ **Brand health perception** (not consumer tracking)
✗ **Recent short-term anomalies** (10-year smoothing)

---

## Integration with 4-Layer Intelligence Model

### Complete Data Stack

```
Layer 1: Weekly POS (GDD)
├─ Recent operational data
├─ Channel/retailer detail
├─ Short-term anomalies
└─ Real-time alerts

Layer 2: Monthly Household (Penetration Panel)
├─ Consumer behavior
├─ Loyalty signals
├─ Penetration reach
└─ Monthly insights

Layer 3: Monthly Brand Health (BGS)
├─ Perception & awareness
├─ Emotional connection
├─ Preference trends
└─ Brand equity

Layer 4: Annual Category (Category Trended) ← NEW
├─ 10-year historical baseline
├─ Structural trends
├─ Cyclical patterns
└─ Long-term trajectory
```

### Combined Intelligence

**Example Scenario:**

```
Current Observation (Week 25, FY2025):
GDD: Revenue ↓ 4% WoW
BGS: Awareness ↓ 2% from prior month
Penetration Panel: Penetration ↓ 1pp from prior month

Interpretation (With Category Trended):
- Category 10-year CAGR: +7.8%
- FY2024-25 trend: +6.3% (already slowing)
- FY2025 trajectory: On pace for ~6% annual growth

Insight:
"Recent 4% weekly decline is NORMAL VARIANCE
within slowing category trend, not an anomaly.
However, brand awareness AND penetration
both declining suggests losing share
in this high-growth base. Monitor closely."

Recommendation:
- Not an emergency (fits category slowdown)
- BUT requires share-defense actions
- Don't over-react to short-term variance
```

---

## Recommended Use in MVP

### Phase 1: Engines 1-5 (Primary: GDD)
- Use weekly GDD for operational anomalies
- Reference Category Trended for 10-year baseline
- Calculate Z-scores using historical volatility

### Phase 2: Cross-Source Insights
- Compare current GDD trends to 10-year category trends
- Identify true anomalies (outliers beyond historical pattern)
- Validate seasonal/cyclical expectations

### Phase 3: Root Cause Analysis
- Use category trend to frame "is this structural or tactical?"
- Different actions for structural decline vs. tactical variance
- Competitive positioning context over long term

---

## Summary Table: All 4 Data Layers

| Aspect | GDD POS | Penetration Panel | BGS Brand Health | Category Trended |
|--------|---|---|---|---|
| **Time Span** | 3 periods (MAT) | 3 periods (MAT) | Single snapshot | 10 years |
| **Granularity** | Weekly | Monthly | Monthly/Quarterly | Annual |
| **Rows** | 281 | 2,129 | 1,074 | 1,277 |
| **Primary Insight** | What happened at retail | Who bought & how much | Why consumers buy | Long-term trajectory |
| **Best For** | Operational anomalies | Household retention | Brand positioning | Structural trends |
| **Data Freshness** | Current MAT | Current MAT | 1-2 months old | ~6 months old |
| **Completeness** | 90%+ | 85%+ | ~50% | 100% |
| **Channel Detail** | ✓ Yes (5 types) | ✗ No | ✗ No | ✗ No |
| **Household Level** | ✗ No | ✓ Yes | ✗ No | ✗ No |
| **Brand Perception** | ✗ No | ✗ No | ✓ Yes | ✗ No |
| **Historical Context** | Implicit | Implicit | None | ✓ Yes |
| **Competitive Set** | By retailer | All brands tracked | All brands | All manufacturers |

---

## Key Insight: Category Context is CRITICAL

**Without Category Trended**:
- A 3% decline looks alarming
- Every metric fluctuation is treated as anomaly
- No baseline for "is this normal variance?"

**With Category Trended**:
- Historical CAGR +7.8%, recent slowdown to +6.3%
- 3% decline in slowing market is worse than at-trend
- But less severe than in growth market
- Flags structural shift (category entering maturity)

---

## Recommendation

✓ **All 4 layers NEEDED for comprehensive intelligence**

- **GDD**: Immediate operational action (this week/month)
- **Penetration Panel**: Customer retention tracking (monthly)
- **BGS**: Brand reputation (monthly strategic)
- **Category Trended**: Market context & baseline (annual/structural)

**Order of MVP Integration**:
1. GDD (foundation, high detail, recent data)
2. Penetration Panel (cross-check, household insights)
3. BGS (root cause, brand context)
4. Category Trended (baseline, long-term pattern)

