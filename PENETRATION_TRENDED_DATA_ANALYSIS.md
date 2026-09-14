# Penetration Category Trended Data Analysis

## Dataset Overview
**File**: Penetreation _Data_Deo_US.xlsx  
**Sheet**: Sheet1  
**Rows**: 2,129  
**Columns**: 61  
**Data Type**: Household Panel Penetration & Purchase Behavior Data  
**Source**: Worldpanel/Kantar (Nielsen household panel)  
**Grain**: Brand × Category × Segment × Metric × Time Period  
**Geography**: North America / United States only  
**Report Period**: June 2026 (Period Ending: 46203)  
**Frequency**: Monthly (with MAT rolling periods)  
**Currency**: USD ($)

---

## Column Structure (61 columns)

### A. Time Dimensions (6 columns)
| Column | Type | Values | Purpose |
|--------|------|--------|---------|
| **Period** | Date | 46235 | Report period ID |
| **Data Period** | Date | 46174 | Data collection period |
| **Period Ending Date** | Date | 46203 | Period ending date (May 2026) |
| **Freq of Delivery** | Categorical | Monthly | Data delivery frequency |
| **Batch** | Text | P06_2026_2 | Batch identifier |
| *(Time periods in metrics)* | — | MAT-2, MAT-1, MAT, L12W | 3 rolling periods |

**Key**: Single monthly snapshot (May 2026) but contains historical 3-period rolling data (same structure as GDD).

### B. Organizational Dimensions (13 columns)
| Column | Type | Sample Values | Purpose |
|--------|------|---|---|
| **Region** | Categorical | North America | Geographic region |
| **Region Code** | Code | MHGEO0225 | Region identifier |
| **Unilever PMU** | Categorical | North America | Unilever PMU grouping |
| **Cluster** | Categorical | United States | Geographic cluster |
| **Group** | Categorical | United States | Group classification |
| **BU Type** | Categorical | BG Led Markets | Business unit type |
| **Business Unit** | Categorical | North America | Business unit |
| **Country** | Categorical | United States of America | Country |
| **COUNTRY CODE** | Code | US | Country code |
| **Business Group** | Categorical | Personal Care | Business group |
| **Business Group Code** | Code | CH1945 | Business group ID |
| **GMI Levels** | Numeric | 6 | Geographic aggregation level |
| **Pentrak** | Categorical | Level 3 | Penetration tracking level |

**Geographic Scope**: Fully United States focused.

### C. Product/Category Dimensions (11 columns)
| Column | Type | Sample Values | Cardinality |
|--------|------|---|---|
| **Category** | Categorical | Deodorants & Fragrances | ~5 |
| **CATEGORY CODE** | Code | CH1118 | Category ID |
| **Market** | Categorical | Deodorants | ~5 |
| **MARKET CODE** | Code | CH1104 | Market ID |
| **Sector** | Categorical | Deo Aerosols | ~8 |
| **Sector Code** | Code | CH0112 | Sector ID |
| **Sub Sector** | Categorical | Deodorants Female & Unisex | ~10 |
| **Sub Sector Code** | Code | #N/A! | Sub-sector ID |
| **Gender** | Categorical | Female & Unisex, Female & Unisex | 2-3 |
| **Sector Detail** | Categorical | Sector, Competition | 2 |
| **Product Form** | Categorical | Deo Aerosols | ~5 |
| **Product Classification** | Categorical | Competition, Competitor Brand | ~5 |
| **Level** | Categorical | Sector | ~5 (aggregation levels) |

**Key Insight**: Primary segmentation is **Sector × Gender** (Deo Aerosols × Female/Male).

### D. Brand/Company Dimensions (7 columns)
| Column | Type | Sample Values | Cardinality |
|--------|------|---|---|
| **UL / Comp** | Categorical | Unilever, Competition | 2 |
| **Product Classification** | Categorical | Unilever Brand, Competitor Brand, Competitor | 3 |
| **Global_Manu_Name** | Categorical | Unilever, Others, Rexona | ~20 |
| **HOLDING COMPANY CODE** | Code | MK000003, MK000399 | Company ID |
| **Brand_Pos_Name** | Categorical | Degree, Dove, Others | ~30-40 |
| **BRAND POSITION CODE** | Code | LB032, LB002 | Brand position ID |
| **Local_Brand_Name** | Categorical | Degree (female), Dove (female) | ~40-50 |
| **BRAND CODE** | Code | BH0143, BH0162 | Brand ID |
| **Power Brands** | Flag | Yes, No | 2 |

**Key Insight**: Clear Unilever vs. Competitor split; Power Brands flagged.

