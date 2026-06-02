# Digest — 2026-06-02 PM

- Window: last 14h
- Raw items considered: 60
- Relevant: 24
- Skippable: 36

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Red Hat NPM Supply Chain Attack Compromises 32 Packages via GitHub Account Hijack — `2026-06-02-red-hat-npm-supply-chain-attack.md`
- [x] **[HIGH]** AI-Built Ransomware Toolkit Automates EDR Evasion and Active Directory Discovery — `2026-06-02-ai-built-ransomware-edr-evasion.md`
- [x] **[HIGH]** Meta AI Confused Deputy Flaw Enables High-Profile Instagram Account Takeovers — `2026-06-02-meta-ai-instagram-account-hijacking.md`
- [x] **[HIGH]** Google Patches Android Zero-Day CVE-2025-48595 Exploited in Targeted Attacks — `2026-06-02-android-june-2026-zero-day-cve-2025-48595.md`
- [x] **[HIGH]** Gamaredon Exploits WinRAR CVE-2025-8088 to Deploy GammaWorm and GammaSteel Against Ukraine — `2026-06-02-gamaredon-winrar-gammaworm-ukraine.md`
- [x] **[HIGH]** Oracle WebLogic CVE-2024-21182 Under Active Exploitation, Added to CISA KEV — `2026-06-02-oracle-weblogic-cve-2024-21182-actively-exploited.md`
- [x] **[HIGH]** One Misconfigured Line Exposed Microsoft Account Tokens Across Billions of Android App Installs — `2026-06-02-microsoft-android-app-token-exposure.md`
- [x] **[HIGH]** Operation FlutterBridge: macOS Malvertising Campaign Distributes New FlutterShell Backdoor — `2026-06-02-operation-flutterbridge-macos-fluttershell.md`
- [x] **[HIGH]** SideCopy Targets Afghanistan Finance Ministry with Xeno RAT via Pashto-Language Spear Phishing — `2026-06-02-sidecopy-afghanistan-finance-xeno-rat.md`
- [x] **[HIGH]** Russia's FSB Claims Foreign Intelligence Agencies Installed Malware on Senior Officials' Phones — `2026-06-02-russia-officials-phones-foreign-espionage.md`
- [x] **[HIGH]** Dashlane Brute-Force Attack Leads to Encrypted Vault Downloads — `2026-06-02-dashlane-brute-force-vault-breach.md`
- [x] **[HIGH]** Critical Stack Overflow in HP VoIP Phones Enables Unauthenticated Remote Code Execution — `2026-06-02-hp-voip-phone-rce-stack-overflow.md`
- [x] **[MEDIUM]** Anthropic Expands Mythos Security Program to 150 Organizations Across Critical Infrastructure — `2026-06-02-anthropic-mythos-150-orgs-critical-infrastructure.md`
- [x] **[MEDIUM]** Microsoft Exchange Online Outage Disrupts Email Across North America and Germany — `2026-06-02-microsoft-exchange-online-outage.md`
- [x] **[MEDIUM]** Google Deploys AI Deepfake Call Detection to Flag Impersonation Scams in Phone App — `2026-06-02-google-ai-deepfake-call-detection.md`
- [x] **[MEDIUM]** Trump Signs Executive Order Creating Voluntary AI Prerelease Government Review Framework — `2026-06-02-trump-ai-executive-order-2026.md`
- [x] **[MEDIUM]** CISA and Eight Agencies Warn of Active Attacks Targeting Automatic Tank Gauge Systems — `2026-06-02-cisa-automatic-tank-gauge-hardening.md`
- [x] **[MEDIUM]** Unit 42 Updates npm Threat Landscape: Wormable Malware, CI/CD Persistence, Multi-Stage Attacks — `2026-06-02-npm-threat-landscape-unit42-june-2026.md`
- [x] **[MEDIUM]** Class Action Filed Against Amazon Over Ring's Unconsented Facial Recognition Data Collection — `2026-06-02-amazon-ring-facial-recognition-class-action.md`
- [x] **[INFORMATIONAL]** Microsoft Launches MAI-Thinking-1, Its First In-House Frontier Reasoning Model — `2026-06-02-microsoft-mai-thinking-1.md`
- [x] **[INFORMATIONAL]** Microsoft Scout Launches as Always-On AI Personal Assistant Built on OpenClaw — `2026-06-02-microsoft-scout-ai-assistant.md`
- [x] **[INFORMATIONAL]** Microsoft Introduces Portable Policy Files for Defining and Enforcing AI Agent Behavior — `2026-06-02-microsoft-ai-agent-policy-control.md`
- [x] **[INFORMATIONAL]** OpenAI Releases Six Codex Plugins Targeting Role-Specific White-Collar Workflows — `2026-06-02-openai-codex-role-plugins.md`
- [x] **[INFORMATIONAL]** H Company Releases Holo3.1: Fast and Local Computer Use Agents — `2026-06-02-holo31-computer-use-agents.md`

