# Digest — 2026-05-04 PM

- Window: last 14h
- Raw items considered: 38
- Relevant: 15
- Skippable: 23

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Backdoored PyTorch Lightning Package on PyPI Delivers Credential Stealer — `2026-05-04-pytorch-lightning-pypi-backdoor.md`
- [x] **[CRITICAL]** 'Copy Fail' Linux Flaw Hits CISA KEV as Active Exploitation Begins — `2026-05-04-copy-fail-linux-cve-exploited.md`
- [x] **[CRITICAL]** cPanel Zero-Day CVE-2026-41940 Exploited Across 40,000+ Servers — `2026-05-04-cpanel-cve-2026-41940-mass-exploitation.md`
- [x] **[HIGH]** Progress Patches Critical Authentication Bypass in MOVEit Automation — `2026-05-04-moveit-automation-auth-bypass-patch.md`
- [x] **[HIGH]** Trellix Discloses Data Breach After Source Code Repository Hack — `2026-05-04-trellix-source-code-repo-breach.md`
- [x] **[HIGH]** DigiCert Support Portal Hacked via Malware; Certificates Revoked — `2026-05-04-digicert-support-portal-breach.md`
- [x] **[HIGH]** VENOMOUS#HELPER: Phishing Campaign Abuses RMM Tools to Persist in 80+ Organizations — `2026-05-04-venomous-helper-rmm-phishing.md`
- [x] **[HIGH]** Silver Fox APT Deploys New ABCDoor Backdoor via Tax-Themed Phishing — `2026-05-04-silver-fox-abcdoor-tax-phishing.md`
- [x] **[HIGH]** Instructure Canvas LMS Discloses Breach Exposing Student Data Amid Leak Threats — `2026-05-04-instructure-canvas-data-breach.md`
- [x] **[MEDIUM]** Attackers Weaponize Amazon SES to Send Phishing Emails That Pass Security Filters — `2026-05-04-amazon-ses-phishing-bec-bypass.md`
- [x] **[MEDIUM]** 2026 Emerges as a Pivotal Year for AI-Assisted Cyberattacks — `2026-05-04-ai-assisted-attacks-2026-trend.md`
- [x] **[MEDIUM]** Global Operation Arrests 276, Seizes $701M in Crypto Investment Fraud Crackdown — `2026-05-04-global-crypto-scam-crackdown-276-arrests.md`
- [x] **[MEDIUM]** Microsoft April 2026 Updates Break Third-Party Backup Apps via Driver Block — `2026-05-04-microsoft-april-2026-update-backup-failures.md`
- [x] **[INFORMATIONAL]** Anthropic and OpenAI Both Launch Enterprise AI Joint Ventures with Asset Managers — `2026-05-04-anthropic-openai-enterprise-ai-joint-ventures.md`
- [x] **[INFORMATIONAL]** OpenAI Launches Advanced Account Security for ChatGPT Users — `2026-05-04-openai-chatgpt-advanced-account-security.md`

## Relevant (details)

### 1. Backdoored PyTorch Lightning Package on PyPI Delivers Credential Stealer
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/backdoored-pytorch-lightning-package-drops-credential-stealer/
- **Severity:** critical
- **Tags:** `supply-chain`, `pypi`, `malware`, `infostealer`
- **Summary:** A malicious PyTorch Lightning version on PyPI drops a credential-stealer targeting browser credentials, `.env` files, and cloud services. ML teams should audit their dependency tree and rotate all exposed credentials immediately — this is an active supply chain compromise of a widely-used ML package.

### 2. 'Copy Fail' Linux Flaw Hits CISA KEV as Active Exploitation Begins
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-says-copy-fail-flaw-now-exploited-to-root-linux-systems/
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`, `zero-day`
- **Summary:** CISA confirmed active exploitation of the "Copy Fail" Linux privilege escalation flaw and added it to KEV, one day after a public PoC dropped. Microsoft also observed limited exploitation. Patch Linux workloads immediately; PoC availability makes mass exploitation imminent.

### 3. cPanel Zero-Day CVE-2026-41940 Exploited Across 40,000+ Servers
- **Source:** SecurityWeek — https://www.securityweek.com/over-40000-servers-compromised-in-ongoing-cpanel-exploitation/
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `vulnerability`, `rce`
- **Summary:** CVE-2026-41940 (recently patched cPanel zero-day) has compromised 40,000+ servers in mass exploitation alongside targeted campaigns against government, military, and MSP targets. Patch cPanel immediately and audit for web shells and unauthorized admin accounts.

### 4. Progress Patches Critical Authentication Bypass in MOVEit Automation
- **Source:** The Hacker News — https://thehackernews.com/2026/05/progress-patches-critical-moveit.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`
- **Summary:** Progress patched a critical auth bypass in MOVEit Automation. No confirmed active exploitation yet, but MOVEit's 2023 mass-exploitation history makes this a priority patch for all organizations running it.

