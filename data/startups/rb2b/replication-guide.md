# RB2B - Replication Guide

> How to build a focused product inspired by RB2B

## Overview

B2B teams get useful website visits but cannot see which companies are researching them. RB2B turns anonymous traffic into sales-ready account signals so teams can follow up while intent is fresh. The public metric snapshot shows $771,529 MRR across 3,663 customers. The lesson is not to copy the brand, but to study the narrow workflow, distribution channel, and pricing model.

**Key Metrics:**
- MRR: $771,529
- Customers: 3,663
- Source: Baremetrics Open Startups
- Category: Marketing
- Team: Team

## Market Opportunity

**Niche:** Website visitor identification and intent data for B2B sales.

**Why it is underserved:** Broad tools tend to ignore the exact workflow, vocabulary, and integrations that a narrow user group needs. A small product can win by being easier to adopt than a generic platform.

**Why now:** Buyers are comfortable subscribing to specialized tools when the product saves time, removes manual work, or plugs into a system they already use.

## MVP Build Guide

### Core Features

1. **Add a lightweight tracking script that identifies visiting companies from IP, firmographic, and enrichment data.**
2. **Build a lead feed with company, page path, visit history, and confidence score.**
3. **Push qualified visits into Slack, HubSpot, Salesforce, or email workflows.**

### Tech Stack

| Layer | Tool | Why |
|-------|------|-----|
| Frontend | Next.js | Proven choice for this workflow |
| Backend | Node.js or Python | Proven choice for this workflow |
| Database | PostgreSQL | Proven choice for this workflow |
| Enrichment | Clearbit/Apollo-style providers | Proven choice for this workflow |
| Integrations | HubSpot, Salesforce, Slack | Proven choice for this workflow |

### Build Time and Cost

- **Build time:** 6-8 weeks
- **Starting cost:** $150-400/mo

## Pricing Strategy

Usage-based or seat-based plans. Start with a free trial, then $99-499/mo based on identified companies and integrations.

## Customer Acquisition

1. Rank for visitor identification and website intent keywords.
2. Partner with outbound agencies and RevOps consultants.
3. Publish teardown content showing missed pipeline from anonymous traffic.

## Unit Economics

- Start with low-touch onboarding if the price is below $50/mo.
- Use concierge onboarding if customers pay more than $100/mo.
- Watch support time per account; niche products can become service businesses if workflows are unclear.

## Common Pitfalls

1. Data quality is the product. Weak match rates will destroy trust quickly.
2. Respect privacy laws and give customers clear compliance controls.
3. Do not overbuild CRM features; integrate with the systems sales teams already use.

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

**Attribution:** Data sourced from [Baremetrics Open Startups](https://rb2b.baremetrics.com) for educational purposes.

**Disclaimer:** This guide is for learning and inspiration. Respect intellectual property, trademarks, and original positioning.
