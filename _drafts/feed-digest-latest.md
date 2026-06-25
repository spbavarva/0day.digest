# Digest — 2026-06-25 PM

- Window: last 14h
- Raw items considered: 49
- Relevant: 13
- Skippable: 36

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[MEDIUM]** Bluekit Phishing Kit Adds Browser-in-the-Middle for Credential Theft — `2026-06-25-bluekit-phishing-kit-browser-in-the-middle.md`
- [x] **[HIGH]** Popular Chrome Ad Blocker With 10M+ Installs Found to Have Dormant Script Injection Capability — `2026-06-25-chrome-ad-blocker-dormant-script-injection.md`
- [x] **[MEDIUM]** Cal Water Finds No OT Systems Breached After Iranian Handala Group's Claims — `2026-06-25-cal-water-handala-no-ot-breach.md`
- [x] **[HIGH]** pydicom/pynetdicom Path Traversal Flaw Allows Unauthenticated Arbitrary File Writes — `2026-06-25-pydicom-pynetdicom-path-traversal.md`
- [x] **[HIGH]** EVoke EV Charging Station Software Has Critical Missing-Authentication Flaw — `2026-06-25-evoke-charging-station-missing-authentication.md`
- [x] **[HIGH]** Lantronix Serial-to-IP Converter Flaw Actively Exploited in OT Attacks — `2026-06-25-lantronix-flaw-exploited-ot-attacks.md`
- [x] **[HIGH]** GitLab Patches Code Execution and Information Disclosure Vulnerabilities — `2026-06-25-gitlab-patches-code-execution-flaws.md`
- [x] **[INFORMATIONAL]** Kaspersky: Fake AI Tools Drive 2026 SMB Threat Landscape — `2026-06-25-kaspersky-smb-threat-landscape-2026.md`
- [x] **[INFORMATIONAL]** How Windows Threat Actors Abuse the Component Object Model (COM) — `2026-06-25-windows-com-abuse-threat-research.md`
- [x] **[INFORMATIONAL]** Europe Becomes Ransomware Gangs' Favorite Target Region — `2026-06-25-europe-ransomware-favorite-region.md`
- [x] **[MEDIUM]** New 'Gaslight' macOS Malware Uses Prompt Injection to Disrupt AI-Assisted Analysis — `2026-06-25-gaslight-macos-malware-prompt-injection.md`
- [x] **[HIGH]** Chrome 149 Patches 18 Severe Vulnerabilities, Mostly Use-After-Free Bugs — `2026-06-25-chrome-149-patches-severe-vulnerabilities.md`
- [x] **[CRITICAL]** Cisco Catalyst SD-WAN Zero-Day CVE-2026-20245 Exploited Months Before Patch — `2026-06-25-cisco-sdwan-zero-day-cve-2026-20245.md`

## Relevant (details)

### 1. Bluekit Phishing Kit Adds Browser-in-the-Middle for Credential Theft
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/bluekit-phishing-kit-adopts-browser-in-the-middle-for-login-theft/
- **Severity:** medium
- **Tags:** `phishing`
- **Summary:** The Bluekit phishing-as-a-service kit added browser-in-the-middle capability for real-time credential theft, with nearly 70 new hostnames identified in the past week.

### 2. Popular Chrome Ad Blocker With 10M+ Installs Found to Have Dormant Script Injection Capability
- **Source:** The Hacker News — https://thehackernews.com/2026/06/chrome-ad-blocker-with-10m-installs.html
- **Severity:** high
- **Tags:** `supply-chain`, `vulnerability`, `xss`
- **Summary:** A Chrome Web Store ad blocker with 10M+ installs and a Featured badge was found to have a dormant capability to execute arbitrary JavaScript, outside its advertised function.

### 3. Cal Water Finds No OT Systems Breached After Iranian Handala Group's Claims
- **Source:** SecurityWeek — https://www.securityweek.com/cal-water-finds-no-evidence-of-ot-activity-after-hackers-claimed-they-could-disrupt-water-supply/
- **Severity:** medium
- **Tags:** `ics`
- **Summary:** Mandiant helped California Water Service investigate a cyberattack attributed to Iranian group Handala; no evidence of OT system breach was found.

