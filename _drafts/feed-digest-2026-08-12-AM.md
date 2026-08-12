# Digest — 2026-08-12 AM

- Window: last 14h
- Raw items considered: 34
- Relevant: 11
- Skippable: 23

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Cisco ASA/FTD Zero-Day Exploited in the Wild for DoS — `2026-08-12-cisco-asa-ftd-zero-day-dos-exploited.md`
- [x] **[CRITICAL]** Windows Kernel Driver Zero-Day Actively Exploited in August Patch Tuesday — `2026-08-11-microsoft-afd-sys-zero-day-actively-exploited.md`
- [x] **[HIGH]** SAP Commerce Cloud Flaw Allows Unauthenticated Remote Code Execution — `2026-08-12-sap-commerce-cloud-cve-2026-58231-rce.md`
- [x] **[HIGH]** SonicWall Patches Critical RCE Flaws in Discontinued GMS Platform — `2026-08-12-sonicwall-gms-critical-vulnerabilities.md`
- [x] **[HIGH]** ShieldBreak PoC Demonstrates Microsoft Defender Patch Bypass — `2026-08-12-shieldbreak-defender-patch-bypass-poc.md`
- [x] **[HIGH]** Researchers Demonstrate Stealing Reasoning Traces From Proprietary LLM APIs — `2026-08-11-stealing-reasoning-traces-llm-apis.md`
- [x] **[HIGH]** Sandworm-Linked UAC-0145 Uses Fake Job Interviews to Push Remote-Control VPN Malware — `2026-08-11-sandworm-uac-0145-fake-job-vpn-malware.md`
- [x] **[HIGH]** Zoom Annotation Flaw Let Meeting Participants Hijack Other Attendees' Clients — `2026-08-11-zoom-annotation-flaw-client-hijack.md`
- [x] **[MEDIUM]** DeadLock Ransomware Uses Blockchain to Resist Infrastructure Takedown — `2026-08-11-deadlock-ransomware-blockchain-infrastructure.md`
- [x] **[MEDIUM]** Gunra Ransomware Exploits Fortinet Flaws, Bypasses MFA — `2026-08-11-gunra-ransomware-fortinet-mfa-bypass.md`
- [x] **[MEDIUM]** Kimwolf v7 Android Botnet Disguises HTTP/2 DDoS Traffic as Legitimate Browsing — `2026-08-11-kimwolf-v7-android-botnet-http2-ddos.md`

## Relevant (details)

### 1. Cisco ASA/FTD Zero-Day Exploited in the Wild for DoS
- **Source:** The Hacker News — https://thehackernews.com/2026/08/cisco-asa-and-ftd-flaw-exploited-in.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `zero-day`, `cisco`
- **Slug:** `cisco-asa-ftd-zero-day-dos-exploited`
- **Must-know:** yes
- **Summary:** Cisco warns that CVE-2026-20349 (CVSS 8.6), an insufficient-error-checking flaw in Secure Firewall ASA/FTD's HTTP request processing, is being actively exploited to remotely crash devices without authentication. Multiple outlets (SecurityWeek, BleepingComputer) independently corroborated active exploitation.

### 2. Windows Kernel Driver Zero-Day Actively Exploited in August Patch Tuesday
- **Source:** The Hacker News — https://thehackernews.com/2026/08/microsoft-patches-398-flaws-including.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `zero-day`, `microsoft`, `privilege-escalation`
- **Slug:** `microsoft-afd-sys-zero-day-actively-exploited`
- **Must-know:** yes
- **Summary:** Microsoft's August 2026 Patch Tuesday closes CVE-2026-68820 (CVSS 7.0), a Windows kernel driver flaw handling network socket operations that is already being exploited to escalate local code execution to SYSTEM. It was one of at least two publicly disclosed or exploited flaws in this month's release, per Krebs and BleepingComputer.

### 3. SAP Commerce Cloud Flaw Allows Unauthenticated Remote Code Execution
- **Source:** The Hacker News — https://thehackernews.com/2026/08/sap-commerce-cloud-flaw-could-let.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `sap-commerce-cloud-cve-2026-58231-rce`
- **Must-know:** no
- **Summary:** SAP patched CVE-2026-58231, a maximum-severity (CVSS 10.0) flaw in Commerce Cloud's Data Hub Adapter caused by insufficient authorization checks and input validation, allowing unauthenticated attackers to execute arbitrary code. No active exploitation has been reported yet.

