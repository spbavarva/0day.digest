# Digest — 2026-08-20 AM

- Window: last 14h
- Raw items considered: 26
- Relevant: 12
- Skippable: 14

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** US Warns of AI-Generated Attacks on Siemens PLCs in Critical Infrastructure — `2026-08-19-ai-powered-attacks-siemens-plcs.md`
- [x] **[HIGH]** Elementor Pro Flaw (CVE-2026-32475) Lets Unauthenticated Attackers Achieve RCE — `2026-08-20-elementor-pro-rce-cve-2026-32475.md`
- [x] **[INFORMATIONAL]** Simon Willison Tests smolmachines as a Sandbox for Untrusted LLM-Generated Code — `2026-08-19-smolmachines-sandbox-untrusted-code.md`
- [x] **[MEDIUM]** Ransomware Affiliate Poses as 'Ransom Busters' Recovery Firm to Steal Payments — `2026-08-19-ransom-busters-fake-recovery-firm-scam.md`
- [x] **[HIGH]** Sakura Internet Hack Exposes Data of Up to 1.36 Million Accounts — `2026-08-19-sakura-internet-data-breach.md`
- [x] **[MEDIUM]** 'Kriminal' AI Platform Offers Guardrail-Free Cybercrime Tools — `2026-08-19-kriminal-ai-platform-cybercrime.md`
- [x] **[HIGH]** CareCloud Data Breach Impacts 3.7 Million Patients — `2026-08-19-carecloud-breach-3-7-million-patients.md`
- [x] **[MEDIUM]** Spectre Attack Leaks JWTs From Co-Located Cloudflare Workers — `2026-08-19-cloudflare-workers-spectre-jwt-leak.md`
- [x] **[INFORMATIONAL]** OpenAI Expands Zero Data Retention and Previews Private Safety Processing — `2026-08-19-openai-zero-data-retention-frontier-models.md`
- [x] **[INFORMATIONAL]** Researchers Say OpenAI Revoked Access to Its Trusted Access for Cyber Program — `2026-08-19-openai-revokes-cyber-program-access.md`
- [x] **[MEDIUM]** CameraSwarm Campaign Compromises 14,500 Dahua Web Cameras — `2026-08-19-dahua-cameraswarm-14500-cameras.md`
- [x] **[MEDIUM]** OpenAI Pauses Frontier RL Training to Tighten Safety Defenses — `2026-08-19-openai-pauses-frontier-rl-training.md`

## Relevant (details)

### 1. US Warns of AI-Generated Attacks on Siemens PLCs in Critical Infrastructure
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/us-warns-of-ai-powered-attacks-on-siemens-plcs-in-critical-infrastructure/
- **Severity:** high
- **Tags:** `vulnerability`, `llm`
- **Summary:** NSA, FBI and other federal agencies warned that threat actors are using AI-generated scripts, combined with exploitation of known vulnerabilities, to target Siemens S7 Series PLCs in U.S. critical infrastructure.

### 2. Elementor Pro Flaw (CVE-2026-32475) Lets Unauthenticated Attackers Achieve RCE
- **Source:** The Hacker News — https://thehackernews.com/2026/08/elementor-pro-flaw-could-let.html
- **Severity:** high
- **Tags:** `rce`, `cve`
- **Summary:** A critical unrestricted file upload flaw in the Elementor Pro WordPress plugin's Forms module (CVSS 9.0) lets unauthenticated attackers upload PHP files and execute code.

### 3. Simon Willison Tests smolmachines as a Sandbox for Untrusted LLM-Generated Code
- **Source:** Simon Willison — https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/
- **Severity:** informational
- **Tags:** `llm`, `appsec`
- **Summary:** Willison had Claude research smolmachines/smolvm as a sandbox for running untrusted, model-generated code with resource limits, no network access, and restricted filesystem access.

### 4. Ransomware Affiliate Poses as 'Ransom Busters' Recovery Firm to Steal Payments
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/rogue-ransomware-affiliate-ransom-busters-poses-as-recovery-firm/
- **Severity:** medium
- **Tags:** `ransomware`, `phishing`
- **Summary:** A suspected ransomware affiliate poses as a recovery firm called "Ransom Busters," contacting victims before an attack becomes public to offer decryption keys or data deletion for a fee.

### 5. Sakura Internet Hack Exposes Data of Up to 1.36 Million Accounts
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/sakura-internet-hack-exposes-data-of-up-to-136-million-accounts/
- **Severity:** high
- **Tags:** `data-breach`, `cloud-security`
- **Summary:** Sakura Internet disclosed unauthorized access to its sales management system, exposing customer contract and membership information for up to 1.36 million accounts.

