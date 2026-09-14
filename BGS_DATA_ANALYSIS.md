# BGS Data_Dummy Analysis: Brand Health Scorecard

## Dataset Overview
**File**: BGS data_dummy.xlsx  
**Sheet**: Sheet1  
**Rows**: 1,074  
**Columns**: 53  
**Data Type**: Brand Health Tracking (Kantar Panel Data)  
**Grain**: Brand × Category × Gender × Segment × Metric × Time Period  
**Time Snapshot**: Q2 2026 (Period Ending Date: 46201)

---

## Column Structure & Dimensions

### A. Time Dimensions (1 column)
| Column | Type | Values | Purpose |
|--------|------|--------|---------|
| **Period Ending Date** | Date | 46201 (Q2 2026) | Single snapshot; no time-series tracking |

**Note**: Data is a single point-in-time snapshot with NO historical trending.

---

### B. Organizational Dimensions (7 columns)
| Column | Type | Sample Values | Cardinality | Purpose |
|--------|------|---|---|---|
| **Country** | Categorical | United States of America | 1 | Geographic market |
| **New Region** | Categorical | North America | 1 | Broad region |
| **New Sub Region** | Categorical | North America | 1 | Sub-regional grouping |
| **Cluster** | Categorical | United States | 1 | Market cluster |
| **Business Group** | Categorical | Personal Care | ~3-5 | Product business group |
| **Business Unit** | Categorical | PC-North America-BG Led | ~3-5 | Business unit classification |
| **BG/IC/1UL Led** | Categorical | BG Led, IC Led, etc. | ~3 | Leadership classification |

**Insight**: All data currently from **North America / United States only**. No global or multi-market comparison.

---

### C. Product/Category Dimensions (10 columns)
| Column | Type | Sample Values | Cardinality | Purpose |
|--------|------|---|---|---|
| **Category Code** | Code | HDOF, HDOM | ~10-15 | Category identifier |
| **Kantar Category Name** | Categorical | Deodorants - Female, Deodorants - Male | ~10-15 | Kantar-defined category |
| **Category Name** | Categorical | Deodorants & Fragrances | ~5-8 | Unilever category |
| **Unilever Category Name** | Categorical | Deodorants & Fragrances | ~5-8 | Internal Unilever category |
| **Market Name** | Categorical | Deodorants | ~5 | Market segment |
| **Sector Name** | Categorical | (mostly null) | ~3-5 | Sector classification |
| **Subsector name** | Categorical | (mostly null) | ~3-5 | Sub-sector classification |
| **Study Gender Classification** | Categorical | Female, Male | 2 | Gender segment |
| **Category Code** | Categorical | HDOF, HDOM | ~20 | Category code |
| **Brand Cells** | Categorical | (varies) | ~50-100 | Specific cell identifier |

**Key Insight**: Main segmentation is **Category × Gender** (Female/Male split of Deodorants & Fragrances).

---

### D. Brand/Manufacturer Dimensions (7 columns)
| Column | Type | Sample Values | Cardinality | Purpose |
|--------|------|---|---|---|
| **UL / Competitor** | Categorical | Unilever, Competitor | 2 | Ownership: Unilever or Competitor |
| **Manufacturer ID** | ID | MK000003, MK000143, etc. | ~10-15 | Manufacturer ID |
| **Manufacturer** | Categorical | Unilever, Procter & Gamble, Colgate Palmolive, etc. | ~10-15 | Manufacturer name |
| **Brand Positioning** | Categorical | Dove, Axe, Native, Secret, Gillette, etc. | ~25-30 | Brand positioning name |
| **Brand Name** | Categorical | Dove, Dove Men+Care, Axe, etc. | ~30-40 | Consumer-facing brand |
| **Power Brands** | Flag | Yes, No | 2 | Is this a power brand? |
| **DBA Top Cells** | Categorical/ID | 1, (null) | 2 | DBA top cells flag |

**Key Insight**: 
- **Unilever Brands**: Dove, Axe, Degree, Rexona, Shea Moisture (Power Brands flagged = Yes)
- **Competitor Brands**: P&G (Old Spice, Gillette, Native, Secret), Colgate (Speed Stick), Henkel (Right Guard), Church & Dwight (Arm & Hammer), Others (Lume, Mando)
- **Power Brands**: Only Unilever brands marked as Power Brands

---

