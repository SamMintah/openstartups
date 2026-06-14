# Rezi — Replication Guide

> How to build an AI-powered resume builder with ATS optimization

## Overview

Rezi is an AI-powered resume builder that helps job seekers create ATS-optimized resumes. It serves ~1M new users per year with a B2C freemium model and an enterprise tier serving 300+ organizations (universities, career centers, staffing agencies). The core insight: most resumes are rejected by Applicant Tracking Systems before a human ever sees them. Rezi reverse-engineers what ATS bots want and generates resumes that pass.

**Key Metrics:**
- MRR: $270K
- TrustMRR Rank: #4
- Growth: +8% MoM
- Team: Small team
- Users: ~1M new/year

## Market Opportunity

**Niche:** AI-assisted job seeker tools — specifically resume writing and optimization.

**Why it's underserved:** Resume writing is a $500M+ market but dominated by (1) expensive human writers ($200-500 per resume), (2) generic templates that don't account for ATS filtering, and (3) free tools with no intelligence. The gap is an affordable, intelligent tool that understands both ATS algorithms and hiring manager psychology.

**Competitive Landscape:**
- **Flowcv, Novoresume** — template-based, no AI optimization
- **Kickresume, Enhancv** — some AI features but weaker ATS focus
- **Jobscan** — ATS matching analysis, not a full builder
- **ChatGPT** — general purpose, no structured resume output
- **Rezi** — purpose-built ATS optimizer with enterprise sales

**Why now:** AI costs have dropped 10x in 2 years. GPT-4 class models can parse job descriptions and generate targeted content. Remote work has expanded the job market globally, increasing resume volume.

## MVP Build Guide

### Core Features (must-have for v1)

1. **ATS Resume Parser & Scorer**
   - Parse uploaded resume (PDF/DOCX) into structured data
   - Score resume against common ATS keywords and formatting rules
   - Output: score (0-100) + specific improvement suggestions

2. **AI Resume Generator**
   - User inputs job description URL or pasted text
   - AI generates tailored resume content for each section
   - Enforce ATS-friendly formatting (no tables, graphics, columns)

3. **Export & Download**
   - Export as PDF (primary) and DOCX (secondary)
   - Maintain ATS-friendly formatting in output

### Tech Stack

| Layer | Tool | Cost | Why |
|-------|------|------|-----|
| Frontend | Next.js + React | Free | Fast, SEO-friendly, huge ecosystem |
| AI/LLM | OpenAI GPT-4o API | ~$0.005/resume | Best reasoning for content generation |
| PDF Parsing | pdf-parse (npm) | Free | Extract text from uploaded resumes |
| DOCX Parsing | mammoth (npm) | Free | Parse Word documents |
| PDF Generation | Puppeteer or @react-pdf/renderer | Free | Generate clean PDFs |
| Database | PostgreSQL (Supabase) | Free tier | User data, resume versions |
| Auth | NextAuth.js | Free | Google/email sign-in |
| Payments | Stripe | 2.9% + $0.30/txn | Industry standard |
| Hosting | Vercel | Free tier | Deploys from git |
| File Storage | Supabase Storage | Free tier | Resume file uploads |

**Total estimated MVP cost: $50–100/month** (mostly API calls)

### No-Code Alternative

**Faster path (2-4 weeks):**
- Frontend: Carrd or Framer (landing page) + Tally (form)
- AI: OpenAI GPT API directly from frontend
- Payments: Stripe Payment Links
- No database initially — email results to user

**Limitations:** No user accounts, no resume saving/history, no enterprise features. Migrate to code when you hit ~100 paying users.

### Build Time & Cost

- **With code (Next.js):** 4-6 weeks for solo dev, 2-3 weeks for small team
- **No-code path:** 1-2 weeks
- **Budget:** $0 if using free tiers, $50-100/mo at launch

## Pricing Strategy

**Rezi's model (reconstructed):**

| Plan | Price | What you get |
|------|-------|-------------|
| Free | $0 | 1 resume, basic AI, watermarked PDF |
| Pro | ~$15-20/mo | Unlimited resumes, full AI, clean exports |
| Lifetime | ~$49-79 one-time | All Pro features, forever |
| Enterprise | $500-2000/yr | Bulk licenses, admin dashboard, SSO |

**Pricing psychology:**
- Free tier is the funnel — users who create one resume convert at 10-15% to paid
- Lifetime deal creates urgency and early cash flow
- Enterprise is where the real money is (300 orgs × $1K avg = $300K ARR)

**How to position:**
- vs. human writers: "AI resume in 5 minutes for $15, not $300 for 3 days"
- vs. templates: "AI that understands your job description, not generic filler"
- vs. ChatGPT: "Purpose-built for resumes, not a chatbot you have to prompt correctly"

