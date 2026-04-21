# Digest — 2026-04-21 PM

- Window: last 14h
- Raw items considered: 53
- Relevant: 14
- Skippable: 39

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** CVE-2026-1731: Critical Bomgar RMM RCE Actively Exploited to Spread Ransomware — `2026-04-21-cve-2026-1731-bomgar-rmm-rce-ransomware.md`
- [x] **[HIGH]** Google Antigravity AI IDE: Prompt Injection Chained to Sandbox Escape and Code Execution — `2026-04-21-google-antigravity-prompt-injection-sandbox-escape.md`
- [x] **[HIGH]** BRIDGE:BREAK — 22 Flaws in Lantronix and Silex Serial-to-IP Converters, 20,000 Devices Exposed — `2026-04-21-bridge-break-22-flaws-serial-ip-converters.md`
- [x] **[HIGH]** CISA KEV Expands: Cisco SD-WAN, Kentico CMS, and Zimbra Actively Exploited — `2026-04-21-cisa-kev-cisco-sd-wan-kentico-zimbra-exploited.md`
- [x] **[HIGH]** 6,400 Apache ActiveMQ Servers Under Active Exploitation via Code Injection Flaw — `2026-04-21-apache-activemq-6400-servers-code-injection-exploited.md`
- [x] **[HIGH]** Progress Patches RCE, OS Command Injection, and WAF Bypass in MOVEit and LoadMaster — `2026-04-21-progress-moveit-waf-loadmaster-rce-patches.md`
- [x] **[HIGH]** NGate Android Malware Trojanizes HandyPay App to Relay NFC Card Data Using AI-Generated Code — `2026-04-21-ngate-handypay-nfc-android-malware.md`
- [x] **[HIGH]** Cisco Talos Documents macOS Living-Off-the-Land Techniques Using Native OS Primitives — `2026-04-21-cisco-talos-macos-lotl-native-primitives.md`
- [x] **[MEDIUM]** Scattered Spider Senior Member 'Tylerb' Pleads Guilty to Hacking 12+ Tech Companies — `2026-04-21-scattered-spider-tylerb-guilty-plea.md`
- [x] **[MEDIUM]** Ransomware Negotiator Pleads Guilty to Secretly Aiding BlackCat (ALPHV) in 2023 Attacks — `2026-04-21-blackcat-ransomware-negotiator-insider-guilty.md`
- [x] **[MEDIUM]** FTC Settlement: Clarifai Deletes 3 Million OkCupid Photos Used Without Consent to Train Facial Recognition AI — `2026-04-21-clarifai-okcupid-ftc-facial-recognition-training-data.md`
- [x] **[MEDIUM]** Healthcare Data Breaches at Three US Organizations Affect 600,000 Patients — `2026-04-21-healthcare-data-breaches-600k-illinois-texas.md`
- [x] **[MEDIUM]** 1,500+ Perforce P4 Servers Expose Sensitive Data Without Authentication — `2026-04-21-perforce-servers-unsecured-data-exposure.md`
- [x] **[INFORMATIONAL]** YouTube Expands AI Deepfake Likeness Detection to Celebrities — `2026-04-21-youtube-ai-deepfake-detection-celebrities.md`

## Relevant (details)

### 1. CVE-2026-1731: Critical Bomgar RMM RCE Actively Exploited to Spread Ransomware
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/surge-bomgar-rmm-exploitation-demonstrates-supply-chain-risk
- **Severity:** critical
- **Tags:** `rce`, `supply-chain`, `ransomware`, `vulnerability`, `cve`
- **Summary:** CVE-2026-1731 is a critical unauthenticated RCE in Bomgar (BeyondTrust) Remote Support actively exploited to spread ransomware. The RMM platform's privileged access to all managed endpoints makes server compromise a direct pivot into every managed system — patch immediately and audit remote session logs.

### 2. Google Antigravity AI IDE: Prompt Injection Chained to Sandbox Escape and Code Execution
- **Source:** The Hacker News — https://thehackernews.com/2026/04/google-patches-antigravity-ide-flaw.html
- **Severity:** high
- **Tags:** `llm`, `rce`, `appsec`, `ai-safety`, `vulnerability`, `google`
- **Summary:** Google patched a flaw in its AI-native IDE Antigravity where prompt injection via the `find_by_name` tool bypassed sandbox isolation and achieved arbitrary code execution. The pattern — prompt injection elevating to OS execution through a trusted tool's capabilities — is likely to recur across agentic development environments.

