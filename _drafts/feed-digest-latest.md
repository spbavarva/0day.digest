# Digest — 2026-10-21 PM

- Window: last 14h
- Raw items considered: 28
- Relevant: 16
- Skippable: 12

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Mozilla, Google, Apple Block Compromised eMudhra Intermediate CA Certificates — `2026-10-21-emudhra-ca-compromise-browsers-block-certificates.md`
- [x] **[CRITICAL]** PHP2Shell: Critical Unpatched PHP RCE Flaws (CVSS 9.2) Trigger Emergency Patch — `2026-10-21-php2shell-critical-unpatched-rce-cvss-9-2.md`
- [x] **[HIGH]** US Orders DeepSeek Removed From Federal Systems; China Pushes Back — `2026-10-21-us-bans-deepseek-federal-systems-china-reaction.md`
- [x] **[HIGH]** Stolen UpdraftCentral Keys Used to Backdoor WordPress Sites — `2026-10-21-updraftcentral-keys-stolen-wordpress-backdoors.md`
- [x] **[HIGH]** CISA Adds Actively Exploited Plex2Shell, Siemens, and SiteGuard Flaws to KEV Catalog — `2026-10-21-cisa-kev-plex2shell-siemens-siteguard.md`
- [x] **[HIGH]** Hijacked Developer Account Used to Plant Stealer in OVHcloud CLI — `2026-10-21-ovhcloud-cli-supply-chain-stealer-glassworm.md`
- [x] **[HIGH]** Operation FlashHole: Lazarus Group Abuses CrossWeb EX in Watering-Hole Campaign — `2026-10-21-lazarus-operation-flashhole-crossweb-ex.md`
- [x] **[HIGH]** Attackers Hijacked Over 300 Tor Exit Relays to Intercept SSH Connections — `2026-10-21-tor-exit-relay-hijack-ssh-credential-theft.md`
- [x] **[MEDIUM]** Talos: Attackers Abuse 25+ Legitimate Platforms as Malware Delivery Pipelines — `2026-10-21-talos-legitimate-platforms-malware-delivery.md`
- [x] **[MEDIUM]** Hackers Hid Vasilek Backdoor in VMware Tools During 2-Year Russian Healthcare Intrusion — `2026-10-21-vasilek-backdoor-vmware-tools-russian-healthcare.md`
- [x] **[MEDIUM]** Chinese AI Model Writes More Hackable Code When Told It's for a US Defense Contractor — `2026-10-21-chinese-ai-model-hackable-code-us-contractor-framing.md`
- [x] **[MEDIUM]** Anthropic Pitches AI Safety Bill That Could Block Models Over Mass-Casualty Risk — `2026-10-20-anthropic-ai-safety-bill-mass-casualty-risk.md`
- [x] **[INFORMATIONAL]** Google Cloud's Confidential Computing on G4 Blackwell GPUs Reaches GA — `2026-10-21-google-cloud-confidential-g4-blackwell-ga.md`

## Relevant (details)

