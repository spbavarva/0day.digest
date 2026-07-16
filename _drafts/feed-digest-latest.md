# Digest — 2026-07-16 PM

- Window: last 14h
- Raw items considered: 64
- Relevant: 25
- Skippable: 39

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[MEDIUM]** Codex Coding Agent Bug Can Delete a User's Home Directory — `2026-07-16-codex-agent-bug-deletes-home-directory.md`
- [x] **[INFORMATIONAL]** NVIDIA Nemotron 3 Embed Tops RTEB Retrieval Benchmark — `2026-07-16-nvidia-nemotron-3-embed-tops-rteb.md`
- [x] **[INFORMATIONAL]** Thinking Machines Lab Releases Inkling, a 975B-Parameter Open-Weights Model — `2026-07-16-thinking-machines-lab-releases-inkling.md`
- [x] **[HIGH]** Sandworm Uses Fake CAPTCHA to Trick Ukrainians Into Running PowerShell — `2026-07-16-sandworm-fake-captcha-powershell-ukraine.md`
- [x] **[INFORMATIONAL]** 23andMe to Pay $18M in Genetic Data Breach Settlement — `2026-07-16-23andme-18-million-breach-settlement.md`
- [x] **[HIGH]** n8n Enterprise Token Exchange Flaw Enables Cross-Issuer Account Takeover — `2026-07-16-n8n-token-exchange-flaw-cross-issuer-takeover.md`
- [x] **[INFORMATIONAL]** Apple Intelligence Approved for Launch in China via Alibaba and Baidu — `2026-07-16-apple-intelligence-approved-china-alibaba-baidu.md`
- [x] **[HIGH]** HelloNet Campaign Pushes Malicious Modules Through ViPNet Update System — `2026-07-16-hellonet-vipnet-update-system-campaign.md`
- [x] **[MEDIUM]** New TELEPUZ Malware Spreads via ClickFix Lures — `2026-07-16-telepuz-malware-clickfix-lures.md`
- [x] **[HIGH]** ClickLock Stealer Kills macOS Apps Every 210ms Until Victims Type Their Password — `2026-07-16-clicklock-stealer-macos-password-loop.md`
- [x] **[HIGH]** GoSerpent Backdoor Evolves With New Data Exfiltration Tools — `2026-07-16-goserpent-backdoor-southeast-asia.md`
- [x] **[INFORMATIONAL]** Scattered Spider Hackers Sentenced to 5.5 Years Over £29M Transport for London Hack — `2026-07-16-scattered-spider-tfl-sentencing.md`
- [x] **[HIGH]** PhantomEnigma Campaign Hijacks 20+ Brazilian Government Websites — `2026-07-16-phantomenigma-brazilian-government-websites.md`
- [x] **[HIGH]** New Data Injection Attack Can Hijack AI Agents Into Misclicks and Attacker Commands — `2026-07-16-ai-agent-data-injection-attack.md`
- [x] **[HIGH]** Daxin Rootkit Resurfaces in Taiwan With New Stupig Backdoor — `2026-07-16-daxin-stupig-backdoor-taiwan.md`
- [x] **[HIGH]** CISA Orders Federal Agencies to Patch Actively Exploited Oracle EBS Flaw by Saturday — `2026-07-16-cisa-oracle-ebs-actively-exploited-deadline.md`
- [x] **[HIGH]** Cisco Talos Discloses UAT-11795's Starland RAT and WLDR C2 Implant — `2026-07-16-uat-11795-starland-rat-wldr-c2.md`
- [x] **[HIGH]** New Spirals Ransomware Encrypts a Victim Network in Under 24 Hours — `2026-07-16-spirals-ransomware-24-hour-encryption.md`
- [x] **[HIGH]** Unpatched Shark Vacuum Flaw Allows Region-Wide Takeover of Other Devices — `2026-07-16-shark-vacuum-flaw-region-wide-takeover.md`
- [x] **[HIGH]** F5 Patches Multiple NGINX, BIG-IP Vulnerabilities — `2026-07-16-f5-nginx-big-ip-vulnerabilities-patched.md`
- [x] **[INFORMATIONAL]** OpenAI's GPT-Red Automates Prompt Injection Red-Teaming for GPT-5.6 — `2026-07-16-openai-gpt-red-prompt-injection-red-teaming.md`
- [x] **[HIGH]** Old UEFI Shims Expose Systems to Secure Boot Bypass — `2026-07-16-old-uefi-shims-secure-boot-bypass.md`
- [x] **[CRITICAL]** Zoom Patches Critical Windows Flaw Enabling Account Takeover — `2026-07-16-zoom-cve-2026-53412-account-takeover.md`
- [x] **[INFORMATIONAL]** Police Disrupt €140M Cyber Fraud Ring in Spain — `2026-07-16-spain-cyber-fraud-ring-disrupted.md`
- [x] **[HIGH]** Nightmare Eclipse Drops 'LegacyHive' Windows Zero-Day — `2026-07-16-legacyhive-windows-zero-day.md`