### 3. BRIDGE:BREAK — 22 Flaws in Lantronix and Silex Serial-to-IP Converters
- **Source:** The Hacker News — https://thehackernews.com/2026/04/22-bridgebreak-flaws-expose-20000.html
- **Severity:** high
- **Tags:** `vulnerability`, `rce`, `iot`, `cve`
- **Summary:** Forescout Vedere Labs disclosed 22 vulnerabilities (BRIDGE:BREAK) in Lantronix and Silex serial-to-IP converters, with ~20,000 devices internet-exposed. These converters bridge legacy OT/ICS serial equipment to IP networks; compromise provides attackers access to systems that would otherwise be unreachable.

### 4. CISA KEV Expands: Cisco SD-WAN, Kentico CMS, and Zimbra Actively Exploited
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-flags-new-sd-wan-flaw-as-actively-exploited-in-attacks/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`, `privilege-escalation`
- **Summary:** CISA added Cisco Catalyst SD-WAN Manager, Kentico CMS, and Zimbra to the KEV catalog; federal agencies have a four-day deadline for the SD-WAN flaw. Five of eight newly added CVEs were previously flagged as exploited, confirming these are ongoing campaigns.

### 5. 6,400 Apache ActiveMQ Servers Under Active Exploitation via Code Injection Flaw
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/actively-exploited-apache-activemq-flaw-impacts-6-400-servers/
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Summary:** Shadowserver found 6,400+ exposed Apache ActiveMQ servers vulnerable to a high-severity code injection flaw under active exploitation. ActiveMQ's broad internal network access makes it a valuable lateral movement pivot; audit and patch internet-facing instances immediately.

### 6. Progress Patches RCE, OS Command Injection, and WAF Bypass in MOVEit and LoadMaster
- **Source:** SecurityWeek — https://www.securityweek.com/progress-patches-multiple-vulnerabilities-in-moveit-waf-loadmaster/
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`, `appsec`
- **Summary:** Progress patched RCE, OS command injection, and WAF bypass flaws in MOVEit Transfer WAF and LoadMaster. Given MOVEit's 2023 mass-exploitation history, these patches warrant urgent deployment — reverse-engineering and exploitation attempts typically follow quickly.

### 7. NGate Android Malware Trojanizes HandyPay App to Relay NFC Card Data Using AI-Generated Code
- **Source:** The Hacker News — https://thehackernews.com/2026/04/ngate-campaign-targets-brazil.html
- **Severity:** high
- **Tags:** `malware`, `phishing`, `llm`, `android`
- **Summary:** ESET found a new NGate variant that patches the legitimate HandyPay NFC relay app with AI-generated malicious code to steal payment card data and PINs in Brazil. AI-generated payloads in trojanized legitimate apps represent a lowering barrier to mobile malware production.

### 8. Cisco Talos Documents macOS Living-Off-the-Land Techniques Using Native OS Primitives
- **Source:** Cisco Talos — https://blog.talosintelligence.com/bad-apples-weaponizing-native-macos-primitives-for-movement-and-execution/
- **Severity:** high
- **Tags:** `appsec`, `malware`, `macos`
- **Summary:** Cisco Talos published macOS LOTL research documenting lateral movement and code execution using only native OS-supplied components. Endpoint defenses relying on known-bad binary detection will miss these techniques; behavioral detection coverage should be evaluated.

### 9. Scattered Spider Senior Member 'Tylerb' Pleads Guilty to Hacking 12+ Tech Companies
- **Source:** Krebs on Security — https://krebsonsecurity.com/2026/04/scattered-spider-member-tylerb-pleads-guilty/
- **Severity:** medium
- **Tags:** `phishing`, `data-breach`, `iam`
- **Summary:** Tyler Buchanan ("Tylerb"), 24, pleaded guilty to wire fraud and identity theft for SMS phishing and SIM swapping attacks that compromised 12+ major tech companies in 2022. Scattered Spider uses no technical exploits — only helpdesk social engineering and identity-layer manipulation.

