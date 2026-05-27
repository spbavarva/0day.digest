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
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `ai-safety`, `llm`, `appsec`, `devsecops`
- **Slug:** `2026-05-27-symjack-ai-coding-agents-mcp-supply-chain`
- **Must-know:** no
- **Summary:** Malicious repositories with disguised symlinks trick AI coding agents into silently installing attacker-controlled MCP servers capable of stealing secrets, compromising CI pipelines, and executing arbitrary code. Any developer using AI coding assistants with repository cloning workflows is potentially exposed.

### 2. Malicious npm Package Exfiltrated Files from Claude AI User Directories
- **Source:** The Hacker News — https://thehackernews.com/2026/05/malicious-npm-package-stole-files-from.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `malware`, `anthropic`, `llm`
- **Slug:** `2026-05-27-npm-mouse5212-super-formatter-claude-user-files`
- **Must-know:** no
- **Summary:** OX Security discovered the npm package "mouse5212-super-formatter" targeting Anthropic's Claude AI tool by uploading files from "/mnt/user-data" — the directory Claude uses for uploads and session outputs. This is a targeted infostealer against developers using Claude Code locally.

### 3. GlassWorm Developer Supply Chain Botnet Dismantled by Industry Coalition
- **Source:** The Hacker News — https://thehackernews.com/2026/05/glassworm-malware-takedown-disrupts.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `npm`, `github`, `devsecops`
- **Slug:** `2026-05-27-glassworm-botnet-disrupted-supply-chain`
- **Must-know:** no
- **Summary:** CrowdStrike, Google, and the Shadowserver Foundation simultaneously took down all four GlassWorm C2 channels, including blockchain- and DHT-based infrastructure designed to resist domain takedowns. GlassWorm has targeted developers via malicious packages since 2025; previously installed implants may remain active.

### 4. AI-Assisted Exploit Development Now Outpaces Vulnerability Scanner Detection
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/ai-assisted-exploit-development-scanner-detection
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ai-safety`, `vulnerability`, `appsec`, `llm`
- **Slug:** `2026-05-27-ai-assisted-exploit-development-outpaces-detection`
- **Must-know:** no
- **Summary:** New research shows AI dramatically compresses time-to-exploit for known CVEs, with AI-generated variants outpacing scanner signature updates. The asymmetry favors attackers: signatures require known patterns; AI-assisted exploit development generates novel variants faster than defenders can characterize them.

### 5. Attackers Use AI Chatbot Responses to Deliver Cryptojacking Malware
- **Source:** The Hacker News — https://thehackernews.com/2026/05/ai-chatbot-recommendations-redirect.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `ai-safety`, `llm`, `phishing`
- **Slug:** `2026-05-27-ai-chatbot-cryptojacking-malware-delivery`
- **Must-know:** no
- **Summary:** Microsoft documented an active campaign where threat actors manipulate AI chatbot interactions to surface malicious lookalike download sites serving cryptojacking malware. The technique extends social engineering into AI-generated responses, which users tend to trust more than organic search results.

### 6. Gitea CVE-2026-27771: Unauthenticated Attackers Can Pull Private Container Images
- **Source:** The Hacker News — https://thehackernews.com/2026/05/gitea-vulnerability-exposes-private.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `container-security`, `appsec`
- **Slug:** `2026-05-27-gitea-cve-2026-27771-unauthenticated-container-images`
- **Must-know:** no
- **Summary:** CVE-2026-27771 in Gitea allows unauthenticated remote attackers to pull private container images without any credentials. All versions prior to 1.26.2 are affected. Organizations using Gitea as a self-hosted container registry should upgrade immediately and audit registry access logs for unauthorized pulls.

### 7. CISA Issues 4-Day Patch Deadline for Actively Exploited LiteSpeed cPanel Plugin
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-gives-feds-4-days-to-patch-actively-exploited-cpanel-plugin-flaw/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`
- **Slug:** `2026-05-27-cisa-kev-litespeed-cpanel-4day-deadline`
- **Must-know:** no
- **Summary:** CISA added a critical flaw in the LiteSpeed cPanel user-end plugin to the KEV catalog and gave federal agencies four days to remediate — reflecting active in-the-wild exploitation. Any organization running cPanel with LiteSpeed should patch immediately and review server logs for evidence of compromise.

### 8. CISA KEV Updated: Daemon Tools, TanStack, and Nx Console Supply Chain CVEs Added
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/alerts/2026/05/27/cisa-adds-three-known-exploited-vulnerabilities-catalog
- **Section:** Government / Advisory
- **Severity:** medium
- **Tags:** `cve`, `supply-chain`, `vulnerability`, `npm`
- **Slug:** `2026-05-27-cisa-kev-daemon-tools-tanstack-nx-console`
- **Must-know:** no
- **Summary:** CISA officially confirmed active exploitation for CVE-2026-8398 (Daemon Tools), CVE-2026-45321 (TanStack), and CVE-2026-48027 (Nx Console) by adding them to the KEV catalog. Two of the three involve embedded malicious code — supply chain compromises previously covered in this digest.

