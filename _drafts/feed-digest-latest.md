# Digest — 2026-05-06 AM

- Window: last 14h
- Raw items considered: 22
- Relevant: 9
- Skippable: 13

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** DAEMON Tools Trojanized in Supply Chain Attack to Deploy Backdoor — `2026-05-05-daemon-tools-supply-chain-backdoor.md`
- [x] **[CRITICAL]** Palo Alto PAN-OS Zero-Day CVE-2026-0300 Under Active Exploitation — `2026-05-06-panos-cve-2026-0300-rce-active-exploitation.md`
- [x] **[CRITICAL]** Copy Fail: Critical Linux Kernel LPE CVE-2026-31431 Impacts Millions of Systems — `2026-05-05-copy-fail-cve-2026-31431-linux-lpe.md`
- [x] **[HIGH]** New Quasar Linux Malware Targets Software Developers with Rootkit and Backdoor — `2026-05-05-quasar-linux-malware-developers.md`
- [x] **[HIGH]** Trellix Source Code Breach Exposes Security Product Internals — `2026-05-05-trellix-source-code-breach-supply-chain.md`
- [x] **[HIGH]** Hacker Claims 280 Million Records Stolen from Instructure Across 8,800 Schools — `2026-05-05-instructure-data-breach-280m-records.md`
- [x] **[MEDIUM]** Middle East Cyber Conflict Escalates as UAE Critical Infrastructure Faces Triple Breach Attempts — `2026-05-06-middle-east-uae-cyber-escalation.md`
- [x] **[INFORMATIONAL]** Oracle Shifts to Monthly Critical Security Patch Updates — `2026-05-06-oracle-monthly-critical-patch-updates.md`
- [x] **[INFORMATIONAL]** Apple Plans Third-Party AI Model Integration System-Wide in iOS 27 — `2026-05-05-apple-ios-27-third-party-ai-models.md`

## Relevant (details)

