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
- **Severity:** critical
- **Tags:** `data-breach`, `cloud-security`, `aws`, `iam`
- **Summary:** A CISA contractor intentionally published AWS GovCloud credentials and other agency secrets to a public GitHub repository; CISA is still working to invalidate leaked credentials. Lawmakers in both chambers are demanding answers as the breach affects GovCloud environments tied to federal infrastructure.

### 2. Grafana Codebase Stolen via TanStack Supply Chain Attack
- **Source:** SecurityWeek — https://www.securityweek.com/grafana-says-codebase-and-other-data-stolen-via-tanstack-supply-chain-attack/
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `data-breach`
- **Summary:** Attackers used an unrotated token from the TanStack supply chain attack to access Grafana's GitHub repositories and exfiltrate its codebase. A textbook example of how tokens exposed in one supply chain incident become the entry point for the next.

### 3. Megalodon GitHub Attack Injects Malicious CI/CD into 5,561 Repos
- **Source:** The Hacker News — https://thehackernews.com/2026/05/megalodon-github-attack-targets-5561.html
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `malware`, `devsecops`
- **Summary:** Automated campaign pushed 5,718 malicious commits to 5,561+ GitHub repos in six hours using forged bot identities to inject base64-encoded CI/CD secret exfiltration payloads. Massive-scale opportunistic supply chain poisoning.

### 4. Drupal CVE-2026-9082 SQL Injection Under Active Exploitation
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/drupal-critical-sql-injection-flaw-now-targeted-in-attacks/
- **Severity:** critical
- **Tags:** `sqli`, `cve`, `zero-day`, `vulnerability`
- **Summary:** Drupal's "highly critical" SQL injection CVE-2026-9082 is actively exploited against thousands of websites; CISA added it to KEV. Patch immediately — unpatched sites are being scanned and exploited.

### 5. Cisco Patches CVSS 10.0 Flaw in Secure Workload REST API
- **Source:** The Hacker News — https://thehackernews.com/2026/05/cisco-patches-cvss-100-secure-workload.html
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `cloud-security`
- **Summary:** CVE-2026-20223 (CVSS 10.0) in Cisco Secure Workload allows unauthenticated remote access to sensitive data via REST API; no active exploitation reported yet. Patch immediately.

### 6. Trend Micro Apex One Zero-Day CVE-2026-34926 Exploited in the Wild
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/trend-micro-warns-of-apex-one-zero-day-exploited-in-attacks/
- **Severity:** high
- **Tags:** `zero-day`, `cve`, `vulnerability`
- **Summary:** Directory traversal zero-day in Apex One on-prem is actively exploited against Windows systems and added to CISA KEV. Patch and review endpoint logs.

### 7. First VPN Cybercrime Service Dismantled in Global Law Enforcement Operation
- **Source:** The Hacker News — https://thehackernews.com/2026/05/first-vpn-dismantled-in-global-takedown.html
- **Severity:** high
- **Tags:** `ransomware`, `malware`
- **Summary:** France and Netherlands led operation seizing 800 servers and arresting two men behind First VPN, a criminal VPN used by 25+ ransomware groups for reconnaissance and intrusions. FBI sharing intel on service users.

### 8. Langflow CVE-2025-34291 (CVSS 9.4) Added to CISA KEV Under Active Exploitation
- **Source:** The Hacker News — https://thehackernews.com/2026/05/cisa-adds-exploited-langflow-and-trend.html
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `llm`, `ai-safety`
- **Summary:** Origin validation error in Langflow (CVSS 9.4) added to KEV under active exploitation. Langflow's role as a low-code LLM workflow platform makes this particularly relevant to AI-deploying organizations.

### 9. Iranian APT Screening Serpens Uses AppDomainManager Hijacking in 2026 Espionage
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/tracking-iran-apt-screening-serpens/
- **Severity:** high
- **Tags:** `malware`, `privilege-escalation`
- **Summary:** Iran-linked APT combines .NET AppDomainManager hijacking with new RAT variants to target tech and defense sectors. Living-off-the-land technique plus custom malware complicates detection.

### 10. China's Webworm APT Abuses Discord and Microsoft Graph to Compromise EU Governments
- **Source:** Dark Reading — https://www.darkreading.com/endpoint-security/chinas-webworm-discord-microsoft-graphs
- **Severity:** high
- **Tags:** `malware`, `cloud-security`, `microsoft`
- **Summary:** Webworm routes C2 through Discord and Microsoft Graph API to target EU governments, supplemented by SoftEther VPN tunneling. IP-based blocks offer little protection when C2 runs through trusted cloud platforms.

### 11. Cloud Atlas APT Deploys PowerCloud and New Persistence Tools in 2025–2026 Campaigns
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/cloud-atlas-2026/119895/
- **Severity:** high
- **Tags:** `malware`, `cloud-security`
- **Summary:** Cloud Atlas targets public sector and diplomatic entities in Russia/Belarus with updated toolset including PowerCloud, ReverseSocks, and Tor-based persistence. Active tradecraft development signals ongoing operational tempo.

