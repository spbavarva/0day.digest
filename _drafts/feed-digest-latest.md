# Digest — 2026-07-13 PM

- Window: last 14h
- Raw items considered: 44
- Relevant: 17
- Skippable: 27

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[MEDIUM]** CrashStealer macOS Malware Uses Notarized Dropper to Bypass Gatekeeper — `2026-07-13-crashstealer-macos-malware-notarized-dropper.md`
- [x] **[HIGH]** Google and Microsoft Pull ModHeader Extension Over Hidden Data Collector — `2026-07-13-modheader-extension-pulled-hidden-collector.md`
- [x] **[HIGH]** GigaWiper: Modular Implant Combines Backdoor and Wiper Capabilities — `2026-07-13-gigawiper-modular-destructive-implant.md`
- [x] **[INFORMATIONAL]** Google Open-Sources k8s-aibom for Automated AI Bills of Materials on GKE — `2026-07-13-google-k8s-aibom-ai-bill-of-materials.md`
- [x] **[HIGH]** Lessons Learned From CISA's Contractor GitHub Credential Leak — `2026-07-13-cisa-github-leak-lessons-learned.md`
- [x] **[HIGH]** MemGhost Attack Plants Persistent False Memories in AI Agents via a Single Email — `2026-07-13-memghost-ai-agent-memory-poisoning-attack.md`
- [x] **[HIGH]** Forg365 Phishing-as-a-Service Targets Microsoft 365 With Device Code and AitM Theft — `2026-07-13-forg365-phishing-as-a-service-microsoft-365.md`
- [x] **[INFORMATIONAL]** Open Source 'ScamBuster' Tool Uses AI Personas to Engage Phishing Scammers — `2026-07-13-scambuster-open-source-ai-scam-baiting-tool.md`
- [x] **[HIGH]** RabbitMQ Vulnerability Exposes OAuth Client Secret, Enables Broker Takeover — `2026-07-13-rabbitmq-oauth-secret-vulnerability.md`
- [x] **[HIGH]** CISA Warns of Russian FSB Targeting Poorly Configured Network Devices — `2026-07-13-cisa-router-hygiene-russian-state-targeting.md`
- [x] **[MEDIUM]** EU and UK Jointly Sanction Russian GRU Hackers Over Cyberattacks — `2026-07-13-eu-uk-sanctions-russian-gru-hackers.md`
- [x] **[MEDIUM]** Attacker Uses Suspected AI-Generated PowerShell Script for AD Enumeration — `2026-07-13-ai-generated-powershell-active-directory-recon.md`
- [x] **[HIGH]** Zimbra Patches Critical Code Execution Vulnerability Triggered by Crafted Emails — `2026-07-13-zimbra-critical-code-execution-vulnerability-patched.md`
- [x] **[HIGH]** Progress Prompts ShareFile Storage Zone Controller Shutdown Amid Security Concerns — `2026-07-13-progress-sharefile-storage-zone-controller-shutdown.md`
- [x] **[CRITICAL]** Centers Laboratory Data Breach Affects 540,000 Individuals — `2026-07-13-centers-laboratory-data-breach-540000-individuals.md`
- [x] **[MEDIUM]** Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365 — `2026-07-13-evilginx-phishing-operations-exposed-misconfigured-server.md`
- [x] **[CRITICAL]** iCagenda and Balbooa Forms Joomla Flaws Exploited as Zero-Days, Added to CISA KEV — `2026-07-13-icagenda-balbooa-joomla-zero-day-exploited.md`

## Relevant (details)

### 1. CrashStealer macOS Malware Uses Notarized Dropper to Bypass Gatekeeper
- **Source:** The Hacker News — https://thehackernews.com/2026/07/crashstealer-macos-malware-uses.html
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** Jamf Threat Labs identified CrashStealer, a native-C++ macOS information stealer that uses a notarized dropper to pass Gatekeeper checks, unlike prior stealers built on AppleScript or Objective-C. It reportedly validates the victim's login password locally before exfiltrating data.

