# Digest — 2026-07-06 AM

- Window: last 14h
- Raw items considered: 10
- Relevant: 6
- Skippable: 4

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Prompt Injection Attacks Trick AI Agents Into Making Crypto Payments — `2026-07-06-prompt-injection-ai-agents-crypto-payments.md`
- [x] **[MEDIUM]** Device Code Phishing Attack Abuses a Microsoft Sign-In Page — `2026-07-06-device-code-phishing-microsoft.md`
- [x] **[MEDIUM]** New TrojPix Attack Leaks Data From Air-Gapped Systems via Video Cable Emissions — `2026-07-06-trojpix-air-gap-video-cable-exfiltration.md`
- [x] **[MEDIUM]** New Java-Based QuimaRAT MaaS Built to Run on Windows, Linux, and macOS — `2026-07-06-quimarat-java-cross-platform-rat.md`
- [x] **[HIGH]** Opera GX Flaw Let Malicious Sites Auto-Install Mods to Steal Data From Visited Pages — `2026-07-06-opera-gx-flaw-auto-install-malicious-mods.md`
- [x] **[MEDIUM]** SkillCloak Lets Malicious AI Agent Skills Evade Static Scanners — `2026-07-06-skillcloak-ai-agent-skill-evasion.md`

## Relevant (details)

### 1. Prompt Injection Attacks Trick AI Agents Into Making Crypto Payments
- **Source:** SecurityWeek — https://www.securityweek.com/prompt-injection-attacks-trick-ai-agents-into-making-crypto-payments/
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `prompt-injection`
- **Summary:** Two campaigns embed indirect prompt injections in malicious websites to redirect autonomous, browsing-capable AI agents into authorizing crypto payments. A concrete case of prompt injection causing direct financial loss rather than just policy bypass.

### 2. Device Code Phishing Attack Abuses a Microsoft Sign-In Page
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/microsoft-device-code-phishing-attack/120350/
- **Severity:** medium
- **Tags:** `phishing`, `microsoft`
- **Summary:** The OAuth 2.0 Device Authorization Grant flow, meant for TVs/IoT/printers, is being abused in a phishing campaign that spoofs a Microsoft sign-in page to harvest session tokens. Sidesteps "check the URL" guidance since the phishing page can look legitimate.

### 3. New TrojPix Attack Leaks Data From Air-Gapped Systems via Video Cable Emissions
- **Source:** The Hacker News — https://thehackernews.com/2026/07/new-trojpix-attack-leaks-data-from-air.html
- **Severity:** medium
- **Tags:** `malware`, `vulnerability`
- **Summary:** Shandong University researchers show TrojPix, which tweaks on-screen pixels so the video cable's electromagnetic emissions radiate a decodable signal to a nearby receiver. Requires malware already on the target machine; it's a post-compromise exfiltration channel.

### 4. New Java-Based QuimaRAT MaaS Built to Run on Windows, Linux, and macOS
- **Source:** The Hacker News — https://thehackernews.com/2026/07/new-java-based-quimarat-maas-built-to.html
- **Severity:** medium
- **Tags:** `malware`, `rce`
- **Summary:** LevelBlue flagged QuimaRAT, a cross-platform Java-based RAT sold as malware-as-a-service for $150/month to $1,200 lifetime. Lowers the bar for running persistent remote access campaigns across mixed-OS environments.

### 5. Opera GX Flaw Let Malicious Sites Auto-Install Mods to Steal Data From Visited Pages
- **Source:** The Hacker News — https://thehackernews.com/2026/07/opera-gx-flaw-let-malicious-sites-auto.html
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`
- **Summary:** A flaw in Opera GX let a malicious site silently install a browser add-on that reads data from later-visited pages with no click. Researchers reconstructed a signed-in user's Gmail address from a single visit; Opera has patched it.

### 6. SkillCloak Lets Malicious AI Agent Skills Evade Static Scanners
- **Source:** The Hacker News — https://thehackernews.com/2026/07/new-skillcloak-technique-lets-malicious.html
- **Severity:** medium
- **Tags:** `llm`, `ai-safety`, `supply-chain`
- **Summary:** HKUST researchers show self-extracting packing tricks evade static scanners for malicious AI coding-agent "skills" over 90% of the time while keeping the malware functional. A supply-chain-style risk for AI agent skill marketplaces; the team's own runtime checker catches most packed variants.

## Skippable

- **LeRobot v0.6.0: Imagine, Evaluate, Improve** — Hugging Face Blog. No summary text provided in the feed; title suggests a routine robotics-framework version release with no security angle.
- **sqlite-utils 4.0rc3** — Simon Willison. Developer tool release note, no security or AI-safety substance.
- **🤗 Kernels: Major Updates** — Hugging Face Blog. No summary text provided in the feed; generic infra/tooling update with no security angle.
- **Some of the nation's rich are letting AI teach their kids** — The Verge AI. Opinion/lifestyle piece on AI in education, no security or technical news value.