## Relevant (details)

### 1. Codex Coding Agent Bug Can Delete a User's Home Directory
- **Source:** Simon Willison — https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything
- **Severity:** medium
- **Tags:** `llm`, `ai-safety`, `openai`
- **Summary:** OpenAI confirmed reports of GPT-5.6-powered Codex unexpectedly deleting files when run in full-access mode without sandboxing. The bug occurs when the model tries to redirect the $HOME env var to a temp directory and instead deletes the real $HOME.

### 2. NVIDIA Nemotron 3 Embed Tops RTEB Retrieval Benchmark
- **Source:** Hugging Face Blog — https://huggingface.co/blog/nvidia/nemotron-3-embed-wins-rteb
- **Severity:** informational
- **Tags:** `model-release`, `llm`
- **Summary:** NVIDIA's Nemotron 3 Embed model took the #1 overall spot on the RTEB retrieval benchmark. The source provided no further technical detail beyond the ranking claim.

### 3. Thinking Machines Lab Releases Inkling, a 975B-Parameter Open-Weights Model
- **Source:** Simon Willison — https://simonwillison.net/2026/Jul/16/inkling/#atom-everything
- **Severity:** informational
- **Tags:** `model-release`, `llm`, `ai-launch`
- **Summary:** Mira Murati's Thinking Machines Lab released Inkling, an Apache-2.0 licensed 975B-parameter (41B active) MoE model trained on 45 trillion multimodal tokens. A smaller Inkling-Small variant is planned but not yet released.

### 4. Sandworm Uses Fake CAPTCHA to Trick Ukrainians Into Running PowerShell
- **Source:** The Record (Recorded Future) — https://therecord.media/ukraine-sandworm-hacks-captcha-powershell
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Summary:** Russian state-linked group Sandworm is using fake CAPTCHA pages that instruct Ukrainian users to paste a PowerShell command instead of verifying humanity, a ClickFix-style technique to gain initial access.

### 5. 23andMe to Pay $18M in Genetic Data Breach Settlement
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/23andme-to-pay-18-million-in-new-genetics-data-breach-settlement/
- **Severity:** informational
- **Tags:** `data-breach`
- **Summary:** 23andMe agreed to pay $18 million settling claims from 43 state attorneys general that it failed to protect customers' genetic data, following its earlier large-scale breach.

