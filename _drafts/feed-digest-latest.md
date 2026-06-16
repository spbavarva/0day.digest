# Digest — 2026-06-15 PM

- Window: last 14h
- Raw items considered: 32
- Relevant: 7
- Skippable: 25

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** SimpleHelp Flaw Lets Unauthenticated Attackers Create Rogue Technician Accounts — `2026-06-15-simplehelp-oidc-rogue-technician-accounts.md`
- [x] **[HIGH]** North Korean Hackers Use Fake Developer Recruitment to Deliver Malware — `2026-06-15-north-korea-developer-recruitment-malware-contagious-interview.md`
- [x] **[CRITICAL]** Cisco Patches SD-WAN vManage Zero-Day Exploited for Root Privilege Escalation — `2026-06-15-cisco-sdwan-vmanage-zero-day-root-privilege-escalation.md`
- [x] **[HIGH]** LiteLLM Vulnerability Chain Lets Low-Privilege Users Take Over AI Gateway Servers — `2026-06-15-litellm-vulnerability-chain-ai-gateway-takeover.md`
- [x] **[MEDIUM]** Cybersecurity Experts Urge White House to Reverse Export Ban on Anthropic's Fable and Mythos Models — `2026-06-15-cybersecurity-experts-protest-anthropic-fable-mythos-export-ban.md`
- [x] **[HIGH]** SearchLeak: One-Click Flaw Chain in Microsoft 365 Copilot Enabled Mail and File Exfiltration — `2026-06-15-m365-copilot-searchleak-one-click-data-exfiltration.md`
- [x] **[HIGH]** China-Linked Group Exploits Exposed REDCap Servers to Deploy InfiniteRed Malware — `2026-06-15-china-nexus-redcap-infinitered-malware-medical-research.md`

## Relevant (details)

