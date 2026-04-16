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
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `rce`, `zero-day`
- **Summary:** CVE-2026-33032 (CVSS 9.8) in nginx-ui is under active exploitation; attackers gain unauthenticated full control of the Nginx service. The vulnerability was introduced via nginx-ui's recently added MCP support and has been dubbed "MCPwn" by Pluto Security.

### 2. 'By Design' Flaw in Model Context Protocol Enables AI Supply Chain Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/by-design-flaw-in-mcp-could-enable-widespread-ai-supply-chain-attacks/
- **Severity:** critical
- **Tags:** `supply-chain`, `llm`, `rce`, `ai-safety`, `anthropic`
- **Summary:** A design flaw in Anthropic's Model Context Protocol allows unsanitized commands to execute silently via tool definitions, enabling full system compromise. Because it is architectural rather than a bug, a protocol-level fix is required; MCP's wide adoption across IDEs and agent frameworks makes this a broad supply chain attack surface.

### 3. ShinyHunters Claims 45 Million McGraw Hill Records via Salesforce Misconfiguration
- **Source:** The Record (Recorded Future) — https://therecord.media/mcgraw-hill-data-leak-tied-to-salesforce-misconfiguration
- **Severity:** critical
- **Tags:** `data-breach`, `cloud-security`
- **Summary:** ShinyHunters claimed 45 million Salesforce records from McGraw Hill and issued a ransom deadline of April 14. McGraw Hill confirmed the leak via a Salesforce misconfiguration rather than a direct system breach.

### 4. 30+ EssentialPlugin WordPress Plugins Backdoored in Supply Chain Compromise
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/wordpress-plugin-suite-hacked-to-push-malware-to-thousands-of-sites/
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `appsec`
- **Summary:** 30+ WordPress plugins in the EssentialPlugin package were backdoored, delivering malicious payloads to thousands of sites through normal plugin update channels.

### 5. 100 Chrome Extensions in Coordinated Campaign Steal User Data and Open Backdoors
- **Source:** SecurityWeek — https://www.securityweek.com/100-chrome-extensions-steal-user-data-open-backdoor/
- **Severity:** high
- **Tags:** `malware`, `data-breach`, `appsec`
- **Summary:** 100 malicious Chrome extensions published through five accounts share C2 infrastructure confirming a coordinated campaign to steal user data and create backdoor access.

### 6. CISA Adds Windows Task Host Privilege Escalation Flaw to Known Exploited Vulnerabilities
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-flags-windows-task-host-vulnerability-as-exploited-in-attacks/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`, `microsoft`
- **Summary:** CISA confirmed active exploitation of a Windows Task Host privilege escalation flaw that elevates attackers to SYSTEM—a key post-exploitation step for credential dumping and lateral movement.

### 7. Prompt Injection Flaws in Salesforce Agentforce and Microsoft Copilot Now Patched
- **Source:** Dark Reading — https://www.darkreading.com/cloud-security/microsoft-salesforce-patch-ai-agent-data-leak-flaws
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `vulnerability`, `microsoft`
- **Summary:** Prompt injection vulnerabilities in Salesforce Agentforce and Microsoft Copilot would have allowed external attackers to exfiltrate sensitive data via AI agents processing untrusted content. Both vendors have patched.

### 8. New AgingFly Malware Targets Ukrainian Government and Hospitals to Steal Browser Credentials
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-agingfly-malware-used-in-attacks-on-ukraine-govt-hospitals/
- **Severity:** high
- **Tags:** `malware`, `data-breach`
- **Summary:** AgingFly, a new malware family, is deployed against Ukrainian local governments and hospitals, harvesting credentials from Chromium browsers and WhatsApp in intelligence-gathering operations targeting wartime-critical organizations.

### 9. Digitally Signed Adware Tool Deploys SYSTEM-Privilege Scripts to Disable Antivirus
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/signed-software-abused-to-deploy-antivirus-killing-scripts/
- **Severity:** high
- **Tags:** `malware`, `privilege-escalation`
- **Summary:** A legitimately signed adware tool is being used to bypass application control policies, escalate to SYSTEM, and kill AV protections across thousands of endpoints in education, utilities, government, and healthcare.

### 10. Mirax RAT-as-a-Service Targets European Android Users as Residential Proxy Network
- **Source:** SecurityWeek — https://www.securityweek.com/mirax-rat-targeting-android-users-in-europe/
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Summary:** Mirax RAT, offered as MaaS to primarily Russian-speaking affiliates, targets European Android users and converts infected devices into residential proxy nodes to route attacker traffic through legitimate consumer IPs.

### 11. UK Government Warns Businesses on AI-Amplified Cyber Threat Landscape
- **Source:** The Record (Recorded Future) — https://therecord.media/anthropic-mythos-uk-cyber-risk
- **Severity:** medium
- **Tags:** `ai-safety`, `anthropic`, `llm`
- **Summary:** The UK minister for civil defense issued guidance to businesses citing Anthropic's Mythos as prompting a reevaluation of the cyber threat landscape—the first allied government to tie formal business-facing guidance to a specific model release.

### 12. NIST to Scale Back NVD Enrichment as CVE Submission Volume Surges
- **Source:** The Record (Recorded Future) — https://therecord.media/nist-to-limit-work-on-cve-entries-surge
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`
- **Summary:** NIST will only enrich NVD records for CVEs meeting a severity threshold, creating gaps in CVSS scores and CPE data that most vulnerability management platforms rely on for prioritization.

