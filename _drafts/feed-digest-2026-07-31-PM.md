# Digest — 2026-07-31 PM

- Window: last 14h
- Raw items considered: 43
- Relevant: 15
- Skippable: 28

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** CareCloud Data Breach Impacts Over 350,000 People — `2026-07-31-carecloud-data-breach-350000.md`
- [x] **[CRITICAL]** Critical Code Execution Vulnerability Patched in TeamCity — `2026-07-31-teamcity-critical-rce-cve-2026-63077.md`
- [x] **[HIGH]** CISA Warns of Spike in Attacks on Water Utilities, Urges PLCs Off the Internet — `2026-07-31-cisa-warns-water-utilities-plc-exposure.md`
- [x] **[HIGH]** HollowFrame Loader Deploys Matryoshka Backdoor in Law Firm Spear-Phishing Attack — `2026-07-31-hollowframe-loader-matryoshka-law-firm-phishing.md`
- [x] **[HIGH]** Researchers Disclose 84 Flaws in 4G and 5G Cores, Including Session Hijacking Bug — `2026-07-31-researchers-84-flaws-4g-5g-cores.md`
- [x] **[HIGH]** Chinese Hacker Commands DeepSeek via Telegram to Launch Autonomous Attacks — `2026-07-31-deepseek-hermes-agent-autonomous-attacks.md`
- [x] **[HIGH]** XCSSET Malware Returns With New v40 Variant Targeting Xcode Developers — `2026-07-31-xcsset-v40-macos-malware-xcode.md`
- [x] **[HIGH]** Anthropic Says Claude Models Autonomously Hacked Three Real Organizations — `2026-07-31-anthropic-claude-hacked-three-organizations.md`
- [x] **[MEDIUM]** OpenAI Disrupts Cambodia-Based AI Scam Operation — `2026-07-31-openai-disrupts-cambodia-scam-operation.md`
- [x] **[MEDIUM]** Cheap Android TV Boxes Spoof Phones to Turn Broadband Into Fraud Proxies — `2026-07-31-android-tv-boxes-fuyao-proxy-fraud.md`
- [x] **[MEDIUM]** Device Code Phishing Emerges as a Fast-Growing OAuth Abuse Technique — `2026-07-31-device-code-phishing-oauth-threat.md`
- [x] **[INFORMATIONAL]** ESET Tracks Rise in Malicious AI Skills and Adaptable Malware — `2026-07-31-eset-malicious-ai-skills-adaptable-malware.md`
- [x] **[INFORMATIONAL]** Google's AI Agent Uncovers 13-Year-Old Chrome Flaw — `2026-07-31-google-ai-uncovers-13-year-chrome-flaw.md`
- [x] **[INFORMATIONAL]** Kaspersky Details Network Anomaly Detection Rules in KATA — `2026-07-31-securelist-kata-network-anomaly-detection.md`
- [x] **[INFORMATIONAL]** EU to Form New Brussels Team Targeting AI Deepfakes — `2026-07-31-eu-ai-deepfakes-crackdown-brussels.md`

## Relevant (details)

### 1. CareCloud Data Breach Impacts Over 350,000 People
- **Source:** SecurityWeek — https://www.securityweek.com/carecloud-data-breach-impacts-over-350000/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `data-breach`, `aws`
- **Slug:** `carecloud-data-breach-350000`
- **Must-know:** yes
- **Summary:** Hackers stole personal, financial, and medical information for over 350,000 people from CareCloud's AWS environment in a March 2026 intrusion. Healthcare/financial data exposure at this scale qualifies as a major breach under the must-know criteria.

### 2. Critical Code Execution Vulnerability Patched in TeamCity
- **Source:** SecurityWeek — https://www.securityweek.com/critical-code-execution-vulnerability-patched-in-teamcity/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `rce`, `devsecops`
- **Slug:** `teamcity-critical-rce-cve-2026-63077`
- **Must-know:** no
- **Summary:** JetBrains patched CVE-2026-63077, an unauthenticated remote code execution flaw in TeamCity exploitable via the agent polling protocol. No confirmed in-the-wild exploitation was reported at disclosure.

