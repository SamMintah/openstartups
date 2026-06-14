#!/usr/bin/env python3
"""Generate startup entries from HTML data."""

import json
import os
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data" / "startups"

STARTUPS = [
    {
        "id": "stan",
        "name": "Stan",
        "rank": 1,
        "mrr": 3569654,
        "growth": None,
        "cat": "SaaS",
        "desc": "Platform enabling people to work for themselves — creator storefronts, subscriptions, bookings.",
        "problem": "Creators lack a single tool to monetize their audience without a team",
        "audience": "Solo creators, coaches",
        "team": "Small team",
        "open": False,
        "source": "https://trustmrr.com/startup/stan",
        "tech": "Custom SaaS",
        "build": [
            "Build a creator storefront with Stripe Checkout",
            "Add subscription & booking modules",
            "Grow via influencer/creator referrals",
            "White-glove onboarding for top creators"
        ],
        "website": "https://stan.store",
        "founded": None,
        "country": None,
    },
    {
        "id": "rezi",
        "name": "Rezi",
        "rank": 4,
        "mrr": 270423,
        "growth": 8,
        "cat": "AI",
        "desc": "AI-powered resume builder. ~1M new users per year. Rezi Enterprise serves 300+ organizations.",
        "problem": "Job seekers lack tools to create ATS-optimized resumes at scale",
        "audience": "Job seekers, universities, enterprises",
        "team": "Small team",
        "open": False,
        "source": "https://trustmrr.com/startup/rezi",
        "tech": "React, Node.js, AI/ML, Stripe",
        "build": [
            "Build ATS resume parser + AI optimizer",
            "Add job description matching feature",
            "Launch freemium: free resume, paid exports",
            "Target universities for bulk licensing deals"
        ],
        "website": "https://rezi.ai",
        "founded": None,
        "country": None,
    },
    {
        "id": "kibu",
        "name": "Kibu",
        "rank": 5,
        "mrr": 234319,
        "growth": None,
        "cat": "SaaS",
        "desc": "EHR and compliance software for organizations serving people with intellectual and developmental disabilities (I/DD). 48 states.",
        "problem": "I/DD provider orgs drown in compliance paperwork and fragmented care documentation",
        "audience": "Healthcare orgs, I/DD providers",
        "team": "Small team",
        "open": False,
        "source": "https://trustmrr.com/startup/kibu",
        "tech": "Healthcare SaaS stack, HIPAA compliant",
        "build": [
            "Pick a single compliance pain point (progress notes)",
            "Get 3 pilot orgs signed up at $0",
            "Charge when you save them 5+ hrs/week",
            "Expand to billing + EHR modules"
        ],
        "website": "https://kibu.com",
        "founded": None,
        "country": None,
    },
    {
        "id": "1lookup",
        "name": "1Lookup",
        "rank": 6,
        "mrr": 226656,
        "growth": 16,
        "cat": "Developer Tools",
        "desc": "Real-time phone, email, and IP validation API. Single endpoint for all data validation needs.",
        "problem": "Developers waste time stitching together 3–5 different validation APIs",
        "audience": "Developers, SaaS companies",
        "team": "Solo/small",
        "open": False,
        "source": "https://trustmrr.com/startup/1lookup",
        "tech": "Node.js, API gateway, Stripe",
        "build": [
            "Wrap 3 validation providers into one API",
            "Launch on RapidAPI marketplace first",
            "Offer 1,000 free credits no card required",
            "Price by usage volume with enterprise plans"
        ],
        "website": "https://1lookup.com",
        "founded": None,
        "country": None,
    },
    {
        "id": "cometly",
        "name": "Cometly",
        "rank": 7,
        "mrr": 201007,
        "growth": 3,
        "cat": "Marketing",
        "desc": "Marketing attribution and analytics for SaaS companies. AI chat interface for ad data.",
        "problem": "Meta/Google pixel attribution breaks after iOS14 — marketers flying blind",
        "audience": "SaaS marketing teams, performance agencies",
        "team": "Small team",
        "open": False,
        "source": "https://trustmrr.com/startup/cometly",
        "tech": "React, Python, Stripe, AI",
        "build": [
            "Build server-side event tracking for Meta + Google",
            "Create a single attribution dashboard",
            "Offer free 14-day trial, no credit card",
            "Target DTC and SaaS CMOs via LinkedIn"
        ],
        "website": "https://cometly.com",
        "founded": None,
        "country": None,
    },
    {
        "id": "supliful",
        "name": "Supliful",
        "rank": 8,
        "mrr": 190816,
        "growth": 2,
        "cat": "SaaS",
        "desc": "All-in-one platform for creators to launch CPG brands — product selection, e-commerce, fulfillment. No upfront costs.",
        "problem": "Creators want physical product lines but lack supplier/logistics relationships",
        "audience": "Content creators, influencers",
        "team": "Team",
        "open": False,
        "source": "https://trustmrr.com/startup/brand-on-demand-inc",
        "tech": "Shopify integration, fulfillment API, Stripe",
        "build": [
            "Partner with 2–3 white-label supplement manufacturers",
            "Build product catalog + brand customization tool",
            "Integrate with Shopify for storefront creation",
            "Charge margin on each sale, no subscription fee"
        ],
        "website": "https://supliful.com",
        "founded": None,
        "country": None,
    },
    {
        "id": "postiz",
        "name": "Postiz",
        "rank": 12,
        "mrr": 142648,
        "growth": 24,
        "cat": "AI",
        "desc": "Agentic social media scheduler tool. 3,896 active subscriptions. Open source.",
        "problem": "Creators and agencies spend hours manually scheduling and repurposing content",
        "audience": "Creators, agencies, B2B",
        "team": "Solo (Nevo David)",
        "open": True,
        "source": "https://trustmrr.com/startup/postiz",
        "tech": "Next.js, NestJS, Prisma, Stripe",
        "build": [
            "Fork the open source repo and customize branding",
            "Offer white-label version for agencies at $200/mo",
            "Grow via Twitter/X building-in-public posts",
            "Add AI repurposing as premium upsell"
        ],
        "website": "https://postiz.com",
        "founded": "2024-07",
        "country": "HK",
    },
    {
        "id": "prosp",
        "name": "PROSP",
        "rank": 14,
        "mrr": 128005,
        "growth": None,
        "cat": "Marketing",
        "desc": "Automate LinkedIn outreach with AI. Prospecting + personalized message sequences.",
        "problem": "Sales teams spend hours on manual LinkedIn prospecting with low reply rates",
        "audience": "B2B sales teams, founders",
        "team": "Small",
        "open": False,
        "source": "https://trustmrr.com/startup/prosp",
        "tech": "LinkedIn API, AI, Stripe",
        "build": [
            "Build LinkedIn connection + message automation",
            "Use AI to personalize openers from profile data",
            "Offer 7-day free trial, then $99/mo",
            "Distribute via LinkedIn influencers and sales communities"
        ],
        "website": "https://prosp.ai",
        "founded": None,
        "country": None,
    },
    {
        "id": "propgpt",
        "name": "PropGPT",
        "rank": 17,
        "mrr": 95915,
        "growth": 3,
        "cat": "AI",
        "desc": "AI sports betting props analysis app. First AI app dedicated to transforming sports betting strategy.",
        "problem": "Sports bettors lack data-driven tools to evaluate prop bets efficiently",
        "audience": "Sports bettors, fantasy players",
        "team": "Small",
        "open": False,
        "source": "https://trustmrr.com/startup/propgpt-ai-props-analysis",
        "tech": "Mobile (iOS/Android), AI/ML, Stripe/IAP",
        "build": [
            "Aggregate public player stats + injury data",
            "Build AI model to score prop bets by value",
            "Launch as iOS app with $9.99/mo subscription",
            "Market via sports betting subreddits and Twitter"
        ],
        "website": "https://propgpt.ai",
        "founded": None,
        "country": None,
    },
    {
        "id": "vidai",
        "name": "Vid.AI",
        "rank": 18,
        "mrr": 92614,
        "growth": 2,
        "cat": "AI",
        "desc": "Turn any idea or script into ready-to-post videos. AI generates voiceovers, visuals, edits in minutes.",
        "problem": "Creators and marketers need video content at scale without video editing skills",
        "audience": "Content creators, marketers, small businesses",
        "team": "Small",
        "open": False,
        "source": "https://trustmrr.com/startup/vidai-llc",
        "tech": "Python, FFmpeg, AI video models, Stripe",
        "build": [
            "Use ElevenLabs API for voiceovers, DALL-E for visuals",
            "Build simple script → video pipeline",
            "Offer 5 free videos/month, then $29/mo",
            "Grow via TikTok demos showing before/after"
        ],
        "website": "https://vid.ai",
        "founded": None,
        "country": None,
    },
    {
        "id": "codedex",
        "name": "Codédex",
        "rank": 19,
        "mrr": 86557,
        "growth": 2,
        "cat": "Education",
        "desc": "Learn-to-code platform built specifically for Gen Z. Gamified curriculum.",
        "problem": "Traditional coding courses are boring and not designed for how Gen Z learns",
        "audience": "Gen Z learners (16–24)",
        "team": "Small team",
        "open": False,
        "source": "https://trustmrr.com/startup/cod-dex",
        "tech": "React, gamification engine, Stripe",
        "build": [
            "Pick one language track (Python is easiest)",
            "Make it feel like Duolingo: XP, streaks, badges",
            "Charge $9.99/mo after 7 free lessons",
            "Distribute through TikTok/YouTube coding content"
        ],
        "website": "https://codedex.io",
        "founded": None,
        "country": None,
    },
    {
        "id": "upscale",
        "name": "Upscale",
        "rank": 22,
        "mrr": 69249,
        "growth": 29,
        "cat": "SaaS",
        "desc": "CRM and lead generation software. Warm Inboxes founder. 29% MoM growth.",
        "problem": "Small businesses need CRM + outreach tools but can't afford enterprise pricing",
        "audience": "SMBs, agencies",
        "team": "Solo/small",
        "open": False,
        "source": "https://trustmrr.com/startup/upscale-system-llc",
        "tech": "CRM stack, email warmup, Stripe",
        "build": [
            "Build lightweight CRM with built-in email sequences",
            "Add email warmup as a differentiator feature",
            "Price at $49/mo flat — undercut competition hard",
            "Acquire customers via cold email (meta-product)"
        ],
        "website": "https://upscale.systems",
        "founded": None,
        "country": None,
    },
    {
        "id": "speel",
        "name": "Speel",
        "rank": 24,
        "mrr": 65843,
        "growth": 0,
        "cat": "AI",
        "desc": "AI-generated UGC-style videos and images for ads. 0 to $1M ARR in 3 months.",
        "problem": "Brands need authentic-looking UGC ad creatives but real UGC is slow and expensive",
        "audience": "DTC brands, performance marketers",
        "team": "Small",
        "open": False,
        "source": "https://trustmrr.com/startup/speel-co",
        "tech": "AI video generation, Stripe",
        "build": [
            "Use AI video models (Runway, Pika) as backend",
            "Build a prompt → UGC video output UI",
            "Offer 10 free credits, then $99/mo",
            "Sell to Shopify DTC brands via Facebook ad groups"
        ],
        "website": "https://speel.co",
        "founded": None,
        "country": None,
    },
    {
        "id": "indexsy",
        "name": "Indexsy",
        "rank": 25,
        "mrr": 65017,
        "growth": 2,
        "cat": "Marketing",
        "desc": "Build, acquire and scale digital assets. SEO consulting + tool suite.",
        "problem": "Businesses struggle with Google indexing delays that kill SEO momentum",
        "audience": "SEO agencies, content sites",
        "team": "Solo (Jacky Chou)",
        "open": False,
        "source": "https://trustmrr.com/startup/indexsy-consulting-ltd",
        "tech": "Python scripts, SEO APIs, Stripe",
        "build": [
            "Build a Google indexing checker + auto-submit tool",
            "Package as SaaS at $49/mo",
            "Distribute through SEO Twitter and Ahrefs community",
            "Add content site acquisition as premium service"
        ],
        "website": "https://indexsy.com",
        "founded": None,
        "country": None,
    },
    {
        "id": "aeoengine",
        "name": "AEO Engine",
        "rank": 27,
        "mrr": 61426,
        "growth": 17,
        "cat": "Marketing",
        "desc": "Network of AI agents that research, create, optimize, and amplify content across Google, ChatGPT, Perplexity, AI Overviews.",
        "problem": "Brands need visibility across AI search engines, not just traditional Google",
        "audience": "B2B marketers, content teams",
        "team": "Small",
        "open": False,
        "source": "https://trustmrr.com/startup/aeo-engine",
        "tech": "AI agents, content APIs, Stripe",
        "build": [
            "Build AEO audit: where does a brand appear in AI answers",
            "Create content optimization recommendations",
            "Charge $500–2k/mo for managed AEO",
            "Target SaaS companies scared of AI search disruption"
        ],
        "website": "https://aeoengine.com",
        "founded": None,
        "country": None,
    },
    {
        "id": "pixelpainters",
        "name": "PixelPainters",
        "rank": 28,
        "mrr": 60770,
        "growth": 7,
        "cat": "SaaS",
        "desc": "Unlimited graphics for churches, created by Christian designers. Productized design service.",
        "problem": "Small churches can't afford design agencies or full-time designers",
        "audience": "Churches, ministries, religious orgs",
        "team": "Small",
        "open": False,
        "source": "https://trustmrr.com/startup/pixelpainters-com",
        "tech": "Design workflow, Trello/Notion, Stripe",
        "build": [
            "Hire 2–3 freelance designers from your niche",
            "Build a simple request portal (Typeform + Notion)",
            "Price at $299/mo unlimited requests",
            "Find customers in church Facebook groups and pastor forums"
        ],
        "website": "https://pixelpainters.com",
        "founded": None,
        "country": None,
    },
    {
        "id": "backpedal",
        "name": "BackPedal",
        "rank": 31,
        "mrr": 58665,
        "growth": 55,
        "cat": "SaaS",
        "desc": "GPS tracking and 24/7 recovery for bikes/e-bikes. Hardware + recurring subscription. 55% MoM growth.",
        "problem": "Bike theft is rampant and current solutions don't offer active recovery",
        "audience": "Cyclists, e-bike owners",
        "team": "Small",
        "open": False,
        "source": "https://trustmrr.com/startup/backpedal-ltd",
        "tech": "IoT hardware, GPS SIM, mobile app, Stripe",
        "build": [
            "Source GPS tracker hardware (Quectel module ~$15)",
            "Build iOS/Android app for real-time tracking",
            "Charge $99 hardware + $9.99/mo subscription",
            "Partner with bike shops for in-store distribution"
        ],
        "website": "https://backpedal.co",
        "founded": None,
        "country": None,
    },
    {
        "id": "seobot",
        "name": "SEOBOT",
        "rank": 32,
        "mrr": 57777,
        "growth": 10,
        "cat": "Marketing",
        "desc": "AI agent for SEO — keywords, research, blog, mini apps, programmatic SEO and more.",
        "problem": "Founders need SEO content at scale but can't afford agencies or big teams",
        "audience": "SaaS founders, content teams",
        "team": "Solo (John Rush)",
        "open": False,
        "source": "https://trustmrr.com/startup/seobot",
        "tech": "Next.js, AI APIs, Stripe",
        "build": [
            "Build keyword → SEO article AI pipeline",
            "Add programmatic SEO page generator",
            "Price at $99/mo, integrate with any CMS",
            "Distribute through Indiehackers + Twitter building-in-public"
        ],
        "website": "https://seobot.ai",
        "founded": None,
        "country": None,
    },
    {
        "id": "hack2hire",
        "name": "Hack2hire",
        "rank": 39,
        "mrr": 45586,
        "growth": 15,
        "cat": "Education",
        "desc": "Coding and system design practice for technical interview preparation.",
        "problem": "LeetCode is gamified but doesn't teach system design or real interview strategy",
        "audience": "Software engineers preparing for FAANG",
        "team": "Small",
        "open": False,
        "source": "https://trustmrr.com/startup/hack2hire",
        "tech": "React, coding sandbox, Stripe",
        "build": [
            "Build system design question library with diagrams",
            "Add mock interview mode with timer",
            "Charge $29/mo; offer 3 free problems/day",
            "Distribute via r/cscareerquestions and LinkedIn"
        ],
        "website": "https://hack2hire.com",
        "founded": None,
        "country": None,
    },
    {
        "id": "chatdash",
        "name": "ChatDash",
        "rank": 43,
        "mrr": 41086,
        "growth": 8,
        "cat": "SaaS",
        "desc": "White-labeled AI assistant dashboard for agencies. Voiceflow + OpenAI integration. Brandable client portals.",
        "problem": "Agencies reselling AI chatbots need a brandable client-facing dashboard",
        "audience": "AI agencies, chatbot resellers",
        "team": "Solo/small",
        "open": False,
        "source": "https://trustmrr.com/startup/chatdash-llc",
        "tech": "React, Voiceflow API, OpenAI API, Stripe",
        "build": [
            "Build embeddable AI chat widget with white-label branding",
            "Integrate with Voiceflow and OpenAI Assistants API",
            "Charge agencies $200–500/mo per client seat",
            "Sell through agency Facebook groups and Slack communities"
        ],
        "website": "https://chatdash.com",
        "founded": None,
        "country": None,
    },
    {
        "id": "simple-analytics",
        "name": "Simple Analytics",
        "rank": 46,
        "mrr": 39096,
        "growth": 0,
        "cat": "SaaS",
        "desc": "Privacy-first web analytics. Simple, GDPR-compliant alternative to Google Analytics.",
        "problem": "GDPR compliance is painful with Google Analytics; devs need a clean alternative",
        "audience": "Developers, privacy-conscious businesses",
        "team": "Solo/duo",
        "open": False,
        "source": "https://trustmrr.com/startup/simple-analytics",
        "tech": "Lightweight JS, no cookies, Stripe",
        "build": [
            "Build sub-1kb tracking script with no cookies",
            "Show pageviews, referrers, top pages — nothing else",
            "Charge $9/mo, offer open source lite version",
            "Market via GDPR fine news and developer communities"
        ],
        "website": "https://simpleanalytics.com",
        "founded": None,
        "country": None,
    },
    {
        "id": "notionlytics",
        "name": "Notionlytics",
        "rank": 47,
        "mrr": 38729,
        "growth": 8,
        "cat": "Developer Tools",
        "desc": "Detailed analytics for Notion — company wikis, knowledge bases, shared documents.",
        "problem": "Teams share Notion docs but have zero visibility into what people actually read",
        "audience": "Ops teams, community managers, knowledge managers",
        "team": "Solo",
        "open": False,
        "source": "https://trustmrr.com/startup/notionlytics",
        "tech": "Notion API, analytics, Stripe",
        "build": [
            "Use Notion API to track page views + engagement",
            "Build a simple dashboard showing read rates",
            "Offer free tier for 1 workspace, paid at $19/mo",
            "Market in Notion communities and r/Notion"
        ],
        "website": "https://notionlytics.com",
        "founded": None,
        "country": None,
    },
    {
        "id": "launch-club",
        "name": "Launch Club",
        "rank": 48,
        "mrr": 36000,
        "growth": 24,
        "cat": "Marketing",
        "desc": "Reddit marketing for AI search visibility. Tools + content for business owners to promote products.",
        "problem": "Founders don't know how to use Reddit for marketing without getting banned",
        "audience": "SaaS founders, indie hackers",
        "team": "Solo (Ken Savage)",
        "open": False,
        "source": "https://trustmrr.com/startup/launch-club",
        "tech": "Reddit API, community tools, Stripe",
        "build": [
            "Create a course: how to market on Reddit without getting banned",
            "Add a subreddit finder tool as a SaaS feature",
            "Charge $99/mo membership",
            "Grow by posting genuinely helpful Reddit marketing tips on Twitter"
        ],
        "website": "https://launchclub.io",
        "founded": None,
        "country": None,
    },
    {
        "id": "virlo",
        "name": "Virlo",
        "rank": 50,
        "mrr": 35521,
        "growth": 26,
        "cat": "SaaS",
        "desc": "Track, manage, and leverage short-form video data. Analytics for TikTok/Reels/Shorts.",
        "problem": "Creators and brands have no single view of performance across all short-form platforms",
        "audience": "Content creators, brand managers",
        "team": "Small",
        "open": False,
        "source": "https://trustmrr.com/startup/virlo",
        "tech": "Social APIs, analytics, Stripe",
        "build": [
            "Build unified TikTok + Reels + Shorts analytics dashboard",
            "Add competitor tracking as key differentiator",
            "Price at $29/mo; free for 1 channel",
            "Grow by posting short-form analytics insights on TikTok"
        ],
        "website": "https://virlo.ai",
        "founded": "2024-11",
        "country": "US",
    },
]


