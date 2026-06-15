# If No Reply - Replication Guide

> How to build a focused product inspired by If No Reply

## Overview

People forget to follow up after important emails. A lightweight reminder and sequence tool can make personal outreach more reliable without a full sales suite. The public metric snapshot shows GBP0 MRR across 0 customers. The lesson is not to copy the brand, but to study the narrow workflow, distribution channel, and pricing model.

**Key Metrics:**
- MRR: GBP0
- Customers: 0
- Source: Baremetrics Open Startups
- Category: Marketing
- Team: Small team

## Market Opportunity

**Niche:** Lightweight email follow-up automation.

**Why it is underserved:** Broad tools tend to ignore the exact workflow, vocabulary, and integrations that a narrow user group needs. A small product can win by being easier to adopt than a generic platform.

**Why now:** Buyers are comfortable subscribing to specialized tools when the product saves time, removes manual work, or plugs into a system they already use.

## MVP Build Guide

### Core Features

1. **Build Gmail/Outlook integration that detects sent emails and reply status.**
2. **Let users set follow-up rules like if no reply after 3 days, remind me or send draft.**
3. **Add templates, snooze, contact history, and privacy controls.**

### Tech Stack

| Layer | Tool | Why |
|-------|------|-----|
| Frontend | Next.js | Proven choice for this workflow |
| Backend | Node.js | Proven choice for this workflow |
| Email APIs | Gmail and Microsoft Graph | Proven choice for this workflow |
| Database | PostgreSQL | Proven choice for this workflow |
| Payments | Stripe | Proven choice for this workflow |

### Build Time and Cost

- **Build time:** 3-4 weeks
- **Starting cost:** $30-100/mo

## Pricing Strategy

Freemium with a small pro tier. Charge GBP 5-15/mo for unlimited follow-ups and templates.

## Customer Acquisition

1. Target freelancer and founder communities with follow-up templates.
2. Create content around polite follow-up emails.
3. Offer a Chrome extension for fast discovery.

## Unit Economics

- Start with low-touch onboarding if the price is below $50/mo.
- Use concierge onboarding if customers pay more than $100/mo.
- Watch support time per account; niche products can become service businesses if workflows are unclear.

## Common Pitfalls

1. Email API permissions create trust friction.
2. Automated sending can feel spammy; keep the product personal and consent-driven.
3. A zero-MRR public dashboard means this should be treated as a case study, not proof of current growth.

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

**Attribution:** Data sourced from [Baremetrics Open Startups](https://ifnoreply.baremetrics.com) for educational purposes.

**Disclaimer:** This guide is for learning and inspiration. Respect intellectual property, trademarks, and original positioning.