### 4. pydicom/pynetdicom Path Traversal Flaw Allows Unauthenticated Arbitrary File Writes
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-176-01
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `ics`, `pypi`
- **Summary:** A CVSS 9.1 path traversal flaw in pynetdicom <3.0.4 lets an unauthenticated attacker write to arbitrary file paths; this open-source DICOM toolkit is widely used in healthcare imaging.

### 5. EVoke EV Charging Station Software Has Critical Missing-Authentication Flaw
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-176-02
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `ics`, `iam`
- **Summary:** CISA disclosed CVSS 9.4 flaws in EVoke Systems' Charging Station Management System, including missing authentication, that could let attackers seize admin control or trigger DoS.

### 6. Lantronix Serial-to-IP Converter Flaw Actively Exploited in OT Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/lantronix-serial-to-ip-converter-flaw-exploited-in-attacks-after-ot-threat-warning/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `ics`
- **Summary:** CVE-2025-67038, disclosed in April under the BRIDGE:BREAK OT research project, is now being actively exploited in attacks against Lantronix serial-to-IP converters.

### 7. GitLab Patches Code Execution and Information Disclosure Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/gitlab-patches-code-execution-information-disclosure-vulnerabilities/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `devsecops`
- **Summary:** GitLab's latest CE/EE release fixes 13 vulnerabilities, including three high-severity code execution and information disclosure defects.

### 8. Kaspersky: Fake AI Tools Drive 2026 SMB Threat Landscape
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/smb-threat-report-2026/120357/
- **Severity:** informational
- **Tags:** `phishing`, `malware`, `llm`
- **Summary:** Kaspersky's 2026 SMB threat report highlights rising attacks impersonating fake AI tools alongside phishing and dark-web data sales targeting small businesses.

### 9. How Windows Threat Actors Abuse the Component Object Model (COM)
- **Source:** Cisco Talos — https://blog.talosintelligence.com/introduction-to-com-usage-by-windows-threats/
- **Severity:** informational
- **Tags:** `malware`, `appsec`
- **Summary:** Cisco Talos detailed how threat actors abuse Windows COM, a legitimate inter-process automation technology, for object activation and automation-driven attack techniques.

### 10. Europe Becomes Ransomware Gangs' Favorite Target Region
- **Source:** Dark Reading — https://www.darkreading.com/cybersecurity-analytics/europe-evolves-ransomware-favorite-region
- **Severity:** informational
- **Tags:** `ransomware`
- **Summary:** Ransomware gangs are increasingly shifting focus to EU organizations and their suppliers after a broader global slowdown in ransomware activity.

### 11. New 'Gaslight' macOS Malware Uses Prompt Injection to Disrupt AI-Assisted Analysis
- **Source:** The Hacker News — https://thehackernews.com/2026/06/new-gaslight-macos-malware-uses-prompt.html
- **Severity:** medium
- **Tags:** `malware`, `llm`, `ai-safety`
- **Summary:** A Rust-based macOS implant dubbed Gaslight embeds prompt-injection payloads designed to trick AI-assisted malware analysis tools into aborting or refusing analysis.

### 12. Chrome 149 Patches 18 Severe Vulnerabilities, Mostly Use-After-Free Bugs
- **Source:** SecurityWeek — https://www.securityweek.com/chrome-149-update-resolves-18-severe-vulnerabilities/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`, `google`
- **Summary:** Chrome 149 resolves 18 high/critical-severity vulnerabilities, more than half use-after-free bugs that can potentially be chained into remote code execution.

### 13. Cisco Catalyst SD-WAN Zero-Day CVE-2026-20245 Exploited Months Before Patch
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cisco-catalyst-sd-wan-zero-day-cve-2026.html
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `vulnerability`, `privilege-escalation`, `cisco`
- **Summary:** Mandiant found CVE-2026-20245, a Cisco Catalyst SD-WAN privilege-escalation flaw, was exploited as a zero-day for at least two months before disclosure and patching — the seventh Cisco SD-WAN vulnerability exploited in 2026.

## Skippable

