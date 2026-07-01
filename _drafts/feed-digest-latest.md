# Digest — 2026-07-01 AM

- Window: last 14h
- Raw items considered: 33
- Relevant: 16
- Skippable: 17

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** ARToken Phishing-as-a-Service Panel Targets Microsoft 365 Accounts — `2026-07-01-artoken-phishing-panel-targets-microsoft-365.md`
- [x] **[HIGH]** Adobe Patches Seven Max-Severity ColdFusion and Campaign Flaws — `2026-07-01-adobe-patches-coldfusion-campaign-max-severity-flaws.md`
- [x] **[HIGH]** Azure CLI Password Spray Compromises 78 Microsoft Accounts in 81M+ Attempts — `2026-07-01-azure-cli-password-spray-78-accounts-compromised.md`
- [x] **[HIGH]** Google Patches 382 Chrome Vulnerabilities, 15 Rated Critical — `2026-07-01-google-chrome-382-vulnerabilities-patched.md`
- [x] **[MEDIUM]** Researcher Analysis of 3,000 ClickFix Payloads Reveals API-Driven Malware Delivery — `2026-07-01-clickfix-3000-payloads-api-driven-malware-delivery.md`
- [x] **[HIGH]** Citrix Patches Six NetScaler Flaws Including CVE-2026-8451 — `2026-07-01-citrix-netscaler-six-flaws-cve-2026-8451.md`
- [x] **[MEDIUM]** Phantom Squatting: AI-Hallucinated Domains Weaponized as Supply Chain Vector — `2026-07-01-phantom-squatting-ai-hallucinated-domains-supply-chain.md`
- [x] **[HIGH]** China-Linked Group Deploys New Backdoor Against Southeast Asia Critical Systems — `2026-07-01-china-linked-group-southeast-asia-critical-systems-backdoor.md`
- [x] **[MEDIUM]** Anthropic Restores Claude Fable 5 After Export Controls Lifted — `2026-07-01-anthropic-restores-claude-fable-5-export-controls-lifted.md`
- [x] **[MEDIUM]** Anthropic Launches Claude Sonnet 5 With Near-Opus 4.8 Performance — `2026-06-30-anthropic-claude-sonnet-5-launch.md`
- [x] **[INFORMATIONAL]** Google Ships Nano Banana 2 Lite, a Faster Gemini Image Model — `2026-06-30-google-nano-banana-2-lite-gemini-image-model.md`
- [x] **[INFORMATIONAL]** OpenClaw Agentic App Launches on Android and iOS — `2026-06-30-openclaw-agentic-app-android-ios-launch.md`
- [x] **[HIGH]** BioShocking Attack Tricks AI Browsers Into Data Theft via Fictional Framing — `2026-06-30-bioshocking-attack-ai-browser-prompt-injection-data-theft.md`
- [x] **[HIGH]** Agentjacking: Fake Bug Reports Hijack AI Coding Agents at Scale — `2026-06-30-agentjacking-fake-bug-reports-hijack-ai-coding-agents.md`
- [x] **[HIGH]** Malicious PyPI Packages Give Attackers Control of Telegram Bot Servers — `2026-06-30-malicious-pypi-packages-telegram-bot-servers.md`
- [x] **[HIGH]** Attackers Hijack Exposed AI Endpoints to Power Offensive Operations — `2026-06-30-attackers-hijack-exposed-ai-endpoints-offensive-ops.md`

## Relevant (details)

### 1. ARToken Phishing-as-a-Service Panel Targets Microsoft 365 Accounts
- **Source:** Cisco Talos — https://blog.talosintelligence.com/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365/
- **Severity:** high
- **Tags:** `phishing`, `microsoft`, `malware`, `iam`
- **Summary:** Cisco Talos identified "ARToken," a fully-featured phishing-as-a-service panel with 80+ API endpoints for device code phishing and Primary Refresh Token theft against Microsoft 365 accounts, sharing infrastructure with the EvilTokens platform.

