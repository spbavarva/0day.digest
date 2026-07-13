# Digest — 2026-07-13 AM

- Window: last 14h
- Raw items considered: 14
- Relevant: 6
- Skippable: 8

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** iCagenda and Balbooa Forms Joomla Flaws Exploited as Zero-Days — `2026-07-13-icagenda-balbooa-joomla-zero-days-kev.md`
- [x] **[HIGH]** Zimbra Patches Critical Code Execution Vulnerability — `2026-07-13-zimbra-critical-code-execution-vulnerability.md`
- [x] **[HIGH]** Progress Prompts ShareFile Storage Zone Controller Shutdown Amid Security Concerns — `2026-07-13-progress-sharefile-storage-zone-controller-shutdown.md`
- [x] **[HIGH]** Centers Laboratory Data Breach Affects 540,000 Individuals — `2026-07-13-centers-laboratory-data-breach-540000.md`
- [x] **[MEDIUM]** Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365 — `2026-07-13-evilginx-phishing-operations-exposed-misconfigured-server.md`
- [x] **[INFORMATIONAL]** EU Targets Russian Intelligence Officers Accused of Running a Yearslong Cyber Spying Campaign — `2026-07-13-eu-sanctions-russian-intelligence-cyber-espionage.md`

## Relevant (details)

### 1. iCagenda and Balbooa Forms Joomla Flaws Reportedly Exploited as Zero-Days
- **Source:** The Hacker News — https://thehackernews.com/2026/07/icagenda-and-balbooa-forms-joomla-flaws.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `zero-day`, `cve`, `vulnerability`
- **Slug:** `icagenda-balbooa-joomla-zero-days-kev`
- **Must-know:** yes
- **Summary:** CISA added two maximum-severity (CVSS 10.0) flaws in the iCagenda and Balbooa Forms Joomla extensions to its Known Exploited Vulnerabilities catalog following reports of in-the-wild zero-day exploitation. One tracked flaw is CVE-2026-48939.

### 2. Zimbra Patches Critical Code Execution Vulnerability
- **Source:** SecurityWeek — https://www.securityweek.com/zimbra-patches-critical-code-execution-vulnerability/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `zimbra-critical-code-execution-vulnerability`
- **Must-know:** no
- **Summary:** Zimbra patched a flaw that allows malicious code embedded in crafted emails to execute when the email is opened. No confirmation of active exploitation in the wild.

### 3. Progress Prompts ShareFile Storage Zone Controller Shutdown Amid Security Concerns
- **Source:** SecurityWeek — https://www.securityweek.com/progress-prompts-sharefile-storage-zone-controller-shutdown-amid-security-concerns/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`
- **Slug:** `progress-sharefile-storage-zone-controller-shutdown`
- **Must-know:** no
- **Summary:** Progress Software told ShareFile Storage Zone Controller customers to manually shut down their servers while it investigates a "credible threat." No breach has been confirmed yet, but Progress's history with MOVEit makes this one to watch.

### 4. Centers Laboratory Data Breach Affects 540,000 Individuals
- **Source:** SecurityWeek — https://www.securityweek.com/centers-laboratory-data-breach-affects-540000-individuals/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `centers-laboratory-data-breach-540000`
- **Must-know:** no
- **Summary:** The WorldLeaks extortion group claims to have stolen 720 GB of data from healthcare testing provider Centers Laboratory, affecting roughly 540,000 individuals.

### 5. Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365
- **Source:** The Hacker News — https://thehackernews.com/2026/07/misconfigured-server-reveals-three.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `malware`
- **Slug:** `evilginx-phishing-operations-exposed-misconfigured-server`
- **Must-know:** no
- **Summary:** French security firm Lexfo found a live Microsoft 365 Evilginx phishing operation exposed via a misconfigured Python HTTP server with directory listing enabled, and used the operator's own bash_history to pivot into two additional related operations.

### 6. EU Targets Russian Intelligence Officers Accused of Running a Yearslong Cyber Spying Campaign
- **Source:** SecurityWeek — https://www.securityweek.com/eu-targets-russian-intelligence-officers-accused-of-running-a-yearslong-cyber-spying-campaign/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `sanctions`, `critical-infrastructure`
- **Slug:** `eu-sanctions-russian-intelligence-cyber-espionage`
- **Must-know:** no
- **Summary:** The EU sanctioned individuals and entities linked to a Russian cyber espionage network accused of targeting governments and carrying out sabotage operations against critical infrastructure.

## Skippable

- **US and allies warn of Russian critical infrastructure attacks** — BleepingComputer. Multi-agency advisory about routers being targeted; no new IOCs or technical detail beyond the general warning.
- **Organizations Warned of Exploited Joomla Extension Vulnerabilities** — SecurityWeek. Duplicate coverage of the iCagenda/Balbooa Joomla zero-days; The Hacker News version has more technical detail (CVE ID, CVSS score, KEV listing).
- **Waze is getting a bunch of new AI-powered features** — The Verge AI. Consumer feature announcement (Gemini integration for trip personalization), no security angle.
- **OpenAI temporarily relaxes GPT-5.6 Sol usage limits** — BleepingComputer. Operational capacity update, not a model launch or capability change.
- **Directly Responsible Individuals (DRI)** — Simon Willison. Opinion piece on org design and AI agents, no news value.
- **shot-scraper 1.11** — Simon Willison. Minor dev tool release, no security implications.
- **Fable gets another bump** — Simon Willison. Anthropic extended an existing Claude Fable 5 access deadline; thin on new substance.
- **sqlite-utils 4.1.1** — Simon Willison. Minor library release fixing a transaction edge case; not security- or AI-relevant enough for a post.
