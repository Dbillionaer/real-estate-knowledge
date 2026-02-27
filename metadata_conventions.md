# Transcript Metadata Conventions

Last Updated: 2025-10-24

## Required YAML Frontmatter Fields
Add these 6 fields to every transcript in `markdown_transcripts/`.

- `demonstrates_technique` (string)
  - A concise name of the primary technique in the call.
  - Examples: "Over Asking Price Offer", "Trojan Horse Method", "Quick 90-Second Pitch", "Mortgage Payment Takeover", "Trust Privacy Framing".

- `objections_handled` (array of strings)
  - List the distinct objections addressed during the call, in Seller’s words where possible.
  - Capitalize first letter, avoid punctuation. Keep phrasing consistent.
  - Examples: ["Seller wants to rent instead", "Price too low", "Need cash now", "Too good to be true", "Due-on-sale concern"].

- `seller_profile` (string)
  - Short phrase describing the seller archetype.
  - Examples: "Distressed homeowner", "Landlord considering rental", "Sophisticated investor", "Inherited property seller", "Privacy-conscious executive".

- `outcome` (enum string)
  - One of exactly: `accepted`, `interested`, `rejected`, `follow-up`, `no-response`.
  - Choose the most representative final state of the call/thread.

- `key_success_factor` (string)
  - Brief phrase describing why the call worked or failed.
  - Examples: "Promised same rental income + down payment", "Built trust through empathy", "Showed total return math and tax deferral", "Failed to address credit concerns".

- `audio_source` (string)
  - Relative path from the markdown file to the corresponding audio file.
  - Format: `../../{audio_directory}/{filename}.mp3`
  - Audio directories:
    - `cash_deals` → `../../fixnfliprecordings/`
    - `creative_finance` → `../../mortgagetakeoverrec/`
    - `seller_finance` → `../../sellerfinancerecordings/`
  - If no audio file exists, set to empty string `""` and flag for manual review.
  - Examples:
    - `"../../fixnfliprecordings/Cash Pitch 1.mp3"`
    - `"../../mortgagetakeoverrec/Subject To Pitch 12 - One of the Best Calls Ever.mp3"`
    - `"../../sellerfinancerecordings/Seller Finance Pitch 30 - 700k House.mp3"`

## Formatting Rules
- Keep existing frontmatter intact; add missing fields without renaming existing keys.
- Use YAML arrays for `objections_handled`.
- Avoid YAML aliases. Do not duplicate structures across keys.
- Maintain consistent casing and concise phrasing.

## Examples

Seller Finance — Quick Pitch
```yaml
---
demonstrates_technique: "Quick 90-Second Pitch"
objections_handled: ["Seller wants to rent instead"]
seller_profile: "Landlord considering rental"
outcome: "interested"
key_success_factor: "Matched rental income with structured payments plus down payment"
audio_source: "../../sellerfinancerecordings/Seller Finance Pitch 26 - 90 Second Pitch.mp3"
---
```

Subject-To — Credit Protection
```yaml
---
demonstrates_technique: "Mortgage Payment Takeover"
objections_handled: ["Too good to be true", "Due-on-sale concern"]
seller_profile: "Distressed homeowner"
outcome: "accepted"
key_success_factor: "Emphasized credit protection with performance mortgage"
audio_source: "../../mortgagetakeoverrec/Subject To - Accepted Offer 2.mp3"
---
```

Trust Acquisition — Privacy Focus
```yaml
---
demonstrates_technique: "Trust Privacy Framing"
objections_handled: ["Complexity concern", "Tax implications"]
seller_profile: "Privacy-conscious executive"
outcome: "follow-up"
key_success_factor: "Led with privacy and asset protection, offered attorney-to-attorney consult"
audio_source: "../../mortgagetakeoverrec/Trust Acquisition Pitch 5 - Pivoting from Cash to Trust.mp3"
---
```

## Workflow Notes
1. Read the full transcript before assigning values.
2. Prefer evidence from the call over filename heuristics.
3. If unclear, set `outcome: "follow-up"` and add a TODO comment for manual review.
4. Keep a change log of files updated and any manual overrides.

