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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `microsoft`, `privilege-escalation`
- **Slug:** `2026-04-17-windows-zero-days-actively-exploited`
- **Must-know:** yes
- **Summary:** Three recently disclosed Windows vulnerabilities are now being actively exploited by threat actors to gain SYSTEM or elevated administrator permissions. Exploitation is in the wild and impacts Windows systems broadly; patching is urgent.

### 2. Apache ActiveMQ CVE-2026-34197 Added to CISA KEV, Actively Exploited
- **Source:** The Hacker News — https://thehackernews.com/2026/04/apache-activemq-cve-2026-34197-added-to.html (primary); BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-flags-apache-activemq-flaw-as-actively-exploited-in-attacks/ (secondary)
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `rce`, `vulnerability`
- **Slug:** `2026-04-17-apache-activemq-cve-2026-34197-cisa-kev`
- **Must-know:** no
- **Summary:** CVE-2026-34197, a high-severity RCE flaw (CVSS 8.8) in Apache ActiveMQ Classic that went undetected for 13 years, is now under active exploitation. CISA added it to the KEV catalog, requiring federal civilian agencies to patch by a set deadline.

### 3. Cursor AI Prompt Injection Chains to Sandbox Bypass and Shell Access
- **Source:** SecurityWeek — https://www.securityweek.com/cursor-ai-vulnerability-exposed-developer-devices/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `vulnerability`, `appsec`, `privilege-escalation`
- **Slug:** `2026-04-17-cursor-ai-prompt-injection-shell-access`
- **Must-know:** no
- **Summary:** A disclosed vulnerability in Cursor AI allows an indirect prompt injection to be chained with a sandbox bypass and the app's remote tunnel feature, resulting in full shell access to the developer's machine. The attack surface is any untrusted codebase or file opened in Cursor.

### 4. Trail of Bits Finds Memory Safety Bugs in Google's Quantum ZK Prover
- **Source:** Trail of Bits — https://blog.trailofbits.com/2026/04/17/we-beat-googles-zero-knowledge-proof-of-quantum-cryptanalysis/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`, `google`
- **Slug:** `2026-04-17-trailofbits-google-zkp-rust-vulns`
- **Must-know:** no
- **Summary:** Trail of Bits exploited multiple memory safety and logic vulnerabilities in Google's Rust zero-knowledge prover code to produce a significantly more efficient proof than Google's own, undermining the soundness of Google's published result. Google patched the prover; the underlying scientific claims about quantum cryptanalysis remain valid.

### 5. Windows April Patch Sends Domain Controllers into Reboot Loops
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-warns-of-reboot-loops-affecting-some-domain-controllers/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `microsoft`, `vulnerability`
- **Slug:** `2026-04-17-windows-april-patch-dc-reboot-loops`
- **Must-know:** no
- **Summary:** Microsoft confirmed that the April 2026 security updates are causing some Windows domain controllers to enter continuous reboot loops. Organizations with affected DCs should review Microsoft's guidance before applying the April patches to production AD environments.

### 6. ZionSiphon ICS Malware Targets Israeli Water Treatment Facilities
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/zionsiphon-malware-designed-to-sabotage-water-treatment-systems/ (primary); SecurityWeek — https://www.securityweek.com/zionsiphon-malware-targets-ics-in-water-facilities/ (secondary)
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `ics`
- **Slug:** `2026-04-16-zionsiphon-ics-water-treatment-malware`
- **Must-know:** no
- **Summary:** A new OT-targeted malware named ZionSiphon has been discovered, configured to sabotage Israeli water treatment and desalination plant control systems. The malware represents a significant threat to critical infrastructure operational technology environments.

### 7. North Korea IT Worker Scheme Facilitators Sentenced to US Prison
- **Source:** SecurityWeek — https://www.securityweek.com/two-north-korean-it-worker-scheme-facilitators-jailed-in-the-us/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `iam`
- **Slug:** `2026-04-17-north-korea-it-worker-facilitators-jailed`
- **Must-know:** no
- **Summary:** Two individuals—Kejia Wang and Zhenxing Wang—were sentenced to prison in the US for compromising the identities of dozens of Americans to help North Korean IT workers land jobs at over 100 US companies. The scheme is part of a broader North Korean effort to infiltrate tech firms via fake identities.

