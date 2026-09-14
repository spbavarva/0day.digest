# Digest — 2026-09-14 PM

- Window: last 14h
- Raw items considered: 53
- Relevant: 18
- Skippable: 29

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Maximum-Severity GitLab Path Traversal Flaw Now Under Active Exploitation — `2026-09-14-gitlab-critical-path-traversal-actively-exploited.md`
- [x] **[CRITICAL]** Chinese Hackers Exploit Critical Tencent IME Flaw for One-Click RCE — `2026-09-14-chinese-hackers-tencent-ime-rce.md`
- [x] **[CRITICAL]** Three JFrog Artifactory Flaws Exploited for Backdoor Deployment — `2026-09-14-jfrog-artifactory-flaws-backdoor-deployment.md`
- [x] **[CRITICAL]** ConnectWise Patches ScreenConnect Flaw Exploited in Worm-Like Attacks — `2026-09-14-connectwise-screenconnect-worm-like-exploitation.md`
- [x] **[HIGH]** Japan's Digital Agency: VPN Flaw Exposed 246,000 Personnel Records — `2026-09-14-japan-digital-agency-vpn-flaw-246k-records.md`
- [x] **[HIGH]** DDRop Attack Breaks Intel TDX and AMD SEV-SNP Confidential Computing — `2026-09-14-ddrop-attack-breaks-intel-tdx-amd-sev-snp.md`
- [x] **[HIGH]** 3BB Attacker Used MeshCentral Backdoor for Root Access — `2026-09-14-3bb-meshcentral-backdoor-root-access.md`
- [x] **[HIGH]** Red Heron Exploits Gitea RCE to Compromise 13 Organizations — `2026-09-14-red-heron-gitea-rce-13-organizations.md`
- [x] **[HIGH]** Hackers Target Exposed Vite Dev Servers to Steal AWS, Azure Secrets — `2026-09-14-vite-dev-servers-aws-azure-secrets-theft.md`
- [x] **[HIGH]** Malicious Twitch Browser Extension Leaks OAuth Tokens From ~31,000 Users — `2026-09-14-twitch-extension-oauth-token-leak.md`
- [x] **[HIGH]** CISA Adds Cisco Secure Email Gateway SQL Injection to KEV Catalog — `2026-09-14-cisa-kev-cisco-secure-email-gateway-sqli.md`
- [x] **[HIGH]** Revolut Data Breach Exposes Financial Info, Passports to Fraudsters — `2026-09-14-revolut-data-breach-fraudster-government-impersonation.md`
- [x] **[MEDIUM]** Telegram Desktop Flaw Lets Hidden JavaScript Exfiltrate Messages From HTML Exports — `2026-09-14-telegram-desktop-hidden-javascript-html-export-flaw.md`
- [x] **[MEDIUM]** Hackers Hijack HBO Max Reddit Account to Push ClickFix Malware — `2026-09-14-hbo-max-reddit-clickfix-malware.md`
- [x] **[INFORMATIONAL]** Anthropic CEO: Time to Shift From Improving to Controlling AI — `2026-09-14-anthropic-ceo-controlling-ai-beijing-response.md`
- [x] **[INFORMATIONAL]** Microsoft Publishes AI Code of Conduct Amid Safety Concerns — `2026-09-14-microsoft-ai-code-of-conduct.md`
- [x] **[INFORMATIONAL]** WordPress Adds Automated Plugin Reviews to Block High-Risk Updates — `2026-09-14-wordpress-automated-plugin-review.md`
- [x] **[INFORMATIONAL]** Unit 42: Behavioral Clustering Maps Cloud Identities for Threat Detection — `2026-09-14-unit42-behavioral-clustering-cloud-identities.md`

## Relevant (details)

### 1. Maximum-Severity GitLab Path Traversal Flaw Now Under Active Exploitation
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/maximum-severity-gitlab-flaw-supply-chains-risk
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `supply-chain`
- **Slug:** `gitlab-critical-path-traversal-actively-exploited`
- **Must-know:** no
- **Summary:** CVE-2026-85706 is a maximum-severity (CVSS 10) path traversal vulnerability affecting GitLab Community and Enterprise Edition. CISA has since confirmed hackers are actively exploiting the flaw in attacks.

