# Early Warning OPFIN System - Analysis Findings Summary

**Date:** September 14, 2026  
**Project:** LangGraph Early Warning System  
**Scope:** Comprehensive deep-dive analysis of 5 primary data source analyses and 8 calculated signals

---

## Executive Summary

The Early Warning OPFIN system processes **5 primary documented analyses** (GDD Nielsen, Circana, Penetration Panel, BGS Brand Health, Category Trended) plus **4 integration data sources** to produce **8 calculated signals** that alert on competitive threats and market opportunities.

**Key Findings:**
- ✅ **8 signals** active and calculating correctly (Price War, Format Crisis, Gel Opportunity, Distribution Loss, Promo Dependency, Competitor Innovation, Rating Crisis, Quality Complaints)
- ⚠️ **Only 3 of 9 data sources actively feeding signals**: Circana, E-Commerce, Social Voice (GDD Nielsen, Penetration Panel, BGS Brand Health, Category Trended, Macro Context currently unused)
- 🔴 **GDD Nielsen configured but broken**: File format mismatch (code expects .csv, actual file is .xlsx) prevents loading
- 🔴 **Critical data quality issue**: Gel Opportunity "+12% YoY" growth is hardcoded; actual data shows -22% decline

---

## The 5 Primary Analyses

| # | Analysis | Data File | Rows | Purpose | Phase | Status |
|---|----------|-----------|------|---------|-------|--------|
| 1 | **GDD Nielsen POS** | gdd_nielsen_pos.csv | 281 | WHAT happened at retail | 1 | ❌ Not loading |
| 2 | **Circana Category** | circana_1000_rows_dummy.csv | 1,000 | Category scenario testing | 1 | ✅ Active |
| 3 | **Penetration Panel** | penetration_panel.csv | 2,129 | WHO bought & loyalty | 2 | ⏸️ Configured, unused |
| 4 | **BGS Brand Health** | bgs_brand_health.csv | 1,074 | WHY consumers chose | 2 | ⏸️ Configured, unused |
| 5 | **Category Trended** | category_trended.csv | 1,277 | STRUCTURAL trends | 3 | ⏸️ Configured, unused |

**Integration Sources** (4 additional layers):
- E-Commerce (`ecommerce_deo_us.csv`) - ✅ Active
- Competitive Intelligence (`competitive_deo_us.csv`) - ✅ Active
- Social Voice (`social_voice_deo_us.csv`) - ✅ Active
- Macro Context (`macro_context_deo_us.csv`) - ⏸️ Unused

---

## The 8 Calculated Signals

| Signal | Type | Data Sources | Active? | Critical Issue |
|--------|------|--------------|---------|---|
| **1. Competitive Price War** | Critical | Circana, Competitive | ✅ YES | None |
| **2. Format Crisis** | Warning | Circana | ✅ YES | None |
| **3. Gel Opportunity** | Opportunity | E-Commerce, Social | ✅ YES | 🔴 **"+12% YoY" hardcoded** |
| **4. Distribution Loss** | Critical | Circana | ✅ YES | ⚠️ Missing GDD Nielsen validation |
| **5. Promo Dependency** | Warning | Circana | ✅ YES | ⚠️ Missing GDD Nielsen validation |
| **6. Competitor Innovation** | Warning | Competitive | ✅ YES | None |
| **7. Online Rating Crisis** | Critical | E-Commerce, Social | ✅ YES | None |
| **8. Quality Complaints** | Critical | Social Voice | ✅ YES | None |

---

## Critical Findings

### 🔴 Finding 1: GDD Nielsen Data Not Loading

**Issue:** GDD Nielsen is configured in the system but **completely unused** due to file format mismatch.

**Evidence:**
- Backend code (`app.py` line 40): Expects file named `gdd_nielsen_pos.csv` (CSV format)
- Actual file: `GDD_Dummy_Neilson.xlsx` (Excel format)
- Result: Silent load failure; data_dict never contains gdd_nielsen key
- Impact: None of the 8 signals reference this data

**Data Available But Unused:**
- 281 rows × 105 columns of weekly POS data
- Contains: revenue, volume, price, distribution, market share, promo breakdowns
- Could validate Circana data and provide multi-category baseline

**Fix Required:**
```
OPTION A: Convert GDD_Dummy_Neilson.xlsx → gdd_nielsen_pos.csv
OPTION B: Update code to load .xlsx files
OPTION C: Rename file to gdd_nielsen_pos.xlsx and update code
```

---

### 🔴 Finding 2: Gel Opportunity "+12% YoY" is Hardcoded

**Issue:** The "Gel format emerging +12% YoY" metric is **completely fabricated**, not calculated from data.

