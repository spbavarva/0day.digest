# Digest — 2026-06-06 AM

- Window: last 14h
- Raw items considered: 10
- Relevant: 8
- Skippable: 2

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Miasma Worm Compromises 73 Microsoft GitHub Repositories in Supply Chain Attack — `2026-06-06-miasma-worm-microsoft-github-supply-chain.md`
- [x] **[CRITICAL]** Cisco Catalyst SD-WAN Manager CVE-2026-20245 Actively Exploited, No Patch Available — `2026-06-06-cisco-sd-wan-cve-2026-20245-no-patch.md`
- [x] **[HIGH]** Autonomous AI Agent Finds 21 Zero-Days in FFmpeg; Chrome 149 Patches Record 429 Bugs — `2026-06-06-ai-agent-ffmpeg-zero-days-chrome-149.md`
- [x] **[HIGH]** CISA Adds Actively Exploited SolarWinds Serv-U DoS Bug CVE-2026-28318 to KEV Catalog — `2026-06-06-cisa-kev-solarwinds-serv-u-cve-2026-28318.md`
- [x] **[HIGH]** Polyfill Supply Chain Attack Surfaces Credential-Harvesting Prompts on Toshiba and Muji Sites — `2026-06-05-polyfill-supply-chain-toshiba-muji.md`
- [x] **[MEDIUM]** Free Apps Secretly Enroll Smart TVs as Exit Nodes in Bright Data's AI Scraping Proxy Network — `2026-06-06-bright-data-smart-tv-proxy-sdk.md`
- [x] **[MEDIUM]** OpenAI Launches Lockdown Mode to Limit Data Exfiltration from Prompt Injection Attacks — `2026-06-05-openai-lockdown-mode-prompt-injection.md`
- [x] **[INFORMATIONAL]** micropython-wasm: A WebAssembly Sandbox for Safe Code Execution in AI Agents — `2026-06-06-micropython-wasm-sandbox-ai-agents.md`

## Relevant (details)

### 1. Miasma Worm Compromises 73 Microsoft GitHub Repositories in Supply Chain Attack
- **Source:** The Hacker News — https://thehackernews.com/2026/06/miasma-worm-hits-73-microsoft-github.html
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `microsoft`, `malware`
- **Summary:** The Miasma self-replicating worm compromised 73 repositories across Microsoft's Azure, Azure-Samples, Microsoft, and MicrosoftDocs GitHub organizations. GitHub disabled access to the affected repos; any code or CI/CD workflows pulled during the impact window should be treated as potentially compromised.

### 2. Cisco Catalyst SD-WAN Manager CVE-2026-20245 Actively Exploited, No Patch Available
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cisco-catalyst-sd-wan-manager-cve-2026.html
- **Severity:** critical
- **Tags:** `cve`, `zero-day`, `cisco`, `vulnerability`, `cloud-security`
- **Summary:** CVE-2026-20245 (CVSS 7.8) in Cisco Catalyst SD-WAN Manager is actively exploited with no patch available. Affects on-prem, Cloud-Pro, Cisco-managed, and FedRAMP deployments. Restrict management-plane access and monitor for unauthorized configuration changes immediately.

### 3. Autonomous AI Agent Finds 21 Zero-Days in FFmpeg; Chrome 149 Patches Record 429 Bugs
- **Source:** The Hacker News — https://thehackernews.com/2026/06/ai-agent-uncovers-21-zero-days-in.html
- **Severity:** high
- **Tags:** `zero-day`, `llm`, `vulnerability`, `cve`, `google`
- **Summary:** An autonomous AI agent discovered 21 unknown vulnerabilities in FFmpeg, the media-processing library embedded in virtually every video-touching application. Separately, Chrome 149 shipped 429 security patches — the most in a single release — with only the FFmpeg bugs being AI-discovered.

### 4. CISA Adds Actively Exploited SolarWinds Serv-U DoS Bug CVE-2026-28318 to KEV Catalog
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cisa-adds-actively-exploited-solarwinds.html
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `zero-day`
- **Summary:** CISA confirmed active exploitation of CVE-2026-28318 (CVSS 7.5), a denial-of-service flaw in SolarWinds Serv-U. Federal agencies must patch under BOD 22-01; enterprises should prioritize remediation given SolarWinds' targeting history.

### 5. Polyfill Supply Chain Attack Surfaces Credential-Harvesting Prompts on Toshiba and Muji Sites
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/suspicious-polyfill-login-prompts-pop-up-on-toshiba-muji-websites/
- **Severity:** high
- **Tags:** `supply-chain`, `phishing`, `xss`
- **Summary:** Toshiba and Muji warned visitors that unexpected sign-in prompts on their sites are linked to polyfill script injections and may be harvesting credentials. Web teams should audit all CDN-hosted polyfill dependencies and replace with self-hosted equivalents.

### 6. Free Apps Secretly Enroll Smart TVs as Exit Nodes in Bright Data's AI Scraping Proxy Network
- **Source:** The Hacker News — https://thehackernews.com/2026/06/free-apps-are-quietly-turning-smart-tvs.html
- **Severity:** medium
- **Tags:** `supply-chain`, `appsec`, `llm`
- **Summary:** Researchers reverse-engineered Bright Data's iOS SDK embedded in consumer apps, showing it silently enrolls devices — including always-on smart TVs — as residential proxy exit nodes marketed to AI companies for web scraping without meaningful user disclosure.

### 7. OpenAI Launches Lockdown Mode to Limit Data Exfiltration from Prompt Injection Attacks
- **Source:** Simon Willison — https://simonwillison.net/2026/Jun/5/openai-help-lockdown-mode/#atom-everything
- **Severity:** medium
- **Tags:** `openai`, `ai-safety`, `llm`, `appsec`
- **Summary:** OpenAI is rolling out Lockdown Mode to personal and self-serve business ChatGPT accounts, limiting outbound network requests that could exfiltrate data after a prompt injection. Targets the exfiltration step only — not injection itself.

### 8. micropython-wasm: A WebAssembly Sandbox for Safe Code Execution in AI Agents
- **Source:** Simon Willison — https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/#atom-everything
- **Severity:** informational
- **Tags:** `llm`, `appsec`, `ai-safety`
- **Summary:** Simon Willison released micropython-wasm (alpha), running MicroPython inside WebAssembly to sandbox code execution in AI agents. Used as a plugin for Datasette Agent; review its threat model before production use.

## Skippable

- **micropython-wasm 0.1a2** — Simon Willison. Minor release note (CLI addition) for the same project covered in depth by item 8; picked the full blog post as the better source.
- **Startup Battlefield 200 applications officially close in 3 days** — TechCrunch AI. Event/marketing announcement for TechCrunch Disrupt; no security or AI technical substance.
