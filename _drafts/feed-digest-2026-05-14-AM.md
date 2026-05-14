# Digest — 2026-05-14 AM

- Window: last 14h
- Raw items considered: 21
- Relevant: 9
- Skippable: 12

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** 18-Year-Old NGINX Rewrite Module Bug Enables Unauthenticated RCE — `2026-05-14-nginx-rewrite-module-rce-cve-2026-42945.md`
- [x] **[CRITICAL]** Critical Exim Mail Server Flaw Allows Unauthenticated Remote Code Execution — `2026-05-14-exim-critical-rce-vulnerability.md`
- [x] **[HIGH]** Researcher Drops YellowKey BitLocker Bypass and GreenPlasma Windows EoP Zero-Days — `2026-05-14-yellowkey-greenplasma-windows-zero-days.md`
- [x] **[HIGH]** Fragnesia Linux Kernel LPE (CVE-2026-46300) Grants Root via Page Cache Corruption — `2026-05-14-fragnesia-linux-kernel-lpe-cve-2026-46300.md`
- [x] **[HIGH]** High-Severity VMware Fusion Vulnerability Patched at Pwn2Own Berlin — `2026-05-14-vmware-fusion-high-severity-vulnerability.md`
- [x] **[HIGH]** MuddyWater Broadens Cyber-Espionage Campaign Across Nine Organizations Globally — `2026-05-14-muddywater-south-korean-electronics-espionage.md`
- [x] **[HIGH]** Attackers Weaponize RubyGems Packages as Data Dead Drops Targeting UK Government Servers — `2026-05-14-rubygems-supply-chain-data-dead-drops.md`
- [x] **[MEDIUM]** Gentlemen RaaS Gang's Internal Data Leaked After OPSEC Failure — `2026-05-14-gentlemen-raas-gang-data-leak.md`
- [x] **[INFORMATIONAL]** AWS GuardDuty Guidance for Detecting and Preventing Cryptocurrency Mining — `2026-05-14-aws-guardduty-crypto-mining-detection.md`

## Relevant (details)

### 1. 18-Year-Old NGINX Rewrite Module Bug Enables Unauthenticated RCE
- **Source:** The Hacker News — https://thehackernews.com/2026/05/18-year-old-nginx-rewrite-module-flaw.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`, `appsec`
- **Slug:** `2026-05-14-nginx-rewrite-module-rce-cve-2026-42945`
- **Must-know:** no
- **Summary:** A heap buffer overflow (CVE-2026-42945, CVSS v4: 9.2) in NGINX's `ngx_http_rewrite_module` has gone undetected for 18 years and enables unauthenticated RCE against both NGINX Plus and NGINX Open Source. Any internet-facing deployment using rewrite rules is potentially exposed and should be patched immediately.

### 2. Critical Exim Mail Server Flaw Allows Unauthenticated Remote Code Execution
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-critical-exim-mailer-flaw-allows-remote-code-execution/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `2026-05-14-exim-critical-rce-vulnerability`
- **Must-know:** no
- **Summary:** A critical flaw in certain Exim configurations allows an unauthenticated remote attacker to execute arbitrary code on the mail server. Exim is among the most widely deployed MTAs globally, elevating urgency for all operators running Exim.

### 3. Researcher Drops YellowKey BitLocker Bypass and GreenPlasma Windows EoP Zero-Days
- **Source:** SecurityWeek — https://www.securityweek.com/researcher-drops-yellowkey-greenplasma-windows-zero-days/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `privilege-escalation`, `vulnerability`, `microsoft`
- **Slug:** `2026-05-14-yellowkey-greenplasma-windows-zero-days`
- **Must-know:** no
- **Summary:** Two unpatched Windows zero-days were publicly released at Pwn2Own Berlin: YellowKey (BitLocker bypass, physical access required) and GreenPlasma (System-level EoP, no physical access required). GreenPlasma is immediately chainable with any remote initial access vector; Microsoft has not yet issued patches.

### 4. Fragnesia Linux Kernel LPE (CVE-2026-46300) Grants Root via Page Cache Corruption
- **Source:** The Hacker News — https://thehackernews.com/2026/05/new-fragnesia-linux-kernel-lpe-grants.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `privilege-escalation`, `cve`, `vulnerability`
- **Slug:** `2026-05-14-fragnesia-linux-kernel-lpe-cve-2026-46300`
- **Must-know:** no
- **Summary:** CVE-2026-46300 (CVSS 7.8), dubbed Fragnesia, is the third Linux kernel LPE discovered in two weeks, exploiting page cache corruption in the XFRM subsystem to gain root. Distribution patches are shipping; multi-tenant hosts and container environments should prioritize this update.

