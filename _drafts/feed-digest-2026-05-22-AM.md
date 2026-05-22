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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `cisco`, `cloud-security`
- **Slug:** `2026-05-22-cisco-cvss-10-secure-workload-rce`
- **Must-know:** no
- **Summary:** CVE-2026-20223 carries a maximum CVSS 10.0 score and allows unauthenticated remote attackers to access sensitive data in Cisco Secure Workload via insufficient REST API validation. No active exploitation reported yet, but the zero-authentication requirement makes this an immediate patching priority.

### 2. CISA Adds Actively Exploited Langflow and Trend Micro Apex One Flaws to KEV
- **Source:** The Hacker News — https://thehackernews.com/2026/05/cisa-adds-exploited-langflow-and-trend.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `zero-day`, `rce`
- **Slug:** `2026-05-22-cisa-kev-langflow-apex-one`
- **Must-know:** no
- **Summary:** CISA added CVE-2025-34291 (Langflow, CVSS 9.4 — origin validation error) and CVE-2026-34926 (Trend Micro Apex One — directory traversal) to the KEV catalog, confirming active exploitation of both. Langflow's broad use in AI agent pipelines makes this especially relevant for teams running self-hosted LLM infrastructure.

### 3. China's Webworm APT Abuses Discord and Microsoft Graph API to Target EU Governments
- **Source:** Dark Reading — https://www.darkreading.com/endpoint-security/chinas-webworm-discord-microsoft-graphs
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `apt`, `cloud-security`, `microsoft`, `malware`
- **Slug:** `2026-05-22-webworm-discord-ms-graph-eu-govts`
- **Must-know:** no
- **Summary:** Webworm, a Chinese APT, is routing C2 traffic through Discord and the Microsoft Graph API to blend into legitimate enterprise cloud traffic while targeting European government entities. SoftEther VPN-based SOCKS proxies are used as an additional layer of obfuscation.

### 4. Cloud Atlas APT Returns With New Tools and Payloads Targeting Russian and Belarusian Government
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/cloud-atlas-2026/119895/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `apt`, `malware`, `vulnerability`
- **Slug:** `2026-05-22-cloud-atlas-apt-new-tools-2026`
- **Must-know:** no
- **Summary:** Kaspersky GReAT documents Cloud Atlas activity from late 2025 into early 2026, including new tools and payloads used against Russian and Belarusian government and diplomatic targets. The group continues to evolve its toolkit while maintaining focus on the same target sector.

### 5. Nation-State Actors Weaponize ROADtools Open-Source Framework for Cloud Intrusions
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `apt`, `cloud-security`, `azure`, `iam`
- **Slug:** `2026-05-22-roadtools-nation-state-cloud-abuse`
- **Must-know:** no
- **Summary:** Unit 42 details how threat actors are misusing ROADtools, a legitimate Azure AD/Entra ID research framework, as an offensive cloud reconnaissance tool. The post includes detection guidance based on distinctive API call patterns and user-agent artifacts the tool leaves in Entra ID logs.

### 6. Kimwolf DDoS Botnet Operator 'Dort' Arrested in Canada, Charged in US and Canada
- **Source:** Krebs on Security — https://krebsonsecurity.com/2026/05/alleged-kimwolf-botmaster-dort-arrested-charged-in-u-s-and-canada/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `botnet`, `ddos`
- **Slug:** `2026-05-22-kimwolf-botmaster-dort-arrested`
- **Must-know:** no
- **Summary:** Jacob Butler (aka "Dort"), 23, of Ottawa was arrested for operating Kimwolf — an AISURU variant botnet that enslaved ~2 million devices for DDoS-for-hire campaigns. Krebs had publicly named him as a suspect in February 2026 after he retaliated against the publication with DDoS and swatting attacks.

### 7. FBI Disrupts 'First VPN' Cybercrime Service Used by Dozens of Ransomware Groups
- **Source:** SecurityWeek — https://www.securityweek.com/first-vpn-cybercrime-service-disrupted-administrator-arrested/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ransomware`, `malware`
- **Slug:** `2026-05-22-first-vpn-cybercrime-service-disrupted`
- **Must-know:** no
- **Summary:** The FBI disrupted First VPN, a cybercrime anonymization service that dozens of ransomware groups used for reconnaissance and intrusion operations. The administrator was arrested; the takedown removes a shared egress resource from the ransomware-as-a-service ecosystem.

### 8. FTC Fines Cox Media Group $1M Over Deceptive AI 'Active Listening' Ad Targeting Service
- **Source:** Simon Willison — https://simonwillison.net/2026/May/22/ftc-active-listening/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-safety`, `privacy`
- **Slug:** `2026-05-22-ftc-active-listening-ai-enforcement`
- **Must-know:** no
- **Summary:** The FTC ordered Cox Media Group and two other firms to pay ~$1M for marketing an AI "active listening" service that allegedly used smart device microphones to capture voice data for ad targeting, without consumer disclosure. The enforcement action signals FTC willingness to pursue AI products that imply undisclosed surveillance capabilities.

### 9. CISA Opens Nomination Form for Researchers to Submit Bugs to Known Exploited Vulnerabilities Catalog
- **Source:** The Record (Recorded Future) — https://therecord.media/cisa-to-allow-researchers-to-report-vulnerabilities-kev
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `vulnerability`, `cve`
- **Slug:** `2026-05-22-cisa-kev-researcher-nominations`
- **Must-know:** no
- **Summary:** CISA created a public nomination form so researchers, vendors, and partners can submit bugs for inclusion in the KEV catalog. This may reduce the lag between public exploitation discovery and catalog inclusion, giving defenders faster signal on patch prioritization.

## Skippable

- **TrendAI Patches Apex One Zero-Day Exploited in the Wild** (SecurityWeek) — CVE-2026-34926 fully covered in the CISA KEV item above; duplicate.
- **Grafana Says Codebase and Other Data Stolen via TanStack Supply Chain Attack** (SecurityWeek) — confirmation of the Grafana TanStack breach already covered in 2026-05-20-grafana-github-breach-tanstack-npm.md; no new actionable information.
- **US and Canada arrest and charge suspected Kimwolf botnet admin** (BleepingComputer) — duplicate of Krebs item; Krebs has superior detail and personal history of the suspect.
- **Kimwolf DDoS Botnet Operator Arrested in Canada Over DDoS-for-Hire Attacks** (The Hacker News) — duplicate of Krebs item.
- **How CISOs Should Prep for Agentic-Ready AI BOMs** (Dark Reading) — opinion/advice piece with no news event; no drafts warranted.
