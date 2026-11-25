# Digest — 2026-11-25 PM

- Window: last 14h
- Raw items considered: 44
- Relevant: 21
- Skippable: 23

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Attacker Exploits 10-Year-Old CVSS 10.0 Hex.pm Flaw to Compromise Package Registry Servers — `2026-11-25-hexpm-rce-cvss-10-package-registry-compromise.md`
- [x] **[CRITICAL]** Palo Alto Networks Patches Fragnesia Flaw Used by China-Linked Group to Root Firewalls — `2026-11-25-palo-alto-fragnesia-flaw-firewall-root-china.md`
- [x] **[CRITICAL]** Critical Drupal RCE Flaw Found by Anthropic Scanner Added to CISA KEV Amid Active Exploitation — `2026-11-25-drupal-fail2install-rce-anthropic-scanner-kev.md`
- [x] **[HIGH]** CISA Warns of Critical Unpatched Flaw in Danfoss Refrigeration Controllers — `2026-11-25-cisa-danfoss-refrigeration-controller-flaw.md`
- [x] **[HIGH]** Attackers Target .NET Developers With Poisoned Job Assessments via Malicious NuGet Packages — `2026-11-25-net-developers-poisoned-job-assessments-nuget.md`
- [x] **[HIGH]** Cyberattacks Hit Ports, Pipelines, and Manufacturing Across Latin America — `2026-11-25-latin-america-cyberattacks-ports-pipelines-manufacturing.md`
- [x] **[HIGH]** Suspected Ransomware Attack Disrupts Cancer Treatments and Surgeries at Guadeloupe Hospital — `2026-11-25-guadeloupe-hospital-ransomware-cancer-treatment-disruption.md`
- [x] **[HIGH]** Hackers Exploit Two GeoServer Flaws, Researchers Warn of Unauthenticated RCE Chains — `2026-11-25-geoserver-cve-2026-120705-cve-2026-129243-rce.md`
- [x] **[HIGH]** US Treasury's FinCEN Takes Systems Offline After Cyber Intrusion — `2026-11-25-fincen-treasury-systems-offline-cyber-intrusion.md`
- [x] **[HIGH]** Hackers Exploit Unpatched Flaw in Defunct Idunno AntiCsrf Library — `2026-11-25-idunno-anticsrf-library-cve-2026-131914.md`
- [x] **[HIGH]** Hackers Reportedly Breached CIA Intelligence Analysis System — `2026-11-25-cia-intelligence-analysis-system-breach.md`
- [x] **[HIGH]** Hackers Compromise 24 Check Point Management Servers in Suspected AI-Driven Campaign — `2026-11-25-check-point-servers-ai-driven-attack-campaign.md`
- [x] **[MEDIUM]** State AGs Fight Character.AI's Plan to Auction Off Users' Private Chats — `2026-11-25-state-ags-character-ai-chat-data-auction.md`
- [x] **[MEDIUM]** Eclypsium: Most Exploited Network Appliance Flaws Trace to Bundled Third-Party Code — `2026-11-25-eclypsium-infratrust-supply-chain-network-appliances.md`
- [x] **[MEDIUM]** ShinyHunters Claims Comeback as Okta Flags Possible Ties to New Inception Group — `2026-11-25-shinyhunters-comeback-inception-group-okta.md`
- [x] **[MEDIUM]** Com-Affiliated Hackers Hijack Cloud Accounts via Vishing for Data Theft and Extortion — `2026-11-25-com-affiliated-vishing-cloud-account-hijack.md`
- [x] **[MEDIUM]** WordPress Blocks Six Backdoored WP Connect Plugins Before Malicious Releases Go Live — `2026-11-25-wordpress-blocks-backdoored-wp-connect-plugins.md`
- [x] **[INFORMATIONAL]** Credential Remediation Lags as Teams Fear What Revoking Secrets Will Break — `2026-11-25-credential-remediation-secrets-sprawl-gitguardian.md`
- [x] **[INFORMATIONAL]** Cisco Talos Traces Tradecraft of an OpenAI-Linked Agentic Attack Swarm — `2026-11-25-cisco-talos-agentic-swarm-tradecraft.md`
- [x] **[INFORMATIONAL]** IBM Research Releases Indic Voice Agent Built on CUGA — `2026-11-25-ibm-research-indic-voice-agent-cuga.md`
- [x] **[INFORMATIONAL]** Kaspersky Details Risks From Preinstalled Android Malware in Device Firmware — `2026-11-25-kaspersky-preinstalled-android-firmware-malware.md`

