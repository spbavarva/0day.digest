# Digest — 2026-05-12 PM

- Window: last 14h
- Raw items considered: 58
- Relevant: 18
- Skippable: 40

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** RubyGems Suspends Signups After Hundreds of Malicious Packages Flood Registry — `2026-05-12-rubygems-supply-chain-malicious-packages.md`
- [x] **[CRITICAL]** Shai Hulud Worm Returns: Signed Malicious TanStack and Mistral npm Packages Deployed — `2026-05-12-shai-hulud-tanstack-mistral-npm-supply-chain.md`
- [x] **[HIGH]** Fortinet Patches Critical RCE Flaws in FortiSandbox and FortiAuthenticator — `2026-05-12-fortinet-rce-fortisandbox-fortiauthenticator.md`
- [x] **[HIGH]** Exim CVE-2026-45185 (Dead.Letter): Use-After-Free in GnuTLS Builds Enables Code Execution — `2026-05-12-exim-cve-2026-45185-dead-letter-rce.md`
- [x] **[HIGH]** Hugging Face Model Tokenizer Files Can Be Weaponized to Hijack Outputs and Exfiltrate Data — `2026-05-12-hugging-face-packages-weaponized-tokenizer.md`
- [x] **[HIGH]** Beyond Source Code: How Attackers Exploit the Files AI Coding Agents Trust — `2026-05-12-ai-coding-agent-attack-surface-files.md`
- [x] **[HIGH]** TrickMo Android Banking Trojan Adopts TON Blockchain C2 and SOCKS5 Network Pivoting — `2026-05-12-trickmo-ton-c2-android-banking-trojan.md`
- [x] **[HIGH]** SAP Patches Critical Code Injection and RCE Flaws in S/4HANA and Commerce Cloud — `2026-05-12-sap-critical-s4hana-commerce-cloud-vulnerabilities.md`
- [x] **[HIGH]** CISA Advisory: ABB AC500 V3 PLC Stack Buffer Overflow Rated CVSS 9.8 Enables RCE — `2026-05-12-abb-ac500-cvss98-ics-rce.md`
- [x] **[MEDIUM]** Instructure Pays Ransom After Canvas Breach as Congress Announces Investigation — `2026-05-12-canvas-instructure-ransom-paid-congress.md`
- [x] **[MEDIUM]** West Pharmaceutical Services Hit by Ransomware, Systems Taken Offline Globally — `2026-05-12-west-pharmaceutical-ransomware.md`
- [x] **[MEDIUM]** Adobe Patches 52 Vulnerabilities Across 10 Products, Many Enabling Code Execution — `2026-05-12-adobe-52-vulnerabilities-10-products.md`
- [x] **[MEDIUM]** CRPx0: Stealthy Cross-Platform Malware Spreads via Free OnlyFans Content Lure — `2026-05-12-crpx0-cross-platform-malware-onlyfans.md`
- [x] **[MEDIUM]** BWH Hotels Discloses Six-Month Unauthorized Access to Guest Reservation Data — `2026-05-12-bwh-hotels-6-month-reservation-breach.md`
- [x] **[MEDIUM]** Škoda Auto Discloses Customer Data Breach After Online Shop Compromise — `2026-05-12-skoda-data-breach-online-shop.md`
- [x] **[MEDIUM]** Android 17 Expands Anti-Scam Call Detection and Banking Privacy Protections — `2026-05-12-android-17-banking-scam-security.md`
- [x] **[MEDIUM]** CISA and G7 Partners Release Minimum Elements Guidance for AI Software Bills of Materials — `2026-05-12-cisa-g7-sbom-ai-minimum-elements.md`
- [x] **[MEDIUM]** Parents Sue OpenAI Over ChatGPT Advice Linked to Son's Fatal Drug Overdose — `2026-05-12-chatgpt-overdose-wrongful-death-lawsuit.md`

## Relevant (details)