## Relevant (details)

### 1. Red Hat NPM Supply Chain Attack Compromises 32 Packages via GitHub Account Hijack
- **Source:** SecurityWeek — https://www.securityweek.com/supply-chain-attack-hits-32-red-hat-npm-packages/ | The Record — https://therecord.media/red-hat-removes-tainted-packages-after-software-pipeline-compromise
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`, `github`
- **Slug:** `2026-06-02-red-hat-npm-supply-chain-attack.md`
- **Must-know:** yes
- **Summary:** Attackers compromised a Red Hat GitHub account and pushed 96 malicious package versions across 32 packages, injecting a credential-stealing worm similar to Mini Shai-Hulud. The affected packages are downloaded ~117,000 times per week, making this a significant supply chain event with broad organizational exposure.

### 2. AI-Built Ransomware Toolkit Automates EDR Evasion and Active Directory Discovery
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/ai-built-ransomware-toolkit-automates-edr-evasion-ad-discovery/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`, `malware`, `llm`, `ai-safety`
- **Slug:** `2026-06-02-ai-built-ransomware-edr-evasion.md`
- **Must-know:** no
- **Summary:** A threat actor has deployed an AI-generated ransomware toolkit that automates Active Directory discovery and EDR evasion, lowering the technical floor for targeted ransomware campaigns. This is an operational deployment — not a PoC — of AI-generated attack tooling.

### 3. Meta AI Confused Deputy Flaw Enables High-Profile Instagram Account Takeovers
- **Source:** SecurityWeek — https://www.securityweek.com/meta-ai-hands-over-high-profile-instagram-accounts-to-hackers/ | BleepingComputer — https://www.bleepingcomputer.com/news/security/instagram-users-locked-out-after-meta-ai-abused-to-steal-accounts/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `meta`, `llm`, `ai-safety`, `data-breach`, `phishing`
- **Slug:** `2026-06-02-meta-ai-instagram-account-hijacking.md`
- **Must-know:** no
- **Summary:** Attackers hijacked high-profile Instagram accounts by asking Meta's AI chatbot to link target accounts to new email addresses, exploiting a confused deputy weakness in the AI support system. The attack required no technical exploit — just a social engineering prompt to the AI.

### 4. Google Patches Android Zero-Day CVE-2025-48595 Exploited in Targeted Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/06/google-june-2026-android-update-patches.html | CISA Alerts — https://www.cisa.gov/news-events/alerts/2026/06/02/cisa-adds-two-known-exploited-vulnerabilities-catalog
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `cve`, `google`, `privilege-escalation`
- **Slug:** `2026-06-02-android-june-2026-zero-day-cve-2025-48595.md`
- **Must-know:** no
- **Summary:** Google's June 2026 Android update patches CVE-2025-48595 (CVSS 8.4, privilege escalation, no user interaction required) confirmed exploited in targeted attacks. CISA added it to KEV alongside CVE-2022-0492 (Linux kernel improper authentication), also confirmed exploited.

### 5. Gamaredon Exploits WinRAR CVE-2025-8088 to Deploy GammaWorm and GammaSteel Against Ukraine
- **Source:** The Hacker News — https://thehackernews.com/2026/06/gamaredon-exploits-winrar-to-deliver.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `vulnerability`, `cve`, `phishing`
- **Slug:** `2026-06-02-gamaredon-winrar-gammaworm-ukraine.md`
- **Must-know:** no
- **Summary:** Russian threat group Gamaredon is actively exploiting CVE-2025-8088 (WinRAR path traversal) to deliver GammaPhish → GammaWorm (propagation) → GammaSteel (data theft) against Ukrainian targets. Attribution by Sekoia based on established Gamaredon TTPs.