**Evidence:**
- Backend code (`app.py` line 209): `'growth_rate': '+12% YoY'` (hardcoded string)
- Actual data in Circana shows:
  - 2025 Gel Format Sales: $5,847
  - 2026 Gel Format Sales: $4,559
  - **Actual YoY: -22% DECLINE** (not +12% growth!)
- E-Commerce data only contains 2026 dates (no historical comparison)
- No YoY calculation logic exists in signal code

**Data Sources Used (Actual):**
- E-Commerce: gel_conversion (3.5%), customer_rating (4.7/5.0), units (6,679)
- Social Voice: sentiment_score (0.71-0.75 average)
- **NOT using Circana** despite claiming it as evidence source

**Impact:** Signal misleads stakeholders about Gel market opportunity

**Fix Required:**
```python
# Current (wrong):
'growth_rate': '+12% YoY'  # Hardcoded

# Should be (if using Circana):
gel_2025 = circana[circana['fiscal_year'] == 2025]['dollar_sales'].sum()
gel_2026 = circana[circana['fiscal_year'] == 2026]['dollar_sales'].sum()
growth_rate = ((gel_2026 - gel_2025) / gel_2025) * 100  # Result: -22%

# OR acknowledge as aspirational target, not data-driven finding
```

---

### 🔴 Finding 3: GDD Nielsen Could Validate Distribution & Promo Signals

**Issue:** Two critical signals (Distribution Loss, Promo Dependency) rely only on Circana data; GDD Nielsen provides multi-category baseline for validation.

**Signal 4: Distribution Loss**
- Currently uses: `circana.distribution_pct` week-over-week
- GDD Nielsen has: `distribution_pct` across multi-category portfolio
- **Gap:** No secondary validation of distribution trends
- **Value if fixed:** Cross-validate deodorant distribution against portfolio average

**Signal 5: Promo Dependency**
- Currently uses: `circana.promo_units / units_sold` ratio
- GDD Nielsen has: Detailed promo breakdown (`base_units`, `incremental_units`, `promo_lift_pct`)
- **Gap:** Single-source promo analysis; no portfolio benchmark
- **Value if fixed:** Compare deodorant promo dependency (currently ~65%) to multi-category average

---

## Signal-to-Data-Source Mapping

### Data Source Usage Matrix

```
                              Circana  E-Com  Social  Competitive  GDD Nielsen  Penetration  BGS  Category  Macro
Signal 1: Price War             ✅       ✅      ✅        ✅           ❌          ❌        ❌      ❌       ❌
Signal 2: Format Crisis         ✅       ✅      ✅        ✅           ❌          ❌        ❌      ❌       ❌
Signal 3: Gel Opportunity       ❌       ✅      ✅        ❌           ❌          ❌        ❌      ❌       ❌  (*)
Signal 4: Distribution Loss     ✅       ✅      ❌        ✅           ❌⚠️        ❌        ❌      ❌       ❌
Signal 5: Promo Dependency      ✅       ✅      ❌        ✅           ❌⚠️        ❌        ❌      ❌       ❌
Signal 6: Competitor Innov.     ❌       ✅      ✅        ✅           ❌          ❌        ❌      ❌       ❌
Signal 7: Rating Crisis         ❌       ✅      ✅        ❌           ❌          ❌        ❌      ❌       ❌
Signal 8: Quality Complaints    ❌       ✅      ✅        ❌           ❌          ❌        ❌      ❌       ❌

Legend: ✅ = Used  |  ❌ = Not used  |  ⚠️ = Should be used  |  (*) = Claims to use Circana but doesn't
```

### Active Data Sources

- **Circana** (1,000 rows): Feeds 5 signals; heavy use for operational metrics
- **E-Commerce** (505 rows): Feeds 4 signals; online conversion, ratings, format trends
- **Social Voice** (300 rows): Feeds 3 signals; sentiment, complaints, engagement
- **Competitive** (110 rows): Feeds 2 signals; price gaps, new SKU launches
- **Macro Context** (100 rows): Configured but unused

### Inactive Data Sources

- **GDD Nielsen** (281 rows): Configured, file format issue prevents loading
- **Penetration Panel** (2,129 rows): Loaded but never referenced in signal calculations
- **BGS Brand Health** (1,074 rows): Loaded but never referenced in signal calculations
- **Category Trended** (1,277 rows): Loaded but never referenced in signal calculations

---

## Sentiment Score Clarification

**Question Asked:** "How is sentiment score 2059.29 calculated?"

**Answer:** 2059.29 is **NOT a sentiment score**. It's likely a **dollar_sales value from Circana data**.

**Social Voice Sentiment Metrics:**
- `sentiment_score` column: 0.62–0.78 range (normalized to -1.0=very negative, +1.0=very positive)
- Scale interpretation: 0.65-0.75 is healthy brand sentiment
- All brands showing positive sentiment (Rexona 0.62 = warning threshold, Native 0.78 = strongest)

