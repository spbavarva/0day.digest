# Digest — 2026-05-06 PM

- Window: last 14h
- Raw items considered: 53
- Relevant: 15
- Skippable: 38

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Palo Alto PAN-OS RCE Zero-Day CVE-2026-0300 Actively Exploited — `2026-05-06-palo-alto-pan-os-rce-zero-day-cve-2026-0300.md`
- [x] **[CRITICAL]** DAEMON Tools Supply Chain Attack Hits Government and Scientific Targets — `2026-05-06-daemon-tools-supply-chain-attack.md`
- [x] **[HIGH]** OceanLotus Suspected of Delivering ZiChatBot Malware via PyPI — `2026-05-06-oceanlotus-pypi-zichatbot-malware.md`
- [x] **[HIGH]** MuddyWater Uses Microsoft Teams for False Flag Ransomware Attack — `2026-05-06-muddywater-microsoft-teams-false-flag-ransomware.md`
- [x] **[HIGH]** CloudZ RAT Abuses Windows Phone Link to Steal Credentials and Bypass 2FA — `2026-05-06-cloudz-rat-windows-phone-link-2fa-bypass.md`
- [x] **[HIGH]** APT37 Targets Ethnic Koreans in China with BirdCall Android Malware — `2026-05-07-apt37-birdcall-android-malware.md`
- [x] **[HIGH]** Quasar Linux RAT Targets Software Developers with Evasive Implant — `2026-05-06-quasar-linux-rat-software-developers.md`
- [x] **[HIGH]** UAE Critical Infrastructure Under Escalating Cyber Attack Amid Iran Conflict — `2026-05-06-middle-east-uae-critical-infrastructure-attacks.md`
- [x] **[MEDIUM]** CISA Launches CI Fortify to Harden Critical Infrastructure Against Cyber Conflict — `2026-05-06-cisa-ci-fortify-critical-infrastructure-isolation.md`
- [x] **[MEDIUM]** Google Launches Android Binary Transparency to Block Supply Chain Attacks — `2026-05-06-android-binary-transparency-supply-chain-defense.md`
- [x] **[MEDIUM]** Mira Murati Testifies Sam Altman Lied About AI Model Safety Standards — `2026-05-06-murati-altman-ai-safety-testimony-openai-trial.md`
- [x] **[MEDIUM]** Cisco Crosswork Network Controller DoS Flaw Requires Manual Reboot to Recover — `2026-05-06-cisco-crosswork-dos-flaw-manual-reboot.md`
- [x] **[INFORMATIONAL]** Google Cloud Introduces IAM Framework for Agentic AI Security — `2026-05-06-google-cloud-iam-agentic-ai-security.md`
- [x] **[INFORMATIONAL]** AWS MCP Server Now Generally Available for Authenticated AI Agent Access — `2026-05-06-aws-mcp-server-generally-available.md`
- [x] **[INFORMATIONAL]** Anthropic Holds Code w/ Claude 2026 Developer Event — `2026-05-06-code-with-claude-2026-anthropic-event.md`

## Relevant (details)

### 1. Palo Alto PAN-OS RCE Zero-Day CVE-2026-0300 Actively Exploited
- **Source:** The Hacker News — https://thehackernews.com/2026/05/palo-alto-pan-os-flaw-under-active.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `rce`, `cve`, `vulnerability`
- **Slug:** `2026-05-06-palo-alto-pan-os-rce-zero-day-cve-2026-0300`
- **Must-know:** yes
- **Summary:** CVE-2026-0300, a CVSS 9.3 unauthenticated buffer overflow in the PAN-OS User-ID Authentication Portal, is under active exploitation on PA-Series and VM-Series firewalls. No patch was available at time of publication; Palo Alto recommends disabling internet-facing portal access as interim mitigation.

### 2. DAEMON Tools Supply Chain Attack Hits Government and Scientific Targets
- **Source:** SecurityWeek — https://www.securityweek.com/government-scientific-entities-hit-via-daemon-tools-supply-chain-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`
- **Slug:** `2026-05-06-daemon-tools-supply-chain-attack`
- **Must-know:** yes
- **Summary:** Attackers trojanized DAEMON Tools Lite installers distributed via the official website; Kaspersky discovered the compromise and the developer released a clean version. A sophisticated backdoor was selectively deployed on approximately a dozen government and scientific systems while trojanized versions distributed globally.

