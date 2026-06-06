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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `microsoft`, `malware`
- **Slug:** `2026-06-06-miasma-worm-microsoft-github-supply-chain`
- **Must-know:** yes
- **Summary:** The Miasma self-replicating worm compromised 73 repositories across Microsoft's Azure, Azure-Samples, Microsoft, and MicrosoftDocs GitHub organizations. GitHub disabled access to the affected repositories; any code or CI/CD workflows pulled from those orgs during the impact window should be treated as potentially compromised.

### 2. Cisco Catalyst SD-WAN Manager CVE-2026-20245 Actively Exploited, No Patch Available
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cisco-catalyst-sd-wan-manager-cve-2026.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `zero-day`, `cisco`, `vulnerability`, `cloud-security`
- **Slug:** `2026-06-06-cisco-sd-wan-cve-2026-20245-no-patch`
- **Must-know:** yes
- **Summary:** CVE-2026-20245 (CVSS 7.8) in Cisco Catalyst SD-WAN Manager is actively exploited with no patch available, affecting on-prem, Cloud-Pro, Cisco-managed cloud, and FedRAMP deployments. SD-WAN Manager's role as network-wide configuration controller makes this a high-value target; organizations should restrict management-plane access and monitor for unauthorized configuration changes immediately.

### 3. Autonomous AI Agent Finds 21 Zero-Days in FFmpeg; Chrome 149 Patches Record 429 Bugs
- **Source:** The Hacker News — https://thehackernews.com/2026/06/ai-agent-uncovers-21-zero-days-in.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `llm`, `vulnerability`, `cve`, `google`
- **Slug:** `2026-06-06-ai-agent-ffmpeg-zero-days-chrome-149`
- **Must-know:** no
- **Summary:** A security startup's autonomous AI agent discovered 21 unknown vulnerabilities in FFmpeg, the media-processing library present in virtually every video-touching application. Separately, Google's Chrome 149 shipped 429 security patches, the most ever in a single release — only the FFmpeg bugs were AI-discovered, marking a milestone for automated vulnerability research at scale.

### 4. CISA Adds Actively Exploited SolarWinds Serv-U DoS Bug CVE-2026-28318 to KEV Catalog
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cisa-adds-actively-exploited-solarwinds.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `zero-day`
- **Slug:** `2026-06-06-cisa-kev-solarwinds-serv-u-cve-2026-28318`
- **Must-know:** no
- **Summary:** CISA confirmed active exploitation of CVE-2026-28318 (CVSS 7.5), a denial-of-service flaw in SolarWinds Serv-U that causes the service to crash. Federal agencies must patch under BOD 22-01; enterprises should prioritize remediation given SolarWinds' history as a high-value target.

### 5. Polyfill Supply Chain Attack Surfaces Credential-Harvesting Prompts on Toshiba and Muji Sites
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/suspicious-polyfill-login-prompts-pop-up-on-toshiba-muji-websites/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `phishing`, `xss`
- **Slug:** `2026-06-05-polyfill-supply-chain-toshiba-muji`
- **Must-know:** no
- **Summary:** Toshiba and Muji warned visitors that unexpected sign-in prompts on their sites are linked to polyfill script injections and may be harvesting credentials. Both companies flagged the issue; web teams should audit all CDN-hosted polyfill dependencies and replace with self-hosted equivalents.

### 6. Free Apps Secretly Enroll Smart TVs as Exit Nodes in Bright Data's AI Scraping Proxy Network
- **Source:** The Hacker News — https://thehackernews.com/2026/06/free-apps-are-quietly-turning-smart-tvs.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `supply-chain`, `appsec`, `llm`
- **Slug:** `2026-06-06-bright-data-smart-tv-proxy-sdk`
- **Must-know:** no
- **Summary:** Researchers reverse-engineered the iOS SDK Bright Data (formerly Luminati) embeds in consumer apps, showing it silently enrolls devices — including always-on smart TVs — as residential proxy exit nodes marketed to AI companies for web scraping. Users of affected apps are unknowingly relaying third-party traffic without meaningful disclosure.

### 7. OpenAI Launches Lockdown Mode to Limit Data Exfiltration from Prompt Injection Attacks
- **Source:** Simon Willison — https://simonwillison.net/2026/Jun/5/openai-help-lockdown-mode/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `openai`, `ai-safety`, `llm`, `appsec`
- **Slug:** `2026-06-05-openai-lockdown-mode-prompt-injection`
- **Must-know:** no
- **Summary:** OpenAI began rolling out Lockdown Mode to personal and self-serve business ChatGPT accounts, limiting outbound network requests that could exfiltrate data following a prompt injection. The feature targets the final exfiltration step, not injection itself, and is rolling out to Free, Go, Plus, Pro, and self-serve Business tiers.

### 8. micropython-wasm: A WebAssembly Sandbox for Safe Code Execution in AI Agents
- **Source:** Simon Willison — https://simonwillison.net/2026/Jun/6/micropython-in-a-sandbox/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `llm`, `appsec`, `ai-safety`
- **Slug:** `2026-06-06-micropython-wasm-sandbox-ai-agents`
- **Must-know:** no
- **Summary:** Simon Willison released micropython-wasm (alpha), which runs MicroPython inside WebAssembly to sandbox code execution for AI agents. The project provides strong host isolation via WASM and is being used as a code execution plugin for Datasette Agent; it's an alpha and its threat model warrants review before production use.

## Skippable

- **micropython-wasm 0.1a2** — Simon Willison. Minor release note (CLI addition) for the same project covered in depth by item 8; pick the full blog post as the better source.
- **Startup Battlefield 200 applications officially close in 3 days** — TechCrunch AI. Event/marketing announcement for TechCrunch Disrupt; no security or AI technical substance.
