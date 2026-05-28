# Digest — 2026-05-28 PM

- Window: last 14h
- Raw items considered: 70
- Relevant: 19
- Skippable: 51

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Gogs Zero-Day RCE Lets Any Authenticated User Execute Arbitrary Code — `2026-05-28-gogs-zero-day-rce-authenticated-user.md`
- [x] **[HIGH]** FortiClient EMS Auth Bypass CVE-2026-35616 Actively Exploited to Deploy EKZ Credential Stealer — `2026-05-28-forticlient-ems-cve-2026-35616-ekz-credential-stealer.md`
- [x] **[HIGH]** Gitea Vulnerability Exposed 30,000 Deployments to Source Code and Credential Theft — `2026-05-28-gitea-vulnerability-30k-deployments-credentials-exposed.md`
- [x] **[HIGH]** JINX-0164 Targets Cryptocurrency Firms with macOS Malware and CI/CD Infrastructure Attacks — `2026-05-28-jinx-0164-crypto-macos-cicd-malware.md`
- [x] **[HIGH]** Carnival Confirms Data Breach Exposing Personal Data of Nearly 6 Million Customers — `2026-05-28-carnival-data-breach-6-million.md`
- [x] **[HIGH]** BTMOB Android RAT Enables Full Device Takeover via Malware-as-a-Service Model — `2026-05-28-btmob-android-rat-maas-full-device-takeover.md`
- [x] **[HIGH]** Russia-Linked GreyVibe Uses ChatGPT and Gemini to Supercharge Cyberattacks — `2026-05-28-greyvibe-russia-ai-assisted-cyberattacks.md`
- [x] **[HIGH]** CISA Warns of Frontier X Medical Device Flaw That Could Allow Attackers to Alter Clinical Readings — `2026-05-28-fourth-frontier-medical-device-patient-harm-cisa.md`
- [x] **[HIGH]** CISA Advisory: XCharge C6 EV Charger Flaws Allow RCE and Admin Takeover (CVSS 9.8) — `2026-05-28-xcharge-c6-ev-charger-rce-cvss-9-8-cisa.md`
- [x] **[MEDIUM]** Anthropic Releases Claude Opus 4.8 with Dynamic Workflows for Multi-Agent Coordination — `2026-05-28-anthropic-claude-opus-4-8-dynamic-workflows.md`
- [x] **[MEDIUM]** Google Launches AI Threat Defense Platform Combining Mandiant, Wiz, and Gemini — `2026-05-28-google-ai-threat-defense-platform-mandiant-wiz-gemini.md`
- [x] **[MEDIUM]** IBM and Red Hat Commit $5 Billion to Secure Open Source Supply Chains Under Project Lightwell — `2026-05-28-ibm-redhat-project-lightwell-open-source-supply-chain-5b.md`
- [x] **[MEDIUM]** Microsoft Pushes Coordinated Disclosure After Removing Researcher GitHub Account Over Zero-Day Drops — `2026-05-28-microsoft-cvd-policy-researcher-github-account-removed.md`
- [x] **[MEDIUM]** Chinese-Speaking Fraud Gang Registers 4,300 Fake FIFA Domains Targeting 2026 World Cup Fans — `2026-05-28-fifa-world-cup-2026-fraud-4300-domains-chinese-gang.md`
- [x] **[MEDIUM]** Cybercrime Gang Targeting Pirated Content Consumers Upgrades Miner to Full RAT — `2026-05-28-pirate-content-cybercrime-gang-adds-rat-module.md`
- [x] **[MEDIUM]** GCHQ Director Warns Russia Is Conducting Daily Hybrid Attacks on UK From Seabed to Cyberspace — `2026-05-28-russia-uk-gchq-hybrid-warfare-cyber-subsea.md`
- [x] **[MEDIUM]** Anthropic Closes $65 Billion Series H at $965 Billion Valuation Ahead of IPO — `2026-05-28-anthropic-65b-series-h-965b-valuation-ipo.md`
- [x] **[MEDIUM]** Cisco Talos Details Heap Overflow in DICOM Medical Imaging Libraries Including Pydicom, GDCM, and Orthanc — `2026-05-28-dicom-medical-imaging-heap-overflow-vulnerability-research.md`
- [x] **[INFORMATIONAL]** Edamame Launches Runtime Security Platform to Detect AI Coding Agent Intent Drift and Supply Chain Attacks — `2026-05-28-edamame-ai-coding-agent-runtime-security-platform.md`