def format_mrr(v):
    if v >= 1_000_000:
        return f"${v/1_000_000:.1f}M"
    if v >= 1_000:
        return f"${v/1_000:.0f}K"
    return f"${v}"


def create_index_md(s):
    growth_line = ""
    if s["growth"]:
        growth_line = f"- **Growth:** +{s['growth']}% MoM\n"

    website_line = f"**Website:** [{s['website']}]({s['website']})" if s["website"] else "**Website:** —"

    return f"""# {s['name']}

> {s['desc']}

{website_line} | **MRR:** {format_mrr(s['mrr'])} | **Ranked:** #{s['rank']} on TrustMRR | **Source:** [TrustMRR]({s['source']})

---

## Problem

{s['problem']}

## Target Audience

- **Primary:** {s['audience']}
- **Team Size:** {s['team']}

## Tech Stack

{s['tech']}

## Key Metrics

- **MRR:** {format_mrr(s['mrr'])}
- **TrustMRR Rank:** #{s['rank']}
{growth_line}
- **Category:** {s['cat']}
{"- **Open Source:** Yes" if s['open'] else ""}

---

**Attribution:** Revenue data sourced from [TrustMRR](https://trustmrr.com) via Stripe API verification — for educational purposes.

**Disclaimer:** This is for learning and inspiration. Respect intellectual property and trademarks when replicating. We are not affiliated with {s['name']}.
"""


