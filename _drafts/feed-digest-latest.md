# Digest — 2026-05-27 PM

- Window: last 14h
- Raw items considered: 58
- Relevant: 16
- Skippable: 42

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** SymJack Attack Weaponizes AI Coding Agents as Supply Chain Delivery Systems — `2026-05-27-symjack-ai-coding-agents-mcp-supply-chain.md`
- [x] **[HIGH]** Malicious npm Package Exfiltrated Files from Claude AI User Directories — `2026-05-27-npm-mouse5212-super-formatter-claude-user-files.md`
- [x] **[HIGH]** GlassWorm Developer Supply Chain Botnet Dismantled by Industry Coalition — `2026-05-27-glassworm-botnet-disrupted-supply-chain.md`
- [x] **[HIGH]** AI-Assisted Exploit Development Now Outpaces Vulnerability Scanner Detection — `2026-05-27-ai-assisted-exploit-development-outpaces-detection.md`
- [x] **[HIGH]** Attackers Use AI Chatbot Responses to Deliver Cryptojacking Malware — `2026-05-27-ai-chatbot-cryptojacking-malware-delivery.md`
- [x] **[HIGH]** Gitea CVE-2026-27771: Unauthenticated Attackers Can Pull Private Container Images — `2026-05-27-gitea-cve-2026-27771-unauthenticated-container-images.md`
- [x] **[HIGH]** CISA Issues 4-Day Patch Deadline for Actively Exploited LiteSpeed cPanel Plugin — `2026-05-27-cisa-kev-litespeed-cpanel-4day-deadline.md`
- [x] **[MEDIUM]** CISA KEV Updated: Daemon Tools, TanStack, and Nx Console Supply Chain CVEs Added — `2026-05-27-cisa-kev-daemon-tools-tanstack-nx-console.md`
- [x] **[MEDIUM]** Iranian MOIS Intelligence Service Linked to LA Metro Cyberattack — `2026-05-27-iran-mois-la-metro-cyberattack.md`
- [x] **[MEDIUM]** FBI Warns Silent Ransom Group Is Making In-Person Visits to US Law Firms — `2026-05-27-silent-ransom-group-law-firms-in-person.md`
- [x] **[MEDIUM]** Purported Leak Exposes 5.8 Million Uruguayan Citizens' Records — `2026-05-27-uruguay-5-8m-citizens-breach.md`
- [x] **[MEDIUM]** Grandoreiro and BTMOB RAT Campaigns Target Banking Users Across Spain, Portugal, Mexico, and Brazil — `2026-05-27-grandoreiro-btmob-banking-trojans.md`
- [x] **[MEDIUM]** Cisco Talos Discloses Four Heap-Based Buffer Overflow Flaws in MediaInfoLib — `2026-05-27-mediaarea-mediainfoflib-heap-overflows.md`
- [x] **[INFORMATIONAL]** UK Cyberspying Chief Calls AI 'Unstoppable Force,' Warns of Russian Gray Zone Escalation — `2026-05-27-uk-gchq-ai-russia-gray-zone.md`
- [x] **[INFORMATIONAL]** Google Cloud Launches AI Threat Defense to Help Security Teams Outpace Attackers — `2026-05-27-google-ai-threat-defense-launch.md`
- [x] **[INFORMATIONAL]** Pretalx Conference Software Vulnerability Gave Attackers 100% Talk Acceptance Rate — `2026-05-27-pretalx-cfp-account-takeover.md`

## Relevant (details)

### 1. SymJack Attack Weaponizes AI Coding Agents as Supply Chain Delivery Systems
- **Source:** SecurityWeek — https://www.securityweek.com/symjack-attack-turns-ai-coding-agents-into-supply-chain-attack-delivery-systems/
- **Severity:** high
- **Tags:** `supply-chain`, `ai-safety`, `llm`, `appsec`, `devsecops`
- **Summary:** Malicious repositories with disguised symlinks trick AI coding agents into silently installing attacker-controlled MCP servers capable of stealing secrets, compromising CI pipelines, and executing arbitrary code. Any developer using AI coding assistants with repository cloning workflows is potentially exposed.

