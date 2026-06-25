# Digest — 2026-06-25 AM

- Window: last 14h
- Raw items considered: 24
- Relevant: 4
- Skippable: 20

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[MEDIUM]** Cisco Talos: How Windows Threats Abuse COM for Stealth and Persistence — `2026-06-25-cisco-talos-com-windows-threat-abuse.md`
- [x] **[HIGH]** Chrome 149 Patches 18 Severe Vulnerabilities, Majority Use-After-Free — `2026-06-25-chrome-149-resolves-18-severe-vulnerabilities.md`
- [x] **[HIGH]** Mandiant: Cisco SD-WAN Zero-Day Exploited via Rogue Peering Two Months Before Patch — `2026-06-25-cisco-sdwan-mandiant-rogue-peering-root.md`
- [x] **[HIGH]** 'Edgecution' Malicious Edge Extension Uses Native Messaging to Escape Browser Sandbox — `2026-06-25-edgecution-malicious-edge-extension-native-messaging.md`

## Relevant (details)

### 1. Cisco Talos: How Windows Threats Abuse COM for Stealth and Persistence
- **Source:** Cisco Talos — https://blog.talosintelligence.com/introduction-to-com-usage-by-windows-threats/
- **Severity:** medium
- **Tags:** `malware`, `appsec`
- **Summary:** Talos research details how threat actors abuse the Windows COM framework to blend execution and persistence into normal-looking system activity, evading signature-based EDR.

### 2. Chrome 149 Patches 18 Severe Vulnerabilities, Majority Use-After-Free
- **Source:** SecurityWeek — https://www.securityweek.com/chrome-149-update-resolves-18-severe-vulnerabilities/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Summary:** Chrome 149 fixes 18 severe bugs, over half use-after-free defects that can potentially chain into RCE. No active exploitation reported.

### 3. Mandiant: Cisco SD-WAN Zero-Day Exploited via Rogue Peering Two Months Before Patch
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cisco-catalyst-sd-wan-zero-day-cve-2026.html
- **Severity:** high
- **Tags:** `zero-day`, `privilege-escalation`
- **Summary:** Mandiant found CVE-2026-20245 (CVSS 7.8) was exploited via rogue peering ~2 months before disclosure, with attackers creating rogue root accounts. New technical detail on a flaw already published as critical/must-know on 2026-06-05.

### 4. 'Edgecution' Malicious Edge Extension Uses Native Messaging to Escape Browser Sandbox
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/malicious-edge-extension-abuses-native-messaging-as-bridge-to-malware/
- **Severity:** high
- **Tags:** `malware`, `ransomware`
- **Summary:** A malicious Edge extension abused the Native Messaging API to escape the browser sandbox to a Python backdoor, used to deploy ransomware.

## Skippable

- **Inside the 2026 SMB threat landscape: From phishing and scams to fake AI tools** — Securelist. Broad annual survey, no specific new technique.
- **Europe Evolves Into Ransomware's Favorite Region** — Dark Reading. Regional trend piece, not a specific incident.
- **25-Year-Old Vulnerability Patched in Curl** — SecurityWeek. Only medium/low-severity fixes.
- **Facebook's Creator Studio has been revived as an AI companion app** — The Verge AI. Consumer feature relaunch, no security angle.
- **New Mistic Backdoor Linked to KongTuke in ClickFix and ModeloRAT Campaigns** — The Hacker News. Duplicate of the Mistic backdoor story already published 2026-06-24.
- **NIST Opens Updated IoT Security Guidance to Public Review** — SecurityWeek. Draft guidance, no immediate action.
- **Cisco SD-WAN Zero-Day Exploited Months Before Patching** — SecurityWeek. Duplicate, folded into Relevant #3.
- **How agents are transforming work** — OpenAI Blog. Productivity research post, no new model/security substance.
- **Europe is pushing back on Washington's chip war** — TechCrunch AI. Geopolitical commentary, no concrete new policy action.
- **simonw/browser-compat-db** — Simon Willison. Personal side-project tooling post.
- **Google releases new privacy controls for activity history, personalization** — BleepingComputer. Consumer privacy settings update, not a vulnerability/incident.
- **Former Infosys chief has a new startup that wants to challenge the IT services world** — TechCrunch AI. Startup/funding news.
- **Cerebras stock plunges after earnings as CEO says margin outlook was misunderstood** — TechCrunch AI. Financial/market news.
- **AI was supposed to kill engineering jobs, but new data suggests they're the most resilient** — TechCrunch AI. Labor-market analysis.
- **DraftKings hacker 'Snoopy' sentenced to 18 months in prison** — BleepingComputer. Sentencing news for a 2022 incident.
- **AI researchers continue to leave Google for its rivals** — TechCrunch AI. Personnel/talent-movement story.
- **The memory chip crunch is paying off for this US company** — TechCrunch AI. Financial/earnings news.
- **Mandiant reveals how Cisco SD-WAN zero-day attacks gained root access** — BleepingComputer. Duplicate, folded into Relevant #3.
- **Attackers Hit Cisco SD-WAN Flaw 2 Months Before Disclosure** — Dark Reading. Duplicate, folded into Relevant #3.
- **2026 FIFA World Cup Faces Surge in Cyber Threats** — Dark Reading. Generic overview; World Cup security already covered 2026-06-18.
