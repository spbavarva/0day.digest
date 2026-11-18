# Digest — 2026-11-18 PM

- Window: last 14h
- Raw items considered: 72
- Relevant: 23
- Skippable: 49

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[INFORMATIONAL]** Ukraine, FBI Arrest Ransomware Gang Members Tied to $40M in Ransoms — `2026-11-18-ukraine-fbi-arrest-ransomware-gang-40m.md`
- [x] **[INFORMATIONAL]** AWS Details Detection for Cross-Cloud Lateral Movement via Federated Identity — `2026-11-18-aws-security-hub-cross-cloud-lateral-movement.md`
- [x] **[HIGH]** Russian APT Uses Stolen Cloud Data to Chain Breaches via Impersonation — `2026-11-18-cold-relic-russian-apt-cloud-breach-chaining.md`
- [x] **[INFORMATIONAL]** Google DeepMind Introduces Gemini 4 Neon — `2026-11-18-google-deepmind-gemini-4-neon.md`
- [x] **[INFORMATIONAL]** Google DeepMind Makes Genie 4 Available — `2026-11-18-google-deepmind-genie-4-available.md`
- [x] **[MEDIUM]** Coinbase Blocks $4.7M in Transfers to Elon Musk Deepfake Scam — `2026-11-18-coinbase-blocks-elon-musk-deepfake-scam.md`
- [x] **[INFORMATIONAL]** Research Details How Iranian Cyber Groups Hand Off Network Access for Destructive Attacks — `2026-11-18-attackiq-iranian-cyber-groups-network-access-handoff.md`
- [x] **[CRITICAL]** Decade-Old NGINX HTTP/2 Flaw Lets Unauthenticated Attackers Execute Code — `2026-11-18-nginx-http2-nginx2root-rce-cve-2026-123007.md`
- [x] **[CRITICAL]** F5 Warns of Six Critical BIG-IP Flaws That Can Crash Traffic, May Allow RCE — `2026-11-18-f5-big-ip-six-critical-flaws.md`
- [x] **[CRITICAL]** Critical Apache Roller RCE Flaw Under Active Exploitation — `2026-11-18-apache-roller-rce-cve-2026-129448-active-exploitation.md`
- [x] **[CRITICAL]** Microsoft's Agent Framework PyPI Package Compromised to Steal Credentials — `2026-11-18-microsoft-agent-framework-pypi-credential-stealer.md`
- [x] **[CRITICAL]** Java4Shell Flaw Enables Pre-Auth RCE in Jira, Jenkins, Keycloak and More — `2026-11-18-java4shell-cve-2026-114938-pre-auth-rce.md`
- [x] **[MEDIUM]** PortSwigger Research: XSS in innerHTML Without Using the Equals Sign — `2026-11-18-xss-in-innerhtml-without-equals.md`
- [x] **[HIGH]** New EggStreme Malware Variant Goes Silent to Evade Security Tools — `2026-11-18-eggstreme-malware-variant-evades-detection-philippines.md`
- [x] **[HIGH]** Major Brazilian Digital Signature Apps Enable RCE and Fraud — `2026-11-18-brazilian-signature-apps-rce-fraud.md`
- [x] **[MEDIUM]** Russian APT Star Blizzard Poses as Employee of Hacked Firm to Breach Another US Organization — `2026-11-18-star-blizzard-poses-as-employee-to-breach-us-org.md`
- [x] **[HIGH]** New Attack Bypasses TPM Lockout to Crack Windows Hello and BitLocker PINs — `2026-11-18-tpm-lockout-bypass-windows-hello-bitlocker-pins.md`
- [x] **[INFORMATIONAL]** Microsoft Takes Perception Agentic Security Platform Out of Preview — `2026-11-18-microsoft-perception-agentic-security-platform-ga.md`
- [x] **[HIGH]** CISA Adds Four Known Exploited Vulnerabilities to Catalog — `2026-11-18-cisa-kev-catalog-adds-four-vulnerabilities.md`
- [x] **[INFORMATIONAL]** The Challenge of Defending Against Bulletproof Dead Drops on Public Blockchains — `2026-11-18-defending-against-blockchain-dead-drops-c2.md`
- [x] **[MEDIUM]** UAT-12643: North Korea-Aligned Actor Blends Blockchain Resilience with Targeted Infostealing — `2026-11-18-uat-12643-north-korea-blockchain-infostealing.md`
- [x] **[CRITICAL]** Critical Perforce Puppet RCE Exploited in Attacks — `2026-11-18-perforce-puppet-rce-cve-2026-115731-exploited.md`
- [x] **[INFORMATIONAL]** Microsoft Announces Windows Server 2028 With Hardened Security — `2026-11-18-windows-server-2028-hardened-security-announced.md`

