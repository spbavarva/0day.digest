# Digest — 2026-04-13 PM

- Window: last 14h
- Raw items considered: 12
- Relevant: 4
- Skippable: 8

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Fake Claude Website Distributes PlugX RAT — `2026-04-13-fake-claude-plugx-rat.md`
- [x] **[HIGH]** North Korea's APT37 Weaponizes Facebook Friendships to Deliver RokRAT — `2026-04-13-apt37-facebook-rokrat.md`
- [x] **[HIGH]** OpenAI Revokes macOS App Certificate After Axios Supply Chain Compromise — `2026-04-13-openai-macos-cert-axios-supply-chain.md`
- [x] **[MEDIUM]** JanelaRAT Financial Malware Campaign Updated, Targeting Latin America — `2026-04-13-janelarat-financial-malware-latam.md`

## Relevant (details)

### 1. Fake Claude Website Distributes PlugX RAT
- **Source:** SecurityWeek — https://www.securityweek.com/fake-claude-website-distributes-plugx-rat/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `anthropic`, `phishing`
- **Slug:** `fake-claude-plugx-rat`
- **Must-know:** no
- **Summary:** Threat actors built a fake Anthropic/Claude installer site to deliver PlugX RAT via DLL sideloading. The malware cleans up after itself to hinder detection and forensics, and exploits AI tool popularity as a social engineering lure.

### 2. North Korea's APT37 Weaponizes Facebook Friendships to Deliver RokRAT
- **Source:** The Hacker News — https://thehackernews.com/2026/04/north-koreas-apt37-uses-facebook-social.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`, `apt`
- **Slug:** `apt37-facebook-rokrat`
- **Must-know:** no
- **Summary:** APT37 (ScarCruft) friended targets on Facebook over time before pivoting to RokRAT delivery — routing the trust-building phase through a legitimate social platform to bypass network controls. Targets in policy, defense, and journalism are the typical focus.

### 3. OpenAI Revokes macOS App Certificate After Axios Supply Chain Compromise
- **Source:** The Hacker News — https://thehackernews.com/2026/04/openai-revokes-macos-app-certificate.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `openai`, `github`, `malware`
- **Slug:** `openai-macos-cert-axios-supply-chain`
- **Must-know:** no
- **Summary:** OpenAI's GitHub Actions signing workflow pulled a malicious Axios library on March 31; the company revoked the affected code-signing certificate and reports no user data was compromised. A follow-up to the broader Axios supply chain compromise first reported in early April.

### 4. JanelaRAT Financial Malware Campaign Updated, Targeting Latin America
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/janelarat-financial-threat-in-latin-america/119332/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `janelarat-financial-malware-latam`
- **Must-know:** no
- **Summary:** Kaspersky GReAT published a technical analysis of an updated JanelaRAT campaign targeting financial sector users in Latin America, including infection chain details and updated evasion techniques. Report includes IOCs for defender use.

## Skippable

- **International Operation Targets Multimillion-Dollar Crypto Theft Schemes** — SecurityWeek. Law enforcement announcement (US/UK/Canada froze $12M crypto); no attacker TTPs or technical detail.
- **CPUID Hacked to Serve Trojanized CPU-Z and HWMonitor Downloads** — SecurityWeek. Already published 2026-04-10 as `2026-04-10-cpuid-supply-chain-cpu-z-hwmonitor.md`; duplicate coverage.
- **Sam Altman reportedly targeted in second attack** — The Verge AI. Physical security incident (shooting at residence); outside scope of cyber/AI technical content.
- **Gmail Brings End-to-End Encryption to Android and iOS for Enterprise Users** — SecurityWeek. Already published 2026-04-10 as `2026-04-10-gmail-e2ee-mobile-rollout.md`; duplicate coverage.
- **The largest orbital compute cluster is open for business** — TechCrunch AI. Space-based GPU compute announcement (Kepler Communications); no security or AI model launch angle.
- **Quoting Bryan Cantrill** — Simon Willison. Opinion commentary on LLM laziness as a design concern; no news value.
- **Gemma 4 audio with MLX** — Simon Willison. Tutorial on audio transcription with Gemma 4 on macOS; not a news item.
- **Hack at Dutch gym chain Basic-Fit exposes customer data in several EU countries** — The Record. Generic breach disclosure with no technical substance or attacker TTPs.
