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
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `rce`, `vulnerability`, `cve`, `malware`
- **Slug:** `2026-05-26-knowledgedeliver-lms-zero-day-godzilla-cobalt-strike.md`
- **Must-know:** no
- **Summary:** CVE-2026-5426 (CVSS 7.5) in KnowledgeDeliver LMS (popular in Japan) was exploited as a zero-day via hardcoded ASP.NET machineKey values enabling ViewState deserialization RCE. Attackers deployed the Godzilla web shell and Cobalt Strike Beacon for post-exploitation.

### 2. Microsoft Copilot Cowork Data Exfiltration via Prompt Injection
- **Source:** Simon Willison — https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** high
- **Tags:** `llm`, `microsoft`, `appsec`, `ai-safety`
- **Slug:** `2026-05-26-microsoft-copilot-cowork-data-exfiltration.md`
- **Must-know:** no
- **Summary:** Microsoft Copilot Cowork can be manipulated via prompt injection to send emails to a user's own inbox, which render external images that exfiltrate data to attacker-controlled servers. Classic agentic exfiltration attack surface on a production Microsoft product.

### 3. CISA Drupal SQL Injection KEV — Active Exploitation, Federal Deadline Wednesday
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-drupal-vulnerability/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `sqli`, `vulnerability`, `cve`
- **Slug:** `2026-05-26-cisa-kev-drupal-sqli-actively-exploited.md`
- **Must-know:** no
- **Summary:** CISA has added an actively exploited Drupal SQL injection to the KEV catalog and ordered federal agencies to patch by Wednesday. Drupal is widely deployed in government and enterprise environments.

### 4. SharePoint RCE CVE-2026-45659 — CVSS 8.8, No Special Conditions
- **Source:** The Hacker News — https://thehackernews.com/2026/05/microsoft-patches-sharepoint-rce-flaw.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`, `microsoft`
- **Slug:** `2026-05-26-cve-2026-45659-sharepoint-rce.md`
- **Must-know:** no
- **Summary:** Microsoft patched CVE-2026-45659, a CVSS 8.8 SharePoint RCE stemming from deserialization of untrusted data with no specialized exploitation conditions required. Active exploitation not yet confirmed but the low-complexity attack on a broadly deployed product warrants urgent patching.

### 5. LiteSpeed cPanel Plugin Privilege Escalation — CISA KEV, Actively Exploited
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/alerts/2026/05/26/cisa-adds-one-known-exploited-vulnerability-catalog
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`, `cve`
- **Slug:** `2026-05-26-cve-2026-48172-litespeed-cpanel-privilege-escalation-kev.md`
- **Must-know:** no
- **Summary:** CVE-2026-48172 in the LiteSpeed cPanel Plugin has been confirmed exploited in the wild and added to CISA's KEV catalog. Common in web hosting environments; immediate patching required under BOD 22-01 for federal agencies.

### 6. Nimbus Manticore Iranian APT — MiniFast and MiniJunk V2 via Phishing + SEO Poisoning
- **Source:** The Hacker News — https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `malware`, `vulnerability`
- **Slug:** `2026-05-26-nimbus-manticore-minifast-minijunk-v2-phishing.md`
- **Must-know:** no
- **Summary:** UNC1549 / Nimbus Manticore has launched a post-Iran-strike campaign targeting aviation and software sectors in the U.S., Europe, and Middle East, deploying two new malware variants (MiniFast, MiniJunk V2) via phishing and SEO poisoning.

### 7. MuddyWater DLL Side-Loading Espionage Campaign — 9 Countries, Q1 2026
- **Source:** The Hacker News — https://thehackernews.com/2026/05/muddywater-uses-dll-side-loading-in.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`, `vulnerability`
- **Slug:** `2026-05-26-muddywater-dll-side-loading-espionage-campaign.md`
- **Must-know:** no
- **Summary:** Iranian APT MuddyWater ran an active Q1 2026 espionage campaign using DLL side-loading against manufacturing, education, government, financial, and professional services targets across 9 countries and 4 continents, per Symantec and Carbon Black.

### 8. Lithuania 600k State Registry Records — Foreign Actor Breach
- **Source:** The Record (Recorded Future) — https://therecord.media/lithuania-investigates-theft-of-state-records
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `2026-05-26-lithuania-600k-state-registry-breach.md`
- **Must-know:** no
- **Summary:** Lithuania's Prosecutor General has opened an investigation after 600k+ state registry records (property and legal entity data) were stolen by a suspected foreign actor. Attack vector and attribution details remain undisclosed.