## Relevant (details)

### 1. Ukraine, FBI Arrest Ransomware Gang Members Tied to $40M in Ransoms
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/ukraine-fbi-arrest-ransomware-gang-members-tied-to-40m-in-ransoms/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ransomware`
- **Slug:** `ukraine-fbi-arrest-ransomware-gang-40m`
- **Must-know:** no
- **Summary:** Ukrainian authorities and the FBI arrested four suspected members of a ransomware operation tied to $40.5M+ in ransom payments from 28+ companies. Law enforcement disruption, not a new technical disclosure.

### 2. AWS Details Detection for Cross-Cloud Lateral Movement via Federated Identity
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/detecting-cross-cloud-lateral-movement-with-aws-security-hub/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `cloud-security`, `aws`, `privilege-escalation`
- **Slug:** `aws-security-hub-cross-cloud-lateral-movement`
- **Must-know:** no
- **Summary:** AWS published practitioner guidance on detecting attackers who pivot across cloud providers through federated identity trust, using AWS Security Hub to correlate scattered signals. Relevant to multicloud/federated-identity shops.

### 3. Russian APT Uses Stolen Cloud Data to Chain Breaches via Impersonation
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/cold-relic-turns-one-cloud-breach-into-another ; The Record — https://therecord.media/russia-cyber-espionage-google
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `data-breach`
- **Slug:** `cold-relic-russian-apt-cloud-breach-chaining`
- **Must-know:** no
- **Summary:** A Russia-linked group ("Cold Relic") uses data stolen from one victim's cloud accounts to impersonate trusted contacts and breach a second set of targets, per research cited by Google. Chaining stolen data this way raises the bar for defenders since messages come from genuinely compromised accounts.

### 4. Google DeepMind Introduces Gemini 4 Neon
- **Source:** Google DeepMind — https://deepmind.google/blog/introducing-gemini-4-neon/
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `google`
- **Slug:** `google-deepmind-gemini-4-neon`
- **Must-know:** no
- **Summary:** Google DeepMind announced a new Gemini 4 variant, "Gemini 4 Neon." The feed carried no capability/benchmark detail beyond the announcement.

### 5. Google DeepMind Makes Genie 4 Available
- **Source:** Google DeepMind — https://deepmind.google/blog/genie-4-is-now-available/
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `google`
- **Slug:** `google-deepmind-genie-4-available`
- **Must-know:** no
- **Summary:** Google DeepMind announced general availability of Genie 4, its world-model system. No further capability detail was in the feed.

### 6. Coinbase Blocks $4.7M in Transfers to Elon Musk Deepfake Scam
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/coinbase-blocks-47-million-in-transfers-to-elon-musk-deepfake-scam/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `deepfake`
- **Slug:** `coinbase-blocks-elon-musk-deepfake-scam`
- **Must-know:** no
- **Summary:** Coinbase blocked $4.7M in crypto transfers tied to a fake-giveaway scam using an AI-generated deepfake of Elon Musk during a Tesla livestream watched by 500k+ viewers. Another case of AI video used for financial fraud at scale.

### 7. Research Details How Iranian Cyber Groups Hand Off Network Access for Destructive Attacks
- **Source:** Dark Reading (AttackIQ research) — https://www.darkreading.com/threat-intelligence/attackiq-research-reveals-iranian-cyber-groups
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `threat-intel`
- **Slug:** `attackiq-iranian-cyber-groups-network-access-handoff`
- **Must-know:** no
- **Summary:** AttackIQ analysis of 20 Iranian state-sponsored groups describes espionage, ransomware, and hacktivist operations intersecting, including groups handing off initial access to units that carry out destructive attacks.

### 8. Decade-Old NGINX HTTP/2 Flaw Lets Unauthenticated Attackers Execute Code
- **Source:** The Hacker News — https://thehackernews.com/2026/11/10-year-old-nginx-http2-flaw-lets.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `nginx-http2-nginx2root-rce-cve-2026-123007`
- **Must-know:** no
- **Summary:** "nginx2root" (CVE-2026-123007) has existed in NGINX's HTTP/2 support since version 1.9.5 (2015) and lets unauthenticated attackers execute code on servers with HTTP/2 enabled. F5 shipped fixes in 1.31.9 and 1.30.7; no active exploitation confirmed yet, but NGINX's footprint makes this a high-value patch.

### 9. F5 Warns of Six Critical BIG-IP Flaws That Can Crash Traffic, May Allow RCE
- **Source:** The Hacker News — https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`
- **Slug:** `f5-big-ip-six-critical-flaws`
- **Must-know:** no
- **Summary:** F5 disclosed six critical BIG-IP flaws letting an unauthenticated attacker crash the Traffic Management Microkernel; some may allow RCE. Each needs a specific config (particular iRule command or APM policy with two specific agent types) to trigger.

