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
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`
- **Slug:** `bluekit-phishing-kit-browser-in-the-middle`
- **Must-know:** no
- **Summary:** The Bluekit phishing-as-a-service kit added browser-in-the-middle capability for real-time credential theft, with nearly 70 new hostnames identified in the past week. The kit's continued evolution makes it a recurring detection priority for phishing defenses.

### 2. Popular Chrome Ad Blocker With 10M+ Installs Found to Have Dormant Script Injection Capability
- **Source:** The Hacker News — https://thehackernews.com/2026/06/chrome-ad-blocker-with-10m-installs.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `vulnerability`, `xss`
- **Slug:** `chrome-ad-blocker-dormant-script-injection`
- **Must-know:** no
- **Summary:** Researchers at Island found that "Adblock for YouTube," a Chrome Web Store extension with a Featured badge and over 10 million installs, has the dormant ability to execute arbitrary JavaScript on pages. The capability sits outside the extension's advertised ad-blocking function, raising browser extension supply-chain concerns.

### 3. Cal Water Finds No OT Systems Breached After Iranian Handala Group's Claims
- **Source:** SecurityWeek — https://www.securityweek.com/cal-water-finds-no-evidence-of-ot-activity-after-hackers-claimed-they-could-disrupt-water-supply/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ics`
- **Slug:** `cal-water-handala-no-ot-breach`
- **Must-know:** no
- **Summary:** Mandiant assisted California Water Service in investigating a cyberattack attributed to Iranian hacker group Handala, which had claimed it could disrupt the water supply. The investigation found no evidence that OT systems were breached.

### 4. pydicom/pynetdicom Path Traversal Flaw Allows Unauthenticated Arbitrary File Writes
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-176-01
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `ics`, `pypi`
- **Slug:** `pydicom-pynetdicom-path-traversal`
- **Must-know:** no
- **Summary:** CISA disclosed a path traversal flaw (CVSS 9.1) in pynetdicom versions ≥1.0.0 and <3.0.4 that lets an unauthenticated attacker write to arbitrary file paths. The open-source pydicom/pynetdicom toolkit is widely used in healthcare DICOM imaging systems; a fix is available in v3.0.4.

### 5. EVoke EV Charging Station Software Has Critical Missing-Authentication Flaw
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-176-02
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `ics`, `iam`
- **Slug:** `evoke-charging-station-missing-authentication`
- **Must-know:** no
- **Summary:** CISA disclosed multiple flaws (CVSS 9.4) in EVoke Systems' Charging Station Management System, including missing authentication for critical functions and weak session handling. Exploitation could give attackers unauthorized admin control of charging stations or let them trigger denial-of-service. No patched version is listed in the advisory.

### 6. Lantronix Serial-to-IP Converter Flaw Actively Exploited in OT Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/lantronix-serial-to-ip-converter-flaw-exploited-in-attacks-after-ot-threat-warning/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `ics`
- **Slug:** `lantronix-flaw-exploited-ot-attacks`
- **Must-know:** no
- **Summary:** CVE-2025-67038, a Lantronix serial-to-IP converter flaw disclosed in April as part of the BRIDGE:BREAK OT research project, is now being actively exploited in attacks following a renewed OT threat warning.

### 7. GitLab Patches Code Execution and Information Disclosure Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/gitlab-patches-code-execution-information-disclosure-vulnerabilities/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `devsecops`
- **Slug:** `gitlab-patches-code-execution-flaws`
- **Must-know:** no
- **Summary:** GitLab's latest CE/EE release fixes 13 vulnerabilities, including three high-severity issues covering code execution and information disclosure. Self-hosted GitLab instances should be updated promptly.

### 8. Kaspersky: Fake AI Tools Drive 2026 SMB Threat Landscape
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/smb-threat-report-2026/120357/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `phishing`, `malware`, `llm`
- **Slug:** `kaspersky-smb-threat-landscape-2026`
- **Must-know:** no
- **Summary:** Kaspersky GReAT's 2026 SMB threat report highlights a rise in attacks impersonating fake AI tools alongside traditional phishing schemes and dark-web data sales targeting small and medium businesses.

