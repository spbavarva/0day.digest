# Digest — 2026-05-26 PM

- Window: last 14h
- Raw items considered: 45
- Relevant: 17
- Skippable: 28

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** KnowledgeDeliver LMS Zero-Day Exploited to Deploy Godzilla Web Shell and Cobalt Strike — `2026-05-26-knowledgedeliver-lms-zero-day-godzilla-cobalt-strike.md`
- [x] **[HIGH]** Microsoft Copilot Cowork Allows Attacker-Controlled Email Images to Exfiltrate User Files — `2026-05-26-microsoft-copilot-cowork-data-exfiltration.md`
- [x] **[HIGH]** CISA Orders Federal Agencies to Patch Actively Exploited Drupal SQL Injection by Wednesday — `2026-05-26-cisa-kev-drupal-sqli-actively-exploited.md`
- [x] **[HIGH]** Microsoft Patches SharePoint RCE CVE-2026-45659 — No Special Conditions Required to Exploit — `2026-05-26-cve-2026-45659-sharepoint-rce.md`
- [x] **[HIGH]** CISA Adds LiteSpeed cPanel Plugin Privilege Escalation CVE-2026-48172 to KEV — Active Exploitation Confirmed — `2026-05-26-cve-2026-48172-litespeed-cpanel-privilege-escalation-kev.md`
- [x] **[HIGH]** Iranian APT Nimbus Manticore Deploys MiniFast and MiniJunk V2 via Phishing and SEO Poisoning — `2026-05-26-nimbus-manticore-minifast-minijunk-v2-phishing.md`
- [x] **[HIGH]** MuddyWater Uses DLL Side-Loading in Global Espionage Campaign Hitting 9 Countries — `2026-05-26-muddywater-dll-side-loading-espionage-campaign.md`
- [x] **[HIGH]** Lithuania Investigates Theft of 600,000 State Registry Records — Foreign Actor Suspected — `2026-05-26-lithuania-600k-state-registry-breach.md`
- [x] **[HIGH]** 7-Eleven Data Breach: ShinyHunters Expose Personal Data of 185,000 Customers — `2026-05-26-7-eleven-shinyhunters-data-breach-185k.md`
- [x] **[HIGH]** CVSS 10.0 DoS in ABB B&R Automation Runtime Threatens Critical Industrial Infrastructure — `2026-05-26-abb-br-automation-runtime-cvss10-dos.md`
- [x] **[HIGH]** CVSS 9.8 Hard-Coded Password in Eppendorf BioFlo 320 Bioreactor Grants Full Device Access — `2026-05-26-eppendorf-bioflo-320-hardcoded-password-cvss98.md`
- [x] **[MEDIUM]** Flashpoint Exposes 'The Com': Decentralized Criminal Network Blending Cyber Fraud and Real-World Violence — `2026-05-26-the-com-illicit-ecosystem-threat-intel.md`
- [x] **[MEDIUM]** Microsoft Defender for Endpoint Tests Automatic Isolation of Compromised Hosts to Block Lateral Movement — `2026-05-26-microsoft-defender-auto-isolate-compromised-endpoints.md`
- [x] **[MEDIUM]** Dutch Authorities Arrest Admins of Bulletproof Hosting Service Backing Russia-Aligned Threat Actors — `2026-05-26-bulletproof-hosting-admins-arrested-netherlands.md`
- [x] **[MEDIUM]** India's CERT-In Issues 12-Hour Patching Mandate for Internet-Facing Systems, Cites AI-Assisted Attacks — `2026-05-26-cert-in-12-hour-patching-mandate-ai-assisted-attacks.md`
- [x] **[INFORMATIONAL]** Anthropic Expands Claude Enterprise Security Governance With 28 New Vendor Integrations — `2026-05-26-anthropic-claude-enterprise-security-28-integrations.md`
- [x] **[INFORMATIONAL]** OWASP Incubates DockSec: Open-Source AI Tool Correlates Docker Vulnerability Scanners and Generates Dockerfile Fixes — `2026-05-26-docksec-ai-docker-vulnerability-scanner-owasp.md`

## Relevant (details)

### 1. KnowledgeDeliver LMS Zero-Day — Godzilla Web Shell + Cobalt Strike
- **Source:** The Hacker News — https://thehackernews.com/2026/05/knowledgedeliver-lms-flaw-exploited-to.html
- **Severity:** high
- **Tags:** `zero-day`, `rce`, `vulnerability`, `cve`, `malware`
- **Summary:** CVE-2026-5426 (CVSS 7.5) in KnowledgeDeliver LMS was exploited as a zero-day via hardcoded ASP.NET machineKey values enabling ViewState deserialization RCE. Attackers deployed Godzilla web shell and Cobalt Strike Beacon.

### 2. Microsoft Copilot Cowork Data Exfiltration via Prompt Injection
- **Source:** Simon Willison — https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything
- **Severity:** high
- **Tags:** `llm`, `microsoft`, `appsec`, `ai-safety`
- **Summary:** Microsoft Copilot Cowork can be manipulated via prompt injection to send emails that render external attacker-controlled images, exfiltrating user data. Classic agentic exfiltration attack on a production Microsoft AI product.

