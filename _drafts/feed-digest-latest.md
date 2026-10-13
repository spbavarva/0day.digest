# Digest — 2026-10-13 PM

- Window: last 14h
- Raw items considered: 29
- Relevant: 11
- Skippable: 18

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** SAP Patches Maximum-Severity OAuth2 SSRF Flaw in Cloud SDK for Python — `2026-10-13-sap-oauth2-ssrf-cloud-sdk-python.md`
- [x] **[CRITICAL]** Ledger Hardware Implant Tied to $86 Million Crypto Theft — `2026-10-13-ledger-hardware-implant-86-million-crypto-heist.md`
- [x] **[INFORMATIONAL]** American Express Launches Framework to Curb Unauthorized AI Agent Purchases — `2026-10-13-amex-ai-agent-purchase-framework.md`
- [x] **[MEDIUM]** Cyberattack Disrupts Ahold Delhaize Grocery Operations in US, Netherlands, and Belgium — `2026-10-13-ahold-delhaize-cyberattack-grocery-disruption.md`
- [x] **[INFORMATIONAL]** Anthropic Warns Small AI Models Could Soon Self-Replicate on IoT Devices — `2026-10-13-anthropic-ai-models-self-replicate-iot.md`
- [x] **[MEDIUM]** XWorm RAT Evolves Into Full Surveillance Platform — `2026-10-13-xworm-rat-surveillance-platform.md`
- [x] **[HIGH]** LG Smart TVs Vulnerable to Pre-Auth Root Takeover From Local Network — `2026-10-13-lg-smart-tv-preauth-root-takeover.md`
- [x] **[HIGH]** Attackers Hijack Danfoss Controllers to Heat French Supermarket Fridges to 50°C — `2026-10-13-danfoss-controller-hijack-french-supermarket-fridges.md`
- [x] **[HIGH]** Two Critical MarkLogic Flaws Allow Persistent Admin Takeover — `2026-10-13-marklogic-critical-privilege-escalation-flaws.md`
- [x] **[HIGH]** GitLab Patches CVSS 10.0 Flaw Allowing Unauthenticated Remote Code Execution — `2026-10-13-gitlab-cvss-10-unauthenticated-rce.md`
- [x] **[CRITICAL]** Low-Cost Android Phones Shipped With Preinstalled Malware for Residential Proxies — `2026-10-13-android-phones-preinstalled-malware-residential-proxies.md`

## Relevant (details)

### 1. SAP Patches Maximum-Severity OAuth2 SSRF Flaw in Cloud SDK for Python
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/sap-warns-of-maximum-severity-oauth2-ssrf-security-flaw/
- **Severity:** high
- **Tags:** `ssrf`, `vulnerability`, `cve`
- **Summary:** SAP's October 2026 updates fix 20 flaws, including a maximum-severity OAuth2 SSRF vulnerability in the Cloud SDK for Python. No active exploitation has been reported.

### 2. Ledger Hardware Implant Tied to $86 Million Crypto Theft
- **Source:** SecurityWeek — https://www.securityweek.com/86-million-crypto-heist-linked-to-ledger-signer-hardware-implant/
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`
- **Summary:** Ledger hardware wallets sold through a Southeast Asian reseller contained a hidden circuit-board implant that read and exfiltrated recovery phrases, linked to an $86 million cryptocurrency theft.

### 3. American Express Launches Framework to Curb Unauthorized AI Agent Purchases
- **Source:** TechCrunch AI — https://techcrunch.com/2026/10/13/amex-introduces-a-framework-to-prevent-ai-agents-from-making-unauthorized-purchases/
- **Severity:** informational
- **Tags:** `llm`, `ai-safety`
- **Summary:** American Express introduced a framework intended to ensure AI shopping agents only make purchases users explicitly authorized.

### 4. Cyberattack Disrupts Ahold Delhaize Grocery Operations in US, Netherlands, and Belgium
- **Source:** The Record (Recorded Future) — https://therecord.media/cyberattack-groceru-ahold-delhaize
- **Severity:** medium
- **Tags:** `data-breach`
- **Summary:** Ahold Delhaize disconnected some systems as a precaution following a cybersecurity incident affecting store operations in the US, Netherlands, and Belgium.

### 5. Anthropic Warns Small AI Models Could Soon Self-Replicate on IoT Devices
- **Source:** SecurityWeek — https://www.securityweek.com/small-ai-models-may-soon-be-able-to-self-replicate-on-iot-devices-anthropic-warns/
- **Severity:** informational
- **Tags:** `ai-safety`, `anthropic`, `llm`
- **Summary:** Anthropic researchers demonstrated that capable small AI models can run on cheap TV-box-class hardware and warned such models may eventually spread across IoT devices unsupervised.

### 6. XWorm RAT Evolves Into Full Surveillance Platform
- **Source:** SecurityWeek — https://www.securityweek.com/xworm-rat-evolves-into-surveillance-platform/
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** The XWorm remote access trojan expanded its plugin count to add location tracking, live audio streaming, and interaction with authenticated browser sessions.

### 7. LG Smart TVs Vulnerable to Pre-Auth Root Takeover From Local Network
- **Source:** The Hacker News — https://thehackernews.com/2026/10/lg-smart-tvs-vulnerable-to-pre-auth.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Summary:** Three chained vulnerabilities in LG's webOS let an attacker on the same local network gain root access to certain smart TVs with no PIN or user interaction. LG has shipped a fix.

### 8. Attackers Hijack Danfoss Controllers to Heat French Supermarket Fridges to 50°C
- **Source:** The Hacker News — https://thehackernews.com/2026/10/attackers-heat-french-supermarket.html
- **Severity:** high
- **Tags:** `iot`, `vulnerability`
- **Summary:** Attackers took remote control of refrigeration units at hundreds of French supermarkets via a remotely-managed Danfoss controller, forcing stores to discard spoiled food.

### 9. Two Critical MarkLogic Flaws Allow Persistent Admin Takeover
- **Source:** The Hacker News — https://thehackernews.com/2026/10/two-critical-marklogic-flaws-could-give.html
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`, `cve`
- **Summary:** Two of 31 newly disclosed MarkLogic Server flaws let a delegated-management account escalate to full administrator control. Fixes have been available since September 10.

