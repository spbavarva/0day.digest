# Digest — 2026-04-14 PM

- Window: last 14h
- Raw items considered: 13
- Relevant: 9
- Skippable: 4

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** ShowDoc RCE Flaw CVE-2025-0520 Actively Exploited on Unpatched Servers — `2026-04-14-showdoc-rce-cve-2025-0520-actively-exploited.md`
- [x] **[CRITICAL]** CISA Adds 6 Known Exploited CVEs: Fortinet FortiClient EMS, Windows, and Adobe — `2026-04-14-cisa-kev-fortinet-microsoft-adobe-six-cves.md`
- [x] **[HIGH]** 108 Malicious Chrome Extensions Share C2 Infrastructure to Steal Google and Telegram Data — `2026-04-14-108-malicious-chrome-extensions-c2-data-theft.md`
- [x] **[HIGH]** Mirax Android RAT Converts Devices into SOCKS5 Proxies via Meta Ad Campaigns — `2026-04-14-mirax-android-rat-socks5-proxy-meta-ads.md`
- [x] **[HIGH]** SAP Patches Critical ABAP Vulnerability Across Enterprise Product Line — `2026-04-14-sap-critical-abap-vulnerability-patch.md`
- [x] **[MEDIUM]** RCI Hospitality Discloses Data Breach via IDOR Vulnerability in Internet Services Platform — `2026-04-14-rci-hospitality-idor-data-breach.md`
- [x] **[MEDIUM]** Triad Nexus Cybercrime Operation Exploits Major Providers to Evade Sanctions and Takedowns — `2026-04-14-triad-nexus-cybercrime-sanctions-evasion.md`
- [x] **[INFORMATIONAL]** Google Ships Rust DNS Parser to Pixel Phones to Eliminate Memory Safety Bug Class — `2026-04-14-google-rust-dns-parser-pixel-memory-safety.md`
- [x] **[INFORMATIONAL]** OpenAI Acquires Personal Finance AI Startup Hiro to Build Financial Planning into ChatGPT — `2026-04-14-openai-acquires-hiro-personal-finance.md`

## Relevant (details)

### 1. ShowDoc RCE Flaw CVE-2025-0520 Actively Exploited on Unpatched Servers
- **Source:** The Hacker News — https://thehackernews.com/2026/04/showdoc-rce-flaw-cve-2025-0520-actively.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `zero-day`, `vulnerability`
- **Slug:** `2026-04-14-showdoc-rce-cve-2025-0520-actively-exploited`
- **Must-know:** yes
- **Summary:** CVE-2025-0520, a CVSS 9.4 unrestricted file upload flaw in ShowDoc (a document management tool popular in China), is under active exploitation. Unauthenticated attackers can upload arbitrary files to achieve RCE on unpatched servers.

### 2. CISA Adds 6 Known Exploited CVEs: Fortinet FortiClient EMS, Windows, and Adobe
- **Source:** The Hacker News — https://thehackernews.com/2026/04/cisa-adds-6-known-exploited-flaws-in.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `zero-day`, `fortinet`, `microsoft`, `adobe`
- **Slug:** `2026-04-14-cisa-kev-fortinet-microsoft-adobe-six-cves`
- **Must-know:** yes
- **Summary:** CISA's KEV catalog expanded by six actively exploited CVEs, led by CVE-2026-21643 — an unauthenticated SQL injection in Fortinet FortiClient EMS (CVSS 9.1). Windows privilege escalation and Adobe Acrobat RCE flaws are also included; federal agencies face mandatory remediation deadlines.

### 3. 108 Malicious Chrome Extensions Share C2 Infrastructure to Steal Google and Telegram Data
- **Source:** The Hacker News — https://thehackernews.com/2026/04/108-malicious-chrome-extensions-steal.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `appsec`, `data-breach`
- **Slug:** `2026-04-14-108-malicious-chrome-extensions-c2-data-theft`
- **Must-know:** no
- **Summary:** Socket researchers found 108 Chrome extensions all communicating with a single C2, collecting Google and Telegram credentials and injecting arbitrary JavaScript into every page. The coordinated campaign has reached ~20,000 users, suggesting a single actor operating at scale via the Chrome Web Store.

