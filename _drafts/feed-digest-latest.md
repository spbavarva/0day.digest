# Digest — 2026-05-08 AM

- Window: last 14h
- Raw items considered: 28
- Relevant: 10
- Skippable: 18

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Dirty Frag Linux Zero-Day Gives Root on All Major Distributions — `2026-05-08-dirty-frag-linux-kernel-lpe-zero-day.md`
- [x] **[CRITICAL]** ShinyHunters Breach Canvas Platform, Threaten 275M Education Records — `2026-05-08-canvas-instructure-shinyhunters-275m-breach.md`
- [x] **[HIGH]** CVE-2025-68670: Pre-Auth RCE Found in xrdp Server — `2026-05-08-cve-2025-68670-xrdp-pre-auth-rce.md`
- [x] **[HIGH]** Claude Chrome Extension Flaw Allows Prompt Injection and Agent Takeover — `2026-05-08-claude-chrome-extension-prompt-injection-takeover.md`
- [x] **[HIGH]** Ivanti Patches EPMM Zero-Day Under Active Targeted Exploitation — `2026-05-08-ivanti-epmm-zero-day-cve-2026-6973-targeted-attacks.md`
- [x] **[HIGH]** TCLBanker Trojan Targets 59 Financial Platforms, Spreads via WhatsApp and Outlook — `2026-05-07-tclbanker-banking-trojan-whatsapp-outlook.md`
- [x] **[HIGH]** MuddyWater Uses Chaos Ransomware as Cover in Iranian APT Intrusion — `2026-05-07-muddywater-chaos-ransomware-cover-iran-apt.md`
- [x] **[HIGH]** PCPJack Worm Steals Cloud Credentials While Evicting TeamPCP — `2026-05-07-pcpjack-worm-cloud-credential-theft.md`
- [x] **[MEDIUM]** RansomHouse Claims Breach of Cybersecurity Vendor Trellix — `2026-05-08-ransomhouse-trellix-ransomware-hack-claim.md`
- [x] **[INFORMATIONAL]** OpenAI Launches Voice Intelligence Features in API — `2026-05-07-openai-voice-intelligence-api-launch.md`

## Relevant (details)

### 1. Dirty Frag Linux Zero-Day Gives Root on All Major Distributions
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-linux-dirty-frag-zero-day-with-poc-exploit-gives-root-privileges/
- **Severity:** critical
- **Tags:** `zero-day`, `privilege-escalation`, `vulnerability`, `cve`
- **Summary:** An unpatched Linux kernel LPE zero-day dubbed "Dirty Frag" allows local attackers to gain root on all major distributions with a single command; a public PoC has been released. It is a successor to Copy Fail (CVE-2026-31431), which is already under active exploitation in the wild.

### 2. ShinyHunters Breach Canvas Platform, Threaten 275M Education Records
- **Source:** Krebs on Security — https://krebsonsecurity.com/2026/05/canvas-breach-disrupts-schools-colleges-nationwide/
- **Severity:** critical
- **Tags:** `data-breach`, `ransomware`
- **Summary:** ShinyHunters defaced Canvas login portals across ~9,000 institutions and threatened to leak data for 275 million students and faculty unless a ransom is paid, disrupting classes nationwide. Instructure has not confirmed the breach vector or claimed data volume.

### 3. CVE-2025-68670: Pre-Auth RCE Found in xrdp Server
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/cve-2025-68670/119742/
- **Severity:** high
- **Tags:** `rce`, `cve`, `vulnerability`
- **Summary:** Kaspersky GReAT discovered CVE-2025-68670, a pre-authentication RCE in xrdp's server component. Project maintainers patched promptly; organizations using xrdp should update immediately.

### 4. Claude Chrome Extension Flaw Allows Prompt Injection and Agent Takeover
- **Source:** SecurityWeek — https://www.securityweek.com/vulnerability-in-claude-extension-for-chrome-exposes-ai-agent-to-takeover/
- **Severity:** high
- **Tags:** `llm`, `vulnerability`, `anthropic`
- **Summary:** Overly permissive extension permissions and improper trust validation in the Claude Chrome extension allow attackers to inject malicious prompts and take over AI agent sessions. Users should update to the latest extension version.

### 5. Ivanti Patches EPMM Zero-Day Under Active Targeted Exploitation
- **Source:** SecurityWeek — https://www.securityweek.com/ivanti-patches-epmm-zero-day-exploited-in-targeted-attacks/
- **Severity:** high
- **Tags:** `zero-day`, `rce`, `cve`, `vulnerability`
- **Summary:** Ivanti patched CVE-2026-6973 in EPMM after targeted exploitation; the flaw enables RCE for authenticated attackers with admin privileges. EPMM is widely deployed in enterprise and government environments.

