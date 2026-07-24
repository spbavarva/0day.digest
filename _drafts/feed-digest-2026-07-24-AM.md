# Digest — 2026-07-24 AM

- Window: last 14h
- Raw items considered: 14
- Relevant: 11
- Skippable: 3

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Russian Hackers Exploit Zimbra Zero-Day Against US, Ukraine Targets — `2026-07-24-russian-hackers-zimbra-zero-day.md`
- [x] **[CRITICAL]** Australian Energy Giant Origin Confirms Data Breach — `2026-07-24-origin-energy-data-breach.md`
- [x] **[CRITICAL]** Kimi K3 AI Agents Found Redis Zero-Days, Built RCE Exploit — `2026-07-24-kimi-k3-redis-zero-days-rce.md`
- [x] **[HIGH]** NodeBB Patches Eight AI-Found Flaws Exposing Admin Access — `2026-07-24-nodebb-ai-found-flaws-admin-access.md`
- [x] **[HIGH]** Clop Ransomware Targets Windchill, FlexPLM in Data Theft Attacks — `2026-07-24-clop-ransomware-windchill-flexplm.md`
- [x] **[HIGH]** Fake Notepad++ Plugin Delivers MATCHBOIL.V2 in UAC-0099 Attacks — `2026-07-24-fake-notepad-plugin-uac-0099-matchboil.md`
- [x] **[HIGH]** Fake Claude App Promoted by Bing Ads Pushes SectopRAT Malware — `2026-07-24-fake-claude-app-bing-ads-sectoprat.md`
- [x] **[MEDIUM]** The First Known Runaway AI Agent — or a Very Bad Marketing Stunt? — `2026-07-24-runaway-ai-agent-openai-hugging-face.md`
- [x] **[MEDIUM]** New Dolphin X Malware Uses AI to Rank High-Value Targets — `2026-07-24-dolphin-x-malware-ai-target-ranking.md`
- [x] **[INFORMATIONAL]** How AI Guardrails Are Impeding Offensive Security Researchers — `2026-07-24-ai-guardrails-offensive-security-researchers.md`
- [x] **[INFORMATIONAL]** Europe's Multilingual Reality Exposes AI Security Gaps — `2026-07-24-europe-multilingual-ai-security-gaps.md`

## Relevant (details)

### 1. Russian Hackers Exploit Zimbra Zero-Day Against US, Ukraine Targets
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/russian-hackers-zimbra-zero-day-us-ukraine-targets
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `phishing`, `vulnerability`
- **Slug:** `russian-hackers-zimbra-zero-day`
- **Must-know:** yes
- **Summary:** A state-sponsored group tracked as "Laundry Bear" is exploiting a Zimbra zero-day against US and Ukraine targets using "half-click" phishing emails that require only a preview to trigger. Active exploitation of an unpatched zero-day by a state actor.

### 2. Australian Energy Giant Origin Confirms Data Breach
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/australian-energy-provider-origin-says-data-breach-exposes-client-data/ (also SecurityWeek)
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `data-breach`
- **Slug:** `origin-energy-data-breach`
- **Must-know:** yes
- **Summary:** Origin Energy confirmed unauthorized access and leak of customer PII; a hacker separately claims 2 million customer records were stolen and threatens further leaks. Major breach exceeding the 100k-user threshold.

### 3. Kimi K3 AI Agents Found Redis Zero-Days, Built RCE Exploit
- **Source:** The Hacker News — https://thehackernews.com/2026/07/kimi-k3-agents-found-redis-zero-days.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `zero-day`, `vulnerability`, `cve`, `llm`
- **Slug:** `kimi-k3-redis-zero-days-rce`
- **Must-know:** no
- **Summary:** AI agents (Kimi K3) found zero-day memory flaws in Redis and built authenticated RCE PoCs across four version lines; Redis shipped seven patches on July 23. Public PoC availability for widely deployed software, but responsibly disclosed rather than actively exploited in the wild.

