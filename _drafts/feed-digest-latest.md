# Digest — 2026-11-12 PM

- Window: last 14h
- Raw items considered: 39
- Relevant: 19
- Skippable: 16

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[INFORMATIONAL]** Police Dismantle Gootloader, CastleRAT, StealC Malware Infrastructure — `2026-11-12-gootloader-castlerat-stealc-takedown.md`
- [x] **[MEDIUM]** Fireworks AI Breach Exposes Notion Customer Chat Transcripts — `2026-11-12-fireworks-ai-notion-breach.md`
- [x] **[HIGH]** Attackers Use Autonomous AI Framework to Breach Semiconductor and Defense Targets — `2026-11-12-cairn-ai-autonomous-attacks.md`
- [x] **[MEDIUM]** Apify Rotates API Tokens, Forces 2FA Resets After Breach — `2026-11-12-apify-breach-token-rotation.md`
- [x] **[CRITICAL]** Hijacked GitHub Accounts Plant CI Secret Stealer in 1,800+ Repositories — `2026-11-12-github-ci-secret-stealer-wfx-loot.md`
- [x] **[HIGH]** Kazakhstan-Linked Hackers Used AI Agent to Spy on Central Asian Governments — `2026-11-12-kazakhstan-ai-agent-espionage.md`
- [x] **[HIGH]** Google Cloud Warns AMD Turin CPU Flaws Can Leak Data Across VM Processes — `2026-11-12-google-cloud-amd-turin-cpu-flaws.md`
- [x] **[CRITICAL]** N-central Zero-Days Under Active Exploitation as N-able Rushes Patches — `2026-11-12-n-central-zero-day-active-exploitation.md`
- [x] **[HIGH]** Google Session Hijacking Campaign Uses Calendar Invites and Live Proxies — `2026-11-12-google-session-hijacking-operation-cloudfire.md`
- [x] **[CRITICAL]** Critical RCE Flaw Patched in PTC Windchill and FlexPLM — `2026-11-12-ptc-windchill-flexplm-rce.md`
- [x] **[HIGH]** AI-Generated Scripts Enabled Rapid Lateral Movement in Retailer Breach — `2026-11-12-ai-attack-us-retailer-lateral-movement.md`
- [x] **[HIGH]** ScreenConnect Rogue Clients Hit 288 Endpoints Across 48 Organizations — `2026-11-12-screenconnect-rogue-clients-campaign.md`
- [x] **[INFORMATIONAL]** Inside a Cloud Pentest: Trust Boundaries Across Cloud Layers — `2026-11-12-cloud-pentest-trust-boundaries.md`
- [x] **[MEDIUM]** Hackers Abuse GSocket for Persistent Access on Linux Servers — `2026-11-12-gsocket-linux-persistent-access.md`
- [x] **[CRITICAL]** Critical Pre-Auth MongoDB Flaw Can Crash Servers During Failover — `2026-11-12-mongodb-preauth-crash-cve-2026-118383.md`
- [x] **[CRITICAL]** Critical Red Hat Quay Flaw Could Expose Private Container Images — `2026-11-12-red-hat-quay-critical-vulnerability.md`
- [x] **[HIGH]** Maersk Confirms Data Theft Amid $5 Million Extortion Demand — `2026-11-12-maersk-data-theft-whitearmor-extortion.md`
- [x] **[HIGH]** Node.js Patches 16 Flaws Including HTTP/2 Crash and Data Leak Bugs — `2026-11-12-nodejs-http2-flaws-crash-leak.md`
- [x] **[CRITICAL]** Critical Apache HTTP/2 Flaw Enables Unauthenticated Remote Code Execution — `2026-11-12-apache-http2-mod-http2-rce-cve-2026-119618.md`

## Relevant (details)

### 1. Police Dismantle Gootloader, CastleRAT, StealC Malware Infrastructure
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/police-dismantles-gootloader-castlerat-stealc-malware-infrastructure/
- **Severity:** informational
- **Tags:** `malware`
- **Summary:** Europol and partners from nine countries seized hundreds of servers and domains behind the Gootloader, CastleRAT, and StealC malware operations. These loaders have been widely used for initial access, including as a path to ransomware.

### 2. Fireworks AI Breach Exposes Notion Customer Chat Transcripts
- **Source:** SecurityWeek — https://www.securityweek.com/notion-customer-data-compromised-in-fireworks-ai-hack/
- **Severity:** medium
- **Tags:** `data-breach`, `llm`
- **Summary:** A breach at AI inference provider Fireworks AI exposed chat transcripts for fewer than 1% of Notion workspaces using Notion's AI features; most transcripts were unattributable. It's Fireworks' second disclosed breach in two months.

