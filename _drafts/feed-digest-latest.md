# Digest — 2026-07-17 AM

- Window: last 14h
- Raw items considered: 17
- Relevant: 8
- Skippable: 9

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** CISA Adds Exploited SharePoint RCE Zero-Day CVE-2026-58644 to KEV — `2026-07-17-sharepoint-cve-2026-58644-kev.md`
- [x] **[HIGH]** CISA Urges Immediate Action on Actively Exploited Fortinet FortiSandbox Flaws — `2026-07-17-fortinet-fortisandbox-cisa-patch.md`
- [x] **[HIGH]** Coca-Cola Fairlife Ransomware Attack Halts US Dairy Production — `2026-07-16-coca-cola-fairlife-ransomware.md`
- [x] **[HIGH]** Claude for Chrome Extension Flaw Lets Malicious Extensions Trigger AI Actions — `2026-07-16-claude-chrome-extension-flaw.md`
- [x] **[MEDIUM]** New ClickLock macOS Malware Traps Users Into Revealing Login Password — `2026-07-16-clicklock-macos-malware.md`
- [x] **[MEDIUM]** 1M+ Emails Use Hidden Text to Dupe AI Security Filters — `2026-07-16-hidden-text-phishing-ai-filters.md`
- [x] **[MEDIUM]** New OkoBot Framework Deploys 20 Payloads to Steal Data, Crypto — `2026-07-16-okobot-malware-framework.md`
- [x] **[INFORMATIONAL]** Kimi K3: Moonshot AI's 2.8T-Parameter Model Launch — `2026-07-16-kimi-k3-moonshot-ai-model-launch.md`

## Relevant (details)

### 1. CISA Adds Exploited SharePoint RCE Zero-Day CVE-2026-58644 to KEV
- **Source:** The Hacker News — https://thehackernews.com/2026/07/cisa-adds-exploited-sharepoint-rce-zero.html
- **Severity:** critical
- **Tags:** `rce`, `cve`, `zero-day`, `vulnerability`
- **Summary:** CISA added CVE-2026-58644 (CVSS 9.8), a critical Microsoft SharePoint Server deserialization RCE, to its KEV catalog after active exploitation was observed shortly after disclosure. FCEB agencies must patch by July 19, 2026.

### 2. CISA Urges Immediate Action on Actively Exploited Fortinet FortiSandbox Flaws
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-warns-feds-to-patch-exploited-fortinet-fortisandbox-flaws-by-sunday/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Summary:** CISA ordered federal agencies to patch two actively exploited vulnerabilities in Fortinet's FortiSandbox threat detection platform by Sunday. No CVE identifiers or technical attack detail were included in the source summary.

### 3. Coca-Cola Fairlife Ransomware Attack Halts US Dairy Production
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/coca-cola-says-fairlife-ransomware-attack-halts-us-dairy-production/
- **Severity:** high
- **Tags:** `ransomware`
- **Summary:** A ransomware attack on Coca-Cola's Fairlife dairy subsidiary has suspended US production. Coca-Cola says product quality/safety is unaffected and Canadian production continues; no details on the threat actor or data impact were disclosed.

### 4. Claude for Chrome Extension Flaw Lets Malicious Extensions Trigger AI Actions
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/claude-chrome-extension-flaw-lets-malicious-extensions-trigger-ai-actions/
- **Severity:** high
- **Tags:** `anthropic`, `llm`, `vulnerability`
- **Summary:** A flaw in Anthropic's Claude for Chrome extension lets a malicious browser extension simulate user clicks to trigger Claude's predefined AI actions, potentially abusing connected services like Gmail, Google Docs, Calendar, and Salesforce.

### 5. New ClickLock macOS Malware Traps Users Into Revealing Login Password
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-clicklock-macos-malware-traps-users-into-revealing-login-password/
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** A new macOS info-stealer called ClickLock terminates all visible processes to force victims into re-entering their login password, which it then captures.

### 6. 1M+ Emails Use Hidden Text to Dupe AI Security Filters
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/1m-emails-hidden-text-dupe-ai-security-filters
- **Severity:** medium
- **Tags:** `phishing`, `llm`
- **Summary:** Researchers found over 1 million phishing emails using hidden "text salting" to evade AI/LLM-based email security filters, letting messages that would otherwise be flagged reach inboxes.

### 7. New OkoBot Framework Deploys 20 Payloads to Steal Data, Crypto
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-okobot-framework-deploys-20-payloads-to-steal-data-crypto/
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** A new modular malware framework called OkoBot delivers more than 20 payloads targeting cryptocurrency wallet seed phrases, credentials, and other sensitive data in a single campaign.

### 8. Kimi K3: Moonshot AI's 2.8T-Parameter Model Launch
- **Source:** Simon Willison — https://simonwillison.net/2026/Jul/16/kimi-k3/#atom-everything
- **Severity:** informational
- **Tags:** `model-release`, `llm`
- **Summary:** Moonshot AI announced Kimi K3, a 2.8 trillion-parameter model it calls the first "open 3T-class model," available now via API with open weights promised by July 27, 2026. Self-reported benchmarks place it above Claude Opus 4.8 Max and GPT-5.5 High but below Claude Fable 5 and GPT-5.6 Sol.

## Skippable

- **Risk Ledger Raises $32 Million in Series B Funding** — SecurityWeek. Funding announcement, no technical or security substance.
- **US charges two over laundering $43 million from investment fraud** — BleepingComputer. Law enforcement/financial crime story with no new IOCs or technical detail.
- **Fresh SharePoint Vulnerability Exploited Soon After Disclosure** — SecurityWeek. Duplicate coverage of CVE-2026-58644, folded into The Hacker News item above.
- **Spot birds not golf** — Simon Willison. Opinion/humor post about data center water use, no news value.
- **Firefox in WebAssembly** — Simon Willison. Interesting engineering demo but no security angle.
- **AI, Automation and Attacks: Unpacking the Unit 42 2026 Global Incident Response Report** — Unit 42. Generic report teaser; summary contains no specific findings.
- **Senator calls on Rubio, Blanche to push back against Canadian surveillance legislation** — The Record. Political pressure letter on proposed foreign legislation, not enacted policy or new technical detail.
- **Coca-Cola Suspends US Fairlife Production Due to Ransomware Attack** — SecurityWeek. Duplicate coverage of the Fairlife ransomware story, folded into the BleepingComputer item above.
- **Agentic AI Is Untamable: Ask the Right Security Questions** — Dark Reading. Opinion piece without concrete news value.
