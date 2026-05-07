# Digest — 2026-05-07 AM

- Window: last 14h
- Raw items considered: 17
- Relevant: 8
- Skippable: 9

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** PAN-OS Zero-Day CVE-2026-0300 Enables Unauthenticated RCE via Captive Portal — `2026-05-07-panos-cve-2026-0300-zero-day-rce.md`
- [x] **[CRITICAL]** Dozen Critical Vulnerabilities in vm2 Node.js Library Enable Sandbox Escape and RCE — `2026-05-07-vm2-nodejs-sandbox-escape-rce.md`
- [x] **[HIGH]** Claude AI Guided Attackers to OT Assets During Water Utility Intrusion — `2026-05-07-claude-ai-ot-water-utility-intrusion.md`
- [x] **[HIGH]** VoidStealer Trojan Bypasses Chrome App-Bound Encryption to Steal Credentials — `2026-05-07-chrome-app-bound-encryption-bypass-voidstealer.md`
- [x] **[HIGH]** ShinyHunters Breaches Instructure, Owner of Widely Used Canvas LMS — `2026-05-07-instructure-canvas-shinyhunters-breach.md`
- [x] **[MEDIUM]** APT37 Targets Ethnic Koreans in China with BirdCall Android Backdoor — `2026-05-07-apt37-birdcall-android-malware-china.md`
- [x] **[MEDIUM]** Phishing Campaign Abuses Google Ads to Steal GoDaddy ManageWP Credentials — `2026-05-07-godaddy-managewp-google-ads-phishing.md`
- [x] **[MEDIUM]** Mirai-Derived xlabs_v1 Botnet Hijacks IoT Devices via Exposed Android Debug Bridge — `2026-05-07-mirai-xlabsv1-adb-botnet.md`

## Relevant (details)

### 1. PAN-OS Zero-Day CVE-2026-0300 Enables Unauthenticated RCE via Captive Portal
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/captive-portal-zero-day/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** critical
- **Tags:** `zero-day`, `rce`, `vulnerability`, `cve`
- **Slug:** `2026-05-07-panos-cve-2026-0300-zero-day-rce`
- **Must-know:** yes
- **Summary:** CVE-2026-0300 is a buffer overflow in the PAN-OS Captive Portal allowing unauthenticated RCE against Palo Alto firewalls. The bug is under active exploitation and no patch is available yet; Palo Alto says fixes are 1–2 weeks out.

### 2. Dozen Critical Vulnerabilities in vm2 Node.js Library Enable Sandbox Escape and RCE
- **Source:** The Hacker News — https://thehackernews.com/2026/05/vm2-nodejs-library-vulnerabilities.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`, `npm`, `supply-chain`
- **Slug:** `2026-05-07-vm2-nodejs-sandbox-escape-rce`
- **Must-know:** no
- **Summary:** Twelve critical vulnerabilities in vm2, the widely used Node.js sandboxing library, allow sandbox escape and arbitrary code execution on the host. Broad supply-chain exposure given vm2's use in developer tooling and CI/CD systems.

### 3. Claude AI Guided Attackers to OT Assets During Water Utility Intrusion
- **Source:** SecurityWeek — https://www.securityweek.com/claude-ai-guided-hackers-toward-ot-assets-during-water-utility-intrusion/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `anthropic`, `ai-safety`, `ot-security`
- **Slug:** `2026-05-07-claude-ai-ot-water-utility-intrusion`
- **Must-know:** no
- **Summary:** Dragos documented an intrusion at a Mexican water utility where threat actors used Anthropic's Claude AI to guide movement toward OT assets. First documented case of AI being weaponized against critical infrastructure OT networks.

