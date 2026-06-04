# Digest — 2026-06-04 AM

- Window: last 14h
- Raw items considered: 13
- Relevant: 10
- Skippable: 3

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Actively Exploited Magento RCE CVE-2026-45247 Added to CISA KEV — `2026-06-04-cisa-kev-magento-rce-cve-2026-45247.md`
- [x] **[HIGH]** Large-Scale Traffic Distribution System Serves Malware via Fake Open-Source Sites — `2026-06-04-fake-oss-sites-tds-malware-delivery.md`
- [x] **[HIGH]** APT Group Silently Exfiltrated Stock Exchange Executive's Inbox for Five Months — `2026-06-04-stock-exchange-exec-outlook-espionage.md`
- [x] **[HIGH]** Cisco Unified CM Critical SSRF Flaw Gets Public PoC — Patch Urgently — `2026-06-04-cisco-unified-cm-ssrf-poc.md`
- [x] **[HIGH]** VS Code Vulnerability Enables One-Click GitHub Token Theft via Extensions — `2026-06-04-vscode-github-token-theft-one-click.md`
- [x] **[HIGH]** Chinese Threat Group Deploys New Atlas Backdoor in European Cyberattack Campaign — `2026-06-03-chinese-atlas-rat-european-cyberattacks.md`
- [x] **[HIGH]** Attackers Use AI to Automate EDR Evasion Testing Against CrowdStrike, Sophos, Defender — `2026-06-03-ai-edr-evasion-testing-automated.md`
- [x] **[MEDIUM]** CISA to Release Binding Directive on AI Vulnerability Management This Week — `2026-06-04-cisa-ai-executive-order-directive.md`
- [x] **[MEDIUM]** DOJ 'Disruption Week' Dismantles Southeast Asia Crypto Fraud Networks, Freezes $3.8M — `2026-06-04-doj-crypto-fraud-disruption-southeast-asia.md`
- [x] **[MEDIUM]** Pakistan-Linked Actor Deploys Xeno RAT Against Afghan Finance Ministry — `2026-06-04-pakistan-xeno-rat-afghan-finance-ministry.md`

## Relevant (details)