### 10. Critical Apache Roller RCE Flaw Under Active Exploitation
- **Source:** The Hacker News — https://thehackernews.com/2026/11/critical-apache-roller-rce-flaw-under.html ; BleepingComputer — https://www.bleepingcomputer.com/news/security/apache-warns-of-roller-rce-vulnerability-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `apache-roller-rce-cve-2026-129448-active-exploitation`
- **Must-know:** yes
- **Summary:** CVE-2026-129448 (CVSS 9.8), an unauthenticated deserialization bug in Apache Roller's XML-RPC endpoint, is under active exploitation per the ASF. Allows RCE without authentication; fixed versions are out — patch or take instances offline now.

### 11. Microsoft's Agent Framework PyPI Package Compromised to Steal Credentials
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/microsofts-agent-framework-pypi-package-compromised-to-steal-credentials/ ; SecurityWeek — https://www.securityweek.com/microsoft-agent-framework-releases-poisoned-with-credential-stealer/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `pypi`, `malware`, `microsoft`
- **Slug:** `microsoft-agent-framework-pypi-credential-stealer`
- **Must-know:** yes
- **Summary:** Microsoft's official "agent-framework" PyPI package was compromised; malicious versions 1.26.1 and 1.26.2 steal Azure, Azure DevOps, and GitHub Actions credentials on Python startup. Supply chain compromise of a widely used Microsoft package — rotate credentials if you installed those versions.

### 12. Java4Shell Flaw Enables Pre-Auth RCE in Jira, Jenkins, Keycloak and More
- **Source:** The Hacker News — https://thehackernews.com/2026/11/java4shell-cve-2026-114938-enables-pre.html ; Dark Reading — https://www.darkreading.com/vulnerabilities-threats/java4shell-flaw-threatens-global-java-application-ecosystem
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `java4shell-cve-2026-114938-pre-auth-rce`
- **Must-know:** no
- **Summary:** "Java4Shell" (CVE-2026-114938), a memory corruption bug in the OpenJDK runtime affecting Java 17.0.6+, lets unauthenticated attackers execute code on Jira, Jenkins, Keycloak and more. Only triggers on x86-64 chips with AVX-512 VBMI; reportedly found via AI-assisted analysis. No confirmed active exploitation yet.

### 13. PortSwigger Research: XSS in innerHTML Without Using the Equals Sign
- **Source:** PortSwigger Research — https://portswigger.net/research/achieving-the-impossible-xss-in-innerhtml-without-equals
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `xss`, `appsec`
- **Slug:** `xss-in-innerhtml-without-equals`
- **Must-know:** no
- **Summary:** Guest researcher Masato Kinugawa demonstrates achieving XSS via innerHTML assignment without using the equals sign, defeating a case previously assumed safe. Relevant to anyone building sanitizers/filters around innerHTML assignment.