### 8. NIST Restricts NVD CVE Enrichment After 263% Submission Surge
- **Source:** The Hacker News — https://thehackernews.com/2026/04/nist-limits-cve-enrichment-after-263.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `cve`, `vulnerability`
- **Slug:** `2026-04-17-nist-nvd-cve-enrichment-limits`
- **Must-know:** no
- **Summary:** NIST has announced it will only enrich a subset of CVEs in the National Vulnerability Database due to a 263% surge in vulnerability submissions. CVEs that don't meet new criteria will still be listed but without enrichment metadata, affecting automated tooling that relies on NVD for CVSS scores and CWE mappings.

### 9. Operation PowerOFF Seizes 53 DDoS-for-Hire Domains, Exposes 3M Accounts
- **Source:** The Hacker News — https://thehackernews.com/2026/04/operation-poweroff-seizes-53-ddos.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `2026-04-17-operation-poweroff-53-ddos-domains`
- **Must-know:** no
- **Summary:** An international law enforcement operation spanning 21 countries seized 53 DDoS-for-hire domains, arrested four individuals, and exposed account data for approximately 3 million users of criminal booter services. Over 75,000 cybercriminals had used the dismantled infrastructure.

### 10. Unit 42: Active Mirai Exploitation of TP-Link Command Injection CVE-2023-33538
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/exploitation-of-cve-2023-33538/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `cve`, `rce`, `malware`, `vulnerability`
- **Slug:** `2026-04-16-tplink-cve-2023-33538-mirai-exploitation`
- **Must-know:** no
- **Summary:** Unit 42 published a deep-dive on ongoing exploitation attempts targeting CVE-2023-33538, a command injection flaw in TP-Link routers, with payloads characteristic of Mirai botnet campaigns. Despite the CVE being from 2023, exploitation activity remains active against unpatched devices.

## Skippable

- **Google Blocks 8.3B Policy-Violating Ads in 2025, Launches Android 17 Privacy Overhaul** — The Hacker News. Ad policy statistics and Android permission update announcement; no security incident or technical vulnerability.
- **Another DraftKings Hacker Sentenced to Prison** — SecurityWeek. Legal sentencing update for a 2022 breach; covered more completely by BleepingComputer item #12, and both are skippable as legal-only updates without technical substance.
- **Lawmakers Gathered Quietly to Talk About AI. Angst and Fears of 'Destruction' Followed** — SecurityWeek. Opinion/policy piece with no actionable technical news.
- **Recent Apache ActiveMQ Vulnerability Exploited in the Wild** — SecurityWeek. Duplicate coverage of CVE-2026-34197; consolidated into post using THN and BleepingComputer as sources.
- **CISA flags Apache ActiveMQ flaw as actively exploited in attacks** — BleepingComputer. Duplicate coverage of CVE-2026-34197; cited as secondary source in consolidated post.
- **Man gets 30 months for selling thousands of hacked DraftKings accounts** — BleepingComputer. Legal sentencing update for a 2022 breach; no technical substance.
- **53 DDoS Domains Taken Down by Law Enforcement** — SecurityWeek. Duplicate of Operation PowerOFF coverage; consolidated into post using THN as primary source.
- **datasette 1.0a28** — Simon Willison. Python data tool alpha release; no security relevance.
- **Factory hits $1.5B valuation to build AI coding for enterprises** — TechCrunch AI. Startup funding news; no security angle.
- **Operation PowerOFF identifies 75k DDoS users, takes down 53 domains** — BleepingComputer. Duplicate of Operation PowerOFF coverage; THN version chosen as primary source.
- **ZionSiphon malware designed to sabotage water treatment systems** — BleepingComputer. Listed as primary source in ZionSiphon post; SecurityWeek version skipped as duplicate.
- **Luma launches AI-powered production studio with faith-focused Wonder Project** — TechCrunch AI. AI entertainment content with no security or technical relevance.
