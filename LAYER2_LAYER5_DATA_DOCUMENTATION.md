# Extended Data Layers Documentation (Layers 2-5)
## US Deodorant Category - Synthetic Data

**Creation Date**: September 2026  
**Data Coverage**: September 7 - September 28, 2026 (4 weeks)  
**Geographic Scope**: United States  
**Category Focus**: Deodorant & Fragrances  
**Brands Included**: Dove, Degree, Secret, Old Spice, Native, Rexona, Axe, Gillette, Speed Stick, Mitchum, Suave, Great Value

---

## Layer 2: E-Commerce Data (ecommerce_deo_us.csv)

### Purpose
Track online marketplace dynamics: pricing, availability, conversion, reviews, and competitive positioning across e-commerce channels.

### File Structure: 505 rows × 19 columns

#### Dimensions
```
├─ Time: week_ending_date (weekly grain)
├─ Channel: marketplace (Amazon, Walmart, Target, Walgreens)
├─ Product: brand_name, format_type (Aerosol, Stick, Gel, Roll-On)
└─ Geography: Implicit US national aggregation
```

#### Key Metrics
```
Pricing Layer:
├─ online_price_usd: Listed price on marketplace
├─ retail_price_usd: In-store retail price (baseline)
├─ price_gap_pct: Online vs retail differential (negative = cheaper online)
└─ Insight: Identifies e-commerce pricing power by brand/format

Availability Layer:
├─ online_availability_pct: % of warehouses with stock
├─ inventory_days_supply: Estimated days until stockout
└─ Insight: Early indicator of demand/supply imbalances online

Conversion Layer:
├─ units_sold_online: Weekly online sales volume
├─ online_conversion_rate: % of site visitors → purchase
└─ Insight: Format/brand preferences differ online vs offline

Review & Reputation:
├─ customer_rating: Aggregate review score (1-5)
├─ review_count: Number of reviews accumulated
└─ Insight: Quality perception proxy; review velocity indicates category interest

Search & Discoverability:
├─ brand_mentions: Brand mentions in comments/reviews
├─ search_volume_index: Relative search interest (100 = baseline)
├─ traffic_rank: Brand ranking by marketplace traffic
├─ category_rank: Rank within deodorant category
└─ Insight: Leading indicator of consumer interest & awareness

Competitive Position:
├─ rank: Absolute position (1 = #1 on marketplace)
└─ Insight: Market share proxy; ranking shifts signal threat/opportunity
```

### Key Findings (Week of 09/28)
- **Dove** dominates e-commerce across formats (traffic rank 2, category rank 1)
- **E-commerce price gaps wider than retail**: Walgreens shows 0-5% gaps; Amazon/Walmart -9 to -16%
- **Gel format emerging online**: Dove Gel converting at 3.7%, above Aerosol (3.5%)
- **Online inventory tightness**: Most brands show 22-52 days supply; stock pressure evident
- **Great Value (Walmart private label) strong**: 2.3K+ aerosol units/week at 4.5% conversion

### Integration Point
**Phase 2 Use**: Refine price pressure threats with online-specific pricing gaps  
**Phase 3 Use**: Validate format shift signals with online format conversion differences

---

## Layer 3: Competitive Intelligence (competitive_deo_us.csv)

### Purpose
Track competitor actions: pricing, promotions, distribution, SKU innovation, media spend to explain market shifts.

### File Structure: 110 rows × 23 columns

#### Dimensions
```
├─ Time: week_ending_date (weekly grain)
├─ Geography: market (New York, Los Angeles, Chicago, Houston, Phoenix, etc.)
├─ Our Brand: Dove (baseline for all comparisons)
├─ Competitor: 10+ brands tracked (Degree, Old Spice, Secret, Rexona, Axe, etc.)
└─ Channel: Retailer + channel combination (Walmart Grocery, Target Mass Merch, etc.)
```

#### Key Metrics