### 6. Oracle WebLogic CVE-2024-21182 Under Active Exploitation, Added to CISA KEV
- **Source:** The Hacker News — https://thehackernews.com/2026/06/oracle-weblogic-cve-2024-21182-added-to.html | BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-oracle-weblogic-flaw/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `2026-06-02-oracle-weblogic-cve-2024-21182-actively-exploited.md`
- **Must-know:** no
- **Summary:** CISA added CVE-2024-21182 (CVSS 7.5) to KEV after confirming active exploitation; the unauthenticated WebLogic takeover flaw was patched in Oracle's January 2024 CPU. Federal agencies must remediate under BOD 22-01.

### 7. One Misconfigured Line Exposed Microsoft Account Tokens Across Billions of Android App Installs
- **Source:** SecurityWeek — https://www.securityweek.com/exclusive-how-one-line-of-code-put-billions-of-microsoft-android-app-downloads-at-risk/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `microsoft`, `vulnerability`, `appsec`, `data-breach`
- **Slug:** `2026-06-02-microsoft-android-app-token-exposure.md`
- **Must-know:** no
- **Summary:** A single development configuration setting in Microsoft's Android apps bypassed protections against unauthorized token access, exposing Microsoft account tokens across billions of installs to any malicious app on the same device. Microsoft has addressed the issue.

### 8. Operation FlutterBridge: macOS Malvertising Campaign Distributes New FlutterShell Backdoor
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/flutterbridge-new-fluttershell-backdoor/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `malware`, `appsec`, `phishing`
- **Slug:** `2026-06-02-operation-flutterbridge-macos-fluttershell.md`
- **Must-know:** no
- **Summary:** Unit 42 documented a macOS malvertising campaign distributing FlutterShell, a new backdoor built with the Flutter framework to evade static analysis. The campaign uses poisoned ads to serve malicious macOS installers, establishing persistent remote access.

### 9. SideCopy Targets Afghanistan Finance Ministry with Xeno RAT via Pashto-Language Spear Phishing
- **Source:** The Hacker News — https://thehackernews.com/2026/06/pakistan-linked-sidecopy-targets.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `malware`, `vulnerability`
- **Slug:** `2026-06-02-sidecopy-afghanistan-finance-xeno-rat.md`
- **Must-know:** no
- **Summary:** Pakistan-aligned SideCopy delivered Xeno RAT to Afghanistan's Ministry of Finance via a spear-phishing ZIP archive with a Pashto-language LNK filename. The campaign reflects ongoing South Asian regional espionage targeting financial ministries for intelligence collection.

