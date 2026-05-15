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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`, `vulnerability`
- **Slug:** `2026-05-12-rubygems-supply-chain-malicious-packages`
- **Must-know:** yes
- **Summary:** RubyGems suspended new account signups after a "major malicious attack" flooded the registry with hundreds of malicious packages. The scale of the attack prompted an emergency access freeze while the registry team responds; payload behavior and specific packages were not detailed in the feed summary.

### 2. Shai Hulud Worm Returns: Signed Malicious TanStack and Mistral npm Packages Deployed
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/shai-hulud-attack-ships-signed-malicious-tanstack-mistral-npm-packages/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `pypi`, `malware`
- **Slug:** `2026-05-12-shai-hulud-tanstack-mistral-npm-supply-chain`
- **Must-know:** yes
- **Summary:** A new wave of the Shai Hulud supply chain campaign (attributed to TeamPCP) compromised hundreds of npm and PyPI packages linked to the TanStack ecosystem and Mistral AI library, delivering credential-stealing malware via cryptographically signed packages. This is a distinct wave from the April 2026 campaign that targeted Bitwarden.

### 3. Fortinet Patches Critical RCE Flaws in FortiSandbox and FortiAuthenticator
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/fortinet-warns-of-critical-rce-flaws-in-fortisandbox-and-fortiauthenticator/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`, `appsec`
- **Slug:** `2026-05-12-fortinet-rce-fortisandbox-fortiauthenticator`
- **Must-know:** no
- **Summary:** Fortinet patched two critical vulnerabilities in FortiSandbox and FortiAuthenticator that allow command or arbitrary code execution. FortiAuthenticator is commonly deployed as RADIUS/SSO infrastructure, elevating its attack value in enterprise environments.

### 4. Exim CVE-2026-45185 (Dead.Letter): Use-After-Free in GnuTLS Builds Enables Code Execution
- **Source:** The Hacker News — https://thehackernews.com/2026/05/new-exim-bdat-vulnerability-exposes.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `2026-05-12-exim-cve-2026-45185-dead-letter-rce`
- **Must-know:** no
- **Summary:** CVE-2026-45185 is a use-after-free in Exim's BDAT handling that affects GnuTLS-linked builds, enabling memory corruption and potential RCE. Only GnuTLS builds are affected; OpenSSL-linked Exim is not. Administrators should identify their build type and patch immediately given Exim's internet-facing role.

### 5. Hugging Face Model Tokenizer Files Can Be Weaponized to Hijack Outputs and Exfiltrate Data
- **Source:** Dark Reading — https://www.darkreading.com/cloud-security/hugging-face-packages-weaponized-single-file-tweak
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `ai-safety`, `llm`, `malware`
- **Slug:** `2026-05-12-hugging-face-packages-weaponized-tokenizer`
- **Must-know:** no
- **Summary:** A single file tweak to a tokenizer library configuration in Hugging Face models can hijack model outputs and exfiltrate inference data. This extends supply chain threats from Python packages to model artifacts loaded implicitly by AI frameworks.

### 6. Beyond Source Code: How Attackers Exploit the Files AI Coding Agents Trust
- **Source:** Google Cloud Security — https://cloud.google.com/blog/products/identity-security/beyond-source-code-the-files-ai-coding-agents-trust-and-attackers-exploit/
- **Section:** Cloud Security & Infrastructure
- **Severity:** high
- **Tags:** `ai-safety`, `llm`, `supply-chain`, `appsec`, `devsecops`
- **Slug:** `2026-05-12-ai-coding-agent-attack-surface-files`
- **Must-know:** no
- **Summary:** Google Cloud Security research details how AI coding agents expand the developer attack surface to include repository files, agent instruction files, runtime settings, and IDE extension packages—all of which can be manipulated to inject commands or exfiltrate data via the agent's privileged access.