### 4. SonicWall Patches Critical RCE Flaws in Discontinued GMS Platform
- **Source:** SecurityWeek — https://www.securityweek.com/sonicwall-patches-critical-vulnerabilities-in-discontinued-gms-platform/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `sonicwall-gms-critical-vulnerabilities`
- **Must-know:** no
- **Summary:** SonicWall patched critical vulnerabilities in its discontinued GMS platform that could let unauthenticated attackers execute arbitrary code remotely and read sensitive data. No active exploitation has been confirmed.

### 5. ShieldBreak PoC Demonstrates Microsoft Defender Patch Bypass
- **Source:** The Hacker News — https://thehackernews.com/2026/08/shieldbreak-zero-day-poc-claims.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `microsoft`, `privilege-escalation`
- **Slug:** `shieldbreak-defender-patch-bypass-poc`
- **Must-know:** no
- **Summary:** A researcher known as Chaotic Eclipse released a public PoC dubbed ShieldBreak that bypasses Microsoft's patch for CVE-2026-50656 ("RoguePlanet," CVSS 7.8) in Microsoft Defender for Windows, reportedly enabling SYSTEM-level access. No confirmed in-the-wild exploitation yet.

### 6. Researchers Demonstrate Stealing Reasoning Traces From Proprietary LLM APIs
- **Source:** Simon Willison — https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `vulnerability`
- **Slug:** `stealing-reasoning-traces-llm-apis`
- **Must-know:** no
- **Summary:** A new paper shows that encrypted chain-of-thought blocks returned by Anthropic, OpenAI, and Google APIs can be replayed across sessions, users, and models. Researchers replayed a frontier model's trace into a weaker sibling model, jailbroke it, and recovered the stronger model's hidden reasoning in plaintext.

### 7. Sandworm-Linked UAC-0145 Uses Fake Job Interviews to Push Remote-Control VPN Malware
- **Source:** The Hacker News — https://thehackernews.com/2026/08/sandworm-linked-uac-0145-uses-fake-job.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Slug:** `sandworm-uac-0145-fake-job-vpn-malware`
- **Must-know:** no
- **Summary:** CERT-UA disclosed a campaign by UAC-0145, a Sandworm/APT44 subgroup, posing as recruiters to trick Ukrainian IT workers into installing a trojanized VPN client capable of running arbitrary commands. BleepingComputer independently reported the same campaign, active since at least May.

### 8. Zoom Annotation Flaw Let Meeting Participants Hijack Other Attendees' Clients
- **Source:** The Hacker News — https://thehackernews.com/2026/08/zoom-annotation-flaws-could-let-meeting.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`
- **Slug:** `zoom-annotation-flaw-client-hijack`
- **Must-know:** no
- **Summary:** Flaws in Zoom's screen-annotation feature let any meeting participant take over another attendee's computer with zero interaction required — no click, no download, no visible prompt. The presenter and any viewer were both exposed; Zoom has issued fixes.

### 9. DeadLock Ransomware Uses Blockchain to Resist Infrastructure Takedown
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/deadlock-ransomware-uses-blockchain-to-resist-infrastructure-takedown/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ransomware`, `malware`
- **Slug:** `deadlock-ransomware-blockchain-infrastructure`
- **Must-know:** no
- **Summary:** The DeadLock ransomware operation is running decentralized, blockchain-backed infrastructure to protect victim communications and its data-leak site from takedown efforts, making standard infrastructure-disruption responses less effective.

### 10. Gunra Ransomware Exploits Fortinet Flaws, Bypasses MFA
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/gunra-ransomware-gang-fortinet-flaws-bypasses-mfa
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ransomware`, `privilege-escalation`, `vulnerability`
- **Slug:** `gunra-ransomware-fortinet-mfa-bypass`
- **Must-know:** no
- **Summary:** The Gunra ransomware-as-a-service operation is compromising critical infrastructure targets by combining leaked Conti source code with older, unpatched flaws in Fortinet firewalls and VPN appliances to bypass MFA.

