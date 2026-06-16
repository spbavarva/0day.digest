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
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `apt`, `microsoft`, `vulnerability`
- **Slug:** `2026-06-16-sprysocks-windows-fishmonger-apt-kernel-driver.md`
- **Must-know:** no
- **Summary:** FishMonger, a China-nexus threat group, has ported the SprySOCKS backdoor to Windows and deployed it against government targets in Honduras, Taiwan, Thailand, and Pakistan. The new variant uses kernel driver abuse to evade endpoint detection — a notable escalation from the previously Linux-only implant.

### 2. Google Vertex AI SDK 'Pickle in the Middle' Flaw Allowed ML Model Hijacking via Bucket Squatting
- **Source:** The Hacker News — https://thehackernews.com/2026/06/google-vertex-ai-sdk-flaw-let-attackers.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `supply-chain`, `google`, `gcp`, `cloud-security`, `llm`
- **Slug:** `2026-06-16-google-vertex-ai-sdk-pickle-in-the-middle.md`
- **Must-know:** no
- **Summary:** Unit 42 found that an attacker with zero access to a victim's GCP project could squat the storage bucket Vertex AI uses for model uploads, causing the victim's ML model to land in attacker-controlled storage. Python pickle deserialization then enables arbitrary code execution inside Google's model-serving infrastructure; patched, no wild exploitation confirmed.

### 3. ClickFix Campaigns Deploy Three New Malware Loaders Targeting Education and Finance
- **Source:** The Hacker News — https://thehackernews.com/2026/06/clickfix-campaigns-expand-malware.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Slug:** `2026-06-16-clickfix-babadeda-lorem-ipsum-potemkin-loaders.md`
- **Must-know:** no
- **Summary:** Three independently documented ClickFix campaigns deliver new loaders: BabaDeda (education/finance, April 2026), Lorem Ipsum (compromised WordPress sites, linked to Vice Society), and Potemkin (fake update lures). The technique tricks users into running malicious clipboard commands via browser error dialogs.

### 4. GhostTree: Recursive NTFS Junctions Force Microsoft Defender Folder Scans to Never Complete
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/ghosttree-attack-abused-recursive-windows-junctions-to-hide-malware/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `vulnerability`, `microsoft`
- **Slug:** `2026-06-16-ghosttree-ntfs-junctions-defender-evasion.md`
- **Must-know:** no
- **Summary:** Varonis published GhostTree, a technique using recursive NTFS junctions to generate infinite valid Windows file paths that cause Microsoft Defender folder scans to loop indefinitely without completing. No elevated privileges required to create the junctions, leaving malware hidden inside the structure undetected.

### 5. Rokarolla Android Trojan Targets 217 Banking and Crypto Apps with Near-Total Device Control
- **Source:** The Hacker News — https://thehackernews.com/2026/06/new-rokarolla-android-malware-steals.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `data-breach`, `android`
- **Slug:** `2026-06-16-rokarolla-android-banking-trojan.md`
- **Must-know:** no
- **Summary:** Zimperium's zLabs documented Rokarolla, an Android banking trojan with 137 remote commands targeting 217 banking and crypto apps. Capabilities include PIN exfiltration, OTP interception via SMS, clipboard hijacking for crypto redirects, and disabling Google Play Protect; distributed as fake TikTok and Chrome installers.

### 6. FulcrumSec Claims 1.3 TB Stolen from Novo Nordisk in Hack-and-Leak Operation
- **Source:** SecurityWeek — https://www.securityweek.com/cybercrime-group-claims-novo-nordisk-hack/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `ransomware`
- **Slug:** `2026-06-16-novo-nordisk-hack-fulcrumsec-1tb.md`
- **Must-know:** no
- **Summary:** Hack-and-leak group FulcrumSec claims to have stolen 1.3 TB from pharmaceutical giant Novo Nordisk. The breach is unconfirmed; FulcrumSec operates via data-theft extortion rather than ransomware encryption, threatening public data dumps to pressure victims.

### 7. CISA Issues Five Rockwell Automation ICS Advisories, Including Critical CVSS 9.4 Auth Bypass
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-167-05
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `ics`
- **Slug:** `2026-06-16-rockwell-ics-cisa-advisories-cvss-94.md`
- **Must-know:** no
- **Summary:** CISA released five advisories for Rockwell Automation OT products on June 16, led by FLEX I/O EtherNet/IP Adapters (CVE-2026-0646/0647, CVSS 9.4) enabling unauthorized access and account takeover via missing authentication. Additional issues affect CompactLogix/ControlLogix 5370/5570 (DoS causing major nonrecoverable fault), RSLinx Classic, FactoryTalk Analytics PavilionX, and CompactLogix 5370 across critical manufacturing, energy, food/agriculture, and water sectors.

### 8. Threat Actors Abuse Steam Workshop to Distribute Malware via Wallpaper Engine Packages
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/steam-workshop-abused-to-spread-malware-via-wallpaper-engine-app/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `supply-chain`
- **Slug:** `2026-06-16-steam-workshop-malware-wallpaper-engine.md`
- **Must-know:** no
- **Summary:** Attackers are embedding malware in wallpaper packages on Steam Workshop for Wallpaper Engine, abusing the platform's trusted community distribution model to bypass endpoint security. Specific malware families dropped are not identified in this report.