- **DHS chief says president has met with potential CISA nominee; agency plans to hire 600** — The Record. Staffing/policy update, no technical content.
- **Microsoft quietly extends free Windows 10 ESU support to October 2027** — BleepingComputer. Generic IT lifecycle news.
- **Beyond IOCs: AI-enabled threat intelligence** — Cisco Talos. Vendor newsletter opinion piece.
- **Anthropic's Claude is winning over paid consumers, a market owned by ChatGPT** — TechCrunch AI. Market-share commentary, no security/model substance.
- **General Intuition's $2.3B bet that video games can train AI agents for the real world** — TechCrunch AI. Funding/startup story.
- **Databricks' former AI chief thinks he can cut AI's power bill by 1,000x** — TechCrunch AI. Funding/startup claim, unverifiable detail.
- **New macOS malware embeds fake errors to confuse AI analysis tools** — BleepingComputer. Duplicate — see Gaslight item above.
- **Which tokens does a hybrid model predict better?** — Hugging Face Blog. Thin research note, no capability claim given.
- **Our latest Google Finance upgrades, including a new app** — Google AI Blog. Product feature update, no security substance.
- **PirloTV sports piracy network disrupted as 44 domains seized** — BleepingComputer. Piracy enforcement, not a security vuln/breach.
- **Netris raises $15M Series A from a16z to help AI neoclouds go live faster** — TechCrunch AI. Funding round.
- **Another Russian dairy company reportedly disrupted by cyberattack** — The Record. Regional incident, no technical detail.
- **The Four Elevations of Effective Fraud Prevention** — BleepingComputer. Vendor marketing content.
- **2 days left to save up to $190: TechCrunch Founder Summit** — TechCrunch AI. Event marketing.
- **Adobe acquires image and video enhancement tool maker Topaz Labs** — TechCrunch AI. M&A news, no security/model substance.
- **Runlayer Raises $30 Million in Series A Funding** — SecurityWeek. Funding round announcement.
- **ThreatsDay Bulletin: Smart TV Proxyware, 24-Year curl Bug, AI Crime Forums + 13 More Stories** — The Hacker News. Weekly aggregator roundup; stories evaluated individually elsewhere.
- **Ukraine's state postal operator reports app disruption after cyberattack** — The Record. Regional incident, no technical detail.
- **Russia used Cellebrite phone-hacking tool to crack down on dissident after firm cut off country** — The Record. Policy/human-rights story, no new vulnerability detail.
- **Webinar: Why account takeovers remain one of the hardest threats to stop** — BleepingComputer. Vendor webinar promotion.
- **Amazon ups India bet with fresh $13B AI infrastructure investment** — TechCrunch AI. Infrastructure investment, no security/model substance.
- **Ford had to hire back former engineers to fix mistakes made by its automated systems** — The Verge AI. Manufacturing/quality story, no security angle.
- **Daktronics Controller Firmware** — CISA Alerts (CVSS 8.1). Routine ICS batch, niche vendor, no known active exploitation.
- **Delta Electronics DTM Soft** — CISA Alerts (CVSS 7.8). Routine ICS batch, niche vendor, no known active exploitation.
- **OHIF Viewers DICOM** — CISA Alerts (CVSS 8.2, SSRF). Requires victim to click a crafted link; ICS coverage already included above.
- **H.VIEW HV-500S6 IP Camera** — CISA Alerts (CVSS 7.2). Niche/regional vendor, routine ICS batch.
- **Schneider Electric PowerLogic P7** — CISA Alerts. Routine ICS batch, no CVSS/exploitation status confirmed.
- **Yokogawa FAST/TOOLS and CI Server** — CISA Alerts (CVSS 7.5, info disclosure only). Routine ICS batch.
- **Horner Automation Cscape** — CISA Alerts (CVSS 7.8). Requires local access, routine ICS batch.
- **Surviving the Mythos Era: Richard Bejtlich on the Case for NDR** — The Hacker News. Vendor-sponsored opinion piece.
- **25-Year-Old Vulnerability Patched in Curl** — SecurityWeek. 18 medium/low-severity bugs only, none critical/exploited.
- **Facebook's Creator Studio has been revived as an AI companion app** — The Verge AI. Product relaunch, no security/model substance.
- **SecurityWeek ICS Cybersecurity Conference Heads to Nashville for Special 25-Year Anniversary Edition** — SecurityWeek. Event/conference announcement.
- **New Mistic Backdoor Linked to KongTuke in ClickFix and ModeloRAT Campaigns** — The Hacker News. Duplicate of Mistic malware family covered yesterday.
- **NIST Opens Updated IoT Security Guidance to Public Review** — SecurityWeek. Draft guidance, no enforceable impact yet.
- **Cisco SD-WAN Zero-Day Exploited Months Before Patching** — SecurityWeek. Duplicate — see Cisco SD-WAN item above.
