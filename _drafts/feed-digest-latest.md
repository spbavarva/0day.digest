# Digest — 2026-04-22 AM

- Window: last 14h
- Raw items considered: 21
- Relevant: 9
- Skippable: 12

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Over 1,300 SharePoint Servers Still Exposed to Actively Exploited Spoofing Zero-Day — `2026-04-22-sharepoint-zero-day-active-exploitation-1300-servers.md`
- [x] **[CRITICAL]** Three Exploits Turn Windows Defender Into an Attacker Tool — Two Remain Unpatched — `2026-04-21-windows-defender-exploits-active-attacks.md`
- [x] **[CRITICAL]** Microsoft Issues Emergency Out-of-Band Patches for Critical ASP.NET Core Privilege Escalation — `2026-04-22-microsoft-aspnet-emergency-patch-privilege-escalation.md`
- [x] **[HIGH]** Unauthorized Group Claimed to Have Gained Access to Anthropic's Restricted Mythos Cyber AI — `2026-04-21-anthropic-mythos-unauthorized-access.md`
- [x] **[HIGH]** Novel Lotus Data Wiper Deployed Against Venezuelan Energy and Utility Infrastructure — `2026-04-21-lotus-data-wiper-venezuela-energy.md`
- [x] **[HIGH]** France Titres Confirms Breach as Hacker Offers Stolen Citizen Identity Data for Sale — `2026-04-21-france-titres-data-breach-citizen-data.md`
- [x] **[HIGH]** Claude Mythos Preview Found 271 Firefox Vulnerabilities in Anthropic-Mozilla Collaboration — `2026-04-22-claude-mythos-firefox-271-vulnerabilities.md`
- [x] **[MEDIUM]** Ransomware Negotiator Pleads Guilty to Colluding With BlackCat in Payment Scheme — `2026-04-21-ransomware-negotiator-guilty-blackcat.md`
- [x] **[INFORMATIONAL]** OpenAI Launches ChatGPT Images 2.0 With Web Search and Multi-Image Generation — `2026-04-21-openai-chatgpt-images-2-web-search.md`

## Relevant (details)

### 1. Over 1,300 SharePoint Servers Still Exposed to Actively Exploited Spoofing Zero-Day
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/over-1-300-microsoft-sharepoint-servers-vulnerable-to-ongoing-attacks/
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`, `microsoft`
- **Summary:** Over 1,300 internet-exposed SharePoint servers remain unpatched against a spoofing zero-day still under active exploitation. The flaw enables credential theft, session hijacking, and lateral movement in enterprise environments.

### 2. Three Exploits Turn Windows Defender Into an Attacker Tool — Two Remain Unpatched
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/exploits-turn-windows-defender-attacker-tool
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `microsoft`, `appsec`
- **Summary:** Three PoC exploits are being used in active attacks against Windows Defender; two are unpatched with no vendor mitigation available. Weaponizing the built-in security tool creates detection blind spots and enables privilege escalation.

### 3. Microsoft Issues Emergency Out-of-Band Patches for Critical ASP.NET Core Privilege Escalation
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-emergency-security-updates-for-critical-aspnet-flaw/
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`, `microsoft`
- **Summary:** Microsoft issued out-of-band patches for a critical ASP.NET Core privilege escalation flaw, bypassing Patch Tuesday cadence to signal urgency. All .NET runtime workloads are potentially affected.

### 4. Unauthorized Group Claimed to Have Gained Access to Anthropic's Restricted Mythos Cyber AI
- **Source:** TechCrunch AI — https://techcrunch.com/2026/04/21/unauthorized-group-has-gained-access-to-anthropics-exclusive-cyber-tool-mythos-report-claims/
- **Severity:** high
- **Tags:** `anthropic`, `ai-safety`, `llm`
- **Summary:** An unauthorized group reportedly gained access to Anthropic's Mythos, a restricted offensive cybersecurity AI model. Anthropic is investigating; no confirmed system compromise, but dual-use risk is significant.