## Relevant (details)

### 1. Attacker Exploits 10-Year-Old CVSS 10.0 Hex.pm Flaw to Compromise Package Registry Servers
- **Source:** The Hacker News — https://thehackernews.com/2026/11/hackers-exploited-cvss-100-hexpm-rce.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `rce`, `cve`, `vulnerability`
- **Slug:** `hexpm-rce-cvss-10-package-registry-compromise`
- **Must-know:** yes
- **Summary:** An attacker ran OS commands on six production servers of Hex.pm, the package registry Elixir and Erlang developers pull dependencies from, exploiting a flaw present in the registry's code since 2016. The maintaining team patched every server within about 15 minutes of the first malicious request.

### 2. Palo Alto Networks Patches Fragnesia Flaw Used by China-Linked Group to Root Firewalls
- **Source:** SecurityWeek — https://www.securityweek.com/palo-alto-networks-patches-fragnesia-flaw-used-to-root-firewalls/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `privilege-escalation`, `cve`, `vulnerability`
- **Slug:** `palo-alto-fragnesia-flaw-firewall-root-china`
- **Must-know:** yes
- **Summary:** A China-linked hacking group chained the PHP2Shell technique with the newly patched Fragnesia flaw in AI-assisted attacks that rooted 25 Palo Alto Networks firewalls. Palo Alto Networks has released a fix.

### 3. Critical Drupal RCE Flaw Found by Anthropic Scanner Added to CISA KEV Amid Active Exploitation
- **Source:** SecurityWeek — https://www.securityweek.com/drupal-flaw-found-by-anthropic-scanner-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`, `anthropic`
- **Slug:** `drupal-fail2install-rce-anthropic-scanner-kev`
- **Must-know:** yes
- **Summary:** A critical Drupal core remote code execution flaw, CVE-2026-132165 ("Fail2Install", CVSS 9.8) and originally surfaced by an Anthropic-built scanner, is under active exploitation. CISA added it to the Known Exploited Vulnerabilities catalog with a patch deadline of November 27, 2026.

### 4. CISA Warns of Critical Unpatched Flaw in Danfoss Refrigeration Controllers
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-warns-of-critical-unpatched-flaw-in-danfoss-refrigeration-controllers/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `ics`
- **Slug:** `cisa-danfoss-refrigeration-controller-flaw`
- **Must-know:** no
- **Summary:** CISA warned of a critical, currently unpatched vulnerability in Danfoss AK-SM 8xxA Series controllers, which food retailers use to manage commercial refrigeration, HVAC, and lighting systems. No fix is available yet.

### 5. Attackers Target .NET Developers With Poisoned Job Assessments via Malicious NuGet Packages
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/attackers-net-developers-poisoned-job-assessments
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `nuget`
- **Slug:** `net-developers-poisoned-job-assessments-nuget`
- **Must-know:** no
- **Summary:** Researchers found 13 malicious NuGet packages distributed as part of a fake recruitment campaign targeting .NET developers. The packages spread malware and give attackers access to developers' machines.

