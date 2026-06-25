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
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `malware`, `appsec`, `windows`
- **Slug:** `cisco-talos-com-windows-threat-abuse`
- **Must-know:** no
- **Summary:** Talos research details how threat actors abuse the Windows COM framework — used legitimately for object activation and automation — to blend execution and persistence into normal-looking system activity. Signature-based EDR can miss this since no known-bad binary is involved.

### 2. Chrome 149 Patches 18 Severe Vulnerabilities, Majority Use-After-Free
- **Source:** SecurityWeek — https://www.securityweek.com/chrome-149-update-resolves-18-severe-vulnerabilities/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `chrome-149-resolves-18-severe-vulnerabilities`
- **Must-know:** no
- **Summary:** Chrome 149 fixes 18 severe-severity bugs, over half of them use-after-free defects that can potentially be chained into RCE. No active exploitation reported; users should update to the latest stable build.

### 3. Mandiant: Cisco SD-WAN Zero-Day Exploited via Rogue Peering Two Months Before Patch
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cisco-catalyst-sd-wan-zero-day-cve-2026.html (also covered by BleepingComputer, Dark Reading, SecurityWeek)
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `privilege-escalation`, `rce`, `vulnerability`, `cve`
- **Slug:** `cisco-sdwan-mandiant-rogue-peering-root`
- **Must-know:** no
- **Summary:** Mandiant found CVE-2026-20245 (CVSS 7.8) in Cisco Catalyst SD-WAN was exploited via rogue peering roughly two months before public disclosure, with attackers creating rogue root accounts. This is a follow-up with new technical detail on a flaw already covered as a critical must-know item on 2026-06-05; severity/must-know are not re-escalated here since it's additive detail, not a new disclosure.

### 4. 'Edgecution' Malicious Edge Extension Uses Native Messaging to Escape Browser Sandbox
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/malicious-edge-extension-abuses-native-messaging-as-bridge-to-malware/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `ransomware`, `appsec`
- **Slug:** `edgecution-malicious-edge-extension-native-messaging`
- **Must-know:** no
- **Summary:** A malicious Edge extension named Edgecution abused the Native Messaging API to bridge out of the browser sandbox to a Python backdoor, which was used to deploy ransomware. The technique can evade defenses that only inspect extension permissions.

## Skippable

- **Inside the 2026 SMB threat landscape: From phishing and scams to fake AI tools** — Securelist (Kaspersky GReAT). Broad annual threat-landscape survey, no single new technique or actionable detail.
- **Europe Evolves Into Ransomware's Favorite Region** — Dark Reading. Regional trend/analysis piece, not a specific incident or new TTP.
- **25-Year-Old Vulnerability Patched in Curl** — SecurityWeek. 18 medium/low-severity fixes, none critical or exploited.
- **Facebook's Creator Studio has been revived as an AI companion app** — The Verge AI. Consumer feature relaunch, no security or frontier-model angle.
- **New Mistic Backdoor Linked to KongTuke in ClickFix and ModeloRAT Campaigns** — The Hacker News. Duplicate coverage of the Mistic/MLTBackdoor malware already published 2026-06-24 (`2026-06-24-mistic-rat-ransomware-access-broker.md`), different vendor naming for the same family.
- **NIST Opens Updated IoT Security Guidance to Public Review** — SecurityWeek. Draft guidance open for comment, no immediate practitioner action.
- **Cisco SD-WAN Zero-Day Exploited Months Before Patching** — SecurityWeek. Duplicate of the Mandiant Cisco SD-WAN story (see Relevant #3); folded into that post.
- **How agents are transforming work** — OpenAI Blog. General productivity research post, no new model release or security substance.
- **Europe is pushing back on Washington's chip war** — TechCrunch AI. Geopolitical commentary/quotes, no concrete new policy action.
- **simonw/browser-compat-db** — Simon Willison. Personal side-project tooling post, not a security or major AI development story.
- **Google releases new privacy controls for activity history, personalization** — BleepingComputer. Consumer privacy settings update, not a vulnerability or incident.
- **Former Infosys chief has a new startup that wants to challenge the IT services world** — TechCrunch AI. Startup/funding news, no security or model substance.
- **Cerebras stock plunges after earnings as CEO says margin outlook was misunderstood** — TechCrunch AI. Financial/market news.
- **AI was supposed to kill engineering jobs, but new data suggests they're the most resilient** — TechCrunch AI. Labor-market analysis, no security angle.
- **DraftKings hacker 'Snoopy' sentenced to 18 months in prison** — BleepingComputer. Sentencing news for a 2022 incident, no new technical detail.
- **AI researchers continue to leave Google for its rivals** — TechCrunch AI. Personnel/talent-movement story, not a model launch or safety incident.
- **The memory chip crunch is paying off for this US company** — TechCrunch AI. Financial/earnings news, no security or model substance.
- **Mandiant reveals how Cisco SD-WAN zero-day attacks gained root access** — BleepingComputer. Duplicate of the Mandiant Cisco SD-WAN story (see Relevant #3); folded into that post.
- **Attackers Hit Cisco SD-WAN Flaw 2 Months Before Disclosure** — Dark Reading. Duplicate of the Mandiant Cisco SD-WAN story (see Relevant #3); folded into that post.
- **2026 FIFA World Cup Faces Surge in Cyber Threats** — Dark Reading. Generic threat-landscape overview, no new technical detail; World Cup security already covered 2026-06-18.
