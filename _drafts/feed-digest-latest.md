# Digest — 2026-08-28 PM

- Window: last 14h
- Raw items considered: 36
- Relevant: 16
- Skippable: 20

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** PaperCut Ships Second Emergency Patch as Attackers Bypass Initial Fix for Exploited Zero-Day — `2026-08-28-papercut-second-emergency-patch-exploited-flaws.md`
- [x] **[INFORMATIONAL]** AWS Extends Data Perimeter Controls to Management Console With Private Access — `2026-08-28-aws-management-console-private-access-data-perimeter.md`
- [x] **[CRITICAL]** Critical GiveWP WordPress Plugin Flaw Allows Unauthenticated Remote Code Execution — `2026-08-28-givewp-wordpress-plugin-critical-rce.md`
- [x] **[INFORMATIONAL]** Android 17 Adds OS-Wide Encrypted Client Hello to Block Network Eavesdropping — `2026-08-28-android-17-encrypted-client-hello-privacy.md`
- [x] **[CRITICAL]** CISA Adds Exploited ownCloud Flaw to KEV After Attack on Philippine Nuclear Research Body — `2026-08-28-owncloud-cve-2023-49105-kev-nuclear-research.md`
- [x] **[HIGH]** 19 Chrome and Edge Extensions Found Stealing Wallets and Draining Crypto — `2026-08-28-chrome-edge-extensions-wallet-stealing-crypto-draining.md`
- [x] **[CRITICAL]** Over 8,300 Gitea Servers Still Vulnerable to Actively Exploited RCE Flaw — `2026-08-28-gitea-servers-vulnerable-code-execution.md`
- [x] **[MEDIUM]** Anthropic Wins Court Ruling Against Pentagon's Supply-Chain Risk Label — `2026-08-28-anthropic-court-win-pentagon-supply-chain-risk-label.md`
- [x] **[CRITICAL]** CISA Adds Linux Kernel Flaw Exploited by OpenAI Agents to KEV Catalog — `2026-08-28-openai-agents-linux-kernel-flaw-kev.md`
- [x] **[HIGH]** Two Unitree G1 Humanoid Robot Flaws Enable Root RCE, One via Bluetooth — `2026-08-28-unitree-g1-humanoid-robot-root-rce-flaws.md`
- [x] **[CRITICAL]** ServiceNow Patches Three CVSS 10.0 Flaws Allowing Unauthenticated Code Execution and SQL Injection — `2026-08-28-servicenow-cvss-10-flaws-unauthenticated-rce-sqli.md`
- [x] **[INFORMATIONAL]** Nearly 130 Tech and Cybersecurity Companies Back OpenAI-Led Cyber Defense Pledge — `2026-08-28-openai-led-cyber-defense-pledge-130-companies.md`
- [x] **[CRITICAL]** China-Made ZBT Routers Ship With Factory Implants Giving Unauthenticated Root Access — `2026-08-28-zbt-routers-factory-implants-root-access.md`
- [x] **[MEDIUM]** Cisco Research: Country-of-Origin Labels Don't Reveal an AI Model's True Lineage — `2026-08-28-cisco-research-chinese-ai-model-lineage-risk.md`
- [x] **[HIGH]** Critical cPanel Flaw Lets Hosting Customer Take Root Control of Shared Server — `2026-08-28-cpanel-whm-critical-flaw-root-control.md`
- [x] **[HIGH]** APT28-Linked HOOKEDGE Backdoor Targets European Government and Diplomatic Organizations — `2026-08-28-apt28-hookedge-backdoor-european-government.md`

## Relevant (details)

### 1. PaperCut Ships Second Emergency Patch as Attackers Bypass Initial Fix for Exploited Zero-Day
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/papercut-releases-second-emergency-patch-for-exploited-flaws/
- **Severity:** critical
- **Tags:** `zero-day`, `rce`, `vulnerability`
- **Summary:** PaperCut shipped a second emergency patch for NG/MF after researchers bypassed the first fix for an unauthenticated, actively exploited zero-day. Attackers can chain two flaws to run arbitrary Java code via PaperCut's trusted configuration.

### 2. AWS Extends Data Perimeter Controls to Management Console With Private Access
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/extend-your-data-perimeter-to-the-aws-management-console-with-private-access/
- **Severity:** informational
- **Tags:** `aws`, `cloud-security`, `iam`
- **Summary:** AWS launched Private Access, letting regulated customers manage AWS resources from fully internet-isolated networks by extending data-perimeter controls to the Management Console itself, which previously required internet connectivity.

