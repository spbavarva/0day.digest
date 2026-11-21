# Digest — 2026-11-21 PM

- Window: last 14h
- Raw items considered: 16
- Relevant: 8
- Skippable: 8

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Microsoft Entra Connect Health Flaw Exploited to Steal Tenant Data — `2026-11-21-microsoft-entra-connect-health-breach.md`
- [x] **[MEDIUM]** BADBOX Botnet Returns With Record 40 Billion Daily Ad Requests — `2026-11-21-badbox-botnet-returns-ad-fraud.md`
- [x] **[HIGH]** FBI Reportedly Hacked Again, Targeting Nationwide Police Database — `2026-11-21-fbi-hacked-again-ncic-database.md`
- [x] **[MEDIUM]** Single Malicious Webpage Let Researchers Hijack Meta Muse and Access Private Chats — `2026-11-21-meta-muse-hijack-malicious-webpage.md`
- [x] **[HIGH]** GnuPG Warns Critical GPGME Flaw Could Expose App Data via Malicious OpenPGP Keys — `2026-11-21-gnupg-gpgme-critical-flaw-cve-2026-129975.md`
- [x] **[CRITICAL]** Attackers' AI Agents Found a Zero-Day in Medical-Imaging Software and Gained Root Access — `2026-11-21-ai-agents-zero-day-medical-imaging-monai.md`
- [x] **[INFORMATIONAL]** Signal Blocks AI Agents From Reading Private Chats via Screenshots — `2026-11-21-signal-blocks-ai-agents-screenshot-reading.md`
- [x] **[CRITICAL]** CISA Adds Actively Exploited VMware, Cisco, SAP, and Apache Flaws to KEV Catalog — `2026-11-21-cisa-kev-vmware-cisco-apache-active-exploitation.md`

## Relevant (details)

### 1. Microsoft Entra Connect Health Flaw Exploited to Steal Tenant Data
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `microsoft`, `azure`, `iam`
- **Slug:** `microsoft-entra-connect-health-breach`
- **Must-know:** no
- **Summary:** Microsoft disclosed a breach where attackers exploited a flaw in its Entra Connect Health service to access administrator email addresses and tenant configuration data. The scope of affected tenants has not been detailed.

### 2. BADBOX Botnet Returns With Record 40 Billion Daily Ad Requests
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/badbox-30-botnet-returns-with-record-breaking-40-billion-daily-ad-requests/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `iot`
- **Slug:** `badbox-botnet-returns-ad-fraud`
- **Must-know:** no
- **Summary:** The BADBOX malware, which infects generic Android TV boxes, has resumed large-scale ad-fraud operations after last year's disruptions. The botnet is now generating a record 40 billion ad requests per day.

### 3. FBI Reportedly Hacked Again, Targeting Nationwide Police Database
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/fbi-reportedly-hacked-again-this-time-targeting-nationwide-police-database/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `fbi-hacked-again-ncic-database`
- **Must-know:** no
- **Summary:** FBI systems were reportedly breached for the second time in two months, this time targeting the National Crime Information Center (NCIC) database used by law enforcement nationwide. No details on data accessed or official confirmation are available yet.

### 4. Single Malicious Webpage Let Researchers Hijack Meta Muse and Access Private Chats
- **Source:** The Hacker News — https://thehackernews.com/2026/11/a-single-malicious-webpage-let.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `llm`, `ai-safety`, `meta`
- **Slug:** `meta-muse-hijack-malicious-webpage`
- **Must-know:** no
- **Summary:** Researchers showed a malicious webpage could extract a Meta Muse user's private conversations and stored memories without any approval prompt, and that the technique could extend to stored account credentials. It was a lab demonstration, not an attack on real users.

### 5. GnuPG Warns Critical GPGME Flaw Could Expose App Data via Malicious OpenPGP Keys
- **Source:** The Hacker News — https://thehackernews.com/2026/11/gnupg-warns-critical-gpgme-flaw-could.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `appsec`
- **Slug:** `gnupg-gpgme-critical-flaw-cve-2026-129975`
- **Must-know:** no
- **Summary:** A malicious OpenPGP key with an unusually long user ID can trigger a critical memory bug in GPGME, the standard library behind GnuPG integrations, tracked as CVE-2026-129975. Fixed versions (2.3.0+) are available.

### 6. Attackers' AI Agents Found a Zero-Day in Medical-Imaging Software and Gained Root Access
- **Source:** The Hacker News — https://thehackernews.com/2026/11/attackers-ai-agents-found-zero-day-in.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `rce`, `ai-safety`, `vulnerability`
- **Slug:** `ai-agents-zero-day-medical-imaging-monai`
- **Must-know:** yes
- **Summary:** Suspected China-linked hackers used autonomous AI agents to discover a previously unknown flaw in the open-source MONAI Label medical-imaging server and gain root access to a university system. The flaw affects MONAI Label 0.8.5 and earlier in its default configuration.

### 7. Signal Blocks AI Agents From Reading Private Chats via Screenshots
- **Source:** The Hacker News — https://thehackernews.com/2026/11/signal-blocks-ai-agents-from-reading.html
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ai-safety`, `llm`
- **Slug:** `signal-blocks-ai-agents-screenshot-reading`
- **Must-know:** no
- **Summary:** Signal will restrict screenshots by default on Android and iOS to stop AI agents from reading private chats, targeting agentic systems built into iOS 27 and newer Android versions. Signal conceded the protection is "incomplete."

### 8. CISA Adds Actively Exploited VMware, Cisco, SAP, and Apache Flaws to KEV Catalog
- **Source:** The Hacker News — https://thehackernews.com/2026/11/hackers-exploit-critical-vmware-cisco.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `rce`
- **Slug:** `cisa-kev-vmware-cisco-apache-active-exploitation`
- **Must-know:** no
- **Summary:** CISA added four actively exploited flaws affecting Apache Roller, Cisco Expressway, SAP NetWeaver, and Broadcom VMware vCenter to its Known Exploited Vulnerabilities catalog. The most severe, CVE-2026-129448, is a deserialization bug with a CVSS score of 9.8.

## Skippable

- **Signal restricts mobile screenshots as it confronts 'existential threat' of AI surveillance** — TechCrunch AI. Duplicate coverage of the Signal screenshot-blocking story; The Hacker News version has more technical detail.
- **A tale of two Nvidias** — TechCrunch AI. Opinion/analysis on Nvidia earnings and leadership chatter, no security angle.
- **The UN fails to agree on rules regulating 'killer robots'** — The Verge AI. Policy discussion ended without any actual regulatory outcome.
- **Here are the top AI agents that can live in your text messages** — TechCrunch AI. Generic product roundup/listicle, no news value.
- **Is selling an AI version of your face to this microdrama startup the future of Hollywood?** — TechCrunch AI. Feature/opinion piece, no security relevance.
- **Can Anthropic afford to put safety first?** — The Verge AI. Podcast/opinion piece about the Anthropic IPO, no new technical or safety information.
- **Chess.com's next move is a new hub for classic games, from mahjong to sudoku** — The Verge AI. Product launch with no security or substantive AI angle.
- **Amazon: China-Linked Hackers' AI Agents Exploited Medical Software Zero-Day** — SecurityWeek. Duplicate coverage of the MONAI Label zero-day story; The Hacker News version has more technical detail.
