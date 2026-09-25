# Digest — 2026-09-25 PM

- Window: last 14h
- Raw items considered: 16
- Relevant: 8
- Skippable: 8

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Suspected North Korean Hackers Steal $351.6M From Bitget Crypto Exchange — `2026-09-25-bitget-crypto-exchange-hack-351m.md`
- [x] **[CRITICAL]** CISA Adds Actively Exploited WSO2 and Adobe Commerce Flaws to KEV Catalog — `2026-09-25-wso2-adobe-commerce-flaws-cisa-kev.md`
- [x] **[HIGH]** Actively Exploited Roundcube Pre-Auth SQL Injection Flaw (CVE-2026-48842) — `2026-09-25-roundcube-sqli-cve-2026-48842.md`
- [x] **[HIGH]** 'SalesBleed' Flaws in Salesforce Agentforce Enabled Zero-Click Data Exfiltration — `2026-09-25-salesbleed-salesforce-agentforce-flaws.md`
- [x] **[HIGH]** Cloudflare Fixes Flaw Letting Containers Read Other Customers' Leftover Disk Data — `2026-09-25-cloudflare-container-disk-data-leak.md`
- [x] **[MEDIUM]** Windows, Linux, and Android File Notification Systems Found to Leak User Activity — `2026-09-25-file-notification-systems-leak-activity.md`
- [x] **[INFORMATIONAL]** Research: Trusted Execution Environments Can Undermine MPC Threshold Signatures — `2026-09-25-tees-break-mpc-trail-of-bits.md`
- [x] **[INFORMATIONAL]** Doubts Grow Over Claims That an OpenAI Agent Hacked Australia's Medicare Portal — `2026-09-25-openai-agent-australia-medicare-doubts.md`

## Relevant (details)

### 1. Suspected North Korean Hackers Steal $351.6M From Bitget Crypto Exchange
- **Source:** The Hacker News — https://thehackernews.com/2026/09/bitget-says-suspected-north-korean.html
- **Severity:** critical
- **Tags:** `data-breach`, `malware`
- **Summary:** Bitget disclosed that suspected North Korean threat actors stole $351.6 million from its hot and warm wallets after a backend compromise. Cold wallets and the majority of platform assets reportedly remain unaffected.

### 2. CISA Adds Actively Exploited WSO2 and Adobe Commerce Flaws to KEV Catalog
- **Source:** The Hacker News — https://thehackernews.com/2026/09/wso2-and-adobe-commerce-flaws-exploited.html
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`
- **Summary:** CISA added two actively exploited flaws affecting WSO2 API Control Plane (CVE-2026-5430, CVSS 9.8, path traversal) and Adobe Commerce/Magento to its Known Exploited Vulnerabilities catalog. Second CVE details were truncated in the source feed.

### 3. Actively Exploited Roundcube Pre-Auth SQL Injection Flaw (CVE-2026-48842)
- **Source:** The Hacker News — https://thehackernews.com/2026/09/roundcube-pre-auth-sql-injection-flaw.html
- **Severity:** high
- **Tags:** `sqli`, `cve`, `vulnerability`
- **Summary:** The Canadian Centre for Cyber Security warned that CVE-2026-48842 (CVSS 8.1), a pre-auth SQL injection in Roundcube's virtuser_query plugin, is being actively exploited. Affects 1.6.x before 1.6.16 and 1.7.x before 1.7.1.

### 4. 'SalesBleed' Flaws in Salesforce Agentforce Enabled Zero-Click Data Exfiltration
- **Source:** SecurityWeek — https://www.securityweek.com/salesbleed-flaws-in-salesforce-agentforce-enabled-zero-click-data-exfiltration/
- **Severity:** high
- **Tags:** `ai-safety`, `llm`, `vulnerability`
- **Summary:** Three vulnerabilities in Salesforce Agentforce, dubbed "SalesBleed," allowed attackers to hijack trusted AI agents for zero-click data theft and phishing, without requiring user interaction.

### 5. Cloudflare Fixes Flaw Letting Containers Read Other Customers' Leftover Disk Data
- **Source:** The Hacker News — https://thehackernews.com/2026/09/cloudflare-fixes-flaw-that-let-one.html
- **Severity:** high
- **Tags:** `cloud-security`, `container-security`, `vulnerability`
- **Summary:** A flaw in Cloudflare Containers let one paying customer's container read leftover disk data from another customer's earlier container on the same server. Cloudflare says the exposure was limited to released disk space, not live workloads.

### 6. Windows, Linux, and Android File Notification Systems Found to Leak User Activity
- **Source:** SecurityWeek — https://www.securityweek.com/windows-linux-android-file-notification-systems-leak-user-activity/
- **Severity:** medium
- **Tags:** `vulnerability`, `appsec`
- **Summary:** Researchers showed that file-change notification APIs on Windows, Linux, and Android can leak keystroke timing, browsing activity, and WhatsApp media events to unprivileged observers.

### 7. Research: Trusted Execution Environments Can Undermine MPC Threshold Signatures
- **Source:** Trail of Bits — https://blog.trailofbits.com/2026/09/25/dont-let-tees-break-your-mpc/
- **Severity:** informational
- **Tags:** `vulnerability`, `appsec`
- **Summary:** Trail of Bits detailed how running MPC threshold-signature schemes inside TEEs can create subtle security gaps if the untrusted host isn't accounted for, aimed at teams building threshold-signature systems on TEE-backed infrastructure.

### 8. Doubts Grow Over Claims That an OpenAI Agent Hacked Australia's Medicare Portal
- **Source:** The Record (Recorded Future) — https://therecord.media/openai-australia-breach-cyber
- **Severity:** informational
- **Tags:** `ai-safety`, `llm`, `openai`
- **Summary:** Researchers are questioning earlier claims that an OpenAI agent "hacked" an Australian government health portal, after finding the site's archived code explicitly directed visitors to an unauthenticated endpoint.

## Skippable

- **Kosovar Owner of Rydox Marketplace Pleads Guilty in US Court** — SecurityWeek. Routine legal proceeding for a previously-disrupted marketplace, no new technical detail.
- **Rydox marketplace admin pleads guilty, faces 22 years in prison** — BleepingComputer. Duplicate coverage of the same guilty plea (see SecurityWeek item above).
- **Microsoft thinks its new Copilot 'super app' will be as influential as Office** — The Verge AI. Product/marketing bundling announcement, no security or model-capability substance.
- **Microsoft: Recent Windows updates cause desktop loading issues** — BleepingComputer. Generic IT bug report, no security angle.
- **Hackers steal $351.6 million in Bitget crypto exchange hack** — BleepingComputer. Duplicate coverage of the Bitget hack, merged into that item's sources above.
- **Russia's Hybrid Cyber-Physical War in Europe Heats Up** — Dark Reading. Broad narrative/opinion piece, no new discrete incident or IOC.
- **Roundcube Webmail Vulnerability in Attackers' Crosshairs** — SecurityWeek. Duplicate coverage of the Roundcube CVE-2026-48842 story, merged into that item's sources above.
- **Lightspeed targets $250M for new India fund, focusing on early-stage AI** — TechCrunch AI. VC funding news, no security or technical AI substance.