### 5. High-Severity VMware Fusion Vulnerability Patched at Pwn2Own Berlin
- **Source:** SecurityWeek — https://www.securityweek.com/high-severity-vulnerability-patched-in-vmware-fusion/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Slug:** `2026-05-14-vmware-fusion-high-severity-vulnerability`
- **Must-know:** no
- **Summary:** Broadcom patched a high-severity VMware Fusion vulnerability coinciding with Pwn2Own Berlin 2026, suggesting competition-related discovery. Full CVE details are pending; macOS users running VMware Fusion should update immediately.

### 6. MuddyWater Broadens Cyber-Espionage Campaign Across Nine Organizations Globally
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/iranian-hackers-targeted-major-south-korean-electronics-maker/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `apt`
- **Slug:** `2026-05-14-muddywater-south-korean-electronics-espionage`
- **Must-know:** no
- **Summary:** Iran-linked MuddyWater (Seedworm/Static Kitten) has targeted at least nine high-profile organizations globally, including a major South Korean electronics manufacturer, in a broad espionage campaign. The group typically abuses legitimate remote management tools (Atera, ScreenConnect) for persistence; defenders should audit RMM tool usage and review current MuddyWater IOCs.

### 7. Attackers Weaponize RubyGems Packages as Data Dead Drops Targeting UK Government Servers
- **Source:** Dark Reading — https://www.darkreading.com/application-security/attackers-weaponize-rubygems-data-dead-drops
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `appsec`
- **Slug:** `2026-05-14-rubygems-supply-chain-data-dead-drops`
- **Must-know:** no
- **Summary:** Malicious RubyGems packages containing scrapers targeting UK government servers have been identified, using the package registry as a covert data dead drop. The technique extends a pattern of abusing open-source registries as C2 and exfiltration infrastructure; objective and attribution remain unclear.

### 8. Gentlemen RaaS Gang's Internal Data Leaked After OPSEC Failure
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/gentlemen-raas-gang-data-leak
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ransomware`
- **Slug:** `2026-05-14-gentlemen-raas-gang-data-leak`
- **Must-know:** no
- **Summary:** An OPSEC failure has exposed internal data from the Gentlemen RaaS group, revealing its affiliate model, TTPs, and organizational structure. Threat intelligence teams should mine the leaked data for IOCs and affiliate profiling to support attribution and detection of future campaigns.

### 9. AWS GuardDuty Guidance for Detecting and Preventing Cryptocurrency Mining
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/detecting-and-preventing-crypto-mining-in-your-aws-environment/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `cloud-security`, `aws`, `cspm`
- **Slug:** `2026-05-14-aws-guardduty-crypto-mining-detection`
- **Must-know:** no
- **Summary:** AWS published guidance on using GuardDuty to detect and prevent cryptomining in AWS environments, covering specialized detection capabilities and multi-layered defense strategies. Cryptomining is a common post-compromise objective in cloud environments compromised via misconfigured credentials or IAM keys.

## Skippable

- **US charges suspected Dream Market admin arrested in Germany** — BleepingComputer. Law enforcement action against a dark web marketplace admin; no technical attack detail or security practitioner takeaway.
- **New Fragnesia Linux flaw lets attackers gain root privileges** — BleepingComputer. Duplicate coverage of CVE-2026-46300; The Hacker News item (item 5) has more technical detail and was selected instead.
- **Who decides what AI tells you? Campbell Brown** — TechCrunch AI. Opinion/commentary piece about AI content governance; no news value.
- **Clio's $500M milestone arrives just as Anthropic ups the ante** — TechCrunch AI. Business milestone story for a legal tech SaaS company; no security or AI model angle.
- **Welcome to the Datasette blog** — Simon Willison. Blog launch announcement with no security or AI model content.
- **West Pharmaceutical says hackers stole data, encrypted systems** — BleepingComputer. Ransomware victim disclosure with no TTPs, IOCs, or technical detail beyond the fact of encryption and exfiltration.
- **Microsoft's Edge Copilot update uses AI to pull information from across your tabs** — The Verge AI. Generic AI product feature update; no security implication.
- **Notion just turned its workspace into a hub for AI agents** — TechCrunch AI. Non-security SaaS productivity feature launch.
- **Checkbox Assessments Aren't Fit to Measure to Risk** — Dark Reading. Opinion piece on security governance methodology; no news value.
- **Alleged Dream Market admin arrested in Germany after US indictment** — The Record (Recorded Future). Duplicate of the BleepingComputer Dream Market story; both skipped for the same reason.
- **Musk's xAI is running nearly 50 gas turbines unchecked at its Mississippi data center** — TechCrunch AI. Environmental/regulatory story about data center power; no security angle.
- **Anthropic's Cat Wu says that AI will anticipate your needs before you know what they are** — TechCrunch AI. Interview/opinion about the future of AI proactivity; no news value.
