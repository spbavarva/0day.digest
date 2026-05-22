# Digest — 2026-05-22 AM

- Window: last 14h
- Raw items considered: 14
- Relevant: 9
- Skippable: 5

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Cisco Patches CVSS 10.0 Secure Workload REST API Flaw Allowing Unauthenticated Data Access — `2026-05-22-cisco-cvss-10-secure-workload-rce.md`
- [x] **[HIGH]** CISA Adds Actively Exploited Langflow and Trend Micro Apex One Flaws to KEV — `2026-05-22-cisa-kev-langflow-apex-one.md`
- [x] **[HIGH]** China's Webworm APT Abuses Discord and Microsoft Graph API to Target EU Governments — `2026-05-22-webworm-discord-ms-graph-eu-govts.md`
- [x] **[MEDIUM]** Cloud Atlas APT Returns With New Tools and Payloads Targeting Russian and Belarusian Government — `2026-05-22-cloud-atlas-apt-new-tools-2026.md`
- [x] **[MEDIUM]** Nation-State Actors Weaponize ROADtools Open-Source Framework for Cloud Intrusions — `2026-05-22-roadtools-nation-state-cloud-abuse.md`
- [x] **[MEDIUM]** Kimwolf DDoS Botnet Operator 'Dort' Arrested in Canada, Charged in US and Canada — `2026-05-22-kimwolf-botmaster-dort-arrested.md`
- [x] **[MEDIUM]** FBI Disrupts 'First VPN' Cybercrime Service Used by Dozens of Ransomware Groups — `2026-05-22-first-vpn-cybercrime-service-disrupted.md`
- [x] **[MEDIUM]** FTC Fines Cox Media Group $1M Over Deceptive AI 'Active Listening' Ad Targeting Service — `2026-05-22-ftc-active-listening-ai-enforcement.md`
- [x] **[INFORMATIONAL]** CISA Opens Nomination Form for Researchers to Submit Bugs to Known Exploited Vulnerabilities Catalog — `2026-05-22-cisa-kev-researcher-nominations.md`

## Relevant (details)

### 1. Cisco Patches CVSS 10.0 Secure Workload REST API Flaw Allowing Unauthenticated Data Access
- **Source:** The Hacker News — https://thehackernews.com/2026/05/cisco-patches-cvss-100-secure-workload.html
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `cisco`, `cloud-security`
- **Summary:** CVE-2026-20223 (CVSS 10.0) allows unauthenticated remote attackers to access sensitive data in Cisco Secure Workload via insufficient REST API validation. No active exploitation confirmed yet; immediate patching recommended.

### 2. CISA Adds Actively Exploited Langflow and Trend Micro Apex One Flaws to KEV
- **Source:** The Hacker News — https://thehackernews.com/2026/05/cisa-adds-exploited-langflow-and-trend.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `zero-day`, `rce`
- **Summary:** CVE-2025-34291 (Langflow, CVSS 9.4) and CVE-2026-34926 (Apex One directory traversal) both confirmed under active exploitation and added to KEV. Langflow's role in AI agent pipelines makes this especially notable for ML/LLM infrastructure operators.

### 3. China's Webworm APT Abuses Discord and Microsoft Graph API to Target EU Governments
- **Source:** Dark Reading — https://www.darkreading.com/endpoint-security/chinas-webworm-discord-microsoft-graphs
- **Severity:** high
- **Tags:** `apt`, `cloud-security`, `microsoft`, `malware`
- **Summary:** Chinese APT Webworm is using Discord and Microsoft Graph API as C2 channels against European government targets, supplemented by SoftEther VPN SOCKS proxies to blend intrusion traffic with legitimate cloud services.

### 4. Cloud Atlas APT Returns With New Tools and Payloads Targeting Russian and Belarusian Government
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/cloud-atlas-2026/119895/
- **Severity:** medium
- **Tags:** `apt`, `malware`, `vulnerability`
- **Summary:** Kaspersky GReAT documents updated Cloud Atlas activity through early 2026, including new tools and payloads targeting government and diplomatic entities in Russia and Belarus. Updated IOCs available in the report.

### 5. Nation-State Actors Weaponize ROADtools Open-Source Framework for Cloud Intrusions
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/
- **Severity:** medium
- **Tags:** `apt`, `cloud-security`, `azure`, `iam`
- **Summary:** Unit 42 details nation-state misuse of ROADtools (a legitimate Azure AD/Entra ID research tool) for offensive cloud reconnaissance, with detection guidance based on distinctive API call patterns in Entra ID audit logs.

### 6. Kimwolf DDoS Botnet Operator 'Dort' Arrested in Canada, Charged in US and Canada
- **Source:** Krebs on Security — https://krebsonsecurity.com/2026/05/alleged-kimwolf-botmaster-dort-arrested-charged-in-u-s-and-canada/
- **Severity:** medium
- **Tags:** `malware`, `botnet`, `ddos`
- **Summary:** Jacob Butler (aka "Dort"), 23, of Ottawa arrested for running the Kimwolf AISURU-variant botnet (~2M devices), used for DDoS-for-hire. Krebs had publicly identified him in February 2026 after retaliatory attacks against the publication.

### 7. FBI Disrupts 'First VPN' Cybercrime Service Used by Dozens of Ransomware Groups
- **Source:** SecurityWeek — https://www.securityweek.com/first-vpn-cybercrime-service-disrupted-administrator-arrested/
- **Severity:** medium
- **Tags:** `ransomware`, `malware`
- **Summary:** FBI disrupted First VPN, a cybercrime anonymization service used by dozens of ransomware groups for network reconnaissance and intrusion. The administrator was arrested.

### 8. FTC Fines Cox Media Group $1M Over Deceptive AI 'Active Listening' Ad Targeting Service
- **Source:** Simon Willison — https://simonwillison.net/2026/May/22/ftc-active-listening/#atom-everything
- **Severity:** medium
- **Tags:** `ai-safety`, `privacy`
- **Summary:** FTC ordered Cox Media Group and two other firms to pay ~$1M for marketing an undisclosed AI "active listening" ad-targeting service allegedly using smart device microphones. Signals FTC willingness to enforce against AI products implying covert surveillance.

### 9. CISA Opens Nomination Form for Researchers to Submit Bugs to Known Exploited Vulnerabilities Catalog
- **Source:** The Record (Recorded Future) — https://therecord.media/cisa-to-allow-researchers-to-report-vulnerabilities-kev
- **Severity:** informational
- **Tags:** `vulnerability`, `cve`
- **Summary:** CISA launched a public form for researchers and vendors to nominate bugs for the KEV catalog, potentially accelerating the lag between exploitation discovery and catalog inclusion.

## Skippable

- **TrendAI Patches Apex One Zero-Day Exploited in the Wild** (SecurityWeek) — CVE-2026-34926 covered by the CISA KEV item; duplicate.
- **Grafana Says Codebase and Other Data Stolen via TanStack Supply Chain Attack** (SecurityWeek) — duplicate; breach already covered in 2026-05-20-grafana-github-breach-tanstack-npm.md.
- **US and Canada arrest and charge suspected Kimwolf botnet admin** (BleepingComputer) — duplicate of Krebs item with less detail.
- **Kimwolf DDoS Botnet Operator Arrested in Canada Over DDoS-for-Hire Attacks** (The Hacker News) — duplicate of Krebs item.
- **How CISOs Should Prep for Agentic-Ready AI BOMs** (Dark Reading) — opinion/advice piece, no news event.
