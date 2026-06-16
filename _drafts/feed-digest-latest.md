# Digest — 2026-06-16 PM

- Window: last 14h
- Raw items considered: 38
- Relevant: 10
- Skippable: 28

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** SprySOCKS Gets a Windows Port: FishMonger APT Abuses Kernel Drivers to Evade Detection — `2026-06-16-sprysocks-windows-fishmonger-apt-kernel-driver.md`
- [x] **[HIGH]** Google Vertex AI SDK 'Pickle in the Middle' Flaw Allowed ML Model Hijacking via Bucket Squatting — `2026-06-16-google-vertex-ai-sdk-pickle-in-the-middle.md`
- [x] **[HIGH]** ClickFix Campaigns Deploy Three New Malware Loaders Targeting Education and Finance — `2026-06-16-clickfix-babadeda-lorem-ipsum-potemkin-loaders.md`
- [x] **[HIGH]** GhostTree: Recursive NTFS Junctions Force Microsoft Defender Folder Scans to Never Complete — `2026-06-16-ghosttree-ntfs-junctions-defender-evasion.md`
- [x] **[HIGH]** Rokarolla Android Trojan Targets 217 Banking and Crypto Apps with Near-Total Device Control — `2026-06-16-rokarolla-android-banking-trojan.md`
- [x] **[HIGH]** FulcrumSec Claims 1.3 TB Stolen from Novo Nordisk in Hack-and-Leak Operation — `2026-06-16-novo-nordisk-hack-fulcrumsec-1tb.md`
- [x] **[HIGH]** CISA Issues Five Rockwell Automation ICS Advisories, Including Critical CVSS 9.4 Auth Bypass — `2026-06-16-rockwell-ics-cisa-advisories-cvss-94.md`
- [x] **[MEDIUM]** Threat Actors Abuse Steam Workshop to Distribute Malware via Wallpaper Engine Packages — `2026-06-16-steam-workshop-malware-wallpaper-engine.md`
- [x] **[MEDIUM]** UK to Mandate ID Upload or Facial Age Scan Before Social Media Account Creation — `2026-06-16-uk-social-media-age-verification.md`
- [x] **[INFORMATIONAL]** AWS Threat Tactic Spotlight: Detecting and Preventing Subdomain Takeover via Dangling DNS — `2026-06-16-subdomain-takeover-aws-dangling-dns.md`

## Relevant (details)

### 1. SprySOCKS Gets a Windows Port: FishMonger APT Abuses Kernel Drivers to Evade Detection
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/sprysocks-windows-variant-kernel-drivers
- **Severity:** high
- **Tags:** `malware`, `apt`, `microsoft`, `vulnerability`
- **Summary:** FishMonger, a China-nexus threat group, has ported the SprySOCKS backdoor to Windows and deployed it against government targets in Honduras, Taiwan, Thailand, and Pakistan. The variant uses kernel driver abuse to evade endpoint detection—a notable escalation from the previously Linux-only implant.

### 2. Google Vertex AI SDK 'Pickle in the Middle' Flaw Allowed ML Model Hijacking via Bucket Squatting
- **Source:** The Hacker News — https://thehackernews.com/2026/06/google-vertex-ai-sdk-flaw-let-attackers.html
- **Severity:** high
- **Tags:** `vulnerability`, `supply-chain`, `google`, `gcp`, `cloud-security`, `llm`
- **Summary:** Unit 42 found that an attacker with zero GCP project access could squat the storage bucket Vertex AI uses for model uploads, causing the victim's ML model to land in attacker storage. Pickle deserialization then enables arbitrary code execution inside Google's model-serving infrastructure; patched, no wild exploitation confirmed.

### 3. ClickFix Campaigns Deploy Three New Malware Loaders Targeting Education and Finance
- **Source:** The Hacker News — https://thehackernews.com/2026/06/clickfix-campaigns-expand-malware.html
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Summary:** Three independently documented ClickFix campaigns deliver new loaders: BabaDeda (education/finance), Lorem Ipsum (compromised WordPress sites, linked to Vice Society ransomware group), and Potemkin (fake update lures). The technique tricks users into running malicious clipboard commands via fake browser error dialogs.

