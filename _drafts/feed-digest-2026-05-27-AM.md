# Digest — 2026-05-27 AM

- Window: last 14h
- Raw items considered: 16
- Relevant: 9
- Skippable: 7

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** CISA Emergency: Exploited LiteSpeed cPanel Plugin Zero-Day Grants Root Access — `2026-05-27-litespeed-cpanel-plugin-zero-day-root-exploit.md`
- [x] **[HIGH]** SymJack: Malicious Repos Turn AI Coding Agents Into Supply Chain Attack Vectors — `2026-05-27-symjack-ai-coding-agents-supply-chain-mcp.md`
- [x] **[HIGH]** Microsoft Warns: AI Chatbot Recommendations Delivering Cryptojacking Malware — `2026-05-27-ai-chatbot-cryptojacking-malware-social-engineering.md`
- [x] **[HIGH]** Iranian State Actors Behind LA Metro Cyberattack, Obscured by Hacktivist Front — `2026-05-27-la-metro-cyberattack-iranian-state-sponsored.md`
- [x] **[HIGH]** FBI Warns: Silent Ransom Group Sends Physical Operatives to Insert USB Drives at Law Firms — `2026-05-27-fbi-silent-ransom-group-physical-usb-law-firms.md`
- [x] **[MEDIUM]** Anthropic Releases Claude Sandbox and Security Guidance Plugin for Developers — `2026-05-27-anthropic-claude-sandbox-security-guidance-plugin.md`
- [x] **[MEDIUM]** GlassWorm Botnet Dismantled: All Four C2 Channels Taken Down — `2026-05-27-glassworm-botnet-disrupted.md`
- [x] **[MEDIUM]** Cisco Talos Releases EvidenceForge for Realistic Synthetic Security Log Generation — `2026-05-27-evidenceforge-synthetic-security-logs-cisco-talos.md`
- [x] **[MEDIUM]** AI-Assisted Bug Reports Are Overwhelming the curl Security Team — `2026-05-27-ai-assisted-security-reports-curl-team.md`

## Relevant (details)

### 1. CISA Emergency: Exploited LiteSpeed cPanel Plugin Zero-Day Grants Root Access
- **Source:** SecurityWeek — https://www.securityweek.com/cisa-urges-immediate-patching-of-exploited-litespeed-cpanel-plugin-zero-day/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `vulnerability`, `rce`
- **Slug:** `2026-05-27-litespeed-cpanel-plugin-zero-day-root-exploit.md`
- **Must-know:** yes
- **Summary:** A critical zero-day in the LiteSpeed cPanel plugin was exploited in the wild before patching, enabling attackers to execute scripts with root privileges. CISA issued an emergency directive requiring federal agencies to patch within four days.

### 2. SymJack: Malicious Repos Turn AI Coding Agents Into Supply Chain Attack Vectors
- **Source:** SecurityWeek — https://www.securityweek.com/symjack-attack-turns-ai-coding-agents-into-supply-chain-attack-delivery-systems/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `llm`, `appsec`, `mcp`
- **Slug:** `2026-05-27-symjack-ai-coding-agents-supply-chain-mcp.md`
- **Must-know:** no
- **Summary:** SymJack is a newly disclosed technique that uses malicious repositories and disguised symlinks to trick AI coding agents into silently installing attacker-controlled MCP servers. Once installed, attackers can steal secrets, compromise CI pipelines, and deploy malicious code downstream.

### 3. Microsoft Warns: AI Chatbot Recommendations Delivering Cryptojacking Malware
- **Source:** The Hacker News — https://thehackernews.com/2026/05/ai-chatbot-recommendations-redirect.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `llm`, `microsoft`, `ai-safety`
- **Slug:** `2026-05-27-ai-chatbot-cryptojacking-malware-social-engineering.md`
- **Must-know:** no
- **Summary:** Microsoft Defender Experts identified an active cryptojacking campaign leveraging AI chatbot interactions to surface malicious software download sites. The technique exploits user trust in AI assistants as a novel social engineering delivery vector, extending attacks beyond conventional search results.

### 4. Iranian State Actors Behind LA Metro Cyberattack, Obscured by Hacktivist Front
- **Source:** SecurityWeek — https://www.securityweek.com/la-metro-cyberattack-linked-to-iranian-state-sponsored-hackers/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `nation-state`, `data-breach`
- **Slug:** `2026-05-27-la-metro-cyberattack-iranian-state-sponsored.md`
- **Must-know:** no
- **Summary:** A cyberattack on LA Metro was initially claimed by a hacktivist group, but infrastructure analysis links the operation to Iranian government threat actors. The use of hacktivist fronts to obscure state-sponsored activity is an established Iranian tradecraft pattern.

