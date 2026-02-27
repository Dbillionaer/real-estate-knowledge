#!/usr/bin/env python3
"""
Batch update metadata for seller_finance/ and creative_finance/ transcripts.
Run from the knowledge base root directory.
"""

import re
import os

# Metadata for each file
METADATA = {
    # ─── SELLER FINANCE ────────────────────────────────────────────────────────
    "seller_finance/Seller Finance Pitch 2.md": {
        "demonstrates_technique": "Above-Asking Seller Finance with Interest-Only Rehab Period",
        "objections_handled": ["Declined seller finance before", "Needs to think about it", "Wants cash upfront"],
        "seller_profile": "Cash-owning investor using property as 1031 exchange component",
        "outcome": "follow-up",
        "key_success_factor": "Offered above asking ($325K vs $310K ask) with interest-only payments during rehab to make monthly payments manageable",
    },
    "seller_finance/Seller Finance Pitch 3 - Condo.md": {
        "demonstrates_technique": "Seller Finance via Agent with Commission Protection",
        "objections_handled": ["Confusion about property scope", "Agent commission concern"],
        "seller_profile": "Absentee owner selling single condo unit through agent",
        "outcome": "follow-up",
        "key_success_factor": "Clarified property scope, offered above asking ($175K vs $170K), assured agent commission paid from down payment",
    },
    "seller_finance/Seller Finance Pitch 4.md": {
        "demonstrates_technique": "Seller Finance with 5-Year Balloon vs Bank Loan Comparison",
        "objections_handled": ["Seller needs cash to finish other projects", "Agent commission concern"],
        "seller_profile": "Flipper/investor selling renovated property through agent",
        "outcome": "follow-up",
        "key_success_factor": "Framed seller finance as better than bank terms: 10% down vs 20%, above asking price, commission paid upfront from down payment",
    },
    "seller_finance/Seller Finance Pitch 5.md": {
        "demonstrates_technique": "Above-Asking Offer on Stale Listing via Agent",
        "objections_handled": ["Seller firm on price", "Market shift concern"],
        "seller_profile": "Absentee owner with long-held property, firm on price",
        "outcome": "follow-up",
        "key_success_factor": "Identified 44-day stale listing, offered $350K (above ask) on terms to motivate seller who bought at $78K",
    },
    "seller_finance/Seller Finance Pitch 6.md": {
        "demonstrates_technique": "Full Seller Finance Education Pitch with Tax Deferral and Capital Gains Benefit",
        "objections_handled": ["Agent needs broker approval", "Unfamiliar with seller finance mechanics"],
        "seller_profile": "Investor who acquired property as part of package deal, represented by agent",
        "outcome": "follow-up",
        "key_success_factor": "Comprehensive education on seller finance mechanics: tax deferral, capital gains reduction, quitclaim deed protection, 84-month balloon",
    },
    "seller_finance/Seller Finance Pitch 7.md": {
        "demonstrates_technique": "Direct-to-Seller Negotiation After Agent Relay Fails",
        "objections_handled": ["Seller wants all money upfront", "Balloon payment concern", "Can make more renting it himself"],
        "seller_profile": "Duplex owner who wants cash upfront, aware of rental income potential",
        "outcome": "follow-up",
        "key_success_factor": "Escalated to direct seller conversation after agent relay; countered rental income objection by showing $250K total vs rental income",
    },
    "seller_finance/Seller Finance Pitch 8.md": {
        "demonstrates_technique": "Subject-To Hybrid with Seller Finance Overlay on Mortgaged Duplex",
        "objections_handled": ["Has existing mortgage", "Due-on-sale clause concern", "Bank won't allow assumption"],
        "seller_profile": "Duplex co-owner with existing mortgage, familiar with creative finance concepts",
        "outcome": "follow-up",
        "key_success_factor": "Addressed due-on-sale concern with Georgia law explanation; offered to take over mortgage payments plus additional monthly payment",
    },
    "seller_finance/Seller Finance Pitch 9 - 2.1m Dollar Deal.md": {
        "demonstrates_technique": "Multi-Property Portfolio Seller Finance with Hedge Fund Comparison",
        "objections_handled": ["Seller wants large down payment ($1.1M)", "Package deal requirement", "Hedge fund buyer preference"],
        "seller_profile": "Intermediary marketing 4-property portfolio for investor partner",
        "outcome": "follow-up",
        "key_success_factor": "Pivoted from hedge fund buyer to seller finance; explained 20% down comparison to justify lower down payment on $2.1M portfolio",
    },
    "seller_finance/Seller Finance Pitch 10.md": {
        "demonstrates_technique": "Seller Finance on Partially Renovated Property with Title Issue History",
        "objections_handled": ["Property has complicated history", "Seller unsure about terms"],
        "seller_profile": "Owner-occupant who bought to renovate but got overwhelmed; property has city easement dispute history",
        "outcome": "follow-up",
        "key_success_factor": "Built rapport by listening to seller's renovation story; positioned seller finance as solution to get full value on partially renovated property",
    },
    "seller_finance/Seller Finance Pitch 11.md": {
        "demonstrates_technique": "Over-Asking Seller Finance Pitch with Leaseback Option",
        "objections_handled": ["Doesn't want to move in December", "Needs time to find new place"],
        "seller_profile": "House-hacking owner-occupant in duplex, needs time to relocate",
        "outcome": "follow-up",
        "key_success_factor": "Offered $1M (above $900K ask) and offered leaseback option to solve seller's relocation timing concern",
    },
    "seller_finance/Seller Finance Pitch 12.md": {
        "demonstrates_technique": "Seller Finance on Duplex with Roofing Contractor Relationship Building",
        "objections_handled": ["Roof condition concern", "Unforeseen rehab risk"],
        "seller_profile": "Agent who is also a roofing contractor, selling duplex for owner relocating to Atlanta",
        "outcome": "follow-up",
        "key_success_factor": "Turned roof concern into relationship opportunity; offered $400K (above list) on seller finance terms while building contractor relationship",
    },
    "seller_finance/Seller Finance Pitch 13 - 1.7m Dollar Multifam.md": {
        "demonstrates_technique": "High-Value Multifamily Seller Finance with Tax Deferral Focus",
        "objections_handled": ["High asking price", "Capital gains concern"],
        "seller_profile": "Multifamily property owner, sophisticated investor concerned about tax implications",
        "outcome": "follow-up",
        "key_success_factor": "Leveraged tax deferral and installment sale benefits to justify seller finance on $1.7M multifamily",
    },
    "seller_finance/Seller Finance Pitch 14.md": {
        "demonstrates_technique": "Seller Finance Pitch with Balloon Payment Explanation",
        "objections_handled": ["Unfamiliar with balloon payment structure"],
        "seller_profile": "Property owner unfamiliar with seller finance mechanics",
        "outcome": "follow-up",
        "key_success_factor": "Clear explanation of balloon payment structure and timeline built seller confidence",
    },
    "seller_finance/Seller Finance Pitch 15.md": {
        "demonstrates_technique": "Seller Finance via Agent with Commission Assurance",
        "objections_handled": ["Agent commission concern", "Seller needs time to consider"],
        "seller_profile": "Property owner represented by agent, needs time to decide",
        "outcome": "follow-up",
        "key_success_factor": "Proactively addressed agent commission concern to keep agent as ally in the deal",
    },
    "seller_finance/Seller Finance Pitch 16.md": {
        "demonstrates_technique": "Seller Finance with Rental Income Comparison",
        "objections_handled": ["Seller considering renting instead"],
        "seller_profile": "Landlord weighing rental vs sale decision",
        "outcome": "follow-up",
        "key_success_factor": "Compared seller finance monthly payment to rental income to show equivalent or better cash flow without landlord headaches",
    },
    "seller_finance/Seller Finance Pitch 17.md": {
        "demonstrates_technique": "Seller Finance Pitch with Down Payment Negotiation",
        "objections_handled": ["Down payment too low", "Wants more cash upfront"],
        "seller_profile": "Property owner negotiating down payment amount",
        "outcome": "follow-up",
        "key_success_factor": "Negotiated down payment to acceptable level while maintaining favorable monthly terms",
    },
    "seller_finance/Seller Finance Pitch 18.md": {
        "demonstrates_technique": "Seller Finance with Appreciation and Long-Term Wealth Building",
        "objections_handled": ["Seller wants full cash price"],
        "seller_profile": "Property owner focused on maximizing total proceeds",
        "outcome": "follow-up",
        "key_success_factor": "Showed total return with interest exceeds cash price, framing seller finance as wealth-building tool",
    },
    "seller_finance/Seller Finance Pitch 20.md": {
        "demonstrates_technique": "Seller Finance on Fully Renovated Duplex",
        "objections_handled": ["Seller asking $400K firm", "Property just renovated"],
        "seller_profile": "Duplex owner who completed full renovation, asking $400K",
        "outcome": "follow-up",
        "key_success_factor": "Gathered detailed renovation info to justify above-asking seller finance offer on fully renovated duplex",
    },
    "seller_finance/Seller Finance Pitch 21.md": {
        "demonstrates_technique": "Over-Asking Seller Finance Pitch After FHA Offer Rejections",
        "objections_handled": ["FHA offers rejected", "Seller wants non-FHA buyer", "Out-of-state investor cash flow concern"],
        "seller_profile": "Agent who rejected FHA offers, wants investor buyer for move-in-ready property",
        "outcome": "follow-up",
        "key_success_factor": "Positioned as non-FHA investor buyer; offered seller finance as solution to cash flow problem at $200K price point",
    },
    "seller_finance/Seller Finance Pitch 22.md": {
        "demonstrates_technique": "Seller Finance Pitch with Market Conditions Rapport Building",
        "objections_handled": ["High interest rate environment concern", "Market slowdown"],
        "seller_profile": "Agent/investor in Houston with personal renovation project, selling investment property",
        "outcome": "follow-up",
        "key_success_factor": "Built rapport through shared experience of high interest rate challenges; positioned seller finance as solution to rate environment",
    },
    "seller_finance/Seller Finance Pitch 24.md": {
        "demonstrates_technique": "Seller Finance in First Lien Position on Free-and-Clear Property",
        "objections_handled": ["Competing offer wants seller in second position", "Multiple competing offers"],
        "seller_profile": "Agent representing free-and-clear property owner with multiple seller finance offers",
        "outcome": "follow-up",
        "key_success_factor": "Differentiated from competing offer by offering first lien position (not subordinate); explained refinance risk of competitor's structure",
    },
    "seller_finance/Seller Finance Pitch 25 - 4 Deals in One Call.md": {
        "demonstrates_technique": "Portfolio Seller Finance - Multiple Properties One Call",
        "objections_handled": ["Seller has multiple properties to sell", "Wants to sell all at once"],
        "seller_profile": "Multi-property owner looking to liquidate portfolio",
        "outcome": "follow-up",
        "key_success_factor": "Structured seller finance terms across 4 properties in single call, showing portfolio acquisition efficiency",
    },
    "seller_finance/Seller Finance Pitch 27.md": {
        "demonstrates_technique": "Subject-To Lender Call - Approving Buyer Terms via HUD Line 203",
        "objections_handled": ["Agent unfamiliar with subject-to process", "Needs documentation"],
        "seller_profile": "Agent representing seller on Skyline Drive, unfamiliar with subject-to transaction",
        "outcome": "follow-up",
        "key_success_factor": "Positioned as lender/financial partner; used HUD line 203 reference to legitimize subject-to transaction for skeptical agent",
    },
    "seller_finance/Seller Finance Pitch 30 - 700k House.md": {
        "demonstrates_technique": "High-Value Seller Finance with Sophisticated Buyer Framing",
        "objections_handled": ["High price point hesitation", "Wants traditional sale"],
        "seller_profile": "High-value property owner ($700K) considering traditional vs creative sale",
        "outcome": "follow-up",
        "key_success_factor": "Positioned seller finance as premium option for sophisticated sellers, showing total return exceeds traditional sale",
    },
    "seller_finance/Seller Finance Pitch 32.md": {
        "demonstrates_technique": "Seller Finance with Florida Insurance Market Education",
        "objections_handled": ["High insurance premiums in Florida", "Older home insurance concerns", "Natural disaster risk"],
        "seller_profile": "Agent in Florida market with insurance-challenged older property",
        "outcome": "follow-up",
        "key_success_factor": "Turned insurance concern into rapport-building conversation; positioned as informed out-of-state investor who understands Florida market challenges",
    },
    "seller_finance/Seller Finance Pitch 33.md": {
        "demonstrates_technique": "Seller Finance with Extended Balloon Negotiation",
        "objections_handled": ["5-year balloon too short", "20% down payment requirement", "Seller wants non-assignable contract"],
        "seller_profile": "Property owner open to seller finance but negotiating balloon length and down payment",
        "outcome": "follow-up",
        "key_success_factor": "Offered above asking ($150K vs $135K) to incentivize longer 10-year balloon; addressed non-assignability requirement",
    },
    "seller_finance/Seller Finance Pitch 34 - Duplex.md": {
        "demonstrates_technique": "Duplex Seller Finance with Rental Income Replacement",
        "objections_handled": ["Currently collecting rent", "Doesn't want to lose rental income"],
        "seller_profile": "Duplex landlord with existing tenants and rental income",
        "outcome": "follow-up",
        "key_success_factor": "Structured monthly seller finance payment to match or exceed current rental income, eliminating landlord responsibilities",
    },
    "seller_finance/Seller Finance Pitch 35.md": {
        "demonstrates_technique": "Quick Seller Finance Pitch Before Agent Showing",
        "objections_handled": ["Agent has showing in 10 minutes", "Previous offer had low down payment"],
        "seller_profile": "Agent with active showing scheduled, representing seller who wants more than $150K down",
        "outcome": "follow-up",
        "key_success_factor": "Adapted to time constraint; quickly established seller finance interest and down payment expectations before agent's showing",
    },
    "seller_finance/Seller Finance Pitch.md": {
        "demonstrates_technique": "Initial Seller Finance Introduction Pitch",
        "objections_handled": [],
        "seller_profile": "Duplex owner (Raven) with off-market property",
        "outcome": "follow-up",
        "key_success_factor": "Established rapport and introduced seller finance concept on off-market duplex",
    },
    "seller_finance/Seller Finance One Liner.md": {
        "demonstrates_technique": "Quick 90-Second Seller Finance One-Liner Pitch",
        "objections_handled": [],
        "seller_profile": "Property owner receiving initial outreach",
        "outcome": "follow-up",
        "key_success_factor": "Concise one-liner that explains seller finance benefit in under 90 seconds to get seller interested",
    },
    "seller_finance/Voicemail - Seller Finance for Multi Family.md": {
        "demonstrates_technique": "Voicemail Script for Multifamily Seller Finance",
        "objections_handled": [],
        "seller_profile": "Multifamily property owner (voicemail)",
        "outcome": "no-response",
        "key_success_factor": "Compelling voicemail that mentions specific benefit (monthly income) to drive callback",
    },
    "seller_finance/Voicemail - Seller Finance One Liner.md": {
        "demonstrates_technique": "Seller Finance Voicemail One-Liner",
        "objections_handled": [],
        "seller_profile": "Property owner (voicemail)",
        "outcome": "no-response",
        "key_success_factor": "Ultra-brief voicemail with single compelling hook to maximize callback rate",
    },
    "seller_finance/Voicemail - Seller Finance One Liners 2.md": {
        "demonstrates_technique": "Seller Finance Voicemail Variations",
        "objections_handled": [],
        "seller_profile": "Property owner (voicemail)",
        "outcome": "no-response",
        "key_success_factor": "Multiple voicemail variations testing different hooks for seller finance callback optimization",
    },
    "seller_finance/Negotiations - Seller Finance - Direct to Seller.md": {
        "demonstrates_technique": "Direct-to-Seller Negotiation Bypassing Agent",
        "objections_handled": ["Agent as gatekeeper", "Seller unfamiliar with terms"],
        "seller_profile": "Property owner being contacted directly without agent intermediary",
        "outcome": "follow-up",
        "key_success_factor": "Direct seller contact allowed more candid negotiation and faster term agreement than agent-mediated approach",
    },
    "seller_finance/Negotiations - Seller Finance - Disliking 2% Interest Rate.md": {
        "demonstrates_technique": "Interest Rate Negotiation and Justification",
        "objections_handled": ["Interest rate too low", "Wants higher return on seller finance"],
        "seller_profile": "Financially sophisticated seller who understands interest rate implications",
        "outcome": "follow-up",
        "key_success_factor": "Justified lower interest rate by showing total return with appreciation and tax benefits exceeds higher rate alternatives",
    },
    "seller_finance/Negotiations - Seller Finance - Father Said No, Talking with His Son.md": {
        "demonstrates_technique": "Multi-Generational Decision Maker Navigation",
        "objections_handled": ["Primary decision maker (father) rejected offer", "Son as secondary influencer"],
        "seller_profile": "Family-owned property with generational decision-making dynamic",
        "outcome": "follow-up",
        "key_success_factor": "Identified son as more open to creative finance; reframed offer to address father's concerns through son's perspective",
    },
    "seller_finance/Hybrid Pitch 1 - 1.85m Dollar AirBNB.md": {
        "demonstrates_technique": "Hybrid Cash + Seller Finance on High-Value AirBNB Property",
        "objections_handled": ["High price point", "AirBNB income concern", "Wants significant cash component"],
        "seller_profile": "AirBNB operator with $1.85M property, income-dependent",
        "outcome": "follow-up",
        "key_success_factor": "Structured hybrid deal with substantial cash down payment plus seller finance to match AirBNB income replacement",
    },
    "seller_finance/Hybrid Pitch 2.md": {
        "demonstrates_technique": "Hybrid Deal Structure with Cash and Seller Finance Components",
        "objections_handled": ["Needs cash component", "Concerned about monthly payment reliability"],
        "seller_profile": "Property owner needing both immediate cash and ongoing income",
        "outcome": "follow-up",
        "key_success_factor": "Balanced hybrid structure addressing both immediate cash need and long-term income desire",
    },
    # ─── CREATIVE FINANCE ──────────────────────────────────────────────────────
    "creative_finance/Hybrid - Explaining a Hybrid Deal.md": {
        "demonstrates_technique": "Hybrid Deal Explanation - Educational Pitch",
        "objections_handled": ["Unfamiliar with hybrid deal structure", "Confused about cash vs seller finance split"],
        "seller_profile": "Property owner unfamiliar with creative finance structures",
        "outcome": "follow-up",
        "key_success_factor": "Clear step-by-step explanation of hybrid deal mechanics made complex structure accessible to seller",
    },
    "creative_finance/Hybrid - Restructuring Seller Finance to Hybrid.md": {
        "demonstrates_technique": "Pivoting from Pure Seller Finance to Hybrid Structure",
        "objections_handled": ["Pure seller finance not enough cash", "Needs larger upfront payment"],
        "seller_profile": "Seller who initially rejected pure seller finance but open to hybrid",
        "outcome": "follow-up",
        "key_success_factor": "Identified seller's cash need and restructured from pure seller finance to hybrid by adding cash component",
    },
    "creative_finance/Hybrid Pitch 1 - 1.85m Dollar AirBNB.md": {
        "demonstrates_technique": "Hybrid Cash + Seller Finance on High-Value AirBNB Property",
        "objections_handled": ["High price point", "AirBNB income replacement concern", "Wants significant cash component"],
        "seller_profile": "AirBNB operator with $1.85M property, income-dependent",
        "outcome": "follow-up",
        "key_success_factor": "Structured hybrid deal with substantial cash down payment plus seller finance to match AirBNB income replacement",
    },
    "creative_finance/Hybrid Pitch 2.md": {
        "demonstrates_technique": "Hybrid Deal Structure Negotiation",
        "objections_handled": ["Needs cash component", "Concerned about monthly payment reliability"],
        "seller_profile": "Property owner needing both immediate cash and ongoing income",
        "outcome": "follow-up",
        "key_success_factor": "Balanced hybrid structure addressing both immediate cash need and long-term income desire",
    },
    # UUID files
    "creative_finance/0e78ebb0-514e-11f0-867b-612231b6f9af.md": {
        "demonstrates_technique": "Subject-To on Multi-Room Rental Property",
        "objections_handled": ["Rental income concern", "Room-by-room rental structure"],
        "seller_profile": "Multi-room rental property owner with engineer tenants, seasonal rental model",
        "outcome": "follow-up",
        "key_success_factor": "Gathered detailed rental income data ($4,900-$5,600/month) to structure subject-to terms matching seller's income needs",
    },
    "creative_finance/023c2580-53a9-11f0-bd4c-078d308e83f9.md": {
        "demonstrates_technique": "Subject-To on Military Separation Distressed Property",
        "objections_handled": ["Ex-spouse still in property", "Carrying double housing costs"],
        "seller_profile": "Military veteran going through separation, carrying mortgage plus rent on two properties",
        "outcome": "follow-up",
        "key_success_factor": "Identified double housing cost distress; positioned subject-to as immediate relief from mortgage burden during separation",
    },
    "creative_finance/383a75f0-53a5-11f0-bd4c-078d308e83f9.md": {
        "demonstrates_technique": "Subject-To Deal Analysis with Low-Equity Seller via Referral",
        "objections_handled": ["Low equity situation", "Seller not yet approached"],
        "seller_profile": "Low-equity property owner referred by channel follower/wholesaler",
        "outcome": "follow-up",
        "key_success_factor": "Educated referring wholesaler on subject-to structure for low-equity deal before approaching seller",
    },
    "creative_finance/cec2c2a0-4d53-11f0-8e0f-1f9b00d1a734.md": {
        "demonstrates_technique": "Subject-To on Vacant Property with Double Carrying Costs",
        "objections_handled": ["Lots of showings but no offers", "Paying mortgage on vacant property"],
        "seller_profile": "Homeowner who moved out and is paying mortgage on vacant property in Cypress, TX",
        "outcome": "follow-up",
        "key_success_factor": "Identified double carrying cost pain point (mortgage + new housing); positioned subject-to as immediate relief",
    },
    "creative_finance/fdbc6bf0-5146-11f0-8da1-912d4cd85c32.md": {
        "demonstrates_technique": "Subject-To Objection Handling Voicemail to Agent",
        "objections_handled": ["Agent has questions about subject-to transaction", "Needs proof of legitimacy"],
        "seller_profile": "Agent (Christine Bouchard) with questions about subject-to transaction for her client",
        "outcome": "follow-up",
        "key_success_factor": "Proactively offered references (attorney, previous agents, previous sellers) to address agent's legitimacy concerns before scheduled call",
    },
}


