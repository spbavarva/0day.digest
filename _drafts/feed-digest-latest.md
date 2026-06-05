# Digest — 2026-06-05 AM

- Window: last 14h
- Raw items considered: 20
- Relevant: 9
- Skippable: 11

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Cisco SD-WAN Zero-Day CVE-2026-20245 Exploited in the Wild — No Patch Available — `2026-06-05-cisco-sd-wan-zero-day-cve-2026-20245.md`
- [x] **[CRITICAL]** Rust-Written IronWorm Malware Hits NPM in Credential-Propagating Supply Chain Attack — `2026-06-04-ironworm-npm-supply-chain-attack.md`
- [x] **[CRITICAL]** CVE-2026-3300: Everest Forms Pro WordPress Plugin RCE Actively Exploited — `2026-06-05-everest-forms-pro-rce-cve-2026-3300.md`
- [x] **[HIGH]** Five Eyes Warns: Chinese Intelligence Officers Pose as Recruiters to Target Government and Military Personnel — `2026-06-05-five-eyes-chinese-spy-fake-job-recruitment.md`
- [x] **[HIGH]** PCPJack Hijacks 230 AWS, GCP, and Azure Servers to Build Covert SMTP Relay Network — `2026-06-05-pcpjack-cloud-smtp-relay-hijack.md`
- [x] **[HIGH]** Magecart Campaign Abuses Stripe API to Host Skimmer Payload and Exfiltrate Stolen Cards — `2026-06-04-magecart-stripe-api-credit-card-theft.md`
- [x] **[HIGH]** Hola Browser for Windows Compromised in Supply Chain Attack Delivering Cryptominer — `2026-06-04-hola-browser-supply-chain-cryptominer.md`
- [x] **[MEDIUM]** FIFA World Cup 2026 Scam Wave: Thousands of Fake Domains, Banking Malware in Pirate Streams — `2026-06-05-fifa-world-cup-2026-scams-banking-malware.md`
- [x] **[INFORMATIONAL]** Anthropic Crosses $47B Annualized Revenue in May as IPO Track Continues — `2026-06-04-anthropic-47b-arr-ipo-trajectory.md`

## Relevant (details)

### 1. Cisco SD-WAN Zero-Day CVE-2026-20245 Exploited in the Wild — No Patch Available
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-cisco-sd-wan-flaw-exploited-in-zero-day-attacks-to-gain-root/
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `rce`, `privilege-escalation`, `vulnerability`
- **Summary:** CVE-2026-20245 in Cisco Catalyst SD-WAN Manager is being actively exploited to achieve root-level command execution — the seventh SD-WAN zero-day in 2026 — with no patch yet available. Isolate management interfaces and monitor for anomalous command execution.

