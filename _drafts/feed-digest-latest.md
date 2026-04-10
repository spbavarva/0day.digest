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
- **Severity:** critical
- **Tags:** `rce`, `cve`, `zero-day`, `vulnerability`
- **Summary:** CVE-2026-39987 is a pre-authenticated RCE (CVSS 9.3) in Marimo, an open-source Python notebook. Sysdig observed active exploitation within 10 hours of the public advisory; all unpatched instances reachable from the network should be treated as at risk.

### 2. Ransomware Attack on ChipSoft Disrupts Dutch Hospital Digital Services
- **Source:** The Record (Recorded Future) — https://therecord.media/chipsoft-ransomware-attack-disrupts-dutch-hospitals
- **Severity:** high
- **Tags:** `ransomware`, `supply-chain`, `healthcare`
- **Summary:** Ransomware struck ChipSoft, a Dutch healthcare software vendor, disabling digital services used by hospitals across the Netherlands. Downstream operational impact across multiple institutions; TTPs and attribution not yet public.

### 3. Chrome 147 Patches 60 Vulnerabilities Including Two Critical WebML Flaws
- **Source:** SecurityWeek — https://www.securityweek.com/chrome-147-patches-60-vulnerabilities-including-two-critical-flaws-worth-86000/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `google`, `browser-security`
- **Summary:** Chrome 147 patches 60 vulnerabilities including two Critical flaws in the WebML component, earning $86,000 in bounty. No active exploitation reported; update promptly.

### 4. Microsoft Discloses EngageLab SDK Flaw Exposing Millions of Android Crypto Wallet Users
- **Source:** SecurityWeek — https://www.securityweek.com/microsoft-finds-vulnerability-exposing-millions-of-android-crypto-wallet-users/
- **Severity:** high
- **Tags:** `vulnerability`, `microsoft`, `android`, `mobile-security`
- **Summary:** A vulnerability in the EngageLab SDK reported by Microsoft exposes millions of Android crypto wallet users; the flaw was disclosed to the vendor ~1 year ago and is now public. SDK flaws multiply impact across every embedding app.

### 5. Google Ships Device Bound Session Credentials in Chrome 146 to Block Cookie Theft
- **Source:** The Hacker News — https://thehackernews.com/2026/04/google-rolls-out-dbsc-in-chrome-146-to.html
- **Severity:** medium
- **Tags:** `google`, `appsec`, `browser-security`, `iam`
- **Summary:** DBSC is now GA on Windows in Chrome 146, binding session tokens to hardware so stolen cookies cannot be replayed. Directly counters info-stealer and adversary-in-the-browser MFA bypass techniques.

### 6. AI Browser Extensions Are an Unguarded Enterprise Threat Surface, LayerX Report Finds
- **Source:** The Hacker News — https://thehackernews.com/2026/04/browser-extensions-are-new-ai.html
- **Severity:** medium
- **Tags:** `llm`, `appsec`, `browser-security`, `ai-safety`
- **Summary:** LayerX documents AI browser extensions as a largely unmonitored threat surface that can access page content and session tokens, bypassing network controls. Shadow AI governance programs are not accounting for extensions.

### 7. Google Extends Gmail End-to-End Encryption to Android and iOS for Enterprise Users
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/google/google-rolls-out-gmail-end-to-end-encryption-on-mobile-devices/
- **Severity:** informational
- **Tags:** `google`, `appsec`, `cloud-security`
- **Summary:** Gmail E2EE is now available on Android and iOS for enterprise Workspace users without third-party tools. Relevant for regulated industries with encrypted email compliance requirements.

### 8. MITRE Publishes Fight Fraud Framework for Behavior-Based Fraud Tactic Modeling
- **Source:** SecurityWeek — https://www.securityweek.com/mitre-releases-fight-fraud-framework/
- **Severity:** informational
- **Tags:** `appsec`, `devsecops`, `fraud`
- **Summary:** MITRE released the Fight Fraud Framework, an ATT&CK-style model for fraud tactics and techniques. Useful for fintech and banking defenders structuring detection logic or fraud-focused tabletop exercises.

## Skippable

- **Gen Z's love-hate relationship with AI** — The Verge AI. Opinion/sociological piece, no technical news or security angle.
- **Microsoft starts removing Copilot buttons from Windows 11 apps** — The Verge AI. UI change only, no security implications.
- **Critical Marimo Flaw Exploited Hours After Public Disclosure** — SecurityWeek. Duplicate of item 1; THN version includes CVE ID and CVSS score.
- **Google Rolls Out Cookie Theft Protections in Chrome** — SecurityWeek. Duplicate of item 5; THN version has more technical context.
- **Backdoored Smart Slider 3 Pro Update Distributed via Compromised Nextend Servers** — The Hacker News. Already published on 2026-04-09 from BleepingComputer coverage.