### 1. Mozilla, Google, Apple Block Compromised eMudhra Intermediate CA Certificates
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/mozilla-google-apple-block-compromised-emudhra-ca-certificates/ (also: Simon Willison — https://simonwillison.net/2026/Oct/20/emudhra-certificates/)
- **Severity:** critical
- **Tags:** `vulnerability`, `certificate-authority`
- **Summary:** Recoverable private keys for eight eMudhra intermediate CA certificates let anyone forge trusted certificates for arbitrary sites; eMudhra revoked the certs and major browsers blocked them, requiring trust-store and library updates downstream.

### 2. PHP2Shell: Critical Unpatched PHP RCE Flaws (CVSS 9.2) Trigger Emergency Patch
- **Source:** The Hacker News — https://thehackernews.com/2026/10/php2shell-what-actually-protects-you.html (also: SecurityWeek — https://www.securityweek.com/php2shell-mass-exploitation-looms-for-leaked-critical-php-flaws/)
- **Severity:** critical
- **Tags:** `rce`, `cve`
- **Summary:** PHP shipped an emergency out-of-cycle patch for CVE-2026-109618 and CVE-2026-109619 (CVSS 9.2, unauthenticated RCE) after details leaked ahead of the official advisory; no fully effective workaround existed before the fix.

### 3. US Orders DeepSeek Removed From Federal Systems; China Pushes Back
- **Source:** The Hacker News — https://thehackernews.com/2026/10/us-orders-deepseek-removed-from-federal.html (also: SecurityWeek — https://www.securityweek.com/china-defends-deepseek-after-us-ban-of-its-ai-from-government-systems/)
- **Severity:** high
- **Tags:** `deepseek`, `ai-regulation`
- **Summary:** DHS ordered US federal civilian agencies to remove DeepSeek products and software built on DeepSeek, and barred new purchases from the company; China's government pushed back, calling the move targeted at Chinese AI technology.

### 4. Stolen UpdraftCentral Keys Used to Backdoor WordPress Sites
- **Source:** The Hacker News — https://thehackernews.com/2026/10/attackers-abuse-updraftcentral-keys-to.html
- **Severity:** high
- **Tags:** `supply-chain`, `credential-theft`
- **Summary:** A breach of TeamUpdraft's website potentially exposed UpdraftCentral/UpdraftVault/UpdraftClone connection keys for the UpdraftPlus plugin (4M+ installs); stolen keys were used to backdoor connected WordPress sites.

### 5. CISA Adds Actively Exploited Plex2Shell, Siemens, and SiteGuard Flaws to KEV Catalog
- **Source:** The Hacker News — https://thehackernews.com/2026/10/cisa-orders-federal-agencies-to-patch.html
- **Severity:** high
- **Tags:** `cve`, `ssrf`
- **Summary:** CISA added four actively exploited flaws to its KEV catalog, including a Plex Media Server SSRF (CVE-2026-96652) and vulnerabilities in Siemens and SiteGuard products, triggering the federal patch mandate.

### 6. Hijacked Developer Account Used to Plant Stealer in OVHcloud CLI
- **Source:** SecurityWeek — https://www.securityweek.com/hijacked-developer-account-used-to-plant-stealer-in-ovhcloud-cli/
- **Severity:** high
- **Tags:** `supply-chain`, `malware`
- **Summary:** A GlassWorm-linked loader compromised a developer account in March, which was used to plant an infostealer in the OVHcloud CLI tool.

### 7. Operation FlashHole: Lazarus Group Abuses CrossWeb EX in Watering-Hole Campaign
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/lazarus-operation-flashhole/121541/
- **Severity:** high
- **Tags:** `malware`, `apt`
- **Summary:** Kaspersky documented a Lazarus-attributed campaign combining a watering-hole technique with abuse of CrossWeb EX financial security software, deploying a sophisticated malware set.

### 8. Attackers Hijacked Over 300 Tor Exit Relays to Intercept SSH Connections
- **Source:** The Hacker News — https://thehackernews.com/2026/10/attackers-hijacked-over-300-tor-exit.html
- **Severity:** high
- **Tags:** `malware`, `credential-theft`
- **Summary:** More than 300 Tor exit relays were hijacked in early October and used to intercept and redirect password-authenticated SSH logins to credential-harvesting servers.

### 9. Talos: Attackers Abuse 25+ Legitimate Platforms as Malware Delivery Pipelines
- **Source:** Cisco Talos — https://blog.talosintelligence.com/parasitizing-trust-how-legitimate-infrastructure-becomes-a-delivery-pipeline-for-attackers/
- **Severity:** medium
- **Tags:** `malware`, `appsec`
- **Summary:** Cisco Talos observed abuse of 25+ legitimate collaboration, file-sharing, and payment platforms as malware delivery pipelines over the past year, exploiting the inherent trust of that infrastructure.

### 10. Hackers Hid Vasilek Backdoor in VMware Tools During 2-Year Russian Healthcare Intrusion
- **Source:** The Hacker News — https://thehackernews.com/2026/10/hackers-hid-vasilek-backdoor-in-vmware.html
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** A Belarus-aligned hacktivist group (Partisan Zmiy / Cyber Partisans) spent nearly two years inside a Russian healthcare organization's network, hiding a backdoor called Vasilek inside VMware Tools.

### 11. Chinese AI Model Writes More Hackable Code When Told It's for a US Defense Contractor
- **Source:** SecurityWeek — https://www.securityweek.com/chinese-ai-model-writes-more-hackable-code-when-told-its-for-us-contractor/
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`
- **Summary:** Researchers found a Chinese AI model produced 19% more hackable code when told the application was for a US defense contractor, raising concerns about context-dependent model behavior in security-sensitive development.

### 12. Anthropic Pitches AI Safety Bill That Could Block Models Over Mass-Casualty Risk
- **Source:** TechCrunch AI — https://techcrunch.com/2026/10/20/anthropic-pitches-ai-safety-bill-that-may-block-a-model-if-50-people-could-be-killed/
- **Severity:** medium
- **Tags:** `anthropic`, `ai-safety`
- **Summary:** Anthropic proposed legislation allowing a model's release to be blocked if it could plausibly enable 50+ deaths, but the bill would require a judge's permission before an agency could act, a structure critics say could slow intervention.

### 13. Google Cloud's Confidential Computing on G4 Blackwell GPUs Reaches GA
- **Source:** Google Cloud Security — https://cloud.google.com/blog/topics/ai-infrastructure/confidential-g4-gpus-are-ga/
- **Severity:** informational
- **Tags:** `cloud-security`, `gcp`
- **Summary:** Google Cloud launched general availability of Confidential Computing on G4 instances with NVIDIA Blackwell GPUs, extending hardware-backed protection to model weights, prompts, and outputs processed on those GPUs.

## Skippable

- **Microsoft PowerToys adds CursorHide, Button Lock mouse tools** — BleepingComputer. Generic feature update, no security angle.
- **Browsers Block eMudhra Intermediate CAs Over Recoverable Private Keys** — SecurityWeek. Duplicate coverage of the eMudhra CA story, folded into item 1 (BleepingComputer/Simon Willison sources).
- **Announcing SimReady Central: An Open Library of Simulation-Ready 3D Assets** — Hugging Face Blog. Asset library release for robotics, no model launch or security substance.
- **The Harness Is the Hard Part of Agentic Pentesting** — The Hacker News. Thought-leadership piece on AI pentesting harness design; no new incident or finding.
- **Microsoft says October updates didn't actually fix VPN issues** — BleepingComputer. Reliability bug, not a security vulnerability.
- **PHP2Shell: Two Unpatched Critical PHP RCE Flaws (CVSS 9.2) Trigger Emergency Security Alert** — The Hacker News. Earlier developing-story coverage of the PHP2Shell flaws, superseded by item 2's sources once CVE numbers were confirmed.
- **CISA: SafePay ransomware hit over 600 critical infrastructure orgs** — BleepingComputer. Victim-count advisory with no new IOCs or TTPs in the summary.
- **State Bank of India Confirms Data Leak After 3,897 Customer Records Found on Dark Web** — The Hacker News. Confirmed scope (~3,897 records) is below the relevance threshold and no technical detail on cause.
- **Accenture, Dragos, SANS Launch $10M Initiative to Defend Small US Utilities** — SecurityWeek. Funding/initiative announcement, not a technical security event.
- **Southeast Asia's digital economy to hit $368 billion** — Google AI Blog. Macro economic report, no AI or security substance.
- **Stolen UpdraftCentral keys used to backdoor WordPress sites** — BleepingComputer. Duplicate coverage of the UpdraftCentral story, folded into item 4 (The Hacker News source).
- **Judge dismisses Sam Altman's sister's sexual abuse lawsuit** — The Verge AI. Personal legal matter, no AI or security substance.
