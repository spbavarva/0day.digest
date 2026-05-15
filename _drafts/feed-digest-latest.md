# Digest — 2026-05-15 PM

- Window: last 14h
- Raw items considered: 36
- Relevant: 14
- Skippable: 22

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Microsoft Exchange CVE-2026-42897 Zero-Day Exploited via Crafted Email — `2026-05-15-cve-2026-42897-exchange-zero-day-exploited.md`
- [x] **[CRITICAL]** Cisco SD-WAN CVE-2026-20182 Added to CISA KEV; Sixth Exploited SD-WAN Zero-Day in 2026 — `2026-05-15-cisco-sd-wan-cve-2026-20182-cisa-kev.md`
- [x] **[CRITICAL]** node-ipc npm Package Compromised in Supply Chain Attack to Steal Credentials — `2026-05-15-node-ipc-npm-supply-chain-credential-theft.md`
- [x] **[CRITICAL]** TanStack Supply Chain Attack Compromised Two OpenAI Employee Devices, Credentials Stolen — `2026-05-15-tanstack-shai-hulud-openai-supply-chain.md`
- [x] **[CRITICAL]** TeamPCP Releases Shai-Hulud Worm Source Code, Invites Supply Chain Attacks with Monetary Rewards — `2026-05-15-teampcp-shai-hulud-source-code-released.md`
- [x] **[HIGH]** Pwn2Own Berlin 2026 Day 2: 15 Zero-Days in Windows 11, Exchange, and RHEL Earn $385K — `2026-05-15-pwn2own-berlin-2026-day-two-zero-days.md`
- [x] **[HIGH]** Russia's Turla APT Retools Kazuar Backdoor Into Modular P2P Botnet — `2026-05-15-turla-kazuar-modular-p2p-botnet.md`
- [x] **[HIGH]** Avada Builder WordPress Plugin Flaws Expose Credentials on 1 Million Sites — `2026-05-15-avada-builder-wordpress-credential-theft.md`
- [x] **[HIGH]** Four OpenClaw Vulnerabilities Chain to Enable Data Theft, Privilege Escalation, and Backdoor Planting — `2026-05-15-openclaw-claw-chain-privilege-escalation.md`
- [x] **[HIGH]** Chrome 148 Patches Critical Use-After-Free Vulnerabilities in Multiple Browser Components — `2026-05-15-chrome-148-critical-vulnerabilities.md`
- [x] **[MEDIUM]** OpenAI Previews ChatGPT Financial Account Integration via Plaid — `2026-05-15-openai-chatgpt-bank-account-plaid.md`
- [x] **[MEDIUM]** Microsoft Edge Will No Longer Load Saved Passwords in Cleartext at Startup — `2026-05-15-microsoft-edge-cleartext-password-fix.md`
- [x] **[MEDIUM]** REMUS Infostealer Prioritizes Session Token Theft Over Passwords in MaaS Campaign — `2026-05-15-remus-infostealer-session-theft-maas.md`
- [x] **[MEDIUM]** Gremlin Stealer Evolves With Resource-File Obfuscation, Crypto Clipping, and Session Hijacking — `2026-05-15-gremlin-stealer-resource-file-obfuscation.md`

## Relevant (details)

### 1. Microsoft Exchange CVE-2026-42897 Zero-Day Exploited via Crafted Email
- **Source:** The Hacker News — https://thehackernews.com/2026/05/on-prem-microsoft-exchange-server-cve.html
- **Severity:** critical
- **Tags:** `zero-day`, `xss`, `rce`, `microsoft`, `cve`, `vulnerability`
- **Summary:** Microsoft disclosed CVE-2026-42897 (CVSS 8.1), an XSS-rooted spoofing vulnerability in on-premises Exchange Server, actively exploited via crafted emails targeting Outlook on the web. CISA added it to the KEV catalog; no patch is available yet, only mitigations.

### 2. Cisco SD-WAN CVE-2026-20182 Added to CISA KEV; Sixth Exploited SD-WAN Zero-Day in 2026
- **Source:** The Hacker News — https://thehackernews.com/2026/05/cisa-adds-cisco-sd-wan-cve-2026-20182.html
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `vulnerability`, `cisco`
- **Summary:** Critical authentication bypass in Cisco Catalyst SD-WAN Controller exploited by UAT-8616; CISA KEV with federal deadline May 17. Sixth Cisco SD-WAN zero-day exploited in 2026.

