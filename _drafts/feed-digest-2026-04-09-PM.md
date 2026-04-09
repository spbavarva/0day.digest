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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `vulnerability`, `cve`, `android`
- **Slug:** `2026-04-09-engagelab-sdk-flaw-50m-android-users`
- **Must-know:** yes
- **Summary:** A now-patched flaw in the widely used EngageLab Android SDK allowed co-installed apps to bypass Android's security sandbox and access private data, exposing 50 million users including 30 million crypto wallet users. Microsoft Defender researchers discovered the vulnerability, which constitutes a supply chain compromise at SDK level.

### 2. Smart Slider 3 Pro Update System Hijacked to Deliver Backdoored WordPress and Joomla Versions
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/smart-slider-updates-hijacked-to-push-malicious-wordpress-joomla-versions/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`, `wordpress`, `appsec`
- **Slug:** `2026-04-09-smart-slider-supply-chain-wordpress-joomla`
- **Must-know:** yes
- **Summary:** Attackers hijacked the update delivery mechanism for the Smart Slider 3 Pro plugin for WordPress and Joomla, pushing a trojanized version with multiple backdoors to sites with auto-updates enabled. Sites that applied the malicious update should treat their installations as compromised and perform full incident response.

### 3. BlueHammer: Researcher Drops PoC for Unpatched Windows Local Privilege Escalation Zero-Day
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/bluehammer-windows-exploit-microsoft-bug-disclosure-issues
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `microsoft`, `privilege-escalation`
- **Slug:** `2026-04-09-bluehammer-windows-zero-day-poc`
- **Must-know:** no
- **Summary:** A researcher under the alias "Chaotic Eclipse" publicly released a PoC exploit for an unpatched Windows local privilege escalation zero-day dubbed BlueHammer, citing a dispute with Microsoft over disclosure. No CVE assigned yet; Microsoft has not issued a patch, materially raising weaponization risk.

### 4. UAT-10362 Deploys Novel LucidRook Malware Against Taiwanese NGOs in Spear-Phishing Campaign
- **Source:** The Hacker News — https://thehackernews.com/2026/04/uat-10362-targets-taiwanese-ngos-with.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`, `apt`
- **Slug:** `2026-04-09-lucidrook-malware-uat-10362-taiwan`
- **Must-know:** no
- **Summary:** Threat cluster UAT-10362 is targeting Taiwanese NGOs and universities via spear-phishing delivering LucidRook, a sophisticated Lua-based malware stager that uses a DLL embedding a Lua interpreter and Rust-compiled libraries. The novel tooling and geopolitical targeting pattern are consistent with a well-resourced state-affiliated actor.

### 5. VENOM Phishing-as-a-Service Platform Targets C-Suite Executives' Microsoft Credentials
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-venom-phishing-attacks-steal-senior-executives-microsoft-logins/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `microsoft`, `iam`
- **Slug:** `2026-04-09-venom-phaas-executive-credential-theft`
- **Must-know:** no
- **Summary:** A previously undocumented PhaaS platform called VENOM is being used to harvest Microsoft credentials from C-suite executives across industries. Compromising senior executive accounts enables business email compromise, financial fraud, and high-privilege lateral movement.

### 6. CISA Advisory: Contemporary Controls BASC 20T PLC Vulnerability (CVSS 9.8) Enables Full Device Control
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-099-01
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `ics`, `cve`, `vulnerability`
- **Slug:** `2026-04-09-contemporary-controls-basc20t-cvss98-ics`
- **Must-know:** no
- **Summary:** CVE-2025-13926 (CVSS 9.8) in Contemporary Controls BASControl20 v3.1 allows unauthenticated remote attackers to fully control the PLC: enumerate, reconfigure, delete, and issue remote procedure calls. Commercial Facilities sector operators should apply patches and isolate devices from internet exposure.

