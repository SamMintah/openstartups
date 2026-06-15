# 1Lookup — Replication Guide

> How to build a unified validation API for phone, email, and IP

## Overview

1Lookup provides real-time phone, email, and IP validation through a single API endpoint. $227K MRR, Rank #6, growing 16% MoM. The core insight: developers waste time stitching together 3-5 different validation APIs. One endpoint that does everything is worth a premium.

**Key Metrics:** MRR: $227K | Rank: #6 | Growth: +16% MoM | Team: Solo/small

## Market Opportunity

**Niche:** Developer-facing data validation APIs.

**Why underserved:** Twilio handles phone, Kickbox handles email, ipinfo handles IP — but nobody combines all three with a single pricing model. The "API marketplace" approach (RapidAPI) has made discovery easier but comparison shopping harder.

**Competitive Landscape:** Twilio (phone-only), Kickbox (email-only), Abstract API (partial). 1Lookup wins on completeness and simplicity.

## MVP Build Guide

### Core Features
1. Single REST endpoint: POST /validate with phone, email, or IP
2. Response: valid/invalid + enriched data (carrier, location, role detection)
3. Batch validation endpoint for bulk lists

### Tech Stack
| Layer | Tool | Cost |
|-------|------|------|
| API | Node.js + Fastify | Free |
| Cache | Redis (Upstash) | Free tier |
| Providers | Twilio + Kickbox + ipinfo | Pay-per-use |
| Database | PostgreSQL | Free tier |
| Payments | Stripe | 2.9%+$0.30 |

**Build time:** 3-4 weeks | **Cost:** $0-50/mo (scales with usage)

### No-Code Alternative
Zapier + individual APIs. Limitations: no single endpoint, high latency, expensive at scale. Only viable for <100 lookups/day.

## Pricing Strategy

Usage-based pricing. $0.001-0.01 per lookup depending on type and volume. Free tier: 1,000 lookups/month. Enterprise: custom volume discounts.

**Positioning:** "One API to validate everything. No more API spaghetti."

## Customer Acquisition

1. **RapidAPI marketplace:** List on RapidAPI. Many developers discover APIs here. Free tier drives trials.
2. **Developer content:** Blog posts: "How to validate emails at scale", "Phone number validation best practices"
3. **Cold outreach:** Contact SaaS companies with validation-heavy onboarding flows.

## Common Pitfalls

1. **API uptime is critical.** Use fallback providers. If Twilio is down, route to a backup. 99.9% uptime minimum.
2. **Rate limiting is tricky.** Implement per-key rate limiting from day one. Don't let one customer hog all resources.
3. **Enterprise sales are different.** Self-serve API ≠ enterprise contracts. Have a separate sales motion for $1K+/mo customers.

## Launch Checklist

### Pre-Launch
- [ ] Integrate 3 providers with fallback routing
- [ ] Build rate limiting and usage tracking
- [ ] Create API documentation (OpenAPI/Swagger)

### Launch
- [ ] List on RapidAPI
- [ ] Post on r/webdev, Indie Hackers
- [ ] Offer 10K free lookups for early adopters

### Post-Launch
- [ ] Monitor uptime obsessively
- [ ] Add batch validation endpoint
- [ ] Begin enterprise outreach

---

**Attribution:** Educational purposes. Data from [TrustMRR](https://trustmrr.com/startup/1lookup).
**Disclaimer:** For learning only. Respect IP and trademarks.
