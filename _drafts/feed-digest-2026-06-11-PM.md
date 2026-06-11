# Digest — 2026-06-11 PM

- Window: last 14h
- Raw items considered: 44
- Relevant: 16
- Skippable: 28

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Max-Severity Ivanti Sentry Vulnerability Now Exploited in Attacks — `2026-06-11-ivanti-sentry-max-severity-exploited.md`
- [x] **[HIGH]** New Attacks Trick OpenClaw AI Agent Into Running Code and Leaking Secrets — `2026-06-11-openclaw-ai-agent-prompt-injection-attacks.md`
- [x] **[HIGH]** GreatXML Exploit Bypasses Windows BitLocker via Recovery Partition XML Files — `2026-06-11-greatxml-bitlocker-bypass-zero-day.md`
- [x] **[HIGH]** The Gentlemen Ransomware Claims 478 Victims, Can Spread Like a Worm — `2026-06-11-gentlemen-ransomware-worm-spread.md`
- [x] **[HIGH]** Oracle Addresses PeopleSoft Vulnerability Amid Reports of Zero-Day Attacks — `2026-06-11-oracle-peoplesoft-cve-2026-35273-zero-day.md`
- [x] **[HIGH]** Hackers Exploit Langflow Vulnerability for Remote Code Execution — `2026-06-11-langflow-rce-actively-exploited.md`
- [x] **[HIGH]** Splunk, Palo Alto Networks Patch Severe Vulnerabilities — `2026-06-11-splunk-palo-alto-severe-vulnerabilities-patched.md`
- [x] **[HIGH]** OceanLotus Hits Vietnam Investors With SPECTRALVIPER in FireAnt Attack — `2026-06-11-oceanlotus-spectralviper-vietnam-campaign.md`
- [x] **[HIGH]** University of Nottingham Confirms Breach After ShinyHunters Leak Data — `2026-06-11-university-of-nottingham-breach-shinyhunters.md`
- [x] **[MEDIUM]** Authorities Dismantle 'AudiA6' Ransomware Crypto-Laundering Service — `2026-06-11-audia6-ransomware-laundering-dismantled.md`
- [x] **[MEDIUM]** OnyxC2 Stealer Offers Cybercriminals Enterprise-Grade Theft for $250 a Month — `2026-06-11-onyxc2-stealer-malware-as-a-service.md`
- [x] **[MEDIUM]** Coupang Hit With Record $409 Million Data Breach Fine in Korea — `2026-06-11-coupang-409-million-data-breach-fine.md`
- [x] **[MEDIUM]** CISA Tells Federal Agencies to Patch Critical Exploited Flaws Within 3 Days — `2026-06-11-cisa-bod-26-04-three-day-patch-directive.md`
- [x] **[MEDIUM]** Trust No Skill: Integrity Verification for AI Agent Supply Chains — `2026-06-11-unit42-ai-agent-supply-chain-integrity.md`
- [x] **[MEDIUM]** GitHub to Disable npm Install Scripts by Default to Stop Supply Chain Attacks — `2026-06-11-github-disable-npm-install-scripts.md`
- [x] **[INFORMATIONAL]** Anthropic Apologizes for Invisible Claude Fable 5 Guardrails — `2026-06-11-anthropic-claude-fable-5-guardrails-apology.md`

## Relevant (details)

### 1. Max-Severity Ivanti Sentry Vulnerability Now Exploited in Attacks
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/max-severity-ivanti-sentry-vulnerability-now-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `rce`, `privilege-escalation`
- **Slug:** `ivanti-sentry-max-severity-exploited`
- **Must-know:** no
- **Summary:** Attackers are actively exploiting a recently patched, maximum-severity Ivanti Sentry flaw to gain root code execution on internet-exposed secure mobile gateways. Unpatched internet-facing instances should be considered at immediate risk.

