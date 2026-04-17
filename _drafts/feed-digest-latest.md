# Digest — 2026-04-17 AM

- Window: last 14h
- Raw items considered: 22
- Relevant: 10
- Skippable: 12

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Windows Zero-Days Leaked, Now Actively Exploited for SYSTEM Privileges — `2026-04-17-windows-zero-days-actively-exploited.md`
- [x] **[CRITICAL]** Apache ActiveMQ CVE-2026-34197 Added to CISA KEV, Actively Exploited — `2026-04-17-apache-activemq-cve-2026-34197-cisa-kev.md`
- [x] **[HIGH]** Cursor AI Prompt Injection Chains to Sandbox Bypass and Shell Access — `2026-04-17-cursor-ai-prompt-injection-shell-access.md`
- [x] **[HIGH]** Trail of Bits Finds Memory Safety Bugs in Google's Quantum ZK Prover — `2026-04-17-trailofbits-google-zkp-rust-vulns.md`
- [x] **[HIGH]** Windows April Patch Sends Domain Controllers into Reboot Loops — `2026-04-17-windows-april-patch-dc-reboot-loops.md`
- [x] **[HIGH]** ZionSiphon ICS Malware Targets Israeli Water Treatment Facilities — `2026-04-16-zionsiphon-ics-water-treatment-malware.md`
- [x] **[HIGH]** North Korea IT Worker Scheme Facilitators Sentenced to US Prison — `2026-04-17-north-korea-it-worker-facilitators-jailed.md`
- [x] **[MEDIUM]** NIST Restricts NVD CVE Enrichment After 263% Submission Surge — `2026-04-17-nist-nvd-cve-enrichment-limits.md`
- [x] **[MEDIUM]** Operation PowerOFF Seizes 53 DDoS-for-Hire Domains, Exposes 3M Accounts — `2026-04-17-operation-poweroff-53-ddos-domains.md`
- [x] **[MEDIUM]** Unit 42: Active Mirai Exploitation of TP-Link Command Injection CVE-2023-33538 — `2026-04-16-tplink-cve-2023-33538-mirai-exploitation.md`

## Relevant (details)

### 1. Windows Zero-Days Leaked, Now Actively Exploited for SYSTEM Privileges
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/recently-leaked-windows-zero-days-now-exploited-in-attacks/
- **Severity:** critical
- **Tags:** `zero-day`, `microsoft`, `privilege-escalation`
- **Summary:** Three recently disclosed Windows vulnerabilities are now being actively exploited by threat actors to gain SYSTEM or elevated administrator permissions. Exploitation is in the wild; patching is urgent.

### 2. Apache ActiveMQ CVE-2026-34197 Added to CISA KEV, Actively Exploited
- **Source:** The Hacker News — https://thehackernews.com/2026/04/apache-activemq-cve-2026-34197-added-to.html
- **Severity:** critical
- **Tags:** `cve`, `rce`, `vulnerability`
- **Summary:** CVE-2026-34197, a CVSS 8.8 RCE flaw in Apache ActiveMQ Classic undetected for 13 years, is under active exploitation. CISA added it to the KEV catalog requiring federal civilian agencies to patch.

### 3. Cursor AI Prompt Injection Chains to Sandbox Bypass and Shell Access
- **Source:** SecurityWeek — https://www.securityweek.com/cursor-ai-vulnerability-exposed-developer-devices/
- **Severity:** high
- **Tags:** `llm`, `vulnerability`, `appsec`, `privilege-escalation`
- **Summary:** An indirect prompt injection in Cursor AI can be chained with a sandbox bypass and the app's remote tunnel feature to achieve full shell access to the developer's machine. Any untrusted codebase or file opened in Cursor is a potential attack vector.