```
Pricing Dynamics:
├─ competitor_price: Competitor brand ASP
├─ our_price: Dove price in same market/channel
├─ price_gap_pct: % difference (positive = competitor more expensive)
└─ Insight: Identifies pricing attacks; threshold >10% = CRITICAL threat

Promotional Activity:
├─ competitor_promotion_flag: 1 = promo active, 0 = no promo
├─ promo_type: Buy One Get One, Bundle, Loyalty Bonus, Clearance, etc.
├─ promo_discount_pct: Effective discount % to consumer
├─ promo_duration_days: How long promo runs
└─ Insight: Explains short-term volume swings; extended promos = competitive pressure

Distribution Battle:
├─ competitor_distribution_pct: % of stores carrying competitor
├─ our_distribution_pct: Dove distribution in market
├─ distribution_gap_pct: Store availability gap (positive = we have more)
└─ Insight: Distribution loss <-5pp signals retail partnership risk

Innovation Pipeline:
├─ competitor_new_sku_launch: 1 = new SKU launched, 0 = existing
├─ sku_description: Product name (e.g., "Old Spice Swagger Spray")
└─ Insight: New SKU launches often precede market share gains

Marketing Offensive:
├─ competitor_media_spend_usd: Weekly ad spend estimate
├─ our_media_spend_usd: Dove media spend for comparison
├─ media_spend_gap_pct: Relative investment (positive = they spend more)
└─ Insight: Share of voice gap correlates with awareness decline

Competitive Outcome:
├─ competitive_win_loss_flag: 1 = won market, 0 = lost market
├─ win_loss_category: Reason (Pricing, Distribution, Innovation, Loyalty)
└─ Insight: Classification of threat type for signal prioritization
```

### Key Findings (Week of 09/28)
- **Price wars evident**: Old Spice -10.9%, Rexona -23.2%, Speed Stick -32.2% vs Dove
- **Promotion intensity increasing**: 15/29 competitors running promotions (52% promo rate)
- **Native gaining distribution fast**: +2.7pp weekly in Philadelphia; innovation launch driving (refillable)
- **Competitor media spend rising**: Degree +2-6% gap vs Dove each week; aggressive push
- **New SKU launches accelerating**: 5 new competitor SKUs week of 09/28 (Gillette, Native, Old Spice)

### Integration Point
**Phase 2 Use**: Amplify price pressure threats with competitor action timing  
**Phase 3 Use**: Distinguish brand-specific threats from competitive offensive patterns

---

## Layer 4: Social Voice & Sentiment (social_voice_deo_us.csv)

### Purpose
Track consumer sentiment, brand mentions, trends, and quality signals across social platforms (Twitter, Instagram, Reddit, TikTok).

### File Structure: 300 rows × 20 columns

#### Dimensions
```
├─ Time: week_ending_date (weekly grain)
├─ Platform: Twitter, Instagram, Reddit, TikTok (4 platforms × 6-8 brands)
├─ Brand: Dove, Degree, Secret, Old Spice, Native, Rexona
└─ Sentiment: Quantified -1.0 to +1.0 scale
```

#### Key Metrics

```
Sentiment & Perception:
├─ sentiment_score: -1.0 (very negative) to +1.0 (very positive); 0 = neutral
├─ mention_count: Volume of brand mentions (weekly aggregate)
├─ impression_count: Reach (how many people saw mentions)
├─ engagement_rate: % of impressions that drove engagement (likes/comments/shares)
└─ Insight: Sentiment >0.70 = strong brand health; <0.65 = warning signs

Quality & Satisfaction Signals:
├─ consumer_complaints_count: Number of complaints/negative comments
├─ positive_reviews_pct: % of reviews/mentions favorable
├─ negative_reviews_pct: % of reviews/mentions unfavorable
├─ product_quality_score: Aggregated rating based on comments (1-5)
└─ Insight: Quality score <4.4 correlates with loyalty erosion; >4.7 = strong

Emerging Trends & Themes:
├─ trending_hashtags: Popular tags (e.g., #NaturalDeodorant, #CleanBeauty)
├─ eco_concern_mentions: Count of eco-related discussions
├─ price_concern_mentions: Count of price/affordability mentions
├─ format_preference_trend: Which formats trending (Aerosol vs Stick etc.)
├─ key_themes: Main consumer talking points
└─ Insight: Hashtag velocity indicates emerging consumer priorities

Influencer Activity:
├─ influencer_posts: Number of influencer/creator posts
├─ influencer_reach: Combined follower reach of influencer posts
└─ Insight: Influencer reach >5M/week = significant awareness driver

Platform-Specific Patterns:
├─ Twitter: News, opinions, real-time reactions; sentiment most volatile
├─ Instagram: Visual storytelling, lifestyle, aspirational; brand control high
├─ Reddit: Authentic opinions, niche communities, eco/value discussions; sentiment predictive
├─ TikTok: Viral trends, younger demographic, UGC; engagement highest but variable
└─ Insight: Format shifts toward Aerosol/Gel evident in TikTok first
```

