# Digest — 2026-05-18 PM

- Window: last 14h
- Raw items considered: 28
- Relevant: 13
- Skippable: 15

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Grafana Source Code Stolen via Compromised GitHub Access Token — `2026-05-18-grafana-codebase-stolen-github-token.md`
- [x] **[HIGH]** Leaked Shai-Hulud Malware Fuels New npm Infostealer Campaign — `2026-05-18-shai-hulud-npm-infostealer-campaign.md`
- [x] **[HIGH]** Triple Supply Chain Strike: npm, PyPI, and Docker Hub Targeted in 48-Hour Window — `2026-05-18-developer-workstations-supply-chain-npm-pypi.md`
- [x] **[HIGH]** SHub Reaper macOS Stealer Bypasses Apple Mitigations, Plants Persistent Backdoor — `2026-05-18-shub-reaper-macos-stealer.md`
- [x] **[HIGH]** OpenClaw 'Claw Chain': Four Flaws Chained for Sandbox Escape and Backdoor Delivery — `2026-05-18-openclaw-claw-chain-sandbox-escape.md`
- [x] **[HIGH]** Critical Patches: Ivanti CVSS 9.6 RCE, Plus Fortinet, SAP, VMware, n8n Fixes — `2026-05-18-ivanti-fortinet-sap-vmware-rce-patches.md`
- [x] **[HIGH]** 7-Eleven Confirms Data Breach After ShinyHunters Claims 600K Salesforce Records Stolen — `2026-05-18-7-eleven-breach-shinyhunters-600k-records.md`
- [x] **[HIGH]** Multiple US Healthcare Data Breaches Added to HHS Tracker, Millions Affected — `2026-05-18-us-healthcare-data-breaches-millions.md`
- [x] **[HIGH]** Iran Expands Cyber Offensive to Internet-Exposed Fuel Tank Gauges — `2026-05-18-iran-atg-fuel-tank-cyber-offensive.md`
- [x] **[MEDIUM]** OpenAI ChatGPT Financial Account Integration Raises Privacy and Security Alarms — `2026-05-18-ai-financial-account-access-chatgpt.md`
- [x] **[MEDIUM]** Red Team Case Study: Social Engineering to Tunneling Attacks Against a Government AI Chatbot — `2026-05-18-red-teaming-government-education-ai.md`
- [x] **[MEDIUM]** Q1 2026 Mobile Threat Report: New SparkCat and Triada Variants Active — `2026-05-18-q1-2026-mobile-threats-sparkcat-triada.md`
- [x] **[INFORMATIONAL]** OpenAI and Dell Partner to Deploy Codex AI Coding Agents On-Premise — `2026-05-18-openai-dell-codex-enterprise-on-premise.md`

## Relevant (details)

### 1. Grafana Source Code Stolen via Compromised GitHub Access Token
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/grafana-says-stolen-github-token-let-hackers-steal-codebase/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `data-breach`
- **Slug:** `2026-05-18-grafana-codebase-stolen-github-token`
- **Must-know:** yes
- **Summary:** Grafana Labs confirmed hackers exfiltrated its source code using a stolen GitHub access token. The company declined to pay the ransom and went public; source code exposure from a widely-deployed monitoring platform creates downstream supply chain risk.

### 2. Leaked Shai-Hulud Malware Fuels New npm Infostealer Campaign
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/leaked-shai-hulud-malware-fuels-new-npm-infostealer-campaign/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `malware`
- **Slug:** `2026-05-18-shai-hulud-npm-infostealer-campaign`
- **Must-know:** no
- **Summary:** The Shai-Hulud infostealer source code, which leaked last week, has been repackaged into malicious npm packages targeting developer credentials. This demonstrates the rapid weaponization cycle from leaked malware to active supply chain attack.

### 3. Triple Supply Chain Strike: npm, PyPI, and Docker Hub Targeted in 48-Hour Window
- **Source:** The Hacker News — https://thehackernews.com/2026/05/developer-workstations-are-now-part-of.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `pypi`, `devsecops`, `malware`
- **Slug:** `2026-05-18-developer-workstations-supply-chain-npm-pypi`
- **Must-know:** no
- **Summary:** Three coordinated campaigns hit npm, PyPI, and Docker Hub within 48 hours, all targeting API keys, cloud credentials, SSH keys, and tokens from developer workstations and CI/CD pipelines. Developer access is now explicitly the primary target in supply chain operations.