## Customer Acquisition

### Primary Channels

1. **SEO — "AI resume builder" keywords**
   - Target: "ai resume builder", "ats resume builder", "resume builder free"
   - Create comparison pages: "Rezi vs [competitor]"
   - Cost: $0 (organic), takes 3-6 months

2. **Product Hunt Launch**
   - Prepare launch assets 2 weeks early
   - Build an email list of 200+ supporters before launch
   - Target top 5 daily product
   - Expected: 1,000-5,000 signups on launch day

3. **University Partnerships**
   - Cold email career centers at 50 universities
   - Offer free bulk licenses for students (costs you ~$0)
   - Students become paying users after graduation
   - This is Rezi's enterprise moat

4. **Reddit & r/jobs, r/resumes**
   - Post genuine value: "I analyzed 500 resumes that got interviews — here's what they had in common"
   - Link to free tool at the end
   - Reddit is the #1 traffic source for resume tools

### Content/SEO Strategy

- **Blog topics:** "How to beat ATS in 2026", "Resume keywords for [industry]", "Resume vs CV: what's the difference"
- **Programmatic pages:** "/resume-template-[industry]" for 100+ industries
- **YouTube:** "Watch me optimize a resume in 60 seconds" — short-form demo content

### Early Traction Tactics

- **First 10 users:** Post on r/resumes offering free resume reviews, link to your tool
- **First 100 users:** Product Hunt launch + cold email 50 university career centers
- **First 1,000 users:** SEO kicks in + university partnerships + referral program

## Growth Levers

- **Referral program:** "Give a friend 1 month Pro, get 1 month free" — resume seekers are in networks of other job seekers
- **University pipeline:** Students use free → graduate → become paying → employer pays for enterprise
- **Template marketplace:** Let designers create and sell resume templates (you take 20%)
- **Job description matching:** Premium feature that scores resume against a specific job posting

## Unit Economics (estimates)

- **ARPU:** $15/mo (Blended: free + pro + enterprise)
- **Estimated CAC:** $5-10 (SEO/content is primary channel)
- **Payback period:** <1 month
- **LTV:** $90-180 (6-12 month retention × $15/mo)
- **LTV:CAC ratio:** 9:1 to 18:1 (excellent)

## Common Pitfalls

1. **Over-engineering the ATS parser.** ATS systems are proprietary and change constantly. Don't try to reverse-engineer all of them — focus on the top 5 (Workday, Greenhouse, Lever, iCIMS, Taleo) and general formatting rules.

2. **Ignoring the enterprise sales cycle.** University and enterprise deals take 3-6 months. Start the conversation early, offer free pilots. Don't build enterprise features until you have 3+ committed prospects.

3. **Competing on features with Canva/Google Docs.** Your edge is intelligence, not design. Stay focused on AI-powered content, not drag-and-drop editors.

4. **Neglecting mobile.** 40%+ of job seekers use mobile. Your resume builder must work on phones, not just desktop.

## Tools & Resources

- **Resume parsing:** pdf-parse, mammoth, textract
- **AI content:** OpenAI GPT-4o, Anthropic Claude
- **PDF generation:** Puppeteer, @react-pdf/renderer, jsPDF
- **ATS research:** Jobscan (analyze ATS compatibility), Resume Worded (scoring)
- **SEO:** Ahrefs or Ubersuggest for keyword research
- **Communities:** r/resumes, r/jobs, Indie Hackers, r/cscareerquestions

## Launch Checklist

### Pre-Launch (Week 1-2)
- [ ] Build MVP with core features (parser + AI generator + export)
- [ ] Create landing page with clear value proposition
- [ ] Set up Stripe payments and auth
- [ ] Test ATS compatibility of generated resumes (use Jobscan)
- [ ] Prepare Product Hunt assets (screenshots, video, copy)
- [ ] Build email list of 200+ supporters

### Launch (Week 3)
- [ ] Launch on Product Hunt
- [ ] Post on r/resumes, r/jobs, Indie Hackers
- [ ] Send launch email to list
- [ ] Monitor for bugs and user feedback

### Post-Launch (Week 4+)
- [ ] Fix top 5 user-reported issues
- [ ] Start SEO content production (2 posts/week)
- [ ] Begin university outreach (50 cold emails)
- [ ] Set up referral program
- [ ] Analyze conversion funnel and optimize

---

**Attribution:** Build guide for educational purposes. Data sourced from [TrustMRR](https://trustmrr.com/startup/rezi).

**Disclaimer:** This is for learning and inspiration. Respect intellectual property and trademarks when replicating.
