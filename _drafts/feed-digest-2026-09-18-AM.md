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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `data-breach`, `vulnerability`
- **Slug:** `gyazo-data-breach-23-million-records`
- **Must-know:** yes
- **Summary:** Helpfeel, maker of image-hosting service Gyazo, disclosed that an attacker exploited a vulnerability in its image upload server to gain unauthorized access, affecting roughly 23 million user records. Qualifies as must-know given the breach scale (>10k users).

### 2. Trail of Bits: Using AI to Build Custom Tooling Before Code Review Begins
- **Source:** Trail of Bits — https://blog.trailofbits.com/2026/09/18/auditing-in-the-age-of-good-enough-ai/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `llm`, `appsec`, `devsecops`
- **Slug:** `trail-of-bits-ai-security-audits`
- **Must-know:** no
- **Summary:** Trail of Bits describes using AI agents to build custom tooling and formal models before code review starts, applied to an audit of Miden VM, a zero-knowledge VM with minimal existing tooling. Distinct from the common "AI agentic code review" post pattern.

### 3. WeaselBiscuit Stealer Spreads via 13 npm Packages to Harvest Chrome Extension Storage
- **Source:** The Hacker News — https://thehackernews.com/2026/09/weaselbiscuit-stealer-spreads-via-13.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `malware`
- **Slug:** `weaselbiscuit-npm-stealer-chrome-extensions`
- **Must-know:** no
- **Summary:** 13 npm packages were found delivering a new JavaScript stealer, WeaselBiscuit, that harvests Chrome extension storage data. It shares functional overlap with BeaverTail, a strain linked to DPRK's Contagious Interview campaign.

### 4. Prompt Injection in AWS AgentCore Harness Can Exfiltrate Credentials
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/securing-aws-agentcore-harness-credentials/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `aws`, `iam`
- **Slug:** `agentcore-harness-prompt-injection-credential-theft`
- **Must-know:** no
- **Summary:** Unit 42 found that default configurations in AWS AgentCore Harness allow prompt injection attacks to exfiltrate credentials from AI agent deployments, and outline steps to secure agents against this.

### 5. Brevo Supply Chain Attack Injects Malware Into 100,000 Websites
- **Source:** SecurityWeek — https://www.securityweek.com/brevo-supply-chain-attack-injects-malware-into-100000-websites/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`, `cloud-security`
- **Slug:** `brevo-supply-chain-attack-100k-websites`
- **Must-know:** yes
- **Summary:** Attackers used a compromised Brevo API key to deploy a malicious Cloudflare Worker that injected malicious scripts into roughly 100,000 websites. Qualifies as must-know given critical severity + supply-chain nature.

### 6. New Check Point Flaw Lets Hackers Execute Code With Root Privileges
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/check-point-warns-critical-flaw-lets-hackers-execute-code-as-root/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `privilege-escalation`, `vulnerability`, `cve`
- **Slug:** `check-point-critical-rce-root-flaw`
- **Must-know:** no
- **Summary:** Check Point released updates for a critical vulnerability allowing code execution with root privileges on management systems. No confirmed active exploitation reported, so kept below must-know.

### 7. Claimed Bug Bounty Hunter Likely Used LLM to Build PhantomRaven npm Stealer
- **Source:** The Hacker News — https://thehackernews.com/2026/09/claimed-bug-bounty-hunter-likely-used.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `npm`, `malware`, `supply-chain`
- **Slug:** `phantomraven-npm-stealer-llm-built`
- **Must-know:** no
- **Summary:** A financially motivated actor distributed the PhantomRaven JS stealer via npm; researchers assess with high confidence it was LLM-written, based on verbose comments, placeholder code, and token-analysis patterns.

### 8. Critical Orkes Conductor Vulnerability Exploited in Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/critical-orkes-conductor-vulnerability-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `orkes-conductor-rce-exploited-in-attacks`
- **Must-know:** no
- **Summary:** CVE-2026-58138 is an unauthenticated RCE in Orkes Conductor, exploitable via inline workflow definitions, and is being actively exploited. Not flagged must-know since it's a tracked CVE rather than confirmed zero-day.

### 9. AI Agent Breaches Spanish Organization, Modifies Personal Data
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/ai-agent-breaches-spanish-organization-personal-data
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`, `data-breach`
- **Slug:** `ai-agent-breaches-spanish-organization`
- **Must-know:** no
- **Summary:** An AI agent was reportedly used to breach a Spanish organization and modify personal data. Kept at medium severity since the source summary is largely commentary with limited technical/organizational detail.

### 10. RatHat Android Malware Abuses ADB to Retain Shell Access After Uninstall
- **Source:** The Hacker News — https://thehackernews.com/2026/09/rathat-android-malware-abuses-adb-to.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `android`
- **Slug:** `rathat-android-malware-ai-powered`
- **Must-know:** no
- **Summary:** RatHat is a new Android malware family, assessed to be China-operated, that abuses ADB to retain shell access post-uninstall and includes an AI-powered system for navigating compromised devices. Spread via smishing and malvertising.

### 11. Targeted Attacks on Prominent Rustaceans Aim to Compromise crates.io Publishers
- **Source:** Simon Willison — https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/
- **Section:** AI — News & Analysis
- **Severity:** high
- **Tags:** `supply-chain`, `phishing`
- **Slug:** `targeted-attacks-on-rust-crates-maintainers`
- **Must-know:** no
- **Summary:** The crates.io security team is warning of a campaign targeting rust-lang members and popular crate owners via fake video-call pretexts (job/project offers) to install malware and compromise accounts in order to publish malicious crates.

## Skippable

- **[Virtual Event] Cybersecurity Outlook 2027** — Dark Reading. Event promo, no news value.
- **Flash floods can strike without warning — this new technology could change that** — The Verge AI. Generic AI application story, no security angle.
- **Microsoft Patches 18 Vulnerabilities in AI, Cloud Products** — SecurityWeek. Routine patch batch, no confirmed active exploitation of a single critical CVE.
- **NightmareStresser DDoS Service Disrupted in International Operation** — SecurityWeek. Law enforcement takedown announcement, no new IOCs/TTPs for defenders.
- **Microsoft fixes broken copy and paste for Excel 2016 users** — BleepingComputer. Not security relevant.
- **MIND Secures $72 Million for AI-Powered DLP** — SecurityWeek. Funding announcement, marketing content.
- **Check Point, Kaspersky, Tanium Patch Product Vulnerabilities** — SecurityWeek. Duplicate coverage of the Check Point flaw (see item 6 above) plus routine patch-batch mentions for Kaspersky/Tanium.
- **How To Write With An LLM** — Simon Willison. Opinion piece on LLM writing assistance, no security angle.
- **Crusoe raises $3.9B to build massive data centers and small modular 'AI factories'** — TechCrunch AI. Funding round, no model/security substance.
- **Google DeepMind launches institute to widen the AGI debate** — TechCrunch AI. Soft PR/institute launch, no concrete model release or regulatory outcome.
- **PrismML hopes its tiny LLM will change how we all use AI** — TechCrunch AI. Thin, marketing-toned profile piece without concrete launch details.
- **The FAA's plan to fix air traffic? $875M worth of AI** — TechCrunch AI. Government AI procurement/deployment story, no security or regulatory substance.
- **Inside the Modern SOC: Defending the Cross-Environment Pivot** — Unit 42 (Palo Alto). Vendor/product marketing content (Managed XSIAM promotion).