### Key Findings (Week of 09/28)
- **Native leading in sentiment**: 0.75 average vs Dove 0.69; eco-positioning resonates
- **Eco concern acceleration**: Native mentions 101 (week 09/28) vs 45 (week 09/07); +124% increase
- **Stick format under fire**: Negative mentions rising (14-15% negative vs 12% earlier); format shift confirmed
- **Secret loyalty strong**: 0.71 sentiment stable; female audience large (48K+ weekly mentions)
- **TikTok driving format trends**: Gel engagement +40% week-over-week; younger demo leading

### Integration Point
**Phase 3 Use**: Validate format shift threat with social trend data  
**Phase 3 Use**: Diagnose awareness decline (social volume + sentiment + mentions)  
**Phase 3 Use**: Identify structural vs tactical shifts (eco-trends vs price wars)

---

## Layer 5: Macro Context (macro_context_deo_us.csv)

### Purpose
Track economic indicators, regulatory changes, market consolidation, and structural category trends affecting demand and competition.

### File Structure: 100 rows × 19 columns

#### Dimensions
```
├─ Time: week_ending_date (weekly grain)
├─ Scenario: Baseline, Post-Inflation, Economic Concern, Competitive Pressure, Social Trends
│   (5 scenarios × 4 weeks = 20 rows per scenario; multiple scenarios per week)
└─ Scope: US national macro conditions
```

#### Key Metrics

```
Economic Indicators:
├─ inflation_rate_pct: CPI inflation (trend: 3.8% → 4.1% over month)
├─ consumer_confidence_index: Conference Board index (trend: 102.5 → 100.0 declining)
├─ unemployment_rate_pct: Labor force unemployment (trend: 4.2% → 4.5% rising)
├─ retail_sales_growth_pct: Monthly retail growth (trend: -1.2% → -2.1% weakening)
└─ Insight: Consumer confidence declining; trading down behavior expected

Consumer Behavior Shifts:
├─ consumer_value_seeking: Score indicating price-sensitivity (trend: 0.9 → 2.7 rising)
├─ disposable_income_index: Real discretionary spending (trend: 98.4 → 96.5 weakening)
├─ credit_card_spending_index: Borrowing-funded consumption (trend: 102.1 → 100.1 flat)
└─ Insight: Income pressure; consumers trading to value formats

Category Trends:
├─ category_interest_trend: Search interest trend (Stable → Declining)
├─ gender_focus_trend: Gender-specific demand shift (Neutral → Female focused)
├─ format_preference_trend: Format popularity shift (Aerosol growing, Stick declining)
├─ price_elasticity_trend: Price sensitivity change (Elastic increasing)
├─ volume_elasticity_trend: Volume response to price (negative, pressured)
└─ Insight: Female segment growing; Gel emerging; price wars escalating

Regulatory & Structural:
├─ regulatory_flag: 1 = pending regulation, 0 = none
├─ regulatory_detail: Description (e.g., "Propellant phase-out timeline 2027")
├─ market_consolidation_flag: 1 = consolidation happening, 0 = stable
├─ consolidation_detail: M&A, retailer closures, market structure changes
└─ Insight: EU propellant ban incoming; Drug consolidation peak; structural format shift

Seasonal Factors:
├─ seasonal_indicator: Seasonal context (Back to School → Seasonal Low)
└─ Insight: Demand cycles; promotional intensity peaks vary by season
```

### Key Findings (Macro Environment 09/28)
- **Economic headwinds building**: Inflation 4.1%, consumer confidence 100.0 (declining), unemployment 4.5% (rising)
- **Disposable income under pressure**: Index fell from 98.4 → 96.5; real discretionary spending weakening
- **Trading down accelerating**: Value seeking +3.5 vs baseline; consumers buying cheaper formats
- **Regulatory impact looming**: EU propellant phase-out 2027 finalized; CA packaging rules effective Q1 2027
- **Retail consolidation peak**: Drug store closures announced; market structure shifting
- **Structural format shift**: Aerosol +6% trend; Stick -5% trend; Gel emerging (volume elasticity -4.2)

### Integration Point
**Phase 3 Use**: Distinguish category-wide trends (macro) from brand-specific threats  
**Phase 3 Use**: Validate structural shifts (eco regulations, format changes) vs tactical noise  
**Phase 3 Use**: Adjust confidence scores (brand threat vs macro pressure)

---

## How These Layers Integrate with Phase 1-3 Implementation