### 2. Rust-Written IronWorm Malware Hits NPM in Credential-Propagating Supply Chain Attack
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/rust-written-ironworm-npm-supply-chain
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`, `credential-theft`
- **Summary:** IronWorm steals npm developer credentials and reuses them to publish trojanized packages that propagate the infection downstream. Rotate npm tokens and audit recent package publishes.

### 3. CVE-2026-3300: Everest Forms Pro WordPress Plugin RCE Actively Exploited
- **Source:** The Hacker News — https://thehackernews.com/2026/06/hackers-exploit-critical-everest-forms.html
- **Severity:** critical
- **Tags:** `cve`, `rce`, `vulnerability`
- **Summary:** CVSS 9.8 RCE in Everest Forms Pro (≤ 1.9.12) is under active exploitation leading to full site compromise. A patch is available; update immediately.

### 4. Five Eyes Warns: Chinese Intelligence Officers Pose as Recruiters to Target Government and Military Personnel
- **Source:** SecurityWeek — https://www.securityweek.com/five-eyes-chinese-spies-target-government-military-staff-with-fake-job-opportunities/
- **Severity:** high
- **Tags:** `phishing`, `social-engineering`, `espionage`
- **Summary:** Chinese intelligence officers are using fake recruiter identities on professional networks to target cleared and privileged personnel. Five Eyes advisory urges training on unsolicited recruitment contacts.

### 5. PCPJack Hijacks 230 AWS, GCP, and Azure Servers to Build Covert SMTP Relay Network
- **Source:** The Hacker News — https://thehackernews.com/2026/06/pcpjack-hijacks-230-aws-google-cloud.html
- **Severity:** high
- **Tags:** `cloud-security`, `aws`, `gcp`, `azure`, `malware`
- **Summary:** PCPJack converted 230 compromised business cloud servers into a synchronized SMTP proxy network for spam/phishing campaigns routed through legitimate infrastructure. Audit outbound SMTP egress and IAM for unauthorized resources.

### 6. Magecart Campaign Abuses Stripe API to Host Skimmer Payload and Exfiltrate Stolen Cards
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/credit-card-theft-campaign-abuses-stripe-to-host-stolen-payment-info/
- **Severity:** high
- **Tags:** `malware`, `appsec`, `data-breach`
- **Summary:** A novel Magecart campaign routes both its card-skimming payload and stolen card exfiltration through Stripe's API, evading network-layer detection. Enforce SRI on checkout scripts and monitor for unauthorized Stripe API key activity.

### 7. Hola Browser for Windows Compromised in Supply Chain Attack Delivering Cryptominer
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hola-browser-for-windows-compromised-to-deliver-cryptominer/
- **Severity:** high
- **Tags:** `supply-chain`, `malware`
- **Summary:** Hola Browser's Windows installer was compromised to bundle a cryptominer. Affected users should remove the software and scan for mining processes.

### 8. FIFA World Cup 2026 Scam Wave: Thousands of Fake Domains, Banking Malware in Pirate Streams
- **Source:** The Hacker News — https://thehackernews.com/2026/06/fifa-world-cup-2026-scams-are-already.html
- **Severity:** medium
- **Tags:** `phishing`, `malware`, `data-breach`
- **Summary:** Ahead of the June 11 kickoff, the FBI and researchers warn of thousands of lookalike FIFA domains, banking malware in pirate streaming apps, and credential-harvesting login clones. Use only official FIFA channels.

### 9. Anthropic Crosses $47B Annualized Revenue in May as IPO Track Continues
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/04/ahead-of-its-ipo-anthropics-daniela-amodei-shrugs-off-doubts-about-ais-returns/
- **Severity:** informational
- **Tags:** `anthropic`, `llm`
- **Summary:** Anthropic's annualized revenue hit $47B in May 2026 (up from ~$9B end of 2025), with Daniela Amodei deflecting ROI skepticism ahead of a likely IPO; enterprise API adoption cited as primary growth driver.

## Skippable

- **Industry Reactions to New Trump AI Cybersecurity Executive Order: Feedback Friday** — SecurityWeek. Editorial reactions roundup; the EO itself is the news, not this commentary.
- **Nightclub Giant RCI Says Data Breach Affects 40,000 Individuals** — SecurityWeek. Breach below 100k threshold with no technical substance.
- **Cisco Warns of 7th SD-WAN Zero-Day Exploited in 2026** — SecurityWeek. Duplicate of CVE-2026-20245 (item 1); BleepingComputer has more detail.
- **Mira Murati steps back into the spotlight, carefully** — TechCrunch AI. Profile piece; no model launch or security angle.
- **AI enthusiasts are in a race against time, AI skeptics are in a race against entropy** — Simon Willison. Opinion piece; no news value.
- **Airbnb's Brian Chesky plans to launch a new AI lab** — TechCrunch AI. Business story; no model launch or security relevance.
- **Amazon Cognito unlocks advanced capabilities with next-generation infrastructure** — AWS Security Blog. AWS marketing post on infrastructure upgrades; no novel security finding.
- **Brave Software releases Origin for a paid, bloat-free browsing experience** — BleepingComputer. Product launch; no security angle.
- **Defense tech, AI, and fundraising take center stage at StrictlyVC Los Angeles on June 18** — TechCrunch AI. Event promotion.
- **China's TA4922 Expands Cybercrime Attacks Globally** — Dark Reading. Summary too thin; no IOCs or TTPs disclosed.
- **4 Critical Threats Where Attackers Have the Advantage** — Dark Reading. Gartner analyst roundup; no new IOCs or technical guidance.
