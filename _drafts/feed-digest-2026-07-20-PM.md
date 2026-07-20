# Digest — 2026-07-20 PM

- Window: last 14h
- Raw items considered: 41
- Relevant: 17
- Skippable: 24

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** SonicWall Zero-Days Exploited to Deliver Custom Malware for Weeks Before Patch — `2026-07-20-sonicwall-zero-days-exploited-custom-malware.md`
- [x] **[CRITICAL]** Critical ServiceNow Code Execution Flaw Now Exploited in Attacks — `2026-07-20-servicenow-critical-rce-exploited.md`
- [x] **[HIGH]** Exposed Server Reveals AI-Assisted Phishing Toolkit Behind WebDAV Malware Campaign — `2026-07-20-ai-assisted-phishing-toolkit-webdav-malware.md`
- [x] **[HIGH]** HollowGraph Malware Hides C2 and Stolen Files in Microsoft 365 Events Dated 2050 — `2026-07-20-hollowgraph-malware-microsoft-365-c2.md`
- [x] **[HIGH]** Russian Intelligence Hacks IP Cameras to Spy on Military Logistics Across NATO States and Ukraine — `2026-07-20-russian-intelligence-ip-camera-hacking-nato.md`
- [x] **[HIGH]** New 7-Zip Vulnerability Could Let Crafted XZ Archives Run Code During Extraction — `2026-07-20-7-zip-xz-archive-rce-vulnerability.md`
- [x] **[HIGH]** Chrome 150 Update Patches Severe Memory Safety Bugs — `2026-07-20-chrome-150-memory-safety-bugs-patched.md`
- [x] **[HIGH]** World's Largest AI Model Repository Hugging Face Breached by Autonomous AI Agent — `2026-07-20-hugging-face-breached-autonomous-ai-agent.md`
- [x] **[HIGH]** WP2Shell WordPress Vulnerabilities Exploited in the Wild — `2026-07-20-wp2shell-wordpress-vulnerabilities-exploited.md`
- [x] **[HIGH]** SleeperGem Uses Three Malicious RubyGems Packages to Target Developer Machines — `2026-07-20-sleepergem-malicious-rubygems-supply-chain.md`
- [x] **[MEDIUM]** Attackers Combo Up Evasion Tactics for BEC Phishing — `2026-07-20-bec-phishing-evasion-tactics-tff-trap.md`
- [x] **[MEDIUM]** OpenSSL Silently Fixes 'HollowByte' DoS Vulnerability — `2026-07-20-openssl-hollowbyte-dos-vulnerability.md`
- [x] **[MEDIUM]** Software Provider to More Than 2,000 US Hospitals Says Hackers Stole Employee and Customer Data — `2026-07-20-craneware-hospital-software-provider-breach.md`
- [x] **[MEDIUM]** Russian-Speaking Hacker Uses Google Gemini CLI to Control Botnet of Eight Dental Clinic PCs — `2026-07-20-gemini-cli-botnet-dental-clinic-pcs.md`
- [x] **[INFORMATIONAL]** Capital One Open Sources AI-Powered 'VulnHunter' Security Tool — `2026-07-20-capital-one-vulnhunter-open-source.md`
- [x] **[INFORMATIONAL]** China Delivers a One-Two Punch to America's AI Dominance — `2026-07-20-china-ai-models-moonshot-alibaba-qwen.md`
- [x] **[INFORMATIONAL]** Safety and Alignment in an Era of Long-Horizon Models — `2026-07-20-openai-safety-alignment-long-horizon-models.md`

## Relevant (details)

### 1. SonicWall Zero-Days Exploited to Deliver Custom Malware for Weeks Before Patch
- **Source:** SecurityWeek — https://www.securityweek.com/sonicwall-zero-days-exploited-to-deliver-custom-malware-for-weeks-before-patch/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`, `malware`
- **Slug:** `2026-07-20-sonicwall-zero-days-exploited-custom-malware`
- **Must-know:** yes
- **Summary:** Two zero-day vulnerabilities in SonicWall devices (CVE-2026-15409, CVE-2026-15410) were exploited by threat actor UTA0533 to deliver custom malware for weeks before a patch existed. This extended pre-patch exploitation window means affected organizations should assume compromise is possible even after patching.

