# Digest — 2026-06-17 AM

- Window: last 14h
- Raw items considered: 26
- Relevant: 8
- Skippable: 18

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** 144 Mastra npm Packages Compromised in Supply Chain Attack — `2026-06-17-mastra-npm-supply-chain-attack.md`
- [x] **[CRITICAL]** CISA Adds Actively Exploited Joomla JCE Flaw to KEV Catalog — `2026-06-17-joomla-jce-cve-2026-48907-kev.md`
- [x] **[HIGH]** Microsoft Working on Patch for 'RoguePlanet' Zero-Day — `2026-06-17-rogueplanet-defender-zero-day.md`
- [x] **[HIGH]** Malicious JetBrains Plugins Steal AI API Keys, Chrome Extensions Capture Chatbot Chats — `2026-06-17-jetbrains-marketplace-malicious-plugins-ai-keys.md`
- [x] **[HIGH]** Chrome and Firefox Patch Critical Memory Safety Bugs — `2026-06-17-chrome-firefox-critical-patches-june-2026.md`
- [x] **[MEDIUM]** Fileless 'Phantom Stealer' Targets Browser Credentials — `2026-06-16-phantom-stealer-fileless-browser-credentials.md`
- [x] **[INFORMATIONAL]** Zhipu Releases GLM-5.2 for Long-Horizon Tasks — `2026-06-17-glm-5-2-long-horizon-release.md`
- [x] **[INFORMATIONAL]** Security Community Pushes Back on US Export Ban for Anthropic's Mythos, Fable — `2026-06-16-security-community-anthropic-export-ban.md`

## Relevant (details)

### 1. 144 Mastra npm Packages Compromised in Supply Chain Attack
- **Source:** The Hacker News — https://thehackernews.com/2026/06/144-mastra-npm-packages-compromised-via.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `llm`, `malware`
- **Slug:** `mastra-npm-supply-chain-attack`
- **Must-know:** yes
- **Summary:** A hijacked npm account mass-published malicious versions of 144 packages in the "@mastra/*" namespace, used by the open-source Mastra AI application framework. JFrog, SafeDep, Socket, and StepSecurity jointly tracked the compromise, codenamed "easy-day-js."

### 2. CISA Adds Actively Exploited Joomla JCE Flaw to KEV Catalog
- **Source:** The Hacker News — https://thehackernews.com/2026/06/cisa-warns-of-actively-exploited-joomla.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `rce`
- **Slug:** `joomla-jce-cve-2026-48907-kev`
- **Must-know:** no
- **Summary:** CISA added CVE-2026-48907 (CVSS 10.0), an improper access control flaw in the Widget Factory Joomla Content Editor (JCE) plugin, to its KEV catalog citing active exploitation. Federal agencies have been given until Friday to patch.

### 3. Microsoft Working on Patch for 'RoguePlanet' Zero-Day
- **Source:** SecurityWeek — https://www.securityweek.com/microsoft-working-on-patch-for-rogueplanet-zero-day/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `privilege-escalation`, `microsoft`
- **Slug:** `rogueplanet-defender-zero-day`
- **Must-know:** no
- **Summary:** Public PoC code exploits a race condition in Microsoft Defender to spawn a SYSTEM-privileged command prompt. Microsoft has not yet shipped a patch.

### 4. Malicious JetBrains Plugins Steal AI API Keys, Chrome Extensions Capture Chatbot Chats
- **Source:** The Hacker News — https://thehackernews.com/2026/06/malicious-jetbrains-plugins-steal-ai.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `llm`
- **Slug:** `jetbrains-marketplace-malicious-plugins-ai-keys`
- **Must-know:** no
- **Summary:** At least 15 malicious JetBrains Marketplace plugins posing as DeepSeek-based AI coding assistants exfiltrate AI provider API keys; companion malicious Chrome extensions capture chatbot conversation logs.

### 5. Chrome and Firefox Patch Critical Memory Safety Bugs
- **Source:** SecurityWeek — https://www.securityweek.com/chrome-and-firefox-updated-to-patch-critical-high-severity-vulnerabilities/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `chrome-firefox-critical-patches-june-2026`
- **Must-know:** no
- **Summary:** Google and Mozilla shipped fixes for multiple critical and high-severity memory safety bugs that could potentially lead to remote code execution.