### 2. Google and Microsoft Pull ModHeader Extension Over Hidden Data Collector
- **Source:** The Hacker News — https://thehackernews.com/2026/07/google-and-microsoft-pull-modheader.html
- **Severity:** high
- **Tags:** `supply-chain`, `malware`
- **Summary:** Google and Microsoft pulled ModHeader, a header-editing extension with ~1.6 million installs, after researchers found a hidden browsing-history collector in the official store version. The collector was dormant and no evidence has emerged that it ever transmitted data.

### 3. GigaWiper: Modular Implant Combines Backdoor and Wiper Capabilities
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/gigawiper-threat-actors-choose-their-own-destructive-attack
- **Severity:** high
- **Tags:** `malware`
- **Summary:** A newly documented implant called GigaWiper borrows components from multiple malware families to combine backdoor and destructive wiper functionality in one modular tool, letting operators choose covert access or a destructive attack while minimizing operational footprint.

### 4. Google Open-Sources k8s-aibom for Automated AI Bills of Materials on GKE
- **Source:** Google Cloud Security — https://cloud.google.com/blog/products/identity-security/introducing-k8s-aibom-on-gke-for-automated-ai-bills-of-materials/
- **Severity:** informational
- **Tags:** `kubernetes`, `cloud-security`, `supply-chain`, `gcp`
- **Summary:** Google open-sourced k8s-aibom, an unprivileged Kubernetes controller that monitors cluster API and container environments to automatically detect running AI runtimes (like vLLM and Triton) and generate standardized AI bills of materials, aimed at giving security teams visibility into shadow AI workloads.

### 5. Lessons Learned From CISA's Contractor GitHub Credential Leak
- **Source:** Krebs on Security — https://krebsonsecurity.com/2026/07/lessons-learned-from-cisas-recent-github-leak/
- **Severity:** high
- **Tags:** `data-breach`, `github`, `aws`
- **Summary:** CISA published a postmortem on a leak in which a contractor exposed dozens of internal CISA credentials, including AWS GovCloud keys, in a public GitHub repo for nearly six months before KrebsOnSecurity notified the agency. Experts say gaps in the initial response hold lessons for any security team.

### 6. MemGhost Attack Plants Persistent False Memories in AI Agents via a Single Email
- **Source:** The Hacker News — https://thehackernews.com/2026/07/new-memghost-attack-plants-persistent.html
- **Severity:** high
- **Tags:** `llm`, `ai-safety`
- **Summary:** Researchers demonstrated MemGhost, an attack where a single crafted email tricks an AI assistant with persistent memory and inbox access into saving a false "fact" about the user, hiding the change, and quietly steering later responses without any visible sign of tampering.

### 7. Forg365 Phishing-as-a-Service Targets Microsoft 365 With Device Code and AitM Theft
- **Source:** The Hacker News — https://thehackernews.com/2026/07/forg365-phaas-targets-microsoft-365.html
- **Severity:** high
- **Tags:** `phishing`, `llm`
- **Summary:** A new phishing-as-a-service operation, Forg365, combines device code phishing, adversary-in-the-middle session theft, antibot evasion, and AI-assisted lure creation to target Microsoft 365 accounts. It's sold via Telegram for $400/month or $3,800/year.

### 8. Open Source 'ScamBuster' Tool Uses AI Personas to Engage Phishing Scammers
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/turning-tables-email-scammers-scambuster
- **Severity:** informational
- **Tags:** `phishing`, `llm`
- **Summary:** ScamBuster, an open source AI-driven system, adopts victim personas to engage with phishing and scam attackers, letting organizations and law enforcement gather intelligence on cybercriminal operations through extended AI-managed conversations.

### 9. RabbitMQ Vulnerability Exposes OAuth Client Secret, Enables Broker Takeover
- **Source:** SecurityWeek — https://www.securityweek.com/rabbitmq-vulnerability-threatens-enterprise-systems/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Summary:** A RabbitMQ vulnerability lets unauthenticated attackers obtain the message broker's confidential OAuth client secret, which can then be used to take full control of the broker.

