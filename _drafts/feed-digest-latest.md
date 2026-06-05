# Digest — 2026-06-05 PM

- Window: last 14h
- Raw items considered: 36
- Relevant: 18
- Skippable: 18

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Cisco Catalyst SD-WAN Manager Zero-Day CVE-2026-20245 Actively Exploited, No Patch Available — `2026-06-05-cisco-sdwan-zero-day-cve-2026-20245-root-rce.md`
- [x] **[CRITICAL]** PAN-OS CVE-2026-0257 Under Active Exploitation: Unit 42 Threat Brief With IOCs — `2026-06-05-panos-cve-2026-0257-active-exploitation.md`
- [x] **[CRITICAL]** Hackers Actively Exploit Everest Forms Pro WordPress Plugin RCE CVE-2026-3300 (CVSS 9.8) — `2026-06-05-wordpress-everest-forms-rce-cve-2026-3300.md`
- [x] **[HIGH]** Chinese APT UNC5221 Deploys New Malware Families Plenet and AgentPSD Against Microsoft 365 — `2026-06-05-chinese-apt-unc5221-brickstorm-plenet-agentpsd.md`
- [x] **[HIGH]** New Chinese Espionage Cluster OP-512 Targets IIS Servers With Custom Web Shell Framework — `2026-06-05-op-512-iis-webshell-chinese-espionage.md`
- [x] **[HIGH]** Five Eyes Advisory: Chinese Intelligence Posing as LinkedIn Recruiters to Target Government and Military — `2026-06-05-five-eyes-chinese-linkedin-recruitment-espionage.md`
- [x] **[HIGH]** ShinyHunters Leaks 234 GB of DentaQuest Data, 2.6 Million Individuals Impacted — `2026-06-05-dentaquest-shinyhunters-breach-26m.md`
- [x] **[HIGH]** PCPJack Hijacks 230 AWS, Azure, and GCP Servers to Build Covert SMTP Relay Network — `2026-06-05-pcpjack-cloud-server-smtp-hijack.md`
- [x] **[HIGH]** Chrome 149 Patches 429 Vulnerabilities, Over 100 Rated Critical or High — `2026-06-05-chrome-149-429-vulnerabilities.md`
- [x] **[HIGH]** 900+ US Gas Station Tank Gauges Exposed Online and Vulnerable to Ongoing Attacks — `2026-06-05-atg-critical-infrastructure-exposed.md`
- [x] **[HIGH]** CISA Adds SolarWinds Serv-U CVE-2026-28318 to Known Exploited Vulnerabilities Catalog — `2026-06-05-cisa-kev-solarwinds-servu-cve-2026-28318.md`
- [x] **[HIGH]** ESET Discovers Android Spyware Asin Targeting Arabic Speakers via Fake News and War Map Apps — `2026-06-05-android-spyware-asin-arabic-users.md`
- [x] **[MEDIUM]** Researchers Warn Adaptive Agentic AI Worms Will Likely Strike Enterprise Networks Within a Year — `2026-06-05-agentic-ai-worms-enterprise-threat.md`
- [x] **[MEDIUM]** EU Unveils Tech Sovereignty Package: Chips Act 2.0, Cloud and AI Development Act — `2026-06-05-eu-tech-sovereignty-chips-act-cada.md`
- [x] **[MEDIUM]** White House AI Executive Order Establishes Voluntary Framework for Government Access to Frontier Models — `2026-06-05-trump-ai-eo-voluntary-frontier-model-testing.md`
- [x] **[MEDIUM]** FBI Warns: FIFA World Cup 2026 Fraud Wave With Banking Malware, Fake Domains, Credential Theft — `2026-06-05-fifa-world-cup-2026-scams-banking-malware.md`
- [x] **[INFORMATIONAL]** OWASP Incubator Releases CVE Lite CLI: Free Open-Source Dependency Vulnerability Scanner — `2026-06-05-owasp-cve-lite-cli-dependency-scanner.md`
- [x] **[INFORMATIONAL]** New York Legislature Passes First US Statewide One-Year Moratorium on New Data Centers — `2026-06-05-new-york-data-center-moratorium.md`

## Relevant (details)

### 1. Cisco Catalyst SD-WAN Manager Zero-Day CVE-2026-20245 Actively Exploited
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-cisco-sd-wan-flaw-exploited-in-zero-day-attacks-to-gain-root/
- **Severity:** critical
- **Tags:** `zero-day`, `privilege-escalation`, `rce`, `vulnerability`, `cve`
- **Summary:** Cisco disclosed CVE-2026-20245, an unpatched zero-day in Catalyst SD-WAN Manager actively exploited for root command execution — the seventh SD-WAN zero-day from Cisco in 2026. No patch is available; restrict management-plane access immediately.

