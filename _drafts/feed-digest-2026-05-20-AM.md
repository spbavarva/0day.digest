# Digest — 2026-05-20 AM

- Window: last 14h
- Raw items considered: 35
- Relevant: 12
- Skippable: 23

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** GitHub Confirms 3,800 Internal Repos Breached via Malicious VS Code Extension — `2026-05-20-github-teampcp-breach-vscode-extension.md`
- [x] **[CRITICAL]** Max-Severity RCE in ChromaDB Allows Unauthenticated Server Hijacking — `2026-05-19-chromadb-rce-ai-apps.md`
- [x] **[HIGH]** Grafana Labs Source Code Exposed via GitHub Breach Linked to TanStack npm Attack — `2026-05-20-grafana-github-breach-tanstack-npm.md`
- [x] **[HIGH]** Windows Zero-Day Barrage: YellowKey, GreenPlasma, and MiniPlasma Disclosed Post-Patch Tuesday — `2026-05-19-windows-zero-days-yellowkey-greenplasma.md`
- [x] **[HIGH]** Unit 42: TamperedChef Clusters Deliver Stealthy Payloads via Trojanized Productivity Apps — `2026-05-20-unit42-tamperedchef-trojanized-apps.md`
- [x] **[HIGH]** Microsoft Disrupts Malware-Signing-as-a-Service Operation Abusing Artifact Signing — `2026-05-19-microsoft-disrupts-malware-signing-service.md`
- [x] **[HIGH]** ExifTool CVE-2026-3102: Malicious Image File Triggers macOS Compromise — `2026-05-20-exiftool-cve-2026-3102-macos.md`
- [x] **[MEDIUM]** Verizon DBIR 2026: Vulnerability Exploitation Surpasses Credential Theft as Top Breach Vector — `2026-05-20-verizon-dbir-2026-vuln-exploitation.md`
- [x] **[MEDIUM]** Google Releases Gemini 3.5 Flash to General Availability at I/O 2026 — `2026-05-19-gemini-35-flash-ga.md`
- [x] **[MEDIUM]** AWS CIRT: Attackers Are Removing Accounts from AWS Organizations to Disable Guardrails — `2026-05-19-aws-cirt-unauthorized-account-removal.md`
- [x] **[MEDIUM]** Flashpoint Monthly AI Threat Report: How Threat Actors Weaponize AI in Illicit Communities — `2026-05-19-flashpoint-ai-threat-report.md`
- [x] **[INFORMATIONAL]** Discord Enables End-to-End Encryption by Default for All Voice and Video Calls — `2026-05-19-discord-e2ee-voice-video.md`

## Relevant (details)

### 1. GitHub Confirms 3,800 Internal Repos Breached via Malicious VS Code Extension
- **Source:** SecurityWeek — https://www.securityweek.com/github-confirms-hack-impacting-3800-internal-repositories/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `malware`, `data-breach`
- **Slug:** `2026-05-20-github-teampcp-breach-vscode-extension`
- **Must-know:** yes
- **Summary:** The TeamPCP threat actor compromised ~3,800 GitHub internal repositories after a GitHub employee installed a malicious VS Code extension. Exfiltrated source code was listed for sale on a cybercrime forum; no customer data outside GitHub's internal systems appears affected. A supply-chain attack on a privileged developer workstation at the world's largest code hosting platform.

### 2. Max-Severity RCE in ChromaDB Allows Unauthenticated Server Hijacking
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/max-severity-flaw-in-chromadb-for-ai-apps-allows-server-hijacking/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `rce`, `llm`, `appsec`
- **Slug:** `2026-05-19-chromadb-rce-ai-apps`
- **Must-know:** no
- **Summary:** A maximum-severity vulnerability in ChromaDB's Python FastAPI version allows unauthenticated attackers to execute arbitrary code on exposed servers. ChromaDB is a widely used vector database for LLM applications, making this a critical risk for AI infrastructure operators.

### 3. Grafana Labs Source Code Exposed via GitHub Breach Linked to TanStack npm Attack
- **Source:** The Hacker News — https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `github`, `data-breach`, `grafana`, `npm`
- **Slug:** `2026-05-20-grafana-github-breach-tanstack-npm`
- **Must-know:** no
- **Summary:** Grafana Labs' GitHub environment was breached, exposing public and private source code via a TanStack npm attack. No customer production systems were affected, but the incident appears linked to the same broad GitHub-targeting wave as the TeamPCP campaign.