### 2. Chinese Hackers Exploit Critical Tencent IME Flaw for One-Click RCE
- **Source:** SecurityWeek — https://www.securityweek.com/chinese-hackers-exploit-critical-tencent-software-flaw-for-one-click-code-execution/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`
- **Slug:** `chinese-hackers-tencent-ime-rce`
- **Must-know:** no
- **Summary:** A critical flaw in Tencent's Chinese-language input method editor for Windows allows remote code execution with a single click. Chinese state-linked hackers are actively exploiting it.

### 3. Three JFrog Artifactory Flaws Exploited for Backdoor Deployment
- **Source:** SecurityWeek — https://www.securityweek.com/three-jfrog-artifactory-flaws-exploited-for-backdoor-deployment/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `privilege-escalation`, `vulnerability`
- **Slug:** `jfrog-artifactory-flaws-backdoor-deployment`
- **Must-know:** yes
- **Summary:** Three vulnerabilities in JFrog Artifactory allow attackers to bypass authentication and escalate privileges to administrator. Attackers have exploited the flaws to deploy backdoors on affected artifact-repository instances.

### 4. ConnectWise Patches ScreenConnect Flaw Exploited in Worm-Like Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/connectwise-patches-screenconnect-vulnerability-exploited-in-worm-like-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`
- **Slug:** `connectwise-screenconnect-worm-like-exploitation`
- **Must-know:** yes
- **Summary:** ConnectWise has patched a ScreenConnect vulnerability that let attackers send and execute files without authorization through an active remote session. The flaw was exploited in worm-like attacks before the patch shipped.

### 5. Japan's Digital Agency: VPN Flaw Exposed 246,000 Personnel Records
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/japans-digital-agency-says-vpn-flaw-exposed-246-000-personnel-records/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `vulnerability`
- **Slug:** `japan-digital-agency-vpn-flaw-246k-records`
- **Must-know:** no
- **Summary:** Japan's Digital Agency discovered a VPN flaw led to a breach exposing roughly 246,000 rows of personal information belonging to government employees.

### 6. DDRop Attack Breaks Intel TDX and AMD SEV-SNP Confidential Computing
- **Source:** The Hacker News — https://thehackernews.com/2026/09/new-ddrop-attack-breaks-intel-tdx-and.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cloud-security`
- **Slug:** `ddrop-attack-breaks-intel-tdx-amd-sev-snp`
- **Must-know:** no
- **Summary:** Researchers disclosed DDRop, a hardware attack that silently drops memory writes to defeat Intel TDX and AMD SEV-SNP confidential computing protections. It requires an attacker who already controls the server software and briefly touches the physical machine to insert a small circuit.

### 7. 3BB Attacker Used MeshCentral Backdoor for Root Access
- **Source:** The Hacker News — https://thehackernews.com/2026/09/3bb-attacker-used-meshcentral-backdoor.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `privilege-escalation`
- **Slug:** `3bb-meshcentral-backdoor-root-access`
- **Must-know:** no
- **Summary:** An attacker maintained root-level remote control inside Thai broadband provider 3BB's network using the legitimate management tool MeshCentral. The intrusion, targeting subscriber credentials, was uncovered after the attacker left a server with their own tools exposed on the internet.

### 8. Red Heron Exploits Gitea RCE to Compromise 13 Organizations
- **Source:** The Hacker News — https://thehackernews.com/2026/09/red-heron-exploits-gitea-rce-to.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`
- **Slug:** `red-heron-gitea-rce-13-organizations`
- **Must-know:** no
- **Summary:** A suspected Chinese threat actor tracked as Red Heron rapidly exploited a recently disclosed Gitea vulnerability to compromise 13 organizations across six countries. The group scanned 1,386 internet-facing Gitea instances as part of the campaign.