### E. Tracking & Classification (4 columns)
| Column | Type | Values | Purpose |
|--------|------|---|---|
| **BE Tracker** | Categorical | TRACKED | Tracking status |
| **Metric** | Categorical | Brand Health Metrics | Metric family |
| **Measure Type** | Categorical | Put People First | Measure classification |
| **Measure Category** | Categorical | Brand Performance | Category classification |
| **Focus Cells** | Flag | no, (null) | Priority cell indicator |

---

## Core KPIs: Household Panel Metrics (3 Time Periods)

### Time Periods
```
MAT-2 = 2 years ago (52-week rolling)
MAT-1 = 1 year ago (52-week rolling)
MAT   = Current (52-week rolling)

Last 12W-2 = 12 weeks from 2 periods back
Last 12W-1 = 12 weeks from 1 period back
Last 12W   = Current 12 weeks

Plus Significance Flags (1, 0, -1):
  1  = Significant growth/change
  0  = Flat/not significant
  -1 = Significant decline/negative change
```

### Penetration & Reach Metrics

| Metric | Time Periods | Meaning | Level |
|--------|---|---|---|
| **Penetration** | MAT-2, MAT-1, MAT, L12W variants | % of households that bought brand | Level 3 (Diagnostic) |
| **Buyers** | All time periods | Number of buyers/households | Level 1 (Outcome) |
| **Trips** | All time periods | Number of purchase trips/occasions | Level 2 (Driver) |
| **Frequency** | All time periods | Purchases per buyer | Level 2 (Driver) |

**Example Data**:
```
Degree Female (Unilever):
  Penetration:
    MAT-2: 4.05%
    MAT-1: 4.23% (Significance: 1 - grew significantly)
    MAT:   4.14% (Significance: -1 - declined from MAT-1)
  
  Buyers:
    MAT-2: 5,341,945
    MAT-1: 5,645,247 (Sig: 1 - grew)
    MAT:   5,604,338 (Sig: -1 - slight decline)
  
  Trips:
    MAT-2: 9,369,754
    MAT-1: 9,713,650 (Sig: 1)
    MAT:   9,806,528 (Sig: 1 - growing)
  
  Interpretation: More trips despite flat/declining penetration
  → Existing buyers buying more frequently
```

### Purchasing Behavior Metrics

| Metric | Meaning | Time Periods |
|--------|---------|---|
| **Value** | Total $ spent (USD) | MAT-2, MAT-1, MAT, L12W |
| **Volume** | Total units purchased | All periods |
| **Spend Per Buyer** | $ per buyer (revenue per customer) | All periods |
| **Spend Per Trip** | $ per purchase occasion | All periods |
| **Volume Per Buyer** | Units per buyer | All periods |
| **Volume Per Trip** | Units per trip/occasion | All periods |
| **Repeat Rate** | % of buyers who repeat purchase | All periods |
| **Loyalty Trips** | (Metric - often null) | All periods |
| **Relative Penetration** | Brand penetration vs. category | All periods |

**Example Data**:
```
Degree Female vs Competitor (Others):

DEGREE (Unilever):
  Value:
    MAT-2: $60,608,847
    MAT-1: $63,118,439 (Sig: 1)
    MAT:   $65,688,572 (Sig: 1)
  Trend: Revenue growing consistently
  
  Spend Per Buyer:
    MAT-2: $11.35
    MAT-1: $11.18 (Sig: -1)
    MAT:   $11.72 (Sig: 1)
  Trend: Price/pack stabilizing

COMPETITOR (Others):
  Value:
    MAT-2: $9,079,490
    MAT-1: $28,551,159 (Sig: 1 - HUGE GROWTH)
    MAT:   $46,208,355 (Sig: 1 - continued growth)
  Trend: Competitor growing 5-6x faster

  Repeat Rate:
    MAT-2: 17.32%
    MAT-1: 12.43% (Sig: -1 - lower loyalty)
    MAT:   15.89% (Sig: 1 - recovering)
  Trend: Consumer retention challenge
```

---

## Diagnostic Indicators

### Significance Flags
```
Values: 1, 0, -1

Example: MAT-1 Significance = 1
→ Change from MAT-2 to MAT-1 is statistically significant (growing)

Example: MAT Significance = -1
→ Change from MAT-1 to MAT is significant (declining)

Example: MAT Significance = 0
→ Change flat/not statistically significant
```

**Purpose**: Built-in statistical confidence; no need to calculate Z-scores from household panel data.

### Household Panel-Specific Metrics

