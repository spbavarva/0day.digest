# Digest — 2026-04-28 AM

- Window: last 14h
- Raw items considered: 20
- Relevant: 11
- Skippable: 9

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** GlassWorm Returns: 73 Sleeper Extensions Planted in OpenVSX Registry — `2026-04-27-glassworm-73-openvsx-sleeper-extensions.md`
- [x] **[CRITICAL]** Medtronic Breach Confirmed: ShinyHunters Claims 9 Million Records Stolen — `2026-04-28-medtronic-breach-shinyhunters-9m-records.md`
- [x] **[HIGH]** Microsoft Patches Entra ID AI Agent Role That Enabled Service Principal Takeover — `2026-04-28-microsoft-entra-id-ai-agent-role-privilege-escalation.md`
- [x] **[HIGH]** CVE-2026-32202: Windows Shell Spoofing Vulnerability Confirmed Under Active Exploitation — `2026-04-28-cve-2026-32202-windows-shell-actively-exploited.md`
- [x] **[HIGH]** UNC6692 Threat Actor Combines Microsoft Teams Lures, AWS S3 C2, and Custom Snow Malware — `2026-04-27-unc6692-teams-aws-snow-malware.md`
- [x] **[MEDIUM]** Silk Typhoon Member Extradited to U.S. for Cyberespionage Against COVID Research Targets — `2026-04-28-silk-typhoon-hacker-extradited-us.md`
- [x] **[MEDIUM]** Robinhood Account Creation Flaw Exploited to Send Phishing via Legitimate Email Infrastructure — `2026-04-27-robinhood-phishing-email-injection.md`
- [x] **[MEDIUM]** Canada Arrests Three for Running SMS Blaster That Injected Phishing Texts at Radio Layer — `2026-04-27-canada-sms-blaster-phishing-arrests.md`
- [x] **[INFORMATIONAL]** Supreme Court Signals Geofencing Location Searches Should Require a Warrant — `2026-04-27-supreme-court-geofencing-warrant-ruling.md`
- [x] **[INFORMATIONAL]** Microsoft VibeVoice: MIT-Licensed Speech-to-Text Model with Built-In Speaker Diarization — `2026-04-27-microsoft-vibevoice-speech-to-text-model.md`
- [x] **[INFORMATIONAL]** talkie-1930: Alec Radford Releases 13B Language Model Trained on Pre-1931 English Text — `2026-04-28-talkie-1930-vintage-language-model.md`

## Relevant (details)

### 1. GlassWorm Returns: 73 Sleeper Extensions Planted in OpenVSX Registry
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/glassworm-malware-attacks-return-via-73-openvsx-sleeper-extensions/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`
- **Slug:** `2026-04-27-glassworm-73-openvsx-sleeper-extensions`
- **Must-know:** yes
- **Summary:** A new GlassWorm wave placed 73 "sleeper" extensions in OpenVSX — the open-source VS Code extension registry used by VSCodium, Eclipse Che, and Gitpod. Extensions appear legitimate at install time and activate malware after a subsequent update, which means standard install-time scanning is insufficient.

### 2. Medtronic Breach Confirmed: ShinyHunters Claims 9 Million Records Stolen
- **Source:** SecurityWeek — https://www.securityweek.com/medtronic-hack-confirmed-after-shinyhunters-threatens-data-leak/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `data-breach`
- **Slug:** `2026-04-28-medtronic-breach-shinyhunters-9m-records`
- **Must-know:** yes
- **Summary:** ShinyHunters claims to have stolen 9 million personal records from Medtronic and is threatening a public data dump. Medtronic has confirmed the breach, making this a significant healthcare data exposure event with downstream phishing and identity fraud risk for affected individuals.

### 3. Microsoft Patches Entra ID AI Agent Role That Enabled Service Principal Takeover
- **Source:** The Hacker News — https://thehackernews.com/2026/04/microsoft-patches-entra-id-role-flaw.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `privilege-escalation`, `iam`, `microsoft`, `vulnerability`
- **Slug:** `2026-04-28-microsoft-entra-id-ai-agent-role-privilege-escalation`
- **Must-know:** no
- **Summary:** The "Agent ID Administrator" Entra ID role — introduced for managing AI agent identities — grants over-broad permissions that Silverfort researchers found could be used to escalate privileges and take over existing service principals. Microsoft has patched the issue; organizations should audit role assignments.

### 4. CVE-2026-32202: Windows Shell Spoofing Vulnerability Confirmed Under Active Exploitation
- **Source:** The Hacker News — https://thehackernews.com/2026/04/microsoft-confirms-active-exploitation.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `cve`, `microsoft`
- **Slug:** `2026-04-28-cve-2026-32202-windows-shell-actively-exploited`
- **Must-know:** no
- **Summary:** Microsoft revised its advisory for CVE-2026-32202 (Windows Shell spoofing, CVSS 4.3) to confirm active in-the-wild exploitation. The flaw enables access to sensitive information. It was included in the April 2026 Patch Tuesday; endpoints not yet updated should be prioritized.

### 5. UNC6692 Threat Actor Combines Microsoft Teams Lures, AWS S3 C2, and Custom Snow Malware
- **Source:** Dark Reading — https://www.darkreading.com/cloud-security/unc6692-social-engineering-malware-cloud-abuse
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `cloud-security`, `microsoft`, `aws`
- **Slug:** `2026-04-27-unc6692-teams-aws-snow-malware`
- **Must-know:** no
- **Summary:** Newly identified threat actor UNC6692 uses Teams-based social engineering to deliver a custom implant ("Snow") and routes C2 traffic through AWS S3 buckets to blend with legitimate cloud traffic. Traditional network controls are ineffective against cloud-native C2; behavioral detections and Teams external access restrictions are the primary mitigations.

### 6. Silk Typhoon Member Extradited to U.S. for Cyberespionage Against COVID Research Targets
- **Source:** The Hacker News — https://thehackernews.com/2026/04/chinese-silk-typhoon-hacker-extradited.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `apt`, `microsoft`
- **Slug:** `2026-04-28-silk-typhoon-hacker-extradited-us`
- **Must-know:** no
- **Summary:** Chinese national Xu Zewei was extradited from Italy to face U.S. charges for alleged Silk Typhoon (Hafnium) operations against American organizations between 2020–2021, including COVID-19 research targets. It is a rare enforcement milestone against an alleged Chinese state-sponsored operator.

### 7. Robinhood Account Creation Flaw Exploited to Send Phishing via Legitimate Email Infrastructure
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/robinhood-account-creation-flaw-abused-to-send-phishing-emails/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`
- **Slug:** `2026-04-27-robinhood-phishing-email-injection`
- **Must-know:** no
- **Summary:** A flaw in Robinhood's account creation process allowed attackers to inject phishing content into legitimate Robinhood emails, which passed SPF/DKIM/DMARC authentication because they originated from Robinhood's own mail infrastructure. Users cannot rely on email security controls to filter these messages.