### 6. Cyberattacks Hit Ports, Pipelines, and Manufacturing Across Latin America
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/latin-america-cyberattacks-ports-pipelines-manufacturing
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ics`, `malware`
- **Slug:** `latin-america-cyberattacks-ports-pipelines-manufacturing`
- **Must-know:** no
- **Summary:** From the Port of Santos in Brazil to a pipeline in Argentina, cyberattacks are increasingly hitting industrial systems across Latin America. The trend spans multiple critical-infrastructure sectors in the region.

### 7. Suspected Ransomware Attack Disrupts Cancer Treatments and Surgeries at Guadeloupe Hospital
- **Source:** The Record (Recorded Future) — https://therecord.media/guadeloupe-ransomware-hospital-cyber
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`
- **Slug:** `guadeloupe-hospital-ransomware-cancer-treatment-disruption`
- **Must-know:** no
- **Summary:** A suspected ransomware attack impaired computer systems at the University Hospital of Guadeloupe, forcing doctors to postpone surgeries, suspend some cancer treatments, and revert to pen and paper. France's national cybersecurity agency is investigating.

### 8. Hackers Exploit Two GeoServer Flaws, Researchers Warn of Unauthenticated RCE Chains
- **Source:** The Hacker News — https://thehackernews.com/2026/11/hackers-exploit-two-geoserver-flaws-as.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `geoserver-cve-2026-120705-cve-2026-129243-rce`
- **Must-know:** no
- **Summary:** Threat actors are actively exploiting two newly patched GeoServer flaws, CVE-2026-120705 (CVSS 8.6, arbitrary file read) and CVE-2026-129243, according to watchTowr. The flaws can be chained with other bugs for unauthenticated remote code execution.

### 9. US Treasury's FinCEN Takes Systems Offline After Cyber Intrusion
- **Source:** The Hacker News — https://thehackernews.com/2026/11/us-treasurys-fincen-takes-some-systems.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `fincen-treasury-systems-offline-cyber-intrusion`
- **Must-know:** no
- **Summary:** The Treasury Department's Financial Crimes Enforcement Network (FinCEN) took some systems offline after a cybersecurity incident resulted in unauthorized access to a limited subset of its systems. FinCEN collects suspicious activity reports and other Bank Secrecy Act filings from banks and financial institutions.

### 10. Hackers Exploit Unpatched Flaw in Defunct Idunno AntiCsrf Library
- **Source:** SecurityWeek — https://www.securityweek.com/hackers-exploit-unpatched-flaw-in-defunct-idunno-anticsrf-library/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `cve`, `vulnerability`, `supply-chain`
- **Slug:** `idunno-anticsrf-library-cve-2026-131914`
- **Must-know:** no
- **Summary:** Attackers are exploiting CVE-2026-131914 in the defunct and unmaintained Idunno AntiCsrf library to achieve remote code execution via a single specially crafted web request. No patch is available since the library is no longer maintained.

### 11. Hackers Reportedly Breached CIA Intelligence Analysis System
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-reportedly-breached-cia-intelligence-analysis-system/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `cia-intelligence-analysis-system-breach`
- **Must-know:** no
- **Summary:** Unknown attackers reportedly breached an open-source intelligence analysis system used by the US Central Intelligence Agency. Details on scope and method were not confirmed in initial reporting.

### 12. Hackers Compromise 24 Check Point Management Servers in Suspected AI-Driven Campaign
- **Source:** The Hacker News — https://thehackernews.com/2026/11/hackers-compromise-24-check-point.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `malware`
- **Slug:** `check-point-servers-ai-driven-attack-campaign`
- **Must-know:** no
- **Summary:** An unknown threat actor used AI-driven offensive tooling, tracked by GreyNoise as GT13, to compromise 24 Check Point Security Management servers across 22 organizations worldwide. Targets span financial services, energy, and government sectors.

### 13. State AGs Fight Character.AI's Plan to Auction Off Users' Private Chats
- **Source:** TechCrunch AI — https://techcrunch.com/2026/11/25/state-ags-fight-character-ais-plan-to-auction-off-users-private-chats/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `privacy`, `ai-safety`
- **Slug:** `state-ags-character-ai-chat-data-auction`
- **Must-know:** no
- **Summary:** State attorneys general are opposing a proposed Character.ai bankruptcy sale that would include sensitive personal data from more than 21 million US accounts, including 2.1 million registered to minors. No breach has occurred; the dispute is over whether the data can be sold as a bankruptcy asset.

