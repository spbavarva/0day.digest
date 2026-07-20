# Digest — 2026-07-20 AM

- Window: last 14h
- Raw items considered: 9
- Relevant: 6
- Skippable: 3

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Critical ServiceNow AI Platform Flaw Actively Exploited — `2026-07-20-servicenow-ai-platform-rce-exploited.md`
- [x] **[HIGH]** Hugging Face Breached by Autonomous AI Agent — `2026-07-20-hugging-face-autonomous-ai-agent-breach.md`
- [x] **[HIGH]** WP2Shell WordPress Vulnerabilities Exploited in the Wild — `2026-07-20-wp2shell-wordpress-vulnerabilities-exploited.md`
- [x] **[HIGH]** SleeperGem Supply Chain Attack Hits RubyGems Developers — `2026-07-20-sleepergem-rubygems-supply-chain-attack.md`
- [x] **[HIGH]** Critical NGINX Flaw Enables Worker Crash, Possible RCE — `2026-07-19-nginx-critical-rce-dos-cve-2026-42533.md`
- [x] **[MEDIUM]** Chrome 150 Patches Severe Memory Safety Bugs — `2026-07-20-chrome-150-memory-safety-patches.md`

## Relevant (details)

### 1. Critical ServiceNow AI Platform Flaw Actively Exploited
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/critical-servicenow-code-execution-flaw-now-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `rce`, `vulnerability`, `zero-day`
- **Slug:** `servicenow-ai-platform-rce-exploited`
- **Must-know:** yes
- **Summary:** Threat intel firm Defused reports active exploitation of CVE-2026-6875, a critical code execution flaw in the ServiceNow AI Platform. Attackers are already exploiting affected instances in the wild.

### 2. Hugging Face Breached by Autonomous AI Agent
- **Source:** The Hacker News — https://thehackernews.com/2026/07/worlds-largest-ai-model-repository.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `ai-safety`, `huggingface`
- **Slug:** `hugging-face-autonomous-ai-agent-breach`
- **Must-know:** no
- **Summary:** Hugging Face disclosed a breach of its production infrastructure carried out by an autonomous AI agent system, detected and responded to last week. Attackers accessed a limited set of internal datasets and several service credentials.

### 3. WP2Shell WordPress Vulnerabilities Exploited in the Wild
- **Source:** SecurityWeek — https://www.securityweek.com/wp2shell-wordpress-vulnerabilities-exploited-in-the-wild/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `rce`, `vulnerability`
- **Slug:** `wp2shell-wordpress-vulnerabilities-exploited`
- **Must-know:** no
- **Summary:** Two new WordPress vulnerabilities (CVE-2026-60137, CVE-2026-63030), dubbed WP2Shell, are being exploited in the wild shortly after disclosure. Site operators running the affected component should patch immediately.

### 4. SleeperGem Supply Chain Attack Hits RubyGems Developers
- **Source:** The Hacker News — https://thehackernews.com/2026/07/sleepergem-uses-three-malicious.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `malware`
- **Slug:** `sleepergem-rubygems-supply-chain-attack`
- **Must-know:** no
- **Summary:** Researchers found three malicious RubyGems packages, including one impersonating the legitimate git_credential_manager tool, published to deliver additional payloads to developer machines.

### 5. Critical NGINX Flaw Enables Worker Crash, Possible RCE
- **Source:** The Hacker News — https://thehackernews.com/2026/07/critical-nginx-vulnerability-can-crash.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `rce`, `vulnerability`
- **Slug:** `nginx-critical-rce-dos-cve-2026-42533`
- **Must-know:** no
- **Summary:** F5 patched a critical nginx heap buffer overflow (CVE-2026-42533) reachable by an unauthenticated remote attacker via crafted HTTP requests. It can crash worker processes and may allow remote code execution.

### 6. Chrome 150 Patches Severe Memory Safety Bugs
- **Source:** SecurityWeek — https://www.securityweek.com/chrome-150-update-patches-severe-memory-safety-bugs/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`
- **Slug:** `chrome-150-memory-safety-patches`
- **Must-know:** no
- **Summary:** Chrome 150 resolves six critical and high-severity use-after-free bugs. No active exploitation was reported at time of disclosure.

## Skippable

- **Hugging Face Hacked in Autonomous AI Attack** — SecurityWeek. Duplicate coverage of the Hugging Face breach; The Hacker News item has more detail and was used as the primary source.
- **Quoting Sam Altman** — Simon Willison. A historical 2022 email quote surfaced in Musk v. Altman litigation; commentary/opinion piece, no current security or product news.
- **What to watch for after Jensen Huang's Japan visit** — TechCrunch AI. Generic forward-looking business analysis with no security or technical substance.
