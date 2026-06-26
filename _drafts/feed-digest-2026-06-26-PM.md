# Digest — 2026-06-26 PM

- Window: last 14h
- Raw items considered: 46
- Relevant: 19
- Skippable: 27

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** CISA Adds Actively Exploited PTC Windchill RCE Flaw to KEV Catalog — `2026-06-26-cisa-kev-ptc-windchill-rce-active-exploitation.md`
- [x] **[CRITICAL]** Miasma Supply-Chain Malware Expands to npm, GitHub Actions, and Go — `2026-06-26-miasma-malware-npm-github-actions-supply-chain.md`
- [x] **[HIGH]** Polymarket Customers Lose $3 Million in Frontend Supply-Chain Attack — `2026-06-26-polymarket-supply-chain-attack-3-million.md`
- [x] **[HIGH]** Chinese-Speaking APT Deploys New TinyRCT Backdoor in Southeast Asia — `2026-06-26-chinese-apt-tinyrct-backdoor-southeast-asia.md`
- [x] **[HIGH]** New Linux 'pedit COW' Exploit Enables Root Access via Cached Binary Poisoning — `2026-06-26-linux-pedit-cow-exploit-root-access.md`
- [x] **[HIGH]** Amazon Q Developer Flaw Allowed Credential Theft via Malicious MCP Configs — `2026-06-26-amazon-q-developer-mcp-credential-theft.md`
- [x] **[HIGH]** New 'DirtyClone' Linux Kernel Flaw Lets Local Users Gain Root — `2026-06-26-dirtyclone-linux-kernel-root-privilege-escalation.md`
- [x] **[HIGH]** Google Attributes New STOCKSTAY Backdoor to Russian APT Turla — `2026-06-26-turla-stockstay-backdoor-ukraine-espionage.md`
- [x] **[MEDIUM]** OpenAI Limits GPT-5.6 Rollout After US Government Request — `2026-06-26-openai-limits-gpt-5-6-rollout-government-request.md`
- [x] **[MEDIUM]** Fraudulent OpenAI Organization Invites Target Cybersecurity Firms — `2026-06-26-fraudulent-openai-org-invites-target-cybersecurity-firms.md`
- [x] **[MEDIUM]** Anthropic's Mythos Models Remain Offline Amid Trump Administration Standoff — `2026-06-26-anthropic-mythos-offline-trump-administration-standoff.md`
- [x] **[MEDIUM]** CISA and FBI Warn of Ongoing Russian Phishing Campaigns Against Messaging App Users — `2026-06-26-cisa-fbi-russian-phishing-messaging-apps.md`
- [x] **[MEDIUM]** OpenAI Previews GPT-5.6 Sol, Its Next-Generation Flagship Model — `2026-06-26-openai-previews-gpt-5-6-sol.md`
- [x] **[MEDIUM]** Microsoft Warns of Photo-Themed ZIP Phishing Campaign Targeting Hotels — `2026-06-26-microsoft-photo-zip-phishing-hotels-nodejs-implant.md`
- [x] **[MEDIUM]** Russia Used Cellebrite Forensic Tools on Activist's iPhone After Sales Cutoff — `2026-06-26-russia-cellebrite-activist-iphone-citizen-lab.md`
- [x] **[MEDIUM]** New Enterprise MCP Specification Shifts Security Responsibilities to Developers — `2026-06-26-mcp-specification-security-challenges.md`
- [x] **[INFORMATIONAL]** 2,000 People Tried to Hack an AI Email Assistant — None Succeeded — `2026-06-26-ai-assistant-prompt-injection-challenge-results.md`
- [x] **[INFORMATIONAL]** Google Cloud Expands VPC Service Controls for Agentic AI Workloads — `2026-06-26-google-cloud-vpc-service-controls-agentic-ai.md`
- [x] **[INFORMATIONAL]** Linux Foundation Launches Akrites Open Source Security Project — `2026-06-26-linux-foundation-akrites-open-source-security-project.md`

## Relevant (details)

### 1. 2,000 People Tried to Hack an AI Email Assistant — None Succeeded
- **Source:** Simon Willison — https://simonwillison.net/2026/Jun/26/hack-my-ai-assistant/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `llm`, `ai-safety`, `prompt-injection`
- **Slug:** `ai-assistant-prompt-injection-challenge-results`
- **Must-know:** no
- **Summary:** A public challenge invited ~2,000 people to email an OpenClaw test instance and try to leak its secrets; across ~6,000 attempts, nobody succeeded. The underlying model (Claude Opus 4.6) ran with explicit anti-prompt-injection system instructions.

