# Digest — 2026-06-08 PM

- Window: last 14h
- Raw items considered: 45
- Relevant: 15
- Skippable: 30

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Meta Blocks NSO Group's New WhatsApp Phishing Attack, Files Contempt Order — `2026-06-08-nso-whatsapp-spyware-phishing-contempt.md`
- [x] **[CRITICAL]** Gogs Patches Critical Zero-Day Enabling Remote Code Execution — `2026-06-08-gogs-critical-zero-day-rce.md`
- [x] **[HIGH]** 'Hades' Campaign Against PyPI Puts New Spin on Shai-Hulud — `2026-06-08-hades-pypi-supply-chain-campaign.md`
- [x] **[CRITICAL]** Critical UniFi OS Bug Lets Hackers Gain Root Without Authentication — `2026-06-08-unifi-os-critical-rce-chain.md`
- [x] **[CRITICAL]** Check Point VPN Zero-Day (CVE-2026-50751) Exploited by Qilin Ransomware Gang — `2026-06-08-check-point-vpn-zero-day-qilin-ransomware.md`
- [x] **[HIGH]** Everest Forms Vulnerability Exploited to Hack WordPress Sites — `2026-06-08-everest-forms-wordpress-rce-exploited.md`
- [x] **[MEDIUM]** 174,000 Impacted by Lansing Community College Data Breach — `2026-06-08-lansing-community-college-breach.md`
- [x] **[MEDIUM]** Silent Ransom Group Uses DNS Fast Flux to Hide C2 Infrastructure — `2026-06-08-silent-ransom-group-dns-fast-flux.md`
- [x] **[HIGH]** VerdantBamboo Deploys BSD Variant of BRICKSTORM Backdoor on Linux Appliances — `2026-06-08-verdantbamboo-brickstorm-bsd-linux.md`
- [x] **[INFORMATIONAL]** OpenAI Rolling Out ChatGPT Account Security Controls — `2026-06-08-openai-chatgpt-account-security-controls.md`
- [x] **[INFORMATIONAL]** Anthropic Urges Industry Coordination to Allow for a 'Pause' in AI Development — `2026-06-08-anthropic-ai-pause-coordination.md`
- [x] **[HIGH]** SolarWinds Serv-U Vulnerability Exploited in the Wild — `2026-06-08-solarwinds-serv-u-vulnerability-exploited.md`
- [x] **[HIGH]** UNC3753 Used Vishing and Physical Intrusions in U.S. Data Theft Extortion Campaign — `2026-06-08-unc3753-vishing-physical-intrusion-extortion.md`
- [x] **[INFORMATIONAL]** VS Code Adds 2-Hour Extension Auto-Update Delay to Limit Supply Chain Attacks — `2026-06-08-vscode-extension-auto-update-delay.md`
- [x] **[HIGH]** Over 20,000 Instagram Accounts Stolen in Meta AI Support Hack — `2026-06-08-instagram-meta-ai-support-breach.md`

## Relevant (details)

### 1. Meta Blocks NSO Group's New WhatsApp Phishing Attack, Files Contempt Order
- **Source:** The Hacker News — https://thehackernews.com/2026/06/meta-blocks-nso-groups-new-whatsapp.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `malware`
- **Slug:** `nso-whatsapp-spyware-phishing-contempt`
- **Must-know:** no
- **Summary:** Meta detected and blocked new spear-phishing attempts against WhatsApp users tied to NSO Group, and is filing a federal contempt order alleging the campaign violates an existing injunction. (Picked over three duplicate stories from BleepingComputer, The Record, and SecurityWeek covering the same disclosure.)

### 2. Gogs Patches Critical Zero-Day Enabling Remote Code Execution
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/gogs-patches-critical-zero-day-enabling-remote-code-execution/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `zero-day`, `vulnerability`, `cve`
- **Slug:** `gogs-critical-zero-day-rce`
- **Must-know:** no
- **Summary:** Gogs patched a critical zero-day allowing remote code execution against internet-facing instances, giving attackers access to all hosted repositories including private ones. Active in-the-wild exploitation is not explicitly confirmed in the source.

### 3. 'Hades' Campaign Against PyPI Puts New Spin on Shai-Hulud
- **Source:** Dark Reading — https://www.darkreading.com/application-security/hades-campaign-pypi-shai-hulud
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `pypi`, `malware`
- **Slug:** `hades-pypi-supply-chain-campaign`
- **Must-know:** no
- **Summary:** A campaign called "Hades" hit 37 PyPI wheels and 19 code packages, marking a new evolution of the Shai-Hulud software supply chain worm targeting the Python ecosystem.

### 4. Critical UniFi OS Bug Lets Hackers Gain Root Without Authentication
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/critical-unifi-os-bug-lets-hackers-gain-root-without-authentication/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `privilege-escalation`, `vulnerability`, `cve`
- **Slug:** `unifi-os-critical-rce-chain`
- **Must-know:** no
- **Summary:** Three already-patched Ubiquiti UniFi OS vulnerabilities can be chained for unauthenticated remote code execution with root privileges, meaning partial patching still leaves devices exposed.

