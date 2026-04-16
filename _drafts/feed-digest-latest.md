# Digest — 2026-04-16 PM

- Window: last 14h
- Raw items considered: 21
- Relevant: 11
- Skippable: 10

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Cisco Patches Four Critical CVEs in ISE and Webex Enabling Code Execution and User Impersonation — `2026-04-16-cisco-critical-ise-webex-cve-2026-20184.md`
- [x] **[HIGH]** Splunk Enterprise Patches RCE Flaw Exploitable by Low-Privileged Users via File Upload — `2026-04-16-splunk-enterprise-rce-low-privilege-file-upload.md`
- [x] **[HIGH]** PHANTOMPULSE RAT Delivered via Obsidian Plugin Abuse in Targeted Finance and Crypto Attacks — `2026-04-16-phantompulse-rat-obsidian-plugin-finance-crypto.md`
- [x] **[HIGH]** Comment and Control: Claude Code, Gemini CLI, and GitHub Copilot Vulnerable to Prompt Injection via Code Comments — `2026-04-16-comment-and-control-ai-coding-agents-prompt-injection.md`
- [x] **[HIGH]** PowMix: Cisco Talos Exposes Novel Botnet Targeting Czech Republic Workforce Since December 2025 — `2026-04-16-powmix-botnet-czech-workforce.md`
- [x] **[HIGH]** UAC-0247 Targets Ukrainian Clinics and Government with AgingFly Espionage Malware — `2026-04-16-uac-0247-agingfly-ukraine-hospitals-espionage.md`
- [x] **[HIGH]** US Nationals Sentenced for Running North Korean IT Worker Laptop Farm Infiltrating 100+ Companies — `2026-04-16-dprk-it-worker-laptop-farm-us-prison.md`
- [x] **[MEDIUM]** OpenAI Launches Trusted Access for Cyber Program with GPT-5.4-Cyber Model and $10M API Grants — `2026-04-16-openai-trusted-access-cyber-gpt54.md`
- [x] **[MEDIUM]** Six-Year Ransomware Campaign Quietly Targets Turkish Homes and SMBs — `2026-04-16-6-year-ransomware-campaign-turkish-smbs.md`
- [x] **[MEDIUM]** NIST Narrows NVD Enrichment to CISA KEV and Critical Software CVEs — `2026-04-16-nist-nvd-enrichment-cisa-kev-prioritization.md`
- [x] **[MEDIUM]** Microsoft Zero Day Quest 2026: $2.3M Paid Out for 80+ Cloud and AI Vulnerabilities — `2026-04-16-microsoft-zero-day-quest-2026.md`

## Relevant (details)

### 1. Cisco Patches Four Critical CVEs in ISE and Webex Enabling Code Execution and User Impersonation
- **Source:** The Hacker News — https://thehackernews.com/2026/04/cisco-patches-four-critical-identity.html
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `rce`, `cisco`
- **Summary:** Cisco patched four critical flaws in ISE and Webex, including CVE-2026-20184 (CVSS 9.8) — an SSO certificate validation bypass enabling full user impersonation. Additional flaws allow unauthenticated RCE; ISE is a high-value pivot point in enterprise network access control.

### 2. Splunk Enterprise Patches RCE Flaw Exploitable by Low-Privileged Users via File Upload
- **Source:** SecurityWeek — https://www.securityweek.com/splunk-enterprise-update-patches-code-execution-vulnerability/
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `rce`
- **Summary:** A Splunk Enterprise RCE flaw lets low-privileged users upload files to a temp directory to execute code on the server. Particularly dangerous where broad Splunk access is granted to operational teams.

### 3. PHANTOMPULSE RAT Delivered via Obsidian Plugin Abuse in Targeted Finance and Crypto Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/04/obsidian-plugin-abuse-delivers.html
- **Severity:** high
- **Tags:** `malware`, `phishing`, `rce`
- **Summary:** Elastic Security Labs (REF6598) documented a novel campaign abusing Obsidian note-taking plugins to deliver the previously unknown PHANTOMPULSE RAT against finance and crypto sector targets. Exploits trust in the Obsidian plugin ecosystem rather than conventional phishing lures.

### 4. Comment and Control: Claude Code, Gemini CLI, and GitHub Copilot Vulnerable to Prompt Injection via Code Comments
- **Source:** SecurityWeek — https://www.securityweek.com/claude-code-gemini-cli-github-copilot-agents-vulnerable-to-prompt-injection-via-comments/
- **Severity:** high
- **Tags:** `llm`, `vulnerability`, `appsec`, `anthropic`, `github`, `google`
- **Summary:** Researcher disclosed "Comment and Control" — adversarial instructions embedded in code comments that cause Claude Code, Gemini CLI, and GitHub Copilot agents to execute injected commands. Any file or repo ingested as agent context is a potential attack surface.

### 5. PowMix: Cisco Talos Exposes Novel Botnet Targeting Czech Republic Workforce Since December 2025
- **Source:** Cisco Talos — https://blog.talosintelligence.com/powmix-botnet-targets-czech-workforce/
- **Severity:** high
- **Tags:** `malware`, `vulnerability`
- **Summary:** Cisco Talos documented PowMix, a previously undocumented botnet running against broad Czech Republic workforce populations since at least December 2025. Multi-month undetected operation and national-scale targeting suggest credential harvesting or proxy-network objectives.

