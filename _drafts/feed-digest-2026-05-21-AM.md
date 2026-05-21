# Digest — 2026-05-21 AM

- Window: last 14h
- Raw items considered: 27
- Relevant: 10
- Skippable: 17

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Microsoft Patches Two Defender Zero-Days Under Active Exploitation — `2026-05-21-microsoft-defender-zero-days-actively-exploited.md`
- [x] **[CRITICAL]** GitHub Breach Traced to Poisoned Nx Console VS Code Extension in TanStack Supply Chain Attack — `2026-05-21-github-breach-tanstack-nx-console-supply-chain.md`
- [x] **[HIGH]** 9-Year-Old Linux Kernel Flaw Allows Unprivileged Users to Execute Commands as Root — `2026-05-21-linux-kernel-cve-2026-46333-lpe-root.md`
- [x] **[HIGH]** Drupal Core Patches Highly Critical RCE Flaw Affecting PostgreSQL Sites — `2026-05-21-drupal-core-cve-2026-9082-rce.md`
- [x] **[HIGH]** Attackers Bypass SonicWall VPN MFA via Incomplete Patch, Deploy Ransomware — `2026-05-20-sonicwall-vpn-mfa-bypass-ransomware.md`
- [x] **[MEDIUM]** Google AI Likely Behind Surge in Chrome Vulnerability Discoveries — `2026-05-21-google-ai-chrome-vulnerability-discovery.md`
- [x] **[MEDIUM]** China and Russia Pledge Joint AI Development and Cyberspace Cooperation — `2026-05-20-xi-putin-ai-cyberspace-cooperation-pledge.md`
- [x] **[MEDIUM]** Ukraine Identifies 18-Year-Old Running Infostealer Operation That Stole 28,000 Accounts — `2026-05-20-ukraine-infostealer-operator-28k-accounts.md`
- [x] **[MEDIUM]** Fake Android Apps Use WebView Injection and OTP Interception for Carrier Billing Fraud — `2026-05-20-fake-android-apps-carrier-billing-fraud.md`
- [x] **[INFORMATIONAL]** AWS Bedrock AgentCore Uses Cedar Policy Language to Secure Agentic AI Workflows — `2026-05-20-aws-bedrock-agentcore-cedar-agentic-security.md`

## Relevant (details)

### 1. Microsoft Patches Two Defender Zero-Days Under Active Exploitation
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/microsoft-warns-of-new-defender-zero-days-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `microsoft`, `vulnerability`, `cve`, `privilege-escalation`
- **Slug:** `2026-05-21-microsoft-defender-zero-days-actively-exploited`
- **Must-know:** yes
- **Summary:** Two Microsoft Defender vulnerabilities (UnDefend and RedSun) were actively exploited in the wild before patches shipped on May 21. Exploitation enables SYSTEM-level privilege escalation or denial-of-service; organizations should confirm patch application immediately.

### 2. GitHub Breach Traced to Poisoned Nx Console VS Code Extension in TanStack Supply Chain Attack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/github-links-repo-breach-to-tanstack-npm-supply-chain-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `npm`, `data-breach`
- **Slug:** `2026-05-21-github-breach-tanstack-nx-console-supply-chain`
- **Must-know:** yes
- **Summary:** GitHub confirmed 3,800 internal repositories were stolen after a compromised Nx developer's machine enabled poisoning of the Nx Console VS Code extension as part of the TanStack npm supply chain attack. The breach was claimed by threat group TeamPCP.

### 3. 9-Year-Old Linux Kernel Flaw Allows Unprivileged Users to Execute Commands as Root
- **Source:** The Hacker News — https://thehackernews.com/2026/05/9-year-old-linux-kernel-flaw-enables.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`, `linux`
- **Slug:** `2026-05-21-linux-kernel-cve-2026-46333-lpe-root`
- **Must-know:** no
- **Summary:** CVE-2026-46333 (CVSS 5.5) is an improper privilege management bug present in the Linux kernel for nine years that lets an unprivileged local user disclose sensitive files and execute arbitrary commands as root. Distro-specific patches are expected via security channels.

### 4. Drupal Core Patches Highly Critical RCE Flaw Affecting PostgreSQL Sites
- **Source:** The Hacker News — https://thehackernews.com/2026/05/highly-critical-drupal-core-flaw.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`, `appsec`
- **Slug:** `2026-05-21-drupal-core-cve-2026-9082-rce`
- **Must-know:** no
- **Summary:** CVE-2026-9082 (CVSS 6.5) in Drupal Core's database abstraction API allows remote code execution, privilege escalation, or information disclosure on PostgreSQL-backed sites. Drupal rates the issue "highly critical" and has released patches.