### 9. 7-Eleven Data Breach — ShinyHunters, 185k Records
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/7-eleven-data-breach-exposes-personal-information-of-185-000-people/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `malware`
- **Slug:** `2026-05-26-7-eleven-shinyhunters-data-breach-185k.md`
- **Must-know:** no
- **Summary:** ShinyHunters breached 7-Eleven in April 2026 and exfiltrated PII (email, name, address, DOB) of 183,000+ individuals, confirmed by Have I Been Pwned. Continues the group's pattern of targeting retail loyalty databases.

### 10. ABB B&R Automation Runtime — CVSS 10.0 DoS, Critical Infrastructure
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-146-04
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Slug:** `2026-05-26-abb-br-automation-runtime-cvss10-dos.md`
- **Must-know:** no
- **Summary:** A CVSS 10.0 denial-of-service vulnerability in ABB B&R Automation Runtime SDM can halt industrial processes in critical manufacturing, energy, and water/wastewater infrastructure. ABB has released an update; operators should patch and segment the SDM interface immediately.

### 11. Eppendorf BioFlo 320 — CVSS 9.8, Hardcoded Password, Healthcare ICS
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-146-01
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Slug:** `2026-05-26-eppendorf-bioflo-320-hardcoded-password-cvss98.md`
- **Must-know:** no
- **Summary:** CVE-2026-7251 (CVSS 9.8) — a hardcoded password in all versions of the Eppendorf BioFlo 320 bioreactor grants full device access. Deployed worldwide in healthcare/biotech; users cannot change the credential themselves and must await a vendor fix while isolating the device.

### 12. "The Com" — Flashpoint Threat Intel on Hybrid Criminal Ecosystem
- **Source:** Flashpoint — https://flashpoint.io/blog/understanding-illicit-ecosystems-the-com/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `phishing`, `ransomware`, `malware`
- **Slug:** `2026-05-26-the-com-illicit-ecosystem-threat-intel.md`
- **Must-know:** no
- **Summary:** Flashpoint details The Com, a decentralized criminal ecosystem blending hacking, extortion, and real-world violence. Its loose structure and minor recruitment make it resilient to takedowns and a growing threat multiplier for fraud and social engineering operations.

### 13. Microsoft Defender for Endpoint — Automatic Endpoint Isolation (Testing)
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-defender-can-now-automatically-isolate-hacked-endpoints/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `microsoft`, `appsec`
- **Slug:** `2026-05-26-microsoft-defender-auto-isolate-compromised-endpoints.md`
- **Must-know:** no
- **Summary:** Microsoft is testing automatic endpoint isolation in Defender for Endpoint to cut off lateral movement without manual analyst action. Teams enabling the feature should validate exclusion lists to avoid false-positive isolation of critical infrastructure.

### 14. Bulletproof Hosting Admins Arrested in Netherlands — Russia-Aligned Customers
- **Source:** SecurityWeek — https://www.securityweek.com/admins-of-bulletproof-hosting-service-used-by-russian-hackers-arrested-in-netherlands/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `2026-05-26-bulletproof-hosting-admins-arrested-netherlands.md`
- **Must-know:** no
- **Summary:** Dutch authorities arrested two operators of a bulletproof hosting service used by Russia-aligned threat actors. The infrastructure disruption should prompt TI teams to watch for actor migration to replacement hosting.

### 15. CERT-In 12-Hour Patching Mandate — AI-Assisted Attack Motivation
- **Source:** The Hacker News — https://thehackernews.com/2026/05/cert-in-mandates-12-hour-patching-for.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`, `vulnerability`
- **Slug:** `2026-05-26-cert-in-12-hour-patching-mandate-ai-assisted-attacks.md`
- **Must-know:** no
- **Summary:** India's CERT-In has issued guidelines requiring 12-hour patching of critical internet-facing vulnerabilities where feasible, explicitly motivated by AI/LLM-accelerated exploitation timelines. Sets a precedent other national CERTs may follow.

### 16. Anthropic Claude — 28 New Enterprise Security Integrations
- **Source:** SecurityWeek — https://www.securityweek.com/anthropic-expands-claudes-enterprise-security-reach-with-28-new-integrations/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `anthropic`, `llm`, `ai-launch`
- **Slug:** `2026-05-26-anthropic-claude-enterprise-security-28-integrations.md`
- **Must-know:** no
- **Summary:** Anthropic announced 28 new Claude integrations with major security vendors (CrowdStrike, Palo Alto, Okta, Zscaler, Wiz, etc.) targeting enterprise governance, investigation, and compliance use cases.