### 9. UK to Mandate ID Upload or Facial Age Scan Before Social Media Account Creation
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/uk-to-require-id-or-face-scan-before-you-can-make-social-media-accounts/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `privacy`, `regulation`, `data-breach`
- **Slug:** `2026-06-16-uk-social-media-age-verification.md`
- **Must-know:** no
- **Summary:** The UK government will ban under-16s from social media by requiring ID or facial age verification before account creation, effective spring 2027. Security experts warn the checks are easily circumvented and that age-verification systems centralizing biometric data create significant new data-breach targets.

### 10. AWS Threat Tactic Spotlight: Detecting and Preventing Subdomain Takeover via Dangling DNS
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/threat-tactic-spotlight-subdomain-takeover/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `cloud-security`, `aws`
- **Slug:** `2026-06-16-subdomain-takeover-aws-dangling-dns.md`
- **Must-know:** no
- **Summary:** AWS published a practitioner guide on subdomain takeover via dangling DNS records, covering how attackers squat abandoned resources to serve phishing content or hijack OAuth flows. Covers Route 53 monitoring, S3/CloudFront audits, and AWS Config rules as detection and prevention controls.

## Skippable

- **New Rokarolla Android malware targets 217 banking, crypto apps** — BleepingComputer. Duplicate; The Hacker News (#29/story 5) has more complete technical detail.
- **Android 17 launches with new multitasking tools** — TechCrunch AI. Generic OS product launch; no security-specific angle beyond vague feature mentions.
- **Rokarolla Android Trojan Levels Up to Full Device Control** — Dark Reading. Duplicate of Rokarolla story; The Hacker News has the primary Zimperium sourcing.
- **Google named a Leader in IDC MarketScape SIEM 2026** — Google Cloud Security. Analyst ranking announcement; marketing content with no technical news value.
- **Apple 2027 rumors: AirPods with cameras for AI** — The Verge AI. Hardware product rumor; no security or AI-substance angle.
- **Qualcomm's latest chip hints at more powerful smart glasses** — The Verge AI. Hardware chip announcement; no security angle.
- **Sixty percent of US consumers say 'AI' in brand messaging is a turnoff** — TechCrunch AI. Consumer marketing survey; not technical, no security angle.
- **Quoting Georgi Gerganov** — Simon Willison. Commentary on using a local LLM for coding tasks; no security news value.
- **SpaceX is public: Everything you need to know post-IPO** — TechCrunch AI. Business/financial coverage; no AI or security angle.
- **India temporarily blocks Telegram over medical exam cheating fears** — The Record. Regional platform restriction for a non-security policy reason; no technical security detail.
- **'Lorem Ipsum' Malware Pivots to ClickFix Delivery** — Dark Reading. Duplicate; covered as part of the broader ClickFix loaders story (story 3).
- **iRhythm Confirms Data Stolen in Hack** — SecurityWeek. Thin summary with no TTPs, IOCs, or breach scope; skippable as generic breach disclosure without technical substance.
- **DOJ claims xAI's unpermitted gas turbines are a matter of national security** — TechCrunch AI. Environmental/energy regulatory story; no security angle.
- **Plaud says its software business topped $100M in ARR** — TechCrunch AI. Business milestone for an AI notetaker company; no security or technical AI news value.
- **Robinhood's note on 10% layoffs shows blaming AI isn't cutting it** — TechCrunch AI. Business/layoff news; no security or technical AI angle.
- **Hacker Conversations: Isira Adithya, the Evolution of an Ethical Hacker** — SecurityWeek. Profile/interview piece; no news value.
- **SpaceX passes Amazon as valuation balloons to $2.7T** — TechCrunch AI. Financial/business; duplicate SpaceX IPO coverage.
- **FTC warns of record $3.5 billion losses to imposter scams in 2025** — BleepingComputer. Aggregate statistics report; no IOCs, novel techniques, or actionable technical guidance.
- **Magnitude Emerges From Stealth Mode With $10 Million in Funding** — SecurityWeek. Startup funding announcement; marketing disguised as news.
- **AI and Cybersecurity – Everything You Wanted to Know, But Were Afraid to Ask** — SecurityWeek. Opinion survey roundup; no specific news event or technical disclosure.
- **Probably raises $9M to build a more reliable kind of AI** — TechCrunch AI. AI startup funding; no technical or security substance.
- **Endpoint Security Startup Ent Emerges From Stealth With $100 Million Seed Round** — SecurityWeek. Startup funding announcement; marketing content.
- **Can CISOs Trust Their Applications? TrustCloud Wants to Replace the Questionnaire** — SecurityWeek. Product marketing; no news value.
- **Rockwell Automation Logix 5370 & 5570 Controllers — CISA ICSA-26-167-03** — CISA Alerts. Covered in the Rockwell ICS batch advisory post (story 7).
- **Rockwell Automation RSLinx — CISA ICSA-26-167-02** — CISA Alerts. Covered in the Rockwell ICS batch advisory post (story 7); CVE-2020-13573 is a 2020-vintage CVE.
- **Rockwell Automation FactoryTalk Analytics PavilionX — CISA ICSA-26-167-01** — CISA Alerts. Covered in the Rockwell ICS batch advisory post (story 7).
- **Rockwell Automation CompactLogix — CISA ICSA-26-167-04** — CISA Alerts. Covered in the Rockwell ICS batch advisory post (story 7).
- **ChatGPT's market share slips below 50% for first time** — TechCrunch AI. Market-share data point; no security or technical AI angle.
