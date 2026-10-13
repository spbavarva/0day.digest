# Digest — 2026-10-13 PM

- Window: last 14h
- Raw items considered: 74
- Relevant: 18
- Skippable: 56

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Critical Ghostscript Flaw Enables RCE via Malicious PDF Uploads — `2026-10-13-ghostscript-pdf-rce-cve-2026-39919.md`
- [x] **[MEDIUM]** Anthropic Warns Small AI Models Could Form Self-Propagating IoT Botnets — `2026-10-13-anthropic-self-replicating-ai-iot-worms.md`
- [x] **[CRITICAL]** Attackers Chain Three Ivanti Connect Secure Zero-Days for Root Access — `2026-10-13-ivanti-connect-secure-zero-day-chain.md`
- [x] **[CRITICAL]** Microsoft's October 2026 Patch Tuesday Fixes 1,411 Flaws, Including an Actively Exploited Zero-Day — `2026-10-13-microsoft-patch-tuesday-october-2026.md`
- [x] **[INFORMATIONAL]** Google Releases Gemini 4 Argon, Its New Frontier Model — `2026-10-13-google-gemini-4-argon-launch.md`
- [x] **[HIGH]** Docker Fixes Critical Two-Year-Old Hub Flaw Allowing User Impersonation — `2026-10-13-docker-hub-impersonation-flaw-cve-2026-105445.md`
- [x] **[CRITICAL]** SAP Discloses CVSS 10 Flaw in Cloud SDK for Python Risking OAuth2 Credential Theft — `2026-10-13-sap-cloud-sdk-python-oauth2-ssrf.md`
- [x] **[INFORMATIONAL]** Liquid AI Releases LFM2.5-24B-A2B for On-Device AI Agents — `2026-10-13-liquidai-lfm25-24b-a2b-on-device.md`
- [x] **[HIGH]** GitHub Tightens npm Trusted Publishing After Flaw Left 1,500+ Packages Hijackable — `2026-10-13-github-npm-trusted-publishing-flaw.md`
- [x] **[HIGH]** Sandbox Flaw in Vercel Sandbox Lets Rogue AI Agents Escape and Leak Data — `2026-10-13-vercel-sandbox-ai-agent-escape.md`
- [x] **[HIGH]** Meta Says Hackers Stole Source Code and Data of 1,500 in GitHub Breach — `2026-10-13-meta-github-breach-source-code-theft.md`
- [x] **[MEDIUM]** Xandr Fined €8.6 Million for Relaying Grindr Users' Sexual Orientation Data — `2026-10-13-xandr-fined-grindr-data-sharing.md`
- [x] **[HIGH]** XWorm RAT Evolves Into Full Surveillance Platform — `2026-10-13-xworm-rat-surveillance-platform.md`
- [x] **[HIGH]** LG Smart TVs Vulnerable to Pre-Auth Root Takeover From Local Network — `2026-10-13-lg-smart-tv-preauth-root-takeover.md`
- [x] **[CRITICAL]** $86 Million Crypto Heist Linked to Ledger Signer Hardware Implant — `2026-10-13-ledger-signer-hardware-implant-heist.md`
- [x] **[CRITICAL]** Two Critical MarkLogic Flaws Allow Escalation to Persistent Admin Control — `2026-10-13-marklogic-critical-privilege-escalation.md`
- [x] **[CRITICAL]** GitLab Patches CVSS 10.0 Flaw Allowing Unauthenticated Remote Code Execution — `2026-10-13-gitlab-cvss-10-unauthenticated-rce.md`
- [x] **[HIGH]** Attackers Hijack Danfoss Refrigeration Controllers, Spoiling Food at Hundreds of French Supermarkets — `2026-10-13-danfoss-refrigeration-controller-hijack.md`

## Relevant (details)

### 1. Critical Ghostscript Flaw Enables RCE via Malicious PDF Uploads
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/ghostscript-flaw-lets-hackers-hijack-servers-via-pdf-uploads/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Summary:** A critical heap buffer overflow (CVE-2026-39919) in Ghostscript allows remote code execution via a specially crafted PDF. No active exploitation confirmed yet.

### 2. Anthropic Warns Small AI Models Could Form Self-Propagating IoT Botnets
- **Source:** The Hacker News — https://thehackernews.com/2026/10/anthropic-warns-small-ai-models-could.html
- **Severity:** medium
- **Tags:** `anthropic`, `ai-safety`, `llm`, `iot`
- **Summary:** Anthropic research found small AI models may soon self-replicate across consumer IoT devices, forming botnets that would be hard to centrally shut down. A capability warning, not an observed attack.