### 5. FBI Warns: Silent Ransom Group Sends Physical Operatives to Insert USB Drives at Law Firms
- **Source:** SecurityWeek — https://www.securityweek.com/fbi-hackers-sending-operatives-in-person-to-insert-usb-drives-and-steal-data/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`, `malware`, `phishing`
- **Slug:** `2026-05-27-fbi-silent-ransom-group-physical-usb-law-firms.md`
- **Must-know:** no
- **Summary:** The FBI issued an alert warning that the Silent Ransom Group is dispatching physical operatives to law firm offices to manually insert USB drives and steal data. The technique bypasses network-layer defenses entirely by gaining direct physical access to endpoints.

### 6. Anthropic Releases Claude Sandbox and Security Guidance Plugin for Developers
- **Source:** SecurityWeek — https://www.securityweek.com/anthropic-releases-new-claude-sandbox-security-guidance-plugin/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `anthropic`, `appsec`, `devsecops`, `llm`
- **Slug:** `2026-05-27-anthropic-claude-sandbox-security-guidance-plugin.md`
- **Must-know:** no
- **Summary:** Anthropic released a Claude Sandbox environment and a security guidance plugin that helps developers identify vulnerabilities during code writing. The plugin was used extensively internally before the public release.

### 7. GlassWorm Botnet Dismantled: All Four C2 Channels Taken Down
- **Source:** SecurityWeek — https://www.securityweek.com/glassworm-botnet-disrupted/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `botnet`
- **Slug:** `2026-05-27-glassworm-botnet-disrupted.md`
- **Must-know:** no
- **Summary:** Security firms coordinated the simultaneous takedown of all four C2 channels used by GlassWorm malware. Disrupting all infrastructure channels at once prevents operators from rerouting infected hosts to backup servers.

### 8. Cisco Talos Releases EvidenceForge for Realistic Synthetic Security Log Generation
- **Source:** Cisco Talos — https://blog.talosintelligence.com/introducing-evidenceforge-synthetic-security-logs-that-dont-look-as-fake/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `devsecops`, `appsec`
- **Slug:** `2026-05-27-evidenceforge-synthetic-security-logs-cisco-talos.md`
- **Must-know:** no
- **Summary:** Cisco Talos released EvidenceForge, a tool that generates high-quality synthetic security logs across multiple formats for SOC training and detection model validation. It addresses the challenge of obtaining realistic, labeled log data without exposing sensitive operational data.

### 9. AI-Assisted Bug Reports Are Overwhelming the curl Security Team
- **Source:** Simon Willison — https://simonwillison.net/2026/May/26/the-pressure/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `llm`, `vulnerability`, `appsec`
- **Slug:** `2026-05-27-ai-assisted-security-reports-curl-team.md`
- **Must-know:** no
- **Summary:** curl project lead Daniel Stenberg reports a 4-5x surge in security bug reports compared to 2024, driven by high-quality AI-assisted security research arriving at more than one report per day. The volume is creating unsustainable maintainer pressure, a signal of how AI tooling is reshaping open-source vulnerability research.

## Skippable

- **The Credential Crisis: How Stolen Credentials Defeat Modern Security** — SecurityWeek. Editorial analysis piece on credential security trends; no specific incident, CVE, or novel technique.
- **CISA gives feds 4 days to patch actively exploited cPanel plugin flaw** — BleepingComputer. Duplicate coverage of the LiteSpeed cPanel zero-day covered by SecurityWeek item above.
- **Dutch police arrests suspect linked to Ajax football club hack** — BleepingComputer. Single-organization arrest with no technical detail or broader relevance.
- **Windows 11 KB5089573 update released with performance improvements** — BleepingComputer. Routine Windows cumulative update with no critical CVE disclosures.
- **Quoting Kyle Ferrana** — Simon Willison. Social media commentary on AI agent failures; no news or technical substance.
- **Did the Pope use AI to write about the dangers of AI?** — The Verge AI. Cultural/opinion piece on AI authorship detection; no technical security angle.
- **DuckDuckGo installs are up 30% as users reject being 'force-fed' Google's AI Search** — TechCrunch AI. Consumer behavior story; no security or technical AI signal.
