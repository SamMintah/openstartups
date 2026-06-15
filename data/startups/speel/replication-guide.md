# Speel — Replication Guide

> How to build an AI UGC video generation platform for ads

## Overview

Speel generates AI UGC-style videos and images for ads. 0 to $1M ARR in 3 months. $66K MRR, Rank #24. The core insight: brands need authentic-looking UGC ad creatives but real UGC is slow and expensive. AI can generate UGC-style content at scale.

**Key Metrics:** MRR: $66K | Rank: #24 | Team: Small

## Market Opportunity

**Niche:** AI-generated UGC for performance marketing.

**Why underserved:** UGC ads convert 4x better than branded content but sourcing real UGC costs $200-500 per video. AI can generate similar quality at 1/10th the cost and 100x the speed.

**Competitive Landscape:** AdCreative.ai (different format), Pika (general video), Runway (pro tools). Speel specifically targets UGC ad format.

## MVP Build Guide

### Core Features
1. Prompt → UGC video pipeline
2. Multiple UGC styles (testimonial, unboxing, demo)
3. Export in ad formats (9:16, 1:1, 16:9)

### Tech Stack
| Layer | Tool | Cost |
|-------|------|------|
| Frontend | Next.js | Free |
| Backend | Python | Free |
| Video AI | Runway / Pika API | $0.05-0.10/sec |
| Voice | ElevenLabs | $0.01/sec |
| Hosting | AWS | Pay-per-use |
| Payments | Stripe | 2.9%+$0.30 |

**Build time:** 4-6 weeks | **Cost:** $200-500/mo (scales with usage)

## Pricing Strategy

$99/mo for 50 credits. $299/mo for 200 credits. Enterprise: custom.

**Positioning:** "AI UGC ads at 1/10th the cost. Launch 100 ads in the time it takes to film 1."

## Customer Acquisition

1. **Shopify DTC communities:** Facebook groups for DTC brands. Show before/after ad performance.
2. **Content marketing:** "How we generated 100 UGC ads in 1 day"
3. **Partnerships:** Ad agencies that manage DTC brands.

## Common Pitfalls

1. **AI video quality is inconsistent.** Offer a human review/edit option for premium tier.
2. **API costs at scale.** Cache common styles. Use cheaper models for drafts.
3. **Brands may not trust AI UGC.** Show performance data. "AI UGC gets 3.2x CTR vs branded."

## Launch Checklist

### Pre-Launch
- [ ] Build prompt → video pipeline
- [ ] Create 20 sample UGC videos
- [ ] Test ad performance vs real UGC

### Launch
- [ ] Post in Shopify DTC Facebook groups
- [ ] Launch on Product Hunt
- [ ] Offer 10 free credits to first 100 users

### Post-Launch
- [ ] Add more UGC styles
- [ ] Build A/B testing for ad variants
- [ ] Create agency dashboard

---

**Attribution:** Educational purposes. Data from [TrustMRR](https://trustmrr.com/startup/speel-co).
**Disclaimer:** For learning only. Respect IP and trademarks.
