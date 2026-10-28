# Digest — 2026-10-28 PM

- Window: last 14h
- Raw items considered: 26
- Relevant: 12
- Skippable: 14

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** CISA Confirms Active Exploitation of Brotli "Node2Shell" Flaw, Hundreds of Adobe Commerce Stores Breached — `2026-10-28-node2shell-brotli-exploited-adobe-commerce-breach.md`
- [x] **[CRITICAL]** ShinyHunters-Exploited Oracle PeopleSoft Zero-Day Turns Out to Be Three Chained Flaws — `2026-10-28-shinyhunters-oracle-peoplesoft-ssrf-chain.md`
- [x] **[HIGH]** TLS Flaws Found in GoAhead Web Server Used in Hundreds of Millions of Devices — `2026-10-28-tls-flaws-goahead-web-server.md`
- [x] **[HIGH]** China-Linked Hackers Exploit PHP2Shell to Root Firewalls — `2026-10-28-china-linked-php2shell-firewalls.md`
- [x] **[HIGH]** Adobe Fixes 8 Critical Campaign Classic Flaws Allowing Code Execution and Security Bypass — `2026-10-28-adobe-campaign-classic-critical-flaws.md`
- [x] **[HIGH]** Hackers Start Probing Fresh Oracle EBS Vulnerability — `2026-10-28-oracle-ebs-sql-injection-probing.md`
- [x] **[HIGH]** Anthropic's Unreleased AI Model Chains Flaws Into Working Browser and OS Exploits — `2026-10-28-anthropic-unreleased-model-chrome-safari-exploits.md`
- [x] **[HIGH]** Tailscale Patches SSH Flaws That Could Let Hacked Devices Gain Root Access on Other Servers — `2026-10-28-tailscale-ssh-flaws-root-access.md`
- [x] **[MEDIUM]** Long-Hidden Flaws Patched in EPICS Research Facility Control Software — `2026-10-28-epics-research-facility-control-flaws.md`
- [x] **[MEDIUM]** American Organizations Under Attack: Skyw4lker Device Code Phishing Campaign Exposed — `2026-10-28-skyw4lker-device-code-phishing-campaign.md`
- [x] **[MEDIUM]** Millions of Security Cameras at Risk: DoS Vulnerability in Intelbras Devices — `2026-10-28-intelbras-camera-dos-vulnerability.md`
- [x] **[INFORMATIONAL]** Introducing Route 53 Resolved IP Validation for AWS Network Firewall — `2026-10-27-aws-network-firewall-route53-resolved-ip-validation.md`

## Relevant (details)

### 1. CISA Confirms Active Exploitation of Brotli "Node2Shell" Flaw, Hundreds of Adobe Commerce Stores Breached
- **Source:** BleepingComputer, SecurityWeek, The Hacker News (merged — same story, three angles)
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `rce`, `cve`, `data-breach`
- **Slug:** `node2shell-brotli-exploited-adobe-commerce-breach`
- **Must-know:** yes
- **Summary:** CISA added a critical, actively-exploited flaw in Google's Brotli decompression library (dubbed Node2Shell) to its KEV catalog, and a related Adobe Commerce/Magento flaw (CVE-2026-111497, CVSS 9.2) chained in "PolyShell" attacks that have breached hundreds of stores. Honeypots have logged live exploitation attempts.

### 2. ShinyHunters-Exploited Oracle PeopleSoft Zero-Day Turns Out to Be Three Chained Flaws
- **Source:** The Hacker News — https://thehackernews.com/2026/10/shinyhunters-exploited-oracle.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `ssrf`, `zero-day`, `cve`, `privilege-escalation`
- **Slug:** `shinyhunters-oracle-peoplesoft-ssrf-chain`
- **Must-know:** yes
- **Summary:** The critical Oracle PeopleSoft bug ShinyHunters has exploited since May turns out to be three flaws chained together, rooted in an SSRF that reaches an internal management interface because PeopleSoft trusts its own loopback address. Oracle patched all three under CVE-2026-35273 in June.

### 3. TLS Flaws Found in GoAhead Web Server Used in Hundreds of Millions of Devices
- **Source:** SecurityWeek — https://www.securityweek.com/tls-flaws-found-in-goahead-web-server-used-in-hundreds-of-millions-of-devices/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`
- **Slug:** `tls-flaws-goahead-web-server`
- **Must-know:** no
- **Summary:** FoxIO disclosed three TLS bugs in the GoAhead embedded web server, which ships in hundreds of millions of devices, that can let revoked certificates be accepted as valid or expose parts of encrypted sessions to eavesdropping.

### 4. China-Linked Hackers Exploit PHP2Shell to Root Firewalls
- **Source:** SecurityWeek — https://www.securityweek.com/china-linked-hackers-exploit-php2shell-to-root-firewalls/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `privilege-escalation`
- **Slug:** `china-linked-php2shell-firewalls`
- **Must-know:** no
- **Summary:** China-linked attackers chained the PHP2Shell and Fragnesia exploits to gain root access on firewall appliances, compromising two servers belonging to a US government-affiliated organization.

### 5. Adobe Fixes 8 Critical Campaign Classic Flaws Allowing Code Execution and Security Bypass
- **Source:** The Hacker News — https://thehackernews.com/2026/10/adobe-fixes-8-critical-campaign-classic.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `cve`, `vulnerability`, `privilege-escalation`
- **Slug:** `adobe-campaign-classic-critical-flaws`
- **Must-know:** no
- **Summary:** Adobe patched eight critical Campaign Classic flaws enabling code execution, security bypass, and privilege escalation; the worst, CVE-2026-104351, is a CVSS 9.9 code injection bug. No active exploitation has been reported.