### 2. Adobe Patches Seven Max-Severity ColdFusion and Campaign Flaws
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/adobe-patches-seven-max-severity-coldfusion-campaign-flaws/
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`
- **Summary:** Adobe released patches for seven maximum-severity vulnerabilities in ColdFusion and Campaign Classic. No exploitation-in-the-wild status was disclosed.

### 3. Azure CLI Password Spray Compromises 78 Microsoft Accounts in 81M+ Attempts
- **Source:** The Hacker News — https://thehackernews.com/2026/07/azure-cli-password-spray-hits-at-least.html
- **Severity:** high
- **Tags:** `azure`, `microsoft`, `iam`
- **Summary:** Huntress identified an ongoing password spray campaign against Azure CLI from an IPv6 range tied to LSHIY LLC, generating 81M+ login attempts and compromising at least 78 accounts between June 12–26.

### 4. Google Patches 382 Chrome Vulnerabilities, 15 Rated Critical
- **Source:** SecurityWeek — https://www.securityweek.com/google-patches-382-chrome-vulnerabilities/
- **Severity:** high
- **Tags:** `google`, `vulnerability`
- **Summary:** Google shipped patches for 382 Chrome vulnerabilities, 15 rated critical and 67 rated high severity. No active exploitation was disclosed.

### 5. Researcher Analysis of 3,000 ClickFix Payloads Reveals API-Driven Malware Delivery
- **Source:** The Hacker News — https://thehackernews.com/2026/07/researcher-analyzes-3000-live-clickfix.html
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Summary:** Analysis of ~3,000 live ClickFix payloads found the fake "prove you're human" pages are now backed by API-driven infrastructure, plus a new delivery method built to evade Windows script scanning.

### 6. Citrix Patches Six NetScaler Flaws Including CVE-2026-8451
- **Source:** The Hacker News — https://thehackernews.com/2026/07/citrix-patches-six-netscaler-flaws.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Summary:** Citrix patched six flaws in NetScaler ADC and Gateway enabling arbitrary file reads or denial-of-service. The most severe, CVE-2026-8451 (CVSS 8.8), is an insufficient input validation issue.

### 7. Phantom Squatting: AI-Hallucinated Domains Weaponized as Supply Chain Vector
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/phantom-squatting-hallucinated-web-domains/
- **Severity:** medium
- **Tags:** `supply-chain`, `llm`, `ai-safety`
- **Summary:** Unit 42 documented "phantom squatting," where attackers register nonexistent domains that LLMs hallucinate and host phishing/malware there — already observed in the wild.

### 8. China-Linked Group Deploys New Backdoor Against Southeast Asia Critical Systems
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/china-linked-group-targets-southeast-asia-critical-systems
- **Severity:** high
- **Tags:** `malware`, `apt`
- **Summary:** A China-linked group compromised at least 10 organizations across Southeast Asia, including two state-owned entities, deploying a new backdoor.

### 9. Anthropic Restores Claude Fable 5 After Export Controls Lifted
- **Source:** The Hacker News — https://thehackernews.com/2026/07/anthropic-restores-claude-fable-5-after.html
- **Severity:** medium
- **Tags:** `anthropic`, `llm`, `ai-safety`
- **Summary:** The U.S. Commerce Department lifted jailbreak-linked export controls on Claude Fable 5 and Mythos 5. Fable 5 returns worldwide July 1 across Claude.ai, the Claude Platform, Claude Code, and Claude Cowork.

### 10. Anthropic Launches Claude Sonnet 5 With Near-Opus 4.8 Performance
- **Source:** Simon Willison — https://simonwillison.net/2026/Jun/30/claude-sonnet-5/#atom-everything
- **Severity:** medium
- **Tags:** `anthropic`, `model-release`, `llm`, `ai-safety`
- **Summary:** Anthropic released Claude Sonnet 5, positioned near Opus 4.8 performance at a lower price. Its system card states Sonnet 5 is significantly less capable at cyber-offensive tasks than Mythos 5, letting it ship with lighter safeguards.

### 11. Google Ships Nano Banana 2 Lite, a Faster Gemini Image Model
- **Source:** Simon Willison — https://simonwillison.net/2026/Jun/30/nano-banana-2-lite/#atom-everything
- **Severity:** informational
- **Tags:** `google`, `model-release`, `llm`
- **Summary:** Google released Nano Banana 2 Lite (Gemini 3.1 Flash Lite Image), billed as its fastest and cheapest Gemini image model.

### 12. OpenClaw Agentic App Launches on Android and iOS
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/30/openclaw-is-finally-available-on-android-and-ios/
- **Severity:** informational
- **Tags:** `ai-launch`, `llm`
- **Summary:** OpenClaw, a free open-source agentic program, is now available on Android and iOS.

### 13. BioShocking Attack Tricks AI Browsers Into Data Theft via Fictional Framing
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-bioshocking-attack-manipulates-ai-browser-into-data-theft/
- **Severity:** high
- **Tags:** `ai-safety`, `llm`, `prompt-injection`
- **Summary:** "BioShocking" is a prompt injection attack that manipulates AI-powered browsers into treating risky real-world actions as part of a fictional scenario, bypassing safety guardrails and enabling data theft.

### 14. Agentjacking: Fake Bug Reports Hijack AI Coding Agents at Scale
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/fake-bug-report-hijacks-ai-coding-agents
- **Severity:** high
- **Tags:** `ai-safety`, `llm`, `prompt-injection`
- **Summary:** "Agentjacking" uses fake bug reports to hijack AI coding agents at scale, exploiting agents' inability to distinguish untrusted content from legitimate instructions.

### 15. Malicious PyPI Packages Give Attackers Control of Telegram Bot Servers
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/malicious-pypi-packages-give-hackers-control-of-telegram-bot-servers/
- **Severity:** high
- **Tags:** `supply-chain`, `pypi`, `malware`
- **Summary:** A campaign active since last November has targeted Python developers building Telegram bots with trojanized Pyrogram forks on PyPI, giving attackers arbitrary file read access on compromised servers.

### 16. Attackers Hijack Exposed AI Endpoints to Power Offensive Operations
- **Source:** Dark Reading — https://www.darkreading.com/cloud-security/attackers-hijack-exposed-ai-endpoints-power-offensive-ops
- **Severity:** high
- **Tags:** `ai-safety`, `llm`, `cloud-security`
- **Summary:** Attackers are hijacking exposed AI endpoints to power offensive operations, exploiting the fact that many require no special authentication to reach.

## Skippable

- **Martin Lee: Running through the Arctic (and the threat landscape)** — Cisco Talos. Personnel profile/interview piece, no technical content.
- **Frontier AI: Six Questions Every Enterprise Should Ask Security Vendors** — SecurityWeek. Generic vendor-evaluation advice, no news value.
- **Amazon fined $2.25M for withholding evidence from fraud victims** — BleepingComputer. Regulatory/legal fine, not a technical security incident.
- **Apple Patches Dozens of Vulnerabilities Across iOS, macOS, and Safari** — SecurityWeek. Routine patch release; no critical actively-exploited CVE specified.
- **Dawnguard Raises $6.3 Million for Security Architecture Automation Platform** — SecurityWeek. Funding/marketing news, no security substance.
- **Massive Password Spray Campaign Targeting Azure CLI** — SecurityWeek. Duplicate coverage; The Hacker News version has more technical detail.
- **Phantom Squatting Uses AI-Hallucinated Domains for Phishing and Malware** — The Hacker News. Duplicate of Unit 42's original research.
- **The 'Father of the Internet' is finally retiring** — TechCrunch AI. Personnel/human-interest piece, no security or model-launch content.
- **Trump drops restrictions on Anthropic's Mythos and Fable models** — TechCrunch AI. Duplicate coverage of the Fable 5 restoration story.
- **Wayve launches $85M employee tender offer at $8.5B valuation** — TechCrunch AI. Startup financing news, no security angle.
- **Anthropic to restore Claude Fable access on Wednesday** — BleepingComputer. Duplicate coverage of Fable 5 restoration.
- **Anthropic's long-sidelined Fable 5 is greenlit to return** — The Verge AI. Duplicate coverage of Fable 5 restoration.
- **Quoting Anthropic** — Simon Willison. Short duplicate quote of the Fable 5 restoration announcement.
- **Anthropic rolls out Sonnet 5 with near-Opus 4.8 performance at a lower price** — BleepingComputer. Duplicate coverage; Simon Willison's post has more technical detail on the system card.
- **Accelerate your infrastructure deployments by up to 4x with AWS CloudFormation Express mode** — AWS News Blog. Generic cloud ops feature, no security angle.
- **Microsoft accelerates quantum-safe roadmap as risks grow** — BleepingComputer. Vague strategic roadmap announcement with no specific timeline or technical detail.
- **Amazon EC2 C9g and C9gd instances powered by AWS Graviton5 processors are now available** — AWS News Blog. Generic compute infrastructure launch, no security angle.