### 2. New Attacks Trick OpenClaw AI Agent Into Running Code and Leaking Secrets
- **Source:** The Hacker News — https://thehackernews.com/2026/06/new-attacks-trick-openclaw-ai-agent.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `prompt-injection`, `ai-safety`
- **Slug:** `openclaw-ai-agent-prompt-injection-attacks`
- **Must-know:** no
- **Summary:** Two separate research teams (Imperva, Varonis) showed that the popular self-hosted OpenClaw AI agent can be driven to run attacker-controlled code or leak secrets via ordinary-looking inputs like vCards and shared location pins. Both attacks rely on prompt injection rather than traditional exploits.

### 3. GreatXML Exploit Bypasses Windows BitLocker via Recovery Partition XML Files
- **Source:** The Hacker News — https://thehackernews.com/2026/06/new-greatxml-exploit-bypasses-windows.html (also SecurityWeek)
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `privilege-escalation`, `microsoft`
- **Slug:** `greatxml-bitlocker-bypass-zero-day`
- **Must-know:** no
- **Summary:** Researcher Chaotic Eclipse released GreatXML, an unpatched PoC that abuses Microsoft Defender's offline scan to spawn a SYSTEM shell from Windows Recovery Mode, defeating BitLocker disk encryption for an attacker with physical access. No Microsoft fix is available yet.

### 4. The Gentlemen Ransomware Claims 478 Victims, Can Spread Like a Worm
- **Source:** The Hacker News — https://thehackernews.com/2026/06/the-gentlemen-ransomware-claims-478.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`, `malware`
- **Slug:** `gentlemen-ransomware-worm-spread`
- **Must-know:** no
- **Summary:** A new analysis of "The Gentlemen" ransomware operation found 478 claimed victims and worm-like self-propagation built into the malware. The group started as a double-extortion affiliate drawing on LockBit, Qilin, and Medusa RaaS resources.

### 5. Oracle Addresses PeopleSoft Vulnerability Amid Reports of Zero-Day Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/oracle-addresses-peoplesoft-vulnerability-amid-reports-of-zero-day-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`
- **Slug:** `oracle-peoplesoft-cve-2026-35273-zero-day`
- **Must-know:** no
- **Summary:** Oracle released mitigations for CVE-2026-35273 in PeopleSoft amid reports linking the flaw to ShinyHunters attacks, though Oracle has not confirmed zero-day exploitation. PeopleSoft operators should apply mitigations and check for indicators of compromise.

### 6. Hackers Exploit Langflow Vulnerability for Remote Code Execution
- **Source:** SecurityWeek — https://www.securityweek.com/hackers-exploit-langflow-vulnerability-for-remote-code-execution/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `llm`
- **Slug:** `langflow-rce-actively-exploited`
- **Must-know:** no
- **Summary:** Attackers are actively exploiting a Langflow flaw disclosed in March that lets unauthenticated attackers write files to arbitrary locations, enabling remote code execution. Langflow operators should confirm they're patched and check for unauthorized file writes.

### 7. Splunk, Palo Alto Networks Patch Severe Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/splunk-palo-alto-networks-patch-severe-vulnerabilities/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`
- **Slug:** `splunk-palo-alto-severe-vulnerabilities-patched`
- **Must-know:** no
- **Summary:** Both vendors patched severe flaws that could let attackers create or modify arbitrary files and access or modify protected resources. No active exploitation has been reported yet.

### 8. OceanLotus Hits Vietnam Investors With SPECTRALVIPER in FireAnt Attack
- **Source:** The Hacker News — https://thehackernews.com/2026/06/oceanlotus-hits-vietnam-investors-with.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `supply-chain`
- **Slug:** `oceanlotus-spectralviper-vietnam-campaign`
- **Must-know:** no
- **Summary:** OceanLotus deployed the SPECTRALVIPER backdoor in two campaigns: a multi-year espionage operation against a Vietnamese infrastructure/transport firm, and a supply-chain-enabled campaign against domestic stock investors.