### 2. Critical ServiceNow Code Execution Flaw Now Exploited in Attacks
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/critical-servicenow-code-execution-flaw-now-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `2026-07-20-servicenow-critical-rce-exploited`
- **Must-know:** no
- **Summary:** Attackers are actively exploiting a critical remote code execution flaw (CVE-2026-6875) in the ServiceNow AI Platform, per threat intel firm Defused. Organizations running the platform should patch immediately given confirmed in-the-wild exploitation.

### 3. Exposed Server Reveals AI-Assisted Phishing Toolkit Behind WebDAV Malware Campaign
- **Source:** The Hacker News — https://thehackernews.com/2026/07/exposed-server-reveals-ai-assisted.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `malware`, `llm`, `appsec`
- **Slug:** `2026-07-20-ai-assisted-phishing-toolkit-webdav-malware`
- **Must-know:** no
- **Summary:** An exposed delivery server let Rapid7 recover a full 1,048-file phishing toolkit showing AI-assisted lure creation, including an active campaign against Windows users in Mexico via a fake government ID-lookup site over WebDAV. The find offers rare visibility into how AI tooling is being folded into phishing kit development and testing.

### 4. HollowGraph Malware Hides C2 and Stolen Files in Microsoft 365 Events Dated 2050
- **Source:** The Hacker News — https://thehackernews.com/2026/07/hollowgraph-malware-hides-c2-and-stolen.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `microsoft`, `cloud-security`
- **Slug:** `2026-07-20-hollowgraph-malware-microsoft-365-c2`
- **Must-know:** no
- **Summary:** A newly identified espionage implant, HollowGraph, uses hijacked Microsoft 365 calendars as a stealthy C2 channel, hiding operator instructions and exfiltrated data in calendar events dated to 2050. Because it rides legitimate Microsoft Graph API traffic, the technique is difficult to distinguish from normal M365 usage.

### 5. Russian Intelligence Hacks IP Cameras to Spy on Military Logistics Across NATO States and Ukraine
- **Source:** The Hacker News — https://thehackernews.com/2026/07/russian-intelligence-hacks-ip-cameras.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `iot-security`, `vulnerability`, `malware`
- **Slug:** `2026-07-20-russian-intelligence-ip-camera-hacking-nato`
- **Must-know:** no
- **Summary:** A Russian intelligence service is systematically hijacking internet-connected security cameras across NATO states and Ukraine to monitor military logistics and troop movements, per a joint Dutch AIVD/MIVD advisory. The campaign represents an ongoing, large-scale surveillance operation rather than an isolated incident.

### 6. New 7-Zip Vulnerability Could Let Crafted XZ Archives Run Code During Extraction
- **Source:** The Hacker News — https://thehackernews.com/2026/07/new-7-zip-vulnerability-could-let.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `cve`, `vulnerability`, `appsec`
- **Slug:** `2026-07-20-7-zip-xz-archive-rce-vulnerability`
- **Must-know:** no
- **Summary:** A heap-based buffer overflow in 7-Zip's XZ archive handling (CVE-2026-14266) allows code execution when a victim opens a crafted archive. A fix already shipped in 7-Zip 26.02, so the main action item is confirming affected installs are updated.

### 7. Chrome 150 Update Patches Severe Memory Safety Bugs
- **Source:** SecurityWeek — https://www.securityweek.com/chrome-150-update-patches-severe-memory-safety-bugs/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`
- **Slug:** `2026-07-20-chrome-150-memory-safety-bugs-patched`
- **Must-know:** no
- **Summary:** Chrome 150 patches six critical and high-severity use-after-free vulnerabilities in a memory-safety-focused update. No detail is available on whether any flaws saw exploitation prior to the fix.

### 8. World's Largest AI Model Repository Hugging Face Breached by Autonomous AI Agent
- **Source:** The Hacker News — https://thehackernews.com/2026/07/worlds-largest-ai-model-repository.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `llm`, `ai-safety`
- **Slug:** `2026-07-20-hugging-face-breached-autonomous-ai-agent`
- **Must-know:** no
- **Summary:** Hugging Face disclosed that an autonomous AI agent system was used to breach its production infrastructure, giving attackers access to internal datasets and credentials. The incident is significant both as a breach of a major AI platform and as a concrete example of autonomous AI tooling being used to conduct an attack.