### 3. OceanLotus Suspected of Delivering ZiChatBot Malware via PyPI
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/oceanlotus-suspected-pypi-zichatbot-campaign/119603/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `supply-chain`, `pypi`, `malware`
- **Slug:** `2026-05-06-oceanlotus-pypi-zichatbot-malware`
- **Must-know:** no
- **Summary:** Kaspersky GReAT found malicious Python wheel packages in PyPI attributed with moderate confidence to OceanLotus (APT32), carrying a dropper for a new malware strain called ZiChatBot targeting both Windows and Linux. Classic APT supply chain pattern: publish plausible packages with embedded payloads and wait for developer installation.

### 4. MuddyWater Uses Microsoft Teams for False Flag Ransomware Attack
- **Source:** The Hacker News — https://thehackernews.com/2026/05/muddywater-uses-microsoft-teams-to.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`, `phishing`, `malware`, `microsoft`
- **Slug:** `2026-05-06-muddywater-microsoft-teams-false-flag-ransomware`
- **Must-know:** no
- **Summary:** Iranian state actor MuddyWater used Microsoft Teams social engineering for initial access in early 2026, then deployed Chaos ransomware as a false flag while conducting credential harvesting and data exfiltration in the background. Rapid7 documented the full kill chain; the false flag tactic is designed to redirect defenders toward ransomware response while espionage activity completes.

### 5. CloudZ RAT Abuses Windows Phone Link to Steal Credentials and Bypass 2FA
- **Source:** The Hacker News — https://thehackernews.com/2026/05/windows-phone-link-exploited-by-cloudz.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`, `microsoft`, `privilege-escalation`
- **Slug:** `2026-05-06-cloudz-rat-windows-phone-link-2fa-bypass`
- **Must-know:** no
- **Summary:** The CloudZ RAT paired with an undocumented plugin called Pheno abuses Windows Phone Link to bridge PC and smartphone, enabling OTP interception and effective SMS-based 2FA bypass. The technique operates through a legitimate Windows feature, making detection harder than typical credential-stealing approaches.

### 6. APT37 Targets Ethnic Koreans in China with BirdCall Android Malware
- **Source:** The Record (Recorded Future) — https://therecord.media/north-korean-hackers-target-ethnic-koreans-in-china
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Slug:** `2026-05-07-apt37-birdcall-android-malware`
- **Must-know:** no
- **Summary:** ESET attributed an Android surveillance campaign to APT37 (North Korea), using a backdoor called BirdCall embedded in card game apps from a company called Sqgame, targeting ethnic Korean communities in China. Demonstrates continued DPRK interest in surveilling Korean diaspora using trojanized entertainment applications.

### 7. Quasar Linux RAT Targets Software Developers with Evasive Implant
- **Source:** SecurityWeek — https://www.securityweek.com/sophisticated-quasar-linux-rat-targets-software-developers/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `rce`
- **Slug:** `2026-05-06-quasar-linux-rat-software-developers`
- **Must-know:** no
- **Summary:** A sophisticated persistent Linux RAT named Quasar is targeting software developers with remote access, surveillance, and credential exfiltration capabilities, designed to evade detection. Targeting developers is a supply chain precursor: compromised workstations expose source code, signing keys, and internal build infrastructure.

### 8. UAE Critical Infrastructure Under Escalating Cyber Attack Amid Iran Conflict
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/middle-east-cyber-battle-field-broadens-uae
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `geopolitics`, `critical-infrastructure`, `data-breach`
- **Slug:** `2026-05-06-middle-east-uae-critical-infrastructure-attacks`
- **Must-know:** no
- **Summary:** Breach attempts targeting the UAE tripled within weeks as the conflict with Iran escalates, with many attacks aimed at critical infrastructure sectors. Pattern reflects the expanding cyber dimension of the Middle East conflict with adversaries shifting toward energy, utilities, and transportation targets.

### 9. CISA Launches CI Fortify to Harden Critical Infrastructure Against Cyber Conflict
- **Source:** SecurityWeek — https://www.securityweek.com/cisa-critical-infrastructure-must-master-isolation-recovery/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `critical-infrastructure`, `cloud-security`, `devsecops`
- **Slug:** `2026-05-06-cisa-ci-fortify-critical-infrastructure-isolation`
- **Must-know:** no
- **Summary:** CISA launched CI Fortify, asking critical infrastructure operators to build OT environments capable of surviving extended isolation from third-party dependencies and operating without reliable internet connectivity. The program emphasizes resilience and recovery testing over pure perimeter defense.

