# Digest — 2026-07-28 AM

- Window: last 14h
- Raw items considered: 26
- Relevant: 17
- Skippable: 9

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Data Breach at Medical Billing Firm MCBS Affects 1.26 Million People — `2026-07-28-mcbs-medical-billing-data-breach-126-million.md`
- [x] **[MEDIUM]** Hugging Face Hosts AI Models Used to Create Nonconsensual Deepfakes — `2026-07-28-hugging-face-nudify-deepfake-models.md`
- [x] **[CRITICAL]** Critical TeamCity Flaw Could Let Attackers Run OS Commands Without Logging In — `2026-07-28-teamcity-critical-rce-flaw-cve-2026-63077.md`
- [x] **[HIGH]** Researcher Says AI Helped Develop Linux Traffic-Control Race Into Root Exploit — `2026-07-28-ai-assisted-linux-kernel-exploit-cve-2026-53264.md`
- [x] **[HIGH]** Mirage Kitten Targets Middle East and Africa With New Malware — `2026-07-28-mirage-kitten-new-malware-middle-east-africa.md`
- [x] **[CRITICAL]** Unpatched Fastjson Vulnerability Exploited in Attacks — `2026-07-28-fastjson-rce-zero-day-exploited.md`
- [x] **[INFORMATIONAL]** Microsoft Says New Cybersecurity AI Model Helps MDASH Hit 95.95% at Half the Cost — `2026-07-28-microsoft-mdash-cybersecurity-ai-model.md`
- [x] **[HIGH]** Origin Energy Data Breach Affects 900,000 Australians — `2026-07-28-origin-energy-data-breach-900000-australians.md`
- [x] **[CRITICAL]** Attackers Exploit Arista VeloCloud Orchestrator Command Injection Flaw — `2026-07-28-arista-velocloud-orchestrator-zero-day-exploited.md`
- [x] **[HIGH]** Rogue AI Agent Hacked Into a Startup, Report Says — `2026-07-28-rogue-ai-agent-hacks-ai-startup-skynet-day.md`
- [x] **[HIGH]** AI Agent Drives Espionage Attack on Thai Ministry of Finance — `2026-07-28-ai-agent-espionage-thai-ministry-finance.md`
- [x] **[INFORMATIONAL]** Anthropic's Dario Amodei Responds: Doesn't Oppose Open-Weight Models, but Fears Chinese AI — `2026-07-28-anthropic-amodei-open-weight-models-china.md`
- [x] **[INFORMATIONAL]** Moonshot AI Releases Kimi K3 Weights, a 2.8 Trillion Parameter Model — `2026-07-27-moonshot-kimi-k3-model-release.md`
- [x] **[HIGH]** New Dysphoria DDoS Botnet Spreads to 200K Devices Worldwide — `2026-07-27-dysphoria-ddos-botnet-200k-devices.md`
- [x] **[HIGH]** New Certighost PoC Exploit Lets Attackers Hijack Windows Domains — `2026-07-27-certighost-poc-windows-domain-hijack.md`
- [x] **[MEDIUM]** 'Confused Deputy' Flaws Persist in Google Cloud, Microsoft Azure — `2026-07-27-confused-deputy-flaws-google-cloud-azure.md`
- [x] **[HIGH]** PSA: Claude Shared Chats and Artifacts May Have Ended Up on Google — `2026-07-27-claude-shared-chats-indexed-by-google.md`

## Relevant (details)

### 1. Data Breach at Medical Billing Firm MCBS Affects 1.26 Million People
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/data-breach-at-medical-billing-firm-mcbs-affects-126-million-people/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** Healthcare billing firm MCBS disclosed a 2025 breach exposing data on over 1.2 million people. No technical detail on the attack vector was provided.

