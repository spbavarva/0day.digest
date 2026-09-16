# Digest — 2026-09-16 PM

- Window: last 14h
- Raw items considered: 29
- Relevant: 13
- Skippable: 16

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Google Patches Actively Exploited Pixel Modem Zero-Day (CVE-2026-58704) — `2026-09-16-google-pixel-modem-zero-day-cve-2026-58704.md`
- [x] **[CRITICAL]** Critical ScreenConnect Flaw Now Actively Exploited, CISA Warns — `2026-09-16-screenconnect-critical-flaw-actively-exploited.md`
- [x] **[CRITICAL]** Active Exploitation Targets WSO2 API Manager JWT Bypass (CVE-2026-5430) — `2026-09-16-wso2-api-manager-jwt-bypass-cve-2026-5430.md`
- [x] **[HIGH]** US, UK, Dutch Agencies Expose Iranian 'Chosen Brick' Surveillance Malware — `2026-09-16-iranian-chosen-brick-surveillance-malware.md`
- [x] **[HIGH]** Unauthenticated RCE Flaws Expose 200,000+ WordPress Sites to Takeover — `2026-09-16-wordpress-events-calendar-rce.md`
- [x] **[HIGH]** Acronis Patches Exploited Privilege Escalation Flaw in cPanel Backup Plugin (CVE-2026-87886) — `2026-09-16-acronis-cpanel-backup-plugin-cve-2026-87886.md`
- [x] **[HIGH]** 280,000 Impacted by Premier Medical Group Data Breach — `2026-09-16-premier-medical-group-data-breach.md`
- [x] **[HIGH]** Attackers Exploit WooCommerce Wholesale Lead Capture Flaw to Plant PHP Web Shells — `2026-09-16-woocommerce-wholesale-lead-capture-rce.md`
- [x] **[MEDIUM]** NightEagle APT Targets Russian Companies With GhostContainer Backdoor — `2026-09-16-nighteagle-apt-ghostcontainer-backdoor.md`
- [x] **[MEDIUM]** Atomic macOS (AMOS) Stealer Activity Uses Deceptive Setup Guides — `2026-09-16-atomic-macos-amos-stealer-activity.md`
- [x] **[MEDIUM]** North Korea-Linked Group Uses Undocumented Linux Toolkit Against South Korean Media, Automotive Sectors — `2026-09-16-north-korean-apt-south-korea-linux-toolkit.md`
- [x] **[INFORMATIONAL]** Google Releases Gemini 3.8 Live and Live Extended Thinking Speech Models — `2026-09-15-google-gemini-3-8-live-audio.md`
- [x] **[INFORMATIONAL]** AWS STS Simplifies Session Token Size Limits, Adds Monitoring — `2026-09-15-aws-sts-session-token-size-limits.md`

## Relevant (details)

### 1. Google Patches Actively Exploited Pixel Modem Zero-Day (CVE-2026-58704)
- **Source:** The Hacker News — https://thehackernews.com/2026/09/google-patches-pixel-modem-flaw-amid.html
- **Severity:** critical
- **Tags:** `zero-day`, `privilege-escalation`, `google`
- **Summary:** Google patched CVE-2026-58704, a high-severity privilege escalation flaw in the Pixel Cellular Modem (CVSS 8.0), disclosing signs of limited targeted exploitation. Shipped in the September 2026 Pixel security update, which addressed 110 vulnerabilities total.