### 4. GhostTree: Recursive NTFS Junctions Force Microsoft Defender Folder Scans to Never Complete
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/ghosttree-attack-abused-recursive-windows-junctions-to-hide-malware/
- **Severity:** high
- **Tags:** `malware`, `vulnerability`, `microsoft`
- **Summary:** Varonis published GhostTree, a technique using recursive NTFS junctions to generate infinite valid Windows file paths that cause Microsoft Defender folder scans to loop indefinitely. No elevated privileges are required to create the junctions, leaving malware hidden inside the structure undetected.

### 5. Rokarolla Android Trojan Targets 217 Banking and Crypto Apps with Near-Total Device Control
- **Source:** The Hacker News — https://thehackernews.com/2026/06/new-rokarolla-android-malware-steals.html
- **Severity:** high
- **Tags:** `malware`, `data-breach`, `android`
- **Summary:** Zimperium's zLabs documented Rokarolla, an Android banking trojan with 137 remote commands targeting 217 banking and crypto apps. Capabilities include PIN exfiltration, OTP interception via SMS, clipboard hijacking for crypto redirects, and disabling Google Play Protect; distributed as fake TikTok and Chrome installers.

### 6. FulcrumSec Claims 1.3 TB Stolen from Novo Nordisk in Hack-and-Leak Operation
- **Source:** SecurityWeek — https://www.securityweek.com/cybercrime-group-claims-novo-nordisk-hack/
- **Severity:** high
- **Tags:** `data-breach`, `ransomware`
- **Summary:** Hack-and-leak group FulcrumSec claims to have stolen 1.3 TB from pharmaceutical giant Novo Nordisk; unconfirmed and unacknowledged by the company. FulcrumSec operates through data-theft extortion, threatening public dumps rather than encryption-based ransomware.

### 7. CISA Issues Five Rockwell Automation ICS Advisories, Including Critical CVSS 9.4 Auth Bypass
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-167-05
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `ics`
- **Summary:** Five CISA advisories cover Rockwell Automation OT products, led by FLEX I/O EtherNet/IP Adapters (CVE-2026-0646/0647, CVSS 9.4) enabling unauthorized access and account takeover. Additional issues affect CompactLogix/ControlLogix 5370/5570, RSLinx Classic, and FactoryTalk Analytics PavilionX across critical manufacturing, energy, and water sectors.

### 8. Threat Actors Abuse Steam Workshop to Distribute Malware via Wallpaper Engine Packages
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/steam-workshop-abused-to-spread-malware-via-wallpaper-engine-app/
- **Severity:** medium
- **Tags:** `malware`, `supply-chain`
- **Summary:** Attackers embed malware in Steam Workshop wallpaper packages for Wallpaper Engine, abusing the platform's trusted community distribution model to bypass endpoint security. Specific malware families dropped are not identified in this report.

### 9. UK to Mandate ID Upload or Facial Age Scan Before Social Media Account Creation
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/uk-to-require-id-or-face-scan-before-you-can-make-social-media-accounts/
- **Severity:** medium
- **Tags:** `privacy`, `regulation`, `data-breach`
- **Summary:** The UK government will ban under-16s from social media by requiring ID or facial age verification before account creation, effective spring 2027. Security experts warn the checks are easily circumvented and that age-verification systems centralizing biometric data create significant new data-breach targets.

### 10. AWS Threat Tactic Spotlight: Detecting and Preventing Subdomain Takeover via Dangling DNS
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/threat-tactic-spotlight-subdomain-takeover/
- **Severity:** informational
- **Tags:** `cloud-security`, `aws`
- **Summary:** AWS published a practitioner guide on subdomain takeover via dangling DNS, covering how attackers squat abandoned resources to serve phishing content or hijack OAuth flows. Covers Route 53 monitoring, S3/CloudFront audits, and AWS Config rules as mitigations.

## Skippable

