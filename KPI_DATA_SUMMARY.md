# Sales & Market Intelligence Data Model Summary

## Overview
Two complementary data sources define the Sales & Market foundation for Early Warnings & Opportunity Finder:

1. **Penetration Summary Dataset** — High-level brand health and penetration metrics
2. **Circana Synthetic CPG Dataset** — Granular point-of-sale transaction data

---

## Data Source 1: Penetration Summary (kpi_column_summary_four_datasets.xlsx)

### Purpose
Brand penetration tracking, market performance, and high-level KPI monitoring across Unilever portfolio.

### Grain
**Dimensions:**
- **Time**: Period, Data Period, Period Ending Date (frequency: Monthly, Quarterly, MAT)
- **Geography**: Region, Region Code, Country, Country Code
- **Organization**: Unilever PMU, Cluster, Group, Business Unit, Business Group, BU Type
- **Product**: Category, Category Code, Market, Market Code, Sector, Sub Sector, Gender, Product Form
- **Brand**: Global_Manu_Name, Brand_Pos_Name, Brand Position Code, Local_Brand_Name, Brand Code

### Key Metrics Structure
**Penetration Metrics** (Level 1 — Business Outcomes):
- Brand awareness
- Brand consideration
- Brand preference
- Purchase behavior (recent purchase, regular purchase)

**Comparison Timeframes:**
- MAT-2, MAT-1, MAT (Moving Annual Total)
- Last 12W-2, Last 12W-1, Last 12W (Last 12 Weeks)
- Significance flags for directional movement

**KPI Tracking Fields:**
- **Measure / KPI**: Specific metric name
- **Source**: Data source program (e.g., consumer tracking)
- **Supplier**: External panel provider (Nielsen, Kantar, etc.)
- **6P**: Internal 6P pillar classification (Product, Price, Place, Promotion, People, Purpose)
- **Measure Type**: Category/scorecard classification
- **BE Tracker**: Brand Equity tracking indicator

### Data Characteristics
- **Frequency**: Monthly, Quarterly, or MAT (Moving Annual Total)
- **Scope**: National and regional aggregation
- **Weighting**: Turnover weights at FMCG level; Brand-level weights
- **Focus**: Power Brands flagged for priority attention
- **Significance**: Statistical significance flags to identify material changes

### Alignment with Product Definition
Maps to **Level 1 & 3 KPIs** in the KPI hierarchy:
- Level 1: Market Share, Category Growth (some)
- Level 3: Diagnostic indicators (sentiment proxies, competitor position)

---

## Data Source 2: Circana Synthetic CPG Dataset (circana_kpi_summary.xlsx)

### Purpose
Point-of-Sale (POS) sales data granularity for revenue, volume, pricing, promotion, and distribution analysis at weekly intervals.

### Grain
**Week × Market × Retailer × Channel × Category × Brand × Product (SKU)**

### Key Dimensions

#### Time
- `week_id`: Synthetic week identifier
- `week_ending_date`: Calendar date
- `fiscal_year`, `fiscal_month`, `quarter`: Period classification

#### Geography
- `market_id`, `market_name`: Local market (city/metro)
- `state`: Two-letter state abbreviation
- `region`: Broad geographic region

#### Channel & Retail
- `channel_id`, `channel_name`: Retail format (Grocery, Convenience, etc.)
- `retailer_id`, `retailer_name`: Specific retailer
- `retailer_scope`: National vs. Regional scope

#### Product Hierarchy
- `category_id`, `category_name`
- `subcategory_id`, `subcategory_name`
- `manufacturer_id`, `manufacturer_name`
- `brand_id`, `brand_name`
- `product_id` (SKU), `upc`: Product identifier
- `product_description`: Human-readable product name
- `package_size`, `package_uom`: Package configuration
- `pack_count`: Multipack count

### Key Metrics

#### Volume & Sales (Level 1 — Business Outcomes)
- `units_sold`: Total packages sold
- `volume_sold`: Physical volume (unit-normalized)
- `dollar_sales`: Total sales value
- `market_share_pct`: Brand/Product share of category

#### Price & Mix (Level 2 — Driver KPIs)
- `average_unit_price`: Listed/menu price per unit
- `realized_unit_price`: Effective price after discounts
- `price_per_volume_unit`: Price normalized to volume

#### Promotion & Support (Level 2 — Driver KPIs)
- `base_units`: Baseline units (no promotion)
- `incremental_units`: Units above baseline due to support
- `promo_units`: Units under promotional conditions
- `base_dollar_sales`: Baseline sales value
- `promo_dollar_sales`: Sales value during promotion
- `is_promoted`: Binary promotion flag
- `promo_lift_pct`: % increase above baseline

#### Distribution & Access (Level 2 — Driver KPIs)
- `distribution_pct`: % of stores carrying product

#### Data Lineage
- `data_source`: Source label
- `load_timestamp`: Data freshness indicator

### Alignment with Product Definition
Maps to **ALL three KPI levels**:

**Level 1 — Business Outcomes:**
- Revenue (dollar_sales)
- Volume (units_sold)
- Market Share (market_share_pct)

**Level 2 — Driver KPIs:**
- Units (units_sold, base_units)
- ASP (average_unit_price, realized_unit_price)
- Distribution (distribution_pct)
- Promotion (promo_units, promo_dollar_sales, is_promoted)

