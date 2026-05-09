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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `privilege-escalation`, `cve`, `linux`
- **Slug:** `2026-05-08-dirty-frag-linux-zero-day-lpe`
- **Must-know:** no
- **Summary:** A new unpatched LPE vulnerability dubbed Dirty Frag affects all major Linux distros, with a public single-command root exploit. It is the successor to Copy Fail (CVE-2026-31431), which is already under active exploitation; Dirty Frag itself has no patch yet.

### 2. Hackers Breach ICS at Five Polish Water Treatment Plants
- **Source:** SecurityWeek — https://www.securityweek.com/polish-security-agency-reports-ics-breaches-at-five-water-treatment-plants/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `ics`, `data-breach`
- **Slug:** `2026-05-08-polish-water-plant-ics-breaches`
- **Must-know:** no
- **Summary:** Poland's security agency confirmed hackers gained unauthorized access to ICS at five water treatment plants and could modify operational parameters. No disruption reported, but attackers had direct capability to affect the public water supply.

### 3. CISA Orders Four-Day Patch for Ivanti EPMM Zero-Day Under Active Exploitation
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-gives-feds-four-days-to-patch-ivanti-flaw-exploited-as-zero-day/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `cve`, `vulnerability`
- **Slug:** `2026-05-08-ivanti-epmm-zero-day-cisa-kev`
- **Must-know:** no
- **Summary:** CISA added CVE-2026-6973 in Ivanti EPMM to its KEV catalog with a four-day federal deadline. The flaw has been exploited in targeted attacks; Ivanti has released a patch.

### 4. CISA Adds BerriAI LiteLLM SQL Injection to Known Exploited Vulnerabilities
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/alerts/2026/05/08/cisa-adds-one-known-exploited-vulnerability-catalog
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `sqli`, `cve`, `vulnerability`, `llm`
- **Slug:** `2026-05-08-litellm-sql-injection-cisa-kev`
- **Must-know:** no
- **Summary:** CISA confirmed active exploitation of CVE-2026-42208, a SQL injection flaw in BerriAI LiteLLM — a widely-used open-source LLM proxy. Exploitation at this layer risks exposing LLM API keys and prompt histories.

### 5. Quasar Linux RAT Targets Developer Credentials for Supply Chain Compromise
- **Source:** The Hacker News — https://thehackernews.com/2026/05/quasar-linux-rat-steals-developer.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `devsecops`, `linux`
- **Slug:** `2026-05-08-quasar-linux-rat-supply-chain`
- **Must-know:** no
- **Summary:** A previously undocumented Linux RAT (QLNX) explicitly targets developer and DevOps credentials to facilitate supply chain compromise. Capabilities include keylogging, clipboard monitoring, credential harvesting, and network tunneling.