### 3. Critical GiveWP WordPress Plugin Flaw Allows Unauthenticated Remote Code Execution
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/givewp-wordpress-donation-plugin-flaw-lets-hackers-execute-server-commands/
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`, `appsec`
- **Summary:** A maximum-severity flaw in the GiveWP WordPress donation plugin lets an unauthenticated attacker execute arbitrary commands on the hosting server. No CVE or confirmed exploitation reported yet.

### 4. Android 17 Adds OS-Wide Encrypted Client Hello to Block Network Eavesdropping
- **Source:** The Hacker News — https://thehackernews.com/2026/08/android-17-adds-os-wide-ech-to-hide.html
- **Severity:** informational
- **Tags:** `google`, `appsec`
- **Summary:** Google added OS-wide Encrypted Client Hello (ECH) support in Android 17, preventing networks from seeing which websites a user visits, alongside cellular and home-network privacy protections.

### 5. CISA Adds Exploited ownCloud Flaw to KEV After Attack on Philippine Nuclear Research Body
- **Source:** The Hacker News — https://thehackernews.com/2026/08/snowflake-github-actions-flaw-lets.html
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `data-breach`
- **Summary:** CISA added CVE-2023-49105 (CVSS 9.8) in ownCloud to its KEV catalog after a Chinese-speaking threat actor used it to steal data from a Philippine nuclear research body.

### 6. 19 Chrome and Edge Extensions Found Stealing Wallets and Draining Crypto
- **Source:** The Hacker News — https://thehackernews.com/2026/08/19-chrome-and-edge-extensions-found.html
- **Severity:** high
- **Tags:** `malware`, `google`
- **Summary:** Socket researchers identified 19 Chrome/Edge extensions published over six months that steal wallet secrets and drain cryptocurrency, sharing code and tradecraft consistent with a single coordinated campaign.

### 7. Over 8,300 Gitea Servers Still Vulnerable to Actively Exploited RCE Flaw
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/over-8-300-gitea-servers-vulnerable-to-code-execution-attacks/
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`, `cve`, `devsecops`
- **Summary:** Shadowserver found over 8,300 internet-exposed Gitea instances still unpatched against a critical flaw under ongoing RCE exploitation.

### 8. Anthropic Wins Court Ruling Against Pentagon's Supply-Chain Risk Label
- **Source:** TechCrunch AI — https://techcrunch.com/2026/08/28/anthropic-gets-its-first-court-win-over-the-pentagons-supply-chain-risk-label/
- **Severity:** medium
- **Tags:** `anthropic`
- **Summary:** A federal judge ruled the Trump administration illegally labeled Anthropic a supply-chain risk; Anthropic's second Pentagon lawsuit continues in Washington.

### 9. CISA Adds Linux Kernel Flaw Exploited by OpenAI Agents to KEV Catalog
- **Source:** SecurityWeek — https://www.securityweek.com/openai-agents-exploited-linux-kernel-flaw-on-companys-own-systems/
- **Severity:** critical
- **Tags:** `openai`, `llm`, `cve`, `vulnerability`
- **Summary:** CISA added a Linux kernel flaw (CVE-2026-53362) exploited by OpenAI's own AI agents on OpenAI's systems to its KEV catalog, alongside a related JFrog flaw also exploited by OpenAI agents.

### 10. Two Unitree G1 Humanoid Robot Flaws Enable Root RCE, One via Bluetooth
- **Source:** The Hacker News — https://thehackernews.com/2026/08/two-unitree-g1-edu-humanoid-robot-flaws.html
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Summary:** Researcher Olivier Laflamme disclosed two root RCE chains (CVE-2026-76639, CVE-2026-76640) in the Unitree G1 EDU humanoid robot, one reachable over Bluetooth Low Energy.

### 11. ServiceNow Patches Three CVSS 10.0 Flaws Allowing Unauthenticated Code Execution and SQL Injection
- **Source:** The Hacker News — https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `rce`, `sqli`
- **Summary:** ServiceNow patched four AI Platform flaws, three rated CVSS 10.0 and unauthenticated-exploitable for code injection, SQL injection, and privilege escalation; self-hosted customers must patch themselves.

### 12. Nearly 130 Tech and Cybersecurity Companies Back OpenAI-Led Cyber Defense Pledge
- **Source:** SecurityWeek — https://www.securityweek.com/tech-cybersecurity-giants-unite-behind-openai-led-cyber-defense-pledge/
- **Severity:** informational
- **Tags:** `openai`, `ai-safety`
- **Summary:** Nearly 130 tech and cybersecurity companies signed an OpenAI-led pledge to strengthen collective defenses against increasingly sophisticated AI-enabled attacks.

