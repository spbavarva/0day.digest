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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `pypi`, `malware`, `infostealer`
- **Slug:** `2026-05-04-pytorch-lightning-pypi-backdoor`
- **Must-know:** yes
- **Summary:** A malicious version of PyTorch Lightning was published to PyPI delivering a credential-stealer targeting browser credentials, `.env` files, and cloud services. PyTorch Lightning's wide adoption in ML workflows makes the supply chain reach significant; any team using the package should audit their dependency tree and rotate exposed credentials immediately.

### 2. 'Copy Fail' Linux Flaw Hits CISA KEV as Active Exploitation Begins
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-says-copy-fail-flaw-now-exploited-to-root-linux-systems/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`, `zero-day`
- **Slug:** `2026-05-04-copy-fail-linux-cve-exploited`
- **Must-know:** yes
- **Summary:** CISA added the "Copy Fail" Linux privilege escalation flaw to the KEV catalog confirming active exploitation, just one day after Theori published a PoC. Microsoft observed limited exploitation associated with PoC testing. Linux system admins should patch immediately; the KEV listing triggers federal remediation mandates and signals broad real-world risk.

### 3. cPanel Zero-Day CVE-2026-41940 Exploited Across 40,000+ Servers
- **Source:** SecurityWeek — https://www.securityweek.com/over-40000-servers-compromised-in-ongoing-cpanel-exploitation/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `vulnerability`, `rce`
- **Slug:** `2026-05-04-cpanel-cve-2026-41940-mass-exploitation`
- **Must-know:** yes
- **Summary:** CVE-2026-41940, a recently patched cPanel zero-day enabling administrative access, has compromised 40,000+ servers in ongoing mass exploitation. A separate targeted campaign hits government and military entities in Southeast Asia and MSPs across multiple countries. Patch immediately and audit for web shells and unauthorized admin accounts.

### 4. Progress Patches Critical Authentication Bypass in MOVEit Automation
- **Source:** The Hacker News — https://thehackernews.com/2026/05/progress-patches-critical-moveit.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`
- **Slug:** `2026-05-04-moveit-automation-auth-bypass-patch`
- **Must-know:** no
- **Summary:** Progress Software patched two flaws in MOVEit Automation including a critical authentication bypass. No confirmed active exploitation yet, but MOVEit's 2023 mass exploitation history makes this a priority patch; ransomware operators are well-acquainted with this attack surface.

### 5. Trellix Discloses Data Breach After Source Code Repository Hack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/trellix-discloses-data-breach-after-source-code-repository-hack/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `supply-chain`
- **Slug:** `2026-05-04-trellix-source-code-repo-breach`
- **Must-know:** no
- **Summary:** Trellix (formerly McAfee Enterprise + FireEye) disclosed attackers accessed a portion of its source code repository. The company found no confirmed impact on source code distribution, but the investigation is ongoing. Customers should monitor Trellix advisories and verify software update integrity.

### 6. DigiCert Support Portal Hacked via Malware; Certificates Revoked
- **Source:** SecurityWeek — https://www.securityweek.com/digicert-revokes-certificates-after-support-portal-hack/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `data-breach`, `pki`
- **Slug:** `2026-05-04-digicert-support-portal-breach`
- **Must-know:** no
- **Summary:** Attackers delivered malware via DigiCert's customer chat channel, infected a support analyst's system, and accessed the internal support portal, prompting DigiCert to revoke customer certificates. Organizations using DigiCert should check for revoked certificates and reissue as necessary.

### 7. VENOMOUS#HELPER: Phishing Campaign Abuses RMM Tools to Persist in 80+ Organizations
- **Source:** The Hacker News — https://thehackernews.com/2026/05/phishing-campaign-hits-80-orgs-using.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `malware`, `rmm`
- **Slug:** `2026-05-04-venomous-helper-rmm-phishing`
- **Must-know:** no
- **Summary:** Active since April 2025, VENOMOUS#HELPER has hit 80+ orgs (mostly U.S.) using phishing to gain initial access, then deploying SimpleHelp and ScreenConnect RMM tools for persistent access. Legitimate RMM usage blends in with IT operations, complicating detection. Audit for unexpected RMM deployments and enforce application allowlisting.

