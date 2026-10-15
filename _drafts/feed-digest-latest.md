# Digest — 2026-10-15 PM

- Window: last 14h
- Raw items considered: 26
- Relevant: 12
- Skippable: 14

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** GhostAction Supply Chain Campaign Compromises 1,900 GitHub Accounts, Targets 30,000+ Repos — `2026-10-15-ghostaction-github-supply-chain-compromise.md`
- [x] **[CRITICAL]** Palo Alto Networks Patches PAN-OS Zero-Day RCE Under Active Exploitation — `2026-10-15-palo-alto-pan-os-rce-active-exploitation.md`
- [x] **[HIGH]** Drupal Patches Critical Core RCE Flaw with No-Login Exploit Path — `2026-10-15-drupal-critical-core-rce-field-ui.md`
- [x] **[HIGH]** Novel Android RAT 'Hirudo' Replaces Banking Apps With Trojanized Copies — `2026-10-15-hirudo-android-rat-banking-trojan.md`
- [x] **[HIGH]** CenterPoint Energy Data Breach Impacts 1 Million Texans — `2026-10-15-centerpoint-energy-data-breach.md`
- [x] **[HIGH]** Langflow Critical Authenticated RCE Flaw Targeted in 1,400+ Honeypot Exploit Attempts — `2026-10-15-langflow-critical-rce-honeypot-exploitation.md`
- [x] **[HIGH]** AhsayCBS Flaws Exploited to Deploy Web Shells Get New Fixes After Incomplete Patches — `2026-10-15-ahsaycbs-web-shell-exploitation.md`
- [x] **[HIGH]** Cisco Warns of Exploited Secure Email Gateway Vulnerability — `2026-10-15-cisco-secure-email-gateway-vulnerability.md`
- [x] **[MEDIUM]** Fake AI Product Campaigns Used to Spread Malware Across US Companies — `2026-10-15-fake-ai-attacks-spread-across-us-companies.md`
- [x] **[MEDIUM]** CikaBika Bot RAT Uses Discord for Command and Control — `2026-10-15-cikabika-bot-rat-discord-cc.md`
- [x] **[MEDIUM]** Unpatched Fridge Firmware Costs EU Grocers Millions — `2026-10-15-eu-grocers-fridge-firmware-ot-security.md`
- [x] **[INFORMATIONAL]** Figma Announces New Features to Define How Agents Work on Its Platform — `2026-10-15-figma-agent-platform-features.md`

## Relevant (details)

### 1. GhostAction Supply Chain Campaign Compromises 1,900 GitHub Accounts, Targets 30,000+ Repos
- **Source:** The Hacker News — https://thehackernews.com/2026/10/ghostaction-compromises-about-1900.html
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `data-breach`
- **Summary:** The GhostAction credential-theft campaign now targets over 30,000 repositories across ~3,000 GitHub users, traced to roughly 1,900 compromised accounts. Attackers attempted to extract 3,174 secrets from public repos' CI pipelines during a spike on October 8-9, 2026.

### 2. Palo Alto Networks Patches PAN-OS Zero-Day RCE Under Active Exploitation
- **Source:** The Hacker News — https://thehackernews.com/2026/10/palo-alto-networks-patches-pan-os.html
- **Severity:** critical
- **Tags:** `cve`, `rce`, `zero-day`, `vulnerability`
- **Summary:** Palo Alto Networks patched CVE-2026-0322 (CVSS 8.6), an RCE flaw in the PAN-OS management interface that has been actively exploited against customer firewalls. Three outlets covered the same zero-day; the Hacker News item had the most technical detail.

### 3. Drupal Patches Critical Core RCE Flaw with No-Login Exploit Path
- **Source:** The Hacker News — https://thehackernews.com/2026/10/drupal-patches-critical-core-rce-flaw.html
- **Severity:** high
- **Tags:** `cve`, `rce`, `vulnerability`
- **Summary:** Drupal fixed a critical RCE in the Field UI module (11.4.10 / 11.3.19 / 10.6.19). Core alone isn't reachable, but contributed-module exploit paths exist, including at least one requiring no login.

### 4. Novel Android RAT 'Hirudo' Replaces Banking Apps With Trojanized Copies
- **Source:** SecurityWeek — https://www.securityweek.com/novel-android-banking-rat-hirudo-replaces-banking-apps-with-trojanized-copies/
- **Severity:** high
- **Tags:** `malware`
- **Summary:** Hirudo is a new Android RAT/banking-trojan hybrid that replaces legitimate banking apps with trojanized copies, giving attackers persistent access to victims' financial accounts.

### 5. CenterPoint Energy Data Breach Impacts 1 Million Texans
- **Source:** SecurityWeek — https://www.securityweek.com/centerpoint-energy-data-breach-impacts-1-million-texans/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** CenterPoint Energy disclosed a breach affecting roughly 1 million Texas customers, exposing names, addresses, SSNs, and driver's license numbers.

