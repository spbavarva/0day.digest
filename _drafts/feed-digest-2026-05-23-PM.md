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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `privilege-escalation`, `vulnerability`, `zero-day`
- **Slug:** `2026-05-23-litespeed-cpanel-cve-2026-48172-privilege-escalation`
- **Must-know:** yes
- **Summary:** CVE-2026-48172 (CVSS 10.0) in the LiteSpeed User-End cPanel Plugin is under active exploitation; any cPanel user can abuse incorrect privilege assignment to run arbitrary scripts as root. Immediate patching required for all LiteSpeed/cPanel environments.

### 2. Packagist Supply Chain Attack Injects Linux Malware Into 8 Composer Packages
- **Source:** The Hacker News — https://thehackernews.com/2026/05/packagist-supply-chain-attack-infects-8.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `github`, `php`
- **Slug:** `2026-05-23-packagist-supply-chain-attack-8-packages`
- **Must-know:** no
- **Summary:** Eight Packagist Composer packages were compromised in a coordinated attack; malicious code was hidden in `package.json` (not `composer.json`) to evade Composer-focused scanners, and downloads a Linux binary from GitHub Releases. Projects shipping both PHP and JavaScript are the primary target.

### 3. Laravel-Lang PHP Packages Compromised to Deliver Cross-Platform Credential Stealer
- **Source:** The Hacker News — https://thehackernews.com/2026/05/laravel-lang-php-packages-compromised.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `data-breach`, `php`
- **Slug:** `2026-05-23-laravel-lang-supply-chain-credential-stealer`
- **Must-know:** no
- **Summary:** Four `laravel-lang` packages were backdoored to deliver a cross-platform credential-stealing framework; suspicious tag timing points to a maintainer pipeline compromise rather than a single account takeover. A second Composer-ecosystem supply chain attack in the same day window.

### 4. Drupal Core SQL Injection CVE-2026-9082 Actively Exploited, Added to CISA KEV
- **Source:** The Hacker News — https://thehackernews.com/2026/05/drupal-core-sql-injection-bug-actively.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `sqli`, `cve`, `vulnerability`
- **Slug:** `2026-05-23-drupal-core-sqli-cve-2026-9082-cisa-kev`
- **Must-know:** no
- **Summary:** CISA added CVE-2026-9082 (SQLi in Drupal Core, all supported versions, CVSS 6.5) to its KEV catalog based on confirmed active exploitation. Federal agencies face a 21-day remediation deadline; all Drupal operators should treat this as urgent.

### 5. 'Underminr' Vulnerability Enables DNS Filtering Bypass Across 88 Million Domains
- **Source:** SecurityWeek — https://www.securityweek.com/underminr-vulnerability-lets-attackers-hide-malicious-connections-behind-trusted-domains/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`, `dns-bypass`
- **Slug:** `2026-05-23-underminr-vulnerability-dns-filtering-bypass`
- **Must-know:** no
- **Summary:** "Underminr" affects ~88 million domains and lets attackers hide C2 traffic behind trusted domain names by exploiting DNS resolution path trust. Security teams relying on DNS filtering as a primary defensive layer may not see this traffic in standard logs.

### 6. Anthropic's Project Glasswing Uncovers 10,000 High-Severity Vulnerabilities in Critical Software
- **Source:** The Hacker News — https://thehackernews.com/2026/05/claude-mythos-ai-finds-10000-high.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `anthropic`, `llm`, `ai-safety`, `vulnerability`
- **Slug:** `2026-05-23-claude-mythos-glasswing-10000-vulnerabilities`
- **Must-know:** no
- **Summary:** Anthropic's Project Glasswing (powered by Claude Mythos) has found over 10,000 high- or critical-severity vulnerabilities in globally critical software since launching last month, building on the earlier Mozilla Firefox collaboration (271 flaws). Signals a step-change in AI-assisted audit throughput with growing coordinated disclosure implications.

### 7. npm Launches Staged Publishing with 2FA Gating to Counter Supply Chain Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/05/npm-adds-2fa-gated-publishing-and.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `npm`, `supply-chain`, `devsecops`
- **Slug:** `2026-05-23-npm-staged-publishing-2fa-supply-chain`
- **Must-know:** no
- **Summary:** GitHub made "staged publishing" GA on npm — requiring a maintainer 2FA challenge before a release is publicly installable — plus new package install controls. Directly counters account-takeover-based supply chain attacks in the npm ecosystem.

### 8. Google Gemini Omni: Hands-On With the Anything-to-Anything Multimodal Model
- **Source:** The Verge AI — https://www.theverge.com/tech/936507/gemini-omni-hands-on-deepfake-ai-video
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `google`
- **Slug:** `2026-05-23-google-gemini-omni-anything-to-anything-model`
- **Must-know:** no
- **Summary:** The Verge's hands-on with Google's Gemini Omni highlights its arbitrary-modality input/output capabilities, including realistic video synthesis. Relevant to teams tracking AI-generated synthetic media for deepfake detection or content provenance work.

## Skippable

- **Ferrari is using IBM's AI to create F1 superfans** — TechCrunch AI. Marketing/enterprise AI use case with no security or model-launch angle; IBM-Ferrari fan experience partnership.
- **Italy disrupts CINEMAGOAL piracy app that stole streaming auth codes** — BleepingComputer. Law enforcement piracy bust; credential theft angle present but no technical detail or novel technique — primarily a legal/piracy story.
- **Elon Musk has given up on solar power (on Earth)** — TechCrunch AI. Energy/business opinion piece about xAI's power choices; no AI launch or security relevance.
