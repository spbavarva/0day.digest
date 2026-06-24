# Digest — 2026-06-24 PM

- Window: last 14h
- Raw items considered: 39
- Relevant: 13
- Skippable: 26

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** CISA Warns of Active Exploitation of Critical Lantronix EDS5000 Flaw — `2026-06-24-cisa-lantronix-eds5000-active-exploitation.md`
- [x] **[CRITICAL]** Cordyceps CI/CD Flaws Expose 300+ GitHub Repositories to Supply-Chain Attacks — `2026-06-24-cordyceps-cicd-github-supply-chain.md`
- [x] **[CRITICAL]** Critical Ubiquiti Vulnerabilities Actively Exploited, CISA Warns — `2026-06-24-ubiquiti-critical-vulnerabilities-exploited.md`
- [x] **[HIGH]** More Malicious OpenClaw Skills Threaten AI Supply Chain — `2026-06-24-openclaw-malicious-skills-ai-supply-chain.md`
- [x] **[HIGH]** Amadey and StealC Malware Network Disrupted, 27 Million Credentials Recovered — `2026-06-24-amadey-stealc-malware-network-disrupted.md`
- [x] **[HIGH]** macOS Weaknesses Chained to Silently Disable Endpoint Security Agents — `2026-06-24-macos-endpoint-security-bypass-chained-weaknesses.md`
- [x] **[HIGH]** New 'Mistic' RAT Opens Door to Several Ransomware Families — `2026-06-24-mistic-rat-ransomware-access-broker.md`
- [x] **[HIGH]** Cisco Unified CM Flaw Exploited After PoC Reveals Root File-Write Path — `2026-06-24-cisco-unified-cm-flaw-exploited-poc.md`
- [x] **[MEDIUM]** BeyondTrust, LastPass Impacted by Klue-Salesforce Incident — `2026-06-24-beyondtrust-lastpass-klue-salesforce-breach.md`
- [x] **[MEDIUM]** StrikeShark Campaign Delivers Cobalt Strike via SharkLoader — `2026-06-24-strikeshark-cobalt-strike-sharkloader.md`
- [x] **[INFORMATIONAL]** When Information Becomes the Attack Surface: Understanding AI Agent Traps — `2026-06-24-ai-agent-traps-attack-surface.md`
- [x] **[INFORMATIONAL]** Google DeepMind Introduces Computer Use in Gemini 3.5 Flash — `2026-06-24-gemini-3-5-flash-computer-use.md`
- [x] **[INFORMATIONAL]** OpenAI and Broadcom Unveil Jalapeño, a Custom LLM Inference Chip — `2026-06-24-openai-broadcom-jalapeno-inference-chip.md`

## Relevant (details)

### 1. CISA Warns of Active Exploitation of Critical Lantronix EDS5000 Flaw
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cisa-warns-critical-lantronix-eds5000.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `rce`
- **Slug:** `cisa-lantronix-eds5000-active-exploitation`
- **Must-know:** no
- **Summary:** CVE-2025-67038 (CVSS 9.8), a code injection flaw in Lantronix EDS5000 devices, is under active exploitation. CISA ordered FCEB agencies to patch by June 26, 2026.

### 2. Cordyceps CI/CD Flaws Expose 300+ GitHub Repositories to Supply-Chain Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cordyceps-cicd-flaws-expose-300-github.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `vulnerability`, `cve`
- **Slug:** `cordyceps-cicd-github-supply-chain`
- **Must-know:** yes
- **Summary:** Novee Security disclosed "Cordyceps," a CI/CD workflow weakness class letting attackers hijack workflows and seize full control of 300+ repos at major orgs including Microsoft, Google, and Apache.

### 3. Critical Ubiquiti Vulnerabilities Actively Exploited, CISA Warns
- **Source:** SecurityWeek — https://www.securityweek.com/critical-ubiquiti-vulnerabilities-in-attackers-crosshairs/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`
- **Slug:** `ubiquiti-critical-vulnerabilities-exploited`
- **Must-know:** no
- **Summary:** CISA warns of active exploitation of max-severity Ubiquiti UniFi OS flaws allowing unauthenticated remote attackers to modify systems, access accounts, and inject commands.