### 9. Iranian MOIS Intelligence Service Linked to LA Metro Cyberattack
- **Source:** The Record (Recorded Future) — https://therecord.media/iranian-intelligence-behind-hack-of-la-transit-system
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`, `appsec`
- **Slug:** `2026-05-27-iran-mois-la-metro-cyberattack`
- **Must-know:** no
- **Summary:** Gambit Security researchers attributed the LA Metro cyberattack to a group with confirmed ties to Iran's MOIS, exposing a state-sponsored operation masked behind a hacktivist cover identity. The finding extends a pattern of Iranian actors targeting US critical infrastructure under deniable personas.

### 10. FBI Warns Silent Ransom Group Is Making In-Person Visits to US Law Firms
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/fbi-warns-of-silent-ransom-group-in-person-data-theft-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `data-breach`, `ransomware`
- **Slug:** `2026-05-27-silent-ransom-group-law-firms-in-person`
- **Must-know:** no
- **Summary:** The FBI warned that SRG has added in-person social engineering visits to US law firms to its existing vishing and callback phishing playbook. Law firms are targeted due to high-value privileged client data; the in-person escalation represents a significant TTP change for the group.

### 11. Purported Leak Exposes 5.8 Million Uruguayan Citizens' Records
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/latin-american-cybercriminals-government-data
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `2026-05-27-uruguay-5-8m-citizens-breach`
- **Must-know:** no
- **Summary:** A purported leak claims to expose 5.8 million Uruguayan citizen records — the latest in a series of Latin American government database breaches. The data is being monetized on underground markets and is likely to fuel targeted phishing campaigns in the region.

### 12. Grandoreiro and BTMOB RAT Campaigns Target Banking Users Across Spain, Portugal, Mexico, and Brazil
- **Source:** The Hacker News — https://thehackernews.com/2026/05/grandoreiro-malware-and-btmob-rat.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`, `data-breach`
- **Slug:** `2026-05-27-grandoreiro-btmob-banking-trojans`
- **Must-know:** no
- **Summary:** WatchGuard and ESET documented concurrent campaigns: Grandoreiro (Windows banking trojan) targeting Spain, Portugal, and Mexico; BTMOB RAT (Android) targeting Brazil. Both are designed to steal banking credentials and intercept OTP codes during active session fraud.

### 13. Cisco Talos Discloses Four Heap-Based Buffer Overflow Flaws in MediaInfoLib
- **Source:** Cisco Talos — https://blog.talosintelligence.com/mediaarea-heap-based-buffer-overflow-vulnerabilities/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`, `appsec`
- **Slug:** `2026-05-27-mediaarea-mediainfoflib-heap-overflows`
- **Must-know:** no
- **Summary:** Talos disclosed four heap-based buffer overflows in MediaInfoLib, a widely-embedded open-source media metadata library. Heap overflows in media parsers can be triggered by crafted files, posing risk to media processing pipelines and applications that handle untrusted input.

### 14. UK Cyberspying Chief Calls AI 'Unstoppable Force,' Warns of Russian Gray Zone Escalation
- **Source:** SecurityWeek — https://www.securityweek.com/uk-cyberspying-chief-calls-ai-an-unstoppable-force-and-warns-about-russia/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ai-safety`
- **Slug:** `2026-05-27-uk-gchq-ai-russia-gray-zone`
- **Must-know:** no
- **Summary:** The UK's signals intelligence chief delivered a public warning about Russia's gray-zone cyber escalation and AI as a force multiplier for both attackers and defenders. Part of a growing Western intelligence consensus on AI-enabled adversarial activity.

### 15. Google Cloud Launches AI Threat Defense to Help Security Teams Outpace Attackers
- **Source:** Google Cloud Security — https://cloud.google.com/blog/products/identity-security/introducing-google-ai-threat-defense/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `ai-safety`, `cloud-security`, `google`, `appsec`
- **Slug:** `2026-05-27-google-ai-threat-defense-launch`
- **Must-know:** no
- **Summary:** Google Cloud announced AI Threat Defense, positioning AI-native detection and response capabilities within its security platform. Limited technical details provided at launch; notable as part of the broader vendor push toward AI-driven security operations.

### 16. Pretalx Conference Software Vulnerability Gave Attackers 100% Talk Acceptance Rate
- **Source:** SecurityWeek — https://www.securityweek.com/vulnerability-in-popular-conference-software-granted-attackers-a-100-talk-acceptance-rate/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `vulnerability`, `appsec`
- **Slug:** `2026-05-27-pretalx-cfp-account-takeover`
- **Must-know:** no
- **Summary:** An account takeover flaw in Pretalx (open-source CFP management) allowed attackers to compromise reviewer accounts and approve any conference submission. Used by many security and open-source conferences; organizers should patch immediately.

## Skippable

