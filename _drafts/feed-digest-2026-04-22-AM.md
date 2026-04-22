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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`, `microsoft`
- **Slug:** `2026-04-22-sharepoint-zero-day-active-exploitation-1300-servers`
- **Must-know:** yes
- **Summary:** Over 1,300 internet-exposed SharePoint servers remain unpatched against a spoofing zero-day that is still being actively exploited. The flaw enables credential theft, session hijacking, and lateral movement in enterprise environments.

### 2. Three Exploits Turn Windows Defender Into an Attacker Tool — Two Remain Unpatched
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/exploits-turn-windows-defender-attacker-tool
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `microsoft`, `appsec`
- **Slug:** `2026-04-21-windows-defender-exploits-active-attacks`
- **Must-know:** yes
- **Summary:** Three PoC exploits are being used in active attacks against Windows Defender; two are unpatched with no vendor mitigation yet available. Weaponizing the security tool itself creates blind spots and enables privilege escalation within the security agent's elevated context.

### 3. Microsoft Issues Emergency Out-of-Band Patches for Critical ASP.NET Core Privilege Escalation
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-emergency-security-updates-for-critical-aspnet-flaw/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`, `microsoft`
- **Slug:** `2026-04-22-microsoft-aspnet-emergency-patch-privilege-escalation`
- **Must-know:** no
- **Summary:** Microsoft issued out-of-band patches for a critical ASP.NET Core privilege escalation vulnerability, bypassing the normal Patch Tuesday cadence to signal urgency. All .NET runtime workloads are potentially affected; no confirmed active exploitation at time of writing.

### 4. Unauthorized Group Claimed to Have Gained Access to Anthropic's Restricted Mythos Cyber AI
- **Source:** TechCrunch AI — https://techcrunch.com/2026/04/21/unauthorized-group-has-gained-access-to-anthropics-exclusive-cyber-tool-mythos-report-claims/
- **Section:** AI — News & Analysis
- **Severity:** high
- **Tags:** `anthropic`, `ai-safety`, `llm`
- **Slug:** `2026-04-21-anthropic-mythos-unauthorized-access`
- **Must-know:** no
- **Summary:** An unauthorized group reportedly gained access to Anthropic's Mythos, a restricted offensive cybersecurity AI model. Anthropic is investigating and says no evidence of internal system compromise, but the incident raises significant dual-use concerns given Mythos' capabilities.

### 5. Novel Lotus Data Wiper Deployed Against Venezuelan Energy and Utility Infrastructure
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-lotus-data-wiper-used-against-venezuelan-energy-utility-firms/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `ics`
- **Slug:** `2026-04-21-lotus-data-wiper-venezuela-energy`
- **Must-know:** no
- **Summary:** A previously undocumented wiper malware called Lotus was used in 2025 against Venezuelan energy and utility organizations. Destructive wiper attacks against critical infrastructure point to nation-state actors prioritizing operational disruption over financial gain.

### 6. France Titres Confirms Breach as Hacker Offers Stolen Citizen Identity Data for Sale
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/french-govt-agency-confirms-breach-as-hacker-offers-to-sell-data/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `2026-04-21-france-titres-data-breach-citizen-data`
- **Must-know:** no
- **Summary:** France Titres, the French government agency issuing national identity documents, confirmed a breach after a threat actor began selling stolen citizen data. The breach affects an agency that processes identity documents for the entire French population, enabling persistent identity fraud.

### 7. Claude Mythos Preview Found 271 Firefox Vulnerabilities in Anthropic-Mozilla Collaboration
- **Source:** Simon Willison — https://simonwillison.net/2026/Apr/22/bobby-holley/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** high
- **Tags:** `ai-safety`, `vulnerability`, `anthropic`, `llm`
- **Slug:** `2026-04-22-claude-mythos-firefox-271-vulnerabilities`
- **Must-know:** no
- **Summary:** Firefox 150 ships with fixes for 271 vulnerabilities found by Claude Mythos Preview in collaboration with Mozilla. The volume of findings from a single AI-assisted evaluation represents a notable step-change in automated vulnerability discovery throughput.

### 8. Ransomware Negotiator Pleads Guilty to Colluding With BlackCat in Payment Scheme
- **Source:** Dark Reading — https://www.darkreading.com/insider-threats/ransomware-negotiator-pleads-guilty-blackcat-scheme
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ransomware`
- **Slug:** `2026-04-21-ransomware-negotiator-guilty-blackcat`
- **Must-know:** no
- **Summary:** A ransomware negotiator pleaded guilty to participating in the BlackCat scheme, a case illustrating how entanglement between negotiation and payment channels can cross into criminality. Practitioners should maintain strict separation of duties when engaging third-party incident response vendors.

### 9. OpenAI Launches ChatGPT Images 2.0 With Web Search and Multi-Image Generation
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/916166/openai-chatgpt-images-2
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `openai`, `ai-launch`, `model-release`
- **Slug:** `2026-04-21-openai-chatgpt-images-2-web-search`
- **Must-know:** no
- **Summary:** OpenAI released ChatGPT Images 2.0 with "thinking" capabilities and live web search integration for image generation. The web-search feature introduces new considerations for content authenticity verification and AI-generated media detection.

## Skippable

- **Changes to GitHub Copilot Individual plans** — Simon Willison. Product pricing changes (usage limits, plan tiers), no security or technical vulnerability angle.
- **Is Claude Code going to cost $100/month?** — Simon Willison. Anthropic pricing page confusion that was quickly reverted; no security substance.
- **Winter 2025 SOC 1 report** — AWS Security Blog. Routine compliance announcement covering 184 services; no incident or practitioner action required.
- **Meta will record employees' keystrokes to train AI models** — TechCrunch AI. Internal HR/data governance story; no exploitable vulnerability or external security incident.
- **SpaceX is working with Cursor and has an option to buy for $60B** — TechCrunch AI. Tech M&A business deal; no security angle.
- **SpaceX cuts a deal to maybe buy Cursor for $60 billion** — The Verge AI. Duplicate of above TechCrunch item.
- **Where's the raccoon with the ham radio? (ChatGPT Images 2.0)** — Simon Willison. Personal blog testing image generation model; no security angle. News covered by The Verge item above.
- **Apple's John Ternus will run one of the world's most powerful companies** — TechCrunch AI. CEO succession speculation; no security relevance.
- **AI research lab NeoCognition lands $40M seed** — TechCrunch AI. Startup funding announcement; no security substance.
- **AI backlash is coming for elections** — The Verge AI. Opinion/analysis piece without a specific news event or actionable finding.
- **ChatGPT's new Images 2.0 model is surprisingly good at generating text** — TechCrunch AI. Duplicate coverage of ChatGPT Images 2.0 launch already covered by The Verge item.
- **Sam Altman throws shade at Anthropic's Mythos: 'fear-based marketing'** — TechCrunch AI. CEO opinion/marketing commentary; no new security information beyond existing Mythos coverage.
