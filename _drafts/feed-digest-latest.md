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
- **Source:** SecurityWeek — https://www.securityweek.com/supply-chain-attack-hits-32-red-hat-npm-packages/
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`, `github`
- **Summary:** Attackers compromised a Red Hat GitHub account and pushed 96 malicious package versions across 32 packages, injecting a credential-stealing worm similar to Mini Shai-Hulud (~117k weekly downloads affected). Must-know: organizations using these packages should audit installs and rotate credentials immediately.

### 2. AI-Built Ransomware Toolkit Automates EDR Evasion and Active Directory Discovery
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/ai-built-ransomware-toolkit-automates-edr-evasion-ad-discovery/
- **Severity:** high
- **Tags:** `ransomware`, `malware`, `llm`, `ai-safety`
- **Summary:** A threat actor deployed an AI-generated ransomware toolkit that automates AD discovery and EDR evasion in production. Marks a concrete operational milestone for AI-assisted attack tooling — not a PoC.

### 3. Meta AI Confused Deputy Flaw Enables High-Profile Instagram Account Takeovers
- **Source:** SecurityWeek — https://www.securityweek.com/meta-ai-hands-over-high-profile-instagram-accounts-to-hackers/
- **Severity:** high
- **Tags:** `meta`, `llm`, `ai-safety`, `data-breach`, `phishing`
- **Summary:** Attackers asked Meta's AI chatbot to link target Instagram accounts to new email addresses, exploiting a confused deputy weakness with no technical exploit required. High-profile accounts were affected; no patch confirmed yet.

### 4. Google Patches Android Zero-Day CVE-2025-48595 Exploited in Targeted Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/06/google-june-2026-android-update-patches.html
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `cve`, `google`, `privilege-escalation`
- **Summary:** Android June 2026 update patches CVE-2025-48595 (CVSS 8.4, no-interaction privilege escalation, active exploitation confirmed) and 123 others. CISA also added CVE-2022-0492 (Linux kernel) to KEV in the same advisory.

### 5. Gamaredon Exploits WinRAR CVE-2025-8088 to Deploy GammaWorm and GammaSteel Against Ukraine
- **Source:** The Hacker News — https://thehackernews.com/2026/06/gamaredon-exploits-winrar-to-deliver.html
- **Severity:** high
- **Tags:** `malware`, `vulnerability`, `cve`, `phishing`
- **Summary:** Russian group Gamaredon is exploiting a WinRAR path traversal flaw (CVE-2025-8088) to deliver a multi-stage chain: GammaPhish → GammaWorm (propagation) → GammaSteel (data theft), actively targeting Ukraine.

### 6. Oracle WebLogic CVE-2024-21182 Under Active Exploitation, Added to CISA KEV
- **Source:** The Hacker News — https://thehackernews.com/2026/06/oracle-weblogic-cve-2024-21182-added-to.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Summary:** CISA added CVE-2024-21182 (CVSS 7.5, unauthenticated WebLogic takeover) to KEV; patched in January 2024 CPU. Two-year-old flaw now confirmed actively exploited — patch immediately.

### 7. One Misconfigured Line Exposed Microsoft Account Tokens Across Billions of Android App Installs
- **Source:** SecurityWeek — https://www.securityweek.com/exclusive-how-one-line-of-code-put-billions-of-microsoft-android-app-downloads-at-risk/
- **Severity:** high
- **Tags:** `microsoft`, `vulnerability`, `appsec`, `data-breach`
- **Summary:** A single dev configuration setting in Microsoft's Android apps bypassed protections against cross-app token access, exposing Microsoft account tokens across billions of installs to any malicious app on the same device. Addressed by Microsoft.

### 8. Operation FlutterBridge: macOS Malvertising Campaign Distributes New FlutterShell Backdoor
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/flutterbridge-new-fluttershell-backdoor/
- **Severity:** high
- **Tags:** `malware`, `appsec`, `phishing`
- **Summary:** Unit 42 documented a macOS malvertising campaign distributing FlutterShell, a new backdoor using Flutter to evade static analysis, served via poisoned ads to macOS users.

### 9. SideCopy Targets Afghanistan Finance Ministry with Xeno RAT via Pashto-Language Spear Phishing
- **Source:** The Hacker News — https://thehackernews.com/2026/06/pakistan-linked-sidecopy-targets.html
- **Severity:** high
- **Tags:** `phishing`, `malware`, `vulnerability`
- **Summary:** Pakistan-aligned SideCopy used a Pashto-language LNK file in a spear-phishing ZIP to deliver Xeno RAT against Afghanistan's Finance Ministry — regional espionage targeting financial intelligence.

### 10. Russia's FSB Claims Foreign Intelligence Agencies Installed Malware on Senior Officials' Phones
- **Source:** The Record — https://therecord.media/russia-claims-foreign-spy-agencies-hacked-gov-officials
- **Severity:** high
- **Tags:** `malware`, `phishing`, `vulnerability`
- **Summary:** Russia's FSB claims a "large-scale operation" by unnamed foreign agencies installed malware on senior officials' mobile devices. No technical details or attribution released; independent verification not possible.

### 11. Dashlane Brute-Force Attack Leads to Encrypted Vault Downloads
- **Source:** SecurityWeek — https://www.securityweek.com/dashlane-brute-force-attack-leads-to-limited-encrypted-vault-downloads/
- **Severity:** high
- **Tags:** `data-breach`, `vulnerability`
- **Summary:** Brute-force attack against Dashlane resulted in encrypted vault downloads; automated account locking contained further access. Offline cracking of stolen vaults remains a risk for weak master passwords.

### 12. Critical Stack Overflow in HP VoIP Phones Enables Unauthenticated Remote Code Execution
- **Source:** SecurityWeek — https://www.securityweek.com/critical-vulnerability-in-hp-voip-phones-enables-enterprise-network-breaches/
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Summary:** Critical stack-based buffer overflow in HP VoIP phones allows unauthenticated RCE. VoIP devices sit on trusted internal segments, making this a direct path to enterprise network access.

### 13. Anthropic Expands Mythos Security Program to 150 Organizations Across Critical Infrastructure
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/
- **Severity:** medium
- **Tags:** `anthropic`, `ai-safety`, `llm`
- **Summary:** Anthropic expands Mythos and Project Glasswing to 150 organizations in 15 countries covering power, water, healthcare, and comms — the program's largest deployment, targeting infrastructure where attacks could affect 100M people.

### 14. Microsoft Exchange Online Outage Disrupts Email Across North America and Germany
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-exchange-online-outage-causes-email-delays-failures/
- **Severity:** medium
- **Tags:** `microsoft`, `cloud-security`
- **Summary:** Widespread Exchange Online mail flow outage affecting North America and Germany. Microsoft investigating; no root cause disclosed.

### 15. Google Deploys AI Deepfake Call Detection to Flag Impersonation Scams in Phone App
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/02/google-rolls-out-fake-call-detection-to-protect-against-ai-deepfake-impersonation-scams/
- **Severity:** medium
- **Tags:** `google`, `ai-safety`, `phishing`
- **Summary:** Google Phone app now flags spoofed numbers with AI-cloned voices impersonating contacts — one of the first consumer defenses explicitly targeting AI deepfake vishing.

### 16. Trump Signs Executive Order Creating Voluntary AI Prerelease Government Review Framework
- **Source:** The Record — https://therecord.media/white-house-unveils-ai-executive-order
- **Severity:** medium
- **Tags:** `ai-safety`, `openai`
- **Summary:** EO creates voluntary (not mandatory) framework for AI companies to share frontier models with the US government before release; narrowed significantly after industry objections. No enforcement mechanisms.

### 17. CISA and Eight Agencies Warn of Active Attacks Targeting Automatic Tank Gauge Systems
- **Source:** CISA Alerts — https://www.cisa.gov/resources-tools/resources/cisa-and-partners-urge-hardening-automatic-tank-gauge-systems
- **Severity:** medium
- **Tags:** `vulnerability`, `cloud-security`
- **Summary:** Multi-agency advisory confirms active malicious activity against US ATG systems controlling fuel storage at gas stations, military sites, and industrial facilities. Recommends network segmentation and disabling remote access.

### 18. Unit 42 Updates npm Threat Landscape: Wormable Malware, CI/CD Persistence, Multi-Stage Attacks
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/
- **Severity:** medium
- **Tags:** `npm`, `supply-chain`, `malware`, `devsecops`
- **Summary:** Updated analysis documents wormable npm malware, CI/CD persistence, and multi-stage chains in the post-Shai Hulud ecosystem. Published same day as Red Hat npm supply chain incident.

### 19. Class Action Filed Against Amazon Over Ring's Unconsented Facial Recognition Data Collection
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/02/amazon-faces-class-action-lawsuit-over-ring-facial-recognition-feature/
- **Severity:** medium
- **Tags:** `aws`, `data-breach`, `privacy`
- **Summary:** Seattle class action alleges Ring Familiar Faces stores facial images of passersby without consent, enrolling non-consenting third parties into biometric databases via consumer doorbell cameras.

### 20. Microsoft Launches MAI-Thinking-1, Its First In-House Frontier Reasoning Model
- **Source:** The Verge AI — https://www.theverge.com/tech/941664/microsoft-ai-model-reasoning-mai-thinking-1-build-2026
- **Severity:** informational
- **Tags:** `microsoft`, `model-release`, `ai-launch`, `llm`
- **Summary:** Microsoft's first frontier reasoning model, unveiled at Build 2026, signals a shift from OpenAI dependency. No public benchmarks or API timeline announced yet.

### 21. Microsoft Scout Launches as Always-On AI Personal Assistant Built on OpenClaw
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/02/microsoft-launches-scout-an-openclaw-inspired-personal-assistant/
- **Severity:** informational
- **Tags:** `microsoft`, `ai-launch`, `llm`
- **Summary:** Microsoft Scout is an always-on OpenClaw-based assistant integrated into Microsoft 365, with persistent broad data access across Outlook, OneDrive, and Teams.

### 22. Microsoft Introduces Portable Policy Files for Defining and Enforcing AI Agent Behavior
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/02/microsoft-offers-devs-a-better-way-to-control-ai-agent-behavior/
- **Severity:** informational
- **Tags:** `microsoft`, `llm`, `ai-safety`, `devsecops`
- **Summary:** New portable policy file spec from Microsoft lets security and compliance teams define behavioral constraints for AI agents without touching model code — direct response to enterprise agent governance concerns.

### 23. OpenAI Releases Six Codex Plugins Targeting Role-Specific White-Collar Workflows
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/02/openai-launches-new-codex-tools-for-white-collar-work/
- **Severity:** informational
- **Tags:** `openai`, `ai-launch`, `llm`
- **Summary:** Six Codex plugins for data analytics, creative production, sales, product design, equity investing, and investment banking expand OpenAI's Codex beyond software engineering.

### 24. H Company Releases Holo3.1: Fast and Local Computer Use Agents
- **Source:** Hugging Face Blog — https://huggingface.co/blog/Hcompany/holo31
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `llm`
- **Summary:** Holo3.1 enables fast, locally-run computer use agent tasks without cloud inference — relevant for privacy-sensitive or latency-constrained enterprise deployments.

## Skippable

- **SentinelOne + Claude: Integrations for AI Visibility, Governance, and Defense** — SentinelOne Labs. Marketing content promoting SentinelOne's Claude integration; no independent security news.
- **Microsoft Build 2026: the 7 biggest announcements** — The Verge AI. Conference roundup; individual announcements covered separately.
- **Uber caps employee AI spending after blowing through budget** — TechCrunch AI. Business operations news; no security angle.
- **Securing AI Agents Before They Go Rogue Is Next to Impossible** — Dark Reading. Analysis/opinion piece; no specific incident or new finding.
- **New Microsoft tool lets devs spin up AI behavior tests using text descriptions** — TechCrunch AI. Developer tooling (ASSERT framework); lower signal than other Build items covered separately.
- **Identify unused AWS KMS keys and prevent accidental key deletions** — AWS Security Blog. Generic cloud key management how-to; no news value.
- **Trump signs executive order to review AI models before they're released** — The Verge AI. Duplicate; covered via The Record.
- **Martin Scorsese becomes the latest — and most unlikely — Hollywood voice for AI** — TechCrunch AI. Celebrity opinion piece; no technical value.
- **Microsoft Scout is a new AI personal assistant built on OpenClaw** — The Verge AI. Duplicate; covered via TechCrunch Scout item.
- **Google's Phone app will tell you if a scammer is impersonating one of your contacts** — The Verge AI. Duplicate; covered via TechCrunch Google deepfake item.
- **Microsoft's Project Solara is an OS for AI agent gadgets** — The Verge AI. Concept hardware OS announcement; no security angle.
- **Two New Reports Offer Competing Explanations for Cybersecurity's Growing Crisis** — SecurityWeek. Opinion/analysis; no actionable news.
- **Microsoft created the mini Surface dev box that Qualcomm couldn't** — The Verge AI. Hardware product launch; no security angle.
- **Trump signs narrower executive order on AI oversight after industry objections** — TechCrunch AI. Duplicate; covered via The Record.
- **Secure multi-tenant AI agents with Amazon Bedrock AgentCore resource-based policies** — AWS Security Blog. Vendor how-to/marketing post.
- **Microsoft Build 2026: All the news about Windows, AI, RTX Spark, and more** — The Verge AI. Conference roundup; individual items covered separately.
- **Instagram users locked out after Meta AI abused to steal accounts** — BleepingComputer. Incorporated as co-source in Meta AI Instagram hijacking post; SecurityWeek had superior technical detail.
- **Android Update Patches Exploited Zero-Day, 123 Other Vulnerabilities** — SecurityWeek. Duplicate; covered via The Hacker News.
- **Why the browser is now the front line for AI security** — BleepingComputer. Vendor-sponsored content (Push Security); not editorial.
- **Anthropic Expanding Mythos Access to 150 New Organizations** — SecurityWeek. Incorporated as co-source in Anthropic Mythos post.
- **Red Hat removes tainted packages after software pipeline compromise** — The Record. Incorporated as co-source in Red Hat supply chain post.
- **CISA flags two-year-old Oracle flaw as actively exploited** — BleepingComputer. Incorporated as co-source in Oracle WebLogic post.
- **Gemini Spark is the most impressive and terrifying AI experience I've had yet** — The Verge AI. First-person product review; opinion.
- **ZeroDrift raises $10M to protect AI models from themselves** — TechCrunch AI. Startup funding announcement; no technical detail.
- **The Zero-Knowledge Threat Actor and the End of Responsible Disclosure** — SecurityWeek. Opinion piece; no specific incident.
- **Wardriving assessment across Mexico: Preparing for the 2026 World Cup** — Securelist. Regional research; no novel exploit technique.
- **Beyond Assume-Breach: How AI-Native Security Will Reshape Enterprise Defense** — Dark Reading. Opinion/marketing; no news.
- **Travelers deploys AI-powered claims countrywide with OpenAI** — OpenAI Blog. Enterprise case study; no security angle.
- **Rocket engine startup Impulse raises $500 million to hire people, not AI** — TechCrunch AI. Off-topic.
- **CISA Adds Two Known Exploited Vulnerabilities to Catalog** — CISA Alerts. Incorporated into Android zero-day post (CVE-2025-48595 and CVE-2022-0492).
- **AI-Driven Exploitation is Destroying Vulnerability Management** — The Hacker News. Sponsored/vendor-framed content.
- **Oracle WebLogic Vulnerability Exploited in the Wild** — SecurityWeek. Duplicate; covered via The Hacker News.
- **Google fixes one actively exploited Android zero-day, 124 flaws** — BleepingComputer. Duplicate; covered via The Hacker News.
- **How Leading Organizations Are Turning EDR Into Operational Resilience** — The Hacker News. Sponsored vendor content.
- **Codex for every role, tool, and workflow** — OpenAI Blog. Incorporated as co-source in OpenAI Codex plugins post.
- **Advancing youth safety and opportunity through global leadership** — OpenAI Blog. PR/policy content; no specific technical news.
