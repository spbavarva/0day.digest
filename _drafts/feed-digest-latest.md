# Digest — 2026-04-30 PM

- Window: last 14h
- Raw items considered: 50
- Relevant: 15
- Skippable: 35

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** PyTorch Lightning Compromised in PyPI Supply Chain Attack to Steal Credentials — `2026-04-30-pytorch-lightning-pypi-supply-chain-attack.md`
- [x] **[CRITICAL]** Critical cPanel and WHM Auth Bypass CVE-2026-41940 Exploited as Zero-Day Since February — `2026-04-30-cpanel-whm-cve-2026-41940-zero-day-exploited.md`
- [x] **[HIGH]** Critical Gemini CLI Flaw Enabled Host Code Execution and Supply Chain Attacks — `2026-04-30-gemini-cli-rce-supply-chain-flaw.md`
- [x] **[HIGH]** Linux 'Copy Fail' CVE-2026-31431 Enables Root on All Major Distros Since 2017 — `2026-04-30-linux-copy-fail-cve-2026-31431-lpe.md`
- [x] **[HIGH]** OpenAI Launching GPT-5.5-Cyber, a Frontier Model Restricted to Critical Cyber Defenders — `2026-04-30-openai-gpt-5-5-cyber-security-model.md`
- [x] **[HIGH]** EtherRAT Campaign Uses GitHub Facades and SEO Poisoning to Target Enterprise Admins — `2026-04-30-etherrat-github-facades-admin-targeting.md`
- [x] **[HIGH]** DEEP#DOOR Python Backdoor Uses Tunneling Services to Steal Browser and Cloud Credentials — `2026-04-30-deepdoor-python-backdoor-tunneling.md`
- [x] **[HIGH]** Anti-DDoS Firm's Breach Enabled Botnet Campaign Against Brazilian ISPs — `2026-04-30-anti-ddos-firm-botnet-brazil-isps.md`
- [x] **[HIGH]** SonicWall Urges Immediate Patching of Firewall Vulnerabilities Enabling Security Bypass and DoS — `2026-04-30-sonicwall-firewall-vulnerabilities-patch.md`
- [x] **[HIGH]** EnOcean SmartServer Flaws Enable Security Bypass and RCE in Building Management Systems — `2026-04-30-enocean-smartserver-rce-buildings.md`
- [x] **[HIGH]** CISA ICS Advisories: ABB Edgenius CVSS 9.6 Auth Bypass and Five Additional ABB Product Flaws — `2026-04-30-abb-ics-edgenius-critical-rce.md`
- [x] **[MEDIUM]** France Investigates 15-Year-Old Over Hack of National Identity Document Agency ANTS — `2026-04-30-france-national-id-agency-breach.md`
- [x] **[MEDIUM]** April Windows 11 Update KB5083769 Breaks Third-Party Backup Software on 24H2 and 25H2 — `2026-04-30-windows-11-kb5083769-backup-failures.md`
- [x] **[MEDIUM]** FBI Warns of Surge in Cyber-Enabled Cargo Theft; $725M in US and Canada Losses in 2025 — `2026-04-30-fbi-cyber-cargo-theft-warning.md`
- [x] **[MEDIUM]** Elon Musk Testifies xAI Trained Grok on OpenAI Model Outputs, Highlighting Distillation Dispute — `2026-04-30-xai-grok-openai-distillation-testimony.md`

## Relevant (details)

### 1. PyTorch Lightning Compromised in PyPI Supply Chain Attack to Steal Credentials
- **Source:** The Hacker News — https://thehackernews.com/2026/04/pytorch-lightning-compromised-in-pypi.html
- **Severity:** critical
- **Tags:** `supply-chain`, `pypi`, `malware`, `credential-theft`
- **Summary:** Malicious versions 2.6.2 and 2.6.3 of the `lightning` PyPI package were pushed on April 30 to steal developer credentials. Three independent security firms confirmed the campaign as an extension of a prior supply chain operation targeting ML tooling.