### 8. Canada Arrests Three for Running SMS Blaster That Injected Phishing Texts at Radio Layer
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/canada-arrests-three-for-operating-sms-blaster-device-in-toronto/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`
- **Slug:** `2026-04-27-canada-sms-blaster-phishing-arrests`
- **Must-know:** no
- **Summary:** Three individuals in Toronto were arrested for operating a physical IMSI catcher that broadcast phishing SMS messages directly to nearby phones at the radio layer, bypassing all carrier filtering. The technique is undetectable by recipients and cannot be blocked by standard SMS security controls.

### 9. Supreme Court Signals Geofencing Location Searches Should Require a Warrant
- **Source:** The Record (Recorded Future) — https://therecord.media/supreme-court-signals-location-data-searches-require-warrant
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `privacy`
- **Slug:** `2026-04-27-supreme-court-geofencing-warrant-ruling`
- **Must-know:** no
- **Summary:** Supreme Court justices signaled during oral arguments that geofence reverse-location searches should require a warrant, suggesting the court may extend Fourth Amendment protections to this widely used investigative tool. A formal ruling is expected before the term ends and will affect how law enforcement and data custodians handle reverse search requests.

### 10. Microsoft VibeVoice: MIT-Licensed Speech-to-Text Model with Built-In Speaker Diarization
- **Source:** Simon Willison — https://simonwillison.net/2026/Apr/27/vibevoice/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `model-release`, `microsoft`
- **Slug:** `2026-04-27-microsoft-vibevoice-speech-to-text-model`
- **Must-know:** no
- **Summary:** Microsoft's VibeVoice (released January 2026, MIT licensed) is a Whisper-style ASR model with speaker diarization built into the model rather than as a post-processing step. Available in a quantized MLX version suitable for local deployment on Apple Silicon, it eliminates data-egress concerns of cloud transcription APIs.

### 11. talkie-1930: Alec Radford Releases 13B Language Model Trained on Pre-1931 English Text
- **Source:** Simon Willison — https://simonwillison.net/2026/Apr/28/talkie/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `model-release`, `llm`
- **Slug:** `2026-04-28-talkie-1930-vintage-language-model`
- **Must-know:** no
- **Summary:** Alec Radford (GPT, GPT-2, Whisper) and collaborators released a 13B model trained on 260B tokens of pre-1931 out-of-copyright English text under Apache 2.0. Both a base and instruction-tuned checkpoint are available, with unusually clean IP provenance due to the out-of-copyright training corpus.

## Skippable

- **Microsoft asks iPhone users to reauthenticate after Outlook outage** — BleepingComputer. Operational availability incident, not a security vulnerability; reauthentication is a routine recovery step post-outage.
- **Spectrum Security Emerges From Stealth Mode With $19 Million** — SecurityWeek. Vendor funding announcement with no technical or threat-intel content.
- **What's new in pip 26.1 - lockfiles and dependency cooldowns!** — Simon Willison. Developer tooling release note; supply chain benefit is indirect and no security finding is reported.
- **Jury selection in Musk v. Altman: 'People don't like him'** — The Verge AI. Legal proceedings coverage with no AI technical or security content.
- **Adaptive Ultrasound Imaging with Physics-Informed NV-Raw2Insights-US AI** — Hugging Face Blog. Medical imaging AI, out of scope for AI/security intersection.
- **Google is testing AI chatbot search for YouTube** — The Verge AI. Product feature experiment, no model launch or security angle.
- **Canonical lays out a plan for AI in Ubuntu Linux** — The Verge AI. Product roadmap announcement with no new capability release or security finding.
- **Tennessee becomes second state to ban cryptocurrency ATMs over scam concerns** — The Record. State-level regulatory action, not technically actionable for practitioners.
- **Alleged Silk Typhoon hacker extradited to US for cyberespionage** — BleepingComputer. Duplicate coverage of item 6 (The Hacker News selected as primary source).
