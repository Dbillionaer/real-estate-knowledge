# 🤖 Agent Knowledge Base Query Guide

> **For AI Agents**: This document explains how to query the wholesale real estate knowledge base using `memory_search` and `memory_get`. Read this before your first query.

## How to Search This Knowledge Base

The knowledge base is indexed by QMD with BM25 + vector search. Use `memory_search` with natural language queries.

### Basic Query Pattern

```
memory_search("your query here")
```

### Query Examples by Agent Role

---

## 🔍 Lead Scout Queries

```
memory_search("distress indicators motivated seller")
memory_search("lead generation sources driving for dollars")
memory_search("probate tax delinquent code violations")
memory_search("skip tracing owner contact")
memory_search("qualifying a lead criteria")
```

**Key files to read directly:**
- `memory_get("Lead_Generation_Playbook.md")`
- `memory_get("comprehensive_decision_tree.md")` — Phase 1: Initial Property Assessment

---

## 📊 Market Analyst Queries

```
memory_search("ARV calculation comparable sales")
memory_search("MAO formula maximum allowable offer")
memory_search("repair cost estimate per square foot")
memory_search("cap rate NOI rental property analysis")
memory_search("70% rule investor purchase price")
memory_search("financial modeling deal analysis")
```

**Key files to read directly:**
- `memory_get("Deal_Analysis_and_Valuation_Guide.md")`
- `memory_get("advanced_financial_modeling_examples.md")`
- `memory_get("Financial_and_Business_Acumen_Playbook.md")`

---

## 🤝 Acquisition Manager Queries

### Finding the Right Pitch Strategy

```
memory_search("seller objection price too low")
memory_search("seller objection need cash now")
memory_search("seller objection too good to be true")
memory_search("seller objection due on sale concern")
memory_search("seller objection wants to rent instead")
memory_search("seller objection agent commission")
memory_search("seller objection high down payment")
```

### Finding Pitch Examples by Deal Type

```
memory_search("cash offer pitch distressed property")
memory_search("seller finance pitch free and clear")
memory_search("subject to pitch behind on payments foreclosure")
memory_search("hybrid deal pitch airbnb rental")
memory_search("morby method subject to")
memory_search("90 second pitch seller finance")
```

### Finding Negotiation Tactics

```
memory_search("negotiation term restructuring interest rate")
memory_search("negotiation rapport building")
memory_search("negotiation pivoting to seller finance")
memory_search("negotiation impossible terms best terms")
memory_search("negotiation 4 deals one call")
memory_search("negotiation explain like they're 5")
```

### Finding Accepted Offer Examples

```
memory_search("accepted offer subject to")
memory_search("outcome accepted deal closed")
```

**Key files to read directly:**
- `memory_get("pitch_strategies_master_guide.md")` — All strategies overview
- `memory_get("deal_type_playbook.md")` — Strategy selection matrix
- `memory_get("seller_finance_playbook.md")` — Seller finance execution
- `memory_get("subject_to_playbook.md")` — Subject-To execution
- `memory_get("complex_scenario_resolution_guide.md")` — Hard scenarios
- `memory_get("authentic_conversation_case_studies.md")` — Real examples

### Transcript Search by Seller Profile

```
memory_search("seller profile distressed homeowner")
memory_search("seller profile landlord considering rental")
memory_search("seller profile sophisticated investor")
memory_search("seller profile inherited property")
memory_search("seller profile privacy conscious executive")
```

---

## 📋 Title Researcher Queries

```
memory_search("title search lien due diligence")
memory_search("IRS tax lien bankruptcy judgment")
memory_search("HOA lien encumbrance easement")
memory_search("chain of title ownership verification")
memory_search("title company closing process")
memory_search("deal killer title issue")
```

**Key files to read directly:**
- `memory_get("Understanding_and_Working_with_Your_Title_Company.md")`
- `memory_get("Contract_Walkthroughs_Guide.md")`
- `memory_get("contracts/Assignment_of_Contract.md")`

---

## 💰 Dispositions Manager Queries

```
memory_search("buyer list cash buyer criteria")
memory_search("deal blast template assignment fee")
memory_search("marketing deal to investors")
memory_search("dispositions assignment contract")
memory_search("buyer tier VIP active")
memory_search("deal marketing channels")
```

**Key files to read directly:**
- `memory_get("Mastering_Dispositions_Playbook.md")`
- `memory_get("Building_Your_Buyers_List_Playbook.md")`
- `memory_get("Deal_Marketing_Guide.md")`

---

## 📝 Transaction Coordinator Queries

```
memory_search("closing checklist timeline 21 days")
memory_search("earnest money escrow title company")
memory_search("assignment contract documents required")
memory_search("purchase sale agreement template")
memory_search("addendum termination agreement")
memory_search("JV agreement joint venture")
```

**Key files to read directly:**
- `memory_get("Closing_Process_Checklist.md")`
- `memory_get("Contract_Walkthroughs_Guide.md")`
- `memory_get("contracts/Assignment_of_Contract.md")`

---

## 📖 Glossary Lookups

When you encounter an unfamiliar term:

```
memory_search("definition [TERM]")
memory_get("Glossary_of_Real_Estate_Terms.md")
```

Common terms: ARV, MAO, LTV, Cap Rate, NOI, Subject-To, Morby Method, Assignment Fee, Earnest Money, Chain of Title, Due-on-Sale Clause, 1031 Exchange

---

## 🧠 Writing to the Knowledge Base

Agents should write new knowledge back to the vault to make it grow:

### After a Deal Closes
```
Write to: agent-lessons/YYYY-MM-DD-[address-slug].md
Format:
---
date: YYYY-MM-DD
address: [full address]
deal_type: [cash/seller-finance/subject-to/hybrid]
outcome: [closed/fell-through]
assignment_fee: $[X]
lessons_learned:
  - [lesson 1]
  - [lesson 2]
key_objections_handled:
  - [objection]: [how it was resolved]
---
```

### After Researching Comps
```
Write to: market-data/[ZIP-CODE]-comps-YYYY-MM.md
Include: address, sold price, sqft, bed/bath, sold date, distance from subject
```

### After Adding a Buyer
```
Update: workspace/MEMORY.md → Buyer List section
Include: name, phone, email, criteria, areas, tier (VIP/Active/Inactive)
```

---

## 🔄 Knowledge Base Update Protocol

When you learn something new that should be remembered:

1. **Tactical insight** (objection handling, pitch technique) → Write to `agent-lessons/`
2. **Market data** (comps, ARV, price trends) → Write to `market-data/`
3. **Buyer/seller contact** → Update `workspace/MEMORY.md`
4. **New call transcript** → Add to appropriate `cash_deals/`, `seller_finance/`, or `creative_finance/` folder with proper YAML frontmatter per [[metadata_conventions]]

---

## ⚡ Quick Decision: Which Strategy?

Use the [[comprehensive_decision_tree]] or this shortcut:

| Situation | Strategy |
|-----------|----------|
| Distressed property, motivated seller | **Cash Offer** |
| Behind on payments, good equity | **Subject-To** |
| Free & clear, income-focused seller | **Seller Finance** |
| High-value, privacy-focused seller | **Trust Acquisition** |
| Mix of equity + cash need | **Hybrid** |
| Low equity, realistic seller | **Creative combo** |

Full matrix: `memory_get("deal_type_playbook.md")` → Master Deal Selection Matrix