### 2. Malicious npm Package Exfiltrated Files from Claude AI User Directories
- **Source:** The Hacker News — https://thehackernews.com/2026/05/malicious-npm-package-stole-files-from.html
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `malware`, `anthropic`, `llm`
- **Summary:** OX Security found "mouse5212-super-formatter" on npm — a targeted infostealer that uploads files from "/mnt/user-data", the directory Anthropic's Claude AI tool uses for uploads and session outputs. Aimed at developers running Claude Code locally.

### 3. GlassWorm Developer Supply Chain Botnet Dismantled by Industry Coalition
- **Source:** The Hacker News — https://thehackernews.com/2026/05/glassworm-malware-takedown-disrupts.html
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `npm`, `github`, `devsecops`
- **Summary:** CrowdStrike, Google, and Shadowserver Foundation took down all four GlassWorm C2 channels including blockchain- and DHT-based infrastructure. Active since 2025 targeting developers via malicious packages; previously installed implants may remain active.

### 4. AI-Assisted Exploit Development Now Outpaces Vulnerability Scanner Detection
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/ai-assisted-exploit-development-scanner-detection
- **Severity:** high
- **Tags:** `ai-safety`, `vulnerability`, `appsec`, `llm`
- **Summary:** Research shows AI dramatically compresses time-to-exploit for known CVEs, with AI-generated variants outpacing scanner signature updates. Defenders relying on signature-based detection face a widening gap against AI-accelerated exploit development.

### 5. Attackers Use AI Chatbot Responses to Deliver Cryptojacking Malware
- **Source:** The Hacker News — https://thehackernews.com/2026/05/ai-chatbot-recommendations-redirect.html
- **Severity:** high
- **Tags:** `malware`, `ai-safety`, `llm`, `phishing`
- **Summary:** Microsoft documented an active campaign where threat actors manipulate AI chatbot interactions to surface malicious lookalike download sites serving cryptojacking malware — extending social engineering into AI-generated responses users trust.

### 6. Gitea CVE-2026-27771: Unauthenticated Attackers Can Pull Private Container Images
- **Source:** The Hacker News — https://thehackernews.com/2026/05/gitea-vulnerability-exposes-private.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `container-security`, `appsec`
- **Summary:** CVE-2026-27771 in Gitea allows unauthenticated remote attackers to pull private container images without credentials. All versions prior to 1.26.2 are affected. Upgrade immediately and audit registry access logs.

