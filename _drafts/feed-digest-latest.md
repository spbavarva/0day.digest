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
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `vulnerability`, `rce`
- **Summary:** A critical zero-day in the LiteSpeed cPanel plugin was exploited in the wild before patching, enabling attackers to execute scripts with root privileges. CISA issued an emergency directive requiring federal agencies to patch within four days.

### 2. SymJack: Malicious Repos Turn AI Coding Agents Into Supply Chain Attack Vectors
- **Source:** SecurityWeek — https://www.securityweek.com/symjack-attack-turns-ai-coding-agents-into-supply-chain-attack-delivery-systems/
- **Severity:** high
- **Tags:** `supply-chain`, `llm`, `appsec`, `mcp`
- **Summary:** SymJack uses malicious repositories and disguised symlinks to trick AI coding agents into silently installing attacker-controlled MCP servers capable of stealing secrets, compromising CI pipelines, and deploying malicious code.

### 3. Microsoft Warns: AI Chatbot Recommendations Delivering Cryptojacking Malware
- **Source:** The Hacker News — https://thehackernews.com/2026/05/ai-chatbot-recommendations-redirect.html
- **Severity:** high
- **Tags:** `malware`, `llm`, `microsoft`, `ai-safety`
- **Summary:** Microsoft Defender Experts identified an active cryptojacking campaign leveraging AI chatbot interactions to surface malicious software download sites. The technique extends social engineering beyond conventional search results by exploiting user trust in AI assistants.

### 4. Iranian State Actors Behind LA Metro Cyberattack, Obscured by Hacktivist Front
- **Source:** SecurityWeek — https://www.securityweek.com/la-metro-cyberattack-linked-to-iranian-state-sponsored-hackers/
- **Severity:** high
- **Tags:** `nation-state`, `data-breach`
- **Summary:** A cyberattack on LA Metro initially claimed by a hacktivist group has been attributed to Iranian government threat actors via infrastructure analysis. The use of hacktivist fronts to obscure state-sponsored operations is an established Iranian tradecraft pattern.

### 5. FBI Warns: Silent Ransom Group Sends Physical Operatives to Insert USB Drives at Law Firms
- **Source:** SecurityWeek — https://www.securityweek.com/fbi-hackers-sending-operatives-in-person-to-insert-usb-drives-and-steal-data/
- **Severity:** high
- **Tags:** `ransomware`, `malware`, `phishing`
- **Summary:** The FBI issued an alert warning that the Silent Ransom Group is dispatching physical operatives to law firm offices to manually insert USB drives and steal data. The hybrid physical-digital technique bypasses network-layer defenses entirely.

### 6. Anthropic Releases Claude Sandbox and Security Guidance Plugin for Developers
- **Source:** SecurityWeek — https://www.securityweek.com/anthropic-releases-new-claude-sandbox-security-guidance-plugin/
- **Severity:** medium
- **Tags:** `anthropic`, `appsec`, `devsecops`, `llm`
- **Summary:** Anthropic released a Claude Sandbox environment and a security guidance plugin that helps developers identify vulnerabilities during code writing, used extensively internally before public release.

### 7. GlassWorm Botnet Dismantled: All Four C2 Channels Taken Down
- **Source:** SecurityWeek — https://www.securityweek.com/glassworm-botnet-disrupted/
- **Severity:** medium
- **Tags:** `malware`, `botnet`
- **Summary:** Security firms coordinated the simultaneous takedown of all four C2 channels used by GlassWorm malware, disrupting botnet operations and preventing operator rerouting to backup infrastructure.

### 8. Cisco Talos Releases EvidenceForge for Realistic Synthetic Security Log Generation
- **Source:** Cisco Talos — https://blog.talosintelligence.com/introducing-evidenceforge-synthetic-security-logs-that-dont-look-as-fake/
- **Severity:** medium
- **Tags:** `devsecops`, `appsec`
- **Summary:** Cisco Talos released EvidenceForge, a tool generating high-quality synthetic security logs across multiple formats for SOC training and detection model validation without requiring real incident data.

### 9. AI-Assisted Bug Reports Are Overwhelming the curl Security Team
- **Source:** Simon Willison — https://simonwillison.net/2026/May/26/the-pressure/#atom-everything
- **Severity:** medium
- **Tags:** `llm`, `vulnerability`, `appsec`
- **Summary:** curl project lead Daniel Stenberg reports security bug reports arriving at 4-5x the 2024 rate, driven by AI-assisted research at over one report per day. The volume signals a broader shift in open-source vulnerability research and is creating unsustainable maintainer pressure.

## Skippable

- **The Credential Crisis: How Stolen Credentials Defeat Modern Security** — SecurityWeek. Editorial analysis piece with no specific incident, CVE, or novel technique.
- **CISA gives feds 4 days to patch actively exploited cPanel plugin flaw** — BleepingComputer. Duplicate coverage of the LiteSpeed cPanel zero-day (item 1 above).
- **Dutch police arrests suspect linked to Ajax football club hack** — BleepingComputer. Single-organization arrest with no technical detail or broader relevance.
- **Windows 11 KB5089573 update released with performance improvements** — BleepingComputer. Routine cumulative update with no critical CVE disclosures.
- **Quoting Kyle Ferrana** — Simon Willison. Social media commentary with no news or technical substance.
- **Did the Pope use AI to write about the dangers of AI?** — The Verge AI. Cultural/opinion piece on AI authorship detection with no technical security angle.
- **DuckDuckGo installs are up 30% as users reject being 'force-fed' Google's AI Search** — TechCrunch AI. Consumer behavior story with no security or technical AI signal.
