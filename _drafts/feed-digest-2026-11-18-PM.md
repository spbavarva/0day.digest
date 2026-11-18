# Digest — 2026-11-18 PM

- Window: last 14h
- Raw items considered: 44
- Relevant: 14
- Skippable: 30

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Attackers Compromise Microsoft's Agent Framework PyPI Package to Steal Cloud Credentials — `2026-11-18-microsoft-agent-framework-pypi-credential-stealer.md`
- [x] **[CRITICAL]** Attackers Used Optimizely Flaw to A/B Test Malware on Top Websites — `2026-11-18-optimizely-malware-ab-test-top-websites.md`
- [x] **[CRITICAL]** CISA Confirms Active Exploitation of Critical Perforce Puppet RCE Flaw — `2026-11-18-perforce-puppet-rce-cve-2026-115731-kev.md`
- [x] **[CRITICAL]** Apache Warns of Roller RCE Vulnerability Exploited in Attacks — `2026-11-18-apache-roller-rce-exploited.md`
- [x] **[HIGH]** Java4Shell Flaw (CVE-2026-114938) Enables Pre-Auth RCE in Jira, Jenkins, Keycloak — `2026-11-18-java4shell-cve-2026-114938-preauth-rce.md`
- [x] **[HIGH]** New Attack Bypasses TPM Lockout to Crack Windows Hello and BitLocker PINs — `2026-11-18-tpm-lockout-bypass-windows-hello-bitlocker.md`
- [x] **[HIGH]** Major Brazilian Digital Signature Apps Found Vulnerable to RCE and Fraud — `2026-11-18-brazilian-signature-apps-rce-fraud.md`
- [x] **[HIGH]** Russian Cold Relic Hackers Use Stolen Google Workspace Data to Breach Second US Organization — `2026-11-18-cold-relic-coldriver-stolen-cloud-data-breach.md`
- [x] **[HIGH]** Russian APT Star Blizzard Poses as Employee of Hacked Firm to Breach US Organization — `2026-11-18-star-blizzard-impersonation-breach-us-org.md`
- [x] **[MEDIUM]** New EggStreme Malware Variant Goes Silent to Evade Detection in Government Attacks — `2026-11-18-eggstreme-malware-variant-government-attacks.md`
- [x] **[MEDIUM]** Researchers Detail Novel XSS Technique: innerHTML Injection Without Equals Signs — `2026-11-18-xss-innerhtml-without-equals-bypass.md`
- [x] **[MEDIUM]** UAT-12643: North Korea-Aligned Actor Uses Blockchain Dead Drops for Infostealer C2 — `2026-11-18-uat-12643-blockchain-dead-drops-infostealer.md`
- [x] **[MEDIUM]** AuditTeam's OpsAgent Framework Disguises Ransomware Extortion as a "Forced Audit" — `2026-11-18-auditteam-opsagent-forced-audit-ransomware.md`
- [x] **[INFORMATIONAL]** Microsoft Takes Perception Agentic Security Platform Out of Preview — `2026-11-18-microsoft-perception-agentic-security-ga.md`

## Relevant (details)

### 1. Attackers Compromise Microsoft's Agent Framework PyPI Package to Steal Cloud Credentials
- **Source:** The Hacker News — https://thehackernews.com/2026/11/attackers-compromise-microsofts-agent.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `pypi`, `microsoft`, `malware`
- **Slug:** `microsoft-agent-framework-pypi-credential-stealer`
- **Must-know:** yes
- **Summary:** Threat actors pushed two malicious versions of Microsoft's agent-framework package on PyPI that steal Azure, Azure DevOps, and GitHub Actions credentials on every Python start. Multiple security vendors independently flagged the compromise within hours of publication.

