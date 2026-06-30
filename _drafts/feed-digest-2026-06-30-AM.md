# Digest — 2026-06-30 AM

- Window: last 14h
- Raw items considered: 22
- Relevant: 8
- Skippable: 14

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** ToddyCat APT Hijacks Gmail via OAuth Tokens with New Umbrij Tool — `2026-06-30-toddycat-umbrij-oauth-gmail-hijack.md`
- [x] **[CRITICAL]** CISA Confirms Active Ransomware Exploitation of Windows BlueHammer Flaw — `2026-06-30-cisa-windows-bluehammer-ransomware-exploit.md`
- [x] **[CRITICAL]** Djinn Stealer Exploits Critical SimpleHelp Auth Bypass (CVE-2026-48558) — `2026-06-29-djinn-stealer-simplehelp-cve-2026-48558.md`
- [x] **[HIGH]** BioShocking Attack Tricks AI Browsers Into Leaking Credentials — `2026-06-30-bioshocking-attack-ai-browsers-credential-leak.md`
- [x] **[CRITICAL]** Critical Pre-Auth RCE in Progress Kemp LoadMaster (CVE-2026-8037) — `2026-06-30-progress-kemp-loadmaster-cve-2026-8037.md`
- [x] **[HIGH]** Apple Patches 30+ Flaws Including AI-Discovered WebKit Bugs — `2026-06-30-apple-patches-ai-discovered-webkit-bugs.md`
- [x] **[CRITICAL]** Oracle E-Business Suite Flaw CVE-2026-46817 Actively Exploited — `2026-06-30-oracle-ebs-cve-2026-46817-active-exploitation.md`
- [x] **[CRITICAL]** Nissan, NAIC Breached via Oracle PeopleSoft Zero-Day, ShinyHunters Campaign — `2026-06-29-nissan-oracle-peoplesoft-zero-day-shinyhunters-breach.md`

## Relevant (details)

### 1. ToddyCat APT Hijacks Gmail via OAuth Tokens with New Umbrij Tool
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/toddycat-apt-umbrij-tool-and-oauth/120251/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `malware`, `iam`, `google`
- **Slug:** `toddycat-umbrij-oauth-gmail-hijack`
- **Must-know:** no
- **Summary:** Kaspersky details a new tool, Umbrij, used by the ToddyCat APT group to compromise corporate Gmail accounts by targeting OAuth authorization tokens rather than passwords. This grants persistent access to Google services without triggering typical credential-based alerts.

### 2. CISA Confirms Active Ransomware Exploitation of Windows BlueHammer Flaw
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-windows-bluehammer-flaw-now-exploited-by-ransomware-gangs/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `ransomware`, `privilege-escalation`, `microsoft`, `vulnerability`
- **Slug:** `cisa-windows-bluehammer-ransomware-exploit`
- **Must-know:** yes
- **Summary:** CISA confirmed ransomware gangs are now exploiting "BlueHammer," a Microsoft Defender privilege escalation flaw previously abused in zero-day attacks. The flaw is a common pre-deployment step for ransomware operators escalating privileges on compromised hosts.

### 3. Djinn Stealer Exploits Critical SimpleHelp Auth Bypass (CVE-2026-48558)
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/djinn-stealer-targets-cloud-ai-credentials
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `malware`, `cloud-security`
- **Slug:** `djinn-stealer-simplehelp-cve-2026-48558`
- **Must-know:** no
- **Summary:** A new infostealer, Djinn, is delivered via CVE-2026-48558, a critical authentication bypass in SimpleHelp remote support software. It targets credentials linking dev and admin environments to cloud, AI, SSH, and crypto wallet access.

### 4. BioShocking Attack Tricks AI Browsers Into Leaking Credentials
- **Source:** The Hacker News — https://thehackernews.com/2026/06/new-bioshocking-attack-tricks-ai.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `phishing`, `anthropic`, `openai`
- **Slug:** `bioshocking-attack-ai-browsers-credential-leak`
- **Must-know:** no
- **Summary:** Security firm LayerX's "BioShocking" technique tricks AI browsers/assistants into leaking user credentials by convincing them they're playing a game. It fooled six AI browsers including ChatGPT Atlas, Perplexity Comet, and Anthropic's Claude browser extension.