### 6. TCLBanker Trojan Targets 59 Financial Platforms, Spreads via WhatsApp and Outlook
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-tclbanker-malware-self-spreads-over-whatsapp-and-outlook/
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Summary:** TCLBanker is a banking trojan delivered via a trojanized Logitech AI Prompt Builder installer, targeting 59 financial and crypto platforms, and self-propagates via WhatsApp and Outlook.

### 7. MuddyWater Uses Chaos Ransomware as Cover in Iranian APT Intrusion
- **Source:** The Record (Recorded Future) — https://therecord.media/iran-government-hackers-use-chaos-ransomware-as-cover
- **Severity:** high
- **Tags:** `ransomware`, `malware`
- **Summary:** Rapid7 attributed an intrusion initially appearing as Chaos ransomware to MuddyWater, an Iranian APT linked to MOIS. Using ransomware as cover for espionage is a deliberate tactic to delay attribution and incident response.

### 8. PCPJack Worm Steals Cloud Credentials While Evicting TeamPCP
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-pcpjack-worm-steals-credentials-cleans-teampcp-infections/
- **Severity:** high
- **Tags:** `malware`, `cloud-security`
- **Summary:** PCPJack targets exposed cloud infrastructure to steal credentials while actively removing competing TeamPCP infections. It uses parquet files for stealthy, pre-validated target discovery across multiple cloud environments.

### 9. RansomHouse Claims Breach of Cybersecurity Vendor Trellix
- **Source:** SecurityWeek — https://www.securityweek.com/ransomware-group-takes-credit-for-trellix-hack/
- **Severity:** medium
- **Tags:** `ransomware`, `data-breach`
- **Summary:** RansomHouse published screenshots claiming access to internal Trellix services; the claim is unverified. A confirmed breach of a major cybersecurity vendor would be significant.

### 10. OpenAI Launches Voice Intelligence Features in API
- **Source:** TechCrunch AI — https://techcrunch.com/2026/05/07/openai-launches-new-voice-intelligence-features-in-its-api/
- **Severity:** informational
- **Tags:** `openai`, `llm`, `ai-launch`
- **Summary:** OpenAI released new voice intelligence API features for customer service, education, and creator platforms, extending developer tooling into real-time voice processing.

## Skippable

- **MedQA: Fine-Tuning a Clinical AI on AMD ROCm** — Hugging Face Blog. Hackathon project tutorial; no security angle.
- **Linux Kernel Dirty Frag LPE Exploit** — The Hacker News. Duplicate of BleepingComputer's Dirty Frag coverage.
- **Why you can never get your doctor to call you back** — TechCrunch AI. AI/healthcare labor opinion piece; no security angle.
- **Canvas login portals hacked in mass ShinyHunters extortion campaign** — BleepingComputer. Duplicate of Krebs on Security's Canvas coverage.
- **Voi founders' new AI startup Pit** — TechCrunch AI. Non-security startup launch; no security angle.
- **After Replacing TeamPCP Malware, 'PCPJack' Steals Cloud Secrets** — Dark Reading. Duplicate of BleepingComputer's PCPJack coverage.
- **OpenAI introduces new 'Trusted Contact' safeguard** — TechCrunch AI. Product safety feature for self-harm detection; not a security vulnerability or incident.
- **Perplexity's Personal Computer is now available to everyone on Mac** — TechCrunch AI. Generic product availability; no security angle.
- **llm-gemini 0.31** — Simon Willison. Minor plugin release; minimal signal value.
- **Mira Murati's deposition pulled back the curtain on Sam Altman's ouster** — The Verge AI. Legal drama; no actionable security content.
- **Apple AirPods with cameras for AI are apparently close to production** — The Verge AI. Hardware product rumor; no security angle.
- **SpaceX has a $55 billion plan to build AI chips in Texas** — The Verge AI. Business/investment news; no security angle.
- **Elon Musk's lawsuit is putting OpenAI's safety record under the microscope** — TechCrunch AI. Legal/opinion piece; no new technical findings.
- **Worries About AI's Risks to Humanity Loom Over the Trial Pitting Musk Against OpenAI's Leaders** — SecurityWeek. Musk v. Altman trial coverage; no actionable security content.
- **Has CISA Finally Found Its New Leader in Tom Parker?** — Dark Reading. Unconfirmed leadership rumor; no actionable security content.
- **Bumble is getting rid of the swipe** — TechCrunch AI. Consumer app UI change; no security relevance.
- **ICYMI: April 2026 @AWS Security** — AWS Security Blog. Monthly marketing roundup; no new findings.
- **Big Words** — Simon Willison. Vibe-coded presentation tool; no security relevance.
