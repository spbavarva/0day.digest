# Digest — 2026-07-21 AM

- Window: last 14h
- Raw items considered: 27
- Relevant: 13
- Skippable: 14

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** WordPress wp2shell Vulnerabilities Under Mass Exploitation — `2026-07-21-wordpress-wp2shell-mass-exploitation.md`
- [x] **[CRITICAL]** ServiceNow AI Platform Flaw Actively Exploited for Unauthenticated RCE — `2026-07-21-servicenow-ai-platform-flaw-exploited-rce.md`
- [x] **[MEDIUM]** Kaspersky Details Project CAV3RN Cyberespionage Framework — `2026-07-21-kaspersky-project-cav3rn-cyberespionage.md`
- [x] **[HIGH]** Zimbra Patches Critical Security Vulnerabilities — `2026-07-21-zimbra-patches-critical-vulnerabilities.md`
- [x] **[HIGH]** Windows LegacyHive Zero-Day Gets Unofficial Patch — `2026-07-21-windows-legacyhive-zero-day-unofficial-patch.md`
- [x] **[HIGH]** JadePuffer Deploys ENCFORGE Ransomware Against AI Infrastructure — `2026-07-21-jadepuffer-encforge-ransomware-ai-infrastructure.md`
- [x] **[INFORMATIONAL]** Anthropic's $1.5B AI Copyright Settlement Gets Final Approval — `2026-07-21-anthropic-copyright-settlement-approved.md`
- [x] **[CRITICAL]** SonicWall SMA1000 Zero-Days Exploited for Weeks to Deploy Malware — `2026-07-20-sonicwall-sma1000-zero-days-exploited.md`
- [x] **[HIGH]** Ostium Loses $23.7M in Off-Chain Infrastructure Attack — `2026-07-20-ostium-23-7m-crypto-theft-off-chain-attack.md`
- [x] **[INFORMATIONAL]** AWS Launches AI-Powered GuardDuty Investigation Agent — `2026-07-20-aws-guardduty-investigation-agent.md`
- [x] **[HIGH]** AI Coding Agents Cursor, Codex, Gemini CLI Hit by Sandbox Escapes — `2026-07-20-ai-coding-agents-sandbox-escapes.md`
- [x] **[INFORMATIONAL]** Model Context Protocol Simplifies Session Handling — `2026-07-20-mcp-session-handling-update.md`
- [x] **[INFORMATIONAL]** Ivanti Pushes LLM-Based Vulnerability Remediation — `2026-07-20-ivanti-llm-vulnerability-remediation.md`

## Relevant (details)

### 1. WordPress wp2shell Vulnerabilities Under Mass Exploitation
- **Source:** The Hacker News — https://thehackernews.com/2026/07/wordpress-wp2shell-exploitation-grows.html
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`, `wordpress`
- **Summary:** Attackers are chaining two critical WordPress vulnerabilities (CVE-2026-63030, CVE-2026-60137), dubbed "wp2shell," for unauthenticated remote code execution. Mass scanning began within days of a public exploit, putting millions of WordPress sites at risk.

### 2. ServiceNow AI Platform Flaw Actively Exploited for Unauthenticated RCE
- **Source:** The Hacker News — https://thehackernews.com/2026/07/critical-servicenow-ai-platform-flaw.html
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`
- **Summary:** A critical ServiceNow AI Platform sandbox escape vulnerability (CVE-2026-6875, CVSS 9.5) is being actively exploited for unauthenticated remote code execution. Threat intel firm Defused Cyber observed in-the-wild exploitation days after the flaw was disclosed and patched.

### 3. Kaspersky Details Project CAV3RN Cyberespionage Framework
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/project-cav3rn-cyberespionage-framework-using-outlook-and-dns/120757/
- **Severity:** medium
- **Tags:** `malware`, `cyberespionage`
- **Summary:** Kaspersky GReAT documented a new C2 module, part of "Project CAV3RN," that abuses Outlook calendar events via Microsoft Graph for command-and-control, with a DNS AAAA-record fallback for configuration recovery. The technique blends C2 traffic into legitimate Microsoft 365 activity.

### 4. Zimbra Patches Critical Security Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/zimbra-update-patches-critical-vulnerabilities/
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `ssrf`, `xss`
- **Summary:** Zimbra released an update resolving command injection, XSS, restriction bypass, and SSRF vulnerabilities. No active exploitation has been reported.

### 5. Windows LegacyHive Zero-Day Gets Unofficial Patch
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/windows-legacyhive-zero-day-flaw-gets-free-unofficial-patches/
- **Severity:** high
- **Tags:** `zero-day`, `privilege-escalation`, `vulnerability`
- **Summary:** A Windows zero-day dubbed "LegacyHive" allows privilege escalation on fully patched systems. Microsoft has not shipped an official fix, but free unofficial patches are now available.

### 6. JadePuffer Deploys ENCFORGE Ransomware Against AI Infrastructure
- **Source:** The Hacker News — https://thehackernews.com/2026/07/new-encforge-ransomware-targets-ai.html
- **Severity:** high
- **Tags:** `ransomware`, `malware`, `rce`, `ai-safety`
- **Summary:** Sysdig linked a second Langflow RCE attack to AI-agent-driven threat actor JADEPUFFER, now deploying ENCFORGE, a Go-based ransomware built specifically to encrypt model weights, vector indexes, and training datasets.