def create_business_model_md(s):
    pricing_note = ""
    if s["id"] == "postiz":
        pricing_note = """
## Pricing Model

Postiz uses a **freemium** model:

| Plan | Price | Details |
|------|-------|---------|
| Free | $0 | Core scheduling features |
| Pro | ~$19/mo | Unlimited posts, AI features |
| Business | ~$49/mo | Team features, priority support |
"""
    elif s["id"] == "simple-analytics":
        pricing_note = """
## Pricing Model

Simple Analytics uses a **flat subscription** model:

| Plan | Price | Details |
|------|-------|---------|
| Starter | $9/mo | Basic analytics |
| Business | $19/mo | Full features |
| Enterprise | Custom | High-volume |
"""
    elif s["id"] == "backpedal":
        pricing_note = """
## Pricing Model

BackPedal uses a **hardware + subscription** model:

| Component | Price | Details |
|-----------|-------|---------|
| GPS Tracker | $99 one-time | Hardware cost |
| Monthly Sub | $9.99/mo | 24/7 monitoring & recovery |
"""
    else:
        pricing_note = f"""
## Revenue

- **MRR:** {format_mrr(s['mrr'])}
- **Category:** {s['cat']}
- **Growth:** {"+" + str(s['growth']) + "% MoM" if s['growth'] else "Steady"}
"""

    return f"""# {s['name']} — Business Model

## Overview

{s['desc']}

## Target Market

{s['audience']}

{pricing_note}

## Growth Strategy

{chr(10).join(f"{i+1}. {step}" for i, step in enumerate(s['build']))}

---

**Attribution:** Data sourced from [TrustMRR](https://trustmrr.com) — for educational purposes.
"""


