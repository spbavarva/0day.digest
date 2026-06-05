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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `rce`, `privilege-escalation`, `vulnerability`
- **Slug:** `2026-06-05-cisco-sd-wan-zero-day-cve-2026-20245`
- **Must-know:** yes
- **Summary:** CVE-2026-20245 in Cisco Catalyst SD-WAN Manager is being actively exploited to achieve root-level command execution with no patch currently available — the seventh Cisco SD-WAN zero-day in 2026. Organizations should isolate SD-WAN management interfaces and monitor for anomalous activity while awaiting a fix.

### 2. Rust-Written IronWorm Malware Hits NPM in Credential-Propagating Supply Chain Attack
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/rust-written-ironworm-npm-supply-chain
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`, `credential-theft`
- **Slug:** `2026-06-04-ironworm-npm-supply-chain-attack`
- **Must-know:** yes
- **Summary:** IronWorm steals npm developer credentials and reuses them to publish trojanized packages that spread the infection further downstream, mirroring the TeamPCP Shai-Hulud technique. Affected developers should rotate npm tokens and audit recently published packages.

### 3. CVE-2026-3300: Everest Forms Pro WordPress Plugin RCE Actively Exploited
- **Source:** The Hacker News — https://thehackernews.com/2026/06/hackers-exploit-critical-everest-forms.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `rce`, `vulnerability`
- **Slug:** `2026-06-05-everest-forms-pro-rce-cve-2026-3300`
- **Must-know:** no
- **Summary:** A CVSS 9.8 RCE flaw in Everest Forms Pro (all versions ≤ 1.9.12) is under active exploitation leading to full WordPress site compromise; a patch exists and should be applied immediately. ~4,000 active installations are at risk.

### 4. Five Eyes Warns: Chinese Intelligence Officers Pose as Recruiters to Target Government and Military Personnel
- **Source:** SecurityWeek — https://www.securityweek.com/five-eyes-chinese-spies-target-government-military-staff-with-fake-job-opportunities/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `social-engineering`, `espionage`
- **Slug:** `2026-06-05-five-eyes-chinese-spy-fake-job-recruitment`
- **Must-know:** no
- **Summary:** Chinese intelligence officers are using fake recruiter personas on professional networking platforms to target personnel with classified or privileged access, eliciting sensitive disclosures under the guise of job opportunities. The Five Eyes advisory urges awareness training focused on unsolicited recruitment from unverifiable profiles.

### 5. PCPJack Hijacks 230 AWS, GCP, and Azure Servers to Build Covert SMTP Relay Network
- **Source:** The Hacker News — https://thehackernews.com/2026/06/pcpjack-hijacks-230-aws-google-cloud.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cloud-security`, `aws`, `gcp`, `azure`, `malware`
- **Slug:** `2026-06-05-pcpjack-cloud-smtp-relay-hijack`
- **Must-know:** no
- **Summary:** PCPJack has turned 230 compromised cloud business servers across three major providers into a synchronized SMTP proxy network refreshed every five minutes, enabling spam or phishing campaigns routed through legitimate infrastructure. Cloud operators should audit outbound SMTP egress and review IAM for unexpected service accounts.

### 6. Magecart Campaign Abuses Stripe API to Host Skimmer Payload and Exfiltrate Stolen Cards
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/credit-card-theft-campaign-abuses-stripe-to-host-stolen-payment-info/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `appsec`, `data-breach`
- **Slug:** `2026-06-04-magecart-stripe-api-credit-card-theft`
- **Must-know:** no
- **Summary:** A novel Magecart campaign routes both its skimming payload and exfiltrated card data through Stripe's legitimate API, making network-layer detection significantly harder than traditional C2 methods. E-commerce operators should enforce SRI on checkout scripts and monitor for unauthorized Stripe API key usage.

### 7. Hola Browser for Windows Compromised in Supply Chain Attack Delivering Cryptominer
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hola-browser-for-windows-compromised-to-deliver-cryptominer/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `malware`
- **Slug:** `2026-06-04-hola-browser-supply-chain-cryptominer`
- **Must-know:** no
- **Summary:** Hola Browser's Windows release was compromised to bundle a cryptominer alongside the browser installer; users who downloaded or updated during the affected window should remove the software and scan for mining processes.

### 8. FIFA World Cup 2026 Scam Wave: Thousands of Fake Domains, Banking Malware in Pirate Streams
- **Source:** The Hacker News — https://thehackernews.com/2026/06/fifa-world-cup-2026-scams-are-already.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `malware`, `data-breach`
- **Slug:** `2026-06-05-fifa-world-cup-2026-scams-banking-malware`
- **Must-know:** no
- **Summary:** With the June 11 kickoff days away, the FBI and researchers are tracking thousands of lookalike FIFA domains, banking malware in pirate streaming apps, and credential-harvesting login clones. Users should avoid third-party streaming apps and only access official FIFA channels.

### 9. Anthropic Crosses $47B Annualized Revenue in May as IPO Track Continues
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/04/ahead-of-its-ipo-anthropics-daniela-amodei-shrugs-off-doubts-about-ais-returns/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `anthropic`, `llm`
- **Slug:** `2026-06-04-anthropic-47b-arr-ipo-trajectory`
- **Must-know:** no
- **Summary:** Anthropic's annualized revenue reached $47B in May 2026, up from ~$9B at end of 2025, as Daniela Amodei deflects ROI skepticism ahead of a likely IPO. The figure is self-reported; enterprise API adoption is cited as the primary growth driver.

## Skippable

- **Industry Reactions to New Trump AI Cybersecurity Executive Order: Feedback Friday** — SecurityWeek. "Feedback Friday" reactions roundup; the EO itself is the news, not the editorial commentary.
- **Nightclub Giant RCI Says Data Breach Affects 40,000 Individuals** — SecurityWeek. Breach below the 100k user threshold with no technical substance disclosed.
- **Cisco Warns of 7th SD-WAN Zero-Day Exploited in 2026** — SecurityWeek. Duplicate coverage of CVE-2026-20245; BleepingComputer version (item 6) has more technical detail.
- **Mira Murati steps back into the spotlight, carefully** — TechCrunch AI. Profile/business piece with no model launch or security angle.
- **AI enthusiasts are in a race against time, AI skeptics are in a race against entropy** — Simon Willison. Opinion piece on AI adoption dynamics; no news value.
- **Airbnb's Brian Chesky plans to launch a new AI lab** — TechCrunch AI. Business story; no model launch, no security angle.
- **Amazon Cognito unlocks advanced capabilities with next-generation infrastructure** — AWS Security Blog. AWS marketing post on infrastructure improvements; no novel security finding for practitioners.
- **Brave Software releases Origin for a paid, bloat-free browsing experience** — BleepingComputer. Product launch with no security-relevant angle.
- **Defense tech, AI, and fundraising take center stage at StrictlyVC Los Angeles on June 18** — TechCrunch AI. Event promotion; no news value.
- **China's TA4922 Expands Cybercrime Attacks Globally** — Dark Reading. Summary too thin to draft a useful post; no IOCs or TTPs disclosed.
- **4 Critical Threats Where Attackers Have the Advantage** — Dark Reading. Gartner analyst roundup; no new IOCs, TTPs, or technical guidance beyond what's already known.