### 8. Silver Fox APT Deploys New ABCDoor Backdoor via Tax-Themed Phishing
- **Source:** The Hacker News — https://thehackernews.com/2026/05/silver-fox-deploys-abcdoor-malware-via.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `malware`, `apt`
- **Slug:** `2026-05-04-silver-fox-abcdoor-tax-phishing`
- **Must-know:** no
- **Summary:** China-based Silver Fox APT ran tax-authority-impersonating phishing campaigns against organizations in India and Russia, distributing 1,600+ messages and deploying a new undocumented backdoor (ABCDoor) plus ValleyRAT. Both campaigns followed near-identical playbooks, suggesting templated operation at scale.

### 9. Instructure Canvas LMS Discloses Breach Exposing Student Data Amid Leak Threats
- **Source:** SecurityWeek — https://www.securityweek.com/edtech-firm-instructure-discloses-data-breach/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `2026-05-04-instructure-canvas-data-breach`
- **Must-know:** no
- **Summary:** Instructure's Canvas LMS was breached; hackers stole names, email addresses, student IDs, and user messages from multiple educational institutions and are threatening to leak data. Affected institutions should issue breach notifications and watch for follow-on phishing using stolen contact data.

### 10. Attackers Weaponize Amazon SES to Send Phishing Emails That Pass Security Filters
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/amazon-ses-phishing-and-bec-attacks/119623/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `phishing`, `aws`, `cloud-security`
- **Slug:** `2026-05-04-amazon-ses-phishing-bec-bypass`
- **Must-know:** no
- **Summary:** Kaspersky GReAT documented BEC and phishing schemes that abuse Amazon SES's established sending reputation to pass SPF/DKIM/DMARC checks. Because SES is a legitimate AWS service, messages bypass infrastructure-reputation filters. Security teams should add behavioral analysis beyond authentication checks to email pipelines.

### 11. Anthropic and OpenAI Both Launch Enterprise AI Joint Ventures with Asset Managers
- **Source:** TechCrunch AI — https://techcrunch.com/2026/05/04/anthropic-and-openai-are-both-launching-joint-ventures-for-enterprise-ai-services/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `anthropic`, `openai`, `ai-launch`
- **Slug:** `2026-05-04-anthropic-openai-enterprise-ai-joint-ventures`
- **Must-know:** no
- **Summary:** Both Anthropic and OpenAI announced enterprise AI joint ventures with asset managers, signaling a shift from developer-first to institutionally backed direct enterprise sales. Organizations evaluating frontier AI vendors should track partnership structures for implications on pricing, data governance, and long-term support terms.

### 12. 2026 Emerges as a Pivotal Year for AI-Assisted Cyberattacks
- **Source:** The Hacker News — https://thehackernews.com/2026/05/2026-year-of-ai-assisted-attacks.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`, `malware`
- **Slug:** `2026-05-04-ai-assisted-attacks-2026-trend`
- **Must-know:** no
- **Summary:** THN analysis documenting how AI tools are lowering attacker skill floors in 2026, with low-sophistication actors using AI for malware generation, phishing lure creation, and large-scale data extraction. A referenced case: a 17-year-old used AI to extract data on 7 million users of a Japanese internet cafe chain. Defenders should revisit threat models.

### 13. Global Operation Arrests 276, Seizes $701M in Crypto Investment Fraud Crackdown
- **Source:** The Hacker News — https://thehackernews.com/2026/05/global-crackdown-arrests-276-shuts-9.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `fraud`
- **Slug:** `2026-05-04-global-crypto-scam-crackdown-276-arrests`
- **Must-know:** no
- **Summary:** Dubai Police, with U.S. and Chinese partners, arrested 276 suspects and shut down 9 crypto scam centers running pig-butchering and fake investment schemes targeting Americans, seizing $701M. The operation highlights the industrialization of social engineering fraud and abuse of crypto infrastructure.

### 14. Microsoft April 2026 Updates Break Third-Party Backup Apps via Driver Block
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-backup-failures-caused-by-vulnerable-driver-block/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `microsoft`, `vulnerability`
- **Slug:** `2026-05-04-microsoft-april-2026-update-backup-failures`
- **Must-know:** no
- **Summary:** April 2026 Windows security updates are blocking psmounterex.sys, breaking third-party backup applications. Undetected backup failures remove ransomware recovery options. Administrators should immediately verify backup job completion and coordinate with their vendor for a patched driver.

