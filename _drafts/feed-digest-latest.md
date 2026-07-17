# Digest — 2026-07-17 PM

- Window: last 14h
- Raw items considered: 40
- Relevant: 14
- Skippable: 26

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** HollowByte DDoS Flaw Bloats OpenSSL Server Memory With 11-Byte Payload — `2026-07-17-hollowbyte-openssl-dos-flaw.md`
- [x] **[HIGH]** New NadMesh Botnet Hunts Exposed AI Services for Cloud Keys and Kubernetes Tokens — `2026-07-17-nadmesh-botnet-ai-services.md`
- [x] **[HIGH]** GoldenEyeDog Subgroup Linked to DigiCert Breach and Code-Signing Certificate Theft — `2026-07-17-goldeneyedog-digicert-code-signing-theft.md`
- [x] **[MEDIUM]** Inside Qilin Ransomware: Custom Rust Loader and Kernel-Level EDR Killer — `2026-07-17-qilin-ransomware-rust-loader-edr-killer.md`
- [x] **[HIGH]** Fake Coding Tests Deliver OtterCookie-Aligned Malware Hidden in SVG Flag Images — `2026-07-17-ottercookie-svg-steganography-fake-coding-tests.md`
- [x] **[INFORMATIONAL]** Google Bets 'Agentic Defense' Strategy Can Outpace Attackers — `2026-07-17-google-agentic-defense-wiz.md`
- [x] **[MEDIUM]** E.U. Orders Google to Open Android Mic, Camera and Screen to Rival AI Assistants — `2026-07-17-eu-google-android-ai-assistant-access.md`
- [x] **[HIGH]** New Windows LegacyHive Zero-Day Gives Hackers Admin Privileges — `2026-07-17-legacyhive-windows-zero-day-privesc.md`
- [x] **[HIGH]** Three Steps to the Terminal: A Siemens ROX II Zero-Day Trilogy — `2026-07-17-siemens-rox-ii-zero-day-trilogy.md`
- [x] **[HIGH]** ACR Stealer Uses ClickFix Lures to Steal Browser Tokens and Microsoft 365 Files — `2026-07-17-acr-stealer-clickfix-microsoft-365.md`
- [x] **[HIGH]** New GoSerpent Malware Targets Southeast Asian Governments and Diplomats for Espionage — `2026-07-17-goserpent-malware-southeast-asia-espionage.md`
- [x] **[HIGH]** CISA Urges Immediate Action on Actively Exploited Fortinet FortiSandbox Flaws — `2026-07-17-cisa-fortinet-fortisandbox-exploited.md`
- [x] **[CRITICAL]** CISA Adds Exploited SharePoint RCE Zero-Day CVE-2026-58644 to KEV — `2026-07-17-cisa-sharepoint-cve-2026-58644-kev.md`
- [x] **[HIGH]** Coca-Cola Suspends US Fairlife Production Due to Ransomware Attack — `2026-07-17-coca-cola-fairlife-ransomware.md`

## Relevant (details)