### E. Metric/KPI Dimensions (7 columns)
| Column | Type | Sample Values | Purpose |
|--------|------|---|---|
| **Metric** | Categorical | Brand Health Metrics | Broad metric family |
| **Measure Type** | Categorical | Brand Tracking | Type of measurement |
| **Measure Category** | Categorical | (mostly null), Build Brand Love | Scorecard category |
| **6P Category** | Categorical | Advertising in a Shop (channel comms), PROPOSITION, Affinity | 6P pillar classification |
| **Measure / KPI** | Categorical | (varies - see below) | Specific KPI name |
| **Source** | Categorical | Brand Tracking | Data source program |
| **Supplier** | Categorical | Kantar | External data supplier |

**Available Metrics** (sample):
- Advertising in a Shop (channel comms)
- Build Brand Love (MDS PROPOSITION category)
- Affinity
- (Additional metrics implied in rows not shown)

---

### F. Time Comparison Metrics (6 columns with Significance Flags)
| Column | Type | Value | Purpose |
|--------|------|---|---|
| **MAT Q2 2024 (MAT-2)** | Numeric | e.g., 8.8, 23.91, 17.19 | Moving Annual Total 2 periods ago |
| **MAT Q2 2025 vs. MAT Q2 2023 (MAT-2 Sig)** | Flag | 0, 1 | Significance of MAT-2 change (1=significant) |
| **MAT Q2 2025 (MAT-1)** | Numeric | e.g., 13.21, 25.97, 18.21 | Moving Annual Total 1 period ago |
| **MAT Q2 2024 vs. MAT Q2 2023 (MAT-1 Sig)** | Flag | 0, 1 | Significance of MAT-1 change (1=significant) |
| **MAT Q2 2026 (MAT)** | Numeric | e.g., 15.96, 27.6, 17.84 | Current Moving Annual Total |
| **MAT Q2 2025 vs. MAT Q2 2024 (MAT Sig)** | Flag | 0, 1 | Significance of current MAT change (1=significant) |

**Example Data**:
```
Dove (Unilever) - Female Deodorants:
  MAT Q2 2024: 23.91
  MAT Q2 2025: 25.97 (sig flag = 0, not significant)
  MAT Q2 2026: 27.6  (sig flag = 0, not significant)
  
Interpretation: Dove shows growing trend (23.91 → 25.97 → 27.6) 
but year-over-year changes not statistically significant.

Lume (Others) - Female Deodorants:
  MAT Q2 2024: 5.84
  MAT Q2 2025: 9.2  (sig flag = 1, SIGNIFICANT)
  MAT Q2 2026: 9.76 (sig flag = 0, not significant)
  
Interpretation: Lume grew significantly from MAT-2 to MAT-1, 
then stabilized.
```

---

### G. Additional Classification Columns (16 columns - mostly null)
Most of these columns are **empty (null)** in the current dataset:
- SLP Classification
- Turnover Weights for Year Ago Comparison
- 2024 Baseline
- 2025 Benchmark for Decline
- 2025 Benchmark for Growth
- Current Brand Power
- Performance Classification
- Turnover Weights for Comparison vs Benchmarks
- Q2 2025 Predicted Performance
- Tertiles
- Overall Ranking
- Market Leader
- UL Market Leader
- Sig gap vs key competitor manufacturer?

**Status**: These columns are **NOT POPULATED** in this dummy dataset.

---

## Data Quality Assessment

### Completeness
| Dimension | Null % | Status |
|-----------|--------|--------|
| KPI Values (MAT metrics) | ~15% | Acceptable |
| Metric Measure | ~5% | Good |
| Brand/Category | 0% | Excellent |
| Significance Flags | ~15% | Acceptable |
| Performance Classifications | 100% | **NOT POPULATED** |
| Benchmarks | 100% | **NOT POPULATED** |

### Data Grain
```
Unique Combinations (observed):
- Categories: 2 (Deodorants-Female, Deodorants-Male)
- Brands: ~30 (mix of Unilever and Competitors)
- Metrics: ~2-3 visible (Advertising in a Shop, Build Brand Love/Affinity)
- Total Rows: 1,074

Expected Grain:
Category × Gender × Brand × Metric = 2 × ~30 × ~2-3 = 120-180 rows
Actual: 1,074 rows

Implication: Multiple rows per brand (different metrics), or 
data structure captures metric variants and measure types
```

---

## Key Findings & Insights

### 1. **Single Time Period**
- Only one snapshot (Q2 2026)
- Contains historical comparison (MAT-2, MAT-1, MAT) but NO separate time periods
- **Cannot be used for trend detection** without additional time periods