### 10. Google Launches Android Binary Transparency to Block Supply Chain Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/05/android-apps-get-public-verification.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `supply-chain`, `google`
- **Slug:** `2026-05-06-android-binary-transparency-supply-chain-defense`
- **Must-know:** no
- **Summary:** Google expanded Binary Transparency for Android with a public append-only ledger verifying that Google apps on devices exactly match what Google built and distributed. Builds on Pixel Binary Transparency (2021) and provides an auditable chain of custody to detect tampered or substituted app binaries.

### 11. Mira Murati Testifies Sam Altman Lied About AI Model Safety Standards
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/925338/openai-musk-v-altman-mira-murati
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `openai`, `ai-safety`, `llm`
- **Slug:** `2026-05-06-murati-altman-ai-safety-testimony-openai-trial`
- **Must-know:** no
- **Summary:** OpenAI's former CTO Mira Murati testified under oath in the Musk v. Altman trial that CEO Sam Altman falsely told her the legal department had cleared a new AI model on safety grounds. Raises significant questions about the reliability of executive communications around internal AI safety review processes at OpenAI.

### 12. Cisco Crosswork Network Controller DoS Flaw Requires Manual Reboot to Recover
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-cisco-dos-flaw-requires-manual-reboot-to-revive-devices/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`
- **Slug:** `2026-05-06-cisco-crosswork-dos-flaw-manual-reboot`
- **Must-know:** no
- **Summary:** Cisco patched a DoS vulnerability in Crosswork Network Controller and Network Services Orchestrator that crashes affected devices and requires manual physical or console reboot for recovery. Particularly disruptive in large-scale network automation environments where these platforms manage many devices.

### 13. Google Cloud Introduces IAM Framework for Agentic AI Security
- **Source:** Google Cloud Security — https://cloud.google.com/blog/products/identity-security/whats-new-in-iam-security-governance-and-runtime-defense/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `iam`, `cloud-security`, `google`, `gcp`, `llm`
- **Slug:** `2026-05-06-google-cloud-iam-agentic-ai-security`
- **Must-know:** no
- **Summary:** Google Cloud introduced a new IAM security and governance framework for AI agents, with foundational Agent Identity concepts and runtime access governance unveiled at Google Cloud Next. Addresses the gap between traditional IAM controls and the needs of autonomous agents operating at machine speed on sensitive resources.

### 14. AWS MCP Server Now Generally Available for Authenticated AI Agent Access
- **Source:** AWS News Blog — https://aws.amazon.com/blogs/aws/the-aws-mcp-server-is-now-generally-available/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `aws`, `cloud-security`, `llm`
- **Slug:** `2026-05-06-aws-mcp-server-generally-available`
- **Must-know:** no
- **Summary:** AWS released the AWS MCP Server as generally available, a managed remote Model Context Protocol server providing AI agents with authenticated access to all AWS services. Practitioners should evaluate credential scoping, token storage, and audit logging of agent actions when adopting MCP-based AWS integrations.

### 15. Anthropic Holds Code w/ Claude 2026 Developer Event
- **Source:** Simon Willison — https://simonwillison.net/2026/May/6/code-w-claude-2026/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `anthropic`, `claude`, `llm`
- **Slug:** `2026-05-06-code-with-claude-2026-anthropic-event`
- **Must-know:** no
- **Summary:** Anthropic held its Code w/ Claude 2026 developer event focused on Claude Code and agentic development, with Simon Willison live-blogging the keynote and sessions. Announcements expected around Claude API capabilities and agentic workflow tooling.

## Skippable

- **New CISA initiative aims for critical infrastructure to operate offline during cyberattacks** — The Record. Duplicate; covered under SecurityWeek's CI Fortify item with more technical detail.
- **DAEMON Tools devs confirm breach, release malware-free version** — BleepingComputer. Duplicate; covered under SecurityWeek's government/scientific entities item.
- **MuddyWater hackers use Chaos ransomware as a decoy in attacks** — BleepingComputer. Duplicate of MuddyWater story; The Hacker News version selected for fuller kill chain detail.
- **Iranian APT Intrusion Masquerades as Chaos Ransomware Attack** — SecurityWeek. Duplicate of MuddyWater story; The Hacker News version selected.
- **Hackers compromise Daemon Tools in global supply-chain attack, researchers say** — The Record. Duplicate of DAEMON Tools supply chain item; SecurityWeek version selected.
- **Attacks Abuse Windows Phone Link to Steal Texts & Bypass 2FA** — Dark Reading. Duplicate of CloudZ RAT story; The Hacker News version selected.
- **Palo Alto Networks warns of firewall RCE zero-day exploited in attacks** — BleepingComputer. Duplicate of PAN-OS CVE-2026-0300; The Hacker News version selected.
- **Palo Alto Networks to Patch Zero-Day Exploited to Hack Firewalls** — SecurityWeek. Duplicate of PAN-OS CVE-2026-0300; The Hacker News version selected.
- **SpaceX may spend up to $119B on 'Terafab' chip factory in Texas** — TechCrunch AI. Semiconductor manufacturing/business news, no security angle.
- **DeepSeek could hit $45B valuation from its first investment round** — TechCrunch AI. Financial/business news, no technical security content.
- **Google named a Leader in the 2026 Gartner® Magic Quadrant™ for Cyberthreat Intelligence Technologies** — Google Cloud Security. Vendor marketing/analyst recognition content.
- **5 gardening tips you can try right in Search** — Google AI Blog. No security or AI substance.
- **Google updates AI search to include quotes from Reddit and other sources** — TechCrunch AI. Consumer search product feature, no security angle.
- **Khosla-backed robotics startup Genesis AI has gone full stack, demo shows** — TechCrunch AI. Non-security AI product launch.
- **Tinder owner Match Group is slowing hiring to pay for its increased use of AI tools** — TechCrunch AI. Business/labor news, no security angle.
- **2026 Gartner® Magic Quadrant™ for Cyber Threat Intelligence: Key Takeaways for Security Leaders** — Flashpoint. Vendor marketing/analyst recognition content.
- **Apple to pay $250M to settle lawsuit over Siri's delayed AI features** — TechCrunch AI. Consumer legal settlement, no security implications.
- **Ethos raises $22.75M from a16z for its expert network with voice onboarding** — TechCrunch AI. Generic startup funding, no security angle.
- **Autonomous Offensive Security Firm XBOW Raises $35 Million** — SecurityWeek. Funding round announcement only, no technical content.
- **At TechCrunch Disrupt 2026, all your M&A questions will be answered** — TechCrunch AI. Event promotional content.
- **Vibe coding and agentic engineering are getting closer than I'd like** — Simon Willison. Opinion/reflection piece, no specific news event.
- **Why ransomware attacks succeed even when backups exist** — BleepingComputer. Acronis-sponsored vendor content disguised as analysis.
- **3 days left to lock in 50% off a second ticket to TechCrunch Disrupt 2026** — TechCrunch AI. Promotional/advertising content.
- **AI boom pushes Samsung to $1T** — TechCrunch AI. Financial/business news, no security angle.
- **Herd Security Raises $3 Million for AI-Powered Training Platform** — SecurityWeek. Minor startup funding, no technical content.
- **Google's AI search summaries will now quote Reddit** — The Verge AI. Consumer search product feature, no security angle.
- **Microsoft's Office and LinkedIn chief now runs Teams in latest reshuffle** — The Verge AI. Corporate leadership news, no security content.
- **Your AI Agents Are Already Inside the Perimeter. Do You Know What They're Doing?** — The Hacker News. Promotional piece with Gartner analyst access request embedded; marketing content.
- **Webinar: Why network incidents escalate and how to fix response gaps** — BleepingComputer. Webinar promotional content.
- **Insights into the clustering and reuse of phone numbers in scam emails** — Cisco Talos. Interesting threat intel research but limited immediate practitioner actionability.
- **Websites with an undefined trust level: avoiding the trap** — Securelist. General security awareness content, no specific news event.
- **Chrome's AI features may be hogging 4GB of your computer storage** — The Verge AI. Storage/UX issue; no active security threat.
- **The Hacker News Launches 'Cybersecurity Stars Awards 2026'** — The Hacker News. Industry awards announcement.
- **From Stuxnet to ChatGPT: 20 News Events That Shaped Cyber** — Dark Reading. 20th anniversary retrospective/opinion piece.
- **Romanian Man Extradited to US for Role in Hacking Scheme 17 Years Ago** — SecurityWeek. Historical arrest from 2017 indictment, minimal current relevance.
- **Peter Sarlin's QuTwo reaches $380M valuation in angel round** — TechCrunch AI. Quantum/AI startup funding, business news.
- **Marc Lore says that AI will soon enable anyone to open a restaurant** — TechCrunch AI. Business news, no security angle.
- **Oracle Debuts Monthly Critical Security Patch Updates** — SecurityWeek. Patching cadence policy change; no specific CVE to act on immediately.
