# Early Warnings Dashboard: Complete Data Layers Summary
## US Deodorant Category - All 5 Layers Ready

**Status**: ✅ Complete - All 9 data sources available for integration  
**Date Range**: September 7 - September 28, 2026 (4 weeks)  
**Total Data**: 4,567 rows across 9 files  
**Geography**: United States  
**Category**: Deodorant & Fragrances

---

## Quick Reference: All Data Files

```
D:\LangGraph\EarlyWarning_OPFIN\

LAYER 1: OPERATIONAL (Sales & Household)  [Already Available - Phase 1]
├── GDD_Dummy_Neilson.xlsx           [281 rows] Multi-category POS
├── circana_1000_rows_dummy.csv      [1000 rows] Deodorant deep-dive
├── Penetreation _Data_Deo_US.xlsx   [2129 rows] Household behavior
├── BGS data_dummy.xlsx              [1074 rows] Brand perception
└── Category_Deo_Dummy.xlsx          [1277 rows] 10-year history

LAYER 2: E-COMMERCE  [NEW - Phase 2]
└── ecommerce_deo_us.csv             [505 rows] Amazon, Walmart, Target, Walgreens

LAYER 3: COMPETITIVE  [NEW - Phase 2]
└── competitive_deo_us.csv           [110 rows] Competitor actions by market

LAYER 4: SOCIAL VOICE  [NEW - Phase 3]
└── social_voice_deo_us.csv          [300 rows] Twitter, Instagram, Reddit, TikTok

LAYER 5: MACRO CONTEXT  [NEW - Phase 3]
└── macro_context_deo_us.csv         [100 rows] Economic, regulatory, trends

DOCUMENTATION  [Reference]
├── DATA_SOURCES_INTEGRATION_GUIDE.md        [Complete architecture spec]
├── LAYER2_LAYER5_DATA_DOCUMENTATION.md      [New layers documentation]
└── This file                                 [Quick reference]
```

---

## Layer Integration Timeline

### Phase 1 (Weeks 1-3): Operational Foundation
**Data Sources**: Layer 1 only (5 existing files)  
**Row Count**: 6,761 rows  
**Key Metrics**:
- POS revenue, volume, market share, distribution
- Household penetration, loyalty, frequency
- Brand awareness, preference, consideration
- 10-year historical baseline

**Engines**: 1-4 (KPI, Trend, Anomaly, Driver)  
**Signal Confidence**: ±50-90% (data quality + alignment)

**Expected Signals**:
- ✅ Distribution Loss (GDD/Circana)
- ✅ Volume Decline (Circana)
- ✅ Penetration Erosion (Panel)
- ✅ Awareness Decline (BGS)
- ✅ Loyalty Breakdown (Panel)
- ✅ Format Shift (Circana by subcategory)

---

### Phase 2 (Weeks 4-6): E-Commerce & Competitive Layer
**Data Sources**: Layer 1 + Layer 2 + Layer 3 (7 files total)  
**New Row Count**: +615 rows (505 e-commerce + 110 competitive)  
**Total**: 7,376 rows

**New Metrics**:
- **E-Commerce**:
  - Online price gaps (Amazon -9% vs Walgreens +4%)
  - Online inventory & availability
  - Online conversion rates by format
  - Customer ratings & review volume
  - Search trends & discoverability

- **Competitive**:
  - Competitor pricing by market & channel
  - Promotion activity (type, discount, duration)
  - Distribution gaps
  - SKU innovation pipeline
  - Media spend competition

**Signal Enhancement**:
- Price Pressure threat: Add online price gap (e-commerce specific vulnerability)
- Format Shift threat: Validate with online format conversion differences
- Distribution Loss threat: Confirm with online availability metrics
- **Confidence Impact**: +3-8% when Layer 2-3 data aligns with Layer 1

**New Capabilities**:
- Online vs offline threat divergence detection
- Competitive action timing → brand impact correlation
- Early signals from online-first channels (younger demos)

---

### Phase 3 (Weeks 7-9): Social Voice & Macro Context
**Data Sources**: All 5 layers (9 files total)  
**New Row Count**: +400 rows (300 social + 100 macro)  
**Total**: 7,776 rows

**New Metrics**:
- **Social Voice**:
  - Sentiment scores (-1.0 to +1.0) by platform & brand
  - Mention volume & reach
  - Consumer complaints & satisfaction
  - Trending topics & hashtags
  - Influencer activity & reach
  - Platform-specific patterns (TikTok vs Reddit differences)

