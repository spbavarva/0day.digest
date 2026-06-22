# Digest — 2026-06-22 PM

- Window: last 14h
- Raw items considered: 17
- Relevant: 9
- Skippable: 8

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Attackers Exploit Gravity SMTP Plugin Flaw to Harvest WordPress Data — `2026-06-22-gravity-smtp-plugin-wordpress-data-leak.md`
- [x] **[CRITICAL]** North Korean Hackers Blamed for Mastra NPM Supply Chain Attack — `2026-06-22-mastra-npm-supply-chain-north-korea.md`
- [x] **[HIGH]** Unpatchable "Usbliter8" Exploit Bypasses Apple's Boot Defenses, Affects Millions of iPhones — `2026-06-22-usbliter8-apple-boot-exploit-iphone.md`
- [x] **[MEDIUM]** VBScript Campaign Spreads Through WhatsApp to Deploy RMM Malware — `2026-06-22-whatsapp-vbscript-rmm-campaign.md`
- [x] **[CRITICAL]** Fortinet Confirms 86,000 Working Credentials Harvested in FortiBleed Campaign — `2026-06-22-fortibleed-86000-confirmed-credentials.md`
- [x] **[INFORMATIONAL]** Canada's CSIS Used First-of-Its-Kind Warrant to Disinfect Botnet Devices — `2026-06-22-csis-botnet-cleanup-warrant.md`
- [x] **[HIGH]** More Cybersecurity Firms Disclose Impact From Klue Supply Chain Hack — `2026-06-22-klue-hack-more-firms-affected.md`
- [x] **[MEDIUM]** AryStinger Malware Infects 4,300 Legacy Routers to Build Reconnaissance Proxy Network — `2026-06-22-arystinger-router-malware.md`
- [x] **[HIGH]** Texas Parks & Wildlife Data Breach Affects 3 Million Individuals — `2026-06-22-texas-parks-wildlife-breach.md`

## Relevant (details)

### 1. Attackers Exploit Gravity SMTP Plugin Flaw to Harvest WordPress Data
- **Source:** SecurityWeek — https://www.securityweek.com/attackers-exploit-gravity-smtp-plugin-flaw-to-harvest-valuable-wordpress-data/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `data-breach`, `appsec`
- **Slug:** `gravity-smtp-plugin-wordpress-data-leak`
- **Must-know:** no
- **Summary:** Attackers are exploiting a flaw in the Gravity SMTP WordPress plugin to harvest API keys, secrets, tokens, and server information from vulnerable sites. The campaign is actively in progress, putting site operators at risk of broader compromise via leaked credentials.

### 2. North Korean Hackers Blamed for Mastra NPM Supply Chain Attack
- **Source:** SecurityWeek — https://www.securityweek.com/north-korean-hackers-blamed-for-mastra-npm-supply-chain-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`
- **Slug:** `mastra-npm-supply-chain-north-korea`
- **Must-know:** yes
- **Summary:** Researchers attribute a supply chain attack on over 140 npm packages in the Mastra ecosystem to North Korean threat actors. The malicious dependency fetches a payload that targets cryptocurrency browser extensions on developer machines.

### 3. Unpatchable "Usbliter8" Exploit Bypasses Apple's Boot Defenses, Affects Millions of iPhones
- **Source:** SecurityWeek — https://www.securityweek.com/new-exploit-bypasses-apples-boot-defenses-affects-millions-of-iphones/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`
- **Slug:** `usbliter8-apple-boot-exploit-iphone`
- **Must-know:** no
- **Summary:** Researchers released a proof-of-concept exploit, "Usbliter8," that bypasses Apple's boot-time security defenses on millions of iPhones. The underlying flaw reportedly cannot be fixed via a standard software patch.

### 4. VBScript Campaign Spreads Through WhatsApp to Deploy RMM Malware
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/whatsapp-vbs-rmm-campaign/120290/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Slug:** `whatsapp-vbscript-rmm-campaign`
- **Must-know:** no
- **Summary:** Kaspersky documented a global campaign distributing VBScript files via WhatsApp through a multi-stage infection chain that ultimately installs a UEMS remote monitoring and management (RMM) agent, giving attackers remote control of victim machines.

