# Digest — 2026-05-13 PM

- Window: last 14h
- Raw items considered: 44
- Relevant: 14
- Skippable: 30

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Unpatched Windows BitLocker Zero-Days YellowKey and GreenPlasma: PoC Released — `2026-05-13-windows-bitlocker-zero-day-yellowkey-greenplasma.md`
- [x] **[CRITICAL]** May 2026 Patch Tuesday: 138 CVEs Including Critical Zero-Click Outlook Flaw CVE-2026-40361 — `2026-05-13-may-2026-patch-tuesday-outlook-zero-click-cve-2026-40361.md`
- [x] **[HIGH]** Foxconn North American Factories Hit by Nitrogen Ransomware, 8TB Stolen — `2026-05-13-foxconn-nitrogen-ransomware-north-america.md`
- [x] **[HIGH]** Google Project Zero Demonstrates 0-Click Exploit Chain for Pixel 10 — `2026-05-13-google-project-zero-pixel10-zero-click-exploit-chain.md`
- [x] **[HIGH]** Fortinet and Ivanti Patch Critical RCE and Information Disclosure Flaws — `2026-05-13-fortinet-ivanti-critical-rce-patches.md`
- [x] **[HIGH]** FamousSparrow APT Targets Azerbaijani Oil and Gas Firm via Microsoft Exchange — `2026-05-13-famoussparrow-apt-azerbaijani-energy-exchange.md`
- [x] **[HIGH]** LatAm Threat Actors Use AI Agents to Generate Custom Attack Tools on the Fly — `2026-05-13-latam-ai-custom-hacking-tools.md`
- [x] **[HIGH]** OpenLoop Health Breach Exposes 716,000 Patients' Personal Data — `2026-05-13-openloop-health-breach-716k.md`
- [x] **[MEDIUM]** SentinelOne: Cloud Secrets and AI Infrastructure Are Merging Attack Surfaces — `2026-05-13-sentinelone-cloud-secrets-ai-risk.md`
- [x] **[MEDIUM]** Microsoft MDASH and Palo Alto Mythos Use AI to Find Hundreds of Vulnerabilities — `2026-05-13-microsoft-mdash-ai-vulnerability-discovery.md`
- [x] **[MEDIUM]** Mandiant M-Trends 2026: Most Remediation Programs Never Confirm Fixes Work — `2026-05-13-mandiant-mtrends-2026-remediation-gap.md`
- [x] **[MEDIUM]** OpenAI Details Secure Sandbox Architecture for Running Codex on Windows — `2026-05-13-openai-codex-windows-sandbox.md`
- [x] **[MEDIUM]** Congress Scrutinizes Instructure Over Canvas LMS Data Breach and Service Disruption — `2026-05-13-instructure-canvas-breach-congressional-scrutiny.md`
- [x] **[INFORMATIONAL]** UK Proposes Computer Misuse Act Overhaul to Protect Security Researchers — `2026-05-13-uk-computer-misuse-act-reform.md`

## Relevant (details)

### 1. Unpatched Windows BitLocker Zero-Days YellowKey and GreenPlasma: PoC Released
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `privilege-escalation`, `microsoft`, `cve`
- **Slug:** `2026-05-13-windows-bitlocker-zero-day-yellowkey-greenplasma`
- **Must-know:** no
- **Summary:** A researcher published PoC exploits for two unpatched Windows flaws — YellowKey (BitLocker drive bypass) and GreenPlasma (privilege escalation) — with no Microsoft patch available. Public PoC code makes exploitation a near-term threat for any organization relying on BitLocker for data-at-rest protection.

### 2. May 2026 Patch Tuesday: 138 CVEs Including Critical Zero-Click Outlook Flaw CVE-2026-40361
- **Source:** SecurityWeek — https://www.securityweek.com/microsoft-patches-critical-zero-click-outlook-vulnerability-threatening-enterprises/ | The Hacker News — https://thehackernews.com/2026/05/microsoft-patches-138-vulnerabilities.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `microsoft`, `rce`, `privilege-escalation`
- **Slug:** `2026-05-13-may-2026-patch-tuesday-outlook-zero-click-cve-2026-40361`
- **Must-know:** no
- **Summary:** Microsoft patched 138 vulnerabilities — 30 Critical — including DNS and Netlogon RCE flaws. CVE-2026-40361, a zero-click Outlook bug compared to the 2015 "BadWinmail" enterprise killer, is the headline item; no CVEs are actively exploited at time of release.

