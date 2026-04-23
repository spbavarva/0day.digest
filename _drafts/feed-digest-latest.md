# Digest — 2026-04-23 AM

- Window: last 14h
- Raw items considered: 15
- Relevant: 8
- Skippable: 7

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Microsoft Defender Zero-Day Exploited to Dump NTLM Hashes and Gain SYSTEM Privileges — `2026-04-23-microsoft-defender-zero-day-ntlm-sam.md`
- [x] **[HIGH]** Apple Patches iOS Bug That Let FBI Recover Deleted Signal Messages via Retained Notifications — `2026-04-22-apple-ios-notification-data-retention.md`
- [x] **[HIGH]** North Korean Hackers Steal $12 Million in Crypto via Malware Campaign in Q1 2026 — `2026-04-22-north-korea-crypto-theft-12m-q1-2026.md`
- [x] **[HIGH]** Mirai Botnet Actively Exploiting RCE Flaw in End-of-Life D-Link DIR-823X Routers — `2026-04-22-mirai-cve-2025-29635-dlink-rce.md`
- [x] **[HIGH]** Previously Unknown Wiper Malware Deployed in Destructive Attack on Venezuela's Energy Sector — `2026-04-22-wiper-malware-venezuela-energy-sector.md`
- [x] **[HIGH]** Kyber Ransomware Gang Experiments with Post-Quantum Encryption on Windows and VMware ESXi — `2026-04-22-kyber-ransomware-post-quantum-encryption.md`
- [x] **[MEDIUM]** 'The Gentlemen' Ransomware Gang Draws Researcher Attention with Rapid Scale-Up — `2026-04-22-gentlemen-ransomware-rapid-rise.md`
- [x] **[MEDIUM]** OpenAI Launches Cloud-Based Workspace Agents for Enterprise ChatGPT Plans — `2026-04-22-openai-workspace-agents-enterprise.md`

## Relevant (details)

### 1. Microsoft Defender Zero-Day Exploited to Dump NTLM Hashes and Gain SYSTEM Privileges
- **Source:** SecurityWeek — https://www.securityweek.com/recent-microsoft-defender-vulnerability-exploited-as-zero-day/
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`, `microsoft`, `privilege-escalation`
- **Summary:** A Microsoft Defender flaw is being actively exploited to access the SAM database, extract NTLM hashes, and escalate to SYSTEM privileges. SAM database access enables credential dumping and lateral movement across Windows environments.

### 2. Apple Patches iOS Bug That Let FBI Recover Deleted Signal Messages via Retained Notifications
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/apple-fixes-ios-bug-that-retained-deleted-notification-data/
- **Severity:** high
- **Tags:** `vulnerability`, `apple`, `privacy`, `ios`
- **Summary:** Apple released out-of-band iOS and iPadOS updates to fix a Notification Services flaw where deleted notifications remained on-device, enabling law enforcement to recover deleted Signal messages. The bug undermines deletion guarantees that encrypted messaging apps depend on at the OS level.

### 3. North Korean Hackers Steal $12 Million in Crypto via Malware Campaign in Q1 2026
- **Source:** The Record (Recorded Future) — https://therecord.media/north-korean-hackers-siphon-12-million-from-crypto-users
- **Severity:** high
- **Tags:** `malware`, `north-korea`, `data-breach`
- **Summary:** A DPRK-affiliated threat group stole over $12 million in cryptocurrency from individual users in Q1 2026 via malware on personal devices. The campaign continues a long-running pattern of North Korean actors using crypto theft as a primary revenue stream.

### 4. Mirai Botnet Actively Exploiting RCE Flaw in End-of-Life D-Link DIR-823X Routers
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-mirai-campaign-exploits-rce-flaw-in-eol-d-link-routers/
- **Severity:** high
- **Tags:** `rce`, `malware`, `vulnerability`, `cve`
- **Summary:** A Mirai-based campaign is actively exploiting CVE-2025-29635, a command-injection RCE in D-Link DIR-823X routers, to build botnet infrastructure. The devices are EoL with no patch available; hardware replacement is the only remediation path.

### 5. Previously Unknown Wiper Malware Deployed in Destructive Attack on Venezuela's Energy Sector
- **Source:** The Record (Recorded Future) — https://therecord.media/hackers-venezuela-wiper-malware-oil
- **Severity:** high
- **Tags:** `malware`, `critical-infrastructure`
- **Summary:** Hackers deployed a novel wiper malware against Venezuela's energy and utilities sector in an attack designed to destroy systems rather than exfiltrate data. Wiper attacks on critical infrastructure are rare and typically indicate state-level or geopolitically motivated actors.

### 6. Kyber Ransomware Gang Experiments with Post-Quantum Encryption on Windows and VMware ESXi
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/kyber-ransomware-gang-toys-with-post-quantum-encryption-on-windows/
- **Severity:** high
- **Tags:** `ransomware`, `malware`, `vulnerability`
- **Summary:** The Kyber ransomware operation targets Windows and VMware ESXi with one variant using Kyber1024 post-quantum key encapsulation, which would make decryption without the attacker's key computationally infeasible. Dual Windows/ESXi targeting follows an emerging pattern of ransomware groups maximizing impact via hypervisor-level encryption.

### 7. 'The Gentlemen' Ransomware Gang Draws Researcher Attention with Rapid Scale-Up
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/gentlemen-rapidly-rise-ransomware
- **Severity:** medium
- **Tags:** `ransomware`, `malware`
- **Summary:** The Gentlemen ransomware group has impressed researchers with the speed of its operational scale-up and overall sophistication. Specific TTPs and IOCs are not yet publicly available; monitor threat intel feeds for emerging indicators.

### 8. OpenAI Launches Cloud-Based Workspace Agents for Enterprise ChatGPT Plans
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/917065/openai-chatgpt-workspace-agents-custom-teams-bots
- **Severity:** medium
- **Tags:** `openai`, `llm`, `ai-launch`
- **Summary:** OpenAI is giving Business, Enterprise, Edu, and Teachers plan subscribers access to cloud-based workspace agents for autonomous long-running business tasks. The launch raises practical questions for security teams around OAuth scope management, API key governance, and prompt injection risk in enterprise contexts.

## Skippable

- **India's app market is booming — but global platforms are capturing most of the gains** — TechCrunch AI. Market analysis piece on consumer spending trends; no security angle.
- **Tesla just increased its spending plan to $25B** — TechCrunch AI. Capex/financial planning news; no security or AI-technical angle.
- **Google updates Workspace to make AI your new office intern** — TechCrunch AI. Product feature announcement with marketing framing; no substantive security or technical depth.
- **Hands on with X's new AI-powered custom feeds** — TechCrunch AI. Product hands-on review of X's Grok-curated feed feature; no security relevance.
- **AI failure could trigger the next financial crisis, warns Elizabeth Warren** — The Verge AI. Policy speech; opinion/political commentary without actionable news or regulatory text.
- **How SpaceX preempted a $2B fundraise with a $60B buyout offer** — TechCrunch AI. Business/M&A news about Cursor and SpaceX; no security angle.
- **Google Cloud launches two new AI chips to compete with Nvidia** — TechCrunch AI. Hardware launch (TPUs); no security or practitioner-relevant angle for this digest.