### 10. CISA Warns of Russian FSB Targeting Poorly Configured Network Devices
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-194a
- **Severity:** high
- **Tags:** `critical-infrastructure`, `vulnerability`
- **Summary:** CISA, the FBI, and international partners warned that Russian FSB Center 16 cyber actors continue to exploit poorly configured and vulnerable networking devices to opportunistically compromise critical infrastructure networks worldwide, building on prior FBI advisories about the same campaign.

### 11. EU and UK Jointly Sanction Russian GRU Hackers Over Cyberattacks
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/eu-and-uk-hit-russia-with-first-joint-cyber-sanctions-package/
- **Severity:** medium
- **Tags:** `nation-state`
- **Summary:** The EU and UK jointly sanctioned dozens of Russian individuals and entities in their first coordinated cyber sanctions package, accusing Russia of coordinating a network of hacking groups responsible for attacks across Europe.

### 12. Attacker Uses Suspected AI-Generated PowerShell Script for AD Enumeration
- **Source:** The Hacker News — https://thehackernews.com/2026/07/attacker-uses-suspected-ai-generated.html
- **Severity:** medium
- **Tags:** `llm`, `malware`
- **Summary:** Researchers flagged an intrusion where a threat actor used a suspected AI-generated ("vibe-coded") PowerShell script to enumerate Active Directory, mapping the domain controller, users, computers, and domains before exporting a report file.

### 13. Zimbra Patches Critical Code Execution Vulnerability Triggered by Crafted Emails
- **Source:** SecurityWeek — https://www.securityweek.com/zimbra-patches-critical-code-execution-vulnerability/
- **Severity:** high
- **Tags:** `rce`, `cve`, `vulnerability`
- **Summary:** Zimbra patched a vulnerability that allows malicious code embedded in crafted emails to execute when a user opens the message, resulting in code execution on the mail server or client.

### 14. Progress Prompts ShareFile Storage Zone Controller Shutdown Amid Security Concerns
- **Source:** SecurityWeek — https://www.securityweek.com/progress-prompts-sharefile-storage-zone-controller-shutdown-amid-security-concerns/
- **Severity:** high
- **Tags:** `vulnerability`
- **Summary:** Progress Software told ShareFile customers to manually shut down their Storage Zone Controller servers while it investigates a credible security threat. Technical details have not yet been disclosed.

### 15. Centers Laboratory Data Breach Affects 540,000 Individuals
- **Source:** SecurityWeek — https://www.securityweek.com/centers-laboratory-data-breach-affects-540000-individuals/
- **Severity:** critical
- **Tags:** `data-breach`
- **Summary:** Healthcare testing and laboratory services provider Centers Laboratory disclosed a breach affecting 540,000 individuals. The WorldLeaks extortion group claimed to have stolen 720 GB of data from the organization.

### 16. Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365
- **Source:** The Hacker News — https://thehackernews.com/2026/07/misconfigured-server-reveals-three.html
- **Severity:** medium
- **Tags:** `phishing`
- **Summary:** French security firm Lexfo found an attacker's Python web server left running with directory listing enabled and the launch command visible in a readable `.bash_history`. That lapse let researchers pull the operator's entire Evilginx toolkit and pivot to two more related Microsoft 365 phishing operations.

### 17. iCagenda and Balbooa Forms Joomla Flaws Exploited as Zero-Days, Added to CISA KEV
- **Source:** The Hacker News — https://thehackernews.com/2026/07/icagenda-and-balbooa-forms-joomla-flaws.html
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `rce`, `vulnerability`
- **Summary:** CISA added two maximum-severity flaws (including CVE-2026-48939, CVSS 10.0) in the iCagenda and Balbooa Forms Joomla extensions to its Known Exploited Vulnerabilities catalog following reports of zero-day exploitation enabling remote code execution via arbitrary file uploads.

## Skippable

