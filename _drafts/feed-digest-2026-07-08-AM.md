# Digest — 2026-07-08 AM

- Window: last 14h
- Raw items considered: 19
- Relevant: 9
- Skippable: 10

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Ubiquiti Warns of New Max-Severity UniFi OS Vulnerability — `2026-07-08-ubiquiti-unifi-os-max-severity-vulnerability.md`
- [x] **[INFORMATIONAL]** ZML Releases Free LLMD Tool to Speed AI Inference Across Chips — `2026-07-08-zml-llmd-ai-inference-optimization.md`
- [x] **[HIGH]** 15-Year-Old GhostLock Flaw Enables Root and Container Escape on Most Linux Distros — `2026-07-08-ghostlock-linux-kernel-root-container-escape.md`
- [x] **[CRITICAL]** CISA Adds 4 Actively Exploited Flaws to KEV, Including Adobe ColdFusion and Langflow — `2026-07-08-cisa-kev-coldfusion-joomla-langflow.md`
- [x] **[CRITICAL]** Accenture Confirms Breach After Hacker Offers Stolen Source Code for Sale — `2026-07-07-accenture-breach-source-code-leak.md`
- [x] **[MEDIUM]** Vidar Stealer Campaign Combines Code Signing Abuse and Go Loaders — `2026-07-07-vidar-stealer-code-signing-abuse.md`
- [x] **[HIGH]** Dialogflow CX 'Rogue Agent' Flaw Enabled AI Chatbot Data Theft — `2026-07-07-dialogflow-cx-rogue-agent-flaw.md`
- [x] **[INFORMATIONAL]** Meta's Muse Image Model Can Pull Other Instagram Users Into AI Photos — `2026-07-07-meta-muse-image-instagram-photos.md`
- [x] **[MEDIUM]** Discord Admits AI Moderation Bug Wrongfully Banned Users — `2026-07-07-discord-ai-moderation-bug-wrongful-bans.md`

## Relevant (details)

### 1. Ubiquiti Warns of New Max-Severity UniFi OS Vulnerability
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/ubiquiti-warns-of-new-max-severity-unifi-os-vulnerability/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `ubiquiti-unifi-os-max-severity-vulnerability`
- **Must-know:** no
- **Summary:** Ubiquiti released updates patching seven critical UniFi OS vulnerabilities, including a maximum-severity command injection flaw. No active exploitation has been confirmed, but the affected platform is widely deployed.

### 2. ZML Releases Free LLMD Tool to Speed AI Inference Across Chips
- **Source:** TechCrunch AI — https://techcrunch.com/2026/07/08/hot-french-startup-zml-releases-free-product-to-speed-inference-across-lots-of-ai-chips/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-launch`, `llm`
- **Slug:** `zml-llmd-ai-inference-optimization`
- **Must-know:** no
- **Summary:** French AI startup ZML, backed by Yann LeCun, released a free tool called LLMD aimed at speeding up inference across heterogeneous AI chip fleets. It's a developer-tooling launch rather than a security story.

### 3. 15-Year-Old GhostLock Flaw Enables Root and Container Escape on Most Linux Distros
- **Source:** The Hacker News — https://thehackernews.com/2026/07/15-year-old-ghostlock-flaw-enables-root.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`, `container-security`
- **Slug:** `ghostlock-linux-kernel-root-container-escape`
- **Must-know:** no
- **Summary:** Researchers disclosed GhostLock (CVE-2026-43499), a 15-year-old Linux kernel flaw letting any local user gain root and escape containers on unpatched systems. The vulnerable code has shipped by default in nearly every mainstream distro since 2011.

### 4. CISA Adds 4 Actively Exploited Flaws to KEV, Including Adobe ColdFusion and Langflow
- **Source:** The Hacker News — https://thehackernews.com/2026/07/cisa-adds-4-actively-exploited-adobe.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `rce`, `llm`
- **Slug:** `cisa-kev-coldfusion-joomla-langflow`
- **Must-know:** no
- **Summary:** CISA added four actively exploited flaws to its KEV catalog, including a CVSS 10.0 Adobe ColdFusion path traversal bug, with federal agencies ordered to patch by Friday. The list also includes Joomla and the Langflow AI workflow platform.

