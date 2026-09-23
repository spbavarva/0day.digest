# Digest — 2026-09-23 PM

- Window: last 14h
- Raw items considered: 26
- Relevant: 9
- Skippable: 17

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** F5 Patches BIG-IP APM Zero-Day Exploited for Unauthenticated RCE — `2026-09-23-f5-big-ip-apm-zero-day-cve-2026-94127.md`
- [x] **[CRITICAL]** Chinese Hackers Chain Chrome-Windows Zero-Days to Deploy CLEANGULP Malware — `2026-09-23-uta0565-chrome-windows-zero-day-cleangulp.md`
- [x] **[CRITICAL]** Check Point Patches Exploited Management Server Zero-Day — `2026-09-23-check-point-management-server-zero-day.md`
- [x] **[CRITICAL]** Arista Urges Immediate Patching of Exploited VCO Zero-Day — `2026-09-23-arista-vco-zero-day-exploited.md`
- [x] **[HIGH]** Adobe Patches Critical Flaws in Connect, AEM Forms — `2026-09-23-adobe-connect-aem-forms-critical-flaws.md`
- [x] **[HIGH]** Critical Next.js ImageResponse Flaw Enables Server RCE via Crafted SVG — `2026-09-23-nextjs-imageresponse-rce-svg.md`
- [x] **[MEDIUM]** Microsoft Disrupts AI-Powered Phishing Platform EvilTokens — `2026-09-23-microsoft-disrupts-eviltokens-ai-phishing.md`
- [x] **[INFORMATIONAL]** OpenAI Extends Daybreak Cyber Program to Ukraine for Civilian Defense — `2026-09-23-openai-daybreak-ukraine-cyber-defense.md`
- [x] **[INFORMATIONAL]** Anthropic Releases Claude Opus 5.5 Amid New Model Price War — `2026-09-22-claude-opus-5-5-launch.md`

## Relevant (details)

### 1. F5 Patches BIG-IP APM Zero-Day Exploited for Unauthenticated RCE
- **Source:** The Hacker News — https://thehackernews.com/2026/09/f5-patches-critical-big-ip-apm-zero-day.html
- **Severity:** critical
- **Tags:** `zero-day`, `rce`, `cve`
- **Summary:** F5 disclosed CVE-2026-94127, a critical unauthenticated RCE flaw in BIG-IP APM affecting systems where APM serves as an OAuth authorization server. It is under active exploitation; F5 has released engineering hotfixes.

### 2. Chinese Hackers Chain Chrome-Windows Zero-Days to Deploy CLEANGULP Malware
- **Source:** The Hacker News — https://thehackernews.com/2026/09/chinese-hackers-exploit-chrome-windows.html
- **Severity:** critical
- **Tags:** `zero-day`, `rce`, `malware`
- **Summary:** Chinese threat actor UTA0565 chained two Chrome zero-days (CVE-2026-85046, CVE-2026-87491) with a Windows ALPC flaw (CVE-2026-85880) via fake websites to deploy CLEANGULP malware. Attacks were detected September 3–4, 2026.

### 3. Check Point Patches Exploited Management Server Zero-Day
- **Source:** SecurityWeek — https://www.securityweek.com/check-point-patches-exploited-management-server-zero-day/
- **Severity:** critical
- **Tags:** `zero-day`, `rce`, `vulnerability`
- **Summary:** Check Point patched a critical, actively exploited zero-day in its management server that let unauthenticated attackers upload and execute arbitrary scripts.

### 4. Arista Urges Immediate Patching of Exploited VCO Zero-Day
- **Source:** SecurityWeek — https://www.securityweek.com/arista-urges-immediate-patching-of-exploited-vco-zero-day/
- **Severity:** critical
- **Tags:** `zero-day`, `privilege-escalation`
- **Summary:** Arista is urging immediate patching of a critical, actively exploited zero-day in its VCO platform that lets remote attackers reach privileged internal functionality.

### 5. Adobe Patches Critical Flaws in Connect, AEM Forms
- **Source:** SecurityWeek — https://www.securityweek.com/adobe-patches-critical-flaws-in-connect-aem-forms/
- **Severity:** high
- **Tags:** `vulnerability`, `rce`, `privilege-escalation`
- **Summary:** Adobe patched nine critical defects in Connect and AEM Forms that could enable arbitrary code execution and privilege escalation. No active exploitation reported.