### 1. RubyGems Suspends Signups After Hundreds of Malicious Packages Flood Registry
- **Source:** The Hacker News — https://thehackernews.com/2026/05/rubygems-suspends-new-signups-after.html
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`, `vulnerability`
- **Summary:** RubyGems suspended new account signups after a "major malicious attack" flooded the registry with hundreds of malicious packages. The scale prompted an emergency access freeze; payload behavior and specific package names were not detailed in the feed summary.

### 2. Shai Hulud Worm Returns: Signed Malicious TanStack and Mistral npm Packages Deployed
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/shai-hulud-attack-ships-signed-malicious-tanstack-mistral-npm-packages/
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `pypi`, `malware`
- **Summary:** A new Shai Hulud wave (attributed to TeamPCP) compromised hundreds of signed npm and PyPI packages in the TanStack ecosystem and Mistral AI library, delivering credential-stealing malware. This is distinct from the April 2026 Bitwarden-targeting campaign.

### 3. Fortinet Patches Critical RCE Flaws in FortiSandbox and FortiAuthenticator
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/fortinet-warns-of-critical-rce-flaws-in-fortisandbox-and-fortiauthenticator/
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`, `appsec`
- **Summary:** Two critical Fortinet vulnerabilities enable command/code execution in FortiSandbox and FortiAuthenticator. FortiAuthenticator's role in RADIUS/SSO infrastructure makes it a high-value target; patches available in May 2026 advisories.

### 4. Exim CVE-2026-45185 (Dead.Letter): Use-After-Free in GnuTLS Builds Enables Code Execution
- **Source:** The Hacker News — https://thehackernews.com/2026/05/new-exim-bdat-vulnerability-exposes.html
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Summary:** CVE-2026-45185 is a use-after-free in Exim BDAT handling that affects GnuTLS-linked builds, enabling RCE. OpenSSL-linked builds are not affected. Administrators should identify their build type and patch immediately given Exim's internet-facing role.

### 5. Hugging Face Model Tokenizer Files Can Be Weaponized to Hijack Outputs and Exfiltrate Data
- **Source:** Dark Reading — https://www.darkreading.com/cloud-security/hugging-face-packages-weaponized-single-file-tweak
- **Severity:** high
- **Tags:** `supply-chain`, `ai-safety`, `llm`, `malware`
- **Summary:** A single file tweak to a tokenizer config in Hugging Face models can hijack outputs and exfiltrate inference data. This extends AI supply chain threats from packages to model artifact files that frameworks load implicitly.

### 6. Beyond Source Code: How Attackers Exploit the Files AI Coding Agents Trust
- **Source:** Google Cloud Security — https://cloud.google.com/blog/products/identity-security/beyond-source-code-the-files-ai-coding-agents-trust-and-attackers-exploit/
- **Severity:** high
- **Tags:** `ai-safety`, `llm`, `supply-chain`, `appsec`, `devsecops`
- **Summary:** Google Cloud Security research details how AI coding agents expand the attack surface to agent instruction files, IDE extensions, and runtime configs—all of which can be weaponized to achieve prompt injection or code execution via the agent's privileged access.

### 7. TrickMo Android Banking Trojan Adopts TON Blockchain C2 and SOCKS5 Network Pivoting
- **Source:** The Hacker News — https://thehackernews.com/2026/05/new-trickmo-variant-uses-ton-c2-and.html
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Summary:** A TrickMo variant observed Jan–Feb 2026 uses The Open Network (TON) blockchain for C2 and SOCKS5 proxying to pivot through infected Android devices, targeting banking/crypto users in France, Italy, and Austria. TON-based C2 makes domain-level blocking ineffective.

### 8. SAP Patches Critical Code Injection and RCE Flaws in S/4HANA and Commerce Cloud
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/sap-fixes-critical-vulnerabilities-in-commerce-cloud-and-s-4hana/
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`, `appsec`
- **Summary:** SAP's May 2026 patch addresses 15 vulnerabilities including critical code injection (Commerce Cloud) and RCE (S/4HANA). SAP ERP systems are frequent APT targets; internet-facing Commerce Cloud deployments should be patched first.

### 9. CISA Advisory: ABB AC500 V3 PLC Stack Buffer Overflow Rated CVSS 9.8 Enables RCE
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-132-05
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`, `ics`
- **Summary:** A CVSS 9.8 stack buffer overflow in ABB AC500 V3 PLCs (PM5xxx 3.9.0 and 3.9.0_HF1) enables DoS or RCE. A firmware update is available; OT teams should apply it and verify network segmentation.

### 10. Instructure Pays Ransom After Canvas Breach as Congress Announces Investigation
- **Source:** The Record (Recorded Future) — https://therecord.media/instructure-pays-ransom-canvas-incident-congress-investigation
- **Severity:** medium
- **Tags:** `ransomware`, `data-breach`
- **Summary:** Instructure paid ransom to attackers who breached Canvas during finals, with a deal for data return and deletion. Congress opened an investigation. Data deletion guarantees from ransomware actors are unverifiable.

