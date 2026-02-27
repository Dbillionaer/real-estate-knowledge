# 📊 Market Data

> This directory stores comp data, ARV notes, and market trends written by the Market Analyst agent.

## File Naming Convention

```
[ZIP-CODE]-comps-YYYY-MM.md       ← Monthly comp snapshots
[ZIP-CODE]-market-notes.md        ← Running market observations
[CITY-STATE]-trends-YYYY-Q[N].md  ← Quarterly trend reports
```

## Comp File Template

```markdown
---
zip: [ZIP CODE]
city: [City, State]
month: YYYY-MM
property_type: single-family | multi-family | condo
source: Zillow | Redfin | MLS | County Records
tags: [#market-data, #comps, #[zip-code]]
---

# Comps: [ZIP CODE] — [Month YYYY]

## Sold Comparables

| Address | Beds | Baths | Sqft | Sold Price | $/Sqft | Sold Date | Distance |
|---------|------|-------|------|-----------|--------|-----------|----------|
| | | | | | | | |

## Active Listings (for context)

| Address | Beds | Baths | Sqft | List Price | DOM | Notes |
|---------|------|-------|------|-----------|-----|-------|
| | | | | | | |

## ARV Estimate Summary

- **Median Sold $/Sqft**: $
- **Average Sold $/Sqft**: $
- **ARV Range for 1,500 sqft**: $X - $X
- **ARV Range for 2,000 sqft**: $X - $X

## Market Notes
- 
```

## Market Notes Template

```markdown
---
zip: [ZIP CODE]
city: [City, State]
last_updated: YYYY-MM-DD
tags: [#market-data, #market-notes, #[zip-code]]
---

# Market Notes: [City, State] — [ZIP CODE]

## Current Conditions
- **Market Type**: Buyer's / Seller's / Neutral
- **Average DOM**: X days
- **Price Trend**: Up X% / Down X% (last 90 days)
- **Investor Activity**: High / Medium / Low

## Active Flippers
- 

## Neighborhoods to Target
- 

## Neighborhoods to Avoid
- 

## Title Companies Active in Area
- 

## Last Updated: [Date]
```

## Index of Market Data Files

| ZIP | City | Last Updated | Notes |
|-----|------|-------------|-------|
| *(agents add rows here)* | | | |