### 2. OpenAI Limits GPT-5.6 Rollout After US Government Request
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/26/openai-limits-gpt-5-6-rollout-after-government-request-says-restrictions-shouldnt-be-the-norm/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `openai`, `llm`, `ai-regulation`, `model-release`
- **Slug:** `openai-limits-gpt-5-6-rollout-government-request`
- **Must-know:** no
- **Summary:** OpenAI limited GPT-5.6's rollout after a US government request and previewed the models to officials ahead of launch. OpenAI said it doesn't want this kind of access process to become the long-term default.

### 3. Polymarket Customers Lose $3 Million in Frontend Supply-Chain Attack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/polymarket-customers-lose-3-million-in-supply-chain-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `appsec`
- **Slug:** `polymarket-supply-chain-attack-3-million`
- **Must-know:** no
- **Summary:** Hackers stole an estimated $3 million from Polymarket customers by injecting a malicious script into the platform's frontend, reached via a breach at a third-party vendor. Polymarket will fully reimburse affected customers.

### 4. Google Cloud Expands VPC Service Controls for Agentic AI Workloads
- **Source:** Google Cloud Security — https://cloud.google.com/blog/products/identity-security/securing-agentic-ai-whats-new-in-vpc-service-controls/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `cloud-security`, `gcp`, `iam`
- **Slug:** `google-cloud-vpc-service-controls-agentic-ai`
- **Must-know:** no
- **Summary:** Google Cloud announced new VPC Service Controls capabilities designed specifically for agentic AI workloads, extending network-level perimeter controls as enterprises scale autonomous agents into production.

### 5. Fraudulent OpenAI Organization Invites Target Cybersecurity Firms
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cybersecurity-firms-targeted-by-fraudulent-openai-organization-invites/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `openai`, `llm`
- **Slug:** `fraudulent-openai-org-invites-target-cybersecurity-firms`
- **Must-know:** no
- **Summary:** Threat actors are creating fake OpenAI tenants impersonating legitimate companies and inviting employees at cybersecurity firms to join, aiming to trick targets into submitting sensitive data through chats and projects.

### 6. Chinese-Speaking APT Deploys New TinyRCT Backdoor in Southeast Asia
- **Source:** The Hacker News — https://thehackernews.com/2026/06/chinese-speaking-apt-deploys-new.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `apt`
- **Slug:** `chinese-apt-tinyrct-backdoor-southeast-asia`
- **Must-know:** no
- **Summary:** A Chinese-speaking APT tracked as CL-STA-1062 is using a new backdoor, TinyRCT, against government entities and critical infrastructure in Southeast Asia, particularly state-owned energy and government targets.

### 7. Anthropic's Mythos Models Remain Offline Amid Trump Administration Standoff
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/957327/anthropic-mythos-fable-ai-trump-administration-negotiations
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `anthropic`, `ai-regulation`, `llm`
- **Slug:** `anthropic-mythos-offline-trump-administration-standoff`
- **Must-know:** no
- **Summary:** Two weeks after taking Mythos-class models offline following a Trump administration ultimatum, Anthropic has sent executives to Washington but has not commented publicly, with no resolution in sight.

### 8. New Linux 'pedit COW' Exploit Enables Root Access via Cached Binary Poisoning
- **Source:** The Hacker News — https://thehackernews.com/2026/06/new-linux-pedit-cow-exploit-enables.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Slug:** `linux-pedit-cow-exploit-root-access`
- **Must-know:** no
- **Summary:** CVE-2026-46331 ("pedit COW") is an out-of-bounds write in the Linux kernel's act_pedit traffic-control action that lets a local unprivileged user gain root. A working public exploit appeared within a day of CVE assignment.

### 9. Amazon Q Developer Flaw Allowed Credential Theft via Malicious MCP Configs
- **Source:** The Hacker News — https://thehackernews.com/2026/06/amazon-q-developer-flaw-could-let.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `aws`, `llm`
- **Slug:** `amazon-q-developer-mcp-credential-theft`
- **Must-know:** no
- **Summary:** CVE-2026-12957 (CVSS 8.5) in Amazon Q Developer allowed a malicious repository to run commands and steal cloud credentials via crafted MCP server configs. AWS has patched the issue.

### 10. CISA Adds Actively Exploited PTC Windchill RCE Flaw to KEV Catalog
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cisa-adds-exploited-ptc-windchill-rce.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `cisa-kev-ptc-windchill-rce-active-exploitation`
- **Must-know:** yes
- **Summary:** CISA added a critical RCE flaw (CVE-2026-12569) in PTC Windchill PDMLink/FlexPLM to its KEV catalog, citing active exploitation; web shell attacks against vulnerable instances are reported to be continuing.

