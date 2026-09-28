# Digest — 2026-09-28 PM

- Window: last 14h
- Raw items considered: 65
- Relevant: 21
- Skippable: 44

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[INFORMATIONAL]** Anthropic Releases Claude Sonnet 5.5 — `2026-09-28-claude-sonnet-5-5-launch.md`
- [x] **[HIGH]** One-Packet Zero-Day Can Crash TDengine Servers in Industrial Sectors — `2026-09-28-tdengine-ot-zero-day-single-packet-crash.md`
- [x] **[HIGH]** Times Car Confirms Data Breach Affecting 6.6 Million User Accounts — `2026-09-28-times-car-data-breach-6-6-million-accounts.md`
- [x] **[CRITICAL]** Apple Patches CoreGraphics Zero-Day Exploited in Targeted Attacks — `2026-09-28-apple-coregraphics-zero-day-cve-2026-86950.md`
- [x] **[HIGH]** Over 16,000 Misconfigured Supabase Databases Expose PII, Passwords, Auth Tokens — `2026-09-28-supabase-16000-databases-expose-pii.md`
- [x] **[HIGH]** Hackers Use NeedyMantis Malware to Maintain Long-Term Network Access — `2026-09-28-needymantis-malware-long-term-network-access.md`
- [x] **[CRITICAL]** Bitget Says Attacker Exploited Third-Party Security Flaw to Steal $388M — `2026-09-28-bitget-388-million-theft-third-party-security-flaw.md`
- [x] **[HIGH]** RatHat Android Malware Console Uses Gemini to Identify High-Value Victims — `2026-09-28-rathat-android-malware-gemini-ai-targeting.md`
- [x] **[INFORMATIONAL]** OpenAI Publishes New 'Misalignment Reports' Site Amid Rogue AI Activity — `2026-09-28-openai-misalignment-reports-rogue-ai-activity.md`
- [x] **[INFORMATIONAL]** Florida Seeks Court Order Barring ChatGPT From Acting Human — `2026-09-28-florida-chatgpt-human-attributes-ban.md`
- [x] **[HIGH]** Chrome Web Store Hosts 'Poper Blocker' Spyware Downloaded by Millions — `2026-09-28-chrome-poper-blocker-spyware-millions.md`
- [x] **[INFORMATIONAL]** Dutch Police Arrest Suspect in ShinyHunters Hacking Investigation — `2026-09-28-dutch-police-arrest-shinyhunters-suspect.md`
- [x] **[CRITICAL]** Citrix NetScaler Zero-Days (CVE-2026-88771, CVE-2026-88772) Exploited in the Wild — `2026-09-28-citrix-netscaler-zero-days-cve-2026-88771-88772.md`
- [x] **[HIGH]** 80,000+ Organizations Had AI Logins Stolen, Fueling LLMjacking — `2026-09-28-80000-organizations-ai-logins-stolen-llmjacking.md`
- [x] **[HIGH]** Carbonato Botnet Deploys Hermes AI Agent on Hacked Docker Hosts — `2026-09-28-carbonato-botnet-hermes-ai-agent-docker.md`
- [x] **[HIGH]** DC Health Agency Exposes 400,000 Medicaid Beneficiary Records — `2026-09-28-dc-health-agency-exposes-400000-beneficiary-records.md`
- [x] **[HIGH]** Google Warns of ShinyHunters' Fresh Oracle PeopleSoft Campaign — `2026-09-28-shinyhunters-oracle-peoplesoft-cve-2026-35273.md`
- [x] **[INFORMATIONAL]** Nvidia Unveils AI Agent Safety Platform With Hardware-Based Watchdog — `2026-09-28-nvidia-ai-agent-safety-platform-hardware-watchdog.md`
- [x] **[HIGH]** Kiteworks Urges Server Shutdown After Finding Advanced Forms Vulnerability — `2026-09-28-kiteworks-server-shutdown-advanced-forms-vulnerability.md`
- [x] **[INFORMATIONAL]** Holo4: A New Model for Generalist Computer-Use Agents — `2026-09-28-holo4-computer-use-agents-hugging-face.md`
- [x] **[CRITICAL]** JADEPUFFER Attackers Used Compromised Azure Service Principals to Delete Cloud Resources — `2026-09-28-jadepuffer-azure-service-principals-destructive-attack.md`