### 5. Check Point VPN Zero-Day (CVE-2026-50751) Exploited by Qilin Ransomware Gang
- **Source:** The Hacker News — https://thehackernews.com/2026/06/critical-check-point-vpn-flaw-exploited.html (+ BleepingComputer attribution coverage)
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `zero-day`, `ransomware`
- **Slug:** `check-point-vpn-zero-day-qilin-ransomware`
- **Must-know:** yes
- **Summary:** A critical certificate-validation flaw (CVSS 9.3) in Check Point Remote Access VPN/Mobile Access using IKEv1 lets unauthenticated attackers bypass passwords; Check Point confirmed active zero-day exploitation and linked the attacks to the Qilin ransomware gang. (Merged with a duplicate BleepingComputer story that added the Qilin attribution.)

### 6. Everest Forms Vulnerability Exploited to Hack WordPress Sites
- **Source:** SecurityWeek — https://www.securityweek.com/everest-forms-vulnerability-exploited-to-hack-wordpress-sites/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`, `appsec`
- **Slug:** `everest-forms-wordpress-rce-exploited`
- **Must-know:** no
- **Summary:** A remote code execution flaw in the Everest Forms WordPress plugin has reportedly been exploited in the wild for two months, putting unpatched sites at risk of full compromise.

### 7. 174,000 Impacted by Lansing Community College Data Breach
- **Source:** SecurityWeek — https://www.securityweek.com/174000-impacted-by-lansing-community-college-data-breach/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `lansing-community-college-breach`
- **Must-know:** no
- **Summary:** Lansing Community College disclosed a breach affecting roughly 174,000 people, stemming from unauthorized access to systems back in February 2025. No technical details on the attack vector have surfaced.

### 8. Silent Ransom Group Uses DNS Fast Flux to Hide C2 Infrastructure
- **Source:** SecurityWeek — https://www.securityweek.com/silent-ransom-group-uses-dns-fast-flux-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ransomware`, `malware`
- **Slug:** `silent-ransom-group-dns-fast-flux`
- **Must-know:** no
- **Summary:** The Silent Ransom Group, which focuses on hacking US law firms, is now using DNS fast flux to rotate IPs and conceal its command-and-control infrastructure from takedown efforts.

### 9. VerdantBamboo Deploys BSD Variant of BRICKSTORM Backdoor on Linux Appliances
- **Source:** The Hacker News — https://thehackernews.com/2026/06/verdantbamboo-deploys-bsd-variant-of.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`
- **Slug:** `verdantbamboo-brickstorm-bsd-linux`
- **Must-know:** no
- **Summary:** Volexity attributes a China-nexus espionage cluster, VerdantBamboo (overlapping with Clay Typhoon), to deploying a new BSD variant of the BRICKSTORM backdoor plus two other malware families against Linux appliances.

### 10. OpenAI Rolling Out ChatGPT Account Security Controls
- **Source:** SecurityWeek — https://www.securityweek.com/openai-rolling-out-chatgpt-account-security-controls/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `openai`, `llm`, `appsec`
- **Slug:** `openai-chatgpt-account-security-controls`
- **Must-know:** no
- **Summary:** OpenAI is broadening rollout of "Active Sessions" and "Lockdown Mode" features to give ChatGPT users more visibility and control over account security.

### 11. Anthropic Urges Industry Coordination to Allow for a 'Pause' in AI Development
- **Source:** SecurityWeek — https://www.securityweek.com/anthropic-urges-industry-coordination-to-allow-for-a-pause-in-ai-development-if-risks-grow/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `anthropic`, `ai-safety`, `llm`
- **Slug:** `anthropic-ai-pause-coordination`
- **Must-know:** no
- **Summary:** Anthropic proposed a coordination mechanism that would let advanced AI labs verify whether rivals have actually slowed development, enabling an industry-wide "pause" if frontier-model risks grow too large.

### 12. SolarWinds Serv-U Vulnerability Exploited in the Wild
- **Source:** SecurityWeek — https://www.securityweek.com/solarwinds-patches-exploited-serv-u-vulnerability/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Slug:** `solarwinds-serv-u-vulnerability-exploited`
- **Must-know:** no
- **Summary:** SolarWinds patched a Serv-U flaw that unauthenticated attackers can exploit with crafted POST requests to crash the service; the bug is already being exploited in the wild as a denial-of-service vector.

### 13. UNC3753 Used Vishing and Physical Intrusions in U.S. Data Theft Extortion Campaign
- **Source:** The Hacker News — https://thehackernews.com/2026/06/unc3753-used-vishing-and-physical.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `data-breach`
- **Slug:** `unc3753-vishing-physical-intrusion-extortion`
- **Must-know:** no
- **Summary:** Google Mandiant/GTIG attributed a financially motivated extortion campaign against dozens of US professional, legal, and financial firms to UNC3753, which combined voice phishing with physical on-site intrusions between January and May 2026.

### 14. VS Code Adds 2-Hour Extension Auto-Update Delay to Limit Supply Chain Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/06/vs-code-adds-2-hour-extension-auto.html
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `supply-chain`, `devsecops`, `microsoft`
- **Slug:** `vscode-extension-auto-update-delay`
- **Must-know:** no
- **Summary:** Microsoft will delay automatic VS Code extension updates by two hours after publication, giving the security community a window to flag malicious updates before broad rollout — a direct mitigation for IDE extension supply chain risk.

