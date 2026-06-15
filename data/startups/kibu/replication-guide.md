# Kibu — Replication Guide

> How to build EHR and compliance software for healthcare organizations

## Overview

Kibu builds EHR and compliance software for organizations serving people with intellectual and developmental disabilities (I/DD). It operates across 48 states with $234K MRR. The core insight: healthcare compliance paperwork is fragmented and state-by-state, creating a massive pain point for providers who just want to focus on care.

**Key Metrics:** MRR: $234K | Rank: #5 | Team: Small team | Focus: Healthcare compliance

## Market Opportunity

**Niche:** I/DD provider compliance software — a $5B+ niche within healthcare IT.

**Why underserved:** Most EHR systems are built for hospitals and clinics. I/DD providers have unique compliance requirements (progress notes, behavioral plans, ISP documentation) that generic EHRs don't handle. State requirements vary, making this a hard market to enter — but defensible once you do.

**Competitive Landscape:** Netsmart (dominant but expensive), Welligent (niche), Propeller Health (different focus). Kibu wins on price and modern UX.

## MVP Build Guide

### Core Features
1. Progress notes module with state-specific compliance templates
2. Client documentation and goal tracking
3. Basic billing/claims integration

### Tech Stack
| Layer | Tool | Cost |
|-------|------|------|
| Frontend | Next.js | Free |
| Backend | Node.js + Express | Free |
| Database | PostgreSQL (Supabase) | Free tier |
| Auth | NextAuth.js | Free |
| Payments | Stripe | 2.9%+$0.30 |

**Build time:** 8-10 weeks | **Cost:** $100-200/mo

### No-Code Alternative
Use Airtable + Typeform for basic client tracking. Limitations: no compliance automation, no billing integration. Migrate to code at ~10 paying customers.

## Pricing Strategy

Enterprise SaaS model. $500-2K/mo per organization. Annual contracts preferred. Pricing based on number of clients served. Free pilot period (60-90 days) to reduce friction.

**Positioning:** "Compliance software that doesn't cost more than your admin staff."

## Customer Acquisition

1. **Direct sales:** Cold email I/DD provider directors. Personalize with state compliance pain points.
2. **Conferences:** Attend ASHA, NADSP, state provider association meetings. Booth + speaking slots.
3. **Case studies:** Publish time-savings data from pilot orgs. "Org X reduced compliance time by 60%."

## Common Pitfalls

1. **Trying to solve all 50 states at once.** Start with 2-3 states, nail compliance there, then expand.
2. **Ignoring the sales cycle.** Healthcare enterprise sales take 6-12 months. Plan cash flow accordingly.
3. **Underestimating EHR integrations.** HL7/FHIR integrations are complex and expensive. Budget 30% of dev time.

## Launch Checklist

### Pre-Launch
- [ ] Build progress notes module for 3 target states
- [ ] Get compliance review from healthcare consultant
- [ ] Line up 3 pilot organizations

### Launch
- [ ] Onboard pilot orgs at $0 for 90 days
- [ ] Collect metrics on time savings
- [ ] Publish first case study

### Post-Launch
- [ ] Begin paid conversion of pilots
- [ ] Expand to 5 more states
- [ ] Add billing module

---

**Attribution:** Educational purposes. Data from [TrustMRR](https://trustmrr.com/startup/kibu).
**Disclaimer:** For learning only. Respect IP and trademarks.