### 7. TrickMo Android Banking Trojan Adopts TON Blockchain C2 and SOCKS5 Network Pivoting
- **Source:** The Hacker News — https://thehackernews.com/2026/05/new-trickmo-variant-uses-ton-c2and.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Slug:** `2026-05-12-trickmo-ton-c2-android-banking-trojan`
- **Must-know:** no
- **Summary:** A new TrickMo variant observed Jan–Feb 2026 routes C2 traffic over The Open Network (TON) blockchain and establishes SOCKS5 pivots from infected Android devices, targeting banking and crypto wallet users in France, Italy, and Austria. TON-based C2 makes domain-blocking ineffective.

### 8. SAP Patches Critical Code Injection and RCE Flaws in S/4HANA and Commerce Cloud
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/sap-fixes-critical-vulnerabilities-in-commerce-cloud-and-s-4hana/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`, `appsec`
- **Slug:** `2026-05-12-sap-critical-s4hana-commerce-cloud-vulnerabilities`
- **Must-know:** no
- **Summary:** SAP's May 2026 patch batch covers 15 vulnerabilities including critical code injection in Commerce Cloud and RCE in S/4HANA. SAP ERP systems are frequent APT targets; internet-facing Commerce Cloud deployments should be prioritized.

### 9. CISA Advisory: ABB AC500 V3 PLC Stack Buffer Overflow Rated CVSS 9.8 Enables RCE
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-132-05
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`, `ics`
- **Slug:** `2026-05-12-abb-ac500-cvss98-ics-rce`
- **Must-know:** no
- **Summary:** A CVSS 9.8 stack buffer overflow in ABB AC500 V3 PLCs (versions PM5xxx 3.9.0 and 3.9.0_HF1) can cause DoS or RCE. A firmware update is available; OT teams should apply it and verify network segmentation around exposed PLCs.

### 10. Instructure Pays Ransom After Canvas Breach as Congress Announces Investigation
- **Source:** The Record (Recorded Future) — https://therecord.media/instructure-pays-ransom-canvas-incident-congress-investigation
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ransomware`, `data-breach`
- **Slug:** `2026-05-12-canvas-instructure-ransom-paid-congress`
- **Must-know:** no
- **Summary:** Instructure confirmed paying ransom to attackers who breached Canvas and disrupted students during finals, with a deal for data return and deletion. Congress has opened an investigation. Canvas serves millions of students globally; data deletion guarantees from ransomware actors are unverifiable.

### 11. West Pharmaceutical Services Hit by Ransomware, Systems Taken Offline Globally
- **Source:** SecurityWeek — https://www.securityweek.com/west-pharmaceutical-services-hit-by-disruptive-ransomware-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ransomware`, `data-breach`
- **Slug:** `2026-05-12-west-pharmaceutical-ransomware`
- **Must-know:** no
- **Summary:** West Pharmaceutical Services, a drug packaging supplier, took systems offline globally after attackers exfiltrated data and deployed ransomware. No ransomware group has claimed responsibility. The company's role in vaccine and biologic supply chains gives the disruption potential downstream impact.

### 12. Adobe Patches 52 Vulnerabilities Across 10 Products, Many Enabling Code Execution
- **Source:** SecurityWeek — https://www.securityweek.com/adobe-patches-52-vulnerabilities-in-10-products/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `2026-05-12-adobe-52-vulnerabilities-10-products`
- **Must-know:** no
- **Summary:** Adobe's May 2026 update cycle patches 52 flaws across 10 products, many with code execution potential. No exploits in the wild as of advisory date. Enterprise administrators should apply updates, prioritizing products that open untrusted external files.

### 13. CRPx0: Stealthy Cross-Platform Malware Spreads via Free OnlyFans Content Lure
- **Source:** SecurityWeek — https://www.securityweek.com/free-onlyfans-lure-used-to-spread-cross-platform-crpx0-malware/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Slug:** `2026-05-12-crpx0-cross-platform-malware-onlyfans`
- **Must-know:** no
- **Summary:** CRPx0 is a stealthy cross-platform malware campaign using a free OnlyFans lure targeting macOS and Windows, with Linux capabilities in development. The campaign is complex and evasion-focused; IOCs were not available in the feed summary.

