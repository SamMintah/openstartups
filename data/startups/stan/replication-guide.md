# Stan — Replication Guide

> How to build a creator monetization platform with storefronts, subscriptions, and bookings

## Overview

Stan is the #1 ranked product on TrustMRR with $3.6M MRR. It's a platform that enables creators, coaches, and influencers to monetize their audience without needing a team. Think: Shopify but specifically designed for individual creators who sell digital products, courses, memberships, and booking sessions. The core insight is that creators don't want to be website builders — they want a link in bio that actually converts.

**Key Metrics:**
- MRR: $3.6M
- TrustMRR Rank: #1
- Growth: Steady (mature)
- Team: Small team
- Focus: Creator economy

## Market Opportunity

**Niche:** Creator monetization — specifically the "link in bio" + digital storefront space.

**Why it's underserved:** Linktree and Beacons are great for linking, but don't handle transactions well. Shopify is powerful but overwhelming for a solo creator who just wants to sell a $29 ebook or a $200 coaching session. Stan sits in the sweet spot: simple enough for a creator to set up in 10 minutes, powerful enough to handle subscriptions, bookings, and digital product delivery.

**Competitive Landscape:**
- **Linktree** — links only, no commerce
- **Beacons** — closer competitor, but less focused on monetization
- **Ko-fi / Gumroad** — digital products only, no bookings or subscriptions
- **Shopify** — too complex for most creators
- **Stan** — all-in-one: storefront + subscriptions + bookings + courses

**Why now:** The creator economy is $100B+ and growing. Every influencer needs a monetization tool, and the existing options are either too simple (Linktree) or too complex (Shopify). AI is also lowering the barrier to creating digital products.

## MVP Build Guide

### Core Features (must-have for v1)

