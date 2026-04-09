# RSS Sources — AI & Security Signal

These are the sources the fetcher checks during each digest run.

---

## Cybersecurity — Primary

- The Hacker News — https://feeds.feedburner.com/TheHackersNews
- BleepingComputer — https://www.bleepingcomputer.com/feed/
- Krebs on Security — https://krebsonsecurity.com/feed/
- Dark Reading — https://www.darkreading.com/rss.xml
- The Record (Recorded Future) — https://therecord.media/feed
- SecurityWeek — https://feeds.feedburner.com/securityweek

## Cybersecurity — Research & Threat Intel

- SentinelOne Labs — https://www.sentinelone.com/feed/
- Cisco Talos — https://blog.talosintelligence.com/rss/
- Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/feed/
- Flashpoint — https://flashpoint.io/feed/
- PortSwigger Research — https://portswigger.net/research/rss
- Trail of Bits — https://blog.trailofbits.com/feed/
- Google Project Zero — https://projectzero.google/feed.xml
- Securelist (Kaspersky GReAT) — https://securelist.com/feed/

## AI — Labs & Model Launches

- OpenAI Blog — https://openai.com/blog/rss.xml
- Google DeepMind — https://deepmind.google/blog/rss.xml
- Google AI Blog — https://blog.google/technology/ai/rss/
- Hugging Face Blog — https://huggingface.co/blog/feed.xml

> **No RSS available:** Anthropic, Meta AI, DeepSeek, Zhipu/GLM, Alibaba Qwen.
> These are covered via Twitter/X feeds below and TechCrunch AI.

## AI — News & Analysis

- TechCrunch AI — https://techcrunch.com/category/artificial-intelligence/feed/
- Simon Willison — https://simonwillison.net/atom/everything/
- Lilian Weng (OpenAI) — https://lilianweng.github.io/index.xml
- The Verge AI — https://www.theverge.com/rss/ai-artificial-intelligence/index.xml

## Twitter / X (manual — automation blocked)

X/Twitter blocks all public RSS bridges (RSSHub, Nitter). These accounts are
worth checking manually until a self-hosted solution is set up. To automate
later: self-host RSSHub with Twitter API keys, or use a paid service like
RSS.app.

### AI Labs (no RSS feed — Twitter is the primary channel)

- @AnthropicAI — Anthropic launches, Claude updates, safety research
- @OpenAI — covered by blog RSS, but Twitter has faster announcements
- @GoogleDeepMind — covered by blog RSS
- @huggingface — covered by blog RSS
- @deepseek_ai — DeepSeek model releases (no blog RSS exists)
- @Alibaba_Qwen — Qwen model releases (no blog RSS exists)

### Security Researchers

- @_JohnHammond — exploit demos, CTF content
- @SwiftOnSecurity — infosec commentary, Windows security
- @GossiTheDog — threat intel, enterprise security
- @taviso — Google Project Zero researcher
- @ProjectDiscovery — nuclei, security tooling
- @PortSwigger — web security research

## Cloud Security & Infrastructure

- AWS Security Blog — https://aws.amazon.com/blogs/security/feed/
- AWS News Blog — https://aws.amazon.com/blogs/aws/feed/
- Google Cloud Security — https://cloudblog.withgoogle.com/products/identity-security/rss/

> **No RSS available:** Wiz, Datadog, Upwind, Orca, Sysdig, Aqua Security,
> Azure/MSRC. Most cloud security vendors don't publish RSS feeds.
> Their news typically surfaces via the Primary cybersec feeds above.

## Government / Advisory

- CISA Alerts — https://www.cisa.gov/cybersecurity-advisories/all.xml

---

## Removed (confirmed dead / 404)

These were in the original list but no longer resolve:

- ~~Anthropic Blog~~ — `https://www.anthropic.com/blog/rss` → 404 (no RSS feed exists)
- ~~Meta AI Blog~~ — `https://ai.meta.com/blog/rss/` → 404
- ~~Google Threat Intelligence (Mandiant)~~ — `https://cloud.google.com/feeds/google-threat-intelligence-blog.xml` → redirect chain → 404
- ~~Ars Technica Security~~ — `https://feeds.arstechnica.com/arstechnica/security` → 403 blocked
- ~~Cybersecurity Dive~~ — removed (too enterprise/marketing, low signal)

---

## What's Relevant vs Skippable

### RELEVANT — include in digest

**Security (technical focus):**
- Novel attack techniques, exploitation primitives, kill chains
- Critical/high CVEs, especially under active exploitation
- Supply chain compromises (npm, PyPI, GitHub Actions, container images)
- Zero-days with technical detail
- Offensive/defensive tool releases with real utility
- Major breaches ONLY if technically interesting or > 100k users
- Source code leaks, credential exposures

**Cloud (AWS, GCP, Azure):**
- New cloud service launches with security implications
- IAM misconfigurations, privilege escalation, cross-account attacks
- Container/Kubernetes security findings
- Cloud-native security tool releases (Wiz, Datadog, Upwind, Orca findings)
- Cloud provider security incidents or outages
- CSPM/CNAPP/CWPP tool capabilities that matter to practitioners

**AI (launches & substance):**
- New model releases from any lab (Anthropic, OpenAI, Google, Meta, Chinese labs)
- Significant model updates, benchmarks, capability jumps
- AI safety incidents, jailbreaks, prompt injection research
- AI + security intersection (LLM vulns, AI-assisted attacks, AI in defense)
- Developer tool launches (agents, APIs, frameworks)
- Regulatory actions with real impact on AI deployment

### SKIPPABLE — list in digest but don't draft a post

- Generic breach disclosures without technical substance ("X company got hacked")
- Regional/local incidents (city government ransomware, single-org phishing)
- Individual phishing kits without novel technique
- Ransomware victim disclosures without TTPs or IOCs
- "FBI/CISA warns" advisories without new IOCs or technical guidance
- Generic enterprise IT (cloud migration, cost optimization)
- Marketing content disguised as news
- Opinion pieces without news value
- Recruitment or career content
- Duplicate coverage (pick the best source, skip the rest)
- Routine patch Tuesday unless a single CVE is critical + exploited
