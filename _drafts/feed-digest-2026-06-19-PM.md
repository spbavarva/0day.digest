# Digest — 2026-06-19 PM

- Window: last 14h
- Raw items considered: 32
- Relevant: 10
- Skippable: 22

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** CISA Warns Fortinet Customers as FortiBleed Credential Leak Hits 86,644 FortiGate Devices — `2026-06-19-fortibleed-cisa-warning-86000-devices.md`
- [x] **[CRITICAL]** CISA: Critical Splunk Enterprise Flaw Actively Exploited, Patch by Sunday — `2026-06-19-cisa-splunk-enterprise-actively-exploited.md`
- [x] **[CRITICAL]** Salesforce Disables Klue App After OAuth Token Abuse Exposes Customer Data in Supply Chain Attack — `2026-06-19-klue-salesforce-supply-chain-attack.md`
- [x] **[CRITICAL]** Texas Government Data Breach Exposes Over 3 Million Driver's Licenses — `2026-06-19-texas-govt-breach-3-million-drivers-licenses.md`
- [x] **[HIGH]** AutoJack Attack Lets a Single Web Page Hijack AI Browsing Agents for Host Code Execution — `2026-06-19-autojack-ai-agent-rce.md`
- [x] **[HIGH]** The Gentlemen RaaS Uses GentleKiller EDR Killer Framework Targeting 400 Security Processes — `2026-06-19-gentlemen-raas-gentlekiller-edr-killer.md`
- [x] **[HIGH]** Unpatchable 'usbliter8' Exploit Breaks Apple A12/A13 SecureROM Boot Chain — `2026-06-19-usbliter8-apple-securerom-exploit.md`
- [x] **[MEDIUM]** Operation Endgame Disrupts SocGholish Infrastructure, Cleans Up Nearly 15,000 WordPress Sites — `2026-06-19-operation-endgame-socgholish-takedown.md`
- [x] **[MEDIUM]** CryptoBandits Malware Combines Backdoor and Infostealer, Abuses Tor for C2 — `2026-06-19-cryptobandits-malware-tor-backdoor.md`
- [x] **[MEDIUM]** Apple Patches Beats Studio Buds Bluetooth Flaw Letting Nearby Attackers Eavesdrop — `2026-06-19-apple-beats-studio-buds-bluetooth-flaw.md`

## Relevant (details)

### 1. CISA Warns Fortinet Customers as FortiBleed Credential Leak Hits 86,644 FortiGate Devices
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cisa-warns-fortinet-customers-as.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `data-breach`, `vulnerability`
- **Slug:** `fortibleed-cisa-warning-86000-devices`
- **Must-know:** yes
- **Summary:** CISA issued a fresh warning that the "FortiBleed" Fortinet credential-leak campaign, attributed to Russian-speaking threat actors, is now affecting 86,644 FortiGate devices — up from the ~74,000 reported yesterday. This is an escalation of a story already covered (June 18): the device count has grown and CISA now confirms ongoing malicious activity targeting affected devices.

