# Digest — 2026-04-13 PM

- Window: last 14h
- Raw items considered: 37
- Relevant: 18
- Skippable: 19

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Anthropic Restricts Mythos Preview After Model Autonomously Exploits Zero-Days in Major OS and Browsers — `2026-04-13-anthropic-mythos-restricted-autonomous-exploits.md`
- [x] **[CRITICAL]** OpenAI Rotates macOS Code-Signing Certs After North Korea-Linked Axios Supply Chain Attack — `2026-04-13-openai-axios-supply-chain-north-korea-cert.md`
- [x] **[CRITICAL]** Critical wolfSSL Vulnerability Allows ECDSA Signature Forgery and Certificate Bypass — `2026-04-13-wolfssl-critical-ecdsa-signature-bypass.md`
- [x] **[HIGH]** CSA Warns CISOs to Prepare for AI Vulnerability Storm Following Claude Mythos Introduction — `2026-04-13-csa-post-mythos-ai-vulnerability-storm.md`
- [x] **[HIGH]** Basic-Fit Data Breach Exposes Data of One Million Members — `2026-04-13-basic-fit-data-breach-1m.md`
- [x] **[HIGH]** Booking.com Confirms Breach Exposing Reservation and User Data, Forces PIN Resets — `2026-04-13-bookingcom-data-breach-reservation-data.md`
- [x] **[HIGH]** JanelaRAT Banking Malware Hits 14,000+ Targets in Latin America — `2026-04-13-janelarat-malware-latam-banks.md`
- [x] **[HIGH]** APT41 Deploys Zero-Detection Backdoor to Harvest Cloud Credentials via Typosquatting C2 — `2026-04-13-apt41-zero-detection-cloud-credential-backdoor.md`
- [x] **[HIGH]** FBI and Indonesian Police Dismantle W3LL Phishing Network Behind $20M in Fraud Attempts — `2026-04-13-w3ll-phishing-network-dismantled-fbi.md`
- [x] **[HIGH]** Storm Infostealer Uses Server-Side Decryption to Hijack Sessions and Bypass MFA — `2026-04-13-storm-infostealer-server-side-session-hijack.md`
- [x] **[HIGH]** CISA Adds Seven Actively Exploited Vulnerabilities to KEV Catalog Including Fortinet and Microsoft Exchange — `2026-04-13-cisa-kev-seven-new-vulnerabilities.md`
- [x] **[HIGH]** Fake Claude Website Delivers PlugX RAT via DLL Sideloading — `2026-04-13-fake-claude-plugx-rat-anthropic.md`
- [x] **[MEDIUM]** ShinyHunters Leaks Rockstar Games Analytics Data Stolen via Anodot Breach — `2026-04-13-rockstar-shinyhunters-anodot-data-leak.md`
- [x] **[MEDIUM]** Regulators Demand Post-Quantum Attestation from OT Operators Lacking the Tools to Deliver It — `2026-04-13-ot-post-quantum-cryptography-readiness-gap.md`
- [x] **[MEDIUM]** Microsoft Testing OpenClaw-Style Autonomous Agents Inside Microsoft 365 Copilot — `2026-04-13-microsoft-openclaw-copilot-365.md`
- [x] **[MEDIUM]** BrowserGate: LinkedIn Browser Extension Spying Claims Disputed by Security Researchers — `2026-04-13-linkedin-browsergate-extension-spying.md`
- [x] **[MEDIUM]** US, UK, Canada Freeze $12M in Coordinated Cryptocurrency Theft Enforcement Action — `2026-04-13-international-crypto-theft-enforcement-action.md`
- [x] **[INFORMATIONAL]** Claude Mythos Preview Now Available via Amazon Bedrock — `2026-04-13-claude-mythos-amazon-bedrock-preview.md`

## Relevant (details)

### 1. Anthropic Restricts Mythos Preview After Model Autonomously Exploits Zero-Days
- **Source:** The Hacker News — https://thehackernews.com/2026/04/your-mttd-looks-great-your-post-alert.html
- **Severity:** critical
- **Tags:** `anthropic`, `llm`, `ai-safety`, `zero-day`, `vulnerability`
- **Summary:** Anthropic restricted the Mythos Preview model after it autonomously found and exploited zero-day vulnerabilities across every major OS and browser. Palo Alto Networks warns similar AI capabilities could proliferate to threat actors within weeks to months.

### 2. OpenAI Rotates macOS Code-Signing Certs After North Korea-Linked Axios Supply Chain Attack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/openai-rotates-macos-certs-after-axios-attack-hit-code-signing-workflow/
- **Severity:** critical
- **Tags:** `supply-chain`, `openai`, `malware`, `github`
- **Summary:** OpenAI is rotating macOS code-signing certificates after a GitHub Actions workflow executed a malicious Axios npm package in a North Korea-linked supply chain attack. Exposed code-signing certs could enable trusted-looking malicious binary distribution.

