# Postiz — Replication Guide

> How to build an open-source AI social media scheduler with agentic capabilities

## Overview

Postiz is an open-source social media scheduling tool with 3,896 active subscriptions and $143K MRR, growing at 24% MoM. Built solo by Nevo David, it's the only open-source alternative to Buffer/Hootsuite that includes AI-powered content repurposing. The core insight: social media management is expensive ($50-500/mo for existing tools) and creators waste hours repurposing content across platforms. Postiz automates this with AI agents that turn one piece of content into platform-specific posts.

**Key Metrics:**
- MRR: $143K
- TrustMRR Rank: #12
- Growth: +24% MoM
- Team: Solo (Nevo David)
- Active subscriptions: 3,896
- Open source: Yes (GitHub)

## Market Opportunity

**Niche:** Social media management for creators, small businesses, and agencies.

**Why it's underserved:** Buffer ($15/mo) is simple but has no AI. Hootsuite ($99/mo) is enterprise-focused and expensive. Later, Sprout Social — same problem. None of them offer open-source self-hosting. The gap: an affordable, AI-powered, open-source tool that handles scheduling + content repurposing.

**Competitive Landscape:**
- **Buffer** — simple, affordable, no AI
- **Hootsuite** — enterprise, expensive, complex
- **Later** — visual planning, Instagram-focused
- **Typefully** — Twitter-only, good AI
- **Postiz** — multi-platform, AI, open source, affordable

**Why now:** AI costs dropped 10x in 2024-2025. Social media platforms are fragmenting (TikTok, Threads, Bluesky, LinkedIn). Creators need to post everywhere but can't afford to manage each platform manually.

## MVP Build Guide

### Core Features (must-have for v1)

1. **Multi-Platform Scheduling**
   - Connect: Twitter/X, LinkedIn, Instagram, Facebook, TikTok
   - Schedule posts with platform-specific formatting
   - Calendar view for visual planning
   - Best-time-to-post suggestions

2. **AI Content Repurposing**
   - Input: one blog post, video, or long-form content
   - Output: platform-specific posts (tweet thread, LinkedIn post, Instagram caption, etc.)
   - Tone and format adaptation per platform

3. **Analytics Dashboard**
   - Track engagement across all connected platforms
   - Best performing content analysis
   - Follower growth tracking

### Tech Stack

| Layer | Tool | Cost | Why |
|-------|------|------|-----|
| Frontend | Next.js + Tailwind | Free | Modern, fast |
| Backend | NestJS | Free | Type-safe, scalable |
| Database | PostgreSQL (Prisma ORM) | Free tier | Relational data |
| AI | OpenAI GPT-4o API | ~$0.01/post | Content generation |
| Social APIs | Twitter API v2, LinkedIn API, Meta Graph API | Free tier | Platform posting |
| Payments | Stripe | 2.9% + $0.30/txn | Subscriptions |
| Auth | NextAuth or Lucia | Free | User accounts |
| Hosting | Vercel + Railway | Free tier | Frontend + backend |
| Redis | Upstash | Free tier | Job queues (BullMQ) |

**Total estimated MVP cost: $0–80/month**

### No-Code Alternative

**Faster path (2-3 weeks):**
- Scheduling: Buffer API or Typefully
- AI: OpenAI API called via Zapier
- Analytics: Platform native analytics
- Landing page: Carrd or Framer

**Limitations:** Can't self-host, limited customization, 10%+ fees on aggregators. The whole point of Postiz is owning the tool.

### Build Time & Cost

- **With code:** 6-8 weeks (solo), 3-4 weeks (team)
- **No-code hybrid:** 2-3 weeks
- **Budget:** $0-80/mo

## Pricing Strategy

**Postiz's model (reconstructed):**

| Plan | Price | What you get |
|------|-------|-------------|
| Free (self-host) | $0 | Full features, your own server |
| Free (cloud) | $0 | 3 social accounts, 30 posts/mo |
| Pro | $19/mo | Unlimited accounts, unlimited posts, AI |
| Business | $49/mo | Team features, white-label, priority support |
| Enterprise | $200+/mo | Self-hosted, dedicated support, custom integrations |

**Pricing psychology:**
- Free tier is generous enough to hook users, limited enough to drive upgrades
- Self-hosting option is a moat — devs love it, competitors can't match it
- AI repurposing is the premium upsell — saves 5+ hours/week

