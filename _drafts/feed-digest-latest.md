# Digest — 2026-06-24 AM

- Window: last 14h
- Raw items considered: 16
- Relevant: 6
- Skippable: 10

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** BeyondTrust, LastPass Impacted by Klue-Salesforce Incident — `2026-06-24-beyondtrust-lastpass-klue-salesforce.md`
- [x] **[CRITICAL]** Scope of Salesforce Attacks Expands as Icarus Leaks Data — `2026-06-23-salesforce-attacks-expand-icarus-leaks-data.md`
- [x] **[HIGH]** Cisco Unified CM Flaw Exploited After PoC Reveals File-Write Path to Root — `2026-06-24-cisco-unified-cm-cve-2026-20230-exploited.md`
- [x] **[HIGH]** StrikeShark: Investigating a New Campaign Delivering Cobalt Strike Through SharkLoader — `2026-06-24-strikeshark-sharkloader-cobalt-strike.md`
- [x] **[HIGH]** OpenClaw's Skill Marketplace and the Emerging AI Supply Chain Threat — `2026-06-23-openclaw-skill-marketplace-ai-supply-chain.md`
- [x] **[MEDIUM]** Anthropic's Mythos Model Found Vulnerabilities in Classified US Government Systems, Official Says — `2026-06-24-anthropic-mythos-classified-govt-vulnerabilities.md`

## Relevant (details)

### 1. BeyondTrust, LastPass Impacted by Klue-Salesforce Incident
- **Source:** SecurityWeek — https://www.securityweek.com/beyondtrust-lastpass-impacted-by-klue-salesforce-incident/
- **Severity:** critical
- **Tags:** `supply-chain`, `data-breach`
- **Summary:** More than a dozen Klue customers, including BeyondTrust and LastPass, have confirmed attackers stole data from their connected Salesforce instances via abused OAuth tokens. This widens the previously disclosed Klue-Salesforce supply chain incident to additional named victims.

### 2. Scope of Salesforce Attacks Expands as Icarus Leaks Data
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/scope-salesforce-attacks-expands-icarus-leaks-data
- **Severity:** critical
- **Tags:** `supply-chain`, `data-breach`
- **Summary:** A threat actor calling itself Icarus has begun leaking data stolen via the Klue OAuth token abuse incident, with more victims emerging beyond the initial disclosure.

### 3. Cisco Unified CM Flaw Exploited After PoC Reveals File-Write Path to Root
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cisco-unified-cm-flaw-exploited-after.html
- **Severity:** high
- **Tags:** `cve`, `ssrf`, `privilege-escalation`
- **Summary:** CVE-2026-20230 (CVSS 8.6), an improper input validation flaw in Cisco Unified Communications Manager and Unified CM SME, is now under active exploitation following a public PoC demonstrating a file-write path to root.

### 4. StrikeShark: Investigating a New Campaign Delivering Cobalt Strike Through SharkLoader
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/strikeshark-campaign/120326/
- **Severity:** high
- **Tags:** `malware`
- **Summary:** Kaspersky GReAT documented a new global campaign, StrikeShark, delivering Cobalt Strike Beacon via a custom loader called SharkLoader.

### 5. OpenClaw's Skill Marketplace and the Emerging AI Supply Chain Threat
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `llm`, `ai-safety`
- **Summary:** Unit 42 found evasive malicious skills on ClawHub, the skill marketplace for the OpenClaw AI agent platform, bypassing automated scanners to deploy infostealers and execute agentic financial fraud.

### 6. Anthropic's Mythos Model Found Vulnerabilities in Classified US Government Systems, Official Says
- **Source:** SecurityWeek — https://www.securityweek.com/anthropics-mythos-model-found-vulnerabilities-in-classified-us-government-systems-official-says/
- **Severity:** medium
- **Tags:** `anthropic`, `llm`, `ai-safety`, `vulnerability`
- **Summary:** A U.S. government official said Anthropic's Mythos model found vulnerabilities in classified government systems within hours during testing, though fast discovery doesn't mean the model could have exploited them in that time.

## Skippable

- **DoJ Seizes Huione Cloud Account Tied to Cyber Scam Money Laundering** — The Hacker News. Law-enforcement/sanctions action against scam-network infrastructure, no new IOCs or technical detail.
- **Webinar Today: Modern Exposure Validation in the AI Era** — SecurityWeek. Vendor webinar promotion, not news.
- **Hackers Exploiting Cisco Unified CM Vulnerability** — SecurityWeek. Duplicate coverage of CVE-2026-20230; The Hacker News write-up has more technical detail.
- **India's MoEngage bets that the future of marketing is millions of AI agents** — TechCrunch AI. Marketing-driven AI agent acquisition story, no security angle.
- **Google Home will soon get better at recognizing you** — The Verge AI. Consumer facial-recognition feature update, no security or model-capability substance.
- **Hollywood is bending the knee to OpenAI** — The Verge AI. Entertainment-industry distribution story, no security or technical AI content.
- **Cisco Unified CM flaw CVE-2026-20230 now exploited in attacks** — BleepingComputer. Duplicate coverage of CVE-2026-20230; consolidated into The Hacker News item.
- **datasette 1.0a35** — Simon Willison. Database tool release notes, no security angle.
- **Tata Electronics confirms cyberattack as hackers leak data** — BleepingComputer. Breach disclosure without TTPs or IOCs.
- **Windows 11 KB5095093 update rolls out new Point-in-Time restore feature** — BleepingComputer. Routine feature update, no vulnerability or security advisory content.
