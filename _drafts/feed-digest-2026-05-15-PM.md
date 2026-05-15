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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `xss`, `rce`, `microsoft`, `cve`, `vulnerability`
- **Slug:** `2026-05-15-cve-2026-42897-exchange-zero-day-exploited`
- **Must-know:** yes
- **Summary:** Microsoft disclosed CVE-2026-42897 (CVSS 8.1), an XSS-rooted spoofing vulnerability in on-premises Exchange Server, now actively exploited via crafted emails targeting Outlook on the web. CISA added it to the KEV catalog; no patch is available yet, only mitigations.

### 2. Cisco SD-WAN CVE-2026-20182 Added to CISA KEV; Sixth Exploited SD-WAN Zero-Day in 2026
- **Source:** The Hacker News — https://thehackernews.com/2026/05/cisa-adds-cisco-sd-wan-cve-2026-20182.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `vulnerability`, `cisco`
- **Slug:** `2026-05-15-cisco-sd-wan-cve-2026-20182-cisa-kev`
- **Must-know:** yes
- **Summary:** A critical authentication bypass in Cisco Catalyst SD-WAN Controller exploited by UAT-8616 has been added to CISA's KEV with a federal patching deadline of May 17. It is the sixth Cisco SD-WAN zero-day exploited so far in 2026.

### 3. node-ipc npm Package Compromised in Supply Chain Attack to Steal Credentials
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/popular-node-ipc-npm-package-compromised-to-steal-credentials/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`, `appsec`, `devsecops`
- **Slug:** `2026-05-15-node-ipc-npm-supply-chain-credential-theft`
- **Must-know:** yes
- **Summary:** Attackers injected credential-stealing malware into newly published node-ipc versions, a popular Node.js IPC package on npm. This is the third significant npm supply chain compromise in recent weeks, alongside TanStack and Bitwarden.

### 4. TanStack Supply Chain Attack Compromised Two OpenAI Employee Devices, Credentials Stolen
- **Source:** The Hacker News — https://thehackernews.com/2026/05/tanstack-supply-chain-attack-hits-two.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `openai`, `malware`, `appsec`
- **Slug:** `2026-05-15-tanstack-shai-hulud-openai-supply-chain`
- **Must-know:** yes
- **Summary:** Two OpenAI corporate employee devices were compromised via the Mini Shai-Hulud malware in the TanStack supply chain attack, resulting in credential theft from OpenAI code repositories. OpenAI says no user data or production systems were impacted.

### 5. TeamPCP Releases Shai-Hulud Worm Source Code, Invites Supply Chain Attacks with Monetary Rewards
- **Source:** SecurityWeek — https://www.securityweek.com/teampcp-ups-the-game-releases-shai-hulud-worms-source-code/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`, `npm`
- **Slug:** `2026-05-15-teampcp-shai-hulud-source-code-released`
- **Must-know:** yes
- **Summary:** TeamPCP publicly released the full source code for the Shai-Hulud supply chain worm and is offering monetary rewards to threat actors who use it in new attacks. The open-sourcing dramatically lowers the barrier for copycat npm supply chain campaigns.

### 6. Pwn2Own Berlin 2026 Day 2: 15 Zero-Days in Windows 11, Exchange, and RHEL Earn $385K
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/pwn2own-day-two-hackers-demo-microsoft-exchange-windows-11-red-had-enterprise-linux-zero-days/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `microsoft`, `rce`
- **Slug:** `2026-05-15-pwn2own-berlin-2026-day-two-zero-days`
- **Must-know:** no
- **Summary:** Day two of Pwn2Own Berlin 2026 yielded 15 unique zero-days across Windows 11, Exchange, and Red Hat Enterprise Linux, earning researchers $385,750. These bugs are distinct from CVE-2026-42897 and vendors have 90 days to patch before disclosure.