### 3. node-ipc npm Package Compromised in Supply Chain Attack to Steal Credentials
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/popular-node-ipc-npm-package-compromised-to-steal-credentials/
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`, `appsec`, `devsecops`
- **Summary:** Credential-stealing malware injected into newly published node-ipc versions on npm. Third significant npm supply chain compromise in recent weeks after TanStack and Bitwarden.

### 4. TanStack Supply Chain Attack Compromised Two OpenAI Employee Devices, Credentials Stolen
- **Source:** The Hacker News — https://thehackernews.com/2026/05/tanstack-supply-chain-attack-hits-two.html
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `openai`, `malware`, `appsec`
- **Summary:** Mini Shai-Hulud malware via TanStack compromised two OpenAI employee devices and stole credential material from code repositories. OpenAI says no user data or production systems affected.

### 5. TeamPCP Releases Shai-Hulud Worm Source Code, Invites Supply Chain Attacks with Monetary Rewards
- **Source:** SecurityWeek — https://www.securityweek.com/teampcp-ups-the-game-releases-shai-hulud-worms-source-code/
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`, `npm`
- **Summary:** TeamPCP open-sourced the Shai-Hulud worm and is offering monetary rewards for supply chain attacks using the code. Dramatically lowers barrier for copycat npm campaigns.

### 6. Pwn2Own Berlin 2026 Day 2: 15 Zero-Days in Windows 11, Exchange, and RHEL Earn $385K
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/pwn2own-day-two-hackers-demo-microsoft-exchange-windows-11-red-had-enterprise-linux-zero-days/
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `microsoft`, `rce`
- **Summary:** Researchers demonstrated 15 unique zero-days across Windows 11, Exchange, and RHEL at Pwn2Own Berlin, earning $385,750. Distinct from CVE-2026-42897; vendors have 90 days to patch before public disclosure.

### 7. Russia's Turla APT Retools Kazuar Backdoor Into Modular P2P Botnet
- **Source:** The Hacker News — https://thehackernews.com/2026/05/turla-turns-kazuar-backdoor-into.html
- **Severity:** high
- **Tags:** `malware`, `apt`
- **Summary:** FSB-linked Turla retooled Kazuar into a modular P2P botnet to eliminate centralized C2 and improve stealth. Targets government, defense, and energy sectors.

### 8. Avada Builder WordPress Plugin Flaws Expose Credentials on 1 Million Sites
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/avada-builder-wordpress-plugin-flaws-allow-site-credential-theft/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`
- **Summary:** Two vulnerabilities in Avada Builder (≈1M installs) enable arbitrary file reads and database credential extraction. Update immediately and rotate exposed secrets.

### 9. Four OpenClaw Vulnerabilities Chain to Enable Data Theft, Privilege Escalation, and Backdoor Planting
- **Source:** The Hacker News — https://thehackernews.com/2026/05/four-openclaw-flaws-enable-data-theft.html
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`, `data-breach`
- **Summary:** Cyera's "Claw Chain" research chains four OpenClaw flaws into an exploit allowing foothold, data exfiltration, privilege escalation, and persistent backdoor installation.

### 10. Chrome 148 Patches Critical Use-After-Free Vulnerabilities in Multiple Browser Components
- **Source:** SecurityWeek — https://www.securityweek.com/chrome-148-update-patches-critical-vulnerabilities/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `google`
- **Summary:** Chrome 148 resolves critical use-after-free and other bugs across browser components commonly leveraged in sandbox-escape chains. Update now.

### 11. OpenAI Previews ChatGPT Financial Account Integration via Plaid
- **Source:** TechCrunch AI — https://techcrunch.com/2026/05/15/openai-launches-chatgpt-for-personal-finance-will-let-you-connect-bank-accounts/
- **Severity:** medium
- **Tags:** `openai`, `llm`, `ai-launch`
- **Summary:** ChatGPT will let users connect bank and brokerage accounts via Plaid across 12,000 institutions. Raises OAuth security and financial data-governance questions.

