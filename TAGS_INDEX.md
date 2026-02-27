# 🏷️ Tags Index

> Complete taxonomy of all tags used in this knowledge base. QMD indexes these for semantic search.

## Document Type Tags

| Tag | Description | Count |
|-----|-------------|-------|
| `#transcript` | Real call recordings | 56+ |
| `#playbook` | Strategy and execution guides | 22 |
| `#reference` | Decision trees, glossaries, case studies | 6 |
| `#contract` | Legal document templates | 7 |
| `#voicemail` | Voicemail scripts | 5 |
| `#negotiation` | Negotiation-focused calls | 3 |

## Deal Type Tags

| Tag | Description | Files |
|-----|-------------|-------|
| `#cash-deals` | Cash offer transcripts | `cash_deals/` |
| `#seller-finance` | Seller financing transcripts | `seller_finance/` |
| `#subjectto` | Subject-To / mortgage takeover | `creative_finance/Subject To*` |
| `#hybrid` | Hybrid deal transcripts | `creative_finance/Hybrid*`, `seller_finance/Hybrid*` |
| `#creative-finance` | All creative financing | `creative_finance/` |

## Outcome Tags

| Tag | Description |
|-----|-------------|
| `#accepted` | Seller accepted the offer |
| `#follow-up` | Call ended with follow-up needed |
| `#rejected` | Seller rejected the offer |
| `#interested` | Seller showed interest, not committed |

## Technique Tags

| Tag | Technique | Example Files |
|-----|-----------|---------------|
| `#morby-method` | Morby Method Subject-To | [[Subject To Pitch 10 - Morby Method]] |
| `#90-second-pitch` | Quick pitch format | [[Seller Finance Pitch 26 - 90 Second Pitch]] |
| `#over-asking` | Offering above asking price | [[Seller Finance Pitch 23 - Offering 100k Above Asking]] |
| `#term-restructuring` | Restructuring impossible terms | [[Seller Finance Pitch 19 - Impossible Terms to Best Terms]] |
| `#explain-like-5` | Simple explanation technique | [[Seller Finance Pitch 28 - Explain it Like They're 5]] |
| `#4-deals-one-call` | Multiple deals in one call | [[Seller Finance Pitch 25 - 4 Deals in One Call]] |
| `#cash-and-seller-finance` | Hybrid cash + seller finance | [[Seller Finance Pitch 29 - Cash & Seller Finance]] |
| `#pivoting` | Pivoting from one strategy to another | [[Seller Finance Pitch 31 - Pivoting to Seller Finance]] |
| `#rapport-building` | Building rapport techniques | [[Subject To Pitch 14 - Building Rapport and Getting Other Listings]] |
| `#no-prior-contact` | Cold outreach, no rapport | [[Subject To Pitch 11 - No Rapport No Prior Contact]] |

## Seller Profile Tags

| Tag | Seller Type | Example Files |
|-----|-------------|---------------|
| `#distressed-seller` | Financially distressed | Most cash deal transcripts |
| `#landlord` | Existing landlord/rental owner | [[Seller Finance Pitch 34 - Duplex]] |
| `#inherited-property` | Inherited property seller | Various cash deal transcripts |
| `#sophisticated-investor` | Experienced investor seller | [[Seller Finance Pitch 9 - 2.1m Dollar Deal]] |
| `#privacy-focused` | Privacy-conscious seller | Trust acquisition transcripts |
| `#high-value` | Deals over $500K | [[Seller Finance Pitch 13 - 1.7m Dollar Multifam]], [[Hybrid Pitch 1 - 1.85m Dollar AirBNB]] |
| `#multifamily` | Multi-family properties | [[Seller Finance Pitch 13 - 1.7m Dollar Multifam]], [[Seller Finance Pitch 34 - Duplex]] |
| `#airbnb` | Short-term rental properties | [[Hybrid Pitch 1 - 1.85m Dollar AirBNB]] |

## Objection Tags

| Tag | Objection Type |
|-----|----------------|
| `#objection-price-low` | "Your price is too low" |
| `#objection-need-cash` | "I need cash now" |
| `#objection-too-good` | "This sounds too good to be true" |
| `#objection-due-on-sale` | "What about the due-on-sale clause?" |
| `#objection-wants-rent` | "I'd rather rent it out" |
| `#objection-agent` | "I have an agent" |
| `#objection-high-down` | "I need a large down payment" |
| `#objection-interest-rate` | "The interest rate is too low" |
| `#objection-sight-unseen` | "I won't sell sight-unseen" |
| `#objection-broker-approval` | "I need broker approval" |

## Strategy Tags

| Tag | Strategy |
|-----|----------|
| `#cash-offer` | Direct cash purchase |
| `#seller-financing` | Seller acts as the bank |
| `#subject-to` | Take over existing mortgage |
| `#hybrid-deal` | Mix of cash + seller finance |
| `#trust-acquisition` | Property held in trust |
| `#portfolio-acquisition` | Multiple properties at once |
| `#1031-exchange` | Tax-deferred exchange |

## Agent-Specific Tags

| Tag | Used By |
|-----|---------|
| `#lead-generation` | Lead Scout |
| `#market-analysis` | Market Analyst |
| `#acquisition` | Acquisition Manager |
| `#title-research` | Title Researcher |
| `#dispositions` | Dispositions Manager |
| `#closing` | Transaction Coordinator |

---

## How to Add New Tags

When adding new transcripts or documents:

1. Use existing tags from this index where applicable
2. Add new tags to this index when you create them
3. Keep tags lowercase with hyphens (e.g., `#new-technique`)
4. Add the tag to the YAML frontmatter `tags:` array in the document
5. Update the count in this index

## Tag Usage in YAML Frontmatter

```yaml
tags: [#transcript, #seller-finance, #high-value, #objection-price-low, #accepted]
```
