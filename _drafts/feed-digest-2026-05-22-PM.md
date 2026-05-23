# Digest — 2026-05-22 PM

- Window: last 14h
- Raw items considered: 44
- Relevant: 21
- Skippable: 23

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** CISA Contractor Exposes AWS GovCloud Keys on Public GitHub — `2026-05-22-cisa-contractor-aws-govcloud-keys-leaked.md`
- [x] **[CRITICAL]** Grafana Codebase Stolen via TanStack Supply Chain Attack — `2026-05-22-grafana-codebase-stolen-tanstack-supply-chain.md`
- [x] **[CRITICAL]** Megalodon GitHub Attack Injects Malicious CI/CD Workflows into 5,561 Repos — `2026-05-22-megalodon-github-attack-malicious-cicd-5561-repos.md`
- [x] **[CRITICAL]** Drupal CVE-2026-9082 SQL Injection Under Active Exploitation — `2026-05-22-drupal-cve-2026-9082-sqli-active-exploitation.md`
- [x] **[CRITICAL]** Cisco Patches CVSS 10.0 Flaw in Secure Workload REST API — `2026-05-22-cisco-secure-workload-cvss-10-rest-api-flaw.md`
- [x] **[HIGH]** Trend Micro Apex One Zero-Day CVE-2026-34926 Exploited in the Wild — `2026-05-22-trend-micro-apex-one-zero-day-cve-2026-34926.md`
- [x] **[HIGH]** First VPN Cybercrime Service Dismantled in Global Law Enforcement Operation — `2026-05-22-first-vpn-cybercrime-service-dismantled.md`
- [x] **[HIGH]** Langflow CVE-2025-34291 (CVSS 9.4) Added to CISA KEV Under Active Exploitation — `2026-05-22-langflow-cve-2025-34291-active-exploitation.md`
- [x] **[HIGH]** Iranian APT Screening Serpens Uses AppDomainManager Hijacking in 2026 Espionage — `2026-05-22-iran-apt-screening-serpens-appdomain-hijacking.md`
- [x] **[HIGH]** China's Webworm APT Abuses Discord and Microsoft Graph to Compromise EU Governments — `2026-05-22-webworm-discord-microsoft-graph-eu-governments.md`
- [x] **[HIGH]** Cloud Atlas APT Deploys PowerCloud and New Persistence Tools in 2025–2026 Campaigns — `2026-05-22-cloud-atlas-apt-powercloud-new-payload-2026.md`
- [x] **[HIGH]** ROADtools Open-Source Framework Abused for Nation-State Cloud Intrusions — `2026-05-22-roadtools-nation-state-cloud-intrusions.md`
- [x] **[HIGH]** Reaper macOS Malware and Two Microsoft Defender Zero-Days Exploited in the Wild — `2026-05-22-reaper-macos-malware-microsoft-defender-zero-days.md`
- [x] **[HIGH]** Ubiquiti Patches Three Maximum-Severity Vulnerabilities in UniFi OS — `2026-05-22-ubiquiti-unifi-os-max-severity-vulnerabilities.md`
- [x] **[HIGH]** Ghostwriter APT Targets Ukrainian Government with Prometheus-Themed Phishing — `2026-05-22-ghostwriter-ukraine-prometheus-phishing.md`
- [x] **[MEDIUM]** Kimwolf DDoS Botnet Operator Arrested in Canada — `2026-05-22-kimwolf-ddos-botnet-operator-arrested.md`
- [x] **[MEDIUM]** Google AI Search Interprets 'Disregard' as a Prompt Injection Instruction — `2026-05-22-google-ai-search-disregard-prompt-injection.md`
- [x] **[MEDIUM]** Trail of Bits Hardens zizmor GitHub Actions Analyzer Against YAML Anchor Gaps — `2026-05-22-trail-of-bits-zizmor-github-actions-hardening.md`
- [x] **[MEDIUM]** Verizon DBIR 2026: Social Engineering Surges in Healthcare Alongside Ransomware — `2026-05-22-verizon-dbir-2026-ransomware-social-engineering.md`
- [x] **[MEDIUM]** BYOVD: Exploiting Vulnerable Windows Kernel Drivers Without Their Target Hardware — `2026-05-22-byovd-vulnerable-drivers-exploitable-without-hardware.md`
- [x] **[INFORMATIONAL]** CISA Opens KEV Nomination Form So Researchers Can Report Actively Exploited Bugs — `2026-05-23-cisa-kev-nomination-form-researchers.md`

