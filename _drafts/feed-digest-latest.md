# Digest — 2026-05-29 PM

- Window: last 14h
- Raw items considered: 42
- Relevant: 19
- Skippable: 23

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Threat Actors Abuse ChatGPT Share Links to Serve Malware as Fake Desktop App — `2026-05-29-chatgpt-share-links-malware.md`
- [x] **[HIGH]** ChatGPhish: ChatGPT's Trust in Markdown Enables Prompt Injection and Phishing — `2026-05-29-chatgphish-prompt-injection-phishing.md`
- [x] **[HIGH]** Attackers Deploy LLM Agent for Post-Exploitation After Marimo RCE (CVE-2026-39987) — `2026-05-29-llm-agent-post-exploitation-marimo-cve-2026-39987.md`
- [x] **[HIGH]** Dutch Authorities Dismantle Botnet of 17 Million Infected Devices, Seize 200+ Servers — `2026-05-29-dutch-botnet-takedown-17-million-devices.md`
- [x] **[HIGH]** Unpatched Gogs Zero-Day (CVSS 9.4) Enables Remote Code Execution via Pull Requests — `2026-05-29-gogs-zero-day-rce-cvss-9-4.md`
- [x] **[HIGH]** GREYVIBE: New Russian-Aligned Threat Actor Targets Ukraine with AI-Powered Attacks — `2026-05-29-greyvibe-russian-ai-cyberattacks-ukraine.md`
- [x] **[HIGH]** Malicious Sicoob NuGet Package Steals Banking Credentials; npm Packages Target Cloud Secrets — `2026-05-29-sicoob-nuget-npm-supply-chain-attack.md`
- [x] **[HIGH]** ShinyHunters Breach Exposes 4.9 Million Charter Communications Accounts — `2026-05-29-charter-communications-breach-shinyhunters.md`
- [x] **[HIGH]** Kimsuky Deploys HTTPSpy and HelloDoor Malware, Abuses VS Code Tunnels for C2 — `2026-05-29-kimsuky-httpspy-hellodoor-vscode-tunnels.md`
- [x] **[MEDIUM]** California AG Sues 23andMe Over Failure to Protect Genetic Data in 2023 Breach — `2026-05-29-california-sues-23andme-genetic-data-breach.md`
- [x] **[MEDIUM]** Google Releases Gemini Omni and Gemini 3.5 at I/O 2026 — `2026-05-29-gemini-omni-3-5-launch.md`
- [x] **[MEDIUM]** Week in Brief: Trump Mobile Data Breach, FIFA 2026 Phishing, CISA on Supply Chain Attacks — `2026-05-29-trump-mobile-breach-fifa-phishing-cisa-supply-chain.md`
- [x] **[MEDIUM]** DDoS-as-a-Service: $5 Attacks to Botnet-Powered Subscription Platforms — `2026-05-29-ddos-as-a-service-market-evolution.md`
- [x] **[MEDIUM]** Microsoft Calls Zero-Day Releases 'Never Justifiable' as Researcher Threatens More PoCs — `2026-05-29-microsoft-zero-day-disclosure-policy.md`
- [x] **[MEDIUM]** Google Rolls Out Device Bound Session Credentials in Chrome to All Users — `2026-05-29-chrome-dbsc-session-cookie-protection.md`
- [x] **[MEDIUM]** North Carolina Man Sentenced to Over 10 Years for Selling Personal Data of 7M Elderly Americans — `2026-05-29-man-sentenced-selling-7m-elderly-data.md`
- [x] **[MEDIUM]** 2,000 Exposed Vibe-Coded Apps Reveal Shadow AI Risk in Production Environments — `2026-05-29-vibe-coded-apps-security-risks.md`
- [x] **[MEDIUM]** Chrome 148 Patches 151 Vulnerabilities Including Critical-Severity RCE Bugs — `2026-05-29-chrome-148-patches-151-vulnerabilities.md`
- [x] **[MEDIUM]** US Charges Google Security Engineer with Using Confidential Data for Polymarket Insider Trading — `2026-05-29-google-engineer-polymarket-insider-trading.md`

## Relevant (details)