### 2. Attackers Used Optimizely Flaw to A/B Test Malware on Top Websites
- **Source:** Krebs on Security — https://krebsonsecurity.com/2026/11/attackers-used-optimizely-to-a-b-test-malware-on-top-websites/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`
- **Slug:** `optimizely-malware-ab-test-top-websites`
- **Must-know:** yes
- **Summary:** A vulnerability in the Optimizely website personalization platform let attackers silently inject data-stealing malware into at least 178 top sites, including the BBC, CNN, Equifax, Ledger, and Zoom, over a 24-hour window. The incident highlights weak controls over third-party scripts on major websites.

### 3. CISA Confirms Active Exploitation of Critical Perforce Puppet RCE Flaw
- **Source:** The Hacker News — https://thehackernews.com/2026/11/hackers-exploiting-critical-puppet-rce.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `perforce-puppet-rce-cve-2026-115731-kev`
- **Must-know:** no
- **Summary:** CISA added CVE-2026-115731 (CVSS 9.4), a critical Perforce Puppet flaw, to its Known Exploited Vulnerabilities catalog after confirming active exploitation. The bug lets any client holding a CA-signed agent certificate execute code on the Puppet server.

### 4. Apache Warns of Roller RCE Vulnerability Exploited in Attacks
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/apache-warns-of-roller-rce-vulnerability-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `apache-roller-rce-exploited`
- **Must-know:** no
- **Summary:** Apache released security updates for a critical remote code execution flaw in Roller, its open-source blogging and content server software, that is already being exploited in attacks. Administrators running Roller should patch immediately.

### 5. Java4Shell Flaw (CVE-2026-114938) Enables Pre-Auth RCE in Jira, Jenkins, Keycloak
- **Source:** The Hacker News — https://thehackernews.com/2026/11/java4shell-cve-2026-114938-enables-pre.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `java4shell-cve-2026-114938-preauth-rce`
- **Must-know:** no
- **Summary:** Security firm Calif disclosed Java4Shell (CVE-2026-114938, CVSS 8.1), an out-of-bounds write flaw affecting Jira, Jenkins, Keycloak, and other Java 17.0.6+ applications that can enable pre-auth remote code execution. CISA urged organizations to patch immediately given how widely the affected software is used.

### 6. New Attack Bypasses TPM Lockout to Crack Windows Hello and BitLocker PINs
- **Source:** The Hacker News — https://thehackernews.com/2026/11/flash-chip-attack-bypasses-tpm-lockout.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `microsoft`, `hardware-security`
- **Slug:** `tpm-lockout-bypass-windows-hello-bitlocker`
- **Must-know:** no
- **Summary:** Researchers at Technische Universität Berlin found that opening the case of certain AMD and Intel PCs allows resetting the TPM lockout protecting Windows Hello and BitLocker PINs, turning a years-long brute-force problem into one that takes days. The attack requires physical access to the device.

