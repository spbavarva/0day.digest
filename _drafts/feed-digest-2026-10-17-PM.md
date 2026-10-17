# Digest — 2026-10-17 PM

- Window: last 14h
- Raw items considered: 8
- Relevant: 4
- Skippable: 4

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** ConnectWise Cloud Backup Breach Exposes 173 Microsoft 365 Tenants — `2026-10-17-connectwise-cloud-backup-supply-chain-m365-breach.md`
- [x] **[HIGH]** Drupal Patches Two Critical RCE Flaws, Warns of Imminent Exploitation — `2026-10-17-drupal-critical-rce-patches.md`
- [x] **[HIGH]** Malicious npm Package 'imgdecode' Hides Shellcode Loader in Windows Native Addon — `2026-10-17-malfex-npm-imgdecode-shellcode-loader.md`
- [x] **[HIGH]** Israeli Ad Firm's Network Doubled as Candiru Zero-Click Spyware Delivery Channel — `2026-10-17-candiru-zero-click-spyware-ad-network.md`

## Relevant (details)

### 1. ConnectWise Cloud Backup Breach Exposes 173 Microsoft 365 Tenants
- **Source:** The Hacker News — https://thehackernews.com/2026/10/hackers-use-compromised-connectwise.html
- **Also covered by:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-breach-microsoft-365-tenants-via-connectwise-supply-chain-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `data-breach`, `cloud-security`, `microsoft`
- **Slug:** `connectwise-cloud-backup-supply-chain-m365-breach`
- **Must-know:** yes
- **Summary:** Attackers used a compromised M365 credential tied to ConnectWise Cloud Backup to sign into 173 customer tenants via the service's application identities. ConnectWise has shut down customer access to the service while it investigates — a supply-chain-style compromise given how widely the platform is used by MSPs.

### 2. Drupal Patches Two Critical RCE Flaws, Warns of Imminent Exploitation
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/drupal-patches-critical-rce-flaws-warns-exploits-may-emerge-soon/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `drupal-critical-rce-patches`
- **Must-know:** no
- **Summary:** Drupal patched two critical RCE vulnerabilities affecting all supported versions and warned public exploits could appear soon. No active exploitation has been confirmed yet, so operators should patch proactively.

### 3. Malicious npm Package 'imgdecode' Hides Shellcode Loader in Windows Native Addon
- **Source:** The Hacker News — https://thehackernews.com/2026/10/malfex-npm-package-imgdecode-hides.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `npm`, `supply-chain`, `malware`
- **Slug:** `malfex-npm-imgdecode-shellcode-loader`
- **Must-know:** no
- **Summary:** A malicious npm package named "imgdecode," part of the MALFEX campaign, ships a Windows native addon hiding a shellcode loader. It was downloaded 979 times and remained live on npm as of disclosure.

### 4. Israeli Ad Firm's Network Doubled as Candiru Zero-Click Spyware Delivery Channel
- **Source:** SecurityWeek — https://www.securityweek.com/israeli-ad-firm-doubled-as-candirus-zero-click-spyware-delivery-channel/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `spyware`
- **Slug:** `candiru-zero-click-spyware-ad-network`
- **Must-know:** no
- **Summary:** Discover-Tech's ad network reportedly let threat actors fingerprint and track devices at scale and selectively deliver Candiru's zero-click spyware to chosen targets, no user interaction required.

## Skippable

- **Replit is no longer working with Anthropic, CEO says** — TechCrunch AI. Business/provider-swap news; no security or model substance.
- **Meta removes language that may have allowed it to scrape news sites** — The Verge AI. Internal ToS wording change following backlash, not a regulatory action or security event.
- **Websites are closing their doors to AI agents** — The Verge AI. Trend/feature piece on bot-blocking with no specific news hook or technical detail.
- **Hackers Use Compromised ConnectWise Credential to Sign In to 173 Microsoft 365 Tenants** — The Hacker News. Same story as the ConnectWise item above; merged as a second source rather than listed separately.