### 6. 'Kriminal' AI Platform Offers Guardrail-Free Cybercrime Tools
- **Source:** Dark Reading — https://www.darkreading.com/application-security/no-filter-kriminal-ai-platform-cybercrime-concerns
- **Severity:** medium
- **Tags:** `llm`, `ai-safety`
- **Summary:** A platform branded "Kriminal" markets guardrail-free social engineering, offensive cybercrime, and OSINT scanning to anyone paying in cryptocurrency, despite officially forbidding illicit use.

### 7. CareCloud Data Breach Impacts 3.7 Million Patients
- **Source:** The Record (Recorded Future) — https://therecord.media/electronic-health-record-company-carecloud-data-breach
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** CareCloud filed HHS documents confirming 3,756,469 individuals had information exposed after a hacker spent roughly eight hours inside one of its EHR environments.

### 8. Spectre Attack Leaks JWTs From Co-Located Cloudflare Workers
- **Source:** The Hacker News — https://thehackernews.com/2026/08/cloudflare-workers-spectre-attack-leaks.html
- **Severity:** medium
- **Tags:** `vulnerability`, `cloud-security`
- **Summary:** Researchers demonstrated a remote Spectre-class side-channel attack leaking a JWT from a co-located Cloudflare Worker in production at up to 12 bits/second, 360x an earlier 2021 demonstration.

### 9. OpenAI Expands Zero Data Retention and Previews Private Safety Processing
- **Source:** OpenAI Blog — https://openai.com/index/offering-zero-data-retention-for-frontier-models
- **Severity:** informational
- **Tags:** `openai`, `ai-safety`
- **Summary:** OpenAI reaffirmed Zero Data Retention for eligible API customers and previewed "Private Safety Processing," a way to run AI safety monitoring without compromising data privacy.

### 10. Researchers Say OpenAI Revoked Access to Its Trusted Access for Cyber Program
- **Source:** TechCrunch AI — https://techcrunch.com/2026/08/19/researchers-complain-that-openai-revoked-their-access-to-limited-cyber-program/
- **Severity:** informational
- **Tags:** `openai`, `appsec`
- **Summary:** Security researchers say OpenAI revoked their access to Trusted Access for Cyber, a program meant to give vetted defenders better models to find and report vulnerabilities faster.

### 11. CameraSwarm Campaign Compromises 14,500 Dahua Web Cameras
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-compromise-14-500-dahua-web-cameras-in-35-day-campaign/
- **Severity:** medium
- **Tags:** `vulnerability`, `malware`
- **Summary:** Researchers tracked a 35-day campaign, dubbed CameraSwarm, that compromised more than 14,500 Dahua IP cameras, concentrated mostly in Ukraine and Russia.

### 12. OpenAI Pauses Frontier RL Training to Tighten Safety Defenses
- **Source:** The Hacker News — https://thehackernews.com/2026/08/openai-pauses-frontier-rl-training-as.html
- **Severity:** medium
- **Tags:** `openai`, `ai-safety`
- **Summary:** OpenAI paused reinforcement learning training for its latest models for two weeks to shore up defenses and expand monitoring, citing a wish to avert "another Hugging Face-like incident."

## Skippable

- **Hackers Using AI to Target Siemens PLCs in Critical US Sectors** — SecurityWeek. Duplicate of the Siemens PLC advisory story.
- **NSA, FBI warns of hackers using AI-generated tools in attacks on critical infrastructure technology** — The Record. Duplicate of the Siemens PLC advisory story.
- **Microsoft says August Windows updates may cause gaming issues** — BleepingComputer. Generic IT bug, no security angle.
- **OpenAI confirms ChatGPT is down as logins and signups fail** — BleepingComputer. Service outage, no security angle.
- **Stripe didn't really buy OpenRouter because of the 'singularity'** — TechCrunch AI. Business/M&A speculation, no technical substance.
- **Quoting Jeremy Morrell** — Simon Willison. Opinion quote, no news value.
- **Conceptual integrity and counting lines of code** — Simon Willison. Opinion piece, no news value.
- **OpenAI seeks to one-up Anthropic with new customer privacy protections** — TechCrunch AI. Duplicate of OpenAI's Zero Data Retention announcement.
- **Cognition CEO denies report that SpaceX tried to acquire the startup** — TechCrunch AI. M&A rumor/denial, no technical substance.
- **AI was supposed to win people over by now — it hasn't** — TechCrunch AI. Opinion piece, no news value.
- **5 new ways to level up your learning with Search** — Google AI Blog. Consumer feature marketing, no security angle.
- **Google packs Search and Gemini with new AI study tools** — TechCrunch AI. Duplicate of Google's study-tools launch; non-security regardless.
- **Google Gemini is getting a dedicated student hub** — The Verge AI. Duplicate of Google's study-tools launch; non-security regardless.
- **CareCloud breach (BleepingComputer version)** — BleepingComputer. Duplicate of the CareCloud breach story.