### 10. Russia's FSB Claims Foreign Intelligence Agencies Installed Malware on Senior Officials' Phones
- **Source:** The Record (Recorded Future) — https://therecord.media/russia-claims-foreign-spy-agencies-hacked-gov-officials
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`, `vulnerability`
- **Slug:** `2026-06-02-russia-officials-phones-foreign-espionage.md`
- **Must-know:** no
- **Summary:** Russia's FSB claims it uncovered a "large-scale operation" by unnamed foreign intelligence agencies that installed malware on mobile devices of senior Russian government officials. Technical details and attribution are absent; independent verification is not possible.

### 11. Dashlane Brute-Force Attack Leads to Encrypted Vault Downloads
- **Source:** SecurityWeek — https://www.securityweek.com/dashlane-brute-force-attack-leads-to-limited-encrypted-vault-downloads/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `vulnerability`
- **Slug:** `2026-06-02-dashlane-brute-force-vault-breach.md`
- **Must-know:** no
- **Summary:** A brute-force attack against Dashlane led to the download of a limited number of encrypted password vaults. Automated account locking contained the attack, but offline cracking of stolen vaults remains a risk for accounts with weak master passwords.

### 12. Critical Stack Overflow in HP VoIP Phones Enables Unauthenticated Remote Code Execution
- **Source:** SecurityWeek — https://www.securityweek.com/critical-vulnerability-in-hp-voip-phones-enables-enterprise-network-breaches/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `2026-06-02-hp-voip-phone-rce-stack-overflow.md`
- **Must-know:** no
- **Summary:** A critical stack-based buffer overflow in HP VoIP phones enables unauthenticated remote code execution. VoIP devices are typically on trusted network segments, making successful exploitation a direct path to enterprise network access.

### 13. Anthropic Expands Mythos Security Program to 150 Organizations Across Critical Infrastructure
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/ | SecurityWeek — https://www.securityweek.com/anthropic-expanding-mythos-access-to-150-new-organizations/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `anthropic`, `ai-safety`, `llm`
- **Slug:** `2026-06-02-anthropic-mythos-150-orgs-critical-infrastructure.md`
- **Must-know:** no
- **Summary:** Anthropic is expanding Project Glasswing and Mythos access to 150 organizations in 15 countries covering power, water, healthcare, and communications sectors. Prior participants (~50 companies) collectively found thousands of vulnerabilities, validating the program's efficacy.

### 14. Microsoft Exchange Online Outage Disrupts Email Across North America and Germany
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-exchange-online-outage-causes-email-delays-failures/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `microsoft`, `cloud-security`
- **Slug:** `2026-06-02-microsoft-exchange-online-outage.md`
- **Must-know:** no
- **Summary:** Microsoft is investigating a widespread Exchange Online mail flow disruption affecting North America and Germany, causing email delays and delivery failures. No root cause disclosed at time of writing.

### 15. Google Deploys AI Deepfake Call Detection to Flag Impersonation Scams in Phone App
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/02/google-rolls-out-fake-call-detection-to-protect-against-ai-deepfake-impersonation-scams/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `google`, `ai-safety`, `phishing`
- **Slug:** `2026-06-02-google-ai-deepfake-call-detection.md`
- **Must-know:** no
- **Summary:** Google's Phone app now flags calls where a spoofed number and AI-cloned voice are used to impersonate a known contact. This is one of the first consumer-level defenses explicitly targeting AI deepfake vishing at the telephony layer.

### 16. Trump Signs Executive Order Creating Voluntary AI Prerelease Government Review Framework
- **Source:** The Record (Recorded Future) — https://therecord.media/white-house-unveils-ai-executive-order | TechCrunch AI — https://techcrunch.com/2026/06/02/trump-signs-narrower-executive-order-on-ai-oversight-after-industry-objections/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`, `openai`
- **Slug:** `2026-06-02-trump-ai-executive-order-2026.md`
- **Must-know:** no
- **Summary:** Trump signed an EO creating a voluntary framework for AI companies to share frontier models with the US government before release, narrowed significantly from earlier drafts after industry pushback. No mandatory timelines, safety thresholds, or enforcement mechanisms are specified.

### 17. CISA and Eight Agencies Warn of Active Attacks Targeting Automatic Tank Gauge Systems
- **Source:** CISA Alerts — https://www.cisa.gov/resources-tools/resources/cisa-and-partners-urge-hardening-automatic-tank-gauge-systems
- **Section:** Government / Advisory
- **Severity:** medium
- **Tags:** `vulnerability`, `cloud-security`
- **Slug:** `2026-06-02-cisa-automatic-tank-gauge-hardening.md`
- **Must-know:** no
- **Summary:** A multi-agency advisory confirms active malicious cyber activity targeting US automatic tank gauge (ATG) systems at gas stations, military sites, and industrial facilities. Hardening actions recommended include network segmentation and disabling unnecessary remote access.

### 18. Unit 42 Updates npm Threat Landscape: Wormable Malware, CI/CD Persistence, Multi-Stage Attacks
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `npm`, `supply-chain`, `malware`, `devsecops`
- **Slug:** `2026-06-02-npm-threat-landscape-unit42-june-2026.md`
- **Must-know:** no
- **Summary:** Unit 42's updated npm threat landscape analysis documents wormable malware, CI/CD persistence techniques, and multi-stage attack chains in the post-Shai Hulud ecosystem. Published the same day as the Red Hat npm supply chain incident, providing useful technical context.

### 19. Class Action Filed Against Amazon Over Ring's Unconsented Facial Recognition Data Collection
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/02/amazon-faces-class-action-lawsuit-over-ring-facial-recognition-feature/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `aws`, `data-breach`, `privacy`
- **Slug:** `2026-06-02-amazon-ring-facial-recognition-class-action.md`
- **Must-know:** no
- **Summary:** A Seattle class action alleges Ring's Familiar Faces feature stores facial images of passersby without consent, enrolling third parties into biometric databases without agreement. The case raises regulatory questions about biometric data collection in consumer IoT security devices.

