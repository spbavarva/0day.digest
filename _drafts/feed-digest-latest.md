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
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`
- **Summary:** A new GlassWorm wave planted 73 sleeper extensions in OpenVSX — the registry backing VSCodium, Eclipse Che, and Gitpod. Extensions become malicious post-install via update, bypassing install-time scanning.

### 2. Medtronic Breach Confirmed: ShinyHunters Claims 9 Million Records Stolen
- **Source:** SecurityWeek — https://www.securityweek.com/medtronic-hack-confirmed-after-shinyhunters-threatens-data-leak/
- **Severity:** critical
- **Tags:** `data-breach`
- **Summary:** ShinyHunters claims 9 million personal records from Medtronic and threatens public release. Medtronic confirmed the breach; downstream phishing and identity fraud risk is elevated for affected individuals.

### 3. Microsoft Patches Entra ID AI Agent Role That Enabled Service Principal Takeover
- **Source:** The Hacker News — https://thehackernews.com/2026/04/microsoft-patches-entra-id-role-flaw.html
- **Severity:** high
- **Tags:** `privilege-escalation`, `iam`, `microsoft`, `vulnerability`
- **Summary:** Silverfort found the "Agent ID Administrator" Entra ID role grants over-broad permissions enabling privilege escalation to service principal takeover. Microsoft has patched it; organizations should audit role assignments.

### 4. CVE-2026-32202: Windows Shell Spoofing Vulnerability Confirmed Under Active Exploitation
- **Source:** The Hacker News — https://thehackernews.com/2026/04/microsoft-confirms-active-exploitation.html
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `cve`, `microsoft`
- **Summary:** Microsoft updated its advisory for CVE-2026-32202 (CVSS 4.3) to confirm active exploitation. Patched in April 2026 Patch Tuesday; endpoints not yet updated should be prioritized.

### 5. UNC6692 Threat Actor Combines Microsoft Teams Lures, AWS S3 C2, and Custom Snow Malware
- **Source:** Dark Reading — https://www.darkreading.com/cloud-security/unc6692-social-engineering-malware-cloud-abuse
- **Severity:** high
- **Tags:** `malware`, `cloud-security`, `microsoft`, `aws`
- **Summary:** UNC6692 uses Teams social engineering to deploy the Snow implant with AWS S3-based C2. Cloud-native infrastructure makes traditional network controls ineffective; behavioral detection and Teams external access restrictions are the primary mitigations.

### 6. Silk Typhoon Member Extradited to U.S. for Cyberespionage Against COVID Research Targets
- **Source:** The Hacker News — https://thehackernews.com/2026/04/chinese-silk-typhoon-hacker-extradited.html
- **Severity:** medium
- **Tags:** `apt`, `microsoft`
- **Summary:** Xu Zewei extradited from Italy to face charges for alleged Silk Typhoon operations against U.S. organizations in 2020–2021. A rare enforcement outcome against an alleged Chinese state-sponsored actor.

### 7. Robinhood Account Creation Flaw Exploited to Send Phishing via Legitimate Email Infrastructure
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/robinhood-account-creation-flaw-abused-to-send-phishing-emails/
- **Severity:** medium
- **Tags:** `phishing`
- **Summary:** Attackers injected phishing content into real Robinhood transactional emails via an account creation flaw, passing SPF/DKIM/DMARC because messages originated from Robinhood servers. Email authentication controls cannot block this class of attack.

### 8. Canada Arrests Three for Running SMS Blaster That Injected Phishing Texts at Radio Layer
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/canada-arrests-three-for-operating-sms-blaster-device-in-toronto/
- **Severity:** medium
- **Tags:** `phishing`
- **Summary:** Three arrested in Toronto for operating an IMSI catcher that pushed phishing SMS at the RF layer, bypassing all carrier filtering. Messages are indistinguishable from legitimate SMS by recipients.

### 9. Supreme Court Signals Geofencing Location Searches Should Require a Warrant
- **Source:** The Record (Recorded Future) — https://therecord.media/supreme-court-signals-location-data-searches-require-warrant
- **Severity:** informational
- **Tags:** `privacy`
- **Summary:** Oral argument signals suggest SCOTUS may extend Fourth Amendment warrant requirements to geofence reverse-location searches. A ruling before term end would affect law enforcement workflows and data custodian compliance obligations.

### 10. Microsoft VibeVoice: MIT-Licensed Speech-to-Text Model with Built-In Speaker Diarization
- **Source:** Simon Willison — https://simonwillison.net/2026/Apr/27/vibevoice/#atom-everything
- **Severity:** informational
- **Tags:** `model-release`, `microsoft`
- **Summary:** Microsoft's VibeVoice (MIT, Jan 2026) is a Whisper-style ASR model with integrated speaker diarization, available in a quantized MLX variant for local Apple Silicon deployment. Eliminates cloud data-egress risk for sensitive transcription workflows.

### 11. talkie-1930: Alec Radford Releases 13B Language Model Trained on Pre-1931 English Text
- **Source:** Simon Willison — https://simonwillison.net/2026/Apr/28/talkie/#atom-everything
- **Severity:** informational
- **Tags:** `model-release`, `llm`
- **Summary:** Alec Radford et al. released a 13B model on 260B tokens of pre-1931 out-of-copyright text under Apache 2.0. Both base and instruction-tuned variants available; unusually clean IP provenance.

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
