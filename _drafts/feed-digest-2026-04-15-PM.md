# Digest — 2026-04-15 PM

- Window: last 14h
- Raw items considered: 54
- Relevant: 16
- Skippable: 38

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** CVE-2026-33032 (MCPwn): Critical Nginx UI Authentication Bypass Actively Exploited — `2026-04-15-cve-2026-33032-nginx-ui-auth-bypass-mcpwn.md`
- [x] **[CRITICAL]** 'By Design' Flaw in Model Context Protocol Enables AI Supply Chain Attacks — `2026-04-15-mcp-by-design-supply-chain-attack-flaw.md`
- [x] **[CRITICAL]** ShinyHunters Claims 45 Million McGraw Hill Records via Salesforce Misconfiguration — `2026-04-15-mcgraw-hill-shinyhunters-salesforce-45m-records.md`
- [x] **[HIGH]** 30+ EssentialPlugin WordPress Plugins Backdoored in Supply Chain Compromise — `2026-04-15-wordpress-essentialplugin-supply-chain-backdoor.md`
- [x] **[HIGH]** 100 Chrome Extensions in Coordinated Campaign Steal User Data and Open Backdoors — `2026-04-15-100-chrome-extensions-coordinated-backdoor-campaign.md`
- [x] **[HIGH]** CISA Adds Windows Task Host Privilege Escalation Flaw to Known Exploited Vulnerabilities — `2026-04-15-cisa-windows-task-host-privilege-escalation-kev.md`
- [x] **[HIGH]** Prompt Injection Flaws in Salesforce Agentforce and Microsoft Copilot Now Patched — `2026-04-15-salesforce-agentforce-microsoft-copilot-prompt-injection.md`
- [x] **[HIGH]** New AgingFly Malware Targets Ukrainian Government and Hospitals to Steal Browser Credentials — `2026-04-15-agingfly-malware-ukraine-government-hospitals.md`
- [x] **[HIGH]** Digitally Signed Adware Tool Deploys SYSTEM-Privilege Scripts to Disable Antivirus — `2026-04-15-signed-adware-system-privilege-av-killing-scripts.md`
- [x] **[MEDIUM]** Mirax RAT-as-a-Service Targets European Android Users as Residential Proxy Network — `2026-04-15-mirax-rat-android-europe-malware-as-a-service.md`
- [x] **[MEDIUM]** UK Government Warns Businesses on AI-Amplified Cyber Threat Landscape — `2026-04-15-uk-warns-ai-amplified-cyber-threats-anthropic-mythos.md`
- [x] **[MEDIUM]** NIST to Scale Back NVD Enrichment as CVE Submission Volume Surges — `2026-04-15-nist-nvd-limits-cve-enrichment-submission-surge.md`
- [x] **[MEDIUM]** OpenAI Agents SDK Adds Native Sandbox Execution and Model-Native Harness — `2026-04-15-openai-agents-sdk-sandbox-model-native-harness.md`
- [x] **[MEDIUM]** Sweden Publicly Attributes Pro-Russian Cyberattack Against District Heating Infrastructure — `2026-04-15-sweden-pro-russian-energy-ics-cyberattack-attribution.md`
- [x] **[MEDIUM]** Kaspersky GReAT ICS Threat Landscape Report Q4 2025 — `2026-04-15-kaspersky-ics-threat-landscape-q4-2025.md`
- [x] **[INFORMATIONAL]** Google Releases Gemini 3.1 Flash TTS with Prompt-Controlled Expressive Audio — `2026-04-15-gemini-31-flash-tts-launch-expressive-audio.md`

## Relevant (details)