### 1. Threat Actors Abuse ChatGPT Share Links to Serve Malware as Fake Desktop App
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/chatgpt-share-links-abused-to-host-fake-outage-pages-to-deliver-malware/
- **Severity:** high
- **Tags:** `malware`, `phishing`, `openai`, `llm`
- **Summary:** Attackers are hosting fake OpenAI outage pages through legitimate chatgpt.com share URLs, luring users into downloading malware disguised as the ChatGPT desktop app. The use of real chatgpt.com domains makes these links harder for security tools to block on reputation alone.

### 2. ChatGPhish: ChatGPT's Trust in Markdown Enables Prompt Injection and Phishing
- **Source:** The Hacker News — https://thehackernews.com/2026/05/chatgphish-vulnerability-turns-chatgpt.html
- **Severity:** high
- **Tags:** `phishing`, `llm`, `vulnerability`, `openai`, `appsec`
- **Summary:** Permiso Security disclosed ChatGPhish: the ChatGPT web renderer trusts Markdown from summarized pages, enabling attacker-controlled sites to inject malicious links that appear inside chatgpt.com responses. This is an indirect prompt injection attack that bypasses user trust by embedding phishing within ChatGPT's own interface.

### 3. Attackers Deploy LLM Agent for Post-Exploitation After Marimo RCE (CVE-2026-39987)
- **Source:** The Hacker News — https://thehackernews.com/2026/05/attackers-use-llm-agent-for-post.html
- **Severity:** high
- **Tags:** `llm`, `rce`, `cve`, `vulnerability`, `cloud-security`
- **Summary:** After exploiting CVE-2026-39987 in a public Marimo notebook, an unknown threat actor deployed an LLM agent to autonomously conduct post-exploitation — extracting cloud credentials without manual intervention. This is among the first documented cases of AI-automated lateral movement in a real attack chain.

### 4. Dutch Authorities Dismantle Botnet of 17 Million Infected Devices, Seize 200+ Servers
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/dutch-govt-disrupts-malware-botnet-with-17-million-infected-devices/
- **Severity:** high
- **Tags:** `malware`, `botnet`
- **Summary:** Dutch law enforcement seized 200+ servers and dismantled a 17-million-device botnet hosted at a local provider. Malware family and attribution details were not immediately available; IOCs are expected as the investigation proceeds.

### 5. Unpatched Gogs Zero-Day (CVSS 9.4) Enables Remote Code Execution via Pull Requests
- **Source:** SecurityWeek — https://www.securityweek.com/gogs-zero-day-exposes-servers-to-remote-code-execution/
- **Severity:** high
- **Tags:** `zero-day`, `rce`, `vulnerability`, `appsec`
- **Summary:** A CVSS 9.4 argument injection flaw in Gogs (self-hosted Git) allows authenticated users to achieve RCE by submitting pull requests with malicious branch names. No patch is available; administrators should restrict pull request access and isolate Gogs instances immediately.

### 6. GREYVIBE: New Russian-Aligned Threat Actor Targets Ukraine with AI-Powered Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/05/new-russian-linked-greyvibe-targets.html
- **Severity:** high
- **Tags:** `malware`, `llm`, `phishing`
- **Summary:** WithSecure attributed GREYVIBE — a previously unknown Russian-speaking APT — to persistent attacks on Ukraine since August 2025, incorporating AI-powered capabilities and spoofed software installer lures. Activity aligns with Kremlin interests.

### 7. Malicious Sicoob NuGet Package Steals Banking Credentials; npm Packages Target Cloud Secrets
- **Source:** The Hacker News — https://thehackernews.com/2026/05/malicious-sicoob-nuget-steals-banking.html
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `npm`
- **Summary:** Socket found malicious versions (2.0.0–2.0.4) of `Sicoob.Sdk` NuGet package exfiltrating PFX certificates and client IDs from Brazilian banking environments. Separately, npm packages in a concurrent campaign are harvesting cloud secrets from developer environments.

### 8. ShinyHunters Breach Exposes 4.9 Million Charter Communications Accounts
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/charter-communications-data-breach-affects-49-million-accounts/
- **Severity:** high
- **Tags:** `data-breach`, `ransomware`
- **Summary:** ShinyHunters stole personal data from 4.9 million Charter Communications (Spectrum) accounts in an April breach, confirmed via HIBP. SecurityWeek noted 42 million total leaked records, suggesting the dataset extends beyond account records.