### 6. Critical Next.js ImageResponse Flaw Enables Server RCE via Crafted SVG
- **Source:** The Hacker News — https://thehackernews.com/2026/09/critical-nextjs-imageresponse-flaw-can.html
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `appsec`
- **Summary:** A critical flaw in Next.js's ImageResponse feature can lead to server-side code execution when apps feed attacker-controlled input into generated images. Vercel fixed it September 22.

### 7. Microsoft Disrupts AI-Powered Phishing Platform EvilTokens
- **Source:** SecurityWeek — https://www.securityweek.com/ai-powered-phishing-platform-eviltokens-disrupted-by-microsoft/
- **Severity:** medium
- **Tags:** `phishing`, `ai-safety`, `malware`
- **Summary:** Microsoft disrupted EvilTokens, a phishing-as-a-service platform that used AI at every step of the attack chain, including writing social engineering messages and picking targets.

### 8. OpenAI Extends Daybreak Cyber Program to Ukraine for Civilian Defense
- **Source:** OpenAI Blog — https://openai.com/index/openai-extends-cyber-access-to-ukraine-for-civilian-defense
- **Severity:** informational
- **Tags:** `openai`, `ai-safety`
- **Summary:** OpenAI is extending its Daybreak program to the Government of Ukraine to support cyber defense of civilian infrastructure.

### 9. Anthropic Releases Claude Opus 5.5 Amid New Model Price War
- **Source:** Simon Willison — https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `anthropic`
- **Summary:** Anthropic released Claude Opus 5.5 the same day OpenAI shipped GPT-6 Sol and Luna at roughly half their prior prices, part of a rapid wave of model releases this week.

## Skippable

- **UAE, Saudi Arabia Face Onslaught of Increasingly Complex Cyberattacks** — Dark Reading. Generic regional threat-landscape stats, no technical detail or TTPs.
- **Honeywell: OT Security Teams Embrace AI, but Autonomy Still Rare** — SecurityWeek. Vendor survey content, no security substance.
- **Microsoft: September Windows updates break Always On VPN connections** — BleepingComputer. Functional regression, not a security vulnerability.
- **OpenAI nabs key Patreon execs ahead of upcoming announcement** — The Verge AI. Personnel/business news, no model or security substance.
- **Chrome 154 Patches 108 Vulnerabilities** — SecurityWeek. Routine patch release with no confirmed active exploitation beyond the zero-day chain already covered above.
- **A Look at AI Doomsday Scenarios That Researchers Say Could Put Humanity at Risk** — SecurityWeek. Opinion/analysis piece, no news event.
- **Outerlimit Raises $16 Million to Stop Rogue AI Agents From Causing Harm** — SecurityWeek. Pre-seed funding announcement, thin technical detail.
- **Ryuk ransomware member sentenced to 24 months in prison** — BleepingComputer. Legal sentencing, no new TTPs or IOCs.
- **Critical F5 BIG-IP Vulnerability Exploited as Zero-Day** — SecurityWeek. Duplicate coverage of the F5 BIG-IP APM zero-day (CVE-2026-94127), covered above via The Hacker News.
- **F5 patches BIG-IP APM zero-day flaw exploited in RCE attacks** — BleepingComputer. Duplicate coverage of the same F5 zero-day.
- **ShinyHunters Claims FBI Hack, Demands Retraction of Threat Report** — SecurityWeek. Follow-up drama with no new technical detail; underlying breach claim already covered.
- **ShinyHunters Claims FBI Breach, Says It Stole Data on Agents and Job Applicants** — The Hacker News. Duplicate of the FBI/PeopleSoft breach claim already published yesterday.
- **'We're already fighting yesterday's battle': Greece's prime minister gets candid about AI** — TechCrunch AI. Opinion/interview piece, no news value.
- **SF October 14th: A Birds of a Feather Session on Agentic Engineering** — Simon Willison. Event announcement, not news.
- **OpenAI wants to consult elite mathematicians about how to not fumble again** — The Verge AI. Analysis/PR piece, no concrete technical or safety incident detail.
- **Grab and OpenAI bring practical AI skills to Southeast Asia** — OpenAI Blog. Non-security business partnership/marketing.
- **TechCrunch Founder Summit's agenda revealed** — TechCrunch AI. Event/marketing content.
