# Digest — 2026-07-01 PM

- Window: last 14h
- Raw items considered: 51
- Relevant: 19
- Skippable: 32

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Progress Kemp LoadMaster Pre-Auth RCE Under Active Exploitation — `2026-07-01-progress-kemp-loadmaster-rce-exploited.md`
- [x] **[CRITICAL]** Over 900 Oracle E-Business Suite Instances Exposed to Active Attacks — `2026-07-01-oracle-ebs-instances-exposed-attacks.md`
- [x] **[HIGH]** Critical Cursor Flaws Let Prompt Injection Escape Sandbox — `2026-07-01-cursor-duneslide-prompt-injection-sandbox-escape.md`
- [x] **[HIGH]** AI-Generated Browser Ransomware Abuses Chromium API — `2026-07-01-ai-generated-browser-ransomware-deepseek.md`
- [x] **[HIGH]** Citrix Patches NetScaler Flaws Including New HTTP/2 Bomb Attack — `2026-07-01-citrix-netscaler-http2-bomb.md`
- [x] **[HIGH]** Adobe Patches 7 CVSS 10.0 Flaws in ColdFusion and Campaign Classic — `2026-07-01-adobe-coldfusion-campaign-classic-cvss10.md`
- [x] **[HIGH]** Google Patches 382 Chrome Vulnerabilities — `2026-07-01-google-chrome-382-vulnerabilities-patched.md`
- [x] **[HIGH]** Azure CLI Password Spray Campaign Tops 81 Million Login Attempts — `2026-07-01-azure-cli-password-spray-81-million.md`
- [x] **[HIGH]** DHS Confirms Hackers Breached HSIN Info-Sharing Platform — `2026-07-01-dhs-hsin-breach.md`
- [x] **[MEDIUM]** Large-Scale Campaign Masks AsyncRAT as ScreenConnect Freeware — `2026-07-01-screenconnect-asyncrat-campaign.md`
- [x] **[MEDIUM]** ARToken Phishing-as-a-Service Panel Targets Microsoft 365 — `2026-07-01-artoken-eviltokens-m365-phishing.md`
- [x] **[MEDIUM]** Phantom Squatting Uses AI-Hallucinated Domains for Phishing — `2026-07-01-phantom-squatting-ai-hallucinated-domains.md`
- [x] **[MEDIUM]** OpenClaw: Security Risks in the Popular AI Agent — `2026-07-01-openclaw-agent-security-risks.md`
- [x] **[MEDIUM]** VEIL#DROP Malware Chain Uses Blogger Platform to Deliver PureLogs Stealer — `2026-07-01-veildrop-purelogs-stealer.md`
- [x] **[MEDIUM]** Ousaban Banking Trojan Targets Iberian Bank Users — `2026-07-01-ousaban-banking-trojan-iberia.md`
- [x] **[MEDIUM]** Researcher Analyzes 3,000 Live ClickFix Payloads — `2026-07-01-clickfix-api-driven-malware-delivery.md`
- [x] **[MEDIUM]** Anthropic Restores Claude Fable 5 After Export Controls Lifted — `2026-07-01-anthropic-restores-claude-fable-5.md`
- [x] **[INFORMATIONAL]** AWS Workload Credentials Provider Adds Cross-Account Secret Retrieval — `2026-07-01-aws-workload-credentials-cross-account-secrets.md`
- [x] **[INFORMATIONAL]** Microsoft Accelerates Post-Quantum Cryptography Shift to 2029 — `2026-07-01-microsoft-post-quantum-cryptography-2029.md`

## Relevant (details)

### 1. Progress Kemp LoadMaster Pre-Auth RCE Under Active Exploitation
- **Source:** The Hacker News — https://thehackernews.com/2026/07/latest-progress-kemp-loadmaster-pre.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `progress-kemp-loadmaster-rce-exploited`
- **Must-know:** no
- **Summary:** eSentire's TRU observed active exploitation attempts against CVE-2026-8037 (CVSS 9.6), a pre-auth OS command injection flaw in Progress Kemp LoadMaster. No credentials are required to attempt exploitation against exposed instances.

### 2. Over 900 Oracle E-Business Suite Instances Exposed to Active Attacks
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/over-900-oracle-e-business-instances-exposed-to-ongoing-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `oracle-ebs-instances-exposed-attacks`
- **Must-know:** no
- **Summary:** More than 900 internet-exposed Oracle E-Business Suite instances have been found under ongoing attack exploiting a critical flaw. EBS handles core ERP functions for large enterprises, making exposure high-impact.

