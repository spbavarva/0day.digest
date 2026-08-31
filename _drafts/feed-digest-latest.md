# Digest — 2026-08-31 PM

- Window: last 14h
- Raw items considered: 33
- Relevant: 12
- Skippable: 21

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[MEDIUM]** Threat Group Drops 'HardBreacher' Exploit for Kaspersky Endpoint Security — `2026-08-31-kaspersky-hardbreacher-exploit.md`
- [x] **[HIGH]** ServiceNow Patches Three Critical Code Injection Vulnerabilities — `2026-08-31-servicenow-critical-code-injection-vulns.md`
- [x] **[INFORMATIONAL]** ChatGPT Now Classified as Very Large Online Search Engine Under EU DSA — `2026-08-31-chatgpt-eu-dsa-regulation.md`
- [x] **[CRITICAL]** McKesson Confirms Data Breach as ShinyHunters Deadline Looms — `2026-08-31-mckesson-data-breach-shinyhunters.md`
- [x] **[MEDIUM]** ValleyRAT Backdoor Hides Inside Signed Adware to Evade Antivirus Exclusions — `2026-08-31-valleyrat-backdoor-signed-adware.md`
- [x] **[HIGH]** Anthropic Warns Claude Users of Infostealer Malware Infections — `2026-08-31-anthropic-claude-infostealer-warning.md`
- [x] **[HIGH]** Aurora Ransomware Operators Used Cursor AI Coding Assistant in Attacks on 10 Targets — `2026-08-31-aurora-ransomware-cursor-ai.md`
- [x] **[INFORMATIONAL]** Anthropic Ships Compliance API and Identity Governance Tools for Claude Code — `2026-08-31-securing-claude-code-compliance-api.md`
- [x] **[CRITICAL]** Critical Ruby on Rails Flaw 'KindaRails2Shell' Actively Targeted by Attackers — `2026-08-31-rails-kindarails2shell-rce.md`
- [x] **[HIGH]** 'Spring Ring' Voice Phishing Campaign Abuses Microsoft Teams to Target Domain Controllers — `2026-08-31-spring-ring-teams-voice-phishing.md`
- [x] **[INFORMATIONAL]** Judge Rules Pentagon's Measures Against Anthropic Were 'Illegal and Baseless' — `2026-08-31-pentagon-anthropic-ruling-illegal.md`
- [x] **[HIGH]** China-Linked Fire Ant Expands Campaign to Hijack Cisco Routers and Blind Security Logs — `2026-08-31-fire-ant-cisco-router-hijack.md`

## Relevant (details)

### 1. Threat Group Drops 'HardBreacher' Exploit for Kaspersky Endpoint Security
- **Source:** SecurityWeek — https://www.securityweek.com/nightmare-eclipse-drops-hardbreacher-kaspersky-product-exploit/
- **Severity:** medium
- **Tags:** `vulnerability`
- **Summary:** A group tracked as Nightmare Eclipse released an exploit dubbed "HardBreacher" against Kaspersky's Endpoint Security product. Kaspersky told SecurityWeek the underlying vulnerability has already been patched.

### 2. ServiceNow Patches Three Critical Code Injection Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/servicenow-patches-3-critical-code-injection-vulnerabilities/
- **Severity:** high
- **Tags:** `vulnerability`, `rce`
- **Summary:** ServiceNow patched three critical code injection flaws that could let attackers execute arbitrary code or access and tamper with data. No CVE identifiers or exploitation status were disclosed.

### 3. ChatGPT Now Classified as Very Large Online Search Engine Under EU DSA
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/986682/openai-chatgpt-eu-dsa
- **Severity:** informational
- **Tags:** `llm`, `openai`
- **Summary:** The EU designated ChatGPT a "Very Large Online Search Engine" under the Digital Services Act, subjecting OpenAI to new obligations around minor safety, mental health impact, and illegal content spread.

### 4. McKesson Confirms Data Breach as ShinyHunters Deadline Looms
- **Source:** SecurityWeek — https://www.securityweek.com/mckesson-confirms-data-breach-as-attacker-deadline-looms/
- **Severity:** critical
- **Tags:** `data-breach`
- **Summary:** McKesson confirmed a breach after the ShinyHunters extortion group claimed theft of 284 million records, with an extortion deadline approaching. No details on affected data types or initial access vector yet.

### 5. ValleyRAT Backdoor Hides Inside Signed Adware to Evade Antivirus Exclusions
- **Source:** The Hacker News — https://thehackernews.com/2026/08/valleyrat-backdoor-hides-in-signed.html
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** The Silver Fox actor is distributing the ValleyRAT backdoor disguised as signed Chinese adware built around the QN Wallpaper tool, running under a trusted process to slip past AV exclusion lists.

### 6. Anthropic Warns Claude Users of Infostealer Malware Infections
- **Source:** SecurityWeek — https://www.securityweek.com/anthropic-warns-claude-users-of-infostealer-malware-infections/
- **Severity:** high
- **Tags:** `anthropic`, `malware`, `llm`
- **Summary:** Anthropic is logging out Claude accounts and removing stored payment data for users whose devices show signs of infostealer malware, which can harvest session tokens and credentials for account takeover.

### 7. Aurora Ransomware Operators Used Cursor AI Coding Assistant in Attacks on 10 Targets
- **Source:** The Hacker News — https://thehackernews.com/2026/08/aurora-ransomware-operators-use-cursor.html
- **Severity:** high
- **Tags:** `ransomware`, `ai-safety`
- **Summary:** CloudSEK and Gambit Security separately found that actors linked to the Aurora ransomware operation used the Cursor AI coding assistant to help breach at least 10 targets, based on exposed infrastructure tied to the group.

