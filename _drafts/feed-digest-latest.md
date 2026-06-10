# Digest — 2026-06-09 PM

- Window: last 14h
- Raw items considered: 55
- Relevant: 21
- Skippable: 34

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Check Point VPN Zero-Day Exploited by Qilin Ransomware Affiliates — `2026-06-09-check-point-vpn-zero-day-qilin-ransomware.md`
- [x] **[CRITICAL]** Chrome V8 Zero-Day CVE-2026-11645 Actively Exploited — Patch Now — `2026-06-09-chrome-v8-zero-day-cve-2026-11645.md`
- [x] **[CRITICAL]** LiteLLM CVE-2026-42271 Exploited in the Wild — Unauthenticated RCE Chain — `2026-06-09-litellm-cve-2026-42271-rce-cisa-kev.md`
- [x] **[CRITICAL]** Microsoft GitHub Repos Compromised to Push Password-Stealing Malware (Miasma) — `2026-06-09-microsoft-github-miasma-supply-chain.md`
- [x] **[CRITICAL]** Shai-Hulud / Hades Supply Chain Campaign Hits 100+ npm and PyPI Packages — `2026-06-09-shai-hulud-hades-pypi-supply-chain.md`
- [x] **[CRITICAL]** Veeam Backup & Replication Critical RCE CVE-2026-44963 (CVSS 9.4) — `2026-06-09-veeam-backup-rce-cve-2026-44963.md`
- [x] **[HIGH]** Microsoft June 2026 Patch Tuesday: 200 Flaws, 3 Publicly Disclosed Zero-Days — `2026-06-09-microsoft-june-2026-patch-tuesday-zero-days.md`
- [x] **[HIGH]** Claude Mythos Turns N-Days Into Working Exploits in Hours — `2026-06-09-claude-mythos-ai-exploit-acceleration.md`
- [x] **[HIGH]** Russian APTs Exploit Patched WinRAR Flaw CVE-2025-8088 Against Ukrainian Targets — `2026-06-09-winrar-cve-2025-8088-russian-apt-ukraine.md`
- [x] **[HIGH]** OpenSSL Patches 18 Vulnerabilities, Many Found by AI Tools — `2026-06-09-openssl-high-severity-ai-assisted-patches.md`
- [x] **[HIGH]** SAP Patches Critical Vulnerabilities in NetWeaver and Commerce — `2026-06-09-sap-critical-netweaver-commerce-patches.md`
- [x] **[HIGH]** Researchers Build Self-Replicating AI Worm That Runs Entirely on Local Open-Weight Models — `2026-06-09-self-replicating-ai-worm-local-models.md`
- [x] **[HIGH]** French Government's Encrypted Messaging Platform Tchap Breached via Account Hijacking — `2026-06-09-french-govt-tchap-breach-account-hijacking.md`
- [x] **[MEDIUM]** Anthropic Releases Claude Fable 5: First Mythos-Class Model Available to the Public — `2026-06-09-claude-fable-5-launch-mythos-class.md`
- [x] **[MEDIUM]** FROST: New SSD Timing Side-Channel Lets Websites Track Browser History and Open Apps — `2026-06-09-frost-ssd-timing-side-channel-attack.md`
- [x] **[MEDIUM]** CISA Binding Directive Transforms How Federal Agencies Prioritize Vulnerabilities — `2026-06-09-cisa-binding-directive-vulnerability-assessment.md`
- [x] **[MEDIUM]** SiribClone APT Poses as Women Seeking Romance to Spy on Russian Soldiers — `2026-06-09-honeytrap-hackers-spy-russian-soldiers.md`
- [x] **[INFORMATIONAL]** Apple WWDC 2026: Siri AI Overhaul, iOS 27, and Apple Intelligence Expansion — `2026-06-09-apple-wwdc-2026-siri-ai-apple-intelligence.md`
- [x] **[INFORMATIONAL]** Google DeepMind Launches Gemini 3.5 Live Translate for Real-Time Speech Translation — `2026-06-09-gemini-35-live-translate.md`
- [x] **[INFORMATIONAL]** Google DeepMind Releases Gemma 4 12B: Unified Encoder-Free Multimodal Model — `2026-06-09-gemma-4-12b-multimodal-launch.md`
- [x] **[INFORMATIONAL]** Google Launches AI Threat Defense with Automated Security Operations Agents — `2026-06-09-google-ai-threat-defense-security-operations.md`