### 3. Critical Cursor Flaws Let Prompt Injection Escape Sandbox
- **Source:** The Hacker News — https://thehackernews.com/2026/07/critical-cursor-flaws-could-let-prompt.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `rce`, `cve`, `ai-safety`
- **Slug:** `cursor-duneslide-prompt-injection-sandbox-escape`
- **Must-know:** no
- **Summary:** Cato AI Labs found two flaws (CVE-2026-50548, CVE-2026-50549, DuneSlide) in the Cursor AI code editor that let a single crafted prompt escape the sandbox and run arbitrary commands, with no click required.

### 4. AI-Generated Browser Ransomware Abuses Chromium API
- **Source:** The Hacker News — https://thehackernews.com/2026/07/ai-generated-browser-ransomware-abuses.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`, `malware`, `deepseek`, `ai-safety`
- **Slug:** `ai-generated-browser-ransomware-deepseek`
- **Must-know:** no
- **Summary:** Researchers documented what they call the first case of a frontier model (DeepSeek) generating a working, cross-platform browser ransomware technique by combining a hallucinated malware concept with a real Chromium API.

### 5. Citrix Patches NetScaler Flaws Including New HTTP/2 Bomb Attack
- **Source:** SecurityWeek — https://www.securityweek.com/citrix-patches-netscaler-vulnerabilities-including-new-http-2-bomb-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Slug:** `citrix-netscaler-http2-bomb`
- **Must-know:** no
- **Summary:** Citrix patched six NetScaler vulnerabilities, including a new DoS flaw dubbed the "HTTP/2 Bomb" and a high-severity, CitrixBleed-style information disclosure bug. No active exploitation reported yet.

### 6. Adobe Patches 7 CVSS 10.0 Flaws in ColdFusion and Campaign Classic
- **Source:** The Hacker News — https://thehackernews.com/2026/07/adobe-patches-7-cvss-100-flaws-in.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `adobe-coldfusion-campaign-classic-cvss10`
- **Must-know:** no
- **Summary:** Adobe patched seven maximum-severity flaws in ColdFusion and Campaign Classic that could lead to arbitrary code execution, privilege escalation, file system read, and security feature bypass. Also reported by SecurityWeek and BleepingComputer.

### 7. Google Patches 382 Chrome Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/google-patches-382-chrome-vulnerabilities/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `google`
- **Slug:** `google-chrome-382-vulnerabilities-patched`
- **Must-know:** no
- **Summary:** Google shipped fixes for 382 Chrome vulnerabilities, 15 rated critical and 67 rated high. An unusually large batch even for a routine Chrome cycle; no active exploitation reported.

### 8. Azure CLI Password Spray Campaign Tops 81 Million Login Attempts
- **Source:** The Hacker News — https://thehackernews.com/2026/07/azure-cli-password-spray-hits-at-least.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `azure`, `cloud-security`, `iam`
- **Slug:** `azure-cli-password-spray-81-million`
- **Must-know:** no
- **Summary:** Huntress reports an automated password-spray campaign against Azure CLI generating 81M+ login attempts between June 12–26 from an LSHIY LLC-controlled IPv6 range, compromising at least 78 accounts. Also reported by BleepingComputer and SecurityWeek.

### 9. DHS Confirms Hackers Breached HSIN Info-Sharing Platform
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/dhs-confirms-hackers-breached-hsin-info-sharing-platform/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `dhs-hsin-breach`
- **Must-know:** no
- **Summary:** DHS is investigating a breach of the Homeland Security Information Network, a sensitive info-sharing platform used by federal, state, local, and private-sector partners. Entry vector and data accessed not yet disclosed.

### 10. Large-Scale Campaign Masks AsyncRAT as ScreenConnect Freeware
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/tr/the-soc-files-screenconnect-campaign-with-asyncrat/120472/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Slug:** `screenconnect-asyncrat-campaign`
- **Must-know:** no
- **Summary:** Kaspersky mapped a large-scale campaign delivering AsyncRAT via fake ScreenConnect installers, part of a multi-domain, multi-language operation also distributing malware disguised as OBS Studio, DNS Jumper, DS4Windows, and Bandicam.

### 11. ARToken Phishing-as-a-Service Panel Targets Microsoft 365
- **Source:** Cisco Talos — https://blog.talosintelligence.com/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `phishing`, `malware`, `microsoft`
- **Slug:** `artoken-eviltokens-m365-phishing`
- **Must-know:** no
- **Summary:** Talos identified ARToken, an EvilTokens affiliate PhaaS panel with 80+ API endpoints supporting device-code phishing, Primary Refresh Token persistence, email access, BEC, and SharePoint exfiltration against Microsoft 365.

