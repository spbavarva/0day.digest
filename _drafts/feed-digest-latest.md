# Digest — 2026-10-29 PM

- Window: last 14h
- Raw items considered: 32
- Relevant: 15
- Skippable: 17

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Adobe, Veeam, Juniper Networks Patch Critical Vulnerabilities — `2026-10-29-adobe-veeam-juniper-critical-vulnerabilities.md`
- [x] **[HIGH]** Over 41,000 DHS Employee Records Leaked Online — `2026-10-29-dhs-employee-records-leaked-okta.md`
- [x] **[HIGH]** Telegram Android Flaw Lets Attackers Run Code When Users Answer Voice Calls — `2026-10-29-telegram-android-voice-call-rce.md`
- [x] **[HIGH]** 26,400 Valid Cloud and AI Credentials Found Exposed in Public Gitee Repositories — `2026-10-29-gitee-cloud-ai-credentials-exposed.md`
- [x] **[CRITICAL]** Hackers Steal 2.6 Million Records From Sony's Japanese ISP So-net — `2026-10-29-sony-so-net-isp-breach-2-6-million.md`
- [x] **[CRITICAL]** Cisco Patches Actively Exploited ASA and FTD VPN Zero-Day — `2026-10-29-cisco-asa-ftd-vpn-zero-day-dos.md`
- [x] **[INFORMATIONAL]** GitHub Launches npm Firewall to Block Malicious Packages Before Installation — `2026-10-29-github-npm-firewall-launch.md`
- [x] **[HIGH]** NIK C2: The New AI-Enabled Command-and-Control Framework — `2026-10-29-nik-c2-ai-enabled-framework.md`
- [x] **[MEDIUM]** Shadowy AI Relay Disables OpenAI Codex, Claude Code Sandboxes — `2026-10-29-shadowy-ai-relay-disables-coding-sandboxes.md`
- [x] **[CRITICAL]** Attacker Tried to Exploit Alpine Linux's GitLab via CVSS 10.0 Flaw — `2026-10-29-alpine-linux-gitlab-cvss10-attempted-exploit.md`
- [x] **[CRITICAL]** HHS Filing Puts iRhythm Data Breach Toll at 8.2 Million — `2026-10-29-irhythm-data-breach-8-2-million.md`
- [x] **[HIGH]** Hackers Exploited Cisco SD-WAN Flaw to Plant KeyDrift Malware, Linked to Volt Typhoon — `2026-10-29-cisco-sd-wan-keydrift-volt-typhoon.md`
- [x] **[MEDIUM]** Unknown APT Uses NetamLoader to Attack Customized Government Windows 10 Build — `2026-10-29-netamloader-apt-customized-government-os.md`
- [x] **[HIGH]** China-Linked Hackers Exploited VMware ESXi Zero-Day, Tied to Warp Panda — `2026-10-29-vmware-esxi-zero-day-warp-panda.md`
- [x] **[CRITICAL]** Attackers Exploit PHP2Shell Flaws in Internet-Exposed Palo Alto Management Interfaces — `2026-10-29-php2shell-palo-alto-management-interface-exploited.md`

## Relevant (details)

### 1. Adobe, Veeam, Juniper Networks Patch Critical Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/adobe-veeam-juniper-networks-patch-critical-vulnerabilities/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Slug:** `adobe-veeam-juniper-critical-vulnerabilities`
- **Must-know:** no
- **Summary:** Adobe, Veeam, and Juniper Networks each patched critical vulnerabilities this week that could lead to arbitrary code execution, authorization bypasses, and privilege escalation. No confirmed active exploitation was reported.

### 2. Over 41,000 DHS Employee Records Leaked Online
- **Source:** SecurityWeek — https://www.securityweek.com/over-41000-dhs-employee-records-leaked-online/
- **Severity:** high
- **Tags:** `data-breach`, `iam`
- **Slug:** `dhs-employee-records-leaked-okta`
- **Must-know:** no
- **Summary:** Personal and work information for more than 41,000 DHS employees was leaked online, allegedly stolen from an Okta single sign-on system earlier this year.

### 3. Telegram Android Flaw Lets Attackers Run Code When Users Answer Voice Calls
- **Source:** The Hacker News — https://thehackernews.com/2026/10/telegram-android-flaw-lets-attackers.html
- **Severity:** high
- **Tags:** `rce`, `vulnerability`
- **Slug:** `telegram-android-voice-call-rce`
- **Must-know:** no
- **Summary:** A flaw in Telegram for Android let an attacker run code on a victim's phone via a voice call once answered, requiring only an ordinary Telegram account. Telegram fixed it in version 12.10.4 (late September); security startup NebuSec disclosed the flaw October 29.