### 5. Trellix Discloses Data Breach After Source Code Repository Hack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/trellix-discloses-data-breach-after-source-code-repository-hack/
- **Severity:** high
- **Tags:** `data-breach`, `supply-chain`
- **Summary:** Attackers accessed a portion of Trellix's source code repository. No confirmed distribution pipeline impact, but investigation is ongoing. Customers should monitor Trellix advisories and verify software update integrity.

### 6. DigiCert Support Portal Hacked via Malware; Certificates Revoked
- **Source:** SecurityWeek — https://www.securityweek.com/digicert-revokes-certificates-after-support-portal-hack/
- **Severity:** high
- **Tags:** `malware`, `data-breach`, `pki`
- **Summary:** Malware delivered via DigiCert's customer chat channel infected a support analyst and enabled portal access. Customer certificates were subsequently revoked. DigiCert customers should verify revocation status and reissue as needed.

### 7. VENOMOUS#HELPER: Phishing Campaign Abuses RMM Tools to Persist in 80+ Organizations
- **Source:** The Hacker News — https://thehackernews.com/2026/05/phishing-campaign-hits-80-orgs-using.html
- **Severity:** high
- **Tags:** `phishing`, `malware`, `rmm`
- **Summary:** Since April 2025, VENOMOUS#HELPER has phished 80+ U.S. organizations and deployed SimpleHelp/ScreenConnect RMM tools for persistent access. Legitimate RMM usage evades detection; audit for unexpected RMM deployments and enforce application allowlisting.

### 8. Silver Fox APT Deploys New ABCDoor Backdoor via Tax-Themed Phishing
- **Source:** The Hacker News — https://thehackernews.com/2026/05/silver-fox-deploys-abcdoor-malware-via.html
- **Severity:** high
- **Tags:** `phishing`, `malware`, `apt`
- **Summary:** China-based Silver Fox sent 1,600+ tax-authority-impersonating phishing messages to targets in India and Russia, deploying the new ABCDoor backdoor plus ValleyRAT. Both waves ran near-identical playbooks, indicating a templated APT operation.

### 9. Instructure Canvas LMS Discloses Breach Exposing Student Data Amid Leak Threats
- **Source:** SecurityWeek — https://www.securityweek.com/edtech-firm-instructure-discloses-data-breach/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** Instructure confirmed hackers stole names, emails, student IDs, and messages from Canvas LMS at multiple institutions. Threat actors are threatening to leak the data. Affected institutions should issue breach notifications and monitor for follow-on phishing.

### 10. Attackers Weaponize Amazon SES to Send Phishing Emails That Pass Security Filters
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/amazon-ses-phishing-and-bec-attacks/119623/
- **Severity:** medium
- **Tags:** `phishing`, `aws`, `cloud-security`
- **Summary:** Kaspersky GReAT documented phishing and BEC campaigns abusing Amazon SES's established sender reputation to pass authentication filters. Teams should add behavioral email analysis beyond SPF/DKIM/DMARC checks to counter this technique.

### 11. Anthropic and OpenAI Both Launch Enterprise AI Joint Ventures with Asset Managers
- **Source:** TechCrunch AI — https://techcrunch.com/2026/05/04/anthropic-and-openai-are-both-launching-joint-ventures-for-enterprise-ai-services/
- **Severity:** informational
- **Tags:** `anthropic`, `openai`, `ai-launch`
- **Summary:** Both Anthropic and OpenAI announced separate joint ventures with asset managers for enterprise AI sales. Organizations evaluating AI vendors should track how these structures affect pricing, data governance, and long-term contractual terms.