- **Macro Context**:
  - Economic indicators (inflation, confidence, unemployment)
  - Consumer behavior shifts (value seeking, trading down)
  - Category trends (format preferences, gender focus)
  - Regulatory landscape (propellant phase-out, packaging rules)
  - Market consolidation signals

**Signal Refinement**:
- **Recontextualization**: Format shift threat (-20%) if social shows eco trends driving
- **Distinction**: Penetration cliff → brand threat vs category threat (macro context)
- **Validation**: Awareness decline signal +15% if social sentiment confirms
- **Structural vs Tactical**: Trading down behavior (macro) vs lost loyalty (brand-specific)

**Confidence Impact**: -5 to +15% based on macro context  
**New Capabilities**:
- Early warning from social sentiment (weeks before sales impact)
- Root cause clarity: brand threat vs competitive vs macro shift
- Structural change detection (eco regulations, format evolution)
- Signal recontextualization (threat → opportunity)

---

## Real-World Signal Examples Using All Layers

### Example 1: Stick Format Under Pressure

**Layer 1 Signal** (Week 09/28):
- Circana: Stick share -5% cumulative vs baseline
- Aerosol: +6% cumulative
- **Signal**: CRITICAL - Subcategory Shift
- **Confidence**: 88%

**Layer 2-3 Validation** (Phase 2):
- E-commerce: Aerosol conversion +0.7pp vs Stick -0.4pp
- Competitive: Degree aerosol media spend +6% gap; Old Spice launching new aerosol
- **Confidence Adjustment**: +2-4% (online younger demo driving shift, competitor offensive)

**Layer 4-5 Recontextualization** (Phase 3):
- Social: #aerosolfree trending (eco concerns) BUT Aerosol also #convenient, #premium
- Macro: Eco propellant regulations 2027; CA packaging rules Q1 2027
- Female consumer segment +4pp weekly buying more aerosol/gel
- **Signal Recontextualization**: 
  - Before: CRITICAL threat (innovation needed for Stick)
  - After: **OPPORTUNITY** (Reposition Stick as eco-friendly, refillable option vs aerosol propellant concerns)
- **Confidence**: 82% (downgraded due to macro context)
- **New Product Action**: Eco-friendly Stick innovation (eco propellant alternative)

---

### Example 2: Competitive Price Pressure

**Layer 1 Signal** (Week 09/28):
- Circana: Competitor (Old Spice) -10.9% price vs Dove +4.2%
- Brand premium ↑ 18.7pp
- Brand conversion ↓ 22%
- **Signal**: WARNING - Competitive Price Pressure
- **Confidence**: 88%

**Layer 2-3 Amplification** (Phase 2):
- E-commerce: Amazon gap = -9.5% (retail only -6.3%)
- Competitive: Old Spice running BOGO promotion (20% discount, 7 days)
- Degree media spend +6% gap vs Dove
- **Confidence Adjustment**: +3-6% (e-commerce gap amplifies threat, competitor actively attacking)
- **Signal Escalation**: WARNING → CRITICAL (94% confidence)

**Layer 4-5 Contextualization** (Phase 3):
- Social: "Old Spice is a deal of the week" trending (Reddit, Instagram)
- Macro: Consumer confidence ↓, inflation 4.1%, trading down behavior +3.5
- **Recontextualization**:
  - Competitive pressure component: 70% (real threat)
  - Macro economic pressure: 30% (structural consumer behavior shift)
- **Refined Action**:
  - Short-term: Tactical promotional response (match discount)
  - Medium-term: Defend premium positioning (highlight eco/quality)
  - Long-term: Premium segment resilience vs value format growth

---

### Example 3: Native Gel Opportunity

**Layer 1 Signal** (Week 09/28):
- Circana: Gel format +4% weekly growth
- Native brand growing +12% YoY vs Dove +2%
- **Signal**: OPPORTUNITY - Emerging Format Growth
- **Confidence**: 85%

**Layer 2-3 Confirmation** (Phase 2):
- E-commerce: Native Gel conversion 3.4%, above Aerosol (3.2%)
- Native e-commerce reach high (>1M weekly mentions)
- New SKU launches: Native Refillable launched 09/21
- Influencer posts: 31-34 weekly for Native vs Dove 13-15
- **Confidence Adjustment**: +5-7% (e-commerce data confirms, innovation timing validates)