### 2. Critical cPanel and WHM Auth Bypass CVE-2026-41940 Exploited as Zero-Day Since February
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/critical-cpanel-and-whm-bug-exploited-as-a-zero-day-poc-now-available/
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`, `privilege-escalation`
- **Summary:** CVE-2026-41940 authentication bypass in cPanel, WHM, and WP Squared has been actively exploited since late February. CISA added it to KEV; a public PoC is now available. Attackers gain admin access without credentials on an estimated 20M+ websites.

### 3. Critical Gemini CLI Flaw Enabled Host Code Execution and Supply Chain Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/critical-gemini-cli-flaw-enabled-host-code-execution-supply-chain-attacks/
- **Severity:** high
- **Tags:** `rce`, `supply-chain`, `google`, `vulnerability`
- **Summary:** A critical Gemini CLI flaw let attackers plant a malicious config file to execute code outside the sandbox and enable supply chain attacks via poisoned shared configs. Google has patched the issue; update the CLI immediately.

### 4. Linux 'Copy Fail' CVE-2026-31431 Enables Root on All Major Distros Since 2017
- **Source:** The Hacker News — https://thehackernews.com/2026/04/new-linux-copy-fail-vulnerability.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Summary:** CVE-2026-31431 (CVSS 7.8) in the Linux kernel's `authencesn` template allows an unprivileged user to gain root by writing four bytes into the page cache. Introduced in 2017, it affects all major distros. A public exploit has been released; apply kernel patches now.

### 5. OpenAI Launching GPT-5.5-Cyber, a Frontier Model Restricted to Critical Cyber Defenders
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/921073/openai-sam-altman-new-cybersecurity-model-gpt-5-5-cyber
- **Severity:** high
- **Tags:** `openai`, `llm`, `ai-launch`
- **Summary:** Sam Altman announced GPT-5.5-Cyber, a new frontier cybersecurity model restricted at launch to vetted "critical cyber defenders." The limited rollout reflects deliberate dual-use risk management from OpenAI.

### 6. EtherRAT Campaign Uses GitHub Facades and SEO Poisoning to Target Enterprise Admins
- **Source:** The Hacker News — https://thehackernews.com/2026/04/etherrat-distribution-spoofing.html
- **Severity:** high
- **Tags:** `malware`, `github`, `phishing`
- **Summary:** Atos TRC identified EtherRAT being distributed via convincing GitHub facade repos surfaced through SEO poisoning, targeting enterprise admins, DevOps engineers, and security analysts. Restrict admin tool downloads to verified vendor sources.

### 7. DEEP#DOOR Python Backdoor Uses Tunneling Services to Steal Browser and Cloud Credentials
- **Source:** The Hacker News — https://thehackernews.com/2026/04/new-python-backdoor-uses-tunneling.html
- **Severity:** high
- **Tags:** `malware`, `phishing`, `credential-theft`
- **Summary:** DEEP#DOOR is a Python-based backdoor delivered via batch script that disables Windows defenses and uses tunneling for stealthy C2 while harvesting browser and cloud credentials. Hunt for unsigned batch scripts disabling Defender and tunneling tools spawned from non-standard parents.

### 8. Anti-DDoS Firm's Breach Enabled Botnet Campaign Against Brazilian ISPs
- **Source:** Krebs on Security — https://krebsonsecurity.com/2026/04/anti-ddos-firm-heaped-attacks-on-brazilian-isps/
- **Severity:** high
- **Tags:** `malware`, `data-breach`
- **Summary:** A Brazilian DDoS protection firm was compromised and its infrastructure used to run extended botnet DDoS attacks against competing ISPs. The firm's CEO attributes it to competitor sabotage. Security vendors are high-value targets given their network access and trusted position.

### 9. SonicWall Urges Immediate Patching of Firewall Vulnerabilities Enabling Security Bypass and DoS
- **Source:** SecurityWeek — https://www.securityweek.com/sonicwall-urges-immediate-patching-of-firewall-vulnerabilities/
- **Severity:** high
- **Tags:** `vulnerability`, `rce`
- **Summary:** SonicWall issued an urgent advisory for firewall flaws enabling security control bypass, restricted service access, and device crashes. Full CVE details pending. Patch immediately or restrict management interface access.

### 10. EnOcean SmartServer Flaws Enable Security Bypass and RCE in Building Management Systems
- **Source:** SecurityWeek — https://www.securityweek.com/enocean-smartserver-flaws-expose-buildings-to-remote-hacking/
- **Severity:** high
- **Tags:** `vulnerability`, `rce`, `ics`
- **Summary:** Claroty found security bypass and RCE flaws in the EnOcean SmartServer building IoT gateway. Exploitation could give attackers control over HVAC, lighting, and access control systems. Patch or isolate management interfaces from the internet.

### 11. CISA ICS Advisories: ABB Edgenius CVSS 9.6 Auth Bypass and Five Additional ABB Product Flaws
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-120-03
- **Severity:** high
- **Tags:** `vulnerability`, `rce`, `ics`
- **Summary:** Six CISA advisories today target ABB ICS products. Edgenius Management Portal (CVSS 9.6) allows auth bypass with arbitrary code execution; OPTIMAX (CVSS 8.1) allows Azure AD SSO bypass. Prioritize patching Edgenius versions 3.2.0.0 and 3.2.1.1.

### 12. France Investigates 15-Year-Old Over Hack of National Identity Document Agency ANTS
- **Source:** The Record (Recorded Future) — https://therecord.media/france-investigates-teen-over-national-id-agency-hack
- **Severity:** medium
- **Tags:** `data-breach`
- **Summary:** A 15-year-old was arrested April 25 for allegedly breaching ANTS, which processes all French passport, national ID, and residence permit applications. Scope of exposed records is unconfirmed; investigation ongoing.

### 13. April Windows 11 Update KB5083769 Breaks Third-Party Backup Software on 24H2 and 25H2
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/april-kb5083769-windows-11-update-causes-backup-software-failures/
- **Severity:** medium
- **Tags:** `microsoft`, `vulnerability`
- **Summary:** KB5083769 breaks third-party backup software on Windows 11 24H2 and 25H2. Microsoft has no fix yet. Verify backup jobs are completing on affected systems; silent failures undermine disaster recovery posture.

### 14. FBI Warns of Surge in Cyber-Enabled Cargo Theft; $725M in US and Canada Losses in 2025
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/fbi-links-cybercriminals-to-sharp-surge-in-cargo-theft-attacks/
- **Severity:** medium
- **Tags:** `phishing`, `data-breach`
- **Summary:** The FBI warned logistics companies of $725M in 2025 losses to cyber-enabled cargo theft using fake carrier profiles and BEC to redirect shipments. Enforce secondary verification for carrier substitutions and anomalous load tender changes.

### 15. Elon Musk Testifies xAI Trained Grok on OpenAI Model Outputs, Highlighting Distillation Dispute
- **Source:** TechCrunch AI — https://techcrunch.com/2026/04/30/elon-musk-testifies-that-xai-trained-grok-on-openai-models/
- **Severity:** medium
- **Tags:** `openai`, `llm`, `ai-safety`
- **Summary:** Musk testified that xAI used OpenAI model outputs to train Grok via distillation. The case is likely to drive stricter API terms around model output reuse for training competing systems and could influence AI training data provenance regulation.

## Skippable

- **Great Responsibility, Without Great Power** — Cisco Talos. Opinion newsletter on empathy in cybersecurity, no news value.
- **FDA Approval, Fundraising, and the Reality of Building in Healthcare** — TechCrunch AI. Startup founder interview, no security angle.
- **Google's Gemini AI Assistant Is Hitting the Road in Millions of Vehicles** — TechCrunch AI. Consumer product rollout, no security angle; duplicate of The Verge item.
- **Romanian Leader of Online Swatting Ring Gets 4 Years in Prison** — BleepingComputer. Criminal sentencing, no novel TTP or technical disclosure.
- **Stripe Introduces Link for AI Agents** — TechCrunch AI. Fintech wallet feature, no vulnerability or security research angle.
- **Zambia Cancels Global Digital Freedoms Conference** — The Record. Civil society/policy news, no technical security content.
- **Meta Is Running Get-Rich-Quick Ads for Its AI Tools** — The Verge AI. Marketing ethics story, no technical security angle.
- **Trump's Cyber Ambassador Nominee Advances to Full Senate Vote** — The Record. Policy appointment, no technical security content.
- **Salesforce Is Crowdsourcing Its AI Roadmap** — TechCrunch AI. Enterprise product roadmap marketing, no security angle.
- **Cloud CISO Perspectives: At Next '26** — Google Cloud Security. Google marketing newsletter, no specific security news.
- **Gemini Is Rolling Out to Cars with Google Built-In** — The Verge AI. Duplicate of TechCrunch Gemini cars item; no security angle.
- **Here's How the New Microsoft and OpenAI Deal Breaks Down** — The Verge AI. Covered in 2026-04-27 published post on the partnership restructure.
- **X Announces a Rebuilt Ad Platform Powered by AI** — TechCrunch AI. Ad platform product launch, no security angle.
- **All These Smart Glasses and Nothing to Do** — The Verge AI. Consumer gadget review, no security angle.
- **What Happens in the First 24 Hours After a New Asset Goes Live** — BleepingComputer. Sponsored content from Sprocket Security, marketing framing.
- **ThreatsDay Bulletin: SMS Blaster Busts, OpenEMR Flaws, 600K Roblox Hacks** — The Hacker News. Aggregator newsletter; individual stories already covered or skippable on their own.
- **New Linux 'Copy Fail' Flaw** — BleepingComputer. Duplicate of The Hacker News CVE-2026-31431 item (item 4 above).
- **Oracle Red Bull Racing Team Revs Up Automation to Boost Security** — Dark Reading. Marketing case study, no new security research.
- **OpenAI Talks About Not Talking About Goblins** — The Verge AI. Covered in 2026-04-29 published post on goblin behavior root cause.
- **Moldova's Health Insurance Agency Reports Possible Data Leak** — The Record. Too thin — "possible" leak of "limited information" with unconfirmed scope.
- **Verified by Spotify Badge Lets You Know This Artist Isn't AI** — The Verge AI. Anti-AI verification product feature, no security research angle.
- **Enabling a New Model for Healthcare with AI Co-Clinician** — Google DeepMind. Healthcare AI research blog post, no security angle.
- **Meta Says Its Business AI Now Facilitates 10 Million Conversations a Week** — TechCrunch AI. Marketing statistics announcement, no security angle.
- **ABB AWIN Gateways** — CISA Alerts. ICS advisory with no CVSS disclosed; lower criticality than Edgenius/OPTIMAX covered in relevant item 11.
- **ABB Ability OPTIMAX** — CISA Alerts. Auth bypass CVSS 8.1; summarized in the ABB ICS advisory post (item 11 above).
- **ABB PCM600** — CISA Alerts. CVSS 4.4 path traversal, low severity; summarized in ABB ICS post.
- **CISA Adds One Known Exploited Vulnerability to Catalog** — CISA Alerts. Duplicate — CVE-2026-41940 KEV addition is covered in the cPanel zero-day post (item 2 above).
- **ABB Ability Symphony Plus Engineering** — CISA Alerts. PostgreSQL code execution via IEC 61850 network access; summarized in ABB ICS post.
- **ABB System 800xA, Symphony Plus IEC 61850** — CISA Alerts. Remote device crash/fault; summarized in ABB ICS post.
- **Meta Lost 20 Million Users Last Quarter** — The Verge AI. Business metrics story, no security angle.
- **Police Dismantles 9 Crypto Scam Centers, Arrests 276 Suspects** — BleepingComputer. Law enforcement action, no technical TTPs disclosed.
- **Critical cPanel & WHM Vulnerability Exploited as Zero-Day for Months** — SecurityWeek. Duplicate of BleepingComputer cPanel zero-day item (item 2 above).
- **The More Young People Use AI, the More They Hate It** — The Verge AI. Opinion/sentiment trend piece, no security angle.
- **'Copy Fail' Logic Flaw in Linux Kernel Enables System Takeover** — SecurityWeek. Duplicate of The Hacker News CVE-2026-31431 item (item 4 above).
- **SAP NPM Packages Targeted in Supply Chain Attack** — SecurityWeek. Covered in 2026-04-29 published post on the Mini Shai-Hulud campaign.