## Relevant (details)

### 1. CISA Contractor Exposes AWS GovCloud Keys on Public GitHub
- **Source:** Krebs on Security — https://krebsonsecurity.com/2026/05/lawmakers-demand-answers-as-cisa-tries-to-contain-data-leak/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `data-breach`, `cloud-security`, `aws`, `iam`
- **Slug:** `cisa-contractor-aws-govcloud-keys-leaked`
- **Must-know:** yes
- **Summary:** A CISA contractor intentionally published AWS GovCloud credentials and other agency secrets to a public GitHub repository; CISA is still working to invalidate leaked credentials. Lawmakers in both chambers are demanding answers as the breach affects GovCloud environments tied to federal infrastructure.

### 2. Grafana Codebase Stolen via TanStack Supply Chain Attack
- **Source:** SecurityWeek — https://www.securityweek.com/grafana-says-codebase-and-other-data-stolen-via-tanstack-supply-chain-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `data-breach`
- **Slug:** `grafana-codebase-stolen-tanstack-supply-chain`
- **Must-know:** yes
- **Summary:** Attackers used a token compromised in the TanStack supply chain attack — never rotated — to access Grafana's GitHub repositories and exfiltrate its codebase. A clear example of how an unrotated token from a prior supply chain incident becomes the next breach.

### 3. Megalodon GitHub Attack Injects Malicious CI/CD into 5,561 Repos
- **Source:** The Hacker News — https://thehackernews.com/2026/05/megalodon-github-attack-targets-5561.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `malware`, `devsecops`
- **Slug:** `megalodon-github-attack-malicious-cicd-5561-repos`
- **Must-know:** yes
- **Summary:** Automated campaign pushed 5,718 malicious commits to 5,561+ GitHub repos in six hours using forged bot identities to inject base64-encoded exfiltration payloads into GitHub Actions workflows. Massive-scale opportunistic supply chain poisoning targeting CI/CD secrets.

### 4. Drupal CVE-2026-9082 SQL Injection Under Active Exploitation
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/drupal-critical-sql-injection-flaw-now-targeted-in-attacks/ / CISA Alerts
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `sqli`, `cve`, `zero-day`, `vulnerability`
- **Slug:** `drupal-cve-2026-9082-sqli-active-exploitation`
- **Must-know:** yes
- **Summary:** Drupal's "highly critical" SQL injection CVE-2026-9082 is under active exploitation with attacks hitting thousands of websites; CISA added it to KEV. Patch or apply mitigations immediately — unpatched sites are being actively scanned and exploited.

### 5. Cisco Patches CVSS 10.0 Flaw in Secure Workload REST API
- **Source:** The Hacker News — https://thehackernews.com/2026/05/cisco-patches-cvss-100-secure-workload.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `cloud-security`
- **Slug:** `cisco-secure-workload-cvss-10-rest-api-flaw`
- **Must-know:** no
- **Summary:** CVE-2026-20223 (CVSS 10.0) in Cisco Secure Workload allows unauthenticated remote attackers to access sensitive data via the REST API; no active exploitation reported yet. Patch immediately given the maximum severity and unauthenticated attack surface.

### 6. Trend Micro Apex One Zero-Day CVE-2026-34926 Exploited in the Wild
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/trend-micro-warns-of-apex-one-zero-day-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `cve`, `vulnerability`
- **Slug:** `trend-micro-apex-one-zero-day-cve-2026-34926`
- **Must-know:** no
- **Summary:** Directory traversal zero-day CVE-2026-34926 in Trend Micro Apex One (on-prem) is actively exploited against Windows systems and added to CISA KEV. Patch and review endpoint logs for exploitation indicators.

