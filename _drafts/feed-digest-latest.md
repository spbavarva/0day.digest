# Digest — 2026-06-09 AM

- Window: last 14h
- Raw items considered: 25
- Relevant: 8
- Skippable: 17

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Shai-Hulud Attack Trojanizes 19 Science-Focused PyPI Packages — `2026-06-08-shai-hulud-pypi-supply-chain-19-packages.md`
- [x] **[CRITICAL]** Check Point VPN Auth-Bypass Zero-Day Exploited by Qilin Ransomware, CISA Issues 3-Day Patch Order — `2026-06-09-check-point-vpn-zero-day-qilin-cisa.md`
- [x] **[CRITICAL]** LiteLLM CVE-2026-42271: Command Injection Chains to Unauthenticated RCE, Added to CISA KEV — `2026-06-09-litellm-cve-2026-42271-command-injection-rce.md`
- [x] **[HIGH]** Google Patches Chrome Zero-Day CVE-2026-11645, Fifth Exploited Flaw of 2026 — `2026-06-09-chrome-zero-day-cve-2026-11645.md`
- [x] **[HIGH]** NFCShare Android Malware Spreads via Fake Banking App Updates Hosted on GitHub — `2026-06-08-nfcshare-android-malware-github.md`
- [x] **[HIGH]** Silent Ransom Group Escalates Law Firm Attacks with Vishing and In-Person Office Intrusions — `2026-06-08-silent-ransom-group-law-firms.md`
- [x] **[MEDIUM]** Unit 42: Attackers Impersonate IT Support in Microsoft Teams Phishing Campaigns — `2026-06-08-microsoft-teams-it-impersonation-phishing.md`
- [x] **[INFORMATIONAL]** Apple Announces Automatic Compromised Password Replacement in iOS 27 — `2026-06-08-apple-intelligence-auto-password-fix.md`

## Relevant (details)

### 1. Shai-Hulud Attack Trojanizes 19 Science-Focused PyPI Packages
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-shai-hulud-attack-trojanizes-19-science-focused-pypi-packages/
- **Severity:** critical
- **Tags:** `supply-chain`, `pypi`, `malware`
- **Summary:** A supply-chain campaign dubbed Shai-Hulud has trojanized 19 PyPI packages in the scientific Python ecosystem, collectively downloaded hundreds of thousands of times, to deliver malware that steals developer secrets and credentials. All affected packages were legitimate prior to compromise; developers should rotate credentials and audit environments immediately.

### 2. Check Point VPN Auth-Bypass Zero-Day Exploited by Qilin Ransomware, CISA Issues 3-Day Patch Order
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-check-point-flaw-exploited-by-ransomware-gangs/
- **Severity:** critical
- **Tags:** `zero-day`, `ransomware`, `vulnerability`, `cve`
- **Summary:** A critical authentication bypass in Check Point Remote Access VPN lets attackers connect without a valid password; a Qilin ransomware affiliate has been exploiting it since early May. CISA added it to the KEV catalog and ordered federal agencies to patch within three days.

### 3. LiteLLM CVE-2026-42271: Command Injection Chains to Unauthenticated RCE, Added to CISA KEV
- **Source:** The Hacker News — https://thehackernews.com/2026/06/litellm-flaw-cve-2026-42271-exploited.html
- **Severity:** critical
- **Tags:** `llm`, `rce`, `vulnerability`, `cve`, `appsec`
- **Summary:** CVE-2026-42271 (CVSS 8.7) in BerriAI LiteLLM is a command injection flaw that escalates to unauthenticated RCE in practice, now on the CISA KEV list with confirmed active exploitation. LiteLLM is widely used as an AI gateway in production LLM pipelines, making this high-priority for AI infrastructure operators.

### 4. Google Patches Chrome Zero-Day CVE-2026-11645, Fifth Exploited Flaw of 2026
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/google-patches-fifth-chrome-zero-day-bug-exploited-in-attacks-this-year/
- **Severity:** high
- **Tags:** `zero-day`, `google`, `vulnerability`, `cve`
- **Summary:** Google patched CVE-2026-11645, a Chrome zero-day actively exploited in the wild and the fifth such flaw this year. Enterprise admins should confirm the update has rolled out across managed fleets.