- **New Rokarolla Android malware targets 217 banking, crypto apps** — BleepingComputer. Duplicate; The Hacker News has more complete Zimperium sourcing (story 5).
- **Android 17 launches with new multitasking tools** — TechCrunch AI. Generic OS product launch with no substantive security angle.
- **Rokarolla Android Trojan Levels Up to Full Device Control** — Dark Reading. Duplicate of Rokarolla story; The Hacker News has the primary technical sourcing.
- **Google named a Leader in IDC MarketScape SIEM 2026** — Google Cloud Security. Analyst ranking announcement; marketing content with no technical news value.
- **Apple 2027 rumors: AirPods with cameras for AI** — The Verge AI. Hardware product rumor; no security or AI-substance angle.
- **Qualcomm's latest chip hints at more powerful smart glasses** — The Verge AI. Hardware chip announcement; no security angle.
- **Sixty percent of US consumers say 'AI' in brand messaging is a turnoff** — TechCrunch AI. Consumer marketing survey; not technical, no security angle.
- **Quoting Georgi Gerganov** — Simon Willison. Commentary on local LLM coding usage; no security news value.
- **SpaceX is public: Everything you need to know post-IPO** — TechCrunch AI. Business/financial coverage; no AI or security angle.
- **India temporarily blocks Telegram over medical exam cheating** — The Record. Regional platform restriction for a non-security policy reason; no technical detail.
- **'Lorem Ipsum' Malware Pivots to ClickFix Delivery** — Dark Reading. Duplicate; covered in the broader ClickFix loaders story (story 3).
- **iRhythm Confirms Data Stolen in Hack** — SecurityWeek. Thin summary with no TTPs, IOCs, or breach scope; generic breach disclosure without technical substance.
- **DOJ claims xAI's unpermitted gas turbines are a matter of national security** — TechCrunch AI. Environmental/energy regulatory story; no security angle.
- **Plaud says its software business topped $100M in ARR** — TechCrunch AI. Business milestone; no security or technical AI news value.
- **Robinhood's note on 10% layoffs shows blaming AI isn't cutting it** — TechCrunch AI. Business/layoff news; no security or technical AI angle.
- **Hacker Conversations: Isira Adithya, the Evolution of an Ethical Hacker** — SecurityWeek. Profile/interview piece; no news value.
- **SpaceX passes Amazon as valuation balloons to $2.7T** — TechCrunch AI. Business/financial; duplicate SpaceX IPO coverage.
- **FTC warns of record $3.5 billion losses to imposter scams in 2025** — BleepingComputer. Aggregate statistics; no IOCs, novel techniques, or actionable technical guidance.
- **Magnitude Emerges From Stealth Mode With $10 Million in Funding** — SecurityWeek. Startup funding; marketing disguised as news.
- **AI and Cybersecurity – Everything You Wanted to Know, But Were Afraid to Ask** — SecurityWeek. Opinion survey roundup; no specific news event or technical disclosure.
- **Probably raises $9M to build a more reliable kind of AI** — TechCrunch AI. AI startup funding; no technical or security substance.
- **Endpoint Security Startup Ent Emerges From Stealth With $100 Million Seed Round** — SecurityWeek. Startup funding; marketing content.
- **Can CISOs Trust Their Applications? TrustCloud Wants to Replace the Questionnaire** — SecurityWeek. Product marketing; no news value.
- **Rockwell Automation Logix 5370 & 5570 Controllers (ICSA-26-167-03)** — CISA Alerts. Covered in the Rockwell ICS batch advisory post (story 7).
- **Rockwell Automation RSLinx (ICSA-26-167-02)** — CISA Alerts. Covered in Rockwell batch post (story 7); CVE-2020-13573 is a 2020-vintage CVE.
- **Rockwell Automation FactoryTalk Analytics PavilionX (ICSA-26-167-01)** — CISA Alerts. Covered in the Rockwell ICS batch advisory post (story 7).
- **Rockwell Automation CompactLogix (ICSA-26-167-04)** — CISA Alerts. Covered in the Rockwell ICS batch advisory post (story 7).
- **ChatGPT's market share slips below 50% for first time** — TechCrunch AI. Market-share data point; no security or technical AI angle.
