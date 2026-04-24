# Digest — 2026-04-24 AM

- Window: last 14h
- Raw items considered: 25
- Relevant: 11
- Skippable: 14

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** FIRESTARTER Backdoor Gave Attackers Persistent Access to US Agency via Cisco Vulnerability — `2026-04-24-firestarter-backdoor-cisco-us-agency-breach.md`
- [x] **[HIGH]** Bitwarden npm Supply Chain Attack Attributed to TeamPCP; Shai-Hulud Worm Component Identified — `2026-04-24-bitwarden-supply-chain-teampcp-shai-hulud.md`
- [x] **[HIGH]** LMDeploy CVE-2026-33626 SSRF Exploited in the Wild Within 13 Hours of Disclosure — `2026-04-24-lmdeploy-cve-2026-33626-ssrf-exploited.md`
- [x] **[HIGH]** China-Backed Hackers Are Industrializing Botnet Operations for Low-Attribution Attacks — `2026-04-24-china-botnet-industrialization.md`
- [x] **[HIGH]** Hackers Actively Exploiting Unauthenticated File Upload Bug in Breeze Cache WordPress Plugin — `2026-04-24-breeze-cache-wordpress-file-upload-exploit.md`
- [x] **[HIGH]** PhantomRPC: Kaspersky Discloses New Windows RPC Architecture Privilege Escalation Technique — `2026-04-24-phantomrpc-windows-rpc-privilege-escalation.md`
- [x] **[HIGH]** Tropic Trooper APT Pivots to Home Routers and Japanese Targets with New TTPs — `2026-04-24-tropic-trooper-apt-home-routers.md`
- [x] **[MEDIUM]** Trigona Ransomware Deploys Custom Exfiltration Tool to Speed Data Theft Before Encryption — `2026-04-24-trigona-ransomware-custom-exfil-tool.md`
- [x] **[MEDIUM]** DeepSeek Releases V4 Preview: Largest Open-Weights Model at 1.6T Parameters Under MIT License — `2026-04-24-deepseek-v4-open-weights-frontier.md`
- [x] **[MEDIUM]** Anthropic Postmortem: Three Claude Code Harness Bugs Caused Two Months of Quality Degradation — `2026-04-24-claude-code-quality-postmortem.md`
- [x] **[INFORMATIONAL]** Anthropic Launches Personal App Connectors for Claude: Spotify, Uber, TurboTax, and More — `2026-04-24-anthropic-claude-personal-app-connectors.md`

## Relevant (details)

### 1. FIRESTARTER Backdoor Gave Attackers Persistent Access to US Agency via Cisco Vulnerability
- **Source:** The Record (Recorded Future) — https://therecord.media/cisa-us-agency-breached-cisco-vulnerability-backdoor
- **Severity:** high
- **Tags:** `malware`, `vulnerability`, `data-breach`, `cve`
- **Summary:** CISA disclosed that an unnamed US government department was breached via a Cisco vulnerability and infected with custom malware called FIRESTARTER that maintained persistent backdoor access through March 2026 without re-exploiting the original CVE. Organizations running internet-exposed Cisco appliances should audit for FIRESTARTER IOCs.

### 2. Bitwarden npm Supply Chain Attack Attributed to TeamPCP; Shai-Hulud Worm Component Identified
- **Source:** SecurityWeek — https://www.securityweek.com/bitwarden-npm-package-hit-in-supply-chain-attack/
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `malware`, `appsec`, `devsecops`
- **Summary:** Follow-up attribution on yesterday's Bitwarden CLI supply chain attack names TeamPCP as the threat actor and identifies a worm component (Shai-Hulud) that can spread the payload across developer environments. Developers who rotated credentials should also check CI/CD logs for worm propagation activity.

### 3. LMDeploy CVE-2026-33626 SSRF Exploited Within 13 Hours of Disclosure
- **Source:** The Hacker News — https://thehackernews.com/2026/04/lmdeploy-cve-2026-33626-flaw-exploited.html
- **Severity:** high
- **Tags:** `cve`, `ssrf`, `llm`, `vulnerability`, `appsec`
- **Summary:** A high-severity SSRF flaw (CVSS 7.5) in the LMDeploy LLM deployment toolkit was exploited in the wild within 13 hours of disclosure, highlighting aggressive attacker interest in LLM infrastructure. Internet-exposed LMDeploy instances should be patched immediately and treated as potentially compromised.

### 4. China-Backed Hackers Are Industrializing Botnet Operations
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/china-hackers-industrializing-botnets
- **Severity:** high
- **Tags:** `malware`, `apt`, `cloud-security`
- **Summary:** Chinese state-backed groups are operating shared botnet infrastructure as a low-cost, deniable attack layer — routing operations through compromised routers and IoT devices across multiple threat actors. Defenders should treat botnet-origin traffic with state-actor scrutiny.