### 6. Hackers Start Probing Fresh Oracle EBS Vulnerability
- **Source:** SecurityWeek, BleepingComputer (merged — same story)
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `sqli`, `rce`, `cve`, `vulnerability`
- **Slug:** `oracle-ebs-sql-injection-probing`
- **Must-know:** no
- **Summary:** CVE-2026-101767, an unauthenticated SQL injection flaw in Oracle E-Business Suite exploitable for RCE, is now being actively scanned for across the internet by attackers, per BleepingComputer.

### 7. Anthropic's Unreleased AI Model Chains Flaws Into Working Browser and OS Exploits
- **Source:** The Hacker News — https://thehackernews.com/2026/10/anthropics-unreleased-ai-model-chains.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ai-safety`, `anthropic`, `llm`, `vulnerability`
- **Slug:** `anthropic-unreleased-model-chrome-safari-exploits`
- **Must-know:** no
- **Summary:** An unreleased Anthropic AI model found flaws in Chrome, Safari, Android, Windows, and Linux and chained them into working PoC exploits in a lab setting. Anthropic reported every flaw to vendors first; all are already patched.

### 8. Tailscale Patches SSH Flaws That Could Let Hacked Devices Gain Root Access on Other Servers
- **Source:** The Hacker News — https://thehackernews.com/2026/10/tailscale-patches-ssh-flaws-that-could.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`
- **Slug:** `tailscale-ssh-flaws-root-access`
- **Must-know:** no
- **Summary:** Tailscale shipped v1.104.4 to fix flaws in how its built-in SSH server forwards connections (run with root privileges), which could let a compromised device reach root-only services and files on other servers.

### 9. Long-Hidden Flaws Patched in EPICS Research Facility Control Software
- **Source:** SecurityWeek — https://www.securityweek.com/long-hidden-flaws-patched-in-epics-research-facility-control-software/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`
- **Slug:** `epics-research-facility-control-flaws`
- **Must-know:** no
- **Summary:** Four long-hidden flaws in EPICS Base, control software used at particle accelerators and fusion labs, were found by an autonomous discovery system and could let an attacker crash control processes.

### 10. American Organizations Under Attack: Skyw4lker Device Code Phishing Campaign Exposed
- **Source:** The Hacker News — https://thehackernews.com/2026/10/american-organizations-under-attack.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`
- **Slug:** `skyw4lker-device-code-phishing-campaign`
- **Must-know:** no
- **Summary:** ANY.RUN detailed Skyw4lker, a device code phishing campaign targeting US organizations that abuses legitimate cloud services and auth workflows to gain account access without traditional credential theft.

### 11. Millions of Security Cameras at Risk: DoS Vulnerability in Intelbras Devices
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/intelbras-camera-vulnerability/121131/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `vulnerability`
- **Slug:** `intelbras-camera-dos-vulnerability`
- **Must-know:** no
- **Summary:** Kaspersky GReAT found a denial-of-service vulnerability affecting Intelbras IP camera systems built on a popular Chinese manufacturer's platform, potentially affecting millions of deployed devices.

### 12. Introducing Route 53 Resolved IP Validation for AWS Network Firewall
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/introducing-route-53-resolved-ip-validation-for-aws-network-firewall/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `aws`, `cloud-security`
- **Slug:** `aws-network-firewall-route53-resolved-ip-validation`
- **Must-know:** no
- **Summary:** AWS added a feature that cross-checks the domain name a client presents in HTTP/HTTPS requests against what Route 53 actually resolves it to, closing a gap where clients could spoof the name to bypass AWS Network Firewall domain-based rules.

## Skippable

- **7 days until TechCrunch Founder Summit** — TechCrunch AI. Conference ad / recruitment content, no news value.
- **Hackers now scanning systems for recently-patched Oracle flaw** — BleepingComputer. Duplicate of the Oracle EBS probing story; SecurityWeek's version with the CVE number was used instead.
- **FBI seizes 'bulletproof' hosting site accused of facilitating child abuse, money laundering** — The Record. Law enforcement seizure, no technical security substance; duplicate of the Hacker News Virtualine item below.
- **CISA warns of hackers now exploiting critical Node2Shell flaw** — BleepingComputer. Duplicate coverage of the Node2Shell/Brotli story, folded into the merged post.
- **Nobody Trusts the Security Questionnaire. We Rely on It Anyway.** — SecurityWeek. Opinion piece, no news value.
- **Quoting Terk Terkowitz** — Simon Willison. Commentary quote, not a news item.
- **Secrets Management Firm Infisical Valued at $600 Million After $40 Million Raise** — SecurityWeek. Funding/business news, no technical security substance.
- **Nefilim and Hive ransomware affiliate gets 70 months in prison** — BleepingComputer. Sentencing disclosure, no new TTPs or IOCs.
- **Legora is building the agentic operating system for legal work** — OpenAI Blog. Customer case study / marketing content, not a model launch.
- **CISA Warns of Node2Shell Exploitation as Honeypots Log Attack Attempts** — SecurityWeek. Duplicate coverage of the Node2Shell/Brotli story, folded into the merged post.
- **FBI Seizes Virtualine Domain Over Alleged Criminal Hosting and Bitcoin Money Laundering** — The Hacker News. Law enforcement seizure, no technical security substance; duplicate of The Record item above.
- **Japan's GMO Offers $1 Million Bounty to Catch Hackers Behind FX Trading Cloud Breach** — The Hacker News. Breach disclosure without technical detail on how the breach occurred.
- **Third Serengeti Sweep Tops 1,400 Arrests as Investigations Mature** — Dark Reading. Law enforcement arrests roundup, no technical substance.
- **VCs will make billions on Anthropic's IPO, but Amazon is set to make much (much) more** — TechCrunch AI. Business/finance story, not an AI launch or safety item.
