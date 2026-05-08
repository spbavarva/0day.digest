# Digest — 2026-05-08 PM

- Window: last 14h
- Raw items considered: 35
- Relevant: 17
- Skippable: 18

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Dirty Frag: Unpatched Linux Zero-Day Gives Root on All Major Distros — `2026-05-08-dirty-frag-linux-zero-day-lpe.md`
- [x] **[CRITICAL]** Hackers Breach ICS at Five Polish Water Treatment Plants — `2026-05-08-polish-water-plant-ics-breaches.md`
- [x] **[HIGH]** CISA Orders Four-Day Patch for Ivanti EPMM Zero-Day Under Active Exploitation — `2026-05-08-ivanti-epmm-zero-day-cisa-kev.md`
- [x] **[HIGH]** CISA Adds BerriAI LiteLLM SQL Injection to Known Exploited Vulnerabilities — `2026-05-08-litellm-sql-injection-cisa-kev.md`
- [x] **[HIGH]** Quasar Linux RAT Targets Developer Credentials for Supply Chain Compromise — `2026-05-08-quasar-linux-rat-supply-chain.md`
- [x] **[HIGH]** RansomHouse Claims Trellix Source Code Breach, Publishes Proof Screenshots — `2026-05-08-trellix-source-code-breach-ransomhouse.md`
- [x] **[HIGH]** Prompt Injection Flaw in Claude Chrome Extension Allows AI Agent Takeover — `2026-05-08-claude-chrome-extension-prompt-injection.md`
- [x] **[HIGH]** CVE-2025-68670: Pre-Auth RCE in xrdp Discovered and Patched — `2026-05-08-xrdp-pre-auth-rce-cve-2025-68670.md`
- [x] **[HIGH]** AI Firm Braintrust Confirms AWS Breach, AI Provider API Keys Exposed — `2026-05-08-braintrust-ai-aws-breach-api-keys.md`
- [x] **[HIGH]** Cybercriminal Group Compromises Canvas LMS, Dozens of Universities Reschedule Finals — `2026-05-08-canvas-lms-cyberattack-universities.md`
- [x] **[HIGH]** PamDOORa: New Linux Backdoor Abuses PAM Modules for Persistent SSH Access — `2026-05-08-pamdoora-linux-pam-backdoor.md`
- [x] **[HIGH]** PCPJack Worm Evicts Rival Malware and Steals AWS and Kubernetes Credentials — `2026-05-08-pcpjack-worm-cloud-credential-theft.md`
- [x] **[MEDIUM]** Zara Data Breach Exposed Personal Information of 197,000 Customers — `2026-05-08-zara-data-breach-197k.md`
- [x] **[MEDIUM]** 28 Fake Call History Apps on Google Play Defraud 7.3 Million Android Users — `2026-05-08-fake-call-history-apps-play-store.md`
- [x] **[MEDIUM]** Virginia Contractor Convicted for Destroying Dozens of Federal Databases After Firing — `2026-05-08-contractor-convicted-federal-database-wipe.md`
- [x] **[MEDIUM]** Pro-Ukraine Hackers BO Team and Head Mare Coordinate C2 Infrastructure Against Russia — `2026-05-08-ukraine-bo-team-head-mare-russia.md`
- [x] **[INFORMATIONAL]** CyberSecQwen-4B: Small Specialized LLM Built for Local Defensive Cybersecurity Use — `2026-05-08-cybersecqwen-4b-defensive-security.md`

## Relevant (details)

### 1. Dirty Frag: Unpatched Linux Zero-Day Gives Root on All Major Distros
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-linux-dirty-frag-zero-day-with-poc-exploit-gives-root-privileges/
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `privilege-escalation`, `cve`, `linux`
- **Summary:** A new unpatched LPE vulnerability dubbed Dirty Frag affects all major Linux distros, with a public single-command root exploit. Successor to Copy Fail (CVE-2026-31431), already under active exploitation; no patch available yet.

### 2. Hackers Breach ICS at Five Polish Water Treatment Plants
- **Source:** SecurityWeek — https://www.securityweek.com/polish-security-agency-reports-ics-breaches-at-five-water-treatment-plants/
- **Severity:** critical
- **Tags:** `vulnerability`, `ics`, `data-breach`
- **Summary:** Poland's security agency confirmed ICS breaches at five water treatment plants; attackers could modify operational parameters. No disruption reported but direct capability to harm public water supply existed.