### 2. **Geographic Limitation**
- Data limited to **North America / United States only**
- No international comparison
- **Not suitable for global rollout validation**

### 3. **Limited Metrics**
- Focus on **Brand Health Tracking** (awareness, preference, affinity)
- NOT operational metrics (sales, volume, distribution, price)
- **Different data layer** from Circana POS

### 4. **Unilever vs. Competitor**
- Clear separation between Unilever brands (marked "Power Brands") and competitors
- Competitive benchmarking built-in (Native vs. Secret vs. Gillette, etc.)
- **Good for competitive positioning analysis**, not sales analysis

### 5. **Significance Flags**
- Binary flags (0/1) indicate statistical significance
- Example: Lume's 9.2 vs 5.84 growth marked as significant (1)
- **Provides confidence indicators** for analytical engine

---

## Data Role in Early Warning System

### Alignment with Product Definition
| Product Layer | Role | BGS Data Fit |
|---|---|---|
| Level 1: Business Outcomes | Revenue, Volume, Market Share | ❌ NO - Brand health metrics, not sales |
| Level 2: Business Drivers | Price, Distribution, Promotion | ❌ NO - These aren't tracked |
| Level 3: Diagnostics | Awareness, Sentiment, Competitive Position | ✓ YES - Core strength |

### Use Case: Supporting Circana POS Analysis
When Circana POS shows:
```
Revenue ↓ 8%
Volume ↓ 10%
ASP ↑ 2%
Competitor Price ↓ 12%
```

BGS data can answer:
```
"Are awareness/preference also declining?"
→ If BGS shows Brand Health ↓, supports volume loss diagnosis
→ If BGS shows Brand Health stable, suggests price/distribution issue
```

---

## Recommendations for Analytical Engine

### 1. **Don't Start Here for MVP**
- BGS data is **brand health context layer**, not foundation
- Foundation should be **Circana POS** (revenue, volume, distribution)
- Use BGS as **supporting evidence** later (Phase 2-3)

### 2. **Data Needs for MVP**
To validate analytical engines, we need:
- ✓ **Circana POS**: Weekly data with time-series (not just one snapshot)
- ✗ **BGS**: Currently single period; needs historical periods for testing
- ❌ **Neither**: Has the 5 synthetic scenarios we planned

### 3. **Synthetic Data Creation Path**
```
Approach A (Recommended for MVP):
  Create synthetic Circana POS data ← USE THIS
    → Engineer 5 test scenarios
    → Validate Engines 1-4
    → Layer in BGS as supporting signal (Phase 2)

Approach B (Not recommended yet):
  Start with BGS data analysis
    → Requires multi-period BGS data (currently single snapshot)
    → Too early in the pipeline
```

---

## Next Steps

### Immediate (MVP Foundation)
1. **Acquire/Create Circana POS Data**
   - Need historical weekly data (12-24 weeks)
   - With known patterns for testing
   
2. **Engineer 5 Test Scenarios in Circana POS**
   - Scenario 1: Distribution-driven decline
   - Scenario 2: Competitive price pressure
   - Scenario 3: Category downturn
   - Scenario 4: Growth opportunity
   - Scenario 5: Premium demand pressure

3. **Validate Engines 1-4 Against Scenarios**
   - KPI calculation
   - Trend detection
   - Anomaly detection
   - Driver decomposition

### Later (Phase 2+)
4. **Enhance BGS Data**
   - Acquire multi-period BGS data
   - Create time-series brand health tracking
   
5. **Build Evidence Chain**
   - Link Circana POS insights to BGS brand health metrics
   - Corroborate sales findings with perception data

---

## Summary Table: BGS vs. Analytical Engine Needs

| Aspect | BGS Data | MVP Needs | Status |
|--------|----------|-----------|--------|
| **Time Series** | Single snapshot | Multi-period (12-24 weeks) | ❌ Missing |
| **Operational KPIs** | Brand health only | Revenue, Volume, Price, Distribution | ❌ Missing |
| **Geographic Scope** | North America only | Multi-region for testing | ❌ Limited |
| **Grain** | Category × Gender × Brand | Brand × Category × Geography × Week | ⚠️ Partial |
| **Supporting Signals** | Awareness, Preference | Competitive, E-commerce, Social | ⚠️ One layer only |
| **Test Scenarios** | Not engineered | 5 known patterns needed | ❌ Missing |

**Conclusion**: BGS data is valuable for **Phase 2-3 corroboration** but insufficient for **MVP foundation**. Focus on Circana POS for analytical engine validation.