### 3. CISA Drupal SQL Injection KEV — Active Exploitation, Federal Deadline Wednesday
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-drupal-vulnerability/
- **Severity:** high
- **Tags:** `sqli`, `vulnerability`, `cve`
- **Summary:** CISA added an actively exploited Drupal SQL injection to the KEV catalog and ordered federal agencies to patch by Wednesday. Drupal is widely deployed across government and enterprise.

### 4. SharePoint RCE CVE-2026-45659 — CVSS 8.8, No Special Conditions
- **Source:** The Hacker News — https://thehackernews.com/2026/05/microsoft-patches-sharepoint-rce-flaw.html
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`, `microsoft`
- **Summary:** CVE-2026-45659 is a CVSS 8.8 SharePoint RCE requiring no specialized exploitation conditions. No active exploitation confirmed yet but low-complexity attack on a widely deployed platform warrants immediate patching.

### 5. LiteSpeed cPanel Plugin Privilege Escalation — CISA KEV, Actively Exploited
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/alerts/2026/05/26/cisa-adds-one-known-exploited-vulnerability-catalog
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`, `cve`
- **Summary:** CVE-2026-48172 in LiteSpeed cPanel Plugin confirmed exploited in the wild; added to CISA KEV. Common in web hosting environments; immediate patching required under BOD 22-01.

### 6. Nimbus Manticore Iranian APT — MiniFast and MiniJunk V2 via Phishing + SEO Poisoning
- **Source:** The Hacker News — https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html
- **Severity:** high
- **Tags:** `phishing`, `malware`, `vulnerability`
- **Summary:** UNC1549 / Nimbus Manticore is running a post-Iran-strike campaign against aviation and software sectors using two new malware variants (MiniFast, MiniJunk V2) delivered via phishing and SEO poisoning.

### 7. MuddyWater DLL Side-Loading Espionage Campaign — 9 Countries, Q1 2026
- **Source:** The Hacker News — https://thehackernews.com/2026/05/muddywater-uses-dll-side-loading-in.html
- **Severity:** high
- **Tags:** `malware`, `phishing`, `vulnerability`
- **Summary:** Iranian APT MuddyWater targeted 9 organizations across 9 countries using DLL side-loading in Q1 2026. Sectors hit: manufacturing, education, government, financial, professional services.

### 8. Lithuania 600k State Registry Records — Foreign Actor Breach
- **Source:** The Record (Recorded Future) — https://therecord.media/lithuania-investigates-theft-of-state-records
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** 600k+ Lithuanian state registry records (property and legal entity data) stolen by suspected foreign actor; investigation ongoing, attack vector undisclosed.

### 9. 7-Eleven Data Breach — ShinyHunters, 185k Records
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/7-eleven-data-breach-exposes-personal-information-of-185-000-people/
- **Severity:** high
- **Tags:** `data-breach`, `malware`
- **Summary:** ShinyHunters breached 7-Eleven in April 2026, exfiltrating PII of 183k+ people. Confirmed via Have I Been Pwned. Continues the group's retail loyalty database targeting pattern.

### 10. ABB B&R Automation Runtime — CVSS 10.0 DoS, Critical Infrastructure
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-146-04
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Summary:** CVSS 10.0 DoS in ABB B&R Automation Runtime SDM can halt operations in critical manufacturing, energy, and water/wastewater infrastructure. Patch available from ABB.

### 11. Eppendorf BioFlo 320 — CVSS 9.8, Hardcoded Password, Healthcare ICS
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-146-01
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Summary:** CVE-2026-7251 (CVSS 9.8) — hardcoded password in all BioFlo 320 bioreactor versions grants full device access. Healthcare deployments worldwide; users cannot mitigate without vendor fix.

### 12. "The Com" — Flashpoint Threat Intel on Hybrid Criminal Ecosystem
- **Source:** Flashpoint — https://flashpoint.io/blog/understanding-illicit-ecosystems-the-com/
- **Severity:** medium
- **Tags:** `phishing`, `ransomware`, `malware`
- **Summary:** Flashpoint details The Com's decentralized structure blending cyber fraud, extortion, and real-world violence. Loose architecture and minor recruitment make it resilient; relevant for fraud/social-engineering incident attribution.

### 13. Microsoft Defender for Endpoint — Automatic Endpoint Isolation (Testing)
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-defender-can-now-automatically-isolate-hacked-endpoints/
- **Severity:** medium
- **Tags:** `microsoft`, `appsec`
- **Summary:** Microsoft is testing automatic endpoint isolation in Defender for Endpoint to cut lateral movement without manual intervention. Teams should validate exclusion lists before enabling.

### 14. Bulletproof Hosting Admins Arrested in Netherlands — Russia-Aligned Customers
- **Source:** SecurityWeek — https://www.securityweek.com/admins-of-bulletproof-hosting-service-used-by-russian-hackers-arrested-in-netherlands/
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** Dutch authorities arrested two operators of a bulletproof hosting service used by Russia-aligned threat actors. Watch for actor migration to replacement infrastructure.

