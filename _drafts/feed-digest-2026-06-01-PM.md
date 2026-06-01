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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `openai`, `malware`
- **Slug:** `2026-06-01-openai-codex-npm-supply-chain-token-theft`
- **Must-know:** yes
- **Summary:** A malicious npm package named codexui-android, posing as a remote web UI for OpenAI Codex, is stealing authentication tokens from developers with 29,000+ weekly downloads. The package remains on npm at time of reporting — developers who installed it should rotate API keys immediately.

### 2. Palo Alto PAN-OS CVE-2026-0257 Authentication Bypass Exploited for Weeks
- **Source:** SecurityWeek — https://www.securityweek.com/recent-palo-alto-networks-vulnerability-exploited-for-weeks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`
- **Slug:** `2026-06-01-paloalto-pan-os-cve-2026-0257-auth-bypass-exploited`
- **Must-know:** no
- **Summary:** CVE-2026-0257 is an authentication bypass in PAN-OS that attackers began exploiting just four days after public disclosure, and exploitation has continued for weeks. PAN-OS customers should patch immediately and restrict management interface access to trusted IPs.

### 3. 19-Year-Old Linux Kernel CIFSwitch Flaw Gets Public PoC, Allows Root Escalation
- **Source:** SecurityWeek — https://www.securityweek.com/19-year-old-linux-kernel-vulnerability-exposes-systems-to-root-access/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`, `cve`
- **Slug:** `2026-06-01-linux-kernel-cifsswitch-19-year-root-escalation`
- **Must-know:** no
- **Summary:** A 19-year-old Linux kernel vulnerability in the CIFSwitch component now has public PoC code enabling local users to escalate to root. The age of the flaw means wide kernel version coverage — administrators should patch from distribution advisories.

### 4. Critical WP Maps Pro Flaw Actively Exploited to Create Rogue Admin Accounts
- **Source:** The Hacker News — https://thehackernews.com/2026/06/critical-wp-maps-pro-flaw-actively.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`, `privilege-escalation`
- **Slug:** `2026-06-01-wp-maps-pro-critical-flaw-admin-account-creation`
- **Must-know:** no
- **Summary:** A critical flaw in WP Maps Pro (15,000+ sales) is being actively exploited to create unauthorized WordPress admin accounts. Site owners should disable the plugin and audit for rogue admin users immediately.

### 5. Microsoft Outage Disrupts MFA Setup and My Sign-Ins Platform
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-outage-affecting-mfa-my-sign-ins-platform/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `microsoft`, `iam`, `azure`
- **Slug:** `2026-06-01-microsoft-mfa-outage-sign-ins`
- **Must-know:** no
- **Summary:** Microsoft confirmed a service outage blocking MFA enrollment and My Sign-Ins access. No breach reported — administrators should defer MFA provisioning and monitor the M365 Service Health Dashboard.

### 6. Unknown Threat Actor Targeted Russian Maritime Universities and Diplomats for Two Years
- **Source:** The Record (Recorded Future) — https://therecord.media/unknown-hacking-group-targeting-russia-for-nearly-two-years
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `2026-05-31-unknown-apt-russia-maritime-universities-espionage`
- **Must-know:** no
- **Summary:** An unattributed actor ran a two-year espionage campaign targeting Russian maritime universities, shipping/fishing training schools, and diplomats. Over half of attacks hit maritime educational institutions; full TTPs were not disclosed.

### 7. Kaspersky GReAT Maps Container Attack Vectors: Escapes, Misconfigs, and Supply Chain
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/container-attack-vectors/120010/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `container-security`, `supply-chain`, `cloud-security`, `kubernetes`
- **Slug:** `2026-06-01-kaspersky-container-attack-vectors-research`
- **Must-know:** no
- **Summary:** GReAT published a structured taxonomy of container attack vectors: exposed secrets, privilege misconfigurations, API compromise, and supply chain attacks. Useful practitioner reference for auditing container security posture end-to-end.

### 8. NVIDIA Launches Cosmos 3: Open Omni-Model for Physical AI and Robotics
- **Source:** Hugging Face Blog — https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `model-release`, `ai-launch`
- **Slug:** `2026-06-01-nvidia-cosmos-3-physical-ai-model-launch`
- **Must-know:** no
- **Summary:** NVIDIA released Cosmos 3 on Hugging Face, described as the first open omni-model for physical AI reasoning and action, targeting robotics applications. Limited technical details available from feed summary.

### 9. Microsoft Pledges Not to Pursue Security Researchers After Zero-Day Backlash
- **Source:** The Record (Recorded Future) — https://therecord.media/microsoft-says-it-will-not-pursue-security-researchers-disclosure
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `microsoft`, `vulnerability`
- **Slug:** `2026-06-01-microsoft-security-researcher-policy`
- **Must-know:** no
- **Summary:** Microsoft issued a public statement that it will not pursue legal action against security researchers for conducting or publishing research, following backlash over an apparent threat tied to a zero-day disclosure. The specific incident was not detailed in available reporting.

### 10. Pentagon Pushes Battlefield AI While Military Leaders Urge Caution
- **Source:** SecurityWeek — https://www.securityweek.com/as-the-pentagon-pushes-for-battlefield-ai-some-military-leaders-urge-caution/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ai-safety`
- **Slug:** `2026-06-01-pentagon-battlefield-ai-military-caution`
- **Must-know:** no
- **Summary:** The Pentagon is accelerating battlefield AI deployment as a strategic advantage while some military leaders publicly urge caution about autonomous systems in lethal environments. Mirrors civilian AI safety debates but with irreversible stakes.

## Skippable

- **Webinar tomorrow: From alert to resolution in network incident response** — BleepingComputer. Webinar promotion / marketing content, no news value.
- **The Security Growth Platform: Why MSPs Are Moving Beyond vCISO Tools** — The Hacker News. Marketing piece for MSP software platform, no technical news.
- **Microsoft fixes KB5089549 Windows security update install issues** — BleepingComputer. Routine patch installation fix, no security exploit or CVE of note.
- **May 2026 newsletter** — Simon Willison. Sponsor-only newsletter paywall announcement, not public news content.
- **datasette 1.0a32** — Simon Willison. Minor bugfix release of a developer tool, no security or AI significance.