### 6. UAC-0247 Targets Ukrainian Clinics and Government with AgingFly Espionage Malware
- **Source:** The Hacker News — https://thehackernews.com/2026/04/uac-0247-targets-ukrainian-clinics-and.html
- **Severity:** high
- **Tags:** `malware`, `data-breach`
- **Summary:** CERT-UA attributed a March–April 2026 espionage campaign (UAC-0247) targeting Ukrainian emergency clinics and government bodies deploying AgingFly, a new malware that steals data from Chromium browsers and WhatsApp. Consistent with ongoing Russian intelligence collection against Ukrainian infrastructure.

### 7. US Nationals Sentenced for Running North Korean IT Worker Laptop Farm Infiltrating 100+ Companies
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/us-nationals-behind-north-korean-it-worker-laptop-farm-sent-to-prison/
- **Severity:** high
- **Tags:** `iam`
- **Summary:** Two US nationals sentenced for enabling DPRK IT workers to fraudulently infiltrate 100+ companies including Fortune 500 firms via a managed laptop farm. The DPRK IT worker infiltration program remains an active ongoing threat.

### 8. OpenAI Launches Trusted Access for Cyber Program with GPT-5.4-Cyber Model and $10M API Grants
- **Source:** OpenAI Blog — https://openai.com/index/accelerating-cyber-defense-ecosystem
- **Severity:** medium
- **Tags:** `openai`, `llm`, `ai-safety`
- **Summary:** OpenAI launched "Trusted Access for Cyber" offering GPT-5.4-Cyber (a specialized cyber model) plus $10M in API grants to security firms building AI-native defense tooling. Competes directly with Anthropic Mythos and Google's security AI programs.

### 9. Six-Year Ransomware Campaign Quietly Targets Turkish Homes and SMBs
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/6-year-ransomware-campaign-turkish-homes-smbs
- **Severity:** medium
- **Tags:** `ransomware`
- **Summary:** A ransomware campaign targeting Turkish residential users and SMBs has run uninterrupted for six years, sustained by persistent under-reporting of sub-enterprise incidents. Highlights the blind spot in threat visibility below the enterprise threshold.

### 10. NIST Narrows NVD Enrichment to CISA KEV and Critical Software CVEs
- **Source:** SecurityWeek — https://www.securityweek.com/nist-prioritizes-nvd-enrichment-for-cves-in-cisa-kev-critical-software/
- **Severity:** medium
- **Tags:** `cve`, `vulnerability`
- **Summary:** NIST announced NVD will only auto-enrich CVEs in the CISA KEV catalog or meeting specific criticality criteria. Vuln management pipelines that pull CVSS/CPE data from NVD for all CVEs will silently receive incomplete results for entries outside the priority set.

### 11. Microsoft Zero Day Quest 2026: $2.3M Paid Out for 80+ Cloud and AI Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/microsoft-paid-out-2-3-million-at-zero-day-quest-2026-hacking-contest/
- **Severity:** medium
- **Tags:** `vulnerability`, `microsoft`, `ai-safety`, `cloud-security`
- **Summary:** Microsoft's Zero Day Quest 2026 paid out $2.3M of a $5M pool for 80+ high-impact cloud and AI vulnerabilities. The density of findings in AI-integrated surfaces confirms these are currently high-yield attack areas.

## Skippable

- **Data breach at edtech giant McGraw Hill affects 13.5 million accounts** — BleepingComputer. Duplicate of existing post `2026-04-15-mcgraw-hill-shinyhunters-salesforce-45m-records.md`; no new technical substance beyond updated account count.
- **Hidden Passenger? How Taboola Routes Logged-In Banking Sessions to Temu** — The Hacker News. Marketing-gated content ("Download now →"); not substantive standalone reporting.
- **Cisco Patches Critical Vulnerabilities in Webex, ISE** — SecurityWeek. Duplicate of item 1 (same Cisco patch batch; The Hacker News version has more CVE detail).
- **More than pretty pictures: Wendy Bishop on visual storytelling in tech** — Cisco Talos. Career/human interest, no security news value.
- **Ransomware Hits Automotive Data Expert Autovista** — SecurityWeek. Victim disclosure without TTPs or IOCs.
- **DeepL, known for text translation, now wants to translate your voice** — TechCrunch AI. Non-security product feature launch.
- **Microsoft: April Windows Server 2025 update may fail to install** — BleepingComputer. Update install failure; IT ops issue, not a security vulnerability.
- **datasette.io news preview** — Simon Willison. Developer tool preview, no security angle.
- **datasette-export-database 0.3a1** — Simon Willison. Minor plugin maintenance release, no security angle.
- **Ukrainian emergency services and hospitals hit by espionage campaign using new AgingFly malware** — The Record (Recorded Future). Duplicate of UAC-0247 item; credited as secondary source in `2026-04-16-uac-0247-agingfly-ukraine-hospitals-espionage.md`.