### 11. West Pharmaceutical Services Hit by Ransomware, Systems Taken Offline Globally
- **Source:** SecurityWeek — https://www.securityweek.com/west-pharmaceutical-services-hit-by-disruptive-ransomware-attack/
- **Severity:** medium
- **Tags:** `ransomware`, `data-breach`
- **Summary:** West Pharmaceutical Services (drug packaging supplier) took global systems offline after data exfiltration and ransomware deployment. Its role in vaccine/biologic supply chains gives the disruption potential downstream impact.

### 12. Adobe Patches 52 Vulnerabilities Across 10 Products, Many Enabling Code Execution
- **Source:** SecurityWeek — https://www.securityweek.com/adobe-patches-52-vulnerabilities-in-10-products/
- **Severity:** medium
- **Tags:** `rce`, `vulnerability`, `cve`
- **Summary:** Adobe's May 2026 update patches 52 flaws across 10 products with code execution potential; no exploits in the wild. Administrators should prioritize products that open untrusted external files.

### 13. CRPx0: Stealthy Cross-Platform Malware Spreads via Free OnlyFans Content Lure
- **Source:** SecurityWeek — https://www.securityweek.com/free-onlyfans-lure-used-to-spread-cross-platform-crpx0-malware/
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Summary:** CRPx0 is a complex, evasion-focused malware campaign using a free OnlyFans lure targeting macOS and Windows, with Linux support in development. IOCs not available in the feed summary.

### 14. BWH Hotels Discloses Six-Month Unauthorized Access to Guest Reservation Data
- **Source:** SecurityWeek — https://www.securityweek.com/bwh-hotels-says-hackers-had-access-to-reservation-data-for-6-months/
- **Severity:** medium
- **Tags:** `data-breach`
- **Summary:** BWH Hotels disclosed six months of threat actor access to guest reservation data before detection. Stolen data includes names and contact information; number of affected guests undisclosed.

### 15. Škoda Auto Discloses Customer Data Breach After Online Shop Compromise
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/skoda-warns-of-customer-data-breach-after-online-shop-hack/
- **Severity:** medium
- **Tags:** `data-breach`
- **Summary:** Škoda Auto's online shop was compromised, with customer personal information exfiltrated. Scope and specific data categories undisclosed. Customers should anticipate targeted phishing using vehicle order details.

### 16. Android 17 Expands Anti-Scam Call Detection and Banking Privacy Protections
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/android-17-to-expand-banking-scam-call-and-privacy-protections/
- **Severity:** medium
- **Tags:** `google`, `phishing`
- **Summary:** Android 17 (releasing next month) adds real-time scam call detection, device theft protections, and banking privacy controls. Financial app developers should review the new APIs ahead of launch.

### 17. CISA and G7 Partners Release Minimum Elements Guidance for AI Software Bills of Materials
- **Source:** CISA Alerts — https://www.cisa.gov/resources-tools/resources/software-bill-materials-ai-minimum-elements
- **Severity:** medium
- **Tags:** `ai-safety`, `supply-chain`, `devsecops`
- **Summary:** CISA and G7 partners published minimum SBOM elements guidance for AI systems, extending supply chain transparency requirements to model components and AI pipeline dependencies.

### 18. Parents Sue OpenAI Over ChatGPT Advice Linked to Son's Fatal Drug Overdose
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/928691/openai-chatgpt-wrongful-death-overdose
- **Severity:** medium
- **Tags:** `ai-safety`, `openai`, `llm`
- **Summary:** Sam Nelson's family filed a wrongful death suit against OpenAI claiming ChatGPT encouraged fatal drug combinations. The case joins growing AI chatbot harm litigation and raises questions about consumer safety guardrails in health-adjacent interactions.

## Skippable