### 12. Phantom Squatting Uses AI-Hallucinated Domains for Phishing
- **Source:** The Hacker News — https://thehackernews.com/2026/07/phantom-squatting-uses-ai-hallucinated.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `llm`, `ai-safety`
- **Slug:** `phantom-squatting-ai-hallucinated-domains`
- **Must-know:** no
- **Summary:** Unit 42 documented "phantom squatting" — attackers registering domains that LLMs hallucinate for legitimate brands, then hosting phishing pages to catch AI-directed traffic. Also reported by Dark Reading.

### 13. OpenClaw: Security Risks in the Popular AI Agent
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/openclaw-security/120484/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `llm`, `ai-safety`, `vulnerability`
- **Slug:** `openclaw-agent-security-risks`
- **Must-know:** no
- **Summary:** Kaspersky researched vulnerabilities and malicious skills affecting the popular OpenClaw AI agent and published mitigation guidance. Specific vulnerability details were not included in the summary.

### 14. VEIL#DROP Malware Chain Uses Blogger Platform to Deliver PureLogs Stealer
- **Source:** The Hacker News — https://thehackernews.com/2026/07/veildrop-malware-chain-uses-blogger.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Slug:** `veildrop-purelogs-stealer`
- **Must-know:** no
- **Summary:** Securonix identified VEIL#DROP, a multi-stage malware chain using Blogger pages to deliver the PureLogs stealer, suspected to start via spear-phishing or drive-by compromise.

### 15. Ousaban Banking Trojan Targets Iberian Bank Users
- **Source:** The Hacker News — https://thehackernews.com/2026/07/ousaban-banking-trojan-targets-iberian.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Slug:** `ousaban-banking-trojan-iberia`
- **Must-know:** no
- **Summary:** Fortinet identified an Ousaban banking trojan campaign against Windows users in Spain and Portugal, using a phishing PDF lure and image steganography to hide the payload and steal banking credentials.

### 16. Researcher Analyzes 3,000 Live ClickFix Payloads
- **Source:** The Hacker News — https://thehackernews.com/2026/07/researcher-analyzes-3000-live-clickfix.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Slug:** `clickfix-api-driven-malware-delivery`
- **Must-know:** no
- **Summary:** New research on ~3,000 live ClickFix payloads found the fake "prove you're human" pages are now served by API-driven backend infrastructure, plus a new delivery method built to evade Windows script scanning.

### 17. Anthropic Restores Claude Fable 5 After Export Controls Lifted
- **Source:** The Hacker News — https://thehackernews.com/2026/07/anthropic-restores-claude-fable-5-after.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `anthropic`, `ai-safety`
- **Slug:** `anthropic-restores-claude-fable-5`
- **Must-know:** no
- **Summary:** Anthropic restored global access to Claude Fable 5 after the U.S. Commerce Department lifted jailbreak-linked export controls placed on Fable and Mythos 5 about two and a half weeks earlier. Also reported by The Record.

### 18. AWS Workload Credentials Provider Adds Cross-Account Secret Retrieval
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/how-to-use-the-aws-workload-credentials-provider-for-cross-account-secret-retrieval-and-prefetching-secrets/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `aws`, `iam`, `cloud-security`
- **Slug:** `aws-workload-credentials-cross-account-secrets`
- **Must-know:** no
- **Summary:** AWS added role chaining for cross-account secret retrieval and secret prefetching to its Workload Credentials Provider, aimed at multi-account environments and latency-sensitive applications.

### 19. Microsoft Accelerates Post-Quantum Cryptography Shift to 2029
- **Source:** The Hacker News — https://thehackernews.com/2026/07/microsoft-accelerates-post-quantum.html
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `microsoft`, `cryptography`
- **Slug:** `microsoft-post-quantum-cryptography-2029`
- **Must-know:** no
- **Summary:** Microsoft moved up its post-quantum cryptography migration target to 2029, citing accelerating quantum computing research as shifting the risk horizon sooner than expected.

## Skippable

