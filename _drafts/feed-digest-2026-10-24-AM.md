# Digest — 2026-10-24 AM

- Window: last 14h
- Raw items considered: 7
- Relevant: 5
- Skippable: 2

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Leaked LiteLLM Master Key Let Attackers Steal GitHub Tokens, Hijack Release Pipeline — `2026-10-24-litellm-leaked-master-key-github-token-theft.md`
- [x] **[CRITICAL]** CISA Adds Actively Exploited Collabora Online and Arista VeloCloud Flaws to KEV — `2026-10-24-cisa-kev-collabora-arista-velocloud-cve-2026-110447.md`
- [x] **[HIGH]** Brotli Decoder Flaw (CVE-2026-111497) Also Hits Bun, Python, and Envoy Beyond Node.js — `2026-10-24-brotli-decoder-flaw-nodejs-rce-cve-2026-111497.md`
- [x] **[MEDIUM]** Security Firm Pushed 2M+ Remote Updates to Kill a Potential Popcorn Time Botnet — `2026-10-24-popcorn-time-updater-botnet-takedown.md`
- [x] **[INFORMATIONAL]** OpenAI Says It Will Stop Training Models on the Live Internet — `2026-10-23-openai-stops-training-on-live-internet.md`

## Relevant (details)

### 1. Leaked LiteLLM Master Key Let Attackers Steal GitHub Tokens and Hijack Release Pipeline
- **Source:** The Hacker News — https://thehackernews.com/2026/10/leaked-litellm-master-key-let-attackers.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `pypi`, `github`, `llm`
- **Slug:** `litellm-leaked-master-key-github-token-theft`
- **Must-know:** yes
- **Summary:** A master key accidentally committed to a public LiteLLM-Labs GitHub repo in May 2026 let an attacker steal GitHub tokens and push a malicious version of the popular LiteLLM Python package. This is a supply chain compromise of a widely-used LLM gateway tool via a leaked credential.

### 2. CISA Flags Two Actively Exploited Critical Flaws in Collabora Online and Arista VeloCloud
- **Source:** The Hacker News — https://thehackernews.com/2026/10/cisa-flags-two-actively-exploited.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `vulnerability`
- **Slug:** `cisa-kev-collabora-arista-velocloud-cve-2026-110447`
- **Must-know:** yes
- **Summary:** CISA added critical flaws in Collabora Online Built-in CODE Server and Arista VeloCloud Orchestrator to its KEV catalog, citing active exploitation. One flaw, CVE-2026-110447, carries a CVSS score of 9.2.

### 3. Brotli Decoder Flaw Behind Node.js RCE Also Affects Bun, Python and Other Widely Used Software
- **Source:** The Hacker News — https://thehackernews.com/2026/10/brotli-decoder-flaw-behind-nodejs-rce.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `rce`, `vulnerability`, `pypi`
- **Slug:** `brotli-decoder-flaw-nodejs-rce-cve-2026-111497`
- **Must-know:** no
- **Summary:** A memory-corruption flaw in Google's Brotli decoder (CVE-2026-111497) affects Node.js, Bun, Python's brotli/brotlicffi packages, and Envoy proxies that decompress Brotli data. Crafted input can corrupt program memory, with RCE potential in at least one affected runtime.

### 4. Researchers Push Over 2 Million Updates to Remotely Disable Popcorn Time Updater That Could Fuel a Botnet
- **Source:** The Hacker News — https://thehackernews.com/2026/10/researchers-push-over-2-million-updates.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `vulnerability`
- **Slug:** `popcorn-time-updater-botnet-takedown`
- **Must-know:** no
- **Summary:** Dutch firm Eye Security pushed over 2 million remote updates between November 2025 and March 2026 to disable an abandoned Popcorn Time fork's updater, which it said could have let an outsider take over affected machines and build a botnet.

### 5. OpenAI says it will no longer train its AI models on the live internet, citing "significant risks"
- **Source:** TechCrunch AI — https://techcrunch.com/2026/10/23/openai-says-it-will-no-longer-train-its-ai-models-on-the-live-internet-citing-significant-risks/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-safety`, `openai`, `llm`
- **Slug:** `openai-stops-training-on-live-internet`
- **Must-know:** no
- **Summary:** OpenAI said it will cut frontier models off from training on the live internet, citing significant risks. The move follows internal disagreement, after an OpenAI engineer reportedly said that approach wouldn't work.

## Skippable

- **Google Says Gmail and Photos Data Shared With AI Search Could Be Used for Targeted Ads** — The Hacker News. Privacy policy clarification about ad targeting; no technical security or AI safety substance.
- **Hottest toy for Christmas? Nvidia CEO plays with adorable Microduck robots, 20,000 sell** — TechCrunch AI. Consumer product marketing piece, no security or substantive AI relevance.