### 3. Critical wolfSSL Vulnerability Allows ECDSA Signature Forgery
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/critical-flaw-in-wolfssl-library-enables-forged-certificate-use/
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `appsec`
- **Summary:** A critical flaw in the wolfSSL SSL/TLS library enables certificate forgery via improper ECDSA hash algorithm verification, affecting IoT, embedded, and automotive systems where wolfSSL is commonly deployed.

### 4. CSA Warns of AI Vulnerability Storm Following Claude Mythos Introduction
- **Source:** Dark Reading — https://www.darkreading.com/cloud-security/csa-cisos-prepare-post-mythos-exploit-storm
- **Severity:** high
- **Tags:** `llm`, `anthropic`, `ai-safety`, `vulnerability`
- **Summary:** The Cloud Security Alliance published a paper warning CISOs of an AI vulnerability storm driven by advanced reasoning models. Calls for updated IR playbooks treating AI-augmented adversaries as a distinct threat class.

### 5. Basic-Fit Data Breach Exposes One Million Members
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/european-gym-giant-basic-fit-data-breach-affects-1-million-members/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** Dutch fitness chain Basic-Fit disclosed a breach of approximately one million customer records across its European operations. Specific data categories not yet detailed.

### 6. Booking.com Confirms Breach Exposing Reservation and User Data
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-bookingcom-data-breach-forces-reservation-pin-resets/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** Booking.com confirmed unauthorized system access exposing sensitive reservation and user data; PIN resets forced. Exposed travel itinerary data creates high-quality social engineering surface for follow-on phishing.

### 7. JanelaRAT Banking Malware Hits 14,000+ Targets in Latin America
- **Source:** The Hacker News — https://thehackernews.com/2026/04/janelarat-malware-targets-latin.html
- **Severity:** high
- **Tags:** `malware`, `data-breach`
- **Summary:** JanelaRAT (modified BX RAT) recorded 14,739 attacks in Brazil in 2025, targeting named financial institutions with keylogging, screenshot capture, and financial credential theft.

### 8. APT41 Zero-Detection Backdoor Harvests Cloud Credentials via Typosquatting C2
- **Source:** Dark Reading — https://www.darkreading.com/cloud-security/apt41-zero-detection-backdoor-harvest-cloud-credentials
- **Severity:** high
- **Tags:** `malware`, `cloud-security`, `iam`, `data-breach`
- **Summary:** China-backed APT41 is targeting AWS, GCP, Azure, and Alibaba with a near-zero-detection backdoor that uses typosquatting to blend C2 traffic with legitimate cloud API calls.

### 9. FBI and Indonesian Police Dismantle W3LL Phishing Network
- **Source:** The Hacker News — https://thehackernews.com/2026/04/fbi-and-indonesian-police-dismantle.html
- **Severity:** high
- **Tags:** `phishing`
- **Summary:** FBI and Indonesian National Police dismantled the W3LL phishing network — first US-Indonesia joint enforcement action targeting a phishing kit developer — linked to $20M+ in fraud attempts.

### 10. Storm Infostealer Bypasses MFA via Server-Side Session Decryption
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/the-silent-storm-new-infostealer-hijacks-sessions-decrypts-server-side/
- **Severity:** high
- **Tags:** `malware`, `data-breach`, `appsec`
- **Summary:** Storm infostealer exfiltrates raw browser data for server-side decryption, evading endpoint tools that monitor local decryption. Stolen session tokens bypass passwords and MFA.

### 11. CISA Adds Seven Actively Exploited Vulnerabilities to KEV
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/alerts/2026/04/13/cisa-adds-seven-known-exploited-vulnerabilities-catalog
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `microsoft`, `zero-day`
- **Summary:** Seven CVEs added to KEV including a new 2026 Fortinet SQL injection, 2023 Microsoft Exchange/Windows flaws, and a 2012 VBA vulnerability still being actively exploited.

### 12. Fake Claude Website Delivers PlugX RAT via DLL Sideloading
- **Source:** SecurityWeek — https://www.securityweek.com/fake-claude-website-distributes-plugx-rat/
- **Severity:** high
- **Tags:** `malware`, `anthropic`, `phishing`
- **Summary:** Threat actors distributing PlugX RAT through a fraudulent Anthropic/Claude installer using DLL sideloading. Campaign targets users seeking AI tools; PlugX enables persistent access and lateral movement.

### 13. ShinyHunters Leaks Rockstar Games Analytics Data via Anodot Breach
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/stolen-rockstar-games-analytics-data-leaked-by-extortion-gang/
- **Severity:** medium
- **Tags:** `data-breach`, `malware`
- **Summary:** ShinyHunters is leaking Rockstar Games analytics data stolen via a breach at third-party analytics platform Anodot. Illustrates supply chain risk through downstream data vendors.