### 5. Attackers Bypass SonicWall VPN MFA via Incomplete Patch, Deploy Ransomware
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-bypass-sonicwall-vpn-mfa-due-to-incomplete-patching/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`, `vulnerability`, `vpn`
- **Slug:** `2026-05-20-sonicwall-vpn-mfa-bypass-ransomware`
- **Must-know:** no
- **Summary:** Threat actors brute-forced SonicWall Gen6 SSL-VPN credentials and bypassed MFA due to an incompletely applied patch, then deployed ransomware tooling. Operators should verify the latest patch revision is fully applied, not just partially installed.

### 6. Google AI Likely Behind Surge in Chrome Vulnerability Discoveries
- **Source:** SecurityWeek — https://www.securityweek.com/googles-surge-in-chrome-vulnerability-discoveries-likely-driven-by-ai/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `google`, `vulnerability`, `llm`, `appsec`
- **Slug:** `2026-05-21-google-ai-chrome-vulnerability-discovery`
- **Must-know:** no
- **Summary:** Over 200 recent Chrome vulnerabilities were credited to "reported by Google," a surge researchers attribute to AI-driven fuzzing and vulnerability discovery. The trend signals that AI-assisted internal security research is outpacing external reports at scale.

### 7. China and Russia Pledge Joint AI Development and Cyberspace Cooperation
- **Source:** The Record (Recorded Future) — https://therecord.media/russia-and-china-pledge-cooperation-2026
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`, `cloud-security`, `geopolitics`
- **Slug:** `2026-05-20-xi-putin-ai-cyberspace-cooperation-pledge`
- **Must-know:** no
- **Summary:** Xi and Putin signed a joint statement pledging cooperation on AI, cyberspace governance, satellite internet, and open-source development, explicitly aimed at reducing Western technology dependence. The alignment has implications for coordination between their respective advanced persistent threat ecosystems.

### 8. Ukraine Identifies 18-Year-Old Running Infostealer Operation That Stole 28,000 Accounts
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/ukraine-identifies-infostealer-operator-tied-to-28-000-stolen-accounts/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `data-breach`, `infostealer`
- **Slug:** `2026-05-20-ukraine-infostealer-operator-28k-accounts`
- **Must-know:** no
- **Summary:** Ukrainian cyberpolice and U.S. law enforcement identified an 18-year-old from Odesa operating an infostealer campaign targeting a California-based online store, resulting in 28,000 stolen accounts. The case highlights the low barrier to entry for commodity infostealer operations.

### 9. Fake Android Apps Use WebView Injection and OTP Interception for Carrier Billing Fraud
- **Source:** Dark Reading — https://www.darkreading.com/mobile-security/fake-android-apps-carrier-billing-fraud
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`, `android`
- **Slug:** `2026-05-20-fake-android-apps-carrier-billing-fraud`
- **Must-know:** no
- **Summary:** Disguised Android apps automate carrier billing fraud via WebView automation, JavaScript injection, and OTP interception to complete unauthorized premium subscriptions without user interaction. Detection evasion is built in, making them harder to catch through standard store scanning.

### 10. AWS Bedrock AgentCore Uses Cedar Policy Language to Secure Agentic AI Workflows
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/why-policy-in-amazon-bedrock-agentcore-chose-cedar-for-securing-agentic-workflows/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `llm`, `ai-safety`, `aws`, `cloud-security`
- **Slug:** `2026-05-20-aws-bedrock-agentcore-cedar-agentic-security`
- **Must-know:** no
- **Summary:** AWS explains how Bedrock AgentCore uses the Cedar policy language to enforce authorization constraints on AI agents, addressing the non-determinism and prompt-injection exposure inherent in LLM-driven workflows. A useful reference for teams building access controls around agentic systems on AWS.

## Skippable

- **Microsoft Patches Exploited UnDefend and RedSun Defender Zero-Days** — SecurityWeek. Duplicate coverage of item #1; BleepingComputer version selected as primary.
- **Meta lays off thousands of employees to offset AI investments** — The Verge AI. HR/business news, no security angle.
- **Supply Chain Security Crisis: Too Many Vulnerabilities, Too Little Visibility** — SecurityWeek. Opinion/analysis piece without specific news value; no new CVEs or incidents disclosed.
- **GitHub Internal Repositories Breached via Malicious Nx Console VS Code Extension** — The Hacker News. Duplicate coverage of item #2; BleepingComputer version selected as primary.
- **In SpaceX's IPO, Elon Musk is a risk factor** — The Verge AI. Business/financial analysis, no security angle.
- **Jensen Huang says he's found a 'brand new' $200B market for Nvidia** — TechCrunch AI. Business prediction, no security angle.
- **Anthropic says it's about to have its first profitable quarter** — TechCrunch AI. Financial news, no security or model-launch angle.
- **Clouted wants to take the guesswork out of making short videos go viral** — TechCrunch AI. Non-security SaaS funding announcement.
- **Quoting SpaceX S-1** — Simon Willison. Commentary on Anthropic-xAI compute deal; business/financial, no security angle.
- **xAI burned $6.4B last year — SpaceX's IPO filing shows why the spending is far from over** — TechCrunch AI. Business/financial, no security angle.
- **Nvidia posts another record quarter, reveals $43B of holdings in startups** — TechCrunch AI. Earnings news, no security angle.
- **Musk's xAI is being sued over its data center generators — now it's buying $2.8B more** — TechCrunch AI. Legal/business news, no security angle.
- **Anthropic will pay xAI $1.25B per month for compute** — TechCrunch AI. Duplicate of Simon Willison item; business/financial news.
- **'Solve all diseases,' you say?** — The Verge AI. Opinion newsletter tied to Google I/O coverage; no news value.
- **Cyber Pros Can't Decide If AI Is a Good or a Bad Thing** — Dark Reading. Opinion piece without actionable news value.
- **GitHub Confirms Breach, 4K Internal Repos Stolen** — Dark Reading. Duplicate coverage of item #2; BleepingComputer version selected as primary.
- **We're announcing new community investments in Missouri** — Google AI Blog. Google PR/community investment announcement, no security angle.