**Other Social Voice Numeric Columns:**
- `mention_count`: 178–4,389 (weekly volume)
- `impression_count`: 6,234–824,567 (reach/exposure)
- `engagement_rate`: 2.0%–8.4% (content resonance)
- `consumer_complaints_count`: 8–56 (issue volume)
- `influencer_reach`: 0–10.08M followers (amplification potential)

---

## Key Insights

1. **Operational System Works**: All 8 signals calculate and render correctly; no technical failures except GDD Nielsen loading

2. **Data Source Redundancy**: Only 3 of 9 data sources actively used; Penetration Panel, BGS Brand Health, Category Trended are loaded but never referenced

3. **Data Quality Risk**: Hardcoded Gel Opportunity value undermines signal credibility if discovered by stakeholders

4. **Architecture Is MVP-Grade**: Simple direct CSV load + in-memory pandas operations; no formal ETL, no validation layer, no data quality monitoring

5. **Single-Source Validation Risk**: Signals 4 & 5 (Distribution, Promo) depend entirely on Circana; no secondary validation or portfolio context

6. **File Format Mismatch Cascades**: Simple Excel→CSV conversion would unlock GDD Nielsen for two signals; 15-min fix with high value

---

## Recommendations

### High Priority (Do First)

1. **Fix GDD Nielsen File Format** (15 min effort, high value)
   - Convert `GDD_Dummy_Neilson.xlsx` → `gdd_nielsen_pos.csv`
   - OR update backend code to read .xlsx files
   - Enables validation for Signals 4 & 5 (Distribution Loss, Promo Dependency)

2. **Fix Gel Opportunity Hardcoded Value** (30 min effort, critical credibility)
   - Replace hardcoded "+12% YoY" with actual calculation from Circana
   - Show actual -22% decline OR acknowledge as aspirational target
   - Document why gel market is "opportunity" despite negative trend (e.g., format shift, online channel growth)

3. **Add Data Quality Monitoring** (1-2 hours effort, risk mitigation)
   - Verify all 9 data sources load successfully on each run
   - Log warnings if optional sources fail silently
   - Add version/freshness tracking for CSV files

### Medium Priority (Phase 2)

4. **Integrate Unused Data Sources** (planning phase)
   - Document why Penetration Panel, BGS Brand Health, Category Trended aren't used
   - Design signals that would use them (e.g., brand loyalty trend, consumer segment shifts)
   - Plan Phase 2 signal expansion

5. **Add Multi-Source Validation** (architectural improvement)
   - For Signals 4 & 5, add portfolio benchmarking from GDD Nielsen
   - Create "multi-source confidence score" instead of single-source signal
   - Document validation logic

6. **Implement Data Audit Trail** (governance)
   - Track which columns from which sources feed each signal
   - Auto-generate data lineage documentation
   - Flag when signal uses hardcoded vs. calculated values

### Low Priority (Technical Debt)

7. **Formalize ETL Pipeline**
   - Replace direct CSV load with proper ETL (Airflow, dbt, or simple scheduled job)
   - Add data validation schemas
   - Implement incremental updates instead of full reload

8. **Add Test Suite**
   - Unit tests for signal calculations
   - Data quality tests (range checks, null detection)
   - Integration tests for full pipeline

---

## System Architecture Summary

```
5 Primary Analyses (Documented)
        ↓
9 Total Data Sources (9 CSV files)
        ↓
load_and_process_data() → In-Memory DataFrames (backend/app.py:27-66)
        ↓
calculate_signals() → 8 Signal Objects (backend/app.py:68-436)
        ↓
Flask REST API (/api/signals, /api/signal/<id>, /api/evidence/<id>)
        ↓
Frontend Dashboard → Interactive Cards + Charts + Evidence Tables
        (backend/templates/dashboard.html)

Data Flow Pattern: CSV → Pandas → JSON → REST → HTML/JS
```

---

## Conclusion

The Early Warning OPFIN system is **functionally operational** with 8 active signals feeding a working dashboard. However, **three critical issues** require attention:

1. **GDD Nielsen not loading** (file format) — easy fix, high value
2. **Gel Opportunity hardcoded metric** — credibility risk, needs fixing
3. **Single-source validation** — risk mitigation, medium effort

The system has solid MVP foundations but would benefit from data quality improvements, multi-source validation, and proper ETL governance for Phase 2 expansion.

---

**Report Generated:** September 14, 2026  
**Analysis Scope:** Complete system deep-dive (3 agents, 4 findings, 8 signal mappings)  
**Status:** Ready for team review and prioritization