### 7. Anthropic's $1.5B AI Copyright Settlement Gets Final Approval
- **Source:** TechCrunch AI — https://techcrunch.com/2026/07/20/anthropics-landmark-1-5b-copyright-settlement-is-approved/
- **Severity:** informational
- **Tags:** `anthropic`, `copyright`
- **Summary:** A federal court gave final approval to Anthropic's $1.5 billion settlement over claims it trained models on copyrighted books without authorization. It resolves one case but leaves the broader industry-wide fair-use question unsettled.

### 8. SonicWall SMA1000 Zero-Days Exploited for Weeks to Deploy Malware
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/sonicwall-sma1000-flaws-exploited-as-zero-days-to-push-custom-malware/
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `malware`, `cve`
- **Summary:** Two SonicWall SMA1000 VPN appliance vulnerabilities were exploited as zero-days for weeks before disclosure, allowing attackers to install custom malware. SMA1000 is widely deployed for enterprise remote access.

### 9. Ostium Loses $23.7M in Off-Chain Infrastructure Attack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-steal-237-million-in-crypto-from-ostium-in-off-chain-attack/
- **Severity:** high
- **Tags:** `data-breach`, `cryptocurrency`
- **Summary:** Attackers stole $23.75 million from the Ostium trading platform's liquidity provider vault by compromising off-chain infrastructure that feeds price data into the protocol.

### 10. AWS Launches AI-Powered GuardDuty Investigation Agent
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/introducing-the-amazon-guardduty-investigation-agent-on-demand-ai-powered-threat-assessment/
- **Severity:** informational
- **Tags:** `aws`, `cloud-security`, `ai-launch`
- **Summary:** AWS launched the Amazon GuardDuty investigation agent in public preview, an AI-powered feature that automatically investigates GuardDuty findings across AWS environments, cutting investigation time from hours to minutes.

### 11. AI Coding Agents Cursor, Codex, Gemini CLI Hit by Sandbox Escapes
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cursor-codex-gemini-cli-antigravity-hit-by-sandbox-escapes/
- **Severity:** high
- **Tags:** `llm`, `appsec`, `vulnerability`, `cve`
- **Summary:** Researchers escaped the sandboxes of Cursor, Codex, Gemini CLI, and Antigravity by having the AI agent write files that trusted host tools later executed outside the sandbox. Multiple CVEs were assigned and patched.

### 12. Model Context Protocol Simplifies Session Handling
- **Source:** TechCrunch AI — https://techcrunch.com/2026/07/20/ais-most-important-protocol-is-getting-a-little-bit-easier-to-use/
- **Severity:** informational
- **Tags:** `llm`, `mcp`
- **Summary:** The Model Context Protocol is moving to a looser, "stateless" approach to server-side session IDs, closer to how ordinary websites already handle sessions.

### 13. Ivanti Pushes LLM-Based Vulnerability Remediation
- **Source:** Dark Reading — https://www.darkreading.com/cybersecurity-operations/remediating-vulnerabilities-llms-ivanti-automation
- **Severity:** informational
- **Tags:** `llm`, `devsecops`, `appsec`
- **Summary:** Ivanti CSO Daniel Spicer described the company's use of LLMs to automate vulnerability remediation, citing surprising early effectiveness from frontier models.

## Skippable

- **Microsoft shares manual fix for WSUS sync delays and timeouts** — BleepingComputer. Generic IT operations/patch management guidance, no vulnerability or security incident.
- **Exploitation of ServiceNow Vulnerability Seen Days After Disclosure** — SecurityWeek. Duplicate coverage of the ServiceNow CVE-2026-6875 story; more detailed THN version included instead.
- **Estée Lauder discloses data breach via Oracle E-Business flaw** — BleepingComputer. Generic breach disclosure without technical detail or affected user count.
- **Trump's latest AI czar has already resigned** — TechCrunch AI. Political personnel news with no technical AI or security substance.
- **Here are the 30,000 songs Sony is suing Udio's AI music generator over** — The Verge AI. Copyright litigation without broader industry/regulatory impact.
- **'WP2Shell' Opens Millions of WordPress Sites to Remote Takeover** — Dark Reading. Duplicate coverage of the wp2shell story; THN version included instead.
- **Google is working on a new AI chip designed to make Gemini more efficient** — TechCrunch AI. Speculative/rumored hardware report, no confirmed launch or security angle.
- **JadePuffer agentic attacks now target AI model data with ransomware** — BleepingComputer. Duplicate coverage of the JadePuffer/ENCFORGE story; THN version included instead.
- **SpaceX in your index fund, explained** — The Verge AI. Financial commentary, no AI or security relevance.
- **Flock Safety kills acoustic system designed to detect 'human distress'** — The Record. Product/policy decision without a security vulnerability or technical AI angle.
- **X relaunches a rebuilt Android app after year-long effort** — TechCrunch AI. Product news with no security relevance.
- **OpenAI is scared of open-weight models. Should the US be?** — TechCrunch AI. Opinion piece without hard news value.
- **25 Years After Code Red: What the Worm Era Can Teach Us About AI Security** — Dark Reading. Retrospective opinion piece without new news value.
- **Reverse-engineering is cheap now** — Simon Willison. Personal commentary/opinion post, not a news item.