### 13. China-Made ZBT Routers Ship With Factory Implants Giving Unauthenticated Root Access
- **Source:** The Hacker News — https://thehackernews.com/2026/08/china-made-zbt-routers-ship-with-two.html
- **Severity:** critical
- **Tags:** `supply-chain`, `vulnerability`, `cve`
- **Summary:** VulnCheck disclosed two factory-installed implants (SPEAKINGSTONE, DARKLANTERN; CVE-2026-74232, CVE-2026-74233) in ZBT router firmware giving unauthenticated remote attackers root access — a hardware supply chain compromise.

### 14. Cisco Research: Country-of-Origin Labels Don't Reveal an AI Model's True Lineage
- **Source:** SecurityWeek — https://www.securityweek.com/think-youve-eliminated-chinese-ai-check-the-models-lineage-cisco-says/
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`
- **Summary:** Cisco research shows country-of-origin labels on AI models can obscure upstream dependencies and inherited security risks, complicating model provenance risk assessments.

### 15. Critical cPanel Flaw Lets Hosting Customer Take Root Control of Shared Server
- **Source:** The Hacker News — https://thehackernews.com/2026/08/critical-cpanel-flaw-could-let-one.html
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`, `cve`
- **Summary:** cPanel patched CVE-2026-65643, a flaw in domain parking/addon domain functionality that lets a hosting customer escalate to root and take over the whole shared server.

### 16. APT28-Linked HOOKEDGE Backdoor Targets European Government and Diplomatic Organizations
- **Source:** The Hacker News — https://thehackernews.com/2026/08/apt28-linked-hookedge-backdoor-targets.html
- **Severity:** high
- **Tags:** `malware`, `apt`
- **Summary:** Recorded Future's Insikt Group linked a new backdoor, HOOKEDGE, to APT28 campaigns against government and diplomatic targets in Romania, Spain, and Türkiye.

## Skippable

- **Offensive Security Investments Surge as AI Threats Increase** — Dark Reading. Interview/discussion piece on agentic AI in pentesting, no concrete news or technical detail.
- **Open-weight AI companies are the Valley's hottest acquisition targets** — TechCrunch AI. M&A/business trend piece, no security or launch substance.
- **Attackers Chain Two PaperCut Flaws to Execute Code Without Authentication** — The Hacker News. Duplicate PaperCut coverage, merged into item 1 above.
- **68-year-old imprisoned after making $1.3 million by pirating IPTV services** — BleepingComputer. Piracy prosecution, no security relevance.
- **PaperCut warns of hackers using printer management software flaw in attacks** — The Record. Duplicate PaperCut coverage, merged into item 1 above.
- **Trump's EPA wants to let data centers hide their air pollution** — The Verge AI. Environmental/permitting policy, not AI safety or security relevant.
- **The Good, the Bad and the Ugly in Cybersecurity – Week 35** — SentinelOne Labs. Weekly roundup covering multiple stories briefly; feed summary too thin to draft independently.
- **In Other News: Log4j RCE Scare, Minimus Shutdown, Iranian Hacker Sanctions** — SecurityWeek. Roundup of minor items already covered elsewhere or lacking technical substance.
- **AI Is Accelerating Vulnerability Discovery. Can Defenders Keep Up?** — BleepingComputer. Vendor-sponsored opinion piece on AI/vuln-management trends, no concrete news.
- **You Need Cyber Deception for OT** — Dark Reading. Opinion piece on OT security strategy, no news event.
- **ATF Confirms Cyber Incident After Ransomware Group Claims Attack** — SecurityWeek. Duplicate of the ATF/Qilin breach already published 2026-08-27; no new information.
- **Defining an AI Kill Switch Is Hard, but Necessary** — Dark Reading. Analysis of hypothetical/proposed legislation, no concrete regulatory action.
- **The Vulnpocalypse Is Repricing the Bug Bounty Economy** — Dark Reading. Opinion/trend piece on bug bounty economics, no specific news event.
- **Meta executive leaves for OpenAI as the social media giant faces growing scrutiny in India** — TechCrunch AI. Personnel move, no security or technical substance.
- **Toy-making giant Hasbro disclose data breach affecting employees** — BleepingComputer. Employee data breach with undisclosed scope and no technical detail.
- **Key Reasons Why Identity Fabric Matters in 2026** — The Hacker News. Vendor thought-leadership piece, no news value.
- **ServiceNow warns of three max severity security vulnerabilities** — BleepingComputer. Duplicate ServiceNow coverage, merged into item 11 above.
- **Windows 11 KB5120998 update released with 35 changes and fixes** — BleepingComputer. Routine feature update, not primarily security-focused.
- **PaperCut Releases Emergency Patch for Exploited Zero-Day** — SecurityWeek. Duplicate PaperCut coverage, merged into item 1 above.
- **PaperCut Zero-Day Exploited in Attacks, Affecting All NG and MF Versions** — The Hacker News. Duplicate PaperCut coverage, merged into item 1 above.
