# Digest — 2026-04-10 AM

- Window: last 14h
- Raw items considered: 13
- Relevant: 8
- Skippable: 5

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Marimo CVE-2026-39987: Pre-Auth RCE Exploited Within 10 Hours of Disclosure — `2026-04-10-marimo-rce-cve-2026-39987-active-exploit.md`
- [x] **[HIGH]** Ransomware Attack on ChipSoft Disrupts Dutch Hospital Digital Services — `2026-04-09-chipsoft-ransomware-dutch-hospitals.md`
- [x] **[HIGH]** Chrome 147 Patches 60 Vulnerabilities Including Two Critical WebML Flaws — `2026-04-10-chrome-147-patches-60-vulns-two-critical.md`
- [x] **[HIGH]** Microsoft Discloses EngageLab SDK Flaw Exposing Millions of Android Crypto Wallet Users — `2026-04-10-android-crypto-wallet-sdk-vulnerability.md`
- [x] **[MEDIUM]** Google Ships Device Bound Session Credentials in Chrome 146 to Block Cookie Theft — `2026-04-10-chrome-dbsc-session-cookie-theft-protection.md`
- [x] **[MEDIUM]** AI Browser Extensions Are an Unguarded Enterprise Threat Surface, LayerX Report Finds — `2026-04-10-ai-browser-extensions-threat-surface.md`
- [x] **[INFORMATIONAL]** Google Extends Gmail End-to-End Encryption to Android and iOS for Enterprise Users — `2026-04-10-gmail-e2ee-mobile-rollout.md`
- [x] **[INFORMATIONAL]** MITRE Publishes Fight Fraud Framework for Behavior-Based Fraud Tactic Modeling — `2026-04-10-mitre-fight-fraud-framework.md`

## Relevant (details)

### 1. Marimo CVE-2026-39987: Pre-Auth RCE Exploited Within 10 Hours of Disclosure
- **Source:** The Hacker News — https://thehackernews.com/2026/04/marimo-rce-flaw-cve-2026-39987.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `zero-day`, `vulnerability`
- **Slug:** `2026-04-10-marimo-rce-cve-2026-39987-active-exploit`
- **Must-know:** yes
- **Summary:** CVE-2026-39987 is a pre-authenticated RCE (CVSS 9.3) in Marimo, a widely-used open-source Python notebook. Sysdig observed a threat actor build a working exploit and begin active exploitation within 10 hours of the public advisory dropping.

### 2. Ransomware Attack on ChipSoft Disrupts Dutch Hospital Digital Services
- **Source:** The Record (Recorded Future) — https://therecord.media/chipsoft-ransomware-attack-disrupts-dutch-hospitals
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`, `supply-chain`, `healthcare`
- **Slug:** `2026-04-09-chipsoft-ransomware-dutch-hospitals`
- **Must-know:** no
- **Summary:** Ransomware hit ChipSoft, a Dutch healthcare software vendor, forcing it to disable digital services used by hospitals and patients across the Netherlands. The attack has downstream operational impact across multiple healthcare institutions; TTPs and attribution have not yet been disclosed.

### 3. Chrome 147 Patches 60 Vulnerabilities Including Two Critical WebML Flaws
- **Source:** SecurityWeek — https://www.securityweek.com/chrome-147-patches-60-vulnerabilities-including-two-critical-flaws-worth-86000/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `google`, `browser-security`
- **Slug:** `2026-04-10-chrome-147-patches-60-vulns-two-critical`
- **Must-know:** no
- **Summary:** Chrome 147 ships patches for 60 vulnerabilities including two Critical flaws in the WebML component, earning $86,000 in combined bounty. No active exploitation reported; organizations should update promptly.

### 4. Microsoft Discloses EngageLab SDK Flaw Exposing Millions of Android Crypto Wallet Users
- **Source:** SecurityWeek — https://www.securityweek.com/microsoft-finds-vulnerability-exposing-millions-of-android-crypto-wallet-users/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `microsoft`, `android`, `mobile-security`
- **Slug:** `2026-04-10-android-crypto-wallet-sdk-vulnerability`
- **Must-know:** no
- **Summary:** Microsoft disclosed a vulnerability in the EngageLab SDK that exposes millions of Android crypto wallet users. The flaw was reported to the vendor approximately one year before public disclosure; SDK-level bugs multiply impact across every embedding application.

### 5. Google Ships Device Bound Session Credentials in Chrome 146 to Block Cookie Theft
- **Source:** The Hacker News — https://thehackernews.com/2026/04/google-rolls-out-dbsc-in-chrome-146-to.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `google`, `appsec`, `browser-security`, `iam`
- **Slug:** `2026-04-10-chrome-dbsc-session-cookie-theft-protection`
- **Must-know:** no
- **Summary:** Google has made DBSC generally available on Windows in Chrome 146, cryptographically binding session tokens to hardware so stolen cookies cannot be replayed. This directly counters info-stealer and adversary-in-the-browser techniques used to bypass MFA.

### 6. AI Browser Extensions Are an Unguarded Enterprise Threat Surface, LayerX Report Finds
- **Source:** The Hacker News — https://thehackernews.com/2026/04/browser-extensions-are-new-ai.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `llm`, `appsec`, `browser-security`, `ai-safety`
- **Slug:** `2026-04-10-ai-browser-extensions-threat-surface`
- **Must-know:** no
- **Summary:** LayerX reports that AI-powered browser extensions represent a largely unmonitored enterprise threat surface, able to access page content and session tokens in ways that bypass network controls. Security programs focused on shadow AI governance are largely not accounting for extensions.

### 7. Google Extends Gmail End-to-End Encryption to Android and iOS for Enterprise Users
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/google/google-rolls-out-gmail-end-to-end-encryption-on-mobile-devices/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `google`, `appsec`, `cloud-security`
- **Slug:** `2026-04-10-gmail-e2ee-mobile-rollout`
- **Must-know:** no
- **Summary:** Google has rolled out Gmail E2EE to Android and iOS for enterprise Workspace users, removing the previous requirement for S/MIME or third-party tools on mobile. Meaningful for regulated industries with encrypted email compliance requirements.

### 8. MITRE Publishes Fight Fraud Framework for Behavior-Based Fraud Tactic Modeling
- **Source:** SecurityWeek — https://www.securityweek.com/mitre-releases-fight-fraud-framework/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `appsec`, `devsecops`, `fraud`
- **Slug:** `2026-04-10-mitre-fight-fraud-framework`
- **Must-know:** no
- **Summary:** MITRE released the Fight Fraud Framework, an ATT&CK-style behavior model for fraud tactics and techniques. Useful for fintech, banking, and e-commerce defenders building detection logic or running fraud-focused tabletop exercises.

## Skippable

- **Gen Z's love-hate relationship with AI** — The Verge AI. Opinion/sociological piece about generational attitudes toward AI; no technical news or security angle.
- **Microsoft starts removing Copilot buttons from Windows 11 apps** — The Verge AI. UI change only, no security implications.
- **Critical Marimo Flaw Exploited Hours After Public Disclosure** — SecurityWeek. Duplicate coverage of Marimo CVE-2026-39987; The Hacker News version includes CVE ID and CVSS score.
- **Google Rolls Out Cookie Theft Protections in Chrome** — SecurityWeek. Duplicate coverage of Chrome DBSC (item 5); The Hacker News version has more technical context.
- **Backdoored Smart Slider 3 Pro Update Distributed via Compromised Nextend Servers** — The Hacker News. Story already published on 2026-04-09 from BleepingComputer coverage.
