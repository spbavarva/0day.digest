# Digest — 2026-08-14 PM

- Window: last 14h
- Raw items considered: 29
- Relevant: 12
- Skippable: 17

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Hackers Exploit macOS Screen Sharing Auth Bypass to Deploy Monero Miner — `2026-08-14-macos-screen-sharing-auth-bypass-monero-miner.md`
- [x] **[INFORMATIONAL]** Meta Releases Glimmer, an Open-Weight AI Model — `2026-08-14-meta-releases-glimmer-open-weight-model.md`
- [x] **[CRITICAL]** Max-Severity SAP Commerce Cloud RCE Flaw Actively Exploited Days After Patch — `2026-08-14-sap-commerce-cloud-critical-rce-actively-exploited.md`
- [x] **[HIGH]** France Investigates Tax Authority Breach Claiming 600,000 Victims — `2026-08-14-france-dgfip-tax-authority-breach.md`
- [x] **[HIGH]** Trivy, Not LiteLLM Packages, Was Behind 2,500-Org Compromise — `2026-08-14-trivy-not-litellm-2500-org-compromise.md`
- [x] **[INFORMATIONAL]** Google Cloud Lays Out Post-Quantum Cryptography Roadmap, Targets 2029 — `2026-08-14-google-cloud-post-quantum-roadmap-2029.md`
- [x] **[HIGH]** RingCentral Data Breach Exposes 1.6 Million Accounts — `2026-08-14-ringcentral-data-breach-1-6-million.md`
- [x] **[INFORMATIONAL]** Apple Reportedly Trained a Custom AI Model for China With Alibaba — `2026-08-14-apple-china-ai-model-alibaba.md`
- [x] **[HIGH]** Beacon CRM Breach Tied to Leaked AWS Key Hits Over 1,000 Charities — `2026-08-14-beacon-crm-breach-aws-key-leak-charities.md`
- [x] **[HIGH]** APT Group HoneyMyte Adds Kernel-Level Windows Rootkit to CoolClient Backdoor — `2026-08-14-honeymyte-coolclient-kernel-rootkit.md`
- [x] **[CRITICAL]** Hackers Exploit Unpatched GeoServer Zero-Day via SQL Injection — `2026-08-14-geoserver-zero-day-sql-injection-rce.md`
- [x] **[MEDIUM]** AmnesiaStealer: New Rust-Based macOS Infostealer Targets Browser Sessions — `2026-08-14-amnesiastealer-macos-infostealer.md`

## Relevant (details)

### 1. Hackers Exploit macOS Screen Sharing Auth Bypass to Deploy Monero Miner
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-exploit-macos-screen-sharing-flaw-to-deploy-monero-miner/
- **Severity:** high
- **Tags:** `vulnerability`, `malware`, `zero-day`
- **Summary:** The Netherlands' NCSC warns attackers are actively exploiting a macOS Screen Sharing authentication bypass after public exploit code emerged. Observed attacks use the bypass to deploy a Monero cryptocurrency miner.

### 2. Meta Releases Glimmer, an Open-Weight AI Model
- **Source:** TechCrunch AI — https://techcrunch.com/podcast/metas-open-ai-and-a-250m-deal-gone-very-wrong/
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `meta`
- **Summary:** Meta released Glimmer, an open-weight model anyone can download and run locally, contrasting with the closed, API-only Muse Spark. The release accompanied a Zuckerberg letter arguing AI should be "for everyone."

### 3. Max-Severity SAP Commerce Cloud RCE Flaw Actively Exploited Days After Patch
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `rce`
- **Summary:** A maximum-severity SAP Commerce Cloud RCE vulnerability, patched only three days ago, is already being targeted in attacks according to threat intel firm Defused.

### 4. France Investigates Tax Authority Breach Claiming 600,000 Victims
- **Source:** The Record (Recorded Future) — https://therecord.media/french-tax-authority-dgfip-confirms-data-breach
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** French authorities confirmed unauthorized access to the DGFiP tax authority's systems in late June, reportedly via misuse of a stolen identity, after a hacker claimed to have data on 600,000 people.

### 5. Trivy, Not LiteLLM Packages, Was Behind 2,500-Org Compromise
- **Source:** SecurityWeek — https://www.securityweek.com/trivy-not-litellm-behind-the-2500-org-compromise/
- **Severity:** high
- **Tags:** `supply-chain`, `pypi`, `container-security`
- **Summary:** New analysis attributes a widely reported compromise of ~2,500 organizations to Trivy rather than the malicious LiteLLM packages initially blamed — over 95% of affected companies were exposed before those packages were even published.

### 6. Google Cloud Lays Out Post-Quantum Cryptography Roadmap, Targets 2029
- **Source:** SecurityWeek — https://www.securityweek.com/google-cloud-sets-out-post-quantum-roadmap-with-2029-readiness-goal/
- **Severity:** informational
- **Tags:** `cloud-security`, `gcp`
- **Summary:** Google Cloud published a roadmap to full post-quantum cryptography readiness, targeting 2029 with intermediate milestones in 2027 and 2028.

