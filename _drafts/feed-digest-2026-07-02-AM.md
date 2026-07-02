# Digest — 2026-07-02 AM

- Window: last 14h
- Raw items considered: 13
- Relevant: 5
- Skippable: 8

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** CISA Adds Actively Exploited SharePoint RCE (CVE-2026-45659) to KEV Catalog — `2026-07-02-sharepoint-rce-cve-2026-45659-cisa-kev.md`
- [x] **[HIGH]** AI Agent Runs Ransomware Attack Start to Finish, Sysdig Says — `2026-07-02-ai-agent-langflow-rce-ransomware-jadepuffer.md`
- [x] **[HIGH]** FortiBleed Credential Theft Tied to INC and Lynx Ransomware Operations — `2026-07-02-fortibleed-credential-theft-linked-ransomware.md`
- [x] **[MEDIUM]** ChocoPoC RAT Hides in Fake Exploit PoCs on GitHub, Targets Researchers — `2026-07-02-chocopoc-rat-targets-vulnerability-researchers.md`
- [x] **[MEDIUM]** Phishing Campaigns Now Auto-Adapt Payloads to Victim's Device and OS — `2026-07-01-phishing-campaigns-auto-adapt-device-os.md`

## Relevant (details)

### 1. CISA Adds Actively Exploited SharePoint RCE (CVE-2026-45659) to KEV Catalog
- **Source:** The Hacker News — https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `sharepoint-rce-cve-2026-45659-cisa-kev`
- **Must-know:** no
- **Summary:** CISA added a CVSS 8.8 deserialization RCE in Microsoft SharePoint Server to its Known Exploited Vulnerabilities catalog, citing evidence of active exploitation. No confirmation was given that this is unpatched (zero-day), so it's flagged critical but not must-know.

### 2. AI Agent Runs Ransomware Attack Start to Finish, Sysdig Says
- **Source:** The Hacker News — https://thehackernews.com/2026/07/ai-agent-exploits-langflow-rce-to.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ai-safety`, `llm`, `ransomware`, `rce`
- **Slug:** `ai-agent-langflow-rce-ransomware-jadepuffer`
- **Must-know:** no
- **Summary:** Sysdig's Threat Research Team says it observed what it believes is the first ransomware attack executed end-to-end by an AI agent (tracked as JADEPUFFER), which exploited a Langflow RCE for initial access before autonomously stealing credentials and encrypting a target database.

### 3. FortiBleed Credential Theft Tied to INC and Lynx Ransomware Operations
- **Source:** The Hacker News — https://thehackernews.com/2026/07/fortibleed-credential-theft-linked-to.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `ransomware`, `vulnerability`
- **Slug:** `fortibleed-credential-theft-linked-ransomware`
- **Must-know:** no
- **Summary:** Researchers attributed the FortiBleed campaign (nearly 74,000 exposed Fortinet VPN credentials) to the INC and Lynx ransomware operations, finding an operator working negotiation panels for both groups. Duplicate coverage from BleepingComputer skipped; THN version used.

### 4. ChocoPoC RAT Hides in Fake Exploit PoCs on GitHub, Targets Researchers
- **Source:** The Hacker News — https://thehackernews.com/2026/07/new-chocopoc-rat-targets-vulnerability.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `github`, `supply-chain`
- **Slug:** `chocopoc-rat-targets-vulnerability-researchers`
- **Must-know:** no
- **Summary:** A RAT called ChocoPoC is distributed inside fake Python PoC exploit repos on GitHub targeting security researchers; running the fake PoC steals saved passwords, cookies, and files. Duplicate coverage from BleepingComputer skipped; THN version used.

### 5. Phishing Campaigns Now Auto-Adapt Payloads to Victim's Device and OS
- **Source:** Dark Reading — https://www.darkreading.com/application-security/phishing-campaigns-auto-adapt-victims-device-os
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`
- **Slug:** `phishing-campaigns-auto-adapt-device-os`
- **Must-know:** no
- **Summary:** Attackers are fingerprinting victims via user-agent data to serve OS/device-specific phishing payloads, which researchers say increases compromise rates versus generic lures.

## Skippable

- **Missed incidents, persistent threats, and response gaps** — Securelist. General year-in-review research report, no specific incident or new technical finding.
- **Alleged Scattered Spider hacker extradited to the United States** — BleepingComputer / The Record (duplicate coverage). Law-enforcement/extradition news, no new technical detail; picked neither as neither adds TTPs.
- **Indian tech tycoon bets $30M of his own money to build AI alternative to Microsoft Office** — TechCrunch AI. Startup funding/vision piece, no product launch detail or security angle.
- **Medtronic notifies customers impacted by ShinyHunters data breach** — BleepingComputer. Breach notification without affected-user count or technical substance.
- **FortiBleed credential-theft campaign linked to Lynx ransomware** — BleepingComputer. Duplicate of The Hacker News item #3 above; THN version used instead.
- **Kubota says hackers had month-long access to network systems** — BleepingComputer. Breach disclosure without technical detail, IOCs, or affected-user count.
- **Teen suspect in Scattered Spider hacks is extradited to US** — The Record. Duplicate of the extradition story above; no new technical detail.
- **New ChocoPoC malware targets researchers via trojanized PoC exploits** — BleepingComputer. Duplicate of The Hacker News item #4 above; THN version used instead.
