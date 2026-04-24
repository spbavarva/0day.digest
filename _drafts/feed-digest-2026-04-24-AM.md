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
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `vulnerability`, `data-breach`, `cve`
- **Slug:** `2026-04-24-firestarter-backdoor-cisco-us-agency-breach`
- **Must-know:** no
- **Summary:** CISA disclosed that an unnamed US government department was breached via a Cisco vulnerability and infected with a custom backdoor called FIRESTARTER, which maintained persistent access through March 2026 without needing to re-exploit the original CVE. The disclosure is notable for the custom implant's persistence capability on network-layer infrastructure.

### 2. Bitwarden npm Supply Chain Attack Attributed to TeamPCP; Shai-Hulud Worm Component Identified
- **Source:** SecurityWeek — https://www.securityweek.com/bitwarden-npm-package-hit-in-supply-chain-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `malware`, `appsec`, `devsecops`
- **Slug:** `2026-04-24-bitwarden-supply-chain-teampcp-shai-hulud`
- **Must-know:** no
- **Summary:** Follow-up on yesterday's Bitwarden CLI npm supply chain attack: the campaign has been attributed to a threat actor called TeamPCP and includes a worm component dubbed Shai-Hulud that can spread the payload across developer environments. Developers who already rotated credentials should additionally check for worm propagation activity in CI/CD logs.

### 3. LMDeploy CVE-2026-33626 SSRF Exploited Within 13 Hours of Disclosure
- **Source:** The Hacker News — https://thehackernews.com/2026/04/lmdeploy-cve-2026-33626-flaw-exploited.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `ssrf`, `llm`, `vulnerability`, `appsec`
- **Slug:** `2026-04-24-lmdeploy-cve-2026-33626-ssrf-exploited`
- **Must-know:** no
- **Summary:** CVE-2026-33626 (CVSS 7.5), a server-side request forgery flaw in the LMDeploy LLM deployment toolkit, was exploited in the wild within 13 hours of public disclosure. The rapid weaponization and high attacker interest in LLM infrastructure make this a priority patch for any organization running internet-exposed LMDeploy instances.

### 4. China-Backed Hackers Are Industrializing Botnet Operations
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/china-hackers-industrializing-botnets
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `apt`, `cloud-security`
- **Slug:** `2026-04-24-china-botnet-industrialization`
- **Must-know:** no
- **Summary:** Chinese state-backed groups are building shared covert botnet infrastructure using compromised routers, IoT devices, and VPS nodes to route attacks with deniability — a service-model approach shared across multiple threat actors. Defenders should treat botnet-sourced traffic with state-actor scrutiny and harden exposed SOHO devices.

### 5. Hackers Actively Exploiting Unauthenticated File Upload Bug in Breeze Cache WordPress Plugin
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-exploit-file-upload-bug-in-breeze-cache-wordpress-plugin/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`
- **Slug:** `2026-04-24-breeze-cache-wordpress-file-upload-exploit`
- **Must-know:** no
- **Summary:** A critical unauthenticated arbitrary file upload vulnerability in the Breeze Cache WordPress plugin is under active exploitation, allowing attackers to plant web shells and achieve remote code execution without credentials. WordPress administrators should update or disable the plugin immediately and audit servers for web shell artifacts.

### 6. PhantomRPC: New Windows RPC Architecture Privilege Escalation Technique
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/phantomrpc-rpc-vulnerability/119428/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`, `microsoft`
- **Slug:** `2026-04-24-phantomrpc-windows-rpc-privilege-escalation`
- **Must-know:** no
- **Summary:** Kaspersky GReAT disclosed PhantomRPC, a technique exploiting a design-level weakness in Windows RPC endpoint binding that lets a local attacker register a fake RPC server to intercept calls from higher-privileged processes and escalate privileges. No CVE is assigned; this appears to be an architectural issue requiring Windows-level mitigations.

### 7. Tropic Trooper APT Pivots to Home Routers and Japanese Targets
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/tropic-trooper-apt-takes-aim-home-routers-japanese-targets
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `apt`
- **Slug:** `2026-04-24-tropic-trooper-apt-home-routers`
- **Must-know:** no
- **Summary:** China-nexus Tropic Trooper is expanding its targeting to home routers and Japanese organizations with updated tooling and TTPs, following a broader state-actor trend of using SOHO gear as persistent, low-visibility footholds. Defenders in Japan and anyone with exposed home routers should review Tropic Trooper IOCs.