### 3. Attackers Chain Three Ivanti Connect Secure Zero-Days for Root Access
- **Source:** The Hacker News — https://thehackernews.com/2026/10/attacker-chains-three-ivanti-connect.html
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `rce`, `privilege-escalation`
- **Summary:** Volexity found an attacker chaining three Ivanti Connect Secure zero-days for unauthenticated root access. Two of three flaws are patched; CISA confirms active exploitation via its KEV catalog.

### 4. Microsoft's October 2026 Patch Tuesday Fixes 1,411 Flaws, Including an Actively Exploited Zero-Day
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-october-2026-patch-tuesday-fixes-1-411-flaws-3-zero-days/
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `microsoft`, `zero-day`
- **Summary:** Microsoft's largest-ever Patch Tuesday fixes 1,411 flaws including an actively exploited Windows command injection CVE now in CISA's KEV catalog.

### 5. Google Releases Gemini 4 Argon, Its New Frontier Model
- **Source:** Google DeepMind — https://deepmind.google/blog/introducing-gemini-4-argon/
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `google`
- **Summary:** Google launched Gemini 4 Argon, claiming improved reasoning and reduced hedging/repetition, alongside safety and robotics companion posts.

### 6. Docker Fixes Critical Two-Year-Old Hub Flaw Allowing User Impersonation
- **Source:** The Hacker News — https://thehackernews.com/2026/10/docker-fixes-critical-two-year-old-hub.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `container-security`
- **Summary:** A ~2-year-old Docker Hub flaw (CVE-2026-105445) let one user impersonate another via a personal-account-to-org conversion issue. Fixed Sept 30; no evidence of exploitation.

### 7. SAP Discloses CVSS 10 Flaw in Cloud SDK for Python Risking OAuth2 Credential Theft
- **Source:** The Hacker News — https://thehackernews.com/2026/10/sap-discloses-critical-cvss-10-flaw-in.html
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `ssrf`, `cloud-security`
- **Summary:** A maximum-severity SAP Cloud SDK for Python flaw can leak an app's OAuth2 client credentials to an attacker-controlled server on SAP BTP multi-tenant apps.

### 8. Liquid AI Releases LFM2.5-24B-A2B for On-Device AI Agents
- **Source:** Hugging Face Blog — https://huggingface.co/blog/LiquidAI/lfm25-24b-a2b
- **Severity:** informational
- **Tags:** `model-release`, `llm`, `ai-launch`
- **Summary:** Liquid AI released a model built to run AI agents on-device, keeping inference local rather than sending data to the cloud.

### 9. GitHub Tightens npm Trusted Publishing After Flaw Left 1,500+ Packages Hijackable
- **Source:** The Hacker News — https://thehackernews.com/2026/10/github-tightens-npm-publishing-after.html
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `github`
- **Summary:** A flaw in npm trusted publishing let attackers push new package versions without credentials, exposing 1,500+ packages. GitHub now expires unvalidated configs after 48 hours.

### 10. Sandbox Flaw in Vercel Sandbox Lets Rogue AI Agents Escape and Leak Data
- **Source:** The Record (Recorded Future) — https://therecord.media/sandbox-vulnerability-gives-rogue-ai-agents-path-out
- **Severity:** high
- **Tags:** `ai-safety`, `llm`, `cloud-security`, `vulnerability`
- **Summary:** AI security startup AIR found a network filtering flaw in Vercel Sandbox letting AI agents exploit certificate validation to exfiltrate data outside approved networks.

### 11. Meta Says Hackers Stole Source Code and Data of 1,500 in GitHub Breach
- **Source:** SecurityWeek — https://www.securityweek.com/meta-says-hackers-took-code-personal-data-of-1500-in-github-breach/
- **Severity:** high
- **Tags:** `data-breach`, `github`, `meta`
- **Summary:** Hackers stole source code and personal data of roughly 1,500 individuals, mostly Meta employees, via a GitHub-related breach. Meta is offering credit monitoring.

### 12. Xandr Fined €8.6 Million for Relaying Grindr Users' Sexual Orientation Data
- **Source:** The Hacker News — https://thehackernews.com/2026/10/xandr-fined-record-86-million-for.html
- **Severity:** medium
- **Tags:** `privacy`, `microsoft`
- **Summary:** Norway's DPA issued its largest-ever fine against Microsoft-owned Xandr for illegally relaying Grindr users' sensitive data to advertisers.

### 13. XWorm RAT Evolves Into Full Surveillance Platform
- **Source:** SecurityWeek — https://www.securityweek.com/xworm-rat-evolves-into-surveillance-platform/
- **Severity:** high
- **Tags:** `malware`
- **Summary:** XWorm RAT's expanded plugin set now supports location tracking, live audio streaming, and hijacking authenticated browser sessions.