## Relevant (details)

### 1. Check Point VPN Zero-Day Exploited by Qilin Ransomware Affiliates
- **Source:** SecurityWeek — https://www.securityweek.com/check-point-vpn-zero-day-exploited-in-qilin-ransomware-attacks/
- **Severity:** critical
- **Tags:** `zero-day`, `ransomware`, `vpn`, `vulnerability`, `cve`
- **Summary:** Authentication bypass zero-day in Check Point Remote Access VPN enables VPN connections without valid credentials. Qilin ransomware affiliates are actively exploiting the flaw; CISA issued an emergency directive giving federal agencies 3 days to patch.

### 2. Chrome V8 Zero-Day CVE-2026-11645 Actively Exploited — Patch Now
- **Source:** The Hacker News — https://thehackernews.com/2026/06/chrome-v8-zero-day-cve-2026-11645.html
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`, `google`, `rce`
- **Summary:** CVE-2026-11645 (CVSS 8.8), OOB read/write in Chrome V8, actively exploited — the fifth Chrome zero-day this year. Patched in Chrome 149.0.7827.103 alongside 73 other vulnerabilities.

### 3. LiteLLM CVE-2026-42271 Exploited in the Wild — Unauthenticated RCE Chain
- **Source:** The Hacker News — https://thehackernews.com/2026/06/litellm-flaw-cve-2026-42271-exploited.html
- **Severity:** critical
- **Tags:** `zero-day`, `rce`, `vulnerability`, `cve`, `llm`, `appsec`
- **Summary:** CISA added CVE-2026-42271 (CVSS 8.7) in BerriAI LiteLLM to the KEV catalog. Command injection chains to unauthenticated RCE in misconfigured deployments of this widely-used LLM proxy layer.

### 4. Microsoft GitHub Repos Compromised to Push Password-Stealing Malware (Miasma)
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/github-disables-microsoft-repos-pushing-password-stealing-malware/
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`, `github`, `microsoft`, `data-breach`
- **Summary:** Infostealer injected into 73 Microsoft GitHub repos across Azure, microsoft, Azure-Samples, and MicrosoftDocs orgs, disrupting CI pipelines. Part of the Miasma campaign; some repos restored, others remain offline pending investigation.

### 5. Shai-Hulud / Hades Supply Chain Campaign Hits 100+ npm and PyPI Packages
- **Source:** SecurityWeek — https://www.securityweek.com/over-100-npm-pypi-packages-hit-in-new-shai-hulud-supply-chain-attacks/
- **Severity:** critical
- **Tags:** `supply-chain`, `pypi`, `npm`, `malware`, `data-breach`
- **Summary:** Shai-Hulud campaign spawned Miasma (npm/GitHub) and Hades (PyPI) waves, compromising 100+ packages. Hades placed 37 malicious wheel artifacts across 19 PyPI packages with a Bun-based credential stealer auto-executing via `.pth` file injection.