### 7. First VPN Cybercrime Service Dismantled in Global Law Enforcement Operation
- **Source:** The Hacker News — https://thehackernews.com/2026/05/first-vpn-dismantled-in-global-takedown.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`, `malware`
- **Slug:** `first-vpn-cybercrime-service-dismantled`
- **Must-know:** no
- **Summary:** Multi-country operation led by France and the Netherlands seized 800 servers and arrested two men behind First VPN Service, a criminal VPN used by 25+ ransomware groups. FBI is sharing intel on the service's users with affected organizations.

### 8. Langflow CVE-2025-34291 (CVSS 9.4) Added to CISA KEV Under Active Exploitation
- **Source:** The Hacker News — https://thehackernews.com/2026/05/cisa-adds-exploited-langflow-and-trend.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `llm`, `ai-safety`
- **Slug:** `langflow-cve-2025-34291-active-exploitation`
- **Must-know:** no
- **Summary:** CISA added an origin validation error in Langflow (CVSS 9.4) to KEV citing active exploitation. Langflow's role as a low-code LLM workflow platform makes this particularly relevant to AI-deploying organizations — patch immediately.

### 9. Iranian APT Screening Serpens Uses AppDomainManager Hijacking in 2026 Espionage
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/tracking-iran-apt-screening-serpens/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `malware`, `privilege-escalation`
- **Slug:** `iran-apt-screening-serpens-appdomain-hijacking`
- **Must-know:** no
- **Summary:** Iran-linked Screening Serpens combines AppDomainManager hijacking (.NET DLL injection) with new RAT variants to target tech and defense sectors in ongoing 2026 espionage campaigns. Living-off-the-land technique plus custom malware complicates detection.

### 10. China's Webworm APT Abuses Discord and Microsoft Graph to Compromise EU Governments
- **Source:** Dark Reading — https://www.darkreading.com/endpoint-security/chinas-webworm-discord-microsoft-graphs
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `cloud-security`, `microsoft`
- **Slug:** `webworm-discord-microsoft-graph-eu-governments`
- **Must-know:** no
- **Summary:** Chinese APT Webworm routes C2 traffic through Discord and Microsoft Graph API to target EU government networks, supplemented by SoftEther VPN SOCKS proxies for tunneling. IP-based blocking provides little protection when C2 runs through trusted cloud platforms.

### 11. Cloud Atlas APT Deploys PowerCloud and New Persistence Tools in 2025–2026 Campaigns
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/cloud-atlas-2026/119895/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `malware`, `cloud-security`
- **Slug:** `cloud-atlas-apt-powercloud-new-payload-2026`
- **Must-know:** no
- **Summary:** Kaspersky GReAT details Cloud Atlas APT targeting public sector and diplomatic entities in Russia/Belarus with updated toolset: PowerCloud, ReverseSocks, SSH tunneling, and Tor. Active tradecraft development signals continued operational tempo.

### 12. ROADtools Open-Source Framework Abused for Nation-State Cloud Intrusions
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `cloud-security`, `iam`, `azure`, `microsoft`
- **Slug:** `roadtools-nation-state-cloud-intrusions`
- **Must-know:** no
- **Summary:** Nation-state APT operators are incorporating ROADtools (open-source Azure AD/Entra ID enumeration framework) into cloud intrusion pre-exploitation phases. Defenders should audit Entra ID logs for ROADtools-characteristic mass enumeration activity.

### 13. Reaper macOS Malware and Two Microsoft Defender Zero-Days Exploited in the Wild
- **Source:** SentinelOne Labs — https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-21-7/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `malware`, `zero-day`, `microsoft`
- **Slug:** `reaper-macos-malware-microsoft-defender-zero-days`
- **Must-know:** no
- **Summary:** SentinelOne Week 21 flags two Microsoft Defender zero-days under active exploitation and Reaper, a new macOS infostealer impersonating Adobe, Notion, and other brands. Defender details limited in this roundup; watch for KEV additions.