### 14. OT Operators Face Post-Quantum Attestation Mandate Without Adequate Tooling
- **Source:** Dark Reading — https://www.darkreading.com/ics-ot-security/ot-lacks-tools-cryptographic-readiness
- **Severity:** medium
- **Tags:** `vulnerability`, `appsec`, `ot-security`
- **Summary:** Regulators require OT asset owners to attest post-quantum cryptographic readiness but tooling doesn't exist for most OT environments; compliance paperwork overstates actual posture.

### 15. Microsoft Testing OpenClaw-Style Autonomous Agents in Microsoft 365 Copilot
- **Source:** The Verge AI — https://www.theverge.com/tech/911080/microsoft-ai-openclaw-365-businesses
- **Severity:** medium
- **Tags:** `microsoft`, `llm`, `ai-launch`
- **Summary:** Microsoft integrating OpenClaw-style autonomous agents into Microsoft 365 Copilot to run tasks autonomously. Security teams should review agent permissions and audit logging before enabling.

### 16. BrowserGate: LinkedIn Extension Spying Claims Under Scrutiny
- **Source:** SecurityWeek — https://www.securityweek.com/browsergate-claims-of-linkedin-spying-clash-with-security-research-findings/
- **Severity:** medium
- **Tags:** `microsoft`, `appsec`
- **Summary:** Claims of large-scale browser surveillance by LinkedIn's extension are contested by independent researchers. Microsoft has not responded formally; situation unresolved.

### 17. US, UK, Canada Freeze $12M in Crypto Theft Enforcement Action
- **Source:** SecurityWeek — https://www.securityweek.com/international-operation-targets-multimillion-dollar-crypto-theft-schemes/
- **Severity:** medium
- **Tags:** `malware`, `data-breach`
- **Summary:** US, UK, and Canada law enforcement identified $45M+ in cryptocurrency linked to theft schemes and froze $12M. No specific actors or methods disclosed in initial reporting.

### 18. Claude Mythos Preview Now Available in Amazon Bedrock
- **Source:** AWS News Blog — https://aws.amazon.com/blogs/aws/aws-weekly-roundup-claude-mythos-preview-in-amazon-bedrock-aws-agent-registry-and-more-april-13-2026/
- **Severity:** informational
- **Tags:** `anthropic`, `llm`, `model-release`, `aws`
- **Summary:** Claude Mythos is now accessible in preview via Amazon Bedrock with IAM integration and audit logging. Note recent Mythos restrictions following autonomous zero-day exploitation before enabling in production.

## Skippable

- **Quoting Steve Yegge** — Simon Willison. Opinion piece on Google's AI adoption footprint; no security angle.
- **Adobe Patches Actively Exploited Zero-Day** — Dark Reading. Already published as `_posts/2026-04-12-adobe-acrobat-reader-cve-2026-34621-patch.md`.
- **Majority of Australian Youth Still Use Social Media Despite Ban** — The Record. Policy/social issue; no security angle.
- **AI Influencers Are 'Everywhere' at Coachella** — The Verge AI. Entertainment; not relevant.
- **Microsoft Is Working on Yet Another OpenClaw-Like Agent** — TechCrunch AI. Duplicate of The Verge item; combined into single post.
- **FBI Takedown of W3LL Phishing Service Leads to Developer Arrest** — BleepingComputer. Duplicate of THN item; combined into W3LL post.
- **Stanford Report Highlights Growing Disconnect Between AI Insiders and Everyone Else** — TechCrunch AI. General AI opinion survey; low security signal.
- **Why Intelligence Requirements Fall Flat** — Flashpoint. Marketing blog; no news value.
- **FBI, Indonesia Take Down W3LL Phishing Tool** — The Record. Duplicate of THN item; combined into W3LL post.
- **Read OpenAI's Latest Internal Memo** — The Verge AI. Business strategy memo; no security angle.
- **Adobe Rolls Out Emergency Fix for Acrobat, Reader Zero-Day** — BleepingComputer. Already published as `_posts/2026-04-12-adobe-acrobat-reader-cve-2026-34621-patch.md`.
- **Vercel CEO Guillermo Rauch Signals IPO Readiness** — TechCrunch AI. Business/funding news; no security angle.
- **Exploring the New `servo` Crate** — Simon Willison. Dev/engineering post; no security angle.
- **Booking.com Says Hackers Accessed User Information** — SecurityWeek. Duplicate of BleepingComputer item.
- **Hackers Claim Breach of Rockstar Games via Cloud Analytics Platform** — The Record. Duplicate of BleepingComputer item (data now leaked, more current).
- **Mark Zuckerberg Is Reportedly Building an AI Clone** — The Verge AI. AI curiosity; no security angle.
- **⚡ Weekly Recap** — The Hacker News. Meta-digest roundup; we produce our own.
- **OpenAI Impacted by North Korea-Linked Axios Supply Chain Hack** — SecurityWeek. Duplicate of BleepingComputer item; combined into OpenAI/Axios post.
- **CPUID Hacked to Serve Trojanized CPU-Z and HWMonitor Downloads** — SecurityWeek. Already published as `_posts/2026-04-10-cpuid-supply-chain-cpu-z-hwmonitor.md`.
