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
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`, `nginx`
- **Summary:** Active exploitation of a critical NGINX vulnerability has begun, causing denial-of-service on default configurations and enabling RCE when ASLR is disabled. Patch immediately; NGINX's ubiquity makes this high-priority.

### 2. MiniPlasma Windows Zero-Day Grants SYSTEM Privileges on Fully Patched Systems
- **Source:** The Hacker News — https://thehackernews.com/2026/05/miniplasma-windows-0-day-enables-system.html
- **Severity:** high
- **Tags:** `zero-day`, `privilege-escalation`, `vulnerability`, `microsoft`
- **Summary:** Researcher "Chaotic Eclipse" released a public PoC for MiniPlasma, an unpatched Windows zero-day targeting `cldflt.sys` that grants SYSTEM privileges on fully patched systems — the third Windows flaw from this researcher.

### 3. Four Malicious npm Packages Deliver Infostealers and Shai-Hulud Worm Clones
- **Source:** The Hacker News — https://thehackernews.com/2026/05/four-malicious-npm-packages-deliver.html
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `malware`
- **Summary:** Four malicious npm packages delivering infostealers and a Phantom Bot DDoS component were found, with one being a Shai-Hulud worm clone from TeamPCP. Combined ~3,000 downloads before removal; audit `package.json` for these package names.

### 4. Grafana Confirms Data Breach Claimed by Coinbase Cartel
- **Source:** SecurityWeek — https://www.securityweek.com/grafana-confirms-breach-after-hackers-claim-they-stole-data/
- **Severity:** high
- **Tags:** `data-breach`, `grafana`
- **Summary:** Grafana confirmed a breach attributed to the Coinbase Cartel (ShinyHunters / Scattered Spider / Lapsus$ linked). Grafana Cloud and Enterprise users should rotate API tokens and datasource credentials.

### 5. DirtyDecrypt: Public PoC Released for Linux Kernel Root Escalation Flaw
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/exploit-available-for-new-dirtydecrypt-linux-root-escalation-flaw/
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`, `cve`, `linux`, `container-security`
- **Summary:** A public PoC now exists for DirtyDecrypt, a patched local privilege escalation in the Linux kernel's `rxgk` module granting root access. Container environments and multi-tenant hosts are at heightened risk.

### 6. Analysis: Pre-Stuxnet Fast16 Malware Was Engineered to Corrupt Nuclear Weapons Simulations
- **Source:** The Hacker News — https://thehackernews.com/2026/05/pre-stuxnet-fast16-malware-tampered.html
- **Severity:** medium
- **Tags:** `malware`, `apt`
- **Summary:** Symantec and Carbon Black confirmed `fast16` was a pre-Stuxnet Lua-based tool that silently corrupted uranium-compression simulations. Not an active threat, but extends the documented history of state-sponsored critical-process sabotage.

### 7. Pwn2Own Berlin 2026: $1.3M Paid for 47 Zero-Days in Windows, Linux, VMware, and AI Products
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-earn-1-298-250-for-47-zero-days-at-pwn2own-berlin-2026/
- **Severity:** medium
- **Tags:** `zero-day`, `vulnerability`, `ai-safety`
- **Summary:** Pwn2Own Berlin 2026 ended with $1,298,250 paid for 47 zero-days across Windows, Linux, VMware, Nvidia, and AI products. Expect related CVEs to be published within 90 days across these product families.

## Skippable

- **Researcher Drops MiniPlasma Windows Exploit for Unpatched 2020 CVE** — SecurityWeek. Duplicate of item 2; The Hacker News has more technical detail.
- **First Shai-Hulud Worm Clones Emerge** — SecurityWeek. Duplicate of item 3; The Hacker News lists specific package names and download counts.
- **Microsoft confirms Windows 11 security update install issues** — BleepingComputer. Patch deployment failure (KB5089549), not a security vulnerability or new threat.
- **Hackers Earn $1.3 Million at Pwn2Own Berlin 2026** — SecurityWeek. Duplicate of item 7 with less detail.
- **Can Laws Stop Deepfakes? South Korea Aims to Find Out** — Dark Reading. Policy opinion piece on election deepfake regulation; no actionable technical security news.
- **New Windows 'MiniPlasma' zero-day exploit gives SYSTEM access, PoC released** — BleepingComputer. Duplicate of item 2; The Hacker News selected as primary source.
