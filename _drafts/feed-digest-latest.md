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
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`, `appsec`
- **Summary:** A heap buffer overflow (CVE-2026-42945, CVSS v4: 9.2) in NGINX's `ngx_http_rewrite_module` has gone undetected for 18 years and enables unauthenticated RCE against NGINX Plus and Open Source. Any internet-facing deployment using rewrite rules is exposed; patch immediately.

### 2. Critical Exim Mail Server Flaw Allows Unauthenticated Remote Code Execution
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-critical-exim-mailer-flaw-allows-remote-code-execution/
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`
- **Summary:** A critical flaw in certain Exim configurations allows unauthenticated remote code execution. Exim is among the most widely deployed MTAs globally; operators should patch immediately or restrict inbound SMTP exposure.

### 3. Researcher Drops YellowKey BitLocker Bypass and GreenPlasma Windows EoP Zero-Days
- **Source:** SecurityWeek — https://www.securityweek.com/researcher-drops-yellowkey-greenplasma-windows-zero-days/
- **Severity:** high
- **Tags:** `zero-day`, `privilege-escalation`, `vulnerability`, `microsoft`
- **Summary:** Two unpatched Windows zero-days released at Pwn2Own Berlin: YellowKey (BitLocker bypass, physical access) and GreenPlasma (System EoP, remote-chainable). Microsoft has no patch available yet.

### 4. Fragnesia Linux Kernel LPE (CVE-2026-46300) Grants Root via Page Cache Corruption
- **Source:** The Hacker News — https://thehackernews.com/2026/05/new-fragnesia-linux-kernel-lpe-grants.html
- **Severity:** high
- **Tags:** `privilege-escalation`, `cve`, `vulnerability`
- **Summary:** CVE-2026-46300 (CVSS 7.8) is the third Linux kernel LPE in two weeks, exploiting page cache corruption in the XFRM subsystem. Distribution patches are shipping; multi-tenant and container hosts should prioritize.

### 5. High-Severity VMware Fusion Vulnerability Patched at Pwn2Own Berlin
- **Source:** SecurityWeek — https://www.securityweek.com/high-severity-vulnerability-patched-in-vmware-fusion/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Summary:** Broadcom patched a high-severity VMware Fusion flaw coinciding with Pwn2Own Berlin 2026. CVE details pending; macOS Fusion users should update immediately.

### 6. MuddyWater Broadens Cyber-Espionage Campaign Across Nine Organizations Globally
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/iranian-hackers-targeted-major-south-korean-electronics-maker/
- **Severity:** high
- **Tags:** `malware`, `apt`
- **Summary:** Iran-linked MuddyWater targeted at least nine high-profile organizations globally including a major South Korean electronics firm, abusing legitimate RMM tools for persistence. Defenders should audit RMM deployments and review current MuddyWater IOCs.

### 7. Attackers Weaponize RubyGems Packages as Data Dead Drops Targeting UK Government Servers
- **Source:** Dark Reading — https://www.darkreading.com/application-security/attackers-weaponize-rubygems-data-dead-drops
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `appsec`
- **Summary:** Malicious RubyGems packages with scrapers targeting UK government servers use the registry as a covert data dead drop. Objective and attribution are unclear; the technique extends abuse of open-source package registries as C2 infrastructure.

### 8. Gentlemen RaaS Gang's Internal Data Leaked After OPSEC Failure
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/gentlemen-raas-gang-data-leak
- **Severity:** medium
- **Tags:** `ransomware`
- **Summary:** An OPSEC failure exposed Gentlemen RaaS internals including its affiliate model, TTPs, and org structure. Threat intel teams should review leaked data for IOCs and affiliate profiling to support attribution.

### 9. AWS GuardDuty Guidance for Detecting and Preventing Cryptocurrency Mining
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/detecting-and-preventing-crypto-mining-in-your-aws-environment/
- **Severity:** informational
- **Tags:** `cloud-security`, `aws`, `cspm`
- **Summary:** AWS published GuardDuty-based guidance for detecting cryptomining in AWS environments, covering detection capabilities and multi-layered defense strategies. Verify GuardDuty is enabled across all regions and integrated into centralized alerting.

## Skippable

- **US charges suspected Dream Market admin arrested in Germany** — BleepingComputer. Law enforcement action, no technical detail or practitioner takeaway.
- **New Fragnesia Linux flaw lets attackers gain root privileges** — BleepingComputer. Duplicate of CVE-2026-46300 coverage; The Hacker News item selected instead.
- **Who decides what AI tells you? Campbell Brown** — TechCrunch AI. Opinion piece on AI content governance, no news value.
- **Clio's $500M milestone arrives just as Anthropic ups the ante** — TechCrunch AI. Legal tech SaaS business milestone, no security or model-release angle.
- **Welcome to the Datasette blog** — Simon Willison. Blog launch announcement, no security or AI model content.
- **West Pharmaceutical says hackers stole data, encrypted systems** — BleepingComputer. Ransomware victim disclosure without TTPs, IOCs, or technical detail.
- **Microsoft's Edge Copilot update uses AI to pull information from across your tabs** — The Verge AI. Generic AI product feature, no security implication.
- **Notion just turned its workspace into a hub for AI agents** — TechCrunch AI. Non-security SaaS productivity launch.
- **Checkbox Assessments Aren't Fit to Measure to Risk** — Dark Reading. Opinion piece on security governance methodology, no news value.
- **Alleged Dream Market admin arrested in Germany** — The Record. Duplicate of the BleepingComputer Dream Market story; both skipped.
- **Musk's xAI is running nearly 50 gas turbines unchecked at its Mississippi data center** — TechCrunch AI. Environmental/regulatory data center story, no security angle.
- **Anthropic's Cat Wu says that AI will anticipate your needs** — TechCrunch AI. Interview about future of AI proactivity, no news value.
