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
- **Severity:** critical
- **Tags:** `cve`, `data-breach`, `vulnerability`
- **Summary:** CISA warns that the FortiBleed Fortinet credential-leak campaign, attributed to Russian-speaking actors, now affects 86,644 FortiGate devices — up from ~74,000 reported yesterday, with confirmed ongoing malicious activity.

### 2. CISA: Critical Splunk Enterprise Flaw Actively Exploited, Patch by Sunday
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-splunk-enterprise-flaw-actively-exploited-patch-by-sunday/
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`
- **Summary:** CISA ordered federal agencies to patch a critical, actively exploited Splunk Enterprise vulnerability by Sunday.

### 3. Salesforce Disables Klue App After OAuth Token Abuse Exposes Customer Data in Supply Chain Attack
- **Source:** The Hacker News — https://thehackernews.com/2026/06/salesforce-disables-klue-app.html
- **Severity:** critical
- **Tags:** `supply-chain`, `data-breach`
- **Summary:** A compromise at Klue led to OAuth token abuse against its Salesforce integration, exposing customer data at multiple downstream firms including Huntress and Recorded Future; Salesforce has disabled the integration.

### 4. Texas Government Data Breach Exposes Over 3 Million Driver's Licenses
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/texas-govt-data-breach-exposes-over-3-million-drivers-licenses/
- **Severity:** critical
- **Tags:** `data-breach`
- **Summary:** A breach at a vendor used by the Texas Parks and Wildlife Department exposed personal data, including driver's licenses, for more than 3 million people.

### 5. AutoJack Attack Lets a Single Web Page Hijack AI Browsing Agents for Host Code Execution
- **Source:** The Hacker News — https://thehackernews.com/2026/06/autojack-attack-lets-one-web-page.html
- **Severity:** high
- **Tags:** `rce`, `llm`, `ai-safety`
- **Summary:** Microsoft researchers detailed AutoJack, where a malicious web page steers an AI browsing agent into executing code on the host with no credentials and no further interaction.

### 6. The Gentlemen RaaS Uses GentleKiller EDR Killer Framework Targeting 400 Security Processes
- **Source:** The Hacker News — https://thehackernews.com/2026/06/the-gentlemen-raas-uses-gentlekiller.html
- **Severity:** high
- **Tags:** `ransomware`, `malware`
- **Summary:** The Gentlemen RaaS distributes GentleKiller, an EDR-killer toolkit covering roughly 400 security processes, to affiliates ahead of encryption.

### 7. Unpatchable 'usbliter8' Exploit Breaks Apple A12/A13 SecureROM Boot Chain
- **Source:** The Hacker News — https://thehackernews.com/2026/06/unpatchable-usbliter8-exploit-breaks.html
- **Severity:** high
- **Tags:** `vulnerability`, `apple`
- **Summary:** Researchers published usbliter8, achieving code execution in the SecureROM of Apple A12/A13 chips — a flaw burned into silicon with no possible software fix.

### 8. Operation Endgame Disrupts SocGholish Infrastructure, Cleans Up Nearly 15,000 WordPress Sites
- **Source:** The Hacker News — https://thehackernews.com/2026/06/operation-endgame-disrupts-socgholish.html
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** Law enforcement from the Netherlands, Canada, Germany and the U.S. disrupted SocGholish infrastructure (linked to Evil Corp) and cleaned nearly 15,000 infected WordPress sites.

### 9. CryptoBandits Malware Combines Backdoor and Infostealer, Abuses Tor for C2
- **Source:** SecurityWeek — https://www.securityweek.com/cryptobandits-malware-doubles-as-a-backdoor-abuses-tor/
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** CryptoBandits runs a local SOCKS5 proxy over Tor for C2 while combining data theft and remote code execution in one backdoor.

### 10. Apple Patches Beats Studio Buds Bluetooth Flaw Letting Nearby Attackers Eavesdrop
- **Source:** The Hacker News — https://thehackernews.com/2026/06/apple-patches-beats-studio-buds-flaw.html
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`, `apple`
- **Summary:** Apple patched CVE-2025-20701 (CVSS 8.8), an incorrect-authorization flaw in the Airoha Bluetooth SDK letting a nearby attacker pair with Beats Studio Buds without consent and eavesdrop.

## Skippable

- **Is the US government's Anthropic ban accidentally helping the brand?** — TechCrunch AI. Opinion piece rehashing the already-reported Anthropic ban.
- **The US banned Anthropic's Fable 5 release, but the numbers don't seem to care** — TechCrunch AI. Duplicate opinion coverage of the same Anthropic ban story.
- **In Other News: Apple Patches Beats Eavesdropping Flaw, DOT Closes Delta CrowdStrike Probe, AWS Continuum** — SecurityWeek. Roundup of one-line mentions with no depth; the Beats item is covered above via a dedicated article.
- **Billionaire Ambani wants AI in every call, app, and home** — TechCrunch AI. Generic AI business story, no security angle.
- **The film about Sam Altman has been dropped by Amazon MGM** — The Verge AI. Entertainment news, no security substance.
- **Every AI Agent Is an Identity. Most Organizations Don't Treat Them That Way** — BleepingComputer. Vendor thought-leadership content, not news.
- **The Good, the Bad and the Ugly in Cybersecurity – Week 25** — SentinelOne Labs. Weekly roundup with no technical substance per sub-item.
- **Stressors, AI Forcing Changes to Cybersecurity Teams** — Dark Reading. Industry/career commentary, no technical news.
- **The CEO of Allbirds' new AI biz has a plan, but no employees** — TechCrunch AI. Generic AI startup story, no security angle.
- **Police raid malware network tied to Russia's Evil Corp hacker group** — The Record. Duplicate of the Operation Endgame/SocGholish takedown, covered above.
- **Webinar: How attackers bypass MFA and how defenders can respond** — BleepingComputer. Vendor webinar promotion, not news.
- **From Assistive to Agentic: The AI Shift That's Redefining Threat Management** — The Hacker News. Vendor thought-leadership piece, no concrete incident.
- **Microsoft: June 2026 Windows updates break Recycle Bin prompts** — BleepingComputer. Cosmetic UI bug, no security impact.
- **UK's information commissioner resigns over 'inappropriate humour'** — The Record. Personnel/political story, no security substance.
- **FortiBleed: 86,000 Fortinet Device Credentials Compromised** — SecurityWeek. Duplicate of the FortiBleed/CISA story, covered above.
- **Forget Data Leakage: Shadow AI's Real Threat Is Access Control** — The Hacker News. Opinion piece, no concrete incident.
- **Cybersecurity Firms Impacted by Klue Supply Chain Attack** — SecurityWeek. Duplicate of the Klue/Salesforce supply chain story, covered above.
- **NY man charged after harassing college student with AI-generated nudes** — BleepingComputer. Single-individual criminal case, regional incident.
- **The US says ASML's top chip tool may be in China. ASML says it isn't** — TechCrunch AI. Unresolved dispute, no confirmed facts.
- **Cisco to Acquire WideField Security to Boost Splunk's Agentic SOC** — SecurityWeek. M&A business news, no actionable technical signal.
- **CISA warns Fortinet users to secure devices after FortiBleed leak** — BleepingComputer. Duplicate of the FortiBleed/CISA story, covered above.
- **15,000 WordPress Websites Cleaned Up in SocGholish Botnet Takedown** — SecurityWeek. Duplicate of the Operation Endgame/SocGholish takedown, covered above.