### 4. 26,400 Valid Cloud and AI Credentials Found Exposed in Public Gitee Repositories
- **Source:** The Hacker News — https://thehackernews.com/2026/10/26400-valid-cloud-and-ai-credentials.html
- **Severity:** high
- **Tags:** `data-breach`, `iam`, `cloud-security`
- **Slug:** `gitee-cloud-ai-credentials-exposed`
- **Must-know:** no
- **Summary:** Independent researcher Ben Zimmermann scanned 7.25 million public Gitee repositories and found 26,400 valid credentials — mostly cloud and AI service keys — still working, meaning anyone who copied one could have used it. Results were reported October 28.

### 5. Hackers Steal 2.6 Million Records From Sony's Japanese ISP So-net
- **Source:** SecurityWeek — https://www.securityweek.com/hackers-steal-2-6-million-records-from-sonys-japanese-isp-so-net/
- **Severity:** critical
- **Tags:** `data-breach`
- **Slug:** `sony-so-net-isp-breach-2-6-million`
- **Must-know:** yes
- **Summary:** Hackers stole 2.6 million records belonging to customers of Sony's Japanese ISP So-net and its Plala service, including 54,401 email account passwords and 16 bank account records.

### 6. Cisco Patches Actively Exploited ASA and FTD VPN Zero-Day
- **Source:** The Hacker News — https://thehackernews.com/2026/10/cisco-patches-actively-exploited-asa.html
- **Source:** SecurityWeek — https://www.securityweek.com/attackers-exploit-second-cisco-firewall-vpn-zero-day-since-august/
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`
- **Slug:** `cisco-asa-ftd-vpn-zero-day-dos`
- **Must-know:** yes
- **Summary:** Cisco patched CVE-2026-76418 (CVSS 8.6), a flaw in the Remote Access SSL VPN service of ASA/FTD Secure Firewall software that unauthenticated remote attackers were exploiting in the wild to force device reloads/crashes. It is the second such ASA/FTD zero-day exploited since August.

### 7. GitHub Launches npm Firewall to Block Malicious Packages Before Installation
- **Source:** The Hacker News — https://thehackernews.com/2026/10/github-launches-npm-firewall-to-block.html
- **Severity:** informational
- **Tags:** `supply-chain`, `npm`, `github`, `devsecops`
- **Slug:** `github-npm-firewall-launch`
- **Must-know:** no
- **Summary:** GitHub introduced an npm Firewall, in public preview, that inspects package metadata requests and downloads for signs of malicious activity, acting as an install-time policy gate to block suspicious npm packages before they install.

### 8. NIK C2: The New AI-Enabled Command-and-Control Framework
- **Source:** Cisco Talos — https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/
- **Severity:** high
- **Tags:** `malware`, `llm`, `ai-safety`
- **Slug:** `nik-c2-ai-enabled-framework`
- **Must-know:** no
- **Summary:** Cisco Talos observed a new AI-integrated command-and-control framework in the wild, dubbed "NIK C2." The feed summary is thin on technical detail.

### 9. Shadowy AI Relay Disables OpenAI Codex, Claude Code Sandboxes
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/ai-relay-service-openai-codex-claude-code-sandboxes
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`, `anthropic`, `openai`
- **Slug:** `shadowy-ai-relay-disables-coding-sandboxes`
- **Must-know:** no
- **Summary:** An unidentified relay service is providing OpenAI Codex and Claude Code access in regions where the products aren't officially sold, including mainland China, with key security/sandbox features turned off.

### 10. Attacker Tried to Exploit Alpine Linux's GitLab via CVSS 10.0 Flaw
- **Source:** The Hacker News — https://thehackernews.com/2026/10/attacker-tried-to-exploit-alpine-linuxs.html
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `alpine-linux-gitlab-cvss10-attempted-exploit`
- **Must-know:** no
- **Summary:** An attacker tried to exploit CVE-2026-97229 (CVSS 10.0), a GitLab flaw that lets code run via a crafted regex in a CI configuration, against Alpine Linux's own GitLab server a week after GitLab released a fix. Alpine found no evidence the attack succeeded.

### 11. HHS Filing Puts iRhythm Data Breach Toll at 8.2 Million
- **Source:** SecurityWeek — https://www.securityweek.com/hhs-filing-puts-irhythm-data-breach-toll-at-8-2-million/
- **Severity:** critical
- **Tags:** `data-breach`
- **Slug:** `irhythm-data-breach-8-2-million`
- **Must-know:** yes
- **Summary:** An HHS filing shows a data breach at iRhythm affected 8.2 million people, with personal information and account/device data stolen from third-party-hosted business applications.

### 12. Hackers Exploited Cisco SD-WAN Flaw to Plant KeyDrift Malware, Linked to Volt Typhoon
- **Source:** The Hacker News — https://thehackernews.com/2026/10/hackers-exploited-cisco-sd-wan-flaw-to.html
- **Source:** SecurityWeek — https://www.securityweek.com/cisco-sd-wan-zero-day-exploitation-tied-to-volt-typhoons-silent-train-network/
- **Severity:** high
- **Tags:** `malware`, `vulnerability`
- **Slug:** `cisco-sd-wan-keydrift-volt-typhoon`
- **Must-know:** no
- **Summary:** Hackers exploited a critical Cisco Catalyst SD-WAN flaw (fixed in February) to plant custom malware called "KeyDrift," built to steal the keys that encrypt inter-site traffic. Cisco Talos said October 28 the attacks are historical and that the infrastructure overlaps with Volt Typhoon's "Silent Train" network.