### 1. CVE-2026-33032 (MCPwn): Critical Nginx UI Authentication Bypass Actively Exploited
- **Source:** The Hacker News — https://thehackernews.com/2026/04/critical-nginx-ui-vulnerability-cve.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `rce`, `zero-day`
- **Slug:** `2026-04-15-cve-2026-33032-nginx-ui-auth-bypass-mcpwn`
- **Must-know:** yes
- **Summary:** CVE-2026-33032 (CVSS 9.8) in nginx-ui is being actively exploited in the wild. Dubbed "MCPwn" by Pluto Security, the flaw allows unauthenticated attackers to take full control of the Nginx service—restart, create, modify, and delete config files. The vulnerability was introduced via nginx-ui's recently added Model Context Protocol (MCP) support.

### 2. 'By Design' Flaw in Model Context Protocol Enables AI Supply Chain Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/by-design-flaw-in-mcp-could-enable-widespread-ai-supply-chain-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `llm`, `rce`, `ai-safety`, `anthropic`
- **Slug:** `2026-04-15-mcp-by-design-supply-chain-attack-flaw`
- **Must-know:** yes
- **Summary:** A design flaw in Anthropic's Model Context Protocol allows unsanitized commands to execute silently via tool definitions, enabling full system compromise across AI environments. Because the issue is architectural rather than a bug, it requires a protocol-level fix; MCP's rapid adoption across IDEs and agent frameworks makes this a wide supply chain attack surface.

### 3. ShinyHunters Claims 45 Million McGraw Hill Records via Salesforce Misconfiguration
- **Source:** The Record (Recorded Future) — https://therecord.media/mcgraw-hill-data-leak-tied-to-salesforce-misconfiguration
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `data-breach`, `cloud-security`
- **Slug:** `2026-04-15-mcgraw-hill-shinyhunters-salesforce-45m-records`
- **Must-know:** yes
- **Summary:** ShinyHunters claimed to have stolen 45 million Salesforce records from educational publisher McGraw Hill and threatened to leak them by April 14 absent a ransom payment. McGraw Hill attributed the exposure to a Salesforce misconfiguration rather than a direct system breach.

### 4. 30+ EssentialPlugin WordPress Plugins Backdoored in Supply Chain Compromise
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/wordpress-plugin-suite-hacked-to-push-malware-to-thousands-of-sites/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `appsec`
- **Slug:** `2026-04-15-wordpress-essentialplugin-supply-chain-backdoor`
- **Must-know:** no
- **Summary:** More than 30 WordPress plugins in the EssentialPlugin package were backdoored with malicious code granting unauthorized site access. Any site that installed or updated these plugins during the compromise window received the payload automatically through normal plugin update channels.

### 5. 100 Chrome Extensions in Coordinated Campaign Steal User Data and Open Backdoors
- **Source:** SecurityWeek — https://www.securityweek.com/100-chrome-extensions-steal-user-data-open-backdoor/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `data-breach`, `appsec`
- **Slug:** `2026-04-15-100-chrome-extensions-coordinated-backdoor-campaign`
- **Must-know:** no
- **Summary:** 100 malicious Chrome extensions published through five developer accounts steal user data and create backdoors; shared C2 infrastructure confirms a coordinated campaign. The multi-account distribution approach is a known technique for evading Google's extension moderation.