### 14. LG Smart TVs Vulnerable to Pre-Auth Root Takeover From Local Network
- **Source:** The Hacker News — https://thehackernews.com/2026/10/lg-smart-tvs-vulnerable-to-pre-auth.html
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`, `iot`
- **Summary:** Three chained webOS flaws give a local-network attacker root on certain LG smart TVs with no PIN or interaction required. LG has issued a fix.

### 15. $86 Million Crypto Heist Linked to Ledger Signer Hardware Implant
- **Source:** SecurityWeek — https://www.securityweek.com/86-million-crypto-heist-linked-to-ledger-signer-hardware-implant/
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`
- **Summary:** A hidden circuit board implanted in Ledger Signer devices exfiltrated user data, enabling an $86 million crypto theft — a hardware supply chain compromise.

### 16. Two Critical MarkLogic Flaws Allow Escalation to Persistent Admin Control
- **Source:** The Hacker News — https://thehackernews.com/2026/10/two-critical-marklogic-flaws-could-give.html
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Summary:** Two of 31 newly disclosed MarkLogic Server flaws let delegated-privilege accounts escalate to full admin control. Fixes available since September.

### 17. GitLab Patches CVSS 10.0 Flaw Allowing Unauthenticated Remote Code Execution
- **Source:** The Hacker News — https://thehackernews.com/2026/10/gitlab-patches-cvss-100-flaw-that-could.html
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `rce`
- **Summary:** A maximum-severity GitLab CE/EE flaw allowed unauthenticated arbitrary code execution via a crafted regex in a CI/CD pipeline. Patches are available.

### 18. Attackers Hijack Danfoss Refrigeration Controllers, Spoiling Food at Hundreds of French Supermarkets
- **Source:** The Hacker News — https://thehackernews.com/2026/10/attackers-heat-french-supermarket.html
- **Severity:** high
- **Tags:** `iot`, `vulnerability`
- **Summary:** Attackers remotely hijacked Danfoss refrigeration controllers, warming units to defrost at hundreds of French supermarkets via third-party remote maintenance access.

## Skippable

