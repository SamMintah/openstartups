# PROSP — Replication Guide

> How to build AI-powered LinkedIn outreach automation

## Overview

PROSP automates LinkedIn outreach with AI. Prospecting + personalized message sequences. $128K MRR, Rank #14. The core insight: sales teams spend hours on manual LinkedIn prospecting with low reply rates. AI personalization at scale changes the math.

**Key Metrics:** MRR: $128K | Rank: #14 | Team: Small

## Market Opportunity

**Niche:** B2B sales automation — LinkedIn specifically.

**Why underserved:** LinkedIn is the #1 B2B prospecting channel but manual outreach doesn't scale. Existing tools (LinkedHelper, Dux-Soup) are clunky and lack AI. PROSP combines automation with AI-written messages.

**Competitive Landscape:** LinkedHelper (automation only), Waalaxy (French market), Lemlist (email-focused). PROSP differentiates on AI personalization quality.

## MVP Build Guide

### Core Features
1. LinkedIn connection request automation
2. AI-personalized follow-up messages
3. Campaign dashboard with reply tracking

### Tech Stack
| Layer | Tool | Cost |
|-------|------|------|
| Backend | Python + Selenium/Playwright | Free |
| AI | OpenAI GPT-4o | ~$0.005/message |
| Frontend | Next.js | Free |
| Database | PostgreSQL | Free tier |
| Payments | Stripe | 2.9%+$0.30 |

**Build time:** 4-6 weeks | **Cost:** $50-100/mo

## Pricing Strategy

$99/mo per seat. Team pricing at $79/seat for 5+. Free 7-day trial. No long-term contracts.

**Positioning:** "10x your LinkedIn pipeline without hiring an SDR."

## Customer Acquisition

1. **LinkedIn influencers:** Partner with 5 sales influencers. They promote PROSP to their audience.
2. **Sales communities:** Post in Sales Hacker, Revenue Collective, LinkedIn sales groups.
3. **Cold outreach:** Use PROSP itself to prospect potential customers (meta-marketing).

## Common Pitfalls

1. **LinkedIn account bans are real.** Implement human-like delays, rotation, and daily limits. This is the #1 risk.
2. **AI personalization must be good.** Bad AI messages = low reply rates = churn. Invest heavily in prompt engineering.
3. **LinkedIn ToS is a gray area.** Automation violates LinkedIn's terms. Have a legal review and clear user warnings.

## Launch Checklist

### Pre-Launch
- [ ] Build connection + messaging automation
- [ ] Implement rate limiting and human-like behavior
- [ ] Create AI personalization engine

### Launch
- [ ] Partner with 3 LinkedIn influencers
- [ ] Post in sales communities
- [ ] Offer 7-day free trial

### Post-Launch
- [ ] Add CRM integrations (HubSpot, Salesforce)
- [ ] Build A/B testing for message variants
- [ ] Create case studies with reply rate data

---

**Attribution:** Educational purposes. Data from [TrustMRR](https://trustmrr.com/startup/prosp).
**Disclaimer:** For learning only. Respect IP and trademarks.