### 2. CISA: Critical Splunk Enterprise Flaw Actively Exploited, Patch by Sunday
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-splunk-enterprise-flaw-actively-exploited-patch-by-sunday/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`
- **Slug:** `cisa-splunk-enterprise-actively-exploited`
- **Must-know:** yes
- **Summary:** CISA ordered U.S. federal agencies to patch a critical Splunk Enterprise vulnerability under active exploitation by Sunday. No technical detail on the vulnerability class was given in the feed summary beyond "critical" and "actively exploited."

### 3. Salesforce Disables Klue App After OAuth Token Abuse Exposes Customer Data in Supply Chain Attack
- **Source:** The Hacker News — https://thehackernews.com/2026/06/salesforce-disables-klue-app.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `data-breach`
- **Slug:** `klue-salesforce-supply-chain-attack`
- **Must-know:** yes
- **Summary:** Salesforce disabled the Klue Battlecards app integration after an OAuth-token-abuse incident at Klue (June 11) exposed customer data, with downstream impact confirmed at cybersecurity firms Huntress and Recorded Future. Classic third-party-app supply chain pattern: a single compromised integration exposing data across multiple customer orgs.

### 4. Texas Government Data Breach Exposes Over 3 Million Driver's Licenses
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/texas-govt-data-breach-exposes-over-3-million-drivers-licenses/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `data-breach`
- **Slug:** `texas-govt-breach-3-million-drivers-licenses`
- **Must-know:** yes
- **Summary:** A breach at a license-system vendor used by the Texas Parks and Wildlife Department exposed personal information, including driver's license data, for more than 3 million individuals. Scale alone (>100k, well past the 10k must-know threshold) makes this notable despite limited technical detail in the disclosure.

### 5. AutoJack Attack Lets a Single Web Page Hijack AI Browsing Agents for Host Code Execution
- **Source:** The Hacker News — https://thehackernews.com/2026/06/autojack-attack-lets-one-web-page.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `llm`, `ai-safety`
- **Slug:** `autojack-ai-agent-rce`
- **Must-know:** no
- **Summary:** Microsoft researchers detailed "AutoJack," an exploit chain where a malicious web page steers an AI browsing agent into reaching a privileged local service on the host machine and spawning a process — remote code execution with no credentials and no further user interaction once the agent loads the page.

### 6. The Gentlemen RaaS Uses GentleKiller EDR Killer Framework Targeting 400 Security Processes
- **Source:** The Hacker News — https://thehackernews.com/2026/06/the-gentlemen-raas-uses-gentlekiller.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`, `malware`
- **Slug:** `gentlemen-raas-gentlekiller-edr-killer`
- **Must-know:** no
- **Summary:** The Gentlemen ransomware-as-a-service operation maintains a dedicated EDR-killer toolkit, GentleKiller, distributed to affiliates to disable defenses across roughly 400 security processes before deploying the encryptor.

### 7. Unpatchable 'usbliter8' Exploit Breaks Apple A12/A13 SecureROM Boot Chain
- **Source:** The Hacker News — https://thehackernews.com/2026/06/unpatchable-usbliter8-exploit-breaks.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `apple` (new tag — Apple-specific hardware exploit coverage)
- **Slug:** `usbliter8-apple-securerom-exploit`
- **Must-know:** no
- **Summary:** Researchers at Paradigm Shift published "usbliter8," an exploit achieving arbitrary code execution inside the SecureROM of Apple A12 and A13 chips. Because SecureROM is fused into silicon at manufacture, no software update can fix it — affected devices keep the flaw for their entire service life. The summary cuts off before specifying the access vector, but states it is not remotely exploitable.

### 8. Operation Endgame Disrupts SocGholish Infrastructure, Cleans Up Nearly 15,000 WordPress Sites
- **Source:** The Hacker News — https://thehackernews.com/2026/06/operation-endgame-disrupts-socgholish.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `operation-endgame-socgholish-takedown`
- **Must-know:** no
- **Summary:** A multinational law enforcement operation (Netherlands, Canada, Germany, U.S.) disrupted infrastructure tied to the SocGholish malware loader, linked to Russia's Evil Corp, and cleaned nearly 15,000 infected WordPress sites. Picked The Hacker News as the primary source over The Record and SecurityWeek, which covered the same takedown with less detail.

### 9. CryptoBandits Malware Combines Backdoor and Infostealer, Abuses Tor for C2
- **Source:** SecurityWeek — https://www.securityweek.com/cryptobandits-malware-doubles-as-a-backdoor-abuses-tor/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `cryptobandits-malware-tor-backdoor`
- **Must-know:** no
- **Summary:** CryptoBandits malware runs a local SOCKS5 proxy over Tor for C2 traffic while combining data-theft and remote-code-execution capability in a single backdoor.

### 10. Apple Patches Beats Studio Buds Bluetooth Flaw Letting Nearby Attackers Eavesdrop
- **Source:** The Hacker News — https://thehackernews.com/2026/06/apple-patches-beats-studio-buds-flaw.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`, `apple`
- **Slug:** `apple-beats-studio-buds-bluetooth-flaw`
- **Must-know:** no
- **Summary:** Apple patched CVE-2025-20701 (CVSS 8.8) in Beats Studio Buds, an incorrect-authorization flaw in the Airoha Bluetooth audio SDK that let a nearby attacker pair with the earbuds without consent and eavesdrop via the microphone.