### 3. Foxconn North American Factories Hit by Nitrogen Ransomware, 8TB Stolen
- **Source:** SecurityWeek — https://www.securityweek.com/foxconn-confirms-north-american-factories-hit-by-cyberattack/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`, `data-breach`
- **Slug:** `2026-05-13-foxconn-nitrogen-ransomware-north-america`
- **Must-know:** no
- **Summary:** The Nitrogen ransomware group claims to have hit Foxconn's North American factories, stealing 8TB of data including confidential documents. The world's largest electronics manufacturer confirmed the attack and says affected factories are working to restore operations.

### 4. Google Project Zero Demonstrates 0-Click Exploit Chain for Pixel 10
- **Source:** Google Project Zero — https://projectzero.google/2026/05/pixel-10-exploit.html
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `rce`
- **Slug:** `2026-05-13-google-project-zero-pixel10-zero-click-exploit-chain`
- **Must-know:** no
- **Summary:** Project Zero extended its Pixel 9 0-click exploit chain to the Pixel 10, building on CVE-2025-54957 (Dolby, patched Jan 2026) with a second-stage exploit to reach root on current Pixel hardware. This is defensive research shared with Google ahead of publication.

### 5. Fortinet and Ivanti Patch Critical RCE and Information Disclosure Flaws
- **Source:** SecurityWeek — https://www.securityweek.com/fortinet-ivanti-patch-critical-vulnerabilities/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `2026-05-13-fortinet-ivanti-critical-rce-patches`
- **Must-know:** no
- **Summary:** Fortinet and Ivanti released patches for critical flaws enabling arbitrary code execution and information disclosure. Both vendors have a consistent track record of rapid in-the-wild exploitation after patch release; internet-facing appliances should be prioritized immediately.

### 6. FamousSparrow APT Targets Azerbaijani Oil and Gas Firm via Microsoft Exchange
- **Source:** The Hacker News — https://thehackernews.com/2026/05/azerbaijani-energy-firm-hit-by-repeated.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `microsoft`, `rce`, `apt`
- **Slug:** `2026-05-13-famoussparrow-apt-azerbaijani-energy-exchange`
- **Must-know:** no
- **Summary:** Bitdefender attributes a multi-wave intrusion against an Azerbaijani oil and gas company to China-linked FamousSparrow (UAT-9244), exploiting Microsoft Exchange repeatedly from December 2025 through February 2026. The group's expansion from hospitality and telecom into critical energy infrastructure marks a notable target shift.