### 10. Ransomware Negotiator Pleads Guilty to Secretly Aiding BlackCat (ALPHV) in 2023 Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/04/ransomware-negotiator-pleads-guilty-to.html
- **Severity:** medium
- **Tags:** `ransomware`
- **Summary:** Angelo Martino, a DigitalMint negotiator, admitted helping BlackCat extract higher ransoms from five victim companies while ostensibly acting on their behalf. Third US security professional guilty of aiding ransomware; highlights supply chain risk in IR engagements.

### 11. FTC Settlement: Clarifai Deletes 3 Million OkCupid Photos Used to Train Facial Recognition AI
- **Source:** TechCrunch AI — https://techcrunch.com/2026/04/21/clarifai-okcupid-facial-recognition-ai-ftc-settlement/
- **Severity:** medium
- **Tags:** `ai-safety`, `data-breach`
- **Summary:** FTC settled with Clarifai after it obtained 3M OkCupid user photos via an undisclosed executive investment relationship and used them without user consent to train facial recognition models. Signals enforcement intent around AI training data sourcing that bypasses consent.

### 12. Healthcare Data Breaches at Three US Organizations Affect 600,000 Patients
- **Source:** SecurityWeek — https://www.securityweek.com/data-breaches-at-healthcare-organizations-in-illinois-and-texas-affect-600000/
- **Severity:** medium
- **Tags:** `data-breach`
- **Summary:** Southern Illinois Dermatology, Saint Anthony Hospital, and North Texas Behavioral Health Authority collectively disclosed breaches affecting ~600,000 individuals. Concurrent multi-org disclosures may indicate shared vendor exposure.

### 13. 1,500+ Perforce P4 Servers Expose Sensitive Data Without Authentication
- **Source:** SecurityWeek — https://www.securityweek.com/unsecured-perforce-servers-expose-sensitive-data-from-major-orgs/
- **Severity:** medium
- **Tags:** `data-breach`, `supply-chain`
- **Summary:** Over 1,500 Perforce Helix Core instances allow unauthenticated read access from the internet, exposing source code, build configs, and potentially embedded credentials. Perforce is common in game studios, defense contractors, and financial firms; source code exposure enables targeted supply chain attacks.

### 14. YouTube Expands AI Deepfake Likeness Detection to Celebrities
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/915872/celebrities-will-be-able-to-find-and-request-removal-of-ai-deepfakes-on-youtube
- **Severity:** informational
- **Tags:** `ai-safety`, `deepfake`
- **Summary:** YouTube expanded AI-powered likeness detection to celebrities for deepfake identification and removal. Represents platform-scale synthetic media management infrastructure emerging in response to commoditized deepfake generation.

## Skippable