## Relevant (details)

### 1. Gogs Zero-Day RCE Lets Any Authenticated User Execute Arbitrary Code
- **Source:** The Hacker News — https://thehackernews.com/2026/05/critical-gogs-rce-vulnerability-lets.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `zero-day`, `vulnerability`
- **Slug:** `gogs-zero-day-rce-authenticated-user`
- **Must-know:** no
- **Summary:** A CVSS 9.4 flaw in the Gogs self-hosted Git service discovered by Rapid7 allows any authenticated user to achieve RCE under certain conditions; no CVE has been assigned and no patch is available. All internet-facing Gogs instances are currently exposed with no vendor fix in sight.

### 2. FortiClient EMS Auth Bypass CVE-2026-35616 Actively Exploited to Deploy EKZ Credential Stealer
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-exploit-forticlient-ems-flaw-to-push-infostealer-malware/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `malware`, `privilege-escalation`
- **Slug:** `forticlient-ems-cve-2026-35616-ekz-credential-stealer`
- **Must-know:** no
- **Summary:** Threat actors are exploiting CVE-2026-35616 in FortiClient EMS to deliver EKZ, an undocumented credential stealer disguised as a Fortinet component. Fortinet hotfixes shipped in April; unpatched EMS deployments should be treated as potentially compromised.

### 3. Gitea Vulnerability Exposed 30,000 Deployments to Source Code and Credential Theft
- **Source:** SecurityWeek — https://www.securityweek.com/gitea-vulnerability-exposed-30000-deployments-to-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `data-breach`, `supply-chain`
- **Slug:** `gitea-vulnerability-30k-deployments-credentials-exposed`
- **Must-know:** no
- **Summary:** A Gitea flaw let attackers pull private container images, exposing source code, credentials, and infrastructure details from approximately 30,000 internet-facing deployments. Affected organizations should patch immediately and rotate any credentials stored in container images.

### 4. JINX-0164 Targets Cryptocurrency Firms with macOS Malware and CI/CD Infrastructure Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/05/jinx-0164-targets-cryptocurrency-firms.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `supply-chain`, `phishing`
- **Slug:** `jinx-0164-crypto-macos-cicd-malware`
- **Must-know:** no
- **Summary:** Wiz researchers identified a previously undocumented threat actor, JINX-0164, using fake job recruitment lures and bespoke macOS malware to target cryptocurrency organizations and steal digital assets. The campaign goes deep into CI/CD infrastructure, suggesting state-level resourcing; DPRK-linked patterns are noted.

### 5. Carnival Confirms Data Breach Exposing Personal Data of Nearly 6 Million Customers
- **Source:** The Record — https://therecord.media/cruise-giant-carnival-confirms-data-breach-affecting-6-million
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `carnival-data-breach-6-million`
- **Must-know:** no
- **Summary:** Carnival Corporation confirmed a threat actor compromised an employee account last month, copied personal data belonging to ~6 million customers, and was evicted by end of April. Affected customers face elevated identity theft risk.

### 6. BTMOB Android RAT Enables Full Device Takeover via Malware-as-a-Service Model
- **Source:** SecurityWeek — https://www.securityweek.com/new-btmob-android-malware-enables-full-device-takeover/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Slug:** `btmob-android-rat-maas-full-device-takeover`
- **Must-know:** no
- **Summary:** BTMOB is a new Android RAT delivered via phishing under a MaaS model with a no-code development interface, combining financial theft, data exfiltration, and remote access for full device takeover. Primarily targeting Brazil and Latin America.