### 6. Veeam Backup & Replication Critical RCE CVE-2026-44963 (CVSS 9.4)
- **Source:** The Hacker News — https://thehackernews.com/2026/06/veeam-backup-replication-rce-flaw-lets.html
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`, `cve`, `privilege-escalation`
- **Summary:** CVE-2026-44963 (CVSS 9.4) lets any authenticated domain user execute remote code on Veeam Backup Server. No confirmed active exploitation yet; patches available — Veeam flaws attract ransomware operators rapidly after disclosure.

### 7. Microsoft June 2026 Patch Tuesday: 200 Flaws, 3 Publicly Disclosed Zero-Days
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-june-2026-patch-tuesday-fixes-3-zero-day-200-flaws/
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `microsoft`, `cve`
- **Summary:** June Patch Tuesday fixes 200 vulnerabilities including three publicly disclosed before patches were available. Updates also push refreshed Secure Boot certificates ahead of current cert expiry.

### 8. Claude Mythos Turns N-Days Into Working Exploits in Hours
- **Source:** SecurityWeek — https://www.securityweek.com/claude-mythos-turns-n-days-into-n-hours-with-rapid-exploit-creation/
- **Severity:** high
- **Tags:** `llm`, `anthropic`, `vulnerability`, `appsec`, `ai-safety`
- **Summary:** Research shows Claude Mythos compresses N-day exploit development from days to hours. XBOW confirms Mythos Preview effective across source-code analysis, reverse engineering, and live-site validation. Safeguards-removed public LLMs also produce working exploits.

### 9. Russian APTs Exploit Patched WinRAR Flaw CVE-2025-8088 Against Ukrainian Targets
- **Source:** The Hacker News — https://thehackernews.com/2026/06/winrar-flaw-exploited-by-russia-aligned.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `malware`
- **Summary:** Earth Dahu (Gamaredon) and SHADOW-EARTH-066 (UAC-0226) exploiting CVE-2025-8088 against Ukrainian military and government nearly a year after the July 2025 WinRAR patch shipped.

### 10. OpenSSL Patches 18 Vulnerabilities, Many Found by AI Tools
- **Source:** SecurityWeek — https://www.securityweek.com/openssl-patches-high-severity-vulnerability-found-with-ai/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `llm`, `ai-safety`, `appsec`
- **Summary:** 18 OpenSSL vulnerabilities patched including one high-severity flaw; many reportedly discovered via AI-assisted analysis. Highlights AI's growing role in accelerating vulnerability discovery in foundational cryptographic libraries.

### 11. SAP Patches Critical Vulnerabilities in NetWeaver and Commerce
- **Source:** SecurityWeek — https://www.securityweek.com/sap-patches-critical-netweaver-commerce-vulnerabilities/
- **Severity:** high
- **Tags:** `vulnerability`, `rce`, `cve`
- **Summary:** Critical SAP patches for NetWeaver and Commerce covering sensitive data disclosure, memory corruption, and system disruption. SAP NetWeaver has historically attracted exploitation within days of critical CVE disclosure.

### 12. Researchers Build Self-Replicating AI Worm That Runs Entirely on Local Open-Weight Models
- **Source:** The Hacker News — https://thehackernews.com/2026/06/researchers-build-self-replicating-ai.html
- **Severity:** high
- **Tags:** `malware`, `llm`, `ai-safety`, `vulnerability`
- **Summary:** University of Toronto PoC AI worm uses a local open-weight LLM to autonomously reason through a network, generate tailored attacks per target, and self-replicate — no commercial AI API, no C2. Meaningful capability advance for autonomous lateral movement including in air-gapped environments.

### 13. French Government's Encrypted Messaging Platform Tchap Breached via Account Hijacking
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/french-govt-messaging-service-breached-in-account-hijacking-attack/
- **Severity:** high
- **Tags:** `data-breach`, `phishing`, `iam`
- **Summary:** Attackers used a hijacked account to breach Tchap, France's government encrypted messaging platform used across ministries. E2EE provides no protection against account-level compromise; MFA enforcement is critical.

### 14. Anthropic Releases Claude Fable 5: First Mythos-Class Model Available to the Public
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/09/anthropic-released-claude-fable-5-its-most-powerful-model-publicly-days-after-warning-ai-is-getting-too-dangerous/
- **Severity:** medium
- **Tags:** `ai-launch`, `anthropic`, `model-release`, `llm`, `ai-safety`
- **Summary:** Anthropic released Claude Fable 5, its most powerful broadly-available model with Mythos-class performance in software engineering, knowledge work, and vision. Ships with cybersecurity guardrails; available on Claude.ai, API, and Amazon Bedrock.

### 15. FROST: New SSD Timing Side-Channel Lets Websites Track Browser History and Open Apps
- **Source:** The Hacker News — https://thehackernews.com/2026/06/new-frost-attack-lets-websites-track.html
- **Severity:** medium
- **Tags:** `vulnerability`, `appsec`
- **Summary:** JavaScript-only FROST attack uses SSD I/O contention timing to infer visited sites and open apps — no native code, extension, or permissions required. Passive and hard to detect; requires browser-level mitigation.

### 16. CISA Binding Directive Transforms How Federal Agencies Prioritize Vulnerabilities
- **Source:** The Record (Recorded Future) — https://therecord.media/cisa-to-transform-how-it-assesses-cyber-vulns-risks
- **Severity:** medium
- **Tags:** `vulnerability`, `devsecops`
- **Summary:** New CISA binding operational directive shifts ~100 federal agencies from blanket patching to risk-based vulnerability prioritization, changing how KEV catalog additions translate to mandatory remediation timelines.

### 17. SiribClone APT Poses as Women Seeking Romance to Spy on Russian Soldiers
- **Source:** The Record (Recorded Future) — https://therecord.media/hackers-pose-as-women-seeking-romance-russian-military
- **Severity:** medium
- **Tags:** `phishing`, `malware`
- **Summary:** SiribClone (F6 attribution) has honey-trapped Russian soldiers via romance personas since summer 2025, deploying surveillance malware against military personnel in border regions for intelligence collection.

### 18. Apple WWDC 2026: Siri AI Overhaul, iOS 27, and Apple Intelligence Expansion
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/09/wwdc-2026-everything-announced-on-siri-ai-os-27-apple-intelligence-and-more/
- **Severity:** informational
- **Tags:** `ai-launch`, `apple`, `llm`
- **Summary:** WWDC 2026 centered on rebuilt Siri AI, iOS 27, and generative AI photo editing under Apple Intelligence, using Private Cloud Compute for privacy. Largely a catch-up play; AI photo editing raises deepfake concerns at consumer scale.

### 19. Google DeepMind Launches Gemini 3.5 Live Translate for Real-Time Speech Translation
- **Source:** Google DeepMind — https://deepmind.google/blog/fluid-natural-voice-translation-with-gemini-35-live-translate/
- **Severity:** informational
- **Tags:** `ai-launch`, `google`, `model-release`, `llm`
- **Summary:** Near-real-time speech translation with voice preservation rolling out to Google AI Studio, Google Translate, and Google Meet. First production consumer deployment of Gemini 3.5.

### 20. Google DeepMind Releases Gemma 4 12B: Unified Encoder-Free Multimodal Model
- **Source:** Google DeepMind — https://deepmind.google/blog/introducing-gemma-4-12b-a-unified-encoder-free-multimodal-model/
- **Severity:** informational
- **Tags:** `ai-launch`, `google`, `model-release`, `llm`
- **Summary:** Open-weight 12B multimodal model with encoder-free architecture for text and vision; targets on-device deployment and local fine-tuning use cases.

### 21. Google Launches AI Threat Defense with Automated Security Operations Agents
- **Source:** Google Cloud Security — https://cloud.google.com/blog/products/identity-security/detecting-and-containing-powered-threats-with-google-security-operations-agents/
- **Severity:** informational
- **Tags:** `ai-safety`, `cloud-security`, `google`, `llm`, `devsecops`
- **Summary:** Google AI Threat Defense integrates AI agents into Google Security Operations for automated threat detection, prioritization, and containment. Four-step framework; Google's first integrated AI-versus-AI defensive product for enterprise SecOps on GCP.

## Skippable

- **Microsoft Patches 200 Vulnerabilities** (SecurityWeek) — Duplicate Patch Tuesday coverage; BleepingComputer version chosen (#7).
- **Quoting Andrej Karpathy** (Simon Willison) — Commentary/quote on Claude Fable 5; no independent news value.
- **Can tech companies learn to love cheaper AI models?** (TechCrunch AI) — Business/economic analysis; no security angle.
- **Microsoft releases Windows 10 KB5094127** (BleepingComputer) — Patch Tuesday implementation detail; covered in #7.
- **Adobe Patches 123 Vulnerabilities** (SecurityWeek) — Routine Patch Tuesday batch; no single CVE confirmed critical and actively exploited.
- **Anthropic Claude Fable 5 on AWS** (AWS News Blog) — Duplicate Fable 5 coverage; incorporated as secondary source in #14.
- **Windows 11 KB5094126 & KB5093998 cumulative updates released** (BleepingComputer) — Patch Tuesday implementation; covered in #7.
- **Meta to Use Off-Site Business Data for Feed and AI Personalization** (The Hacker News) — Privacy/ad targeting policy change; no security incident.
- **Anthropic's Claude Fable 5 is a version of Mythos the public can access today** (TechCrunch AI) — Primary source for #14; listed here as context.
- **Anthropic releases its first Mythos-class model Claude Fable** (The Verge AI) — Duplicate Fable 5 coverage; covered in #14.
- **Microsoft Restores Some GitHub Repos, Keeps Others Offline as Miasma Probe Continues** (The Hacker News) — Duplicate Miasma coverage; BleepingComputer version chosen as primary (#4).
- **XBOW tests Anthropic's Mythos Preview for offensive security** (BleepingComputer) — Duplicate Mythos exploit research; incorporated as secondary context in #8.
- **Apple is embracing the fantasy of AI photo editing** (The Verge AI) — WWDC feature without independent security angle; covered in #18.
- **It's not FAANG anymore. It's MANGOS.** (TechCrunch AI) — Business/industry commentary; no security angle.
- **Russian Attackers Weaponize WinRAR Flaw Against Ukrainian Orgs** (Dark Reading) — Duplicate WinRAR coverage; THN version chosen for attribution detail (#9).
- **Microsoft AI chief walks back comments about AI taking over white-collar work** (The Verge AI) — Industry commentary; no security impact.
- **New Veeam vulnerability exposes backup servers to RCE attacks** (BleepingComputer) — Duplicate Veeam coverage; THN version chosen for CVE/CVSS detail (#6).
- **Apple's AI promises are finally, almost, sort of here** (The Verge AI) — Duplicate WWDC coverage; covered in #18.
- **Powering the future of robotics in Europe** (Google DeepMind) — Robotics initiative; no AI security or model release angle.
- **Sandstone raises $30M to bring AI to in-house legal teams** (TechCrunch AI) — SaaS funding; no security angle.
- **Apple's best AI idea looks a lot like vibe coding** (The Verge AI) — Commentary; duplicate WWDC angle.
- **New Platform Uses Cryptographic Invisibility to Protect AI-Built Applications** (SecurityWeek) — Vendor product launch (Atsign); reads as press release with insufficient technical detail.
- **Lovable says it has hit $500M in annualized revenue** (TechCrunch AI) — SaaS growth metrics; no security angle.
- **Apple's AI pitch will live or die by its privacy promise** (The Verge AI) — Opinion piece; duplicate WWDC coverage.
- **How an e-scooter founder raised $5 million to build space data centers** (TechCrunch AI) — Off-topic infrastructure funding.
- **Siemens KACO Blueplanet Inverters** (CISA Alerts) — Routine ICS advisory; no confirmed active exploitation.
- **Schneider Electric EcoStruxure Panel Server** (CISA Alerts) — Routine ICS advisory; no confirmed active exploitation.
- **Schneider Electric Modicon Network Managed Switches** (CISA Alerts) — Routine ICS advisory; no confirmed active exploitation.
- **The Hidden Security Risk in Modern Networks: The Work Between Tools** (The Hacker News) — Vendor-sponsored content; no new vulnerability or technical finding.
- **Will AI Kill the Bug Bounty Industry?** (SecurityWeek) — Opinion/analysis; underlying Mythos research covered in #8.
- **Amazon employees ask Seattle to put the brakes on new data centers** (The Verge AI) — Policy/activism; no security angle.
- **CISA gives feds 3 days to patch Check Point VPN bug exploited as zero-day** (BleepingComputer) — Duplicate Check Point VPN coverage; SecurityWeek version chosen (#1).
- **Hades PyPI Attack: 19 Packages Poisoned to Auto-Run Bun Credential Stealer** (The Hacker News) — Duplicate Hades/PyPI coverage; incorporated as secondary detail in #5, SecurityWeek chosen for broader campaign scope.
- **Google patches new Chrome zero-day flaw exploited in the wild** (BleepingComputer) — Duplicate Chrome zero-day coverage; THN version chosen for CVE and CVSS detail (#2).
