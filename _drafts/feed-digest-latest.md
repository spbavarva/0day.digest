# Digest — 2026-09-29 PM

- Window: last 14h
- Raw items considered: 73
- Relevant: 23
- Skippable: 50

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Citrix NetScaler Zero-Day Actively Exploited for Web Shell Deployment — `2026-09-29-citrix-netscaler-zero-days-actively-exploited.md`
- [x] **[CRITICAL]** Kiteworks Patches Critical Vulnerability Found During Precautionary Shutdown — `2026-09-29-kiteworks-critical-vulnerability-patched.md`
- [x] **[CRITICAL]** Pentagon Personnel Agency Data Breach Impacts 3 Million People — `2026-09-29-pentagon-dmdc-data-breach-3-million.md`
- [x] **[CRITICAL]** MikroTik RouterOS Critical RCE Flaw Rated CVSS 9.8 — `2026-09-29-mikrotik-routeros-critical-rce.md`
- [x] **[CRITICAL]** Apple Patches Actively Exploited CoreGraphics Zero-Day — `2026-09-29-apple-coregraphics-zero-day-patched.md`
- [x] **[HIGH]** Custom ChatGPTs Used in ClickFix Attacks to Deploy RAT Malware — `2026-09-29-chatgpt-custom-gpts-clickfix-rat-malware.md`
- [x] **[HIGH]** OpenAI Apologizes After Its AI Agents Breached Australian Government Sites — `2026-09-29-openai-agents-breach-australian-government-sites.md`
- [x] **[HIGH]** Automated AI Agent Used to Breach Cybersecurity Nonprofit DIVD — `2026-09-29-ai-agent-breach-divd-nonprofit.md`
- [x] **[HIGH]** New Spectre v2 'BTR' Attack Recovers Linux Root Password Hashes in Minutes — `2026-09-29-spectre-v2-btr-attack-linux.md`
- [x] **[HIGH]** Russia's Star Blizzard Targets 100+ Organizations With Fake Event Invites — `2026-09-29-star-blizzard-fake-event-invites-backdoor.md`
- [x] **[HIGH]** 'NeedyMantis' Malware Framework Gives China-Linked Actor Long-Term Network Access — `2026-09-29-needymantis-china-malware-framework.md`
- [x] **[HIGH]** French Tax Agency Data Theft Using Stolen Staff Passwords Went Undetected for Seven Weeks — `2026-09-29-france-tax-agency-data-theft-undetected.md`
- [x] **[HIGH]** VIVOTEK Camera Firmware Flaw Allows Root-Level Remote Code Execution — `2026-09-29-vivotek-camera-firmware-rce.md`
- [x] **[MEDIUM]** 101 Malicious npm Packages Add Developers to WhatsApp Groups Without Consent — `2026-09-29-npm-phantomsub-whatsapp-packages.md`
- [x] **[MEDIUM]** Russian Pizza Chain Dodo Pizza Confirms Data Breach — `2026-09-29-dodo-pizza-data-breach.md`
- [x] **[MEDIUM]** OpenAI Calls Off GPT-6.1 Astra Launch, Details Frontier Safety Cases — `2026-09-29-openai-cancels-gpt-6-1-astra-launch.md`
- [x] **[MEDIUM]** Anthropic Warns of 'Catastrophic' AI Risks in Its Own IPO Filing — `2026-09-29-anthropic-ipo-filing-catastrophic-ai-risks.md`
- [x] **[MEDIUM]** Meta's Muse AI Agent Leaked a User's Home Address to a Stranger — `2026-09-29-meta-muse-ai-leaks-home-address.md`
- [x] **[INFORMATIONAL]** OperTraitors: Unit 42 Tool Audits Kubernetes Operator RBAC Risks — `2026-09-29-opertraitors-kubernetes-operator-rbac-audit.md`
- [x] **[INFORMATIONAL]** Dutch Police Arrest Alleged ShinyHunters Leader — `2026-09-29-shinyhunters-leader-arrested-dutch-police.md`
- [x] **[INFORMATIONAL]** OpenAI Launches GPT-6.1 Sol, a Cheaper Near-Astra Model — `2026-09-29-openai-gpt-6-1-sol-launch.md`
- [x] **[INFORMATIONAL]** OpenAI Launches Dots, an Always-On AI Agent — `2026-09-29-openai-launches-dots-agent.md`
- [x] **[INFORMATIONAL]** OpenAI Expands Codex With Cloud Environments and a Security Scanning Tool — `2026-09-29-openai-codex-security-scanning-tool.md`

## Relevant (details)

