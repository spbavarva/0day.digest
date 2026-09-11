# Digest — 2026-09-11 AM

- Window: last 14h
- Raw items considered: 19
- Relevant: 12 (11 draft posts — PaperCut items merged into one)
- Skippable: 7

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors — `2026-09-11-jfrog-artifactory-flaws-admin-backdoors.md`
- [x] **[CRITICAL]** Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware — `2026-09-11-cisco-fmc-auth-bypass-qilin-ransomware-cve-2026-20079.md`
- [x] **[HIGH]** GitLab Patches Max-Severity Path Traversal Flaw (CVE-2026-85706) — `2026-09-11-gitlab-max-severity-path-traversal-cve-2026-85706.md`
- [x] **[HIGH]** Check Point Patches Critical VPN Vulnerabilities — `2026-09-11-check-point-critical-vpn-vulnerabilities-rce.md`
- [x] **[HIGH]** Anthropic Says Russian Hackers Used Claude to Automate Malware Evasion — `2026-09-11-anthropic-russian-hackers-claude-malware-evasion.md`
- [x] **[HIGH]** PaperCut Flaws Exploited in AI-Powered Attacks — `2026-09-11-papercut-flaws-ai-powered-attacks-patched.md`
- [x] **[HIGH]** Trezor: 347,000 Users Targeted in Phishing After Brevo Breach — `2026-09-11-trezor-phishing-brevo-breach-347k-targeted.md`
- [x] **[HIGH]** China-Linked UNC3569 Exploited Sogou Input Method Flaw to Deploy GRAYRABBIT — `2026-09-11-unc3569-sogou-input-method-grayrabbit-backdoor.md`
- [x] **[HIGH]** Indonesia Hit by Android Banking App-Cloning Campaign — `2026-09-11-indonesia-android-banking-app-cloning-goldfactory.md`
- [x] **[MEDIUM]** Surfshark Systems Targeted by Hackers — `2026-09-11-surfshark-test-server-breach.md`
- [x] **[MEDIUM]** Datasette 1.0a39 and 0.65.4 Security Releases — `2026-09-11-datasette-security-releases-1-0a39-0-65-4.md`

## Relevant (details)

### 1. Attackers Chain JFrog Artifactory Flaws to Gain Admin Control and Plant Backdoors
- **Source:** The Hacker News — https://thehackernews.com/2026/09/attackers-chain-jfrog-artifactory-flaws.html
- **Severity:** critical
- **Tags:** `supply-chain`, `rce`, `privilege-escalation`, `wiz`
- **Summary:** Attackers chained two flaws in JFrog Artifactory to gain admin control of self-hosted servers and plant backdoors; Wiz observed active exploitation between Aug 15–Sep 8, a supply chain risk for consumers of served artifacts.

### 2. Cisco FMC Flaws Exploited to Steal Credentials and Deploy Qilin Ransomware
- **Source:** The Hacker News — https://thehackernews.com/2026/09/cisco-fmc-flaws-exploited-to-steal.html
- **Severity:** critical
- **Tags:** `ransomware`, `vulnerability`, `cve`, `privilege-escalation`
- **Summary:** Three distinct threat clusters, including ransomware operators and state-sponsored groups, are exploiting CVE-2026-20079 (CVSS 10.0), an unauthenticated auth bypass in Cisco Secure FMC, to steal credentials and deploy Qilin ransomware.