### 9. Kimsuky Deploys HTTPSpy and HelloDoor Malware, Abuses VS Code Tunnels for C2
- **Source:** The Hacker News — https://thehackernews.com/2026/05/kimsuky-deploys-httpspy-expands-arsenal.html
- **Severity:** high
- **Tags:** `malware`, `phishing`, `microsoft`
- **Summary:** Kimsuky (North Korean APT) ran a March–April 2026 campaign against South Korean targets using new tools HTTPSpy and HelloDoor, routing C2 through VS Code remote tunneling to blend with legitimate developer traffic. Lures included spoofed security software and fake Webex meetings.

### 10. California AG Sues 23andMe Over Failure to Protect Genetic Data in 2023 Breach
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/california-ag-sues-23andme-over-2023-breach-exposing-health-data/
- **Severity:** medium
- **Tags:** `data-breach`
- **Summary:** California AG sued Chrome Holding Co. (formerly 23andMe) over the 2023 breach of genetic and health data, alleging inadequate security controls. The case pursues post-bankruptcy liability for a pre-bankruptcy security failure.

### 11. Google Releases Gemini Omni and Gemini 3.5 at I/O 2026
- **Source:** Google AI Blog — https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-3-5-videos/
- **Severity:** medium
- **Tags:** `model-release`, `google`, `ai-launch`
- **Summary:** Google debuted Gemini Omni and Gemini 3.5 at I/O 2026, with nine demo videos published. Gemini Omni extends multimodal handling; Gemini 3.5 targets reasoning improvements; no security evaluation details were included.

### 12. Week in Brief: Trump Mobile Data Breach, FIFA 2026 Phishing, CISA on Supply Chain Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/in-other-news-trump-mobile-data-breach-fifa-world-cup-phishing-cisa-responds-to-supply-chain-attacks/
- **Severity:** medium
- **Tags:** `data-breach`, `phishing`, `supply-chain`
- **Summary:** Three-item roundup: Trump Mobile customer data exposed, FIFA World Cup 2026 phishing campaigns targeting fans, and a CISA statement on recent supply chain attacks. Technical details limited in the summary.

### 13. DDoS-as-a-Service: $5 Attacks to Botnet-Powered Subscription Platforms
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/from-5-attacks-to-botnet-powered-platforms-inside-the-ddos-as-a-service-market/
- **Severity:** medium
- **Tags:** `malware`, `ddos`
- **Summary:** Flare research maps the DDoS-for-hire market from $5 entry-level attacks to subscription tiers with botnet-backed capacity, support desks, and resellers. Commoditization mirrors the RaaS model and eliminates the skill barrier for volumetric attacks.

### 14. Microsoft Calls Zero-Day Releases 'Never Justifiable' as Researcher Threatens More PoCs
- **Source:** The Record (Recorded Future) — https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more
- **Severity:** medium
- **Tags:** `zero-day`, `microsoft`, `vulnerability`
- **Summary:** A researcher published working PoC exploit code for multiple Microsoft vulnerabilities to GitHub; Microsoft called such releases "never justifiable." The researcher has threatened additional disclosures, making patching of affected products urgent.

### 15. Google Rolls Out Device Bound Session Credentials in Chrome to All Users
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/google-chrome-adds-session-cookie-theft-protection-for-all-users/
- **Severity:** medium
- **Tags:** `google`, `appsec`
- **Summary:** Chrome's DBSC feature is now GA, cryptographically binding session tokens to the originating device so stolen cookies are useless without the device's private key. Directly counters infostealer-driven account takeover that bypasses MFA via cookie replay.

### 16. North Carolina Man Sentenced to Over 10 Years for Selling Personal Data of 7M Elderly Americans
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/man-sent-to-prison-for-selling-data-of-7-millions-elderly-americans/
- **Severity:** medium
- **Tags:** `data-breach`, `phishing`
- **Summary:** A man received 10+ years in federal prison for compiling and selling personal data on 7 million elderly Americans to Jamaican fraud rings for phone scams. Establishes significant criminal liability for data brokers enabling downstream fraud.

### 17. 2,000 Exposed Vibe-Coded Apps Reveal Shadow AI Risk in Production Environments
- **Source:** The Hacker News — https://thehackernews.com/2026/05/what-2000-exposed-vibe-coded-apps.html
- **Severity:** medium
- **Tags:** `llm`, `appsec`, `ai-safety`
- **Summary:** Analysis of 2,000+ AI-generated apps found employees routinely building and deploying production tools with AI coding assistants — exposing secrets, skipping auth, and wiring them to internal systems without IT or security review. Shadow AI has grown from chat leakage to deployed attack surface.