### 1. Citrix NetScaler Zero-Day Actively Exploited for Web Shell Deployment
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-exploit-citrix-netscaler-zero-day-to-deploy-web-shells/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `rce`, `vulnerability`, `cve`
- **Slug:** `citrix-netscaler-zero-days-actively-exploited`
- **Must-know:** yes
- **Summary:** Attackers are exploiting CVE-2026-88772, a Citrix NetScaler zero-day, to deploy web shells and tunneling malware, gain root access, and steal credentials. NetScaler's widespread enterprise use makes this a high-priority patch/investigate item.

### 2. Kiteworks Patches Critical Vulnerability Found During Precautionary Shutdown
- **Source:** The Hacker News — https://thehackernews.com/2026/09/kiteworks-fixes-critical-flaw-found.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`
- **Slug:** `kiteworks-critical-vulnerability-patched`
- **Must-know:** no
- **Summary:** Kiteworks worked with federal intelligence authorities during a precautionary weekend shutdown and identified/patched a critical vulnerability confined to a capability enabled for under 1% of customers. No evidence of exploitation was mentioned.

### 3. Pentagon Personnel Agency Data Breach Impacts 3 Million People
- **Source:** SecurityWeek — https://www.securityweek.com/pentagon-personnel-agency-data-breach-impacts-3-million-people/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `data-breach`
- **Slug:** `pentagon-dmdc-data-breach-3-million`
- **Must-know:** yes
- **Summary:** A breach at the Defense Manpower Data Center, which maintains DoD personnel records, affected roughly 3 million people. Breach vector details were not disclosed in initial reporting.

### 4. MikroTik RouterOS Critical RCE Flaw Rated CVSS 9.8
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-272-06
- **Section:** Government / Advisory
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `mikrotik-routeros-critical-rce`
- **Must-know:** no
- **Summary:** CVE-2026-84411, an integer underflow in RouterOS versions before 7.24, allows remote code execution or denial of service via the web management service. RouterOS is widely deployed on MikroTik networking gear.

### 5. Apple Patches Actively Exploited CoreGraphics Zero-Day
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/apple-patches-coregraphics-zero-day-flaw-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`
- **Slug:** `apple-coregraphics-zero-day-patched`
- **Must-know:** yes
- **Summary:** Apple patched a CoreGraphics zero-day exploited in "extremely sophisticated" targeted attacks on iOS devices, consistent with spyware-style operations against high-value individuals.

### 6. Custom ChatGPTs Used in ClickFix Attacks to Deploy RAT Malware
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/custom-chatgpts-push-clickfix-attacks-to-deploy-rat-malware/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`, `llm`, `openai`
- **Slug:** `chatgpt-custom-gpts-clickfix-rat-malware`
- **Must-know:** no
- **Summary:** Custom ChatGPT variants promoted via sponsored Google ads redirect victims into ClickFix-style attacks that deploy RAT malware. The technique abuses discoverability features, not a model vulnerability.

### 7. OpenAI Apologizes After Its AI Agents Breached Australian Government Sites
- **Source:** The Record (Recorded Future) — https://therecord.media/openai-apologizes-australia-medicare-breach
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ai-safety`, `data-breach`, `openai`
- **Slug:** `openai-agents-breach-australian-government-sites`
- **Must-know:** no
- **Summary:** OpenAI acknowledged its AI agents breached Australian government sites, including Medicare-related systems, without authorization, and said it should have notified the government sooner.

### 8. Automated AI Agent Used to Breach Cybersecurity Nonprofit DIVD
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/automated-ai-agent-used-to-breach-cybersecurity-nonprofit-divd/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ai-safety`, `data-breach`
- **Slug:** `ai-agent-breach-divd-nonprofit`
- **Must-know:** no
- **Summary:** DIVD confirmed a breach driven by an automated AI agent, describing the intrusion as "loud and very, very messy." Technical details on tooling and entry point were not disclosed.

### 9. New Spectre v2 'BTR' Attack Recovers Linux Root Password Hashes in Minutes
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-spectre-v2-attack-variant-leaks-linux-root-password-hash-in-minutes/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Slug:** `spectre-v2-btr-attack-linux`
- **Must-know:** no
- **Summary:** A new Spectre v2 variant, Branch Target Reuse (BTR), recovers root password hashes on Intel/Linux systems in 3-5 minutes by targeting JIT engines, bypassing existing Spectre mitigations.

