# Digest — 2026-04-09 PM

- Window: last 14h
- Raw items considered: 31
- Relevant: 14
- Skippable: 17

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** EngageLab SDK Flaw Exposed 50 Million Android Users Including 30 Million Crypto Wallets — `2026-04-09-engagelab-sdk-flaw-50m-android-users.md`
- [x] **[CRITICAL]** Smart Slider 3 Pro Update System Hijacked to Deliver Backdoored WordPress and Joomla Versions — `2026-04-09-smart-slider-supply-chain-wordpress-joomla.md`
- [x] **[HIGH]** BlueHammer: Researcher Drops PoC for Unpatched Windows Local Privilege Escalation Zero-Day — `2026-04-09-bluehammer-windows-zero-day-poc.md`
- [x] **[HIGH]** UAT-10362 Deploys Novel LucidRook Malware Against Taiwanese NGOs in Spear-Phishing Campaign — `2026-04-09-lucidrook-malware-uat-10362-taiwan.md`
- [x] **[HIGH]** VENOM Phishing-as-a-Service Platform Targets C-Suite Executives' Microsoft Credentials — `2026-04-09-venom-phaas-executive-credential-theft.md`
- [x] **[HIGH]** CISA Advisory: Contemporary Controls BASC 20T PLC Vulnerability (CVSS 9.8) Enables Full Device Control — `2026-04-09-contemporary-controls-basc20t-cvss98-ics.md`
- [x] **[HIGH]** CISA Advisory: GPL Odorizers GPL750 Missing Auth Flaw (CVSS 8.6) Could Enable Remote Gas Odorant Manipulation — `2026-04-09-gpl-odorizers-gpl750-ics-gas-vulnerability.md`
- [x] **[MEDIUM]** AI Hiring Startup Mercor Faces Lawsuits and Customer Losses After Data Breach — `2026-04-09-mercor-data-breach-ai-startup.md`
- [x] **[MEDIUM]** Flashpoint 2026 Tax Season Threat Intel: How Actors Source Identities, Bypass Verification, and Cash Out — `2026-04-09-tax-refund-fraud-2026-flashpoint.md`
- [x] **[MEDIUM]** Google Chrome 146 Ships Device Bound Session Credentials to Block Infostealer Cookie Theft — `2026-04-09-chrome-dbsc-session-cookie-protection.md`
- [x] **[INFORMATIONAL]** Florida Attorney General Opens Investigation into OpenAI Over National Security and Public Safety Concerns — `2026-04-09-florida-ag-openai-investigation.md`
- [x] **[INFORMATIONAL]** Anthropic's Restricted Mythos Release Highlights AI Model Capability as an Offensive Security Risk — `2026-04-09-anthropic-mythos-limited-release-security-analysis.md`
- [x] **[INFORMATIONAL]** Google Cloud Model Armor Brings Prompt Injection and Data Leakage Guardrails to GKE AI Inference — `2026-04-09-gke-model-armor-ai-inference-security.md`
- [x] **[INFORMATIONAL]** US Treasury Launches Cyber Threat Intelligence Sharing Program for Crypto and Digital Asset Industry — `2026-04-09-treasury-crypto-threat-sharing.md`

## Relevant (details)

### 1. EngageLab SDK Flaw Exposed 50 Million Android Users Including 30 Million Crypto Wallets
- **Source:** The Hacker News — https://thehackernews.com/2026/04/engagelab-sdk-flaw-exposed-50m-android.html
- **Severity:** critical
- **Tags:** `supply-chain`, `vulnerability`, `cve`, `android`
- **Summary:** A now-patched flaw in the widely used EngageLab Android SDK allowed co-installed apps to bypass Android's security sandbox and access private data, exposing 50 million users including 30 million crypto wallet users. SDK-level supply chain compromise affecting a massive user base; developers should verify they are on the patched version.

