# Digest — 2026-07-09 AM

- Window: last 14h
- Raw items considered: 23
- Relevant: 11
- Skippable: 12

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** 'GodDamn' Ransomware Uses Signed Malicious Driver to Kill Security Software — `2026-07-09-goddamn-ransomware-byovd-signed-driver.md`
- [x] **[HIGH]** Microsoft Patches RoguePlanet Defender Privilege Escalation Flaw — `2026-07-09-microsoft-defender-rogueplanet-cve-2026-50656.md`
- [x] **[HIGH]** AssuranceAmerica Data Breach Exposes 6.9 Million Drivers' Records — `2026-07-09-assuranceamerica-data-breach-6-9-million-drivers.md`
- [x] **[INFORMATIONAL]** Meta's Muse Image Tool Lets Others Use Public Instagram Photos in AI Generations — `2026-07-09-meta-muse-image-instagram-photos-ai.md`
- [x] **[HIGH]** 'Friendly Fire' Attack Tricks AI Code-Review Agents Into Running Malicious Code — `2026-07-09-friendly-fire-ai-coding-agents-malicious-code.md`
- [x] **[HIGH]** Unpatched Backdoor in Tenda Firmware Grants Unauthenticated Admin Access — `2026-07-09-tenda-firmware-unpatched-backdoor-cve-2026-11405.md`
- [x] **[HIGH]** GhostApproval Symlink Flaw Lets Malicious Repos Hijack AI Coding Agents — `2026-07-09-ghostapproval-symlink-ai-coding-agents.md`
- [x] **[MEDIUM]** Fake 7-Zip Installers Turn Victim Devices Into Residential Proxy Nodes — `2026-07-09-fake-7zip-installers-lurking-lizard-proxy.md`
- [x] **[INFORMATIONAL]** OpenAI Launches GPT-Live, New Model Behind ChatGPT Voice Mode — `2026-07-09-openai-gpt-live-chatgpt-voice-mode.md`
- [x] **[INFORMATIONAL]** Google's Deepfake Detection System Debunks Viral McConnell Hoax Image — `2026-07-09-google-deepfake-detector-mcconnell-hoax.md`
- [x] **[HIGH]** Lone Attacker Uses AI to Breach AWS Cloud Environment in 72 Hours — `2026-07-09-lone-attacker-ai-aws-cloud-breach-extortion.md`

## Relevant (details)

### 1. 'GodDamn' Ransomware Uses Signed Malicious Driver to Kill Security Software
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/goddamn-ransomware-byovd-smite-companies
- **Severity:** high
- **Tags:** `ransomware`, `malware`, `privilege-escalation`
- **Summary:** Ransomware operators are abusing a Microsoft-co-signed kernel driver (BYOVD) to kill security software on US company networks before deploying ransomware. The signed driver bypasses typical trust checks, reducing detection risk during the attack.

### 2. Microsoft Patches RoguePlanet Defender Privilege Escalation Flaw
- **Source:** The Hacker News — https://thehackernews.com/2026/07/microsoft-patches-rogueplanet-defender.html
- **Severity:** high
- **Tags:** `microsoft`, `vulnerability`, `cve`, `privilege-escalation`
- **Summary:** Microsoft patched CVE-2026-50656 ("RoguePlanet"), a CVSS 7.8 privilege escalation flaw in the Malware Protection Engine (mpengine.dll) that can grant SYSTEM privileges. The fix landed nearly a month after details became public.

### 3. AssuranceAmerica Data Breach Exposes 6.9 Million Drivers' Records
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/assuranceamerica-data-breach-exposes-records-of-69-million-drivers/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** Insurance company AssuranceAmerica disclosed a breach affecting nearly 7 million drivers after attackers gained access to its systems earlier this year. Specific data types exposed were not detailed in initial disclosures.

### 4. Meta's Muse Image Tool Lets Others Use Public Instagram Photos in AI Generations
- **Source:** The Hacker News — https://thehackernews.com/2026/07/metas-new-ai-image-tool-lets-others-use.html
- **Severity:** informational
- **Tags:** `ai-safety`, `meta`
- **Summary:** Meta's new Muse Image model lets users generate AI images referencing public Instagram accounts, enabled by default rather than opt-in. This raises consent questions since public Instagram users are included without a separate opt-in for this specific use.

### 5. 'Friendly Fire' Attack Tricks AI Code-Review Agents Into Running Malicious Code
- **Source:** The Hacker News — https://thehackernews.com/2026/07/friendly-fire-ai-agents-built-to-catch.html
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `rce`, `anthropic`, `openai`
- **Summary:** The AI Now Institute published a PoC showing that autonomous, self-approving AI code-review agents (Claude Code, OpenAI Codex) can be tricked into executing an attacker's malicious code instead of just scanning it. The attack targets agents running in modes that approve their own actions.