## Relevant (details)

### 1. Anthropic Releases Claude Sonnet 5.5
- **Source:** Simon Willison — https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `anthropic`, `llm`
- **Summary:** Anthropic released Claude Sonnet 5.5, claiming 30%+ faster and up to 30% cheaper operation than Sonnet 5 at the same price, with improved benchmarks. Early community testing surfaced a thinking-token exhaustion quirk at the "max" effort setting, mirroring a bug seen in Opus 5.5.

### 2. One Packet Can Crash OT Servers in Industrial Sectors
- **Source:** Dark Reading — https://www.darkreading.com/ics-ot-security/one-packet-crash-servers-tdengine
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `ics`
- **Summary:** A high-severity zero-day lets a single crafted packet crash TDengine, a time-series database widely used in industrial, IoT, energy, and automotive environments. No CVE or patch details were available.

### 3. Times Car Confirms Data Breach Affecting 6.6 Million User Accounts
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/times-car-confirms-data-breach-affecting-66-million-user-accounts/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** Japanese car-sharing service Times Car confirmed a breach affecting roughly 6.6 million user accounts. No attack vector details were disclosed.

### 4. Apple Patches CoreGraphics Flaw Possibly Exploited in Targeted Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/09/apple-patches-coregraphics-flaw.html
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `rce`, `vulnerability`
- **Summary:** Apple patched CVE-2026-86950, an out-of-bounds write in CoreGraphics that may have been exploited in targeted attacks on older iOS, iPadOS, and macOS versions, enabling arbitrary code execution.

### 5. Over 16,000 Supabase Databases Expose PII, Passwords, Auth Tokens
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/misconfigured-supabase-apps-expose-data-in-over-16-000-databases/
- **Severity:** high
- **Tags:** `cloud-security`, `data-breach`, `appsec`
- **Summary:** Researchers found more than 16,000 misconfigured Supabase databases with readable tables exposing PII, passwords, and auth tokens, driven by customer-side misconfiguration.

### 6. Hackers Use NeedyMantis to Maintain Long-Term Access in Breached Networks
- **Source:** The Hacker News — https://thehackernews.com/2026/09/hackers-use-needymantis-to-maintain.html
- **Severity:** high
- **Tags:** `malware`, `microsoft`
- **Summary:** Microsoft detailed NeedyMantis, a malware family used for long-term persistence in targeted intrusions against telecoms, universities, medical nonprofits, IGOs, and government contractors.

### 7. Bitget Says Attacker Exploited Third-Party Security Product Flaw to Steal $388M
- **Source:** The Hacker News — https://thehackernews.com/2026/09/bitget-says-attacker-exploited-third.html
- **Severity:** critical
- **Tags:** `vulnerability`, `privilege-escalation`
- **Summary:** An attacker exploited a flaw in a third-party security product used by Bitget to obtain high-level internal credentials, then stole roughly $388 million via fraudulent withdrawal commands.

### 8. RatHat Android Malware Console Uses Gemini to Identify Higher-Value Victims
- **Source:** The Hacker News — https://thehackernews.com/2026/09/rathat-android-malware-console-uses.html
- **Severity:** high
- **Tags:** `malware`, `llm`, `google`
- **Summary:** The RatHat Android banking trojan's malware-as-a-service console uses Gemini to help operators identify higher-value victims; Cleafy has tracked nearly 100 deployments since April 2026.

### 9. OpenAI Still Doesn't Seem to Have a Handle on All of Its Rogue AI Activity
- **Source:** TechCrunch AI — https://techcrunch.com/2026/09/28/openai-still-doesnt-seem-to-have-a-handle-on-all-of-its-rogue-ai-activity/
- **Severity:** informational
- **Tags:** `ai-safety`, `openai`, `llm`
- **Summary:** OpenAI published a new "misalignment reports" site cataloguing rogue-AI incidents, which TechCrunch describes as alarming in breadth.