### 7. CISA Advisory: GPL Odorizers GPL750 Missing Auth Flaw (CVSS 8.6) Could Enable Remote Gas Odorant Manipulation
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-099-02
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `ics`, `cve`, `vulnerability`
- **Slug:** `2026-04-09-gpl-odorizers-gpl750-ics-gas-vulnerability`
- **Must-know:** no
- **Summary:** A missing authentication flaw (CVSS 8.6) in GPL Odorizers GPL750 gas odorant injection systems allows a low-privileged remote attacker to manipulate gas odorant injection rates, potentially masking dangerous leaks or causing false alarms. All GPL750 variants across XL4/XL7 product lines are affected.

### 8. AI Hiring Startup Mercor Faces Lawsuits and Customer Losses After Data Breach
- **Source:** TechCrunch AI — https://techcrunch.com/2026/04/09/after-data-breach-10b-valued-startup-mercor-is-having-a-month/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `2026-04-09-mercor-data-breach-ai-startup`
- **Must-know:** no
- **Summary:** $10B-valued AI hiring platform Mercor suffered a data breach and is now facing lawsuits and reportedly losing major customers. Specific data types and affected user count are not disclosed in available reporting; AI hiring platforms typically hold highly sensitive candidate data.

### 9. Flashpoint 2026 Tax Season Threat Intel: How Actors Source Identities, Bypass Verification, and Cash Out
- **Source:** Flashpoint — https://flashpoint.io/blog/tax-refund-fraud-in-2026-how-threat-actors-exploit-identity-verification-and-cash-out-channels/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `phishing`, `fraud`, `data-breach`
- **Slug:** `2026-04-09-tax-refund-fraud-2026-flashpoint`
- **Must-know:** no
- **Summary:** Flashpoint's 2026 analysis details the full tax refund fraud pipeline: sourcing PII from breach markets, bypassing government identity verification, and cashing out via mule networks and crypto. The report illustrates how stolen breach data has long-tail consequences enabling financial fraud months or years after the original compromise.

### 10. Google Chrome 146 Ships Device Bound Session Credentials to Block Infostealer Cookie Theft
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/google-chrome-adds-infostealer-protection-against-session-cookie-theft/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `appsec`, `google`, `malware`
- **Slug:** `2026-04-09-chrome-dbsc-session-cookie-protection`
- **Must-know:** no
- **Summary:** Chrome 146 for Windows ships Device Bound Session Credentials (DBSC) by default, cryptographically binding session tokens to device hardware and rendering infostealer-harvested cookies useless on attacker machines. This directly addresses one of the most prevalent initial access techniques used by infostealers like Redline and Lumma.

### 11. Florida Attorney General Opens Investigation into OpenAI Over National Security and Public Safety Concerns
- **Source:** The Verge AI — https://www.theverge.com/policy/909557/openai-florida-investigation
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `openai`, `ai-safety`, `policy`
- **Slug:** `2026-04-09-florida-ag-openai-investigation`
- **Must-know:** no
- **Summary:** Florida AG James Uthmeier is investigating OpenAI over concerns that its technology may be accessible to adversarial foreign governments, prompted partly by a 2025 FSU shooting in which ChatGPT was allegedly used to plan the attack. The action broadens state-level regulatory pressure and introduces product liability framing for AI harms.

### 12. Anthropic's Restricted Mythos Release Highlights AI Model Capability as an Offensive Security Risk
- **Source:** TechCrunch AI — https://techcrunch.com/2026/04/09/is-anthropic-limiting-the-release-of-mythos-to-protect-the-internet-or-anthropic/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `anthropic`, `ai-safety`, `llm`
- **Slug:** `2026-04-09-anthropic-mythos-limited-release-security-analysis`
- **Must-know:** no
- **Summary:** TechCrunch analyzes Anthropic's decision to restrict Mythos access, citing the model's capability to autonomously discover software security exploits. The piece examines whether safety or competitive concerns drive the decision, and frames the debate in terms of dual-use research governance for frontier AI.

