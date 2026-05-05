# Digest — 2026-05-05 AM

- Window: last 14h
- Raw items considered: 16
- Relevant: 7
- Skippable: 9

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Weaver E-cology RCE CVE-2026-22679 Actively Exploited via Debug API — `2026-05-05-weaver-ecology-rce-cve-2026-22679-active-exploit.md`
- [x] **[CRITICAL]** cPanel Authentication-Bypass Flaw Draws Exploit Frenzy, Possible Zero-Day Claims — `2026-05-04-cpanel-auth-bypass-critical-exploit-frenzy.md`
- [x] **[HIGH]** Microsoft Tracks Large-Scale Phishing Campaign Targeting 35,000 Users Across 26 Countries — `2026-05-05-microsoft-phishing-credential-theft-35k-users.md`
- [x] **[HIGH]** RMM Tools Abused to Power Stealthy Phishing Campaign Against 80-Plus Organizations — `2026-05-04-rmm-tools-phishing-campaign-evasion.md`
- [x] **[HIGH]** Amazon SES Increasingly Abused in Phishing Campaigns to Bypass Email Security — `2026-05-04-amazon-ses-phishing-filter-bypass.md`
- [x] **[MEDIUM]** WhatsApp Discloses File Spoofing and Arbitrary URL Scheme Vulnerabilities — `2026-05-05-whatsapp-file-spoofing-url-scheme-vulnerabilities.md`
- [x] **[INFORMATIONAL]** IBM Releases Granite 4.1 LLM Family Under Apache 2.0 — `2026-05-04-ibm-granite-41-llm-family-open-source-release.md`

## Relevant (details)

### 1. Weaver E-cology RCE CVE-2026-22679 Actively Exploited via Debug API
- **Source:** The Hacker News — https://thehackernews.com/2026/05/weaver-e-cology-rce-flaw-cve-2026-22679.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`, `zero-day`
- **Slug:** `2026-05-05-weaver-ecology-rce-cve-2026-22679-active-exploit`
- **Must-know:** no
- **Summary:** CVE-2026-22679 (CVSS 9.8) is an unauthenticated RCE in Weaver E-cology enterprise OA software, actively exploited via the debug API endpoint since mid-March. Versions prior to the March 12 patch are affected; patch immediately or restrict `/papi/` access at the perimeter.

### 2. cPanel Authentication-Bypass Flaw Draws Exploit Frenzy, Possible Zero-Day Claims
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/exploit-cyber-frenzy-critical-cpanel-vulnerability
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `rce`, `zero-day`
- **Slug:** `2026-05-04-cpanel-auth-bypass-critical-exploit-frenzy`
- **Must-know:** yes
- **Summary:** A critical cPanel auth-bypass drew multiple PoC exploits immediately after disclosure; at least one researcher claims exploitation predates the patch by a month. cPanel's millions-strong deployment footprint elevates risk significantly.

### 3. Microsoft Tracks Large-Scale Phishing Campaign Targeting 35,000 Users Across 26 Countries
- **Source:** The Hacker News — https://thehackernews.com/2026/05/microsoft-details-phishing-campaign.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `microsoft`
- **Slug:** `2026-05-05-microsoft-phishing-credential-theft-35k-users`
- **Must-know:** no
- **Summary:** A multi-stage credential theft campaign (April 14–16) used code-of-conduct lures delivered via legitimate email services to steal authentication tokens from 35,000 users at 13,000+ organizations in 26 countries. The use of trusted sending infrastructure is a growing evasion technique.

### 4. RMM Tools Abused to Power Stealthy Phishing Campaign Against 80-Plus Organizations
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/rmm-tools-stealthy-phishing-campaign
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `malware`
- **Slug:** `2026-05-04-rmm-tools-phishing-campaign-evasion`
- **Must-know:** no
- **Summary:** Attackers are weaponizing two legitimate RMM tools as post-compromise C2 in a campaign affecting 80+ organizations. RMM software's allowlisted status in most enterprises makes behavioral detection largely ineffective.

### 5. Amazon SES Increasingly Abused in Phishing Campaigns to Bypass Email Security
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/amazon-ses-increasingly-abused-in-phishing-to-evade-detection/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `aws`, `cloud-security`
- **Slug:** `2026-05-04-amazon-ses-phishing-filter-bypass`
- **Must-know:** no
- **Summary:** Threat actors are routing phishing email through Amazon SES to leverage its high sender reputation and defeat blocklist-based filtering. Content and URL analysis are required to detect this vector; reputation alone is insufficient.

### 6. WhatsApp Discloses File Spoofing and Arbitrary URL Scheme Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/whatsapp-discloses-file-spoofing-arbitrary-url-scheme-vulnerabilities/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `meta`
- **Slug:** `2026-05-05-whatsapp-file-spoofing-url-scheme-vulnerabilities`
- **Must-know:** no
- **Summary:** Meta disclosed two patched WhatsApp bugs—file spoofing and an arbitrary URL scheme issue—found via bug bounty. No exploitation reported; users on current versions are not at risk.

### 7. IBM Releases Granite 4.1 LLM Family Under Apache 2.0
- **Source:** Simon Willison — https://simonwillison.net/2026/May/4/granite-41-3b-svg-pelican-gallery/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `model-release`, `llm`, `ai-launch`
- **Slug:** `2026-05-04-ibm-granite-41-llm-family-open-source-release`
- **Must-know:** no
- **Summary:** IBM released Granite 4.1 (3B, 8B, 30B) under Apache 2.0; Unsloth already has 21 GGUF quantized variants of the 3B available. Apache 2.0 licensing makes it viable for unrestricted commercial use.

## Skippable

- **As workers worry about AI, Nvidia's Jensen Huang says AI is 'creating jobs'** — TechCrunch AI. Opinion/commentary by Nvidia CEO without news value or technical substance.
- **Quoting John Gruber: Y Combinator's Stake in OpenAI** — Simon Willison. Financial analysis of YC's ~0.6% OpenAI stake; no security or technical angle.
- **OpenAI's president does 'all the things,' except answer a question** — The Verge AI. Coverage of the Musk vs. OpenAI trial proceedings; legal/business news without technical substance.
- **Weaver E-cology critical bug exploited in attacks since March** — BleepingComputer. Duplicate coverage of CVE-2026-22679; The Hacker News item selected as the more technically detailed source.
- **OpenAI's cozy partner Cerebras is on track for a blockbuster IPO** — TechCrunch AI. Business/financial news on AI chip company valuation; no security or technical angle.
- **OpenAI and PwC collaborate to reimagine the office of the CFO** — OpenAI Blog. Enterprise partnership marketing announcement without technical substance.
- **Quoting Andy Masley: pushback on data center land-use argument** — Simon Willison. Opinion commentary on data center land use; no security or technical angle.
- **April 2026 newsletter** — Simon Willison. Paywalled newsletter announcement; no standalone news value.
- **Image AI models now drive app growth, beating chatbot upgrades** — TechCrunch AI. App store market analysis; no security or AI technical substance.