### 6. CISA Adds Windows Task Host Privilege Escalation Flaw to Known Exploited Vulnerabilities
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-flags-windows-task-host-vulnerability-as-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`, `microsoft`
- **Slug:** `2026-04-15-cisa-windows-task-host-privilege-escalation-kev`
- **Must-know:** no
- **Summary:** CISA has added a Windows Task Host privilege escalation vulnerability to the KEV catalog after confirming exploitation in the wild. The flaw allows attackers to elevate to SYSTEM privileges, a critical step in post-exploitation chains enabling credential dumping and lateral movement.

### 7. Prompt Injection Flaws in Salesforce Agentforce and Microsoft Copilot Now Patched
- **Source:** Dark Reading — https://www.darkreading.com/cloud-security/microsoft-salesforce-patch-ai-agent-data-leak-flaws
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `vulnerability`, `microsoft`
- **Slug:** `2026-04-15-salesforce-agentforce-microsoft-copilot-prompt-injection`
- **Must-know:** no
- **Summary:** Prompt injection vulnerabilities in Salesforce Agentforce and Microsoft Copilot would have let external attackers exfiltrate sensitive data processed by the AI agents. Both vendors have issued patches; the disclosures highlight the continued lack of trust boundaries in enterprise AI agent implementations.

### 8. New AgingFly Malware Targets Ukrainian Government and Hospitals to Steal Browser Credentials
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-agingfly-malware-used-in-attacks-on-ukraine-govt-hospitals/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `data-breach`
- **Slug:** `2026-04-15-agingfly-malware-ukraine-government-hospitals`
- **Must-know:** no
- **Summary:** A newly identified malware family, AgingFly, is being deployed against Ukrainian local governments and hospitals. It harvests credentials from Chromium-based browsers and WhatsApp, fitting a continuing pattern of intelligence-gathering operations against Ukrainian wartime-critical organizations.

### 9. Digitally Signed Adware Tool Deploys SYSTEM-Privilege Scripts to Disable Antivirus
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/signed-software-abused-to-deploy-antivirus-killing-scripts/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `privilege-escalation`
- **Slug:** `2026-04-15-signed-adware-system-privilege-av-killing-scripts`
- **Must-know:** no
- **Summary:** A legitimately signed adware tool is being used to deploy SYSTEM-privilege payloads that kill antivirus protections across thousands of endpoints in education, utilities, government, and healthcare. The signed certificate bypasses application control policies, providing a trusted foothold for AV termination and further payload delivery.

### 10. Mirax RAT-as-a-Service Targets European Android Users as Residential Proxy Network
- **Source:** SecurityWeek — https://www.securityweek.com/mirax-rat-targeting-android-users-in-europe/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Slug:** `2026-04-15-mirax-rat-android-europe-malware-as-a-service`
- **Must-know:** no
- **Summary:** Mirax, a new RAT offered as MaaS to primarily Russian-speaking affiliates, is targeting Android users in Europe and converting infected devices into residential proxy nodes. The proxy layer monetizes infections beyond data theft and complicates detection by routing attacker traffic through legitimate consumer IPs.

### 11. UK Government Warns Businesses on AI-Amplified Cyber Threat Landscape
- **Source:** The Record (Recorded Future) — https://therecord.media/anthropic-mythos-uk-cyber-risk
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`, `anthropic`, `llm`
- **Slug:** `2026-04-15-uk-warns-ai-amplified-cyber-threats-anthropic-mythos`
- **Must-know:** no
- **Summary:** The UK minister for civil defense issued guidance to businesses to strengthen cyber defenses, citing Anthropic's Mythos model as prompting a reevaluation of the threat landscape. This is the first allied government to issue formal business-facing guidance tied directly to a specific AI model release.

### 12. NIST to Scale Back NVD Enrichment as CVE Submission Volume Surges
- **Source:** The Record (Recorded Future) — https://therecord.media/nist-to-limit-work-on-cve-entries-surge
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`
- **Slug:** `2026-04-15-nist-nvd-limits-cve-enrichment-submission-surge`
- **Must-know:** no
- **Summary:** NIST will no longer enrich every CVE in the National Vulnerability Database—only those meeting a severity threshold—abandoning its comprehensive categorization mission as submission volume surges. This creates gaps in CVSS scores, CWE classifications, and CPE data that most VM platforms rely on for prioritization.

### 13. OpenAI Agents SDK Adds Native Sandbox Execution and Model-Native Harness
- **Source:** OpenAI Blog — https://openai.com/index/the-next-evolution-of-the-agents-sdk
- **Section:** AI — Labs & Model Launches
- **Severity:** medium
- **Tags:** `llm`, `openai`, `appsec`
- **Slug:** `2026-04-15-openai-agents-sdk-sandbox-model-native-harness`
- **Must-know:** no
- **Summary:** OpenAI's updated Agents SDK introduces native sandbox execution—constraining agent access to tools, filesystem, and network—and a model-native harness that standardizes tool interactions to reduce prompt injection risk. This is the most security-relevant SDK update since the framework launched.

### 14. Sweden Publicly Attributes Pro-Russian Cyberattack Against District Heating Infrastructure
- **Source:** SecurityWeek — https://www.securityweek.com/sweden-blames-pro-russian-group-for-cyberattack-last-year-on-its-energy-infrastructure/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ics`, `malware`
- **Slug:** `2026-04-15-sweden-pro-russian-energy-ics-cyberattack-attribution`
- **Must-know:** no
- **Summary:** Sweden has for the first time publicly attributed a 2025 cyberattack on a district heating plant in western Sweden to a pro-Russian threat group. The attribution marks the first official Swedish disclosure of a state-linked OT attack against civilian energy infrastructure.