### 7. RingCentral Data Breach Exposes 1.6 Million Accounts
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/ringcentral-data-breach-exposed-info-of-16-million-accounts/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** The ShinyHunters extortion group stole personal data (names, addresses, emails, phone numbers) from 1.6 million RingCentral accounts after breaching the company in July.

### 8. Apple Reportedly Trained a Custom AI Model for China With Alibaba
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/980160/apple-intelligence-china-custom-ai-model-alibaba
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `apple`, `alibaba`
- **Summary:** Apple reportedly trained a custom LLM for the China market in partnership with Alibaba, per Reuters sources — a rare cross-border collaboration amid US-China tech tensions. Neither company has confirmed details.

### 9. Beacon CRM Breach Tied to Leaked AWS Key Hits Over 1,000 Charities
- **Source:** SecurityWeek — https://www.securityweek.com/over-1000-charities-hit-by-beacon-crm-data-breach/
- **Severity:** high
- **Tags:** `data-breach`, `cloud-security`, `aws`
- **Summary:** A breach affecting 1,000+ charities using Beacon CRM is believed to stem from a compromised AWS access key that was exposed in publicly available JavaScript build artifacts.

### 10. APT Group HoneyMyte Adds Kernel-Level Windows Rootkit to CoolClient Backdoor
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/
- **Severity:** high
- **Tags:** `malware`, `privilege-escalation`, `rootkit`
- **Summary:** Kaspersky found a new CoolClient backdoor variant used by APT group HoneyMyte, now bundled with a kernel-mode rootkit driver that hides processes, files, and network connections from security tools.

### 11. Hackers Exploit Unpatched GeoServer Zero-Day via SQL Injection
- **Source:** SecurityWeek — https://www.securityweek.com/hackers-exploiting-unpatched-geoserver-zero-day/
- **Severity:** critical
- **Tags:** `zero-day`, `sqli`, `rce`, `vulnerability`
- **Summary:** Attackers are actively exploiting an unpatched SQL injection zero-day in GeoServer that can be leveraged to achieve remote code execution. No patch is currently available.

### 12. AmnesiaStealer: New Rust-Based macOS Infostealer Targets Browser Sessions
- **Source:** SecurityWeek — https://www.securityweek.com/amnesiastealer-macos-malware-steals-data-controls-browser-sessions/
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** A new Rust-based macOS infostealer, AmnesiaStealer, harvests saved passwords, Keychain data, Chromium browser data, and Safari cookies, and can control active browser sessions.

## Skippable

- **Mark Zuckerberg has an Instagzam** — The Verge AI. Podcast about an Instagram logo redesign, no security/AI substance.
- **You can now turn off Google Gemini's visible watermarks** — The Verge AI. Minor UI setting; invisible provenance watermark is unaffected.
- **Google will now allow users to remove visible watermark from its AI generations** — TechCrunch AI. Duplicate coverage of the Gemini watermark toggle.
- **Scottish Govt Suffers Potentially Widening Data Breach at Prosecutor's Office** — Dark Reading. Regional breach, scope unconfirmed, no technical detail.
- **Does Mark Zuckerberg really believe AI is 'for everyone'?** — TechCrunch AI. Opinion/podcast piece; the underlying Glimmer launch is covered separately.
- **The Good, the Bad and the Ugly in Cybersecurity – Week 33** — SentinelOne Labs. Weekly roundup format; individual items too thin on detail to draft separately.
- **Kog is going deeper to squeeze more inference out of GPUs** — TechCrunch AI. Startup/product piece, no security or model-launch substance.
- **Hyperscalers might regret embracing natural gas if new forecast proves correct** — TechCrunch AI. Energy market speculation, not AI or security news.
- **The Modern Attack Chain: Rethinking Google Workspace Security in the Age of AI** — BleepingComputer. Vendor-sponsored content (Material Security).
- **What Boards Need to Know About Tech Risk** — Dark Reading. Opinion piece, no news value.
- **Cyera's Oasis Security Buy Is All About AI Agent Control** — Dark Reading. M&A/business deal coverage, not a technical finding.
- **In Other News: Rapid7 Layoffs, Hacking a Boeing 737, Refrigeration System Vulnerabilities** — SecurityWeek. Link-dump roundup, no single item detailed enough to draft.
- **Shell investigates 'potential incident' after Clop data theft claims** — BleepingComputer. Ransomware victim disclosure without TTPs or IOCs.
- **Who's Tracking You? Use This New Service to Find Out** — Krebs on Security. Consumer ad-tracking transparency tool, not a security vulnerability or incident.
- **1.6 Million Likely Impacted by RingCentral Data Breach** — SecurityWeek. Duplicate coverage of the RingCentral breach (BleepingComputer version used).
- **Data analyst sent to prison for stealing data, extorting employer** — BleepingComputer. Sentencing news on an already-resolved insider incident, no novel technique.
- **14,000 Trezor Customers Impacted by Data Breach at ShipMonk** — SecurityWeek. Under 100k users, standard PII exposure, no technical novelty.
