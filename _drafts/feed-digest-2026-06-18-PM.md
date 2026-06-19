# Digest — 2026-06-18 PM

- Window: last 14h
- Raw items considered: 54
- Relevant: 15
- Skippable: 39

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[INFORMATIONAL]** AWS Launches Kiro CLI to Accelerate Security Investigations — `2026-06-18-aws-kiro-cli-security-investigations.md`
- [x] **[HIGH]** FIFA Bug Exposed World Cup Streams to Remote Takeover via Unenforced Entra Controls — `2026-06-18-fifa-entra-access-control-bug-world-cup-streams.md`
- [x] **[MEDIUM]** 'Popa' Android Botnet Linked to Publicly-Traded Israeli Proxy Firm — `2026-06-18-popa-botnet-netnut-alarum-technologies.md`
- [x] **[CRITICAL]** F5 Patches Two Critical NGINX Open Source RCE Flaws — `2026-06-18-f5-nginx-critical-rce-flaws-patched.md`
- [x] **[MEDIUM]** Most Internet-Exposed REDCap Servers Are Running Outdated Versions — `2026-06-18-redcap-servers-outdated-unc6508-targeting.md`
- [x] **[HIGH]** Microsoft Details Windows Clipper Malware Spread via USB LNK Worm and Tor C2 — `2026-06-18-windows-clipper-malware-usb-lnk-worm-tor-c2.md`
- [x] **[HIGH]** Klue OAuth Breach Tied to 'Icarus' Salesforce Data Theft Campaign — `2026-06-18-klue-oauth-breach-icarus-salesforce-data-theft.md`
- [x] **[MEDIUM]** INC Ransomware Claims 830+ Victims Since 2023, Emerges as Major RaaS Threat — `2026-06-18-inc-ransomware-830-victims-raas-evolution.md`
- [x] **[HIGH]** DragonForce-Linked Actors Abuse Microsoft Teams Relays to Hide Backdoor.Turn C2 Traffic — `2026-06-18-dragonforce-teams-relay-backdoor-turn-c2.md`
- [x] **[INFORMATIONAL]** Law Enforcement Cleans Nearly 15,000 SocGholish-Infected Sites Tied to Evil Corp — `2026-06-18-socgholish-takedown-evil-corp-15000-sites.md`
- [x] **[CRITICAL]** ShapedPlugin Update Mechanism Hijacked to Distribute Malware to WordPress Sites — `2026-06-18-shapedplugin-wordpress-supply-chain-attack.md`
- [x] **[CRITICAL]** 'FortiBleed' Leak Exposes Fortinet VPN Credentials for 73,000 Devices — `2026-06-18-fortibleed-fortinet-vpn-credential-leak.md`
- [x] **[HIGH]** Apple Fixes Beats Studio Buds Flaw That Allowed Eavesdropping — `2026-06-18-apple-beats-studio-buds-eavesdropping-flaw.md`
- [x] **[CRITICAL]** CISA Adds Actively Exploited Splunk Enterprise Auth Bypass to KEV Catalog — `2026-06-18-cisa-kev-splunk-enterprise-missing-authentication.md`
- [x] **[CRITICAL]** Critical Flaw in AVer PTC Cameras (CVSS 9.8) Allows Arbitrary Code Execution — `2026-06-18-aver-ptc-cameras-critical-rce-flaw.md`

## Relevant (details)

### 1. AWS Launches Kiro CLI to Accelerate Security Investigations
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/accelerate-security-investigations-with-kiro-cli/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `cloud-security`, `aws`, `llm`, `devsecops`
- **Slug:** `aws-kiro-cli-security-investigations`
- **Must-know:** no
- **Summary:** AWS released a CLI tool designed to speed up security investigations by reducing manual correlation work across GuardDuty, CloudTrail, and other services. Targets analysts who currently struggle with recalling AWS CLI syntax during incident response.

### 2. FIFA Bug Exposed World Cup Streams to Remote Takeover via Unenforced Entra Controls
- **Source:** Dark Reading — https://www.darkreading.com/application-security/fifa-bug-world-cup-streams-remote-takeover
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `iam`, `vulnerability`, `appsec`, `microsoft`
- **Slug:** `fifa-entra-access-control-bug-world-cup-streams`
- **Must-know:** no
- **Summary:** Unenforced Microsoft Entra access controls on FIFA's infrastructure could have let a hacker hijack World Cup stream broadcasts. Highlights identity/access misconfiguration risk on high-profile public infrastructure.