- **Your SEO strategy is optimized for a search engine that no longer exists** — TechCrunch AI. SEO/AI search opinion podcast; no security or technical substance.
- **Romanian national sentenced to more than 4 years for hacking Oregon systems** — The Record. Routine law enforcement sentencing; duplicate of SecurityWeek item below.
- **Meta launches Instagram, Facebook, and WhatsApp subscriptions** — TechCrunch AI. Non-security SaaS/business launch.
- **ITBench-AA: Frontier Models Score Below 50% on Agentic IT Tasks** — Hugging Face Blog. AI benchmark for enterprise IT; no security angle.
- **I think Anthropic and OpenAI have found product-market fit** — Simon Willison. Opinion/analysis post, no news value.
- **Meet Our Newest AWS Heroes – May 2026** — AWS News Blog. Community/marketing content.
- **AI coding startup Cognition raises $1B at $25B valuation** — TechCrunch AI. VC funding announcement; no security content.
- **Rudd orders Cyber Command reviews as Pentagon presses reform agenda** — The Record. Administrative/policy; no technical security content.
- **AI tried to bury this politician** — The Verge AI. AI/politics story; no technical security content.
- **Robinhood will let your AI agent trade stocks** — The Verge AI. Non-security consumer product; duplicate of TechCrunch item.
- **Startup Battlefield 200 applications close today** — TechCrunch AI. Event marketing.
- **ElevenLabs' new music-generation model** — TechCrunch AI. AI model launch; no security angle.
- **Can you enforce strong Active Directory password rules without frustrating users?** — BleepingComputer. Sponsored content from Specops Software; marketing disguised as advice.
- **TechCrunch Disrupt 2026 Early Bird ticket savings end in 3 days** — TechCrunch AI. Event marketing.
- **SOND sleep tech startup exits stealth with $7M** — TechCrunch AI. Off-topic consumer tech.
- **This smart bird feeder captures more of my backyard drama** — The Verge AI. Off-topic consumer product review.
- **China is increasingly keeping its best AI talent to itself** — TechCrunch AI. Geopolitical analysis; no security angle.
- **5 Steps to Managing Shadow AI Tools Without Slowing Down Employees** — The Hacker News. Generic enterprise IT management; no technical substance.
- **Glassworm botnet disrupted after resilient C2 infrastructure takedown** — BleepingComputer. Duplicate of The Hacker News item (kept).
- **Dutch police arrest man over cyber breach at Ajax football club** — The Record. Regional law enforcement; single-org incident. Duplicate of BleepingComputer item.
- **ClickHouse triples annualized revenue to $250M** — TechCrunch AI. Business news; no security angle.
- **SecurityWeek to Host AI Risk Summit August 11-12** — SecurityWeek. Event marketing.
- **YouTube will now automatically label AI videos** — TechCrunch AI. Platform policy; duplicate of The Verge item.
- **YouTube is putting AI labels where you'll actually see them** — The Verge AI. Platform policy; duplicate of TechCrunch item.
- **Robinhood now lets your AI agents trade stocks** — TechCrunch AI. Non-security; duplicate of The Verge item.
- **Tech CEOs are apparently suffering from AI psychosis** — TechCrunch AI. Opinion/commentary; no news value.
- **Cybersecurity Evolution: How We Went From Perimeter Defense to AI-Native Security** — Dark Reading. Retrospective editorial; no actionable intelligence.
- **The AI fight brewing inside The New York Times** — The Verge AI. Labor/media story; no security angle.
- **The Pope isn't AGI-pilled** — The Verge AI. Policy/cultural commentary; no security angle.
- **RevEng.AI Raises $15 Million to Hunt for Flaws and Backdoors** — SecurityWeek. VC funding; interesting tool but insufficient technical substance for a post.
- **3 SOC Steps that Shut Down Incident Risks Early** — The Hacker News. Generic enterprise security content; likely sponsored.
- **Romanian Hacker Sentenced to Prison in US for Selling Access to State Network** — SecurityWeek. Duplicate of The Record sentencing item; routine law enforcement.
- **Lastwall Raises $11.5 Million for Quantum-Resilient Identity Platform** — SecurityWeek. VC/funding; no technical content.
- **The Credential Crisis: How Stolen Credentials Defeat Modern Security** — SecurityWeek. Generic security content; appears sponsored.
- **GlassWorm Botnet Disrupted** — SecurityWeek. Duplicate of The Hacker News item (kept).
- **Introducing EvidenceForge: Synthetic security logs that don't look (as) fake** — Cisco Talos. Defensive tool release; useful but low urgency for this digest.
- **LA Metro Cyberattack Linked to Iranian State-Sponsored Hackers** — SecurityWeek. Duplicate of The Record item (kept).
- **Dutch police arrests suspect linked to Ajax football club hack** — BleepingComputer. Duplicate of The Record item; regional law enforcement.
- **Windows 11 KB5089573 update released with performance improvements** — BleepingComputer. Routine cumulative update; no critical CVE.
- **Building self-improving tax agents with Codex** — OpenAI Blog. AI use case story; no security angle.
- **Quoting Kyle Ferrana** — Simon Willison. Quote/link post; no substance.