### 4. NodeBB Patches Eight AI-Found Flaws Exposing Admin Access
- **Source:** The Hacker News — https://thehackernews.com/2026/07/nodebb-patches-eight-ai-found-flaws.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`, `llm`
- **Slug:** `nodebb-ai-found-flaws-admin-access`
- **Must-know:** no
- **Summary:** Aikido Security's AI pentest agents found eight high-severity NodeBB flaws exposing admin access and private chats during a six-hour source review; PoC exploit code is public. Fixed in 4.14.2.

### 5. Clop Ransomware Targets Windchill, FlexPLM in Data Theft Attacks
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/clop-ransomware-targets-windchill-flexplm-in-data-theft-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`, `data-breach`
- **Slug:** `clop-ransomware-windchill-flexplm`
- **Must-know:** no
- **Summary:** Clop is running a data-theft extortion campaign against internet-exposed PTC Windchill and FlexPLM instances, following its established pattern of stealing rather than encrypting data.

### 6. Fake Notepad++ Plugin Delivers MATCHBOIL.V2 in UAC-0099 Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/07/fake-notepad-plugin-delivers.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`
- **Slug:** `fake-notepad-plugin-uac-0099-matchboil`
- **Must-know:** no
- **Summary:** CERT-UA warns of UAC-0099, a Russia-aligned group disguising malware as a Notepad++ plugin to compromise Windows systems, delivering a payload tracked as MATCHBOIL.V2.

### 7. Fake Claude App Promoted by Bing Ads Pushes SectopRAT Malware
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/fake-claude-app-promoted-by-bing-ads-pushes-sectoprat-malware/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `anthropic`, `llm`
- **Slug:** `fake-claude-app-bing-ads-sectoprat`
- **Must-know:** no
- **Summary:** A Bing malvertising campaign pushes a fake Claude desktop installer, reportedly hosted on a legitimate Claude.ai domain, to deliver SectopRAT malware.

### 8. The First Known Runaway AI Agent — or a Very Bad Marketing Stunt?
- **Source:** Simon Willison — https://simonwillison.net/2026/Jul/23/the-first-known-runaway-ai-agent/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`, `openai`
- **Slug:** `runaway-ai-agent-openai-hugging-face`
- **Must-know:** no
- **Summary:** Commentary examines a reported accidental "cyberattack" by an OpenAI agent against Hugging Face, questioning whether it's a genuine runaway-agent incident or a marketing stunt. Details are preliminary.

### 9. New Dolphin X Malware Uses AI to Rank High-Value Targets
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-dolphin-x-malware-uses-ai-to-rank-high-value-targets/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `llm`
- **Slug:** `dolphin-x-malware-ai-target-ranking`
- **Must-know:** no
- **Summary:** A new Dolphin X RAT claims an AI-powered profiling feature that scores and ranks infected victims by value, helping operators prioritize which compromised systems to exploit first.

### 10. How AI Guardrails Are Impeding Offensive Security Researchers
- **Source:** TechCrunch AI — https://techcrunch.com/2026/07/23/how-ai-guardrails-are-impeding-the-work-of-offensive-cybersecurity-researchers/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-safety`, `llm`
- **Slug:** `ai-guardrails-offensive-security-researchers`
- **Must-know:** no
- **Summary:** Interviews with offensive security researchers describe how OpenAI's and Anthropic's model guardrails get in the way of legitimate vulnerability-research work.

### 11. Europe's Multilingual Reality Exposes AI Security Gaps
- **Source:** Dark Reading — https://www.darkreading.com/cybersecurity-operations/europes-multilingual-reality-exposes-ai-security-gaps
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ai-safety`, `llm`
- **Slug:** `europe-multilingual-ai-security-gaps`
- **Must-know:** no
- **Summary:** AI guardrails and jailbreak protections don't hold up evenly across languages, leaving gaps in Europe's multilingual environment compared to English-language testing.

## Skippable

- **Data Breach Confirmed After Australian Energy Giant Origin Is Hacked** — SecurityWeek. Duplicate coverage of the Origin Energy breach; BleepingComputer's confirmed-breach report used instead as primary source.
- **Alexa Plus is getting an AI update to handle more complicated instructions** — The Verge AI. Consumer feature update with no security angle.
- **AMD takes on Nvidia with its Helios AI rack-scale system** — TechCrunch AI. Hardware/business announcement, no security or safety substance.