1. **Creator Storefront**
   - Custom URL (yourname.stan.store or custom domain)
   - Product grid layout with images, prices, descriptions
   - One-click checkout with Stripe
   - Mobile-first design (most creators' audience is mobile)

2. **Digital Product Delivery**
   - Upload and deliver PDFs, templates, presets, courses
   - Automatic delivery after payment
   - DRM or watermarking for premium content

3. **Booking/Consultation Module**
   - Calendar integration (Google Calendar, Calendly-style)
   - Accept payments for time slots
   - Automated confirmation emails

### Tech Stack

| Layer | Tool | Cost | Why |
|-------|------|------|-----|
| Frontend | Next.js + Tailwind | Free | Fast, mobile-first, SEO |
| Backend | Node.js + Express or tRPC | Free | Type-safe API |
| Database | PostgreSQL (Supabase) | Free tier | Products, orders, users |
| Payments | Stripe Connect | 2.9% + $0.30/txn | Handles splits, payouts |
| File Storage | Cloudflare R2 or Supabase Storage | Free tier | Digital product files |
| Calendar | Google Calendar API | Free | Booking integration |
| Auth | NextAuth or Clerk | Free tier | User accounts |
| Hosting | Vercel | Free tier | Auto-deploys |
| Email | Resend or Postmark | Free tier | Transactional emails |

**Total estimated MVP cost: $0–50/month**

### No-Code Alternative

**Faster path (1-3 weeks):**
- Storefront: Stan Store itself (meta — study their UX)
- Products: Gumroad for digital delivery
- Bookings: Calendly + Stripe
- Link page: Linktree or Beacons
- Integrate with Zapier

**Limitations:** Multiple tools = fragmented experience, higher fees (Gumroad takes 10%), no unified branding. Stan's advantage is the all-in-one simplicity.

### Build Time & Cost

- **With code:** 6-8 weeks for MVP (solo), 3-4 weeks (small team)
- **No-code hybrid:** 1-2 weeks
- **Budget:** $0-50/mo using free tiers

## Pricing Strategy

**Stan's model (reconstructed):**

| Plan | Price | What you get |
|------|-------|-------------|
| Free | $0 | Basic storefront, limited products |
| Pro | $29/mo | Unlimited products, bookings, analytics |
| Premium | $99/mo | Custom domain, priority support, team features |

**Pricing psychology:**
- $29/mo is the sweet spot — less than a single coaching session
- Creators think in terms of "one sale pays for the month"
- No transaction fees on paid plans (unlike Gumroad's 10%)

**How to position:**
- vs. Shopify: "Set up in 10 minutes, not 10 hours"
- vs. Linktree: "Turn your link in bio into a store"
- vs. Gumroad: "No transaction fees, plus bookings and subscriptions"

## Customer Acquisition

### Primary Channels

1. **Creator Partnerships (Affiliate/Referral)**
   - Pay creators 20-30% recurring commission for referrals
   - Creators recommend Stan to other creators (natural network effect)
   - This is likely Stan's primary growth engine

2. **TikTok / Instagram / YouTube Shorts**
   - Short-form content: "How I made $10K selling digital products"
   - Show the storefront in action
   - Creators are the audience AND the distribution channel

3. **SEO — "sell digital products" keywords**
   - Target: "how to sell digital products", "link in bio store", "sell courses online"
   - Create templates and guides that link to Stan

4. **Word of Mouth**
   - Stan's #1 position suggests strong organic growth
   - Creators talk to other creators at events, in DMs, in communities

### Content/SEO Strategy

- **Blog:** "How to sell your first digital product", "Creator monetization guide 2026"
- **Templates:** Free storefront templates that require Stan to use
- **YouTube:** Tutorials on setting up your creator store

### Early Traction Tactics

- **First 10 users:** DM 50 micro-creators (1K-10K followers) on Instagram, offer free Pro plan for 3 months
- **First 100 users:** Launch on Product Hunt + post in creator Facebook groups
- **First 1,000 users:** Affiliate program goes live + SEO content starts ranking

## Growth Levers

- **Affiliate program:** Every creator becomes a salesperson. 20% recurring commission means affiliates earn $5.80/mo per referral at $29/mo plan
- **Template marketplace:** Creators sell/customize storefront templates
- **Course builder:** Add a course creation tool (compete with Teachable)
- **AI product generator:** "Describe your product and I'll create the listing"

## Unit Economics (estimates)

- **ARPU:** $29/mo (most on Pro plan)
- **Estimated CAC:** $20-40 (affiliate commissions + marketing)
- **Payback period:** <2 months
- **LTV:** $348-580 (12-20 month avg retention × $29/mo)
- **LTV:CAC ratio:** 9:1 to 29:1 (excellent)

## Common Pitfalls

1. **Building too many features too fast.** Stan's genius is simplicity. Don't add 50 product types — start with digital products + bookings, nail that, then expand. Creators choose Stan BECAUSE it's simple.

2. **Ignoring mobile.** 70%+ of creator audiences browse on mobile. Your storefront MUST be mobile-first. Test on real phones, not just browser dev tools.

3. **Underpricing.** Creators will pay $29/mo if you save them time and make them money. Don't price at $9/mo — it signals low value and makes the math hard with affiliate commissions.

4. **Neglecting the checkout experience.** Every extra click loses 20% of buyers. Stripe Checkout (hosted) is fine — don't build custom checkout until you're at $1M+ MRR.

## Tools & Resources

- **Payments:** Stripe Connect (marketplace payments)
- **Calendar:** Google Calendar API, Calendly embed
- **File delivery:** Cloudflare R2, Supabase Storage
- **Email:** Resend, Postmark, Loops
- **Analytics:** Plausible, PostHog
- **Communities:** Creator Economy subreddit, Indie Hackers, Twitter #BuildInPublic

## Launch Checklist

### Pre-Launch (Week 1-2)
- [ ] Build storefront + digital product delivery
- [ ] Add booking module with calendar integration
- [ ] Set up Stripe Connect for payments
- [ ] Create 5 demo storefronts for different creator types
- [ ] Mobile test on 3+ real devices

### Launch (Week 3)
- [ ] Product Hunt launch with video demo
- [ ] DM 50 micro-creators with free Pro offer
- [ ] Post in 5 creator Facebook groups
- [ ] Set up analytics and conversion tracking

### Post-Launch (Week 4+)
- [ ] Onboard first 10 paying creators personally
- [ ] Launch affiliate program
- [ ] Start SEO content production
- [ ] Collect and implement top 5 feature requests
- [ ] Add referral program

---

**Attribution:** Build guide for educational purposes. Data sourced from [TrustMRR](https://trustmrr.com/startup/stan).

**Disclaimer:** This is for learning and inspiration. Respect intellectual property and trademarks when replicating.