### 4. Windows Zero-Day Barrage: YellowKey, GreenPlasma, and MiniPlasma Disclosed Post-Patch Tuesday
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/windows-zero-day-barrage-continues-after-patch-tuesday
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `cve`, `microsoft`
- **Slug:** `2026-05-19-windows-zero-days-yellowkey-greenplasma`
- **Must-know:** no
- **Summary:** A security researcher disclosed three new Windows zero-days — YellowKey (CVE-2026-45585, CVSS 6.8, BitLocker bypass), GreenPlasma, and MiniPlasma — continuing a six-week disclosure campaign. Microsoft has issued a mitigation for YellowKey; patches for the other two are pending.

### 5. Unit 42: TamperedChef Clusters Deliver Stealthy Payloads via Trojanized Productivity Apps
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/tracking-tampered-chef-clusters/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `malware`, `supply-chain`, `phishing`
- **Slug:** `2026-05-20-unit42-tamperedchef-trojanized-apps`
- **Must-know:** no
- **Summary:** Unit 42 details TamperedChef, a threat cluster using trojanized productivity apps and malvertising to deliver stealthy payloads. The group's certificate and code reuse patterns allow attribution across rebranded campaigns. Includes IOCs and certificate fingerprints for detection.

### 6. Microsoft Disrupts Malware-Signing-as-a-Service Operation Abusing Artifact Signing
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cybercrime-service-disrupted-for-abusing-microsoft-platform-to-sign-malware/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `ransomware`, `microsoft`, `supply-chain`
- **Slug:** `2026-05-19-microsoft-disrupts-malware-signing-service`
- **Must-know:** no
- **Summary:** Microsoft took down a cybercrime service that abused Microsoft Artifact Signing to generate fraudulent code-signing certificates for ransomware gangs and other threat actors. The disruption undermines a service that allowed malicious payloads to bypass signature-based security controls.

### 7. ExifTool CVE-2026-3102: Malicious Image File Triggers macOS Compromise
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/exiftool-compromise-mac/119866/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `rce`, `macos`
- **Slug:** `2026-05-20-exiftool-cve-2026-3102-macos`
- **Must-know:** no
- **Summary:** Kaspersky GReAT analyzes CVE-2026-3102, a flaw in ExifTool enabling macOS compromise via a malicious image file. Particularly dangerous in automated media processing pipelines (CMS, CI/CD, upload systems). Patch immediately; restrict untrusted image input.

### 8. Verizon DBIR 2026: Vulnerability Exploitation Surpasses Credential Theft as Top Breach Vector
- **Source:** SecurityWeek — https://www.securityweek.com/verizon-dbir-2026-vulnerability-exploitation-overtakes-credential-theft-as-top-breach-vector/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `data-breach`, `ransomware`
- **Slug:** `2026-05-20-verizon-dbir-2026-vuln-exploitation`
- **Must-know:** no
- **Summary:** Verizon's 2026 DBIR documents vulnerability exploitation overtaking credential theft as the leading breach vector, accelerated by AI-assisted attacks and slow enterprise patching. Ransomware and third-party compromise continue rising. A key data point for reshaping security investment priorities.

### 9. Google Releases Gemini 3.5 Flash to General Availability at I/O 2026
- **Source:** Simon Willison — https://simonwillison.net/2026/May/19/gemini-35-flash/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-launch`, `model-release`, `google`
- **Slug:** `2026-05-19-gemini-35-flash-ga`
- **Must-know:** no
- **Summary:** Google shipped Gemini 3.5 Flash directly to GA at I/O 2026, integrating it across Gemini app, Google Search, Gemini API, and enterprise products. More expensive than prior Flash variants, but positioned as Google's production AI backbone across billions of users.

### 10. AWS CIRT: Attackers Are Removing Accounts from AWS Organizations to Disable Guardrails
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/cirt-insights-how-to-help-prevent-unauthorized-account-removals-from-aws-organizations/
- **Section:** Cloud Security & Infrastructure
- **Severity:** medium
- **Tags:** `aws`, `iam`, `cloud-security`
- **Slug:** `2026-05-19-aws-cirt-unauthorized-account-removal`
- **Must-know:** no
- **Summary:** AWS CIRT documents a trending tactic where attackers remove member accounts from AWS Organizations to disable SCPs and centralized logging. The post details vulnerable configurations and architectural mitigations drawn from live incidents. Highly actionable for multi-account AWS environments.

