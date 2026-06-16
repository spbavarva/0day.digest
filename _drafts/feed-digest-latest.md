# Digest — 2026-06-16 PM

- Window: last 14h
- Raw items considered: 30
- Relevant: 16
- Skippable: 14

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Supply Chain Attack Hits 1,500 Arch Linux AUR Packages — `2026-06-16-atomic-arch-aur-supply-chain-attack.md`
- [x] **[CRITICAL]** Attackers Exploit Three Fortinet FortiSandbox Flaws Including CVSS 9.1 — `2026-06-16-fortinet-fortisandbox-three-cves-exploited.md`
- [x] **[HIGH]** Cisco Patches Actively Exploited SD-WAN Manager Zero-Day CVE-2026-20262 — `2026-06-16-cisco-sdwan-zero-day-cve-2026-20262.md`
- [x] **[HIGH]** CISA Adds LiteSpeed cPanel Plugin Flaw to KEV, Sets 3-Day Deadline — `2026-06-16-cisa-kev-litespeed-cpanel-cve-2026-54420.md`
- [x] **[HIGH]** DragonForce Ransomware Hides C2 Traffic Inside Microsoft Teams Infrastructure — `2026-06-16-dragonforce-ransomware-teams-relay-c2.md`
- [x] **[HIGH]** Vertex AI Python SDK Flaw Allows Cross-Tenant RCE via Bucket Squatting — `2026-06-16-vertex-ai-sdk-rce-bucket-squatting.md`
- [x] **[HIGH]** China-Linked SprySOCKS Backdoor Gets Windows Variants, Targets Government Orgs — `2026-06-16-sprysocks-windows-variants-government-targets.md`
- [x] **[HIGH]** Trump Administration Issues Export Control Directive Against Anthropic Fable 5 and Mythos 5 — `2026-06-16-anthropic-fable-5-mythos-export-controls.md`
- [x] **[HIGH]** North Korea's APT37 Delivers NarwhalRAT via Fake Microsoft Account Alerts — `2026-06-16-apt37-narwhalrat-fake-microsoft-alerts.md`
- [x] **[HIGH]** iRhythm Confirms Data Breach Exposing Patient Personal and Health Information — `2026-06-16-irhythm-patient-data-breach.md`
- [x] **[MEDIUM]** SpaceX Acquires AI Coding Tool Cursor for $60 Billion — `2026-06-16-spacex-acquires-cursor-60-billion.md`
- [x] **[MEDIUM]** Cal Water Investigates Iranian Hacker Claims Against Critical Infrastructure — `2026-06-16-cal-water-iranian-hackers-investigation.md`
- [x] **[MEDIUM]** White House NSPM-12 Establishes New NSS Cybersecurity Governance Framework — `2026-06-16-nspm-12-nss-cybersecurity-memo.md`
- [x] **[MEDIUM]** Tech Coalition 'Athena' Launches Pre-Disclosure OSS Vulnerability Triage Platform — `2026-06-16-athena-coalition-oss-pre-disclosure.md`
- [x] **[MEDIUM]** Malicious Wallpapers on Steam Workshop Deploy Infostealer Malware — `2026-06-16-steam-workshop-malicious-wallpapers.md`
- [x] **[INFORMATIONAL]** Estonia Mandates Security Screening for Russian .ru Emails to Government Officials — `2026-06-16-estonia-russian-email-quarantine.md`

## Relevant (details)