### 7. Russia-Linked GreyVibe Uses ChatGPT and Gemini to Supercharge Cyberattacks
- **Source:** SecurityWeek — https://www.securityweek.com/russia-linked-greyvibe-attackers-use-ai-to-supercharge-cyberattacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ai-safety`, `llm`, `malware`
- **Slug:** `greyvibe-russia-ai-assisted-cyberattacks`
- **Must-know:** no
- **Summary:** Russia-linked GreyVibe extensively integrates ChatGPT, Gemini, and other AI tools into attack operations, previewing how state-aligned actors will operationalize commercial AI at scale. Defenders should anticipate increased AI-assisted attack velocity and AI-generated phishing.

### 8. CISA Warns of Frontier X Medical Device Flaw That Could Allow Attackers to Alter Clinical Readings
- **Source:** CISA — https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-148-01
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `iam`
- **Slug:** `fourth-frontier-medical-device-patient-harm-cisa`
- **Must-know:** no
- **Summary:** A missing authentication flaw (CVSS 8.8) in the Fourth Frontier Frontier X cardiac monitor allows an attacker to alter clinical readings via Bluetooth and cause patient harm. Affected: Android app < v15.0.0, iOS app < v25.0.0, Frontier X2 (all versions).

### 9. CISA Advisory: XCharge C6 EV Charger Flaws Allow RCE and Admin Takeover (CVSS 9.8)
- **Source:** CISA — https://www.cisa.gov/news-events/ics-advisories/icsa-26-148-08
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `vulnerability`, `rce`
- **Slug:** `xcharge-c6-ev-charger-rce-cvss-9-8-cisa`
- **Must-know:** no
- **Summary:** CISA advisory ICSA-26-148-08 covers CVSS 9.8 flaws in the XCharge C6 EV charger including stack-based buffer overflow and insecure code download, enabling RCE or full admin takeover. Deployed worldwide in transportation infrastructure.

### 10. Anthropic Releases Claude Opus 4.8 with Dynamic Workflows for Multi-Agent Coordination
- **Source:** TechCrunch AI — https://techcrunch.com/2026/05/28/anthropic-releases-opus-4-8-with-new-dynamic-workflow-tool/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-launch`, `anthropic`, `llm`, `model-release`
- **Slug:** `anthropic-claude-opus-4-8-dynamic-workflows`
- **Must-know:** no
- **Summary:** Anthropic released Claude Opus 4.8 with a new Dynamic Workflows tool for coordinating swarms of subagents, alongside improvements to model honesty and uncertainty acknowledgment. Available via API.

### 11. Google Launches AI Threat Defense Platform Combining Mandiant, Wiz, and Gemini
- **Source:** SecurityWeek — https://www.securityweek.com/google-unveils-ai-threat-defense-platform-to-fight-ai-powered-cyberattacks/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`, `google`, `cloud-security`, `wiz`
- **Slug:** `google-ai-threat-defense-platform-mandiant-wiz-gemini`
- **Must-know:** no
- **Summary:** Google unveiled an AI Threat Defense platform integrating Mandiant threat intel, Wiz cloud security, and Gemini AI to detect and respond to AI-powered attacks at machine speed. Positions itself as an AI-vs-AI defensive play.

### 12. IBM and Red Hat Commit $5 Billion to Secure Open Source Supply Chains Under Project Lightwell
- **Source:** SecurityWeek — https://www.securityweek.com/ibm-and-red-hat-commit-5-billion-to-secure-open-source-supply-chains-under-project-lightwell/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `supply-chain`, `devsecops`
- **Slug:** `ibm-redhat-project-lightwell-open-source-supply-chain-5b`
- **Must-know:** no
- **Summary:** IBM and Red Hat announced Project Lightwell, committing $5 billion to remediate open source supply chain vulnerabilities without breaking production workloads. Technical details on tooling and process have not yet been published.

