# Ghost - Replication Guide

> How to build a focused product inspired by Ghost

## Overview

Independent publishers need publishing, newsletters, memberships, and payments in one place without handing their audience to closed social platforms. Ghost packages open source publishing with managed hosting. The public metric snapshot shows $895,920 MRR. The lesson is not to copy the brand, but to study the narrow workflow, distribution channel, and pricing model.

**Key Metrics:**
- MRR: $895,920
- Source: Ghost official metrics
- Category: SaaS
- Team: Team

## Market Opportunity

**Niche:** Creator publishing and membership infrastructure.

**Why it is underserved:** Broad tools tend to ignore the exact workflow, vocabulary, and integrations that a narrow user group needs. A small product can win by being easier to adopt than a generic platform.

**Why now:** Buyers are comfortable subscribing to specialized tools when the product saves time, removes manual work, or plugs into a system they already use.

## MVP Build Guide

### Core Features

1. **Build publishing primitives: editor, posts, themes, tags, and SEO metadata.**
2. **Add membership accounts, subscriptions, email newsletters, and Stripe billing.**
3. **Offer managed hosting, migrations, backups, and premium support as the commercial layer.**

### Tech Stack

| Layer | Tool | Why |
|-------|------|-----|
| Frontend | Theme system + admin app | Proven choice for this workflow |
| Backend | Node.js | Proven choice for this workflow |
| Database | MySQL | Proven choice for this workflow |
| Payments | Stripe | Proven choice for this workflow |
| Email | Mailgun-style provider | Proven choice for this workflow |

### Build Time and Cost

- **Build time:** 10-12 weeks
- **Starting cost:** $100-300/mo

## Pricing Strategy

Open source core plus hosted plans. Price by publication size, staff seats, and newsletter volume.

## Customer Acquisition

1. Own search around creator publishing, newsletter platform, and Substack alternatives.
2. Use open source community as trust and distribution.
3. Publish transparent metrics to build credibility with publishers.

## Unit Economics

- Start with low-touch onboarding if the price is below $50/mo.
- Use concierge onboarding if customers pay more than $100/mo.
- Watch support time per account; niche products can become service businesses if workflows are unclear.

## Common Pitfalls

1. Email deliverability is a core product surface, not an add-on.
2. Theme ecosystem quality affects activation.
3. Large publishers need migration and support, not just software.

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

**Attribution:** Data sourced from [Ghost official metrics](https://ghost.org/about/#metrics) for educational purposes.

**Disclaimer:** This guide is for learning and inspiration. Respect intellectual property, trademarks, and original positioning.
