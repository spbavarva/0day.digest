# Digest — 2026-06-03 AM

- Window: last 14h
- Raw items considered: 22
- Relevant: 14
- Skippable: 8

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Kirki WordPress Plugin CVE-2026-8206 Actively Exploited to Hijack Admin Accounts — `2026-06-03-kirki-wordpress-cve-2026-8206-admin-takeover.md`
- [x] **[HIGH]** Acer Wave 7 Mesh Routers Carry Two Max-Severity Zero-Days — `2026-06-03-acer-wave7-router-zero-day.md`
- [x] **[HIGH]** Trail of Bits: Malicious AI Skills Bypass Every Public Skill Scanner — `2026-06-03-trail-of-bits-ai-skills-scanner-bypass.md`
- [x] **[HIGH]** Unpatched Windows Search URI Flaw Leaks NTLMv2 Hashes — `2026-06-03-windows-search-uri-ntlmv2-hash-leak.md`
- [x] **[HIGH]** Global Stock Exchange Hit by Monthslong Email Compromise via LOLBins — `2026-06-03-global-stock-exchange-email-lolbins.md`
- [x] **[HIGH]** HTTP/2 Bomb: Remote DoS Hits NGINX, Apache, IIS, Envoy, and Cloudflare by Default — `2026-06-03-http2-bomb-dos-nginx-apache.md`
- [x] **[HIGH]** VS Code Zero-Day Lets Attackers Steal GitHub Tokens in One Click — `2026-06-03-vscode-zero-day-github-token-theft.md`
- [x] **[MEDIUM]** Google Adds Android Protection Against AI Deepfake Scam Calls — `2026-06-03-google-android-ai-deepfake-call-detection.md`
- [x] **[MEDIUM]** Argamal RAT Distributed via Infected Hentai Games — `2026-06-03-argamal-rat-hentai-games.md`
- [x] **[MEDIUM]** Microsoft Unveils MAI-Thinking-1 and MAI-Code-1-Flash LLMs — `2026-06-03-microsoft-mai-thinking-code-models.md`
- [x] **[MEDIUM]** WeedHack Malware Campaign Infects 116,000 Minecraft Systems — `2026-06-03-weedhack-minecraft-116k-infected.md`
- [x] **[INFORMATIONAL]** Microsoft Responds to Backlash Over Legal Threats Against Zero-Day Disclosures — `2026-06-03-microsoft-zero-day-disclosure-legal-threat.md`
- [x] **[INFORMATIONAL]** UK Regulator Rules Google Must Let Publishers Opt Out of AI Search — `2026-06-03-uk-cma-google-ai-search-publisher-opt-out.md`
- [x] **[INFORMATIONAL]** OpenAI Upgrades GPT-5.5, Begins Retiring Legacy Models Including o3 — `2026-06-03-openai-gpt55-update-legacy-model-retirement.md`

## Relevant (details)

### 1. Kirki WordPress Plugin CVE-2026-8206 Actively Exploited to Hijack Admin Accounts
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/critical-kirki-flaw-exploited-to-hijack-wordpress-admin-accounts/
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`, `wordpress`, `appsec`
- **Summary:** Threat actors are actively exploiting CVE-2026-8206, a critical unauthenticated privilege escalation flaw in the widely-used Kirki Customizer Framework WordPress plugin, to take over administrator accounts. Site owners should patch or deactivate the plugin immediately.

### 2. Acer Wave 7 Mesh Routers Carry Two Max-Severity Zero-Days
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/acer-warns-of-max-severity-zero-days-affecting-wave-7-routers/
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `cve`
- **Summary:** Acer disclosed two CVSS 10.0 zero-day vulnerabilities in its Wave 7 mesh router line and is developing patches. Users should monitor Acer advisories and consider disabling remote management interfaces as a precaution.

### 3. Trail of Bits: Malicious AI Skills Bypass Every Public Skill Scanner
- **Source:** Trail of Bits — https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `appsec`, `supply-chain`
- **Summary:** Trail of Bits bypassed ClawHub's detector, Cisco's scanner, and all three skills.sh scanners — each in under an hour — using four malicious skills that steal credentials, exfiltrate data, and hijack agents. AI agent skill marketplaces are exposed as an under-secured distribution vector.

### 4. Unpatched Windows Search URI Flaw Leaks NTLMv2 Hashes
- **Source:** The Hacker News — https://thehackernews.com/2026/06/unpatched-windows-search-uri.html
- **Severity:** high
- **Tags:** `vulnerability`, `zero-day`, `microsoft`, `cve`
- **Summary:** Huntress researchers disclosed an unpatched flaw in the Windows search: URI handler that leaks NTLMv2 hashes via a single crafted link, mirroring CVE-2026-33829. Hashes can be cracked offline or relayed; no patch is available yet.

### 5. Global Stock Exchange Hit by Monthslong Email Compromise via LOLBins
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/global-stock-exchange-hit-monthslong-email-campaign
- **Severity:** high
- **Tags:** `malware`, `phishing`, `iam`
- **Summary:** A threat actor maintained near-continuous access to a senior finance executive's inbox at a global stock exchange for months using native Windows LOLBins for stealth. The campaign demonstrates sustained high-value access without detectable malware deployment.

### 6. HTTP/2 Bomb: Remote DoS Hits NGINX, Apache, IIS, Envoy, and Cloudflare by Default
- **Source:** The Hacker News — https://thehackernews.com/2026/06/new-http2-bomb-vulnerability-allows.html
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`, `cloud-security`
- **Summary:** HTTP/2 Bomb chains a compression bomb with a Slowloris-style hold to exhaust resources in seconds on default-configured NGINX, Apache, IIS, Envoy, and Cloudflare Pingora. The flaw was discovered by OpenAI Codex; organizations should apply vendor patches and harden HTTP/2 timeout settings.