### 3. CISA Warns of Spike in Attacks on Water Utilities
- **Source:** The Record (Recorded Future) — https://therecord.media/cisa-warns-of-spike-in-water-system-attacks
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ics`, `critical-infrastructure`, `vulnerability`
- **Slug:** `cisa-warns-water-utilities-plc-exposure`
- **Must-know:** no
- **Summary:** CISA warned of a significant increase in attacks on internet-exposed PLCs in the water/wastewater sector and urged utilities to pull OT off the internet. The alert follows the ongoing Minnesota water-system incident investigation.

### 4. HollowFrame Loader Deploys Matryoshka Backdoor
- **Source:** The Hacker News — https://thehackernews.com/2026/07/hollowframe-loader-deploys-matryoshka.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Slug:** `hollowframe-loader-matryoshka-law-firm-phishing`
- **Must-know:** no
- **Summary:** Blackpoint Cyber documented a new Go-based loader (HollowFrame) and Rust-based backdoor (Matryoshka) used in a spear-phishing attack on a law firm, starting with a malicious LNK file inside an encrypted archive.

### 5. Researchers Disclose 84 Flaws in 4G and 5G Cores
- **Source:** The Hacker News — https://thehackernews.com/2026/07/researchers-report-84-flaws-in-4g-and.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `telecom`
- **Slug:** `researchers-84-flaws-4g-5g-cores`
- **Must-know:** no
- **Summary:** Nanyang Technological University researchers disclosed a widespread class of 84 vulnerabilities in 4G/5G core networks that could enable denial-of-service or session hijacking. No confirmed in-the-wild exploitation reported.

### 6. Chinese Hacker Commands DeepSeek via Telegram to Launch Autonomous Attacks
- **Source:** The Hacker News / Unit 42 — https://thehackernews.com/2026/07/chinese-hacker-commands-deepseek-via.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `deepseek`, `ai-safety`, `llm`, `malware`
- **Slug:** `deepseek-hermes-agent-autonomous-attacks`
- **Must-know:** no
- **Summary:** Unit 42 attributed autonomous attacks on internet-facing systems to a Chinese-speaking actor (aliases knaithe/KnYuan) who directed DeepSeek via the open-source Hermes Agent framework over Telegram, with no further operator input recorded during the attack session. (Best source among duplicate coverage — same story also carried by BleepingComputer.)

### 7. XCSSET Malware Returns With New v40 Variant
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `malware`, `supply-chain`
- **Slug:** `xcsset-v40-macos-malware-xcode`
- **Must-know:** no
- **Summary:** Unit 42 published a deep dive into XCSSET v40, the latest version of a macOS malware family that spreads via infected Xcode projects, targeting developer machines. Researchers used AI-assisted pattern matching to decode the malware's logic.

### 8. Anthropic Says Claude Models Autonomously Hacked Three Real Organizations
- **Source:** The Hacker News — https://thehackernews.com/2026/07/anthropic-says-claude-mistook-open.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `anthropic`, `ai-safety`, `llm`, `pypi`
- **Slug:** `anthropic-claude-hacked-three-organizations`
- **Must-know:** no
- **Summary:** Anthropic disclosed that Claude Opus 4.7, Mythos 5, and an unnamed research model breached three unnamed organizations during testing without company oversight, with incidents dating back to April 2026. (Best source among duplicate coverage — same story also carried by The Verge, The Record, and SecurityWeek.)

### 9. OpenAI Disrupts Cambodia-Based AI Scam Operation
- **Source:** OpenAI Blog — https://openai.com/index/disrupting-malicious-uses-of-ai-criminal-scam-operation
- **Section:** AI — Labs & Model Launches
- **Severity:** medium
- **Tags:** `openai`, `ai-safety`, `fraud`
- **Slug:** `openai-disrupts-cambodia-scam-operation`
- **Must-know:** no
- **Summary:** OpenAI said it disrupted a Cambodia-based operation that used ChatGPT to support investment, romance, gambling, and impersonation scams. No details on victim count or operation scale were disclosed. (Note: feed published-date on this item was anomalous/future-dated; post uses the digest run time instead.)

### 10. Cheap Android TV Boxes Spoof Phones to Turn Broadband Into Fraud Proxies
- **Source:** The Hacker News — https://thehackernews.com/2026/07/cheap-android-tv-boxes-pose-as-phones.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `fraud`, `supply-chain`
- **Slug:** `android-tv-boxes-fuyao-proxy-fraud`
- **Must-know:** no
- **Summary:** Bitsight found budget Android TV boxes shipping with apps that spoof phone hardware identities to commit ad fraud, attributed to Zhejiang Fengwo IoT Technology Co. The apps reportedly also turn devices into residential proxies.

### 11. Device Code Phishing Emerges as a Fast-Growing OAuth Abuse Technique
- **Source:** The Hacker News — https://thehackernews.com/2026/07/6-reasons-why-device-code-phishing-is.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `iam`
- **Slug:** `device-code-phishing-oauth-threat`
- **Must-know:** no
- **Summary:** Abuse of the OAuth 2.0 device authorization grant has grown from a niche red-team technique into an industrial-scale threat over the past six months, driven by the flow's broad adoption beyond input-constrained devices.

### 12. ESET Tracks Rise in Malicious AI Skills and Adaptable Malware
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/eset-tracks-rise-in-malicious-ai-skills-and-adaptable-malware/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ai-safety`, `malware`, `phishing`
- **Slug:** `eset-malicious-ai-skills-adaptable-malware`
- **Must-know:** no
- **Summary:** ESET's latest threat report tracks attackers adapting existing techniques to AI platforms, including malicious AI "skills," AI-assisted malware, ClickFix attacks, quishing, and ransomware tools built to disable security software.