### 9. WP2Shell WordPress Vulnerabilities Exploited in the Wild
- **Source:** SecurityWeek — https://www.securityweek.com/wp2shell-wordpress-vulnerabilities-exploited-in-the-wild/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `appsec`
- **Slug:** `2026-07-20-wp2shell-wordpress-vulnerabilities-exploited`
- **Must-know:** no
- **Summary:** Two new WordPress vulnerabilities (CVE-2026-60137, CVE-2026-63030), tracked as WP2Shell, are already under active exploitation shortly after disclosure. Site operators should patch immediately given the fast-moving exploitation timeline.

### 10. SleeperGem Uses Three Malicious RubyGems Packages to Target Developer Machines
- **Source:** The Hacker News — https://thehackernews.com/2026/07/sleepergem-uses-three-malicious.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `malware`
- **Slug:** `2026-07-20-sleepergem-malicious-rubygems-supply-chain`
- **Must-know:** no
- **Summary:** Three malicious RubyGems packages, including one impersonating the legitimate "git_credential_manager" tool, were published to deliver additional payloads to developer machines in a supply chain attack dubbed SleeperGem. The typosquat naming increases risk that developers install the malicious package believing it's the official tool.

### 11. Attackers Combo Up Evasion Tactics for BEC Phishing
- **Source:** Dark Reading — https://www.darkreading.com/endpoint-security/attackers-combo-evasion-tactics-bec-phishing
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `malware`, `appsec`
- **Slug:** `2026-07-20-bec-phishing-evasion-tactics-tff-trap`
- **Must-know:** no
- **Summary:** A campaign dubbed "The TFF Trap" combines fileless execution techniques with low-detection loaders to deploy a mix of RATs and stealers (Agent Tesla, Remcos, XWorm, Best Private Logger). The evasion combination makes the campaign harder to catch with signature-based defenses.

### 12. OpenSSL Silently Fixes 'HollowByte' DoS Vulnerability
- **Source:** SecurityWeek — https://www.securityweek.com/openssl-silently-fixes-hollowbyte-dos-vulnerability/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `appsec`, `cve`
- **Slug:** `2026-07-20-openssl-hollowbyte-dos-vulnerability`
- **Must-know:** no
- **Summary:** OpenSSL quietly patched a denial-of-service flaw, dubbed HollowByte, where crafted payloads trigger unfreed buffer pre-allocations that exhaust server memory. Because no advisory accompanied the fix, some deployments may be unaware they need to update.