### 3. Attackers Use Autonomous AI Framework to Breach Semiconductor and Defense Targets
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/cairn-framework-ai-autonomous-attacks/
- **Severity:** high
- **Tags:** `ai-safety`, `llm`, `malware`
- **Summary:** Unit 42 observed attackers using the open-source Cairn AI agent framework to autonomously breach semiconductor, defense, and civil society targets. The agent planned and executed attack-chain steps with limited human direction.

### 4. Apify Rotates API Tokens, Forces 2FA Resets After Breach
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/apify-rotates-api-tokens-prompts-2fa-resets-after-breach/
- **Severity:** medium
- **Tags:** `data-breach`, `cloud-security`
- **Summary:** Apify rotated internal secrets and revoked some third-party OAuth connections after detecting unauthorized access, and is prompting customers to reset 2FA.

### 5. Hijacked GitHub Accounts Plant CI Secret Stealer in 1,800+ Repositories
- **Source:** The Hacker News — https://thehackernews.com/2026/11/4837-hijacked-github-accounts-ran-ci.html
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `data-breach`
- **Summary:** An attacker used 4,837 hijacked GitHub accounts to plant the wfx-loot CI secret stealer in at least 1,806 repositories, harvesting secrets and cloud credentials reachable from CI workflows.

### 6. Kazakhstan-Linked Hackers Used AI Agent to Spy on Central Asian Governments
- **Source:** The Record (Recorded Future) — https://therecord.media/kazakhstan-hackers-central-asia
- **Severity:** high
- **Tags:** `ai-safety`, `llm`, `privilege-escalation`
- **Summary:** Suspected Kazakhstan-linked hackers used an AI agent to help spy on Central Asian governments, steal sensitive documents, and infiltrate critical infrastructure networks.

### 7. Google Cloud Warns AMD Turin CPU Flaws Can Leak Data Across VM Processes
- **Source:** The Hacker News — https://thehackernews.com/2026/11/google-cloud-warns-three-amd-turin-cpu.html
- **Severity:** high
- **Tags:** `cloud-security`, `vulnerability`, `gcp`
- **Summary:** Three CPU side-channel flaws in AMD Turin processors could let code on the same core infer data from other processes or the kernel inside a Google Cloud VM.

### 8. N-central Zero-Days Under Active Exploitation as N-able Rushes Patches
- **Source:** SecurityWeek — https://www.securityweek.com/hackers-target-n-central-zero-days-as-n-able-rushes-patches/
- **Severity:** critical
- **Tags:** `zero-day`, `rce`, `vulnerability`
- **Summary:** Attackers began targeting N-able's N-central shortly after a researcher dropped 30+ zero-days; new exploits reportedly still work against patched servers with the Legacy API exposed, enabling root RCE / Windows SYSTEM access.

### 9. Google Session Hijacking Campaign Uses Calendar Invites and Live Proxies
- **Source:** The Hacker News — https://thehackernews.com/2026/11/calendar-invites-and-live-proxies.html
- **Severity:** high
- **Tags:** `phishing`, `google`
- **Summary:** A phishing operation dubbed Operation CloudFire has been stealing live Google sessions from corporate users since mid-August 2026 using calendar invites and live proxy infrastructure that evades standard link-reputation checks.

### 10. Critical RCE Flaw Patched in PTC Windchill and FlexPLM
- **Source:** The Hacker News — https://thehackernews.com/2026/11/ptc-patches-critical-windchill-and.html
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `rce`
- **Summary:** PTC patched CVE-2026-126325 (CVSS v4 9.2) in Windchill and FlexPLM, an improper input validation / insecure deserialization flaw that could enable remote code execution.

### 11. AI-Generated Scripts Enabled Rapid Lateral Movement in Retailer Breach
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/inside-ai-attack-us-retailer
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `privilege-escalation`
- **Summary:** An attacker switched to AI-generated scripts after hand-typed commands failed to breach a US retailer, then used them to achieve lateral movement within minutes.

### 12. ScreenConnect Rogue Clients Hit 288 Endpoints Across 48 Organizations
- **Source:** The Hacker News — https://thehackernews.com/2026/11/screenconnect-attacks-target-at-least.html
- **Severity:** high
- **Tags:** `malware`, `vulnerability`
- **Summary:** ConnectWise disabled five third-party ScreenConnect extensions after rogue clients deployed malware across 288 endpoints in 48 organizations; attackers exploited a flaw in one extension to bypass ScreenConnect authentication.

### 13. Inside a Cloud Pentest: Trust Boundaries Across Cloud Layers
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/how-a-cloud-pentest-works/121921/
- **Severity:** informational
- **Tags:** `cloud-security`, `appsec`, `devsecops`
- **Summary:** First in a Kaspersky GReAT series on cloud pentesting, covering the External/Overlay/Underlay layer model, common architectures like OpenStack and Kubernetes, and typical attack chains.