- **The wildest allegations in Apple's trade secrets lawsuit against OpenAI** — TechCrunch AI. Business/legal drama, no security-technical substance.
- **'Yellow Teams' Are Defining the Future of AI Security** — Dark Reading. Trend/opinion piece without a concrete incident or new technique.
- **Amazon SQS turns 20** — AWS News Blog. Anniversary marketing post, no security content.
- **Understanding Illicit Ecosystems: How Dark Web Forums Structure Cybercrime** — Flashpoint. Generic explainer, no specific incident or actionable intel.
- **Sam Altman's space data center trash talk** — TechCrunch AI. Celebrity feud commentary, not security/technical news.
- **Russian celebrity journalist Ksenia Sobchak says hackers accessed Telegram channels via email breach** — The Record. Individual account breach, regional, no technical detail.
- **The 6 wildest claims in Apple's lawsuit against OpenAI** — The Verge AI. Duplicate coverage of the Apple/OpenAI lawsuit story; no security substance either way.
- **Should AI help you get away with killing your spouse?** — TechCrunch AI. Opinion piece, no news value.
- **AWS Weekly Roundup** — AWS News Blog. Generic roundup, no security substance.
- **Anthropic starts localizing Claude pricing for India** — TechCrunch AI. Pricing/business update, not a model launch or security news.
- **CISA warns of actively exploited RCE flaws in Joomla extensions** — BleepingComputer. Duplicate coverage of the iCagenda/Balbooa Joomla zero-days; best source (The Hacker News, with CVE + CVSS) used instead.
- **Weekly Recap: ShareFile Threat, Citrix Bleed 2 Ransomware, AI Coding Attacks, and More** — The Hacker News. Aggregator roundup, not a single event.
- **Hacker Conversations: Jesse McGraw (GhostExodus)** — SecurityWeek. Human-interest profile, no news value.
- **Lidl discloses online shop breach after service provider hack** — BleepingComputer. Breach disclosure without technical substance or disclosed scale.
- **Waze adds new AI-powered features and customization updates** — TechCrunch AI. Duplicate of The Verge's Waze story; not a security topic.
- **Breach at the Beach: Play the Ultimate Entra ID CTF** — BleepingComputer. Vendor marketing for a CTF/training product.
- **UK charges suspects linked to Russian Coms call spoofing platform** — BleepingComputer. Law enforcement action without new technical detail.
- **New compliance guidance available: HITRUST i1 on AWS** — AWS Security Blog. Vendor compliance marketing content.
- **Cybersecurity M&A Roundup: 37 Deals Announced in June 2026** — SecurityWeek. Business/deal news, no security substance.
- **CISA Adds One Known Exploited Vulnerability to Catalog** — CISA Alerts. Routine KEV addition of an 18-year-old, low-severity Cisco IOS CSRF bug (CVE-2008-4128).
- **Meta Files Patent for AI That Can Listen All Day and Track How You're Feeling** — The Hacker News. Speculative patent filing, no deployed product or incident.
- **Thinking Fast and Slow in the SOC: The Case for Combining Autonomous AI with Analyst Copilots** — The Hacker News. Vendor-flavored analysis/opinion piece, no concrete news.
- **Rust-proof your code with our new Testing Handbook chapter** — Trail of Bits. Educational documentation, not a news item or incident.
- **EU Targets Russian Intelligence Officers Accused of Running a Yearslong Cyber Spying Campaign** — SecurityWeek. Duplicate coverage of the EU/UK sanctions action; best source (BleepingComputer, more detail) used instead.
- **US and allies warn of Russian critical infrastructure attacks** — BleepingComputer. Duplicate coverage of CISA's router-hygiene advisory; primary source (CISA) used instead.
- **Organizations Warned of Exploited Joomla Extension Vulnerabilities** — SecurityWeek. Duplicate coverage of the iCagenda/Balbooa Joomla zero-days; best source used instead.
- **Waze is getting a bunch of new AI-powered features** — The Verge AI. Duplicate of TechCrunch's Waze story; not a security topic.