### 13. Microsoft Pushes Coordinated Disclosure After Removing Researcher GitHub Account Over Zero-Day Drops
- **Source:** The Hacker News — https://thehackernews.com/2026/05/microsoft-slams-public-zero-day.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `zero-day`, `github`, `microsoft`
- **Slug:** `microsoft-cvd-policy-researcher-github-account-removed`
- **Must-know:** no
- **Summary:** Microsoft removed the GitHub account of researcher Chaotic Eclipse (aka Nightmare-Eclipse) after they publicly dropped details of multiple unpatched Microsoft zero-days, then publicly endorsed Coordinated Vulnerability Disclosure. Highlights ongoing tension between independent researchers and vendor-managed disclosure timelines.

### 14. Chinese-Speaking Fraud Gang Registers 4,300 Fake FIFA Domains Targeting 2026 World Cup Fans
- **Source:** The Record — https://therecord.media/chinese-speaking-fraud-gang-fifa-world-cup-scam
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`
- **Slug:** `fifa-world-cup-2026-fraud-4300-domains-chinese-gang`
- **Must-know:** no
- **Summary:** A Chinese-speaking gang has registered 4,300+ fraudulent FIFA domains since August 2025 to steal financial data and sell fake World Cup tickets and packages. The FBI also issued a warning on fake FIFA sites; the scale suggests a well-resourced, sustained operation.

### 15. Cybercrime Gang Targeting Pirated Content Consumers Upgrades Miner to Full RAT
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/video-books-pirates-miners-rat/119943/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `pirate-content-cybercrime-gang-adds-rat-module`
- **Must-know:** no
- **Summary:** A cybercrime gang targeting pirated book and movie consumers has upgraded its malware from a miner to a full RAT, expanding to sites with tens of millions of monthly visitors. Users who have downloaded pirated content from these sites may face full device compromise.

### 16. GCHQ Director Warns Russia Is Conducting Daily Hybrid Attacks on UK From Seabed to Cyberspace
- **Source:** The Record — https://therecord.media/russia-conducting-attacks-on-uk-gchq-briefing
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `cloud-security`
- **Slug:** `russia-uk-gchq-hybrid-warfare-cyber-subsea`
- **Must-know:** no
- **Summary:** GCHQ director Anne Keast-Butler disclosed that Russia is conducting daily hybrid attacks on the UK including subsea cable interference, energy pipeline sabotage, and cyber operations. The unusually candid public statement signals escalation; UK critical infrastructure teams should revisit Russian hybrid threat models.

### 17. Anthropic Closes $65 Billion Series H at $965 Billion Valuation Ahead of IPO
- **Source:** TechCrunch AI — https://techcrunch.com/2026/05/28/anthropic-raises-65-billion-nears-1t-valuation-ahead-of-ipo/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `anthropic`, `ai-launch`
- **Slug:** `anthropic-65b-series-h-965b-valuation-ipo`
- **Must-know:** no
- **Summary:** Anthropic closed a $65 billion Series H at a $965 billion post-money valuation, its likely final private round before an IPO. The capital targets model development, compute, and international expansion.

### 18. Cisco Talos Details Heap Overflow in DICOM Medical Imaging Libraries Including Pydicom, GDCM, and Orthanc
- **Source:** Cisco Talos — https://blog.talosintelligence.com/dicom-pydicom-gdcm-and-orthanc-a-technical-tour-of-what-really-happens-in-the-heap/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `vulnerability`, `rce`, `appsec`
- **Slug:** `dicom-medical-imaging-heap-overflow-vulnerability-research`
- **Must-know:** no
- **Summary:** Cisco Talos detailed how malformed DICOM files can trigger heap overflow vulnerabilities in Pydicom, GDCM, and Orthanc — widely deployed medical imaging libraries. Healthcare organizations should review the advisory and validate DICOM inputs at ingestion boundaries.

### 19. Edamame Launches Runtime Security Platform to Detect AI Coding Agent Intent Drift and Supply Chain Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/new-edamame-platform-aims-to-catch-ai-coding-agents-going-off-the-rails/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ai-safety`, `supply-chain`, `devsecops`, `appsec`
- **Slug:** `edamame-ai-coding-agent-runtime-security-platform`
- **Must-know:** no
- **Summary:** French startup Edamame launched a runtime verification platform using host telemetry and AI analysis to detect intent drift, secret theft, and supply chain attacks by AI coding agents in real time. Targets the growing risk of autonomous coding agents taking unintended or malicious actions in development pipelines.

