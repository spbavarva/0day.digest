# Digest — 2026-07-10 PM

- Window: last 14h
- Raw items considered: 43
- Relevant: 18
- Skippable: 25

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Injective Labs GitHub Compromise Pushes Wallet-Key-Stealing npm Package — `2026-07-10-injective-labs-github-npm-supply-chain.md`
- [x] **[HIGH]** Progress Urges ShareFile Customers to Shut Down Servers Over 'Credible' Threat — `2026-07-10-progress-sharefile-credible-threat-shutdown.md`
- [x] **[MEDIUM]** Six New U-Boot Flaws Could Let Malicious Images Crash Devices or Run Code at Boot — `2026-07-10-u-boot-six-flaws-boot-code-execution.md`
- [x] **[CRITICAL]** Hackers Exploit Critical Auth Bypass in Gitea Docker Image — `2026-07-10-gitea-docker-auth-bypass-exploited.md`
- [x] **[MEDIUM]** Laser Attack Resets Tangem Wallet Passwords on Cards That Can't Be Patched — `2026-07-10-tangem-wallet-laser-attack-password-reset.md`
- [x] **[HIGH]** Researcher Details WhatsApp-to-Host Attack Chain Using Three OpenClaw Flaws — `2026-07-10-openclaw-whatsapp-attack-chain.md`
- [x] **[HIGH]** New Software Bugs in Microsoft BitLocker Wrapper Put ATMs at Risk — `2026-07-10-atm-bitlocker-crypto-software-bugs.md`
- [x] **[MEDIUM]** China, India Ran Separate Spying Campaigns Against Same Pakistani Police Force — `2026-07-10-china-india-spy-campaigns-pakistani-police.md`
- [x] **[MEDIUM]** New MODBEACON RAT Uses gRPC Streaming for Encrypted C2 Traffic — `2026-07-10-modbeacon-rat-grpc-c2.md`
- [x] **[HIGH]** Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP/3 Servers — `2026-07-10-xring-xquic-http3-dos-unpatched.md`
- [x] **[HIGH]** Zimbra Urges Customers to Patch Critical Web Client XSS Flaw — `2026-07-10-zimbra-web-client-xss-patch.md`
- [x] **[HIGH]** Exposed Hacker Server Reveals WP-SHELLSTORM Backdooring Thousands of WordPress Sites — `2026-07-10-wp-shellstorm-wordpress-backdoor-campaign.md`
- [x] **[MEDIUM]** Study of 281 Free Android VPN Apps Finds Traffic Leaks, Unencrypted Data, and Tracking — `2026-07-10-android-vpn-apps-study-traffic-leaks.md`
- [x] **[HIGH]** Hackers Use Fake Microsoft Entra Passkey Enrollment to Gain Microsoft 365 Access — `2026-07-10-fake-entra-passkey-enrollment-vishing.md`
- [x] **[HIGH]** GigaWiper Combines Multiple Malware for System-Level Sabotage — `2026-07-10-gigawiper-multi-malware-sabotage.md`
- [x] **[CRITICAL]** Attackers Exploit 'Ill Bloom' Vulnerability to Drain Over $5 Million From Cryptocurrency Wallets — `2026-07-10-ill-bloom-crypto-wallet-vulnerability.md`
- [x] **[HIGH]** 'HalluSquatting' Turns AI Hallucinations Into Botnet Delivery Mechanism — `2026-07-10-hallusquatting-ai-hallucination-botnet.md`
- [x] **[HIGH]** Network of 200 GitHub Repositories Used for Malware Infection — `2026-07-10-github-repo-network-malware-infection.md`

## Relevant (details)

### 1. Injective Labs GitHub Compromise Pushes Wallet-Key-Stealing npm Package
- **Source:** The Hacker News — https://thehackernews.com/2026/07/injective-labs-github-compromise-pushes.html
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `github`, `malware`
- **Summary:** Attackers compromised the GitHub repo for Injective Labs' SDK project and used it to publish a malicious npm release embedded with fake telemetry that exfiltrates crypto wallet private keys and seed phrases.

### 2. Progress Urges ShareFile Customers to Shut Down Servers Over 'Credible' Threat
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/progress-urges-sharefile-customers-to-shut-down-servers-over-credible-threat/
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`
- **Summary:** Progress Software is emailing ShareFile customers running on-prem Storage Zone Controllers to immediately shut down servers over a "credible external security threat." No technical details or patch published yet.

### 3. Six New U-Boot Flaws Could Let Malicious Images Crash Devices or Run Code at Boot
- **Source:** The Hacker News — https://thehackernews.com/2026/07/six-new-u-boot-flaws-could-let.html
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`
- **Summary:** Binarly disclosed six U-Boot bootloader flaws affecting routers, cameras, and data-center management chips. Four crash devices; two allow code execution at boot given a malicious boot image.

