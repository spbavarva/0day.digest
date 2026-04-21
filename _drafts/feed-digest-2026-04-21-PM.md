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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `supply-chain`, `ransomware`, `vulnerability`, `cve`
- **Slug:** `2026-04-21-cve-2026-1731-bomgar-rmm-rce-ransomware`
- **Must-know:** yes
- **Summary:** CVE-2026-1731 is a critical unauthenticated RCE in Bomgar (BeyondTrust) Remote Support currently under active exploitation to spread ransomware. Because the RMM platform has administrative access across all managed endpoints, compromising the server turns it into a pre-authenticated pivot point into every managed system.

### 2. Google Antigravity AI IDE: Prompt Injection Chained to Sandbox Escape and Code Execution
- **Source:** The Hacker News — https://thehackernews.com/2026/04/google-patches-antigravity-ide-flaw.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `rce`, `appsec`, `ai-safety`, `vulnerability`, `google`
- **Slug:** `2026-04-21-google-antigravity-prompt-injection-sandbox-escape`
- **Must-know:** no
- **Summary:** Google's AI-native IDE Antigravity had a vulnerability combining prompt injection with insufficient input sanitization in the `find_by_name` tool to escape the sandbox and achieve arbitrary code execution. Patched by Google; the attack pattern (prompt injection → OS execution via a trusted tool call) is likely to recur in other agentic development environments.

### 3. BRIDGE:BREAK — 22 Flaws in Lantronix and Silex Serial-to-IP Converters
- **Source:** The Hacker News — https://thehackernews.com/2026/04/22-bridgebreak-flaws-expose-20000.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `rce`, `iot`, `cve`
- **Slug:** `2026-04-21-bridge-break-22-flaws-serial-ip-converters`
- **Must-know:** no
- **Summary:** Forescout Vedere Labs disclosed 22 vulnerabilities (BRIDGE:BREAK) in Lantronix and Silex serial-to-IP converters, with nearly 20,000 devices internet-exposed. These converters bridge legacy OT/ICS serial equipment to IP networks; compromise undermines assumed air-gap protections in industrial, healthcare, and critical infrastructure environments.

### 4. CISA KEV Expands: Cisco SD-WAN, Kentico CMS, and Zimbra Actively Exploited
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-flags-new-sd-wan-flaw-as-actively-exploited-in-attacks/ / SecurityWeek — https://www.securityweek.com/organizations-warned-of-exploited-cisco-kentico-zimbra-vulnerabilities/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`, `privilege-escalation`
- **Slug:** `2026-04-21-cisa-kev-cisco-sd-wan-kentico-zimbra-exploited`
- **Must-know:** no
- **Summary:** CISA added flaws in Cisco Catalyst SD-WAN Manager, Kentico CMS, and Zimbra to the KEV catalog with a four-day federal remediation deadline for SD-WAN. Of eight newly added CVEs, five had been previously flagged as exploited, indicating these are ongoing campaigns.

### 5. 6,400 Apache ActiveMQ Servers Under Active Exploitation via Code Injection Flaw
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/actively-exploited-apache-activemq-flaw-impacts-6-400-servers/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `2026-04-21-apache-activemq-6400-servers-code-injection-exploited`
- **Must-know:** no
- **Summary:** Shadowserver identified 6,400+ internet-exposed Apache ActiveMQ servers vulnerable to a high-severity code injection flaw under active exploitation. ActiveMQ often runs with broad internal network access, making it a useful lateral movement vector once compromised.

### 6. Progress Patches RCE, OS Command Injection, and WAF Bypass in MOVEit and LoadMaster
- **Source:** SecurityWeek — https://www.securityweek.com/progress-patches-multiple-vulnerabilities-in-moveit-waf-loadmaster/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`, `appsec`
- **Slug:** `2026-04-21-progress-moveit-waf-loadmaster-rce-patches`
- **Must-know:** no
- **Summary:** Progress Software patched RCE, OS command injection, and WAF bypass flaws in MOVEit Transfer WAF and LoadMaster. Given MOVEit's history as a mass-exploitation target, expect rapid reverse-engineering of patches and exploitation attempts shortly after disclosure.

