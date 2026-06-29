# Digest — 2026-06-29 PM

- Window: last 14h
- Raw items considered: 47
- Relevant: 10
- Skippable: 37

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Researchers Demonstrate Claude Code Attack That Hijacks Developer Machines via Booby-Trapped Repos — `2026-06-29-claude-code-prompt-injection-reverse-shell.md`
- [x] **[HIGH]** Critical SimpleHelp Flaw (CVE-2026-48558) Exploited to Deploy New Djinn Stealer Malware — `2026-06-29-simplehelp-cve-2026-48558-djinn-stealer.md`
- [x] **[HIGH]** Hackers Exploit Critical Oracle E-Business Suite Flaw (CVE-2026-46817) — `2026-06-29-oracle-ebs-cve-2026-46817-exploited.md`
- [x] **[HIGH]** Insurance Regulator NAIC Confirms Oracle PeopleSoft Breach, ShinyHunters Claims 3.1TB Stolen — `2026-06-29-naic-oracle-peoplesoft-breach-shinyhunters.md`
- [x] **[HIGH]** 236,000 Sites Built on DCloud Uni-App Framework Used in Crypto Scams and Phishing — `2026-06-29-dcloud-uni-app-crypto-scam-sites.md`
- [x] **[HIGH]** Amazon Q VS Code Extension Flaw Enables Cloud Credential Theft — `2026-06-29-amazon-q-vscode-extension-credential-theft.md`
- [x] **[MEDIUM]** Mustang Panda Abuses Zoho WorkDrive as C2 Channel in Indian Government Espionage Campaign — `2026-06-29-mustang-panda-zoho-workdrive-india-espionage.md`
- [x] **[INFORMATIONAL]** Anthropic Strikes Deal With California Gov. Newsom for Half-Price Claude Access — `2026-06-29-anthropic-newsom-california-claude-deal.md`
- [x] **[INFORMATIONAL]** DeepReinforce Releases Ornith-1.0, Open-Weights Coding Model Family — `2026-06-29-deepreinforce-ornith-1-coding-model.md`
- [x] **[INFORMATIONAL]** Lawmakers Plan Bill to Ban AI Companies From Selling Health and Location Data — `2026-06-29-lawmakers-ban-ai-health-location-data-sale.md`

## Relevant (details)

### 1. Researchers Demonstrate Claude Code Attack That Hijacks Developer Machines via Booby-Trapped Repos
- **Source:** SecurityWeek — https://www.securityweek.com/new-attack-abuses-claude-code-and-harmless-looking-repositories-to-hijack-developer-machines/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `rce`, `ai-safety`, `anthropic`
- **Slug:** `claude-code-prompt-injection-reverse-shell`
- **Must-know:** no
- **Summary:** Researchers showed that indirect prompt injection hidden in an apparently harmless repository can cause Claude Code to spawn a reverse shell on the developer's machine, giving an attacker remote access without the developer running anything directly.

### 2. Critical SimpleHelp Flaw (CVE-2026-48558) Exploited to Deploy New Djinn Stealer Malware
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-simplehelp-flaw-deploy-new-djinn-infostealer-taskweaver-malware/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `malware`
- **Slug:** `simplehelp-cve-2026-48558-djinn-stealer`
- **Must-know:** no
- **Summary:** Attackers are exploiting critical CVE-2026-48558 in SimpleHelp remote support software to deploy a new cross-platform infostealer (Djinn Stealer) and a tool called TaskWeaver, targeting Windows, macOS, and Linux.

### 3. Hackers Exploit Critical Oracle E-Business Suite Flaw (CVE-2026-46817)
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-oracle-e-business-suite-flaw-now-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`
- **Slug:** `oracle-ebs-cve-2026-46817-exploited`
- **Must-know:** no
- **Summary:** Threat intel firm Defused reports active exploitation of CVE-2026-46817, a critical flaw in the Oracle E-Business Suite financial application, putting unpatched ERP/financial deployments at risk.

### 4. Insurance Regulator NAIC Confirms Oracle PeopleSoft Breach, ShinyHunters Claims 3.1TB Stolen
- **Source:** SecurityWeek — https://www.securityweek.com/insurance-regulators-group-naic-hit-in-oracle-peoplesoft-hack/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `naic-oracle-peoplesoft-breach-shinyhunters`
- **Must-know:** no
- **Summary:** The National Association of Insurance Commissioners was breached via its Oracle PeopleSoft deployment; the ShinyHunters extortion group claims to have stolen 3.1TB of data from the organization.

### 5. 236,000 Sites Built on DCloud Uni-App Framework Used in Crypto Scams and Phishing
- **Source:** The Hacker News — https://thehackernews.com/2026/06/236000-dcloud-uni-app-sites-used-in.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`
- **Slug:** `dcloud-uni-app-crypto-scam-sites`
- **Must-know:** no
- **Summary:** Infoblox found more than 236,000 sites built on the legitimate DCloud Uni-App framework running investment-scam templates that power fake crypto exchanges, pig-butchering scams, WhatsApp phishing, and brand-impersonation operations.