### 20. Microsoft Launches MAI-Thinking-1, Its First In-House Frontier Reasoning Model
- **Source:** The Verge AI — https://www.theverge.com/tech/941664/microsoft-ai-model-reasoning-mai-thinking-1-build-2026
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `microsoft`, `model-release`, `ai-launch`, `llm`
- **Slug:** `2026-06-02-microsoft-mai-thinking-1.md`
- **Must-know:** no
- **Summary:** Microsoft unveiled MAI-Thinking-1, its first frontier reasoning model, at Build 2026 — marking a shift from relying exclusively on OpenAI models. No public benchmarks or API availability timeline announced.

### 21. Microsoft Scout Launches as Always-On AI Personal Assistant Built on OpenClaw
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/02/microsoft-launches-scout-an-openclaw-inspired-personal-assistant/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `microsoft`, `ai-launch`, `llm`
- **Slug:** `2026-06-02-microsoft-scout-ai-assistant.md`
- **Must-know:** no
- **Summary:** Microsoft Scout is an always-on AI assistant built on OpenClaw, integrated into Microsoft 365 apps. Unlike prompt-driven Copilot, Scout operates continuously with broad data access — raising enterprise security policy questions around persistent agent permissions.

### 22. Microsoft Introduces Portable Policy Files for Defining and Enforcing AI Agent Behavior
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/02/microsoft-offers-devs-a-better-way-to-control-ai-agent-behavior/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `microsoft`, `llm`, `ai-safety`, `devsecops`
- **Slug:** `2026-06-02-microsoft-ai-agent-policy-control.md`
- **Must-know:** no
- **Summary:** Microsoft's new portable policy file specification lets security and compliance teams define behavioral constraints for AI agents without modifying model code. Announced at Build 2026 as a direct response to enterprise concerns about high-autonomy agent scope.

### 23. OpenAI Releases Six Codex Plugins Targeting Role-Specific White-Collar Workflows
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/02/openai-launches-new-codex-tools-for-white-collar-work/ | OpenAI Blog — https://openai.com/index/codex-for-every-role-tool-workflow
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `openai`, `ai-launch`, `llm`
- **Slug:** `2026-06-02-openai-codex-role-plugins.md`
- **Must-know:** no
- **Summary:** OpenAI released six Codex plugins for data analytics, creative production, sales, product design, equity investing, and investment banking — expanding Codex from engineering into general white-collar AI workforce tooling.

### 24. H Company Releases Holo3.1: Fast and Local Computer Use Agents
- **Source:** Hugging Face Blog — https://huggingface.co/blog/Hcompany/holo31
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `llm`
- **Slug:** `2026-06-02-holo31-computer-use-agents.md`
- **Must-know:** no
- **Summary:** H Company released Holo3.1, a model for fast, locally-run computer use agent tasks, enabling privacy-sensitive or latency-constrained enterprise deployments without cloud inference. Detailed benchmarks not available in feed summary.

## Skippable

