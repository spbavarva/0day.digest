# Digest — 2026-11-24 PM

- Window: last 14h
- Raw items considered: 52
- Relevant: 19
- Skippable: 33

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** CISA Adds Actively Exploited N-able MailAssure and MONAI Label Flaws to KEV Catalog — `2026-11-24-cisa-kev-nable-mailassure-monai-label-zero-days.md`
- [x] **[HIGH]** Radware Discloses Breach Exposing Customer Cloud Access Keys — `2026-11-24-radware-breach-exposed-cloud-access-keys.md`
- [x] **[HIGH]** Iran-Aligned Volant Manticore Uses New IPFS-Based KuboShell Backdoor — `2026-11-24-volant-manticore-ipfs-kuboshell-backdoor.md`
- [x] **[HIGH]** Hackers Compromise Check Point Security Management Servers at 22 Organizations — `2026-11-24-check-point-management-servers-compromised-22-orgs.md`
- [x] **[HIGH]** VMware Patches Critical 9.8-Rated Auth Bypass in vCenter (CVE-2026-123903) — `2026-11-24-vmware-vcenter-auth-bypass-cve-2026-123903.md`
- [x] **[HIGH]** Attackers Find a Way Around GitHub Actions SHA Pinning — `2026-11-24-github-sha-pinning-bypass-supply-chain.md`
- [x] **[HIGH]** Google Researcher Shows Single-Bit .NET File Change Bypasses Windows Code Integrity — `2026-11-24-dotnet-single-bit-bypass-windows-code-integrity.md`
- [x] **[HIGH]** Danfoss AK-SM 8xxA Flaw Allows Unauthenticated Code Execution (CVE-2026-129713) — `2026-11-24-danfoss-ak-sm-8xxa-stack-overflow-cve-2026-129713.md`
- [x] **[HIGH]** 1.5 Million Impacted by Data Breach at South Korean Electric Company KEPCO — `2026-11-24-kepco-data-breach-1-5-million-customers.md`
- [x] **[HIGH]** Microsoft Fixes Azure API Management Flaw After Actor Targets Customer Secrets — `2026-11-24-azure-apim-classic-flaw-targeted-secrets.md`
- [x] **[HIGH]** Elecbrakes Bluetooth Vulnerabilities Expose Trailers to Forced Braking — `2026-11-24-elecbrakes-bluetooth-forced-braking-vulnerabilities.md`
- [x] **[HIGH]** WHMCS SQL Injection Flaw Exposes Customer Data and Admin Password Hashes Without Login — `2026-11-24-whmcs-sql-injection-exposes-admin-password-hashes.md`
- [x] **[MEDIUM]** European Commission Confirms AI-Assisted Cyberattack Behind EU Academy Breach — `2026-11-24-eu-academy-breach-ai-assisted-cyberattack.md`
- [x] **[MEDIUM]** UK Cyber Agency Reports Marked Rise in AI-Driven Cyberattacks — `2026-11-24-uk-ncsc-ai-driven-cyberattacks-rise.md`
- [x] **[MEDIUM]** Okta Links ShinyHunters-Associated Vishing Group to New INCEPTION Data Leak Site — `2026-11-24-shinyhunters-inception-data-leak-site.md`
- [x] **[MEDIUM]** McDonald's Japan Breach Exposes Customer Purchase History and Location Data — `2026-11-24-mcdonalds-japan-breach-purchase-location-data.md`
- [x] **[INFORMATIONAL]** Unit 42 Details Tactics in Agentic AI Attack Campaigns — `2026-11-24-unit42-agentic-ai-attack-campaigns.md`
- [x] **[INFORMATIONAL]** Anthropic Expands Enterprise Safeguards for Detecting Claude Misuse — `2026-11-24-anthropic-enterprise-safeguards-misuse-detection.md`
- [x] **[INFORMATIONAL]** OpenAI and Cisco Launch Shirudo, an Open-Source Linux Exploit Shield — `2026-11-24-openai-cisco-shirudo-linux-exploit-shield.md`

## Relevant (details)

