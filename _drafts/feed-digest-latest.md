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
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`
- **Summary:** CISA added a CVSS 8.8 deserialization RCE in Microsoft SharePoint Server to its KEV catalog, citing active exploitation. Not confirmed as unpatched/zero-day, so flagged critical but not must-know.

### 2. AI Agent Runs Ransomware Attack Start to Finish, Sysdig Says
- **Source:** The Hacker News — https://thehackernews.com/2026/07/ai-agent-exploits-langflow-rce-to.html
- **Severity:** high
- **Tags:** `ai-safety`, `llm`, `ransomware`, `rce`
- **Summary:** Sysdig says it observed what it believes is the first ransomware attack executed end-to-end by an AI agent (tracked as JADEPUFFER), exploiting a Langflow RCE for initial access before autonomously stealing credentials and encrypting a target database.

### 3. FortiBleed Credential Theft Tied to INC and Lynx Ransomware Operations
- **Source:** The Hacker News — https://thehackernews.com/2026/07/fortibleed-credential-theft-linked-to.html
- **Severity:** high
- **Tags:** `data-breach`, `ransomware`, `vulnerability`
- **Summary:** Researchers attributed the FortiBleed campaign (~74,000 exposed Fortinet VPN credentials) to the INC and Lynx ransomware operations, finding an operator working negotiation panels for both groups.

### 4. ChocoPoC RAT Hides in Fake Exploit PoCs on GitHub, Targets Researchers
- **Source:** The Hacker News — https://thehackernews.com/2026/07/new-chocopoc-rat-targets-vulnerability.html
- **Severity:** medium
- **Tags:** `malware`, `github`, `supply-chain`
- **Summary:** A RAT called ChocoPoC is distributed inside fake Python PoC exploit repos on GitHub targeting security researchers; running the fake PoC steals saved passwords, cookies, and files.

### 5. Phishing Campaigns Now Auto-Adapt Payloads to Victim's Device and OS
- **Source:** Dark Reading — https://www.darkreading.com/application-security/phishing-campaigns-auto-adapt-victims-device-os
- **Severity:** medium
- **Tags:** `phishing`
- **Summary:** Attackers are fingerprinting victims via user-agent data to serve OS/device-specific phishing payloads, increasing compromise rates versus generic lures.

## Skippable

- **Missed incidents, persistent threats, and response gaps** — Securelist. General year-in-review research report, no specific incident.
- **Alleged Scattered Spider hacker extradited to the United States** — BleepingComputer / The Record. Law-enforcement/extradition news, no new technical detail.
- **Indian tech tycoon bets $30M of his own money to build AI alternative to Microsoft Office** — TechCrunch AI. Startup funding/vision piece, no security angle.
- **Medtronic notifies customers impacted by ShinyHunters data breach** — BleepingComputer. Breach notification without user count or technical substance.
- **FortiBleed credential-theft campaign linked to Lynx ransomware** — BleepingComputer. Duplicate of item #3 above.
- **Kubota says hackers had month-long access to network systems** — BleepingComputer. Breach disclosure without technical detail or IOCs.
- **Teen suspect in Scattered Spider hacks is extradited to US** — The Record. Duplicate of the extradition story above.
- **New ChocoPoC malware targets researchers via trojanized PoC exploits** — BleepingComputer. Duplicate of item #4 above.
