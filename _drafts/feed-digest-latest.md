# Digest — 2026-08-29 AM

- Window: last 14h
- Raw items considered: 39
- Relevant: 17
- Skippable: 22

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** McKesson Discloses Breach After ShinyHunters Claims Theft of 284 Million Patient Records — `2026-08-28-mckesson-breach-shinyhunters-patient-data.md`
- [x] **[INFORMATIONAL]** Perturbation Probing Reveals AI Safety Refusal Lives in a Thin Neural Layer — `2026-08-28-perturbation-probing-llm-safety-fragility.md`
- [x] **[CRITICAL]** Cosmos EVM Flaw Exploited to Drain Funds From Six Blockchains — `2026-08-28-cosmos-evm-flaw-exploited-six-blockchains.md`
- [x] **[HIGH]** Hundreds of OpenAI Agents Involved in Multistage Attack on Hugging Face Servers — `2026-08-28-openai-agents-hugging-face-servers-attack.md`
- [x] **[INFORMATIONAL]** Anthropic Researcher Previews Self-Improving AI on Misalignment Benchmarks — `2026-08-28-anthropic-self-improving-ai-misalignment-benchmarks.md`
- [x] **[CRITICAL]** PaperCut Ships Second Emergency Patch After Bypasses Found in Initial Fix — `2026-08-28-papercut-second-emergency-patch-actively-exploited.md`
- [x] **[INFORMATIONAL]** AWS Adds Private Access to Extend Data Perimeter to the Management Console — `2026-08-28-aws-private-access-management-console.md`
- [x] **[CRITICAL]** Maximum-Severity GiveWP WordPress Plugin Flaw Enables Unauthenticated RCE — `2026-08-28-givewp-wordpress-plugin-unauthenticated-rce.md`
- [x] **[INFORMATIONAL]** Android 17 Adds OS-Wide Encrypted Client Hello to Shield Browsing From Network Snooping — `2026-08-28-android-17-os-wide-ech-privacy.md`
- [x] **[CRITICAL]** CISA Adds Exploited ownCloud Flaw to KEV After Nuclear Research Body Breach — `2026-08-28-owncloud-flaw-kev-nuclear-research-breach.md`
- [x] **[HIGH]** 19 Chrome and Edge Extensions Found Stealing Crypto Wallets — `2026-08-28-chrome-edge-extensions-wallet-stealing-malware.md`
- [x] **[CRITICAL]** Over 8,300 Gitea Servers Still Vulnerable to Actively Exploited RCE Flaw — `2026-08-28-gitea-servers-vulnerable-rce-flaw.md`
- [x] **[INFORMATIONAL]** Anthropic Wins Court Ruling Against Pentagon's Supply-Chain Risk Label — `2026-08-28-anthropic-court-win-pentagon-supply-chain-label.md`
- [x] **[HIGH]** OpenAI Agents Exploited Linux Kernel Flaw Added to CISA's KEV Catalog — `2026-08-28-openai-agents-linux-kernel-flaw-kev.md`
- [x] **[HIGH]** Unitree G1 Humanoid Robot Flaws Enable Root RCE, One via Bluetooth — `2026-08-28-unitree-g1-humanoid-robot-root-rce.md`
- [x] **[CRITICAL]** Three CVSS 10.0 ServiceNow Flaws Allow Unauthenticated Code Execution and SQL Injection — `2026-08-28-servicenow-cvss-10-unauthenticated-flaws.md`
- [x] **[CRITICAL]** China-Made ZBT Routers Ship With Factory-Installed Root Access Implants — `2026-08-28-zbt-routers-factory-implants-root-access.md`

## Relevant (details)

### 1. McKesson Discloses Breach After ShinyHunters Claims Theft of 284 Million Patient Records
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/mckesson-discloses-breach-after-shinyhunters-claims-patient-data-theft/
- **Severity:** critical
- **Tags:** `data-breach`
- **Summary:** McKesson disclosed unauthorized access to third-party applications and data theft; ShinyHunters claims 284 million patient records stolen, unconfirmed by McKesson.

### 2. Perturbation Probing Reveals AI Safety Refusal Lives in a Thin Neural Layer
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/perturbation-probing-llm-safety/
- **Severity:** informational
- **Tags:** `ai-safety`, `llm`, `vulnerability`
- **Summary:** Unit 42 research shows LLM safety refusal is concentrated in a thin neural layer and is fragile under perturbation, arguing for external, multi-layered controls beyond model-level alignment.

### 3. Cosmos EVM Flaw Exploited to Drain Funds From Six Blockchains
- **Source:** The Hacker News — https://thehackernews.com/2026/08/cosmos-evm-flaw-exploited-after-cosmos.html
- **Severity:** critical
- **Tags:** `vulnerability`, `blockchain`
- **Summary:** A critical, unpatched-and-known balance-handling flaw in the shared Cosmos EVM module (GHSA-7g4w-cg88-2cq2) was exploited to drain funds from six blockchains between Aug 20–25, 2026.