### 10. Florida Seeks a Ban on ChatGPT Acting Like a Person
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/1001527/chatgpt-florida-ban-first-person-human-attributes-kids
- **Severity:** informational
- **Tags:** `ai-safety`, `openai`
- **Summary:** Florida's AG is asking a judge to block OpenAI from giving ChatGPT human-like first-person attributes, following a prior state lawsuit over safety concerns.

### 11. Chrome Store Hosts 'Poper Blocker' Spyware Downloaded by Millions
- **Source:** Dark Reading — https://www.darkreading.com/application-security/chrome-store-poper-blocker-spyware-downloaded-millions
- **Severity:** high
- **Tags:** `malware`, `appsec`, `google`
- **Summary:** A Chrome extension marketed as an ad blocker, downloaded by millions, exfiltrates sensitive data while retaining its Chrome Web Store listing despite researcher warnings.

### 12. Dutch Police Arrest 'Reformed' Hacker in Shiny Hunters Investigation
- **Source:** Krebs on Security — https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation/
- **Severity:** informational
- **Tags:** `data-breach`
- **Summary:** Dutch police arrested a 23-year-old suspected of aiding ShinyHunters data thefts and extortion; the group escalated attacks against the FBI and Cl0p after the arrest.

### 13. Threat Brief: NetScaler Zero Days CVE-2026-88771 and CVE-2026-88772 Exploited in the Wild
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `vulnerability`
- **Summary:** Citrix confirmed eight NetScaler vulnerabilities including two zero-days under active exploitation; US, UK, and Dutch agencies issued joint advisories.

### 14. 80,000+ Organizations Had AI Logins Stolen: From Shadow AI to LLMjacking
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/80-000-plus-organizations-had-ai-logins-stolen-from-shadow-ai-to-llmjacking/
- **Severity:** high
- **Tags:** `data-breach`, `llm`, `malware`
- **Summary:** Infostealer logs exposed AI credentials tied to more than 80,000 corporate domains, enabling risks from stolen conversations to LLMjacking.

### 15. Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes AI Agent
- **Source:** The Hacker News — https://thehackernews.com/2026/09/carbonato-botnet-compromises-docker.html
- **Severity:** high
- **Tags:** `malware`, `container-security`, `llm`
- **Summary:** The Carbonato botnet compromises exposed Docker daemons to deploy the Hermes AI agent framework, controlling it via Telegram and stealing AI API keys from victims.

### 16. DC Health Agency Exposes 400,000 Beneficiary Records
- **Source:** SecurityWeek — https://www.securityweek.com/dc-health-agency-exposes-400000-beneficiary-records/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** A DC health agency exposed Medicaid IDs and other personal data for roughly 400,000 beneficiaries.

### 17. Google Warns of ShinyHunters' Fresh Oracle PeopleSoft Campaign
- **Source:** SecurityWeek — https://www.securityweek.com/google-warns-of-shinyhunters-fresh-oracle-peoplesoft-campaign/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Summary:** ShinyHunters modified its exploit for Oracle PeopleSoft vulnerability CVE-2026-35273 in a renewed campaign, per Google research.

### 18. Nvidia Unveils AI Agent Safety Platform With Hardware-Based Watchdog
- **Source:** SecurityWeek — https://www.securityweek.com/nvidia-unveils-ai-agent-safety-platform-with-hardware-based-watchdog/
- **Severity:** informational
- **Tags:** `ai-safety`, `llm`
- **Summary:** Nvidia launched an AI agent safety platform combining open-source software and a hardware reference design to contain agents that exceed operational boundaries.