### 11. Kimwolf v7 Android Botnet Disguises HTTP/2 DDoS Traffic as Legitimate Browsing
- **Source:** The Hacker News — https://thehackernews.com/2026/08/kimwolf-v7-android-botnet-makes-http2.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `ddos`
- **Slug:** `kimwolf-v7-android-botnet-http2-ddos`
- **Must-know:** no
- **Summary:** Unit 42 identified Kimwolf v7 (aka AISURU), a new version of an Android/IoT botnet that adds HTTP/2-based DDoS traffic designed to blend in with legitimate browsing, improving both resilience and attack effectiveness.

## Skippable

- **ICS Patch Tuesday: Siemens, Schneider, Phoenix Contact** — SecurityWeek. Routine ICS advisory roundup, no single critical+exploited CVE called out.
- **Cisco Patches Firewall Zero-Day Exploited for DoS Attacks** — SecurityWeek. Duplicate coverage of the CVE-2026-20349 story (picked The Hacker News as primary source).
- **Google says Chrome cuts 7 billion unwanted Android notifications a day** — BleepingComputer. Generic anti-abuse feature stat, no security substance.
- **Saber denies replacing Rideshare Stimulator's writers with ChatGPT** — The Verge AI. Gaming-industry labor dispute, no security or AI-capability substance.
- **There are no lossless transformations of natural-language text** — Simon Willison. Opinion piece on AI writing ethics, no news value.
- **Microsoft Patch Tuesday for August 2026 — Snort rules** — Cisco Talos. Duplicate patch Tuesday coverage.
- **Landing Zone Accelerator Assessment Report for C5:2020** — AWS Security Blog. Compliance-report announcement, no practitioner-relevant security detail.
- **Microsoft's Patch Tuesday Deluge Continues** — Dark Reading. Duplicate/opinion coverage of the same patch Tuesday release.
- **Accel closes oversubscribed $550M India fund** — TechCrunch AI. VC funding news, no security or AI-capability substance.
- **Microsoft Plugs Nearly 400 Security Holes** — Krebs on Security. Duplicate patch Tuesday coverage.
- **Sandworm hackers target IT pros with trojanized WireGuard VPN client** — BleepingComputer. Duplicate of the UAC-0145 fake-job-interview campaign (picked The Hacker News as primary source).
- **datasette-upload-dbs 0.5a0** — Simon Willison. Niche personal dev-tool plugin release, no broad security or AI substance.
- **NSA installs DHS lawyer as new general counsel** — The Record. Personnel appointment, no technical substance.
- **Cisco warns of ASA and FTD VPN flaw exploited to crash devices** — BleepingComputer. Duplicate of the CVE-2026-20349 story.
- **ChatGPT and Gemini both just passed 1 billion users** — The Verge AI. User-count milestone/marketing stat, no capability or security substance.
- **OpenAI launches ChatGPT desktop app for Linux** — TechCrunch AI. Routine platform port, no capability or security substance.
- **Ransomware group hijacks hospital system's Facebook page** — The Record. Victim disclosure without TTPs or IOCs; no confirmed user count.
- **Summer 2026 SOC 1 report is now available** — AWS Security Blog. Compliance-report announcement, routine.
- **Google's Gemini app surges to 1 billion users** — TechCrunch AI. Duplicate of the 1-billion-users milestone story.
- **August 2026 Patch Tuesday: Microsoft Fixes 421 CVEs, One Exploited Zero-Day** — SecurityWeek. Duplicate patch Tuesday coverage (picked The Hacker News as primary source for the exploited zero-day).
- **Delta probes Wi-Fi deauth attack on flight carrying DEF CON attendees** — BleepingComputer. Developing story, no confirmed technical details or IOCs yet.
- **Microsoft releases Windows 10 KB5120249 extended security update** — BleepingComputer. Routine cumulative update, no critical/exploited CVE called out.
- **Microsoft August 2026 Patch Tuesday fixes 400 flaws, 3 zero-days** — BleepingComputer. Duplicate patch Tuesday coverage.
