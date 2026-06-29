# Digest — 2026-06-29 AM

- Window: last 14h
- Raw items considered: 13
- Relevant: 9
- Skippable: 4

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Public PoC Released for Critical libssh2 CVE-2026-55200 Client-Side SSH Flaw — `2026-06-29-libssh2-cve-2026-55200-poc.md`
- [x] **[HIGH]** Hijacked npm and Go Packages Use VS Code Tasks to Deploy Python Infostealer — `2026-06-29-hijacked-npm-go-packages-infostealer.md`
- [x] **[HIGH]** Microsoft Removes 119 Edge Extensions That Hid Malware in Images and Fonts — `2026-06-29-microsoft-removes-edge-extensions-stegoad-malware.md`
- [x] **[HIGH]** 'DirtyClone' Linux Kernel Vulnerability Leads to Root Access — `2026-06-29-dirtyclone-linux-kernel-privilege-escalation.md`
- [x] **[HIGH]** The Gentlemen RaaS: Custom Backdoors and Evolving Tactics — `2026-06-29-gentlemen-raas-custom-backdoors.md`
- [x] **[MEDIUM]** Gamaredon Expands Ukraine Attacks with New Malware and Cloud Service Abuse — `2026-06-29-gamaredon-ukraine-cloud-service-abuse.md`
- [x] **[MEDIUM]** OpenAI and Anthropic Limit New AI Models to Trump-Approved Customers During Cybersecurity Review — `2026-06-29-openai-anthropic-limit-ai-models-trump-approved-customers.md`
- [x] **[MEDIUM]** US Offers $10 Million Bounty for Russian State Hackers as Messaging App Attacks Evolve — `2026-06-29-us-bounty-russian-state-hackers-messaging-apps.md`
- [x] **[INFORMATIONAL]** OpenAI Unveils GPT-5.6 Sol as Its Most Advanced Cybersecurity AI — `2026-06-29-openai-gpt-5-6-sol-cybersecurity-ai.md`

## Relevant (details)

### 1. Public PoC Released for Critical libssh2 CVE-2026-55200 Client-Side SSH Flaw
- **Source:** The Hacker News — https://thehackernews.com/2026/06/public-poc-released-for-critical.html
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `rce`
- **Summary:** A public PoC is now available for CVE-2026-55200, a CVSS 9.2 memory corruption flaw in libssh2 that lets a malicious SSH server compromise a connecting client with no auth or user interaction. Affects all releases up to 1.11.1.

### 2. Hijacked npm and Go Packages Use VS Code Tasks to Deploy Python Infostealer
- **Source:** The Hacker News — https://thehackernews.com/2026/06/hijacked-npm-and-go-packages-use-vs.html
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `malware`
- **Summary:** JFrog found two hijacked npm packages and a cluster of Go packages deploying a Python infostealer via VS Code task configs, sidestepping npm lifecycle-script hardening. Cross-ecosystem supply chain attack.

### 3. Microsoft Removes 119 Edge Extensions That Hid Malware in Images and Fonts
- **Source:** The Hacker News — https://thehackernews.com/2026/06/microsoft-removes-119-edge-extensions.html
- **Severity:** high
- **Tags:** `malware`, `supply-chain`, `appsec`
- **Summary:** Microsoft pulled 119 Edge extensions tied to one actor active since 2021, which hid payloads in image/font files ("StegoAd") and woke up days post-install to steal credentials and run ad fraud.

### 4. 'DirtyClone' Linux Kernel Vulnerability Leads to Root Access
- **Source:** SecurityWeek — https://www.securityweek.com/dirtyclone-linux-kernel-vulnerability-leads-to-root-access/
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`, `cve`
- **Summary:** A DirtyFrag variant dubbed "DirtyClone" lets unprivileged local Linux users manipulate the page cache to gain root. Local-access-only; no CVE ID or patch status given in the summary.

### 5. The Gentlemen RaaS: Custom Backdoors and Evolving Tactics
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/the-gentlemen-raas/120447/
- **Severity:** high
- **Tags:** `ransomware`, `malware`
- **Summary:** Kaspersky disclosed tools and TTPs of "The Gentlemen" RaaS group, including a newly identified ransomware variant and custom backdoors, indicating active toolset development.

### 6. Gamaredon Expands Ukraine Attacks with New Malware and Cloud Service Abuse
- **Source:** The Hacker News — https://thehackernews.com/2026/06/gamaredon-expands-ukraine-attacks-with.html
- **Severity:** medium
- **Tags:** `malware`, `phishing`, `cloud-security`
- **Summary:** ESET tracked 35 new Gamaredon spear-phishing campaigns against Ukraine through 2025, plus new malware and cloud-service abuse for C2/exfiltration.

### 7. OpenAI and Anthropic Limit New AI Models to Trump-Approved Customers During Cybersecurity Review
- **Source:** SecurityWeek — https://www.securityweek.com/openai-and-anthropic-limit-new-ai-models-to-trump-approved-customers-during-cybersecurity-review/
- **Severity:** medium
- **Tags:** `openai`, `anthropic`, `ai-safety`, `llm`
- **Summary:** OpenAI is restricting a new model's release to government-approved customers at the Trump administration's request during a cybersecurity review; Anthropic is reportedly under similar restrictions.

### 8. US Offers $10 Million Bounty for Russian State Hackers as Messaging App Attacks Evolve
- **Source:** SecurityWeek — https://www.securityweek.com/us-offers-10-million-bounty-for-russian-state-hackers-as-messaging-app-attacks-evolve/
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Summary:** The US is offering $10M for info on UNC5792/UNC4221, Russian state hackers targeting US officials and military via messaging app attacks.

### 9. OpenAI Unveils GPT-5.6 Sol as Its Most Advanced Cybersecurity AI
- **Source:** SecurityWeek — https://www.securityweek.com/openai-unveils-gpt-5-6-sol-as-its-most-advanced-cybersecurity-ai/
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `openai`, `llm`
- **Summary:** OpenAI launched GPT-5.6 "Sol," billed as its most advanced cybersecurity-focused model, claiming parity with Anthropic's Mythos Preview using about a third of the output tokens.

## Skippable

- **Why Post-Quantum Cryptography Starts With Credentials** — The Hacker News. Generic educational/opinion piece on PQC migration, no specific news event.
- **US seizes hundreds of FIFA World Cup illegal streaming domains** — BleepingComputer. Piracy domain seizure, no infosec/AI angle.
- **Mapping Europe's AI Workforce Opportunity** — OpenAI Blog. Labor-market/economic report, no security or model-capability substance.
- **Quoting Jon Udell** — Simon Willison. Opinion commentary on agentic coding philosophy, no news value.