### 14. Eclypsium: Most Exploited Network Appliance Flaws Trace to Bundled Third-Party Code
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/infratrust-warns-of-exploited-supply-chain-flaws-in-network-appliances/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `supply-chain`, `vulnerability`
- **Slug:** `eclypsium-infratrust-supply-chain-network-appliances`
- **Must-know:** no
- **Summary:** Eclypsium's November InfraTrust report found that most infrastructure security advisories addressing exploited vulnerabilities over the past month involve flaws in third-party software bundled into network appliances, rather than code the vendors wrote themselves. The finding underscores ongoing supply chain risk in network hardware.

### 15. ShinyHunters Claims Comeback as Okta Flags Possible Ties to New Inception Group
- **Source:** SecurityWeek — https://www.securityweek.com/shinyhunters-claims-comeback-new-inception-group-rejects-alleged-ties/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`, `malware`
- **Slug:** `shinyhunters-comeback-inception-group-okta`
- **Must-know:** no
- **Summary:** An account tied to the ShinyHunters extortion group announced its return, as Okta researchers spot possible links between the group and a newer "Inception" group, which rejects the alleged ties. No new victim data has been confirmed yet.

### 16. Com-Affiliated Hackers Hijack Cloud Accounts via Vishing for Data Theft and Extortion
- **Source:** The Hacker News — https://thehackernews.com/2026/11/com-affiliated-hackers-hijack-cloud.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `cloud-security`
- **Slug:** `com-affiliated-vishing-cloud-account-hijack`
- **Must-know:** no
- **Summary:** Unit 42 is tracking numerous waves of vishing attacks by Com-affiliated threat actors since August 2026 that led to cloud account hijacking, data theft, and extortion. Targets include financial services, healthcare, legal, and construction firms in the US, UK, and Australia.

### 17. WordPress Blocks Six Backdoored WP Connect Plugins Before Malicious Releases Go Live
- **Source:** The Hacker News — https://thehackernews.com/2026/11/wordpress-blocks-six-backdoored-wp.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `supply-chain`
- **Slug:** `wordpress-blocks-backdoored-wp-connect-plugins`
- **Must-know:** no
- **Summary:** WordPress removed six WP Connect plugins after they were backdoored on November 22, 2026, following a suspected compromise of the developer's account, which would have enabled arbitrary code execution on sites running them. The WordPress plugins team proactively detected and blocked the malicious releases before they went live.

### 18. Credential Remediation Lags as Teams Fear What Revoking Secrets Will Break
- **Source:** The Hacker News — https://thehackernews.com/2026/11/credential-remediation-is-slow-when-you.html
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `appsec`, `devsecops`
- **Slug:** `credential-remediation-secrets-sprawl-gitguardian`
- **Must-know:** no
- **Summary:** GitGuardian's State of Secrets Sprawl 2026 report found more than 64% of valid secrets discovered in 2022 still worked as of January 2026, because teams stall on what revoking them will break. The report also found validity-only triage misses 46% of critical secrets, arguing for impact-based prioritization instead.

### 19. Cisco Talos Traces Tradecraft of an OpenAI-Linked Agentic Attack Swarm
- **Source:** Cisco Talos — https://blog.talosintelligence.com/the-great-escape-tradecraft-insights-from-an-agentic-swarm/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `llm`, `openai`, `malware`
- **Slug:** `cisco-talos-agentic-swarm-tradecraft`
- **Must-know:** no
- **Summary:** Cisco Talos analyzed the tradecraft behind OpenAI-linked agentic swarm activity from 2026, which is fully traceable through public records, and compared it to early signals from current agentic attack activity seen in the wild. The post is a technical look at how AI-driven offensive tooling behaves operationally.

### 20. IBM Research Releases Indic Voice Agent Built on CUGA
- **Source:** Hugging Face Blog — https://huggingface.co/blog/ibm-research/an-indic-voice-agent-with-cuga
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `llm`
- **Slug:** `ibm-research-indic-voice-agent-cuga`
- **Must-know:** no
- **Summary:** IBM Research published a Hugging Face blog post introducing a voice agent for Indic languages built on CUGA. No further technical detail was available in the source summary.