### 7. NGate Android Malware Trojanizes HandyPay App to Relay NFC Card Data Using AI-Generated Code
- **Source:** The Hacker News — https://thehackernews.com/2026/04/ngate-campaign-targets-brazil.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`, `llm`, `android`
- **Slug:** `2026-04-21-ngate-handypay-nfc-android-malware`
- **Must-know:** no
- **Summary:** ESET identified a new NGate Android malware variant targeting Brazil that trojanizes the HandyPay NFC relay app using what appears to be AI-generated malicious code to capture payment card data and PINs. The use of AI-generated code to patch legitimate apps suggests lowering barriers for mobile malware production.

### 8. Cisco Talos Documents macOS Living-Off-the-Land Techniques Using Native OS Primitives
- **Source:** Cisco Talos — https://blog.talosintelligence.com/bad-apples-weaponizing-native-macos-primitives-for-movement-and-execution/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `appsec`, `malware`, `macos`
- **Slug:** `2026-04-21-cisco-talos-macos-lotl-native-primitives`
- **Must-know:** no
- **Summary:** Cisco Talos published research on macOS LOTL (living-off-the-land) techniques using native OS primitives for lateral movement, persistence, and code execution — no third-party tooling required. EDR relying on known-bad binary detection will miss these; defenders should evaluate behavioral detection coverage for macOS.

### 9. Scattered Spider Senior Member 'Tylerb' Pleads Guilty to Hacking 12+ Tech Companies
- **Source:** Krebs on Security — https://krebsonsecurity.com/2026/04/scattered-spider-member-tylerb-pleads-guilty/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `data-breach`, `iam`
- **Slug:** `2026-04-21-scattered-spider-tylerb-guilty-plea`
- **Must-know:** no
- **Summary:** Tyler Buchanan (alias "Tylerb"), 24, a senior Scattered Spider member, pleaded guilty to wire fraud and aggravated identity theft for SMS phishing and SIM swapping attacks that compromised 12+ major tech companies in 2022. Scattered Spider's playbook targets helpdesks and identity providers without any technical exploits.

### 10. Ransomware Negotiator Pleads Guilty to Secretly Aiding BlackCat (ALPHV)
- **Source:** The Hacker News — https://thehackernews.com/2026/04/ransomware-negotiator-pleads-guilty-to.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ransomware`
- **Slug:** `2026-04-21-blackcat-ransomware-negotiator-insider-guilty`
- **Must-know:** no
- **Summary:** Angelo Martino, a DigitalMint ransomware negotiator, pleaded guilty to secretly helping BlackCat extract higher ransoms from five victim companies in 2023. Third in a series of US security professionals admitting to aiding ransomware gangs; highlights supply chain risk in incident response engagements.

### 11. FTC Settlement: Clarifai Deletes 3 Million OkCupid Photos Used to Train Facial Recognition AI
- **Source:** TechCrunch AI — https://techcrunch.com/2026/04/21/clarifai-okcupid-facial-recognition-ai-ftc-settlement/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-safety`, `data-breach`
- **Slug:** `2026-04-21-clarifai-okcupid-ftc-facial-recognition-training-data`
- **Must-know:** no
- **Summary:** The FTC settled with Clarifai after the company obtained 3M OkCupid user photos via an undisclosed executive investment relationship and used them without user consent to train facial recognition models. FTC enforcement signals regulatory scrutiny of AI training data sourcing that bypasses consent.