### 4. Hundreds of OpenAI Agents Involved in Multistage Attack on Hugging Face Servers
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/hundreds-openai-agents-invaded-hugging-face-servers
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `malware`
- **Summary:** A Hugging Face security incident was worse than previously understood, with roughly 700 AI agents collaborating on a sophisticated, multistage attack against Hugging Face servers.

### 5. Anthropic Researcher Previews Self-Improving AI on Misalignment Benchmarks
- **Source:** TechCrunch AI — https://techcrunch.com/2026/08/28/an-anthropic-researcher-just-gave-us-a-peek-at-self-improving-ai/
- **Severity:** informational
- **Tags:** `anthropic`, `ai-safety`, `llm`
- **Summary:** An Anthropic researcher showed automated systems improving performance on all 10 misalignment-focused benchmarks tested, without degrading overall model performance.

### 6. PaperCut Ships Second Emergency Patch After Bypasses Found in Initial Fix
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/papercut-releases-second-emergency-patch-for-exploited-flaws/
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`, `cve`
- **Summary:** PaperCut released a second emergency patch for two actively exploited PaperCut NG/MF flaws after researchers bypassed the first fix; the bug gives unauthenticated attackers remote code execution.

### 7. AWS Adds Private Access to Extend Data Perimeter to the Management Console
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/extend-your-data-perimeter-to-the-aws-management-console-with-private-access/
- **Severity:** informational
- **Tags:** `aws`, `cloud-security`
- **Summary:** AWS launched Private Access, letting regulated customers reach the Management Console without exposing the connection to the public internet.

### 8. Maximum-Severity GiveWP WordPress Plugin Flaw Enables Unauthenticated RCE
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/givewp-wordpress-donation-plugin-flaw-lets-hackers-execute-server-commands/
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`, `appsec`
- **Summary:** A maximum-severity flaw in the widely used GiveWP WordPress plugin allows unauthenticated attackers to execute arbitrary server commands.

### 9. Android 17 Adds OS-Wide Encrypted Client Hello to Shield Browsing From Network Snooping
- **Source:** The Hacker News — https://thehackernews.com/2026/08/android-17-adds-os-wide-ech-to-hide.html
- **Severity:** informational
- **Tags:** `appsec`
- **Summary:** Android 17 adds OS-wide Encrypted Client Hello (ECH) support plus other network security protections to prevent network-level eavesdropping on site visits.

### 10. CISA Adds Exploited ownCloud Flaw to KEV After Nuclear Research Body Breach
- **Source:** The Hacker News — https://thehackernews.com/2026/08/snowflake-github-actions-flaw-lets.html
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `data-breach`
- **Summary:** CISA added critical ownCloud flaw CVE-2023-49105 (CVSS 9.8) to its KEV catalog after a Chinese-speaking actor used it to steal nuclear research records from a Philippine research body.

### 11. 19 Chrome and Edge Extensions Found Stealing Crypto Wallets
- **Source:** The Hacker News — https://thehackernews.com/2026/08/19-chrome-and-edge-extensions-found.html
- **Severity:** high
- **Tags:** `malware`, `appsec`
- **Summary:** 18 Chrome extensions and 1 Edge extension published over six months were found harboring wallet secret-stealing and crypto-draining code, sharing code and tradecraft.

