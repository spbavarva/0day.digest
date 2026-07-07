# Digest — 2026-07-07 AM

- Window: last 14h
- Raw items considered: 21
- Relevant: 11
- Skippable: 10

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[MEDIUM]** UAT-7810 Expands ORB Proxy Network With New Custom Malware — `2026-07-07-uat-7810-orb-network-malware.md`
- [x] **[HIGH]** 16-Year-Old Linux Kernel Flaw Enables VM Escape on Intel and AMD — `2026-07-07-linux-kernel-januscape-vm-escape.md`
- [x] **[HIGH]** China-Aligned Hackers Exploit Roundcube Flaws to Target University Networks — `2026-07-07-roundcube-flaws-china-aligned-hackers-universities.md`
- [x] **[HIGH]** CERT/CC Warns of Hidden Admin Backdoor in Tenda Router Firmware — `2026-07-07-tenda-router-firmware-backdoor.md`
- [x] **[HIGH]** BeyondTrust Patches Critical Pre-Auth Flaws in Remote Support and PRA — `2026-07-07-beyondtrust-critical-auth-bypass-patched.md`
- [x] **[INFORMATIONAL]** Hugging Face Releases LeRobot v0.6.0 for Robotics AI — `2026-07-07-lerobot-v060-release.md`
- [x] **[MEDIUM]** Tencent Releases Hy3, a 295B-Parameter Open-Weight MoE Model — `2026-07-06-tencent-hy3-model-release.md`
- [x] **[MEDIUM]** 'First' AI-Run Ransomware Attack Still Required a Human Operator — `2026-07-06-ai-run-ransomware-attack-human-involvement.md`
- [x] **[HIGH]** 'BusySnake' Infostealer Hits Critical Infrastructure in Russia, Brazil, Kazakhstan — `2026-07-06-busysnake-infostealer-critical-infrastructure.md`
- [x] **[HIGH]** New NetScaler Memory Disclosure Flaw Under Active Attack — `2026-07-06-netscaler-vulnerability-active-exploitation.md`
- [x] **[MEDIUM]** Fake IT Support Calls on Microsoft Teams Deliver EtherRAT Malware — `2026-07-06-fake-it-support-teams-etherrat-malware.md`

## Relevant (details)

### 1. UAT-7810 Expands ORB Proxy Network With New Custom Malware
- **Source:** Cisco Talos — https://blog.talosintelligence.com/uat-7810/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `uat-7810-orb-network-malware`
- **Must-know:** no
- **Summary:** Cisco Talos reports that threat actor UAT-7810 continues developing custom malware to expand its operational relay box (ORB) proxy network. No specific victims or CVEs were disclosed in the summary.

### 2. 16-Year-Old Linux Kernel Flaw Enables VM Escape on Intel and AMD
- **Source:** SecurityWeek — https://www.securityweek.com/linux-kernel-vulnerability-allows-vm-escape-on-intel-and-amd-systems/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`, `privilege-escalation`
- **Slug:** `linux-kernel-januscape-vm-escape`
- **Must-know:** no
- **Summary:** A 16-year-old flaw dubbed "Januscape" in Linux's KVM hypervisor allows a guest VM to escape its boundary and potentially execute code on the host, affecting both Intel and AMD systems. No active exploitation was reported.

### 3. China-Aligned Hackers Exploit Roundcube Flaws to Target University Networks
- **Source:** The Hacker News — https://thehackernews.com/2026/07/suspected-china-aligned-hackers-exploit.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `xss`
- **Slug:** `roundcube-flaws-china-aligned-hackers-universities`
- **Must-know:** no
- **Summary:** A suspected China-aligned threat cluster is exploiting patched Roundcube webmail flaws, including CVE-2024-42009, to steal credentials from US and Canadian university physics and engineering departments. Fixes for the exploited flaws already exist.

### 4. CERT/CC Warns of Hidden Admin Backdoor in Tenda Router Firmware
- **Source:** The Hacker News — https://thehackernews.com/2026/07/certcc-warns-of-hidden-admin-backdoor.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Slug:** `tenda-router-firmware-backdoor`
- **Must-know:** no
- **Summary:** CERT/CC disclosed an undocumented authentication backdoor (CVE-2026-11405) in several Tenda router firmware versions that lets an attacker bypass password verification for admin access. No confirmation of active exploitation was included.

### 5. BeyondTrust Patches Critical Pre-Auth Flaws in Remote Support and PRA
- **Source:** The Hacker News — https://thehackernews.com/2026/07/beyondtrust-patches-critical-auth.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `beyondtrust-critical-auth-bypass-patched`
- **Must-know:** no
- **Summary:** BeyondTrust patched two critical flaws in Remote Support and Privileged Remote Access, including a pre-authentication CVE-2026-40138 (CVSS 9.2) that could let an unauthenticated attacker take control of affected devices. No active exploitation reported at disclosure.