### 13. Unknown APT Uses NetamLoader to Attack Customized Government Windows 10 Build
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/netamloader/121676/
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `netamloader-apt-customized-government-os`
- **Must-know:** no
- **Summary:** Kaspersky researchers analyzed a targeted attack using "NetamLoader," a malicious loader framework, against a customized Windows 10 build used by governments in Asia.

### 14. China-Linked Hackers Exploited VMware ESXi Zero-Day, Tied to Warp Panda
- **Source:** The Hacker News — https://thehackernews.com/2026/10/china-linked-hackers-exploited-vmware.html
- **Source:** SecurityWeek — https://www.securityweek.com/chinese-hackers-quietly-used-low-severity-esxi-logging-flaw-as-zero-day/
- **Severity:** high
- **Tags:** `zero-day`, `cve`, `vulnerability`
- **Slug:** `vmware-esxi-zero-day-warp-panda`
- **Must-know:** no
- **Summary:** CISA added CVE-2026-41709, a Broadcom VMware ESX logging flaw, to its Known Exploited Vulnerabilities catalog after CrowdStrike revealed the China-nexus group "Warp Panda" weaponized it against the U.S. legal sector. The flaw lets an attacker with administrative privileges perform operations without being logged.

### 15. Attackers Exploit PHP2Shell Flaws in Internet-Exposed Palo Alto Management Interfaces
- **Source:** The Hacker News — https://thehackernews.com/2026/10/attackers-exploit-php2shell-flaws-in.html
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `php2shell-palo-alto-management-interface-exploited`
- **Must-know:** no
- **Summary:** Palo Alto Networks warned that threat actors are actively exploiting recently patched "PHP2Shell" vulnerabilities against internet-exposed management interfaces, per an updated advisory.

## Skippable

- **Granite Switch 4.1.1** — Hugging Face Blog. Title-only item, no summary provided; minor model-tooling update.
- **Cyberattack disrupts Belgian tax services before filing deadline** — The Record. Single-agency disruption, no technical detail or IOCs disclosed.
- **University of New Mexico restores hospital systems, urges no contact with hackers** — The Record. Single-org ransomware recovery, no TTPs/IOCs.
- **Anthropic's business plan: Build God or die trying** — The Verge AI. Opinion/analysis piece on Anthropic's S-1 and compute spend, no technical news.
- **BAE Says No Data Extracted in Incident Hitting Bankruptcy Courts** — SecurityWeek. No data was actually breached; low substance.
- **Deepgram acquires Pipecat-maker Daily to bolster its voice AI infrastructure** — TechCrunch AI. Business acquisition, no security angle.
- **Amazon updates Alexa to help you manage shopping lists, subscriptions, and update delivery instructions** — TechCrunch AI. Consumer feature update, no security angle.
- **Windows 11 KB5127936 update released with 41 changes and fixes** — BleepingComputer. Routine feature update, not security-critical.
- **Webinar: How to Build AI Threat Readiness Into Your Security Operations** — The Hacker News. Sponsored webinar/marketing content.
- **The Rise of the Threat Operator: How AI Will Redefine Security Operations and Careers** — The Hacker News. Opinion piece on AI/SOC careers, no news value.
- **New Cisco firewall zero-day exploited to crash SSL VPN devices** — BleepingComputer. Duplicate coverage of the Cisco ASA/FTD zero-day (CVE-2026-76418); see item 6 above.
- **Cisco SD-WAN Zero-Day Exploitation Tied to Volt Typhoon's 'Silent Train' Network** — SecurityWeek. Duplicate coverage of the Cisco SD-WAN KeyDrift story, cited as a secondary source in item 12 above.
- **AI has come for Arizona's water** — The Verge AI. Feature piece on data center water use, no security angle.
- **Attackers Exploit Second Cisco Firewall VPN Zero-Day Since August** — SecurityWeek. Duplicate coverage of the Cisco ASA/FTD zero-day, cited as a secondary source in item 6 above.
- **Chinese Hackers Quietly Used Low-Severity ESXi Logging Flaw as Zero-Day** — SecurityWeek. Duplicate coverage of the VMware ESXi/Warp Panda story, cited as a secondary source in item 14 above.
- **Cyber Vulnerabilities Besiege Italy, Absent Clear Cause** — Dark Reading. Vague trend piece, no technical substance or specific incident.
- **Introducing AnySpeechRecognizer and AnyDecisionModel: Open Models for Speech and Decisions on Apple Platforms** — Hugging Face Blog. Title-only item, no summary provided; insufficient detail for a factual post.