def create_replication_guide_md(s):
    steps = ""
    for i, step in enumerate(s['build'], 1):
        steps += f"""
### Step {i}: {step}

Details for implementing this step depend on your specific tech stack and market. Focus on delivering value quickly and iterating based on user feedback.
"""

    return f"""# {s['name']} — Replication Guide

> How to build a {s['cat'].lower()} product like {s['name']}

## Overview

This guide covers building a product similar to {s['name']} in the {s['cat']} space.

**Problem to solve:** {s['problem']}

**Target audience:** {s['audience']}

## Tech Stack Reference

{s['tech']}

## Build Steps

{steps}

## Launch Checklist

- [ ] MVP functional with core features
- [ ] Landing page with clear value proposition
- [ ] Payment integration (Stripe)
- [ ] Analytics tracking
- [ ] Initial user outreach
- [ ] Feedback collection system

## Marketing Channels

{chr(10).join(f"- {step}" for step in s['build'][:3])}

## Cost Estimate

| Item | Monthly Cost |
|------|-------------|
| Hosting | $0–$20 |
| Domain | $1 |
| Third-party APIs | $20–$100 |
| Stripe fees | 2.9% + $0.30/txn |
| **Total** | **~$21–$121/mo** |

---

**Attribution:** Build steps sourced from [TrustMRR]({s['source']}) — for educational purposes.

**Disclaimer:** This is for learning and inspiration. Respect intellectual property and trademarks when replicating.
"""


def create_metrics_json(s):
    return {
        "startup": s["name"],
        "slug": s["id"],
        "last_updated": "2026-06-14",
        "source": "TrustMRR",
        "metrics": {
            "mrr": s["mrr"],
            "ranked": s["rank"],
            "growth_mom": s["growth"],
        },
        "category": s["cat"],
        "audience": s["audience"],
        "team_size": s["team"],
        "open_source": s["open"],
        "trustmrr_url": s["source"],
        "website": s.get("website"),
        "founded": s.get("founded"),
        "country": s.get("country"),
        "tech_stack": s["tech"],
    }


def main():
    for s in STARTUPS:
        slug = s["id"]
        dir_path = DATA_DIR / slug
        dir_path.mkdir(parents=True, exist_ok=True)

        (dir_path / "index.md").write_text(create_index_md(s))
        (dir_path / "business-model.md").write_text(create_business_model_md(s))
        (dir_path / "replication-guide.md").write_text(create_replication_guide_md(s))
        (dir_path / "metrics.json").write_text(
            json.dumps(create_metrics_json(s), indent=2) + "\n"
        )

        print(f"Created {slug}/")


if __name__ == "__main__":
    main()