### 9. University of Nottingham Confirms Breach After ShinyHunters Leak Data
- **Source:** SecurityWeek — https://www.securityweek.com/university-of-nottingham-confirms-breach-after-hackers-leak-data/ (also BleepingComputer)
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `university-of-nottingham-breach-shinyhunters`
- **Must-know:** no
- **Summary:** ShinyHunters claimed a breach of the University of Nottingham's student records system, leaking 450,000+ email addresses and other data on current students and alumni, including international campuses.

### 10. Authorities Dismantle 'AudiA6' Ransomware Crypto-Laundering Service
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/legal/authorities-dismantle-audia6-ransomware-crypto-laundering-service/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ransomware`
- **Slug:** `audia6-ransomware-laundering-dismantled`
- **Must-know:** no
- **Summary:** Law enforcement dismantled "AudiA6," a crypto-laundering service allegedly used by ransomware actors and other cybercriminals to launder more than $380 million.

### 11. OnyxC2 Stealer Offers Cybercriminals Enterprise-Grade Theft for $250 a Month
- **Source:** SecurityWeek — https://www.securityweek.com/onyxc2-stealer-offers-cybercriminals-enterprise-grade-theft-for-250-a-month/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `onyxc2-stealer-malware-as-a-service`
- **Must-know:** no
- **Summary:** A new malware-as-a-service infostealer, OnyxC2, targets 200+ apps and browser extensions for $250/month, evading detection via encrypted payloads, DLL sideloading, and in-memory execution.

### 12. Coupang Hit With Record $409 Million Data Breach Fine in Korea
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/south-korea-hits-coupang-with-record-409-million-fine-over-data-breach/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `coupang-409-million-data-breach-fine`
- **Must-know:** no
- **Summary:** South Korea's privacy regulator fined Coupang a record 624.6 billion won (~$409M) over a breach affecting more than 37 million customers, signaling tougher enforcement.

### 13. CISA Tells Federal Agencies to Patch Critical Exploited Flaws Within 3 Days
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-tells-govt-agencies-to-patch-critical-exploited-flaws-in-3-days/ (also SecurityWeek)
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `devsecops`
- **Slug:** `cisa-bod-26-04-three-day-patch-directive`
- **Must-know:** no
- **Summary:** CISA's new Binding Operational Directive 26-04 requires FCEB agencies to patch critical, actively exploited (KEV-listed) vulnerabilities within three days — a sharp tightening of prior remediation timelines.

### 14. Trust No Skill: Integrity Verification for AI Agent Supply Chains
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/ai-agent-supply-chain-risks/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `llm`, `supply-chain`, `ai-safety`
- **Slug:** `unit42-ai-agent-supply-chain-integrity`
- **Must-know:** no
- **Summary:** Unit 42 research details how unaudited third-party "skills" for AI agents can introduce hidden vulnerabilities or chain into multi-stage attacks, recommending integrity verification before deployment.

### 15. GitHub to Disable npm Install Scripts by Default to Stop Supply Chain Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/06/github-to-disable-npm-install-scripts.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `npm`, `supply-chain`, `github`, `devsecops`
- **Slug:** `github-disable-npm-install-scripts`
- **Must-know:** no
- **Summary:** GitHub announced npm v12 will disable install-script lifecycle hooks by default, removing a major automatic code-execution path abused in supply chain attacks against npm packages.

### 16. Anthropic Apologizes for Invisible Claude Fable 5 Guardrails
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/948280/anthropic-claude-fable-invisible-distillation-guardrail
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `anthropic`, `ai-safety`, `llm`
- **Slug:** `anthropic-claude-fable-5-guardrails-apology`
- **Must-know:** no
- **Summary:** Anthropic apologized for stealthily throttling Claude Fable 5 with undisclosed guardrails that affected researchers and rivals using it for competing development. The company says it will be more transparent going forward, even if Fable refuses more queries.

## Skippable

- **Phishing Attack Volume Down 20%, but Risk Still Rising** — Dark Reading. General industry trend commentary, no specific incident or technical detail.
- **A tale of two eras** — Cisco Talos. Personal newsletter reminiscence, no technical security content.
- **Amazon's data centers used 2.5 billion gallons of water last year** — The Verge AI. Environmental/resource story, no security or AI-launch angle.
- **Cyber Force not included in Senate defense policy roadmap** — The Record. Procedural legislative news, no direct practitioner impact.
- **Deezer's new tool can identify AI music from Spotify, Apple Music, and others** — TechCrunch AI. Non-security AI product launch (duplicate of Verge coverage, item below).
- **Pool's new app turns your screenshots into something useful** — TechCrunch AI. Consumer app launch, no security angle.
- **datasette 1.0a33** — Simon Willison. Minor alpha release of an existing dev tool, no security substance.
- **British high school sends students home following cyberattack** — The Record. Single-school incident, no TTPs or IOCs.
- **Hacker linked to Void Blizzard faces charges over cyberespionage campaign** — The Record. Law enforcement update with no new technical detail or IOCs.
- **Segmentation Works for OT If Operators Are Paying Attention** — Dark Reading. General best-practice opinion piece, no specific incident.
- **DoorDash's new AI chatbot lets you order with prompts and photos** — TechCrunch AI. Consumer product launch, no security angle.
- **Why AI-driven threats are exposing the limits of MSP security stacks** — BleepingComputer. Vendor-sponsored (Kaseya) marketing content.
- **University of Nottingham confirms cyber incident as Shiny Hunters group claims data theft** — The Record. Duplicate coverage of the Nottingham breach (see item 9 above).
- **Alert Fatigue Is Becoming a Security Threat of Its Own** — SecurityWeek. Opinion piece on industry trends, no specific incident.
- **Cybersecurity Stars Awards 2026: Winners Announced Across 95 Categories** — The Hacker News. Awards announcement, no security substance.
- **ThreatsDay Bulletin: Worm Code Leaked, AI Agent Phished, Claude Code Patch + 28 New Stories** — The Hacker News. Weekly roundup bulletin; constituent stories already represented individually in this digest.
- **CISA Directs Federal Agencies to Prioritize Security Patches Based on Risk** — SecurityWeek. Duplicate coverage of CISA BOD 26-04 (see item 13 above).
- **Yarbo Android/iOS Mobile Application and Cloud Infrastructure** — CISA Alerts. Routine ICS advisory for a niche consumer robot product, no active exploitation reported.
- **Naxclow IoT Platform** — CISA Alerts. Routine ICS advisory for niche consumer IoT devices, no active exploitation reported.
- **Brickcom Cameras** — CISA Alerts. Routine ICS advisory for a niche camera product, no active exploitation reported.
- **Siemens Says Desigo CC Files Flagged as Malware by Security Engines** — SecurityWeek. Antivirus false-positive issue, not an actual vulnerability or threat.
- **AI Broke Vulnerability Management. That's Why CISOs Are Moving Budget to BAS.** — The Hacker News. Vendor-flavored opinion piece on industry trends, no specific incident.
- **FBI Seizes 13 Websites That Officials Say Were Used by China to Target and Recruit US Workers** — SecurityWeek. Law enforcement action, no new IOCs or technical guidance.
- **'GreatXML' Zero-Day Exploit Bypasses BitLocker** — SecurityWeek. Duplicate coverage of GreatXML BitLocker bypass (see item 3 above).
- **Microsoft fixes BitLocker recovery bug on Windows Server 2025** — BleepingComputer. Routine update-related bug fix, not a security vulnerability.
- **Deezer launches an AI music detector for other streaming services** — The Verge AI. Non-security AI product launch (duplicate of TechCrunch coverage above).
- **Nottingham University data breach affects over 450,000 students** — BleepingComputer. Duplicate coverage of the Nottingham breach (see item 9 above).
- **asyncinject 0.7** — Simon Willison. Minor library release update, no security substance.