### 1. HollowByte DDoS Flaw Bloats OpenSSL Server Memory With 11-Byte Payload
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hollowbyte-ddos-flaw-bloats-openssl-server-memory-with-11-byte-payload/
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`
- **Summary:** A newly disclosed vulnerability dubbed HollowByte lets unauthenticated attackers trigger a denial-of-service condition on OpenSSL servers using a malicious payload as small as 11 bytes, bloating memory and risking crashes on internet-facing services.

### 2. New NadMesh Botnet Hunts Exposed AI Services for Cloud Keys and Kubernetes Tokens
- **Source:** The Hacker News — https://thehackernews.com/2026/07/new-nadmesh-botnet-hunts-exposed-ai.html
- **Severity:** high
- **Tags:** `malware`, `cloud-security`, `iam`, `kubernetes`
- **Summary:** A Go-based botnet named NadMesh scans for exposed AI services — ComfyUI, Ollama, n8n, Open WebUI, Langflow, Gradio — to harvest cloud credentials and Kubernetes tokens; its operator claims over 3,800 stolen AWS keys collected since early July.

### 3. GoldenEyeDog Subgroup Linked to DigiCert Breach and Code-Signing Certificate Theft
- **Source:** The Hacker News — https://thehackernews.com/2026/07/goldeneyedog-subgroup-linked-to.html
- **Severity:** high
- **Tags:** `supply-chain`, `data-breach`, `malware`
- **Summary:** Expel attributed the April 2026 DigiCert security incident, which involved theft of code-signing certificates, to CylindricalCanine, a sub-group of the Chinese cybercrime group GoldenEyeDog. Stolen code-signing certs can be used to sign malware so it appears trusted.

### 4. Inside Qilin Ransomware: Custom Rust Loader and Kernel-Level EDR Killer
- **Source:** Flashpoint — https://flashpoint.io/blog/inside-qilin-ransomware/
- **Severity:** medium
- **Tags:** `ransomware`, `malware`
- **Summary:** New Flashpoint analysis details Qilin ransomware's custom Rust-based loader and kernel-level EDR killer used to disable endpoint defenses before encryption, reflecting a broader trend of ransomware operators investing in defense-evasion tooling.

### 5. Fake Coding Tests Deliver OtterCookie-Aligned Malware Hidden in SVG Flag Images
- **Source:** The Hacker News — https://thehackernews.com/2026/07/north-korea-linked-hackers-hide.html
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Summary:** North Korean threat actors tied to the Contagious Interview campaign are hiding malicious payloads inside SVG image files via steganography, delivered through fake coding tests; victims receive a four-stage OTTERCOOKIE-aligned payload including credential and crypto wallet stealers.

### 6. Google Bets 'Agentic Defense' Strategy Can Outpace Attackers
- **Source:** Dark Reading — https://www.darkreading.com/cloud-security/google-bets-agentic-defense-strategy-outpace-attackers
- **Severity:** informational
- **Tags:** `cloud-security`, `wiz`, `google`, `ai-safety`
- **Summary:** Google Cloud is folding Wiz capabilities into a new "agentic defense" platform meant to automate threat detection and remediation, betting on agentic automation to counter AI-driven attacks.

### 7. E.U. Orders Google to Open Android Mic, Camera and Screen to Rival AI Assistants
- **Source:** The Hacker News — https://thehackernews.com/2026/07/eu-orders-google-to-open-android-mic.html
- **Severity:** medium
- **Tags:** `google`, `ai-safety`, `regulation`
- **Summary:** The European Commission ordered Google to give rival AI assistants the same Android system access Gemini has — camera, microphone, screen content, and background app control — by Android 18 and no later than August 1, 2027, expanding the attack surface for third-party AI assistants.

### 8. New Windows LegacyHive Zero-Day Gives Hackers Admin Privileges
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-windows-legacyhive-zero-day-exploit-grants-hackers-admin-access/
- **Severity:** high
- **Tags:** `zero-day`, `privilege-escalation`, `microsoft`, `vulnerability`
- **Summary:** A researcher using the handle "Nightmare Eclipse" publicly released a Windows zero-day exploit dubbed LegacyHive allowing privilege escalation to admin on fully patched Windows systems, with no official Microsoft patch available yet.

### 9. Three Steps to the Terminal: A Siemens ROX II Zero-Day Trilogy
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/siemens-rox-ii-zero-day-vulnerabilities/
- **Severity:** high
- **Tags:** `zero-day`, `privilege-escalation`, `vulnerability`
- **Summary:** Unit 42 published technical details on three chained zero-day vulnerabilities in Siemens ROX II OT switches that together allow privilege escalation and persistent root access on industrial control system network equipment.

### 10. ACR Stealer Uses ClickFix Lures to Steal Browser Tokens and Microsoft 365 Files
- **Source:** The Hacker News — https://thehackernews.com/2026/07/acr-stealer-uses-clickfix-lures-to.html
- **Severity:** high
- **Tags:** `malware`, `phishing`, `microsoft`
- **Summary:** ACR Stealer, active since 2024, is using ClickFix-style lures that trick victims into pasting and running commands via the Windows Run box to steal browser credentials, session tokens, and Microsoft 365/OneDrive/SharePoint files.

### 11. New GoSerpent Malware Targets Southeast Asian Governments and Diplomats for Espionage
- **Source:** The Hacker News — https://thehackernews.com/2026/07/new-goserpent-malware-targets-southeast.html
- **Severity:** high
- **Tags:** `malware`
- **Summary:** Kaspersky discovered a previously undocumented malware family called GoSerpent used in espionage operations against government and diplomatic entities in Southeast Asia since late 2025, focused on long-term access and intelligence gathering.

### 12. CISA Urges Immediate Action on Actively Exploited Fortinet FortiSandbox Flaws
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-warns-feds-to-patch-exploited-fortinet-fortisandbox-flaws-by-sunday/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `fortinet`
- **Summary:** CISA ordered federal agencies to patch two actively exploited vulnerabilities in Fortinet's FortiSandbox threat detection platform by Sunday, confirming attackers are already exploiting the flaws in the wild.

### 13. CISA Adds Exploited SharePoint RCE Zero-Day CVE-2026-58644 to KEV
- **Source:** The Hacker News — https://thehackernews.com/2026/07/cisa-adds-exploited-sharepoint-rce-zero.html
- **Severity:** critical
- **Tags:** `zero-day`, `rce`, `cve`, `vulnerability`, `microsoft`
- **Summary:** CISA added CVE-2026-58644, a critical (CVSS 9.8) deserialization flaw in Microsoft SharePoint Server, to its Known Exploited Vulnerabilities catalog after confirming active exploitation; FCEB agencies must patch by July 19, 2026.

### 14. Coca-Cola Suspends US Fairlife Production Due to Ransomware Attack
- **Source:** SecurityWeek — https://www.securityweek.com/coca-cola-suspends-us-fairlife-production-due-to-ransomware-attack/
- **Severity:** high
- **Tags:** `ransomware`
- **Summary:** Coca-Cola-owned dairy brand Fairlife suspended U.S. production, including plants in Michigan, New York, and Arizona, following a ransomware attack; the company has not yet determined the full scope of the incident.

## Skippable

- **How Apple's big lawsuit could disrupt OpenAI's IPO plans** — TechCrunch AI. Video segment, duplicate coverage of the Apple/OpenAI lawsuit story.
- **Apple's plot to crush OpenAI** — The Verge AI. Podcast episode, duplicate coverage of the Apple/OpenAI lawsuit story.
- **The Real AI Threat Is Blind Trust** — Dark Reading. Opinion piece without concrete news value.
- **The Good, the Bad and the Ugly in Cybersecurity – Week 29** — SentinelOne Labs. Weekly link roundup, no single technical deep-dive.
- **Fine-tune video and image models at scale with NVIDIA NeMo Automodel and Diffusers** — Hugging Face Blog. Tooling tutorial, no security or news angle.
- **Patreon stops asking AI bots not to scrape — and starts blocking them** — TechCrunch AI. Platform policy change, no security substance.
- **Ernst & Young discloses data breach after support system hack** — BleepingComputer. Generic breach disclosure without technical detail or confirmed scale.
- **In Other News: Iran Tracks US Military Phones, CrashStealer macOS Malware, CVD Blueprint** — SecurityWeek. Link roundup, no single deep-dive.
- **Inside the Search for "Clean" Residential Proxies for Carding** — BleepingComputer. Underground fraud economics analysis, not practitioner-actionable.
- **Apple's lawsuit couldn't come at a worse time for OpenAI** — TechCrunch AI. Podcast episode, duplicate coverage of the Apple/OpenAI lawsuit story.
- **Quoting Kimi K3** — Simon Willison. Brief quote blurb, no substantial news.
- **Dairy company Fairlife suspends production in US after cyber incident** — The Record. Duplicate of the Coca-Cola/Fairlife ransomware story; SecurityWeek version has more detail (confirmed ransomware).
- **Gold Eagle Clearinghouse Targets Security Gap, but How Is Unclear** — Dark Reading. Speculative piece; the headline itself says the mechanism is unclear.
- **Zelensky appoints Ukraine's acting security service chief as acting defense minister** — The Record. Political/military appointment, not cybersecurity.
- **Podcast: Broken Governance, Agentic AI, and the MindStone Agent Exclusive** — SecurityWeek. Podcast format, no concrete news.
- **Why the first GPU financiers are turning to inference chips in a $400 million deal** — TechCrunch AI. Business/financing news, no security angle.
- **Beacon Security Raises $13 Million for Security Data Platform** — SecurityWeek. Funding announcement.
- **The Race to Field Military Autonomy Is On, Can Trusted Information Infrastructure Keep Pace?** — The Hacker News. Thought-leadership piece, no concrete news.
- **Industry Reactions to Pentagon Suspending CMMC Phase 2: Feedback Friday** — SecurityWeek. Opinion/reactions roundup, not primary news.
- **Armenia Detains Russian Tourist on U.S. Warrant for REvil Hacker, Lawyers Say Wrong Man** — The Hacker News. Law enforcement misidentification story, not technical.
- **A scorecard for the AI age** — OpenAI Blog. Business/ROI framing, not a model launch.
- **Windows Server 2022 reach end of mainstream support in 90 days** — BleepingComputer. Routine lifecycle notice.
- **Cyberattack Disrupts Operations of Japanese Frozen Food Giant Nichirei** — SecurityWeek. Ransomware victim disclosure without TTPs or IOCs.
- **Risk Ledger Raises $32 Million in Series B Funding** — SecurityWeek. Funding announcement.
- **US charges two over laundering $43 million from investment fraud** — BleepingComputer. Individual law enforcement case, no technical substance.
- **Fresh SharePoint Vulnerability Exploited Soon After Disclosure** — SecurityWeek. Duplicate of the CISA/CVE-2026-58644 story; The Hacker News version has the CVE and CVSS detail.