### 21. Kaspersky Details Risks From Preinstalled Android Malware in Device Firmware
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/tr/how-to-protect-against-preinstalled-android-malware/122093/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `malware`
- **Slug:** `kaspersky-preinstalled-android-firmware-malware`
- **Must-know:** no
- **Summary:** Kaspersky GReAT examined trojans embedded in Android device firmware, sharing statistics on preinstalled malware and the risks it poses to corporate users. The post discusses countermeasures including Kaspersky Next.

## Skippable

- **Florida ransomware recovery CEO indicted for allegedly paying hacker ransoms** — The Record. Legal/indictment story about a recovery firm executive, no new technical substance or IOCs.
- **Australia passes tough legislation requiring big tech to preempt foreseeable harms** — The Record. Broad online-harms policy, not AI- or cyber-specific.
- **Nothing offers a full look at its AI earbuds and charging case** — The Verge AI. Consumer gadget preview, no security angle.
- **AI data centers are becoming harder to build, and neoclouds are feeling it** — TechCrunch AI. Business/financing story, no security substance.
- **Two Newly Disclosed GeoServer Vulnerabilities Under Attack** — SecurityWeek. Duplicate; fuller CVE/CVSS detail captured via The Hacker News item.
- **It's a Bot World. We're Just Living in It** — Dark Reading. Opinion piece without news value.
- **More Pentests Without More Pentesters: Where AI Safely Helps** — BleepingComputer. Vendor-sponsored AI-pentest-assist content, no new technical substance.
- **The AI Threat Horizon: Why Speed, Edge AI and Baselines Are Our Best Defense** — Unit 42. Generic strategic thought-leadership post, no specific incident or technical detail.
- **Cyber Insurers See New Divide: AI Defense 'Haves' & 'Have Nots'** — Dark Reading. Podcast/opinion episode, no news substance.
- **Amazon is reportedly in talks to end Muse AI shopping block** — The Verge AI. Business deal story, no security angle; duplicate of the TechCrunch item below.
- **Amazon and Meta reportedly in talks to lift blockade on AI agent Muse** — TechCrunch AI. Business deal story, no security angle.
- **US Treasury's FinCEN Disconnects Systems Following Cyber Incident** — SecurityWeek. Duplicate; fuller detail captured via The Hacker News item.
- **Ground Truth: CISO Matt Martin on Building a Real Security Program Without an Enterprise Budget** — SecurityWeek. Career/profile piece, no news value.
- **The questions Jensen Huang and Nvidia will still have to answer about Megaspeed** — TechCrunch AI. Investigative business/legal story, not a security or AI-launch item.
- **Has vibe coding made open source the new normal for synths?** — The Verge AI. AI dev-culture piece, no security relevance.
- **Drupal Fail2Install Exploit Details Emerge as Critical RCE Flaw Faces Active Exploitation** — The Hacker News. Duplicate; CVE/CVSS detail folded into the SecurityWeek item covering the same KEV-listed flaw.
- **Microsoft fixes Microsoft 365 bug blocking access to Office apps** — BleepingComputer. Generic product bug fix, no security relevance.
- **Securing Grandma's groceries with Pierre Cadieux** — Cisco Talos. Personal profile piece, no news value.
- **Ex-OpenAI Employee Accused of Bugging Company Offices Granted $1 Million Bail** — The Hacker News. Procedural bail-hearing update on an already-reported arrest, no new technical substance.
- **Plagiarism Checker Turnitin Investigating Cyberattack** — SecurityWeek. Generic breach disclosure, no technical detail or victim count.
- **Treasury's FinCEN takes systems offline after cybersecurity incident** — The Record. Duplicate; fuller detail captured via The Hacker News item.
- **Hackers now exploit critical Drupal RCE flaw to hijack sites** — BleepingComputer. Duplicate; folded into the SecurityWeek item covering the same KEV-listed flaw.
- **Microsoft confirms authentication issues after November updates** — BleepingComputer. Patch side-effect bug report, no new vulnerability or exploitation detail.