### 13. Software Provider to More Than 2,000 US Hospitals Says Hackers Stole Employee and Customer Data
- **Source:** The Record (Recorded Future) — https://therecord.media/software-provider-for-us-hospitals-customer-data-breach
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`, `supply-chain`
- **Slug:** `2026-07-20-craneware-hospital-software-provider-breach`
- **Must-know:** no
- **Summary:** Craneware, a software provider to more than 2,000 US hospitals, disclosed hackers accessed a subset of its data environment, stealing employee and customer information. Given Craneware's reach across the US hospital sector, downstream effects could extend to many healthcare organizations' data.

### 14. Russian-Speaking Hacker Uses Google Gemini CLI to Control Botnet of Eight Dental Clinic PCs
- **Source:** The Hacker News — https://thehackernews.com/2026/07/russian-speaking-hacker-uses-google.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `llm`, `malware`, `google`
- **Slug:** `2026-07-20-gemini-cli-botnet-dental-clinic-pcs`
- **Must-know:** no
- **Summary:** A Russian-speaking threat actor used Google's open-source Gemini CLI to help operate a small botnet of eight compromised dental clinic PCs, including for password cracking and proxy setup. While the botnet itself is small, it's a concrete example of an attacker operationalizing an open-source AI CLI for offensive tasks.

### 15. Capital One Open Sources AI-Powered 'VulnHunter' Security Tool
- **Source:** SecurityWeek — https://www.securityweek.com/capital-one-open-sources-ai-powered-vulnhunter-security-tool/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `appsec`, `llm`, `devsecops`
- **Slug:** `2026-07-20-capital-one-vulnhunter-open-source`
- **Must-know:** no
- **Summary:** Capital One open-sourced VulnHunter, an agentic AI tool that identifies exploitable code flaws, traces attack paths, and recommends remediations. The release adds to the growing set of AI-assisted vulnerability discovery tools available to the security community.

### 16. China Delivers a One-Two Punch to America's AI Dominance
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/967781/chinese-ai-models-open-source-moonshot-kimi-k3-alibaba-qwen
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `model-release`, `ai-launch`
- **Slug:** `2026-07-20-china-ai-models-moonshot-alibaba-qwen`
- **Must-know:** no
- **Summary:** Chinese labs Moonshot and Alibaba released new frontier models (Kimi K3 and an updated Qwen) this week, which the companies claim rival top US models at a fraction of the cost. The releases add to evidence that the gap between US and Chinese frontier AI is narrowing.

### 17. Safety and Alignment in an Era of Long-Horizon Models
- **Source:** OpenAI Blog — https://openai.com/index/safety-alignment-long-horizon-models
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `ai-safety`, `openai`, `llm`
- **Slug:** `2026-07-20-openai-safety-alignment-long-horizon-models`
- **Must-know:** no
- **Summary:** OpenAI published lessons from deploying long-running AI models, describing new safety risks and safeguards developed through iterative deployment. The post signals continued focus on agentic-model safety as deployments trend toward longer autonomous task horizons.

## Skippable

- **India says allegedly leaked nuclear plant files pose no safety risk** — The Record. Officials confirmed no safety/security-relevant data was in the leak; no ongoing risk to report.
- **New HollowGraph malware uses Microsoft Graph for stealthy C2 comms** — BleepingComputer. Duplicate coverage of the HollowGraph story; The Hacker News version has more technical detail.
- **More than 1,000 domains illegally streaming World Cup games seized, DOJ says** — The Record. Piracy enforcement action, no security/technical angle.
- **Who's Afraid of Chinese Models?** — Simon Willison. Opinion/policy commentary on distillation law, not a news event.
- **2026 ISO and CSA STAR certificates are now available with two additional services** — AWS Security Blog. Routine compliance certification announcement, no security substance.
- **AWS Weekly Roundup: One-click Lambda setup prompt, OpenAI GPT-5.6 models on Bedrock, and more** — AWS News Blog. Generic weekly roundup/marketing content.
- **Adobe's 'natural look' camera app embraces generative AI** — The Verge AI. Consumer product feature, no security angle.
- **Introducing Cosmos 3 Edge** — Hugging Face Blog. Feed entry had no summary text; insufficient detail to draft a factual post.
- **YouTube clarifies policies around AI slop and upsetting videos** — TechCrunch AI. Content policy/monetization update, no security relevance.
- **Hackers were inside South Korea's diplomat training system for 9 months** — The Record. Regional government breach disclosure without TTPs or IOCs.
- **Neo Emerges From Stealth With $100M to Control and Secure Enterprise AI Software** — SecurityWeek. Funding announcement, marketing content.
- **Romania races to restore land registry after cyberattack** — The Record. Regional incident without technical detail.
- **An AI SOC Evaluation Guide for Security Leaders** — BleepingComputer. Vendor guide/marketing content, not news.
- **Cybersecurity Keeps Events 'Uneventful'** — Dark Reading. Reflective opinion piece, no news value.
- **Weekly Recap: WordPress RCE, SonicWall 0-Days, AI Service Attacks, SharePoint 0-Day and More** — The Hacker News. Roundup duplicating stories already covered individually.
- **The Agentic SOC: Transforming Data into Defensive Velocity** — SentinelOne Labs. Vendor thought-leadership content, not news.
- **Hugging Face warns an autonomous AI agent hacked its network** — BleepingComputer. Duplicate coverage of the Hugging Face breach; The Hacker News version selected as primary.
- **New Index Tracks Material Breaches — And Refuses to Add Up the Losses** — SecurityWeek. Coverage of a tracking resource, not a news event itself.
- **Mythos Didn't Break Your Security Program. Your Exposure Window Could.** — The Hacker News. Industry-response opinion/analysis piece, no new news.
- **Ernst & Young Data Breach Affects Personal, Financial Information** — SecurityWeek. Generic breach disclosure without technical detail or confirmed scale.
- **Microsoft confirms Windows Server Update Services sync delays** — BleepingComputer. Generic IT operational issue, no security angle.
- **Watch on Demand: Cloud & Data Security Summit** — SecurityWeek. Webinar/event promotion.
- **Windows KB5121767 OOB update fixes shutdowns on some Dell PCs** — BleepingComputer. Generic hardware bug fix, not a security vulnerability.
- **Hugging Face Hacked in Autonomous AI Attack** — SecurityWeek. Duplicate coverage of the Hugging Face breach; The Hacker News version selected as primary.