### 9. Hackers Target Exposed Vite Dev Servers to Steal AWS, Azure Secrets
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-target-exposed-vite-dev-servers-to-steal-aws-azure-secrets/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cloud-security`, `aws`, `azure`
- **Slug:** `vite-dev-servers-aws-azure-secrets-theft`
- **Must-know:** no
- **Summary:** A mass-scanning campaign is targeting internet-exposed Vite development servers to steal AWS and Azure credentials and configuration data left accessible on those hosts.

### 10. Malicious Twitch Browser Extension Leaks OAuth Tokens From ~31,000 Users
- **Source:** The Hacker News — https://thehackernews.com/2026/09/malicious-twitch-browser-extension.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `malware`
- **Slug:** `twitch-extension-oauth-token-leak`
- **Must-know:** no
- **Summary:** A cross-store Chrome/Firefox extension called "Twitch Enhanced Viewer | JeetBot" sent users' Twitch OAuth session tokens to a Russian commercial bot service. BleepingComputer separately reported roughly 30,000 installs of the extension.

### 11. CISA Adds Cisco Secure Email Gateway SQL Injection to KEV Catalog
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/alerts/2026/09/14/cisa-adds-one-known-exploited-vulnerability-catalog
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `sqli`, `cve`, `vulnerability`
- **Slug:** `cisa-kev-cisco-secure-email-gateway-sqli`
- **Must-know:** no
- **Summary:** CISA added CVE-2026-76461, a SQL injection vulnerability in Cisco Secure Email Gateway, to its Known Exploited Vulnerabilities Catalog based on evidence of active exploitation. Federal civilian agencies must remediate per BOD 26-04.

### 12. Revolut Data Breach Exposes Financial Info, Passports to Fraudsters
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/revolut-discloses-data-breach-exposing-financial-info-passports/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `revolut-data-breach-fraudster-government-impersonation`
- **Must-know:** no
- **Summary:** Fintech Revolut disclosed that customer financial information and passport data were shared with a threat actor who impersonated a government agency. The Record reports the fraudsters obtained the data using an "emergency data request" submitted from a compromised legitimate government email account.

### 13. Telegram Desktop Flaw Lets Hidden JavaScript Exfiltrate Messages From HTML Exports
- **Source:** The Hacker News — https://thehackernews.com/2026/09/telegram-desktop-flaw-lets-hidden.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `xss`
- **Slug:** `telegram-desktop-hidden-javascript-html-export-flaw`
- **Must-know:** no
- **Summary:** A flaw in Telegram Desktop let a bot-planted message embed hidden JavaScript that ran when a user opened an exported HTML chat log in a browser, silently copying every message in the file. Researchers at ExPatch published the writeup on September 12.

### 14. Hackers Hijack HBO Max Reddit Account to Push ClickFix Malware
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-hijack-hbo-max-reddit-account-to-push-malware-in-clickfix-ads/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Slug:** `hbo-max-reddit-clickfix-malware`
- **Must-know:** no
- **Summary:** Hackers compromised HBO Max's official Reddit account and used it to push malicious ads running ClickFix attacks, infecting Windows and macOS devices with information-stealing malware.

### 15. Anthropic CEO: Time to Shift From Improving to Controlling AI
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/anthropic-ceo-shift-from-improving-to-controlling-ai
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `anthropic`, `ai-safety`
- **Slug:** `anthropic-ceo-controlling-ai-beijing-response`
- **Must-know:** no
- **Summary:** Anthropic CEO Dario Amodei said it's time to slow the pace of frontier AI improvements so security and risk-prevention efforts can catch up. China's Ministry of Foreign Affairs responded to the essay by calling for parties to work together on AI, per SecurityWeek.

### 16. Microsoft Publishes AI Code of Conduct Amid Safety Concerns
- **Source:** The Verge — https://www.theverge.com/news/994566/microsoft-humanist-ai-code-of-conduct
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `microsoft`, `ai-safety`
- **Slug:** `microsoft-ai-code-of-conduct`
- **Must-know:** no
- **Summary:** Microsoft published a 37-page "humanist AI code of conduct" directing its models not to hack systems or trick humans, amid growing safety concerns following Anthropic CEO Dario Amodei's call for a coordinated AI slowdown.

### 17. WordPress Adds Automated Plugin Reviews to Block High-Risk Updates
- **Source:** The Hacker News — https://thehackernews.com/2026/09/wordpress-adds-automated-plugin-reviews.html
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `supply-chain`, `appsec`
- **Slug:** `wordpress-automated-plugin-review`
- **Must-know:** no
- **Summary:** WordPress.org is launching automated security review of every plugin release before it's distributed through the update API, analyzing updates for risk before they ship rather than only reviewing new plugins at submission.

### 18. Unit 42: Behavioral Clustering Maps Cloud Identities for Threat Detection
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `cloud-security`, `iam`
- **Slug:** `unit42-behavioral-clustering-cloud-identities`
- **Must-know:** no
- **Summary:** Unit 42 researchers built a behavioral clustering model that maps cloud identity roles from audit logs, enabling continuous threat detection using standard SQL queries.

## Skippable

- **[Virtual Event] What Every Enterprise Should Know About Securing Cloud Assets in the Age of AI** — Dark Reading. Marketing webinar/event listing, no news content.
- **[Virtual Event] Building a Secure AI Strategy for the Enterprise** — Dark Reading. Marketing webinar/event listing.
- **What blog posts influenced your thinking the most?** — Simon Willison. Personal reflection post, no security or AI news value.
- **Homebrew 7.0.0 gets built-in GUI, better security controls** — BleepingComputer. Primarily a GUI/feature release; no vulnerability detail to report.
- **Members of 'Black Axe' cybercriminal group extradited from South Africa** — The Record. Law enforcement/legal news without new TTPs or technical detail.
- **AWS Security Reference Architecture: A deep dive into PCI DSS compliance** — AWS Security Blog. Vendor compliance guide, not a news event.
- **With iOS 27, I'm actually using Siri again** — TechCrunch AI. Consumer product review, no security angle.
- **Fashion app Daydream uses Apple Intelligence to help you shop the outfits in your camera roll** — TechCrunch AI. Consumer app launch, no security angle.
- **Pro-Ukraine Hacking Cat group deploying new malware against Russian targets** — The Record. Hacktivist campaign reported without technical IOCs or TTPs.
- **Hundreds of fake government websites target users in Central Asia** — The Record. Generic phishing/scam campaign, no novel technique.
- **DevFest is back** — Google AI Blog. Developer conference marketing announcement.
- **AWS Weekly Roundup: OpenAI GPT-6 Astra on Amazon Bedrock, Amazon Quick desktop GA, Kiro for students, and more** — AWS News Blog. Weekly marketing roundup, no single newsworthy security item.
- **Only at TechCrunch Disrupt 2026: What happens when OpenAI ships your roadmap?** — TechCrunch AI. Conference marketing.
- **Superhuman acquires YC-backed notetaker Fathom** — TechCrunch AI. Business acquisition, no security angle.
- **Weekly Recap: Rogue AI Agents, WeChat Worm, PaperCut Attacks, AI Espionage, and Rootkits** — The Hacker News. Roundup of stories already covered individually.
- **Quoting Laurie Voss** — Simon Willison. Opinion quote, no news value.
- **Hear how AI can engineer nature's comeback at TechCrunch Disrupt 2026** — TechCrunch AI. Conference marketing.
- **Why Patch Automation Needs Brakes, Not Just an Accelerator** — BleepingComputer. Vendor-sponsored opinion content.
- **5 days left to exhibit at TechCrunch Disrupt 2026** — TechCrunch AI. Conference marketing.
- **A Vinyl Bar in Shibuya is a startup from a former Spotify leader for making music apps** — TechCrunch AI. Consumer startup story, no security angle.
- **New Warnings About the Risks of AI to Humanity Revive a Long-Running Debate** — SecurityWeek. Opinion/trend piece without a specific news event.
- **The Race to Control AI and Protect What Makes Us Human** — SecurityWeek. Opinion piece without news value.
- **Webinar: How malicious OAuth apps can lead to Google Workspace breaches** — BleepingComputer. Webinar/marketing content.
- **How Fyxer built an AI executive assistant people trust** — OpenAI Blog. Customer case study, no security angle.
- **AI Changed the Exposure Problem. Validation Needs to Change With It.** — The Hacker News. Vendor trend analysis, no specific event.
- **CISOs Race to Control AI Agents Without Destroying Their Value** — SecurityWeek. Generic trend piece, no specific incident.
- **Telus Warns Customers of Account Breaches** — SecurityWeek. Breach disclosure without user count or technical detail.
- **Microsoft: September updates cause RDS failures on Windows Server** — BleepingComputer. IT reliability bug, not a security issue.
- **Microsoft: September updates break audio on some Windows PCs** — BleepingComputer. IT reliability bug, not a security issue.