### 6. Unpatched Backdoor in Tenda Firmware Grants Unauthenticated Admin Access
- **Source:** SecurityWeek — https://www.securityweek.com/unpatched-backdoor-in-tenda-firmware-grants-admin-access-to-devices/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Summary:** CVE-2026-11405 lets unauthenticated attackers access the web management interface of affected Tenda firmware devices. No patch is currently available.

### 7. GhostApproval Symlink Flaw Lets Malicious Repos Hijack AI Coding Agents
- **Source:** The Hacker News — https://thehackernews.com/2026/07/ghostapproval-symlink-flaws-could-let.html
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `rce`, `anthropic`, `aws`
- **Summary:** Wiz disclosed a symlink-based flaw ("GhostApproval") affecting six AI coding assistants — Amazon Q Developer, Claude Code, Augment, Cursor, Google Antigravity, and Windsurf — where an approved edit to one file is silently redirected to overwrite a sensitive file. A malicious repo can use this to take control of a developer's machine despite the approval prompt.

### 8. Fake 7-Zip Installers Turn Victim Devices Into Residential Proxy Nodes
- **Source:** The Hacker News — https://thehackernews.com/2026/07/fake-7-zip-installers-turn-devices-into.html
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** A threat actor dubbed "Lurking Lizard" runs a residential proxy business using fake 7-Zip installers distributed via 230+ lookalike domains, with infrastructure dating back to at least August 2022 according to Infoblox.

### 9. OpenAI Launches GPT-Live, New Model Behind ChatGPT Voice Mode
- **Source:** Simon Willison — https://simonwillison.net/2026/Jul/8/introducing-gptlive/#atom-everything
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `openai`, `llm`
- **Summary:** OpenAI upgraded the model behind ChatGPT voice mode to GPT-Live, which can delegate harder requests to GPT-5.5 in the background while keeping the conversation flowing. No security or safety disclosures accompanied the launch.

### 10. Google's Deepfake Detection System Debunks Viral McConnell Hoax Image
- **Source:** TechCrunch AI — https://techcrunch.com/2026/07/08/googles-deepfake-detector-system-used-to-debunk-mcconnell-hoax-pic/
- **Severity:** informational
- **Tags:** `ai-safety`, `google`
- **Summary:** A viral image purporting to show Senator Mitch McConnell in medical distress was confirmed as an AI-generated fake using Google's deepfake detection system, a practical example of detection tooling countering AI-generated misinformation.

### 11. Lone Attacker Uses AI to Breach AWS Cloud Environment in 72 Hours
- **Source:** Dark Reading — https://www.darkreading.com/cloud-security/lone-attacker-ai-breach-aws-cloud-environment
- **Severity:** high
- **Tags:** `cloud-security`, `aws`, `ai-safety`, `llm`
- **Summary:** A single attacker combined AI workflows with chained cloud misconfigurations and stolen credentials to breach a large Amazon customer's AWS environment within 72 hours, then used the access to extort the victim.

## Skippable

- **Mount Royal University Confirms Data Stolen in Ransomware Attack** — SecurityWeek. Ransomware victim disclosure without new TTPs/IOCs; duplicate of the BleepingComputer item below.
- **Police arrests 5,800 suspects in global anti-fraud crackdown** — BleepingComputer. Law enforcement operation summary with no technical detail or practitioner guidance.
- **AI Coding Tools Tricked Into Hacking Developer Machine via Decades-Old Technique** — SecurityWeek. Duplicate coverage of the GhostApproval story; The Hacker News item has more technical detail (affected tools, symlink mechanism) and was drafted instead.
- **European Organizations Have a Collaboration Security Confidence Gap** — Dark Reading. Survey/opinion piece, no news value.
- **Chrome 150 Update Patches 27 Vulnerabilities** — SecurityWeek. Routine browser patch release; no confirmed active exploitation of the critical-severity bugs.
- **8Layers Raises $2.9 Million for Identity Security Platform** — SecurityWeek. Funding announcement, no security substance.
- **Microsoft patches RoguePlanet Defender zero-day vulnerability** — BleepingComputer. Duplicate coverage of the RoguePlanet story; The Hacker News item has the CVE number and CVSS score and was drafted instead.
- **Rewriting Bun in Rust** — Simon Willison. General engineering blog post, no security or AI safety angle.
- **Lovable reportedly in talks to double its valuation to $13.2B** — TechCrunch AI. Funding/valuation news, no security angle.
- **Mexico's New Cyber Plan Faces Its First Real Test** — Dark Reading. Regional policy narrative piece, no new technical substance.
- **Mount Royal University confirms breach as hackers claim attack** — BleepingComputer. Duplicate of the SecurityWeek item above; ransomware victim disclosure without TTPs/IOCs.
- **Greek victims file lawsuit against Intellexa over Predator spyware** — The Record. Revisits a 2022 spyware scandal via a new legal filing; no new technical detail.