### 14. New EggStreme Malware Variant Goes Silent to Evade Security Tools
- **Source:** The Hacker News (Bitdefender report) — https://thehackernews.com/2026/11/eggstreme-hackers-rebuild-malware-with.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `threat-intel`
- **Slug:** `eggstreme-malware-variant-evades-detection-philippines`
- **Must-know:** no
- **Summary:** A suspected Chinese APT rebuilt its EggStreme toolkit to go silent when it detects security tooling, continuing to target Philippine government organizations. Bitdefender notes the group prefers cheap retooling (new hash/domain) over abandoning infrastructure once exposed.

### 15. Major Brazilian Digital Signature Apps Enable RCE and Fraud
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/major-brazilian-signature-app-rce-fraud
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`
- **Slug:** `brazilian-signature-apps-rce-fraud`
- **Must-know:** no
- **Summary:** Government-sanctioned authentication middleware behind legally binding digital signatures in Brazil reportedly carries RCE bugs, creating both a technical and a document-fraud risk. No CVE ID or vendor name given in the feed.

### 16. Russian APT Star Blizzard Poses as Employee of Hacked Firm to Breach Another US Organization
- **Source:** SecurityWeek — https://www.securityweek.com/russian-apt-poses-as-employee-of-hacked-firm-to-breach-another-us-organization/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`
- **Slug:** `star-blizzard-poses-as-employee-to-breach-us-org`
- **Must-know:** no
- **Summary:** Star Blizzard weaponized data and identities stolen from a late-2025 victim to phish and compromise a separate US organization by posing as the earlier victim's employee — the same stolen-identity chaining pattern seen elsewhere this cycle.

### 17. New Attack Bypasses TPM Lockout to Crack Windows Hello and BitLocker PINs
- **Source:** The Hacker News — https://thehackernews.com/2026/11/flash-chip-attack-bypasses-tpm-lockout.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`
- **Slug:** `tpm-lockout-bypass-windows-hello-bitlocker-pins`
- **Must-know:** no
- **Summary:** TU Berlin researchers found that on AMD and some Intel PCs, opening the case lets an attacker reset the TPM lockout protecting Windows Hello/BitLocker PINs, cracking a 4-digit PIN or 6-digit BitLocker PIN in days instead of years. Requires physical access.

### 18. Microsoft Takes Perception Agentic Security Platform Out of Preview
- **Source:** SecurityWeek — https://www.securityweek.com/microsoft-takes-perception-agentic-security-platform-out-of-preview/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `microsoft`, `ai-launch`, `cloud-security`
- **Slug:** `microsoft-perception-agentic-security-platform-ga`
- **Must-know:** no
- **Summary:** Microsoft's "Perception" agentic security platform is now GA with four blue-team agents and a Recon Agent; integrations and vulnerability shielding remain in preview. Part of the broader push to embed AI agents directly in SOC workflows.

### 19. CISA Adds Four Known Exploited Vulnerabilities to Catalog
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/alerts/2026/11/18/cisa-adds-four-known-exploited-vulnerabilities-catalog
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `cve`, `vulnerability`
- **Slug:** `cisa-kev-catalog-adds-four-vulnerabilities`
- **Must-know:** no
- **Summary:** CISA added four actively-exploited CVEs to its KEV catalog: Synology DSM output-encoding flaw, BerriAI LiteLLM unprotected alternate channel, Apache Axis unsafe reflection, and Vanderbilt REDCap code injection. Federal agencies must remediate on CISA's timeline.

### 20. The Challenge of Defending Against Bulletproof Dead Drops on Public Blockchains
- **Source:** Cisco Talos — https://blog.talosintelligence.com/the-challenge-of-defending-against-bulletproof-dead-drops-on-public-blockchains/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `malware`, `threat-intel`
- **Slug:** `defending-against-blockchain-dead-drops-c2`
- **Must-know:** no
- **Summary:** Cisco Talos explains how malware C2 infrastructure is shifting from fragile centralized servers/domains to decentralized public-blockchain storage, which can't be taken down once written, making conventional domain/IP-based disruption much harder.

