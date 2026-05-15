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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `privilege-escalation`, `vulnerability`, `cve`
- **Slug:** `2026-05-08-dirty-frag-linux-kernel-lpe-zero-day`
- **Must-know:** no
- **Summary:** An unpatched Linux kernel LPE zero-day dubbed "Dirty Frag" allows local attackers to gain root on all major distributions with a single command; a public PoC has been released. It is described as a successor to Copy Fail (CVE-2026-31431), which is already under active exploitation in the wild, and no patch has been issued yet.

### 2. ShinyHunters Breach Canvas Platform, Threaten 275M Education Records
- **Source:** Krebs on Security — https://krebsonsecurity.com/2026/05/canvas-breach-disrupts-schools-colleges-nationwide/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `data-breach`, `ransomware`
- **Slug:** `2026-05-08-canvas-instructure-shinyhunters-275m-breach`
- **Must-know:** yes
- **Summary:** ShinyHunters defaced Canvas login portals across ~9,000 institutions and threatened to leak data for 275 million students and faculty unless a ransom is paid; classes were disrupted nationwide today. Instructure has not yet confirmed the breach vector or the claimed data volume.

### 3. CVE-2025-68670: Pre-Auth RCE Found in xrdp Server
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/cve-2025-68670/119742/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `2026-05-08-cve-2025-68670-xrdp-pre-auth-rce`
- **Must-know:** no
- **Summary:** Kaspersky GReAT found CVE-2025-68670, a pre-authentication RCE in xrdp's server component, during an internal security assessment. Project maintainers patched promptly; organizations using xrdp for Linux remote desktop access should update immediately.

### 4. Claude Chrome Extension Flaw Allows Prompt Injection and Agent Takeover
- **Source:** SecurityWeek — https://www.securityweek.com/vulnerability-in-claude-extension-for-chrome-exposes-ai-agent-to-takeover/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `vulnerability`, `anthropic`
- **Slug:** `2026-05-08-claude-chrome-extension-prompt-injection-takeover`
- **Must-know:** no
- **Summary:** Overly permissive extension permissions and improper trust validation in the Claude Chrome extension allow attackers to inject malicious prompts and take over the AI agent session. Users should update to the latest extension version and review site permissions granted to the extension.

### 5. Ivanti Patches EPMM Zero-Day Under Active Targeted Exploitation
- **Source:** SecurityWeek — https://www.securityweek.com/ivanti-patches-epmm-zero-day-exploited-in-targeted-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `rce`, `cve`, `vulnerability`
- **Slug:** `2026-05-08-ivanti-epmm-zero-day-cve-2026-6973-targeted-attacks`
- **Must-know:** no
- **Summary:** Ivanti patched CVE-2026-6973 in EPMM after it was exploited in targeted attacks; the flaw enables RCE for an authenticated attacker with admin privileges. EPMM is widely used for mobile device management in enterprise and government environments.

### 6. TCLBanker Trojan Targets 59 Financial Platforms, Spreads via WhatsApp and Outlook
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-tclbanker-malware-self-spreads-over-whatsapp-and-outlook/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Slug:** `2026-05-07-tclbanker-banking-trojan-whatsapp-outlook`
- **Must-know:** no
- **Summary:** TCLBanker is a new banking trojan distributed via a trojanized MSI installer for Logitech AI Prompt Builder, targeting 59 banking, fintech, and cryptocurrency platforms. It self-propagates through WhatsApp and Outlook, significantly broadening its reach beyond the initial infection vector.