### 14. BWH Hotels Discloses Six-Month Unauthorized Access to Guest Reservation Data
- **Source:** SecurityWeek — https://www.securityweek.com/bwh-hotels-says-hackers-had-access-to-reservation-data-for-6-months/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `2026-05-12-bwh-hotels-6-month-reservation-breach`
- **Must-know:** no
- **Summary:** BWH Hotels disclosed threat actors had access to its reservation data for six months before detection, stealing guest names and contact information. The six-month dwell time indicates a detection gap; the number of affected guests was not disclosed.

### 15. Škoda Auto Discloses Customer Data Breach After Online Shop Compromise
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/skoda-warns-of-customer-data-breach-after-online-shop-hack/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `2026-05-12-skoda-data-breach-online-shop`
- **Must-know:** no
- **Summary:** Škoda Auto's online shop was hacked and customer personal information was exfiltrated. The number of affected customers and specific data categories were not disclosed. Affected customers should anticipate targeted phishing using vehicle order details.

### 16. Android 17 Expands Anti-Scam Call Detection and Banking Privacy Protections
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/android-17-to-expand-banking-scam-call-and-privacy-protections/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `google`, `phishing`
- **Slug:** `2026-05-12-android-17-banking-scam-security`
- **Must-know:** no
- **Summary:** Android 17 (releasing next month) adds enhanced real-time scam call detection, device theft protections, and banking privacy controls. Financial app developers should review the new APIs for scam-detection integration before the release.

### 17. CISA and G7 Partners Release Minimum Elements Guidance for AI Software Bills of Materials
- **Source:** CISA Alerts — https://www.cisa.gov/resources-tools/resources/software-bill-materials-ai-minimum-elements
- **Section:** Government / Advisory
- **Severity:** medium
- **Tags:** `ai-safety`, `supply-chain`, `devsecops`
- **Slug:** `2026-05-12-cisa-g7-sbom-ai-minimum-elements`
- **Must-know:** no
- **Summary:** CISA and G7 partners published joint guidance defining minimum SBOM elements for AI systems, extending supply chain transparency requirements to model components and AI pipeline dependencies. Relevant to organizations deploying AI in regulated or critical infrastructure contexts.

