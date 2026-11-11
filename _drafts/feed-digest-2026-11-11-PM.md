# Digest — 2026-11-11 PM

- Window: last 14h
- Raw items considered: 35
- Relevant: 15
- Skippable: 20

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[MEDIUM]** Blind Trust: Stealing Credentials Through CSP — `2026-11-11-blind-trust-csp-credential-theft.md`
- [x] **[HIGH]** Hackers Target Qlik Sense Servers With Reverse Shells, Stage ActiveMQ and Veeam Exploits — `2026-11-11-qlik-sense-servers-reverse-shells.md`
- [x] **[HIGH]** Citrix, Ivanti Patch Critical and High-Severity Vulnerabilities — `2026-11-11-citrix-ivanti-patch-critical-vulnerabilities.md`
- [x] **[HIGH]** Poland Shuts Down Government Services Platform ePUAP Following Cyberattack — `2026-11-11-poland-epuap-shutdown-cyberattack.md`
- [x] **[INFORMATIONAL]** Britain, France Set Out First Guidelines for Commercial Hacking Firms — `2026-11-11-uk-france-guidelines-commercial-hacking-firms.md`
- [x] **[CRITICAL]** N-able Releases Security Hotfixes for Zero-Day Vulnerabilities — `2026-11-11-n-able-zero-day-hotfixes-n-central.md`
- [x] **[HIGH]** Over 35,000 Grok-Built Apps Exposed Online, Some Leaking Confidential Data and Passwords — `2026-11-11-grok-built-apps-exposed-online.md`
- [x] **[HIGH]** eMudhra Revokes 8 More CAs It Previously Declared Unaffected by Key Compromise — `2026-11-11-emudhra-revokes-8-more-cas.md`
- [x] **[HIGH]** Cisco BroadWorks and Openwave Flaws Actively Exploited Despite Available Patches — `2026-11-11-cisco-broadworks-openwave-flaws-exploited.md`
- [x] **[HIGH]** Citrus Ransomware: VLESS for Traffic, Sn00py for Encryption, and LLMs Lending a Hand — `2026-11-11-citrus-ransomware-vless-sn00py-llm.md`
- [x] **[HIGH]** Microsoft Patches 1,259 Flaws, Including Exploited Outlook Bug That May Expose NTLMv2 Hashes — `2026-11-11-microsoft-patch-tuesday-november-2026-outlook-ntlm.md`
- [x] **[HIGH]** Recently Patched Barracuda Vulnerabilities Exploited in Attacks — `2026-11-11-barracuda-vulnerabilities-exploited-attacks.md`
- [x] **[HIGH]** Railway Says Stolen Customer AI Keys Led to $740,000 in Estimated Unauthorized Usage Charges — `2026-11-11-railway-stolen-ai-keys-unauthorized-charges.md`
- [x] **[MEDIUM]** Microsoft Researchers Show AI Agents Can Be Backdoored by Editing Fewer Than 10 Neurons — `2026-11-11-microsoft-ai-agent-backdoor-10-neurons.md`
- [x] **[INFORMATIONAL]** BotPsy: On-Device Personal Assistant with a Sub-Billion-Parameter Agentic Language Model — `2026-11-11-botpsy-on-device-agentic-model.md`

## Relevant (details)

### 1. Blind Trust: Stealing Credentials Through CSP
- **Source:** PortSwigger Research — https://portswigger.net/research/blind-trust-stealing-credentials-through-csp
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `xss`, `appsec`, `vulnerability`
- **Slug:** `blind-trust-csp-credential-theft`
- **Must-know:** no
- **Summary:** PortSwigger researchers describe a technique for turning HTML injection into credential theft even on pages protected by a Content Security Policy, when the policy allow-lists a domain that can itself be abused. This undermines the protection CSP is meant to provide.

### 2. Hackers Target Qlik Sense Servers With Reverse Shells, Stage ActiveMQ and Veeam Exploits
- **Source:** The Hacker News — https://thehackernews.com/2026/11/hackers-target-qlik-sense-servers-with.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `malware`
- **Slug:** `qlik-sense-servers-reverse-shells`
- **Must-know:** no
- **Summary:** Threat actors targeted Qlik Sense servers in October 2026 with PowerShell reverse shell attempts against multiple E.U.-based environments, identified by Cynet's CyOps and Research teams. The activity is linked to broader exploitation staging ActiveMQ and Veeam exploits.

### 3. Citrix, Ivanti Patch Critical and High-Severity Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/citrix-ivanti-patch-critical-and-high-severity-vulnerabilities/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `citrix-ivanti-patch-critical-vulnerabilities`
- **Must-know:** no
- **Summary:** Citrix and Ivanti patched critical and high-severity vulnerabilities that could let attackers tamper with certificate entries, achieve remote code execution, or compromise hosts. Both vendors are frequent high-value exploitation targets.