### 3. 'Popa' Android Botnet Linked to Publicly-Traded Israeli Proxy Firm
- **Source:** Krebs on Security — https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `data-breach`
- **Slug:** `popa-botnet-netnut-alarum-technologies`
- **Must-know:** no
- **Summary:** A four-year-old Android botnet relaying traffic from millions of TV boxes has been linked to NetNut, a residential proxy service operated by NASDAQ-listed Alarum Technologies. Traffic supported ad fraud, account takeovers, and data scraping.

### 4. F5 Patches Two Critical NGINX Open Source RCE Flaws
- **Source:** The Hacker News — https://thehackernews.com/2026/06/f5-patches-two-critical-nginx-open.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`, `cve`, `appsec`
- **Slug:** `f5-nginx-critical-rce-flaws-patched`
- **Must-know:** no
- **Summary:** F5 patched two critical NGINX Open Source flaws enabling remote code execution. CVE-2026-42530 (CVSS v4 9.2) is an unauthenticated, remote use-after-free in ngx_http_v3_module.

### 5. Most Internet-Exposed REDCap Servers Are Running Outdated Versions
- **Source:** SecurityWeek — https://www.securityweek.com/majority-of-internet-accessible-redcap-servers-outdated/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `appsec`, `privilege-escalation`
- **Slug:** `redcap-servers-outdated-unc6508-targeting`
- **Must-know:** no
- **Summary:** Most internet-accessible REDCap research servers are outdated and regularly targeted by China-linked UNC6508 for initial access and backdoor deployment.

### 6. Microsoft Details Windows Clipper Malware Spread via USB LNK Worm and Tor C2
- **Source:** The Hacker News — https://thehackernews.com/2026/06/microsoft-details-windows-clipper.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `microsoft`
- **Slug:** `windows-clipper-malware-usb-lnk-worm-tor-c2`
- **Must-know:** no
- **Summary:** Microsoft detailed a crypto-clipper campaign active since February 2026 that self-propagates via USB LNK files and uses ActiveX/WSH to launch a Tor proxy polling a hidden-service C2 server.