### 7. Major Brazilian Digital Signature Apps Found Vulnerable to RCE and Fraud
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/major-brazilian-signature-app-rce-fraud
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`
- **Slug:** `brazilian-signature-apps-rce-fraud`
- **Must-know:** no
- **Summary:** Government-sanctioned digital signature middleware used for legally binding documents in Brazil was found to contain remote code execution vulnerabilities. Exploitation could enable both system compromise and fraudulent document signing.

### 8. Russian Cold Relic Hackers Use Stolen Google Workspace Data to Breach Second US Organization
- **Source:** The Hacker News — https://thehackernews.com/2026/11/russian-cold-relic-hackers-use-stolen.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `cloud-security`, `google`
- **Slug:** `cold-relic-coldriver-stolen-cloud-data-breach`
- **Must-know:** no
- **Summary:** Google's Mandiant and Threat Intelligence Group say the Russia-linked group Cold Relic (formerly COLDRIVER/UNC4057) turned a single cloud account compromise into a chain of further intrusions by weaponizing stolen Google Workspace data to impersonate trusted contacts. The campaign breached a second US-based organization beyond the original target.

### 9. Russian APT Star Blizzard Poses as Employee of Hacked Firm to Breach US Organization
- **Source:** SecurityWeek — https://www.securityweek.com/russian-apt-poses-as-employee-of-hacked-firm-to-breach-another-us-organization/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `data-breach`
- **Slug:** `star-blizzard-impersonation-breach-us-org`
- **Must-know:** no
- **Summary:** The Russian state-linked group Star Blizzard weaponized data and identities stolen from a firm it compromised in late 2025 to phish and breach a separate US organization. Posing as an employee of the already-breached company added credibility to the phishing attempts.

### 10. New EggStreme Malware Variant Goes Silent to Evade Detection in Government Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/11/eggstreme-hackers-rebuild-malware-with.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `eggstreme-malware-variant-government-attacks`
- **Must-know:** no
- **Summary:** A suspected Chinese APT group rebuilt its EggStreme malware toolkit after exposure, continuing to target government organizations in the Philippines. Bitdefender notes that rotating file hashes, domains, and builds is cheap for the attackers, so the campaign is likely to persist.

### 11. Researchers Detail Novel XSS Technique: innerHTML Injection Without Equals Signs
- **Source:** PortSwigger Research — https://portswigger.net/research/achieving-the-impossible-xss-in-innerhtml-without-equals
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `xss`, `appsec`
- **Slug:** `xss-innerhtml-without-equals-bypass`
- **Must-know:** no
- **Summary:** Guest researcher Masato Kinugawa, writing on PortSwigger Research, demonstrated a way to trigger innerHTML-based script injection without using an equals sign — a construct many sanitizers and detection rules assume is required. Teams with custom XSS filters or CSP mitigations should check whether their rules depend on that assumption.

### 12. UAT-12643: North Korea-Aligned Actor Uses Blockchain Dead Drops for Infostealer C2
- **Source:** Cisco Talos — https://blog.talosintelligence.com/uat-12643-suspected-north-korea-aligned-actor-blends-blockchain-resilience-with-targeted-infostealing/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `uat-12643-blockchain-dead-drops-infostealer`
- **Must-know:** no
- **Summary:** Cisco Talos identified infrastructure tied to a financially motivated, suspected North Korea-aligned group (UAT-12643) that hosts command-and-control data on public blockchain networks instead of centralized servers or domains. The approach reflects a broader shift toward "bulletproof" C2 that resists conventional takedowns.

### 13. AuditTeam's OpsAgent Framework Disguises Ransomware Extortion as a "Forced Audit"
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/auditteam-opsagent-forced-audit/122031/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `ransomware`, `malware`
- **Slug:** `auditteam-opsagent-forced-audit-ransomware`
- **Must-know:** no
- **Summary:** Kaspersky's GReAT team detailed a ransomware operation, AuditTeam, that frames its double-extortion demands as a "forced audit" consulting fee rather than a traditional ransom note. The group's implant, OpsAgent, has been rewritten in Rust.

### 14. Microsoft Takes Perception Agentic Security Platform Out of Preview
- **Source:** SecurityWeek — https://www.securityweek.com/microsoft-takes-perception-agentic-security-platform-out-of-preview/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `microsoft`, `devsecops`, `llm`
- **Slug:** `microsoft-perception-agentic-security-ga`
- **Must-know:** no
- **Summary:** Microsoft moved four blue-team agents and a Recon Agent in its Perception agentic security platform to general availability, with integrations and vulnerability shielding still in preview. It's part of a broader vendor push to deploy AI agents for defensive, not just offensive or assistive, security tasks.

## Skippable

- **Quoting Daniel Stenberg** — Simon Willison. Opinion/quote post about curl's Rust rewrite project, no news value.
- **Remember the frontier AI pause? Chip companies don't either** — The Verge AI. Nvidia/AMD earnings-call analysis; the AI-safety angle is background recap, not new reporting.
- **VeroSecurity Raises $11 Million for AI Security Engineering Platform** — SecurityWeek. Funding announcement, no technical substance.
- **Russian cyber-espionage group used stolen cloud data to hack into organizations, Google says** — The Record. Duplicate coverage of the Cold Relic/COLDRIVER story; The Hacker News version carries more detail (see item 8).
- **Time-Series Models in the Streamhouse** — Hugging Face Blog. Data-engineering blog post, no security or major model-launch angle.
- **From Deepfakes to Helpdesk Impersonation: Why Stronger Verification Matters** — BleepingComputer. Vendor-sponsored (Specops) generic guidance, no specific incident or new technique.
- **British hacker gets 6 year sentence for $11.6M crypto theft scheme** — The Record. Duplicate sentencing coverage of the Scattered Spider case (see items 16, 39); no new technical detail.
- **The PSF end-of-year fundraiser** — Simon Willison. Non-profit fundraising post, no security/AI news value.
- **Will Wright's next game uses AI to map your memories** — The Verge AI. Gaming feature, no security angle.
- **Ice hockey governing body website defaced amid dispute over Russia's exclusion** — The Record. Simple defacement, no technical detail, limited impact.
- **Cyberattack hits Norwegian energy giant Equinor, disrupting internal services** — The Record. Victim disclosure with no TTPs or IOCs provided.
- **Last of Five Defendants Sentenced in US Scattered Spider Hacking Case** — SecurityWeek. Duplicate sentencing coverage of the same case (see items 7, 39).
- **Nvidia isn't selling any more AI chips to China** — The Verge AI. Export/business policy news, not a security story.
- **Nvidia clarifies when it will — and won't — keep financing neoclouds** — TechCrunch AI. Business financing news, not security-relevant.
- **AI Pentesting Checklist for Web Apps: 15 Questions to Ask Before Choosing a Vendor** — The Hacker News. Vendor marketing checklist, no specific incident or finding.
- **CISO Conversations: Patti Degnan** — SecurityWeek. Interview/profile piece, no news value.
- **Felicis leads $7.5M bet on Unsiloed AI** — TechCrunch AI. Funding round for a non-security document-processing startup.
- **Dizigom illegal streaming service with 21M monthly visits shuts down** — BleepingComputer. Piracy shutdown, no security angle.
- **Chrome 158 Patches 204 Vulnerabilities** — SecurityWeek. Routine browser patch release; no single critical/exploited CVE called out.
- **India's Humyn Labs raises $47M to feed U.S. robotics companies the data they need** — TechCrunch AI. Funding round, non-security.
- **Suno now lets you make AI videos for your AI music** — The Verge AI. Minor product feature, no security or major capability relevance.
- **Microsoft Agent Framework Releases Poisoned With Credential Stealer** — SecurityWeek. Duplicate coverage of the PyPI supply-chain compromise; The Hacker News version carries more detail (see item 1).
- **Quality Isn't The Main Worry About AI Pentesting** — The Hacker News. Vendor-sponsored marketing content, no specific incident or finding.
- **The challenge of defending against bulletproof dead drops on public blockchains** — Cisco Talos. General-technique companion piece; folded into the UAT-12643 item (see item 12).
- **Critical Perforce Puppet RCE Exploited in Attacks** — SecurityWeek. Duplicate coverage of the Puppet RCE/KEV story; The Hacker News version has the CISA KEV confirmation (see item 3).
- **Microsoft announces Windows Server 2028 with hardened security** — BleepingComputer. Product announcement with no specific technical security detail in the available summary.
- **Oracle Patches 950 Vulnerabilities With November 2026 CSPU** — SecurityWeek. Routine quarterly CPU release; no single actively-exploited critical CVE called out.
- **CISA Urges Immediate Patching of Java4Shell Flaw** — The Hacker News. Duplicate coverage of the Java4Shell story (see item 5).
- **British Scattered Spider hacker sentenced to 6 years in prison** — BleepingComputer. Duplicate sentencing coverage of the same case (see items 7, 16).
- **Java4Shell Vulnerability Puts Enterprise Applications at Risk of Takeover** — SecurityWeek. Duplicate coverage of the Java4Shell story (see item 5).