### 14. Ubiquiti Patches Three Maximum-Severity Vulnerabilities in UniFi OS
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/ubiquiti-patches-three-max-severity-unifi-os-vulnerabilities/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `rce`
- **Slug:** `ubiquiti-unifi-os-max-severity-vulnerabilities`
- **Must-know:** no
- **Summary:** Three maximum-severity vulnerabilities in UniFi OS, all exploitable remotely without authentication. No CVE details or active exploitation reported yet; patch immediately given the attack surface.

### 15. Ghostwriter APT Targets Ukrainian Government with Prometheus-Themed Phishing
- **Source:** The Hacker News — https://thehackernews.com/2026/05/ghostwriter-targets-ukraine-government.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `malware`
- **Slug:** `ghostwriter-ukraine-prometheus-phishing`
- **Must-know:** no
- **Summary:** Belarus-aligned Ghostwriter (UAC-0057/UNC1151) is phishing Ukrainian government entities using Prometheus (a legitimate Ukrainian online learning platform) as a lure. CERT-UA tracking; malware delivered via attachments or links in campaign emails.

### 16. Kimwolf DDoS Botnet Operator Arrested in Canada
- **Source:** The Record (Recorded Future) — https://therecord.media/canadian-man-arrested-charged-running-kimwolf-botnet
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `kimwolf-ddos-botnet-operator-arrested`
- **Must-know:** no
- **Summary:** Jacob Butler (23, Ottawa) arrested for operating KimWolf, a DDoS-for-hire botnet (AISURU variant) infecting nearly 2 million devices worldwide. US extradition request filed.

### 17. Google AI Search Interprets 'Disregard' as a Prompt Injection Instruction
- **Source:** The Verge AI — https://www.theverge.com/tech/936176/google-ai-overviews-search-disregard
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `llm`, `ai-safety`, `prompt-injection`
- **Slug:** `google-ai-search-disregard-prompt-injection`
- **Must-know:** no
- **Summary:** Searching "disregard" in Google triggers an LLM instruction-override in AI Overviews, returning chatbot-style responses instead of search results. Real-world prompt injection in a consumer-facing LLM-augmented interface; no fix issued as of publication.

### 18. Trail of Bits Hardens zizmor GitHub Actions Analyzer Against YAML Anchor Gaps
- **Source:** Trail of Bits — https://blog.trailofbits.com/2026/05/22/we-hardened-zizmors-github-actions-static-analyzer/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `supply-chain`, `devsecops`, `github`
- **Slug:** `trail-of-bits-zizmor-github-actions-hardening`
- **Must-know:** no
- **Summary:** Trail of Bits closed an analysis gap in zizmor (GitHub Actions static analyzer) introduced by YAML anchor support added in September 2025 — the same class of misconfiguration that led to the trivy-action supply chain attack and LiteLLM PyPI backdoor in March 2026.