### 7. Klue OAuth Breach Tied to 'Icarus' Salesforce Data Theft Campaign
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/klue-oauth-breach-linked-to-icarus-salesforce-data-theft-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `supply-chain`, `iam`
- **Slug:** `klue-oauth-breach-icarus-salesforce-data-theft`
- **Must-know:** no
- **Summary:** Klue suffered an OAuth breach enabling "Icarus" threat actors to steal Salesforce CRM data from multiple connected orgs, including cybersecurity vendor Huntress, in an ongoing extortion campaign. (Best-source pick over Dark Reading's broader coverage of the same incident, item skipped below.)

### 8. INC Ransomware Claims 830+ Victims Since 2023, Emerges as Major RaaS Threat
- **Source:** The Hacker News — https://thehackernews.com/2026/06/inc-ransomware-claims-830-victims-since.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ransomware`, `malware`
- **Slug:** `inc-ransomware-830-victims-raas-evolution`
- **Must-know:** no
- **Summary:** INC has grown into a major ransomware-as-a-service operation with 830+ victims since August 2023, absorbing affiliates displaced by the LockBit and BlackCat takedowns.

### 9. DragonForce-Linked Actors Abuse Microsoft Teams Relays to Hide Backdoor.Turn C2 Traffic
- **Source:** The Hacker News — https://thehackernews.com/2026/06/dragonforce-hackers-abuse-microsoft.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`, `malware`, `microsoft`
- **Slug:** `dragonforce-teams-relay-backdoor-turn-c2`
- **Must-know:** no
- **Summary:** DragonForce-linked actors used a Go-based RAT (Backdoor.Turn) to hide C2 traffic inside Microsoft Teams relay infrastructure, deployed against a major U.S. services firm per Symantec/Carbon Black.

### 10. Law Enforcement Cleans Nearly 15,000 SocGholish-Infected Sites Tied to Evil Corp
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/law-enforcement-nukes-socgholish-malware-from-nearly-15-000-sites/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `malware`
- **Slug:** `socgholish-takedown-evil-corp-15000-sites`
- **Must-know:** no
- **Summary:** International law enforcement cleaned SocGholish malware from ~15,000 WordPress sites and took down 100+ servers tied to Evil Corp, disrupting a major fake-update initial-access malware family.

### 11. ShapedPlugin Update Mechanism Hijacked to Distribute Malware to WordPress Sites
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/shapedplugin-update-flow-hacked-to-infect-wordpress-sites/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`
- **Slug:** `shapedplugin-wordpress-supply-chain-attack`
- **Must-know:** yes
- **Summary:** Multiple ShapedPlugin WordPress plugins were compromised in a supply chain attack distributing infected releases to paying customers via the vendor's own update system.

### 12. 'FortiBleed' Leak Exposes Fortinet VPN Credentials for 73,000 Devices
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/fortibleed-leak-exposes-fortinet-vpn-credentials-for-73-000-devices/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `data-breach`, `vulnerability`, `cve`
- **Slug:** `fortibleed-fortinet-vpn-credential-leak`
- **Must-know:** yes
- **Summary:** A leak dubbed "FortiBleed" exposed Fortinet/FortiGate VPN credentials for 73,932 firewall URLs worldwide, a large-scale credential exposure warranting precautionary rotation.

### 13. Apple Fixes Beats Studio Buds Flaw That Allowed Eavesdropping
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/apple-fixes-beats-studio-buds-flaw-that-let-hackers-spy-on-conversations/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`
- **Slug:** `apple-beats-studio-buds-eavesdropping-flaw`
- **Must-know:** no
- **Summary:** Apple patched a high-severity flaw in Beats Studio Buds that let nearby attackers eavesdrop on conversations over Bluetooth.

### 14. CISA Adds Actively Exploited Splunk Enterprise Auth Bypass to KEV Catalog
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/alerts/2026/06/18/cisa-adds-one-known-exploited-vulnerability-catalog
- **Section:** Government / Advisory
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `zero-day`, `iam`
- **Slug:** `cisa-kev-splunk-enterprise-missing-authentication`
- **Must-know:** yes
- **Summary:** CISA added CVE-2026-20253, a missing-authentication flaw in Splunk Enterprise, to its KEV catalog based on evidence of active exploitation; federal agencies must prioritize patching under BOD 26-04.

### 15. Critical Flaw in AVer PTC Cameras (CVSS 9.8) Allows Arbitrary Code Execution
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-169-01
- **Section:** Government / Advisory
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `aver-ptc-cameras-critical-rce-flaw`
- **Must-know:** no
- **Summary:** A critical flaw (CVSS 9.8) in AVer PTC pan-tilt cameras, caused by files/directories exposed to external parties, could allow arbitrary code execution; devices are deployed worldwide across government, commercial, and healthcare sectors.

## Skippable

- **Almost half of U.S. singles feel negatively about AI in dating** — TechCrunch AI. Generic consumer/dating AI sentiment story, no security or AI-substance angle.
- **Nintendo confirms data stolen in WebMD subsidiary cyberattack** — BleepingComputer. Generic breach disclosure (third-party TinyPulse survey data) with no technical detail or victim count.
- **Amazon hopes to challenge Nvidia more directly by selling its AI chips** — TechCrunch AI. Generic business/competitive AI hardware news, no security angle.
- **MosaicLeaks: Can your research agent keep a secret?** — Hugging Face Blog. No usable summary in the feed pull; insufficient information to draft a factual post without fabricating details.
- **Close Encounters of the Human Kind** — Cisco Talos. Opinion/awareness piece on human behavior in security, no new technical content.
- **AI data centers just got a government-mandated fast lane to the grid** — TechCrunch AI. Energy/grid policy story, not a security or AI-capability item.
- **The smartphone era created an attention crisis. Slowtech is fixing it** — TechCrunch AI. Generic lifestyle/consumer tech story, no security relevance.
- **New usage analytics and updated spend controls for enterprises** — OpenAI Blog. Generic product/billing feature announcement, no security or safety substance.
- **'Queer Eye's' life coach Karamo Brown launches Kē** — TechCrunch AI. Generic consumer AI wellness app launch, no security angle.
- **Spring 2026 SOC 1 and 2 reports are now available in OSCAL format** — AWS Security Blog. Compliance-report format update; procedural, not actionable security content.
- **Salesforce Data Thefts Continue via Klue App Compromise** — Dark Reading. Duplicate coverage of the Klue/Icarus story; BleepingComputer's OAuth-breach angle (item 7 above) carries more technical detail.
- **USB worm spreads crypto-stealing malware via Windows shortcut files** — BleepingComputer. Duplicate coverage of the same clipper campaign; Microsoft's own technical writeup (item 6 above) is the better source.
- **Amazon employees say they're facing termination for backing data center limits** — The Verge AI. Labor/political dispute story, no security or technical AI content.
- **Orphaned AI Agents: How to Find Hidden Access Risks Inside Your Network** — The Hacker News. Reads as vendor thought-leadership/sponsored content without specific findings, IOCs, or new research.
- **ThreatsDay Bulletin: Claude Chat Abuse, NastyC2 npm Packages, Device-Code Phishing + 25 More Stories** — The Hacker News. Weekly roundup bulletin; individual items teased but not detailed enough to draft a factual standalone post without fabrication.
- **General Intuition in talks to raise $300M at around $2B valuation** — TechCrunch AI. Generic startup funding news, no security angle.
- **A tech worker-backed PAC is bringing a $5M knife to Big Tech's $100M gunfight** — TechCrunch AI. AI policy/politics story, no direct security substance.
- **Australian sugar producer works to restore operations as ransomware group claims attack** — The Record. Ransomware victim disclosure without TTPs or IOCs.
- **Who decides when AI is too dangerous?** — The Verge AI (podcast). Commentary/podcast discussion of an already-known prior controversy, not new news.
- **The Scripts on Your Checkout Page Are Now a PCI DSS Problem** — The Hacker News. Marketing content (vendor-commissioned QSA assessment) disguised as news.
- **5 reasons Microsoft 365 backup isn't enough for business data protection** — BleepingComputer. Sponsored/marketing content (Acronis), no new technical substance.
- **Accenture to Acquire Majority Stake in Dragos, All of runZero, NetRise in $4.1 Billion OT Cybersecurity Push** — SecurityWeek. M&A/business news, no technical security content.
- **Get Out of Security Debt by Tackling the Exposure Problem** — Dark Reading. Opinion/strategy piece without specific news value.
- **Photoshop and Premiere now have AI assistants** — The Verge AI. Consumer product feature rollout, no security or safety substance.
- **Adobe's redesigned AI studio remembers what your creations look like** — The Verge AI. Consumer product feature rollout, no security or safety substance.
- **No Exploits Required** — SecurityWeek. Opinion piece without specific news value.
- **Telegram admits it couldn't police exam-leak channels, India tells court** — BleepingComputer. Legal/content-moderation court story, no technical security relevance.
- **Pixi's new iOS app turns text messages into interactive AR experiences** — TechCrunch AI. Generic consumer messaging app launch, no security angle.
- **Apollo Pharmacy Blood Glucose Monitoring System APG-01 BT** — CISA Alerts. Routine ICS/medical advisory (CVSS 6.5), below the bar relative to other items in this window.
- **Schneider Electric EasyLogic T150 and Saitel DP** — CISA Alerts. Routine ICS advisory, below the bar relative to other items in this window.
- **Rockwell Automation FactoryTalk Historian Site Edition** — CISA Alerts. Routine ICS advisory (CVSS 7.7), below the bar relative to other items in this window.
- **AzeoTech DAQFactory** — CISA Alerts. Routine ICS advisory (CVSS 7.8), below the bar relative to other items in this window.
- **Schneider Electric Easergy, EcoStruxture, PowerLogic, and Saitel Products** — CISA Alerts. Routine ICS advisory, below the bar relative to other items in this window.
- **Mitsubishi Electric MELSEC iQ-F Series** — CISA Alerts. Routine ICS advisory, denial-of-service only (CVSS 7.5).
- **Mitsubishi Electric Co.'s MELSEC iQ-F Series FX5-ENET/IP Ethernet Module** — CISA Alerts. Routine ICS advisory, denial-of-service only; same product family as the prior item.
- **Dream Raises $260 Million at $3 Billion Valuation** — SecurityWeek. Generic startup funding news, no technical substance.
- **F5 issues out-of-band patches for critical NGINX vulnerabilities** — BleepingComputer. Duplicate coverage of the F5/NGINX story; The Hacker News' coverage with the CVE/CVSS detail (item 4 above) is the better source.
- **Improving health intelligence in ChatGPT** — OpenAI Blog. Generic product feature update, no security or safety-incident substance.
- **Using AI to help physicians diagnose rare genetic diseases affecting children** — OpenAI Blog. Health-applications case study, no security angle.