### 7. Russia's Turla APT Retools Kazuar Backdoor Into Modular P2P Botnet
- **Source:** The Hacker News — https://thehackernews.com/2026/05/turla-turns-kazuar-backdoor-into.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `apt`
- **Slug:** `2026-05-15-turla-kazuar-modular-p2p-botnet`
- **Must-know:** no
- **Summary:** Russia's Turla APT (FSB Center 16) has evolved its Kazuar backdoor into a modular P2P botnet, eliminating centralized C2 and making detection and takedown substantially harder. Primary targets remain government, defense, and energy sectors.

### 8. Avada Builder WordPress Plugin Flaws Expose Credentials on 1 Million Sites
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/avada-builder-wordpress-plugin-flaws-allow-site-credential-theft/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`
- **Slug:** `2026-05-15-avada-builder-wordpress-credential-theft`
- **Must-know:** no
- **Summary:** Two vulnerabilities in the Avada Builder WordPress plugin (≈1 million active installations) allow arbitrary file reads and credential extraction from the database. Site admins should update immediately and rotate any exposed secrets.

### 9. Four OpenClaw Vulnerabilities Chain to Enable Data Theft, Privilege Escalation, and Backdoor Planting
- **Source:** The Hacker News — https://thehackernews.com/2026/05/four-openclaw-flaws-enable-data-theft.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`, `data-breach`
- **Slug:** `2026-05-15-openclaw-claw-chain-privilege-escalation`
- **Must-know:** no
- **Summary:** Cyera disclosed four chained flaws in OpenClaw dubbed "Claw Chain," enabling initial foothold, sensitive data exfiltration, privilege escalation, and persistent backdoor installation when exploited in sequence.

### 10. Chrome 148 Patches Critical Use-After-Free Vulnerabilities in Multiple Browser Components
- **Source:** SecurityWeek — https://www.securityweek.com/chrome-148-update-patches-critical-vulnerabilities/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `google`
- **Slug:** `2026-05-15-chrome-148-critical-vulnerabilities`
- **Must-know:** no
- **Summary:** Google's Chrome 148 update addresses critical use-after-free bugs and other vulnerabilities across multiple browser components. UAF flaws in browsers frequently appear in sandbox-escape exploit chains.

### 11. OpenAI Previews ChatGPT Financial Account Integration via Plaid
- **Source:** TechCrunch AI — https://techcrunch.com/2026/05/15/openai-launches-chatgpt-for-personal-finance-will-let-you-connect-bank-accounts/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `openai`, `llm`, `ai-launch`
- **Slug:** `2026-05-15-openai-chatgpt-bank-account-plaid`
- **Must-know:** no
- **Summary:** OpenAI previewed bank and brokerage account connectivity for ChatGPT via Plaid, covering 12,000 financial institutions. The feature introduces OAuth attack surface and raises questions about financial data handling in an AI assistant.

### 12. Microsoft Edge Will No Longer Load Saved Passwords in Cleartext at Startup
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-edge-to-stop-loading-cleartext-passwords-in-memory-on-startup/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `microsoft`, `vulnerability`
- **Slug:** `2026-05-15-microsoft-edge-cleartext-password-fix`
- **Must-know:** no
- **Summary:** Microsoft reversed a "by design" behavior in Edge that loaded all saved passwords into process memory as cleartext at startup. The fix closes an easy credential-harvesting vector for infostealers targeting Edge's process memory.

### 13. REMUS Infostealer Prioritizes Session Token Theft Over Passwords in MaaS Campaign
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/inside-the-remus-infostealer-session-theft-maas-and-rapid-evolution/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `2026-05-15-remus-infostealer-session-theft-maas`
- **Must-know:** no
- **Summary:** Flare's analysis of REMUS shows it targets browser session tokens over passwords to bypass MFA, operates as a MaaS with rapid iteration cycles, and has evolved for operational scalability. Short session lifetimes and token-replay monitoring are the primary mitigations.