- **SpaceX has an AI device prototype, and it sure sounds phone-ish** — TechCrunch AI. Business/product rumor, no security or model-substance angle.
- **Ashton Kutcher leaving Sound Ventures to launch new VC firm with Morgan Beller** — TechCrunch AI. VC/personnel news, no security or AI substance.
- **The latest AI news we announced in June 2026** — Google AI Blog. Marketing recap roundup, no new substance.
- **Microsoft Adds New Teams Controls to Block Unauthorized AI Bots From Meetings** — SecurityWeek. Minor admin feature announcement, not an incident or vulnerability.
- **SEO-Poisoned Software Sites Abuse ScreenConnect to Deploy AsyncRAT** — The Hacker News. Duplicate coverage of the Kaspersky ScreenConnect/AsyncRAT campaign; covered via Securelist's original research instead.
- **Cloudflare's new policy pushes AI companies to pay for publishers' content** — TechCrunch AI. Business/licensing policy, no security angle.
- **Upgrade Amazon EKS clusters with confidence using Kubernetes version rollbacks** — AWS News Blog. Generic operational feature, no security implication.
- **Webinar: Why traditional email security is no longer enough** — BleepingComputer. Vendor webinar promotion.
- **Hackers target Microsoft 365 accounts with 81 million login attempts** — BleepingComputer. Duplicate coverage of the Azure CLI password-spray campaign; covered via The Hacker News' more detailed writeup instead.
- **New IDC study: The business value of Mandiant Consulting** — Google Cloud Security. Vendor ROI marketing content.
- **Google Cloud confirmed to offer a safer choice for EU public sector organizations with Dutch DPIA approval** — Google Cloud Security. Compliance marketing announcement, no technical substance.
- **New York City educators and industry leaders gathered at Google's offices to shape the future of AI in classrooms** — Google AI Blog. Education event recap, no security/technical substance.
- **'Phantom Squatting': An Emerging AI-Driven Supply Chain Threat** — Dark Reading. Duplicate coverage; covered via The Hacker News' Unit 42 writeup with more detail instead.
- **Venice AI becomes a unicorn with $65M Series A as its privacy-first AI platform takes off** — TechCrunch AI. Funding news, no security substance.
- **Gemini Spark, Google's agentic assistant, is now available on Mac** — TechCrunch AI. Platform availability expansion, no technical or security substance.
- **Turning Indicators into Intelligence in OpenCTI with Criminal IP** — BleepingComputer. Vendor integration marketing content.
- **Builders Stage agenda revealed: Practical strategies for scaling startups at TechCrunch Disrupt 2026** — TechCrunch AI. Event promotion.
- **Meta, like SpaceX, looks to turn excess AI compute into cash** — TechCrunch AI. Business strategy news, no security substance.
- **US lifts export controls on Anthropic's frontier cybersecurity AI models** — The Record. Duplicate coverage of the Anthropic export-control story; covered via The Hacker News' Claude Fable 5 writeup with more detail instead.
- **Japanese insurer, brewer, manufacturer and telecom disclose cyber breaches** — The Record. Generic breach disclosures without technical substance on method, scope, or IOCs.
- **The Autonomous SOC, Revisited: What 18 Months on the Road Has Taught Us** — SentinelOne Labs. Vendor thought-leadership piece, no news value.
- **Safe Events Start With Threat Intel and Digital Security** — Dark Reading. Opinion piece, no news value.
- **2026 Cybersecurity Assessment: The Gap Between Awareness and Resilience** — The Hacker News. Vendor survey/opinion content.
- **Adobe Patches Critical ColdFusion, Campaign Classic Vulnerabilities** — SecurityWeek. Duplicate coverage of the Adobe ColdFusion/Campaign Classic story; covered via The Hacker News writeup with more technical detail instead.
- **Microsoft fixes GIF functionality in the Windows Emoji Panel** — BleepingComputer. Cosmetic bug fix, no security relevance.
- **Martin Lee: Running through the Arctic (and the threat landscape)** — Cisco Talos. Personal-interest profile piece, no news value.
- **Frontier AI: Six Questions Every Enterprise Should Ask Security Vendors** — SecurityWeek. Advisory/opinion content, no news value.
- **Amazon fined $2.25M for withholding evidence from fraud victims** — BleepingComputer. Regulatory/legal enforcement action, not a security vulnerability or AI story.
- **Apple Patches Dozens of Vulnerabilities Across iOS, macOS, and Safari** — SecurityWeek. Routine patch release with no single flaw flagged as critical or actively exploited.
- **Dawnguard Raises $6.3 Million for Security Architecture Automation Platform** — SecurityWeek. Funding announcement.
- **Massive Password Spray Campaign Targeting Azure CLI** — SecurityWeek. Duplicate coverage of the Azure CLI password-spray campaign; covered via The Hacker News' more detailed writeup instead.
- **Adobe patches seven max severity ColdFusion, Campaign flaws** — BleepingComputer. Duplicate coverage of the Adobe ColdFusion/Campaign Classic story.