### 6. Langflow Critical Authenticated RCE Flaw Targeted in 1,400+ Honeypot Exploit Attempts
- **Source:** The Hacker News — https://thehackernews.com/2026/10/langflows-critical-authenticated-rce.html
- **Severity:** high
- **Tags:** `cve`, `rce`, `llm`, `vulnerability`
- **Summary:** CVE-2026-105740 (CVSS 9.9), a critical authenticated RCE in the open-source AI agent platform Langflow, is being actively probed — 1,423 honeypot exploit attempts recorded by Previdian.

### 7. AhsayCBS Flaws Exploited to Deploy Web Shells Get New Fixes After Incomplete Patches
- **Source:** The Hacker News — https://thehackernews.com/2026/10/ahsaycbs-flaws-exploited-to-deploy-web.html
- **Severity:** high
- **Tags:** `cve`, `rce`, `vulnerability`, `malware`
- **Summary:** Ahsay Backup reissued fixes for CVE-2026-105133 and CVE-2026-105134 after earlier patches were incomplete; the chained flaws bypass auth and have been used to deploy web shells and XMRig miners.

### 8. Cisco Warns of Exploited Secure Email Gateway Vulnerability
- **Source:** SecurityWeek — https://www.securityweek.com/cisco-warns-of-exploited-secure-email-gateway-vulnerability/
- **Severity:** high
- **Tags:** `cve`, `rce`, `vulnerability`
- **Summary:** Cisco warned of an actively exploited Secure Email Gateway flaw allowing unauthenticated attackers to write arbitrary files and execute commands as root. No CVE ID was given in the feed summary.

### 9. Fake AI Product Campaigns Used to Spread Malware Across US Companies
- **Source:** The Hacker News — https://thehackernews.com/2026/10/fake-ai-attacks-spread-across-us.html
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Summary:** ANY.RUN tied 1,258 sandbox analyses to campaigns impersonating AI products to spread malware and steal browser sessions; US orgs were 16% of country-attributed targets.

### 10. CikaBika Bot RAT Uses Discord for Command and Control
- **Source:** SecurityWeek — https://www.securityweek.com/cikabika-bot-rat-uses-discord-for-cc/
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Summary:** A new RAT, CikaBika, is delivered via phishing and uses Discord for C2, providing recon, remote execution, and exfiltration capabilities.

### 11. Unpatched Fridge Firmware Costs EU Grocers Millions
- **Source:** Dark Reading — https://www.darkreading.com/ics-ot-security/eu-grocers-unpatched-fridge-firmware
- **Severity:** medium
- **Tags:** `vulnerability`, `ics`
- **Summary:** Hundreds of EU grocery stores lost millions of dollars after third-party-managed, outdated OT firmware in their cooling systems failed — an OT patch-management cautionary tale.

### 12. Figma Announces New Features to Define How Agents Work on Its Platform
- **Source:** TechCrunch AI — https://techcrunch.com/2026/10/14/figma-announces-new-features-to-define-how-agents-work-on-its-platform/
- **Severity:** informational
- **Tags:** `ai-launch`
- **Summary:** Figma announced features for defining how AI agents operate on its design platform, alongside an open beta of its code layers feature. No security detail was reported.

## Skippable

- **Amazon's always-listening Bee wearable can now help you buy stuff** — The Verge AI. Consumer AI gadget announcement, no security angle.
- **Police arrests 95 suspects in international CSAM crackdown action** — BleepingComputer. Law enforcement action without technical security substance.
- **Why AI Confidence Is Not Validation** — The Hacker News. Opinion piece on AI governance, no concrete news event.
- **Your secrets aren't safe with this cute robot toy — they're on Chinese servers ready to be hacked** — The Verge AI. Consumer gadget privacy-concern piece, no disclosed vulnerability or CVE.
- **India Mandates Registered Caller Name Display on 4G and Newer Networks From November 1** — The Hacker News. Telecom regulation unrelated to core security/AI scope.
- **Microsoft fixes bug causing Windows black screens, Explorer crashes** — BleepingComputer. Bug fix, not a security vulnerability.
- **CISO Conversations: James Robinson – Many Jobs, One Journey to Netskope CISO** — SecurityWeek. Career/interview content.
- **UK Legal Aid Agency: Hackers stole records dating back to 1978** — BleepingComputer. Recap of a previously known April 2025 breach; no new technical detail or confirmed scale.
- **Palo Alto Networks Patches PAN-OS Zero-Day Exploited for Remote Code Execution** — SecurityWeek. Duplicate coverage of CVE-2026-0322, drafted via The Hacker News item.
- **Ricursive Intelligence is betting on AI-designed chips to help solve the compute crisis** — TechCrunch AI. Early-stage startup pitch, no concrete launch or benchmark data.
- **Gudea leverages AI to help organizations prevent social media crises before they erupt** — TechCrunch AI. Generic SaaS startup launch, marketing content.
- **Ukraine says Elon Musk's Starshield service partially restored after restrictions disrupted drone missions** — The Record (Recorded Future). Geopolitical/military comms story, outside technical security/AI scope.
- **Palo Alto Networks warns of PAN-OS RCE flaw exploited in attacks** — BleepingComputer. Duplicate coverage of CVE-2026-0322, drafted via The Hacker News item.
- **McKinsey is making job applicants spar with a fake AI client** — The Verge AI. HR/recruiting feature, no security substance.