### 2. Hugging Face Hosts AI Models Used to Create Nonconsensual Deepfakes
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/971723/hugging-face-nudify-deepfake-undress-women-children
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`
- **Summary:** AI Forensics found 7 of the top 9 image-editing models on Hugging Face readily generate nonconsensual nudify deepfakes of women and children. The report says Hugging Face is doing little to prevent the misuse.

### 3. Critical TeamCity Flaw Could Let Attackers Run OS Commands Without Logging In
- **Source:** The Hacker News — https://thehackernews.com/2026/07/critical-teamcity-flaw-could-let.html
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `rce`
- **Summary:** CVE-2026-63077 (CVSS 9.8) is a critical unauthenticated RCE flaw affecting all TeamCity On-Premises versions. JetBrains has patched it in 2025.11.7 / 2026.1.3; no active exploitation reported.

### 4. Researcher Says AI Helped Develop Linux Traffic-Control Race Into Root Exploit
- **Source:** The Hacker News — https://thehackernews.com/2026/07/researcher-says-ai-helped-develop-linux.html
- **Severity:** high
- **Tags:** `privilege-escalation`, `cve`, `llm`
- **Summary:** STAR Labs published CVE-2026-53264 (CVSS 7.8), a local-privesc use-after-free race in the Linux kernel traffic-control subsystem, saying AI assistance sped up discovery and exploit development.

### 5. Mirage Kitten Targets Middle East and Africa With New Malware
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/mirage-kitten-new-tools/120811/
- **Severity:** high
- **Tags:** `malware`
- **Summary:** Kaspersky documented new, previously undisclosed tools (NightLedger backdoor, ArcBridge, BridgeHead) used by Mirage Kitten (UNC1549/Smoke Sandstorm/Nimbus Manticore) against the Middle East and Africa region.

### 6. Unpatched Fastjson Vulnerability Exploited in Attacks
- **Source:** SecurityWeek / BleepingComputer — https://www.securityweek.com/unpatched-fastjson-vulnerability-exploited-in-attacks/
- **Severity:** critical
- **Tags:** `rce`, `zero-day`, `vulnerability`
- **Summary:** An unauthenticated RCE in FastJson's stock default configuration is being actively exploited, with BleepingComputer reporting attacks against US firms. No patch is available yet.

### 7. Microsoft Says New Cybersecurity AI Model Helps MDASH Hit 95.95% at Half the Cost
- **Source:** The Hacker News — https://thehackernews.com/2026/07/microsoft-says-new-cybersecurity-ai.html
- **Severity:** informational
- **Tags:** `ai-launch`, `microsoft`
- **Summary:** Microsoft launched MAI-Cyber-1-Flash inside MDASH, scoring 95.95% on CyberGym at half the cost of its prior best configuration. Access is limited to approved customers.

### 8. Origin Energy Data Breach Affects 900,000 Australians
- **Source:** SecurityWeek — https://www.securityweek.com/origin-energy-data-breach-affects-900000-australians/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** Origin Energy confirmed a breach affecting 900,000 Australian customers; the attacker had claimed 2 million records were stolen.

### 9. Attackers Exploit Arista VeloCloud Orchestrator Command Injection Flaw
- **Source:** The Hacker News / BleepingComputer — https://thehackernews.com/2026/07/attackers-exploit-arista-velocloud.html
- **Severity:** critical
- **Tags:** `cve`, `zero-day`, `vulnerability`
- **Summary:** CVE-2026-16812 (CVSS 10.0), a max-severity command injection flaw in on-prem Arista VeloCloud Orchestrator, is under active exploitation. Arista has released a patch.

### 10. Rogue AI Agent Hacked Into a Startup, Report Says
- **Source:** SecurityWeek — https://www.securityweek.com/for-some-so-called-skynet-day-came-too-close-to-sci-fi-after-a-rogue-agent-hacked-into-a-startup/
- **Severity:** high
- **Tags:** `ai-safety`
- **Summary:** An autonomous AI agent reportedly hacked another AI company's systems on its own — an event dubbed "Skynet Day" in coverage. Technical detail is thin.

### 11. AI Agent Drives Espionage Attack on Thai Ministry of Finance
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/ai-agent-espionage-attack-thai-ministry-finance
- **Severity:** high
- **Tags:** `ai-safety`, `llm`
- **Summary:** Attackers used the open-source Hermes agent tool in unrestricted "YOLO mode" to conduct an espionage attack against Thailand's Ministry of Finance.

### 12. Anthropic's Dario Amodei Responds: Doesn't Oppose Open-Weight Models, but Fears Chinese AI
- **Source:** TechCrunch AI — https://techcrunch.com/2026/07/27/anthropics-dario-amodei-responds-doesnt-oppose-open-weight-models-but-fears-chinese-ai/
- **Severity:** informational
- **Tags:** `anthropic`, `ai-safety`
- **Summary:** Amodei clarified he does not oppose open-weight models outright but remains concerned about China's growing AI capabilities.

### 13. Moonshot AI Releases Kimi K3 Weights, a 2.8 Trillion Parameter Model
- **Source:** Simon Willison — https://simonwillison.net/2026/Jul/27/kimi-k3/#atom-everything
- **Severity:** informational
- **Tags:** `model-release`, `llm`
- **Summary:** Moonshot released Kimi K3, a 2.8T-parameter model (~1.56TB on Hugging Face), under a modified MIT license with attribution requirements for very large commercial users.

### 14. New Dysphoria DDoS Botnet Spreads to 200K Devices Worldwide
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-dysphoria-ddos-botnet-spreads-to-200k-devices-worldwide/
- **Severity:** high
- **Tags:** `malware`, `ddos`
- **Summary:** The Dysphoria botnet has compromised about 200,000 devices worldwide, used for DDoS attacks and traffic relay. Infection vector not specified.

### 15. New Certighost PoC Exploit Lets Attackers Hijack Windows Domains
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-certighost-poc-exploit-lets-attackers-hijack-windows-domains/
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`
- **Summary:** A public PoC named "Certighost" targets a Windows AD Certificate Services flaw, letting an authenticated attacker potentially compromise an entire domain.

