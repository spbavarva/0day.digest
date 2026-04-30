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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `pypi`, `malware`, `credential-theft`
- **Slug:** `2026-04-30-pytorch-lightning-pypi-supply-chain-attack`
- **Must-know:** yes
- **Summary:** Threat actors pushed two malicious versions of the `lightning` PyPI package (2.6.2 and 2.6.3) on April 30, designed to steal developer credentials. Aikido Security, Socket, and StepSecurity independently confirmed the campaign as an extension of a prior supply chain operation targeting ML tooling.

### 2. Critical cPanel and WHM Auth Bypass CVE-2026-41940 Exploited as Zero-Day Since February
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/critical-cpanel-and-whm-bug-exploited-as-a-zero-day-poc-now-available/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`, `privilege-escalation`
- **Slug:** `2026-04-30-cpanel-whm-cve-2026-41940-zero-day-exploited`
- **Must-know:** yes
- **Summary:** CVE-2026-41940 is a critical authentication bypass in cPanel, WHM, and WP Squared that has been actively exploited since at least late February 2026. CISA added it to KEV today; a public PoC is now available. Attackers can gain admin access to cPanel servers without credentials.

### 3. Critical Gemini CLI Flaw Enabled Host Code Execution and Supply Chain Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/critical-gemini-cli-flaw-enabled-host-code-execution-supply-chain-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `supply-chain`, `google`, `vulnerability`
- **Slug:** `2026-04-30-gemini-cli-rce-supply-chain-flaw`
- **Must-know:** no
- **Summary:** A critical flaw in Google's Gemini CLI let an attacker plant a malicious configuration file to execute arbitrary commands outside the sandbox. The vulnerability also enabled supply chain attacks via poisoned configs in shared repos. Patched by Google; developers should update immediately.

### 4. Linux 'Copy Fail' CVE-2026-31431 Enables Root on All Major Distros Since 2017
- **Source:** The Hacker News — https://thehackernews.com/2026/04/new-linux-copy-fail-vulnerability.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Slug:** `2026-04-30-linux-copy-fail-cve-2026-31431-lpe`
- **Must-know:** no
- **Summary:** CVE-2026-31431 "Copy Fail" (CVSS 7.8) is a local privilege escalation in the Linux kernel's `authencesn` cryptographic template, introduced in 2017. An unprivileged user can gain root by writing four bytes into the page cache of any readable file. A public exploit has been released; kernel patches are in progress across major distros.

### 5. OpenAI Launching GPT-5.5-Cyber, a Frontier Model Restricted to Critical Cyber Defenders
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/921073/openai-sam-altman-new-cybersecurity-model-gpt-5-5-cyber
- **Section:** AI — News & Analysis
- **Severity:** high
- **Tags:** `openai`, `llm`, `ai-launch`
- **Slug:** `2026-04-30-openai-gpt-5-5-cyber-security-model`
- **Must-know:** no
- **Summary:** Sam Altman announced GPT-5.5-Cyber, a new frontier cybersecurity model that will not be publicly available at launch. Initial access is restricted to vetted "critical cyber defenders." The restricted rollout is a deliberate dual-use risk management approach by OpenAI.

### 6. EtherRAT Campaign Uses GitHub Facades and SEO Poisoning to Target Enterprise Admins
- **Source:** The Hacker News — https://thehackernews.com/2026/04/etherrat-distribution-spoofing.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `github`, `phishing`
- **Slug:** `2026-04-30-etherrat-github-facades-admin-targeting`
- **Must-know:** no
- **Summary:** Atos TRC identified a campaign distributing EtherRAT through convincing GitHub facade repos targeting enterprise admins, DevOps engineers, and security analysts via SEO-poisoned search results. The technique weaponizes GitHub's trusted reputation; organizations should restrict tool downloads to verified vendor sources only.

### 7. DEEP#DOOR Python Backdoor Uses Tunneling Services to Steal Browser and Cloud Credentials
- **Source:** The Hacker News — https://thehackernews.com/2026/04/new-python-backdoor-uses-tunneling.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`, `credential-theft`
- **Slug:** `2026-04-30-deepdoor-python-backdoor-tunneling`
- **Must-know:** no
- **Summary:** DEEP#DOOR is a Python-based backdoor delivered via `install_obf.bat` that disables Windows security controls before establishing persistent access and harvesting browser/cloud credentials. It uses a tunneling service for C2, complicating perimeter detection.