### 21. UAT-12643: North Korea-Aligned Actor Blends Blockchain Resilience with Targeted Infostealing
- **Source:** Cisco Talos — https://blog.talosintelligence.com/uat-12643-suspected-north-korea-aligned-actor-blends-blockchain-resilience-with-targeted-infostealing/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `malware`, `threat-intel`
- **Slug:** `uat-12643-north-korea-blockchain-infostealing`
- **Must-know:** no
- **Summary:** Cisco Talos identified malicious infrastructure tied to a financially motivated group, UAT-12643, suspected to be North Korea-aligned, combining blockchain-based infrastructure resilience with targeted infostealer campaigns.

### 22. Critical Perforce Puppet RCE Exploited in Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/critical-perforce-puppet-rce-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `perforce-puppet-rce-cve-2026-115731-exploited`
- **Must-know:** yes
- **Summary:** CVE-2026-115731 lets any client holding a CA-signed agent certificate execute code on a Puppet server, and it's being exploited in attacks. Serious given Puppet's broad configuration-management access across managed fleets — patch immediately.

### 23. Microsoft Announces Windows Server 2028 With Hardened Security
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-announces-windows-server-2028-with-hardened-security/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `microsoft`
- **Slug:** `windows-server-2028-hardened-security-announced`
- **Must-know:** no
- **Summary:** Microsoft announced Windows Server 2028 at Ignite 2026, with hardened security as a stated theme. No specific technical feature detail was in the feed.

## Skippable