### 7. CISA Issues 4-Day Patch Deadline for Actively Exploited LiteSpeed cPanel Plugin
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-gives-feds-4-days-to-patch-actively-exploited-cpanel-plugin-flaw/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`
- **Summary:** CISA added a critical LiteSpeed cPanel plugin flaw to KEV with a 4-day federal remediation deadline — a compressed window reflecting active, widespread exploitation. Any org running cPanel with LiteSpeed should patch immediately.

### 8. CISA KEV Updated: Daemon Tools, TanStack, and Nx Console Supply Chain CVEs Added
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/alerts/2026/05/27/cisa-adds-three-known-exploited-vulnerabilities-catalog
- **Severity:** medium
- **Tags:** `cve`, `supply-chain`, `vulnerability`, `npm`
- **Summary:** CISA confirmed active exploitation for CVE-2026-8398 (Daemon Tools), CVE-2026-45321 (TanStack), and CVE-2026-48027 (Nx Console) by adding them to KEV. Two are supply chain embedded malicious code compromises previously covered in this digest.

### 9. Iranian MOIS Intelligence Service Linked to LA Metro Cyberattack
- **Source:** The Record (Recorded Future) — https://therecord.media/iranian-intelligence-behind-hack-of-la-transit-system
- **Severity:** medium
- **Tags:** `data-breach`, `appsec`
- **Summary:** Gambit Security attributed the LA Metro cyberattack to a group with confirmed ties to Iran's MOIS, revealing state-sponsored activity disguised as hacktivism. Extends a pattern of Iranian actors targeting US critical infrastructure under deniable personas.

### 10. FBI Warns Silent Ransom Group Is Making In-Person Visits to US Law Firms
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/fbi-warns-of-silent-ransom-group-in-person-data-theft-attacks/
- **Severity:** medium
- **Tags:** `phishing`, `data-breach`, `ransomware`
- **Summary:** SRG has added in-person social engineering visits to US law firms to its existing vishing and callback phishing playbook. The TTP escalation targets firms holding high-value privileged client data.

### 11. Purported Leak Exposes 5.8 Million Uruguayan Citizens' Records
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/latin-american-cybercriminals-government-data
- **Severity:** medium
- **Tags:** `data-breach`
- **Summary:** A purported 5.8 million-record leak from Uruguayan government databases is the latest in a series targeting Latin American government agencies for underground market monetization.

### 12. Grandoreiro and BTMOB RAT Banking Trojan Campaigns
- **Source:** The Hacker News — https://thehackernews.com/2026/05/grandoreiro-malware-and-btmob-rat.html
- **Severity:** medium
- **Tags:** `malware`, `phishing`, `data-breach`
- **Summary:** Concurrent campaigns: Grandoreiro (Windows) targeting banking users in Spain, Portugal, Mexico; BTMOB RAT (Android) targeting Brazil. Both harvest banking credentials and OTP codes.

### 13. Cisco Talos Discloses Four Heap-Based Buffer Overflow Flaws in MediaInfoLib
- **Source:** Cisco Talos — https://blog.talosintelligence.com/mediaarea-heap-based-buffer-overflow-vulnerabilities/
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`, `appsec`
- **Summary:** Four heap-based buffer overflows in MediaInfoLib (widely-embedded media metadata library). Exploitable via crafted media files in any pipeline processing untrusted input.

### 14. UK Cyberspying Chief Warns of Russian Gray Zone Escalation and AI Threat
- **Source:** SecurityWeek — https://www.securityweek.com/uk-cyberspying-chief-calls-ai-an-unstoppable-force-and-warns-about-russia/
- **Severity:** informational
- **Tags:** `ai-safety`
- **Summary:** UK signals intelligence chief describes AI as an "unstoppable force" and warns of Russia's gray-zone escalation. Part of growing Western intelligence consensus on AI-enabled adversarial activity.

### 15. Google Cloud Launches AI Threat Defense
- **Source:** Google Cloud Security — https://cloud.google.com/blog/products/identity-security/introducing-google-ai-threat-defense/
- **Severity:** informational
- **Tags:** `ai-safety`, `cloud-security`, `google`, `appsec`
- **Summary:** Google Cloud announced AI Threat Defense, integrating AI-powered detection and response into its security platform. Limited technical detail at launch.

### 16. Pretalx Conference Software Account Takeover Vulnerability
- **Source:** SecurityWeek — https://www.securityweek.com/vulnerability-in-popular-conference-software-granted-attackers-a-100-talk-acceptance-rate/
- **Severity:** informational
- **Tags:** `vulnerability`, `appsec`
- **Summary:** Account takeover flaw in Pretalx (open-source CFP tool) allowed attackers to compromise reviewer accounts and approve any conference submission. Widely used by security conferences; patch immediately.

## Skippable

