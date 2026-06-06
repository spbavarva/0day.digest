# Digest — 2026-06-06 PM

- Window: last 14h
- Raw items considered: 15
- Relevant: 9
- Skippable: 6

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Miasma Worm Compromises 73 Microsoft GitHub Repositories in Supply Chain Attack — `2026-06-06-miasma-worm-microsoft-github-supply-chain.md`
- [x] **[CRITICAL]** Cisco SD-WAN Manager CVE-2026-20245 Under Active Exploitation — No Patch Available — `2026-06-06-cisco-sdwan-cve-2026-20245-no-patch-active-exploit.md`
- [x] **[CRITICAL]** CVE-2026-3300: Critical Everest Forms Pro Flaw Actively Exploited for WordPress Takeover — `2026-06-06-everest-forms-pro-cve-2026-3300-wordpress-exploit.md`
- [x] **[HIGH]** AI Agent Autonomously Discovers 21 Zero-Days in FFmpeg; Chrome Ships Record 429 Patches — `2026-06-06-ai-agent-ffmpeg-21-zero-days-chrome-429-patches.md`
- [x] **[HIGH]** Free Apps Quietly Turn Smart TVs Into Web-Scraping Proxy Nodes for AI Data Collection — `2026-06-06-bright-data-sdk-smart-tv-proxy-network.md`
- [x] **[HIGH]** CISA Adds Actively Exploited SolarWinds Serv-U DoS Flaw CVE-2026-28318 to KEV Catalog — `2026-06-06-solarwinds-servu-dos-cisa-kev-cve-2026-28318.md`
- [x] **[MEDIUM]** OpenAI Rolls Out ChatGPT Lockdown Mode to Limit Prompt Injection Data Exfiltration — `2026-06-06-chatgpt-lockdown-mode-prompt-injection-defense.md`
- [x] **[MEDIUM]** Apple WWDC 2026: Siri Gets a Reboot with Apparent Gemini Integration — `2026-06-06-apple-wwdc-2026-siri-gemini-ai-update.md`
- [x] **[MEDIUM]** Trump Administration in Talks for U.S. Government Equity Stake in OpenAI — `2026-06-06-trump-administration-openai-equity-stake.md`

## Relevant (details)

### 1. Miasma Worm Compromises 73 Microsoft GitHub Repositories in Supply Chain Attack
- **Source:** The Hacker News — https://thehackernews.com/2026/06/miasma-worm-hits-73-microsoft-github.html
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `microsoft`, `malware`
- **Summary:** A self-replicating Miasma worm compromised 73 repositories across Microsoft's Azure, Azure-Samples, Microsoft, and MicrosoftDocs GitHub organizations. GitHub disabled the affected repos; pipelines consuming dependencies from these orgs should be treated as potentially compromised pending Microsoft confirmation.

### 2. Cisco SD-WAN Manager CVE-2026-20245 Under Active Exploitation — No Patch Available
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cisco-catalyst-sd-wan-manager-cve-2026.html
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `cloud-security`
- **Summary:** CVE-2026-20245 (CVSS 7.8) in Cisco Catalyst SD-WAN Manager is under active exploitation with no patch or workaround timeline published. Affects on-prem, cloud, and FedRAMP government deployments.

### 3. CVE-2026-3300: Critical Everest Forms Pro Flaw Actively Exploited for WordPress Takeover
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/critical-everest-forms-pro-flaw-exploited-to-take-over-wordpress-sites/
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `rce`, `zero-day`
- **Summary:** Hackers are actively exploiting CVE-2026-3300 in the Everest Forms Pro WordPress plugin for full unauthenticated site takeover. Patch or deactivate the plugin immediately.

### 4. AI Agent Autonomously Discovers 21 Zero-Days in FFmpeg; Chrome Ships Record 429 Patches
- **Source:** The Hacker News — https://thehackernews.com/2026/06/ai-agent-uncovers-21-zero-days-in.html
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `llm`, `cve`
- **Summary:** A security startup's autonomous AI agent found 21 unknown vulnerabilities in FFmpeg — embedded in virtually every video-handling application. Chrome 149 also shipped a record 429 bug patches, though those were human-discovered.

### 5. Free Apps Quietly Turn Smart TVs Into Web-Scraping Proxy Nodes for AI Data Collection
- **Source:** The Hacker News — https://thehackernews.com/2026/06/free-apps-are-quietly-turning-smart-tvs.html
- **Severity:** high
- **Tags:** `appsec`, `supply-chain`, `data-breach`
- **Summary:** The Bright Data SDK embedded in free consumer apps silently turns devices — including always-on smart TVs — into residential proxy exit nodes that relay AI-industry web-scraping traffic without meaningful user disclosure.

### 6. CISA Adds Actively Exploited SolarWinds Serv-U DoS Flaw CVE-2026-28318 to KEV Catalog
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cisa-adds-actively-exploited-solarwinds.html
- **Severity:** high
- **Tags:** `cve`, `vulnerability`
- **Summary:** CISA confirmed active exploitation of CVE-2026-28318 (CVSS 7.5), a DoS flaw in SolarWinds Serv-U that crashes the file-server service. Federal agencies must remediate per BOD 22-01; all Serv-U operators should patch promptly.

### 7. OpenAI Rolls Out ChatGPT Lockdown Mode to Limit Prompt Injection Data Exfiltration
- **Source:** The Hacker News — https://thehackernews.com/2026/06/new-chatgpt-lockdown-mode-limits-tools.html
- **Severity:** medium
- **Tags:** `llm`, `openai`, `ai-safety`, `appsec`
- **Summary:** ChatGPT Lockdown Mode restricts tool-use capabilities exploitable by prompt injection for data exfiltration. Available across all logged-in tiers; relevant for organizations deploying ChatGPT in sensitive workflows.

### 8. Apple WWDC 2026: Siri Gets a Reboot with Apparent Gemini Integration
- **Source:** The Verge AI — https://www.theverge.com/tech/944245/apple-wwdc-2026-ai-siri-gemini
- **Severity:** medium
- **Tags:** `ai-launch`, `llm`, `google`
- **Summary:** Apple is re-launching Siri at WWDC 2026 with apparent Google Gemini integration, extending the trend of major platforms outsourcing frontier model capabilities externally. Privacy boundaries between on-device and cloud processing are expected to be detailed at the keynote.

### 9. Trump Administration in Talks for U.S. Government Equity Stake in OpenAI
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/06/the-trump-administration-might-take-an-equity-stake-in-openai/
- **Severity:** medium
- **Tags:** `openai`, `ai-policy`
- **Summary:** President Trump signaled discussions about a U.S. government equity stake in OpenAI, citing intent for "the American people to benefit from AI success." No formal agreement exists; such an arrangement would be unprecedented for a frontier AI lab.

## Skippable

- **Sriram Krishnan leaving White House AI advisor role** — TechCrunch AI. Personnel news; context included in the OpenAI equity item.
- **Job Searcher (Hugging Face Build Hackathon)** — Hugging Face Blog. Hackathon demo app, no security or model-launch significance.
- **Mayor of Shelbyville says data center opponents live in "shitty houses"** — The Verge AI. Local data-center politics, no technical angle.
- **Meta made its own AI-generated clickbait news feed** — The Verge AI. Product feature with no security angle; editorial territory.
- **Opal Security Raises $23 Million for AI-Native Identity Governance** — SecurityWeek. Funding round, no technical findings.
- **micropython-wasm 0.1a2** — Simon Willison. Developer tooling release; no security or significant AI model significance.