| Metric | Type | Interpretation |
|--------|------|---|
| **Penetration** | % of HH universe | Market reach / adoption |
| **Relative Penetration** | Index (vs category) | Brand strength vs category average |
| **Repeat Rate** | % of buyers repeating | Customer loyalty indicator |
| **Frequency** | Purchases per buyer | Purchase intensity |
| **Loyalty Trips** | (\* often null) | Repeat purchase occasions |

**Example Insight**:
```
If Penetration ↑ but Repeat Rate ↓:
→ New buyers coming in but existing buyers churning
→ Loyalty/satisfaction issue

If Penetration stable but Frequency ↑:
→ Same buyers buying more often
→ Increased consumption/loyalty
```

---

## Data Completeness & Quality

### Null/Missing Analysis
```
Minimal nulls (< 5%):
- Company, Brand, Category fields
- Buyers, Trips, Value, Volume
- Frequency, Spend Per Buyer, Spend Per Trip

High nulls (30-50%):
- Volume Per Buyer (often not calculated)
- Volume Per Trip (often not calculated)
- Loyalty Trips (rarely populated)
- Last 12W variants (only for recent periods)

Reason: Some metrics not applicable to household panel data structure
```

### Data Grain

```
Unique dimensions:
- Brands: ~30-40
- UL vs Competitor: 2
- Sectors: ~8 (Deo Aerosols, etc.)
- Gender: 2-3
- Aggregation Levels: ~5

Expected rows: 40 × 2 × 8 × 3 × 5 ≈ 4,800
Actual rows: 2,129

Reason: Not all combinations tracked; focus on power brands 
and key competitive sets
```

---

## Key Differences: Penetration vs. POS (GDD) vs. Brand Health (BGS)

### Data Layer Comparison

| Aspect | Penetration Panel | GDD (POS Nielsen) | BGS (Brand Health) |
|--------|---|---|---|
| **Source** | Household survey | Retail POS scans | Consumer tracking |
| **What Measures** | Consumer behavior | Store sales | Brand perception |
| **Unit** | Households buying | Dollars & units sold | Awareness %, preference |
| **Grain** | Brand × Segment | Brand × Channel × Retailer | Brand × Gender |
| **Time Period** | Monthly households | Weekly retail | Monthly/Quarterly |
| **Penetration** | ✓ Yes | ✗ Implicit | ✗ No |
| **Value/Volume** | ✓ Yes (by household) | ✓ Yes (retail) | ✗ No |
| **Frequency/Loyalty** | ✓ Yes | ✗ No | ✗ No |
| **Distribution** | ✗ No | ✓ Yes (TDP, Wtd) | ✗ No |
| **Price** | Implied (spend/units) | ✓ Yes (SPPD) | ✗ No |
| **Brand Perception** | ✗ No | ✗ No | ✓ Yes |

### Complementary Roles

```
GDD (POS Data):
  "Dove sold €407M across all channels in current MAT"
  
+ Penetration Panel Data:
  "12.23% of households bought Dove in current MAT"
  
= Insight:
  Revenue per penetrated household = €407M / (12.23% × HH universe)
  
BGS (Brand Health):
  "Dove penetration health = 27.6% (brand awareness)"
  
+ Penetration Panel:
  "Actual purchase penetration = 12.23%"
  
= Insight:
  Awareness-to-action gap = 27.6% - 12.23% = 15.37pp
  → Brand awareness not converting to purchase
```

---

## Three-Layer Data Stack Summary

### Layer 1: Retail Sales (GDD)
**What**: Dollar sales, units, distribution, price at point-of-sale
**From**: Retail scanner data (Nielsen syndicated)
**Grain**: Weekly × Channel × Retailer

### Layer 2: Consumer Behavior (Penetration Panel)
**What**: Household penetration, purchase frequency, loyalty, spend per buyer
**From**: Household panel survey (Worldpanel/Nielsen)
**Grain**: Monthly × Segment × Brand

### Layer 3: Brand Health (BGS)
**What**: Brand awareness, perception, preference, emotional connection
**From**: Consumer tracking study (Kantar Brand Tracker)
**Grain**: Monthly/Quarterly × Brand × Gender

### How They Connect

```
GDD Sales ↓ 8%
    ↓
Penetration Panel Shows:
  - Penetration ↓ 2pp (fewer HH buying)
  - Frequency → (buyers staying same purchase rate)
  ↓
Driver: Penetration loss, not loyalty loss

BGS Brand Health Shows:
  - Awareness ↓ 5%
  - Preference ↓ 3%
  ↓
Root Cause: Brand losing mental availability
(awareness down → fewer people even consider it)
```

---

## Alignment with Analytical Engine