### 7. VS Code Zero-Day Lets Attackers Steal GitHub Tokens in One Click
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/vs-code-zero-day-lets-hackers-steal-github-tokens-in-one-click/
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `github`, `microsoft`
- **Summary:** A researcher released exploit code for an unpatched VS Code URI handler flaw enabling GitHub token theft via a single malicious link click, requiring no extensions. Stolen tokens grant full repository and organization access; no patch exists yet.

### 8. Google Adds Android Protection Against AI Deepfake Scam Calls
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/google-adds-android-protection-against-ai-deepfake-scam-calls/
- **Severity:** medium
- **Tags:** `google`, `ai-safety`, `llm`, `phishing`
- **Summary:** Google's new on-device Android feature detects AI-synthesized voice impersonation of contacts in real time during calls. Initial rollout targets recent Pixel devices; broader availability is expected later in 2026.

### 9. Argamal RAT Distributed via Infected Hentai Games
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/argamal-rat-distributed-with-hentai-games/119999/
- **Severity:** medium
- **Tags:** `malware`, `data-breach`
- **Summary:** Kaspersky GReAT documented Argamal, a RAT bundled inside functional hentai game archives that provides attackers full remote control including keylogging, screen capture, and credential theft. The campaign targets banking session data and exploits piracy distribution channels.

### 10. Microsoft Unveils MAI-Thinking-1 and MAI-Code-1-Flash LLMs
- **Source:** Simon Willison — https://simonwillison.net/2026/Jun/2/microsofts-new-models/#atom-everything
- **Severity:** medium
- **Tags:** `microsoft`, `ai-launch`, `model-release`, `llm`
- **Summary:** Microsoft announced MAI-Thinking-1 (1T-param MoE reasoning model, 35B active) and MAI-Code-1-Flash (137B, 5B active, for GitHub Copilot) at Build 2026. This is Microsoft's first disclosed in-house LLM series separate from OpenAI.

### 11. WeedHack Malware Campaign Infects 116,000 Minecraft Systems
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/over-116-000-minecraft-systems-infected-in-weedhack-malware-campaign/
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Summary:** WeedHack MaaS has compromised 116,000+ Windows systems since January 2026 via trojanized Minecraft mods distributed through YouTube tutorials. The campaign grants full system control and targets a demographic with elevated privileges and minimal security tooling.

### 12. Microsoft Responds to Backlash Over Legal Threats Against Zero-Day Disclosures
- **Source:** SecurityWeek — https://www.securityweek.com/microsoft-tries-to-calm-legal-threat-fears-after-zero-day-disclosure-backlash/
- **Severity:** informational
- **Tags:** `microsoft`, `zero-day`, `vulnerability`
- **Summary:** Microsoft issued a public response to researcher backlash after reports of legal threats over zero-day disclosures. No concrete policy change was announced; the research community remains concerned about chilling effects on coordinated disclosure.

### 13. UK Regulator Rules Google Must Let Publishers Opt Out of AI Search
- **Source:** The Verge AI — https://www.theverge.com/tech/942302/google-search-ai-overviews-uk-cma-publisher-opt-out
- **Severity:** informational
- **Tags:** `google`, `llm`, `ai-safety`
- **Summary:** The UK CMA issued a conduct rule requiring Google to allow publishers to exclude content from AI Overviews without losing standard search indexing. This is the first major regulatory win for publishers contesting AI-powered scraping.

### 14. OpenAI Upgrades GPT-5.5, Begins Retiring Legacy Models Including o3
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/artificial-intelligence/openai-upgrades-gpt-55-as-it-plans-to-retire-legacy-chatgpt-models/
- **Severity:** informational
- **Tags:** `openai`, `ai-launch`, `model-release`, `llm`
- **Summary:** OpenAI rolled out a server-side update to GPT-5.5 Instant and announced deprecation of legacy models including o3. Developers should consult the OpenAI deprecation schedule for migration timelines.

## Skippable

- **'HTTP/2 Bomb' Exploit Knocks Web Servers Offline in Seconds** — SecurityWeek. Duplicate of item 6; The Hacker News version carries more technical detail.
- **Police dismantles 9 crime groups in illegal streaming crackdown** — BleepingComputer. Law enforcement piracy action; no technical security angle for practitioners.
- **New cyber force would cost up to $11 billion to start** — The Record. Policy/budget item without technical substance or practitioner impact.
- **AI has a water problem. Google thinks it has a fix** — The Verge AI. Environmental commitments story; no security or AI-technical angle.
- **Weedhack Attacks Minecraft Users, CountLoader Hits 86K, Miners Spread via Pirated Content** — The Hacker News. Duplicate of WeedHack item; BleepingComputer version has fuller figures (116k systems).
- **Microsoft's Coreutils project brings Linux commands to Windows** — BleepingComputer. Developer tooling announcement; no security substance.
- **Cyera eyes $12B valuation at 80x ARR multiple despite operating losses** — TechCrunch AI. VC/financial news; no technical content.
- **Zoom CISO: AI as Security Enabler, Not Role-Replacer** — Dark Reading. CISO opinion interview; no news value.
