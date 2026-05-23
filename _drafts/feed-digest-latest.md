# Digest — 2026-05-23 PM

- Window: last 14h
- Raw items considered: 11
- Relevant: 8
- Skippable: 3

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** LiteSpeed cPanel Plugin CVE-2026-48172 Actively Exploited for Root Privilege Escalation — `2026-05-23-litespeed-cpanel-cve-2026-48172-privilege-escalation.md`
- [x] **[HIGH]** Packagist Supply Chain Attack Injects Linux Malware Into 8 Composer Packages — `2026-05-23-packagist-supply-chain-attack-8-packages.md`
- [x] **[HIGH]** Laravel-Lang PHP Packages Compromised to Deliver Cross-Platform Credential Stealer — `2026-05-23-laravel-lang-supply-chain-credential-stealer.md`
- [x] **[HIGH]** Drupal Core SQL Injection CVE-2026-9082 Actively Exploited, Added to CISA KEV — `2026-05-23-drupal-core-sqli-cve-2026-9082-cisa-kev.md`
- [x] **[HIGH]** 'Underminr' Vulnerability Enables DNS Filtering Bypass Across 88 Million Domains — `2026-05-23-underminr-vulnerability-dns-filtering-bypass.md`
- [x] **[HIGH]** Anthropic's Project Glasswing Uncovers 10,000 High-Severity Vulnerabilities in Critical Software — `2026-05-23-claude-mythos-glasswing-10000-vulnerabilities.md`
- [x] **[MEDIUM]** npm Launches Staged Publishing with 2FA Gating to Counter Supply Chain Attacks — `2026-05-23-npm-staged-publishing-2fa-supply-chain.md`
- [x] **[INFORMATIONAL]** Google Gemini Omni: Hands-On With the Anything-to-Anything Multimodal Model — `2026-05-23-google-gemini-omni-anything-to-anything-model.md`

## Relevant (details)

### 1. LiteSpeed cPanel Plugin CVE-2026-48172 Actively Exploited for Root Privilege Escalation
- **Source:** The Hacker News — https://thehackernews.com/2026/05/litespeed-cpanel-plugin-cve-2026-48172.html
- **Severity:** critical
- **Tags:** `cve`, `privilege-escalation`, `vulnerability`, `zero-day`
- **Summary:** CVE-2026-48172 (CVSS 10.0) in the LiteSpeed User-End cPanel Plugin is under active exploitation; any cPanel user can run arbitrary scripts as root via incorrect privilege assignment. Immediate patching required.

### 2. Packagist Supply Chain Attack Injects Linux Malware Into 8 Composer Packages
- **Source:** The Hacker News — https://thehackernews.com/2026/05/packagist-supply-chain-attack-infects-8.html
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `github`, `php`
- **Summary:** Eight Packagist Composer packages compromised in a coordinated attack; malicious code hidden in `package.json` downloads a Linux binary from GitHub Releases, evading Composer-focused security scanners.

### 3. Laravel-Lang PHP Packages Compromised to Deliver Cross-Platform Credential Stealer
- **Source:** The Hacker News — https://thehackernews.com/2026/05/laravel-lang-php-packages-compromised.html
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `data-breach`, `php`
- **Summary:** Four `laravel-lang` packages backdoored to deliver a cross-platform credential stealer; suspicious tag timing indicates maintainer pipeline compromise. Second Composer supply chain attack in today's window.

### 4. Drupal Core SQL Injection CVE-2026-9082 Actively Exploited, Added to CISA KEV
- **Source:** The Hacker News — https://thehackernews.com/2026/05/drupal-core-sql-injection-bug-actively.html
- **Severity:** high
- **Tags:** `sqli`, `cve`, `vulnerability`
- **Summary:** CISA added CVE-2026-9082 (SQLi in all supported Drupal Core versions, CVSS 6.5) to KEV based on confirmed active exploitation. 21-day federal remediation deadline; urgent for all Drupal operators.

### 5. 'Underminr' Vulnerability Enables DNS Filtering Bypass Across 88 Million Domains
- **Source:** SecurityWeek — https://www.securityweek.com/underminr-vulnerability-lets-attackers-hide-malicious-connections-behind-trusted-domains/
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`, `dns-bypass`
- **Summary:** "Underminr" affects ~88 million domains and enables C2 traffic concealment behind trusted domain names by exploiting DNS resolution path trust, bypassing perimeter DNS filtering controls.

### 6. Anthropic's Project Glasswing Uncovers 10,000 High-Severity Vulnerabilities in Critical Software
- **Source:** The Hacker News — https://thehackernews.com/2026/05/claude-mythos-ai-finds-10000-high.html
- **Severity:** high
- **Tags:** `anthropic`, `llm`, `ai-safety`, `vulnerability`
- **Summary:** Project Glasswing (Claude Mythos) has found over 10,000 high/critical vulnerabilities in globally critical software since last month's launch, significantly expanding on the earlier Mozilla collaboration. Signals AI-assisted auditing reshaping coordinated disclosure at scale.

### 7. npm Launches Staged Publishing with 2FA Gating to Counter Supply Chain Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/05/npm-adds-2fa-gated-publishing-and.html
- **Severity:** medium
- **Tags:** `npm`, `supply-chain`, `devsecops`
- **Summary:** GitHub made "staged publishing" GA on npm — requiring maintainer 2FA approval before a release is publicly installable. Directly counters account-takeover-based supply chain attacks.

### 8. Google Gemini Omni: Hands-On With the Anything-to-Anything Multimodal Model
- **Source:** The Verge AI — https://www.theverge.com/tech/936507/gemini-omni-hands-on-deepfake-ai-video
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `google`
- **Summary:** The Verge's hands-on with Gemini Omni highlights arbitrary-modality generation including realistic video synthesis. Relevant to deepfake detection and synthetic media policy teams tracking Google's multimodal capability trajectory.

## Skippable

- **Ferrari is using IBM's AI to create F1 superfans** — TechCrunch AI. Marketing/enterprise AI fan experience piece; no security or model-launch angle.
- **Italy disrupts CINEMAGOAL piracy app that stole streaming auth codes** — BleepingComputer. Law enforcement piracy bust; no novel technique or meaningful technical detail.
- **Elon Musk has given up on solar power (on Earth)** — TechCrunch AI. Energy/business opinion piece; no AI launch or security relevance.