**How to position:**
- vs. Buffer: "AI-powered repurposing, not just scheduling"
- vs. Hootsuite: "Enterprise features at 1/5th the price"
- vs. Typefully: "Multi-platform, not just Twitter"

## Customer Acquisition

### Primary Channels

1. **Open Source Community (GitHub)**
   - Build in public on Twitter/X with #BuildInPublic
   - GitHub stars drive organic discovery (aim for 5K+ stars)
   - Contributors become evangelists
   - Self-hosters often upgrade to paid cloud

2. **Twitter/X Building in Public**
   - Post weekly MRR updates, feature launches, user stories
   - Nevo David's personal brand drives significant traffic
   - Engage with #IndieHacker and #SaaS communities

3. **SEO — "open source social media scheduler"**
   - Target: "open source buffer alternative", "free social media scheduler", "AI content repurposing"
   - Comparison pages: "Postiz vs Buffer vs Hootsuite"

4. **Product Hunt**
   - Launch the open-source version first
   - Launch cloud version separately later
   - Open source launches get extra community support

### Content/SEO Strategy

- **Blog:** "How I built a $143K MRR SaaS solo", "Open source social media management guide"
- **YouTube:** "Building Postiz in public" series
- **GitHub:** Detailed README, contributing guide, good first issues

### Early Traction Tactics

- **First 10 users:** Post on r/selfhosted, r/opensource, Indie Hackers. Offer free cloud tier.
- **First 100 users:** GitHub reaches 1K stars → Hacker News front page
- **First 1,000 users:** Product Hunt launch + Twitter viral thread

## Growth Levers

- **Open source flywheel:** More stars → more contributors → better product → more stars
- **Self-hosting → cloud conversion:** Devs self-host for free, then pay for convenience
- **Agency white-label:** $200/mo for agencies to brand Postiz as their own
- **AI upsell:** Free scheduling, paid AI repurposing

## Unit Economics (estimates)

- **ARPU:** $19/mo (Pro plan)
- **Estimated CAC:** $5-15 (organic/SEO-driven)
- **Payback period:** <1 month
- **LTV:** $190-380 (10-20 month retention × $19/mo)
- **LTV:CAC ratio:** 13:1 to 76:1 (excellent)

## Common Pitfalls

1. **Social API rate limits and deprecations.** Twitter, LinkedIn, and Meta change their APIs constantly. Build abstraction layers so you can swap providers. Budget 20% of engineering time for API maintenance.

2. **Underestimating the self-hosting support burden.** Open source users file issues for things that aren't bugs. Have a clear triage process and label issues by priority.

3. **AI costs spiraling.** GPT-4o calls add up at scale. Cache common repurposing patterns, use GPT-4o-mini for simple tasks, and set per-user AI quotas.

4. **Feature creep from community requests.** The open source community will want every platform and every feature. Stay focused on the core: scheduling + AI repurposing. Let plugins handle the rest.

## Tools & Resources

- **Social APIs:** Twitter API v2, LinkedIn Marketing API, Meta Graph API, TikTok API
- **AI:** OpenAI GPT-4o, Anthropic Claude
- **Scheduling:** BullMQ (Redis-based job queue)
- **Open Source:** GitHub Actions for CI/CD, Docker for self-hosting
- **Communities:** r/selfhosted, Indie Hackers, Product Hunt, Twitter #BuildInPublic

## Launch Checklist

### Pre-Launch (Week 1-2)
- [ ] Fork/build the core scheduling engine
- [ ] Integrate 3 social platforms minimum
- [ ] Add AI repurposing for 2 platforms
- [ ] Set up Stripe for cloud version
- [ ] Write comprehensive README and docs

### Launch (Week 3)
- [ ] Launch on GitHub with good README
- [ ] Post on r/selfhosted, Indie Hackers
- [ ] Share on Twitter with build-in-public thread
- [ ] Submit to Product Hunt

### Post-Launch (Week 4+)
- [ ] Respond to all GitHub issues within 24 hours
- [ ] Ship top 3 community-requested features
- [ ] Start SEO content production
- [ ] Launch affiliate/referral program
- [ ] Begin enterprise outreach

---

**Attribution:** Build guide for educational purposes. Data sourced from [TrustMRR](https://trustmrr.com/startup/postiz).

**Disclaimer:** This is for learning and inspiration. Respect intellectual property and trademarks when replicating.
