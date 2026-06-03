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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`, `wordpress`, `appsec`
- **Slug:** `2026-06-03-kirki-wordpress-cve-2026-8206-admin-takeover`
- **Must-know:** no
- **Summary:** Threat actors are actively exploiting CVE-2026-8206, a critical unauthenticated privilege escalation flaw in the widely-used Kirki Customizer Framework WordPress plugin, to take over administrator accounts. Site owners should patch or deactivate the plugin immediately.

### 2. Acer Wave 7 Mesh Routers Carry Two Max-Severity Zero-Days
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/acer-warns-of-max-severity-zero-days-affecting-wave-7-routers/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `cve`
- **Slug:** `2026-06-03-acer-wave7-router-zero-day`
- **Must-know:** no
- **Summary:** Acer disclosed two CVSS 10.0 zero-day vulnerabilities in its Wave 7 mesh router line and is developing patches. Full technical details have not been published; users should monitor Acer advisories and disable remote management interfaces as a precaution.

### 3. Trail of Bits: Malicious AI Skills Bypass Every Public Skill Scanner
- **Source:** Trail of Bits — https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `appsec`, `supply-chain`
- **Slug:** `2026-06-03-trail-of-bits-ai-skills-scanner-bypass`
- **Must-know:** no
- **Summary:** Trail of Bits researchers bypassed ClawHub's malicious skill detector, Cisco's agent skill scanner, and all three scanners integrated into skills.sh — each in under an hour — using four malicious skills that steal credentials, exfiltrate data, and hijack agents. The finding exposes AI agent skill marketplaces as an under-secured distribution vector following the same early arc as npm and PyPI.

### 4. Unpatched Windows Search URI Flaw Leaks NTLMv2 Hashes
- **Source:** The Hacker News — https://thehackernews.com/2026/06/unpatched-windows-search-uri.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `zero-day`, `microsoft`, `cve`
- **Slug:** `2026-06-03-windows-search-uri-ntlmv2-hash-leak`
- **Must-know:** no
- **Summary:** Huntress researchers disclosed an unpatched flaw in the Windows search: URI handler that can coerce NTLMv2 hash disclosure from any user who clicks a crafted link, mirroring CVE-2026-33829 in the Snipping Tool handler. Captured hashes can be cracked offline or relayed; no patch is available yet.

### 5. Global Stock Exchange Hit by Monthslong Email Compromise via LOLBins
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/global-stock-exchange-hit-monthslong-email-campaign
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`, `iam`
- **Slug:** `2026-06-03-global-stock-exchange-email-lolbins`
- **Must-know:** no
- **Summary:** A threat actor maintained persistent near-continuous access to a senior finance executive's inbox at a global stock exchange for months by leveraging native Windows LOLBins to blend with legitimate activity and evade EDR. The campaign demonstrates how credential theft plus LOL-technique persistence can sustain long-term high-value access without deploying detectable malware.

### 6. HTTP/2 Bomb: Remote DoS Hits NGINX, Apache, IIS, Envoy, and Cloudflare by Default
- **Source:** The Hacker News — https://thehackernews.com/2026/06/new-http2-bomb-vulnerability-allows.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`, `cloud-security`
- **Slug:** `2026-06-03-http2-bomb-dos-nginx-apache`
- **Must-know:** no
- **Summary:** Researchers disclosed HTTP/2 Bomb, a remote DoS technique that chains a compression bomb with a Slowloris-style hold to exhaust server resources in seconds against default-configured NGINX, Apache HTTPD, Microsoft IIS, Envoy, and Cloudflare Pingora. Notably the flaw was discovered by OpenAI Codex; organizations should apply vendor patches and harden HTTP/2 connection timeout settings immediately.

### 7. VS Code Zero-Day Lets Attackers Steal GitHub Tokens in One Click
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/vs-code-zero-day-lets-hackers-steal-github-tokens-in-one-click/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `github`, `microsoft`
- **Slug:** `2026-06-03-vscode-zero-day-github-token-theft`
- **Must-know:** no
- **Summary:** A security researcher released exploit code for an unpatched VS Code URI handler flaw that allows GitHub authentication token theft with a single click on a malicious link, requiring no extensions or elevated privileges. Stolen tokens grant full access to every repository and organization the victim can reach; no patch is available yet.

### 8. Google Adds Android Protection Against AI Deepfake Scam Calls
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/google-adds-android-protection-against-ai-deepfake-scam-calls/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `google`, `ai-safety`, `llm`, `phishing`
- **Slug:** `2026-06-03-google-android-ai-deepfake-call-detection`
- **Must-know:** no
- **Summary:** Google is rolling out an on-device Android feature that detects AI-synthesized voice cloning in real time during calls and flags suspected impersonation of contacts. The defensive capability targets a rising wave of voice-deepfake social engineering fraud; initial rollout is on recent Pixel devices.