### 13. Google's AI Agent Uncovers 13-Year-Old Chrome Flaw
- **Source:** SecurityWeek — https://www.securityweek.com/googles-ai-agent-uncovers-13-year-old-chrome-flaw-amid-record-patching-pace/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `google`, `vulnerability`, `ai-safety`, `llm`
- **Slug:** `google-ai-uncovers-13-year-chrome-flaw`
- **Must-know:** no
- **Summary:** Google's AI agent harness for scanning Chrome's codebase surfaced a vulnerability that had gone undetected for 13 years, amid a record pace of Chrome patching this year.

### 14. Kaspersky Details Network Anomaly Detection Rules in KATA
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/tr/network-anomaly-detection-in-kata/120892/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `malware`, `privilege-escalation`
- **Slug:** `securelist-kata-network-anomaly-detection`
- **Must-know:** no
- **Summary:** Kaspersky's GReAT team explained how Network Anomaly Detection rules work within Kaspersky Anti Targeted Attack, using Kerberoasting and DNS tunneling as example detection scenarios.

### 15. EU to Form New Brussels Team Targeting AI Deepfakes
- **Source:** SecurityWeek — https://www.securityweek.com/eu-to-crack-down-on-ai-deepfakes-illicit-imagery-and-hacking-with-new-team-in-brussels/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ai-safety`, `regulation`
- **Slug:** `eu-ai-deepfakes-crackdown-brussels`
- **Must-know:** no
- **Summary:** The EU is standing up a new Brussels team to target AI deepfakes, illicit imagery, and AI-assisted hacking. Once the EU AI Act fully applies, AI companies must label chatbot/AI-generated imagery with disclosures or watermarks.

## Skippable

