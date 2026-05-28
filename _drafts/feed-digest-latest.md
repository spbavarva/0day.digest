# Digest — 2026-05-28 AM

- Window: last 14h
- Raw items considered: 13
- Relevant: 8
- Skippable: 5

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** JINX-0164 Targets Cryptocurrency Firms with Fake Recruiter Lures and macOS Malware — `2026-05-28-jinx-0164-crypto-macos-malware-cicd.md`
- [x] **[HIGH]** GPU Mining Malware Spreads via SEO Poisoning and AI Chatbot Manipulation — `2026-05-27-gpu-miner-seo-poisoning-ai-chatbot.md`
- [x] **[HIGH]** DICOM, Pydicom, GDCM, Orthanc: Heap Overflow via Medical Imaging Format — `2026-05-28-dicom-heap-overflow-medical-imaging.md`
- [x] **[MEDIUM]** Google Unveils AI Threat Defense Platform Combining Mandiant, Wiz, and Gemini — `2026-05-28-google-ai-threat-defense-platform.md`
- [x] **[MEDIUM]** Piracy Site Cybercrime Gang Gains RAT Module, Reaches Tens of Millions of Users — `2026-05-28-piracy-site-miner-rat-kaspersky.md`
- [x] **[MEDIUM]** 2026 World Cup: Ransomware Groups and State Actors Targeting Event Infrastructure — `2026-05-28-world-cup-2026-attack-surface.md`
- [x] **[MEDIUM]** The Evolving Cyber Extortion Economy: AI Accelerating Data Theft and Ransomware Operations — `2026-05-27-cyber-extortion-economy-unit42.md`
- [x] **[INFORMATIONAL]** SQLite Adds AGENTS.md to Set Explicit AI Agent Contribution Policy — `2026-05-27-sqlite-agents-md-ai-coding.md`

## Relevant (details)

### 1. JINX-0164 Targets Cryptocurrency Firms with Fake Recruiter Lures and macOS Malware
- **Source:** The Hacker News — https://thehackernews.com/2026/05/jinx-0164-targets-cryptocurrency-firms.html
- **Severity:** high
- **Tags:** `malware`, `phishing`, `supply-chain`, `cryptocurrency`, `macos`
- **Summary:** A previously undocumented threat actor (JINX-0164) is targeting crypto organizations via fake recruiter lures that deliver custom macOS malware, with Wiz researchers confirming deep CI/CD infrastructure targeting. The focus on CI/CD pipelines is significant — developer machine compromise can translate into repository-level access and secondary supply chain exposure.

### 2. GPU Mining Malware Spreads via SEO Poisoning and AI Chatbot Manipulation
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/gpu-mining-malware-spreads-via-seo-poisoning-ai-chatbots/
- **Severity:** high
- **Tags:** `malware`, `cryptocurrency`, `llm`
- **Summary:** An ongoing cryptojacking campaign targeting high-performance GPU systems is spreading through coordinated SEO poisoning that also manipulates AI chatbot recommendations. Attackers are now poisoning LLM outputs alongside search results — a notable evolution in malware distribution that extends traditional SEO abuse into AI recommendation channels.

### 3. DICOM, Pydicom, GDCM, Orthanc: Heap Overflow via Medical Imaging Format
- **Source:** Cisco Talos — https://blog.talosintelligence.com/dicom-pydicom-gdcm-and-orthanc-a-technical-tour-of-what-really-happens-in-the-heap/
- **Severity:** high
- **Tags:** `vulnerability`, `rce`, `appsec`
- **Summary:** Cisco Talos published a technical white paper demonstrating how the DICOM medical imaging file format can be exploited to create heap overflow vulnerabilities in Pydicom, GDCM, and the Orthanc DICOM server. Healthcare organizations and medical device manufacturers processing DICOM files should assess their exposure.

### 4. Google Unveils AI Threat Defense Platform Combining Mandiant, Wiz, and Gemini
- **Source:** SecurityWeek — https://www.securityweek.com/google-unveils-ai-threat-defense-platform-to-fight-ai-powered-cyberattacks/
- **Severity:** medium
- **Tags:** `google`, `wiz`, `ai-safety`, `llm`
- **Summary:** Google announced an AI Threat Defense platform combining Mandiant threat intelligence, Wiz cloud security sensors, and Gemini reasoning to help organizations detect and respond to AI-powered attacks. The platform is positioned as an AI-versus-AI defense tool; specific detection capabilities and pricing have not yet been disclosed.

### 5. Piracy Site Cybercrime Gang Gains RAT Module, Reaches Tens of Millions of Users
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/video-books-pirates-miners-rat/119943/
- **Severity:** medium
- **Tags:** `malware`, `cryptocurrency`
- **Summary:** A long-running cybercrime gang targeting pirated content consumers has expanded to new sites with tens of millions of visitors and upgraded its crypto miner payload with a full RAT module. The addition of remote access capability to an established miner represents a significant escalation beyond passive coin theft.

### 6. 2026 World Cup: Ransomware Groups and State Actors Targeting Event Infrastructure
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/fifa-world-cup-attack-surface/
- **Severity:** medium
- **Tags:** `ransomware`, `malware`, `vulnerability`
- **Summary:** Unit 42 assessed the cyber threat landscape for the 2026 FIFA World Cup, identifying ransomware groups, state-aligned actors, and opportunistic attackers targeting ticketing systems, broadcast infrastructure, and venue OT. Organizations providing services to the tournament should expect elevated and targeted activity.

### 7. The Evolving Cyber Extortion Economy: AI Accelerating Data Theft and Ransomware Operations
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/cyber-extortion-economy/
- **Severity:** medium
- **Tags:** `ransomware`, `llm`, `data-breach`
- **Summary:** Unit 42 published a research report on data theft and extortion trends, examining how advancing frontier AI models are reshaping attacker strategies for reconnaissance, data staging, and extortion. Key defensive recommendations cover data classification, exfiltration detection, and negotiation preparedness for double-extortion scenarios.

### 8. SQLite Adds AGENTS.md to Set Explicit AI Agent Contribution Policy
- **Source:** Simon Willison — https://simonwillison.net/2026/May/27/sqlite-agents/#atom-everything
- **Severity:** informational
- **Tags:** `llm`, `github`
- **Summary:** SQLite added an AGENTS.md file establishing explicit policies for AI coding agents, barring agentic code submissions while allowing agents to contribute bug reports if reviewed by a human. Simon Willison flagged this as an early example of a major open-source project proactively defining AI agent governance.

## Skippable

- **Sextortionist sentenced to 33 years for targeting 145 children** — BleepingComputer. Legal sentencing of individual criminal; no technical security angle.
- **YouTube will let you ask AI to make a custom video feed** — The Verge AI. Consumer AI product feature with no security angle.
- **Nordic CISOs Handle Rising Cyber Threats Remarkably Well** — Dark Reading. Survey/opinion piece without technical news value.
- **Vertu wants CEOs to run companies from an AI foldable starting at $6,880** — TechCrunch AI. Luxury consumer product launch, no security or substantive AI technical content.
- **Why Google's AI can't spell Google (or anything else)** — TechCrunch AI. Opinion/criticism piece without news value.
