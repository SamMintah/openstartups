# 1Forge - Replication Guide

> How to build a focused product inspired by 1Forge

## Overview

Developers need reliable FX rates without negotiating with banks or data vendors. 1Forge packages currency data behind a simple API. The public metric snapshot shows $8,479 MRR across 173 customers. The lesson is not to copy the brand, but to study the narrow workflow, distribution channel, and pricing model.

**Key Metrics:**
- MRR: $8,479
- Customers: 173
- Source: Baremetrics Open Startups
- Category: Developer Tools
- Team: Small team

## Market Opportunity

**Niche:** Financial data APIs for currency and exchange-rate workflows.

**Why it is underserved:** Broad tools tend to ignore the exact workflow, vocabulary, and integrations that a narrow user group needs. A small product can win by being easier to adopt than a generic platform.

**Why now:** Buyers are comfortable subscribing to specialized tools when the product saves time, removes manual work, or plugs into a system they already use.

## MVP Build Guide

### Core Features

1. **Aggregate exchange-rate data from licensed or partner data feeds.**
2. **Expose REST and websocket endpoints with API keys, rate limits, and usage logs.**
3. **Add dashboards, docs, SDK examples, and billing by request volume.**

### Tech Stack

| Layer | Tool | Why |
|-------|------|-----|
| API | Fastify or Go | Proven choice for this workflow |
| Database | PostgreSQL | Proven choice for this workflow |
| Cache | Redis | Proven choice for this workflow |
| Docs | Mintlify/Docusaurus | Proven choice for this workflow |
| Payments | Stripe | Proven choice for this workflow |

### Build Time and Cost

- **Build time:** 4-6 weeks
- **Starting cost:** $100-300/mo

## Pricing Strategy

Usage-based API tiers. Free sandbox, then $9-99/mo by requests, symbols, and websocket access.

## Customer Acquisition

1. List in API marketplaces and developer directories.
2. Publish currency conversion examples for popular languages.
3. Target fintech builders and spreadsheet automation users.

## Unit Economics

- Start with low-touch onboarding if the price is below $50/mo.
- Use concierge onboarding if customers pay more than $100/mo.
- Watch support time per account; niche products can become service businesses if workflows are unclear.

## Common Pitfalls

1. Licensing matters. Do not resell data without rights.
2. Latency and uptime expectations are high for finance users.
3. Free tier abuse needs rate limiting from day one.

## Launch Checklist

### Pre-Launch
- [ ] Interview 10 target users and collect exact workflow language.
- [ ] Build the smallest workflow that produces a paid result.
- [ ] Add billing, onboarding, support email, and basic analytics.

### Launch
- [ ] Invite the first 20 prospects manually.
- [ ] Publish a comparison or teardown post for the existing manual process.
- [ ] Offer high-touch setup for the first paying customers.

### Post-Launch
- [ ] Turn repeated support questions into onboarding screens.
- [ ] Track activation, churn reasons, and top integrations.
- [ ] Add one acquisition channel at a time.

---

**Attribution:** Data sourced from [Baremetrics Open Startups](https://1forgeopen.baremetrics.com) for educational purposes.

**Disclaimer:** This guide is for learning and inspiration. Respect intellectual property, trademarks, and original positioning.