### 5. Critical Pre-Auth RCE in Progress Kemp LoadMaster (CVE-2026-8037)
- **Source:** The Hacker News — https://thehackernews.com/2026/06/progress-kemp-loadmaster-flaw-could-let.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `progress-kemp-loadmaster-cve-2026-8037`
- **Must-know:** no
- **Summary:** CVE-2026-8037 (CVSS 9.8) in Progress Kemp LoadMaster lets an unauthenticated attacker run arbitrary root commands via a crafted API request. A patch is available; no active exploitation reported yet.

### 6. Apple Patches 30+ Flaws Including AI-Discovered WebKit Bugs
- **Source:** The Hacker News — https://thehackernews.com/2026/06/apple-patches-30-ios-macos-safari-flaws.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `llm`, `anthropic`, `openai`
- **Slug:** `apple-patches-ai-discovered-webkit-bugs`
- **Must-know:** no
- **Summary:** Apple patched 30+ flaws across iOS, macOS, and Safari, including four WebKit memory-corruption bugs discovered using AI tools — Anthropic Claude and OpenAI Codex Security. No active exploitation reported.

### 7. Oracle E-Business Suite Flaw CVE-2026-46817 Actively Exploited
- **Source:** The Hacker News — https://thehackernews.com/2026/06/oracle-e-business-suite-flaw-cve-2026.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Slug:** `oracle-ebs-cve-2026-46817-active-exploitation`
- **Must-know:** no
- **Summary:** CVE-2026-46817 (CVSS 9.8), an improper privilege management/authentication flaw in Oracle Payments within Oracle E-Business Suite, is under active exploitation according to Defused Cyber. Easily exploitable; attackers can take over vulnerable instances.

### 8. Nissan, NAIC Breached via Oracle PeopleSoft Zero-Day, ShinyHunters Campaign
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/nissan-discloses-employee-data-breach-linked-to-oracle-zero-day-attacks/ and https://www.bleepingcomputer.com/news/security/naic-says-public-data-stolen-in-shinyhunters-peoplesoft-breach/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `data-breach`, `zero-day`, `vulnerability`
- **Slug:** `nissan-oracle-peoplesoft-zero-day-shinyhunters-breach`
- **Must-know:** yes
- **Summary:** Nissan and NAIC both confirmed data was taken after attackers exploited an Oracle PeopleSoft zero-day, part of a ShinyHunters extortion campaign that reportedly targeted around 100 organizations. Only a handful of victims have confirmed breaches so far.

## Skippable

- **The AI Token Costs That Can Break Cybersecurity** — SecurityWeek. Opinion/analysis on AI economics, no concrete news.
- **Kali Linux 2026.2 released with 9 new tools, NetHunter updates** — BleepingComputer. Routine tool release announcement, no novel security technique.
- **Blackfield ransomware asks Nidec Corporation for $2 million ransom** — BleepingComputer. Ransomware victim disclosure without TTPs or IOCs.
- **Nissan Employee Data Breached in Oracle PeopleSoft Hack** — SecurityWeek. Duplicate coverage; merged into the fuller Nissan/NAIC PeopleSoft item above.
- **Crypto exchange OKX wants AI agents to hire and pay each other** — TechCrunch AI. Business/crypto AI news, no security angle.
- **Critical SimpleHelp Vulnerability Exploited for Malware Delivery** — SecurityWeek. Duplicate coverage of the more detailed Djinn Stealer item above.
- **Quantifind Raises $200 Million for AI-Native Risk Intelligence** — SecurityWeek. Funding announcement, no technical substance.
- **Unlocking Britain's next era of productivity: Building a nation of AI trailblazers** — Google AI Blog. Government PR/marketing content, no news value.
- **New Controller Flaws Expose Highway Signs and Billboards to Remote Hacking** — SecurityWeek. Niche ICS advisory, no active exploitation, limited practitioner relevance.
- **The AI jobs debate just got messier** — TechCrunch AI. Opinion/analysis piece, no security angle.
- **Vibe coding platform Base44 launches own model as AI startups seek defensibility** — TechCrunch AI. Minor product launch with business framing, not a frontier model release.
- **HTML table extractor** — Simon Willison. Personal dev utility, no security or AI-launch relevance.
- **Vulnerabilities Expose Private Data in Indian Government Systems** — Dark Reading. Thin technical detail, single-nation scope, no CVE or confirmed widespread impact.
- **NAIC says public data stolen in ShinyHunters' PeopleSoft breach** — BleepingComputer. Duplicate coverage; merged into the Nissan/NAIC PeopleSoft item above.