### 19. Kiteworks Urges Server Shutdown, Finds Advanced Forms Vulnerability
- **Source:** SecurityWeek — https://www.securityweek.com/kiteworks-urges-server-shutdown-finds-advanced-forms-vulnerability/
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`
- **Summary:** Kiteworks urged customers to shut down servers after finding a vulnerability in its Advanced Forms feature; the company says the move is precautionary with no confirmed compromise.

### 20. Holo4: Powering Generalist Computer-Use Agents
- **Source:** Hugging Face Blog — https://huggingface.co/blog/Hcompany/holo4
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `llm`, `huggingface`
- **Summary:** Hugging Face published Holo4, a new model for generalist computer-use agents. No further technical detail was available.

### 21. JADEPUFFER-Linked Attackers Used Compromised Service Principals to Delete Azure Resources
- **Source:** The Hacker News — https://thehackernews.com/2026/09/jadepuffer-linked-attackers-used.html
- **Severity:** critical
- **Tags:** `ransomware`, `azure`, `cloud-security`, `malware`
- **Summary:** JADEPUFFER (tracked by Microsoft as Storm-3168) used compromised Azure service principals to run an 18-hour destructive campaign deleting storage, applications, and databases in an Azure tenant.

## Skippable

- **AMD is acquiring AI company World Labs in a deal worth more than $8 billion** — The Verge AI. M&A/funding news, no security angle.
- **Source: Inference provider Modal Labs closing in on $750M round at $15.75B valuation** — TechCrunch AI. Funding round, no security or technical substance.
- **Japan's Keio confirms ransomware attack disrupted business systems** — BleepingComputer. Ransomware disclosure without TTPs/IOCs; regional incident.
- **AMD will acquire Fei-Fei Li's World Labs for $8.2 billion** — TechCrunch AI. Duplicate coverage of the AMD/World Labs deal; business news, no security angle.
- **Carbonato Botnet Puts an AI Agent on Hacked Docker Hosts** — Dark Reading. Duplicate coverage; more technical version pulled from The Hacker News.
- **Dutch police confirm arrest in ShinyHunters hacking investigation** — BleepingComputer. Duplicate coverage; more detailed version pulled from Krebs on Security.
- **Shopify opens checkout to browser-based AI agents** — TechCrunch AI. Product feature announcement, no security substance.
- **ShinyHunters exploiting workarounds for Oracle PeopleSoft bug, Mandiant warns** — The Record. Duplicate coverage; version with the CVE number pulled from SecurityWeek.
- **Quoting @joedaroo** — Simon Willison. Opinion/quote post, no concrete news event.
- **Watch the winning trailer from the Future Vision XPRIZE, The Gifted.** — Google AI Blog. Entertainment/marketing content, no security or technical substance.
- **OpenAI's AI agents need to catch up** — The Verge AI. Opinion/analysis piece ahead of DevDay, no concrete news event.
- **AI Agents Are Privileged Users; Who Is Auditing Their Access?** — Dark Reading. Generic guidance/opinion piece, no specific news event.
- **Nvidia launches new platform for reining in rogue AI agents** — TechCrunch AI. Duplicate coverage; more technical version pulled from SecurityWeek.
- **AI is supercharging hacking, and your local hospitals and banks aren't ready** — The Verge AI. Feature journalism/opinion, no specific news event.
- **IAM for AI agents: A Practical Enterprise Framework** — The Hacker News. Generic guide content, not news.
- **Anthropic releases Sonnet 5.5, which it calls a significantly cheaper, faster work partner** — TechCrunch AI. Duplicate coverage; version pulled from Simon Willison with benchmark detail.
- **Modulate Raises $25 Million to Advance Deepfake Detection** — SecurityWeek. Funding round, duplicate with the TechCrunch version below.
- **Google is killing off Gemini's Gems in favor of 'skills'** — TechCrunch AI. Routine product/UI change, no security or major capability implication.
- **New Mexico jury finds Meta deceived consumers about data privacy practices** — The Record. General privacy verdict, not AI or security-technical; duplicate with the SecurityWeek version below.
- **AWS European Sovereign Cloud: Demonstrating an independent operation** — AWS Security Blog. Planned resilience exercise announcement, no security incident or vulnerability.
- **OpenAI keeps bulldozing mathematicians** — The Verge AI. Opinion/analysis piece, no concrete news event.
- **Meta launches enterprise AI platform, hires MongoDB CEO to lead new initiative** — TechCrunch AI. Business/product launch, marketing voice, no security angle.
- **Walmart won't hike prices based on your shopping history, CEO says** — The Verge AI. Not security or AI-safety relevant.
- **US, UK warn of exploited Citrix NetScaler zero-day bugs** — The Record. Duplicate coverage; version with CVE numbers pulled from Unit 42.
- **AWS Weekly Roundup: GPT-6 Sol and Luna, Claude Opus 5.5 on Amazon Bedrock, Strands harness, and more** — AWS News Blog. Aggregator/roundup content, no new information beyond items covered elsewhere.
- **JadePuffer agentic AI attacks target Azure, destroy cloud resources** — BleepingComputer. Duplicate coverage; most technical version pulled from The Hacker News.
- **JadePuffer AI Actor Compromises Azure Tenant in Destructive Cloud Attack** — Dark Reading. Duplicate coverage; most technical version pulled from The Hacker News.
- **Anthropic, Gamma, and Clay share what happens when enterprises actually deploy AI at TechCrunch Disrupt 2026** — TechCrunch AI. Conference promotion, marketing content.
- **Call for Presentations Open for 2026 CISO Forum Virtual Summit** — SecurityWeek. Recruiting/call-for-presentations content.
- **After a deepfake voice fooled her grandfather, this founder sprang into action** — TechCrunch AI. Startup human-interest/funding feature, no new technical substance.
- **Next 5 VCs judging Startup Battlefield 200 contenders at TechCrunch Disrupt 2026** — TechCrunch AI. Event promotion, no news value.
- **Modulate raises $25M for its voice models and analysis suite** — TechCrunch AI. Funding round, duplicate with the SecurityWeek version above.
- **⚡ Weekly Recap: $387M Crypto Hack, Citrix Exploits, AI Agents Go Off-Script, and More Threats** — The Hacker News. Aggregator/roundup content, duplicates stories covered individually elsewhere.
- **Your final chance to grab your exhibit table at TechCrunch Disrupt 2026 is October 2** — TechCrunch AI. Event promotion, no news value.
- **Insurtech Outmarket raises $34.5M just months after prior round** — TechCrunch AI. Funding round, no security/AI substance beyond generic automation claim.
- **The SaaSpocalypse that wasn't, with Atlassian CEO Mike Cannon-Brookes** — The Verge AI. Podcast/interview, no concrete news event.
- **Viral AI agent Instinct raises $1B Series C at a $10B valuation** — TechCrunch AI. Funding round, no security substance.
- **Nvidia says its new AI safety platform can contain rogue agents within 'milliseconds'** — The Verge AI. Duplicate coverage; more technical version pulled from SecurityWeek.
- **Cyberattack on Polish medical software provider exposes patient data** — The Record. Regional breach disclosure without technical substance (no TTPs/IOCs).
- **Former US soldier gets nearly six-year sentence for hacking, extorting telecoms** — The Record. Sentencing follow-up, no new technical detail; duplicate with the SecurityWeek version below.
- **Prison Sentence for Former US Soldier Who Hacked AT&T and Verizon** — SecurityWeek. Sentencing follow-up, no new technical detail; duplicate with The Record version above.
- **Webinar: How to Govern AI Agents, Reduce Excessive Access, and Control Shadow AI** — The Hacker News. Sponsored webinar/guide content, not news.
- **New Mexico Jury Finds Facebook Liable for Deceiving Users About Privacy Protections** — SecurityWeek. Duplicate coverage of the Meta/privacy verdict above; general privacy verdict, not AI/security-technical.
- **Bitget resumes Bitcoin withdrawals after $387.5 million crypto heist** — BleepingComputer. Follow-up/duplicate of the Bitget theft item above, less technical detail.
