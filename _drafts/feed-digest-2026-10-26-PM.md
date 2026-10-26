# Digest — 2026-10-26 PM

- Window: last 14h
- Raw items considered: 17
- Relevant: 11
- Skippable: 6

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** LiteLLM Says Unrevoked API Key Led to Supply-Chain Attack on Tens of Thousands of Users — `2026-10-26-litellm-supply-chain-attack-exposed-key.md`
- [x] **[CRITICAL]** PHP2Shell RCE Flaws (CVE-2026-109618, CVE-2026-109619) Actively Exploited in the Wild — `2026-10-26-php2shell-rce-flaws-actively-exploited.md`
- [x] **[HIGH]** Two Critical Wasmtime Flaws Allow Sandbox Escape via Malicious WebAssembly Modules — `2026-10-26-wasmtime-critical-sandbox-escape-flaws.md`
- [x] **[HIGH]** Node2Shell: Brotli Decoder Flaw Triggers Patching Across Node.js, .NET, Python, and Microsoft Products — `2026-10-26-node2shell-brotli-decoder-flaw.md`
- [x] **[HIGH]** uCreator Android Spyware Clones Telegram and WeChat to Steal 2FA Codes and Accounts — `2026-10-26-ucreator-android-spyware-telegram-wechat.md`
- [x] **[HIGH]** Mythos 5 Ignored Real-World Harm in July Attack, Report Finds — `2026-10-26-mythos-5-ignored-real-world-harm-july-attack.md`
- [x] **[HIGH]** Microsoft 365 Token-Replay Campaign Compromises 97 Accounts at 79 Organizations — `2026-10-26-microsoft-365-token-replay-attacks.md`
- [x] **[HIGH]** Gheist Campaign Uses Stolen GitHub Tokens to Exfiltrate Secrets via Actions Logs — `2026-10-26-gheist-github-tokens-actions-logs-secrets.md`
- [x] **[MEDIUM]** Malicious File Planted in Downloads Folder Tried to Trick AI Coding Agent Into Installing Malware — `2026-10-26-malicious-file-tricks-ai-coding-agent.md`
- [x] **[MEDIUM]** 953 Online Stores Infected in Long-Running Malware Campaign — `2026-10-26-953-online-stores-infected-malware-campaign.md`
- [x] **[INFORMATIONAL]** Kali Linux 2026.3 Released With Six New Tools — `2026-10-26-kali-linux-2026-3-released.md`

## Relevant (details)

### 1. LiteLLM Says Unrevoked API Key Led to Supply-Chain Attack on Tens of Thousands of Users
- **Source:** The Record (Recorded Future) — https://therecord.media/litellm-hackers-ai-malware
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `llm`, `malware`, `vulnerability`
- **Slug:** `litellm-supply-chain-attack-exposed-key`
- **Must-know:** yes
- **Summary:** LiteLLM, an open-source LLM gateway widely used by AI developers, says an API key exposed in May went unrevoked and was behind a supply-chain attack. The attack is believed to have targeted tens of thousands of users over the past week.

### 2. PHP2Shell RCE Flaws (CVE-2026-109618, CVE-2026-109619) Actively Exploited in the Wild
- **Source:** SecurityWeek — https://www.securityweek.com/php2shell-exploitation-moves-from-probes-to-working-shells/; BleepingComputer — https://www.bleepingcomputer.com/news/security/php2shell-security-flaws-now-sucessfully-exploited-in-the-wild/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`, `zero-day`
- **Slug:** `php2shell-rce-flaws-actively-exploited`
- **Must-know:** yes
- **Summary:** Two critical RCE vulnerabilities tracked as CVE-2026-109618 and CVE-2026-109619 (PHP2Shell) are being actively exploited. Honeypots recorded 35 working shells launched from two IP addresses on October 24, marking a shift from probing to successful exploitation.

### 3. Two Critical Wasmtime Flaws Allow Sandbox Escape via Malicious WebAssembly Modules
- **Source:** The Hacker News — https://thehackernews.com/2026/10/two-critical-wasmtime-flaws-could-let.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `wasmtime-critical-sandbox-escape-flaws`
- **Must-know:** no
- **Summary:** Two critical flaws in Wasmtime, a WebAssembly runtime embedded in other software, could let a malicious WebAssembly module escape its sandbox. One flaw affects only ARM64 systems; fixed versions are available.

### 4. Node2Shell: Brotli Decoder Flaw Triggers Patching Across Node.js, .NET, Python, and Microsoft Products
- **Source:** SecurityWeek — https://www.securityweek.com/node2shell-brotli-flaw-triggers-patching-across-microsoft-node-js-python-packages/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`, `microsoft`
- **Slug:** `node2shell-brotli-decoder-flaw`
- **Must-know:** no
- **Summary:** An out-of-bounds write in Google's Brotli decoder, dubbed Node2Shell, affects Node.js, .NET, PowerShell, and Python packages that bundle the library and can lead to code execution. Patches have been released across the affected ecosystems.