### 4. Trail of Bits Finds Memory Safety Bugs in Google's Quantum ZK Prover
- **Source:** Trail of Bits — https://blog.trailofbits.com/2026/04/17/we-beat-googles-zero-knowledge-proof-of-quantum-cryptanalysis/
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`, `google`
- **Summary:** Trail of Bits exploited memory safety and logic vulnerabilities in Google's Rust ZK prover to produce a more efficient proof than Google's own, undermining the soundness of the published result. Google patched the prover; the underlying quantum cryptanalysis claims remain valid.

### 5. Windows April Patch Sends Domain Controllers into Reboot Loops
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-warns-of-reboot-loops-affecting-some-domain-controllers/
- **Severity:** high
- **Tags:** `microsoft`, `vulnerability`
- **Summary:** Microsoft confirmed the April 2026 security updates are causing some Windows domain controllers to enter continuous reboot loops. AD-dependent organizations should review guidance before applying April patches to production.

### 6. ZionSiphon ICS Malware Targets Israeli Water Treatment Facilities
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/zionsiphon-malware-designed-to-sabotage-water-treatment-systems/
- **Severity:** high
- **Tags:** `malware`, `ics`
- **Summary:** ZionSiphon is a new OT-targeted malware configured to sabotage Israeli water treatment and desalination plant control systems. It represents a significant threat to critical infrastructure OT environments.

### 7. North Korea IT Worker Scheme Facilitators Sentenced to US Prison
- **Source:** SecurityWeek — https://www.securityweek.com/two-north-korean-it-worker-scheme-facilitators-jailed-in-the-us/
- **Severity:** high
- **Tags:** `supply-chain`, `iam`
- **Summary:** Kejia Wang and Zhenxing Wang were sentenced for compromising dozens of American identities to help North Korean IT workers infiltrate over 100 US companies. The case is part of a broader NK effort to embed workers inside tech firms.

### 8. NIST Restricts NVD CVE Enrichment After 263% Submission Surge
- **Source:** The Hacker News — https://thehackernews.com/2026/04/nist-limits-cve-enrichment-after-263.html
- **Severity:** medium
- **Tags:** `cve`, `vulnerability`
- **Summary:** NIST will only enrich a subset of CVEs in the NVD due to a 263% explosion in submissions. Unenriched entries will lack CVSS scores and CWE data, affecting security tools and workflows that depend on NVD metadata.

### 9. Operation PowerOFF Seizes 53 DDoS-for-Hire Domains, Exposes 3M Accounts
- **Source:** The Hacker News — https://thehackernews.com/2026/04/operation-poweroff-seizes-53-ddos.html
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** A 21-country law enforcement operation seized 53 DDoS-for-hire domains, arrested four people, and exposed account data for ~3 million users of criminal booter services used by over 75,000 cybercriminals.

### 10. Unit 42: Active Mirai Exploitation of TP-Link Command Injection CVE-2023-33538
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/exploitation-of-cve-2023-33538/
- **Severity:** medium
- **Tags:** `cve`, `rce`, `malware`, `vulnerability`
- **Summary:** Unit 42 documented ongoing exploitation of CVE-2023-33538, a command injection flaw in TP-Link routers, with Mirai botnet payloads. Despite the CVE dating to 2023, exploitation activity persists against unpatched devices.

## Skippable

- **Google Blocks 8.3B Policy-Violating Ads in 2025, Launches Android 17 Privacy Overhaul** — The Hacker News. Ad policy statistics and Android permission update; no security incident.
- **Another DraftKings Hacker Sentenced to Prison** — SecurityWeek. Legal sentencing for a 2022 breach; no new technical substance.
- **Lawmakers Gathered Quietly to Talk About AI. Angst and Fears of 'Destruction' Followed** — SecurityWeek. Opinion/policy piece, no actionable news.
- **Recent Apache ActiveMQ Vulnerability Exploited in the Wild** — SecurityWeek. Duplicate of CVE-2026-34197 coverage; consolidated into single post.
- **CISA flags Apache ActiveMQ flaw as actively exploited in attacks** — BleepingComputer. Duplicate of CVE-2026-34197 coverage; cited as secondary source.
- **Man gets 30 months for selling thousands of hacked DraftKings accounts** — BleepingComputer. Legal sentencing for a 2022 breach; no technical substance.
- **53 DDoS Domains Taken Down by Law Enforcement** — SecurityWeek. Duplicate of Operation PowerOFF; THN version used as primary.
- **datasette 1.0a28** — Simon Willison. Python data tool alpha release; no security relevance.
- **Factory hits $1.5B valuation to build AI coding for enterprises** — TechCrunch AI. Startup funding news; no security angle.
- **Operation PowerOFF identifies 75k DDoS users, takes down 53 domains** — BleepingComputer. Duplicate of Operation PowerOFF; THN version used as primary.
- **ZionSiphon malware designed to sabotage water treatment systems** — BleepingComputer. Used as primary source in ZionSiphon post; SecurityWeek version skipped as duplicate.
- **Luma launches AI-powered production studio with faith-focused Wonder Project** — TechCrunch AI. AI entertainment content; no security relevance.