### 6. n8n Enterprise Token Exchange Flaw Enables Cross-Issuer Account Takeover
- **Source:** The Hacker News — https://thehackernews.com/2026/07/n8n-token-exchange-flaw-could-let.html
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`, `appsec`
- **Summary:** n8n Enterprise instances trusting multiple token issuers matched JWTs to local users by the sub claim alone, ignoring iss, letting a valid token from one issuer log an attacker in as a same-sub user under a different issuer.

### 7. Apple Intelligence Approved for Launch in China via Alibaba and Baidu
- **Source:** TechCrunch AI — https://techcrunch.com/2026/07/16/apple-intelligence-approved-for-launch-in-china-with-alibabas-qwen-ai/
- **Severity:** informational
- **Tags:** `ai-launch`
- **Summary:** Chinese regulators approved Apple Intelligence for launch in China through partnerships with Alibaba and Baidu, a long-rumored deal marking a key step for Apple's AI ambitions in the market.

### 8. HelloNet Campaign Pushes Malicious Modules Through ViPNet Update System
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/tr/hellonet-vipnet/120700/
- **Severity:** high
- **Tags:** `supply-chain`, `malware`
- **Summary:** Kaspersky identified targeted infection attempts against large Russian organizations delivered through the ViPNet secure-networking update system, abusing the trusted update channel to distribute malicious modules.

### 9. New TELEPUZ Malware Spreads via ClickFix Lures
- **Source:** The Hacker News — https://thehackernews.com/2026/07/new-telepuz-malware-spreads-via.html
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** Elastic Security Labs identified a new modular malware family, TELEPUZ, spreading via ClickFix-style lures since late April 2026, capable of data theft and command execution with a currently small but growing C2 footprint.

### 10. ClickLock Stealer Kills macOS Apps Every 210ms Until Victims Type Their Password
- **Source:** The Hacker News — https://thehackernews.com/2026/07/new-clicklock-macos-stealer-kills-apps.html
- **Severity:** high
- **Tags:** `malware`
- **Summary:** ClickLock Stealer, delivered via a pasted Terminal command, repeatedly kills running macOS apps until a victim enters their password behind a fake system dialog, then installs LaunchAgents to steal credentials and crypto.

### 11. GoSerpent Backdoor Evolves With New Data Exfiltration Tools
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/goserpent-backdoor-in-southeast-asia/120687/
- **Severity:** high
- **Tags:** `malware`
- **Summary:** Kaspersky detailed a two-phase campaign using the GoSerpent backdoor, Stowaway RAT, and ThumbcacheService to steal data from government entities in Southeast Asia, showing continued tooling evolution.

### 12. Scattered Spider Hackers Sentenced to 5.5 Years Over £29M Transport for London Hack
- **Source:** The Record (Recorded Future) — https://therecord.media/scattered-spider-hackers-tfl-sentenced
- **Severity:** informational
- **Tags:** `law-enforcement`
- **Summary:** Two Scattered Spider members were sentenced to more than five years in prison for the 2024 Transport for London cyberattack, which caused an estimated £29 million in damages.

### 13. PhantomEnigma Campaign Hijacks 20+ Brazilian Government Websites
- **Source:** The Hacker News — https://thehackernews.com/2026/07/20-hijacked-government-websites.html
- **Severity:** high
- **Tags:** `malware`, `appsec`
- **Summary:** More than 20 Brazilian government websites were hijacked into malware delivery channels in the PhantomEnigma campaign uncovered by ANY.RUN, which revealed previously undocumented backdoor behavior and hidden infrastructure.

### 14. New Data Injection Attack Can Hijack AI Agents Into Misclicks and Attacker Commands
- **Source:** The Hacker News — https://thehackernews.com/2026/07/new-agent-data-injection-attack-can.html
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `prompt-injection`
- **Summary:** Researchers describe a technique where planted content — a fake review or GitHub comment — corrupts the data an AI agent trusts without hijacking its stated task, causing unintended purchases or arbitrary command execution.

### 15. Daxin Rootkit Resurfaces in Taiwan With New Stupig Backdoor
- **Source:** The Hacker News — https://thehackernews.com/2026/07/daxin-resurfaces-in-taiwan-alongside.html
- **Severity:** high
- **Tags:** `malware`
- **Summary:** The Daxin kernel-mode rootkit, first documented by Symantec in 2022 and linked to a China-based actor, resurfaced after four-plus years in an attack on a Taiwan manufacturer, alongside a new pre-login SYSTEM backdoor dubbed Stupig.

### 16. CISA Orders Federal Agencies to Patch Actively Exploited Oracle EBS Flaw by Saturday
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-oracle-flaw-by-saturday/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Summary:** CISA ordered federal agencies to secure systems by Saturday against ongoing attacks exploiting a critical vulnerability in Oracle E-Business Suite, reflecting confirmed active in-the-wild exploitation.

### 17. Cisco Talos Discloses UAT-11795's Starland RAT and WLDR C2 Implant
- **Source:** Cisco Talos — https://blog.talosintelligence.com/uat-11795-deploys-novel-starland-rat-and-bespoke-wldr-c2-implant-in-financially-motivated-campaign/
- **Severity:** high
- **Tags:** `malware`
- **Summary:** Cisco Talos disclosed UAT-11795, a Russian-speaking financially motivated actor running a campaign against U.S. and European targets since mid-2025, deploying a novel Starland RAT and bespoke WLDR C2 implant via trojanized WebEx/Zoom installers.

### 18. New Spirals Ransomware Encrypts a Victim Network in Under 24 Hours
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-spirals-ransomware-encrypts-victim-network-in-under-24-hours/
- **Severity:** high
- **Tags:** `ransomware`
- **Summary:** A new ransomware actor, Spirals, completed a full intrusion — initial access through encryption — in under 24 hours, compressing the window defenders have to detect and respond.

### 19. Unpatched Shark Vacuum Flaw Allows Region-Wide Takeover of Other Devices
- **Source:** The Hacker News — https://thehackernews.com/2026/07/unpatched-shark-vacuum-flaw-could-let.html
- **Severity:** high
- **Tags:** `vulnerability`, `iot`
- **Summary:** A researcher found that extracting a certificate from a Shark RV2320EDUS vacuum allows running root commands against other Shark vacuums in the same AWS region, exposing cameras, navigation maps, and plaintext Wi-Fi passwords.

### 20. F5 Patches Multiple NGINX, BIG-IP Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/f5-patches-multiple-nginx-big-ip-vulnerabilities/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Summary:** F5 patched multiple NGINX and BIG-IP vulnerabilities that could let attackers modify configurations, disrupt processes, cross security boundaries, leak memory, or execute code across widely deployed infrastructure.

### 21. OpenAI's GPT-Red Automates Prompt Injection Red-Teaming for GPT-5.6
- **Source:** The Hacker News — https://thehackernews.com/2026/07/openais-gpt-red-automates-prompt.html
- **Severity:** informational
- **Tags:** `llm`, `ai-safety`, `openai`, `prompt-injection`
- **Summary:** OpenAI disclosed GPT-Red, an internal automated red-teaming model that scales prompt injection vulnerability discovery, used to adversarially train newer models including GPT-5.6 before wide deployment.

### 22. Old UEFI Shims Expose Systems to Secure Boot Bypass
- **Source:** SecurityWeek — https://www.securityweek.com/old-uefi-shims-expose-systems-to-secure-boot-bypass/
- **Severity:** high
- **Tags:** `vulnerability`, `microsoft`
- **Summary:** Outdated UEFI shim bootloaders signed by Microsoft can be abused to bypass Secure Boot on any system regardless of OS, since their valid signature passes boot-chain trust checks despite known vulnerabilities.

### 23. Zoom Patches Critical Windows Flaw Enabling Account Takeover
- **Source:** The Hacker News — https://thehackernews.com/2026/07/zoom-patches-critical-windows-flaw-that.html
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`
- **Summary:** Zoom patched CVE-2026-53412 (CVSS 9.8), an improper input validation flaw affecting the Zoom Desktop Client, VDI Client, and Meeting SDK for Windows that could facilitate account takeover.