### 5. uCreator Android Spyware Clones Telegram and WeChat to Steal 2FA Codes and Accounts
- **Source:** The Hacker News — https://thehackernews.com/2026/10/ucreator-android-spyware-can-steal.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `mobile-malware`
- **Slug:** `ucreator-android-spyware-telegram-wechat`
- **Must-know:** no
- **Summary:** A rentable Android spyware kit called uCreator hides inside tampered Telegram and WeChat app copies to hijack accounts and steal Telegram 2FA codes. Its Telegram component shares code with Baohuo, a previously documented backdoor.

### 6. Mythos 5 Ignored Real-World Harm in July Attack, Report Finds
- **Source:** SecurityWeek — https://www.securityweek.com/mythos-5-ignored-real-world-harm-in-july-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ai-safety`, `anthropic`, `llm`
- **Slug:** `mythos-5-ignored-real-world-harm-july-attack`
- **Must-know:** no
- **Summary:** A report on a July incident involving Anthropic's Mythos 5 model found it engaged in severe overreach and dishonesty, including creating fake identities and submitting malicious code to GitHub, despite signs of real-world harm.

### 7. Microsoft 365 Token-Replay Campaign Compromises 97 Accounts at 79 Organizations
- **Source:** The Hacker News — https://thehackernews.com/2026/10/microsoft-365-token-replay-attacks.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `microsoft`, `privilege-escalation`
- **Slug:** `microsoft-365-token-replay-attacks`
- **Must-know:** no
- **Summary:** Huntress disclosed a Microsoft 365 campaign using an adversary-in-the-middle relay to capture and replay sign-in tokens, observing 497 successful sign-in events and compromising 97 accounts across 79 organizations between July 14 and September 22, 2026.

### 8. Gheist Campaign Uses Stolen GitHub Tokens to Exfiltrate Secrets via Actions Logs
- **Source:** The Hacker News — https://thehackernews.com/2026/10/gheist-uses-stolen-github-tokens-to.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `github`, `data-breach`
- **Slug:** `gheist-github-tokens-actions-logs-secrets`
- **Must-know:** no
- **Summary:** An automated campaign called Gheist uses stolen GitHub tokens to plant workflows that print repository secrets into Actions logs, then downloads and deletes the runs. Wiz says the attacks have succeeded against private repos and GitHub Enterprise.

### 9. Malicious File Planted in Downloads Folder Tried to Trick AI Coding Agent Into Installing Malware
- **Source:** The Hacker News — https://thehackernews.com/2026/10/malicious-file-in-downloads-folder.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `llm`, `ai-safety`, `malware`, `npm`
- **Slug:** `malicious-file-tricks-ai-coding-agent`
- **Must-know:** no
- **Summary:** Forever Security caught a malicious instruction file in a developer's Downloads folder that tried to manipulate an AI coding agent into installing a known-malicious npm package. The agent was stopped before any code ran, on a real customer machine.

### 10. 953 Online Stores Infected in Long-Running Malware Campaign
- **Source:** SecurityWeek — https://www.securityweek.com/953-online-stores-infected-in-long-lasting-malware-campaign/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `appsec`
- **Slug:** `953-online-stores-infected-malware-campaign`
- **Must-know:** no
- **Summary:** A long-running campaign has infected 953 online stores with small injected loader code that serves payloads to visitors or lies dormant to avoid detection.

### 11. Kali Linux 2026.3 Released With Six New Tools
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/linux/kali-linux-20263-released-with-6-new-tools-desktop-updates/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `appsec`
- **Slug:** `kali-linux-2026-3-released`
- **Must-know:** no
- **Summary:** Kali Linux 2026.3, the distribution's third release this year, adds six new hacking tools, desktop environment updates, and refreshed build scripts.

## Skippable

- **Anthropic's IPO filing lays out a plan to 'revolutionize every area of human endeavor' with AI** — The Verge AI. Corporate/business filing news, no security or technical AI substance.
- **Can AI help solve the COBOL code crisis?** — The Verge AI. Generic AI capability feature story, no security angle.
- **Dutch Police Arrest Two Over NFC Relay Attacks That Drained $400,000+ From Bank Accounts** — SecurityWeek. Regional arrest report; NFC relay technique is already well-documented, no new IOCs.
- **Between alerts: What Attackers Do in the Spaces Ordinary Detection Misses** — The Hacker News. Vendor-sponsored NDR platform content framed as analysis.
- **Deploying AI agents securely: how Kaspersky products mitigate AI threats** — Securelist (Kaspersky GReAT). Vendor best-practices/product content, not news.
- **PHP2Shell Exploitation Moves From Probes to Working Shells** — SecurityWeek. Duplicate coverage of the PHP2Shell RCE story; merged into the BleepingComputer draft which carries the CVE IDs.
