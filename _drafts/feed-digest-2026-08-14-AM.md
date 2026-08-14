# Digest — 2026-08-14 AM

- Window: last 14h
- Raw items considered: 18
- Relevant: 9
- Skippable: 9

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Hackers Exploiting Unpatched GeoServer Zero-Day — `2026-08-14-geoserver-zero-day-sqli-rce.md`
- [x] **[MEDIUM]** AmnesiaStealer macOS Malware Steals Data, Controls Browser Sessions — `2026-08-14-amnesiastealer-macos-infostealer.md`
- [x] **[MEDIUM]** Apple Sends New 'Threat Notification' Alerts Over Mercenary Spyware Attacks — `2026-08-14-apple-threat-notification-mercenary-spyware.md`
- [x] **[INFORMATIONAL]** AWS Certificate Manager Will Discontinue Email Validation for Public Certificates — `2026-08-14-aws-acm-email-validation-deprecation.md`
- [x] **[HIGH]** Akira Hackers Disable EDR With Safe Mode, Steal Data but Fail to Encrypt — `2026-08-14-akira-ransomware-edr-safe-mode-bypass.md`
- [x] **[CRITICAL]** Global Threat Campaign Hits Critical VMware vCenter Flaw — `2026-08-14-vmware-vcenter-cve-2026-59310-exploited.md`
- [x] **[INFORMATIONAL]** OpenAI Introduces 'Ultrafast,' a Mode That Runs GPT-5.6 Sol at 14x Speed — `2026-08-14-openai-ultrafast-gpt-5-6-sol.md`
- [x] **[MEDIUM]** Anthropic Set AI Agents Loose on the Same Task. They Started a Turf War. — `2026-08-14-anthropic-multi-agent-turf-war.md`
- [x] **[MEDIUM]** Hackers Breach Govt Webmail While Running Parallel Crypto Fraud — `2026-08-14-jewelbug-govt-webmail-breach-crypto-fraud.md`

## Relevant (details)

### 1. Hackers Exploiting Unpatched GeoServer Zero-Day
- **Source:** SecurityWeek — https://www.securityweek.com/hackers-exploiting-unpatched-geoserver-zero-day/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `sqli`, `rce`, `vulnerability`
- **Slug:** `geoserver-zero-day-sqli-rce`
- **Must-know:** yes
- **Summary:** Attackers are actively exploiting an unpatched zero-day in GeoServer described as a SQL injection flaw that can be chained to remote code execution. No patch is currently available.

### 2. AmnesiaStealer macOS Malware Steals Data, Controls Browser Sessions
- **Source:** SecurityWeek — https://www.securityweek.com/amnesiastealer-macos-malware-steals-data-controls-browser-sessions/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `amnesiastealer-macos-infostealer`
- **Must-know:** no
- **Summary:** A Rust-based macOS infostealer harvests passwords, Keychain data, Chromium browser data, and Safari cookies, and can also control active browser sessions.

### 3. Apple Sends New 'Threat Notification' Alerts Over Mercenary Spyware Attacks
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/apple/apple-sends-new-threat-notification-alerts-over-mercenary-spyware-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `apple-threat-notification-mercenary-spyware`
- **Must-know:** no
- **Summary:** Apple has begun sending a new "Threat Notification" alert format warning iPhone users of detected mercenary spyware attacks against their device.

### 4. AWS Certificate Manager Will Discontinue Email Validation for Public Certificates
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/aws-certificate-manager-will-discontinue-email-validation-to-prove-domain-validation-for-certificates/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `aws`, `cloud-security`
- **Slug:** `aws-acm-email-validation-deprecation`
- **Must-know:** no
- **Summary:** AWS will discontinue email-validated public certificates in ACM by September 30, 2027, aligning with the CA/Browser Forum's industry-wide deprecation of email-based domain validation. Teams must migrate to DNS validation before then.

### 5. Akira Hackers Disable EDR With Safe Mode, Steal Data but Fail to Encrypt
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/akira-hackers-disable-edr-with-safe-mode-steal-data-but-fail-to-encrypt/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`
- **Slug:** `akira-ransomware-edr-safe-mode-bypass`
- **Must-know:** no
- **Summary:** An Akira ransomware affiliate rebooted a compromised host into Safe Mode with Networking to disable EDR tooling, exfiltrating data before failing to complete encryption.

### 6. Global Threat Campaign Hits Critical VMware vCenter Flaw
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/global-threat-campaign-critical-vmware-vcenter-flaw
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `rce`
- **Slug:** `vmware-vcenter-cve-2026-59310-exploited`
- **Must-know:** no
- **Summary:** A global campaign has been exploiting critical VMware vCenter flaw CVE-2026-59310 since earlier this month; patching alone may not fully remediate already-compromised systems.

### 7. OpenAI Introduces 'Ultrafast,' a Mode That Runs GPT-5.6 Sol at 14x Speed
- **Source:** TechCrunch AI — https://techcrunch.com/2026/08/13/openai-introduces-ultrafast-a-new-mode-that-makes-gpt-5-6-sol-work-at-14x-the-speed/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-launch`, `openai`, `llm`
- **Slug:** `openai-ultrafast-gpt-5-6-sol`
- **Must-know:** no
- **Summary:** OpenAI launched a preview of "Ultrafast," an inference mode that runs GPT-5.6 Sol at 14x the speed of standard mode, targeting enterprise users needing lower latency.

### 8. Anthropic Set AI Agents Loose on the Same Task. They Started a Turf War.
- **Source:** TechCrunch AI — https://techcrunch.com/2026/08/13/anthropic-set-ai-agents-loose-on-the-same-task-they-started-a-turf-war/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-safety`, `anthropic`, `llm`
- **Slug:** `anthropic-multi-agent-turf-war`
- **Must-know:** no
- **Summary:** Anthropic research found that AI agents assigned the same task can clash, collude, and coordinate unexpectedly, raising questions about whether current safety evaluations capture multi-agent risks.

### 9. Hackers Breach Govt Webmail While Running Parallel Crypto Fraud
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-breach-govt-webmail-while-running-parallel-crypto-fraud/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `jewelbug-govt-webmail-breach-crypto-fraud`
- **Must-know:** no
- **Summary:** The Jewelbug hacker group has been running espionage operations against governments and militaries, including breaching government webmail, while separately conducting cryptocurrency fraud.

## Skippable

- **sqlite-utils 4.2.1** — Simon Willison. Dev-tool bugfix release, no security or AI substance.
- **Microsoft's Clippy-like Mico character is no longer the face of Copilot** — The Verge AI. UI/product cosmetic change, no security or capability substance.
- **Writer introduces new AI model and upgraded harness to contain token costs** — TechCrunch AI. Thin post-training model announcement, mostly marketing framing.
- **Ukraine shuts down 94 fraudulent call centers, seize millions in cash** — BleepingComputer. Regional law-enforcement action without technical detail or IOCs.
- **Databricks wanted to raise $1B, investors wanted $15B. It settled on $5B at a $190B valuation.** — TechCrunch AI. Funding news, no security or technical substance.
- **sqlite-utils 4.2** — Simon Willison. Dev-tool feature release, no security or AI substance.
- **llm-gemini 0.33** — Simon Willison. Plugin release adding model support, not a lab model launch itself.
- **OpenAI is losing its second executive this week** — The Verge AI. Personnel/departure news, no security or technical substance.
- **IBM partners with OpenAI to bolster enterprise AI push** — TechCrunch AI. Partnership/marketing announcement, no security angle.
