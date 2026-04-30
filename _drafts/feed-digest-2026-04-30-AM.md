# Digest — 2026-04-30 AM

- Window: last 14h
- Raw items considered: 26
- Relevant: 10
- Skippable: 16

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Google Patches CVSS 10 Gemini CLI RCE Enabling Supply-Chain Code Execution — `2026-04-30-gemini-cli-cvss10-rce-supply-chain.md`
- [x] **[CRITICAL]** Official SAP npm Packages Compromised in TeamPCP Supply-Chain Attack — `2026-04-29-sap-npm-supply-chain-teampcp.md`
- [x] **[HIGH]** Sandhills Medical Ransomware Breach Affects 170,000 Patients — `2026-04-30-sandhills-medical-ransomware-170k.md`
- [x] **[HIGH]** Silver Fox Deploys New ABCDoor Backdoor Alongside ValleyRAT in Tax-Lure Campaign — `2026-04-30-silver-fox-abcdoor-backdoor.md`
- [x] **[HIGH]** WordPress Redirect Plugin Hid Dormant Backdoor for Five Years Across 70,000 Sites — `2026-04-29-wordpress-redirect-plugin-dormant-backdoor.md`
- [x] **[HIGH]** Qinglong Task Scheduler RCE Under Active Exploitation for Cryptomining — `2026-04-29-qinglong-rce-active-exploit.md`
- [x] **[HIGH]** Wiz Used AI Reverse Engineering to Uncover High-Severity GitHub Vulnerability — `2026-04-29-wiz-ai-reverse-engineering-github-bug.md`
- [x] **[HIGH]** AI Finds 38 Security Flaws in OpenEMR Platform Used by 100,000+ Healthcare Providers — `2026-04-29-ai-finds-38-openemr-flaws.md`
- [x] **[MEDIUM]** Claude Mythos Alarm Spreads to Japan's Financial Services Sector — `2026-04-30-claude-mythos-japan-financial-sector.md`
- [x] **[INFORMATIONAL]** OpenAI Publishes Root Cause Analysis of GPT-5 Goblin Behavior Quirks — `2026-04-29-openai-gpt5-goblin-behavior-root-cause.md`

## Relevant (details)

### 1. Google Patches CVSS 10 Gemini CLI RCE Enabling Supply-Chain Code Execution
- **Source:** The Hacker News — https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `supply-chain`, `npm`, `github`, `google`, `vulnerability`, `cve`
- **Slug:** `2026-04-30-gemini-cli-cvss10-rce-supply-chain`
- **Must-know:** yes
- **Summary:** A CVSS 10 flaw in the official `@google/gemini-cli` npm package and the `google-github-actions/run-gemini-cli` GitHub Actions workflow allowed unprivileged external attackers to force malicious content to load as Gemini configuration and execute arbitrary commands on host systems. Any CI/CD pipeline consuming either artifact was potentially exposed; update immediately and treat runner environments from affected versions as compromised.

### 2. Official SAP npm Packages Compromised in TeamPCP Supply-Chain Attack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/official-sap-npm-packages-compromised-to-steal-credentials/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`
- **Slug:** `2026-04-29-sap-npm-supply-chain-teampcp`
- **Must-know:** yes
- **Summary:** Multiple official SAP npm packages were backdoored by the TeamPCP threat actor to steal developer credentials and authentication tokens from affected systems. Packages were published under SAP's official namespace, making them trusted by enterprise CI/CD pipelines — rotate all credentials from systems that installed affected versions and audit package lock files immediately.

### 3. Sandhills Medical Ransomware Breach Affects 170,000 Patients
- **Source:** SecurityWeek — https://www.securityweek.com/sandhills-medical-says-ransomware-breach-affects-170000/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`, `data-breach`
- **Slug:** `2026-04-30-sandhills-medical-ransomware-170k`
- **Must-know:** no
- **Summary:** Sandhills Medical disclosed a ransomware breach affecting 170,000 individuals — attributed to the Inc Ransom group — nearly one year after the initial attack. The delayed disclosure timeline is a significant compliance concern under HIPAA and highlights how healthcare organizations continue to lag on breach notification obligations.

### 4. Silver Fox Deploys New ABCDoor Backdoor Alongside ValleyRAT in Tax-Lure Campaign
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/silver-fox-tax-notification-campaign/119575/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Slug:** `2026-04-30-silver-fox-abcdoor-backdoor`
- **Must-know:** no
- **Summary:** The Silver Fox APT group is targeting organizations in Russia and India using tax-authority impersonation lures to deliver ValleyRAT alongside a newly identified backdoor called ABCDoor. The introduction of new custom tooling signals continued investment by the group; security teams in affected regions should prioritize detection of both malware families.

### 5. WordPress Redirect Plugin Hid Dormant Backdoor for Five Years Across 70,000 Sites
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/popular-wordpress-redirect-plugin-hid-dormant-backdoor-for-years/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `appsec`, `malware`
- **Slug:** `2026-04-29-wordpress-redirect-plugin-dormant-backdoor`
- **Must-know:** no
- **Summary:** The Quick Page/Post Redirect plugin, installed on over 70,000 WordPress sites, contained a backdoor added five years ago enabling arbitrary code injection into affected sites. The backdoor remained dormant and undetected until now; administrators should remove the plugin immediately and audit sites for unauthorized modifications.