### 9. How Windows Threat Actors Abuse the Component Object Model (COM)
- **Source:** Cisco Talos — https://blog.talosintelligence.com/introduction-to-com-usage-by-windows-threats/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `malware`, `appsec`
- **Slug:** `windows-com-abuse-threat-research`
- **Must-know:** no
- **Summary:** Cisco Talos published research detailing how threat actors abuse Windows COM — the legitimate inter-process automation technology used by many applications — for object activation and automation-driven attack techniques.

### 10. Europe Becomes Ransomware Gangs' Favorite Target Region
- **Source:** Dark Reading — https://www.darkreading.com/cybersecurity-analytics/europe-evolves-ransomware-favorite-region
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ransomware`
- **Slug:** `europe-ransomware-favorite-region`
- **Must-know:** no
- **Summary:** Dark Reading reports ransomware gangs are increasingly shifting focus to EU organizations and their suppliers after a broader global slowdown in ransomware activity.

### 11. New 'Gaslight' macOS Malware Uses Prompt Injection to Disrupt AI-Assisted Analysis
- **Source:** The Hacker News — https://thehackernews.com/2026/06/new-gaslight-macos-malware-uses-prompt.html (also: BleepingComputer — https://www.bleepingcomputer.com/news/security/new-macos-malware-embeds-fake-errors-to-confuse-ai-analysis-tools/)
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `llm`, `ai-safety`
- **Slug:** `gaslight-macos-malware-prompt-injection`
- **Must-know:** no
- **Summary:** A previously undocumented Rust-based macOS implant and info-stealer, dubbed Gaslight, embeds prompt-injection payloads designed to trick AI-assisted malware analysis tools into aborting or refusing to analyze it. Researchers assess with high confidence the technique specifically targets AI-driven triage pipelines.

### 12. Chrome 149 Patches 18 Severe Vulnerabilities, Mostly Use-After-Free Bugs
- **Source:** SecurityWeek — https://www.securityweek.com/chrome-149-update-resolves-18-severe-vulnerabilities/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`, `google`
- **Slug:** `chrome-149-patches-severe-vulnerabilities`
- **Must-know:** no
- **Summary:** Google's Chrome 149 update resolves 18 high/critical-severity vulnerabilities, more than half of them use-after-free bugs — a class that can potentially be chained into remote code execution. No active exploitation has been reported.