### 6. Amazon Q VS Code Extension Flaw Enables Cloud Credential Theft
- **Source:** Dark Reading — https://www.darkreading.com/cloud-security/amazon-q-vs-extension-flaw-leads-cloud-credential-theft
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `aws`, `cloud-security`
- **Slug:** `amazon-q-vscode-extension-credential-theft`
- **Must-know:** no
- **Summary:** A flaw in the Amazon Q VS Code extension lets an attacker plant a malicious repository that executes arbitrary code and steals cloud credentials when opened, highlighting growing MCP-related risk in AI coding tools.

### 7. Mustang Panda Abuses Zoho WorkDrive as C2 Channel in Indian Government Espionage Campaign
- **Source:** The Hacker News — https://thehackernews.com/2026/06/mustang-panda-uses-zoho-workdrive-as.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `cloud-security`
- **Slug:** `mustang-panda-zoho-workdrive-india-espionage`
- **Must-know:** no
- **Summary:** China-aligned group Mustang Panda is running campaigns against Indian government and hydropower targets, deploying new malware and using Zoho WorkDrive as a command-and-control channel; Acronis found active compromises in Indian government networks.

### 8. Anthropic Strikes Deal With California Gov. Newsom for Half-Price Claude Access
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/29/anthropic-and-gov-newsom-forge-deal-allowing-california-government-to-use-claude-at-half-price/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `anthropic`, `llm`
- **Slug:** `anthropic-newsom-california-claude-deal`
- **Must-know:** no
- **Summary:** Anthropic and California Gov. Gavin Newsom's office reached a deal letting California state government agencies use Claude at half price, deepening Anthropic's ties with the state.

### 9. DeepReinforce Releases Ornith-1.0, Open-Weights Coding Model Family
- **Source:** Simon Willison — https://simonwillison.net/2026/Jun/29/ornith/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `model-release`, `llm`, `ai-launch`
- **Slug:** `deepreinforce-ornith-1-coding-model`
- **Must-know:** no
- **Summary:** DeepReinforce released Ornith-1.0, an MIT-licensed open-weights model family (9B/31B dense, 35B/397B MoE) built on Gemma 4 and Qwen 3.5, claiming SOTA among open-source models of comparable size on coding benchmarks.

### 10. Lawmakers Plan Bill to Ban AI Companies From Selling Health and Location Data
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/959033/health-location-data-protection-act-ai-warren-scanlon
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `privacy`, `llm`
- **Slug:** `lawmakers-ban-ai-health-location-data-sale`
- **Must-know:** no
- **Summary:** Sen. Warren and Rep. Scanlon plan to introduce an updated Health and Location Data Protection Act barring the sale of health/location data to data brokers, explicitly covering information shared with AI chatbots like ChatGPT or Claude.

## Skippable