### 15. CERT-In 12-Hour Patching Mandate — AI-Assisted Attack Motivation
- **Source:** The Hacker News — https://thehackernews.com/2026/05/cert-in-mandates-12-hour-patching-for.html
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`, `vulnerability`
- **Summary:** India's CERT-In mandates 12-hour patching for critical internet-facing vulnerabilities, citing AI/LLM-accelerated exploitation. Sets a precedent for national CERT patching SLAs.

### 16. Anthropic Claude — 28 New Enterprise Security Integrations
- **Source:** SecurityWeek — https://www.securityweek.com/anthropic-expands-claudes-enterprise-security-reach-with-28-new-integrations/
- **Severity:** informational
- **Tags:** `anthropic`, `llm`, `ai-launch`
- **Summary:** Anthropic announced 28 new Claude integrations with CrowdStrike, Palo Alto, Okta, Zscaler, Wiz, and others targeting enterprise security governance and compliance use cases.

### 17. DockSec — OWASP Incubator AI Docker Vulnerability Scanner
- **Source:** SecurityWeek — https://www.securityweek.com/open-source-docksec-uses-ai-to-cut-through-vulnerability-noise-in-docker-images/
- **Severity:** informational
- **Tags:** `container-security`, `appsec`, `llm`
- **Summary:** DockSec is an OWASP incubator project using AI to correlate multi-scanner Docker image findings and generate plain-English remediation guidance and Dockerfile fixes.

## Skippable

- **Welcoming the AWS Customer Incident Response Team** — AWS Security Blog. Republished 2022 post; CIRT service marketing, no new security content.
- **OpenRouter more than doubles valuation to $1.3B** — TechCrunch AI. VC valuation story; no security or model-release angle.
- **Well-Architected Best Practices for Software Supply Chain Security** — AWS Security Blog. Educational best-practices blog referencing past attacks; no new incident news.
- **This startup is betting India's gig economy can train the world's robots** — TechCrunch AI. Physical AI data collection startup; no security relevance.
- **Quoting Paul Graham** — Simon Willison. Opinion on AI-generated email; no news value.
- **Universal Music Group and TikTok renew agreement to combat unauthorized AI music** — TechCrunch AI. Entertainment licensing deal; no cybersecurity angle.
- **TechCrunch Disrupt 2026 Early Bird ticket rates end May 29** — TechCrunch AI. Conference ticket promotion.
- **Sundar Pichai on AI, the future of search** — The Verge AI. Podcast interview; no breaking news.
- **Iranian APT Targets Aviation, Software Companies With Updated Tools** — SecurityWeek. Duplicate of Nimbus Manticore item; The Hacker News version has more technical detail.
- **Nobody wants to tell me why they only listen to their own Suno slop** — The Verge AI. Cultural opinion on AI music; no security relevance.
- **Webinar: Too many tools are slowing network incident response** — BleepingComputer. Webinar promotion.
- **Remembering Tim Wilson** — Dark Reading. Memorial tribute; not a security news item.
- **AI warfare is already here** — The Verge AI. Policy/opinion on autonomous weapons; no actionable near-term news.
- **ABB Ability Camera Connect** — CISA Alerts. Routine 3rd-party VLC component update; no active exploitation.
- **ABB LVS MConfig** — CISA Alerts. CVSS 7.4, local network access required; limited exploitability.
- **ABB AC500 V2** — CISA Alerts. CVSS 5.8 buffer over-read; medium severity, limited impact.
- **ABB Terra AC** — CISA Alerts. EV charger firmware vulnerability; no CVSS shown, no active exploitation.
- **ABB AbilityTM Zenon Remote Transport** — CISA Alerts. Unauthorized reboot; not remotely exploitable without prior network access.
- **185,000 Likely Impacted by 7-Eleven Data Breach** — SecurityWeek. Duplicate of BleepingComputer item; BleepingComputer version is more detailed.
- **[THN Webinar] New AI DDoS Attacks Are Smarter** — The Hacker News. Webinar promotion; no substantive technical content.
- **Hackers Exploited KnowledgeDeliver Zero-Day for Web Shell Deployment** — SecurityWeek. Duplicate of The Hacker News KnowledgeDeliver item.
- **Watch on Demand: Threat Detection & Incident Response Summit** — SecurityWeek. Event promotion.
- **MFA Prompt Bombing: Why Your Second Factor Isn't Saving You** — The Hacker News. Educational/marketing article; no new technique or incident.
- **Lithuania Suspects Foreign Involvement in Data Leak** — SecurityWeek. Duplicate of The Record Lithuania item.
- **Uber president says AI spending is getting 'harder to justify'** — The Verge AI. Business ROI commentary; no security angle.
- **How Varonis Atlas integrates Claude Compliance API for AI governance** — BleepingComputer. Sponsored vendor marketing content.
- **AppOmni's Marlin AI Brings Autonomous Investigation to SaaS Security** — SecurityWeek. Product launch announcement without technical depth.
- **Microsoft: Domain Controller lookup may fail on Windows Server 2016** — BleepingComputer. Patch regression operational issue; not a security vulnerability.