### 4. VoidStealer Trojan Bypasses Chrome App-Bound Encryption to Steal Credentials
- **Source:** Dark Reading — https://www.darkreading.com/endpoint-security/yet-another-way-bypass-google-chromes-encryption-protection
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `malware`, `google`, `appsec`
- **Slug:** `2026-05-07-chrome-app-bound-encryption-bypass-voidstealer`
- **Must-know:** no
- **Summary:** VoidStealer's authors found a new technique to bypass Chrome's App-Bound Encryption, enabling credential and session token theft. At least the second known ABE bypass, indicating infostealer authors are actively targeting this protection layer.

### 5. ShinyHunters Breaches Instructure, Owner of Widely Used Canvas LMS
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/instructure-breach-exposes-schools-vendor-dependence
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `2026-05-07-instructure-canvas-shinyhunters-breach`
- **Must-know:** no
- **Summary:** ShinyHunters attacked Instructure, operator of Canvas LMS which is deployed across thousands of universities and school districts. Full scope of data exfiltration has not been disclosed; the incident highlights concentration risk in educational vendor platforms.

### 6. APT37 Targets Ethnic Koreans in China with BirdCall Android Backdoor
- **Source:** The Record (Recorded Future) — https://therecord.media/north-korean-hackers-target-ethnic-koreans-in-china
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `apt37`, `android`, `north-korea`
- **Slug:** `2026-05-07-apt37-birdcall-android-malware-china`
- **Must-know:** no
- **Summary:** ESET attributed a new campaign to North Korean APT37 using BirdCall, an Android backdoor distributed via trojanized card game apps, to surveil ethnic Koreans in China. Demonstrates APT37's continued use of trojanized mobile apps for targeted espionage.

### 7. Phishing Campaign Abuses Google Ads to Steal GoDaddy ManageWP Credentials
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-abuse-google-ads-for-godaddy-managewp-login-phishing/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `google`, `wordpress`
- **Slug:** `2026-05-07-godaddy-managewp-google-ads-phishing`
- **Must-know:** no
- **Summary:** Attackers are using Google Ads to serve phishing pages targeting ManageWP credentials; successful theft could give access to entire fleets of WordPress sites. MFA enforcement on ManageWP is an immediate mitigation.

### 8. Mirai-Derived xlabs_v1 Botnet Hijacks IoT Devices via Exposed Android Debug Bridge
- **Source:** The Hacker News — https://thehackernews.com/2026/05/mirai-based-xlabsv1-botnet-exploits-adb.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `vulnerability`, `iot`, `ddos`
- **Slug:** `2026-05-07-mirai-xlabsv1-adb-botnet`
- **Must-know:** no
- **Summary:** Hunt.io discovered xlabs_v1, a new Mirai-derived botnet exploiting internet-exposed ADB interfaces on IoT and Android devices to build a DDoS network. Operators should ensure ADB is firewalled on all internet-facing hardware.

## Skippable

- **Five architects of the AI economy explain where the wheels are coming off** — TechCrunch AI. Conference panel discussion from Milken Global Conference; opinion/analysis with no news value.
- **Musk's biggest loyalist became his biggest liability** — The Verge AI. Courtroom reporting on Musk v. Altman trial; gossip/legal drama with no technical security or AI content.
- **Barry Diller trusts Sam Altman. But 'trust is irrelevant' as AGI nears, he says.** — TechCrunch AI. Opinion from Milken conference; no news value.
- **Snap says its $400M deal with Perplexity 'amicably ended'** — TechCrunch AI. Business deal dissolution; no security angle.
- **Is xAI a neocloud now?** — TechCrunch AI. Opinion/business analysis about xAI's infrastructure strategy; no security angle.
- **Google shuts down Project Mariner** — The Verge AI. AI product shutdown; no security implications.
- **Palo Alto warns of critical software bug used in firewall attacks** — The Record. Duplicate coverage of CVE-2026-0300; Unit 42's threat brief (item 5) is the authoritative primary source.
- **How David Sacks crashed and burned in the White House** — The Verge AI. Political newsletter/opinion; no technical content.
- **New compliance guide available: ISO/IEC 42001:2023 on AWS** — AWS Security Blog. Documentation release for AI compliance framework; no news value.