### 17. DockSec — OWASP Incubator AI Docker Vulnerability Scanner
- **Source:** SecurityWeek — https://www.securityweek.com/open-source-docksec-uses-ai-to-cut-through-vulnerability-noise-in-docker-images/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `container-security`, `appsec`, `llm`
- **Slug:** `2026-05-26-docksec-ai-docker-vulnerability-scanner-owasp.md`
- **Must-know:** no
- **Summary:** DockSec is an OWASP incubator project that uses AI to correlate Docker image scanner findings from multiple tools and generate plain-English remediation guidance and exact Dockerfile fixes.

## Skippable

- **Welcoming the AWS Customer Incident Response Team** — AWS Security Blog. Republished 2022 post; generic CIRT service marketing, no new security content.
- **OpenRouter more than doubles valuation to $1.3B** — TechCrunch AI. VC funding/valuation story; no security or model-release angle.
- **Well-Architected Best Practices for Software Supply Chain Security** — AWS Security Blog. Educational best-practices blog referencing past attacks already covered; no new incident news.
- **This startup is betting India's gig economy can train the world's robots** — TechCrunch AI. Physical AI data collection startup; no security relevance.
- **Quoting Paul Graham** — Simon Willison. Opinion on AI-generated email writing quality; no news value.
- **Universal Music Group and TikTok renew agreement to combat unauthorized AI music** — TechCrunch AI. Entertainment licensing deal; no cybersecurity angle.
- **TechCrunch Disrupt 2026 Early Bird ticket rates end May 29** — TechCrunch AI. Conference ticket promotion.
- **Sundar Pichai on AI, the future of search, and what's happening to the web** — The Verge AI. Podcast/interview; opinion, no breaking news value.
- **Iranian APT Targets Aviation, Software Companies With Updated Tools** — SecurityWeek. Duplicate of item 43 (Nimbus Manticore); The Hacker News version has more technical detail.
- **Nobody wants to tell me why they only listen to their own Suno slop** — The Verge AI. Cultural opinion on AI-generated music; no security relevance.
- **Webinar: Too many tools are slowing network incident response** — BleepingComputer. Webinar promotion; no news value.
- **Remembering Tim Wilson, Whose Legacy Lives on at Dark Reading** — Dark Reading. Memorial tribute to Dark Reading co-founder; not a security news item.
- **AI warfare is already here** — The Verge AI. Long-form policy/opinion on autonomous weapons; no immediate actionable news.
- **ABB Ability Camera Connect** — CISA Alerts. Routine ICS advisory for outdated VLC 3rd-party component in a camera product; low impact, no active exploitation.
- **ABB LVS MConfig** — CISA Alerts. CVSS 7.4, cleartext storage in memory, requires local network access; limited reach and no active exploitation.
- **ABB AC500 V2** — CISA Alerts. CVSS 5.8, buffer over-read leaking Modbus telegram fragments; medium severity, limited exploitability.
- **ABB Terra AC** — CISA Alerts. EV charger firmware vulnerability; no CVSS shown, no active exploitation confirmed, lower priority than other ICS advisories covered.
- **ABB AbilityTM Zenon Remote Transport Vulnerability** — CISA Alerts. Unauthorized reboot trigger; not remotely exploitable without prior network access, no active exploitation.
- **185,000 Likely Impacted by 7-Eleven Data Breach** — SecurityWeek. Duplicate of BleepingComputer item 44; BleepingComputer version is more detailed.
- **[THN Webinar] New AI DDoS Attacks Are Smarter** — The Hacker News. Webinar promotion dressed as news; no substantive technical content.
- **Hackers Exploited KnowledgeDeliver Zero-Day for Web Shell Deployment** — SecurityWeek. Duplicate of The Hacker News item 45; The Hacker News version has more kill-chain detail.
- **Watch on Demand: Threat Detection & Incident Response Summit** — SecurityWeek. Event promotion.
- **MFA Prompt Bombing: Why Your Second Factor Isn't Saving You** — The Hacker News. Educational/marketing article about MFA bypass; no new technique or incident, no news value.
- **Lithuania Suspects Foreign Involvement in Data Leak** — SecurityWeek. Duplicate of The Record item 10; The Record version appeared earlier.
- **Uber president says AI spending is getting 'harder to justify'** — The Verge AI. Business/ROI commentary; no security or model-launch angle.
- **How Varonis Atlas integrates Claude Compliance API for AI governance** — BleepingComputer. Vendor marketing content sponsored post; no independent news value.
- **AppOmni's Marlin AI Brings Autonomous Investigation to SaaS Security** — SecurityWeek. AI security product launch announcement without technical depth.
- **Microsoft: Domain Controller lookup may fail on Windows Server 2016** — BleepingComputer. Operational patch regression issue; not a security vulnerability or exploit.