### 4. More Malicious OpenClaw Skills Threaten AI Supply Chain
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/malicious-openclaw-skills-clawhub-threaten-ai-supply-chain
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `llm`, `ai-safety`
- **Slug:** `openclaw-malicious-skills-ai-supply-chain`
- **Must-know:** no
- **Summary:** OpenClaw removed five malicious skills packages from its ClawHub marketplace that bypassed security checks despite containing infostealers, highlighting weak vetting in AI agent skill ecosystems.

### 5. Amadey and StealC Malware Network Disrupted, 27 Million Credentials Recovered
- **Source:** The Hacker News — https://thehackernews.com/2026/06/amadey-and-stealc-malware-network.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `ransomware`
- **Slug:** `amadey-stealc-malware-network-disrupted`
- **Must-know:** no
- **Summary:** A law enforcement operation (Microsoft, Europol, Bitdefender, Bitsight, ESET) under Operation Endgame took down infrastructure for Amadey and StealC malware, recovering 27 million stolen credentials.

### 6. macOS Weaknesses Chained to Silently Disable Endpoint Security Agents
- **Source:** SecurityWeek — https://www.securityweek.com/macos-weaknesses-chained-to-silently-disable-endpoint-security-agents/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`, `macos`
- **Slug:** `macos-endpoint-security-bypass-chained-weaknesses`
- **Must-know:** no
- **Summary:** A chain of legitimate macOS behaviors (not software bugs) can be abused by a standard non-admin account to silently disable endpoint security agents, with no admin privileges or kernel exploit needed.

### 7. New 'Mistic' RAT Opens Door to Several Ransomware Families
- **Source:** SecurityWeek — https://www.securityweek.com/new-mistic-rat-opens-door-to-several-ransomware-families/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `ransomware`
- **Slug:** `mistic-rat-ransomware-access-broker`
- **Must-know:** no
- **Summary:** Initial access broker Woodgnat is using a new RAT called Mistic to feed access to multiple ransomware operations including Qilin, Interlock, Rhysida, Akira, 8Base, and Black Basta.

### 8. Cisco Unified CM Flaw Exploited After PoC Reveals Root File-Write Path
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cisco-unified-cm-flaw-exploited-after.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `rce`, `vulnerability`
- **Slug:** `cisco-unified-cm-flaw-exploited-poc`
- **Must-know:** no
- **Summary:** CVE-2026-20230 (CVSS 8.6) in Cisco Unified CM and Unified CM SME is being actively exploited after a public PoC revealed an unauthenticated file-write path to root.

### 9. BeyondTrust, LastPass Impacted by Klue-Salesforce Incident
- **Source:** SecurityWeek — https://www.securityweek.com/beyondtrust-lastpass-impacted-by-klue-salesforce-incident/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`, `supply-chain`
- **Slug:** `beyondtrust-lastpass-klue-salesforce-breach`
- **Must-know:** no
- **Summary:** Over a dozen customers of Klue, including BeyondTrust and LastPass, confirmed attackers stole data from their Salesforce instances via the Klue integration.

### 10. StrikeShark Campaign Delivers Cobalt Strike via SharkLoader
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/strikeshark-campaign/120326/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `strikeshark-cobalt-strike-sharkloader`
- **Must-know:** no
- **Summary:** Kaspersky GReAT analyzed a new global campaign, StrikeShark, delivering Cobalt Strike Beacon via a custom loader called SharkLoader.

### 11. When Information Becomes the Attack Surface: Understanding AI Agent Traps
- **Source:** SecurityWeek — https://www.securityweek.com/when-information-becomes-the-attack-surface-understanding-ai-agent-traps/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `llm`, `ai-safety`, `vulnerability`
- **Slug:** `ai-agent-traps-attack-surface`
- **Must-know:** no
- **Summary:** An analysis piece on how attackers turn trusted data sources into traps for autonomous AI agents, from hidden content injections to "cognitive state poisoning."

### 12. Google DeepMind Introduces Computer Use in Gemini 3.5 Flash
- **Source:** Google DeepMind — https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash/
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `google`, `llm`
- **Slug:** `gemini-3-5-flash-computer-use`
- **Must-know:** no
- **Summary:** Google DeepMind added a computer use capability to Gemini 3.5 Flash, letting the model directly operate a computer interface. No further detail was available in the feed item.

