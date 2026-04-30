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
- **Severity:** critical
- **Tags:** `rce`, `supply-chain`, `npm`, `github`, `google`, `vulnerability`, `cve`
- **Summary:** A CVSS 10 flaw in the official `@google/gemini-cli` npm package and `google-github-actions/run-gemini-cli` GitHub Actions workflow let unprivileged attackers load malicious Gemini configuration and execute arbitrary commands on host systems. Update immediately; treat runner environments from affected versions as potentially compromised.

### 2. Official SAP npm Packages Compromised in TeamPCP Supply-Chain Attack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/official-sap-npm-packages-compromised-to-steal-credentials/
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`
- **Summary:** Multiple official SAP npm packages were backdoored by TeamPCP to steal developer credentials and authentication tokens. Published under SAP's official namespace, the packages were trusted by enterprise CI/CD pipelines — rotate all credentials from affected systems and audit package lock files immediately.

### 3. Sandhills Medical Ransomware Breach Affects 170,000 Patients
- **Source:** SecurityWeek — https://www.securityweek.com/sandhills-medical-says-ransomware-breach-affects-170000/
- **Severity:** high
- **Tags:** `ransomware`, `data-breach`
- **Summary:** Sandhills Medical disclosed an Inc Ransom breach affecting 170,000 individuals nearly one year after the initial attack. The delayed disclosure highlights persistent HIPAA notification failures in the healthcare sector.

### 4. Silver Fox Deploys New ABCDoor Backdoor Alongside ValleyRAT in Tax-Lure Campaign
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/silver-fox-tax-notification-campaign/119575/
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Summary:** Silver Fox APT is targeting organizations in Russia and India via tax-authority impersonation, delivering ValleyRAT alongside the new ABCDoor backdoor. New custom tooling signals active investment in the group's malware infrastructure.

### 5. WordPress Redirect Plugin Hid Dormant Backdoor for Five Years Across 70,000 Sites
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/popular-wordpress-redirect-plugin-hid-dormant-backdoor-for-years/
- **Severity:** high
- **Tags:** `supply-chain`, `appsec`, `malware`
- **Summary:** The Quick Page/Post Redirect plugin, on 70,000+ WordPress sites, contained a backdoor enabling arbitrary code injection added five years ago and undetected until now. Remove the plugin immediately and audit affected sites for unauthorized modifications.

### 6. Qinglong Task Scheduler RCE Under Active Exploitation for Cryptomining
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-exploit-rce-flaws-in-qinglong-task-scheduler-for-cryptomining/
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `malware`
- **Summary:** Two authentication bypass flaws in the Qinglong open-source task scheduler are being actively exploited to run arbitrary commands and deploy cryptominers. Update and restrict access immediately; unpatched exposed instances should be treated as compromised.

### 7. Wiz Used AI Reverse Engineering to Uncover High-Severity GitHub Vulnerability
- **Source:** Dark Reading — https://www.darkreading.com/application-security/reverse-engineering-ai-unearths-high-severity-github-bug
- **Severity:** high
- **Tags:** `vulnerability`, `github`, `appsec`, `llm`
- **Summary:** Wiz's AI reverse-engineering tool found a high-severity GitHub vulnerability that traditional analysis would have been too costly to uncover. The bug is patched; the case illustrates how AI is shifting vulnerability discovery economics for both defenders and attackers.

### 8. AI Finds 38 Security Flaws in OpenEMR Platform Used by 100,000+ Healthcare Providers
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/ai-finds-38-security-flaws-openemr
- **Severity:** high
- **Tags:** `vulnerability`, `rce`, `appsec`, `llm`
- **Summary:** An AI-assisted audit of OpenEMR surfaced 38 vulnerabilities including RCE, database compromise, and data theft in a platform used by 100,000+ healthcare providers. Patch immediately; the breadth of findings suggests OpenEMR has not received thorough prior security review and more targeted research will likely follow.

### 9. Claude Mythos Alarm Spreads to Japan's Financial Services Sector
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/claude-mythos-startle-japans-financial-sector
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`, `anthropic`
- **Summary:** Japan's financial sector is alarmed by Mythos as a "superhacker" AI while security experts see the reaction as disproportionate. Finance CISOs should prepare calibrated, evidence-based briefings to address board-level AI threat perception without reactive posture shifts.

### 10. OpenAI Publishes Root Cause Analysis of GPT-5 Goblin Behavior Quirks
- **Source:** OpenAI Blog — https://openai.com/index/where-the-goblins-came-from
- **Severity:** informational
- **Tags:** `ai-safety`, `llm`, `openai`
- **Summary:** OpenAI's post-mortem on unexpected "goblin" personality quirks in GPT-5 covers timeline, root cause, and fixes — rare transparency on model behavior anomalies. Practitioners deploying GPT-5 should implement behavioral monitoring to catch output character shifts when model updates are pushed.

## Skippable

- **SoftBank Robotics/Data Center Company Eyes $100B IPO** — TechCrunch AI. Business and infrastructure news, no security angle.
- **Zig Project's Firm Anti-AI Contribution Policy** — Simon Willison. Developer policy commentary, no security news value.
- **Amazon AWS Cloud Business Surging, Capital Spending Rising** — TechCrunch AI. Earnings/financial news, no security angle.
- **Anthropic Could Raise $50B Round at $900B Valuation** — TechCrunch AI. Funding news, no security angle.
- **Elon Musk's Worst Enemy in Court is Elon Musk** — The Verge AI. Legal proceedings coverage, no security angle.
- **On the Stand, Elon Musk Can't Escape His Own Tweets** — TechCrunch AI. Legal proceedings, duplicate Verge coverage.
- **Meta is Still Burning Money on AR/VR** — TechCrunch AI. Financial/business metrics, no security angle.
- **Satya Nadella Says He's Ready to 'Exploit' the New OpenAI Deal** — TechCrunch AI. Business partnership news, no security angle.
- **llm 0.32a1** — Simon Willison. Minor bug fix release in developer tooling, no security relevance.
- **Microsoft Says It Has Over 20M Paid Copilot Users** — TechCrunch AI. Marketing/business metrics, no security angle.
- **Google Cloud Surpasses $20B, Growth Capacity-Constrained** — TechCrunch AI. Earnings news, no security angle.
- **Google Gains 25M Subscriptions in Q1** — TechCrunch AI. Business metrics, no security angle.
- **House Approves Spy Program on Second Attempt, Senate Fate Murky** — The Record. FISA 702 renewal; summary too thin to support a substantive post and bill not yet signed into law.
- **US, China Partner on Scam Center Takedown in Dubai** — The Record. Law enforcement action against crypto fraud; no technical substance or IOCs.
- **Google Search Queries Hit an 'All Time High' Last Quarter** — The Verge AI. Earnings metrics, no security angle.
- **Designing Trust and Safety into Amazon Bedrock Powered Applications** — AWS Security Blog. Vendor best-practices marketing content, no news value.