### 2. PAN-OS CVE-2026-0257 Under Active Exploitation
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`, `rce`
- **Summary:** Unit 42 confirmed active exploitation of CVE-2026-0257 in PAN-OS and published IOCs and mitigations. Palo Alto firewalls are prime targets for nation-state actors; apply patches or workarounds immediately.

### 3. Everest Forms Pro WordPress Plugin RCE CVE-2026-3300
- **Source:** The Hacker News — https://thehackernews.com/2026/06/hackers-exploit-critical-everest-forms.html
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`, `cve`, `appsec`, `zero-day`
- **Summary:** CVE-2026-3300 (CVSS 9.8) in Everest Forms Pro is under active exploitation for full WordPress site compromise via RCE. Patch or deactivate the plugin immediately across all versions ≤ 1.9.12.

### 4. Chinese APT UNC5221 — Brickstorm/Plenet/AgentPSD
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/chinese-apt-deploys-new-malware-to-keep-access-to-hacked-networks/
- **Severity:** high
- **Tags:** `malware`, `apt`, `microsoft`, `iam`
- **Summary:** UNC5221 (China) is using Brickstorm plus two new malware families (Plenet, AgentPSD) to maintain persistent M365 access. Audit OAuth grants, conditional access policies, and service principal activity.

### 5. OP-512 Chinese Espionage Cluster — IIS Web Shell Framework
- **Source:** The Hacker News — https://thehackernews.com/2026/06/new-threat-cluster-op-512-targets.html
- **Severity:** high
- **Tags:** `malware`, `microsoft`, `vulnerability`, `apt`
- **Summary:** A newly discovered China-linked espionage group (OP-512) deploys a custom web shell framework against IIS servers for durable, stealthy persistence. Audit web-accessible directories and IIS module configs.

### 6. Five Eyes: Chinese Fake LinkedIn Recruiter Operation
- **Source:** SecurityWeek — https://www.securityweek.com/five-eyes-chinese-spies-target-government-military-staff-with-fake-job-opportunities/
- **Severity:** high
- **Tags:** `phishing`, `iam`, `apt`
- **Summary:** Five Eyes agencies warn that Chinese intelligence officers are impersonating LinkedIn recruiters to target government and military personnel. Personnel should report unsolicited recruitment outreach to their security officer.

### 7. DentaQuest Breach — ShinyHunters / 2.6M Records
- **Source:** SecurityWeek — https://www.securityweek.com/hackers-leak-dentaquest-information-impacting-2-6-million/
- **Severity:** high
- **Tags:** `data-breach`, `ransomware`
- **Summary:** ShinyHunters leaked 234 GB of DentaQuest data affecting 2.6 million individuals, likely including PHI. Affected customers should monitor for fraud and await breach notification with data-specific guidance.

### 8. PCPJack — 230 Cloud Servers Hijacked for SMTP Relay
- **Source:** The Hacker News — https://thehackernews.com/2026/06/pcpjack-hijacks-230-aws-google-cloud.html
- **Severity:** high
- **Tags:** `malware`, `cloud-security`, `aws`, `azure`, `gcp`
- **Summary:** PCPJack converted 230 compromised AWS/GCP/Azure servers into a covert SMTP relay network, syncing to downstream consumers every five minutes. Audit cloud SMTP egress and rotate credentials if anomalous activity is found.

### 9. Chrome 149 — 429 Vulnerabilities Patched
- **Source:** SecurityWeek — https://www.securityweek.com/chrome-149-patches-429-vulnerabilities/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`, `google`
- **Summary:** Chrome 149 patches 429 bugs with 100+ critical/high, primarily use-after-free and input validation issues. Verify managed deployments are rolling out version 149 immediately.

### 10. 900+ ATG Systems — Critical Infrastructure Exposed
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/over-900-us-gas-station-tank-gauge-systems-exposed-to-attacks/
- **Severity:** high
- **Tags:** `vulnerability`, `ot-security`, `ics`
- **Summary:** Over 900 US automatic tank gauge systems are directly internet-exposed and under active attack. Operators should isolate ATG systems from internet-facing networks and enforce VPN-only management access.

### 11. CISA KEV — SolarWinds Serv-U CVE-2026-28318
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/alerts/2026/06/05/cisa-adds-one-known-exploited-vulnerability-catalog
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `zero-day`
- **Summary:** CISA confirmed active exploitation of CVE-2026-28318 in SolarWinds Serv-U and added it to the KEV catalog. Federal agencies must patch by BOD 22-01 deadline; all others should patch immediately.

### 12. Android Spyware Asin — Arabic-Speaking Targets
- **Source:** The Hacker News — https://thehackernews.com/2026/06/android-spyware-asin-targets-arabic.html
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Summary:** ESET uncovered Asin, a multi-wave Android spyware campaign targeting Arabic speakers since early 2025 via fake news and government-themed apps with distinct per-wave infrastructure.

### 13. Agentic AI Worms — Emerging Enterprise Threat
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/adaptive-agentic-ai-worms-enterprise-cyber-threat
- **Severity:** medium
- **Tags:** `llm`, `malware`, `ai-safety`, `vulnerability`
- **Summary:** Researchers warn adaptive AI worms — malware that autonomously adapts, discovers vulnerabilities, and self-propagates — are likely to hit enterprises within a year. Begin evaluating agent sandboxing and AI workload segmentation now.