### 2. Smart Slider 3 Pro Update System Hijacked to Deliver Backdoored WordPress and Joomla Versions
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/smart-slider-updates-hijacked-to-push-malicious-wordpress-joomla-versions/
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`, `wordpress`, `appsec`
- **Summary:** The update delivery mechanism for the Smart Slider 3 Pro plugin was hijacked to push a trojanized version with multiple backdoors to sites with auto-updates enabled. Sites that applied the malicious update should treat them as fully compromised and begin incident response immediately.

### 3. BlueHammer: Researcher Drops PoC for Unpatched Windows Local Privilege Escalation Zero-Day
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/bluehammer-windows-exploit-microsoft-bug-disclosure-issues
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `microsoft`, `privilege-escalation`
- **Summary:** Researcher "Chaotic Eclipse" released a public PoC for an unpatched Windows local privilege escalation zero-day (BlueHammer) after a disclosure dispute with Microsoft. No CVE or patch is available yet; PoC availability significantly raises weaponization risk.

### 4. UAT-10362 Deploys Novel LucidRook Malware Against Taiwanese NGOs in Spear-Phishing Campaign
- **Source:** The Hacker News — https://thehackernews.com/2026/04/uat-10362-targets-taiwanese-ngos-with.html
- **Severity:** high
- **Tags:** `malware`, `phishing`, `apt`
- **Summary:** Threat cluster UAT-10362 is using spear-phishing to deliver LucidRook, a novel Lua-based malware stager that embeds a Lua interpreter and Rust-compiled libraries in a DLL. Geopolitically targeted campaign against Taiwanese civil society; IOCs available in the source report.

### 5. VENOM Phishing-as-a-Service Platform Targets C-Suite Executives' Microsoft Credentials
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-venom-phishing-attacks-steal-senior-executives-microsoft-logins/
- **Severity:** high
- **Tags:** `phishing`, `microsoft`, `iam`
- **Summary:** A previously undocumented PhaaS platform called VENOM provides ready-made infrastructure for harvesting Microsoft credentials from C-suite executives across industries. Enforce FIDO2 MFA and device-bound conditional access on all executive accounts.

### 6. CISA Advisory: Contemporary Controls BASC 20T PLC Vulnerability (CVSS 9.8) Enables Full Device Control
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-099-01
- **Severity:** high
- **Tags:** `ics`, `cve`, `vulnerability`
- **Summary:** CVE-2025-13926 (CVSS 9.8) in Contemporary Controls BASControl20 v3.1 enables unauthenticated remote attackers to fully control the PLC — reconfigure, delete, and execute remote calls. Commercial Facilities operators should patch and isolate devices.

### 7. CISA Advisory: GPL Odorizers GPL750 Missing Auth Flaw (CVSS 8.6) Could Enable Remote Gas Odorant Manipulation
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-099-02
- **Severity:** high
- **Tags:** `ics`, `cve`, `vulnerability`
- **Summary:** Missing authentication in GPL Odorizers GPL750 (CVSS 8.6) allows a low-privileged remote attacker to manipulate gas odorant injection levels, potentially masking gas leaks or triggering false alarms. All GPL750 XL4/XL7 variants are affected; isolate devices from internet exposure immediately.

### 8. AI Hiring Startup Mercor Faces Lawsuits and Customer Losses After Data Breach
- **Source:** TechCrunch AI — https://techcrunch.com/2026/04/09/after-data-breach-10b-valued-startup-mercor-is-having-a-month/
- **Severity:** medium
- **Tags:** `data-breach`
- **Summary:** $10B AI hiring platform Mercor suffered a breach and is now facing lawsuits and customer churn. Specific breach details are not yet disclosed; companies using Mercor for candidate data should assess their exposure under data processing agreements.

### 9. Flashpoint 2026 Tax Season Threat Intel: How Actors Source Identities, Bypass Verification, and Cash Out
- **Source:** Flashpoint — https://flashpoint.io/blog/tax-refund-fraud-in-2026-how-threat-actors-exploit-identity-verification-and-cash-out-channels/
- **Severity:** medium
- **Tags:** `phishing`, `fraud`, `data-breach`
- **Summary:** Flashpoint details the 2026 tax refund fraud pipeline from PII sourcing to verification bypass and crypto cash-out, illustrating how breach data enables downstream financial fraud long after the original compromise.

### 10. Google Chrome 146 Ships Device Bound Session Credentials to Block Infostealer Cookie Theft
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/google-chrome-adds-infostealer-protection-against-session-cookie-theft/
- **Severity:** medium
- **Tags:** `appsec`, `google`, `malware`
- **Summary:** Chrome 146 for Windows enables DBSC by default, binding session tokens to device hardware and making infostealer-stolen cookies useless on attacker machines. No user action required; enterprise teams should verify SSO/SAML compatibility.

### 11. Florida Attorney General Opens Investigation into OpenAI Over National Security and Public Safety Concerns
- **Source:** The Verge AI — https://www.theverge.com/policy/909557/openai-florida-investigation
- **Severity:** informational
- **Tags:** `openai`, `ai-safety`, `policy`
- **Summary:** Florida AG launched a formal investigation into OpenAI citing foreign adversary data access risks and a connection to a 2025 shooting where ChatGPT was allegedly used to plan the attack. Represents broadening state-level regulatory pressure with product liability framing.

### 12. Anthropic's Restricted Mythos Release Highlights AI Model Capability as an Offensive Security Risk
- **Source:** TechCrunch AI — https://techcrunch.com/2026/04/09/is-anthropic-limiting-the-release-of-mythos-to-protect-the-internet-or-anthropic/
- **Severity:** informational
- **Tags:** `anthropic`, `ai-safety`, `llm`
- **Summary:** TechCrunch analyzes Anthropic's decision to restrict Mythos access due to the model's capability to autonomously find software exploits, framing it against dual-use research governance debates. The decision has implications for how frontier AI labs govern future high-capability model releases.

### 13. Google Cloud Model Armor Brings Prompt Injection and Data Leakage Guardrails to GKE AI Inference
- **Source:** Google Cloud Security — https://cloud.google.com/blog/products/identity-security/securing-ai-inference-on-gke-with-model-armor/
- **Severity:** informational
- **Tags:** `cloud-security`, `kubernetes`, `gcp`, `google`, `prompt-injection`, `llm`
- **Summary:** Google Cloud's Model Armor provides gateway-level prompt injection and data leakage protection for LLM inference workloads on GKE, addressing attack vectors that traditional network controls miss. Relevant for practitioners deploying production AI on GCP.

### 14. US Treasury Launches Cyber Threat Intelligence Sharing Program for Crypto and Digital Asset Industry
- **Source:** The Record (Recorded Future) — https://therecord.media/treasury-department-announces-crypto-info-sharing
- **Severity:** informational
- **Tags:** `policy`, `cloud-security`
- **Summary:** Treasury is extending its financial-sector threat intelligence sharing program to eligible crypto firms at no cost, treating digital asset businesses as critical financial infrastructure for the first time. Firms should review eligibility and enroll to access government threat indicators.

## Skippable

- **ChatGPT $100/Month Pro Subscription** — The Verge AI. Subscription pricing tier change for Codex usage, not a model launch or security story.
- **LucidRook (BleepingComputer)** — BleepingComputer. Duplicate of item 4; The Hacker News report provides more technical detail on UAT-10362 malware internals.
- **GitHub Repo Size** — Simon Willison. Developer utility tool with no security relevance.
- **ChatGPT $100/Month Pro Plan** — TechCrunch AI. Duplicate of The Verge AI coverage of the same OpenAI subscription change.
- **Russia's Fancy Bear APT Continues Its Global Onslaught** — Dark Reading. Expert commentary without new TTPs, IOCs, or specific incident detail.
- **Florida AG Investigates OpenAI (TechCrunch)** — TechCrunch AI. Duplicate of item 11; The Verge AI selected as primary source.
- **FCC Proposes New Rule to Crackdown on Illegal Robocalls** — The Record. Telecom regulatory action; no cybersecurity or AI technical angle.
- **Healthcare IT Provider ChipSoft Hit by Ransomware** — BleepingComputer. Victim disclosure without TTPs or IOCs; generic ransomware incident.
- **Meta AI App Climbs to No. 5 on App Store After Muse Spark Launch** — TechCrunch AI. App Store ranking update; Muse Spark launch already covered in prior post.
- **Google and Intel Deepen AI Infrastructure Partnership** — TechCrunch AI. Chip co-development business announcement; no security angle.
- **Do Ceasefires Slow Cyberattacks? History Suggests Not** — Dark Reading. Opinion analysis without new incident or technical content.
- **The Threat Hunter's Gambit** — Cisco Talos. Strategy/opinion piece with no technical research or tooling.
- **Google Gemini AI Can Answer Questions with 3D Models and Simulations** — The Verge AI. Product feature announcement with no security angle.
- **Sierra's Bret Taylor Says the Era of Clicking Buttons Is Over** — TechCrunch AI. Marketing/opinion piece from startup CEO.
- **Russia Accuses Former Radio Free Europe Journalist of Aiding Cyberattacks** — The Record. Political espionage narrative without technical practitioner relevance.
- **Amazon CEO Takes Aim at Nvidia, Intel, Starlink in Shareholder Letter** — TechCrunch AI. Corporate shareholder letter; no security angle.
- **When Attackers Already Have the Keys, MFA Is Just Another Door to Open** — BleepingComputer. Vendor-sponsored content promoting Token biometric authentication product.