### 18. Chrome 148 Patches 151 Vulnerabilities Including Critical-Severity RCE Bugs
- **Source:** SecurityWeek — https://www.securityweek.com/chrome-148-update-patches-151-vulnerabilities/
- **Severity:** medium
- **Tags:** `google`, `vulnerability`, `rce`, `cve`
- **Summary:** Chrome 148 patches 151 vulnerabilities including critical-severity RCE issues; none reported as actively exploited at time of release. Prompt enterprise deployment is warranted given the critical-severity classification.

### 19. US Charges Google Security Engineer with Using Confidential Data for Polymarket Insider Trading
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/us-charges-google-security-engineer-with-polymarket-insider-trading/
- **Severity:** medium
- **Tags:** `google`, `data-breach`, `insider-threat`
- **Summary:** A Google security engineer is federally charged for using non-public company data to win $1.2M on the Polymarket crypto prediction market. A novel insider threat pattern: privileged access exploited for financial gain via a decentralized venue.

## Skippable

- **Take our I/O 2026 quiz, vibe coded in Google AI Studio** — Google AI Blog. Promotional quiz marketing content for I/O 2026, no news value.
- **So you've heard these AI terms and nodded along** — TechCrunch AI. Evergreen AI glossary explainer, not news.
- **What happens when companies become too AI-pilled?** — TechCrunch AI. Opinion interview (Aaron Levie), no hard news.
- **Tech companies desperately want to film you doing chores** — The Verge AI. AI training data story, no security angle; duplicated by item #31.
- **After Nvidia's $20B not-aqui-hire, AI chip startup Groq reportedly raising $650M** — TechCrunch AI. VC funding news, no security angle.
- **Cognition's Scott Wu says AI coding agents shouldn't replace humans** — TechCrunch AI. Opinion interview, no hard news.
- **Cloud CISO Perspectives: How to build an AI-ready security program for the public sector** — Google Cloud Security. Vendor marketing advisory from Google.
- **Charter Communications Data Breach Could Impact Nearly 5 Million** — SecurityWeek. Duplicate of the Charter/ShinyHunters breach; BleepingComputer selected as primary.
- **The Good, the Bad and the Ugly in Cybersecurity – Week 22** — SentinelOne Labs. Weekly roundup format; individual items covered elsewhere or lack technical depth.
- **MokN Raises $15 Million for Phish-Back Platform** — SecurityWeek. VC funding/product launch announcement.
- **Today is the last day to apply to speak at TechCrunch Disrupt 2026** — TechCrunch AI. Event speaker recruitment promo.
- **Final 24 hours to save up to $410 on your TechCrunch Disrupt 2026 ticket** — TechCrunch AI. Event ticket advertising.
- **How to Align and Measure Threat Intelligence Operations: Flashpoint Priority Intelligence Requirements** — Flashpoint. Product marketing for Flashpoint Ignite.
- **Kiwibit's AI-powered bird feeder is my new backyard buddy** — TechCrunch AI. Consumer gadget review, no security angle.
- **Jony Ive's funky Ferrari** — The Verge AI. Car design/podcast, off-topic.
- **Boston Children's uses AI to unlock new diagnoses** — OpenAI Blog. Healthcare AI case study, no security angle.
- **How Braintrust turns customer requests into code with Codex** — OpenAI Blog. Product customer story, no security angle.
- **Check out real-life AI prototypes from the Futures Lab** — Google AI Blog. University student project showcase, no news value.
- **This chip startup just raised $135M on a bet that AI's biggest bottleneck isn't compute — it's memory** — TechCrunch AI. AI chip startup funding, no security angle.
- **This AI startup will clean your home for free to train future robots** — The Verge AI. Duplicate of the filming-chores story (Shift startup, different outlet).
- **California Sues 23andMe, Alleging It Failed to Protect User Data in 2023 Breach** — SecurityWeek. Duplicate of BleepingComputer 23andMe lawsuit story; BleepingComputer selected as primary.
- **Adobe's conversational AI agent is a mediocre design intern** — The Verge AI. Product review, no security angle.
- **What's in the container? Analyzing vulnerabilities, risks and protection with Kaspersky Container Security** — Securelist. Kaspersky product marketing in educational framing.