### 19. Verizon DBIR 2026: Social Engineering Surges in Healthcare Alongside Ransomware
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/verizon-dbir-healthcare-fends-off-increased-social-engineering-attacks
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ransomware`, `phishing`, `data-breach`
- **Slug:** `verizon-dbir-2026-ransomware-social-engineering`
- **Must-know:** no
- **Summary:** Verizon's 2026 DBIR highlights healthcare as a sector seeing escalating social engineering alongside persistent ransomware and vendor breaches. Evolving social engineering tactics are increasing exposure even where baseline controls have improved.

### 20. BYOVD: Exploiting Vulnerable Windows Kernel Drivers Without Their Target Hardware
- **Source:** The Hacker News — https://thehackernews.com/2026/05/making-vulnerable-drivers-exploitable.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `privilege-escalation`
- **Slug:** `byovd-vulnerable-drivers-exploitable-without-hardware`
- **Must-know:** no
- **Summary:** Research shows hardware-gating is not a reliable barrier to exploiting signed-but-vulnerable Windows kernel-mode drivers; user-mode interaction is often possible without the target hardware. Expands the viable pool of drivers for BYOVD privilege escalation and EDR evasion attacks.

### 21. CISA Opens KEV Nomination Form So Researchers Can Report Actively Exploited Bugs
- **Source:** The Record (Recorded Future) — https://therecord.media/cisa-to-allow-researchers-to-report-vulnerabilities-kev
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `vulnerability`, `cve`
- **Slug:** `cisa-kev-nomination-form-researchers`
- **Must-know:** no
- **Summary:** CISA launched a nomination form for researchers, vendors, and partners to submit exploited vulnerabilities for KEV inclusion. Expands KEV coverage by incorporating community intelligence beyond CISA's own monitoring.

## Skippable

- **Elon Musk Can't Hear You Over the Sound of His $1.75 Trillion IPO** — TechCrunch AI. Off-topic podcast; no security or AI model angle.
- **Catch up on the Dialogues stage at Google I/O 2026** — Google AI Blog. Generic event recap with no new model launch or security content.
- **Netherlands seizes 800 servers of hosting firm enabling cyberattacks** — BleepingComputer. Duplicate coverage of the First VPN operation; THN selected as primary.
- **Elon, stop trying to make Grok happen** — The Verge AI. Opinion piece, no technical security or model substance.
- **Drupal Vulnerability in Hacker Crosshairs Shortly After Disclosure** — SecurityWeek. Duplicate of BleepingComputer Drupal item.
- **You can no longer Google the word 'disregard'** — TechCrunch AI. Duplicate of The Verge AI item selected as primary.
- **Akamai Joins Growing Chorus of Vendors Betting Big on Secure Enterprise Browsers** — Dark Reading. Acquisition announcement; no specific technical security news.
- **We tried Google's AI glasses and they're almost there** — TechCrunch AI. Product demo, no security angle.
- **Former US execs plead guilty to aiding tech support scammers** — BleepingComputer. Criminal proceeding, no technical security content.
- **Specialization Beats Scale: A Strategic Variable Most AI Procurement Decisions Overlook** — Hugging Face Blog. AI procurement opinion piece, no news value.
- **Why the Supreme Court's Chatrie case could change the meaning of privacy in America** — The Record. Legal analysis, no technical security substance.
- **SpaceX files to go public, and the math requires a little faith** — TechCrunch AI. Duplicate SpaceX IPO content; off-topic.
- **The literary world isn't prepared for AI** — The Verge AI. Cultural opinion piece, no security or technical angle.
- **Spotify says its AI remix tool is for superfans** — The Verge AI. Non-security SaaS product launch.
- **In Other News: Industrial Router Exploitation, CISA KEV Nomination Form, Gas Station Hacking** — SecurityWeek. Roundup; CISA KEV form covered separately, other items lack standalone detail.
- **Why Chargebacks are Just One Piece of the Fraud Puzzle** — BleepingComputer. Sponsored marketing content from IPQS.
- **Canadian Man Arrested for Operating Kimwolf Botnet** — SecurityWeek. Duplicate of The Record item selected as primary.
- **CISA Adds One Known Exploited Vulnerability to Catalog** — CISA Alerts. Duplicate; Drupal CVE-2026-9082 covered in BleepingComputer post with CISA as secondary source.
- **Samsung's memory chip employees negotiated $340,000 bonuses this year** — The Verge AI. Off-topic; no AI or security relevance.
- **'First VPN' Cybercrime Service Disrupted, Administrator Arrested** — SecurityWeek. Duplicate of The Hacker News item selected as primary.
- **US and Canada arrest and charge suspected Kimwolf botnet admin** — BleepingComputer. Duplicate of The Record item selected as primary.
- **Kimwolf DDoS Botnet Operator Arrested in Canada Over DDoS-for-Hire Attacks** — The Hacker News. Duplicate of The Record item selected as primary.
- **TrendAI Patches Apex One Zero-Day Exploited in the Wild** — SecurityWeek. Duplicate of BleepingComputer Apex One item.