### 8. Trigona Ransomware Custom Exfiltration Tool
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/trigona-ransomware-attacks-use-custom-exfiltration-tool-to-steal-data/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ransomware`, `malware`
- **Slug:** `2026-04-24-trigona-ransomware-custom-exfil-tool`
- **Must-know:** no
- **Summary:** Trigona ransomware operators have adopted a custom command-line exfiltration tool that avoids detection by hash-based controls targeting common utilities like Rclone. The shift to purpose-built tooling indicates operational maturation and requires behavioral detection approaches rather than signature-based blocking.

### 9. DeepSeek V4 Preview Release
- **Source:** Simon Willison — https://simonwillison.net/2026/Apr/24/deepseek-v4/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `deepseek`, `ai-launch`, `model-release`, `llm`
- **Slug:** `2026-04-24-deepseek-v4-open-weights-frontier`
- **Must-know:** no
- **Summary:** DeepSeek released V4-Pro (1.6T / 49B active parameters) and V4-Flash (284B / 13B active), both under MIT license with 1M token context — making V4-Pro the largest available open-weights model. The open MIT licensing means unrestricted commercial use and self-hosting with no API dependency.

### 10. Anthropic Postmortem: Three Claude Code Harness Bugs
- **Source:** Simon Willison — https://simonwillison.net/2026/Apr/24/recent-claude-code-quality-reports/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `anthropic`, `llm`
- **Slug:** `2026-04-24-claude-code-quality-postmortem`
- **Must-know:** no
- **Summary:** Anthropic's postmortem on two months of Claude Code quality complaints reveals three harness-level bugs, not model regressions — including one that cleared accumulated "thinking" from idle sessions, degrading complex agentic tasks. A useful case study for teams building on top of AI coding agents.

### 11. Anthropic Claude Personal App Connectors
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/917871/anthropic-claude-personal-app-connectors
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `anthropic`, `ai-launch`
- **Slug:** `2026-04-24-anthropic-claude-personal-app-connectors`
- **Must-know:** no
- **Summary:** Anthropic launched personal app connectors for Claude covering Spotify, Uber, TurboTax, AllTrails, Instacart, and others via OAuth flows. Security implication: expanded attack surface for prompt injection attacks via connected data sources, especially apps holding financial or location data.

## Skippable

- **Copperhelm Raises $7 Million for Agentic Cloud Security Platform** — SecurityWeek. Startup funding announcement; no technical content or security news.
- **Millisecond Converter** — Simon Willison. Trivial developer utility with no AI/security relevance.
- **It's a big one** — Simon Willison. Newsletter meta-announcement, no news content.
- **russellromney/honker** — Simon Willison. SQLite NOTIFY/LISTEN extension; useful dev tooling but no security or AI angle.
- **Serving the For You feed** — Simon Willison. Bluesky feed algorithm architecture post; general tech, not security/AI relevant.
- **Extract PDF text in your browser with LiteParse for the web** — Simon Willison. PDF parsing developer tool; no security or AI angle.
- **Bret Taylor's Sierra buys YC-backed AI startup Fragment** — TechCrunch AI. M&A news with no technical or security content.
- **Frontier AI and the Future of Defense: Your Top Questions Answered** — Unit 42 (Palo Alto). Marketing Q&A blog post; opinion/thought leadership with no hard news.
- **US sanctions Cambodian senator for millions earned through scam compounds** — The Record. Policy/enforcement action against cybercrime; no technical detail or IOCs.
- **A pelican for GPT-5.5 via the semi-official Codex backdoor API** — Simon Willison. Duplicate coverage of GPT-5.5 launch already published in `_posts/2026-04-23-openai-gpt-5-5-launch.md`.
- **Meta is laying off 10 percent of its staff** — The Verge AI. Corporate news; no security or AI technical content.
- **Meet Noscroll, an AI bot that does your doomscrolling for you** — TechCrunch AI. Consumer product launch; not relevant to security or AI practitioner audience.
- **llm-openai-via-codex 0.1a0** — Simon Willison. Minor developer tool for accessing GPT-5.5 via Codex credentials; trivial utility, no news value.
- **Bitwarden CLI npm package compromised to steal developer credentials** — BleepingComputer. Duplicate of existing `_posts/2026-04-23-checkmarx-supply-chain-bitwarden-kics.md`; new attribution details covered in item 2 above.
