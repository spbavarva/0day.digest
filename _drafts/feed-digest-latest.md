# Digest — 2026-06-01 PM

- Window: last 14h
- Raw items considered: 15
- Relevant: 10
- Skippable: 5

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** OpenAI Codex Auth Tokens Stolen via codexui-android npm Supply Chain Attack — `2026-06-01-openai-codex-npm-supply-chain-token-theft.md`
- [x] **[CRITICAL]** Palo Alto PAN-OS CVE-2026-0257 Authentication Bypass Exploited for Weeks — `2026-06-01-paloalto-pan-os-cve-2026-0257-auth-bypass-exploited.md`
- [x] **[HIGH]** 19-Year-Old Linux Kernel CIFSwitch Flaw Gets Public PoC, Allows Root Escalation — `2026-06-01-linux-kernel-cifsswitch-19-year-root-escalation.md`
- [x] **[HIGH]** Critical WP Maps Pro Flaw Actively Exploited to Create Rogue Admin Accounts — `2026-06-01-wp-maps-pro-critical-flaw-admin-account-creation.md`
- [x] **[MEDIUM]** Microsoft Outage Disrupts MFA Setup and My Sign-Ins Platform — `2026-06-01-microsoft-mfa-outage-sign-ins.md`
- [x] **[MEDIUM]** Unknown Threat Actor Targeted Russian Maritime Universities and Diplomats for Two Years — `2026-05-31-unknown-apt-russia-maritime-universities-espionage.md`
- [x] **[INFORMATIONAL]** Kaspersky GReAT Maps Container Attack Vectors: Escapes, Misconfigs, and Supply Chain — `2026-06-01-kaspersky-container-attack-vectors-research.md`
- [x] **[INFORMATIONAL]** NVIDIA Launches Cosmos 3: Open Omni-Model for Physical AI and Robotics — `2026-06-01-nvidia-cosmos-3-physical-ai-model-launch.md`
- [x] **[INFORMATIONAL]** Microsoft Pledges Not to Pursue Security Researchers After Zero-Day Backlash — `2026-06-01-microsoft-security-researcher-policy.md`
- [x] **[INFORMATIONAL]** Pentagon Pushes Battlefield AI While Military Leaders Urge Caution — `2026-06-01-pentagon-battlefield-ai-military-caution.md`

## Relevant (details)

### 1. OpenAI Codex Auth Tokens Stolen via codexui-android npm Supply Chain Attack
- **Source:** The Hacker News — https://thehackernews.com/2026/06/openai-codex-authentication-tokens.html
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `openai`, `malware`
- **Summary:** Malicious npm package codexui-android (29k+ weekly downloads) steals OpenAI Codex auth tokens from developers. Package still live on npm — rotate API keys immediately if installed.

### 2. Palo Alto PAN-OS CVE-2026-0257 Authentication Bypass Exploited for Weeks
- **Source:** SecurityWeek — https://www.securityweek.com/recent-palo-alto-networks-vulnerability-exploited-for-weeks/
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`
- **Summary:** Auth bypass in PAN-OS exploited in the wild just four days after disclosure, ongoing for weeks. Patch immediately and restrict management interface access.

### 3. 19-Year-Old Linux Kernel CIFSwitch Flaw Gets Public PoC, Allows Root Escalation
- **Source:** SecurityWeek — https://www.securityweek.com/19-year-old-linux-kernel-vulnerability-exposes-systems-to-root-access/
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`, `cve`
- **Summary:** Public PoC now available for CIFSwitch kernel flaw enabling local-to-root escalation across a broad range of kernel versions. Apply distribution patches promptly.

### 4. Critical WP Maps Pro Flaw Actively Exploited to Create Rogue Admin Accounts
- **Source:** The Hacker News — https://thehackernews.com/2026/06/critical-wp-maps-pro-flaw-actively.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`, `privilege-escalation`
- **Summary:** Active exploitation of WP Maps Pro (15k+ installs) creates unauthorized WordPress admin accounts. Disable plugin and audit user table now.

### 5. Microsoft Outage Disrupts MFA Setup and My Sign-Ins Platform
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-outage-affecting-mfa-my-sign-ins-platform/
- **Severity:** medium
- **Tags:** `microsoft`, `iam`, `azure`
- **Summary:** Service outage blocks MFA enrollment and My Sign-Ins access. No breach — defer provisioning and monitor M365 Service Health Dashboard.

### 6. Unknown Threat Actor Targeted Russian Maritime Universities and Diplomats for Two Years
- **Source:** The Record (Recorded Future) — https://therecord.media/unknown-hacking-group-targeting-russia-for-nearly-two-years
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** Two-year espionage campaign against Russian maritime schools and diplomats by an unattributed actor. Majority of targets are maritime educational institutions; TTPs not publicly disclosed.

### 7. Kaspersky GReAT Maps Container Attack Vectors: Escapes, Misconfigs, and Supply Chain
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/container-attack-vectors/120010/
- **Severity:** informational
- **Tags:** `container-security`, `supply-chain`, `cloud-security`, `kubernetes`
- **Summary:** GReAT published a structured taxonomy of container attack vectors — secrets exposure, privilege misconfigs, API compromise, supply chain. Good practitioner audit reference.

### 8. NVIDIA Launches Cosmos 3: Open Omni-Model for Physical AI and Robotics
- **Source:** Hugging Face Blog — https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai
- **Severity:** informational
- **Tags:** `model-release`, `ai-launch`
- **Summary:** NVIDIA released Cosmos 3 on Hugging Face — open omni-model targeting physical AI and robotics reasoning. Limited technical detail in feed.

### 9. Microsoft Pledges Not to Pursue Security Researchers After Zero-Day Backlash
- **Source:** The Record (Recorded Future) — https://therecord.media/microsoft-says-it-will-not-pursue-security-researchers-disclosure
- **Severity:** informational
- **Tags:** `microsoft`, `vulnerability`
- **Summary:** Microsoft publicly committed to not pursuing legal action against security researchers following backlash over an apparent threat tied to a zero-day disclosure.

### 10. Pentagon Pushes Battlefield AI While Military Leaders Urge Caution
- **Source:** SecurityWeek — https://www.securityweek.com/as-the-pentagon-pushes-for-battlefield-ai-some-military-leaders-urge-caution/
- **Severity:** informational
- **Tags:** `ai-safety`
- **Summary:** Pentagon accelerates battlefield AI deployment as a strategic advantage; some military leaders warn about autonomous systems in lethal environments without adequate oversight.

## Skippable

- **Webinar tomorrow: From alert to resolution in network incident response** — BleepingComputer. Webinar promotion / marketing content, no news value.
- **The Security Growth Platform: Why MSPs Are Moving Beyond vCISO Tools** — The Hacker News. Marketing piece for MSP software platform, no technical news.
- **Microsoft fixes KB5089549 Windows security update install issues** — BleepingComputer. Routine patch installation fix, no security exploit or CVE of note.
- **May 2026 newsletter** — Simon Willison. Sponsor-only newsletter paywall announcement, not public news content.
- **datasette 1.0a32** — Simon Willison. Minor bugfix release of a developer tool, no security or AI significance.