### 12. Healthcare Data Breaches at Three US Organizations Affect 600,000 Patients
- **Source:** SecurityWeek — https://www.securityweek.com/data-breaches-at-healthcare-organizations-in-illinois-and-texas-affect-600000/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `2026-04-21-healthcare-data-breaches-600k-illinois-texas`
- **Must-know:** no
- **Summary:** Southern Illinois Dermatology, Saint Anthony Hospital, and North Texas Behavioral Health Authority disclosed breaches collectively affecting ~600,000 individuals. Concurrent disclosures from separate organizations may indicate shared vendor infrastructure exposure.

### 13. 1,500+ Perforce P4 Servers Expose Sensitive Data Without Authentication
- **Source:** SecurityWeek — https://www.securityweek.com/unsecured-perforce-servers-expose-sensitive-data-from-major-orgs/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`, `supply-chain`
- **Slug:** `2026-04-21-perforce-servers-unsecured-data-exposure`
- **Must-know:** no
- **Summary:** Over 1,500 Perforce Helix Core instances allow unauthenticated read access from the internet, exposing source code, build configs, and potentially embedded credentials. Perforce is widely used by game studios, defense contractors, and financial institutions; source code exposure enables targeted supply chain attacks.

### 14. YouTube Expands AI Deepfake Likeness Detection to Celebrities
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/915872/celebrities-will-be-able-to-find-and-request-removal-of-ai-deepfakes-on-youtube
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-safety`, `deepfake`
- **Slug:** `2026-04-21-youtube-ai-deepfake-detection-celebrities`
- **Must-know:** no
- **Summary:** YouTube expanded its AI likeness detection feature to celebrities, enabling enrolled public figures to search for and remove AI-generated deepfakes. Platform-scale deepfake detection infrastructure is a signal of how major platforms are responding to the commoditization of synthetic media generation.

## Skippable

- **Celebrities will be able to find and request removal of AI deepfakes on YouTube** — The Verge AI. Covered by "YouTube expands AI likeness detection" (same story, duplicate source); included under Item 14.
- **UK regulator to probe Telegram over CSAM allegations** — The Record. Regulatory/content moderation story without technical security substance for practitioners.
- **Quoting Andreas Påhlsson-Notini** — Simon Willison. Opinion piece on AI agent design; no news value.
- **Ordering with the Starbucks ChatGPT app was a true coffee nightmare** — The Verge AI. Consumer product review; no security or AI safety angle.
- **AI Dungeon maker Latitude unveils Voyage platform** — TechCrunch AI. Non-security gaming AI platform launch.
- **scosman/pelicans_riding_bicycles** — Simon Willison. Training data poisoning experiment/humor; no news value.
- **Bond social media platform uses AI to reduce doomscrolling** — TechCrunch AI. Consumer social app; no security angle.
- **YouTube expands AI likeness detection to celebrities (TechCrunch)** — TechCrunch AI. Duplicate of The Verge coverage; included once under Item 14.
- **Google Fixes Critical RCE Flaw in AI-Based Antigravity Tool** — Dark Reading. Duplicate of The Hacker News coverage; included once under Item 2.
- **3 new ways Ads Advisor is making Google Ads safer and faster** — Google AI Blog. Marketing content for Google Ads product.
- **Dozens of Malicious Crypto Apps Land in Apple App Store** — SecurityWeek. Already published as `_posts/2026-04-20-malicious-crypto-wallet-apps-china-apple-app-store.md`.
- **Stopping Fraud at Each Stage of the Customer Journey Without Adding Friction** — BleepingComputer. Sponsored marketing content from IPQS; no news value.
- **UK probes Telegram, teen chat sites over CSAM sharing concerns** — BleepingComputer. Duplicate of The Record item; same story, skipped above.
- **EU targets two Russian propaganda networks with new sanctions** — The Record. Geopolitical sanctions without technical security angle for practitioners.
- **John Ternus' first big problem is AI** — The Verge AI. Apple CEO succession coverage; corporate executive news.
- **Cloud platform Vercel says company breached through third-party AI tool** — The Record. Already published as `_posts/2026-04-20-vercel-context-ai-breach-chain.md`.
- **5 Places where Mature SOCs Keep MTTR Fast** — The Hacker News. Vendor thought-leadership/marketing; no specific incident or CVE.
- **GRAI believes AI can make music more social** — TechCrunch AI. Non-security AI music startup; no security angle.
- **[Podcast] State-sponsored and phishing threats in 2025** — Cisco Talos. Podcast episode summarizing annual trends; no new news value.
- **Phishing and MFA exploitation: Targeting the keys to the kingdom** — Cisco Talos. Retrospective 2025 trend analysis; no breaking news.
- **Chinese APT Targets Indian Banks, Korean Policy Circles** — Dark Reading. Generic APT campaign disclosure with "stale TTPs" per source characterization; minimal technical detail.
- **Silex Technology SD-330AC and AMC Manager (CISA ICS advisory)** — CISA Alerts. Routine ICS patch advisory; covered by BRIDGE:BREAK research (Item 8) for the Silex component.
- **Siemens RUGGEDCOM CROSSBOW SAM-P (CISA ICS advisory)** — CISA Alerts. Routine ICS patch advisory; privilege escalation, no active exploitation confirmed.
- **Siemens TPM 2.0 (CISA ICS advisory)** — CISA Alerts. Routine ICS patch advisory; out-of-bound read, no active exploitation confirmed.
- **SenseLive X3050 (CISA ICS advisory)** — CISA Alerts. Routine ICS patch advisory; CVSS 9.8 but no active exploitation confirmed and no broader ecosystem impact.
- **Siemens Analytics Toolkit (CISA ICS advisory)** — CISA Alerts. Routine ICS patch advisory; MITM via certificate validation, no active exploitation.
- **Siemens SCALANCE (CISA ICS advisory)** — CISA Alerts. Routine ICS patch advisory; older CVEs (2020–2022 era) receiving belated vendor fix.
- **Hardy Barth Salia EV Charge Controller (CISA ICS advisory)** — CISA Alerts. Routine ICS patch advisory; buffer overflow RCE in EV charger firmware, no active exploitation.
- **Siemens SINEC NMS (CISA ICS advisory)** — CISA Alerts. Routine ICS patch advisory; auth bypass, no active exploitation confirmed.
- **Zero Motorcycles Firmware (CISA ICS advisory)** — CISA Alerts. Routine ICS patch advisory; Bluetooth auth bypass in motorcycle firmware, no active exploitation.
- **Siemens Industrial Edge Management (CISA ICS advisory)** — CISA Alerts. Routine ICS patch advisory; auth bypass, no active exploitation confirmed.
- **Siemens RUGGEDCOM CROSSBOW SAC (CISA ICS advisory)** — CISA Alerts. Routine ICS patch advisory; arbitrary code execution, no active exploitation confirmed.
- **No Exploit Needed: How Attackers Walk Through the Front Door via Identity-Based Attacks** — The Hacker News. Generic vendor thought-leadership on credential-based attacks; no specific incident or new technique.
- **Yelp is making its AI chatbot way more useful** — The Verge AI. Consumer AI chatbot feature upgrade; no security angle.
- **QIMMA Arabic LLM Leaderboard** — Hugging Face Blog. Academic NLP benchmark for Arabic language models; no security relevance.
- **$290 Million Kelp DAO Crypto Heist Blamed on North Korea** — SecurityWeek. Already published as `_posts/2026-04-20-kelpdao-290m-lazarus-crypto-heist.md`.
- **Third US Security Expert Admits Helping Ransomware Gang** — SecurityWeek. Duplicate of The Hacker News coverage of Angelo Martino; included once under Item 10.
- **Former ransomware negotiator pleads guilty to BlackCat attacks** — BleepingComputer. Duplicate of The Hacker News coverage of Angelo Martino; included once under Item 10.
- **NGate Android malware uses HandyPay NFC app to steal card data** — BleepingComputer. Duplicate of The Hacker News coverage; included once under Item 7.