## Skippable

- **The Gentlemen RaaS** is covered above; no separate skip entry needed.
- **Is the US government's Anthropic ban accidentally helping the brand?** — TechCrunch AI. Opinion/analysis piece rehashing the already-reported Anthropic model ban; no new facts.
- **The US banned Anthropic's Fable 5 release, but the numbers don't seem to care** — TechCrunch AI. Duplicate opinion coverage of the same Anthropic ban story as above.
- **In Other News: Apple Patches Beats Eavesdropping Flaw, DOT Closes Delta CrowdStrike Probe, AWS Continuum** — SecurityWeek. Roundup of one-line mentions (Android TV botnet, Velvet Ant, unpatched GCP Config Connector flaw) with no depth on any single item; the Beats flaw it mentions is covered in full above via a dedicated article.
- **Billionaire Ambani wants AI in every call, app, and home** — TechCrunch AI. Generic AI business/marketing story, no security angle.
- **The film about Sam Altman has been dropped by Amazon MGM** — The Verge AI. Entertainment news, no security or technical substance.
- **Every AI Agent Is an Identity. Most Organizations Don't Treat Them That Way** — BleepingComputer. Vendor (Token Security) thought-leadership content, not news.
- **The Good, the Bad and the Ugly in Cybersecurity – Week 25** — SentinelOne Labs. Weekly roundup; each sub-item (PhaaS takedown, DragonForce/MS Teams abuse, REDCap breach) is mentioned only in passing with no technical substance to draft from.
- **Stressors, AI Forcing Changes to Cybersecurity Teams** — Dark Reading. Industry/career commentary on CISO workload, no technical news.
- **The CEO of Allbirds' new AI biz has a plan, but no employees** — TechCrunch AI. Generic AI startup business story, no security angle.
- **Police raid malware network tied to Russia's Evil Corp hacker group** — The Record. Duplicate coverage of the Operation Endgame/SocGholish takedown, covered above via The Hacker News.
- **Webinar: How attackers bypass MFA and how defenders can respond** — BleepingComputer. Vendor webinar promotion, not news.
- **From Assistive to Agentic: The AI Shift That's Redefining Threat Management** — The Hacker News. Vendor thought-leadership piece on AI SOC tooling, no concrete incident or news.
- **Microsoft: June 2026 Windows updates break Recycle Bin prompts** — BleepingComputer. Cosmetic UI bug, no security impact.
- **UK's information commissioner resigns over 'inappropriate humour'** — The Record. Personnel/political story, no security substance.
- **FortiBleed: 86,000 Fortinet Device Credentials Compromised** — SecurityWeek. Duplicate coverage of the FortiBleed/CISA story, covered above via The Hacker News (more current device count and threat-actor attribution).
- **Forget Data Leakage: Shadow AI's Real Threat Is Access Control** — The Hacker News. Opinion/thought-leadership piece, no concrete incident.
- **Cybersecurity Firms Impacted by Klue Supply Chain Attack** — SecurityWeek. Duplicate coverage of the Klue/Salesforce supply chain story, covered above via The Hacker News (more technical detail on the OAuth token abuse).
- **NY man charged after harassing college student with AI-generated nudes** — BleepingComputer. Single-individual criminal case, regional/local incident.
- **The US says ASML's top chip tool may be in China. ASML says it isn't** — TechCrunch AI. Unresolved dispute/analysis piece, no confirmed facts or security impact.
- **Cisco to Acquire WideField Security to Boost Splunk's Agentic SOC** — SecurityWeek. M&A business news, no actionable technical signal.
- **CISA warns Fortinet users to secure devices after FortiBleed leak** — BleepingComputer. Duplicate coverage of the FortiBleed/CISA story, covered above via The Hacker News.
- **15,000 WordPress Websites Cleaned Up in SocGholish Botnet Takedown** — SecurityWeek. Duplicate coverage of the Operation Endgame/SocGholish takedown, covered above via The Hacker News.