- **OpenAI is teasing new hardware for Codex** — The Verge AI. Marketing teaser video for an unreleased device; no real product details yet.
- **Count the number of Safari tabs** — Simon Willison. AppleScript TIL, no AI/security relevance.
- **South Korean tech giants commit over $550B to ease 'RAMageddon'** — TechCrunch AI. Macro chip-investment story, no security or model-launch substance.
- **DiScoFormer: One transformer for density and score, across distributions** — Hugging Face Blog. Niche research paper announcement with no summary detail to report on factually.
- **WhatsApp rolls out usernames to help users hide their phone number** — BleepingComputer / The Hacker News / SecurityWeek (duplicate coverage across 3 sources). Consumer privacy feature rollout, not a vulnerability or attack story.
- **Arena, the AI leaderboard everyone uses, is now a $100M business** — TechCrunch AI. Generic business news, no security or model-launch substance.
- **Microsoft extends Windows Server 2022 hotpatching until October 2027** — BleepingComputer. Lifecycle/support extension announcement, not a vulnerability or attack.
- **US racks up about 400 wins over illegal World Cup streaming sites** — The Record / BleepingComputer (duplicate). Piracy domain takedown, no infosec/AI angle.
- **Cursor now has a mobile app for guiding your coding agent on the go** — TechCrunch AI. Minor product feature, no security substance.
- **AWS Weekly Roundup...** — AWS News Blog. Generic vendor roundup/marketing.
- **TIDAL cracks down on AI music by cutting off monetization** — TechCrunch AI. Content-moderation/business story, no security or AI-safety angle.
- **Cloud CISO Perspectives: How Google Cloud Security uses AI internally** — Google Cloud Security. Newsletter intro with no concrete news event.
- **Ask an AI expert: What exactly is the full stack?** — Google AI Blog. Explainer content, no news value.
- **⚡ Weekly Recap: Linux Kernel Flaws, AI Malware Tricks, Turla Backdoor, Infostealers and More** — The Hacker News. Aggregator roundup of stories already covered individually.
- **Unmasking the Digital Trail: Essential Techniques for Vetting AI-Generated Content** — Flashpoint. Webinar promotion, no concrete news.
- **Straiker Raises $64 Million for AI Security Platform** — SecurityWeek. Funding announcement, no technical substance.
- **Agentic AI Has an Identity Problem and Attackers Know It** — BleepingComputer. Vendor-sponsored opinion piece, no concrete incident.
- **Robot hand company settles Tesla trade secret suit and announces $11M raise** — TechCrunch AI. Generic startup/business news.
- **Ukraine to use seized crypto from cybercrime group to buy war bonds** — The Record. Asset-recovery/financial story, low technical security relevance.
- **Omen AI's plan to optimize data centers is all wet** — TechCrunch AI. Startup funding news, no security angle.
- **Webinar: Why business email compromise attacks keep succeeding** — BleepingComputer. Webinar promotion disguised as news.
- **Why Post-Quantum Cryptography Starts With Credentials** — The Hacker News. Generic educational/opinion piece, no specific news event.
- **US seizes hundreds of FIFA World Cup illegal streaming domains** — BleepingComputer. Duplicate of the Record's World Cup streaming takedown story; piracy, no infosec angle.
- **Mapping Europe's AI Workforce Opportunity** — OpenAI Blog. Labor-market/economic report, no security or capability substance.
- **'DirtyClone' Linux Kernel Vulnerability Leads to Root Access** — SecurityWeek. Already drafted in the pending, unmerged PR `digest/2026-06-29-1155` from earlier today — skipping to avoid duplicate posts.
- **OpenAI and Anthropic Limit New AI Models to Trump-Approved Customers During Cybersecurity Review** — SecurityWeek. Already drafted in pending PR `digest/2026-06-29-1155`.
- **The Gentlemen are knocking: custom backdoors and evolving tactics** — Securelist (Kaspersky GReAT). Already drafted in pending PR `digest/2026-06-29-1155`.
- **US Offers $10 Million Bounty for Russian State Hackers as Messaging App Attacks Evolve** — SecurityWeek / The Record / BleepingComputer (duplicate). Already drafted in pending PR `digest/2026-06-29-1155`.
- **Microsoft Removes 119 Edge Extensions That Hid Malware in Images and Fonts** — The Hacker News. Already drafted in pending PR `digest/2026-06-29-1155`.
- **OpenAI Unveils GPT-5.6 Sol as Its Most Advanced Cybersecurity AI** — SecurityWeek. Already drafted in pending PR `digest/2026-06-29-1155`.
- **Public PoC Released for Critical libssh2 CVE-2026-55200 Client-Side SSH Flaw** — The Hacker News. Already drafted in pending PR `digest/2026-06-29-1155`.
- **Gamaredon Expands Ukraine Attacks with New Malware and Cloud Service Abuse** — The Hacker News. Already drafted in pending PR `digest/2026-06-29-1155`.
- **Hijacked npm and Go Packages Use VS Code Tasks to Deploy Python Infostealer** — The Hacker News. Already drafted in pending PR `digest/2026-06-29-1155`.