### 5. Hackers Actively Exploiting Unauthenticated File Upload Bug in Breeze Cache WordPress Plugin
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-exploit-file-upload-bug-in-breeze-cache-wordpress-plugin/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`
- **Summary:** Active exploitation of a critical unauthenticated file upload bug in the Breeze Cache WordPress plugin enables remote code execution via web shell placement. WordPress admins should update or disable the plugin immediately and audit for web shells.

### 6. PhantomRPC: New Windows RPC Architecture Privilege Escalation Technique
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/phantomrpc-rpc-vulnerability/119428/
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`, `microsoft`
- **Summary:** Kaspersky GReAT disclosed PhantomRPC, a design-level Windows RPC weakness that lets a local attacker create a fake RPC server to intercept calls from higher-privileged processes and escalate privileges without modifying system files or loading unsigned drivers.

### 7. Tropic Trooper APT Pivots to Home Routers and Japanese Targets
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/tropic-trooper-apt-takes-aim-home-routers-japanese-targets
- **Severity:** high
- **Tags:** `malware`, `apt`
- **Summary:** China-nexus Tropic Trooper is expanding to home router targeting and Japanese organizations with updated TTPs, continuing the state-actor trend of using SOHO gear as low-visibility persistent footholds. Defenders in Japan should review Tropic Trooper IOCs.

### 8. Trigona Ransomware Deploys Custom Exfiltration Tool
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/trigona-ransomware-attacks-use-custom-exfiltration-tool-to-steal-data/
- **Severity:** medium
- **Tags:** `ransomware`, `malware`
- **Summary:** Trigona ransomware has adopted a custom exfiltration tool in recent attacks to evade hash-based detection of known utilities like Rclone. Behavioral detections for large-scale file staging are more effective than signature-based controls against this tooling.

### 9. DeepSeek Releases V4 Preview
- **Source:** Simon Willison — https://simonwillison.net/2026/Apr/24/deepseek-v4/#atom-everything
- **Severity:** medium
- **Tags:** `deepseek`, `ai-launch`, `model-release`, `llm`
- **Summary:** DeepSeek released V4-Pro (1.6T parameters, now the largest open-weights model) and V4-Flash under MIT license with 1M token context, enabling unrestricted commercial deployment and self-hosting without API dependency.

### 10. Anthropic Postmortem: Three Claude Code Harness Bugs
- **Source:** Simon Willison — https://simonwillison.net/2026/Apr/24/recent-claude-code-quality-reports/#atom-everything
- **Severity:** medium
- **Tags:** `anthropic`, `llm`
- **Summary:** Anthropic confirmed three harness-level bugs — not model regressions — caused two months of Claude Code quality degradation, including one that cleared session "thinking" after idle periods. Useful case study for teams building agentic AI workflows.

### 11. Anthropic Claude Personal App Connectors
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/917871/anthropic-claude-personal-app-connectors
- **Severity:** informational
- **Tags:** `anthropic`, `ai-launch`
- **Summary:** Anthropic launched OAuth-based personal app connectors for Claude covering Spotify, Uber, TurboTax, AllTrails, and others, expanding the attack surface for prompt injection via connected data sources.

## Skippable

- **Copperhelm Raises $7 Million for Agentic Cloud Security Platform** — SecurityWeek. Startup funding; no technical content.
- **Millisecond Converter** — Simon Willison. Trivial developer utility; no AI/security relevance.
- **It's a big one** — Simon Willison. Newsletter announcement; no news content.
- **russellromney/honker** — Simon Willison. SQLite extension for pub/sub; not security or AI relevant.
- **Serving the For You feed** — Simon Willison. Bluesky feed architecture; general tech, not security/AI relevant.
- **Extract PDF text in your browser with LiteParse for the web** — Simon Willison. PDF parsing tool; no security or AI angle.
- **Bret Taylor's Sierra buys YC-backed AI startup Fragment** — TechCrunch AI. M&A news; no technical or security content.
- **Frontier AI and the Future of Defense: Your Top Questions Answered** — Unit 42 (Palo Alto). Marketing Q&A; opinion content with no hard news.
- **US sanctions Cambodian senator for millions earned through scam compounds** — The Record. Policy/enforcement action; no technical detail or IOCs.
- **A pelican for GPT-5.5 via the semi-official Codex backdoor API** — Simon Willison. Duplicate of `_posts/2026-04-23-openai-gpt-5-5-launch.md`.
- **Meta is laying off 10 percent of its staff** — The Verge AI. Corporate news; no security or AI technical content.
- **Meet Noscroll, an AI bot that does your doomscrolling for you** — TechCrunch AI. Consumer product; not relevant.
- **llm-openai-via-codex 0.1a0** — Simon Willison. Minor developer tool; no news value.
- **Bitwarden CLI npm package compromised to steal developer credentials** — BleepingComputer. Duplicate of `_posts/2026-04-23-checkmarx-supply-chain-bitwarden-kics.md`; attribution update covered in item 2 above.