- **Celebrities will be able to find and request removal of AI deepfakes on YouTube** — The Verge AI. Duplicate source; covered under Item 14.
- **UK regulator to probe Telegram over CSAM allegations** — The Record. Content moderation regulatory story; no technical security substance for practitioners.
- **Quoting Andreas Påhlsson-Notini** — Simon Willison. Opinion piece; no news value.
- **Ordering with the Starbucks ChatGPT app was a true coffee nightmare** — The Verge AI. Consumer product review; no security or AI safety angle.
- **AI Dungeon maker Latitude unveils Voyage platform** — TechCrunch AI. Non-security gaming AI launch.
- **scosman/pelicans_riding_bicycles** — Simon Willison. Training data experiment/humor; no news value.
- **Bond social media platform uses AI to reduce doomscrolling** — TechCrunch AI. Consumer app; no security angle.
- **YouTube expands AI likeness detection to celebrities (TechCrunch)** — TechCrunch AI. Duplicate of The Verge; covered under Item 14.
- **Google Fixes Critical RCE Flaw in AI-Based Antigravity Tool** — Dark Reading. Duplicate of The Hacker News; covered under Item 2.
- **3 new ways Ads Advisor is making Google Ads safer** — Google AI Blog. Marketing content.
- **Dozens of Malicious Crypto Apps Land in Apple App Store** — SecurityWeek. Already published (`_posts/2026-04-20-malicious-crypto-wallet-apps-china-apple-app-store.md`).
- **Stopping Fraud at Each Stage of the Customer Journey** — BleepingComputer. Sponsored marketing content.
- **UK probes Telegram, teen chat sites over CSAM** — BleepingComputer. Duplicate of The Record item; both skipped.
- **EU targets two Russian propaganda networks with sanctions** — The Record. Geopolitical policy; no technical security angle.
- **John Ternus' first big problem is AI** — The Verge AI. Corporate executive succession news.
- **Cloud platform Vercel says company breached through third-party AI tool** — The Record. Already published (`_posts/2026-04-20-vercel-context-ai-breach-chain.md`).
- **5 Places where Mature SOCs Keep MTTR Fast** — The Hacker News. Vendor thought-leadership; no specific incident or CVE.
- **GRAI believes AI can make music more social** — TechCrunch AI. Non-security AI music startup.
- **[Podcast] State-sponsored and phishing threats in 2025** — Cisco Talos. Podcast summary; no standalone news value.
- **Phishing and MFA exploitation: Targeting the keys to the kingdom** — Cisco Talos. Retrospective 2025 trend analysis; no breaking news.
- **Chinese APT Targets Indian Banks, Korean Policy Circles** — Dark Reading. Generic APT disclosure with "stale TTPs" per source; minimal actionable detail.
- **Silex Technology SD-330AC and AMC Manager (CISA advisory)** — CISA Alerts. Routine ICS patch advisory; Silex component covered by BRIDGE:BREAK (Item 3).
- **Siemens RUGGEDCOM CROSSBOW SAM-P (CISA advisory)** — CISA Alerts. Routine ICS patch advisory; no active exploitation confirmed.
- **Siemens TPM 2.0 (CISA advisory)** — CISA Alerts. Routine ICS patch advisory; no active exploitation confirmed.
- **SenseLive X3050 (CISA advisory)** — CISA Alerts. Routine ICS patch advisory; CVSS 9.8 but no active exploitation and niche product.
- **Siemens Analytics Toolkit (CISA advisory)** — CISA Alerts. Routine ICS patch advisory; MITM via cert validation, no active exploitation.
- **Siemens SCALANCE (CISA advisory)** — CISA Alerts. Routine ICS patch advisory; older CVEs (2020–2022) receiving belated fix.
- **Hardy Barth Salia EV Charge Controller (CISA advisory)** — CISA Alerts. Routine ICS patch advisory; no active exploitation confirmed.
- **Siemens SINEC NMS (CISA advisory)** — CISA Alerts. Routine ICS patch advisory; no active exploitation confirmed.
- **Zero Motorcycles Firmware (CISA advisory)** — CISA Alerts. Routine ICS patch advisory; Bluetooth auth bypass, no active exploitation.
- **Siemens Industrial Edge Management (CISA advisory)** — CISA Alerts. Routine ICS patch advisory; no active exploitation confirmed.
- **Siemens RUGGEDCOM CROSSBOW SAC (CISA advisory)** — CISA Alerts. Routine ICS patch advisory; no active exploitation confirmed.
- **No Exploit Needed: How Attackers Walk Through the Front Door** — The Hacker News. Generic vendor thought-leadership on identity-based attacks; no news.
- **Yelp is making its AI chatbot way more useful** — The Verge AI. Consumer AI feature update; no security angle.
- **QIMMA Arabic LLM Leaderboard** — Hugging Face Blog. Academic NLP benchmark; no security relevance.
- **$290 Million Kelp DAO Crypto Heist Blamed on North Korea** — SecurityWeek. Already published (`_posts/2026-04-20-kelpdao-290m-lazarus-crypto-heist.md`).
- **Third US Security Expert Admits Helping Ransomware Gang** — SecurityWeek. Duplicate of The Hacker News (Angelo Martino); covered under Item 10.
- **Former ransomware negotiator pleads guilty to BlackCat attacks** — BleepingComputer. Duplicate of The Hacker News (Angelo Martino); covered under Item 10.
- **NGate Android malware uses HandyPay NFC app to steal card data** — BleepingComputer. Duplicate of The Hacker News; covered under Item 7.