### 13. Cisco Catalyst SD-WAN Zero-Day CVE-2026-20245 Exploited Months Before Patch
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cisco-catalyst-sd-wan-zero-day-cve-2026.html (also: SecurityWeek — https://www.securityweek.com/cisco-sd-wan-zero-day-exploited-months-before-patching/)
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `vulnerability`, `privilege-escalation`, `cisco`
- **Slug:** `cisco-sdwan-zero-day-cve-2026-20245`
- **Must-know:** yes
- **Summary:** Mandiant found that CVE-2026-20245, a privilege-escalation flaw in Cisco Catalyst SD-WAN, was exploited as a zero-day for at least two months before its public disclosure and patch. SecurityWeek notes it's the seventh Cisco SD-WAN vulnerability exploited in 2026, underscoring sustained adversary focus on the product line.

## Skippable

- **DHS chief says president has met with potential CISA nominee; agency plans to hire 600** — The Record. Staffing/policy update, no technical security content.
- **Microsoft quietly extends free Windows 10 ESU support to October 2027** — BleepingComputer. Generic IT lifecycle news, no security vulnerability.
- **Beyond IOCs: AI-enabled threat intelligence** — Cisco Talos. Vendor newsletter opinion piece, no concrete findings.
- **Anthropic's Claude is winning over paid consumers, a market owned by ChatGPT** — TechCrunch AI. Market-share commentary, no model launch or security substance.
- **General Intuition's $2.3B bet that video games can train AI agents for the real world** — TechCrunch AI. Funding/startup story, no security angle.
- **Databricks' former AI chief thinks he can cut AI's power bill by 1,000x** — TechCrunch AI. Funding/startup claim, no verifiable technical detail.
- **New macOS malware embeds fake errors to confuse AI analysis tools** — BleepingComputer. Duplicate coverage — see the Gaslight item above (The Hacker News).
- **Which tokens does a hybrid model predict better?** — Hugging Face Blog. Thin research note, no capability claim provided in the feed summary.
- **Our latest Google Finance upgrades, including a new app** — Google AI Blog. Product feature update, no security/AI substance.
- **PirloTV sports piracy network disrupted as 44 domains seized** — BleepingComputer. IP/piracy enforcement action, not a security vuln or breach story.
- **Netris raises $15M Series A from a16z to help AI neoclouds go live faster** — TechCrunch AI. Funding round, no security/AI substance.
- **Another Russian dairy company reportedly disrupted by cyberattack** — The Record. Regional incident, no technical detail or TTPs.
- **The Four Elevations of Effective Fraud Prevention** — BleepingComputer. Vendor (IPQS) marketing content.
- **2 days left to save up to $190: TechCrunch Founder Summit** — TechCrunch AI. Event marketing.
- **Adobe acquires image and video enhancement tool maker Topaz Labs** — TechCrunch AI. M&A news, no security/model substance.
- **Runlayer Raises $30 Million in Series A Funding** — SecurityWeek. Funding round announcement.
- **ThreatsDay Bulletin: Smart TV Proxyware, 24-Year curl Bug, AI Crime Forums + 13 More Stories** — The Hacker News. Weekly aggregator roundup; underlying stories (e.g. the curl bug) are evaluated individually elsewhere in this digest.
- **Ukraine's state postal operator reports app disruption after cyberattack** — The Record. Regional incident, no technical detail or attribution.
- **Russia used Cellebrite phone-hacking tool to crack down on dissident after firm cut off country** — The Record. Policy/human-rights story, no new technical vulnerability detail.
- **Webinar: Why account takeovers remain one of the hardest threats to stop** — BleepingComputer. Vendor webinar promotion.
- **Amazon ups India bet with fresh $13B AI infrastructure investment** — TechCrunch AI. Infrastructure investment news, no security/model substance.
- **Ford had to hire back former engineers to fix mistakes made by its automated systems** — The Verge AI. Manufacturing/quality story, no security angle.
- **Daktronics Controller Firmware** — CISA Alerts (CVSS 8.1). Routine weekly ICS advisory batch, niche scoreboard-controller vendor, no known active exploitation.
- **Delta Electronics DTM Soft** — CISA Alerts (CVSS 7.8). Routine ICS advisory batch, niche engineering-tool vendor, no known active exploitation.
- **OHIF Viewers DICOM** — CISA Alerts (CVSS 8.2, SSRF). Requires a victim to click a crafted link; today's ICS coverage already includes the pydicom and EVoke advisories.
- **H.VIEW HV-500S6 IP Camera** — CISA Alerts (CVSS 7.2). Niche/regional camera vendor, routine ICS advisory batch.
- **Schneider Electric PowerLogic P7** — CISA Alerts. Routine ICS advisory batch, no CVSS/exploitation status confirmed in the feed summary.
- **Yokogawa FAST/TOOLS and CI Server** — CISA Alerts (CVSS 7.5, info disclosure only). Routine ICS advisory batch.
- **Horner Automation Cscape** — CISA Alerts (CVSS 7.8). Requires local access, routine ICS advisory batch.
- **Surviving the Mythos Era: Richard Bejtlich on the Case for NDR** — The Hacker News. Vendor-sponsored opinion piece, no news event.
- **25-Year-Old Vulnerability Patched in Curl** — SecurityWeek. Patches 18 medium/low-severity bugs only; none critical or actively exploited.
- **Facebook's Creator Studio has been revived as an AI companion app** — The Verge AI. Product relaunch, no security/model substance.
- **SecurityWeek ICS Cybersecurity Conference Heads to Nashville for Special 25-Year Anniversary Edition** — SecurityWeek. Event/conference announcement.
- **New Mistic Backdoor Linked to KongTuke in ClickFix and ModeloRAT Campaigns** — The Hacker News. Duplicate of the Mistic malware family already covered yesterday (different attribution — KongTuke vs. Woodgnat — but same core finding).
- **NIST Opens Updated IoT Security Guidance to Public Review** — SecurityWeek. Draft guidance open for public comment, no enforceable impact yet.
- **Cisco SD-WAN Zero-Day Exploited Months Before Patching** — SecurityWeek. Duplicate coverage — see the Cisco SD-WAN item above (The Hacker News, with Mandiant detail).