### 11. CISA and FBI Warn of Ongoing Russian Phishing Campaigns Against Messaging App Users
- **Source:** CISA Alerts — https://www.cisa.gov/resources-tools/resources/russian-intelligence-services-continue-target-commercial-messaging-applications
- **Section:** Government / Advisory
- **Severity:** medium
- **Tags:** `phishing`
- **Slug:** `cisa-fbi-russian-phishing-messaging-apps`
- **Must-know:** no
- **Summary:** CISA and the FBI updated a PSA on Russian Intelligence Services phishing campaigns targeting commercial messaging app users, adding recent tactics, mitigations, and phishing message samples.

### 12. New 'DirtyClone' Linux Kernel Flaw Lets Local Users Gain Root
- **Source:** The Hacker News — https://thehackernews.com/2026/06/new-dirtyclone-linux-kernel-flaw-lets.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Slug:** `dirtyclone-linux-kernel-root-privilege-escalation`
- **Must-know:** no
- **Summary:** CVE-2026-43503 ("DirtyClone", CVSS 8.8) is a Linux kernel privilege escalation in the DirtyFrag family that lets a local user corrupt file-backed memory via a cloned network packet and gain root. JFrog published a working exploit walkthrough.

### 13. Linux Foundation Launches Akrites Open Source Security Project
- **Source:** SecurityWeek — https://www.securityweek.com/linux-foundation-unveils-new-open-source-security-project-akrites/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `devsecops`, `vulnerability`
- **Slug:** `linux-foundation-akrites-open-source-security-project`
- **Must-know:** no
- **Summary:** The Linux Foundation launched Akrites, a new project providing tools and channels to report, patch, and disclose open source software vulnerabilities.

### 14. Miasma Supply-Chain Malware Expands to npm, GitHub Actions, and Go
- **Source:** The Hacker News — https://thehackernews.com/2026/06/miasma-malware-targets-npm-packages-and.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `github`, `malware`
- **Slug:** `miasma-malware-npm-github-actions-supply-chain`
- **Must-know:** yes
- **Summary:** Miasma, the latest evolution of the Mini Shai-Hulud/Hades supply-chain attack lineage, has compromised new npm packages (LeoPlatform, RStreams), abused GitHub Actions workflows, and propagated to the Go ecosystem.

### 15. OpenAI Previews GPT-5.6 Sol, Its Next-Generation Flagship Model
- **Source:** OpenAI Blog — https://openai.com/index/previewing-gpt-5-6-sol
- **Section:** AI — Labs & Model Launches
- **Severity:** medium
- **Tags:** `ai-launch`, `model-release`, `llm`, `openai`
- **Slug:** `openai-previews-gpt-5-6-sol`
- **Must-know:** no
- **Summary:** OpenAI previewed GPT-5.6 Sol, Terra, and Luna, with gains in coding, science, and cybersecurity capability plus a new safety stack. Rollout is limited following coordination with the US government.

### 16. Microsoft Warns of Photo-Themed ZIP Phishing Campaign Targeting Hotels
- **Source:** The Hacker News — https://thehackernews.com/2026/06/microsoft-warns-of-photo-zip-phishing.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `malware`, `microsoft`
- **Slug:** `microsoft-photo-zip-phishing-hotels-nodejs-implant`
- **Must-know:** no
- **Summary:** An active phishing campaign since April 2026 targets hospitality organizations in Europe and Asia with photo-themed ZIP lures that drop a Node.js implant on front-desk machines. Attribution is unknown.

### 17. Russia Used Cellebrite Forensic Tools on Activist's iPhone After Sales Cutoff
- **Source:** The Hacker News — https://thehackernews.com/2026/06/russia-used-cellebrite-on-jailed.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `privacy`, `surveillance`
- **Slug:** `russia-cellebrite-activist-iphone-citizen-lab`
- **Must-know:** no
- **Summary:** Citizen Lab found Russian authorities used Cellebrite's UFED to break into a detained activist's iPhone in 2021, three months after Cellebrite said it cut off sales to Russia and Belarus.

### 18. New Enterprise MCP Specification Shifts Security Responsibilities to Developers
- **Source:** SecurityWeek — https://www.securityweek.com/new-enterprise-ready-mcp-specification-brings-new-security-challenges/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `llm`, `appsec`, `mcp`
- **Slug:** `mcp-specification-security-challenges`
- **Must-know:** no
- **Summary:** A major overhaul of the Model Context Protocol specification moves several security responsibilities from the protocol itself onto developers and platform operators building and deploying MCP servers.