### 9. Argamal RAT Distributed via Infected Hentai Games
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/argamal-rat-distributed-with-hentai-games/119999/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `malware`, `data-breach`
- **Slug:** `2026-06-03-argamal-rat-hentai-games`
- **Must-know:** no
- **Summary:** Kaspersky GReAT documented Argamal, a RAT bundled inside infected hentai game archives on sharing platforms that grants attackers full remote control of victim machines including keylogging, screen capture, and file exfiltration. The campaign targets credentials and banking session data and relies on functional games hiding the payload to reduce detection likelihood.

### 10. Microsoft Unveils MAI-Thinking-1 and MAI-Code-1-Flash LLMs
- **Source:** Simon Willison — https://simonwillison.net/2026/Jun/2/microsofts-new-models/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `microsoft`, `ai-launch`, `model-release`, `llm`
- **Slug:** `2026-06-03-microsoft-mai-thinking-code-models`
- **Must-know:** no
- **Summary:** Microsoft announced MAI-Thinking-1, a 1T-parameter mixture-of-experts reasoning model (35B active) available to select early partners, and MAI-Code-1-Flash, a 137B-parameter code model (5B active) rolling out now to GitHub Copilot users in VS Code. This is Microsoft's first publicly disclosed in-house LLM series separate from its OpenAI collaboration.

### 11. WeedHack Malware Campaign Infects 116,000 Minecraft Systems
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/over-116-000-minecraft-systems-infected-in-weedhack-malware-campaign/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Slug:** `2026-06-03-weedhack-minecraft-116k-infected`
- **Must-know:** no
- **Summary:** The WeedHack malware-as-a-service campaign has compromised more than 116,000 Windows systems since January 2026 by distributing trojanized Minecraft clients and mods via YouTube tutorials. The campaign grants full system control to operators and targets a demographic — gaming communities — that frequently runs with elevated privileges and minimal security tooling.

### 12. Microsoft Responds to Backlash Over Legal Threats Against Zero-Day Disclosures
- **Source:** SecurityWeek — https://www.securityweek.com/microsoft-tries-to-calm-legal-threat-fears-after-zero-day-disclosure-backlash/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `microsoft`, `zero-day`, `vulnerability`
- **Slug:** `2026-06-03-microsoft-zero-day-disclosure-legal-threat`
- **Must-know:** no
- **Summary:** Microsoft issued a public response attempting to reassure security researchers after reports that it had threatened legal action over zero-day disclosures sparked community backlash. No concrete policy change was announced; the vulnerability research community remains concerned about chilling effects on coordinated disclosure.

### 13. UK Regulator Rules Google Must Let Publishers Opt Out of AI Search
- **Source:** The Verge AI — https://www.theverge.com/tech/942302/google-search-ai-overviews-uk-cma-publisher-opt-out
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `google`, `llm`, `ai-safety`
- **Slug:** `2026-06-03-uk-cma-google-ai-search-publisher-opt-out`
- **Must-know:** no
- **Summary:** The UK CMA issued a conduct rule requiring Google to let publishers exclude their content from AI Overviews and other AI Search features without losing standard search indexing. This is the first major regulatory win for publishers contesting AI-powered scraping and is likely to be cited in EU and US proceedings.

### 14. OpenAI Upgrades GPT-5.5, Begins Retiring Legacy Models Including o3
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/artificial-intelligence/openai-upgrades-gpt-55-as-it-plans-to-retire-legacy-chatgpt-models/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `openai`, `ai-launch`, `model-release`, `llm`
- **Slug:** `2026-06-03-openai-gpt55-update-legacy-model-retirement`
- **Must-know:** no
- **Summary:** OpenAI rolled out a server-side update to GPT-5.5 Instant and announced the scheduled deprecation of several legacy models including o3 as the company consolidates around the GPT-5 generation. Developers relying on deprecated endpoints should consult the OpenAI deprecation schedule for migration timelines.

## Skippable

- **'HTTP/2 Bomb' Exploit Knocks Web Servers Offline in Seconds** — SecurityWeek. Duplicate of item 13 (The Hacker News version carries more technical detail including affected platforms and AI-discovery angle).
- **Police dismantles 9 crime groups in illegal streaming crackdown** — BleepingComputer. Law enforcement action against piracy rings; no cybersecurity technical angle for practitioners.
- **New cyber force would cost up to $11 billion to start** — The Record. Policy/budget item without technical substance or practitioner impact.
- **AI has a water problem. Google thinks it has a fix** — The Verge AI. Environmental and corporate commitments story; no security or AI-technical angle.
- **Weedhack Attacks Minecraft Users, CountLoader Hits 86K, Miners Spread via Pirated Content** — The Hacker News. Duplicate of item 21; BleepingComputer version has fuller infection count (116k systems).
- **Microsoft's Coreutils project brings Linux commands to Windows** — BleepingComputer. Developer tooling announcement with no security substance.
- **Cyera eyes $12B valuation at 80x ARR multiple despite operating losses** — TechCrunch AI. VC/financial news; no technical content.
- **Zoom CISO: AI as Security Enabler, Not Role-Replacer** — Dark Reading. CISO opinion interview; no news value.