### 5. NFCShare Android Malware Spreads via Fake Banking App Updates Hosted on GitHub
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/nfcshare-android-malware-spreads-via-fake-banking-app-updates-on-github/
- **Severity:** high
- **Tags:** `malware`, `android`, `github`
- **Summary:** New NFCShare variants are distributed as fake banking app updates hosted on GitHub, abusing the platform's trusted reputation to bypass URL-based defenses. The malware steals NFC payment data and banking credentials.

### 6. Silent Ransom Group Escalates Law Firm Attacks with Vishing and In-Person Office Intrusions
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/silent-ransom-us-law-firms-extortion-attacks
- **Severity:** high
- **Tags:** `ransomware`, `phishing`, `data-breach`, `social-engineering`
- **Summary:** The Silent Ransom Group is hitting US law firms with a multi-vector campaign blending vishing, IT impersonation, and physical in-person office intrusions—an unusual escalation for a financially motivated extortion group. Organizations should review physical access controls and out-of-band MFA requirements.

### 7. Unit 42: Attackers Impersonate IT Support in Microsoft Teams Phishing Campaigns
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/microsoft-teams-phishing/
- **Severity:** medium
- **Tags:** `phishing`, `microsoft`, `social-engineering`
- **Summary:** Unit 42 documents attackers increasingly impersonating IT support inside Microsoft Teams, exploiting the implicit trust of internal collaboration platforms to bypass email-phishing defenses. Defenders should restrict external Teams messaging and train users to verify IT requests out-of-band.

### 8. Apple Announces Automatic Compromised Password Replacement in iOS 27
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/apple/new-apple-feature-automatically-changes-your-compromised-passwords/
- **Severity:** informational
- **Tags:** `apple`, `iam`, `ai-launch`
- **Summary:** Apple's WWDC 26 unveiled an Apple Intelligence feature that automatically replaces weak or breached passwords in Safari/iCloud Keychain, rolling out with iOS 27. Limited to Safari; third-party browsers and password managers are unaffected.

## Skippable

- **Amazon employees ask Seattle to put the brakes on new data centers** — The Verge AI. Urban planning/policy item with no security angle.
- **NeuroBait: I fine-tuned a model to spark dopamine for ADHD brain** — Hugging Face Blog. Hackathon project with no security or substantive AI-launch relevance.
- **Check Point VPN Zero-Day Exploited in Qilin Ransomware Attacks** — SecurityWeek. Duplicate; BleepingComputer selected as primary source.
- **Google Patches 5th Chrome Zero-Day Exploited in 2026** — SecurityWeek. Duplicate; BleepingComputer selected as primary source.
- **Why Apple's slow-and-steady AI bet is starting to look pretty smart** — TechCrunch AI. Opinion piece without news value.
- **Mercor's Brendan Foody calls out Sequoia, accusing it of 'dual-pricing' valuation tricks** — TechCrunch AI. VC/finance drama with no security or AI-technical angle.
- **Siri AI at WWDC 2026** — Simon Willison. Analysis/opinion; no new security or model-launch substance.
- **As OpenAI files for IPO, Sam Altman's eye-scanning company is doing layoffs** — TechCrunch AI. Business/finance news without technical substance.
- **Apple's WWDC AI demos looked more real after $250M false ad settlement** — TechCrunch AI. Opinion/context piece, no security or model-launch substance.
- **Apple is using AI to fix Safari's extension problem** — The Verge AI. Consumer AI feature with no security relevance.
- **SoFi confirms third-party data breach at Hong Kong subsidiary** — BleepingComputer. Generic breach disclosure with no technical details or attacker TTPs.
- **OpenAI files for IPO, following Anthropic** — The Verge AI. Business/financial news without technical substance.
- **AWS Weekly Roundup** — AWS News Blog. Generic cloud services roundup with no security angle.
- **Apple plays catch-up at WWDC** — TechCrunch AI. WWDC overview/analysis, no new security or model substance.
- **ICYMI: May 2026 @AWS Security** — AWS Security Blog. Monthly marketing roundup with no actionable signal.
- **Apple bets cheaper AI will woo small developers** — TechCrunch AI. Developer incentive program with no security angle.
- **Check Point VPN Flaw Exploited Since Early May** — Dark Reading. Duplicate; consolidated into primary BleepingComputer post.