### 1. CISA Adds Actively Exploited N-able MailAssure and MONAI Label Flaws to KEV Catalog
- **Source:** The Hacker News — https://thehackernews.com/2026/11/hackers-exploit-n-able-mailassure-flaw.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `ssrf`, `cve`, `vulnerability`
- **Slug:** `cisa-kev-nable-mailassure-monai-label-zero-days`
- **Must-know:** yes
- **Summary:** CISA added CVE-2026-134624 (CVSS 9.3, SSRF in N-able MailAssure's LDAP integration) and a MONAI Label zero-day to its KEV catalog, citing confirmed active exploitation. The MONAI Label flaw is reportedly being exploited by AI agents.

### 2. Radware Discloses Breach Exposing Customer Cloud Access Keys
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `cloud-security`
- **Slug:** `radware-breach-exposed-cloud-access-keys`
- **Must-know:** no
- **Summary:** Attackers gained access to some Radware customers' account details and cloud access keys through an unsecured internal Cloud WAF management API exposed online. The number of affected customers hasn't been disclosed.

### 3. Iran-Aligned Volant Manticore Uses New IPFS-Based KuboShell Backdoor
- **Source:** The Hacker News — https://thehackernews.com/2026/11/iran-aligned-volant-manticore-uses-ipfs.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `espionage`
- **Slug:** `volant-manticore-ipfs-kuboshell-backdoor`
- **Must-know:** no
- **Summary:** A previously undocumented Iran-aligned group, Volant Manticore, is targeting telecoms, airlines, and critical infrastructure in Cyprus using a new backdoor, KuboShell, that relies on IPFS for command-and-control alongside a post-compromise framework called Homa.

### 4. Hackers Compromise Check Point Security Management Servers at 22 Organizations
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-compromise-check-point-servers-in-22-organizations/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`
- **Slug:** `check-point-management-servers-compromised-22-orgs`
- **Must-know:** no
- **Summary:** Threat actors exploited multiple vulnerabilities to compromise roughly two dozen Check Point Security Management Servers in an ongoing campaign spanning 22 organizations across multiple industries.

### 5. VMware Patches Critical 9.8-Rated Auth Bypass in vCenter (CVE-2026-123903)
- **Source:** The Hacker News — https://thehackernews.com/2026/11/vmware-vcenter-hit-by-another-critical.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Slug:** `vmware-vcenter-auth-bypass-cve-2026-123903`
- **Must-know:** no
- **Summary:** Broadcom patched 23 vulnerabilities across VMware ESX, vCenter, Workstation, Fusion, and Avi Load Balancer, including CVE-2026-123903, a critical 9.8-rated authentication bypass in VMware Directory Service (vmdir).

### 6. Attackers Find a Way Around GitHub Actions SHA Pinning
- **Source:** The Hacker News — https://thehackernews.com/2026/11/hackers-found-way-around-github-sha.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `github`, `devsecops`
- **Slug:** `github-sha-pinning-bypass-supply-chain`
- **Must-know:** no
- **Summary:** Researchers found a way to circumvent GitHub Actions SHA pinning, long considered the standard defense against supply chain attacks, echoing the March 2026 hijack of the Trivy security scanner.

### 7. Google Researcher Shows Single-Bit .NET File Change Bypasses Windows Code Integrity
- **Source:** The Hacker News — https://thehackernews.com/2026/11/google-researcher-shows-how-single-bit.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Slug:** `dotnet-single-bit-bypass-windows-code-integrity`
- **Must-know:** no
- **Summary:** Google Project Zero's James Forshaw showed a quirk in how .NET Framework loads a program file lets a local attacker bypass two Windows protections and Oracle VirtualBox's process hardening (CVE-2026-87268).

### 8. Danfoss AK-SM 8xxA Flaw Allows Unauthenticated Code Execution (CVE-2026-129713)
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-03
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Slug:** `danfoss-ak-sm-8xxa-stack-overflow-cve-2026-129713`
- **Must-know:** no
- **Summary:** CISA disclosed CVE-2026-129713, a 9.8-rated stack-based buffer overflow in an unauthenticated CGI handler used by Danfoss AK-SM 8xxA Series controllers (≤5.4.0), deployed worldwide in commercial facilities.

### 9. 1.5 Million Impacted by Data Breach at South Korean Electric Company KEPCO
- **Source:** SecurityWeek — https://www.securityweek.com/1-5-million-impacted-by-data-breach-at-south-korean-electric-company-kepco/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `kepco-data-breach-1-5-million-customers`
- **Must-know:** no
- **Summary:** Hackers stole personal information from KEPCO's customer portal and supplier relationship management platform, affecting roughly 1.5 million people.

### 10. Microsoft Fixes Azure API Management Flaw After Actor Targets Customer Secrets
- **Source:** The Hacker News — https://thehackernews.com/2026/11/microsoft-fixes-azure-api-management.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `azure`, `microsoft`, `cloud-security`, `vulnerability`
- **Slug:** `azure-apim-classic-flaw-targeted-secrets`
- **Must-know:** no
- **Summary:** Norway's NSM disclosed a Microsoft Azure API Management (APIM) vulnerability an unknown actor exploited to search for access tokens, secrets, and named values at multiple Norwegian firms, including Equinor and Skagerak Energi. Microsoft has fixed the flaw.

### 11. Elecbrakes Bluetooth Vulnerabilities Expose Trailers to Forced Braking
- **Source:** SecurityWeek — https://www.securityweek.com/elecbrakes-bluetooth-vulnerabilities-expose-trailers-to-forced-braking/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`
- **Slug:** `elecbrakes-bluetooth-forced-braking-vulnerabilities`
- **Must-know:** no
- **Summary:** Critical Bluetooth flaws in Elecbrakes trailer brake controllers could let a nearby attacker force trailer braking, potentially causing accidents.

### 12. WHMCS SQL Injection Flaw Exposes Customer Data and Admin Password Hashes Without Login
- **Source:** The Hacker News — https://thehackernews.com/2026/11/whmcs-sql-injection-flaw-could-expose.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `sqli`, `vulnerability`
- **Slug:** `whmcs-sql-injection-exposes-admin-password-hashes`
- **Must-know:** no
- **Summary:** A SQL injection flaw in WHMCS's shopping cart module lets anyone on the internet retrieve customer records and admin password hashes with no login required. WHMCS is widely used by web hosting companies.

### 13. European Commission Confirms AI-Assisted Cyberattack Behind EU Academy Breach
- **Source:** SecurityWeek — https://www.securityweek.com/european-commission-uncovers-data-breach-in-cyberattack-investigation/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `eu-academy-breach-ai-assisted-cyberattack`
- **Must-know:** no
- **Summary:** The European Commission confirmed names and email addresses of EU Academy users were exposed in an AI-assisted cyberattack it detected in October. The number of affected users hasn't been disclosed.

### 14. UK Cyber Agency Reports Marked Rise in AI-Driven Cyberattacks
- **Source:** The Record (Recorded Future) — https://therecord.media/cyberattacks-uk-artificial-intelligence
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`
- **Slug:** `uk-ncsc-ai-driven-cyberattacks-rise`
- **Must-know:** no
- **Summary:** Britain's NCSC reported a "marked rise" since September in AI-assisted cyberattacks, warning the technology increases attackers' speed, scale, and persistence — mostly by exploiting long-standing basic security weaknesses.

### 15. Okta Links ShinyHunters-Associated Vishing Group to New INCEPTION Data Leak Site
- **Source:** The Hacker News — https://thehackernews.com/2026/11/okta-links-shinyhunters-associated.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `data-breach`
- **Slug:** `shinyhunters-inception-data-leak-site`
- **Must-know:** no
- **Summary:** Okta's Threat Intelligence team linked vishing cluster O-UNC-053, previously tied to ShinyHunters, to a new data leak site called INCEPTION, following a wave of FBI arrests targeting alleged ShinyHunters members.

### 16. McDonald's Japan Breach Exposes Customer Purchase History and Location Data
- **Source:** The Record (Recorded Future) — https://therecord.media/japan-mcdonalds-cyberattack-breach
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `mcdonalds-japan-breach-purchase-location-data`
- **Must-know:** no
- **Summary:** McDonald's Japan disclosed a breach exposing customers' purchase histories and mobile device location data collected through the company's smartphone app.

### 17. Unit 42 Details Tactics in Agentic AI Attack Campaigns
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/autonomous-ai-agent-threat-campaigns/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `llm`, `ai-safety`, `malware`
- **Slug:** `unit42-agentic-ai-attack-campaigns`
- **Must-know:** no
- **Summary:** Palo Alto's Unit 42 tracked campaigns where attackers deployed autonomous AI agents to automate multi-platform intrusions using standard tooling, while leaving operational traces defenders can use for detection.

### 18. Anthropic Expands Enterprise Safeguards for Detecting Claude Misuse
- **Source:** SecurityWeek — https://www.securityweek.com/anthropic-expands-enterprise-safeguards-for-detecting-ai-misuse/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `anthropic`, `ai-safety`, `llm`
- **Slug:** `anthropic-enterprise-safeguards-misuse-detection`
- **Must-know:** no
- **Summary:** Anthropic rolled out an Enterprise Feature Set that helps zero-retention customers detect Claude misuse spread across many requests while keeping conversation data in their own cloud environment.

### 19. OpenAI and Cisco Launch Shirudo, an Open-Source Linux Exploit Shield
- **Source:** The Hacker News — https://thehackernews.com/2026/11/openai-and-cisco-unveil-ai-assisted.html
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `openai`, `devsecops`, `llm`
- **Slug:** `openai-cisco-shirudo-linux-exploit-shield`
- **Must-know:** no
- **Summary:** OpenAI and Cisco released Shirudo, an open-source Linux runtime that lets AI agents write dynamic eBPF controls to shield unpatched systems from exploits without a restart, buying defenders time to patch.

## Skippable

- **David Fincher is being dragged for suspected use of AI in his latest film** — The Verge AI. Entertainment controversy, no security/safety substance.
- **UK warns AI-driven cyberattacks are exposing years of weak security** — TechCrunch AI. Duplicate coverage of the NCSC AI-attack warning (see The Record item).
- **Lawmakers warn ID verification companies to bolster security after September hack** — The Record. Congressional letter with no new technical detail beyond the already-reported September IDscan breach.
- **AWS achieves Spain's national Limited Distribution and NATO Restricted accreditation** — AWS Security Blog. Compliance/accreditation announcement, no security substance.
- **Tidal will start banning AI-generated music next month** — The Verge AI. Platform content-policy change, no security angle.
- **Built for trust and control: Powering the next wave of AI agents across Google Workspace and Google Cloud** — Google Cloud Security. Marketing overview of existing safeguards, no new incident or finding.
- **Meta brings its Muse AI assistant directly into Instagram DMs** — TechCrunch AI. Product feature launch, no security angle.
- **GPT 6.2 Astra Solves a Historical Mystery** — Simon Willison. Capability anecdote, no security/safety substance.
- **Tidal to ban and remove millions of AI-generated tracks** — TechCrunch AI. Duplicate coverage of Tidal's AI music ban.
- **Microduck Obstacle Avoidance: A Sim2Real Workflow with Isaac Lab and Newton** — Hugging Face Blog. Robotics tutorial, not a major model launch or security-relevant.
- **VMware Updates Patch Critical ESX, vCenter Vulnerabilities** — SecurityWeek. Duplicate coverage of the VMware vCenter patch (see Hacker News item with CVE detail).
- **ShinyHunters claims to return after FBI arrests, uses old PGP keys as proof** — BleepingComputer. Duplicate coverage of the ShinyHunters/INCEPTION story (see Hacker News/Okta item).
- **Jensen Huang deepfakes are the hot new AI slop** — The Verge AI. Viral deepfake gossip, no technical security substance.
- **European Commission confirms data theft in EU Academy breach** — BleepingComputer. Duplicate coverage of the EU Academy breach (see SecurityWeek item with AI-assisted detail).
- **Why a Crusoe investor is betting on solar and batteries to power future AI data centers** — TechCrunch AI. Energy/infrastructure investment story, no security angle.
- **The New York Times warns photographers not to update Photoshop over AI features** — The Verge AI. Consumer AI-features controversy, no security substance.
- **Pinterest will now let parents limit the AI-generated content their teens see** — TechCrunch AI. Platform parental-control feature, no security angle.
- **Carnegie Endowment for International Peace says third-party breach leaked donation info** — The Record. Generic third-party vendor breach disclosure, no technical detail or scale given.
- **How Gemini is changing the game for Golden State's organization and fans** — Google AI Blog. Marketing/partnership announcement, no security or model-launch substance.
- **Amazon's Decart acquisition is a bet on using software to narrow the silicon gap with Nvidia** — TechCrunch AI. AI chip/acquisition business story, no security angle.
- **AWS Weekly Roundup: Local Zone in Bogotá, 30-minute Lambda timeout, and more** — AWS News Blog. Generic service roundup, no security substance.
- **Police disrupt 57 illegal streaming services with 7.3 million visits** — BleepingComputer. Piracy enforcement action, no security/AI angle.
- **From Vulnerability Noise to Resilience: Rethinking Security in the AI Era** — BleepingComputer (RapidFort). Vendor marketing content disguised as news.
- **CISA warns of exploited N-able bug as company restores email platform** — The Record. Duplicate coverage of the N-able MailAssure KEV addition (see Hacker News item with CVE/CVSS detail).
- **Check Point Security Management Servers Hacked in AI-Assisted Campaign** — SecurityWeek. Duplicate coverage of the Check Point compromise (see BleepingComputer item).
- **Flashpoint Surpasses 8,600 Known Exploited Vulnerabilities as AI Accelerates Discovery** — Flashpoint. Vendor milestone/marketing content.
- **McDonald's Japan data breach exposes customer location information** — BleepingComputer. Duplicate coverage of the McDonald's Japan breach (see The Record item).
- **New Shirudo tool uses AI to shield unpatched Linux systems from exploits** — BleepingComputer. Duplicate coverage of the Shirudo launch (see Hacker News item).
- **OpenAI, Cisco Unveil Open Source Tool to Shield Unpatched Linux Systems** — SecurityWeek. Duplicate coverage of the Shirudo launch (see Hacker News item).
- **2027 SOC Budget Reset: 5 Priorities to Cut Costs and Reduce Cyber Risk** — The Hacker News (ANY.RUN sponsored). Vendor marketing content disguised as news.
- **Schneider Electric EcoStruxure Power Build Rapsody software** — CISA Alerts. Local-attacker-only ICS advisory, routine disclosure without active exploitation.
- **AutomationDirect C-More EA9 Programming Software** — CISA Alerts. Requires a user to open a malicious file; routine ICS advisory without active exploitation.
- **Peninsula Energy Halts Trading After Cyber Incident Hits US Uranium Mine** — SecurityWeek. Generic incident disclosure, no technical detail or IOCs given.