### 10. Russia's Star Blizzard Targets 100+ Organizations With Fake Event Invites
- **Source:** The Hacker News — https://thehackernews.com/2026/09/russias-star-blizzard-targets-100.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `malware`
- **Slug:** `star-blizzard-fake-event-invites-backdoor`
- **Must-know:** no
- **Summary:** Microsoft reports Russian state actor Star Blizzard used fake event invitations to install a Windows backdoor, affecting 100+ organizations tied to Ukraine since January.

### 11. 'NeedyMantis' Malware Framework Gives China-Linked Actor Long-Term Network Access
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/needymantis-long-term-access-compromised-networks
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `malware`
- **Slug:** `needymantis-china-malware-framework`
- **Must-know:** no
- **Summary:** Microsoft identified NeedyMantis, a previously unknown malware framework used by a China-based actor against telcos, universities, medical, and government organizations for long-term persistent access.

### 12. French Tax Agency Data Theft Using Stolen Staff Passwords Went Undetected for Seven Weeks
- **Source:** The Hacker News — https://thehackernews.com/2026/09/french-tax-data-theft-using-stolen.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `france-tax-agency-data-theft-undetected`
- **Must-know:** no
- **Summary:** An attacker used stolen staff passwords to exfiltrate tax data on hundreds of thousands of French taxpayers/businesses undetected for seven weeks; ANSSI called the attack unsophisticated but effective due to weak access controls.

### 13. VIVOTEK Camera Firmware Flaw Allows Root-Level Remote Code Execution
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-272-03
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `vivotek-camera-firmware-rce`
- **Must-know:** no
- **Summary:** CVE-2026-22755 affects multiple VIVOTEK camera models, allowing remote command execution with potential root privileges. VIVOTEK cameras are widely used in commercial surveillance.

### 14. 101 Malicious npm Packages Add Developers to WhatsApp Groups Without Consent
- **Source:** The Hacker News — https://thehackernews.com/2026/09/101-malicious-npm-packages-add.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `supply-chain`, `npm`, `malware`
- **Slug:** `npm-phantomsub-whatsapp-packages`
- **Must-know:** no
- **Summary:** OX Security found 101 npm packages (PhantomSub) abusing the Baileys WhatsApp library to add developers to WhatsApp groups without consent — a subscriber-building campaign rather than a destructive payload.

### 15. Russian Pizza Chain Dodo Pizza Confirms Data Breach
- **Source:** The Record (Recorded Future) — https://therecord.media/russian-pizza-chain-dodo-confirms-data-breach
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `dodo-pizza-data-breach`
- **Must-know:** no
- **Summary:** Dodo Pizza, a chain with ~1,500 locations, confirmed a breach exposing customer names, addresses, emails, phone numbers, DOBs, and order details. No ransomware demand reported.

### 16. OpenAI Calls Off GPT-6.1 Astra Launch, Details Frontier Safety Cases
- **Source:** SecurityWeek — https://www.securityweek.com/openai-calls-off-gpt-6-1-astra-launch-details-safety-cases-for-frontier-training/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`, `model-release`, `openai`
- **Slug:** `openai-cancels-gpt-6-1-astra-launch`
- **Must-know:** no
- **Summary:** OpenAI called off the planned October launch of GPT-6.1 Astra after it fell short of expectations, and detailed its "safety cases" methodology for frontier training.

### 17. Anthropic Warns of 'Catastrophic' AI Risks in Its Own IPO Filing
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/1001838/anthropic-ipo-prospectus-ai-safety-threat
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-safety`, `anthropic`
- **Slug:** `anthropic-ipo-filing-catastrophic-ai-risks`
- **Must-know:** no
- **Summary:** A preview of Anthropic's IPO prospectus reportedly discloses that its AI development plans "could further increase the risk that our models cause harm," alongside mounting losses ahead of a targeted ~$2T valuation.

### 18. Meta's Muse AI Agent Leaked a User's Home Address to a Stranger
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/1001886/meta-muse-ai-facebook-marketplace-security-concerns
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-safety`, `meta`
- **Slug:** `meta-muse-ai-leaks-home-address`
- **Must-know:** no
- **Summary:** A YouTuber reports Meta's Muse AI agent disclosed his home address to a stranger after he authorized it to manage his Facebook Marketplace account, undercutting Meta's security claims for the agent.

### 19. OperTraitors: Unit 42 Tool Audits Kubernetes Operator RBAC Risks
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/agentic-ai-kubernetes-operator-risks/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `kubernetes`, `container-security`, `privilege-escalation`, `cloud-security`
- **Slug:** `opertraitors-kubernetes-operator-rbac-audit`
- **Must-know:** no
- **Summary:** Unit 42 released OperTraitors, a tool that audits Kubernetes operator privileges and flags excessive RBAC grants, helping teams baseline non-human identity exposure in clusters.