### 10. GitLab Patches CVSS 10.0 Flaw Allowing Unauthenticated Remote Code Execution
- **Source:** The Hacker News — https://thehackernews.com/2026/10/gitlab-patches-cvss-100-flaw-that-could.html
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Summary:** GitLab patched a CVSS 10.0 flaw in CE/EE that could let an unauthenticated user execute arbitrary code via a crafted regular expression in a CI/CD pipeline context.

### 11. Low-Cost Android Phones Shipped With Preinstalled Malware for Residential Proxies
- **Source:** The Hacker News — https://thehackernews.com/2026/10/low-cost-android-phones-ship-with.html
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`
- **Summary:** Low-cost Android phones built on MediaTek platforms shipped from the factory with malware baked into firmware, tracked by Bitdefender as "Midnight Mimosa," turning devices into residential proxies.

## Skippable

- **The MFA Gaps Attackers are Still Exploiting** — BleepingComputer. Vendor-sponsored advice piece, no new technique or incident.
- **TechCrunch Disrupt 2026: Day 1** — TechCrunch AI. Conference promo, no news value.
- **SpaceXSI bundles X Premium, Grok and Cursor into one subscription** — TechCrunch AI. Product bundling announcement, no security or model substance.
- **Quoting Geoffrey Huntley** — Simon Willison. Opinion/quote post, no news value.
- **The final Disrupt Stage lineup** — TechCrunch AI. Conference promo, no news value.
- **Russian internet provider SkyNet reports outages after cyberattack** — The Record. Regional DDoS incident, no TTPs or technical detail.
- **Ledger says hardware implant in cryptocurrency wallets stole recovery phrases** — The Record. Duplicate coverage of the Ledger implant story; merged into the SecurityWeek item above.
- **Xandr Fined a Record €8.6 Million for Relaying Grindr Data** — The Hacker News. Adtech privacy enforcement action, not a vulnerability or breach.
- **South African clothing retailer Foschini Group investigating cyberattack** — The Record. Generic breach disclosure, no technical substance.
- **Apple launches HomeView, its first smart display for the home** — The Verge AI. Consumer product launch, no security or AI-safety angle.
- **The Enterprise Threat Intelligence Report: 2026** — Flashpoint. Vendor report promo, not a specific news item.
- **Just 5 years in, interactive chatbot platform Character.AI files for bankruptcy** — TechCrunch AI. Business/financial news, no security angle; duplicate of The Verge coverage below.
- **[Webinar] How to Stop AI-Driven Privilege Escalation With Runtime Identity Controls** — The Hacker News. Webinar promo / marketing content.
- **AI Turns Familiar Cyberattacks Into a Race Against Time** — SecurityWeek. Opinion/interview piece, no new technical detail.
- **Character.AI files for bankruptcy** — The Verge AI. Business/financial news, no security angle; duplicate of TechCrunch coverage above.
- **Product Walkthrough: Bitdefender AI Visibility and Control** — The Hacker News. Vendor product walkthrough, marketing content.
- **Cyberattack Prompts Grocery Giant Ahold Delhaize to Disconnect Systems** — SecurityWeek. Duplicate coverage of the Ahold Delhaize story; merged into The Record item above.
- **Refrigeration Controller Hack Spoils Food Across European Supermarkets** — SecurityWeek. Duplicate coverage of the Danfoss fridge-hijacking story; merged into The Hacker News item above.
