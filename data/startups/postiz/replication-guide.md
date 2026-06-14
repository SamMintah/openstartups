# Postiz — Replication Guide

> How to build a social media scheduling tool from scratch

## Overview

This guide walks you through building an AI-powered social media scheduler inspired by Postiz.

## Phase 1: MVP (Week 1-2)

### Core Features
- User authentication
- Connect 1-2 social platforms (Twitter + LinkedIn)
- Basic scheduling (time-slot based)
- Simple dashboard

### Tech Stack
- **Frontend:** Next.js + Tailwind CSS
- **Backend:** Next.js API routes
- **Database:** Supabase (PostgreSQL + Auth)
- **Payments:** Stripe
- **AI:** OpenAI API

### Steps

1. **Set up project**
   ```bash
   npx create-next-app@latest social-scheduler --typescript --tailwind
   cd social-scheduler
   npm install @supabase/supabase-js stripe openai
   ```

2. **Configure Supabase**
   - Create project at supabase.com
   - Set up users table
   - Configure auth providers

3. **Build Twitter integration**
   - Use Twitter API v2
   - OAuth 2.0 flow
   - Schedule posts endpoint

4. **Create scheduling UI**
   - Calendar view
   - Post composer
   - Platform selector

5. **Add Stripe payments**
   - Create pricing page
   - Set up webhook handler
   - Gate features behind subscription

## Phase 2: Launch (Week 3-4)

### Pre-Launch
- Build landing page with clear value prop
- Set up analytics (Plausible/PostHog)
- Create Product Hunt listing

### Launch Day
- Post on Twitter/X
- Submit to Product Hunt
- Share in relevant communities (r/SaaS, Indie Hackers)
- Email your network

### Post-Launch
- Respond to all feedback
- Fix critical bugs immediately
- Ship quick wins from user requests

## Phase 3: Growth (Month 2+)

### Content Marketing
- Write about social media strategy
- Share building-in-public updates
- Create comparison posts (vs competitors)

### SEO
- Target "social media scheduler" keywords
- Create landing pages for each platform
- Write how-to guides

### Community
- Active Twitter/X presence
- Discord/Slack community
- Open-source contributions

## No-Code Alternative

For non-technical builders:
- **Tool:** Bubble.io or Softr
- **Auth:** Clerk or Auth0
- **Payments:** Stripe or Lemon Squeezy
- **Scheduling:** Use Make.com or Zapier for integrations

## Cost Estimate

| Item | Monthly Cost |
|------|-------------|
| Vercel hosting | $0 (hobby) |
| Supabase | $0 (free tier) |
| Domain | $1 |
| Stripe | 2.9% + $0.30/txn |
| OpenAI API | ~$20/mo |
| **Total** | **~$21/mo** |

---

**Attribution:** Sourced from [TrustMRR](https://trustmrr.com) – for educational purposes.

**Disclaimer:** This is for learning and inspiration. Respect intellectual property and trademarks when replicating.
