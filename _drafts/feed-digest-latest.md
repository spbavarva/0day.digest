# Digest — 2026-07-16 AM

- Window: last 14h
- Raw items considered: 19
- Relevant: 9
- Skippable: 10

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** xAI Open-Sources Grok CLI After It Silently Uploaded Users' Files to the Cloud — `2026-07-15-xai-grok-cli-uploads-user-files-cloud-storage.md`
- [x] **[CRITICAL]** Zoom Patches Critical Windows Flaw Enabling Account Takeover (CVE-2026-53412) — `2026-07-16-zoom-critical-windows-account-takeover-cve-2026-53412.md`
- [x] **[HIGH]** Forgotten UEFI Shim Bootloaders Leave a Years-Long Secure Boot Blind Spot — `2026-07-15-forgotten-uefi-bootloaders-secure-boot-bypass.md`
- [x] **[HIGH]** Researcher Drops 'LegacyHive' Windows Zero-Day, Withholds Full PoC — `2026-07-16-legacyhive-windows-zero-day.md`
- [x] **[HIGH]** Trend Micro, Tanium, ESET, and Tenable Patch Severe Product Vulnerabilities — `2026-07-16-trend-micro-tanium-eset-tenable-patch-vulnerabilities.md`
- [x] **[INFORMATIONAL]** Unit 42 Updates Its Map of the Post-Shai-Hulud npm Threat Landscape — `2026-07-15-unit42-npm-threat-landscape-update.md`
- [x] **[INFORMATIONAL]** Identity Attacks Overtake Exploits as Leading Ransomware Root Cause — `2026-07-15-identity-attacks-top-ransomware-cause.md`
- [x] **[INFORMATIONAL]** Trump Administration Launches AI-Assisted Cyber Vulnerability Clearinghouse 'Gold Eagle' — `2026-07-15-gold-eagle-ai-vulnerability-clearinghouse.md`
- [x] **[INFORMATIONAL]** xAI Sues User Over Alleged Use of Grok to Generate CSAM — `2026-07-15-xai-sues-user-grok-csam-lawsuit.md`

## Relevant (details)

### 1. xAI Open-Sources Grok CLI After It Silently Uploaded Users' Files to the Cloud
- **Source:** Simon Willison — https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything
- **Severity:** critical
- **Tags:** `data-breach`, `llm`, `ai-safety`
- **Summary:** xAI's open-sourced Grok CLI tool uploaded entire local directories — including one user's SSH keys and password manager database — to xAI's Google Cloud buckets when run. xAI has not published a technical explanation; Musk acknowledged the issue but remediation details are thin.

### 2. Zoom Patches Critical Windows Flaw Enabling Account Takeover (CVE-2026-53412)
- **Source:** The Hacker News — https://thehackernews.com/2026/07/zoom-patches-critical-windows-flaw-that.html
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`
- **Summary:** CVE-2026-53412 (CVSS 9.8) is an improper input validation flaw in Zoom's Windows Desktop Client, VDI Client, and Meeting SDK that could enable account takeover. Zoom has released patches; no active exploitation reported.

### 3. Forgotten UEFI Shim Bootloaders Leave a Years-Long Secure Boot Blind Spot
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/forgotten-bootloaders-expose-secure-boot-blind-spot
- **Severity:** high
- **Tags:** `vulnerability`, `microsoft`
- **Summary:** Nearly a dozen vulnerable, now-revoked UEFI shim bootloaders remained trusted for years, giving attackers a Secure Boot bypass path.

### 4. Researcher Drops 'LegacyHive' Windows Zero-Day, Withholds Full PoC
- **Source:** SecurityWeek — https://www.securityweek.com/nightmare-eclipse-drops-legacyhive-windows-zero-day/
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `microsoft`
- **Summary:** A researcher published a Windows zero-day ("LegacyHive") but stripped the PoC to prevent immediate exploitation. No Microsoft patch is available yet and no active exploitation has been reported.

### 5. Trend Micro, Tanium, ESET, and Tenable Patch Severe Product Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/trend-micro-tanium-eset-and-tenable-patch-severe-product-vulnerabilities/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`
- **Summary:** Four security vendors shipped patches for critical/high-severity vulnerabilities in their own products this week. Specific CVEs and exploitation details weren't in the initial reporting.

### 6. Unit 42 Updates Its Map of the Post-Shai-Hulud npm Threat Landscape
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/
- **Severity:** informational
- **Tags:** `supply-chain`, `npm`
- **Summary:** Unit 42 refreshed its analysis of npm supply chain attack surface post-Shai-Hulud, covering wormable malware, CI/CD persistence, and multi-stage attacks.

### 7. Identity Attacks Overtake Exploits as Leading Ransomware Root Cause
- **Source:** Dark Reading — https://www.darkreading.com/identity-access-management-security/identity-attacks-overtake-exploits-top-ransomware-cause
- **Severity:** informational
- **Tags:** `ransomware`, `iam`
- **Summary:** Identity-based attacks overtook exploited vulnerabilities as the top ransomware root cause last year; MFA was present in 97% of credential-based attacks but still failed to stop compromise.

### 8. Trump Administration Launches AI-Assisted Cyber Vulnerability Clearinghouse 'Gold Eagle'
- **Source:** The Record (Recorded Future) — https://therecord.media/gold-eagle-cybersecurity-vulnerabilities-clearinghouse
- **Severity:** informational
- **Tags:** `vulnerability`, `ai-safety`
- **Summary:** The administration announced "Gold Eagle," an AI-supported clearinghouse meant to help industry and government detect, prioritize, and patch vulnerabilities faster.

### 9. xAI Sues User Over Alleged Use of Grok to Generate CSAM
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/966293/xai-grok-user-lawsuit-csam
- **Severity:** informational
- **Tags:** `ai-safety`, `llm`
- **Summary:** xAI is suing a South Carolina man it alleges used Grok to circumvent safeguards and generate/distribute CSAM. A legal action rather than a technical disclosure.

## Skippable

- **China's Top Cybersecurity Firms Hit by Mounting Military Procurement Bans** — SecurityWeek. Procurement/policy story, no technical security content.
- **Old UEFI Shims Expose Systems to Secure Boot Bypass** — SecurityWeek. Duplicate coverage; Dark Reading version used instead.
- **Police Disrupt a €140M Cyber Fraud Ring in Spain** — Dark Reading. Regional law enforcement action, no TTPs or technical detail.
- **Applied Computing wants to give oil and gas operators an AI model for the entire plant** — TechCrunch AI. Funding announcement, no security angle.
- **Mermaid to Unicode box art (grok-mermaid)** — Simon Willison. Niche hobby tool post, no news value.
- **Microsoft is reportedly training salespeople to talk down OpenAI and Anthropic** — TechCrunch AI. Competitive business gossip, not security/technical.
- **Dutch police bust investment fraud ring stealing over €100 million** — BleepingComputer. Regional law enforcement, no technical substance.
- **Zoom warns of critical account takeover vulnerability** — BleepingComputer. Duplicate coverage; The Hacker News version used instead.
- **AI slop movies are the new direct-to-video cash grabs** — The Verge AI. Opinion/culture piece, no security or technical AI substance.
- **Amid hardware legal battle, OpenAI releases a $230 keyboard for Codex** — TechCrunch AI. Product marketing/accessory launch, no substantive news.