### 6. Fileless 'Phantom Stealer' Targets Browser Credentials
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/fileless-phantom-stealer-targets-browser-credentials
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `phantom-stealer-fileless-browser-credentials`
- **Must-know:** no
- **Summary:** A newly identified fileless malware strain targets browser-stored credentials, executing entirely in memory with added anti-analysis techniques to evade detection.

### 7. Zhipu Releases GLM-5.2 for Long-Horizon Tasks
- **Source:** Hugging Face Blog — https://huggingface.co/blog/zai-org/glm-52-blog
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `llm`
- **Slug:** `glm-5-2-long-horizon-release`
- **Must-know:** no
- **Summary:** Zhipu (Z.ai) released GLM-5.2, positioned for long-horizon, multi-step agentic tasks. Announced via Hugging Face's blog, one of the few RSS-trackable channels for this lab.

### 8. Security Community Pushes Back on US Export Ban for Anthropic's Mythos, Fable
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/security-community-slams-us-ban-on-exporting-mythos-fable
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `anthropic`, `export-controls`
- **Slug:** `security-community-anthropic-export-ban`
- **Must-know:** no
- **Summary:** Dozens of security researchers signed an open letter urging the US government to reverse export restrictions on Anthropic's Claude Fable 5 and Mythos 5 models, arguing the ban hampers security research relying on frontier model access.

## Skippable

- **Microsoft Teams Relay Servers Abused in DragonForce Ransomware Attack** — SecurityWeek. Duplicate coverage of the DragonForce/Teams-relay C2 story already published 2026-06-16.
- **The Top 10 Attack Surface Exposures in 2026** — The Hacker News. Generic trend listicle, no single news event.
- **From the Hugging Face Hub to robot hardware with Strands Agents and LeRobot** — Hugging Face Blog. Integration tutorial, not news.
- **CISA orders feds to patch max severity Joomla plugin flaw by Friday** — BleepingComputer. Duplicate coverage of the Joomla JCE CVE-2026-48907 story (see drafted item).
- **The next humanoid robot might not look human at all** — The Verge AI. Product feature piece, no model-launch or security substance.
- **Oracle's Second Monthly Security Updates Deliver 245 Patches** — SecurityWeek. Routine patch bundle; no single critical+exploited CVE called out.
- **UK Social Media Ban for Minors Has Privacy Experts Worried** — Dark Reading. General privacy/policy debate, not AI- or security-technical.
- **From AI potential to agentic reality: Driving the UK's next chapter** — Google Cloud Security. Summit/partnership PR piece.
- **Joomla, LiteSpeed Vulnerabilities Exploited in Attacks** — SecurityWeek. Duplicate coverage of the Joomla JCE story (see drafted item).
- **Kodak confirms data breach claimed by ShinyHunters extortion gang** — BleepingComputer. Breach disclosure without technical detail or confirmed scale.
- **3 Recently Patched Fortinet FortiSandbox Vulnerabilities in Hacker Crosshairs** — SecurityWeek. Continuation/duplicate of the FortiSandbox story already published 2026-06-16.
- **<click-to-play> — a still that plays** — Simon Willison. Web component tool post, no security/AI substance.
- **NetNewsWire Status** — Simon Willison. Software retirement retrospective, not relevant.
- **Amazon S3 annotations: attach rich, queryable context directly to your objects** — AWS News Blog. Feature launch with no stated security implications.
- **Anthropic's latest feud with the Trump admin may actually help it, sales data suggests** — TechCrunch AI. Business/sales commentary, not technical or safety news.
- **Malicious JetBrains Marketplace plugins steal AI API keys from developers** — BleepingComputer. Duplicate coverage (see drafted JetBrains/Chrome item from The Hacker News).
- **datasette 1.0a34** — Simon Willison. Dev tool release note, no security/AI safety angle.
- **Unlocking UK house-building with AI-accelerated planning** — Google DeepMind. Government partnership PR piece.