- **SentinelOne + Claude: Integrations for AI Visibility, Governance, and Defense** — SentinelOne Labs. Marketing content promoting SentinelOne's Claude integration; no independent security news value.
- **Microsoft Build 2026: the 7 biggest announcements** — The Verge AI. Conference roundup; individual announcements covered separately.
- **Uber caps employee AI spending after blowing through budget** — TechCrunch AI. Business operations news with no security angle.
- **Securing AI Agents Before They Go Rogue Is Next to Impossible** — Dark Reading. Analysis/opinion piece without a specific incident or new technical finding.
- **New Microsoft tool lets devs spin up AI behavior tests using text descriptions** — TechCrunch AI. Developer tooling (ASSERT framework); lower signal than other Build items already covered.
- **Identify unused AWS KMS keys and prevent accidental key deletions** — AWS Security Blog. Generic cloud key management how-to; no news value.
- **Trump signs executive order to review AI models before they're released** — The Verge AI. Duplicate; covered via The Record.
- **Martin Scorsese becomes the latest — and most unlikely — Hollywood voice for AI** — TechCrunch AI. Celebrity opinion piece; no technical or security value.
- **Microsoft Scout is a new AI personal assistant built on OpenClaw** — The Verge AI. Duplicate with TechCrunch Scout item; incorporated as context.
- **Google's Phone app will tell you if a scammer is impersonating one of your contacts** — The Verge AI. Duplicate; covered via TechCrunch Google deepfake item.
- **Microsoft's Project Solara is an OS for AI agent gadgets** — The Verge AI. Concept hardware OS announcement; no immediate security angle.
- **Two New Reports Offer Competing Explanations for Cybersecurity's Growing Crisis** — SecurityWeek. Opinion/analysis without an actionable finding.
- **Microsoft created the mini Surface dev box that Qualcomm couldn't** — The Verge AI. Hardware product launch; no security angle.
- **Trump signs narrower executive order on AI oversight after industry objections** — TechCrunch AI. Duplicate; covered via The Record.
- **Secure multi-tenant AI agents with Amazon Bedrock AgentCore resource-based policies** — AWS Security Blog. Vendor how-to post; marketing content.
- **Microsoft Build 2026: All the news about Windows, AI, RTX Spark, and more** — The Verge AI. Conference roundup; individual items covered separately.
- **Instagram users locked out after Meta AI abused to steal accounts** — BleepingComputer. Incorporated as co-source in Meta AI Instagram hijacking post; SecurityWeek had superior technical detail.
- **Android Update Patches Exploited Zero-Day, 123 Other Vulnerabilities** — SecurityWeek. Duplicate; covered via The Hacker News.
- **Why the browser is now the front line for AI security** — BleepingComputer. Vendor-sponsored content from Push Security; not independent editorial.
- **Anthropic Expanding Mythos Access to 150 New Organizations** — SecurityWeek. Incorporated as co-source in Anthropic Mythos post; TechCrunch had broader context.
- **Red Hat removes tainted packages after software pipeline compromise** — The Record. Incorporated as co-source in Red Hat supply chain post; SecurityWeek had the technical payload detail.
- **CISA flags two-year-old Oracle flaw as actively exploited** — BleepingComputer. Incorporated as co-source in Oracle WebLogic post; The Hacker News used as primary.
- **Gemini Spark is the most impressive and terrifying AI experience I've had yet** — The Verge AI. First-person product review; opinion piece without news value.
- **ZeroDrift raises $10M to protect AI models from themselves** — TechCrunch AI. Startup funding announcement; no technical detail or novel finding.
- **The Zero-Knowledge Threat Actor and the End of Responsible Disclosure** — SecurityWeek. Opinion piece about AI-assisted attack tooling; no specific incident.
- **Wardriving assessment across Mexico: Preparing for the 2026 World Cup** — Securelist. Regional Wi-Fi security assessment; no novel exploit technique.
- **Beyond Assume-Breach: How AI-Native Security Will Reshape Enterprise Defense** — Dark Reading. Opinion/marketing content; no specific news.
- **Travelers deploys AI-powered claims countrywide with OpenAI** — OpenAI Blog. Enterprise case study; no security angle.
- **Rocket engine startup Impulse raises $500 million to hire people, not AI** — TechCrunch AI. Off-topic; no AI or security news value.
- **CISA Adds Two Known Exploited Vulnerabilities to Catalog** — CISA Alerts. Incorporated into Android zero-day post (CVE-2025-48595 and CVE-2022-0492); not a standalone story.
- **AI-Driven Exploitation is Destroying Vulnerability Management** — The Hacker News. Sponsored vendor content; opinion framing without a specific new finding.
- **Oracle WebLogic Vulnerability Exploited in the Wild** — SecurityWeek. Duplicate; covered via The Hacker News.
- **Google fixes one actively exploited Android zero-day, 124 flaws** — BleepingComputer. Duplicate; covered via The Hacker News.
- **Meta AI Hands Over High-Profile Instagram Accounts to Hackers** — SecurityWeek. Used as primary source (with better technical detail) for Meta AI Instagram post; BleepingComputer item (31) incorporated as co-source.
- **How Leading Organizations Are Turning EDR Into Operational Resilience** — The Hacker News. Sponsored vendor content about EDR adoption.
- **Supply Chain Attack Hits 32 Red Hat NPM Packages** — SecurityWeek. This item IS the primary source for the Red Hat supply chain post; The Record (item 38) was incorporated as co-source.
- **Codex for every role, tool, and workflow** — OpenAI Blog. Incorporated as co-source in OpenAI Codex plugins post; TechCrunch had more contextual detail.
- **Advancing youth safety and opportunity through global leadership** — OpenAI Blog. PR/policy content; no specific technical news or security angle.