### 3. CISA Orders Four-Day Patch for Ivanti EPMM Zero-Day Under Active Exploitation
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-gives-feds-four-days-to-patch-ivanti-flaw-exploited-as-zero-day/
- **Severity:** high
- **Tags:** `zero-day`, `cve`, `vulnerability`
- **Summary:** CVE-2026-6973 in Ivanti EPMM added to CISA KEV with a four-day federal deadline. Already exploited in targeted attacks; patch available from Ivanti.

### 4. CISA Adds BerriAI LiteLLM SQL Injection to Known Exploited Vulnerabilities
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/alerts/2026/05/08/cisa-adds-one-known-exploited-vulnerability-catalog
- **Severity:** high
- **Tags:** `sqli`, `cve`, `vulnerability`, `llm`
- **Summary:** CVE-2026-42208 in BerriAI LiteLLM (a widely-used LLM proxy) confirmed actively exploited. SQL injection at this layer risks LLM API key and prompt history exposure.

### 5. Quasar Linux RAT Targets Developer Credentials for Supply Chain Compromise
- **Source:** The Hacker News — https://thehackernews.com/2026/05/quasar-linux-rat-steals-developer.html
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `devsecops`, `linux`
- **Summary:** Undocumented Linux RAT QLNX explicitly targets developer and DevOps credentials for supply chain compromise, with keylogging, credential harvesting, and network tunneling capabilities.

### 6. RansomHouse Claims Trellix Source Code Breach, Publishes Proof Screenshots
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/trellix-source-code-breach-claimed-by-ransomhouse-hackers/
- **Severity:** high
- **Tags:** `ransomware`, `data-breach`
- **Summary:** RansomHouse claimed last week's Trellix source code breach with screenshot proof. Source code from a major security vendor heightens downstream exploit risk for Trellix customers.

### 7. Prompt Injection Flaw in Claude Chrome Extension Allows AI Agent Takeover
- **Source:** SecurityWeek — https://www.securityweek.com/vulnerability-in-claude-extension-for-chrome-exposes-ai-agent-to-takeover/
- **Severity:** high
- **Tags:** `vulnerability`, `llm`, `appsec`, `anthropic`, `xss`
- **Summary:** Lax permissions and improper trust in Anthropic's Claude Chrome extension let malicious pages inject arbitrary prompts into the AI agent. Real-world browser-layer prompt injection in a widely-deployed AI tool.

### 8. CVE-2025-68670: Pre-Auth RCE in xrdp Discovered and Patched
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/cve-2025-68670/119742/
- **Severity:** high
- **Tags:** `rce`, `cve`, `vulnerability`
- **Summary:** Kaspersky found and responsibly disclosed a pre-auth RCE in the xrdp open-source RDP server. Patched by maintainers; admins with public-facing xrdp should update immediately.

### 9. AI Firm Braintrust Confirms AWS Breach, AI Provider API Keys Exposed
- **Source:** SecurityWeek — https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/
- **Severity:** high
- **Tags:** `data-breach`, `aws`, `cloud-security`, `ai-safety`
- **Summary:** Attackers hit Braintrust's AWS account and accessed stored LLM provider API keys. Illustrates supply chain risk from AI orchestration platforms that aggregate credentials across providers.

### 10. Cybercriminal Group Compromises Canvas LMS, Dozens of Universities Reschedule Finals
- **Source:** The Record (Recorded Future) — https://therecord.media/universities-forced-to-reschedule-exams-canvas-incident
- **Severity:** high
- **Tags:** `data-breach`, `vulnerability`
- **Summary:** Cybercriminal group injected messages into Instructure Canvas during finals, forcing exam reschedules at dozens of universities. Data access scope not yet disclosed.

### 11. PamDOORa: New Linux Backdoor Abuses PAM Modules for Persistent SSH Access
- **Source:** The Hacker News — https://thehackernews.com/2026/05/new-linux-pamdoora-backdoor-uses-pam.html
- **Severity:** high
- **Tags:** `malware`, `vulnerability`, `linux`
- **Summary:** Commercial Linux backdoor PamDOORa ($1,600 on Russian forums) abuses PAM to install a magic-password SSH backdoor that survives reboots and credential rotation.

### 12. PCPJack Worm Evicts Rival Malware and Steals AWS and Kubernetes Credentials
- **Source:** SecurityWeek — https://www.securityweek.com/pcpjack-worm-removes-teampcp-infections-steals-credentials/
- **Severity:** high
- **Tags:** `malware`, `cloud-security`, `aws`, `kubernetes`, `container-security`
- **Summary:** PCPJack evicts TeamPCP malware from compromised hosts then steals AWS, Docker, and Kubernetes credentials. Competitive evict-and-replace behavior signals a sophisticated cloud-targeting actor.