### 4. Hackers Exploit Critical Auth Bypass in Gitea Docker Image
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-auth-bypass-in-gitea-docker-image/
- **Severity:** critical
- **Tags:** `vulnerability`, `appsec`, `container-security`
- **Summary:** Active exploitation of a critical auth bypass in the official Gitea Docker image lets attackers impersonate any user, including admins, giving full instance takeover.

### 5. Laser Attack Resets Tangem Wallet Passwords on Cards That Can't Be Patched
- **Source:** The Hacker News — https://thehackernews.com/2026/07/laser-attack-resets-tangem-wallet.html
- **Severity:** medium
- **Tags:** `vulnerability`
- **Summary:** A precisely timed laser pulse against a Tangem crypto wallet card's chip can reset its password, giving full wallet control. Requires physical access; not fixable via firmware.

### 6. Researcher Details WhatsApp-to-Host Attack Chain Using Three OpenClaw Flaws
- **Source:** The Hacker News — https://thehackernews.com/2026/07/researcher-details-whatsapp-to-host.html
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `vulnerability`, `rce`, `privilege-escalation`
- **Summary:** Three now-patched flaws in the OpenClaw personal AI assistant could be chained from a WhatsApp message to credential theft, privilege escalation, and code execution on the host.

### 7. New Software Bugs in Microsoft BitLocker Wrapper Put ATMs at Risk
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/atm-crypto-software-bugs-jackpot-bust
- **Severity:** high
- **Tags:** `vulnerability`, `microsoft`
- **Summary:** Newly identified bugs in a Microsoft BitLocker security wrapper used in ATM crypto software put affected organizations and possibly ATMs at risk of compromise.

### 8. China, India Ran Separate Spying Campaigns Against Same Pakistani Police Force
- **Source:** The Record (Recorded Future) — https://therecord.media/china-india-ran-separate-spy-campaigns-against-same-police-force
- **Severity:** medium
- **Tags:** `espionage`
- **Summary:** China- and India-linked hacking groups separately targeted Pakistan's Balochistan Police force between Feb 2024 and April 2026, in some cases breaching the exact same systems.

### 9. New MODBEACON RAT Uses gRPC Streaming for Encrypted C2 Traffic
- **Source:** The Hacker News — https://thehackernews.com/2026/07/new-modbeacon-rat-uses-grpc-streaming.html
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** China-linked group Silver Fox has been tied to a new Rust-based RAT, MODBEACON, which uses gRPC streaming to encrypt C2 traffic.

### 10. Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP/3 Servers
- **Source:** The Hacker News — https://thehackernews.com/2026/07/unpatched-xring-flaw-in-xquic-lets.html
- **Severity:** high
- **Tags:** `vulnerability`, `zero-day`
- **Summary:** A single incorrect variable in Alibaba's XQUIC library lets any remote unauthenticated client crash a server with ~260 bytes of ordinary traffic. Disclosed July 8, still unpatched.

### 11. Zimbra Urges Customers to Patch Critical Web Client XSS Flaw
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/zimbra-urges-customers-to-patch-critical-web-client-xss-flaw/
- **Severity:** high
- **Tags:** `xss`, `vulnerability`
- **Summary:** Zimbra is urging customers to patch a critical XSS flaw in the Classic Web Client used to access Zimbra Collaboration Suite.

### 12. Exposed Hacker Server Reveals WP-SHELLSTORM Backdooring Thousands of WordPress Sites
- **Source:** The Hacker News — https://thehackernews.com/2026/07/exposed-hacker-server-reveals-wp.html
- **Severity:** high
- **Tags:** `malware`, `vulnerability`
- **Summary:** A cybercrime crew's own server sat exposed for three weeks, revealing a mass WordPress-hacking operation with a target list of 1.4M+ sites.

### 13. Study of 281 Free Android VPN Apps Finds Traffic Leaks, Unencrypted Data, and Tracking
- **Source:** The Hacker News — https://thehackernews.com/2026/07/study-of-281-free-android-vpn-apps.html
- **Severity:** medium
- **Tags:** `vulnerability`
- **Summary:** Testing of 281 popular free Android VPN apps found many fail at basic traffic-privacy protections; combined install base of flagged apps exceeds 2.4 billion.

### 14. Hackers Use Fake Microsoft Entra Passkey Enrollment to Gain Microsoft 365 Access
- **Source:** The Hacker News — https://thehackernews.com/2026/07/hackers-use-fake-microsoft-entra.html
- **Severity:** high
- **Tags:** `phishing`, `microsoft`
- **Summary:** Okta-tracked actor O-UNC-066 uses voice-based social engineering to trick M365 users into enrolling attacker-controlled Entra passkeys for data-extortion attacks.

### 15. GigaWiper Combines Multiple Malware for System-Level Sabotage
- **Source:** SecurityWeek — https://www.securityweek.com/gigawiper-combines-multiple-malware-for-system-level-sabotage/
- **Severity:** high
- **Tags:** `malware`, `ransomware`
- **Summary:** A new backdoor, GigaWiper, bundles a standalone wiper, ransomware-style encryption, and a multi-pass wipe command in one tool.

