# Digest — 2026-11-09 PM

- Window: last 14h
- Raw items considered: 41
- Relevant: 17
- Skippable: 24

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Hackers Exploit SSHole OpenSSH Flaw to Breach Linux Systems — `2026-11-09-sshole-openssh-flaw-actively-exploited.md`
- [x] **[INFORMATIONAL]** AWS Adds IAM Outbound Identity Federation for Cross-Partition Access — `2026-11-09-aws-iam-outbound-identity-federation.md`
- [x] **[MEDIUM]** Bitter APT Deploys New PapRAT Backdoor Against South Asian Targets — `2026-11-09-bitter-apt-paprat-backdoor-south-asia.md`
- [x] **[HIGH]** AI-Assisted Attack Breaches German Web Host Through Assistant Interface — `2026-11-09-ai-aided-cyberattack-breaches-german-web-host.md`
- [x] **[MEDIUM]** Revolve Data Breach Affects 1.5 Million Customers — `2026-11-09-revolve-data-breach-1-5-million.md`
- [x] **[HIGH]** Iris Plaza Breach May Have Exposed Data of 7.7 Million Customers — `2026-11-09-iris-plaza-breach-7-7-million.md`
- [x] **[HIGH]** Amplifon Americas Data Breach Impacts 1.3 Million, Exposes SSNs and Health Data — `2026-11-09-amplifon-americas-data-breach-1-3-million.md`
- [x] **[HIGH]** Frontline Education Data Breach Affects Over 3 Million Students and Staff — `2026-11-09-frontline-education-data-breach-3-million.md`
- [x] **[MEDIUM]** Pro-Russian Hackers Leak Personal Data of European Officials, Offer Crypto Rewards for More — `2026-11-09-pro-russian-hackers-leak-european-officials-data.md`
- [x] **[HIGH]** Plex2Shell Flaw Chain Exploited Against QNAP NAS Users — `2026-11-09-plex2shell-exploited-qnap-nas.md`
- [x] **[HIGH]** Default 'admin:admin' Password Let Researchers Hack Two Automakers' Connected Cars — `2026-11-09-default-admin-password-automaker-account-takeover.md`
- [x] **[MEDIUM]** Web3Auth Flaw Exploited to Steal Keplr Crypto Wallets — `2026-11-09-web3auth-flaw-keplr-wallet-theft.md`
- [x] **[CRITICAL]** LNbits Urges Operators to Shut Down Bitcoin Lightning Servers Amid Active Attacks — `2026-11-09-lnbits-urges-shutdown-active-exploitation.md`
- [x] **[HIGH]** Hacker Used BOSSAI AI Agents to Steal Taipei Emergency Dispatch Records — `2026-11-09-bossai-ai-agent-taipei-dispatch-breach.md`
- [x] **[INFORMATIONAL]** Google DeepMind's AI Agents Cut Cost of Attacking 1024-Bit RSA Keys — `2026-11-09-deepmind-ai-agents-rsa-1024-attack-cost.md`
- [x] **[MEDIUM]** US Agencies Warn of Attacks on Industrial Refrigeration Controllers — `2026-11-09-refrigeration-controller-attacks-warning.md`
- [x] **[HIGH]** CISA Adds SonicWall SonicOS MFA Bypass Flaw to KEV Catalog Amid Exploitation Reports — `2026-11-09-sonicwall-sonicos-mfa-bypass-kev.md`

## Relevant (details)