### 14. EU Tech Sovereignty — Chips Act 2.0 / CADA
- **Source:** The Record (Recorded Future) — https://therecord.media/eu-unveils-tech-sovereignty-package-cut-reliance-us-china
- **Severity:** medium
- **Tags:** `ai-safety`, `cloud-security`
- **Summary:** The EU unveiled Chips Act 2.0 and the Cloud and AI Development Act (CADA) to reduce reliance on US and Chinese cloud and semiconductor suppliers. Organizations serving EU customers should track CADA's compliance requirements.

### 15. Trump AI EO — Voluntary Frontier Model Testing
- **Source:** Dark Reading — https://www.darkreading.com/cybersecurity-operations/trump-ai-order-seeks-voluntary-frontier-model-testing
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`, `anthropic`, `openai`
- **Summary:** The White House EO creates a voluntary framework for AI labs to share frontier model evaluations with the government before public release. Industry reaction is mixed on sufficiency; mandatory requirements may follow.

### 16. FIFA World Cup 2026 Scam Wave
- **Source:** The Hacker News — https://thehackernews.com/2026/06/fifa-world-cup-2026-scams-are-already.html
- **Severity:** medium
- **Tags:** `phishing`, `malware`, `data-breach`
- **Summary:** The FBI warns of thousands of fake FIFA domains, banking malware in pirate streaming apps, and account-takeover phishing pages ahead of the June 11 kickoff. Use only official platforms and enable MFA.

### 17. OWASP CVE Lite CLI — Free Dependency Scanner
- **Source:** SecurityWeek — https://www.securityweek.com/owasp-incubator-project-helps-developers-find-and-fix-vulnerable-dependencies-in-seconds/
- **Severity:** informational
- **Tags:** `appsec`, `vulnerability`, `supply-chain`, `devsecops`
- **Summary:** OWASP Incubator released a free, open-source CLI tool for instant package-level CVE scanning of project dependencies — suitable for CI/CD integration with no license required.

### 18. New York Data Center Moratorium
- **Source:** The Verge AI — https://www.theverge.com/policy/944041/new-york-data-center-moratorium
- **Severity:** informational
- **Tags:** `cloud-security`
- **Summary:** New York's legislature passed the first US statewide one-year ban on new large data centers, pending the governor's signature. The policy constrains AI infrastructure expansion in New York during the review period.

## Skippable

- **Dark web Nemesis Market vendor gets 26 years** — BleepingComputer. Drug trafficking sentencing; no cybersecurity or AI angle.
- **The most interesting startups right now want to get you off your phone** — TechCrunch AI. Lifestyle/trend piece about "together tech" startups; no security or model-launch substance.
- **Building secure B2C applications with Cognito and Verified Permissions** — AWS Security Blog. Tutorial/marketing content from AWS; no news value.
- **Connecting Vulnerability Intelligence to Real-World Exposure With Flashpoint EASM** — Flashpoint. Vendor product announcement; marketing content.
- **The token bill comes due** — TechCrunch AI. Cost-management analysis piece; no specific news or security relevance.
- **The latest AI news we announced in May 2026** — Google AI Blog. Monthly recap with no specific newsworthy item surfaced in the summary.
- **What 2026 DBIR Confirms: Attacks Are Living in the Browser** — BleepingComputer. Keep Aware vendor-sponsored analysis of the Verizon DBIR; marketing content.
- **The 'together tech' wave might be the most intriguing startup bet of 2026** — TechCrunch AI. Duplicate of the anti-phone startup trend piece; same podcast content as item 3.
- **This AI startup says it can tell if a script will make a hit film** — The Verge AI. Entertainment AI tool; no security angle.
- **In Other News: Anthropic Maps AI Threats, Unpatched Comodo Flaw, Palantir Chief Eyed for CISA** — SecurityWeek. Aggregator roundup with insufficient technical depth on individual items.
- **AirTrunk commits $30B to build 5GW of AI data centers in India** — TechCrunch AI. Infrastructure investment; no security angle.
- **The Good, the Bad and the Ugly in Cybersecurity – Week 23** — SentinelOne Labs. Weekly roundup; PAN-OS exploitation covered better by Unit 42 item; other items lack detail.
- **Only 10% of SOCs Say They're Getting Excellent Value From AI** — The Hacker News. Vendor-sponsored survey promoting AI SOC platforms; marketing content.
- **Quoting Andreas Kling** — Simon Willison. Commentary on Ladybird browser halting public PRs over AI-code concerns; editorial with no practitioner news value.
- **Industry Reactions to New Trump AI Cybersecurity Executive Order** — SecurityWeek. Follow-up reactions piece; primary news captured in Trump AI EO item.
- **Nightclub Giant RCI Says Data Breach Affects 40,000 Individuals** — SecurityWeek. Generic breach disclosure; 40K affected is below the 100K threshold and lacks technical substance.
- **Cisco Warns of 7th SD-WAN Zero-Day Exploited in 2026** — SecurityWeek. Duplicate coverage of CVE-2026-20245; BleepingComputer selected as primary source.
- **Mira Murati steps back into the spotlight, carefully** — TechCrunch AI. Profile piece; no AI model launch or security news.