### 16. Attackers Exploit 'Ill Bloom' Vulnerability to Drain Over $5 Million From Cryptocurrency Wallets
- **Source:** The Hacker News — https://thehackernews.com/2026/07/attackers-exploit-ill-bloom.html
- **Severity:** critical
- **Tags:** `vulnerability`, `zero-day`
- **Summary:** Coinspect disclosed "Ill Bloom," a weak-randomness flaw in wallet recovery-phrase generation that attackers are actively exploiting. A confirmed sweep drained over $5 million.

### 17. 'HalluSquatting' Turns AI Hallucinations Into Botnet Delivery Mechanism
- **Source:** SecurityWeek — https://www.securityweek.com/hallusquatting-turns-ai-hallucinations-into-botnet-delivery-mechanism/
- **Severity:** high
- **Tags:** `ai-safety`, `llm`, `malware`
- **Summary:** Researchers demonstrated adversarial "hallucination squatting" against popular AI coding assistants to achieve remote code execution and botnet delivery.

### 18. Network of 200 GitHub Repositories Used for Malware Infection
- **Source:** SecurityWeek — https://www.securityweek.com/network-of-200-github-repositories-used-for-malware-infection/
- **Severity:** high
- **Tags:** `malware`, `github`, `supply-chain`
- **Summary:** A ~200-repo GitHub network distributes malware via a malicious Go module that loads PowerShell, which fetches a resolver from public dead drops to retrieve Windows malware.

## Skippable

- **Ryuk ransomware member pleads guilty in the US, faces 15 years in prison** — BleepingComputer. Legal sentencing news, no new technical detail.
- **SK Hynix raises $26.5B in the biggest foreign IPO in US history** — TechCrunch AI. Business/finance news, no security angle.
- **Quoting Nilay Patel** — Simon Willison. Opinion piece on AR glasses hardware constraints, no security substance.
- **Ryuk operator pleads guilty; Blackcat/AlphV conspirator gets nearly 6-year sentence** — The Record. Duplicate legal/sentencing coverage.
- **Contributing to U.K. financial sector resilience as a critical third party** — Google Cloud Security. Regulatory/compliance PR announcement, no technical substance.
- **Cybercriminals Flock to Healthcare Businesses as Attacks Surge** — Dark Reading. Generic trend stats, no TTPs or IOCs.
- **License plate cameras may be next target after Supreme Court reins in location tracking** — The Record. Policy/legal analysis, not a vuln or incident.
- **Police suspects Dutch hackers were involved in Odido breach** — BleepingComputer. Regional breach follow-up, no new technical detail.
- **The Good, the Bad and the Ugly in Cybersecurity – Week 28** — SentinelOne Labs. Weekly link roundup; stories covered individually elsewhere.
- **AWS designated as a critical third party to the UK financial sector** — AWS Security Blog. Regulatory/compliance PR announcement, duplicate of the Google Cloud item.
- **Money launderer accused of stealing seized crypto while in prison** — BleepingComputer. Novelty crime story, no technical security content.
- **In Other News: DHS Database Hacked, Adobe Boosts Patch Cadence, Canada Disrupts Ransomware Ops** — SecurityWeek. Link roundup without technical detail on any single item.
- **The Replicant in Your Directory: AI Agents and the Identity Security Gap** — BleepingComputer (Netwrix). Vendor thought-leadership/marketing content.
- **Hugging Face's CEO on why companies are done renting their AI** — TechCrunch AI. Business interview, no security or launch substance.
- **More Countries Jump on the Social Media 'Ban Wagon'** — Dark Reading. Policy piece, not a vuln or incident.
- **Instagram's Adam Mosseri: If you don't like AI, 'then you shouldn't have it in your feed'** — The Verge AI. Opinion/interview, no news value.
- **Would you host part of an AI data center in your home?** — The Verge AI. Business/infrastructure story, no security angle.
- **AI Coding: Do Security Risks Outweigh Productivity Gains?** — Dark Reading. Opinion piece without new data.
- **Third US Security Expert Sentenced to Prison for Helping Ransomware Gang** — SecurityWeek. Duplicate legal/sentencing coverage of the BlackCat negotiator story.
- **China, India-Linked Hackers Both Targeted Same Pakistani Police Force** — SecurityWeek. Duplicate coverage; The Record version has more detail.
- **From 17,000 to 1.1 Million Assets: How Lumen Technologies Rebuilt Exposure Management at Scale** — The Hacker News (Axonius). Vendor case study/marketing content.
- **Okta Warns of Vishing Attacks Targeting Microsoft 365 Customers** — SecurityWeek. Duplicate coverage; The Hacker News version has more technical detail.
- **Former ransomware negotiator gets 4 years for BlackCat attacks** — BleepingComputer. Duplicate legal/sentencing coverage.
- **Ransomware Negotiator Gets 70 Months in Prison for Aiding BlackCat Attacks** — The Hacker News. Duplicate legal/sentencing coverage.
- **How Deutsche Telekom is rewiring telecommunications with AI** — OpenAI Blog. Customer case study/marketing content, not a launch or incident.