### Phase 1 (Weeks 1-3): Layer 1 Only
- **Data Used**: GDD, Circana, Penetration Panel, BGS, Category Trended
- **Engines**: 1-4 (KPI, Trend, Anomaly, Driver)
- **Output**: Threat/opportunity signals with Layer 1 confidence scores

### Phase 2 (Weeks 4-6): Add Layers 2-3
- **Data Added**: `ecommerce_deo_us.csv`, `competitive_deo_us.csv`
- **Enhancement**: 
  - Price pressure threats refined with e-commerce pricing gaps
  - Distribution loss validated with online availability
  - Competitive timing correlation added (competitor actions → brand impact)
  - Signal confidence adjusted: +5-10% when Layer 2/3 data aligns
  
### Phase 3 (Weeks 7-9): Add Layers 4-5
- **Data Added**: `social_voice_deo_us.csv`, `macro_context_deo_us.csv`
- **Enhancement**:
  - Format shift validated with social trend velocity
  - Awareness decline diagnosis: brand-specific (Layer 4) vs category-wide (Layer 5)
  - Threats recontextualized: brand threat vs competitive offensive vs macro shift
  - Signal confidence adjusted: -5-20% if macro pressure explains signal

---

## Data Quality & Assumptions

### E-Commerce Data
- **Source Type**: Synthetic (realistic patterns)
- **Completeness**: 100% (no nulls)
- **Update Frequency**: Weekly
- **Limitation**: US aggregation only (no regional detail)
- **Validation**: Price gaps, inventory levels, conversion rates realistic per market

### Competitive Intelligence
- **Source Type**: Synthetic (realistic competitor actions)
- **Completeness**: 100%
- **Coverage**: 10 major competitors + private labels
- **Limitation**: Confidential data estimated; not actual competitor data
- **Validation**: Price actions, promotion timing, media spend ratios realistic

### Social Voice
- **Source Type**: Synthetic (realistic sentiment patterns)
- **Completeness**: 100% (no missing scores)
- **Platform Coverage**: Twitter, Instagram, Reddit, TikTok (4/9 major platforms)
- **Limitation**: Aggregate scores; not raw posts/comments
- **Validation**: Sentiment volatility, platform differences, theme consistency realistic

### Macro Context
- **Source Type**: Synthetic (realistic economic patterns)
- **Completeness**: 100%
- **Scenario Approach**: Multiple parallel scenarios showing different macro contexts
- **Limitation**: Single national view (no regional macro variation)
- **Validation**: Economic indicator relationships, regulatory timing realistic

---

## File Locations
```
D:\LangGraph\EarlyWarning_OPFIN\
├── ecommerce_deo_us.csv          [Layer 2 - E-Commerce]
├── competitive_deo_us.csv        [Layer 3 - Competitive]
├── social_voice_deo_us.csv       [Layer 4 - Social Voice]
├── macro_context_deo_us.csv      [Layer 5 - Macro Context]
└── LAYER2_LAYER5_DATA_DOCUMENTATION.md  [This file]
```

---

## Next Steps

### For Phase 2 Implementation:
1. Load `ecommerce_deo_us.csv` and `competitive_deo_us.csv` into SQLite
2. Create dimension tables: marketplace, competitor, channel
3. Build join logic: match brand × market × week across layers
4. Enhance signal classifier: add e-commerce price gap logic, competitor action timing

### For Phase 3 Implementation:
1. Load `social_voice_deo_us.csv` and `macro_context_deo_us.csv`
2. Create aggregation logic: platform-level sentiment, macro scenario selection
3. Build validation logic: does Layer 4 confirm Layer 2-3 signals?
4. Build contextualization logic: is threat brand-specific or macro-driven?

---

## Questions for Analysis
- **Price Pressure**: Widest online gap in Walmart Great Value (-15.6%); Walgreens online prices flat. Does this explain Dove losing share online?
- **Format Shift**: Gel conversion 3.7% vs Stick 3.0%; native TikTok engagement 8.4% vs Dove 8.0%. Is format shift driven by online younger demo?
- **Eco Concern**: Native eco mentions +124% month; regulations pending 2027. Is Stick format threatened structurally or just tactically?
- **Economic Impact**: Consumer confidence declining; inflation 4.1%; trading down +3.5. Will value formats (Great Value, Suave) cannibalize our premium?
- **Competitive**: Degree media spend +6% gap; Secret loyalty high (4.7 rating). Are we losing share to direct competitor offense or category shift?