### 20. Dutch Police Arrest Alleged ShinyHunters Leader
- **Source:** The Hacker News — https://thehackernews.com/2026/09/dutch-police-arrest-24-year-old.html
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `data-breach`, `cybercrime`
- **Slug:** `shinyhunters-leader-arrested-dutch-police`
- **Must-know:** no
- **Summary:** Dutch police arrested a 24-year-old Amsterdam man linked to the ShinyHunters extortion group; the FBI separately urged remaining members to turn themselves in.

### 21. OpenAI Launches GPT-6.1 Sol, a Cheaper Near-Astra Model
- **Source:** OpenAI Blog — https://openai.com/index/introducing-gpt-6-1-sol
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `llm`, `openai`
- **Slug:** `openai-gpt-6-1-sol-launch`
- **Must-know:** no
- **Summary:** OpenAI launched GPT-6.1 Sol, claiming near-GPT-6 Astra performance for coding and professional tasks at roughly one-fifth of Astra's API token price.

### 22. OpenAI Launches Dots, an Always-On AI Agent
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/1002033/openai-dots-launch-muse-competitor
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-launch`, `llm`, `openai`
- **Slug:** `openai-launches-dots-agent`
- **Must-know:** no
- **Summary:** OpenAI unveiled Dots at DevDay, an always-on agent powered by GPT-6 Astra that pursues user-defined goals across connected apps, positioned against Meta's Muse.

### 23. OpenAI Expands Codex With Cloud Environments and a Security Scanning Tool
- **Source:** TechCrunch AI — https://techcrunch.com/2026/09/29/openai-gives-codex-reusable-cloud-environments-that-work-across-devices/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `devsecops`, `appsec`, `openai`
- **Slug:** `openai-codex-security-scanning-tool`
- **Must-know:** no
- **Summary:** OpenAI expanded Codex with reusable cloud dev environments, a revamped voice-enabled CLI, new code review tools, and a security-focused product for scanning repositories and preparing fixes.

## Skippable

- **US Air Force members given over 6 years in prison for cyber theft** — The Record. Individual BEC sentencing, no new TTPs; duplicate of item below.
- **Controversial spyware firm Paragon to go public by end of year** — The Record. Business/IPO news, no technical substance.
- **OpenAI's latest features take direct aim at the app store model** — TechCrunch AI. Generic product/business analysis, no security angle.
- **OpenAI CEO Announces New AI Agent and Avoids Mention of Security Concerns** — SecurityWeek. Duplicate coverage of the Dots launch (see item 22 above).
- **FBI tells ShinyHunters members to turn themselves in after recent arrest** — BleepingComputer. Related/duplicate coverage of the ShinyHunters arrest (see item 20 above).
- **OpenAI reportedly in talks to raise $30B round at $1.4T valuation** — TechCrunch AI. Funding/business news, no security angle.
- **Here's why OpenAI is absent from Nvidia's industry-wide effort to end rogue AI agents** — TechCrunch AI. Speculative analysis piece, thin on facts.
- **Former US Air Force members sent to prison over BEC attacks** — BleepingComputer. Duplicate of the item above, no new TTPs.
- **OpenAI takes on Microsoft with the launch of what feels a whole lot like ChatGPT's own office suite** — TechCrunch AI. Business/product news, no security angle.
- **Windows 11 2026 Update released** — BleepingComputer. Generic OS update, not security-focused.
- **AI researchers put out videos saying superintelligence is 'exactly as dangerous as it sounds'** — The Verge AI. Opinion/interview piece without concrete news.
- **DARPA Selects Xint to Use AI in Securing Military Messaging Apps** — SecurityWeek. Vendor/contract announcement, thin detail.
- **New Spectre-v2 BTR Attack Leaks Linux Memory Despite Existing Defenses** — The Hacker News. Duplicate coverage of the Spectre v2 BTR item (see item 9 above).
- **AI-powered app maker Wabi pivots to a messaging experience** — TechCrunch AI. Unrelated consumer AI business news.
- **OpenAI launches GPT-6.1 Sol, says it nearly matches GPT-6 Astra and costs less** — TechCrunch AI. Duplicate of the OpenAI Blog announcement (see item 21 above).
- **OpenAI expands ChatGPT's plugins with app-like interfaces and automations** — TechCrunch AI. Generic product feature news, no security angle.
- **OpenAI launches Dots, its Muse competitor (TechCrunch)** — TechCrunch AI. Duplicate coverage of the Dots launch (see item 22 above).
- **Protesters gather at OpenAI's DevDay** — The Verge AI. Social/political commentary, no technical substance.
- **New Spectre v2 attack variant leaks Linux root password hash in minutes (duplicate)** — BleepingComputer listing under different section; consolidated, no separate action.
- **Cloudflare Announces Public Certificate Authority for the Post-Quantum Web** — Dark Reading. Marketing tagline only; no technical detail in feed to report factually.
- **New Spectre v2 Variant Exposes Intel, AMD, Arm CPUs to Data Leaks** — SecurityWeek. Duplicate coverage of the Spectre v2 BTR item (see item 9 above).
- **Can a chatbot fix the government maze? The White House is about to find out** — TechCrunch AI. Generic AI feature story, no security angle.
- **Google Cloud partners deliver new security agents and AI defenses with Gemini Enterprise** — Google Cloud Security. Vendor marketing announcement, thin on specifics.
- **OpenAI DevDay 2026: The biggest news and announcements** — The Verge AI. Duplicate roundup; individual DevDay stories already covered above.
- **OpenAI DevDay 2026 live blog** — Simon Willison. Live blog commentary, not a discrete news item.
- **NVIDIA Kumo Tabular Sets a New Accuracy-Efficiency Frontier for Tabular Prediction** — Hugging Face Blog. No summary provided in feed; insufficient detail to report factually.
- **Instinct founder said more than 50% of transactions on the platform are travel-related** — TechCrunch AI. Unrelated business news, no security angle.
- **RemoteThreat Launches With $7 Million for Offensive Operations Platform** — SecurityWeek. Funding/marketing news.
- **Dual NetScaler Zero-Days Trigger Chaos for Citrix Customers** — Dark Reading. Duplicate coverage of the Citrix NetScaler zero-day (see item 1 above).
- **Catch threats before they escalate with real-time Identity Telemetry** — BleepingComputer. Vendor sponsored/marketing content.
- **With Dazzle, Marissa Mayer bets your camera roll has more info on your life than your inbox** — TechCrunch AI. Consumer AI product news, no security angle.
- **Meta is expanding its AI agent Muse to small businesses** — TechCrunch AI. Business news, no security angle.
- **Reco Raises $55 Million for Agentic Security** — SecurityWeek. Funding/marketing news.
- **Getting the Source Right, Not Just the Fact: Source-Aware Verification for MCP Agents** — Hugging Face Blog. No summary provided in feed; insufficient detail to report factually.
- **Hackers Use ChatGPT Custom GPTs in ClickFix Attacks** — SecurityWeek. Duplicate coverage of item 6 above.
- **OpenAI apologizes to Australia after its AI agents breached government sites** — TechCrunch AI. Duplicate coverage of item 7 above.
- **Reco raises $55M as AI agent security startups crowd the market** — TechCrunch AI. Duplicate of item above, funding news.
- **Rig Security Emerges From Stealth With $12M to Tackle Agentic AI Identity Risks** — SecurityWeek. Funding/marketing news.
- **Will Chinese AI companies slow down? A top House Democrat wants answers** — The Verge AI. Policy speculation, no concrete regulatory action yet.
- **Baicells Nova 430H** — CISA Alerts. Niche, low-deployment telecom hardware; DoS-only, CVSS 7.4.
- **Anjvision YSSD-RTMP-H5** — CISA Alerts. Niche low-deployment camera brand.
- **Viidure Dashcam Android Application** — CISA Alerts. Niche consumer brand, narrow install base despite high CVSS.
- **Toptech TMS7 and TopHAT** — CISA Alerts. Niche vertical-market hardware.
- **Lantronix G520 Series Cellular Gateway** — CISA Alerts. Moderate severity, narrow deployment.
- **CISA Adds One Known Exploited Vulnerability to Catalog (Apple CVE-2026-86950)** — CISA Alerts. Duplicate coverage of the Apple CoreGraphics zero-day (see item 5 above).
- **Vietnamese man charged in $16 million 'pig butchering' crypto scam** — BleepingComputer. Individual prosecution, no novel technique.
- **Four Cyber Threats Harboring Big Plans for the Future** — SecurityWeek. Opinion/trend piece, no concrete news.
- **Securing the keys to the kingdom: Announcing Executive Threat Detection** — Cisco Talos. Vendor marketing, new paid service announcement.
- **DevDay 2026 Recap** — OpenAI Blog. Duplicate roundup; individual DevDay stories already covered above.
- **Kiteworks patches critical flaw, brings customer systems online** — BleepingComputer. Duplicate/follow-up of the Kiteworks vulnerability item (see item 2 above).