### 8. Anti-DDoS Firm's Breach Enabled Botnet Campaign Against Brazilian ISPs
- **Source:** Krebs on Security — https://krebsonsecurity.com/2026/04/anti-ddos-firm-heaped-attacks-on-brazilian-isps/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `data-breach`
- **Slug:** `2026-04-30-anti-ddos-firm-botnet-brazil-isps`
- **Must-know:** no
- **Summary:** Krebs reports that a Brazilian DDoS protection firm was compromised, with the breach enabling a sustained botnet DDoS campaign against rival ISPs. The firm's CEO attributes it to a competitor using the intrusion as sabotage. Security vendors' infrastructure access makes them high-value targets.

### 9. SonicWall Urges Immediate Patching of Firewall Vulnerabilities Enabling Security Bypass and DoS
- **Source:** SecurityWeek — https://www.securityweek.com/sonicwall-urges-immediate-patching-of-firewall-vulnerabilities/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `rce`
- **Slug:** `2026-04-30-sonicwall-firewall-vulnerabilities-patch`
- **Must-know:** no
- **Summary:** SonicWall issued an urgent advisory for firewall vulnerabilities allowing security control bypass, restricted service access, and device crashes. Full CVE details are not yet published. SonicWall firewalls are widely deployed at enterprise edges; patch immediately or restrict management access.

### 10. EnOcean SmartServer Flaws Enable Security Bypass and RCE in Building Management Systems
- **Source:** SecurityWeek — https://www.securityweek.com/enocean-smartserver-flaws-expose-buildings-to-remote-hacking/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `rce`, `ics`
- **Slug:** `2026-04-30-enocean-smartserver-rce-buildings`
- **Must-know:** no
- **Summary:** Claroty disclosed two flaws in the EnOcean SmartServer building IoT gateway — security bypass and RCE — affecting building management systems for HVAC, lighting, and access control. Exploitation could give attackers physical building control. Patch or isolate management interfaces from the internet.

### 11. CISA ICS Advisories: ABB Edgenius CVSS 9.6 Auth Bypass and Five Additional ABB Product Flaws
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-120-03
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `vulnerability`, `rce`, `ics`
- **Slug:** `2026-04-30-abb-ics-edgenius-critical-rce`
- **Must-know:** no
- **Summary:** CISA published six ICS advisories for ABB products. ABB Edgenius Management Portal (CVSS 9.6) has an auth bypass enabling arbitrary code execution; ABB OPTIMAX (CVSS 8.1) has an Azure AD SSO bypass. Four additional ABB products (System 800xA, Symphony Plus, PCM600, AWIN) carry lower-severity flaws.

### 12. France Investigates 15-Year-Old Over Hack of National Identity Document Agency ANTS
- **Source:** The Record (Recorded Future) — https://therecord.media/france-investigates-teen-over-national-id-agency-hack
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `2026-04-30-france-national-id-agency-breach`
- **Must-know:** no
- **Summary:** A 15-year-old was taken into custody April 25 for allegedly breaching ANTS, France's national identity document processing agency (passports, national IDs, residence permits, driver's licenses). Scope of exposed records has not been disclosed; the investigation is ongoing.

### 13. April Windows 11 Update KB5083769 Breaks Third-Party Backup Software on 24H2 and 25H2
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/april-kb5083769-windows-11-update-causes-backup-software-failures/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `microsoft`, `vulnerability`
- **Slug:** `2026-04-30-windows-11-kb5083769-backup-failures`
- **Must-know:** no
- **Summary:** Microsoft's April 2026 KB5083769 breaks third-party backup applications on Windows 11 24H2 and 25H2. Microsoft acknowledges the issue but has no fix yet. Silent backup failures from a security patch pose a meaningful DR risk; verify backup jobs are completing on affected systems.

