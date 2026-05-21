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
- **Severity:** critical
- **Tags:** `zero-day`, `microsoft`, `vulnerability`, `cve`, `privilege-escalation`
- **Summary:** Two Microsoft Defender vulnerabilities (UnDefend and RedSun) were actively exploited before patches shipped on May 21. Exploitation enables SYSTEM-level privilege escalation or DoS; organizations should confirm patch application immediately.

### 2. GitHub Breach Traced to Poisoned Nx Console VS Code Extension in TanStack Supply Chain Attack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/github-links-repo-breach-to-tanstack-npm-supply-chain-attack/
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `npm`, `data-breach`
- **Summary:** GitHub confirmed 3,800 internal repos were stolen after a poisoned Nx Console VS Code extension — part of the TanStack npm supply chain attack — compromised an employee device. Claimed by threat group TeamPCP.

### 3. 9-Year-Old Linux Kernel Flaw Allows Unprivileged Users to Execute Commands as Root
- **Source:** The Hacker News — https://thehackernews.com/2026/05/9-year-old-linux-kernel-flaw-enables.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`, `linux`
- **Summary:** CVE-2026-46333 (CVSS 5.5) has lurked in the Linux kernel for nine years, allowing unprivileged local users to read sensitive files and run commands as root on major distros. Distro-level patches are expected via standard security channels.

### 4. Drupal Core Patches Highly Critical RCE Flaw Affecting PostgreSQL Sites
- **Source:** The Hacker News — https://thehackernews.com/2026/05/highly-critical-drupal-core-flaw.html
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`, `appsec`
- **Summary:** CVE-2026-9082 (CVSS 6.5) in Drupal Core's database abstraction API enables RCE, privilege escalation, or information disclosure on PostgreSQL-backed sites. Drupal rates it "highly critical" and has released patches.

### 5. Attackers Bypass SonicWall VPN MFA via Incomplete Patch, Deploy Ransomware
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-bypass-sonicwall-vpn-mfa-due-to-incomplete-patching/
- **Severity:** high
- **Tags:** `ransomware`, `vulnerability`, `vpn`
- **Summary:** Threat actors exploited incomplete patching on SonicWall Gen6 SSL-VPN to bypass MFA after brute-forcing credentials, then deployed ransomware. Operators should verify full patch application, not just partial updates.

### 6. Google AI Likely Behind Surge in Chrome Vulnerability Discoveries
- **Source:** SecurityWeek — https://www.securityweek.com/googles-surge-in-chrome-vulnerability-discoveries-likely-driven-by-ai/
- **Severity:** medium
- **Tags:** `google`, `vulnerability`, `llm`, `appsec`
- **Summary:** More than 200 recent Chrome vulnerabilities were credited to internal Google discovery, a surge attributed to AI-assisted fuzzing. AI-driven security research is now outpacing external researchers at scale inside major browser teams.

### 7. China and Russia Pledge Joint AI Development and Cyberspace Cooperation
- **Source:** The Record (Recorded Future) — https://therecord.media/russia-and-china-pledge-cooperation-2026
- **Severity:** medium
- **Tags:** `ai-safety`, `cloud-security`, `geopolitics`
- **Summary:** Xi and Putin signed a joint statement committing to deeper AI, satellite internet, and open-source software cooperation aimed at reducing Western technology dependence. The alignment raises the prospect of tighter coordination between their advanced threat ecosystems.

### 8. Ukraine Identifies 18-Year-Old Running Infostealer Operation That Stole 28,000 Accounts
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/ukraine-identifies-infostealer-operator-tied-to-28-000-stolen-accounts/
- **Severity:** medium
- **Tags:** `malware`, `data-breach`, `infostealer`
- **Summary:** Ukrainian and U.S. law enforcement identified a teen from Odesa operating an infostealer campaign that stole roughly 28,000 accounts from a California-based online store. The case illustrates the low barrier to running commodity infostealer operations.

### 9. Fake Android Apps Use WebView Injection and OTP Interception for Carrier Billing Fraud
- **Source:** Dark Reading — https://www.darkreading.com/mobile-security/fake-android-apps-carrier-billing-fraud
- **Severity:** medium
- **Tags:** `malware`, `phishing`, `android`
- **Summary:** Disguised Android apps automate carrier billing fraud by chaining WebView automation, JavaScript injection, and OTP interception to subscribe victims to premium services without consent or visible interaction.

### 10. AWS Bedrock AgentCore Uses Cedar Policy Language to Secure Agentic AI Workflows
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/why-policy-in-amazon-bedrock-agentcore-chose-cedar-for-securing-agentic-workflows/
- **Severity:** informational
- **Tags:** `llm`, `ai-safety`, `aws`, `cloud-security`
- **Summary:** AWS details how Bedrock AgentCore enforces authorization on AI agents using the Cedar policy language, addressing LLM non-determinism and prompt injection risk with auditable, expressive policies. A practical reference for teams building agentic access controls on AWS.

## Skippable

- **Microsoft Patches Exploited UnDefend and RedSun Defender Zero-Days** — SecurityWeek. Duplicate of item #1; BleepingComputer selected as primary source.
- **Meta lays off thousands of employees to offset AI investments** — The Verge AI. HR/business news, no security angle.
- **Supply Chain Security Crisis: Too Many Vulnerabilities, Too Little Visibility** — SecurityWeek. Opinion/analysis without specific news value; no new CVEs or incidents.
- **GitHub Internal Repositories Breached via Malicious Nx Console VS Code Extension** — The Hacker News. Duplicate of item #2; BleepingComputer selected as primary source.
- **In SpaceX's IPO, Elon Musk is a risk factor** — The Verge AI. Business/financial analysis, no security angle.
- **Jensen Huang says he's found a 'brand new' $200B market for Nvidia** — TechCrunch AI. Business prediction, no security angle.
- **Anthropic says it's about to have its first profitable quarter** — TechCrunch AI. Financial news, no security or model-launch angle.
- **Clouted wants to take the guesswork out of making short videos go viral** — TechCrunch AI. Non-security SaaS funding announcement.
- **Quoting SpaceX S-1** — Simon Willison. Commentary on Anthropic-xAI compute deal; business/financial, no security angle.
- **xAI burned $6.4B last year — SpaceX's IPO filing shows why the spending is far from over** — TechCrunch AI. Business/financial, no security angle.
- **Nvidia posts another record quarter, reveals $43B of holdings in startups** — TechCrunch AI. Earnings news, no security angle.
- **Musk's xAI is being sued over its data center generators — now it's buying $2.8B more** — TechCrunch AI. Legal/business news, no security angle.
- **Anthropic will pay xAI $1.25B per month for compute** — TechCrunch AI. Duplicate of Simon Willison item; business/financial news.
- **'Solve all diseases,' you say?** — The Verge AI. Opinion newsletter, no news value.
- **Cyber Pros Can't Decide If AI Is a Good or a Bad Thing** — Dark Reading. Opinion piece, no actionable news value.
- **GitHub Confirms Breach, 4K Internal Repos Stolen** — Dark Reading. Duplicate of item #2; BleepingComputer selected as primary source.
- **We're announcing new community investments in Missouri** — Google AI Blog. Google PR/community investment announcement, no security angle.
