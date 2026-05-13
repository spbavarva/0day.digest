# Digest — 2026-05-13 AM

- Window: last 14h
- Raw items considered: 23
- Relevant: 8
- Skippable: 15

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** GemStuffer: 500+ Malicious RubyGems Packages Used as Data Exfiltration Channel — `2026-05-13-gemstuffer-rubygems-supply-chain-exfiltration.md`
- [x] **[HIGH]** Foxconn Confirms Cyberattack Impacting North American Manufacturing Factories — `2026-05-12-foxconn-cyberattack-north-america-factories.md`
- [x] **[MEDIUM]** US House Committee Demands Instructure Testimony on Canvas ShinyHunters Breaches — `2026-05-12-canvas-instructure-congressional-inquiry.md`
- [x] **[MEDIUM]** May 2026 Patch Tuesday: Near-Record Volumes as AI-Assisted Bug Discovery Accelerates — `2026-05-12-may-2026-patch-tuesday-ai-bug-hunting.md`
- [x] **[MEDIUM]** AWS Security Agent Gains Full Repository Code Scanning in Preview — `2026-05-12-aws-security-agent-full-repo-code-scanning.md`
- [x] **[MEDIUM]** UK ICO Fines South Staffordshire Water £963k Over Breach Exposing 664k Records — `2026-05-12-south-staffordshire-water-data-breach-fine.md`
- [x] **[MEDIUM]** Android Adds Forensic Intrusion Logging for Spyware Investigation — `2026-05-13-android-intrusion-logging-spyware-forensics.md`
- [x] **[MEDIUM]** Signal Rolls Out In-App Warnings Against Phishing and Social Engineering — `2026-05-12-signal-phishing-social-engineering-warnings.md`

## Relevant (details)

### 1. GemStuffer: 500+ Malicious RubyGems Packages Used as Data Exfiltration Channel
- **Source:** The Hacker News — https://thehackernews.com/2026/05/gemstuffer-abuses-150-rubygems-to.html
- **Severity:** high
- **Tags:** `supply-chain`, `data-breach`, `rubygems`
- **Summary:** The GemStuffer campaign pushed 500+ malicious packages to RubyGems, using the registry as a covert exfiltration channel for scraped UK council portal data rather than targeting developer machines directly. RubyGems temporarily suspended package registrations in response.

### 2. Foxconn Confirms Cyberattack Impacting North American Manufacturing Factories
- **Source:** The Record (Recorded Future) — https://therecord.media/foxconn-confirms-cyberattack-north-american-factories
- **Severity:** high
- **Tags:** `malware`, `data-breach`
- **Summary:** Foxconn confirmed a cyberattack hitting factories across six US states and Mexico; no threat actor or attack type disclosed. As the world's largest electronics contract manufacturer, disruptions could affect supply chains for Apple, Microsoft, and others.

### 3. US House Committee Demands Instructure Testimony on Canvas ShinyHunters Breaches
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/us-govt-seeks-instructure-testimony-on-massive-canvas-cyberattack/
- **Severity:** medium
- **Tags:** `data-breach`, `ransomware`
- **Summary:** The House Committee on Homeland Security is demanding Instructure executives testify about two ShinyHunters attacks on Canvas LMS. Congressional scrutiny follows the company's reported ransom payment to suppress the data leak.

### 4. May 2026 Patch Tuesday: Near-Record Volumes as AI-Assisted Bug Discovery Accelerates
- **Source:** Krebs on Security — https://krebsonsecurity.com/2026/05/patch-tuesday-may-2026-edition/
- **Severity:** medium
- **Tags:** `vulnerability`, `microsoft`, `google`, `apple`
- **Summary:** Apple, Google, Microsoft, Mozilla, and Oracle patched near-record bug volumes, with Krebs attributing the acceleration to AI tools finding code vulnerabilities faster. Microsoft's 137-flaw batch included no zero-days for the first time in two years.

### 5. AWS Security Agent Gains Full Repository Code Scanning in Preview
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/aws-security-agent-full-repository-code-scanning-feature-now-available-in-preview/
- **Severity:** medium
- **Tags:** `aws`, `appsec`, `ai-launch`, `cloud-security`
- **Summary:** AWS Security Agent now performs deep AI-driven code scanning across entire codebases, generating working exploits to validate findings. Positions AWS as a direct competitor to third-party SAST tools for cloud-native teams.

### 6. UK ICO Fines South Staffordshire Water £963k Over Breach Exposing 664k Records
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/uk-fines-water-supplier-13m-for-exposing-data-of-664k-customers/
- **Severity:** medium
- **Tags:** `data-breach`
- **Summary:** The UK ICO fined South Staffordshire Water £963,900 after a cyberattack exposed data on 663,887 customers and employees. Signals heightened regulatory pressure on critical infrastructure operators under UK GDPR.

### 7. Android Adds Forensic Intrusion Logging for Spyware Investigation
- **Source:** The Hacker News — https://thehackernews.com/2026/05/android-adds-intrusion-logging-for.html
- **Severity:** medium
- **Tags:** `malware`, `appsec`, `google`
- **Summary:** Google's opt-in Intrusion Logging feature in Android Advanced Protection Mode stores privacy-preserving forensic logs for spyware investigation. Targeted at high-risk users — journalists, activists, executives — facing sophisticated surveillance tools.

### 8. Signal Rolls Out In-App Warnings Against Phishing and Social Engineering
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/signal-adds-security-warnings-for-social-engineering-phishing-attacks/
- **Severity:** medium
- **Tags:** `phishing`
- **Summary:** Signal added in-app warning dialogs to protect users from phishing and social engineering attempts. Applied automatically to existing users; no settings change required.

## Skippable

- **Data centers are coming for rural America** — The Verge AI. Infrastructure/economic story; no security angle.
- **Chipmaker Patch Tuesday: Intel and AMD Patch 70 Vulnerabilities** — SecurityWeek. Duplicate Patch Tuesday coverage; no individual CVE flagged as critical or actively exploited.
- **Hundreds of Malicious Packages Force RubyGems to Suspend Registrations** — SecurityWeek. Duplicate of GemStuffer campaign coverage; THN item has more technical detail.
- **ICS Patch Tuesday: New Security Advisories From Siemens, Schneider, CISA** — SecurityWeek. Routine ICS advisory roundup; no standout critical findings.
- **CSP Allow-list Experiment** — Simon Willison. Developer experiment; no practitioner news value.
- **Medicare's new payment model is built for AI** — TechCrunch AI. Healthcare policy; no security angle.
- **datasette 1.0a29** — Simon Willison. Open-source library release notes; no security angle.
- **Sam Altman was winning on the stand** — The Verge AI. Legal/business trial coverage; no technical security content.
- **Quoting Mo Bitar** — Simon Willison. Satire about AI hype; opinion, no news value.
- **Quoting Mitchell Hashimoto** — Simon Willison. Enterprise tech commentary; opinion, no news value.
- **It's Patch Tuesday for Microsoft and Not a Zero-Day In Sight** — Dark Reading. Duplicate Patch Tuesday coverage; key detail surfaced in the Krebs item.
- **Meta won't let you block its AI account on Threads** — The Verge AI. Social media feature; no technical security content.
- **Microsoft Patch Tuesday for May 2026 — Snort rules and prominent vulnerabilities** — Cisco Talos. Duplicate Patch Tuesday coverage.
- **Congressman launches inquiry into how food retailers use surveillance pricing** — The Record. Consumer data privacy policy; no technical security angle.
- **Webinar: Fixing the gaps in network incident response** — BleepingComputer. Sponsored webinar announcement; marketing content.