### Level 1: Business Outcomes ✓✓ COMPLETE (Household-based)
- Revenue (HH spending): ✓ Value metric
- Volume (units HH buy): ✓ Volume metric
- Market Share (household): ✓ Relative penetration
- Category Growth: ✓ Category-level metrics available

### Level 2: Business Drivers ✓ PARTIAL (Household behavior)
- Price / ASP: ✓ Implied (spend per unit)
- Distribution: ✗ NOT TRACKED (not household-facing metric)
- Promotion: ✗ NOT TRACKED (panel doesn't capture promotion exposure)
- Loyalty: ✓ Repeat rate, frequency

### Level 3: Diagnostic Indicators ✓✓ STRONG
- Penetration reach: ✓ Direct metric
- Consumer loyalty: ✓ Repeat rate
- Category context: ✓ Relative penetration index
- Purchase intensity: ✓ Frequency
- Churn signals: ✓ Penetration + Repeat Rate combined

---

## Use in Analytical Engine: Three-Source Intelligence Model

### MVP Architecture (Using All 3 Layers)

```
GDD (Retail Layer)
  Revenue ↓ 8%, Volume ↓ 10%, ASP ↑ 2%
  Distribution ↓ 5 pts
        ↓
    What happened at retail?
        ↓
Penetration Panel (Household Layer)
  Penetration ↓ 2.5 pp, Frequency ↑ 1.2 purchases
  Spend per buyer → stable
        ↓
    Why? Consumer-side insights
        ↓
BGS (Brand Health Layer)
  Awareness ↓ 5%, Preference ↓ 3%
  Repeat Rate ↓ 4 pp
        ↓
    Root cause: Brand perception issue
        ↓
INSIGHT CHAIN:
"Revenue decline driven by lost household penetration 
(-2.5pp), despite stable purchase frequency per buyer. 
Brand awareness deteriorating (-5%), suggesting reduced 
mental availability. Recommendation: Amplify brand 
communications to rebuild awareness and re-acquire 
lapsed households."
```

---

## Data Quality Assessment

| Dimension | Quality | Status |
|-----------|---------|--------|
| **Completeness** | 85%+ | Excellent (some metrics legitimately null) |
| **Grain Consistency** | High | Well-defined segments |
| **Significance Flags** | Present | Built-in statistical rigor |
| **Time-Series** | 3 periods | Good for trend analysis |
| **Brand Coverage** | ~40 brands | Sufficient for competitive analysis |
| **Geographic Scope** | North America only | Consistent with GDD & BGS |

---

## Recommended Use in MVP

### Phase 1: Engines 1-5 (Primary: GDD)
- Use GDD as primary data source
- Reference Penetration Panel for household-level validation
- Validate GDD insights against household trends

### Phase 2: Cross-Source Insights (Add Penetration Panel)
- Combine GDD + Penetration Panel for complete view
- Example: GDD shows Volume ↓, Panel shows Penetration ↓
  → Confirm: Volume loss due to lost customers, not reduced repeat rate

### Phase 3: Root Cause Deep-Dive (Add BGS)
- Use BGS to explain WHY penetration changed
- Triangulate: GDD (what) + Panel (who) + BGS (why)

---

## Size & Coverage

| Metric | Value | Assessment |
|--------|-------|-----------|
| **Rows** | 2,129 | Comprehensive coverage |
| **Columns** | 61 | Rich household-level metrics |
| **Time Periods** | 3 rolling (MAT-2, MAT-1, MAT) | Good for trend validation |
| **Brands** | ~40 | Full competitive set covered |
| **Segments** | 8 (by sector/gender) | Detailed segmentation |
| **Data Freshness** | May 2026 | Current/recent |
| **Completeness** | 85%+ | Very good |

---

## Summary: Penetration Panel Role in MVP

**✓ YES - Ready for Phase 2 (Cross-Source Validation)**

### What It Adds
1. **Household-level perspective** — Who is buying?
2. **Loyalty diagnostics** — Repeat rate tells us if it's retention or acquisition problem
3. **Penetration reach** — Market access from household perspective
4. **Frequency insights** — Purchase intensity per buyer
5. **Significance validation** — Built-in statistical confidence

### What It Can't Do (Alone)
- Can't diagnose channel-specific issues (no channel detail)
- Can't measure distribution loss (retail-side metric)
- Can't show promotion effectiveness (panel doesn't track promo exposure)
- Can't explain brand perception (use BGS for that)

### When to Add to MVP
**After Engines 1-5 validate on GDD**, use Penetration Panel to:
- Confirm that GDD revenue decline is driven by penetration loss vs. reduced repeat rate
- Validate relative penetration trends
- Support early warning classifications (e.g., "Losing Penetration" alert)

