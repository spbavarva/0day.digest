# Digest — 2026-05-18 AM

- Window: last 14h
- Raw items considered: 13
- Relevant: 7
- Skippable: 6

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Exploitation of Critical NGINX Vulnerability Begins — `2026-05-18-nginx-critical-rce-active-exploitation.md`
- [x] **[HIGH]** MiniPlasma Windows Zero-Day Grants SYSTEM Privileges on Fully Patched Systems — `2026-05-18-miniplasma-windows-zero-day-poc-system-escalation.md`
- [x] **[HIGH]** Four Malicious npm Packages Deliver Infostealers and Shai-Hulud Worm Clones — `2026-05-18-shai-hulud-worm-clones-npm-infostealer.md`
- [x] **[HIGH]** Grafana Confirms Data Breach Claimed by Coinbase Cartel — `2026-05-18-grafana-breach-coinbase-cartel-shinyhunters.md`
- [x] **[HIGH]** DirtyDecrypt: Public PoC Released for Linux Kernel Root Escalation Flaw — `2026-05-18-dirtydecrypt-linux-root-escalation-poc.md`
- [x] **[MEDIUM]** Analysis: Pre-Stuxnet Fast16 Malware Was Engineered to Corrupt Nuclear Weapons Simulations — `2026-05-18-fast16-pre-stuxnet-nuclear-simulation-tampering.md`
- [x] **[MEDIUM]** Pwn2Own Berlin 2026: $1.3M Paid for 47 Zero-Days in Windows, Linux, VMware, and AI Products — `2026-05-18-pwn2own-berlin-2026-47-zero-days.md`

## Relevant (details)

### 1. Exploitation of Critical NGINX Vulnerability Begins
- **Source:** SecurityWeek — https://www.securityweek.com/exploitation-of-critical-nginx-vulnerability-begins/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`, `nginx`
- **Slug:** `2026-05-18-nginx-critical-rce-active-exploitation`
- **Must-know:** yes
- **Summary:** Active exploitation of a critical NGINX vulnerability has begun, causing denial-of-service on default configurations and enabling RCE when ASLR is disabled. NGINX's ubiquity as a web server and reverse proxy makes patch urgency high.

### 2. MiniPlasma Windows Zero-Day Grants SYSTEM Privileges on Fully Patched Systems
- **Source:** The Hacker News — https://thehackernews.com/2026/05/miniplasma-windows-0-day-enables-system.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `privilege-escalation`, `vulnerability`, `microsoft`
- **Slug:** `2026-05-18-miniplasma-windows-zero-day-poc-system-escalation`
- **Must-know:** no
- **Summary:** Researcher "Chaotic Eclipse" released a public PoC for MiniPlasma, an unpatched Windows zero-day targeting `cldflt.sys` that grants SYSTEM privileges on fully patched systems. This is the third Windows flaw from the same researcher after YellowKey and GreenPlasma.

### 3. Four Malicious npm Packages Deliver Infostealers and Shai-Hulud Worm Clones
- **Source:** The Hacker News — https://thehackernews.com/2026/05/four-malicious-npm-packages-deliver.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `malware`
- **Slug:** `2026-05-18-shai-hulud-worm-clones-npm-infostealer`
- **Must-know:** no
- **Summary:** Four malicious npm packages were found delivering infostealers and a Phantom Bot DDoS component, with one package being a clone of the Shai-Hulud worm open-sourced by TeamPCP. The packages had ~3,000 combined downloads before removal.

### 4. Grafana Confirms Data Breach Claimed by Coinbase Cartel
- **Source:** SecurityWeek — https://www.securityweek.com/grafana-confirms-breach-after-hackers-claim-they-stole-data/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `grafana`
- **Slug:** `2026-05-18-grafana-breach-coinbase-cartel-shinyhunters`
- **Must-know:** no
- **Summary:** Grafana confirmed a breach after the Coinbase Cartel (linked to ShinyHunters, Scattered Spider, Lapsus$) claimed to have stolen data. Grafana is widely deployed for observability dashboards, making its credential and configuration data particularly valuable to attackers.

### 5. DirtyDecrypt: Public PoC Released for Linux Kernel Root Escalation Flaw
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/exploit-available-for-new-dirtydecrypt-linux-root-escalation-flaw/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`, `cve`, `linux`, `container-security`
- **Slug:** `2026-05-18-dirtydecrypt-linux-root-escalation-poc`
- **Must-know:** no
- **Summary:** A public PoC exploit now exists for DirtyDecrypt, a recently patched local privilege escalation in the Linux kernel's `rxgk` module that grants root access. Container environments and multi-tenant hosts are at heightened risk given the availability of a working exploit.

### 6. Analysis: Pre-Stuxnet Fast16 Malware Was Engineered to Corrupt Nuclear Weapons Simulations
- **Source:** The Hacker News — https://thehackernews.com/2026/05/pre-stuxnet-fast16-malware-tampered.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `apt`
- **Slug:** `2026-05-18-fast16-pre-stuxnet-nuclear-simulation-tampering`
- **Must-know:** no
- **Summary:** Symantec and Carbon Black analysis confirmed that the Lua-based `fast16` was a pre-Stuxnet cyber sabotage tool designed to silently corrupt uranium-compression simulations. The findings extend the documented timeline of state-sponsored critical-process sabotage.

### 7. Pwn2Own Berlin 2026: $1.3M Paid for 47 Zero-Days in Windows, Linux, VMware, and AI Products
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-earn-1-298-250-for-47-zero-days-at-pwn2own-berlin-2026/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `zero-day`, `vulnerability`, `ai-safety`
- **Slug:** `2026-05-18-pwn2own-berlin-2026-47-zero-days`
- **Must-know:** no
- **Summary:** Pwn2Own Berlin 2026 concluded with $1,298,250 paid for 47 zero-days across Windows, Linux, VMware, Nvidia, and AI products. Vendors have 90 days to patch; expect a wave of CVEs against these product families in the coming weeks.

## Skippable

- **Researcher Drops MiniPlasma Windows Exploit for Unpatched 2020 CVE** — SecurityWeek. Duplicate coverage of the MiniPlasma zero-day; The Hacker News item (above) has more technical detail.
- **First Shai-Hulud Worm Clones Emerge** — SecurityWeek. Duplicate coverage of the malicious npm packages / Shai-Hulud clones story; The Hacker News item (above) lists specific package names and download counts.
- **Microsoft confirms Windows 11 security update install issues** — BleepingComputer. Patch deployment failure (KB5089549 error 0x800f0922), not a security vulnerability or new threat.
- **Hackers Earn $1.3 Million at Pwn2Own Berlin 2026** — SecurityWeek. Duplicate of the BleepingComputer Pwn2Own item (above) with less detail.
- **Can Laws Stop Deepfakes? South Korea Aims to Find Out** — Dark Reading. Policy opinion piece about South Korea election deepfake regulation; no actionable technical security news.
- **New Windows 'MiniPlasma' zero-day exploit gives SYSTEM access, PoC released** — BleepingComputer. Duplicate coverage of the MiniPlasma zero-day; The Hacker News item (above) selected as primary source.