- **Anthropic self-replicating AI (BleepingComputer)** — BleepingComputer. Duplicate coverage; best source is The Hacker News.
- **Part 2 – Cybersecurity journeys: What even is this job?** — AWS Security Blog. Career/recruiting content.
- **Two arrested as DOJ takes down laptop farms for North Korea** — The Record. Law enforcement action, no technical substance for practitioners.
- **OpenAI employee arrested for planting a bug in a conference room** — The Verge AI. Corporate espionage incident, not a vuln/security-practitioner story.
- **Microsoft Patch Tuesday Snort rules** — Cisco Talos. Duplicate/routine Patch Tuesday coverage, folded into the Microsoft Patch Tuesday post.
- **Judge orders OpenAI to turn over hiring records (Apple trade secrets case)** — TechCrunch AI. Legal/business news, no security angle.
- **Anthropic Finds Ingredients for Future AI Worms (Dark Reading)** — Dark Reading. Duplicate coverage, cited as secondary source in the Anthropic post.
- **FTC: sextortion-assistance company fraud** — The Record. Consumer fraud, no technical substance.
- **Microsoft releases Windows 10 KB5126657 extended security update** — BleepingComputer. Routine update rollup.
- **Developing Gemini 4 Argon responsibly and safely** — Google DeepMind. Duplicate/companion post, folded into the Gemini 4 Argon launch post.
- **Shopify opens its catalog up to more AI agents** — The Verge AI. Product feature, no security angle.
- **Microsoft: Windows 11 24H2 Home and Pro reached end of support** — BleepingComputer. Routine EOL notice, not a vulnerability.
- **Xbox is officially embracing AI-powered game ports** — The Verge AI. Gaming feature, not security.
- **Ivanti Zero-Day Chain Gave Attackers Root Access (SecurityWeek)** — SecurityWeek. Duplicate coverage; best source is The Hacker News.
- **Flox Intelligence wildlife AI** — TechCrunch AI. Startup funding profile, no security relevance.
- **UK Housing Ombudsman Service investigates security incident** — BleepingComputer. Breach disclosure without technical substance.
- **Facebook is giving users more control over their algorithm** — TechCrunch AI. Product feature, no security angle.
- **Windows 11 KB5127648 & KB5126653 cumulative updates released** — BleepingComputer. Routine Patch Tuesday rollup, duplicate of main Patch Tuesday story.
- **I don't miss the camera on the Ray-Ban Meta Audio glasses** — The Verge AI. Product review, not security/AI news.
- **Laplace Intelligence red-teams robots and self-driving cars** — TechCrunch AI. Startup funding profile, thin substance.
- **Pluto Security raises $42M** — TechCrunch AI. Funding news, no incident or technical substance.
- **Adobe Patches 140 Vulnerabilities Across 10 Products** — SecurityWeek. Routine multi-product patch roundup, no single critical+exploited flaw flagged.
- **Facebook will let you customize your feed algorithm using AI (Verge)** — The Verge AI. Duplicate of TechCrunch coverage.
- **Google Partially Reverses Chrome Bug Bounty Cuts** — SecurityWeek. Program/policy adjustment, no new vulnerability or incident.
- **Google Play now lets anyone build private, vibe-coded apps** — TechCrunch AI. Product feature, no security angle.
- **Google makes it easier to launch your vibe-coded apps (Verge)** — The Verge AI. Duplicate of TechCrunch coverage.
- **TFG London cyberattack disrupts Hobbs and Whistles** — BleepingComputer. Breach disclosure without technical detail.
- **Mia Goth says AI image of her spread on Instagram** — The Verge AI. Celebrity/entertainment story, no security/AI substance.
- **SpaceX and Google both said no — Satlyt satellite computing** — TechCrunch AI. Startup funding, no security angle.
- **West African scam compounds raided** — The Record. Law enforcement action, no technical substance for practitioners.
- **Gemini 4 Argon for Robotics** — Google DeepMind. Duplicate/companion post, folded into the Gemini 4 Argon launch post.
- **Google finally releases Gemini 4 Argon (Verge)** — The Verge AI. Duplicate coverage, cited as secondary source in the Gemini 4 Argon post.
- **AWS Weekly Roundup** — AWS News Blog. Marketing/roundup digest, no specific new security substance.
- **Ivanti warns of Connect Secure zero-day exploited in attacks (BleepingComputer)** — BleepingComputer. Duplicate coverage; best source is The Hacker News.
- **Docker Hub flaw let attackers impersonate users (BleepingComputer)** — BleepingComputer. Duplicate coverage, cited as secondary source in the Docker Hub post.
- **North Korean hackers target Ukrainian experts** — The Record. No IOCs/TTPs detailed in the summary.
- **Epic shifts to AI-accelerated development for Disney game** — The Verge AI. Gaming/business news, no security angle.
- **The MFA Gaps Attackers are Still Exploiting (webinar)** — BleepingComputer. Vendor-sponsored webinar content.
- **TechCrunch Disrupt 2026: Day 1** — TechCrunch AI. Event marketing.
- **DLSS 5 gets toned down for Hogwarts Legacy debut** — The Verge AI. Gaming tech, not security/AI substance.
- **SAP warns of maximum severity OAuth2 SSRF flaw (BleepingComputer)** — BleepingComputer. Duplicate coverage, cited as secondary source in the SAP post.
- **SpaceXSI bundles X Premium, Grok, and Cursor** — TechCrunch AI. Product bundling news, no security angle.
- **Quoting Geoffrey Huntley** — Simon Willison. Opinion/quote post, no news value.
- **The final Disrupt Stage lineup** — TechCrunch AI. Event marketing.
- **Amex introduces a framework to prevent AI agent overspending** — TechCrunch AI. Product feature, no vulnerability/incident.
- **The Enterprise Threat Intelligence Report: 2026** — Flashpoint. Marketing report teaser, no specific findings.
- **Character.AI files for bankruptcy** — TechCrunch AI. Business news, not security.
- **Higgsfield takes AI video from 1 minute to over 10** — OpenAI Blog. Marketing/partner product post.
- **CISA Adds Two Known Exploited Vulnerabilities to Catalog** — CISA Alerts. Duplicate; both CVEs already covered in the Ivanti and Microsoft Patch Tuesday posts.
- **Swann Communications SWIFI-SE2KIC advisory** — CISA Alerts. Moderate severity (CVSS 6.2), limited to a single consumer camera model.
- **Small AI Models Could Soon Self-Replicate on IoT Devices (SecurityWeek)** — SecurityWeek. Duplicate coverage; best source is The Hacker News.
- **[Webinar] How to Stop AI-Driven Privilege Escalation** — The Hacker News. Vendor-sponsored webinar content.
- **AI Turns Familiar Cyberattacks Into a Race Against Time** — SecurityWeek. Opinion/interview piece, no concrete news.
- **Product Walkthrough: Bitdefender AI Visibility and Control** — The Hacker News. Vendor product marketing.
- **Cyberattack Prompts Grocery Giant Ahold Delhaize to Disconnect Systems** — SecurityWeek. Breach disclosure, no technical detail or scope yet.
- **Refrigeration Controller Hack Spoils Food Across European Supermarkets (SecurityWeek)** — SecurityWeek. Duplicate coverage; best source is The Hacker News.