### 13. OpenAI Agents SDK Adds Native Sandbox Execution and Model-Native Harness
- **Source:** OpenAI Blog — https://openai.com/index/the-next-evolution-of-the-agents-sdk
- **Severity:** medium
- **Tags:** `llm`, `openai`, `appsec`
- **Summary:** OpenAI's updated Agents SDK introduces native sandbox execution to constrain agent blast radius and a model-native harness to reduce prompt injection risk through standardized tool interactions.

### 14. Sweden Publicly Attributes Pro-Russian Cyberattack Against District Heating Infrastructure
- **Source:** SecurityWeek — https://www.securityweek.com/sweden-blames-pro-russian-group-for-cyberattack-last-year-on-its-energy-infrastructure/
- **Severity:** medium
- **Tags:** `ics`, `malware`
- **Summary:** Sweden publicly attributed a 2025 attack on a western Swedish district heating plant to a pro-Russian group—the first Swedish official attribution of a state-linked OT attack against civilian energy infrastructure.

### 15. Kaspersky GReAT ICS Threat Landscape Report Q4 2025
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/industrial-threat-report-q4-2025/119392/
- **Severity:** medium
- **Tags:** `ics`, `malware`
- **Summary:** Kaspersky GReAT's Q4 2025 ICS report covers infection vectors, malware types, and regional/industry attack statistics for industrial automation environments through the period immediately preceding several early-2026 ICS campaigns.

### 16. Google Releases Gemini 3.1 Flash TTS with Prompt-Controlled Expressive Audio
- **Source:** Google DeepMind — https://deepmind.google/blog/gemini-3-1-flash-tts-the-next-generation-of-expressive-ai-speech/
- **Severity:** informational
- **Tags:** `google`, `model-release`, `llm`
- **Summary:** Google DeepMind released Gemini 3.1 Flash TTS, available via the Gemini API, supporting narrative-style prompts for granular expressive voice control.

## Skippable

