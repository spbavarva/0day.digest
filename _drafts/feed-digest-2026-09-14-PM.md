# Digest — 2026-09-14 PM

- Window: last 14h
- Raw items considered: 22
- Relevant: 9
- Skippable: 13

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Revolut Discloses Data Breach After Fraudsters Impersonate Government Agency — `2026-09-14-revolut-data-breach-government-impersonation.md`
- [x] **[CRITICAL]** Chinese Hackers Exploit Critical Tencent Software Flaw for One-Click Code Execution — `2026-09-14-chinese-hackers-exploit-tencent-ime-flaw.md`
- [x] **[INFORMATIONAL]** Microsoft Publishes 'Humanist AI' Code of Conduct Amid Safety Concerns — `2026-09-14-microsoft-humanist-ai-code-of-conduct.md`
- [x] **[INFORMATIONAL]** Unit 42 Details Behavioral Clustering Model for Cloud Identity Threat Detection — `2026-09-14-unit42-behavioral-clustering-cloud-identities.md`
- [x] **[HIGH]** Three JFrog Artifactory Flaws Exploited for Backdoor Deployment — `2026-09-14-jfrog-artifactory-flaws-backdoor-deployment.md`
- [x] **[CRITICAL]** ConnectWise Patches ScreenConnect Vulnerability Exploited in Worm-Like Attacks — `2026-09-14-connectwise-screenconnect-worm-vulnerability.md`
- [x] **[HIGH]** Malicious Twitch Browser Extension Leaks OAuth Tokens From Nearly 31,000 Users — `2026-09-14-malicious-twitch-extension-oauth-token-leak.md`
- [x] **[CRITICAL]** CISA Warns Hackers Are Exploiting Max-Severity GitLab Flaw — `2026-09-14-cisa-max-severity-gitlab-flaw-exploited.md`
- [x] **[INFORMATIONAL]** Perplexity Puts GPT-6 Astra in Charge of End-to-End Production Systems — `2026-09-14-perplexity-gpt-6-astra-production-systems.md`

## Relevant (details)

### 1. Revolut Discloses Data Breach After Fraudsters Impersonate Government Agency
- **Source:** The Record (Recorded Future) — https://therecord.media/revolut-scam-crypto-impersonation
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `revolut-data-breach-government-impersonation`
- **Must-know:** no
- **Summary:** Revolut disclosed a data breach after fraudsters using a legitimate government email account submitted fraudulent requests, leading Revolut to disclose customer financial info and passport details. The exact number of affected customers was not confirmed.

### 2. Chinese Hackers Exploit Critical Tencent Software Flaw for One-Click Code Execution
- **Source:** SecurityWeek — https://www.securityweek.com/chinese-hackers-exploit-critical-tencent-software-flaw-for-one-click-code-execution/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `chinese-hackers-exploit-tencent-ime-flaw`
- **Must-know:** yes
- **Summary:** Chinese threat actors are exploiting a critical flaw in Tencent's Windows IME software that allows remote code execution with minimal user interaction. Active exploitation is already underway.

### 3. Microsoft Publishes 'Humanist AI' Code of Conduct Amid Safety Concerns
- **Source:** The Verge — https://www.theverge.com/news/994566/microsoft-humanist-ai-code-of-conduct
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-safety`, `microsoft`, `anthropic`
- **Slug:** `microsoft-humanist-ai-code-of-conduct`
- **Must-know:** no
- **Summary:** Microsoft published a 37-page "humanist AI" code of conduct amid rising safety concerns, following Anthropic CEO Dario Amodei's weekend call for a coordinated AI development slowdown. The move reflects growing industry unease about AI progress outpacing safe deployment.

### 4. Unit 42 Details Behavioral Clustering Model for Cloud Identity Threat Detection
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `cloud-security`, `iam`, `cspm`
- **Slug:** `unit42-behavioral-clustering-cloud-identities`
- **Must-know:** no
- **Summary:** Unit 42 built a behavioral clustering model that maps cloud identity roles from audit logs using standard SQL queries. The technique enables continuous, low-overhead identity threat detection for defenders.

### 5. Three JFrog Artifactory Flaws Exploited for Backdoor Deployment
- **Source:** SecurityWeek — https://www.securityweek.com/three-jfrog-artifactory-flaws-exploited-for-backdoor-deployment/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`, `cve`
- **Slug:** `jfrog-artifactory-flaws-backdoor-deployment`
- **Must-know:** no
- **Summary:** Attackers are exploiting three JFrog Artifactory flaws to bypass authentication and escalate privileges to administrator, then deploy backdoors. Patch status was not confirmed in the source reporting.