### 6. RansomHouse Claims Trellix Source Code Breach, Publishes Proof Screenshots
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/trellix-source-code-breach-claimed-by-ransomhouse-hackers/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`, `data-breach`
- **Slug:** `2026-05-08-trellix-source-code-breach-ransomhouse`
- **Must-know:** no
- **Summary:** RansomHouse claimed the Trellix source code repository breach from last week, publishing screenshots as proof. Source code exposure from a major security vendor is high-risk for downstream exploit development.

### 7. Prompt Injection Flaw in Claude Chrome Extension Allows AI Agent Takeover
- **Source:** SecurityWeek — https://www.securityweek.com/vulnerability-in-claude-extension-for-chrome-exposes-ai-agent-to-takeover/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `llm`, `appsec`, `anthropic`, `xss`
- **Slug:** `2026-05-08-claude-chrome-extension-prompt-injection`
- **Must-know:** no
- **Summary:** Lax extension permissions and improper trust handling in Anthropic's Claude Chrome extension allow malicious pages to inject arbitrary prompts into the AI agent. A real-world browser-layer prompt injection attack vector affecting a widely-deployed AI tool.

### 8. CVE-2025-68670: Pre-Auth RCE in xrdp Discovered and Patched
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/cve-2025-68670/119742/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `2026-05-08-xrdp-pre-auth-rce-cve-2025-68670`
- **Must-know:** no
- **Summary:** Kaspersky researchers found CVE-2025-68670, a pre-auth RCE in the xrdp open-source RDP server. Patch is available; admins running xrdp in public-facing environments should apply it immediately.

### 9. AI Firm Braintrust Confirms AWS Breach, AI Provider API Keys Exposed
- **Source:** SecurityWeek — https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `aws`, `cloud-security`, `ai-safety`
- **Slug:** `2026-05-08-braintrust-ai-aws-breach-api-keys`
- **Must-know:** no
- **Summary:** Attackers compromised a Braintrust AWS account and accessed stored AI provider secrets (API keys for LLM providers). Demonstrates growing risk from AI orchestration platforms that aggregate credentials across multiple providers.

### 10. Cybercriminal Group Compromises Canvas LMS, Dozens of Universities Reschedule Finals
- **Source:** The Record (Recorded Future) — https://therecord.media/universities-forced-to-reschedule-exams-canvas-incident
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `vulnerability`
- **Slug:** `2026-05-08-canvas-lms-cyberattack-universities`
- **Must-know:** no
- **Summary:** A cybercriminal group injected messages into the Canvas LMS used by thousands of universities, forcing exam reschedules during finals. Extent of data access not yet disclosed.

### 11. PamDOORa: New Linux Backdoor Abuses PAM Modules for Persistent SSH Access
- **Source:** The Hacker News — https://thehackernews.com/2026/05/new-linux-pamdoora-backdoor-uses-pam.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `vulnerability`, `linux`
- **Slug:** `2026-05-08-pamdoora-linux-pam-backdoor`
- **Must-know:** no
- **Summary:** PamDOORa is a $1,600 commercial Linux backdoor sold on Russian cybercrime forums that abuses PAM modules for persistent SSH access, surviving reboots and credential rotation.

### 12. PCPJack Worm Evicts Rival Malware and Steals AWS and Kubernetes Credentials
- **Source:** SecurityWeek — https://www.securityweek.com/pcpjack-worm-removes-teampcp-infections-steals-credentials/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `cloud-security`, `aws`, `kubernetes`, `container-security`
- **Slug:** `2026-05-08-pcpjack-worm-cloud-credential-theft`
- **Must-know:** no
- **Summary:** PCPJack targets web apps and cloud environments, evicting rival TeamPCP malware before stealing AWS, Docker, and Kubernetes credentials. The evict-and-replace behavior signals a competitive cloud-targeting threat actor.

### 13. Zara Data Breach Exposed Personal Information of 197,000 Customers
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/zara-data-breach-exposed-personal-information-of-197-000-people/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `2026-05-08-zara-data-breach-197k`
- **Must-know:** no
- **Summary:** Hackers stole personal data of 197,000+ Zara customers; breach reported to HIBP. Attack vector not disclosed.

### 14. 28 Fake Call History Apps on Google Play Defraud 7.3 Million Android Users
- **Source:** The Hacker News — https://thehackernews.com/2026/05/fake-call-history-apps-stole-payments.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Slug:** `2026-05-08-fake-call-history-apps-play-store`
- **Must-know:** no
- **Summary:** 28 fraudulent Android apps on Google Play falsely promised call history lookup, then subscribed users to paid fake services. 7.3 million downloads combined; Google notified.

### 15. Virginia Contractor Convicted for Destroying Dozens of Federal Databases After Firing
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/former-govt-contractor-convicted-for-wiping-dozens-of-federal-databases/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`, `insider-threat`
- **Slug:** `2026-05-08-contractor-convicted-federal-database-wipe`
- **Must-know:** no
- **Summary:** A former federal contractor used retained access after termination to wipe dozens of government databases. A textbook insider threat enabled by incomplete offboarding and access revocation failures.