- **Your SEO strategy is optimized for a search engine that no longer exists** — TechCrunch AI. SEO/AI search opinion podcast; no security or technical substance.
- **Romanian national sentenced to more than 4 years for hacking Oregon systems** — The Record. Routine law enforcement sentencing; duplicate of SecurityWeek item.
- **Meta launches Instagram, Facebook, and WhatsApp subscriptions** — TechCrunch AI. Non-security SaaS/business launch.
- **ITBench-AA: Frontier Models Score Below 50% on Agentic IT Tasks** — Hugging Face Blog. AI benchmark; no security angle.
- **I think Anthropic and OpenAI have found product-market fit** — Simon Willison. Opinion piece; no news value.
- **Meet Our Newest AWS Heroes – May 2026** — AWS News Blog. Community/marketing content.
- **AI coding startup Cognition raises $1B at $25B valuation** — TechCrunch AI. VC funding; no security content.
- **Rudd orders Cyber Command reviews** — The Record. Administrative/policy; no technical content.
- **AI tried to bury this politician** — The Verge AI. AI/politics; no security content.
- **Robinhood will let your AI agent trade stocks** — The Verge AI. Non-security; duplicate of TechCrunch item.
- **Startup Battlefield 200 applications close today** — TechCrunch AI. Event marketing.
- **ElevenLabs' new music-generation model** — TechCrunch AI. AI launch; no security angle.
- **Can you enforce strong Active Directory password rules without frustrating users?** — BleepingComputer. Sponsored content from Specops Software.
- **TechCrunch Disrupt 2026 Early Bird ticket savings** — TechCrunch AI. Event marketing.
- **SOND sleep tech startup exits stealth with $7M** — TechCrunch AI. Off-topic consumer tech.
- **This smart bird feeder captures more of my backyard drama** — The Verge AI. Off-topic consumer product.
- **China is increasingly keeping its best AI talent to itself** — TechCrunch AI. Geopolitical analysis; no security angle.
- **5 Steps to Managing Shadow AI Tools** — The Hacker News. Generic enterprise IT; no technical substance.
- **Glassworm botnet disrupted** — BleepingComputer. Duplicate of The Hacker News item (kept).
- **Dutch police arrest man over cyber breach at Ajax football club** — The Record. Regional law enforcement; single-org. Duplicate of BleepingComputer item.
- **ClickHouse triples annualized revenue to $250M** — TechCrunch AI. Business news; no security angle.
- **SecurityWeek to Host AI Risk Summit August 11-12** — SecurityWeek. Event marketing.
- **YouTube will now automatically label AI videos** — TechCrunch AI. Platform policy; duplicate of The Verge item.
- **YouTube is putting AI labels where you'll actually see them** — The Verge AI. Platform policy; duplicate of TechCrunch item.
- **Robinhood now lets your AI agents trade stocks** — TechCrunch AI. Non-security; duplicate of The Verge item.
- **Tech CEOs are apparently suffering from AI psychosis** — TechCrunch AI. Opinion/commentary; no news value.
- **Cybersecurity Evolution: Perimeter Defense to AI-Native Security** — Dark Reading. Retrospective editorial; no actionable intelligence.
- **The AI fight brewing inside The New York Times** — The Verge AI. Labor/media story; no security angle.
- **The Pope isn't AGI-pilled** — The Verge AI. Policy/cultural commentary; no security angle.
- **RevEng.AI Raises $15 Million** — SecurityWeek. VC funding; insufficient technical substance.
- **3 SOC Steps that Shut Down Incident Risks Early** — The Hacker News. Generic enterprise content; likely sponsored.
- **Romanian Hacker Sentenced to Prison** — SecurityWeek. Duplicate of The Record sentencing item.
- **Lastwall Raises $11.5 Million for Quantum-Resilient Identity Platform** — SecurityWeek. VC/funding; no technical content.
- **The Credential Crisis: How Stolen Credentials Defeat Modern Security** — SecurityWeek. Generic sponsored content.
- **GlassWorm Botnet Disrupted** — SecurityWeek. Duplicate of The Hacker News item (kept).
- **Introducing EvidenceForge: Synthetic security logs** — Cisco Talos. Defensive tool; useful but low urgency.
- **LA Metro Cyberattack Linked to Iranian State-Sponsored Hackers** — SecurityWeek. Duplicate of The Record item (kept).
- **Dutch police arrests suspect linked to Ajax football club hack** — BleepingComputer. Duplicate of The Record item; regional law enforcement.
- **Windows 11 KB5089573 update released with performance improvements** — BleepingComputer. Routine cumulative update; no critical CVE.
- **Building self-improving tax agents with Codex** — OpenAI Blog. AI use case story; no security angle.
- **FBI warns extortion hackers are visiting US law firms to steal data** — The Record. Duplicate of BleepingComputer item (kept).
- **Quoting Kyle Ferrana** — Simon Willison. Quote/link post; no substance.