### 4. SHub Reaper macOS Stealer Bypasses Apple Mitigations, Plants Persistent Backdoor
- **Source:** SentinelOne Labs — https://www.sentinelone.com/blog/shub-reaper-macos-stealer-spoofs-apple-google-and-microsoft-in-a-single-attack-chain/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `malware`, `phishing`, `appsec`, `macos`
- **Slug:** `2026-05-18-shub-reaper-macos-stealer`
- **Must-know:** no
- **Summary:** SHub Reaper is a macOS infostealer that impersonates Apple, Google, and Microsoft simultaneously in one attack chain, bypasses Terminal mitigations, steals credentials, and installs a persistent backdoor. New research from SentinelOne with full kill chain detail.

### 5. OpenClaw 'Claw Chain': Four Flaws Chained for Sandbox Escape and Backdoor Delivery
- **Source:** SecurityWeek — https://www.securityweek.com/claw-chain-openclaw-flaws-allow-sandbox-escape-backdoor-delivery/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`, `rce`
- **Slug:** `2026-05-18-openclaw-claw-chain-sandbox-escape`
- **Must-know:** no
- **Summary:** Researchers chained four OpenClaw vulnerabilities to achieve credential theft, sandbox escape, and persistent backdoor delivery. Patches are available and should be applied immediately, especially in deployments adjacent to sensitive infrastructure.

### 6. Critical Patches: Ivanti CVSS 9.6 RCE, Plus Fortinet, SAP, VMware, n8n Fixes
- **Source:** The Hacker News — https://thehackernews.com/2026/05/ivanti-fortinet-sap-vmware-n8n-patch.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `rce`, `sqli`, `privilege-escalation`, `cve`
- **Slug:** `2026-05-18-ivanti-fortinet-sap-vmware-rce-patches`
- **Must-know:** no
- **Summary:** Five enterprise vendors released patches in a coordinated disclosure. Top priority is CVE-2026-8043 in Ivanti Xtraction (CVSS 9.6). Fortinet, SAP, VMware, and n8n also fixed auth bypass, SQLi, RCE, and privilege escalation flaws.

### 7. 7-Eleven Confirms Data Breach After ShinyHunters Claims 600K Salesforce Records Stolen
- **Source:** SecurityWeek — https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `ransomware`
- **Slug:** `2026-05-18-7-eleven-breach-shinyhunters-600k-records`
- **Must-know:** no
- **Summary:** 7-Eleven confirmed a breach after ShinyHunters demanded a ransom and claimed to have stolen 600,000+ Salesforce records with personal and corporate data. Full scope and notification status not yet disclosed.

### 8. Multiple US Healthcare Data Breaches Added to HHS Tracker, Millions Affected
- **Source:** SecurityWeek — https://www.securityweek.com/millions-impacted-across-several-us-healthcare-data-breaches/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `healthcare`
- **Slug:** `2026-05-18-us-healthcare-data-breaches-millions`
- **Must-know:** no
- **Summary:** Several new healthcare data breach disclosures have been added to the HHS portal, collectively impacting hundreds of thousands to millions of US patients across hospital networks and healthcare service providers.

### 9. Iran Expands Cyber Offensive to Internet-Exposed Fuel Tank Gauges
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/fuel-tank-breaches-expand-scope-irans-cyber-offensive
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `critical-infrastructure`
- **Slug:** `2026-05-18-iran-atg-fuel-tank-cyber-offensive`
- **Must-know:** no
- **Summary:** Iranian threat actors have expanded OT/ICS targeting to include internet-exposed automatic tank gauge (ATG) systems at fuel facilities. ATG tampering can trigger false alarms, forced shutdowns, or physical overflow incidents.

### 10. OpenAI ChatGPT Financial Account Integration Raises Privacy and Security Alarms
- **Source:** The Record (Recorded Future) — https://therecord.media/experts-warn-of-privacy-cyer-risks-ai-finance
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `llm`, `openai`, `ai-safety`
- **Slug:** `2026-05-18-ai-financial-account-access-chatgpt`
- **Must-know:** no
- **Summary:** OpenAI is rolling out ChatGPT financial account linking for personal finance advice. Security researchers warn of centralized financial data exposure risk and unanswered questions around data retention and training use.