### 6. Hugging Face Releases LeRobot v0.6.0 for Robotics AI
- **Source:** Hugging Face Blog — https://huggingface.co/blog/lerobot-release-v060
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`
- **Slug:** `lerobot-v060-release`
- **Must-know:** no
- **Summary:** Hugging Face shipped LeRobot v0.6.0, the latest version of its open-source robotics learning framework. The source did not provide further capability detail beyond the version release itself.

### 7. Tencent Releases Hy3, a 295B-Parameter Open-Weight MoE Model
- **Source:** Simon Willison — https://simonwillison.net/2026/Jul/6/hy3/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `model-release`, `llm`, `ai-launch`
- **Slug:** `tencent-hy3-model-release`
- **Must-know:** no
- **Summary:** Tencent's Hy Team released Hy3, an Apache 2.0-licensed 295B-parameter (21B active) mixture-of-experts model, following up on its April preview. Tencent says the model rivals larger flagship open-source models on benchmarks after refined post-training.

### 8. 'First' AI-Run Ransomware Attack Still Required a Human Operator
- **Source:** TechCrunch AI — https://techcrunch.com/2026/07/06/the-first-ai-run-ransomware-attack-still-needed-a-human/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ransomware`, `ai-safety`, `llm`
- **Slug:** `ai-run-ransomware-attack-human-involvement`
- **Must-know:** no
- **Summary:** New details on last week's widely reported "first AI-run ransomware attack" show a human still chose the victim, built the attack infrastructure, and supplied stolen credentials, even though an AI agent handled technical execution. The finding tempers claims of a fully autonomous cybercrime debut.

### 9. 'BusySnake' Infostealer Hits Critical Infrastructure in Russia, Brazil, Kazakhstan
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/busysnake-infostealer-critical-infrastructure-networks
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`
- **Slug:** `busysnake-infostealer-critical-infrastructure`
- **Must-know:** no
- **Summary:** A threat group tracked as "Armored Likho" is using the BusySnake infostealer to compromise government agencies and electrical power entities across Russia, Brazil, and Kazakhstan. No IOCs or initial-access vector were included in the available summary.

### 10. New NetScaler Memory Disclosure Flaw Under Active Attack
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/citrixbleed-ing-again-netscaler-vulnerability-under-attack
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`
- **Slug:** `netscaler-vulnerability-active-exploitation`
- **Must-know:** no
- **Summary:** Attackers began exploiting a newly disclosed memory disclosure flaw in Citrix NetScaler almost immediately after researchers published a proof-of-concept, echoing the earlier "CitrixBleed" incident. CVE identifier and patch status were not specified in the source summary.

### 11. Fake IT Support Calls on Microsoft Teams Deliver EtherRAT Malware
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/fake-it-support-calls-on-microsoft-teams-push-etherrat-malware/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `malware`
- **Slug:** `fake-it-support-teams-etherrat-malware`
- **Must-know:** no
- **Summary:** Threat actors are abusing Microsoft Teams voice calls, impersonating corporate IT support, to trick employees into installing EtherRAT malware and gain initial network access. The technique mirrors known "helpdesk vishing" tactics used by other groups.

## Skippable

- **Threat landscape for industrial automation systems, Q1 2026** — Securelist. Generic quarterly threat statistics report, no single incident or novel technique.
- **Microsoft to enable Windows settings backup by default for orgs** — BleepingComputer. Generic enterprise IT feature rollout, no security angle.
- **Keyfactor Scores $1 Billion+ Investment for AI, Post-Quantum Security** — SecurityWeek. Funding/investment news, marketing content.
- **The first American autonomous ground vehicles are fighting in Ukraine** — TechCrunch AI. Military hardware deployment news, no AI safety/security substance; summary too thin to draft safely.
- **BeyondTrust warns of critical flaws in remote access software** — BleepingComputer. Duplicate coverage of the same BeyondTrust story; The Hacker News version has more technical detail (CVE, CVSS).
- **Microsoft testing new Cloud Rebuild Windows 11 recovery feature** — BleepingComputer. Generic OS feature testing, no security angle.
- **US investors will soon get access to SK Hynix** — TechCrunch AI. IPO/market news, no security or technical AI substance.
- **Canadian spy agency reports hacking three criminal groups in 2025** — The Record. Retrospective policy disclosure, no new technical detail or IOCs.
- **Attackers vote themselves $20 million in BONK cryptocurrency** — The Record. Niche DeFi/crypto governance exploit, out of scope, thin sourcing (social media claim only).
- **Phishing poses as big-brand job interview to steal Google accounts** — BleepingComputer. Established fake-interview phishing tactic, no novel technique.