### 15. OpenAI Launches Advanced Account Security for ChatGPT Users
- **Source:** SecurityWeek — https://www.securityweek.com/openai-rolls-out-advanced-security-for-chatgpt-accounts/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `openai`, `iam`, `llm`
- **Slug:** `2026-05-04-openai-chatgpt-advanced-account-security`
- **Must-know:** no
- **Summary:** OpenAI rolled out Advanced Account Security for ChatGPT with stronger login, more secure recovery, shorter sessions, and training exclusion options. Enterprise teams managing ChatGPT Enterprise or Teams accounts should evaluate and enforce available security controls.

## Skippable

- **TRE Python binding — ReDoS robustness demo** — Simon Willison. Personal developer experiment with a regex library; no news event, no security incident, no actionable signal.
- **AWS Weekly Roundup (May 4, 2026)** — AWS News Blog. Generic cloud ops summary covering conference content and partnership announcements; no security angle.
- **The latest AI news we announced in April 2026** — Google AI Blog. Thin monthly bulletin with no specific model launch or security-relevant update surfaced in the summary.
- **Elon Musk's only AI expert witness at the OpenAI trial fears an AGI arms race** — TechCrunch AI. Opinion and trial commentary from Stuart Russell; no actionable security or AI safety news.
- **The creator of Roomba is back with a furry robot companion** — The Verge AI. Consumer robotics product launch with no security or AI-safety angle.
- **Forbes preliminarily agrees to pay $10 million to settle California wiretapping lawsuit** — The Record. Privacy class-action settlement; no technical security content or practitioner relevance.
- **Sierra raises $950M as the race to own enterprise AI gets serious** — TechCrunch AI. AI startup funding news; no security angle.
- **Elon Musk sent ominous texts to Greg Brockman, Sam Altman after asking for a settlement** — TechCrunch AI. OpenAI trial drama; no security content.
- **Redis Array Playground** — Simon Willison. Interactive developer demo for a new Redis data type; no security angle.
- **Ransomware group claims breach of pro-Orbán Hungarian media firm Mediaworks** — The Record. Ransomware victim disclosure without TTPs, IOCs, or technical detail per relevance rules.
- **⚡ Weekly Recap: AI-Powered Phishing, Android Spying Tool, Linux Exploit, GitHub RCE & More** — The Hacker News. Roundup article; individual stories covered in this digest separately.
- **5 days only: 50% off a second TechCrunch Disrupt 2026 pass** — TechCrunch AI. Conference ticket promotion.
- **They don't hack, they borrow: How fraudsters target credit unions** — BleepingComputer. Sponsored vendor content from Flare; marketing framing, no novel attack technique.
- **Cybersecurity M&A Roundup: 33 Deals Announced in April 2026** — SecurityWeek. Business deals roundup; no technical security content.
- **DoorDash adds AI tools to speed up merchant onboarding, edit photos of dishes** — TechCrunch AI. Consumer product AI feature; no security angle.
- **Webinar: Why MSPs must rethink security and backup strategies** — BleepingComputer. Sponsored Kaseya webinar; promotional content.
- **How Dark Reading Lifted Off the Launchpad in 2006** — Dark Reading. 20th-anniversary editorial retrospective; no news value.
- **Trellix Source Code Repository Breached** — SecurityWeek. Duplicate coverage of Trellix breach; merged into BleepingComputer primary post.
- **Educational company Infrastructure reports cyber incident** — The Record. Duplicate coverage of Instructure/Canvas breach; merged into SecurityWeek primary post.
- **Silver Fox Springs Tax-Themed Attacks on Orgs in India, Russia** — Dark Reading. Duplicate coverage of Silver Fox/ABCDoor campaign; merged into The Hacker News primary post.
- **Progress warns of critical MOVEit Automation auth bypass flaw** — BleepingComputer. Duplicate coverage of MOVEit patch; merged into The Hacker News primary post.
- **Exploitation of 'Copy Fail' Linux Vulnerability Begins** — SecurityWeek. Duplicate coverage of Copy Fail flaw; merged into BleepingComputer primary post.
- **Critical cPanel Vulnerability Weaponized to Target Government and MSP Networks** — The Hacker News. Duplicate coverage of cPanel CVE-2026-41940; targeting detail incorporated into SecurityWeek primary post.
