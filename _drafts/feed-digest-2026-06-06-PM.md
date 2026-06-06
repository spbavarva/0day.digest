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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `microsoft`, `malware`
- **Slug:** `2026-06-06-miasma-worm-microsoft-github-supply-chain`
- **Must-know:** yes
- **Summary:** A self-replicating Miasma worm hit 73 Microsoft GitHub repositories across Azure, Azure-Samples, Microsoft, and MicrosoftDocs organizations. GitHub disabled the affected repos; any pipeline consuming dependencies from these organizations should be treated as potentially compromised.

### 2. Cisco SD-WAN Manager CVE-2026-20245 Under Active Exploitation — No Patch Available
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cisco-catalyst-sd-wan-manager-cve-2026.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `cloud-security`
- **Slug:** `2026-06-06-cisco-sdwan-cve-2026-20245-no-patch-active-exploit`
- **Must-know:** yes
- **Summary:** Cisco confirmed CVE-2026-20245 (CVSS 7.8) in Catalyst SD-WAN Manager is under active exploitation with no patch or workaround timeline published. Affects on-prem, cloud, and FedRAMP deployments.

### 3. CVE-2026-3300: Critical Everest Forms Pro Flaw Actively Exploited for WordPress Takeover
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/critical-everest-forms-pro-flaw-exploited-to-take-over-wordpress-sites/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `rce`, `zero-day`
- **Slug:** `2026-06-06-everest-forms-pro-cve-2026-3300-wordpress-exploit`
- **Must-know:** yes
- **Summary:** Hackers are actively exploiting CVE-2026-3300 in the Everest Forms Pro WordPress plugin for complete site takeover. The flaw is unauthenticated; site owners should patch or deactivate immediately.

### 4. AI Agent Autonomously Discovers 21 Zero-Days in FFmpeg; Chrome Ships Record 429 Patches
- **Source:** The Hacker News — https://thehackernews.com/2026/06/ai-agent-uncovers-21-zero-days-in.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `llm`, `cve`
- **Slug:** `2026-06-06-ai-agent-ffmpeg-21-zero-days-chrome-429-patches`
- **Must-know:** no
- **Summary:** An autonomous AI agent from a security startup found 21 unknown vulnerabilities in FFmpeg, which ships in virtually every video-handling application. Separately, Chrome 149 patched a record 429 bugs — highlighting both the scale of browser attack surface and AI's growing role in offensive vulnerability research.

### 5. Free Apps Quietly Turn Smart TVs Into Web-Scraping Proxy Nodes for AI Data Collection
- **Source:** The Hacker News — https://thehackernews.com/2026/06/free-apps-are-quietly-turning-smart-tvs.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `appsec`, `supply-chain`, `data-breach`
- **Slug:** `2026-06-06-bright-data-sdk-smart-tv-proxy-network`
- **Must-know:** no
- **Summary:** A researcher documented how the Bright Data SDK, embedded in free consumer apps including smart TV apps, silently turns devices into residential proxy exit nodes that relay web-scraping traffic sold to AI companies. Users have no meaningful disclosure of this role.

### 6. CISA Adds Actively Exploited SolarWinds Serv-U DoS Flaw CVE-2026-28318 to KEV Catalog
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cisa-adds-actively-exploited-solarwinds.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`
- **Slug:** `2026-06-06-solarwinds-servu-dos-cisa-kev-cve-2026-28318`
- **Must-know:** no
- **Summary:** CISA confirmed in-the-wild exploitation of CVE-2026-28318 (CVSS 7.5) in SolarWinds Serv-U, a DoS flaw that crashes the file-server service. Federal agencies must remediate per BOD 22-01; all Serv-U operators should patch promptly.

### 7. OpenAI Rolls Out ChatGPT Lockdown Mode to Limit Prompt Injection Data Exfiltration
- **Source:** The Hacker News — https://thehackernews.com/2026/06/new-chatgpt-lockdown-mode-limits-tools.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `llm`, `openai`, `ai-safety`, `appsec`
- **Slug:** `2026-06-06-chatgpt-lockdown-mode-prompt-injection-defense`
- **Must-know:** no
- **Summary:** OpenAI's new ChatGPT Lockdown Mode restricts tool-use capabilities that prompt injection attacks could exploit to exfiltrate data. Available to all tier levels for logged-in users; useful for organizations handling sensitive data via ChatGPT.

### 8. Apple WWDC 2026: Siri Gets a Reboot with Apparent Gemini Integration
- **Source:** The Verge AI — https://www.theverge.com/tech/944245/apple-wwdc-2026-ai-siri-gemini
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-launch`, `llm`, `google`
- **Slug:** `2026-06-06-apple-wwdc-2026-siri-gemini-ai-update`
- **Must-know:** no
- **Summary:** Apple is announcing an updated Siri at WWDC 2026 with apparent Google Gemini integration, continuing a pattern of major device platforms outsourcing frontier model capabilities to AI labs. Privacy details — particularly on-device vs. cloud processing boundaries — are expected at the keynote.

### 9. Trump Administration in Talks for U.S. Government Equity Stake in OpenAI
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/06/the-trump-administration-might-take-an-equity-stake-in-openai/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `openai`, `ai-policy`
- **Slug:** `2026-06-06-trump-administration-openai-equity-stake`
- **Must-know:** no
- **Summary:** President Trump said he's in discussions about deals "where the American people can benefit from the success of AI," signaling a possible government equity stake in OpenAI. No formal agreement exists; such an arrangement would mark unprecedented government entanglement with a frontier AI lab.

## Skippable

- **Sriram Krishnan leaving White House AI advisor role** — TechCrunch AI. Policy personnel news; context folded into the OpenAI equity post above.
- **Job Searcher (Hugging Face Build Hackathon)** — Hugging Face Blog. Hackathon project demo, no security or model-launch significance.
- **Mayor of Shelbyville says opponents live in "shitty houses"** — The Verge AI. Local data-center NIMBY politics, no security or AI technical angle.
- **Meta made its own AI-generated clickbait news feed** — The Verge AI. Product feature critique; no security angle, editorial territory.
- **Opal Security Raises $23 Million for AI-Native Identity Governance** — SecurityWeek. Funding news with no technical findings.
- **micropython-wasm 0.1a2** — Simon Willison. Developer tooling library release; interesting but no security or significant AI model significance for this digest window.