### 13. Zara Data Breach Exposed Personal Information of 197,000 Customers
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/zara-data-breach-exposed-personal-information-of-197-000-people/
- **Severity:** medium
- **Tags:** `data-breach`
- **Summary:** 197,000+ Zara customer records stolen and reported to HIBP. Attack vector undisclosed.

### 14. 28 Fake Call History Apps on Google Play Defraud 7.3 Million Android Users
- **Source:** The Hacker News — https://thehackernews.com/2026/05/fake-call-history-apps-stole-payments.html
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Summary:** 28 fraudulent Android apps on Google Play enrolled 7.3 million users in subscription scams delivering fake call data.

### 15. Virginia Contractor Convicted for Destroying Dozens of Federal Databases After Firing
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/former-govt-contractor-convicted-for-wiping-dozens-of-federal-databases/
- **Severity:** medium
- **Tags:** `data-breach`, `insider-threat`
- **Summary:** Federal contractor used retained post-termination access to wipe dozens of government databases. Textbook insider threat from incomplete access revocation.

### 16. Pro-Ukraine Hackers BO Team and Head Mare Coordinate C2 Infrastructure Against Russia
- **Source:** The Record (Recorded Future) — https://therecord.media/ukraine-bo-team-head-mare-hacktivists-team-up-kaspersky
- **Severity:** medium
- **Tags:** `malware`, `threat-intel`
- **Summary:** Kaspersky found shared C2 infrastructure between BO Team and Head Mare hacktivist groups, indicating coordinated attacks against Russian targets.

### 17. CyberSecQwen-4B: Small Specialized LLM Built for Local Defensive Cybersecurity Use
- **Source:** Hugging Face Blog — https://huggingface.co/blog/lablab-ai-amd-developer-hackathon/cybersecqwen-4b
- **Severity:** informational
- **Tags:** `llm`, `ai-launch`, `model-release`, `devsecops`
- **Summary:** 4B-parameter locally-runnable LLM fine-tuned for defensive security tasks, suited for air-gapped environments. No benchmarks yet.

## Skippable

- **PlayStation sees AI as a 'powerful tool' to help make games** — The Verge AI. AI in gaming, no security angle.
- **NVIDIA confirms GeForce NOW data breach affecting Armenian users** — BleepingComputer. Limited regional scope, no technical detail.
- **EMO: Pretraining mixture of experts for emergent modularity** — Hugging Face Blog. AI research paper, no security relevance.
- **The "people's airline" and the enterprise AI gold rush** — TechCrunch AI. Podcast, opinion/analysis, no news value.
- **Microsoft was worried OpenAI would run off to Amazon and 'shit-talk' Azure** — The Verge AI. Legal/business story, no security angle.
- **See what happens when creative legends use AI to make ads for small businesses** — Google AI Blog. Marketing announcement, no relevance.
- **In Other News: Train Hacker Arrested, PamDOORa Linux Backdoor, New CISA Director Frontrunner** — SecurityWeek. Weekly roundup; items covered individually.
- **Why More Analysts Won't Solve Your SOC's Alert Problem** — BleepingComputer. Vendor marketing content (Prophet Security).
- **One Click, Total Shutdown: The "Patient Zero" Webinar on Killing Stealth Breaches** — The Hacker News. Vendor webinar advertisement.
- **Last 24 hours to get 50% off a second pass to TechCrunch Disrupt 2026** — TechCrunch AI. Event advertisement.
- **Everybody wants to rule the AI world** — The Verge AI. Vergecast podcast, no news value.
- **The Good, the Bad and the Ugly in Cybersecurity – Week 19** — SentinelOne Labs. Weekly roundup; PCPJack and Ivanti covered individually.
- **Cyberattack Hits Canvas System Used by Thousands of Schools as Finals Loom** — SecurityWeek. Duplicate of The Record's Canvas item.
- **One Missed Threat Per Week: What 25M Alerts Reveal About Low-Severity Risk** — The Hacker News. Vendor analysis report with marketing angle.
- **Ransomware Group Takes Credit for Trellix Hack** — SecurityWeek. Duplicate of BleepingComputer Trellix item.
- **Ivanti Patches EPMM Zero-Day Exploited in Targeted Attacks** — SecurityWeek. Duplicate of BleepingComputer Ivanti item.
- **Linux Kernel Dirty Frag LPE Exploit Enables Root Access Across Major Distributions** — The Hacker News. Duplicate of BleepingComputer Dirty Frag item.
- **The fax machine is the bottleneck in US healthcare, and VCs are starting to notice** — TechCrunch AI. VC/AI investment piece, no security angle.