**Level 3 — Diagnostic Indicators:**
- Competitive metrics (implicit: retailer & category context)
- Promotional pressure (promo_lift_pct)
- Channel performance (channel mix)

---

## Cross-Dataset Integration

### How They Work Together

| Penetration Summary | Circana POS | Purpose |
|---|---|---|
| Brand awareness, preference | units_sold, market_share | Align consumer intent with actual purchase behavior |
| Category growth, market trends | category performance, channel mix | Contextualize brand performance within market |
| Significance flags (↑↓) | units_sold, dollar_sales trends | Identify material changes and anomalies |
| Regional/country scope | market_name, region | Granular geographic diagnosis |
| Brand health 6P pillar | Price, Distribution, Promotion flags | Map health drivers to POS drivers |

### Data Flow for Analysis

```
Penetration Summary (Aggregate Level)
        │
        ├─→ Identify anomaly: Market Share ↓
        │
Circana POS (Detail Level)
        │
        ├─→ Disaggregate by channel, retailer, category, brand
        │
        └─→ Root cause: Distribution ↓ OR units_sold ↓ OR realized_unit_price ↑
```

---

## KPI Hierarchy Mapping

### Level 1: Business Outcomes (What Happened?)
| KPI | Penetration Summary | Circana POS |
|---|---|---|
| Revenue | Implied by brand health | **dollar_sales** ✓ |
| Volume | Purchase frequency implied | **units_sold** ✓ |
| Market Share | Not explicit | **market_share_pct** ✓ |
| Category Growth | **Category Growth metric** ✓ | Derived from category totals |

### Level 2: Business Drivers (Why Did It Happen?)
| KPI | Penetration Summary | Circana POS |
|---|---|---|
| Price / ASP | Not tracked | **average_unit_price, realized_unit_price** ✓ |
| Distribution | Not tracked | **distribution_pct** ✓ |
| Promotion | Implied in promotions 6P | **promo_units, is_promoted, promo_lift_pct** ✓ |
| Competitor Price | Not tracked | Implicit (retailer context) |

### Level 3: Diagnostic Indicators (What Could Happen Next?)
| Indicator | Penetration Summary | Circana POS |
|---|---|---|
| Competitor Activity | **6P pillar tracking** | Implicit in channel/retailer shifts |
| Search Interest | Not tracked | Not tracked — needs E-commerce layer |
| Social Sentiment | Not tracked | Not tracked — needs Social layer |
| Availability | Not tracked | **distribution_pct, channel presence** |
| Macro Context | Not tracked | Not tracked — needs Macro layer |

---

## Data Characteristics & Quality Notes

### Penetration Summary
- **Frequency**: Monthly, Quarterly, or MAT (rolling)
- **Lag**: Typically 2-4 weeks (consumer panel data)
- **Sample**: Panel-based (Nielsen, Kantar, etc.)
- **Confidence**: Weighted, with statistical significance flags
- **Scope**: National and regional aggregates
- **Maturity**: High — established tracking

### Circana POS
- **Frequency**: Weekly granularity
- **Lag**: Near real-time (1-2 weeks for syndicated data)
- **Coverage**: Multi-retailer, multi-channel (Grocery, Convenience, etc.)
- **Scope**: Market-level detail
- **Synthetic?**: Yes — the dataset is deliberately engineered for prototyping
- **Grain**: Very granular (week × market × retailer × SKU)

---

## Implementation Readiness

### Data Ready?
✓ **YES** — Both datasets have:
- Comprehensive dimension hierarchies
- Multiple time comparison periods
- Promotional and distribution flags
- Market share and competitive context

### Gaps to Address?
1. **E-commerce signals** — NOT in these datasets (marketplace price, availability, conversion)
2. **Competitive pricing** — Implicit only; need explicit competitor tracking
3. **Social/sentiment** — NOT included; needs Social Media dataset
4. **Macro context** — NOT included; needs Economic Indicators dataset
5. **Causality evidence** — Need to engineer synthetic scenarios with known root causes

### Next Recommended Steps

1. **Create synthetic scenarios** using Circana POS:
   - Scenario 1: Distribution-driven decline
   - Scenario 2: Competitive price pressure
   - Scenario 3: Category downturn
   - Scenario 4: Growth opportunity
   - Scenario 5: Premium demand pressure

2. **Build analytical engines** to process both datasets:
   - KPI calculation (Revenue = Units × ASP)
   - Trend detection (MoM, QoQ, YoY)
   - Anomaly detection (Z-score, baselines)
   - Driver decomposition
   - Relative performance (Brand vs Category)

3. **Establish cross-dataset rules**:
   - When Penetration Summary shows ↓, validate with Circana POS
   - Route POS-level detail as evidence chain
   - Track distribution, price, promotion as causal factors

4. **Prepare E-commerce, Competitive, Social layers** for Phase 2

---

## Recommended MVP Scope

**Phase 1: Sales & Market Foundation**
- Dataset: Circana POS + Penetration Summary insights
- Grain: Brand × Category × Geography × Week
- Scenarios: 3–5 engineered patterns (distribution, price pressure, category downturn)
- Output: Structured insights with evidence chains
- Success: Detect known patterns with high confidence

**Phase 2: E-commerce & Competitive**
- Add marketplace indicators and competitor pricing
- Corroborate POS findings with leading signals

**Phase 3: Social & Macro**
- Add sentiment and economic context
- Complete the intelligence model