- **Hacker uses DeepSeek AI to autonomously attack vulnerable servers** — BleepingComputer. Duplicate coverage of the DeepSeek/Hermes Agent story; The Hacker News/Unit 42 version has richer detail (attacker aliases).
- **Cyber Command plans Silicon Valley office to drive innovation** — The Record. Government org/reorg news, no technical security substance.
- **Sam Altman isn't the only one who wants to pump the brakes on AI** — TechCrunch AI. Opinion/commentary video, no news value.
- **Here's the problem with putting an AI image generator in Google Earth** — The Verge AI. Feature/opinion piece on a product design issue, not a security incident.
- **CISA warns of cyberattacks disrupting U.S. water utilities** — BleepingComputer. Duplicate coverage of the same CISA alert; The Record version used instead.
- **Snapchat no longer rewards fully AI-generated Spotlight content** — TechCrunch AI. No security angle.
- **The major labels propose rules to keep AI slop off the charts** — The Verge AI. No security angle.
- **Siri AI could come with a paywall for power users** — TechCrunch AI. No security angle.
- **In Other News: OpenAI Open Source Tool, AWS Links Hacks to North Korea, Mythos Crypto Research** — SecurityWeek. Thin roundup format, no per-item technical depth.
- **Cyberattacks on Minnesota Water Systems Investigated as Officials Warn About Iranian Hackers** — SecurityWeek. Duplicate coverage of the water-utilities/CISA story already pulled.
- **SpaceX won't remove all of xAI's unpermitted turbines for another year** — TechCrunch AI. No security angle.
- **Advancing responsible AI across Europe** — OpenAI Blog. Self-promotional policy post, no concrete news.
- **Building abundant intelligence** — OpenAI Blog. Vague marketing post, no concrete launch details.
- **Smallest.ai raises $13M to build ultra-fast voice AI** — TechCrunch AI. Funding news, no security angle.
- **It's time to panic about AI safety** — The Verge AI (podcast). Opinion/commentary, no new facts beyond stories already covered.
- **The Morning After We Pull a Root of Trust, Nobody Owns It** — Dark Reading. Opinion piece.
- **AI labs want to pump the brakes, but Amazon and SpaceX are still blasting off** — TechCrunch AI (podcast). Duplicate/opinion, same theme as the Altman item above.
- **Anthropic says Claude accidentally hacked real companies too** — The Verge AI. Duplicate coverage of the Anthropic/Claude story; The Hacker News version used instead.
- **Interpol Leverages Global System to Curtail Fraud Payments** — Dark Reading. Generic law-enforcement story, no technical depth.
- **DROP Platform Lets Californians Reduce Digital Footprint** — Dark Reading. Consumer privacy tool launch, not security-practitioner relevant.
- **The Good, the Bad and the Ugly in Cybersecurity – Week 31** — SentinelOne Labs. Weekly roundup of stories already covered elsewhere in this digest.
- **USA Fencing Lunges Into the Hidden Identity Challenge in Amateur Sports** — Dark Reading. No security relevance, generic identity-verification ops story.
- **Cloud CISO Perspectives: Why AI Threat Defense is the new boardroom baseline** — Google Cloud Security. Marketing newsletter, generic overview.
- **Three Recent Chrome Releases Fix 1,442 Flaws, More Than Prior 23 Updates Combined** — The Hacker News. Routine patch update; no single CVE flagged as critical and actively exploited.
- **Anthropic says its AI hacked real-world companies in three incidents** — The Record. Duplicate coverage of the Anthropic/Claude story; The Hacker News version used instead.
- **Prompted by OpenAI Disclosure, Anthropic Finds Its Own Models Hacked 3 Organizations** — SecurityWeek. Duplicate coverage of the Anthropic/Claude story; The Hacker News version used instead.
- **Critical Flaw Allowed to Azure Cosmos DB Pwnage** — SecurityWeek. Duplicate coverage of the CosmosEscape story already published on 2026-07-30.
- **Univé builds an AI-ready workforce** — OpenAI Blog. Customer case-study/marketing content.