### 14. Hackers Abuse GSocket for Persistent Access on Linux Servers
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-plant-gsocket-on-linux-servers-for-persistent-access/
- **Severity:** medium
- **Tags:** `malware`, `appsec`
- **Summary:** Multiple threat actors are abusing the legitimate open-source tool GSocket to maintain persistent access to Linux servers even after the vulnerabilities used for initial access are patched.

### 15. Critical Pre-Auth MongoDB Flaw Can Crash Servers During Failover
- **Source:** The Hacker News — https://thehackernews.com/2026/11/critical-pre-auth-mongodb-flaw-cve-2026.html
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`
- **Summary:** CVE-2026-118383 lets an unauthenticated attacker crash a MongoDB replica-set member with two requests, but only if that server is later elected primary while missing recent changes. Fixed versions are already out.

### 16. Critical Red Hat Quay Flaw Could Expose Private Container Images
- **Source:** SecurityWeek — https://www.securityweek.com/critical-red-hat-quay-vulnerability-could-expose-private-container-images/
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `container-security`
- **Summary:** A critical Red Hat Quay flaw could let attackers steal private container images, overwrite repositories, and maintain persistent access on self-hosted registries.

### 17. Maersk Confirms Data Theft Amid $5 Million Extortion Demand
- **Source:** SecurityWeek — https://www.securityweek.com/maersk-confirms-data-theft-amid-5-million-extortion-attempt/
- **Severity:** high
- **Tags:** `ransomware`, `data-breach`
- **Summary:** Maersk confirmed data theft after the WhiteArmor ransomware group claimed to have stolen 100GB of data and demanded $5 million.

### 18. Node.js Patches 16 Flaws Including HTTP/2 Crash and Data Leak Bugs
- **Source:** The Hacker News — https://thehackernews.com/2026/11/nodejs-fixes-16-flaws-including-http2.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Summary:** Node.js fixed 16 flaws including two HTTP/2 bugs: one lets unauthenticated clients crash servers, the other can leak memory from other connections. Fixed in 22.23.5, 24.22.3, and 26.13.1.

### 19. Critical Apache HTTP/2 Flaw Enables Unauthenticated Remote Code Execution
- **Source:** The Hacker News — https://thehackernews.com/2026/11/critical-apache-http2-flaw-could-let.html
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `rce`
- **Summary:** CVE-2026-119618 in Apache's mod_http2 module lets a remote, unauthenticated attacker execute code on servers with HTTP/2 enabled. Affects 2.4.55–2.4.70; fixed in 2.4.71.

## Skippable

- **Jensen Huang is out at Nvidia — who is Colette Kress, his interim replacement?** — TechCrunch AI. Business/personnel leadership change, no security angle.
- **Norwest pushes deeper into AI with new $4B fund** — TechCrunch AI. VC funding announcement, no security substance.
- **Your Endpoint Management Platform Could Be Your Biggest Security Risk** — BleepingComputer (Action1). Vendor-sponsored marketing content disguised as news.
- **Hijacked email accounts complicate investigations into European bomb hoaxes** — The Record. Regional incident without novel technique or IOCs.
- **The unfolding Jensen Huang scandal: a timeline** — TechCrunch AI. Personnel/business scandal, no security content.
- **I reviewed the Apple HomeView, ask me anything** — The Verge AI. Product review, not security or model news.
- **Nvidia CEO Jensen Huang resigns amid spy, affair scandals** — The Verge AI. Personnel scandal, no technical substance.
- **Chrome, Firefox Updates Patch Over 180 Vulnerabilities** — SecurityWeek. Routine browser patch cycle, no single critical actively-exploited CVE called out.
- **Romania says it stopped Russian cyberattack targeting government emails** — The Record. No IOCs or technical detail disclosed.
- **Nine Korean startups vie for a spot in Disrupt 2027's Startup Battlefield 200 competition** — TechCrunch AI. Startup competition announcement, no security/model substance.
- **Daylight Lands $80 Million for AI-Powered Security Operations** — SecurityWeek. Funding announcement, no technical substance.
- **Microsoft: Recent Windows updates cause SQL Server performance issues** — BleepingComputer. Performance bug, not a security vulnerability.
- **Webinar: See How Identity Blind Spots Put Your SOC at Risk and How to Close Them** — The Hacker News. Vendor webinar/marketing content.
- **Holiday Extras is rethinking what it can build with Codex** — OpenAI Blog. Customer marketing story, no launch or substance.
- **Microsoft confirms Windows security updates installation issues** — BleepingComputer. Installation bug, not an exploit or vulnerability.
- **Who could replace Jensen Huang? A highly unscientific list of possible successors** — TechCrunch AI. Speculative listicle, no security/AI substance.