### 5. Novel Lotus Data Wiper Deployed Against Venezuelan Energy and Utility Infrastructure
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-lotus-data-wiper-used-against-venezuelan-energy-utility-firms/
- **Severity:** high
- **Tags:** `malware`, `ics`
- **Summary:** A previously undocumented wiper malware called Lotus targeted Venezuelan energy and utility organizations in 2025. The destructive attack pattern points to nation-state actors prioritizing operational disruption; ICS/OT teams should review IOCs.

### 6. France Titres Confirms Breach as Hacker Offers Stolen Citizen Identity Data for Sale
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/french-govt-agency-confirms-breach-as-hacker-offers-to-sell-data/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** France Titres, the national agency issuing French identity documents, confirmed a breach with citizen data now for sale. Affects an agency handling passports, IDs, and driver's licenses for the entire French population.

### 7. Claude Mythos Preview Found 271 Firefox Vulnerabilities in Anthropic-Mozilla Collaboration
- **Source:** Simon Willison — https://simonwillison.net/2026/Apr/22/bobby-holley/#atom-everything
- **Severity:** high
- **Tags:** `ai-safety`, `vulnerability`, `anthropic`, `llm`
- **Summary:** Firefox 150 ships with 271 vulnerability fixes found by Claude Mythos Preview in collaboration with Mozilla. The volume signals a step-change in AI-assisted vulnerability discovery throughput.

### 8. Ransomware Negotiator Pleads Guilty to Colluding With BlackCat in Payment Scheme
- **Source:** Dark Reading — https://www.darkreading.com/insider-threats/ransomware-negotiator-pleads-guilty-blackcat-scheme
- **Severity:** medium
- **Tags:** `ransomware`
- **Summary:** A ransomware negotiator pleaded guilty to participating in the BlackCat scheme, a case illustrating risks when negotiation and payment channels are entangled. Practitioners should maintain strict separation of duties with third-party IR vendors.

### 9. OpenAI Launches ChatGPT Images 2.0 With Web Search and Multi-Image Generation
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/916166/openai-chatgpt-images-2
- **Severity:** informational
- **Tags:** `openai`, `ai-launch`, `model-release`
- **Summary:** OpenAI released ChatGPT Images 2.0 with live web-search integration and improved instruction-following. The web-search feature has implications for content authenticity and AI-generated media detection workflows.

## Skippable

- **Changes to GitHub Copilot Individual plans** — Simon Willison. Product pricing changes (usage limits, plan tiers), no security or technical vulnerability angle.
- **Is Claude Code going to cost $100/month?** — Simon Willison. Pricing page confusion quickly reverted; no security substance.
- **Winter 2025 SOC 1 report** — AWS Security Blog. Routine compliance announcement; no incident or practitioner action required.
- **Meta will record employees' keystrokes to train AI models** — TechCrunch AI. Internal HR/data governance story; no exploitable vulnerability or external security incident.
- **SpaceX is working with Cursor and has an option to buy for $60B** — TechCrunch AI. Tech M&A business deal; no security angle.
- **SpaceX cuts a deal to maybe buy Cursor for $60 billion** — The Verge AI. Duplicate of above TechCrunch item.
- **Where's the raccoon with the ham radio? (ChatGPT Images 2.0)** — Simon Willison. Personal blog testing image generation; no security angle; news covered by The Verge item.
- **Apple's John Ternus will run one of the world's most powerful companies** — TechCrunch AI. CEO succession speculation; no security relevance.
- **AI research lab NeoCognition lands $40M seed** — TechCrunch AI. Startup funding announcement; no security substance.
- **AI backlash is coming for elections** — The Verge AI. Opinion/analysis piece without a specific news event or actionable finding.
- **ChatGPT's new Images 2.0 model is surprisingly good at generating text** — TechCrunch AI. Duplicate coverage of ChatGPT Images 2.0 launch already covered by The Verge item.
- **Sam Altman throws shade at Anthropic's Mythos: 'fear-based marketing'** — TechCrunch AI. CEO opinion/marketing commentary; no new security information beyond existing Mythos coverage.