### 13. Google Cloud Model Armor Brings Prompt Injection and Data Leakage Guardrails to GKE AI Inference
- **Source:** Google Cloud Security — https://cloud.google.com/blog/products/identity-security/securing-ai-inference-on-gke-with-model-armor/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `cloud-security`, `kubernetes`, `gcp`, `google`, `prompt-injection`, `llm`
- **Slug:** `2026-04-09-gke-model-armor-ai-inference-security`
- **Must-know:** no
- **Summary:** Google Cloud has published guidance on deploying Model Armor as a gateway-level guardrail for AI inference on GKE, blocking prompt injection and sensitive data leakage at the infrastructure layer. This addresses a gap where traditional network controls are insufficient for LLM-specific attack vectors.

### 14. US Treasury Launches Cyber Threat Intelligence Sharing Program for Crypto and Digital Asset Industry
- **Source:** The Record (Recorded Future) — https://therecord.media/treasury-department-announces-crypto-info-sharing
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `policy`, `cloud-security`
- **Slug:** `2026-04-09-treasury-crypto-threat-sharing`
- **Must-know:** no
- **Summary:** The U.S. Treasury Department is extending its existing financial-sector cyber threat intelligence sharing program to eligible cryptocurrency and digital asset firms at no cost. This is a policy shift recognizing crypto firms as part of critical financial infrastructure warranting coordinated government threat intelligence.

## Skippable

- **ChatGPT $100/Month Pro Subscription** — The Verge AI. Subscription pricing tier change for Codex usage, not a model launch or security story.
- **LucidRook (BleepingComputer)** — BleepingComputer. Duplicate coverage of item 4; The Hacker News report (UAT-10362) provides more technical detail on the threat cluster and malware internals.
- **GitHub Repo Size** — Simon Willison. Developer utility tool for checking GitHub repo sizes via the API; no security relevance.
- **ChatGPT $100/Month Pro Plan** — TechCrunch AI. Duplicate of The Verge AI coverage of the same OpenAI subscription pricing change.
- **Russia's Fancy Bear APT Continues Its Global Onslaught** — Dark Reading. Thematic analysis and expert commentary without new TTPs, IOCs, or specific incident reporting.
- **Florida AG Investigates OpenAI (TechCrunch)** — TechCrunch AI. Duplicate of item 11; The Verge AI coverage selected as primary source.
- **FCC Proposes New Rule to Crackdown on Illegal Robocalls** — The Record. Telecom regulatory action with no direct cybersecurity or AI technical angle.
- **Healthcare IT Provider ChipSoft Hit by Ransomware** — BleepingComputer. Ransomware victim disclosure without TTPs, IOCs, or technical detail beyond the fact of the attack.
- **Meta AI App Climbs to No. 5 on App Store After Muse Spark Launch** — TechCrunch AI. App Store ranking update; the Muse Spark model launch was already covered in a prior post (2026-04-08).
- **Google and Intel Deepen AI Infrastructure Partnership** — TechCrunch AI. Business partnership announcement for chip co-development; no security angle.
- **Do Ceasefires Slow Cyberattacks? History Suggests Not** — Dark Reading. Opinion piece analyzing cyberattack patterns around geopolitical ceasefires; no new incident or technical content.
- **The Threat Hunter's Gambit** — Cisco Talos. Strategy/opinion piece on threat hunting mindset; no technical research, IOCs, or new tooling.
- **Google Gemini AI Can Answer Questions with 3D Models and Simulations** — The Verge AI. AI product feature announcement (3D model generation); no security angle.
- **Sierra's Bret Taylor Says the Era of Clicking Buttons Is Over** — TechCrunch AI. Opinion/marketing piece on AI agents from a startup CEO; no news value.
- **Russia Accuses Former Radio Free Europe Journalist of Aiding Cyberattacks** — The Record. Political espionage narrative without technical security content or practitioner relevance.
- **Amazon CEO Takes Aim at Nvidia, Intel, Starlink in Shareholder Letter** — TechCrunch AI. Corporate shareholder letter; business strategy content with no security angle.
- **When Attackers Already Have the Keys, MFA Is Just Another Door to Open** — BleepingComputer. Vendor-sponsored content promoting Token biometric authentication product; marketing disguised as analysis.