### 4. Poland Shuts Down Government Services Platform ePUAP Following Cyberattack
- **Source:** The Record (Recorded Future) — https://therecord.media/poland-shuts-down-government-services-platform-cyberattack
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `poland-epuap-shutdown-cyberattack`
- **Must-know:** no
- **Summary:** Poland took its nationwide ePUAP government services platform offline after a cyberattack. The system is used by citizens to submit official documents and complete administrative procedures online.

### 5. Britain, France Set Out First Guidelines for Commercial Hacking Firms
- **Source:** The Record (Recorded Future) — https://therecord.media/britain-france-set-out-guidelines-for-commercial-hacking-firms
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `policy`
- **Slug:** `uk-france-guidelines-commercial-hacking-firms`
- **Must-know:** no
- **Summary:** The UK and France published joint guidelines for commercial cyber intrusion capability (CCIC) providers, calling on them to vet customers, implement technical safeguards, and monitor/report abuse.

### 6. N-able Releases Security Hotfixes for Zero-Day Vulnerabilities
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/n-able-releases-security-hotfixes-for-zero-day-vulnerabilities/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`
- **Slug:** `n-able-zero-day-hotfixes-n-central`
- **Must-know:** yes
- **Summary:** N-able released hotfixes for zero-day bugs in its N-central RMM platform, disclosed publicly over the weekend and serious enough to force N-able to take vulnerable hosted environments offline. RMM platforms are high-value targets due to downstream access to many customer networks.

### 7. Over 35,000 Grok-Built Apps Exposed Online, Some Leaking Confidential Data and Passwords
- **Source:** The Hacker News — https://thehackernews.com/2026/11/over-35000-grok-built-apps-exposed.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `llm`, `ai-safety`
- **Slug:** `grok-built-apps-exposed-online`
- **Must-know:** no
- **Summary:** Security firm Claroc found 37,571 apps built with Grok's app-building feature online, with 35,578 accessible without sign-in; about 1 in 10 of those contained internal business data or passwords. The exposed set included apps built by staff at X and SpaceX.

### 8. eMudhra Revokes 8 More CAs It Previously Declared Unaffected by Key Compromise
- **Source:** The Hacker News — https://thehackernews.com/2026/11/emudhra-revokes-8-more-cas-it.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `data-breach`
- **Slug:** `emudhra-revokes-8-more-cas`
- **Must-know:** no
- **Summary:** eMudhra revoked 8 additional intermediate certificate authorities tied to its October key-compromise incident, after initially declaring those CAs unaffected. A flaw in the in-house script used to generate the CAs is behind the second round of revocations.

### 9. Cisco BroadWorks and Openwave Flaws Actively Exploited Despite Available Patches
- **Source:** The Hacker News — https://thehackernews.com/2026/11/cisco-broadworks-and-openwave-flaws.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `cisco-broadworks-openwave-flaws-exploited`
- **Must-know:** no
- **Summary:** CISA added two vulnerabilities in Cisco BroadWorks and Openwave Messaging Webtop Media Transcoder to its KEV catalog, citing active exploitation despite patches already being available. One flaw, CVE-2026-20320 (CVSS 7.5), is an XML external entity issue.

### 10. Citrus Ransomware: VLESS for Traffic, Sn00py for Encryption, and LLMs Lending a Hand
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/citrus-ransomware/121879/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `ransomware`, `llm`, `malware`
- **Slug:** `citrus-ransomware-vless-sn00py-llm`
- **Must-know:** no
- **Summary:** Kaspersky's GReAT team detailed the Citrus Ransomware group's TTPs, including VLESS traffic tunneling, a custom Sn00py encryption tool, and LLM-assisted tooling, with links to the Toy Ghouls cluster.

### 11. Microsoft Patches 1,259 Flaws, Including Exploited Outlook Bug That May Expose NTLMv2 Hashes
- **Source:** The Hacker News — https://thehackernews.com/2026/11/microsoft-patches-1259-flaws-including.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Slug:** `microsoft-patch-tuesday-november-2026-outlook-ntlm`
- **Must-know:** no
- **Summary:** Microsoft's November 2026 Patch Tuesday addressed 1,259 vulnerabilities, including an actively exploited Outlook bug that may expose NTLMv2 hashes usable in relay or offline-cracking attacks.

### 12. Recently Patched Barracuda Vulnerabilities Exploited in Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/recently-patched-barracuda-vulnerabilities-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`, `cve`
- **Slug:** `barracuda-vulnerabilities-exploited-attacks`
- **Must-know:** no
- **Summary:** Vulnerabilities in Barracuda products that were recently patched are now being exploited in active attacks, allowing authorization bypass and root-level access to affected devices.