### 11. Flashpoint Monthly AI Threat Report: How Threat Actors Weaponize AI in Illicit Communities
- **Source:** Flashpoint — https://flashpoint.io/blog/ai-threat-report-monthly/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`, `malware`
- **Slug:** `2026-05-19-flashpoint-ai-threat-report`
- **Must-know:** no
- **Summary:** Flashpoint's monthly report analyzes AI adoption by threat actors in illicit forums and marketplaces, including AI-generated phishing kits, jailbreaks, and automated fraud tooling. Useful standing reference for teams tracking the AI-crime intersection.

### 12. Discord Enables End-to-End Encryption by Default for All Voice and Video Calls
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/discord-rolls-out-end-to-end-encryption-on-voice-video-calls/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `appsec`
- **Slug:** `2026-05-19-discord-e2ee-voice-video`
- **Must-know:** no
- **Summary:** Discord rolled out default E2EE for all voice and video calls, requiring no user action. A meaningful security upgrade for a platform heavily used by security and developer communities.

## Skippable

- **Real-World ICS Security Tales From the Trenches** — SecurityWeek. Opinion/experience piece with no hard news value.
- **Virtual Event Today: Threat Detection & Incident Response Summit** — SecurityWeek. Marketing content promoting a vendor event.
- **Microsoft Releases Mitigation for YellowKey BitLocker Bypass CVE-2026-45585 Exploit** — The Hacker News. Narrower duplicate of item 4 (Dark Reading covers YellowKey plus GreenPlasma/MiniPlasma).
- **Microsoft shares mitigation for YellowKey Windows zero-day** — BleepingComputer. Duplicate of above; item 4 chosen as best source for broader Windows zero-day story.
- **Interpol's 'Operation Ramz' Pioneers Cross-Region Collabs in Middle East** — Dark Reading. Law enforcement news without technical substance or IOCs.
- **GitHub investigates internal repositories breach claimed by TeamPCP** — BleepingComputer. Earlier investigation-stage reporting; item 1 (SecurityWeek confirmed) chosen as best source.
- **GitHub Breached — Employee Device Hack Led to Exfiltration of 3,800+ Internal Repos** — The Hacker News. Duplicate of GitHub breach story; item 1 chosen as best source.
- **The next phase of OpenAI's Education for Countries** — OpenAI Blog. Education partnership expansion with no security angle.
- **llm-gemini 0.32** — Simon Willison. Minor library release; covered by the Gemini 3.5 Flash GA story.
- **What Will Make AI BOMs Real?** — Dark Reading. Opinion piece without breaking news.
- **Demis Hassabis said this might be the 'foothills of the singularity'** — The Verge. Commentary on Google I/O keynote; no news value.
- **Verizon DBIR: Enterprises Face a Dangerous Vulnerability Glut** — Dark Reading. Duplicate DBIR coverage; SecurityWeek item 8 chosen as best source.
- **Google just declared itself a contender in AI design at IO 2026** — TechCrunch AI. Product design tool launch with no security angle.
- **You can now talk to your Gmail inbox, as seen at Google IO 2026** — TechCrunch AI. Consumer product feature; no security angle.
- **The future of Google is a search box that does everything** — The Verge. Opinion/analysis of Google I/O; no news value.
- **How to use Google's new AI agents to go beyond your standard searches** — TechCrunch AI. Product tutorial; no security angle.
- **From teen hacker to Iron Dome researcher, this founder raised $28M to fight AI phishing** — TechCrunch AI. VC funding announcement; not technical news.
- **Google's AI future demands trust — and your personal data** — The Verge. Opinion/analysis of Google I/O data practices; no breaking news.
- **datasette-llm-accountant 0.1a4** — Simon Willison. Minor alpha library bugfix release.
- **llm-gemini 0.32a0** — Simon Willison. Alpha precursor to item 15; minor library release.
- **Introducing OpenAI for Singapore** — OpenAI Blog. Government partnership announcement with no technical or security content.
- **datasette-llm 0.1a8** — Simon Willison. Minor library bugfix release.
- **Gemini 3.5 Flash: more expensive, but Google plan to use it for everything** — Simon Willison. Selected as item 9 (best source for Gemini 3.5 Flash); this duplicate entry is the same URL, counted once.