### 14. FBI Warns of Surge in Cyber-Enabled Cargo Theft; $725M in US and Canada Losses in 2025
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/fbi-links-cybercriminals-to-sharp-surge-in-cargo-theft-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `data-breach`
- **Slug:** `2026-04-30-fbi-cyber-cargo-theft-warning`
- **Must-know:** no
- **Summary:** The FBI warns the transportation and logistics sector of $725M in 2025 losses to cyber-enabled cargo theft, using fake carrier profiles and BEC tactics to redirect shipments. Organizations should enforce secondary verification for carrier substitutions and treat anomalous load tender changes as red flags.

### 15. Elon Musk Testifies xAI Trained Grok on OpenAI Model Outputs, Highlighting Distillation Dispute
- **Source:** TechCrunch AI — https://techcrunch.com/2026/04/30/elon-musk-testifies-that-xai-trained-grok-on-openai-models/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `openai`, `llm`, `ai-safety`
- **Slug:** `2026-04-30-xai-grok-openai-distillation-testimony`
- **Must-know:** no
- **Summary:** Musk testified that xAI trained Grok using OpenAI model outputs (distillation). The case surfaces amid ongoing legal disputes over model output reuse for training and is likely to drive stricter API terms of service across frontier labs regarding training data provenance.

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
- **ThreatsDay Bulletin: SMS Blaster Busts, OpenEMR Flaws, 600K Roblox Hacks** — The Hacker News. Aggregator newsletter; individual stories are already covered or skippable on their own.
- **New Linux 'Copy Fail' Flaw** — BleepingComputer. Duplicate of The Hacker News CVE-2026-31431 item (item 4 above).
- **Oracle Red Bull Racing Team Revs Up Automation to Boost Security** — Dark Reading. Marketing case study, no new security research.
- **OpenAI Talks About Not Talking About Goblins** — The Verge AI. Duplicate — covered in 2026-04-29 published post on goblin behavior root cause.
- **Moldova's Health Insurance Agency Reports Possible Data Leak** — The Record. Too thin — "possible" leak of "limited information" with unconfirmed scope.
- **Verified by Spotify Badge Lets You Know This Artist Isn't AI** — The Verge AI. Anti-AI verification product feature, no security research angle.
- **Enabling a New Model for Healthcare with AI Co-Clinician** — Google DeepMind. Healthcare AI research blog post, no security angle.
- **Meta Says Its Business AI Now Facilitates 10 Million Conversations a Week** — TechCrunch AI. Marketing statistics announcement, no security angle.
- **ABB AWIN Gateways** — CISA Alerts. ICS advisory with no CVSS disclosed; lower criticality than Edgenius/OPTIMAX covered in item 11.
- **ABB Ability OPTIMAX** — CISA Alerts. Auth bypass CVSS 8.1; covered and summarized in the ABB ICS advisory post (item 11 above).
- **ABB PCM600** — CISA Alerts. CVSS 4.4 path traversal, low severity; covered in ABB ICS post summary.
- **CISA Adds One Known Exploited Vulnerability to Catalog** — CISA Alerts. Duplicate — the KEV addition is CVE-2026-41940, covered in the cPanel zero-day post (item 2 above).
- **ABB Ability Symphony Plus Engineering** — CISA Alerts. PostgreSQL code execution via IEC 61850 network access; covered in ABB ICS post summary.
- **ABB System 800xA, Symphony Plus IEC 61850** — CISA Alerts. Remote device crash/fault; covered in ABB ICS post summary.
- **Meta Lost 20 Million Users Last Quarter** — The Verge AI. Business metrics story, no security angle.
- **Police Dismantles 9 Crypto Scam Centers, Arrests 276 Suspects** — BleepingComputer. Law enforcement action with no technical TTPs disclosed.
- **Critical cPanel & WHM Vulnerability Exploited as Zero-Day for Months** — SecurityWeek. Duplicate of BleepingComputer cPanel zero-day item (item 2 above).
- **The More Young People Use AI, the More They Hate It** — The Verge AI. Opinion/sentiment trend piece, no security angle.
- **'Copy Fail' Logic Flaw in Linux Kernel Enables System Takeover** — SecurityWeek. Duplicate of The Hacker News CVE-2026-31431 item (item 4 above).
- **SAP NPM Packages Targeted in Supply Chain Attack** — SecurityWeek. Duplicate — covered in 2026-04-29 published post on the Mini Shai-Hulud campaign.