### 13. OpenAI and Broadcom Unveil Jalapeño, a Custom LLM Inference Chip
- **Source:** OpenAI Blog — https://openai.com/index/openai-broadcom-jalapeno-inference-chip
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `ai-launch`, `openai`
- **Slug:** `openai-broadcom-jalapeno-inference-chip`
- **Must-know:** no
- **Summary:** OpenAI and Broadcom introduced Jalapeño, a custom ASIC built for LLM inference, marking OpenAI's first move into custom AI silicon.

## Skippable

- **Quoting Tom MacWright** — Simon Willison. Opinion piece on AI-generated résumés/career commentary, no security or news value.
- **The $27 million AI proxy war over Alex Bores** — The Verge AI. Political horse-race coverage of a congressional primary funded by AI super PACs, not a regulatory action or technical story.
- **Facebook rolls out an AI companion app for creators** — TechCrunch AI. Minor feature rollout, no security or capability substance.
- **Agility Robotics plans to go public via SPAC in a $2.5B deal** — TechCrunch AI. Business/SPAC news, no security angle.
- **Figma adds code layers, support for animations, more AI features** — TechCrunch AI. Generic product feature update, no security relevance.
- **Figma now has AI motion graphics and shader tools** — The Verge AI. Duplicate coverage of the same Figma Config announcement.
- **Accelerating Transformers Fine-Tuning with NVIDIA NeMo AutoModel** — Hugging Face Blog. Developer tutorial content, not a notable launch or security story.
- **Microsoft and Allies Smash Shared Infrastructure of Amadey and StealC Malware** — SecurityWeek. Duplicate coverage of the Amadey/StealC takedown.
- **OpenAI unveils its first custom chip, built by Broadcom** — TechCrunch AI. Duplicate coverage of the Jalapeño chip announcement.
- **OpenAI reveals its first AI processor: Jalapeño** — The Verge AI. Duplicate coverage of the Jalapeño chip announcement.
- **CISA warns of max severity Ubiquiti flaws exploited in attacks** — BleepingComputer. Duplicate roundup of the Lantronix and Ubiquiti CVEs, each covered as separate items above.
- **Amadey, StealC malware operations disrupted in Operation Endgame action** — BleepingComputer. Duplicate coverage of the Amadey/StealC takedown.
- **Exclusive: Meet AIVEX, a New Triage Model Built to Reduce Supply Chain Threat and Risk** — SecurityWeek. Vendor-sponsored "exclusive" promoting a commercial framework, marketing content.
- **German rail services resume after wireless communications outage** — The Record. Confirmed technical malfunction in GSM-R communications, not a cyberattack.
- **Securing the service desk: Why social engineering attacks keep succeeding** — BleepingComputer. Vendor-sponsored (Specops) generic advisory, no new IOCs or technique.
- **3 days left to save up to $190 on your TechCrunch Founder Summit 2026 pass** — TechCrunch AI. Event marketing, not news.
- **Indian auto giant Bajaj Auto hit by ransomware incident** — The Record. Regional ransomware victim disclosure without TTPs or IOCs.
- **The Google Home Speaker sounds good and looks great — but it's finicky** — The Verge AI. Consumer product review, no security angle.
- **Third DraftKings Hacker Sentenced to 18 Months in Prison** — SecurityWeek. Legal sentencing update, no new technical information.
- **Apple's MacOS Gap Lets Users Disable Security Tools** — Dark Reading. Duplicate coverage of the macOS endpoint-security-bypass story.
- **Agentic AI Security: Wrong Context, Wrong Decisions at Machine Speed** — SecurityWeek. Generic opinion/thought-leadership piece without concrete technical findings.
- **Using SASE in a Modern TIC 3.0 Solution** — CISA Alerts. Generic zero-trust/SASE guidance document, no new technical content.
- **Dawn of the Apex Agentic Adversary** — The Hacker News. Vendor thought-leadership piece on "agentic threats," no concrete technical detail or IOCs.
- **Exploitable CI/CD Vulnerabilities Expose Millions of Repositories to Hijacking** — SecurityWeek. Duplicate coverage of the Cordyceps CI/CD story.
- **Stealthy Mistic backdoor linked to ransomware access broker KongTuke** — BleepingComputer. Duplicate coverage of the Mistic RAT story.
- **DoJ Seizes Huione Cloud Account Tied to Cyber Scam Money Laundering** — The Hacker News. Law enforcement/sanctions action against a money-laundering network, no technical detail or practitioner-relevant TTPs.
