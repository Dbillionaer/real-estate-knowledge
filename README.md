Florida Wholesale ATM KB first - prioritize FL market data, county guides, distressed hunting rules.
# 🏠 Wholesale Real Estate Knowledge Base

> **AI Agent Knowledge Vault** — Indexed by QMD for semantic search. All agents in the [wholesaile](https://github.com/Dbillionaer/wholesaile) system query this vault via `memory_search`.

## 🗺️ Vault Structure

```
knowledge-base/
├── README.md                          ← You are here (navigation hub)
├── KNOWLEDGE_BASE.md                  ← Agent query guide (how to search this vault)
├── TAGS_INDEX.md                      ← All tags and what they index
│
├── 📚 Playbooks (strategy guides)
│   ├── Foundations_of_Wholesaling_Playbook.md
│   ├── deal_type_playbook.md          ← MASTER: strategy selection matrix
│   ├── pitch_strategies_master_guide.md
│   ├── cash_deals_playbook.md
│   ├── seller_finance_playbook.md
│   ├── subject_to_playbook.md
│   ├── Hybrid_Deals_Playbook.md
│   ├── trust_acquisition_playbook.md
│   ├── Lead_Generation_Playbook.md
│   ├── Mastering_Dispositions_Playbook.md
│   ├── Building_Your_Buyers_List_Playbook.md
│   ├── Deal_Analysis_and_Valuation_Guide.md
│   ├── Deal_Marketing_Guide.md
│   ├── Financial_and_Business_Acumen_Playbook.md
│   ├── Scaling_the_Wholesaling_Business.md
│   ├── The_Modern_Wholesalers_Tech_Stack.md
│   ├── Understanding_and_Working_with_Your_Title_Company.md
│   ├── Contract_Walkthroughs_Guide.md
│   └── Closing_Process_Checklist.md
│
├── 🧠 Reference Guides
│   ├── comprehensive_decision_tree.md ← MASTER: deal routing logic
│   ├── complex_scenario_resolution_guide.md
│   ├── authentic_conversation_case_studies.md
│   ├── advanced_financial_modeling_examples.md
│   ├── portfolio_acquisition_frameworks.md
│   └── Glossary_of_Real_Estate_Terms.md
│
├── 📞 Call Transcripts
│   ├── cash_deals/                    ← 4 transcripts (cash offers, voicemails)
│   ├── seller_finance/                ← 38 transcripts (seller financing)
│   └── creative_finance/              ← 14 transcripts (Subject-To, Hybrid)
│
├── 📄 Contracts
│   └── contracts/                     ← Legal templates (PDF, DOCX, MD)
│
└── 🗒️ Agent Memory (living documents)
    ├── agent-lessons/                 ← Lessons learned from real deals
    ├── market-data/                   ← Comps, ARV data, market notes
    └── buyer-profiles/                ← Buyer preferences and history
```

## 🤖 Agent Quick Reference

| Agent | Primary Queries | Key Files |
|-------|----------------|-----------|
| **Lead Scout** 🔍 | `distress indicators`, `lead sources`, `motivated seller` | [[Lead_Generation_Playbook]], [[comprehensive_decision_tree]] |
| **Market Analyst** 📊 | `ARV calculation`, `MAO formula`, `repair estimate` | [[Deal_Analysis_and_Valuation_Guide]], [[advanced_financial_modeling_examples]] |
| **Acquisition Manager** 🤝 | `seller objection: [X]`, `pitch technique`, `negotiation` | [[pitch_strategies_master_guide]], [[seller_finance_playbook]], [[subject_to_playbook]] |
| **Title Researcher** 📋 | `title issue`, `lien`, `due diligence` | [[Understanding_and_Working_with_Your_Title_Company]], [[Contract_Walkthroughs_Guide]] |
| **Dispositions Manager** 💰 | `buyer criteria`, `deal blast`, `assignment fee` | [[Mastering_Dispositions_Playbook]], [[Building_Your_Buyers_List_Playbook]] |
| **Transaction Coordinator** 📝 | `closing checklist`, `contract`, `timeline` | [[Closing_Process_Checklist]], [[Contract_Walkthroughs_Guide]] |

## 📊 Transcript Index by Outcome

| Outcome | Count | Best Examples |
|---------|-------|---------------|
| `accepted` | See [[TAGS_INDEX]] | [[Subject to - Accepted Offer 1]], [[Subject To - Accepted Offer 2]], [[Subject To - Accepted Offer 3]] |
| `follow-up` | Most transcripts | [[Seller Finance Pitch 19 - Impossible Terms to Best Terms]], [[Subject To Pitch 12 - One of the Best Calls Ever]] |

## 🔄 How This Vault Grows

This is a **living knowledge base**. It grows in three ways:

1. **New Transcripts** — Add new call recordings to `cash_deals/`, `seller_finance/`, or `creative_finance/` with proper YAML frontmatter (see [[metadata_conventions]])
2. **Agent Lessons** — After each deal, agents write lessons to `agent-lessons/YYYY-MM-DD-[address].md`
3. **Market Data** — Agents store comp data and ARV notes in `market-data/`

## 🏷️ Tag System

All transcripts use consistent tags for semantic search:

- `#transcript` — All call recordings
- `#cash-deals` — Cash offer calls
- `#seller-finance` — Seller financing calls
- `#subjectto` — Subject-To / mortgage takeover calls
- `#hybrid` — Hybrid deal calls
- `#voicemail` — Voicemail scripts
- `#negotiation` — Negotiation-focused calls
- `#accepted` — Calls that resulted in accepted offers
- `#high-value` — Deals over $500K

See [[TAGS_INDEX]] for the complete tag taxonomy.

## Florida Wholesale Data
Added market-data/florida/ for county ARVs, comps. Tagged with Grok/county.