### 7. LatAm Threat Actors Use AI Agents to Generate Custom Attack Tools on the Fly
- **Source:** Dark Reading — https://www.darkreading.com/cloud-security/ai-agents-generate-custom-hacking-tools
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ai-safety`, `llm`, `malware`
- **Slug:** `2026-05-13-latam-ai-custom-hacking-tools`
- **Must-know:** no
- **Summary:** Two threat campaigns targeting Mexico and Brazil entities used AI agents to generate custom attack tooling in real time during live intrusions, enabling lower-skill actors to field bespoke payloads previously requiring specialist development. Signature-based detection is increasingly insufficient against this AI-assisted attack model.

### 8. OpenLoop Health Breach Exposes 716,000 Patients' Personal Data
- **Source:** SecurityWeek — https://www.securityweek.com/716000-impacted-by-openloop-health-data-breach/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `vulnerability`
- **Slug:** `2026-05-13-openloop-health-breach-716k`
- **Must-know:** no
- **Summary:** Telehealth platform OpenLoop Health disclosed a January 2026 breach exposing personal data of 716,000 individuals. Specific data categories were not disclosed but likely include HIPAA-covered health PII given the platform's virtual care services.

### 9. SentinelOne: Cloud Secrets and AI Infrastructure Are Merging Attack Surfaces
- **Source:** SentinelOne Labs — https://www.sentinelone.com/blog/the-convergence-of-cloud-secrets-and-ai-risk/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `cloud-security`, `llm`, `iam`, `ai-safety`
- **Slug:** `2026-05-13-sentinelone-cloud-secrets-ai-risk`
- **Must-know:** no
- **Summary:** SentinelOne's report maps how credential theft and AI infrastructure exposure are converging: attackers who compromise cloud secrets in modern environments can pivot to AI training pipelines and inference endpoints, not just storage and compute. Key risk areas include hardcoded keys in repos and over-permissioned service accounts for AI agents.

### 10. Microsoft MDASH and Palo Alto Mythos Use AI to Find Hundreds of Vulnerabilities
- **Source:** The Hacker News — https://thehackernews.com/2026/05/microsofts-mdash-ai-system-finds-16.html | SecurityWeek — https://www.securityweek.com/microsoft-palo-alto-networks-find-many-vulnerabilities-by-using-ai-on-their-own-code/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `microsoft`, `vulnerability`, `llm`, `ai-safety`
- **Slug:** `2026-05-13-microsoft-mdash-ai-vulnerability-discovery`
- **Must-know:** no
- **Summary:** Microsoft's MDASH agentic scanning system found 16 vulnerabilities fixed in this month's Patch Tuesday; Palo Alto's Mythos found dozens more in its own code. Microsoft has already patched 500+ CVEs in 2026's first five months, on pace to break its annual record as AI-driven discovery accelerates faster than remediation capacity.

### 11. Mandiant M-Trends 2026: Most Remediation Programs Never Confirm Fixes Work
- **Source:** The Hacker News — https://thehackernews.com/2026/05/most-remediation-programs-never-confirm.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `appsec`, `devsecops`
- **Slug:** `2026-05-13-mandiant-mtrends-2026-remediation-gap`
- **Must-know:** no
- **Summary:** Mandiant M-Trends 2026 highlights that mean time to exploit is now estimated at negative seven days (attackers move before patches deploy), while median time to remediate edge devices sits at 32 days — and most programs never validate that applied patches actually worked. Autonomous post-patch validation is recommended as a core remediation workflow.

### 12. OpenAI Details Secure Sandbox Architecture for Running Codex on Windows
- **Source:** OpenAI Blog — https://openai.com/index/building-codex-windows-sandbox
- **Section:** AI — Labs & Model Launches
- **Severity:** medium
- **Tags:** `openai`, `llm`, `ai-safety`, `appsec`
- **Slug:** `2026-05-13-openai-codex-windows-sandbox`
- **Must-know:** no
- **Summary:** OpenAI published technical details of the sandbox constraining Codex's file access and network reach on Windows, addressing the risk that AI coding agents could become local privilege-escalation or exfiltration vectors. Useful architecture reference for teams building or evaluating agentic code-execution environments.

### 13. Congress Scrutinizes Instructure Over Canvas LMS Data Breach and Service Disruption
- **Source:** SecurityWeek — https://www.securityweek.com/government-to-scrutinize-instructure-on-canvas-disruption-data-breach/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `2026-05-13-instructure-canvas-breach-congressional-scrutiny`
- **Must-know:** no
- **Summary:** The House Committee on Homeland Security has demanded a briefing from Instructure on a Canvas LMS breach and service disruption; Canvas serves tens of millions of US students and educators. Scope of the breach has not been publicly disclosed; congressional pressure typically accelerates mandatory disclosure.

### 14. UK Proposes Computer Misuse Act Overhaul to Protect Security Researchers
- **Source:** The Record (Recorded Future) — https://therecord.media/uk-moves-to-shield-security-researchers-cybercrime
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `appsec`, `devsecops`
- **Slug:** `2026-05-13-uk-computer-misuse-act-reform`
- **Must-know:** no
- **Summary:** The UK has outlined reforms to the Computer Misuse Act 1990 that would create a legal defense for authorized security research — currently absent from UK law — as part of a broader national security legislation package. UK-based researchers and red-teamers should follow the legislative progress closely.

## Skippable

- **European Commission head pushes teen social media access law** — The Record. EU legislative push on age verification; no technical security content.
- **Mark Zuckerberg announces 'completely private' encrypted Meta AI chat** — The Verge AI. Privacy product feature launch; no vulnerability or incident.
- **Who trusts Sam Altman?** — TechCrunch AI. Opinion piece on Altman trial testimony; no news value.
- **Origin Lab raises $8M for video game data marketplace** — TechCrunch AI. Startup funding; no security angle.
- **PCI PIN and P2PE compliance packages for AWS Payment Cryptography** — AWS Security Blog. Compliance certification announcement; not security news.
- **Quoting Boris Mann** — Simon Willison. Opinion/quote on AI agent terminology; no news value.
- **The new era of SaMD: cloud infrastructure for digital health** — Google Cloud Security. GCP marketing content.
- **Anthropic courts small business owners** — TechCrunch AI. Business strategy; no technical content.
- **Webinar tomorrow: Why security alone won't stop modern attacks** — BleepingComputer. Webinar promotion.
- **Microsoft fixes BitLocker recovery issue only for Windows 11 users** — BleepingComputer. Routine bug fix for a separate BitLocker boot-loop issue unrelated to the YellowKey zero-day.
- **Microsoft doesn't want any of this** — The Verge AI. Opinion/commentary on Musk v. Altman trial.
- **Amazon launches an AI shopping assistant** — TechCrunch AI. Non-security product launch.
- **Sweet Security Launches Agentic AI Red Teaming** — SecurityWeek. Vendor product launch with limited independent research value.
- **Microsoft fixes Windows Autopatch bug installing restricted drivers** — BleepingComputer. Routine bug fix.
- **Introducing the 6 stages at TechCrunch Disrupt 2026** — TechCrunch AI. Conference promotion.
- **Anthropic now has more business customers than OpenAI** — TechCrunch AI. Business metrics; no technical content.
- **WhatsApp adds incognito mode in Meta AI chats** — TechCrunch AI. Duplicate of the Meta AI Incognito Chat story.
- **Microsoft's MDASH AI System Finds 16 Windows Flaws** — The Hacker News. Merged as secondary source into the MDASH/Mythos post (item 10 above).
- **Webinar Today: ROI for Cyber-Physical Security Programs** — SecurityWeek. Webinar promotion.
- **Poppy debuts a proactive AI assistant** — TechCrunch AI. Non-security consumer app launch.
- **China's 'FamousSparrow' APT Nests in South Caucasus Energy Firm** — Dark Reading. Duplicate of the FamousSparrow story; The Hacker News used as primary source.
- **Alexa is moving into Amazon.com** — The Verge AI. Duplicate of Amazon AI shopping assistant item.
- **Microsoft on pace to break annual vulnerability record** — The Record. Incorporated as supporting context into the MDASH/Mythos post.
- **Foxconn confirms cyberattack claimed by Nitrogen ransomware gang** — BleepingComputer. Duplicate of the Foxconn story; SecurityWeek used as primary source.
- **73 Seconds to Breach, 24 Hours to Patch** — BleepingComputer. Picus Security vendor marketing disguised as news.
- **Adaption aims big with AutoScientist** — TechCrunch AI. AI model self-training tool; no security angle.
- **Microsoft says some users can't install Office on Windows 365** — BleepingComputer. Routine IT installation issue; no security relevance.
- **[Webinar] How Modern Attack Paths Cross Code, Pipelines, and Cloud** — The Hacker News. Wiz webinar promotion.
- **Microsoft Patches 138 Vulnerabilities, Including DNS and Netlogon RCE Flaws** — The Hacker News. Merged as secondary source into the Patch Tuesday post (item 2 above).
- **Breaking things to keep them safe with Philippe Laulheret** — Cisco Talos. Career/human interest content; no news value.