### 13. Railway Says Stolen Customer AI Keys Led to $740,000 in Estimated Unauthorized Usage Charges
- **Source:** The Hacker News — https://thehackernews.com/2026/11/railway-says-stolen-customer-ai-keys.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `llm`, `supply-chain`
- **Slug:** `railway-stolen-ai-keys-unauthorized-charges`
- **Must-know:** no
- **Summary:** PaaS provider Railway disclosed that customer-stored AI provider API keys were stolen in an October breach and used to generate an estimated $740,000 in unauthorized usage charges. Railway said it will cover costs the AI providers won't refund.

### 14. Microsoft Researchers Show AI Agents Can Be Backdoored by Editing Fewer Than 10 Neurons
- **Source:** The Hacker News — https://thehackernews.com/2026/11/microsoft-researchers-show-ai-agents.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`, `vulnerability`
- **Slug:** `microsoft-ai-agent-backdoor-10-neurons`
- **Must-know:** no
- **Summary:** Microsoft researchers showed an AI model can be given a hidden backdoor by editing fewer than 10 rarely-used neurons without retraining. A trigger input causes the model to emit an attacker's command, which a connected agent would execute with its own permissions; the attack requires weight-modification access.

### 15. BotPsy: On-Device Personal Assistant with a Sub-Billion-Parameter Agentic Language Model
- **Source:** Hugging Face Blog — https://huggingface.co/blog/qvac/botpsy
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `model-release`, `llm`, `ai-launch`
- **Slug:** `botpsy-on-device-agentic-model`
- **Must-know:** no
- **Summary:** Hugging Face published a blog post introducing BotPsy, an on-device personal assistant built on a sub-billion-parameter agentic language model. No further technical detail was available in the source summary.

## Skippable

- **Gilbert + Tobin rethinks the business of law with AI** — OpenAI Blog. Customer-story marketing content, no security/technical substance.
- **Plurai wants to help AI agents work better using the same approach that helped get self-driving cars to roads** — TechCrunch AI. Generic AI-agent-reliability startup coverage, no security angle.
- **Adobe's AI experiments let you walk around in photos and interview your characters** — The Verge AI. Feature/marketing announcement, no security angle.
- **Asus, Zoom Release Security Patches** — SecurityWeek. Thin vendor patch announcement with no CVE specifics or confirmed exploitation.
- **Finite State Raises $27 Million to Secure Software and Firmware in Connected Devices** — SecurityWeek. Funding announcement, no new technical substance.
- **Inside the Fraud Underground: Key Takeaways for Retail and Financial Services Teams** — Flashpoint. Webinar recap/marketing content, no new technical substance.
- **Fortinet Patches Nearly 100 Vulnerabilities** — SecurityWeek. Routine patch-volume disclosure; no single critical-and-exploited CVE called out.
- **We Built An Agent That Broke All of Our Security Rules. Here's What We Learned.** — The Hacker News (vendor). Vendor thought-leadership/lessons-learned piece without a concrete new incident or technique.
- **Bay Raises $50 Million to Control What Enterprise AI Agents Can Do** — SecurityWeek. Funding announcement, no new technical substance.
- **Microsoft fixes audio issues caused by September security updates** — BleepingComputer. Non-security bug fix.
- **Dreeze Emerges From Stealth With $33M to Rebuild Cloud Apps After Cyberattacks** — SecurityWeek. Funding announcement, no new technical substance.
- **ICS Patch Tuesday: Siemens Flags High-Severity Flaws, Node2Shell Exposure** — SecurityWeek. Routine ICS patch-Tuesday roundup; no single critical-and-exploited CVE called out.
- **CISA flags Cisco BroadWorks flaw as actively exploited in attacks** — BleepingComputer. Duplicate coverage of the BroadWorks/Openwave KEV story; best source (The Hacker News, with CVE/CVSS detail) covered instead.
- **Microsoft fixes Exchange sign-ins broken by Windows Server updates** — BleepingComputer. Non-security bug fix.
- **Threat Actors Exploit Openwave, Cisco BroadWorks Vulnerabilities** — SecurityWeek. Duplicate coverage of the BroadWorks/Openwave KEV story; best source covered instead.
- **Experience the art and legacy of Dr. Esther Mahlangu** — Google AI Blog. Cultural/arts feature, no security or technical substance.
- **Chipmaker Patch Tuesday: Over 200 Vulnerabilities Addressed by Intel, AMD** — SecurityWeek. Routine chipmaker patch disclosure; no confirmed active exploitation.
- **ChatGPT Plus for veterans and servicemembers** — OpenAI Blog. Marketing/community program announcement, no security angle.
- **Nvidia's crisis has corporate governance experts reaching for the popcorn** — TechCrunch AI. Vague opinion piece about unspecified Nvidia governance drama, no technical/security substance.
- **Microsoft Patch Tuesday for November 2026 — Snort rules and prominent vulnerabilities** — Cisco Talos. Duplicate coverage of Microsoft Patch Tuesday; best source (The Hacker News, highlighting the actively exploited Outlook NTLM bug) covered instead.