### 11. Red Team Case Study: Social Engineering to Tunneling Attacks Against a Government AI Chatbot
- **Source:** SentinelOne Labs — https://www.sentinelone.com/blog/red-teaming-a-government-edubot/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `llm`, `ai-safety`, `appsec`
- **Slug:** `2026-05-18-red-teaming-government-education-ai`
- **Must-know:** no
- **Summary:** SentinelOne red-teamed a government education AI chatbot, escalating from social engineering to tunneling attacks. Key finding: AI content-layer defenses don't protect the underlying infrastructure, which remains vulnerable to traditional techniques.

### 12. Q1 2026 Mobile Threat Report: New SparkCat and Triada Variants Active
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/malware-report-q1-2026-mobile-statistics/119819/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `malware`, `vulnerability`, `mobile-security`
- **Slug:** `2026-05-18-q1-2026-mobile-threats-sparkcat-triada`
- **Must-know:** no
- **Summary:** Kaspersky Q1 2026 mobile stats highlight new SparkCat variants (OCR-based crypto wallet stealer) and updated Triada Android banking trojan variants. Both families show continued active development.

### 13. OpenAI and Dell Partner to Deploy Codex AI Coding Agents On-Premise
- **Source:** OpenAI Blog — https://openai.com/index/dell-codex-enterprise-partnership
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `openai`, `ai-launch`, `llm`
- **Slug:** `2026-05-18-openai-dell-codex-enterprise-on-premise`
- **Must-know:** no
- **Summary:** OpenAI and Dell partnered to bring Codex AI coding agents to hybrid and on-premise enterprise environments, enabling AI-assisted development for organizations with data residency or compliance constraints on cloud AI services.

## Skippable

- **Grafana refuses to pay ransom after codebase theft** — The Record. Duplicate of BleepingComputer item #15 which has better technical detail (stolen GitHub token vector); BleepingComputer version selected.
- **Elon Musk loses his case against Sam Altman** — The Verge AI. Legal verdict with no security or AI technology angle; statute-of-limitations ruling.
- **Elon Musk has lost his lawsuit against Sam Altman and OpenAI** — TechCrunch AI. Duplicate coverage of same verdict; skip both.
- **INTERPOL Operation Ramz Disrupts MENA Cybercrime Networks** — The Hacker News. Law enforcement arrest announcement without technical detail, IOCs, or TTPs.
- **Fine-Tuning NVIDIA Cosmos Predict 2.5 with LoRA/DoRA** — Hugging Face Blog. ML fine-tuning tutorial for robot video generation; no security angle.
- **Amazon Alexa Plus can now create AI-generated podcasts** — The Verge AI. Non-security consumer AI feature launch.
- **PaddleOCR 3.5: Running OCR and Document Parsing Tasks** — Hugging Face Blog. OCR library update; no security angle.
- **Amazon's new Alexa+ powered feature can generate podcast episodes** — TechCrunch AI. Duplicate of Alexa AI podcast item above.
- **Glaucous-winged Gull, Brown Pelican, Snowy Egret, Canada Goose** — Simon Willison. Personal birdwatching blog post; not technical content.
- **The Open Agent Leaderboard** — Hugging Face Blog. Generic AI agent benchmarking tool announcement; no summary, no security angle.
- **⚡ Weekly Recap: Exchange 0-Day, npm Worm, Fake AI Repo, Cisco Exploit** — The Hacker News. Roundup article; individual items covered separately in this digest.
- **How to Reduce Phishing Exposure Before It Turns into Business Disruption** — The Hacker News. Sponsored/marketing content disguised as SOC guidance; no news value.
- **IT threat evolution in Q1 2026. Non-mobile statistics** — Securelist. General PC/IoT quarterly stats without specific notable findings; mobile report (item 21) captures the headline malware families.
- **Microsoft testing adjustable taskbar, Start menu in Windows 11** — BleepingComputer. Generic Windows UI feature update; no security angle.
- **South Korea's LetinAR is building optics behind AI glasses** — TechCrunch AI. Hardware optics startup profile; no security angle.