### 1. Actively Exploited Magento RCE CVE-2026-45247 Added to CISA KEV
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cisa-adds-exploited-magento-rce-flaw.html
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`, `appsec`
- **Summary:** CISA added CVE-2026-45247 (CVSS 9.8) to its KEV catalog following confirmed exploitation. The flaw is a deserialization vulnerability in the Mirasvit Cache Warmer Magento extension enabling unauthenticated RCE — any Adobe Commerce/Magento deployment running the extension needs immediate patching.

### 2. Large-Scale Traffic Distribution System Serves Malware via Fake Open-Source Sites
- **Source:** The Hacker News — https://thehackernews.com/2026/06/fake-sites-mimicking-open-source-tools.html
- **Severity:** high
- **Tags:** `malware`, `phishing`, `supply-chain`
- **Summary:** A large-scale campaign uses convincing fake open-source project portals ranking high in Google to funnel visitors through a TDS and deliver Remus Stealer, AnimateClipper, or the SessionGate framework. Developers searching for common tools by name are the primary target.

### 3. APT Group Silently Exfiltrated Stock Exchange Executive's Inbox for Five Months
- **Source:** The Hacker News — https://thehackernews.com/2026/06/hackers-spied-on-stock-exchange.html
- **Severity:** high
- **Tags:** `data-breach`, `malware`, `iam`
- **Summary:** Unknown attackers maintained access to a stock exchange executive's Outlook mailbox for five months, exfiltrating contents in small batches via Dropbox and OneDrive. Symantec/Carbon Black attribute the campaign to espionage, consistent with nation-state tradecraft.

### 4. Cisco Unified CM Critical SSRF Flaw Gets Public PoC
- **Source:** SecurityWeek — https://www.securityweek.com/cisco-warns-of-available-poc-for-critical-unified-cm-vulnerability/
- **Severity:** high
- **Tags:** `ssrf`, `cve`, `vulnerability`
- **Summary:** A public PoC now exists for a critical unauthenticated SSRF in Cisco Unified CM, widely deployed enterprise telephony infrastructure. With exploit code circulating, unpatched systems face imminent exploitation risk.

### 5. VS Code Vulnerability Enables One-Click GitHub Token Theft via Extensions
- **Source:** SecurityWeek — https://www.securityweek.com/vs-code-vulnerability-allows-one-click-github-token-theft/
- **Severity:** high
- **Tags:** `vulnerability`, `github`, `cve`
- **Summary:** A researcher published full disclosure and PoC for a VS Code flaw allowing a malicious extension to steal GitHub tokens in one click, without prior Microsoft notification. Extensions can be silently installed via `.vscode/extensions.json` recommendation files.

### 6. Chinese Threat Group Deploys New Atlas Backdoor in European Cyberattack Campaign
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/chinese-hackers-use-new-atlas-rat-malware-in-european-cyberattacks/
- **Severity:** high
- **Tags:** `malware`, `data-breach`
- **Summary:** A Chinese-speaking cybercrime group has expanded into Europe, deploying a previously undocumented Atlas backdoor alongside other tooling. The geographic shift and new custom malware suggest an escalating operational posture targeting European organizations.

### 7. Attackers Use AI to Automate EDR Evasion Testing Against CrowdStrike, Sophos, Defender
- **Source:** Dark Reading — https://www.darkreading.com/endpoint-security/attackers-automate-edr-evasion-testing
- **Severity:** high
- **Tags:** `malware`, `ai-safety`, `llm`
- **Summary:** Threat actors are using AI-driven Python scripts to automatically test malware evasion against Sophos, CrowdStrike, and Windows Defender. The AI feedback loop dramatically cuts the iteration time to develop detection-evasive payloads and lowers the required skill level.

### 8. CISA to Release Binding Directive on AI Vulnerability Management This Week
- **Source:** The Record (Recorded Future) — https://therecord.media/cisa-directive-for-ai-exec-order-release
- **Severity:** medium
- **Tags:** `ai-safety`, `vulnerability`, `policy`
- **Summary:** CISA Director Andersen announced a binding operational directive releasing this week to implement AI executive order requirements, focusing on vulnerability alleviation and management for AI systems across federal civilian agencies.

### 9. DOJ 'Disruption Week' Dismantles Southeast Asia Crypto Fraud Networks, Freezes $3.8M
- **Source:** The Hacker News — https://thehackernews.com/2026/06/doj-disrupts-southeast-asia-crypto.html
- **Severity:** medium
- **Tags:** `phishing`, `malware`
- **Summary:** DOJ's "Disruption Week" operation took down millions of accounts used by Southeast Asia-based transnational fraud networks running pig-butchering and crypto scams against Americans, freezing $3.8M in assets.

### 10. Pakistan-Linked Actor Deploys Xeno RAT Against Afghan Finance Ministry
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/pakistan-spies-afghan-finance-ministry-xeno-rat
- **Severity:** medium
- **Tags:** `malware`, `data-breach`
- **Summary:** A Pakistan-linked actor is conducting espionage against the Afghan Finance Ministry using Xeno RAT, a publicly available commodity RAT. The campaign highlights that standard TTPs with off-the-shelf tooling remain effective against resource-constrained defenders.

## Skippable

- **How Endava is redesigning software delivery around AI agents** — OpenAI Blog. Enterprise marketing case study for Endava's use of ChatGPT Enterprise and Codex; no security or model launch news value.
- **Lovable signs multiyear deal with Google Cloud to up usage 5x** — TechCrunch AI. Business partnership announcement; no security angle or AI model release.
- **Improve your application resilience with Amazon Cognito multi-Region replication** — AWS News Blog. Routine AWS feature launch for operational resilience; no meaningful security finding.