- **The Evolution of the Geotag** — Flashpoint. Informational research blog on OSINT trends; no security incident or actionable technical finding.
- **Windows 11 KB5089549 & KB5087420 cumulative updates** — BleepingComputer. Routine Windows patch distribution; no zero-day or critical exploited flaw.
- **Microsoft May 2026 Patch Tuesday fixes 120 flaws, no zero-days** — BleepingComputer. Routine Patch Tuesday; no actively exploited CVEs.
- **Microsoft Patches 137 Vulnerabilities** — SecurityWeek. Duplicate of Patch Tuesday coverage; no single critical exploited CVE stands out.
- **Musk mulled handing OpenAI to his children, Altman testifies** — TechCrunch AI. Trial testimony; no technical substance.
- **Anthropic warns investors against secondary share platforms** — TechCrunch AI. Business/financial news; no security angle.
- **Sam Altman says Musk's mind games were damaging OpenAI** — The Verge AI. Trial testimony; no technical substance.
- **Google and SpaceX in talks to put data centers into orbit** — TechCrunch AI. Speculative business reporting; no security angle.
- **Exaforce Raises $125 Million for Agentic SOC Platform** — SecurityWeek. Vendor funding announcement; no technical findings.
- **Everything Google announced at its Android Show** — TechCrunch AI. Product launch roundup; security angle covered by dedicated Android 17 item.
- **Google brings agentic AI and vibe-coded widgets to Android** — TechCrunch AI. Product announcement; no security angle.
- **The AI legal services industry is heating up. Anthropic is getting in on the action.** — TechCrunch AI. Product launch; no security angle.
- **Google's 'Create My Widget' feature** — TechCrunch AI. Consumer product feature; no security angle.
- **Google adds Gemini-powered Dictation to Gboard** — TechCrunch AI. Consumer product feature; no security angle.
- **The 9 biggest new features in Android 17** — The Verge AI. Duplicate of Android 17 security item; general feature roundup.
- **Gemini's latest updates are all about controlling your phone** — The Verge AI. Product announcement; no security angle.
- **European countries exporting surveillance tech to human rights concern countries** — The Record. Policy advocacy report; no new IOCs or technical findings.
- **Threads tests a Meta AI integration that works similarly to Grok** — TechCrunch AI. Consumer product feature; no security angle.
- **Sam Altman takes the stand in trial against Elon Musk** — The Verge AI. Legal proceedings; no technical substance.
- **Amazon Redshift introduces AWS Graviton-based RG instances** — AWS News Blog. Cloud computing product launch; no security angle.
- **George Clooney, Tom Hanks, and Meryl Streep back Human Consent Standard for AI** — The Verge AI. AI policy/entertainment; no security angle.
- **Rivian's AI-powered voice assistant is ready to roll** — The Verge AI. Automotive product; no security angle.
- **White Circle Raises $11 Million for AI Control Platform** — SecurityWeek. Vendor funding; no technical findings.
- **Enabling AI sovereignty on AWS** — AWS Security Blog. Marketing blog; no actionable security content.
- **Dessn raises $6M for production-focused design tool** — TechCrunch AI. Startup funding; no security angle.
- **Apple Patches Dozens of Vulnerabilities in macOS, iOS** — SecurityWeek. Patch batch with no critical actively exploited CVEs noted in feed summary.
- **20 Leaders Who Built the CISO Era** — Dark Reading. Retrospective/opinion for Dark Reading's anniversary; no news value.
- **Subnet Solutions PowerSYSTEM Center** — CISA Alerts. Narrow ICS product; info disclosure and CRLF injection with limited exposure scope.
- **ABB WebPro SNMP Card PowerValue Multiple Vulnerabilities** — CISA Alerts. ICS advisory covering DoS and session expiration; limited exposure scope.
- **ABB AC500 V3 Multiple Vulnerabilities** — CISA Alerts. CVSS 8.3 advisory for same ABB product family; covered alongside the CVSS 9.8 item above.
- **ABB Automation Builder Gateway for Windows** — CISA Alerts. CVSS 5.3; unauthenticated PLC search only, actual PLC access blocked by device user management.
- **Fuji Electric Tellus** — CISA Alerts. CVSS 7.8 privilege escalation in narrow ICS product; limited global exposure.
- **Webinar: What the Riskiest SOC Alerts Go Unanswered** — The Hacker News. Promotional webinar content for Radiant Security.
- **AI voice startup Vapi hits $500M valuation** — TechCrunch AI. AI startup milestone; no security angle.
- **Deal Reached With Hackers to Delete Data Stolen From Canvas** — SecurityWeek. Duplicate of The Record's Canvas/Instructure coverage.
- **SAP Patches Critical S/4HANA, Commerce Vulnerabilities** — SecurityWeek. Duplicate of BleepingComputer's SAP coverage.
- **Worm Redux: Fresh Mini Shai-Hulud Infections Bite Supply Chain** — Dark Reading. Duplicate of BleepingComputer's Shai Hulud coverage.
- **Go fuzzing was missing half the toolkit. We forked the toolchain to fix it.** — Trail of Bits. Interesting developer tooling (gosentry fork); no incident or vulnerability.
- **Why Agentic AI Is Security's Next Blind Spot** — The Hacker News. Opinion/sponsored analysis; no news value beyond Google Cloud Security item above.
- **State-sponsored actors, better known as the friends you don't want** — Cisco Talos. IR guidance blog; no new incident or IOCs.