### 8. Anthropic Ships Compliance API and Identity Governance Tools for Claude Code
- **Source:** The Hacker News — https://thehackernews.com/2026/08/securing-claude-code-new-compliance-api.html
- **Severity:** informational
- **Tags:** `anthropic`, `devsecops`, `iam`
- **Summary:** Anthropic released Compliance API endpoints and local visibility tooling to help security teams monitor Claude Code activity, though the report notes activity logs alone can't confirm whether an agent's access is legitimate.

### 9. Critical Ruby on Rails Flaw 'KindaRails2Shell' Actively Targeted by Attackers
- **Source:** SecurityWeek — https://www.securityweek.com/critical-ruby-on-rails-vulnerability-in-attackers-crosshairs/
- **Severity:** critical
- **Tags:** `vulnerability`, `rce`
- **Summary:** A critical Ruby on Rails arbitrary file read vulnerability dubbed KindaRails2Shell, which allows secret extraction and remote code execution, is reportedly being targeted by attackers. No CVE ID or patch status was given.

### 10. 'Spring Ring' Voice Phishing Campaign Abuses Microsoft Teams to Target Domain Controllers
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/
- **Severity:** high
- **Tags:** `phishing`, `malware`
- **Summary:** Unit 42 detailed "Spring Ring," a campaign combining voice phishing with Microsoft Teams abuse to deploy malware and pivot to enterprise domain controllers after initial access.

### 11. Judge Rules Pentagon's Measures Against Anthropic Were 'Illegal and Baseless'
- **Source:** SecurityWeek — https://www.securityweek.com/judge-says-pentagons-measures-against-anthropic-were-illegal-and-baseless/
- **Severity:** informational
- **Tags:** `anthropic`
- **Summary:** A judge ruled the Pentagon's measures against Anthropic "illegal and baseless," a setback for the government in its dispute after labeling the company a supply chain risk earlier this year.

### 12. China-Linked Fire Ant Expands Campaign to Hijack Cisco Routers and Blind Security Logs
- **Source:** The Hacker News — https://thehackernews.com/2026/08/china-linked-fire-ant-hijacks-cisco.html
- **Severity:** high
- **Tags:** `malware`, `privilege-escalation`
- **Summary:** Sygnia found that China-nexus actor Fire Ant expanded beyond VMware hypervisors to compromise Cisco IOS XR routers, TACACS servers, and Linux management hosts, using the footholds to steal credentials and blind security logging.

## Skippable

- **[Virtual Event] What Every Enterprise Should Know About Securing Cloud Assets in the Age of AI** — Dark Reading. Event promo, not news.
- **[Virtual Event] Building a Secure AI Strategy for the Enterprise** — Dark Reading. Event promo, not news.
- **File servers are here to stay. Here's how to manage them securely** — BleepingComputer. Generic enterprise IT tips, no security incident.
- **New York Governor Kathy Hochul thinks AI should be 'less evil'** — The Verge AI. Political podcast/opinion, no technical or news substance.
- **Weekly Recap: Chinese Spy Proxy, AI Agents Go Off-Task, Router Backdoors and More** — The Hacker News. Roundup duplicating stories already covered individually.
- **Berlin confirms data theft after Rhysida ransomware attack claims** — BleepingComputer. Regional incident without TTPs/IOCs; duplicate of Berlin/Rhysida coverage below.
- **Instagram cracks down on AI accounts pretending to be human** — The Verge AI. Content-labeling policy tweak, no security angle.
- **Meeting notetaker Circleback adds a free tier to attract more customers** — TechCrunch AI. Generic SaaS pricing news, no security or model substance.
- **Pharmaceutical giant McKesson warns of 'service degradation' following cyberattack** — The Record. Duplicate of the McKesson/ShinyHunters breach story covered via SecurityWeek with more detail.
- **Slovenian casinos reopen after cyberattack knocked gaming systems offline** — The Record. Regional incident, no technical detail or attribution.
- **What the Hugging Face Incident Teaches Security Leaders About AI Agent Access** — SecurityWeek. Opinion/analysis piece referencing a past incident without new facts.
- **Boston Scientific Still Recovering From Cyberattack** — SecurityWeek. Ongoing incident follow-up without named threat actor, TTPs, or IOCs.
- **Extortion Group Claims Manchester Airports Group Data Breach** — SecurityWeek. Regional extortion claim without confirmation or technical detail.
- **Microsoft says Windows 11 KB5120998 update resets mouse settings** — BleepingComputer. Non-security bug.
- **ValleyRAT masquerading as adware** — Securelist. Duplicate of the ValleyRAT/Silver Fox story covered via The Hacker News with more detail.
- **Nigerians extradited to US for sextortion, deaths of two teens** — BleepingComputer. Criminal case, not a technical security or AI story.
- **Berlin Won't Pay Extortion Group Claiming Data Theft** — SecurityWeek. Duplicate of Berlin/Rhysida coverage; regional incident without TTPs.
- **Microsoft asks users to ignore 'Antivirus is turned off' errors** — BleepingComputer. Non-security product notice.
- **DoJ Corrects China Hacking Claim, Says U.S. Agencies Were Targets, Not Victims** — The Hacker News. Administrative correction, no new IOCs or technical guidance.
- **A milestone in expanding access to AI** — OpenAI Blog. Ad-revenue business milestone, no security or model-capability substance.
- **The U.S. is building barriers around drones and robots, but China has scale to get around them** — TechCrunch AI. General trade/geopolitics analysis, no AI safety or security specifics.
