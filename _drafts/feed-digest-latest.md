# Digest — 2026-09-18 AM

- Window: last 14h
- Raw items considered: 24
- Relevant: 11
- Skippable: 13

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** 23 Million User Records Compromised in Gyazo Data Breach — `2026-09-18-gyazo-data-breach-23-million-records.md`
- [x] **[INFORMATIONAL]** Trail of Bits: Using AI to Build Custom Tooling Before Code Review Begins — `2026-09-18-trail-of-bits-ai-security-audits.md`
- [x] **[HIGH]** WeaselBiscuit Stealer Spreads via 13 npm Packages to Harvest Chrome Extension Storage — `2026-09-18-weaselbiscuit-npm-stealer-chrome-extensions.md`
- [x] **[HIGH]** Prompt Injection in AWS AgentCore Harness Can Exfiltrate Credentials — `2026-09-18-agentcore-harness-prompt-injection-credential-theft.md`
- [x] **[CRITICAL]** Brevo Supply Chain Attack Injects Malware Into 100,000 Websites — `2026-09-18-brevo-supply-chain-attack-100k-websites.md`
- [x] **[HIGH]** New Check Point Flaw Lets Hackers Execute Code With Root Privileges — `2026-09-18-check-point-critical-rce-root-flaw.md`
- [x] **[HIGH]** Claimed Bug Bounty Hunter Likely Used LLM to Build PhantomRaven npm Stealer — `2026-09-18-phantomraven-npm-stealer-llm-built.md`
- [x] **[CRITICAL]** Critical Orkes Conductor Vulnerability Exploited in Attacks — `2026-09-18-orkes-conductor-rce-exploited-in-attacks.md`
- [x] **[MEDIUM]** AI Agent Breaches Spanish Organization, Modifies Personal Data — `2026-09-18-ai-agent-breaches-spanish-organization.md`
- [x] **[HIGH]** RatHat Android Malware Abuses ADB to Retain Shell Access After Uninstall — `2026-09-18-rathat-android-malware-ai-powered.md`
- [x] **[HIGH]** Targeted Attacks on Prominent Rustaceans Aim to Compromise crates.io Publishers — `2026-09-17-targeted-attacks-on-rust-crates-maintainers.md`

## Relevant (details)

### 1. 23 Million User Records Compromised in Gyazo Data Breach
- **Source:** SecurityWeek — https://www.securityweek.com/23-million-user-records-compromised-in-gyazo-data-breach/
- **Severity:** critical
- **Tags:** `data-breach`, `vulnerability`
- **Summary:** Helpfeel, maker of Gyazo, disclosed that an attacker exploited a vulnerability in its image upload server, affecting roughly 23 million user records.

### 2. Trail of Bits: Using AI to Build Custom Tooling Before Code Review Begins
- **Source:** Trail of Bits — https://blog.trailofbits.com/2026/09/18/auditing-in-the-age-of-good-enough-ai/
- **Severity:** informational
- **Tags:** `llm`, `appsec`
- **Summary:** Trail of Bits describes using AI agents to build custom tooling and formal models before code review starts, applied to an audit of the Miden zero-knowledge VM.

### 3. WeaselBiscuit Stealer Spreads via 13 npm Packages to Harvest Chrome Extension Storage
- **Source:** The Hacker News — https://thehackernews.com/2026/09/weaselbiscuit-stealer-spreads-via-13.html
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `malware`
- **Summary:** 13 npm packages were found delivering a new stealer, WeaselBiscuit, that harvests Chrome extension storage and overlaps with a DPRK-linked malware strain.

### 4. Prompt Injection in AWS AgentCore Harness Can Exfiltrate Credentials
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/securing-aws-agentcore-harness-credentials/
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `aws`
- **Summary:** Default configurations in AWS AgentCore Harness allow prompt injection attacks to exfiltrate credentials from AI agent deployments.