### 4. Mirax Android RAT Converts Devices into SOCKS5 Proxies via Meta Ad Campaigns
- **Source:** The Hacker News — https://thehackernews.com/2026/04/mirax-android-rat-turns-devices-into.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `rce`
- **Slug:** `2026-04-14-mirax-android-rat-socks5-proxy-meta-ads`
- **Must-know:** no
- **Summary:** Mirax is a new Android RAT spreading via paid Meta ads to Spanish-speaking users, reaching 220,000+ accounts across Facebook, Instagram, and Threads. Infected devices are enrolled as SOCKS5 proxies while attackers retain full device control.

### 5. SAP Patches Critical ABAP Vulnerability Across Enterprise Product Line
- **Source:** SecurityWeek — https://www.securityweek.com/sap-patches-critical-abap-vulnerability/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`
- **Slug:** `2026-04-14-sap-critical-abap-vulnerability-patch`
- **Must-know:** no
- **Summary:** SAP's April patch cycle includes 19 security notes covering 12+ enterprise products, with a critical flaw in ABAP — the proprietary language powering SAP business logic. SAP systems are high-value targets given the sensitive business data they host.

### 6. RCI Hospitality Discloses Data Breach via IDOR Vulnerability in Internet Services Platform
- **Source:** SecurityWeek — https://www.securityweek.com/nightclub-giant-rci-hospitality-reports-data-breach/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`, `vulnerability`, `appsec`
- **Slug:** `2026-04-14-rci-hospitality-idor-data-breach`
- **Must-know:** no
- **Summary:** RCI Hospitality disclosed in an SEC filing that an IDOR flaw in its internet services platform exposed contractor data. The SEC filing indicates the company deemed it material; breach scope appears limited to contractor records based on the disclosure.

### 7. Triad Nexus Cybercrime Operation Exploits Major Providers to Evade Sanctions and Takedowns
- **Source:** SecurityWeek — https://www.securityweek.com/triad-nexus-evades-sanctions-to-fuel-cybercrime/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `2026-04-14-triad-nexus-cybercrime-sanctions-evasion`
- **Must-know:** no
- **Summary:** The Triad Nexus criminal operation is routing activity through legitimate major providers to frustrate sanctions enforcement and infrastructure takedowns. This resilience-by-proxy technique raises the operational cost of disruption by entangling law enforcement with major cloud/ISP providers.

### 8. Google Ships Rust DNS Parser to Pixel Phones to Eliminate Memory Safety Bug Class
- **Source:** SecurityWeek — https://www.securityweek.com/google-adds-rust-dns-parser-to-pixel-phones-for-better-security/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `appsec`, `google`
- **Slug:** `2026-04-14-google-rust-dns-parser-pixel-memory-safety`
- **Must-know:** no
- **Summary:** Google is shipping a Rust-based DNS resolver to Pixel devices, replacing memory-unsafe C/C++ code in a low-level networking component. The move is designed to eliminate buffer overflows and related memory safety bugs from DNS parsing in Android.

### 9. OpenAI Acquires Personal Finance AI Startup Hiro to Build Financial Planning into ChatGPT
- **Source:** TechCrunch AI — https://techcrunch.com/2026/04/13/openai-has-bought-ai-personal-finance-startup-hiro/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `openai`, `ai-launch`
- **Slug:** `2026-04-14-openai-acquires-hiro-personal-finance`
- **Must-know:** no
- **Summary:** OpenAI acquired Hiro, an AI personal finance startup, signaling an intent to embed financial planning capabilities into ChatGPT. The move raises questions about how OpenAI will handle sensitive financial data at consumer scale.

## Skippable

- **Analysis of 216M Security Findings Shows a 4x Increase In Critical Risk** — The Hacker News / OX Security. Vendor-commissioned report; marketing content dressed as research, no news event.
- **Bringing people together at AI for the Economy Forum** — Google AI Blog. PR/event coverage for a Google-MIT forum; no technical content.
- **Organizations Warned of Exploited Windows, Adobe Acrobat Vulnerabilities** — SecurityWeek. Duplicate coverage — the CISA KEV item covers the same exploited Windows and Adobe CVEs with broader scope.
- **Daniel Moreno-Gama is facing federal charges for attacking Sam Altman's home and OpenAI's HQ** — The Verge AI. Physical security/crime news; no cyber or AI technology angle.