### 16. Pro-Ukraine Hackers BO Team and Head Mare Coordinate C2 Infrastructure Against Russia
- **Source:** The Record (Recorded Future) — https://therecord.media/ukraine-bo-team-head-mare-hacktivists-team-up-kaspersky
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `threat-intel`
- **Slug:** `2026-05-08-ukraine-bo-team-head-mare-russia`
- **Must-know:** no
- **Summary:** Kaspersky identified shared C2 infrastructure between BO Team and Head Mare, two pro-Ukraine hacktivist groups, suggesting coordinated operations against Russian targets.

### 17. CyberSecQwen-4B: Small Specialized LLM Built for Local Defensive Cybersecurity Use
- **Source:** Hugging Face Blog — https://huggingface.co/blog/lablab-ai-amd-developer-hackathon/cybersecqwen-4b
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `llm`, `ai-launch`, `model-release`, `devsecops`
- **Slug:** `2026-05-08-cybersecqwen-4b-defensive-security`
- **Must-know:** no
- **Summary:** CyberSecQwen-4B is a 4B-parameter locally-runnable model fine-tuned for defensive security tasks, suited for air-gapped environments. No detailed benchmarks published yet.

## Skippable

- **PlayStation sees AI as a 'powerful tool' to help make games** — The Verge AI. AI in gaming product development, no security angle.
- **NVIDIA confirms GeForce NOW data breach affecting Armenian users** — BleepingComputer. Limited regional scope, no technical detail; generic breach disclosure.
- **EMO: Pretraining mixture of experts for emergent modularity** — Hugging Face Blog. AI research paper from AllenAI, no security relevance.
- **The "people's airline" and the enterprise AI gold rush** — TechCrunch AI. Podcast episode, analysis/opinion, no news value.
- **Microsoft was worried OpenAI would run off to Amazon and 'shit-talk' Azure** — The Verge AI. Legal/business court docs story, no security angle.
- **See what happens when creative legends use AI to make ads for small businesses** — Google AI Blog. Marketing campaign announcement, no relevance.
- **In Other News: Train Hacker Arrested, PamDOORa Linux Backdoor, New CISA Director Frontrunner** — SecurityWeek. Weekly roundup; constituent stories covered individually.
- **Why More Analysts Won't Solve Your SOC's Alert Problem** — BleepingComputer. Vendor marketing content (Prophet Security), no news value.
- **One Click, Total Shutdown: The "Patient Zero" Webinar on Killing Stealth Breaches** — The Hacker News. Vendor webinar advertisement.
- **Last 24 hours to get 50% off a second pass to TechCrunch Disrupt 2026** — TechCrunch AI. Event advertisement.
- **Everybody wants to rule the AI world** — The Verge AI. Vergecast podcast episode, no news value.
- **The Good, the Bad and the Ugly in Cybersecurity – Week 19** — SentinelOne Labs. Weekly roundup; PCPJack (item 28) and Ivanti zero-day (item 18) covered individually.
- **Cyberattack Hits Canvas System Used by Thousands of Schools as Finals Loom** — SecurityWeek. Duplicate of The Record's Canvas item (item 5); The Record has more detail.
- **One Missed Threat Per Week: What 25M Alerts Reveal About Low-Severity Risk** — The Hacker News. Vendor analysis report with marketing angle.
- **Ransomware Group Takes Credit for Trellix Hack** — SecurityWeek. Duplicate of BleepingComputer Trellix item (item 15).
- **Ivanti Patches EPMM Zero-Day Exploited in Targeted Attacks** — SecurityWeek. Duplicate of BleepingComputer Ivanti item (item 18).
- **Linux Kernel Dirty Frag LPE Exploit Enables Root Access Across Major Distributions** — The Hacker News. Duplicate of BleepingComputer Dirty Frag item (item 31).
- **The fax machine is the bottleneck in US healthcare, and VCs are starting to notice** — TechCrunch AI. AI/healthcare VC investment piece, no security angle.