### 1. SimpleHelp Flaw Lets Unauthenticated Attackers Create Rogue Technician Accounts
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/simplehelp-bug-lets-hackers-create-rogue-remote-support-accounts/
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`, `appsec`
- **Summary:** A vulnerability in SimpleHelp's remote support software lets unauthenticated attackers create privileged technician accounts via its OIDC authentication flow. These rogue accounts grant full remote-access capabilities over any endpoint managed through the affected instance.

### 2. North Korean Hackers Use Fake Developer Recruitment to Deliver Malware
- **Source:** The Hacker News — https://thehackernews.com/2026/06/north-korean-hackers-are-turning.html
- **Severity:** high
- **Tags:** `malware`, `phishing`, `supply-chain`
- **Summary:** Proofpoint linked two new campaigns to the Contagious Interview cluster (aka Famous Chollima, HexagonalRodent, Void Dokkaebi), which uses fake developer recruitment and code-review lures to deliver malware. Targets are tricked into running malicious code samples disguised as interview tasks.

### 3. Cisco Patches SD-WAN vManage Zero-Day Exploited for Root Privilege Escalation
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisco-fixes-sd-wan-vmanage-flaw-exploited-in-zero-day-attacks/
- **Severity:** critical
- **Tags:** `zero-day`, `privilege-escalation`, `vulnerability`, `cve`
- **Summary:** Cisco patched CVE-2026-20262, a directory traversal flaw in Catalyst SD-WAN Manager exploited in the wild to gain root. CISA added it to the KEV catalog alongside CVE-2026-54420, a LiteSpeed cPanel symlink-following flaw.

### 4. LiteLLM Vulnerability Chain Lets Low-Privilege Users Take Over AI Gateway Servers
- **Source:** The Hacker News — https://thehackernews.com/2026/06/litellm-vulnerability-chain-lets-low.html
- **Severity:** high
- **Tags:** `llm`, `privilege-escalation`, `rce`, `vulnerability`
- **Summary:** Obsidian Security found that a default low-privilege account on a LiteLLM proxy can chain three bugs to reach full admin and remote code execution. A takeover would expose every provider API key the gateway holds across 100+ model providers.

### 5. Cybersecurity Experts Urge White House to Reverse Export Ban on Anthropic's Fable and Mythos Models
- **Source:** TechCrunch — https://techcrunch.com/2026/06/15/cybersecurity-vets-protest-dangerous-us-government-ban-on-anthropics-most-powerful-models/
- **Severity:** medium
- **Tags:** `anthropic`, `llm`, `ai-safety`, `ai-regulation`
- **Summary:** Dozens of cybersecurity experts urged the White House to lift export controls that forced Anthropic to take Fable 5 and Mythos 5 offline worldwide. The group argues the ban hampers defenders who rely on the models to secure their own software.

### 6. SearchLeak: One-Click Flaw Chain in Microsoft 365 Copilot Enabled Mail and File Exfiltration
- **Source:** The Hacker News — https://thehackernews.com/2026/06/one-click-microsoft-365-copilot-flaw.html
- **Severity:** high
- **Tags:** `llm`, `vulnerability`, `microsoft`, `appsec`
- **Summary:** Varonis Threat Labs chained three bugs in Microsoft 365 Copilot Enterprise Search into SearchLeak, a one-click attack exfiltrating mail, files, and MFA codes via a link on a legitimate microsoft.com domain. The legitimate domain let the link bypass anti-phishing filters.

### 7. China-Linked Group Exploits Exposed REDCap Servers to Deploy InfiniteRed Malware
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/chinese-hackers-breach-redcap-servers-steal-medical-research/
- **Severity:** high
- **Tags:** `malware`, `data-breach`
- **Summary:** A China-linked group exploited exposed REDCap research-data servers to deploy InfiniteRed malware and steal data from a North American medical research institution. Google's Threat Intelligence Group disrupted the broader campaign, which had stolen REDCap credentials from numerous institutions over roughly a year.

## Skippable

- **All the news about Anthropic's new AI fight with the White House** — The Verge AI. Link-roundup of the ongoing Fable/Mythos export-ban story; the new cybersecurity-community angle is covered separately above.
- **Meta's new 'AI Mode' on Facebook pulls from public info across its platforms** — TechCrunch AI. Consumer feature rollout with no security angle.
- **SpaceX is public: Everything you need to know post-IPO** — TechCrunch AI. Off-topic business/IPO coverage, no AI or security substance.
- **Trump's Anthropic shutdown just made the case for non-American AI** — The Verge AI. Opinion/analysis piece on the already-covered Fable/Mythos export ban story.
- **Big Tech's desperate last push at AI regulation** — The Verge AI. General policy/lobbying commentary on federal AI preemption, no specific new action.
- **OptinMonster WordPress plugin hacked in CDN supply-chain attack** — BleepingComputer. Duplicate of the PushEngage/OptinMonster/TrustPulse supply-chain story already published today via The Hacker News.
- **China-Nexus Actor Spy on US Researchers Undetected for a Year** — Dark Reading. Duplicate coverage of the REDCap/China-nexus espionage campaign; covered via BleepingComputer above.
- **Most CISOs Report Pressure to Bury Bad Security News** — Dark Reading. Industry survey/opinion piece, no specific incident or technical detail.
- **Council of Europe investigates ShinyHunters data breach claims** — BleepingComputer. Duplicate of the ShinyHunters/Council of Europe story already published today via SecurityWeek.
- **Cloud CISO Perspectives: The 4 lessons that guided AI Threat Defense** — Google Cloud Security. Vendor newsletter/thought-leadership piece with promotional framing, no concrete new findings.
- **FBI: Fraudsters use couriers to steal money in crypto scams** — BleepingComputer. FBI warning without new IOCs or technical guidance.
- **Ransomware Attack Shuts Down Mills of Australia's Second-Largest Sugar Producer** — SecurityWeek. Ransomware victim disclosure without TTPs or IOCs.
- **The Beginning of the End of Social Engineering** — Dark Reading. Opinion/analysis piece on AI and social engineering, no specific news event.
- **We're strengthening our presence in Alabama through new investments and community support** — Google AI Blog. Data center investment/community PR announcement, no model or security substance.
- **"They screwed us": Personality clashes sent Anthropic's models offline** — Simon Willison. Gossip/behind-the-scenes commentary on the already-covered Fable/Mythos export ban story.
- **Salesforce acquires AI customer service platform Fin for $3.6 billion** — TechCrunch AI. M&A/business news without security or technical substance.
- **Chinese Hackers Target Medical, Military, and AI Research in North America** — SecurityWeek. Duplicate coverage of the REDCap/China-nexus espionage campaign; covered via BleepingComputer above.
- **Vibe coders are gonna vibe code: How CISOs are tackling code sprawl** — BleepingComputer. Sponsored/Tines-authored content with marketing framing.
- **Skydio CEO Adam Bry on why Silicon Valley shouldn't draw red lines for drone use** — The Verge AI. Podcast interview/opinion piece, no news event.
- **⚡ Weekly Recap: Chrome 0-Day, UniFi Exploits, macOS Stealers, VPN Flaw and More** — The Hacker News. Weekly roundup of stories covered individually elsewhere.
- **Sarvam becomes India's newest AI unicorn with $234 million funding round led by HCLTech** — TechCrunch AI. Funding announcement without technical or security substance.
- **New attack turned Microsoft 365 Copilot into 1-click data theft tool** — BleepingComputer. Duplicate of the SearchLeak/M365 Copilot story already covered via The Hacker News above.
- **NewCore Emerges From Stealth Mode With $66 Million in Funding** — SecurityWeek. Startup funding announcement without technical product detail; duplicate of TechCrunch coverage below.
- **As AI agents become employees, NewCore emerges with $66M to give them identities** — TechCrunch AI. Startup funding announcement without technical product detail.
- **CISA Adds Two Known Exploited Vulnerabilities to Catalog** — CISA Alerts. CVE-2026-20262 (Cisco SD-WAN) is covered separately above; CVE-2026-54420 (LiteSpeed cPanel symlink) has no further detail beyond the catalog addition.