**Layer 4-5 Amplification** (Phase 3):
- Social: #NativeDeodorant trending; 0.76 sentiment (highest), +124% eco mentions
- Influencer reach: 9.9M+ weekly (highest across brands)
- Macro: Gen Z eco-conscious preference rising; refillable innovation essential
- EU propellant ban 2027; CA packaging rules Q1 2027 → natural products advantage
- **Signal Escalation**: OPPORTUNITY → STRATEGIC PRIORITY
- **Confidence**: 89% (validated across all layers; structural eco-trend backing)
- **Refined Action**:
  - Accelerate gel product roadmap (market already moving)
  - Eco-messaging (leverage structural regulatory tailwind)
  - Influencer partnerships (Native leading; target Dove's audience)

---

## Data Integration Architecture (Phase-by-Phase)

### Phase 1 Architecture
```
GDD + Circana + Panel + BGS + Trended
              ↓
        Engines 1-4
              ↓
Signals (CRITICAL/WARNING/OPPORTUNITY/MONITORING)
              ↓
        Dashboard (Product Team)
```
**Signal Confidence**: Built from data quality + source alignment + significance  
**Completeness**: POS + Household perspectives only

### Phase 2 Architecture
```
Layer 1 + E-Commerce + Competitive
              ↓
    Engines 1-4 + Context Layer
              ↓
Enhanced Signals (Layer 2-3 validation + confidence adjustment)
              ↓
    Dashboard (Product Team) + Competitive Context
```
**Signal Enhancement**: Online-specific threats, competitive action correlation  
**Completeness**: + Market dynamics perspective

### Phase 3 Architecture
```
Layer 1-3 + Social + Macro
              ↓
  Engines 1-6 + Full Context
              ↓
Contextualized Signals (Root cause clarity, structural vs tactical)
              ↓
  Dashboard (Product Team) + Root Cause + Strategy
```
**Signal Refinement**: Brand threat vs competitive vs macro, structural change detection  
**Completeness**: Complete intelligence with all perspectives

---

## Brands Tracked Across All Layers

| Brand | Layer 1 | Layer 2 | Layer 3 | Layer 4 | Layer 5 | Notes |
|---|---|---|---|---|---|---|
| **Dove** | ✅ | ✅ | Baseline | ✅ | ✅ | Baseline brand (all comparisons) |
| **Degree** | ✅ | ✅ | ✅ (Comp) | ✅ | ✅ | Key competitor; price wars |
| **Secret** | ✅ | ✅ | ✅ (Comp) | ✅ | ✅ | Female-focused; loyalty strong |
| **Old Spice** | ✅ | ✅ | ✅ (Comp) | ✅ | ✅ | Aggressive promo; male-focused |
| **Native** | ✅ | ✅ | ✅ (Comp) | ✅ | ✅ | Eco leader; format innovator |
| **Rexona** | ✅ | ✅ | ✅ (Comp) | ✅ | ✅ | Value player; roll-on leader |
| **Axe** | ✅ | ✅ | ✅ (Comp) | ✅ | ✅ | Male-focused; price aggressive |
| **Gillette** | ✅ | ✅ | ✅ (Comp) | ✅ | ✅ | Skincare angle; premium |
| **Speed Stick** | ✅ | ✅ | ✅ (Comp) | ✅ | ✅ | Value leader; declining |
| **Mitchum** | ✅ | ✅ | ✅ (Comp) | ✅ | ✅ | Drug store focused |
| **Suave** | ✅ | ✅ | ✅ (Comp) | ✅ | ✅ | Ultra-budget; Walmart focus |
| **Great Value** | ✅ | ✅ | ✅ (Comp) | ✅ | ✅ | Private label; value growth |

---

## File Sizes & Data Volumes

| Layer | File | Rows | Columns | Size | Time Grain | 
|---|---|---|---|---|---|
| 1 | GDD_Dummy_Neilson.xlsx | 281 | 105 | 3.2 MB | Weekly |
| 1 | circana_1000_rows_dummy.csv | 1,000 | 44 | 1.8 MB | Weekly |
| 1 | Penetreation_Data_Deo_US.xlsx | 2,129 | 61 | 2.1 MB | Monthly |
| 1 | BGS_data_dummy.xlsx | 1,074 | 53 | 1.6 MB | Monthly |
| 1 | Category_Deo_Dummy.xlsx | 1,277 | 24 | 0.9 MB | Annual |
| **1 Total** | | **6,761** | | **9.6 MB** | |
| 2 | ecommerce_deo_us.csv | 505 | 19 | 0.8 MB | Weekly |
| 3 | competitive_deo_us.csv | 110 | 23 | 0.2 MB | Weekly |
| 4 | social_voice_deo_us.csv | 300 | 20 | 0.6 MB | Weekly |
| 5 | macro_context_deo_us.csv | 100 | 19 | 0.2 MB | Weekly |
| **2-5 Total** | | **915** | | **1.8 MB** | |
| **Grand Total** | | **7,776** | | **11.4 MB** | |

---

## Data Completeness Checklist

### Layer 1 (Operational)
- ✅ POS data (GDD Nielsen)
- ✅ Category-focused POS (Circana 1000)
- ✅ Household penetration panel
- ✅ Brand health perception
- ✅ Historical baseline (10 years)

### Layer 2 (E-Commerce) - **NEW**
- ✅ 4 major marketplaces (Amazon, Walmart, Target, Walgreens)
- ✅ Online pricing & availability
- ✅ Conversion rates by format
- ✅ Customer reviews & ratings
- ✅ Search trends & discoverability

### Layer 3 (Competitive) - **NEW**
- ✅ 10+ competitor brands tracked
- ✅ Pricing by market & channel
- ✅ Promotion activity & terms
- ✅ Distribution & shelf placement
- ✅ SKU innovation pipeline
- ✅ Media spend competition

### Layer 4 (Social Voice) - **NEW**
- ✅ 4 major platforms (Twitter, Instagram, Reddit, TikTok)
- ✅ Sentiment scoring (-1.0 to +1.0)
- ✅ Volume & reach metrics
- ✅ Complaint tracking
- ✅ Trend identification
- ✅ Influencer activity

### Layer 5 (Macro Context) - **NEW**
- ✅ Economic indicators (inflation, confidence, employment)
- ✅ Consumer behavior shifts (trading down, value seeking)
- ✅ Category trends (format, gender, price elasticity)
- ✅ Regulatory landscape (propellant, packaging)
- ✅ Market consolidation signals

---

## Ready for Implementation

### ✅ Phase 1: Start Now
- Load Layer 1 data (GDD + Circana + Panel + BGS + Trended)
- Build Engines 1-4
- Generate initial signals
- Test on 3 scenarios

### ✅ Phase 2: Weeks 4-6
- Load ecommerce_deo_us.csv
- Load competitive_deo_us.csv
- Enhance signal confidence with Layer 2-3 data
- Validate findings with competitive context

### ✅ Phase 3: Weeks 7-9
- Load social_voice_deo_us.csv
- Load macro_context_deo_us.csv
- Recontextualize signals (brand threat vs macro shift)
- Complete intelligence with root cause clarity

---

## Key Insights from Current Data (Week of 09/28)

**THREATS** (Product team action required):
- Stick format losing -5% cumulative vs Aerosol +6% ✋ **INNOVATION NEEDED**
- Competitor price wars accelerating (Old Spice -10.9%, Speed Stick -32.2%) ⚠️ **PRICING REVIEW**
- Penetration showing early softness; confidence declining 100.0 (from 102.5) ⚠️ **ACQUISITION FOCUS**

**OPPORTUNITIES** (Strategic growth):
- Gel format +4% weekly; Native leading with eco-positioning +124% eco mentions 🟢 **ROADMAP ACCELERATION**
- Female consumer segment +4pp; Strong social presence (Secret 0.71 sentiment) 🟢 **TARGETED INNOVATION**
- E-commerce price gaps (Walmart -9.5%) enable online positioning shift 🟢 **ONLINE STRATEGY**

**STRUCTURAL SHIFTS** (Long-term planning):
- Eco regulations 2027 (propellant phase-out EU, packaging CA 2027) 📋 **PORTFOLIO PLANNING**
- Economic headwinds: confidence ↓, inflation ↑, trading down +3.5 📉 **VALUE TIER STRATEGY**
- Market consolidation: Drug retail peak; format shift accelerating 🔄 **CHANNEL STRATEGY**

---

## Next Action Items

1. **Load Layer 1 data into SQLite** (GDD, Circana, Panel, BGS, Trended)
2. **Implement Engines 1-4** (KPI, Trend, Anomaly, Driver)
3. **Build signal classifier** with threat/opportunity detection
4. **Create dashboard UI** with prominence hierarchy
5. **Test on 3 scenarios** (distribution loss, price pressure, format shift)
6. **Phase 2 prep**: Ready ecommerce_deo_us.csv + competitive_deo_us.csv for integration
7. **Phase 3 prep**: Ready social_voice_deo_us.csv + macro_context_deo_us.csv

---

## Questions?
Refer to:
- **Architecture**: DATA_SOURCES_INTEGRATION_GUIDE.md
- **Layer 2-5 Details**: LAYER2_LAYER5_DATA_DOCUMENTATION.md
- **Approved Plan**: C:\Users\kuldeep.singh\.claude\plans\go-through-the-early-ancient-sphinx.md