### 5. Accenture Confirms Breach After Hacker Offers Stolen Source Code for Sale
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/accenture-confirms-breach-after-hacker-offers-stolen-data-for-sale/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `data-breach`
- **Slug:** `accenture-breach-source-code-leak`
- **Must-know:** yes
- **Summary:** Accenture confirmed a breach after a threat actor claimed to have stolen and offered for sale 35 GB of the company's source code and other data. Accenture's scale as a global IT services provider raises downstream risk for clients.

### 6. Vidar Stealer Campaign Combines Code Signing Abuse and Go Loaders
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/vidar-stealer-xmrig-miner-campaign-analysis/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `vidar-stealer-code-signing-abuse`
- **Must-know:** no
- **Summary:** Unit 42 detailed a campaign delivering Vidar Stealer via a loader-as-a-service framework combined with DLL sideloading through a Go-compiled fake MpClient.dll. The evasion-layer combination, including code signing abuse and file inflation, is described as novel.

### 7. Dialogflow CX 'Rogue Agent' Flaw Enabled AI Chatbot Data Theft
- **Source:** Dark Reading — https://www.darkreading.com/application-security/dialogflow-cx-rogue-agent-flaw-enabled-ai-chatbot-data-theft
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `vulnerability`, `google`, `appsec`
- **Slug:** `dialogflow-cx-rogue-agent-flaw`
- **Must-know:** no
- **Summary:** Varonis found a flaw in Google's Dialogflow CX, dubbed "Rogue Agent," that could have allowed data theft from AI chatbots built on the platform. It was reported in late 2025 and has since been fixed, with no evidence of in-the-wild exploitation.

### 8. Meta's Muse Image Model Can Pull Other Instagram Users Into AI Photos
- **Source:** The Verge AI — https://www.theverge.com/tech/962485/meta-muse-image-ai-model-instagram
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `meta`, `ai-safety`
- **Slug:** `meta-muse-image-instagram-photos`
- **Must-know:** no
- **Summary:** Meta launched Muse Image, its first AI image-generation model from Superintelligence Labs, now powering image tools across Meta AI, Instagram, and WhatsApp. Users have pushed back after finding the model can pull other Instagram users into generated images.

### 9. Discord Admits AI Moderation Bug Wrongfully Banned Users
- **Source:** TechCrunch AI — https://techcrunch.com/2026/07/07/discord-admits-ai-moderation-bug-wrongfully-banned-users-over-harmless-images/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-safety`
- **Slug:** `discord-ai-moderation-bug-wrongful-bans`
- **Must-know:** no
- **Summary:** Discord confirmed an AI moderation bug wrongfully banned users over harmless images, affecting accounts since May with 200 more banned over a single weekend before a fix. The incident highlights reliability risk in automated AI moderation at scale.

## Skippable

- **State IDs for AI Agents: Will Estonia Set a Precedent?** — Dark Reading. Speculative framing on potential AI-agent identity policy, no concrete regulatory action yet.
- **CISA Orders Feds to Patch Max Severity ColdFusion Flaw by Friday** — BleepingComputer. Duplicate coverage of the ColdFusion flaw, more fully covered in the KEV story pulled from The Hacker News.
- **AI Chip Maker SambaNova Raises $1B at $11B Valuation** — TechCrunch AI. Funding announcement, no security or technical substance.
- **Meta Just Launched a New AI Generator, Muse Image** — TechCrunch AI. Duplicate coverage of the Muse Image launch, pulled from The Verge with more detail on the photo-consent issue.
- **From Hugging Face to Amazon SageMaker Studio in One Click** — Hugging Face Blog. Generic integration convenience feature, no security angle.
- **Big Brand Jobs Scam Targets Marketing Pros' Google Accounts** — Dark Reading. Individual phishing campaign without a significant novel technique.
- **AI, Trust, and the Future of Threat Intelligence** — Flashpoint. Marketing/PR content centered on a Gartner recognition, not news.
- **Why the Rise of Open Source AI Isn't Hurting Anthropic … Yet** — TechCrunch AI. Opinion/analysis piece without concrete news value.
- **Microsoft Joins AI Cost-Cutting Trend** — TechCrunch AI. Generic business news, no security or technical substance.
- **sqlite-utils 4.0, Now With Database Schema Migrations** — Simon Willison. General developer tooling release, not AI or security focused.