### 5. Fortinet Confirms 86,000 Working Credentials Harvested in FortiBleed Campaign
- **Source:** SecurityWeek — https://www.securityweek.com/fortinet-responds-to-fortibleed-campaign/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `data-breach`, `vulnerability`
- **Slug:** `fortibleed-86000-confirmed-credentials`
- **Must-know:** yes
- **Summary:** Fortinet confirmed the FortiBleed credential-harvesting campaign produced a database of more than 86,000 confirmed working VPN credentials. This is a follow-up to the previously reported FortiBleed leak, now confirming the credentials are valid rather than merely exposed.

### 6. Canada's CSIS Used First-of-Its-Kind Warrant to Disinfect Botnet Devices
- **Source:** The Hacker News — https://thehackernews.com/2026/06/canadas-spy-agency-used-first-of-its.html
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `malware`
- **Slug:** `csis-botnet-cleanup-warrant`
- **Must-know:** no
- **Summary:** A newly public ruling shows Canada's CSIS used its threat reduction warrant powers for the first time to remotely clean botnet infections from servers, routers, and IoT devices on Canadian soil, neutralizing two foreign-run botnets.

### 7. More Cybersecurity Firms Disclose Impact From Klue Supply Chain Hack
- **Source:** SecurityWeek — https://www.securityweek.com/more-cybersecurity-firms-disclose-impact-from-klue-hack/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `data-breach`
- **Slug:** `klue-hack-more-firms-affected`
- **Must-know:** no
- **Summary:** HackerOne, Huntress, Jamf, OneTrust, Recorded Future, Snyk, and Tanium are among additional cybersecurity vendors now disclosing impact from the Klue Salesforce integration breach, showing the OAuth token abuse had a wider blast radius than initially known.

### 8. AryStinger Malware Infects 4,300 Legacy Routers to Build Reconnaissance Proxy Network
- **Source:** The Hacker News — https://thehackernews.com/2026/06/arystinger-malware-infects-4300-legacy.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `arystinger-router-malware`
- **Must-know:** no
- **Summary:** QiAnXin's XLab identified a new malware family, AryStinger, that has infected at least 4,300 legacy routers to build a reconnaissance and proxy network rather than a traditional DDoS botnet, supporting pre-breach attack stages.

### 9. Texas Parks & Wildlife Data Breach Affects 3 Million Individuals
- **Source:** SecurityWeek — https://www.securityweek.com/texas-parks-wildlife-data-breach-affects-3-million-individuals/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `texas-parks-wildlife-breach`
- **Must-know:** no
- **Summary:** A breach at a third-party license vendor serving the Texas Parks and Wildlife Department exposed personal information of approximately 3 million individuals. The vendor's systems, not TPWD's own infrastructure, were the entry point.

## Skippable

- **Stop Your Legacy Infrastructure from Hijacking Your AI Agents** — The Hacker News. Conference-recap opinion piece on AI agent security with no specific new technical finding.
- **Read this before you vibe-code another app** — The Verge AI. Feature/anecdote about one vibe-coded app's SQL injection flaw, not news of a new vulnerability class or incident.
- **Weekly Recap: Browser Bugs, EDR Killers, TV Botnet, OpenBSD Flaw, Android Trojan, and More** — The Hacker News. Roundup of previously covered stories, no standalone new item.
- **What the Latest ShinyHunters Breaches Reveal About Modern Cyberattacks** — SecurityWeek. Analysis/opinion piece on prior breaches, no new incident disclosed.
- **INTERPOL Warns Phishing, Ransomware, and AI Scams Are Rising Across Asia-Pacific** — The Hacker News. Regional advisory/report without new IOCs or technical guidance.
- **sqlite-utils 4.0rc1 adds migrations and nested transactions** — Simon Willison. Generic dev-tool release note, no security or AI-model relevance.
- **sqlite-utils 4.0rc1** — Simon Willison. Duplicate coverage of the same release as the item above.
- **Samsung Electronics brings ChatGPT and Codex to employees** — OpenAI Blog. Enterprise adoption announcement, no new model capability or security angle.