### 15. Over 20,000 Instagram Accounts Stolen in Meta AI Support Hack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/meta-ai-support-data-breach-affects-20-000-instagram-accounts/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `llm`, `meta`
- **Slug:** `instagram-meta-ai-support-breach`
- **Must-know:** no
- **Summary:** Meta confirmed that 20,225 Instagram accounts were hijacked after attackers abused its AI-powered support system to trigger password resets — a concrete case of an AI workflow becoming the weak point in account recovery.

## Skippable

- **WWDC 2026: Everything announced on Siri AI, iOS 27, Apple Intelligence and more** — TechCrunch AI. Generic Apple product announcement roundup, no security angle.
- **Apple just taught your iPhone to finish your sentences, your photos, and your workflows** — TechCrunch AI. Generic Apple Intelligence feature coverage.
- **Apple will let you build workflows using AI in its new Shortcuts app** — TechCrunch AI. Generic product feature, no security substance.
- **WhatsApp says it disrupted new NSO spyware phishing attacks** — BleepingComputer. Duplicate of the NSO/WhatsApp story; The Hacker News version with the contempt-order detail was selected instead.
- **Apple's Image Playground doesn't suck anymore** — TechCrunch AI. Generic product feature update.
- **Apple's Photos app is getting new AI editing features** — TechCrunch AI. Generic product feature update.
- **Apple gives Siri its own dedicated app** — TechCrunch AI. Generic product announcement.
- **Apple is fixing the headache of splitting the bill with its new Siri in Camera feature** — TechCrunch AI. Generic consumer feature, no security relevance.
- **Apple's long-awaited AI Siri overhaul is finally here** — TechCrunch AI. Generic product launch coverage, duplicate WWDC theme.
- **Amazon is launching AI-generated custom merch** — The Verge AI. Generic consumer product launch, no security angle.
- **Apple announces Siri AI and its next generation of Apple Intelligence** — The Verge AI. Duplicate WWDC/Siri coverage.
- **A Security Raises $37 Million for Autonomous Offensive Security Platform** — SecurityWeek. Funding/stealth-exit announcement with no technical detail about the platform itself.
- **Armenia's pro-Europe party wins election despite Russia-linked disinformation** — The Record. Geopolitical election story; disinformation angle is too thin and regional for this feed.
- **WhatsApp says NSO targeted users with spearfishing attacks in violation of court order** — The Record. Duplicate of the NSO/WhatsApp story already covered via The Hacker News.
- **Operationalizing AWS security: A maturity roadmap** — AWS Security Blog. Generic vendor maturity-model content, marketing-adjacent.
- **NotebookLM's Gemini 3.5 upgrade adds a cloud computer and help finding sources** — The Verge AI. Incremental product update using an existing model, not a new model launch.
- **Amazon now lets you design custom merch using AI** — TechCrunch AI. Duplicate of the Amazon AI merch story.
- **WWDC 2026: What to expect, from Siri's highly anticipated revamp to Apple Intelligence and iOS 27** — TechCrunch AI. Pre-event preview piece, duplicate WWDC theme.
- **Everybody Is Vibe Coding But Nobody Told the Security Team** — SecurityWeek. Opinion/analysis piece without concrete news or technical findings.
- **Russia upgrades rules for its digital spy system to better track citizens online** — The Record. Regional regulatory change to a domestic surveillance system, low practitioner impact.
- **Reducing security operations complexity with Wazuh Cloud** — BleepingComputer. Vendor/sponsored content about a SIEM product.
- **Microsoft's AI chief says superintelligence is near, but won't take your job** — The Verge AI. Interview/opinion piece without concrete news value.
- **WhatsApp Catches Spyware Firm NSO Defying No-Hacking Court Order** — SecurityWeek. Duplicate of the NSO/WhatsApp contempt-order story.
- **AI Phishing Is Crushing SOCs with Alert Volume: How to Reduce Tier 1 Overload** — The Hacker News. Vendor advice/marketing content framed as news, no new incident or technique.
- **⚡ Weekly Recap: Instagram Account Hacks, Android Zero-Day, GitHub Worm and More** — The Hacker News. Roundup of stories already covered individually elsewhere in this window.
- **Check Point links VPN zero-day attacks to Qilin ransomware gang** — BleepingComputer. Duplicate coverage of the Check Point VPN zero-day; its Qilin attribution detail was merged into that draft.
- **Cybersecurity M&A Roundup: 26 Deals Announced in May 2026** — SecurityWeek. Business/deals roundup, no security substance.
- **The Hardest Fork** — The Hacker News. First-person opinion piece musing on AI vulnerability-chaining findings ("Mythos") without disclosing concrete new technical details.
- **Oxford University discloses data breach after careers platform hack** — BleepingComputer. Third-party platform breach with no victim count or technical detail provided.
- **WWDC 2026: How to watch and what to expect** — The Verge AI. Event-viewing guide, no news content.