### 12. 2026 Emerges as a Pivotal Year for AI-Assisted Cyberattacks
- **Source:** The Hacker News — https://thehackernews.com/2026/05/2026-year-of-ai-assisted-attacks.html
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`, `malware`
- **Summary:** THN analysis of AI-assisted attack trends: low-sophistication actors are using AI tools for malware generation, phishing, and large-scale data extraction, lowering the skill floor for attacks. Security teams should revisit threat models accordingly.

### 13. Global Operation Arrests 276, Seizes $701M in Crypto Investment Fraud Crackdown
- **Source:** The Hacker News — https://thehackernews.com/2026/05/global-crackdown-arrests-276-shuts-9.html
- **Severity:** medium
- **Tags:** `phishing`, `fraud`
- **Summary:** International operation (Dubai, U.S., China) shut down 9 crypto scam centers and arrested 276 suspects running pig-butchering fraud against Americans, seizing $701M. Underscores the industrialization of social engineering fraud via crypto infrastructure.

### 14. Microsoft April 2026 Updates Break Third-Party Backup Apps via Driver Block
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-backup-failures-caused-by-vulnerable-driver-block/
- **Severity:** medium
- **Tags:** `microsoft`, `vulnerability`
- **Summary:** April 2026 Windows updates block psmounterex.sys, breaking third-party backup tools. Undetected backup failure removes ransomware recovery capability. Verify backup jobs are completing and coordinate with your backup vendor on a patched driver.

### 15. OpenAI Launches Advanced Account Security for ChatGPT Users
- **Source:** SecurityWeek — https://www.securityweek.com/openai-rolls-out-advanced-security-for-chatgpt-accounts/
- **Severity:** informational
- **Tags:** `openai`, `iam`, `llm`
- **Summary:** OpenAI added Advanced Account Security to ChatGPT: stronger login, more secure recovery, shorter sessions, training opt-out. Enterprise teams should evaluate and enforce these controls for ChatGPT Enterprise/Teams accounts.

## Skippable

- **TRE Python binding — ReDoS robustness demo** — Simon Willison. Personal developer experiment; no news event or actionable signal.
- **AWS Weekly Roundup (May 4, 2026)** — AWS News Blog. Generic cloud ops and conference summary; no security angle.
- **The latest AI news we announced in April 2026** — Google AI Blog. Thin monthly bulletin; no specific launch or security-relevant update surfaced.
- **Elon Musk's only AI expert witness at the OpenAI trial fears an AGI arms race** — TechCrunch AI. Opinion and trial commentary; no actionable security or AI safety news.
- **The creator of Roomba is back with a furry robot companion** — The Verge AI. Consumer robotics product; no security angle.
- **Forbes preliminarily agrees to pay $10 million to settle California wiretapping lawsuit** — The Record. Privacy class-action settlement; no technical security content.
- **Sierra raises $950M as the race to own enterprise AI gets serious** — TechCrunch AI. AI startup funding news; no security angle.
- **Elon Musk sent ominous texts to Greg Brockman, Sam Altman** — TechCrunch AI. OpenAI trial drama; no security content.
- **Redis Array Playground** — Simon Willison. Developer demo for new Redis data type; no security angle.
- **Ransomware group claims breach of pro-Orbán Hungarian media firm Mediaworks** — The Record. Ransomware victim disclosure without TTPs or IOCs; skippable per relevance rules.
- **⚡ Weekly Recap: AI-Powered Phishing, Android Spying Tool, Linux Exploit, GitHub RCE** — The Hacker News. Roundup article; individual stories covered in this digest.
- **5 days only: 50% off a second TechCrunch Disrupt 2026 pass** — TechCrunch AI. Conference ticket promotion.
- **They don't hack, they borrow: How fraudsters target credit unions** — BleepingComputer. Sponsored vendor content from Flare; marketing framing, no novel technique.
- **Cybersecurity M&A Roundup: 33 Deals Announced in April 2026** — SecurityWeek. Business deals roundup; no technical security content.
- **DoorDash adds AI tools to speed up merchant onboarding** — TechCrunch AI. Consumer product feature; no security angle.
- **Webinar: Why MSPs must rethink security and backup strategies** — BleepingComputer. Sponsored Kaseya webinar; promotional content.
- **How Dark Reading Lifted Off the Launchpad in 2006** — Dark Reading. 20th-anniversary editorial; no news value.
- **Trellix Source Code Repository Breached** — SecurityWeek. Duplicate of Trellix breach; merged into BleepingComputer primary post.
- **Educational company Infrastructure reports cyber incident** — The Record. Duplicate of Instructure/Canvas breach; merged into SecurityWeek primary post.
- **Silver Fox Springs Tax-Themed Attacks on Orgs in India, Russia** — Dark Reading. Duplicate of Silver Fox/ABCDoor campaign; merged into The Hacker News primary post.
- **Progress warns of critical MOVEit Automation auth bypass flaw** — BleepingComputer. Duplicate of MOVEit patch coverage; merged into The Hacker News primary post.
- **Exploitation of 'Copy Fail' Linux Vulnerability Begins** — SecurityWeek. Duplicate of Copy Fail flaw; merged into BleepingComputer primary post.
- **Critical cPanel Vulnerability Weaponized to Target Government and MSP Networks** — The Hacker News. Duplicate of cPanel CVE-2026-41940; targeting context incorporated into SecurityWeek primary post.