### 6. ConnectWise Patches ScreenConnect Vulnerability Exploited in Worm-Like Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/connectwise-patches-screenconnect-vulnerability-exploited-in-worm-like-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `connectwise-screenconnect-worm-vulnerability`
- **Must-know:** yes
- **Summary:** ConnectWise patched a ScreenConnect flaw that was exploited in worm-like attacks before the fix shipped, allowing unauthorized file transfer and execution through active remote sessions. Admins should update immediately.

### 7. Malicious Twitch Browser Extension Leaks OAuth Tokens From Nearly 31,000 Users
- **Source:** The Hacker News — https://thehackernews.com/2026/09/malicious-twitch-browser-extension.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `malware`, `supply-chain`
- **Slug:** `malicious-twitch-extension-oauth-token-leak`
- **Must-know:** no
- **Summary:** A malicious Twitch browser extension distributed on the Chrome Web Store and Firefox Add-Ons leaked OAuth tokens for nearly 31,000 users. Stolen tokens were routed to proxy servers run by a Russian commercial bot service.

### 8. CISA Warns Hackers Are Exploiting Max-Severity GitLab Flaw
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-hackers-now-exploit-max-severity-gitlab-flaw-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `gitlab`
- **Slug:** `cisa-max-severity-gitlab-flaw-exploited`
- **Must-know:** yes
- **Summary:** CISA warned that attackers are actively exploiting a maximum-severity GitLab vulnerability. Organizations running self-managed GitLab instances should patch immediately.

### 9. Perplexity Puts GPT-6 Astra in Charge of End-to-End Production Systems
- **Source:** OpenAI Blog — https://openai.com/index/perplexity-improving-accuracy-with-astra
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `openai`, `llm`
- **Slug:** `perplexity-gpt-6-astra-production-systems`
- **Must-know:** no
- **Summary:** Perplexity is using OpenAI's GPT-6 Astra model to write communications, modify software, and monitor production systems with far fewer human check-ins than earlier models required. The case study illustrates a shift toward higher-autonomy AI agents on live production infrastructure.

## Skippable

- **[Virtual Event] What Every Enterprise Should Know About Securing Cloud Assets in the Age of AI** — Dark Reading. Event promo, not news.
- **[Virtual Event] Building a Secure AI Strategy for the Enterprise** — Dark Reading. Event promo, not news.
- **Personal, Financial Info Exposed in Revolut Data Breach** — SecurityWeek. Duplicate coverage of the Revolut breach; see item 1 (The Record/BleepingComputer).
- **The Race to Control AI and Protect What Makes Us Human** — SecurityWeek. Opinion piece without concrete news value.
- **Webinar: How malicious OAuth apps can lead to Google Workspace breaches** — BleepingComputer. Webinar promo, not news.
- **AI Changed the Exposure Problem. Validation Needs to Change With It.** — The Hacker News. Vendor-style marketing content, no specific incident.
- **CISOs Race to Control AI Agents Without Destroying Their Value** — SecurityWeek. Generic trend/opinion piece with no specific incident or technical finding.
- **Telus Warns Customers of Account Breaches** — SecurityWeek. Generic breach disclosure without technical substance (credential-stuffing style, no TTPs/IOCs).
- **Microsoft: September updates cause RDS failures on Windows Server** — BleepingComputer. Routine patch bug, not a security issue.
- **Revolut discloses data breach exposing financial info, passports** — BleepingComputer. Duplicate coverage of the Revolut breach; see item 1.
- **Microsoft: September updates break audio on some Windows PCs** — BleepingComputer. Routine patch bug, not a security issue.
- **commit-rewriter 0.1** — Simon Willison. Niche personal dev tool release, no security/AI substance.
- **shot-scraper 1.12** — Simon Willison. Niche personal tool update, no security/AI substance.