## Skippable

- **Name That Toon Contest** — Dark Reading. Anniversary contest promotion, no security news value.
- **Introducing the next generation of AWS Resilience Hub for generative AI-based SRE resilience journey** — AWS News Blog. Generic AWS product launch with no security incident or novel technique.
- **FBI warns of fake FIFA websites running World Cup fraud schemes** — BleepingComputer. Duplicate; more detailed FIFA fraud report from The Record used instead.
- **Simplifying policy management with URL and Domain Category filtering on AWS Network Firewall** — AWS Security Blog. Cloud networking feature announcement; no security incident or novel security technique.
- **Just like gold and oil, we'll soon be able to trade AI token futures** — TechCrunch AI. Financial product speculation, no security or technical angle.
- **Introducing the next generation of Amazon OpenSearch Serverless for building your agentic AI applications** — AWS News Blog. Generic AWS product launch, no security angle.
- **Less panic patching, more precision** — Cisco Talos. Newsletter opinion piece on EPSS/GCVE patching strategy; useful framing but not a news item.
- **In just 3 weeks, StrictlyVC is coming to Los Angeles** — TechCrunch AI. Event promotion.
- **Geordie Raises $30 Million for AI Security and Governance Platform** — SecurityWeek. VC funding announcement with no technical disclosure or practitioner impact.
- **Claude's new model is more 'honest' when it messes up** — The Verge AI. Duplicate coverage of Anthropic Opus 4.8; primary sourced from TechCrunch.
- **A $2,000 AI-generated film will make its debut at Tribeca** — The Verge AI. Entertainment and arts, no security or AI research angle.
- **YouTube takes baby steps to being a real podcast app** — The Verge AI. Consumer product feature, no AI research or security relevance.
- **Agentic AI Isn't Risky; the Way Orgs Deploy It Is** — Dark Reading. Opinion piece without a specific news item or technical finding.
- **How long is Anthropic's lease with SpaceX? Opinions vary.** — TechCrunch AI. Business/legal dispute with no technical substance.
- **Sesame, the conversational AI startup from Oculus founders, launches its iOS app** — TechCrunch AI. Consumer AI app launch with no security or research angle.
- **Threat Actors Exploit Critical FortiClient EMS Flaw to Deploy Credential Stealer** — The Hacker News. Duplicate; FortiClient EMS story covered with more EKZ detail from BleepingComputer.
- **Catch up on 12 major I/O 2026 moments** — Google AI Blog. Thin video highlights roundup without specific newsworthy disclosures.
- **Carnival Data Breach Exposed 6 Million People** — SecurityWeek. Duplicate; Carnival breach covered with employee compromise detail from The Record.
- **Sneak peek at new Siri app reveals Apple's plans to take on ChatGPT and more** — TechCrunch AI. Product render speculation, no security angle.
- **These new iOS 27 renders hint at Siri's big redesign** — The Verge AI. Duplicate of Siri render story; no security angle.
- **RSI is the new AGI — and it's just as hard to pin down** — TechCrunch AI. Opinion/analysis without news value.
- **At TechCrunch Disrupt 2026: Databricks' co-founder on what kills enterprise AI deals** — TechCrunch AI. Conference panel commentary, no new technical information.
- **YouTube adds new podcast features, including an AI recommendation tool and 'Auto speed'** — TechCrunch AI. Duplicate of YouTube podcast story; consumer product with no security angle.
- **New Gogs zero-day flaw lets hackers get remote code execution** — BleepingComputer. Duplicate of Gogs zero-day; primary from The Hacker News used for Rapid7 CVSS 9.4 detail.
- **CNN sues Perplexity over 'verbatim' copycat articles** — The Verge AI. IP/copyright lawsuit, no security angle.
- **How SIEM helps MSPs reduce noise and stop threats faster** — BleepingComputer. Vendor-sponsored marketing content.
- **2 days left: Lock in ticket savings of up to $410 to TechCrunch Disrupt 2026** — TechCrunch AI. Event ticket promotion.
- **Visa invests in Replit to power agentic payments for developers** — TechCrunch AI. Investment news without security or novel technical substance.
- **Rivian's software chief thinks you don't need CarPlay or buttons** — The Verge AI. Automotive software interview, not security-related.
- **Canadian man gets 33 years for using social media to coerce US children into sending sexual content** — The Record. Criminal sentencing; not technically focused.
- **ThreatsDay Bulletin: Claude Security Plugin, Azure Priv-Esc, Kali365 MFA Bypass, FIFA Scams +15 More** — The Hacker News. Aggregated newsletter roundup; individual stories covered as standalone items.
- **Has the hunt for AI compute uncovered the next Cerebras?** — TechCrunch AI. Investment/market analysis, no security or technical research angle.
- **Critical FortiClient EMS Vulnerability Exploited in Fresh Attacks** — SecurityWeek. Duplicate of FortiClient EMS exploit story.
- **Romanian gets 5 years in prison for hacking Oregon govt network** — BleepingComputer. Criminal sentencing without novel technique or practitioner takeaway.
- **Focus on Cyber Insurance: How Quantifying Risk Is Reshaping Security** — Dark Reading. Video discussion/opinion piece without a news event.
- **Webinar: Why network incidents take too long to resolve** — BleepingComputer. Vendor webinar promotion.
- **ABB EIBPORT** — CISA Alerts. ICS advisory for building automation device; limited deployment footprint and advisory detail too thin for a standalone post.
- **Schnieider Electric EcoStruxure Machine Expert HVAC** — CISA Alerts. ICS advisory for HVAC programming software; limited scope and thin detail.
- **Jinan USR IOT Technology Limited (PUSR) USR-W610 RS232/485 to Wi-Fi/Ethernet Converter** — CISA Alerts. CVSS 9.8 industrial IoT converter; advisory detail too thin for a useful post.
- **ABB Busch-Welcome 2 Wire Door Opener Actuator** — CISA Alerts. CVSS 6.8 building automation device; narrow scope and limited detail.
- **CP Plus 8 Ch. Network Video Recorder** — CISA Alerts. XSS in NVR web interface; advisory is too thin and scope too narrow.
- **KMW CCTV Security Cameras** — CISA Alerts. CVSS 9.1 but advisory detail is too thin for a standalone informative post.
- **MacGregor Voyage Data Recorder (VDR) G4e** — CISA Alerts. CVSS 8.3 maritime device with default credentials; advisory is thin and deployment is narrow.
- **New AI Usage Report: Enterprise AI Risk Is Heavily Concentrated Among a Small Group of AI "Power users"** — The Hacker News. Vendor research report from LayerX Security; marketing framing, no technical disclosure.
- **Raising the Cybersecurity Stakes: Ante up for the Agentic Era** — SecurityWeek. Opinion/editorial without a concrete news event.
- **2026 World Cup: Discussing The World's Biggest Game's Attack Surface** — Unit 42 (Palo Alto). General threat overview; more specific FIFA fraud campaign already covered from The Record.
- **Sextortionist sentenced to 33 years for targeting 145 children** — BleepingComputer. Duplicate criminal sentencing story already covered from The Record.
- **BTMOB RAT Spreads Across Brazil, LatAm via MaaS Model** — Dark Reading. Duplicate of BTMOB RAT story; primary from SecurityWeek used.
- **YouTube will let you ask AI to make a custom video feed** — The Verge AI. Consumer product feature, no security or research angle.
- **Nordic CISOs Handle Rising Cyber Threats Remarkably Well** — Dark Reading. Regional survey opinion piece without hard news or technical findings.
- **Vertu wants CEOs to run companies from an AI foldable starting at $6,880** — TechCrunch AI. Luxury tech product launch, no security or AI research angle.