### 12. Microsoft Edge Will No Longer Load Saved Passwords in Cleartext at Startup
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-edge-to-stop-loading-cleartext-passwords-in-memory-on-startup/
- **Severity:** medium
- **Tags:** `microsoft`, `vulnerability`
- **Summary:** Microsoft reversed Edge's "by design" behavior of loading all saved passwords into process memory as cleartext at startup, closing an easy infostealer harvesting vector.

### 13. REMUS Infostealer Prioritizes Session Token Theft Over Passwords in MaaS Campaign
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/inside-the-remus-infostealer-session-theft-maas-and-rapid-evolution/
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** REMUS targets browser session tokens to bypass MFA, operates as a MaaS with fast iteration cycles. Short session lifetimes and token-replay monitoring are the primary defensive measures.

### 14. Gremlin Stealer Evolves With Resource-File Obfuscation, Crypto Clipping, and Session Hijacking
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** Updated Gremlin stealer embeds malicious code in resource files to evade static detection, adds crypto clipboard hijacking, and steals session tokens. Signature-based tools need updated definitions.

## Skippable

- **Silicon Valley's vacationland needs a new energy provider** — TechCrunch AI. Energy pricing article, no security or AI launch angle.
- **The AWS AI Security Framework** — AWS Security Blog. Marketing framework with sales-engagement CTA; no new security finding.
- **AI radio hosts demonstrate why AI can't be trusted alone** — The Verge AI. AI-agents experiment, no security or model-launch substance.
- **Does Trump Mobile know how many stripes are on the American flag?** — The Verge AI. Consumer gadget column, off-topic.
- **Google updates its spam rules to include attempts to 'manipulate' AI** — The Verge AI. Routine spam policy update, no direct security impact.
- **OpenAI now wants ChatGPT to access your bank accounts** — The Verge AI. Duplicate of TechCrunch item 9.
- **In Other News: Big Tech vs Canada Encryption Bill, Cisco's Free AI Security Spec, Audi App Flaws** — SecurityWeek. Multi-item roundup; individual items lack standalone post depth.
- **Runway started by helping filmmakers — now it wants to beat Google at AI** — TechCrunch AI. Business profile, no model launch or security angle.
- **The promises and pitfalls of personalized health** — The Verge AI. Consumer health newsletter, off-topic.
- **CISA orders all federal agencies to patch Cisco SD-WAN bug by Sunday** — The Record. Duplicate of Cisco SD-WAN CVE-2026-20182.
- **The Good, the Bad and the Ugly in Cybersecurity – Week 20** — SentinelOne Labs. Weekly roundup; stories surfaced individually or lack depth for standalone posts.
- **Microsoft to automatically roll back faulty Windows drivers** — BleepingComputer. Defensive Windows feature improvement, not a security incident.
- **Osaurus brings both local and cloud AI models to your Mac** — TechCrunch AI. Non-security AI productivity app.
- **Microsoft Warns of Exchange Server Zero-Day Exploited in the Wild** — SecurityWeek. Duplicate of CVE-2026-42897.
- **Cyber Pioneers Ponder Past as Prologue** — Dark Reading. Reflective opinion column, no news value.
- **CISA Adds One Known Exploited Vulnerability to Catalog (CVE-2026-42897)** — CISA Alerts. Duplicate; incorporated into Exchange zero-day post.
- **American Lending Center Data Breach Affects 123,000 Individuals** — SecurityWeek. Ransomware victim disclosure with no TTPs or IOCs.
- **What 45 Days of Watching Your Own Tools Will Tell You About Your Real Attack Surface** — The Hacker News. Vendor-sponsored analysis blog, no specific news event.
- **AI research papers are getting better, and it's a big problem for scientists** — The Verge AI. Academic commentary, no security angle.
- **OpenAI Hit by TanStack Supply Chain Attack** — SecurityWeek. Duplicate of TanStack → OpenAI story.
- **Microsoft warns of Exchange zero-day flaw exploited in attacks** — BleepingComputer. Duplicate of CVE-2026-42897.
- **Cisco Patches Another SD-WAN Zero-Day, the Sixth Exploited in 2026** — SecurityWeek. Duplicate of Cisco SD-WAN CVE-2026-20182; context incorporated into main post.