### 1. Hackers Exploit SSHole OpenSSH Flaw to Breach Linux Systems
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-exploit-sshole-openssh-flaw-to-breach-linux-systems/ (also SecurityWeek — https://www.securityweek.com/hackers-exploiting-sshole-authentication-bypass-in-openssh/)
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `rce`
- **Slug:** `sshole-openssh-flaw-actively-exploited`
- **Must-know:** no
- **Summary:** Attackers are actively exploiting the "SSHole" authentication bypass vulnerability (CVE-2026-123158) in OpenSSH to execute commands, steal credentials, and establish persistent access on Linux systems. Initial exploitation attempts are attributed to botnets and crypto miners, with other threat actors expected to follow.

### 2. AWS Adds IAM Outbound Identity Federation for Cross-Partition Access
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/simplify-cross-partition-access-with-aws-iam-outbound-identity-federation/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `aws`, `cloud-security`, `iam`
- **Slug:** `aws-iam-outbound-identity-federation`
- **Must-know:** no
- **Summary:** AWS now lets workloads use IAM outbound federation tokens to assume roles across AWS partitions (Commercial, China, GovCloud US, European Sovereign Cloud). This simplifies cross-partition access for workloads that previously needed separate credential management per partition.

### 3. Bitter APT Deploys New PapRAT Backdoor Against South Asian Targets
- **Source:** The Hacker News — https://thehackernews.com/2026/11/bitter-hackers-deploy-new-paprat.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `rce`
- **Slug:** `bitter-apt-paprat-backdoor-south-asia`
- **Must-know:** no
- **Summary:** The South Asian cyber espionage group Bitter (aka APT-C-08, Hazy Tiger, TA397) is using a previously unreported remote access trojan called PapRAT against South Asian organizations. Fortinet FortiGuard Labs says PapRAT has both C++ and Rust implementations with command execution and file capabilities.

### 4. AI-Assisted Attack Breaches German Web Host Through Assistant Interface
- **Source:** The Record (Recorded Future) — https://therecord.media/cyberattack-germany-ai-mittwald
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `data-breach`
- **Slug:** `ai-aided-cyberattack-breaches-german-web-host`
- **Must-know:** no
- **Summary:** Hackers allegedly used AI assistance to breach German web hosting company Mittwald through a tool designed to let customers connect AI assistants to their accounts. The company disclosed the incident, marking a notable real-world case of an AI-assistant integration being used as an attack vector.

### 5. Revolve Data Breach Affects 1.5 Million Customers
- **Source:** SecurityWeek — https://www.securityweek.com/revolve-puts-data-breach-victim-count-at-1-5-million/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `revolve-data-breach-1-5-million`
- **Must-know:** no
- **Summary:** Online fashion retailer Revolve told regulators that a September cyberattack affected more than 1.5 million individuals. No further detail on the data types exposed has been disclosed.

### 6. Iris Plaza Breach May Have Exposed Data of 7.7 Million Customers
- **Source:** SecurityWeek — https://www.securityweek.com/iris-plaza-breach-may-have-exposed-data-of-7-7-million-customers/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `cloud-security`
- **Slug:** `iris-plaza-breach-7-7-million`
- **Must-know:** no
- **Summary:** Hackers compromised an external cloud service used by shopping platform Iris Plaza and may have stolen personal information belonging to up to 7.7 million customers. The breach originated through a third-party cloud service rather than Iris Plaza's own infrastructure.

### 7. Amplifon Americas Data Breach Impacts 1.3 Million, Exposes SSNs and Health Data
- **Source:** SecurityWeek — https://www.securityweek.com/amplifon-americas-data-breach-impacts-1-3-million/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `amplifon-americas-data-breach-1-3-million`
- **Must-know:** no
- **Summary:** Hearing aid retailer Amplifon Americas disclosed that hackers stole personal, health, and insurance information — including Social Security numbers — from its internal systems, affecting 1.3 million people. The sensitivity of the exposed data (SSNs, health records) elevates this beyond a typical breach disclosure.

### 8. Frontline Education Data Breach Affects Over 3 Million Students and Staff
- **Source:** SecurityWeek — https://www.securityweek.com/3-million-people-hit-by-frontline-education-data-breach/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `frontline-education-data-breach-3-million`
- **Must-know:** no
- **Summary:** Frontline Education told Indiana regulators that an August data breach affected over 3 million school district staff and students. This is one of the largest education-sector breach disclosures reported this week.

### 9. Pro-Russian Hackers Leak Personal Data of European Officials, Offer Crypto Rewards for More
- **Source:** The Record (Recorded Future) — https://therecord.media/hackers-russia-italy-noname (also SecurityWeek — https://www.securityweek.com/italys-meloni-blames-pro-russian-hackers-for-leak-of-foreign-ministers-data-on-the-dark-web/)
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `pro-russian-hackers-leak-european-officials-data`
- **Must-know:** no
- **Summary:** Pro-Russian hackers published the personal information of Italian Foreign Minister Antonio Tajani and other senior European officials on the dark web, and are offering cryptocurrency rewards for additional personal details about them and their families. Italian PM Giorgio Meloni's office confirmed the leak involving Tajani.

### 10. Plex2Shell Flaw Chain Exploited Against QNAP NAS Users
- **Source:** SecurityWeek — https://www.securityweek.com/plex2shell-exploited-against-qnap-nas-users/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `rce`
- **Slug:** `plex2shell-exploited-qnap-nas`
- **Must-know:** no
- **Summary:** Threat actors are exploiting a four-flaw vulnerability chain, dubbed Plex2Shell, to compromise Plex Media Server installations running on QNAP NAS devices. QNAP NAS owners running Plex should prioritize patching.

### 11. Default 'admin:admin' Password Let Researchers Hack Two Automakers' Connected Cars
- **Source:** The Hacker News — https://thehackernews.com/2026/11/default-adminadmin-server-password.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`
- **Slug:** `default-admin-password-automaker-account-takeover`
- **Must-know:** no
- **Summary:** Researchers found that the login systems behind two car brands' mobile apps, both backed by the ForgeRock identity platform (now part of Ping Identity), could be fully taken over due to a default 'admin:admin' server password. The access allowed researchers to reach any customer's account and, for connected-car owners, remotely unlock doors and start the engine.

### 12. Web3Auth Flaw Exploited to Steal Keplr Crypto Wallets
- **Source:** The Hacker News — https://thehackernews.com/2026/11/web3auth-flaw-exploited-to-steal-keplr.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`
- **Slug:** `web3auth-flaw-keplr-wallet-theft`
- **Must-know:** no
- **Summary:** An attacker exploited a security flaw in Web3Auth, which powers Google and Apple sign-in for the Keplr crypto wallet, to steal funds from users who set up Keplr via those sign-in options. Web3Auth said it used the attacker's own access route to empty other at-risk wallets before further theft could occur.

### 13. LNbits Urges Operators to Shut Down Bitcoin Lightning Servers Amid Active Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/11/lnbits-urges-all-operators-to-shut-down.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `zero-day`
- **Slug:** `lnbits-urges-shutdown-active-exploitation`
- **Must-know:** yes
- **Summary:** The LNbits project is urging all operators of its open-source Bitcoin Lightning wallet system to shut down their servers immediately due to a wave of active attacks, ahead of releasing several unreleased security fixes. One operator reported losing about 0.023 BTC (2,285,545 satoshis) to an attacker before taking the server offline.

### 14. Hacker Used BOSSAI AI Agents to Steal Taipei Emergency Dispatch Records
- **Source:** The Hacker News — https://thehackernews.com/2026/11/taiwan-based-hacker-used-bossai-ai.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `data-breach`
- **Slug:** `bossai-ai-agent-taipei-dispatch-breach`
- **Must-know:** no
- **Summary:** Researchers at Acronis's Threat Research Unit say a single Taiwan-based attacker used BOSSAI AI agents to pull emergency dispatch records covering seven Taipei districts. The same agents also found an exposed Taipei fire department platform leaking patient data from 2018, including ECG readings and ambulance video footage, with no login required.

### 15. Google DeepMind's AI Agents Cut Cost of Attacking 1024-Bit RSA Keys
- **Source:** SecurityWeek — https://www.securityweek.com/google-deepminds-ai-agents-make-1024-bit-rsa-keys-cheaper-to-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ai-safety`, `vulnerability`
- **Slug:** `deepmind-ai-agents-rsa-1024-attack-cost`
- **Must-know:** no
- **Summary:** Working with cryptographers, Google DeepMind's AI agents reduced the cost of forging RSA-1024 signatures and found a cheaper method for factoring RSA-1024 keys. The finding is a research result rather than an active attack, but is relevant for anyone still relying on 1024-bit RSA.

### 16. US Agencies Warn of Attacks on Industrial Refrigeration Controllers
- **Source:** The Hacker News — https://thehackernews.com/2026/11/us-agencies-warn-refrigeration.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`
- **Slug:** `refrigeration-controller-attacks-warning`
- **Must-know:** no
- **Summary:** U.S. government agencies warned that threat actors are actively targeting industrial refrigeration and cold-chain monitoring systems globally, aiming to cause service disruptions, fire hazards, and inventory loss. The actors are exploiting vulnerabilities or weaknesses in unpatched or internet-exposed controllers to remotely alter settings.

### 17. CISA Adds SonicWall SonicOS MFA Bypass Flaw to KEV Catalog Amid Exploitation Reports
- **Source:** The Hacker News — https://thehackernews.com/2026/11/cisa-flags-sonicwall-sonicos-mfa-bypass.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`
- **Slug:** `sonicwall-sonicos-mfa-bypass-kev`
- **Must-know:** no
- **Summary:** CISA added a high-severity SonicWall SonicOS vulnerability (CVE-2026-19868, CVSS 7.1–7.5) to its Known Exploited Vulnerabilities catalog following reports that it may have been exploited in real-world attacks. The flaw is described as an authentication bypass affecting MFA enforcement.

## Skippable

- **Anthropic joins AI's natural gas frenzy, buys $3.4B worth of turbines** — TechCrunch AI. Business/infrastructure deal, no security or model-release substance.
- **Binance denies data breach after alleged ShinyHunters claims** — BleepingComputer. Unconfirmed claim that the company denies; no verified breach.
- **Medium's new TK app brings AI assistance directly into the writing process** — TechCrunch AI. Product launch, no security angle.
- **Cloud CISO Perspectives: Our security forecast for 2027** — Google Cloud Security. Newsletter/opinion roundup, not news.
- **Trump's 60 Minutes interview touched on AI safety, threat to arrest an AI exec** — The Verge AI. Political commentary without new technical or regulatory substance.
- **NIST: Solo Shouldn't Mean Less Secure** — Dark Reading. Generic guidance for solo business owners, no new CVE or incident.
- **Disney and Adobe are building generative AI tools together** — The Verge AI. Product partnership announcement, no security angle.
- **Hold up — I had a great time talking to the RIAA guy** — The Verge AI. Podcast/opinion piece, no news value.
- **Ukraine arrests four in $5 million crypto scam targeting Germans** — The Record. Regional law enforcement action, no technical substance.
- **Nemotron-Personas-Finance-Japan: A Synthetic Dataset** — Hugging Face Blog. Niche synthetic dataset release, not a notable model launch.
- **The Biggest Threat to Your GRC Job Isn't AI. It's Ignoring AI.** — BleepingComputer. Opinion/career piece, no news value.
- **FBI agent stole $2.5 million in crypto from hackers under investigation** — BleepingComputer. Individual corruption case, no technical substance.
- **Jonathan Kanter is using AI to take on Big Tech** — The Verge AI. Policy/antitrust commentary, no security angle.
- **Automattic debuts a platform to deploy vibe-coding apps amid a changing internet** — TechCrunch AI. Product launch/marketing, no security substance.
- **US bans MEXC crypto exchange over sanctions evasion, cybercrime links** — BleepingComputer. Treasury sanctions action, no technical security substance.
- **⚡ Weekly Recap: SSHole Exploited, APT Root RCE, Robot Takeovers, 15K Hacked Sites, and More** — The Hacker News. Aggregator roundup duplicating stories already covered individually.
- **Your Experts Have Partners. There's HOPE for Keeping Them Together** — Hugging Face Blog. Niche research blog post, not a notable model launch.
- **Italy's Meloni Blames Pro-Russian Hackers for Leak of Foreign Minister's Data on the Dark Web** — SecurityWeek. Duplicate coverage of the European officials leak (see Relevant #9); less detail than The Record.
- **Ukraine dismantles crypto scam network that stole €4.3 million** — BleepingComputer. Regional law enforcement action, no technical substance.
- **Hackers Exploiting 'SSHole' Authentication Bypass in OpenSSH** — SecurityWeek. Duplicate coverage of SSHole (see Relevant #1); merged into the BleepingComputer item.
- **Former OpenAI Engineer Pleads Not Guilty to Planting Covert Device in Executive Meeting Room** — The Hacker News. Legal proceeding update, no technical substance.
- **Is Jensen Huang's job on the line? Yale's Jeffrey Sonnenfeld estimates it's "about a 50-50"** — TechCrunch AI. Speculative business/leadership commentary, no security or model-release substance.
- **The Web Is More Than Enough, by Paul Ford** — Simon Willison. Personal blog post/opinion, no news value.
- **Hide your slop PR descriptions behind `<details><summary>`** — Simon Willison. Opinion piece on AI coding workflow, no news value.