### 15. Kaspersky GReAT ICS Threat Landscape Report Q4 2025
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/industrial-threat-report-q4-2025/119392/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `ics`, `malware`
- **Slug:** `2026-04-15-kaspersky-ics-threat-landscape-q4-2025`
- **Must-know:** no
- **Summary:** Kaspersky GReAT's Q4 2025 ICS threat report covers infection vectors, malware categories, and regional/industry statistics for industrial automation systems. The Q4 2025 period immediately precedes several notable ICS-targeting campaigns disclosed in early 2026.

### 16. Google Releases Gemini 3.1 Flash TTS with Prompt-Controlled Expressive Audio
- **Source:** Google DeepMind — https://deepmind.google/blog/gemini-3-1-flash-tts-the-next-generation-of-expressive-ai-speech/
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `google`, `model-release`, `llm`
- **Slug:** `2026-04-15-gemini-31-flash-tts-launch-expressive-audio`
- **Must-know:** no
- **Summary:** Google DeepMind released Gemini 3.1 Flash TTS, a text-to-speech model accessible via the Gemini API (`gemini-3.1-flash-tts-preview`). The model accepts narrative-style prompts for granular voice direction and outputs audio only.

## Skippable

- **datasette 1.0a27** — Simon Willison. Alpha release of a developer data tool with CSRF and table-rename changes; no security angle.
- **Critical Nginx UI auth bypass flaw now actively exploited** — BleepingComputer. Duplicate of item 47 (The Hacker News); covered under CVE-2026-33032 with more detail.
- **Critical MCP Integration Flaw Puts NGINX at Risk** — Dark Reading. Duplicate of item 47 (The Hacker News); same CVE, less detail.
- **Trump's posting even more AI-generated Trump-Jesus fan art** — The Verge AI. Political/cultural content; no security or AI substance.
- **Teen arrested in Northern Ireland over cyberattack on school network** — The Record. Regional incident involving a single 16-year-old; no technical IOCs or novel TTPs.
- **Navigating the Unique Security Risks of Asia's Digital Supply Chain** — Dark Reading. Opinion/analysis piece on regional supply chain risk; no specific news event.
- **OpenAI updates its Agents SDK** — TechCrunch AI. Duplicate of item 54 (OpenAI Blog); covered with primary source.
- **Flashpoint Surpasses Cataloging 7,000 Known Exploited Vulnerabilities** — Flashpoint. Vendor milestone/marketing announcement with no new vulnerability data.
- **Hightouch reaches $100M ARR fueled by marketing tools powered by AI** — TechCrunch AI. Non-security SaaS business news; no security angle.
- **LinkedIn data shows AI isn't to blame for hiring decline** — TechCrunch AI. Labor market analysis; no security angle.
- **AI learning app Gizmo levels up with 13M users and a $22M investment** — TechCrunch AI. Edtech funding announcement; no security angle.
- **Can AI judge journalism? A Thiel-backed startup says yes** — TechCrunch AI. AI policy opinion piece; no specific news event.
- **Google rolls out a native Gemini app for Mac** — TechCrunch AI. Duplicate of The Verge item on same launch.
- **Google launches a Gemini AI app on Mac** — The Verge AI. Consumer app launch; no security angle.
- **The musician-turned-biotech-founder waiting to fundraise** — TechCrunch AI. Biotech podcast episode; off-topic.
- **India's vibe-coding startup Emergent enters OpenClaw-like AI agent space** — TechCrunch AI. Startup launch announcement; no security angle.
- **Quoting John Gruber** — Simon Willison. Commentary on Apple platform developer trends; no news value.
- **Gemini 3.1 Flash TTS** — Simon Willison. Duplicate of Google DeepMind's direct announcement; covered from primary source.
- **n8n Webhooks Abused Since October 2025 to Deliver Malware** — The Hacker News. Already published as `_posts/2026-04-15-n8n-agentic-ai-workflow-abuse-email-campaigns.md`.
- **Microsoft pays $2.3M for cloud and AI flaws at Zero Day Quest** — BleepingComputer. Bug bounty event results announced without disclosing specific vulnerability details; no actionable technical content.
- **Allbirds announced a switch from shoes to AI** — The Verge AI. Duplicate of TechCrunch item on same business pivot; no security angle.
- **Cloud CISO Perspectives: How CISOs can pursue technical and cultural resilience** — Google Cloud Security. Interview/opinion format; no breaking news.
- **Quoting Kyle Kingsbury** — Simon Willison. Commentary on AI accountability and "meat shields"; no news event.
- **Prepping for 'Q-Day': Why Quantum Risk Management Should Start Now** — Dark Reading. Opinion piece on quantum risk; no new research or news event.
- **Exploited Vulnerability Exposes Nginx Servers to Hacking** — SecurityWeek. Duplicate of item 47 (The Hacker News); same CVE-2026-33032 coverage.
- **Audit: Big Tech Often Ignores CA Privacy Law Opt-Out Requests** — Dark Reading. Privacy compliance audit finding; regulatory/policy story without technical security substance.
- **After sale of its shoe business, Allbirds pivots to AI** — TechCrunch AI. Same business pivot story as The Verge item; no security angle.
- **Rolling Networks: Securing the Transportation Sector** — BleepingComputer. Conference promotion content for NMFTA Cybersecurity Conference; no news.
- **Capsule Security Emerges From Stealth With $7 Million in Funding** — SecurityWeek. AI agent runtime security startup funding announcement; no research or technical findings disclosed.
- **Reid Hoffman weighs in on the 'tokenmaxxing' debate** — TechCrunch AI. Opinion/commentary on AI token metrics; no news event.
- **Adobe's new Firefly AI assistant can use Creative Cloud apps to complete tasks** — TechCrunch AI. Duplicate of The Verge item on same Adobe launch.
- **CISO Conversations: Ross McKerchar, CISO at Sophos** — SecurityWeek. Leadership interview; no news.
- **Gitar, a startup that uses agents to secure code, emerges from stealth with $9 million** — TechCrunch AI. Startup funding announcement; no research or technical findings.
- **This startup is betting tokenmaxxing will create the next compute giant** — TechCrunch AI. Startup funding ($32M Series A for Parasail); no security angle.
- **Adobe embraces conversational AI editing** — The Verge AI. Creative software update; no security angle.
- **April Patch Tuesday Fixes Critical Flaws Across SAP, Adobe, Microsoft, Fortinet, and More** — The Hacker News. April Patch Tuesday already covered in `_posts/2026-04-14-april-2026-patch-tuesday-sharepoint-zero-day.md`; duplicate.
- **Inside VAKRA: Reasoning, Tool Use, and Failure Modes of Agents** — Hugging Face Blog. No summary available in feed; unclear relevance without content.
- **Deterministic + Agentic AI: The Architecture Exposure Validation Requires** — The Hacker News. Appears to be sponsored/marketing content from Pentera's 2026 AI Security report; no independent news value.