### 12. ROADtools Open-Source Framework Abused for Nation-State Cloud Intrusions
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/
- **Severity:** high
- **Tags:** `cloud-security`, `iam`, `azure`, `microsoft`
- **Summary:** Nation-state actors are using ROADtools for Azure/Entra ID enumeration during cloud intrusion pre-exploitation. Audit Entra ID logs for anomalous mass directory enumeration.

### 13. Reaper macOS Malware and Two Microsoft Defender Zero-Days Exploited in the Wild
- **Source:** SentinelOne Labs — https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-21-7/
- **Severity:** high
- **Tags:** `malware`, `zero-day`, `microsoft`
- **Summary:** Two Microsoft Defender zero-days actively exploited, plus Reaper macOS infostealer spoofing major brands. Apply Defender updates as they ship; watch for KEV additions with technical details.

### 14. Ubiquiti Patches Three Maximum-Severity Vulnerabilities in UniFi OS
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/ubiquiti-patches-three-max-severity-unifi-os-vulnerabilities/
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `rce`
- **Summary:** Three max-severity, unauthenticated-remote vulnerabilities in UniFi OS; no CVE details or active exploitation yet. Patch immediately given the attack surface.

### 15. Ghostwriter APT Targets Ukrainian Government with Prometheus-Themed Phishing
- **Source:** The Hacker News — https://thehackernews.com/2026/05/ghostwriter-targets-ukraine-government.html
- **Severity:** high
- **Tags:** `phishing`, `malware`
- **Summary:** Belarus-aligned Ghostwriter phishing Ukrainian government entities with Prometheus-branded lures delivering malware. CERT-UA tracking.

### 16. Kimwolf DDoS Botnet Operator Arrested in Canada
- **Source:** The Record (Recorded Future) — https://therecord.media/canadian-man-arrested-charged-running-kimwolf-botnet
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** Jacob Butler (23, Ottawa) arrested for operating KimWolf DDoS-for-hire botnet (AISURU variant, ~2M infected devices). US extradition request filed.

### 17. Google AI Search Interprets 'Disregard' as a Prompt Injection Instruction
- **Source:** The Verge AI — https://www.theverge.com/tech/936176/google-ai-overviews-search-disregard
- **Severity:** medium
- **Tags:** `llm`, `ai-safety`, `prompt-injection`
- **Summary:** Searching "disregard" in Google triggers an LLM instruction-override in AI Overviews, returning chatbot output instead of search results. Real-world prompt injection in a consumer-facing LLM interface.

### 18. Trail of Bits Hardens zizmor GitHub Actions Analyzer Against YAML Anchor Gaps
- **Source:** Trail of Bits — https://blog.trailofbits.com/2026/05/22/we-hardened-zizmors-github-actions-static-analyzer/
- **Severity:** medium
- **Tags:** `supply-chain`, `devsecops`, `github`
- **Summary:** zizmor updated to close a YAML anchor analysis gap; background: the same class of GitHub Actions misconfiguration led to the trivy-action supply chain attack and LiteLLM PyPI backdoor in March 2026.

### 19. Verizon DBIR 2026: Social Engineering Surges in Healthcare Alongside Ransomware
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/verizon-dbir-healthcare-fends-off-increased-social-engineering-attacks
- **Severity:** medium
- **Tags:** `ransomware`, `phishing`, `data-breach`
- **Summary:** Verizon DBIR 2026 highlights escalating social engineering in healthcare alongside persistent ransomware and vendor breaches. Practitioner-grade annual benchmark.

### 20. BYOVD: Exploiting Vulnerable Windows Kernel Drivers Without Their Target Hardware
- **Source:** The Hacker News — https://thehackernews.com/2026/05/making-vulnerable-drivers-exploitable.html
- **Severity:** medium
- **Tags:** `vulnerability`, `privilege-escalation`
- **Summary:** Research shows hardware-gating is not a reliable barrier for BYOVD attacks; user-mode interaction with signed-but-vulnerable kernel drivers is often possible without the target hardware present. Expands viable driver pool for privilege escalation and EDR evasion.

### 21. CISA Opens KEV Nomination Form So Researchers Can Report Actively Exploited Bugs
- **Source:** The Record (Recorded Future) — https://therecord.media/cisa-to-allow-researchers-to-report-vulnerabilities-kev
- **Severity:** informational
- **Tags:** `vulnerability`, `cve`
- **Summary:** CISA launched a public nomination form for researchers, vendors, and partners to submit exploited vulnerabilities for KEV consideration. Expands catalog coverage beyond CISA's own monitoring.

## Skippable

- **Elon Musk Can't Hear You Over the Sound of His $1.75 Trillion IPO** — TechCrunch AI. Off-topic podcast; no security or AI model angle.
- **Catch up on the Dialogues stage at Google I/O 2026** — Google AI Blog. Generic event recap with no new model launch or security content.
- **Netherlands seizes 800 servers of hosting firm enabling cyberattacks** — BleepingComputer. Duplicate of First VPN operation; THN selected as primary.
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