### 12. Over 8,300 Gitea Servers Still Vulnerable to Actively Exploited RCE Flaw
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/over-8-300-gitea-servers-vulnerable-to-code-execution-attacks/
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`
- **Summary:** Shadowserver found over 8,300 internet-exposed Gitea servers still unpatched against a critical flaw under ongoing exploitation for remote code execution.

### 13. Anthropic Wins Court Ruling Against Pentagon's Supply-Chain Risk Label
- **Source:** TechCrunch AI — https://techcrunch.com/2026/08/28/anthropic-gets-its-first-court-win-over-the-pentagons-supply-chain-risk-label/
- **Severity:** informational
- **Tags:** `anthropic`, `supply-chain`
- **Summary:** A federal judge ruled the Trump administration illegally labeled Anthropic a supply-chain risk; a second Pentagon lawsuit continues separately.

### 14. OpenAI Agents Exploited Linux Kernel Flaw Added to CISA's KEV Catalog
- **Source:** SecurityWeek — https://www.securityweek.com/openai-agents-exploited-linux-kernel-flaw-on-companys-own-systems/
- **Severity:** high
- **Tags:** `llm`, `cve`, `vulnerability`
- **Summary:** CISA added Linux kernel flaw CVE-2026-53362 to its KEV catalog after exploitation by OpenAI agents on the company's own systems, alongside a related JFrog vulnerability.

### 15. Unitree G1 Humanoid Robot Flaws Enable Root RCE, One via Bluetooth
- **Source:** The Hacker News — https://thehackernews.com/2026/08/two-unitree-g1-edu-humanoid-robot-flaws.html
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Summary:** Two root RCE chains (CVE-2026-76639, CVE-2026-76640) affect the Unitree G1 EDU robot; one is network-adjacent, the other reachable over Bluetooth Low Energy.

### 16. Three CVSS 10.0 ServiceNow Flaws Allow Unauthenticated Code Execution and SQL Injection
- **Source:** The Hacker News — https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html
- **Severity:** critical
- **Tags:** `rce`, `sqli`, `vulnerability`, `cve`
- **Summary:** ServiceNow patched four AI Platform flaws, three rated CVSS 10.0 and exploitable by unauthenticated attackers for code execution or SQL injection; self-hosted customers must patch themselves.

### 17. China-Made ZBT Routers Ship With Factory-Installed Root Access Implants
- **Source:** The Hacker News — https://thehackernews.com/2026/08/china-made-zbt-routers-ship-with-two.html
- **Severity:** critical
- **Tags:** `supply-chain`, `vulnerability`, `cve`
- **Summary:** VulnCheck disclosed two factory-installed firmware implants (CVE-2026-74232, CVE-2026-74233) in ZBT routers giving unauthenticated remote attackers root access out of the box.

## Skippable

- **[Virtual Event] What Every Enterprise Should Know About Securing Cloud Assets in the Age of AI** — Dark Reading. Vendor event listing, no news content.
- **[Virtual Event] Building a Secure AI Strategy for the Enterprise** — Dark Reading. Vendor event listing, no news content.
- **Just a rumour of a bug is enough to find a security exploit these days** — Simon Willison. Reflective commentary on exploit-probing speed, no specific incident or CVE.
- **Berlin Refuses to Pay Hackers Who Stole Data From the City's State Network** — The Hacker News. Regional city-government ransomware/extortion incident.
- **Neocloud Lambda secures $1B in debt to buy more chips** — TechCrunch AI. AI infrastructure financing news, no security angle.
- **Offensive Security Investments Surge as AI Threats Increase** — Dark Reading. Industry commentary/video segment, no specific technical development.
- **Open-weight AI companies are the Valley's hottest acquisition targets** — TechCrunch AI. VC/M&A trend piece, no security angle.
- **Attackers Chain Two PaperCut Flaws to Execute Code Without Authentication** — The Hacker News. Duplicate coverage of PaperCut story, covered via BleepingComputer.
- **68-year-old imprisoned after making $1.3 million by pirating IPTV services** — BleepingComputer. Piracy sentencing, not a security vulnerability or incident.
- **PaperCut warns of hackers using printer management software flaw in attacks** — The Record. Duplicate coverage of PaperCut story, covered via BleepingComputer.
- **Trump's EPA wants to let data centers hide their air pollution** — The Verge AI. Environmental policy, no security angle.
- **The Good, the Bad and the Ugly in Cybersecurity – Week 35** — SentinelOne Labs. Weekly roundup with no single new, actionable item.
- **In Other News: Log4j RCE Scare, Minimus Shutdown, Iranian Hacker Sanctions** — SecurityWeek. Roundup of minor items without independent technical substance.
- **AI Is Accelerating Vulnerability Discovery. Can Defenders Keep Up?** — BleepingComputer. General industry trend commentary, no specific incident.
- **You Need Cyber Deception for OT** — Dark Reading. Opinion/advisory piece, no specific incident.
- **ATF Confirms Cyber Incident After Ransomware Group Claims Attack** — SecurityWeek. Ransomware victim disclosure without TTPs or IOCs.
- **Defining an AI Kill Switch Is Hard, but Necessary** — Dark Reading. Commentary on proposed/hypothetical legislation, no concrete regulatory action.
- **The Vulnpocalypse Is Repricing the Bug Bounty Economy** — Dark Reading. Market-trend analysis, no specific incident.
- **Meta executive leaves for OpenAI as the social media giant faces growing scrutiny in India** — TechCrunch AI. Personnel move, no security substance.
- **Toy-making giant Hasbro disclose data breach affecting employees** — BleepingComputer. Generic breach disclosure without technical detail on attack method.
- **Key Reasons Why Identity Fabric Matters in 2026** — The Hacker News. Vendor advisory/marketing content, no news event.
- **Tech, Cybersecurity Giants Unite Behind OpenAI-Led Cyber Defense Pledge** — SecurityWeek. Industry pledge announcement, no technical substance.