### 1. Supply Chain Attack Hits 1,500 Arch Linux AUR Packages
- **Source:** SecurityWeek — https://www.securityweek.com/atomic-arch-supply-chain-attack-hits-1500-aur-packages/
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`, `linux`
- **Summary:** Attackers uploaded ~1,500 malicious packages to AUR, forcing Arch Linux to suspend account registrations. AUR is the community-driven repository used by millions of Arch users; supply chain compromise at this scale could affect a large fraction of the active ecosystem.

### 2. Attackers Exploit Three Fortinet FortiSandbox Flaws Including CVSS 9.1
- **Source:** The Hacker News — https://thehackernews.com/2026/06/attackers-exploit-three-fortinet.html
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `rce`, `zero-day`, `fortinet`
- **Summary:** Defused Cyber confirmed active exploitation of CVE-2026-39813 (CVSS 9.1, path traversal/RCE), CVE-2026-39808, and CVE-2026-25089 within the past 24 hours; one was patched only last week. FortiSandbox is widely deployed in enterprise threat detection pipelines.

### 3. Cisco Patches Actively Exploited SD-WAN Manager Zero-Day CVE-2026-20262
- **Source:** SecurityWeek — https://www.securityweek.com/cisco-patches-another-sd-wan-zero-day-exploited-in-attacks/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `zero-day`, `cisco`
- **Summary:** CVE-2026-20262 allows authenticated remote attackers to write arbitrary files to the OS on Catalyst SD-WAN Manager; exploitation was confirmed before the patch shipped. This is framed as another SD-WAN zero-day, indicating sustained pressure on this platform.

### 4. CISA Adds LiteSpeed cPanel Plugin Flaw to KEV, Sets 3-Day Deadline
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-warns-of-another-actively-exploited-cpanel-plugin-flaw/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Summary:** CVE-2026-54420 (CVSS 8.5) in the LiteSpeed cPanel plugin allows root privilege escalation and is actively exploited; FCEB agencies must remediate by June 18. High impact for hosting providers and MSPs running cPanel + LiteSpeed.

### 5. DragonForce Ransomware Hides C2 Traffic Inside Microsoft Teams Infrastructure
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/ransomware-gang-abuses-microsoft-teams-relays-to-hide-malicious-traffic/
- **Severity:** high
- **Tags:** `ransomware`, `malware`, `microsoft`
- **Summary:** DragonForce's 'Backdoor.Turn' malware tunnels C2 through Microsoft Teams relay infrastructure to blend into allowlisted enterprise traffic. Part of a growing pattern of threat actors abusing trusted platforms for command-and-control.

### 6. Vertex AI Python SDK Flaw Allows Cross-Tenant RCE via Bucket Squatting
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/
- **Severity:** high
- **Tags:** `rce`, `cloud-security`, `gcp`, `vulnerability`, `llm`
- **Summary:** Predictable GCS bucket naming in the Vertex AI SDK lets an attacker pre-claim a bucket and inject a malicious pickle payload, achieving RCE when a victim loads a model. Cross-tenant blast radius makes this a significant cloud AI platform risk.

### 7. China-Linked SprySOCKS Backdoor Gets Windows Variants, Targets Government Orgs
- **Source:** The Hacker News — https://thehackernews.com/2026/06/china-linked-sprysocks-backdoor-expands.html
- **Severity:** high
- **Tags:** `malware`, `microsoft`
- **Summary:** ESET found Windows variants WIN_DRV and WIN_PLUS of the previously Linux-only SprySOCKS backdoor, featuring driver-level stealth and hardcoded C2. Used against government organizations in at least four countries by China-nexus actors.

### 8. Trump Administration Issues Export Control Directive Against Anthropic Fable 5 and Mythos 5
- **Source:** The Verge — https://www.theverge.com/ai-artificial-intelligence/950412/anthropic-trump-adminstration-claude-mythos-fable-5-export-controls
- **Severity:** high
- **Tags:** `anthropic`, `ai-safety`, `llm`
- **Summary:** The White House directed Anthropic to suspend Mythos 5 and Fable 5 access for foreign nationals after a report claimed a multi-step "fix this code" prompt produced cyberoffensive-usable output. Cybersecurity experts disputed the finding, calling it normal defensive research, and a coalition of security executives formally urged reversal.

### 9. North Korea's APT37 Delivers NarwhalRAT via Fake Microsoft Account Alerts
- **Source:** The Hacker News — https://thehackernews.com/2026/06/fake-microsoft-alerts-used-to-deploy.html
- **Severity:** high
- **Tags:** `malware`, `phishing`, `microsoft`
- **Summary:** ScarCruft (APT37) is using spear-phishing emails impersonating Microsoft Account security alerts to deliver NarwhalRAT, a full-featured remote access trojan. Campaign is currently active; historically targets South Korean individuals and defector communities.

### 10. iRhythm Confirms Data Breach Exposing Patient Personal and Health Information
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/irhythm-discloses-data-breach-says-hackers-stole-patient-info/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** iRhythm Holdings (maker of the Zio cardiac patch) disclosed that hackers stole patient personal and health data from third-party-hosted business applications. Breach size is undisclosed; third-party hosting remains a persistent healthcare attack surface.

### 11. SpaceX Acquires AI Coding Tool Cursor for $60 Billion
- **Source:** The Verge — https://www.theverge.com/ai-artificial-intelligence/950571/spacex-is-officially-buying-cursor-for-60-billion
- **Severity:** medium
- **Tags:** `ai-launch`
- **Summary:** SpaceX officially agreed to acquire Cursor for $60B in stock days after its IPO, framing it as a move to win enterprise developer customers and close the AI gap with Anthropic and OpenAI. Raises questions about Cursor's independence and enterprise customer trust under Musk ownership.

### 12. Cal Water Investigates Iranian Hacker Claims Against Critical Infrastructure
- **Source:** SecurityWeek — https://www.securityweek.com/cal-water-investigating-iranian-hackers-claims/
- **Severity:** medium
- **Tags:** `critical-infrastructure`
- **Summary:** Cal Water (serving ~2 million Californians) is investigating Iranian hacker claims of system compromise; no operational disruptions to water or wastewater systems confirmed. Aligns with documented Iran-linked ICS/OT reconnaissance activity against US water utilities.

### 13. White House NSPM-12 Establishes New NSS Cybersecurity Governance Framework
- **Source:** SecurityWeek — https://www.securityweek.com/white-house-issues-memo-to-bolster-nss-cybersecurity/
- **Severity:** medium
- **Tags:** `policy`
- **Summary:** NSPM-12 establishes governance and accountability structure for National Security System cybersecurity and reestablishes the Committee on National Security Systems. Covers classified/sensitive government networks outside FISMA/CISA civilian authority.

### 14. Tech Coalition 'Athena' Launches Pre-Disclosure OSS Vulnerability Triage Platform
- **Source:** SecurityWeek — https://www.securityweek.com/tech-coalition-athena-targets-oss-vulnerabilities-ahead-of-disclosure/
- **Severity:** medium
- **Tags:** `supply-chain`, `appsec`, `devsecops`
- **Summary:** 24+ organizations built a shared platform (Athena) to triage and fix OSS vulnerabilities before CVE publication, coordinating patches across downstream consumers under NDA. Addresses the longstanding gap where disclosure outpaces fix propagation in widely-used libraries.

### 15. Malicious Wallpapers on Steam Workshop Deploy Infostealer Malware
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/dozens-of-malicious-wallpapers-found-on-steam-workshop/120186/
- **Severity:** medium
- **Tags:** `malware`, `supply-chain`
- **Summary:** Since late 2025, dozens of Steam Workshop wallpapers embed malware targeting gamers in China and Russia, abusing the platform's trusted content-sharing infrastructure. Steam Workshop lacks the vetting applied to the main store, making it an effective distribution channel.

### 16. Estonia Mandates Security Screening for Russian .ru Emails to Government Officials
- **Source:** The Record (Recorded Future) — https://therecord.media/estonia-quarantine-russian-emails
- **Severity:** informational
- **Tags:** `phishing`, `policy`
- **Summary:** Estonia will quarantine .ru domain emails before they reach government officials, adding a security screening layer against Russian-origin phishing and influence campaigns. Estonia, a frequent Russian cyber target, continues hardening its digitized government.

## Skippable

- **Survey: 94% of Incidents Involve Anonymized Infrastructure** — The Hacker News. Sponsored survey content with marketing framing; no news value.
- **SpaceX to acquire Cursor for $60B** — TechCrunch AI. Duplicate of The Verge coverage used in item 11.
- **Cybersecurity Executives Urge Trump Admin to Ease Restrictions on Anthropic AI Models** — SecurityWeek. Covered as part of the Anthropic export controls story in item 8.
- **Critical Fortinet FortiSandbox flaws now exploited in attacks** — BleepingComputer. Duplicate of The Hacker News coverage in item 2.
- **Windows version of SprySOCKS Linux malware used to attack govt orgs** — BleepingComputer. Duplicate of The Hacker News/ESET coverage in item 7.
- **Malaysia's Respond.io raises $62.5M** — TechCrunch AI. Non-security SaaS funding round with no security angle.
- **Cisco Releases Security Updates for Actively Exploited SD-WAN Manager Flaw** — The Hacker News. Duplicate of SecurityWeek coverage in item 3.
- **CISA Flags LiteSpeed cPanel Plugin Flaw** — The Hacker News. Duplicate of BleepingComputer coverage in item 4.
- **The Fable 5 Export Controls Harm US Cyber Defense** — Simon Willison. Commentary on the Anthropic export controls story covered in item 8.
- **Quoting Matteo Wong, The Atlantic** — Simon Willison. Additional commentary on same Anthropic export controls story; covered in item 8.
- **Cloudflare CAPTCHA on at least one ampersand** — Simon Willison. Personal WAF rule tip with no news value.
- **UK to ban social media access for children under 16** — The Record. Social media age regulation; not security or AI technical.
- **Sundar Pichai faces boos, walkout at Stanford graduation** — TechCrunch AI. Political protest at commencement; no security or AI-technical substance.
- **Inside the Modern SOC: The 72-Minute Race** — Unit 42 (Palo Alto). Vendor marketing content for XSIAM/MDR; not independent news.