### 6. Qinglong Task Scheduler RCE Under Active Exploitation for Cryptomining
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-exploit-rce-flaws-in-qinglong-task-scheduler-for-cryptomining/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `malware`
- **Slug:** `2026-04-29-qinglong-rce-active-exploit`
- **Must-know:** no
- **Summary:** Two authentication bypass vulnerabilities in the Qinglong open-source task scheduler are being actively exploited by attackers to execute remote commands and deploy cryptominers on developer servers. Qinglong is commonly exposed without network-level controls; update to a patched version and restrict access immediately.

### 7. Wiz Used AI Reverse Engineering to Uncover High-Severity GitHub Vulnerability
- **Source:** Dark Reading — https://www.darkreading.com/application-security/reverse-engineering-ai-unearths-high-severity-github-bug
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `github`, `appsec`, `llm`
- **Slug:** `2026-04-29-wiz-ai-reverse-engineering-github-bug`
- **Must-know:** no
- **Summary:** Wiz used an AI reverse-engineering tool to identify a high-severity GitHub vulnerability that traditional analysis would have been too costly to find. The bug is now patched; the disclosure illustrates how AI is lowering the economics of vulnerability discovery in compiled codebases, a shift that will benefit both defensive researchers and threat actors.

### 8. AI Finds 38 Security Flaws in OpenEMR Platform Used by 100,000+ Healthcare Providers
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/ai-finds-38-security-flaws-openemr
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `rce`, `appsec`, `llm`
- **Slug:** `2026-04-29-ai-finds-38-openemr-flaws`
- **Must-know:** no
- **Summary:** An AI-assisted security audit of OpenEMR — used by more than 100,000 healthcare providers — surfaced 38 vulnerabilities including remote code execution, database compromise, and data theft. Healthcare organizations running OpenEMR should patch immediately; the breadth of findings suggests the platform has not undergone thorough security review and further targeted research is likely.

### 9. Claude Mythos Alarm Spreads to Japan's Financial Services Sector
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/claude-mythos-startle-japans-financial-sector
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`, `anthropic`
- **Slug:** `2026-04-30-claude-mythos-japan-financial-sector`
- **Must-know:** no
- **Summary:** Japan's financial services sector is alarmed by Anthropic's Mythos AI model amid "superhacker" framing in media, while cybersecurity experts note the reaction is disproportionate to Mythos's bounded and restricted capabilities. Finance sector CISOs should prepare evidence-based briefings to manage board-level AI risk perception without triggering reactive posture shifts.

### 10. OpenAI Publishes Root Cause Analysis of GPT-5 Goblin Behavior Quirks
- **Source:** OpenAI Blog — https://openai.com/index/where-the-goblins-came-from
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `ai-safety`, `llm`, `openai`
- **Slug:** `2026-04-29-openai-gpt5-goblin-behavior-root-cause`
- **Must-know:** no
- **Summary:** OpenAI published a post-mortem on "goblin" personality-driven behavior quirks in GPT-5, covering timeline, root cause, and fixes. The disclosure is notable for its transparency; practitioners deploying GPT-5 in production should implement behavioral monitoring and regression testing to detect output character shifts when model updates are pushed.

## Skippable

- **SoftBank Robotics/Data Center Company Eyes $100B IPO** — TechCrunch AI. Business and infrastructure news, no security angle.
- **Zig Project's Firm Anti-AI Contribution Policy** — Simon Willison. Developer policy commentary, no security news value.
- **Amazon AWS Cloud Business Surging, Capital Spending Rising** — TechCrunch AI. Earnings/financial news, no security angle.
- **Anthropic Could Raise $50B Round at $900B Valuation** — TechCrunch AI. Funding news, no security angle.
- **Elon Musk's Worst Enemy in Court is Elon Musk** — The Verge AI. Legal proceedings coverage, no security angle.
- **On the Stand, Elon Musk Can't Escape His Own Tweets** — TechCrunch AI. Legal proceedings, duplicate of Verge coverage.
- **Meta is Still Burning Money on AR/VR** — TechCrunch AI. Financial/business metrics, no security angle.
- **Satya Nadella Says He's Ready to 'Exploit' the New OpenAI Deal** — TechCrunch AI. Business partnership news, no security angle.
- **llm 0.32a1** — Simon Willison. Minor bug fix release in developer tooling, no security relevance.
- **Microsoft Says It Has Over 20M Paid Copilot Users** — TechCrunch AI. Marketing/business metrics, no security angle.
- **Google Cloud Surpasses $20B, Growth Capacity-Constrained** — TechCrunch AI. Earnings news, no security angle.
- **Google Gains 25M Subscriptions in Q1** — TechCrunch AI. Business metrics, no security angle.
- **House Approves Spy Program on Second Attempt, Senate Fate Murky** — The Record. FISA Section 702 renewal legislative update; summary too thin (no technical details, bill not yet law) to support a substantive post.
- **US, China Partner on Scam Center Takedown in Dubai** — The Record. Law enforcement operation against cryptocurrency fraud; no technical substance or IOCs.
- **Google Search Queries Hit an 'All Time High' Last Quarter** — The Verge AI. Earnings metrics, no security angle.
- **Designing Trust and Safety into Amazon Bedrock Powered Applications** — AWS Security Blog. Vendor best-practices marketing content, no news value.