- **Satya Nadella predicts AI agents will reshuffle the economics of the web** — TechCrunch AI. Opinion/analysis, no security angle.
- **Anthropic reportedly prices IPO at $83 a share, above projected range** — TechCrunch AI. Business/financial news, no security or model substance.
- **Nvidia created a weird bit of intrigue by not filing a routine SEC report** — TechCrunch AI. Business news.
- **Palmer Luckey warns AI-powered cyberattacks are outpacing defenses** — TechCrunch AI. Opinion/commentary quote, no new technical detail.
- **Palmer Luckey thinks China is 'thrilled to have Jensen out'** — TechCrunch AI. Business/personnel opinion.
- **Strike Graph Launches Integration AI to Automate Continuous Compliance Evidence** — Dark Reading. Marketing/product launch.
- **Judge signs off on sale of Spirit Airlines' data to Google** — The Record. Legal/business news, no breach or vuln.
- **Sam Altman says his life is so weird that he's unfazed by Andrew Garfield portraying him** — TechCrunch AI. Celebrity/culture, no news value.
- **Trump administration officials size-up a bad stretch for tech** — The Record. Policy remarks, no new technical detail.
- **Snapchat now lets developers build AR Lenses with AI assistants like Claude Code and Cursor** — TechCrunch AI. Product feature, no security angle.
- **DaisyRose-27B: Pushing the Frontier of Post-Training Efficiency** — Hugging Face Blog. Niche community model post, no summary, thin.
- **Trump's latest land grab is an AI hub in the Philippines** — The Verge AI. Politics/travel color piece.
- **Data breach impacts 40 Irish credit unions in reported IT provider hack** — BleepingComputer. Breach disclosure without TTPs/IOCs.
- **AWS Lambda now supports GPU instances for Event Functions** — AWS News Blog. Generic product launch, no security angle.
- **Nvidia's rise, visualized** — The Verge AI. Business data-viz piece.
- **Tech lawsuits defined 2026 — and lawmakers want more** — The Verge AI. Policy roundup/opinion.
- **Lawmakers call on White House to develop defensive AI cyber systems** — The Record. Advocacy ask, no concrete regulatory action yet.
- **Why your fine-tuning job takes longer than the FLOPs say** — Hugging Face Blog. Educational/tutorial, no news value.
- **What is Nvidia without AI's sugar daddy in charge?** — The Verge AI. Opinion piece.
- **Google's AI feature in Search gets its own incognito mode** — TechCrunch AI. Product feature, no security angle.
- **Disney's new Star Wars animatronics interact with guests using AI** — The Verge AI. Entertainment/lifestyle tech feature.
- **More banks say customers using AI agents are on their own — even if they get hacked** — TechCrunch AI. Policy/liability commentary, no new incident detail.
- **The Gemini app is now available on lower-memory Android devices** — Google AI Blog. Generic product feature.
- **Sam Altman warns against a future where AI, not humans, calls the shots** — TechCrunch AI. Opinion/policy commentary.
- **NSA continues response to interruptions in classified internal network** — The Record. Thin on technical detail; unclear if attack-related.
- **OpenAI CEO Sam Altman says it's 'hard to imagine the AI industry without Jensen'** — TechCrunch AI. Personnel/opinion.
- **Quoting Daniel Stenberg** — Simon Willison. Commentary/opinion blurb on curl Rust rewrites.
- **Remember the frontier AI pause? Chip companies don't either** — The Verge AI. Opinion/analysis recapping known events.
- **VeroSecurity Raises $11 Million for AI Security Engineering Platform** — SecurityWeek. Funding announcement, marketing.
- **Russian cyber-espionage group used stolen cloud data to hack into organizations, Google says** — The Record. Duplicate coverage, merged into "Russian APT Uses Stolen Cloud Data to Chain Breaches" above.
- **Time-Series Models in the Streamhouse: A New Frontier and Use Cases** — Hugging Face Blog (IBM Research). Niche technical tutorial, no news value.
- **From Deepfakes to Helpdesk Impersonation: Why Stronger Verification Matters** — BleepingComputer (Specops Software). Vendor marketing content.
- **The PSF end-of-year fundraiser** — Simon Willison. No security/AI news content.
- **Will Wright's next game uses AI to map your memories** — The Verge AI. Entertainment/gaming feature.
- **Last of Five Defendants Sentenced in US Scattered Spider Hacking Case** — SecurityWeek. Routine sentencing update, no new technical detail.
- **Nvidia isn't selling any more AI chips to China** — The Verge AI. Business/export policy news.
- **Nvidia clarifies when it will — and won't — keep financing neoclouds** — TechCrunch AI. Business/financing news.
- **AI Pentesting Checklist for Web Apps: 15 Questions to Ask Before Choosing a Vendor** — The Hacker News. Sponsored listicle/marketing content.
- **CISO Conversations: Patti Degnan – Part of the Job Is Deciding What Not to Do** — SecurityWeek. Interview/feature content, no news value.
- **Felicis leads $7.5M bet on Unsiloed AI** — TechCrunch AI. Funding/startup news.
- **Java4Shell Flaw (CVE-2026-114938) Enables Pre-Auth RCE** (Hacker News duplicate entry) — merged into "Java4Shell Flaw Enables Pre-Auth RCE" above.
- **Dizigom illegal streaming service with 21M monthly visits shuts down** — BleepingComputer. Piracy/IP enforcement, not a security vuln.
- **Chrome 158 Patches 204 Vulnerabilities** — SecurityWeek. Routine patch release, no single critical+exploited CVE called out.
- **India's Humyn Labs raises $47M to feed US robotics companies training data** — TechCrunch AI. Funding/business news.
- **Suno now lets you make AI videos for your AI music** — The Verge AI. Product feature, no security angle.
- **Microsoft Agent Framework Releases Poisoned With Credential Stealer** (SecurityWeek duplicate entry) — merged into "Microsoft's Agent Framework PyPI Package Compromised" above.
- **Quality Isn't The Main Worry About AI Pentesting — Data Privacy and Production Safety Are** — The Hacker News. Sponsored/vendor content.
- **Apache warns of Roller RCE vulnerability exploited in attacks** (BleepingComputer duplicate entry) — merged into "Critical Apache Roller RCE Flaw Under Active Exploitation" above.
- **The Silent Consensus** — OpenAI Blog. Policy/philosophy essay, no concrete news.