### 7. MuddyWater Uses Chaos Ransomware as Cover in Iranian APT Intrusion
- **Source:** The Record (Recorded Future) — https://therecord.media/iran-government-hackers-use-chaos-ransomware-as-cover
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`, `malware`
- **Slug:** `2026-05-07-muddywater-chaos-ransomware-cover-iran-apt`
- **Must-know:** no
- **Summary:** Rapid7 attributed an intrusion initially appearing to be a Chaos ransomware attack to MuddyWater, an Iranian APT linked to Iran's Ministry of Intelligence and Security. Using ransomware as a cover for state-sponsored espionage muddies attribution and delays incident response.

### 8. PCPJack Worm Steals Cloud Credentials While Evicting TeamPCP
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-pcpjack-worm-steals-credentials-cleans-teampcp-infections/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `cloud-security`
- **Slug:** `2026-05-07-pcpjack-worm-cloud-credential-theft`
- **Must-know:** no
- **Summary:** PCPJack is a new malware framework targeting exposed cloud infrastructure to steal credentials while actively removing competing TeamPCP infections from compromised hosts. It uses parquet files for stealthy, pre-validated target discovery across multiple cloud environments.

### 9. RansomHouse Claims Breach of Cybersecurity Vendor Trellix
- **Source:** SecurityWeek — https://www.securityweek.com/ransomware-group-takes-credit-for-trellix-hack/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ransomware`, `data-breach`
- **Slug:** `2026-05-08-ransomhouse-trellix-ransomware-hack-claim`
- **Must-know:** no
- **Summary:** RansomHouse published screenshots claiming to demonstrate access to internal Trellix services; Trellix has not confirmed the breach. A confirmed compromise of a major cybersecurity vendor would be significant, but the claim is unverified as of this digest.

### 10. OpenAI Launches Voice Intelligence Features in API
- **Source:** TechCrunch AI — https://techcrunch.com/2026/05/07/openai-launches-new-voice-intelligence-features-in-its-api/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `openai`, `llm`, `ai-launch`
- **Slug:** `2026-05-07-openai-voice-intelligence-api-launch`
- **Must-know:** no
- **Summary:** OpenAI released new voice intelligence API features targeting customer service, education, and creator platforms. The capabilities extend developer tooling beyond text into real-time voice processing.

## Skippable

- **MedQA: Fine-Tuning a Clinical AI on AMD ROCm** — Hugging Face Blog. Hackathon project tutorial; no security angle.
- **Linux Kernel Dirty Frag LPE Exploit** — The Hacker News. Duplicate of BleepingComputer coverage of the same Dirty Frag zero-day.
- **Why you can never get your doctor to call you back** — TechCrunch AI. AI/healthcare labor displacement opinion; no security angle.
- **Canvas login portals hacked in mass ShinyHunters extortion campaign** — BleepingComputer. Duplicate of Krebs on Security's Canvas breach coverage.
- **Voi founders' new AI startup Pit** — TechCrunch AI. Non-security SaaS startup launch; no security angle.
- **After Replacing TeamPCP Malware, 'PCPJack' Steals Cloud Secrets** — Dark Reading. Duplicate of BleepingComputer's PCPJack coverage.
- **OpenAI introduces new 'Trusted Contact' safeguard** — TechCrunch AI. Product safety feature for self-harm detection; not a security vulnerability or incident.
- **Perplexity's Personal Computer is now available to everyone on Mac** — TechCrunch AI. Generic product availability; no security angle.
- **llm-gemini 0.31** — Simon Willison. Minor plugin release noting Gemini 3.1 Flash-Lite left preview; minimal signal value.
- **Mira Murati's deposition pulled back the curtain on Sam Altman's ouster** — The Verge AI. Legal drama/governance retrospective; no actionable security content.
- **Apple AirPods with cameras for AI are apparently close to production** — The Verge AI. Hardware product rumor; no security angle.
- **SpaceX has a $55 billion plan to build AI chips in Texas** — The Verge AI. Business/investment news; no security angle.
- **Elon Musk's lawsuit is putting OpenAI's safety record under the microscope** — TechCrunch AI. Legal/opinion piece without new technical findings.
- **Worries About AI's Risks to Humanity Loom Over the Trial Pitting Musk Against OpenAI's Leaders** — SecurityWeek. Musk v. Altman trial coverage; no actionable security content.
- **Has CISA Finally Found Its New Leader in Tom Parker?** — Dark Reading. Unconfirmed CISA leadership rumor; no actionable security content.
- **Bumble is getting rid of the swipe** — TechCrunch AI. Consumer app UI change; no security relevance.
- **ICYMI: April 2026 @AWS Security** — AWS Security Blog. Monthly marketing roundup; no new findings.
- **Big Words** — Simon Willison. Vibe-coded presentation tool; no security relevance.