def update_metadata(filepath, metadata):
    """Update the metadata fields in a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Update demonstrates_technique
    content = re.sub(
        r'demonstrates_technique: ".*?"',
        'demonstrates_technique: "{}"'.format(metadata["demonstrates_technique"].replace('"', '\\"')),
        content
    )
    
    # Update objections_handled
    objections = metadata["objections_handled"]
    if objections:
        obj_str = "[" + ", ".join('"' + o.replace('"', '\\"') + '"' for o in objections) + "]"
    else:
        obj_str = "[]"
    content = re.sub(
        r'objections_handled: \[.*?\]',
        'objections_handled: {}'.format(obj_str),
        content
    )
    
    # Update seller_profile
    content = re.sub(
        r'seller_profile: ".*?"',
        'seller_profile: "{}"'.format(metadata["seller_profile"].replace('"', '\\"')),
        content
    )
    
    # Update outcome
    content = re.sub(
        r'outcome: ".*?"',
        'outcome: "{}"'.format(metadata["outcome"]),
        content
    )
    
    # Update key_success_factor
    content = re.sub(
        r'key_success_factor: ".*?"',
        'key_success_factor: "{}"'.format(metadata["key_success_factor"].replace('"', '\\"')),
        content
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated: {filepath}")
    else:
        print(f"⚠️  No changes: {filepath}")


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    updated = 0
    skipped = 0
    
    for filepath, metadata in METADATA.items():
        full_path = os.path.join(base_dir, filepath)
        if os.path.exists(full_path):
            update_metadata(full_path, metadata)
            updated += 1
        else:
            print(f"❌ Not found: {filepath}")
            skipped += 1
    
    print(f"\n✅ Processed {updated} files, {skipped} not found")


if __name__ == "__main__":
    main()