### 3. GitLab Patches Max-Severity Path Traversal Flaw (CVE-2026-85706)
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/gitlab-urges-users-to-patch-max-severity-path-traversal-flaw/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`, `gitlab`
- **Summary:** GitLab urged self-managed instance admins to patch immediately against CVE-2026-85706, a maximum-severity path traversal flaw. No confirmed in-the-wild exploitation reported yet.

### 4. Check Point Patches Critical VPN Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/check-point-patches-critical-vpn-vulnerabilities/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Summary:** Check Point patched two critical VPN vulnerabilities, CVE-2026-85102 and CVE-2026-85103, that could be exploited for remote code execution.

### 5. Anthropic Says Russian Hackers Used Claude to Automate Malware Evasion
- **Source:** SecurityWeek — https://www.securityweek.com/anthropic-says-russian-hackers-used-claude-ai-to-automate-malware-evasion/
- **Severity:** high
- **Tags:** `anthropic`, `llm`, `ai-safety`, `malware`
- **Summary:** Anthropic disclosed a Russian-linked criminal group used Claude to automate malware evasion techniques, part of a broader pattern of actors targeting AI vendors' own infrastructure, including an attempt to steal a pre-release Claude model.

### 6. PaperCut Flaws Exploited in AI-Powered Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/papercut-flaws-exploited-in-ai-powered-attacks/ (merged with The Hacker News coverage)
- **Severity:** high
- **Tags:** `vulnerability`, `rce`, `malware`, `llm`
- **Summary:** A Russian threat actor used AI tooling to build, test, and deploy exploits against PaperCut across hundreds of orgs. PaperCut has since shipped maintenance releases replacing earlier emergency patches for the actively exploited flaws.

### 7. Trezor: 347,000 Users Targeted in Phishing After Brevo Breach
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/trezor-347-000-users-targeted-in-phishing-attacks-after-brevo-breach/
- **Severity:** high
- **Tags:** `phishing`, `data-breach`
- **Summary:** Phishing attacks stemming from a breach at email vendor Brevo targeted roughly 347,000 Trezor customer email addresses; about 2,500 users clicked the embedded malicious link.

### 8. China-Linked UNC3569 Exploited Sogou Input Method Flaw to Deploy GRAYRABBIT
- **Source:** The Hacker News — https://thehackernews.com/2026/09/china-linked-unc3569-exploited-sogou.html
- **Severity:** high
- **Tags:** `malware`, `privilege-escalation`
- **Summary:** China-linked UNC3569 exploited a flaw in Sogou Input Method, a widely used Chinese-character typing tool, to deploy the GRAYRABBIT backdoor via a crafted link.

### 9. Indonesia Hit by Android Banking App-Cloning Campaign
- **Source:** Dark Reading — https://www.darkreading.com/mobile-security/indonesia-android-banking-app-cloning-campaign
- **Severity:** high
- **Tags:** `malware`
- **Summary:** The GoldFactory group is abusing the Android Work Profile feature to deliver the Gigabud banking trojan via cloned banking apps in Indonesia; a separate group, Mantax Otax, runs a similar campaign.

### 10. Surfshark Systems Targeted by Hackers
- **Source:** SecurityWeek — https://www.securityweek.com/surfshark-systems-targeted-by-hackers/
- **Severity:** medium
- **Tags:** `data-breach`, `cloud-security`
- **Summary:** A misconfigured Surfshark test server containing internal engineering material and configuration data was accessed by threat actors. No customer credential or VPN traffic data was reported affected.

### 11. Datasette 1.0a39 and 0.65.4 Security Releases
- **Source:** Simon Willison — https://simonwillison.net/2026/Sep/11/datasette-security/
- **Severity:** medium
- **Tags:** `appsec`, `vulnerability`
- **Summary:** Datasette shipped security patches (1.0a39, 0.65.4) fixing issues that could expose private tables on instances mixing public and private data.

## Skippable

- **[Virtual Event] What Every Enterprise Should Know About Securing Cloud Assets in the Age of AI** — Dark Reading. Event promo, no news value.
- **[Virtual Event] Building a Secure AI Strategy for the Enterprise** — Dark Reading. Event promo, no news value.
- **Ukrainian Conti Ransomware Developer Sentenced to 4 Years in US Prison** — SecurityWeek. Sentencing news without new TTPs/IOCs; duplicate of BleepingComputer's coverage below.
- **Kiteworks Acquires Bonfy.AI to Fill the AI Gap in Data Governance** — SecurityWeek. M&A/business news, no security substance.
- **Microsoft Fixes Teams, Outlook Launch Failures on ARM Windows PCs** — BleepingComputer. Bug fix, no security angle.
- **Conti Ransomware Gang Member Sentenced to 4 Years in Prison** — BleepingComputer. Duplicate coverage of the SecurityWeek sentencing item above.
- **Any Nix Package, Live in Your Browser** — Simon Willison. Interesting dev tooling, no security angle.