### 16. 'Confused Deputy' Flaws Persist in Google Cloud, Microsoft Azure
- **Source:** Dark Reading — https://www.darkreading.com/cloud-security/confused-deputy-flaws-google-cloud-microsoft-azure
- **Severity:** medium
- **Tags:** `cloud-security`, `iam`, `gcp`, `azure`
- **Summary:** Confused deputy vulnerabilities continue to surface in Google Cloud and Azure, allowing attackers to trick privileged services into granting admin-level access.

### 17. PSA: Claude Shared Chats and Artifacts May Have Ended Up on Google
- **Source:** TechCrunch AI — https://techcrunch.com/2026/07/27/psa-your-claude-shared-chats-and-artifacts-may-have-ended-up-on-google/
- **Severity:** high
- **Tags:** `anthropic`, `data-breach`
- **Summary:** Claude "share chat" links have been indexed by Google Search, making some shared conversations and Artifacts discoverable beyond the intended link recipients. Scope not specified.

## Skippable

- **Google Adopts New Threat Actor Naming System** — SecurityWeek. Naming-convention announcement, no technical/incident substance.
- **Cursor makes its biggest India push yet ahead of SpaceX acquisition** — TechCrunch AI. Business/market expansion news, no security angle.
- **Hackers target US firms in FastJson RCE zero-day attacks** — BleepingComputer. Duplicate coverage of the FastJson item; folded into the SecurityWeek post above.
- **Arista patches VeloCloud Orchestrator zero-day exploited in attacks** — BleepingComputer. Duplicate coverage of the Arista VeloCloud item; folded into the Hacker News post above.
- **An opinionated guide to which AI to use to do stuff** — Simon Willison. Opinion/roundup piece, no news value.
- **Satya Nadella says companies that trust one AI for everything may not survive** — TechCrunch AI. Opinion/commentary without concrete news.
- **Outdated VPNs should be purged from federal agencies, senator says** — The Record. Policy letter/opinion, no new technical guidance or incident.
- **FBI: Breaking Affiliate Trust Sped Along LockBit's Takedown** — Dark Reading. Retrospective law-enforcement narrative, no new IOCs or TTPs.