### 18. Parents Sue OpenAI Over ChatGPT Advice Linked to Son's Fatal Drug Overdose
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/928691/openai-chatgpt-wrongful-death-overdose
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-safety`, `openai`, `llm`
- **Slug:** `2026-05-12-chatgpt-overdose-wrongful-death-lawsuit`
- **Must-know:** no
- **Summary:** The family of Sam Nelson filed a wrongful death suit against OpenAI claiming ChatGPT encouraged fatal drug combinations. The case joins growing litigation over AI chatbot harm and raises questions about consumer AI safety guardrails in health-adjacent conversations.

## Skippable

- **The Evolution of the Geotag** — Flashpoint. Informational research blog on OSINT geotag trends; no security incident or technical finding to act on.
- **Windows 11 KB5089549 & KB5087420 cumulative updates** — BleepingComputer. Routine Windows patch distribution; no zero-day or critical exploited flaw.
- **Microsoft May 2026 Patch Tuesday fixes 120 flaws, no zero-days** — BleepingComputer. Routine Patch Tuesday; no actively exploited CVEs disclosed.
- **Microsoft Patches 137 Vulnerabilities** — SecurityWeek. Duplicate of Patch Tuesday coverage; picks up Azure/Dynamics items but no single exploited critical stands out.
- **Musk mulled handing OpenAI to his children, Altman testifies** — TechCrunch AI. Trial testimony with no technical substance.
- **Anthropic warns investors against secondary share platforms** — TechCrunch AI. Business/financial news; no security angle.
- **Sam Altman says Musk's mind games were damaging OpenAI** — The Verge AI. Trial testimony; no technical substance.
- **Google and SpaceX in talks to put data centers into orbit** — TechCrunch AI. Speculative business reporting; no security angle.
- **Exaforce Raises $125 Million for Agentic SOC Platform** — SecurityWeek. Vendor funding announcement; no technical findings.
- **Everything Google announced at its Android Show** — TechCrunch AI. Product launch roundup; security angle covered by dedicated Android 17 item.
- **Google brings agentic AI and vibe-coded widgets to Android** — TechCrunch AI. Product announcement; no security angle.
- **The AI legal services industry is heating up. Anthropic is getting in on the action.** — TechCrunch AI. Product launch announcement; no security angle.
- **Google's 'Create My Widget' feature** — TechCrunch AI. Consumer product feature; no security angle.
- **Google adds Gemini-powered Dictation to Gboard** — TechCrunch AI. Consumer product feature; no security angle.
- **The 9 biggest new features in Android 17** — The Verge AI. Duplicate of Android 17 security item; general feature roundup.
- **Gemini's latest updates are all about controlling your phone** — The Verge AI. Product announcement; no security angle.
- **European countries are exporting surveillance tech to poor human rights record countries** — The Record. Policy advocacy report; no technical findings or new IOCs.
- **Threads tests a Meta AI integration that works similarly to Grok** — TechCrunch AI. Consumer product feature; no security angle.
- **Sam Altman takes the stand in trial against Elon Musk** — The Verge AI. Legal proceedings; no technical substance.
- **Amazon Redshift introduces AWS Graviton-based RG instances** — AWS News Blog. Cloud computing product launch; no security angle.
- **George Clooney, Tom Hanks, and Meryl Streep back new 'Human Consent Standard' for AI licensing** — The Verge AI. AI policy/entertainment; no security angle.
- **Rivian's AI-powered voice assistant is ready to roll** — The Verge AI. Automotive product; no security angle.
- **White Circle Raises $11 Million for AI Control Platform** — SecurityWeek. Vendor funding announcement; no technical findings.
- **Enabling AI sovereignty on AWS** — AWS Security Blog. Marketing blog post; no actionable security content.
- **Dessn raises $6M for its production-focused design tool** — TechCrunch AI. Startup funding; no security angle.
- **Apple Patches Dozens of Vulnerabilities in macOS, iOS** — SecurityWeek. Patch batch with no critical actively exploited CVEs; insufficient detail in feed to elevate.
- **20 Leaders Who Built the CISO Era** — Dark Reading. Retrospective/opinion piece for Dark Reading's anniversary; no news value.
- **Subnet Solutions PowerSYSTEM Center** — CISA Alerts. Narrow ICS product advisory covering info disclosure and CRLF injection; limited exposure scope.
- **ABB WebPro SNMP Card PowerValue Multiple Vulnerabilities** — CISA Alerts. ICS advisory covering DoS and session expiration issues; limited exposure scope.
- **ABB AC500 V3 Multiple Vulnerabilities** — CISA Alerts. Separate CVSS 8.3 advisory for the same ABB product family; covered alongside the CVSS 9.8 advisory item above.
- **ABB Automation Builder Gateway for Windows** — CISA Alerts. CVSS 5.3 low-severity advisory; unauthenticated PLC search only, actual PLC access blocked by user management.
- **Fuji Electric Tellus** — CISA Alerts. CVSS 7.8 privilege escalation in narrow ICS product; limited global exposure.
- **Webinar: What the Riskiest SOC Alerts Go Unanswered** — The Hacker News. Promotional webinar content for Radiant Security.
- **AI voice startup Vapi hits $500M valuation** — TechCrunch AI. AI startup funding milestone; no security angle.
- **Deal Reached With Hackers to Delete Data Stolen From Canvas** — SecurityWeek. Duplicate of The Record's Canvas/Instructure coverage; The Record has more detail on Congress investigation.
- **SAP Patches Critical S/4HANA, Commerce Vulnerabilities** — SecurityWeek. Duplicate of BleepingComputer's SAP coverage.
- **Worm Redux: Fresh Mini Shai-Hulud Infections Bite Supply Chain** — Dark Reading. Duplicate of BleepingComputer's Shai Hulud coverage.
- **Go fuzzing was missing half the toolkit. We forked the toolchain to fix it.** — Trail of Bits. Interesting developer tooling research (gosentry); no incident or vulnerability.
- **Why Agentic AI Is Security's Next Blind Spot** — The Hacker News. Opinion/sponsored analysis piece; no news value beyond the Google Cloud Security research item above.
- **State-sponsored actors, better known as the friends you don't want** — Cisco Talos. IR guidance blog post; no new incident or IOCs.