- **datasette 1.0a27** — Simon Willison. Alpha developer tool release; no security angle.
- **Critical Nginx UI auth bypass flaw now actively exploited** — BleepingComputer. Duplicate of item 47; covered from The Hacker News with more detail.
- **Critical MCP Integration Flaw Puts NGINX at Risk** — Dark Reading. Duplicate of item 47; same CVE, less detail.
- **Trump's posting even more AI-generated Trump-Jesus fan art** — The Verge AI. Political/cultural content; no security or AI substance.
- **Teen arrested in Northern Ireland over cyberattack on school network** — The Record. Regional incident; no novel TTPs or IOCs.
- **Navigating the Unique Security Risks of Asia's Digital Supply Chain** — Dark Reading. Opinion/analysis piece; no specific news event.
- **OpenAI updates its Agents SDK** — TechCrunch AI. Duplicate of OpenAI Blog item 54.
- **Flashpoint Surpasses Cataloging 7,000 Known Exploited Vulnerabilities** — Flashpoint. Vendor milestone announcement; no new vulnerability data.
- **Hightouch reaches $100M ARR** — TechCrunch AI. Non-security SaaS business news.
- **LinkedIn data shows AI isn't to blame for hiring decline** — TechCrunch AI. Labor market analysis; no security angle.
- **AI learning app Gizmo levels up with $22M investment** — TechCrunch AI. Edtech funding; no security angle.
- **Can AI judge journalism? A Thiel-backed startup says yes** — TechCrunch AI. AI policy opinion; no news event.
- **Google rolls out a native Gemini app for Mac** — TechCrunch AI. Duplicate of The Verge item on same launch.
- **Google launches a Gemini AI app on Mac** — The Verge AI. Consumer app launch; no security angle.
- **The musician-turned-biotech-founder waiting to fundraise** — TechCrunch AI. Biotech podcast; off-topic.
- **India's vibe-coding startup Emergent enters OpenClaw-like AI agent space** — TechCrunch AI. Startup launch; no security angle.
- **Quoting John Gruber** — Simon Willison. Commentary on Apple platform trends; no news value.
- **Gemini 3.1 Flash TTS** — Simon Willison. Duplicate of Google DeepMind direct announcement.
- **n8n Webhooks Abused Since October 2025 to Deliver Malware** — The Hacker News. Already published as `_posts/2026-04-15-n8n-agentic-ai-workflow-abuse-email-campaigns.md`.
- **Microsoft pays $2.3M for cloud and AI flaws at Zero Day Quest** — BleepingComputer. Bug bounty results announced without disclosed vulnerability details; no actionable technical content.
- **Allbirds announced a switch from shoes to AI** — The Verge AI. Duplicate of TechCrunch business pivot item; no security angle.
- **Cloud CISO Perspectives: How CISOs can pursue technical and cultural resilience** — Google Cloud Security. Interview/opinion; no breaking news.
- **Quoting Kyle Kingsbury** — Simon Willison. Commentary on AI accountability; no news event.
- **Prepping for 'Q-Day': Why Quantum Risk Management Should Start Now** — Dark Reading. Opinion piece; no new research or news event.
- **Exploited Vulnerability Exposes Nginx Servers to Hacking** — SecurityWeek. Duplicate of item 47; same CVE-2026-33032.
- **Audit: Big Tech Often Ignores CA Privacy Law Opt-Out Requests** — Dark Reading. Privacy compliance audit; no technical security event.
- **After sale of its shoe business, Allbirds pivots to AI** — TechCrunch AI. Same business pivot story; no security angle.
- **Rolling Networks: Securing the Transportation Sector** — BleepingComputer. Conference promotion content; no news.
- **Capsule Security Emerges From Stealth With $7 Million in Funding** — SecurityWeek. Startup funding; no research or findings disclosed.
- **Reid Hoffman weighs in on the 'tokenmaxxing' debate** — TechCrunch AI. Opinion on AI token metrics; no news event.
- **Adobe's new Firefly AI assistant** — TechCrunch AI. Duplicate of The Verge Adobe item.
- **CISO Conversations: Ross McKerchar, CISO at Sophos** — SecurityWeek. Leadership interview; no news.
- **Gitar, a startup that uses agents to secure code** — TechCrunch AI. Startup funding; no research or findings.
- **This startup is betting tokenmaxxing will create the next compute giant** — TechCrunch AI. Startup funding; no security angle.
- **Adobe embraces conversational AI editing** — The Verge AI. Creative software update; no security angle.
- **April Patch Tuesday Fixes Critical Flaws Across SAP, Adobe, Microsoft, Fortinet** — The Hacker News. Already covered in `_posts/2026-04-14-april-2026-patch-tuesday-sharepoint-zero-day.md`.
- **Inside VAKRA: Reasoning, Tool Use, and Failure Modes of Agents** — Hugging Face Blog. No summary in feed; insufficient content to evaluate.
- **Deterministic + Agentic AI: The Architecture Exposure Validation Requires** — The Hacker News. Sponsored/marketing content from Pentera's report; no independent news value.