### 14. Gremlin Stealer Evolves With Resource-File Obfuscation, Crypto Clipping, and Session Hijacking
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `2026-05-15-gremlin-stealer-resource-file-obfuscation`
- **Must-know:** no
- **Summary:** Unit 42 analyzed an updated Gremlin stealer variant using resource-file embedding to evade static detection, combined with crypto clipboard hijacking and session token theft. The obfuscation technique reduces detection rates for signature-based tools.

## Skippable

- **Silicon Valley's vacationland needs a new energy provider** — TechCrunch AI. Energy pricing and business article, no security or AI launch angle.
- **The AWS AI Security Framework** — AWS Security Blog. Marketing framework with a sales-engagement CTA; no new security finding.
- **AI radio hosts demonstrate why AI can't be trusted alone** — The Verge AI. AI-agents-running-businesses experiment; interesting but no security or model-launch substance.
- **Does Trump Mobile know how many stripes are on the American flag?** — The Verge AI. Consumer gadget column, completely off-topic.
- **Google updates its spam rules to include attempts to 'manipulate' AI** — The Verge AI. Routine spam policy update, no direct security impact.
- **OpenAI now wants ChatGPT to access your bank accounts** — The Verge AI. Duplicate of TechCrunch item 9 (same story, less detail).
- **In Other News: Big Tech vs Canada Encryption Bill, Cisco's Free AI Security Spec, Audi App Flaws** — SecurityWeek. Multi-item roundup; individual stories (ShinyHunters/Canvas, Nvidia breach) not covered in sufficient depth for a standalone post.
- **Runway started by helping filmmakers — now it wants to beat Google at AI** — TechCrunch AI. Business profile, no model launch or security angle.
- **The promises and pitfalls of personalized health** — The Verge AI. Consumer health newsletter, off-topic.
- **CISA orders all federal agencies to patch exploited bug in Cisco SD-WAN systems by Sunday** — The Record. Duplicate of Cisco SD-WAN CVE-2026-20182 story (item 36).
- **The Good, the Bad and the Ugly in Cybersecurity – Week 20** — SentinelOne Labs. Weekly roundup; interesting items (ShinyHunters edutech, AI zero-day tooling) surfaced elsewhere or lack standalone post depth.
- **Microsoft to automatically roll back faulty Windows drivers** — BleepingComputer. Defensive Windows feature improvement, not a security incident or vulnerability.
- **Osaurus brings both local and cloud AI models to your Mac** — TechCrunch AI. Non-security AI productivity app launch.
- **Microsoft Warns of Exchange Server Zero-Day Exploited in the Wild** — SecurityWeek. Duplicate of CVE-2026-42897 (item 35).
- **Cyber Pioneers Ponder Past as Prologue** — Dark Reading. Reflective opinion column marking a 20-year milestone; no news value.
- **CISA Adds One Known Exploited Vulnerability to Catalog (CVE-2026-42897)** — CISA Alerts. Duplicate of Exchange zero-day story; incorporated into item 35 post.
- **American Lending Center Data Breach Affects 123,000 Individuals** — SecurityWeek. Ransomware victim disclosure with no TTPs, IOCs, or technical detail.
- **What 45 Days of Watching Your Own Tools Will Tell You About Your Real Attack Surface** — The Hacker News. Vendor-sponsored analysis blog; no specific news event.
- **AI research papers are getting better, and it's a big problem for scientists** — The Verge AI. Academic commentary on AI-generated paper quality; no security angle.
- **OpenAI Hit by TanStack Supply Chain Attack** — SecurityWeek. Duplicate of TanStack → OpenAI story (item 28); less technical detail.
- **Microsoft warns of Exchange zero-day flaw exploited in attacks** — BleepingComputer. Duplicate of CVE-2026-42897 (item 35).
- **Cisco Patches Another SD-WAN Zero-Day, the Sixth Exploited in 2026** — SecurityWeek. Duplicate of Cisco SD-WAN CVE-2026-20182 (item 36); context incorporated into main post.
