# Digest — 2026-11-21 PM

- Window: last 14h
- Raw items considered: 8
- Relevant: 6
- Skippable: 2

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** FBI Reportedly Breached Again, This Time Targeting Nationwide Police Database — `2026-11-21-fbi-ncic-police-database-breach.md`
- [x] **[HIGH]** Single Malicious Webpage Could Hijack Meta Muse and Expose Private Chats — `2026-11-21-meta-muse-malicious-webpage-hijack.md`
- [x] **[HIGH]** GnuPG Warns Critical GPGME Flaw Could Expose App Data via Malicious OpenPGP Keys — `2026-11-21-gnupg-gpgme-critical-flaw-cve-2026-129975.md`
- [x] **[CRITICAL]** China-Linked Hackers Used AI Agents to Exploit Zero-Day in Medical Imaging Software — `2026-11-21-monai-label-zero-day-ai-agents-root-access.md`
- [x] **[INFORMATIONAL]** Signal Blocks AI Agents From Reading Private Chats via Screenshots on Android and iOS — `2026-11-21-signal-blocks-ai-agents-screenshots.md`
- [x] **[CRITICAL]** Hackers Exploit Critical VMware, Cisco, and Apache Flaws as Espionage Attacks Emerge — `2026-11-21-cisa-kev-vmware-cisco-apache-sap-exploited.md`

## Relevant (details)

### 1. FBI Reportedly Breached Again, This Time Targeting Nationwide Police Database
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/fbi-reportedly-hacked-again-this-time-targeting-nationwide-police-database/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `vulnerability`
- **Slug:** `fbi-ncic-police-database-breach`
- **Must-know:** no
- **Summary:** FBI systems reportedly suffered a second breach in two months, this time targeting the National Crime Information Center (NCIC), the database used to share criminal justice data between local, state, and federal agencies. Scope of exposed data and intrusion method aren't yet detailed.

### 2. Single Malicious Webpage Could Hijack Meta Muse and Expose Private Chats
- **Source:** The Hacker News — https://thehackernews.com/2026/11/a-single-malicious-webpage-let.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `meta`, `ai-safety`, `vulnerability`
- **Slug:** `meta-muse-malicious-webpage-hijack`
- **Must-know:** no
- **Summary:** Researchers showed a single malicious webpage could extract a Meta Muse user's private conversations and stored memories without triggering any approval prompt, and said the technique could extend to credentials Muse stores for connected accounts. The work was a lab demonstration against the researchers' own account, not an attack on real users.

### 3. GnuPG Warns Critical GPGME Flaw Could Expose App Data via Malicious OpenPGP Keys
- **Source:** The Hacker News — https://thehackernews.com/2026/11/gnupg-warns-critical-gpgme-flaw-could.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`
- **Slug:** `gnupg-gpgme-critical-flaw-cve-2026-129975`
- **Must-know:** no
- **Summary:** A malicious OpenPGP key with an unusually long user ID can trigger a critical memory bug in GPGME, the library programs use to work with GnuPG, tracked as CVE-2026-129975. The flaw affects all software using GPGME before version 2.3.0; fixed versions are available.

### 4. China-Linked Hackers Used AI Agents to Exploit Zero-Day in Medical Imaging Software
- **Source:** The Hacker News — https://thehackernews.com/2026/11/attackers-ai-agents-found-zero-day-in.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `llm`, `rce`, `privilege-escalation`
- **Slug:** `monai-label-zero-day-ai-agents-root-access`
- **Must-know:** yes
- **Summary:** Suspected China-linked hackers used autonomous AI agents to find a previously unknown flaw in MONAI Label, an open-source medical-imaging server, and used it to gain root access to a university server, per Amazon Threat Intelligence. The flaw lets an unauthenticated attacker write files outside the server's storage folder and affects MONAI Label 0.8.5 and earlier in the default setup.

### 5. Signal Blocks AI Agents From Reading Private Chats via Screenshots on Android and iOS
- **Source:** The Hacker News — https://thehackernews.com/2026/11/signal-blocks-ai-agents-from-reading.html
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ai-safety`, `llm`
- **Slug:** `signal-blocks-ai-agents-screenshots`
- **Must-know:** no
- **Summary:** Signal will restrict screenshots by default to stop AI agents built into Android and iOS from reading private chats, targeting agentic systems in iOS 27 and compatible Android versions. Signal conceded the protection is "incomplete."

### 6. Hackers Exploit Critical VMware, Cisco, and Apache Flaws as Espionage Attacks Emerge
- **Source:** The Hacker News — https://thehackernews.com/2026/11/hackers-exploit-critical-vmware-cisco.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`
- **Slug:** `cisa-kev-vmware-cisco-apache-sap-exploited`
- **Must-know:** no
- **Summary:** CISA added four actively exploited flaws to its KEV catalog — Apache Roller (CVE-2026-129448, CVSS 9.8, deserialization), Cisco Expressway, SAP NetWeaver, and Broadcom VMware vCenter — citing evidence of active exploitation and emerging espionage activity tied to the flaws.

## Skippable

- **Chess.com's next move is a new hub for classic games, from mahjong to sudoku** — The Verge AI. Consumer gaming platform expansion with no security angle and no substantive AI content.
- **Amazon: China-Linked Hackers' AI Agents Exploited Medical Software Zero-Day** — SecurityWeek. Duplicate coverage of the MONAI Label zero-day; The Hacker News version carries more technical detail and was used for the draft post.