### 2. Critical ScreenConnect Flaw Now Actively Exploited, CISA Warns
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-warns-of-hackers-exploiting-critical-screenconnect-flaw/
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`
- **Summary:** CISA warned that a critical-severity ConnectWise ScreenConnect vulnerability is being actively exploited in attacks against widely deployed remote access/support software.

### 3. Active Exploitation Targets WSO2 API Manager JWT Bypass (CVE-2026-5430)
- **Source:** The Hacker News — https://thehackernews.com/2026/09/active-exploitation-attempts-target.html
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `iam`
- **Summary:** A critical WSO2 API Manager flaw (CVE-2026-5430, CVSS 9.8) is under active exploitation, letting attackers forge admin JWTs for account takeover via improper cryptographic signature verification.

### 4. US, UK, Dutch Agencies Expose Iranian 'Chosen Brick' Surveillance Malware
- **Source:** SecurityWeek — https://www.securityweek.com/us-uk-dutch-agencies-expose-iranian-chosen-brick-surveillance-malware/
- **Severity:** high
- **Tags:** `malware`
- **Summary:** US, UK, and Dutch agencies published a joint report on "Chosen Brick," surveillance malware attributed to Iranian actors, with the FBI describing abuse of Telegram for command-and-control.

### 5. Unauthenticated RCE Flaws Expose 200,000+ WordPress Sites to Takeover
- **Source:** SecurityWeek — https://www.securityweek.com/unauthenticated-rce-flaws-could-expose-200000-wordpress-sites-to-takeover/
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `appsec`
- **Summary:** Vulnerabilities in The Events Calendar WordPress plugin allow unauthenticated remote code execution, exposing more than 200,000 sites running unpatched versions to full takeover.

### 6. Acronis Patches Exploited Privilege Escalation Flaw in cPanel Backup Plugin (CVE-2026-87886)
- **Source:** The Hacker News — https://thehackernews.com/2026/09/acronis-cpanel-backup-plugin.html
- **Severity:** high
- **Tags:** `privilege-escalation`, `cve`, `vulnerability`
- **Summary:** Acronis patched CVE-2026-87886 (CVSS 7.8), a local privilege escalation flaw in its Backup plugin for cPanel/WHM caused by insecure file permissions, confirming exploitation in targeted attacks.

### 7. 280,000 Impacted by Premier Medical Group Data Breach
- **Source:** SecurityWeek — https://www.securityweek.com/280000-impacted-by-premier-medical-group-data-breach/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** Premier Medical Group disclosed a June 2026 breach exposing patient names, contact information, diagnosis details, and health insurance information for roughly 280,000 people.

### 8. Attackers Exploit WooCommerce Wholesale Lead Capture Flaw to Plant PHP Web Shells
- **Source:** The Hacker News — https://thehackernews.com/2026/09/attackers-exploit-woocommerce-wholesale.html
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `appsec`
- **Summary:** Threat actors are actively exploiting a critical flaw in WooCommerce Wholesale Lead Capture (6,000+ active installs) that lets unauthenticated attackers upload PHP web shells and achieve RCE.

### 9. NightEagle APT Targets Russian Companies With GhostContainer Backdoor
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/tr/nighteagle-apt-ghostcontainer-and-tunneling/121323/
- **Severity:** medium
- **Tags:** `malware`, `github`
- **Summary:** Kaspersky GReAT uncovered a new NightEagle APT campaign against Russian companies using the GhostContainer backdoor and GitHub-hosted tooling, also exploiting Active Directory and RDP vulnerabilities.

### 10. Atomic macOS (AMOS) Stealer Activity Uses Deceptive Setup Guides
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** Unit 42 detailed ongoing Atomic macOS Stealer (AMOS) activity that uses deceptive fake setup guides to trick users into installing the malware and surrendering credentials and sensitive data.

### 11. North Korea-Linked Group Uses Undocumented Linux Toolkit Against South Korean Media, Automotive Sectors
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/cyber-south-korean-media-automotive
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** A likely North Korean APT group used a previously undocumented Linux espionage toolkit to compromise load balancers at South Korean media and automotive organizations, expanding into victim networks.

### 12. Google Releases Gemini 3.8 Live and Live Extended Thinking Speech Models
- **Source:** Simon Willison — https://simonwillison.net/2026/Sep/15/gemini-live/
- **Severity:** informational
- **Tags:** `model-release`, `google`, `llm`, `ai-launch`
- **Summary:** Google released Gemini 3.8 Live and Gemini 3.8 Live Extended Thinking, two speech-to-speech models. Simon Willison built a no-dependency browser UI for trying them out.

### 13. AWS STS Simplifies Session Token Size Limits, Adds Monitoring
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/aws-sts-simplifies-session-token-size-limits-and-adds-session-token-size-monitoring/
- **Severity:** informational
- **Tags:** `aws`, `iam`, `cloud-security`
- **Summary:** AWS STS replaced its separate packed-policy-size and session-token-size limits with a single unified 4,096-byte token size limit, and now reports session token size in API responses for monitoring.

## Skippable

- **[Virtual Event] What Every Enterprise Should Know About Securing Cloud Assets in the Age of AI** — Dark Reading. Event/webinar promo, no news content.
- **Microsoft says Copilot buttons still missing in classic Outlook** — BleepingComputer. Generic product bug, no security angle.
- **Webinar: What happens in the first hours of a Google Workspace breach** — BleepingComputer. Webinar promo, not news.
- **A brief history of AI executives calling for regulation** — The Verge AI. Opinion/retrospective piece, no news value.
- **Threat Intelligence Alone Won't Close the Exploitation Gap** — The Hacker News. Vendor-style opinion piece without concrete news.
- **Hackuity Raises $19 Million for AI-Powered Vulnerability Management** — SecurityWeek. Funding announcement, not security news.
- **Amazon launches Alexa+ in India with Hindi support** — TechCrunch AI. Regional product feature rollout, no security or model-capability substance.
- **Chrome, Firefox Updates Patch 115 Vulnerabilities** — SecurityWeek. Routine patch roundup, no single critical+exploited CVE called out.
- **Securing the unpatchable in an age of AI-driven vulnerabilities** — Cisco Talos. Generic vendor advisory content, no concrete finding.
- **Acronis Patches Exploited Vulnerability in cPanel Backup Plugin** — SecurityWeek. Duplicate coverage of CVE-2026-87886, folded into the Hacker News item above.
- **Windows Server 2022 reaches end of mainstream support next month** — BleepingComputer. Lifecycle/EOL notice, no security exploit.
- **Enterprises Warned of Attacks Exploiting WSO2 Vulnerability** — SecurityWeek. Duplicate coverage of CVE-2026-5430, folded into the Hacker News item above.
- **Oracle Patches 800+ Vulnerabilities in September 2026 Security Update** — SecurityWeek. Routine patch Tuesday roundup, no single actively exploited CVE named.
- **Google fixes actively exploited Android zero-day on Pixel devices** — BleepingComputer. Duplicate coverage of the Pixel modem zero-day, folded into the Hacker News item above.
- **We don't need AI regulation — leave safety to us, Nvidia's Jensen Huang says** — TechCrunch AI. Opinion/commentary piece, no news value.
- **AI and data centers are incredibly unpopular in every poll** — The Verge AI. Poll/sentiment analysis, not a security or model-capability story.
