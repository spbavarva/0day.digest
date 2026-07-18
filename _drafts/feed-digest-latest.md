# Digest — 2026-07-18 AM

- Window: last 14h
- Raw items considered: 14
- Relevant: 6
- Skippable: 8

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[INFORMATIONAL]** Anthropic Makes Claude Fable 5 Permanent in Subscription Plans — `2026-07-18-claude-fable-5-permanent-subscriptions.md`
- [x] **[CRITICAL]** Unauthenticated RCE in WordPress Core (wp2shell) Now Has Public PoC — `2026-07-17-wordpress-wp2shell-unauthenticated-rce.md`
- [x] **[MEDIUM]** OpenSSL HollowByte Flaw Let 11-Byte Requests Exhaust Server Memory — `2026-07-17-openssl-hollowbyte-memory-dos.md`
- [x] **[CRITICAL]** Inc Ransomware Chains SonicWall SMA Zero-Days for Root Access — `2026-07-17-inc-ransomware-sonicwall-sma-zero-days.md`
- [x] **[INFORMATIONAL]** TikTok Tests Opt-In AI Likeness Detection Tool — `2026-07-17-tiktok-ai-likeness-detection.md`
- [x] **[CRITICAL]** Seven Malicious npm Packages Target Vite, Use Blockchain C2 to Deliver RAT — `2026-07-17-vite-npm-blockchain-c2-rat.md`

## Relevant (details)

### 1. Anthropic Makes Claude Fable 5 Permanent in Subscription Plans
- **Source:** Simon Willison — https://simonwillison.net/2026/Jul/18/claude-make-fable-5-permanent/#atom-everything
- **Severity:** informational
- **Tags:** `anthropic`, `llm`
- **Summary:** Anthropic reversed plans to pull Claude Fable 5 from subscription plans, keeping it in Max/Team Premium at 50% limits and offering Pro/Team Standard users a one-time $100 credit. The move follows competitive pressure from GPT-5.6 Sol and Kimi 3.

### 2. Unauthenticated RCE in WordPress Core (wp2shell) Now Has Public PoC
- **Source:** The Hacker News — https://thehackernews.com/2026/07/new-wp2shell-wordpress-core-flaw-lets.html
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`, `appsec`
- **Summary:** A core WordPress flaw (wp2shell) lets unauthenticated attackers run code via a single HTTP request on any 6.9/7.0 site, even with zero plugins. CVE IDs are now assigned and a working proof-of-concept is public.

### 3. OpenSSL HollowByte Flaw Let 11-Byte Requests Exhaust Server Memory
- **Source:** The Hacker News — https://thehackernews.com/2026/07/openssl-hollowbyte-flaw-could-freeze.html
- **Severity:** medium
- **Tags:** `vulnerability`, `appsec`
- **Summary:** Okta's Red Team disclosed a denial-of-service bug (HollowByte) where an 11-byte TLS request forces a vulnerable OpenSSL server to hold up to 131KB of memory until restart. OpenSSL quietly patched it in June with no CVE or advisory.

### 4. Inc Ransomware Chains SonicWall SMA Zero-Days for Root Access
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/inc-ransomware-exploits-sonicwall-sma-zero-days
- **Severity:** critical
- **Tags:** `ransomware`, `zero-day`, `vulnerability`, `privilege-escalation`
- **Summary:** The Inc ransomware group is chaining two zero-day vulnerabilities in SonicWall SMA appliances to gain root-level access, turning a remote-access gateway into a network foothold.

### 5. TikTok Tests Opt-In AI Likeness Detection Tool
- **Source:** The Verge — https://www.theverge.com/tech/967486/tiktok-ai-likeness-detection-tool
- **Severity:** informational
- **Tags:** `ai-safety`
- **Summary:** TikTok is testing an opt-in tool that scans for AI-generated likenesses of creators and lets them report deepfakes, currently limited to a small group of US creators. It mirrors a similar effort at YouTube.

### 6. Seven Malicious npm Packages Target Vite, Use Blockchain C2 to Deliver RAT
- **Source:** The Hacker News — https://thehackernews.com/2026/07/seven-malicious-vite-npm-packages-use.html
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`
- **Summary:** Checkmarx found seven malicious npm packages targeting the Vite ecosystem (campaign "ViteVenom"), an expansion of the ChainVeil supply chain operation using four-tier blockchain-based C2 to deliver a RAT.

## Skippable

- **nascheme/quixote** — Simon Willison. Nostalgia post about a 21-year-old Python web framework getting a commit; no AI/security substance.
- **Neil Rimer thinks the AI money is coming back out** — TechCrunch AI. VC opinion/prediction piece on AI wealth redistribution, no news substance.
- **Vertu wants executives to pay $6,880 for an AI agent** — TechCrunch AI. Product review of a luxury-phone AI agent; marketing-adjacent, no security substance.
- **Databricks hits $188B valuation** — TechCrunch AI. Funding/valuation story with no technical or security angle.
- **The Zoom hack that says, 'Don't record me'** — TechCrunch AI. Opinion piece on AI meeting-transcription fatigue, not a technical hack disclosure.
- **Abbott probes two cyber incidents amid extortion claims** — BleepingComputer. Investigation still ongoing; no confirmed technical details, TTPs, or IOCs yet.
- **Agility Robotics plants its flag in Tesla's backyard** — TechCrunch AI. New robotics training center; no security or model-launch substance.
- **AI-driven memory crunch jolts India's smartphone market** — TechCrunch AI. Market/economics analysis piece, no security or technical AI substance.