### 24. Police Disrupt €140M Cyber Fraud Ring in Spain
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/police-disrupt-140m-euro-cyber-fraud-ring-spain
- **Severity:** informational
- **Tags:** `fraud`, `law-enforcement`
- **Summary:** Spanish police disrupted an Iberian cyber fraud ring responsible for an estimated €140 million in losses, which laundered proceeds through complex financial networks.

### 25. Nightmare Eclipse Drops 'LegacyHive' Windows Zero-Day
- **Source:** SecurityWeek — https://www.securityweek.com/nightmare-eclipse-drops-legacyhive-windows-zero-day/
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `microsoft`
- **Summary:** A researcher operating as "Nightmare Eclipse" disclosed a Windows zero-day dubbed LegacyHive, deliberately stripping the proof-of-concept before release to prevent immediate exploitation.

## Skippable

- **Begun, the Patch Wars have** — Cisco Talos. Vague teaser post with no substantive technical content.
- **UK investigates TikTok for alleged age-verification lapses** — The Record. Child-safety regulatory story, not AI/security technical.
- **Ukrainians rally against dismissal of tech-minded defense minister Fedorov** — The Record. Political story, no security/AI substance.
- **Cloud CISO Perspectives: How AI leverages deep context as the defender's advantage** — Google Cloud Security. Vendor newsletter/opinion, no concrete technical news.
- **Why teens deserve access to safe AI** — OpenAI Blog. Marketing/policy blog post, no technical substance.
- **Connect more of your apps to Search** — Google AI Blog. Consumer product feature, no security angle.
- **Create, edit and star in videos with two Google Vids updates** — Google AI Blog. Consumer product feature, no security angle.
- **Google's AI Mode now lets you link and interact with select apps** — TechCrunch AI. Consumer feature launch, not security-relevant.
- **ThreatsDay: Game Cheat Spyware, 24-Hour Ransomware, Chrome Sync Stalking + 12 More Stories** — The Hacker News. Weekly roundup duplicating stories already covered individually.
- **Yes, you can now order DoorDash from the command line** — TechCrunch AI. Novelty product news, no security angle.
- **Why is OpenAI selling a ChatGPT basketball?** — TechCrunch AI. Marketing/fluff, no news value.
- **Legacy Systems, Real-World Impacts: The Reality of OT Security** — SecurityWeek. General opinion piece, no specific incident.
- **How a former DeepMind researcher raised at a $300M pre-seed valuation** — TechCrunch AI. Funding/business news, not security-relevant.
- **Why AMI Labs' Alexandre LeBrun won't call his AI 'AGI' or 'superintelligence'** — TechCrunch AI. Opinion/branding piece, no news value.
- **Moonshot's upcoming Kimi 3 is expected to close the gap with Anthropic's Opus 4.8** — TechCrunch AI. Speculative rumor, no confirmed release details.
- **AI Agents Broke the Security Playbook. Here's What Replaces It.** — BleepingComputer (Token Security). Vendor-sponsored content, marketing.
- **Quoting Linus Torvalds** — Simon Willison. Opinion commentary, no news value.
- **Two Scattered Spider Hackers Sentenced to Jail in UK** — SecurityWeek. Duplicate coverage; see The Record item above.
- **AI Data Centers Are Being Built Faster Than They Can Be Secured** — SecurityWeek. Opinion/trend piece, no specific incident.
- **'ClickLock Stealer' Bypasses macOS Security With Social Engineering, Process Killing** — SecurityWeek. Duplicate, thinner coverage than the Hacker News version above.
- **Scattered Spider members behind TfL hack get five years in prison** — BleepingComputer. Duplicate coverage; see The Record item above.
- **Rockwell Automation CompactLogix, ControlLogix, Compact GuardLogix and GuardLogix** — CISA Alerts. Routine ICS advisory, DoS only, no active exploitation.
- **Rockwell Automation Flex 5000 Adapter** — CISA Alerts. Routine ICS advisory, no active exploitation.
- **Siemens SICAM 8** — CISA Alerts. Routine ICS advisory, DoS only, no active exploitation.
- **SALTO ProAccess Space** — CISA Alerts. Routine ICS advisory requiring authenticated access, no active exploitation.
- **Rockwell Automation FactoryTalk DataMosaix** — CISA Alerts. Routine ICS advisory, no active exploitation.
- **NASA Core Flight System (cFS) Health & Safety (HS) Application** — CISA Alerts. Routine ICS advisory, DoS only, niche software.
- **Rockwell Automation Arena** — CISA Alerts. Routine ICS advisory, no confirmed active exploitation.
- **AutomationDirect Productivity Suite** — CISA Alerts. Routine ICS advisory requiring local/physical access.
- **Rockwell Automation 1756-EN2, 1756-EN3, and 1756-ENBT** — CISA Alerts. Routine ICS advisory, DoS only, no active exploitation.
- **Windows 11 24H2 Home and Pro reach end of support in 90 days** — BleepingComputer. Lifecycle notice, not a security incident.
- **Newer Models, Same Advantage** — Hugging Face Blog (Dharma-AI). No summary content provided, likely low-signal marketing.
- **Oak Emerges From Stealth Mode With $60 Million in Funding** — SecurityWeek. Funding announcement, no technical substance.
- **Splunk, Zoom Patch Critical Vulnerabilities** — SecurityWeek. Duplicate/less detailed than the dedicated Zoom CVE coverage above.
- **Russian hackers trojanize WebEx, Zoom apps to push Starland malware** — BleepingComputer. Duplicate; see the Cisco Talos original disclosure above.
- **AI Can Find Bugs, But Human Knowledge Still Proves Them** — The Hacker News. Opinion piece, no specific news item.
- **The Hunter's Paradox: Is it time to embrace automated threat hunting?** — Cisco Talos. Opinion/musing piece, no concrete news.
- **Our approach to bioresilience** — Google DeepMind. Thin policy announcement, no actionable technical detail.
- **China's Top Cybersecurity Firms Hit by Mounting Military Procurement Bans** — SecurityWeek. Geopolitical/business story, no technical security substance.
