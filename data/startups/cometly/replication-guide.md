# Cometly — Replication Guide

> How to build marketing attribution analytics for SaaS companies

## Overview

Cometly provides marketing attribution and analytics for SaaS companies with an AI chat interface for ad data. $201K MRR, Rank #7. The core insight: iOS14 broke pixel-based attribution. Marketers need server-side tracking to understand which ads actually drive revenue.

**Key Metrics:** MRR: $201K | Rank: #7 | Growth: +3% MoM | Team: Small team

## Market Opportunity

**Niche:** SaaS marketing attribution — post-iOS14 world.

**Why underserved:** Google Analytics last-click attribution is broken. Facebook's pixel lost 60%+ accuracy after iOS14. Server-side tracking is the answer but requires technical setup that most marketers can't do.

**Competitive Landscape:** Ruler Analytics, Dreamdata, Northbeam. Cometly differentiates with AI chat interface — ask questions about your ad data in natural language.

## MVP Build Guide

### Core Features
1. Server-side event tracking script (Meta CAPI + Google Enhanced Conversions)
2. Attribution dashboard showing revenue per channel/campaign
3. AI chat: "Which campaign drove the most signups last week?"

### Tech Stack
| Layer | Tool | Cost |
|-------|------|------|
| Frontend | Next.js | Free |
| Backend | Node.js | Free |
| Database | PostgreSQL + TimescaleDB | Free tier |
| AI | OpenAI GPT-4o | ~$0.01/query |
| Hosting | Vercel + Railway | Free tier |

**Build time:** 6-8 weeks | **Cost:** $100-300/mo

## Pricing Strategy

$99-499/mo based on monthly events tracked. Tiers: Starter (100K events), Growth (500K), Scale (2M+). Enterprise: custom pricing with dedicated support.

**Positioning:** "Know which ads actually make you money. Ask in plain English."

## Customer Acquisition

1. **LinkedIn content:** Share attribution insights. "Your Facebook ROAS is probably wrong. Here's why."
2. **Agency partnerships:** White-label for marketing agencies. They resell to their clients.
3. **Case studies:** "How [SaaS company] found 40% of their ad spend was wasted."

## Common Pitfalls

1. **Meta/Google APIs change constantly.** Budget 20% of engineering for API maintenance.
2. **Attribution is imprecise.** Don't overpromise. Say "directionally accurate" not "exact."
3. **Data storage costs scale fast.** Events table grows millions of rows. Implement data retention policies early.

## Launch Checklist

### Pre-Launch
- [ ] Build server-side tracking for Meta + Google
- [ ] Create attribution dashboard
- [ ] Add AI chat interface

### Launch
- [ ] Offer free attribution audit to 50 SaaS companies
- [ ] Post on LinkedIn with data insights
- [ ] Partner with 3 marketing agencies

### Post-Launch
- [ ] Add multi-touch attribution models
- [ ] Build integrations with HubSpot, Salesforce
- [ ] Scale to 100 paying customers

---

**Attribution:** Educational purposes. Data from [TrustMRR](https://trustmrr.com/startup/cometly).
**Disclaimer:** For learning only. Respect IP and trademarks.