### 1. DAEMON Tools Trojanized in Supply Chain Attack to Deploy Backdoor
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/daemon-tools-trojanized-in-supply-chain-attack-to-deploy-backdoor/
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`
- **Summary:** Attackers trojanized official DAEMON Tools installers served from the official website since April 8, delivering a backdoor to thousands of systems. The backdoor was selectively activated only on roughly a dozen government and scientific targets — a targeted espionage campaign nested inside a broad supply chain compromise.

### 2. Palo Alto PAN-OS Zero-Day CVE-2026-0300 Under Active Exploitation
- **Source:** The Hacker News — https://thehackernews.com/2026/05/palo-alto-pan-os-flaw-under-active.html
- **Severity:** critical
- **Tags:** `zero-day`, `rce`, `vulnerability`, `cve`
- **Summary:** CVE-2026-0300 (CVSS 9.3) is a critical buffer overflow in PAN-OS enabling unauthenticated RCE, actively exploited in the wild. Affects Captive Portal and User-ID Authentication Portal on PA and VM series firewalls when internet-exposed.

### 3. Copy Fail: Critical Linux Kernel LPE CVE-2026-31431 Impacts Millions of Systems
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/cve-2026-31431-copy-fail/
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Summary:** CVE-2026-31431 ("Copy Fail") is a critical Linux kernel LPE granting stealthy root access, impacting millions of systems. Unit 42 calls it the most severe Linux threat in years; no confirmed active exploitation yet, but urgency to patch is high.

### 4. New Quasar Linux Malware Targets Software Developers with Rootkit and Backdoor
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-stealthy-quasar-linux-malware-targets-software-developers/
- **Severity:** high
- **Tags:** `malware`, `supply-chain`
- **Summary:** Quasar Linux (QLNX) is a newly discovered implant combining rootkit, backdoor, and credential theft, targeting software developers. Compromised developer machines pose direct supply chain risk through poisoned commits and stolen credentials.

### 5. Trellix Source Code Breach Exposes Security Product Internals
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/trellix-source-code-breach-supply-chain-threats
- **Severity:** high
- **Tags:** `supply-chain`, `data-breach`
- **Summary:** Trellix suffered a source code breach with limited details; access to security product source exposes detection logic and evasion paths to attackers. Continues a pattern of security vendors being targeted to undermine defensive tooling.

### 6. Hacker Claims 280 Million Records Stolen from Instructure Across 8,800 Schools
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/instructure-hacker-claims-data-theft-from-8-800-schools-universities/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** A threat actor claims 280 million student and staff records exfiltrated from 8,809 institutions via Instructure (Canvas LMS). Claim unverified; if accurate, would rank among the largest education-sector breaches on record.

### 7. Middle East Cyber Conflict Escalates as UAE Critical Infrastructure Faces Triple Breach Attempts
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/middle-east-cyber-battle-field-broadens-uae
- **Severity:** medium
- **Tags:** `critical-infrastructure`
- **Summary:** Breach attempts against UAE critical infrastructure tripled within weeks, aligning with regional tensions and indicating state-affiliated actors broadening cyber operations into Gulf nations.

### 8. Oracle Shifts to Monthly Critical Security Patch Updates
- **Source:** SecurityWeek — https://www.securityweek.com/oracle-debuts-monthly-critical-security-patch-updates/
- **Severity:** informational
- **Tags:** `vulnerability`
- **Summary:** Oracle adds a monthly critical patch release cadence for the highest-severity vulnerabilities, supplementing its quarterly CPU. Practitioners should update patching workflows accordingly.

### 9. Apple Plans Third-Party AI Model Integration System-Wide in iOS 27
- **Source:** TechCrunch AI — https://techcrunch.com/2026/05/05/apple-plans-to-make-ios-27-a-choose-your-own-adventure-of-ai-models/
- **Severity:** informational
- **Tags:** `ai-launch`, `llm`
- **Summary:** Apple reportedly plans to allow users to select third-party AI models for system-wide Apple Intelligence tasks in iOS 27, iPadOS 27, and macOS 27. Raises data access and sandboxing questions as external models gain deeper OS integration.

## Skippable

- **Peter Sarlin's QuTwo reaches $380M valuation** — TechCrunch AI. AI startup funding with no security angle.
- **Marc Lore: AI will enable anyone to open a restaurant** — TechCrunch AI. Opinion/marketing piece, no security relevance.
- **Palo Alto Networks to Patch Zero-Day Exploited to Hack Firewalls** — SecurityWeek. Duplicate of CVE-2026-0300 coverage; The Hacker News selected as primary.
- **SAP bets $1.16B on German AI lab and says yes to NemoClaw** — TechCrunch AI. Corporate acquisition, no security or model-launch angle.
- **datasette-referrer-policy 0.1** — Simon Willison. Minor library release, no security relevance.
- **Altara secures $7M to bridge the data gap in physical sciences** — TechCrunch AI. AI startup funding, no security angle.
- **Our AI started a cafe in Stockholm** — Simon Willison. Autonomous AI experiment, no security news value.
- **Google Home's Gemini AI can handle more complicated requests** — The Verge AI. Incremental assistant update, not a significant model launch.
- **Apple agrees to pay $250M for not delivering AI Siri** — The Verge AI. Legal settlement, no security incident.
- **ASML CEO on his company's monopoly** — TechCrunch AI. Executive interview, no security or AI launch news.
- **Microsoft gives up on Xbox Copilot AI** — The Verge AI. Product wind-down, no security relevance.
- **Apple could let you pick a favorite AI model in iOS 27** — The Verge AI. Duplicate of TechCrunch iOS 27 coverage; TechCrunch selected as primary.
- **Government, Scientific Entities Hit via Daemon Tools Supply Chain Attack** — SecurityWeek. Duplicate of Daemon Tools coverage; both sources cited in primary post.