### 19. Google Attributes New STOCKSTAY Backdoor to Russian APT Turla
- **Source:** The Hacker News (citing Google) — https://thehackernews.com/2026/06/google-details-turlas-new-stockstay.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `apt`
- **Slug:** `turla-stockstay-backdoor-ukraine-espionage`
- **Must-know:** no
- **Summary:** Google's Threat Intelligence Group attributed a new .NET backdoor, STOCKSTAY, to Russian APT Turla, deployed against Ukrainian government/military targets and entities tied to Italian foreign policy.

## Skippable

- **OpenAI poaches Uber India chief to lead its biggest market outside the U.S.** — TechCrunch AI. Business/hiring news, no security angle.
- **Incident Report: CVE-2026-LGTM** — Simon Willison. Explicitly a hypothetical/satirical incident report, not real news.
- **Why everyone from OpenAI to SpaceX is building their own chips** — TechCrunch AI. Hardware/business story, no security angle.
- **Cisco Adds NHI to Security Stack With Astrix, WideField Acquisitions** — Dark Reading. M&A announcement without technical substance.
- **Quoting OpenAI** — Simon Willison. Duplicate coverage of the GPT-5.6 launch already covered via OpenAI's own blog post.
- **OpenAI unveils GPT-5.6 amid US AI regulatory drama** — The Verge AI. Duplicate coverage of stories already covered separately.
- **It's not about Anthropic vs. OpenAI anymore** — TechCrunch AI. Opinion piece without concrete news.
- **AI Won't Wipe-Out Entry-Level Cybersecurity Jobs** — Dark Reading. Opinion/career piece.
- **Amazon Q Flaw Enabled Cloud Credential Theft via Malicious Repositories** — SecurityWeek. Duplicate of more detailed Hacker News coverage with the CVE.
- **More Klue Breach Victims Identified as Hackers Get Hacked** — SecurityWeek. Generic breach disclosure without technical substance.
- **In Other News: Chinese Mythos-Like AI, Tata Electronics Breach, Snyk Layoffs** — SecurityWeek. Low-signal roundup of items already covered or too thin individually.
- **Your First GRC Agent: A Red Teamer's Walkthrough** — BleepingComputer. Vendor tutorial/marketing content.
- **OpenAI's Jalapeño chip is Big Tech's spiciest move away from Nvidia** — TechCrunch AI. Duplicate hardware/business story.
- **Russia accuses Apple of 'political censorship' after VK apps removed from App Store** — The Record. Policy/business story, no technical security content.
- **Meeting Trump's 2030 Quantum Deadline Will be Expensive, Complex** — Dark Reading. Generic strategy piece without concrete technical content.
- **Turla group adds more malware to Russia's espionage efforts against Ukraine** — The Record. Duplicate of more detailed Google/Hacker News coverage of the same STOCKSTAY backdoor.
- **Russia used social engineering to breach prominent messaging accounts, Ukraine says** — The Record. Generic breach disclosure without IOCs/TTPs; overlaps with the CISA advisory.
- **Thanks for Crushing the Submissions Inbox. We're Trying to Keep Up** — Dark Reading. Admin/meta post, no news value.
- **The Good, the Bad and the Ugly in Cybersecurity – Week 26** — SentinelOne Labs. Weekly roundup with no single item carrying enough new detail.
- **Early Bird pricing ends tonight for TechCrunch Founder Summit** — TechCrunch AI. Event marketing.
- **Nebulock Raises $25 Million for AI-Native Contextual Security** — SecurityWeek. Startup funding announcement, marketing content.
- **FCC votes to toughen rules in bid to better protect undersea cables** — The Record. Telecom policy with limited direct relevance to AI/security practitioners.
- **Guardian Agents: The Next Layer of Identity Governance** — The Hacker News. Vendor guide content, not news.
- **$3 Million Reportedly Stolen in Polymarket Hack** — SecurityWeek. Duplicate of more detailed BleepingComputer coverage.
- **Russian APT Deploys 'StockStay' Backdoor Against Ukrainian Targets** — SecurityWeek. Duplicate of more detailed Google/Hacker News coverage.
- **First-Ever Exploitation of PTC Windchill Vulnerability Discovered in the Wild** — SecurityWeek. Duplicate of more detailed KEV/web-shell coverage.
- **Philip Martin Joins Uber as Chief Information Security Officer** — SecurityWeek. Recruitment/career news.
