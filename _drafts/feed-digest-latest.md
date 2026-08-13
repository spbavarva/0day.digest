# Digest — 2026-08-13 AM

- Window: last 14h
- Raw items considered: 14
- Relevant: 9
- Skippable: 5

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[MEDIUM]** Armored Likho Expands Its Cyber-Espionage Toolkit — `2026-08-13-armored-likho-still-toolkit-telegram.md`
- [x] **[HIGH]** Belgium's eID Authentication System Opens Citizen Accounts to RCE — `2026-08-13-belgium-eid-authentication-rce.md`
- [x] **[HIGH]** Attackers Exploit SharePoint Auth Bypass After Public PoC Release (CVE-2026-55040) — `2026-08-13-sharepoint-auth-bypass-cve-2026-55040-exploited.md`
- [x] **[INFORMATIONAL]** DeepSeek Releases V4 Pro 0813 via API — `2026-08-12-deepseek-v4-pro-0813-release.md`
- [x] **[HIGH]** "City-Forum" Data-Theft Campaign Targets Salesforce, ServiceNow Portals — `2026-08-12-city-forum-data-theft-salesforce-servicenow.md`
- [x] **[HIGH]** Android Malware Combo Steals Cards via NFC Relay in Real Time — `2026-08-12-android-windrelay-spynote-nfc-malware.md`
- [x] **[INFORMATIONAL]** AWS IAM Role Manager Rethinks the Starting Point for IAM Roles — `2026-08-12-aws-iam-role-manager-launch.md`
- [x] **[HIGH]** Hackers Exploit Critical Adobe Commerce Flaw to Hijack Customer Accounts (CVE-2026-71362) — `2026-08-12-adobe-commerce-cve-2026-71362-exploited.md`
- [x] **[MEDIUM]** Hundreds of Fake Chrome VPN Extensions Route Traffic Through a Proxy — `2026-08-12-fake-chrome-vpn-extensions-proxy-campaign.md`

## Relevant (details)

### 1. Armored Likho Expands Its Cyber-Espionage Toolkit
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/armored-likho-still-toolkit/121033/
- **Severity:** medium
- **Tags:** `malware`, `data-breach`
- **Summary:** Kaspersky detailed a new Armored Likho campaign using fundraising lures to deliver an updated Still Toolkit that steals Telegram data and eavesdrops on victims.

### 2. Belgium's eID Authentication System Opens Citizen Accounts to RCE
- **Source:** Dark Reading — https://www.darkreading.com/application-security/belgium-eid-authentication-citizen-accounts-rce
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `appsec`
- **Summary:** Severe vulnerabilities in a browser extension underlying Belgium's eID trust framework allowed remote code execution against citizen accounts.

### 3. Attackers Exploit SharePoint Auth Bypass After Public PoC Release (CVE-2026-55040)
- **Source:** The Hacker News — https://thehackernews.com/2026/08/attackers-exploit-sharepoint.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`
- **Summary:** Attackers are exploiting CVE-2026-55040 (CVSS 9.1), a SharePoint auth bypass patched in July 2026, after PoC code went public.

### 4. DeepSeek Releases V4 Pro 0813 via API
- **Source:** Simon Willison — https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `deepseek`, `llm`
- **Summary:** DeepSeek's V4 Pro 0813 model is available via OpenRouter with no official announcement page yet; open weights are unconfirmed but plausible.

### 5. "City-Forum" Data-Theft Campaign Targets Salesforce, ServiceNow Portals
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/city-forum-data-theft-attacks-target-salesforce-servicenow-portals/
- **Severity:** high
- **Tags:** `data-breach`, `cloud-security`, `appsec`
- **Summary:** The "City-Forum" campaign has used custom tooling since at least March 2025 to steal data exposed to anonymous users via Salesforce Experience Cloud and ServiceNow portals.

### 6. Android Malware Combo Steals Cards via NFC Relay in Real Time
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/android-malware-combo-takes-out-loans-and-relays-victims-credit-cards/
- **Severity:** high
- **Tags:** `malware`
- **Summary:** A new Android NFC relay malware, WindRelay, is paired with the SpyNote RAT to take out fraudulent loans and relay live credit card data in real time.

### 7. AWS IAM Role Manager Rethinks the Starting Point for IAM Roles
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/how-aws-iam-role-manager-rethinks-the-starting-point-for-iam-roles/
- **Severity:** informational
- **Tags:** `iam`, `cloud-security`, `aws`
- **Summary:** AWS introduced IAM Role Manager to give teams a better default starting point for creating IAM roles, reducing overly broad permissions from the outset.

### 8. Hackers Exploit Critical Adobe Commerce Flaw to Hijack Customer Accounts (CVE-2026-71362)
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-adobe-commerce-flaw-to-hijack-customer-accounts/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`
- **Summary:** Active exploitation attempts have been detected against CVE-2026-71362, a critical Adobe Commerce/Magento vulnerability that could let attackers hijack customer accounts.

### 9. Hundreds of Fake Chrome VPN Extensions Route Traffic Through a Proxy
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hundreds-of-fake-chrome-vpn-extensions-route-traffic-through-a-proxy/
- **Severity:** medium
- **Tags:** `malware`, `appsec`
- **Summary:** More than 737 Chrome Web Store extensions impersonated VPN/proxy services while secretly routing user traffic through a single provider's SOCKS5 proxy network.

## Skippable

- **Some Claude users are mad that Anthropic's new watermarks will catch them using it at their jobs, classes** — TechCrunch AI. Social-media backlash story with no technical or security substance.
- **Long-running Data Theft Campaign Targeting Salesforce, ServiceNow** — Dark Reading. Duplicate coverage of the "City-Forum" campaign already captured via BleepingComputer.
- **Amazon will train on Twitch streamers' content by default, unless they opt out** — TechCrunch AI. Consumer data-policy/opt-out story, no security or AI-model-substance angle.
- **alchemy-utils 0.1a0** — Simon Willison. Personal side-project library experiment, not significant enough for a digest post.
- **AI coding startup Cognition reportedly already in talks to raise at $40B valuation** — TechCrunch AI. Funding/valuation news with no technical or security substance.