### 5. Brevo Supply Chain Attack Injects Malware Into 100,000 Websites
- **Source:** SecurityWeek — https://www.securityweek.com/brevo-supply-chain-attack-injects-malware-into-100000-websites/
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`
- **Summary:** A compromised Brevo API key was used to deploy a malicious Cloudflare Worker that injected malware into roughly 100,000 websites.

### 6. New Check Point Flaw Lets Hackers Execute Code With Root Privileges
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/check-point-warns-critical-flaw-lets-hackers-execute-code-as-root/
- **Severity:** high
- **Tags:** `rce`, `privilege-escalation`
- **Summary:** Check Point released updates for a critical vulnerability allowing root-level code execution on management systems.

### 7. Claimed Bug Bounty Hunter Likely Used LLM to Build PhantomRaven npm Stealer
- **Source:** The Hacker News — https://thehackernews.com/2026/09/claimed-bug-bounty-hunter-likely-used.html
- **Severity:** high
- **Tags:** `llm`, `npm`, `malware`
- **Summary:** A financially motivated actor distributed the PhantomRaven JS stealer via npm; researchers assess with high confidence it was LLM-written.

### 8. Critical Orkes Conductor Vulnerability Exploited in Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/critical-orkes-conductor-vulnerability-exploited-in-attacks/
- **Severity:** critical
- **Tags:** `rce`, `cve`
- **Summary:** CVE-2026-58138, an unauthenticated RCE in Orkes Conductor exploitable via inline workflow definitions, is being actively exploited.

### 9. AI Agent Breaches Spanish Organization, Modifies Personal Data
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/ai-agent-breaches-spanish-organization-personal-data
- **Severity:** medium
- **Tags:** `ai-safety`, `data-breach`
- **Summary:** An AI agent was reportedly used to breach a Spanish organization and modify personal data; source detail is limited.

### 10. RatHat Android Malware Abuses ADB to Retain Shell Access After Uninstall
- **Source:** The Hacker News — https://thehackernews.com/2026/09/rathat-android-malware-abuses-adb-to.html
- **Severity:** high
- **Tags:** `malware`, `android`
- **Summary:** RatHat, a new China-linked Android malware family, abuses ADB to retain shell access post-uninstall and uses AI to navigate compromised devices.

### 11. Targeted Attacks on Prominent Rustaceans Aim to Compromise crates.io Publishers
- **Source:** Simon Willison — https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/
- **Severity:** high
- **Tags:** `supply-chain`, `phishing`
- **Summary:** The crates.io security team warns of a campaign using fake video-call pretexts to compromise rust-lang members and popular crate owners.

## Skippable

- **[Virtual Event] Cybersecurity Outlook 2027** — Dark Reading. Event promo, no news value.
- **Flash floods can strike without warning — this new technology could change that** — The Verge AI. Generic AI application story, no security angle.
- **Microsoft Patches 18 Vulnerabilities in AI, Cloud Products** — SecurityWeek. Routine patch batch, no confirmed active exploitation.
- **NightmareStresser DDoS Service Disrupted in International Operation** — SecurityWeek. Law enforcement takedown, no new IOCs/TTPs.
- **Microsoft fixes broken copy and paste for Excel 2016 users** — BleepingComputer. Not security relevant.
- **MIND Secures $72 Million for AI-Powered DLP** — SecurityWeek. Funding announcement, marketing content.
- **Check Point, Kaspersky, Tanium Patch Product Vulnerabilities** — SecurityWeek. Duplicate of the Check Point flaw above plus routine patch mentions.
- **How To Write With An LLM** — Simon Willison. Opinion piece, no security angle.
- **Crusoe raises $3.9B to build massive data centers and small modular 'AI factories'** — TechCrunch AI. Funding round, no model/security substance.
- **Google DeepMind launches institute to widen the AGI debate** — TechCrunch AI. Soft PR/institute launch, no concrete outcome.
- **PrismML hopes its tiny LLM will change how we all use AI** — TechCrunch AI. Thin, marketing-toned profile piece.
- **The FAA's plan to fix air traffic? $875M worth of AI** — TechCrunch AI. Government AI procurement story, no security substance.
- **Inside the Modern SOC: Defending the Cross-Environment Pivot** — Unit 42 (Palo Alto). Vendor/product marketing content.
