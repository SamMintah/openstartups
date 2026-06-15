# PropGPT — Replication Guide

> How to build an AI sports betting analysis app

## Overview

PropGPT is an AI sports betting props analysis app — the first AI app dedicated to transforming sports betting strategy. $96K MRR, Rank #17. The core insight: sports bettors lack data-driven tools to evaluate prop bets efficiently. AI can aggregate stats and identify value bets.

**Key Metrics:** MRR: $96K | Rank: #17 | Growth: +3% MoM | Team: Small

## Market Opportunity

**Niche:** AI-powered sports betting analysis — props specifically.

**Why underserved:** Sports betting is $100B+ globally. Existing tools are either expensive pro services or basic stat lookups. AI can analyze player trends, injury impacts, and matchup data to find value in prop bets.

**Competitive Landscape:** Action Network (news, not analysis), TheScore (basic stats), PrizePicks (platform, not analysis). PropGPT is the AI layer on top of betting data.

## MVP Build Guide

### Core Features
1. Aggregated player stats + injury data
2. AI model to score prop bets by expected value
3. Mobile app with daily recommendations

### Tech Stack
| Layer | Tool | Cost |
|-------|------|------|
| Mobile | React Native | Free |
| Backend | Python + FastAPI | Free |
| AI | OpenAI / custom ML model | $50-100/mo |
| Data | Sports data APIs (SportsDataIO) | $50-100/mo |
| Database | PostgreSQL | Free tier |
| Payments | Stripe | 2.9%+$0.30 |

**Build time:** 6-8 weeks | **Cost:** $100-200/mo

## Pricing Strategy

$9.99/mo for standard access. $29.99/mo for premium (more props, real-time alerts). No free tier — bettors expect to pay for edges.

**Positioning:** "AI-powered prop analysis. Data-driven bets, not gut feelings."

## Customer Acquisition

1. **Reddit:** r/sportsbook, r/dfsports. Share insights, not promotions.
2. **Twitter:** Post daily prop analysis. Build following before selling.
3. **Affiliate:** Partner with sportsbooks for referral revenue.

## Common Pitfalls

1. **Sports data APIs are expensive.** Budget $500+/mo for comprehensive data. Start with one sport (NFL or NBA).
2. **Gambling regulations vary.** Consult legal counsel. You're providing analysis, not taking bets.
3. **User expectations are unrealistically high.** They want guaranteed wins. Set expectations: "Data-driven, not guaranteed."

## Launch Checklist

### Pre-Launch
- [ ] Integrate sports data API for one sport
- [ ] Build AI scoring model
- [ ] Create mobile app MVP

### Launch
- [ ] Post daily analysis on Twitter
- [ ] Share on r/sportsbook
- [ ] Launch at $9.99/mo

### Post-Launch
- [ ] Add more sports (NFL, NBA, MLB, NHL)
- [ ] Build parlay builder feature
- [ ] Add live betting alerts

---

**Attribution:** Educational purposes. Data from [TrustMRR](https://trustmrr.com/startup/propgpt-ai-props-analysis).
**Disclaimer:** For learning only. Respect IP and trademarks.
