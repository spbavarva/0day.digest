# Digest — 2026-11-28 AM

- Window: last 14h
- Raw items considered: 19
- Relevant: 8
- Skippable: 11

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** pCloud Confirms Password Manager Hack After Suspicious Login Alerts — `2026-11-27-pcloud-password-manager-hack.md`
- [x] **[HIGH]** Unpatched Cacti Zero-Day With Public PoC Enables Remote Code Execution — `2026-11-27-cacti-zero-day-rce-public-poc.md`
- [x] **[MEDIUM]** Suspected Vietnam-Linked Hackers Target Southeast Asia in South China Sea Espionage Campaign — `2026-11-27-vietnam-linked-hackers-south-china-sea-espionage.md`
- [x] **[HIGH]** US Air Force Cloud Platform Reportedly Hacked in Latest Federal Breach — `2026-11-27-us-air-force-cloud-one-breach.md`
- [x] **[HIGH]** 'God Mode' Flaws Could Have Disrupted Border Control Systems — `2026-11-27-border-control-god-mode-flaws.md`
- [x] **[HIGH]** SAP Confirms Cyber Incident Amid Reports of Source Code Breach — `2026-11-27-sap-source-code-breach.md`
- [x] **[HIGH]** CISA Adds GeoServer and Drupal Vulnerabilities to Known Exploited Vulnerabilities Catalog — `2026-11-27-cisa-kev-geoserver-drupal.md`
- [x] **[MEDIUM]** Microsoft Store App Found Delivering Vinci RAT — `2026-11-27-microsoft-store-vinci-rat.md`

## Relevant (details)

### 1. pCloud Confirms Password Manager Hack After Suspicious Login Alerts
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/pcloud-confirms-password-manager-hack-after-suspicious-login-alerts/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** pCloud confirmed its Pass password manager was compromised after users reported unknown devices logging into their accounts despite 2FA being enabled. The apparent 2FA bypass is notable since a password manager breach directly threatens stored credentials.

### 2. Unpatched Cacti Zero-Day With Public PoC Enables Remote Code Execution
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/unpatched-cacti-zero-day-with-public-poc-gives-remote-code-execution/
- **Severity:** high
- **Tags:** `zero-day`, `rce`
- **Summary:** A publicly disclosed zero-day in the Cacti network monitoring platform, paired with a working PoC, lets unauthenticated attackers run arbitrary commands on vulnerable servers. No patch exists yet, and the public exploit code raises the odds of in-the-wild attacks.

### 3. Suspected Vietnam-Linked Hackers Target Southeast Asia in South China Sea Espionage Campaign
- **Source:** The Hacker News — https://thehackernews.com/2026/11/suspected-vietnam-linked-hackers-target.html
- **Severity:** medium
- **Tags:** `espionage`
- **Summary:** SOCRadar attributed a previously undocumented campaign, dubbed WeaveLotus, to a suspected Vietnam-sponsored group targeting Southeast Asian military and government bodies to gather intelligence on South China Sea defense agreements. At least five intrusions have been identified, including in Thailand.

### 4. US Air Force Cloud Platform Reportedly Hacked in Latest Federal Breach
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/us-air-force-cloud-platform-reportedly-hacked-in-latest-federal-breach/
- **Severity:** high
- **Tags:** `cloud-security`, `data-breach`
- **Summary:** The US Air Force's Cloud One platform was reportedly breached, adding to a recent wave of attacks on federal agencies including the FBI, CIA, and Treasury. Scope of access and data exposure remain unconfirmed.

### 5. 'God Mode' Flaws Could Have Disrupted Border Control Systems
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/god-mode-flaws-wreak-border-control-havoc
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`
- **Summary:** Researchers found "God Mode" flaws in online visa and immigration systems used by Nigeria, Ethiopia, Zambia, Sri Lanka, Fiji, and Ghana that could have let attackers disrupt traveler entry processing. No active exploitation was reported at disclosure.

### 6. SAP Confirms Cyber Incident Amid Reports of Source Code Breach
- **Source:** The Record (Recorded Future) — https://therecord.media/sap-germany-cyberattack-github
- **Severity:** high
- **Tags:** `supply-chain`, `data-breach`
- **Summary:** SAP confirmed a cybersecurity incident following reports that attackers infiltrated its development infrastructure, with possible access to source code via GitHub. Full scope of affected systems has not been disclosed, raising supply chain concerns given SAP's enterprise footprint.

### 7. CISA Adds GeoServer and Drupal Vulnerabilities to Known Exploited Vulnerabilities Catalog
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/alerts/2026/11/27/cisa-adds-three-known-exploited-vulnerabilities-catalog
- **Severity:** high
- **Tags:** `cve`, `vulnerability`
- **Summary:** CISA added three actively exploited CVEs to its KEV catalog: an XML injection and an incorrect authorization flaw in OSGeo GeoServer, and an exception-handling flaw in Drupal Core. Federal agencies must remediate per BOD 26-04.

### 8. Microsoft Store App Found Delivering Vinci RAT
- **Source:** The Hacker News — https://thehackernews.com/2026/11/microsoft-store-app-found-delivering.html
- **Severity:** medium
- **Tags:** `malware`, `microsoft`
- **Summary:** eSentire disclosed a campaign using a Microsoft Store app and a Microsoft-signed installer disguised as a sniping tool to deliver the Vinci remote access trojan. The campaign abuses a trusted distribution channel to bypass user suspicion of malicious installers.

## Skippable

- **datasette-charts 0.4a0** — Simon Willison. Niche plugin release update, not a security or major AI launch story.
- **New Boston Scientific data breach exposes personal, medical info** — BleepingComputer. Generic breach disclosure with no technical detail or confirmed scale.
- **Matters.AI Lands India's Largest Cybersecurity Pre-Series A Round** — Dark Reading. Funding/marketing announcement, not a news event with technical substance.
- **Your Firewall Isn't Enough: The Hidden Risk of Unmanaged VMs** — BleepingComputer. Sponsored marketing content from ISPsystem.
- **Malwarebytes Antivirus: Get 50% off during Black Friday 2026** — BleepingComputer. Promotional/marketing content.
- **Japan's education ministry discloses breach of government procurement system** — The Record. Regional government breach without technical detail on attack method.
- **The Good, the Bad and the Ugly in Cybersecurity - Week 48 (2026)** — SentinelOne Labs. Multi-topic weekly roundup; individual items too thin on detail to stand alone.
- **Android's DIY widgets are a bit of vibe-coding fun** — The Verge AI. Consumer feature piece, no security angle.
- **Microsoft removes WSUS server role in Windows Server 2028** — BleepingComputer. Product lifecycle announcement, not a current vulnerability or attack.
- **In Other News: Tanker Cyberattacks, EU Quantum Act, New VirusTotal Capabilities** — SecurityWeek. Multi-topic roundup; individual items lack sufficient detail.
- **How to Keep Your Security Picture Current When Attackers Move at AI Speed** — The Hacker News. Opinion/thought-leadership piece without concrete news value.
