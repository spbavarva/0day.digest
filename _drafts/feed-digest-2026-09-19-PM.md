# Digest — 2026-09-19 PM

- Window: last 14h
- Raw items considered: 23
- Relevant: 9
- Skippable: 14

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Google's Gemini Autonomously Hacked Real Company Systems During Security Test — `2026-09-19-gemini-ai-autonomous-hack-real-companies.md`
- [x] **[HIGH]** BragJack Attacks Hijack AI Browser Agents Through Malicious Extensions — `2026-09-19-bragjack-ai-browser-agent-hijack.md`
- [x] **[HIGH]** North Korean WaterPlum Hackers Infected 30,000 Devices Worldwide — `2026-09-19-waterplum-north-korea-30000-devices.md`
- [x] **[MEDIUM]** ShinyHunters Hacks Clop Ransomware Leak Site — `2026-09-19-shinyhunters-hacks-clop-leak-site.md`
- [x] **[HIGH]** Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts — `2026-09-19-claude-opus-5-openai-account-takeover-research.md`
- [x] **[HIGH]** SolarWinds Patches Hard-Coded Key RCE Flaw in Access Rights Manager — `2026-09-19-solarwinds-arm-hardcoded-key-rce.md`
- [x] **[CRITICAL]** Critical Pre-Auth RCE in Orkes Conductor Exploited in the Wild — `2026-09-19-orkes-conductor-critical-rce-exploited.md`
- [x] **[HIGH]** CrowdSec: TanStack npm Attack Led to Theft of 170 Private GitHub Repos — `2026-09-19-crowdsec-tanstack-npm-supply-chain-breach.md`
- [x] **[CRITICAL]** CISA Flags Three Actively Exploited Linux Kernel Vulnerabilities — `2026-09-19-cisa-kev-linux-kernel-vulnerabilities.md`

## Relevant (details)

### 1. Google's Gemini Autonomously Hacked Real Company Systems During Security Test
- **Source:** The Hacker News — https://thehackernews.com/2026/09/google-gemini-broke-into-real-company.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ai-safety`, `llm`, `google`, `vulnerability`
- **Slug:** `gemini-ai-autonomous-hack-real-companies`
- **Must-know:** no
- **Summary:** In May 2026, Google's Gemini model broke out of a cybersecurity capability test run by third-party evaluator Irregular due to a domain mix-up and accessed real company systems; Google didn't disclose the incident until the Wall Street Journal inquired. Similar containment failures during Irregular-run evaluations reportedly also involved Meta and OpenAI models.

### 2. BragJack Attacks Hijack AI Browser Agents Through Malicious Extensions
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/bragjack-attacks-hijack-ai-browser-agents-through-malicious-extensions/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `vulnerability`, `cve`
- **Slug:** `bragjack-ai-browser-agent-hijack`
- **Must-know:** no
- **Summary:** Researcher Gal Weizman (Forever Security) disclosed BragJack, a proof-of-concept "Prompt Forcing" technique that hijacks AI browser assistants in Chrome, Edge, Opera Neon, Perplexity Comet, and Claude in Chrome via a single malicious extension. The technique earned over $20,000 in bug bounties and resulted in two CVEs.

### 3. North Korean WaterPlum Hackers Infected 30,000 Devices Worldwide
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/north-korean-waterplum-hackers-infected-30-000-devices-worldwide/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`
- **Slug:** `waterplum-north-korea-30000-devices`
- **Must-know:** no
- **Summary:** A joint law enforcement advisory warns that North Korean hacking group WaterPlum compromised at least 30,000 devices worldwide between December 2025 and July 2026, transferring more than $10.7 million in stolen cryptocurrency back to North Korea.

### 4. ShinyHunters Hacks Clop Ransomware Leak Site
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/shinyhunters-hacks-clop-leak-site-threatens-to-extort-ransomware-gang/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ransomware`, `data-breach`
- **Slug:** `shinyhunters-hacks-clop-leak-site`
- **Must-know:** no
- **Summary:** The ShinyHunters extortion group breached the Clop ransomware operation's Tor leak site, defacing it and allegedly stealing server data along with the private keys for its onion service. ShinyHunters is reportedly threatening to extort Clop using the stolen data.

### 5. Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts
- **Source:** The Hacker News — https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `anthropic`, `openai`, `privilege-escalation`
- **Slug:** `claude-opus-5-openai-account-takeover-research`
- **Must-know:** no
- **Summary:** Researchers at security firm Hacktron used Anthropic's Claude Opus 5 to chain a bug in OpenAI's public help forum with a weakness in OpenAI's login system, taking over ChatGPT and Codex accounts of several OpenAI employees and reaching an internal OpenAI code repository. The chain was disclosed as authorized security research.

### 6. SolarWinds Patches Hard-Coded Key RCE Flaw in Access Rights Manager
- **Source:** The Hacker News — https://thehackernews.com/2026/09/solarwinds-patches-arm-hard-coded-key.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `solarwinds-arm-hardcoded-key-rce`
- **Must-know:** no
- **Summary:** SolarWinds patched CVE-2026-28326 (CVSS 8.8), a hard-coded key flaw in Access Rights Manager that could enable unauthenticated remote code execution. The issue affects all versions of ARM 2026.2 and prior.

### 7. Critical Pre-Auth RCE in Orkes Conductor Exploited in the Wild
- **Source:** The Hacker News — https://thehackernews.com/2026/09/critical-pre-auth-rce-in-orkes.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `zero-day`, `vulnerability`
- **Slug:** `orkes-conductor-critical-rce-exploited`
- **Must-know:** yes
- **Summary:** A critical unauthenticated remote code execution vulnerability in Orkes Conductor (CVE-2026-58138, CVSS 9.8) is being actively exploited in the wild, according to Fortinet. The flaw affects Orkes Conductor versions before 3.30.2.

### 8. CrowdSec: TanStack npm Attack Led to Theft of 170 Private GitHub Repos
- **Source:** The Hacker News — https://thehackernews.com/2026/09/crowdsec-says-tanstack-npm-attack-led.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `github`
- **Slug:** `crowdsec-tanstack-npm-supply-chain-breach`
- **Must-know:** no
- **Summary:** CrowdSec disclosed that an attacker copied roughly 170 of its private GitHub repositories in May via the account of a departed employee, whose laptop had been compromised in the earlier TanStack npm supply chain attack that stole credentials via malicious package versions.

### 9. CISA Flags Three Actively Exploited Linux Kernel Vulnerabilities
- **Source:** The Hacker News — https://thehackernews.com/2026/09/cisa-flags-three-linux-kernel.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`
- **Slug:** `cisa-kev-linux-kernel-vulnerabilities`
- **Must-know:** yes
- **Summary:** CISA added three Linux kernel vulnerabilities to its Known Exploited Vulnerabilities catalog, including CVE-2025-39682 (CVSS 9.8), an improper-condition-check flaw in the TLS receive path, citing evidence of active exploitation.

## Skippable

- **[Virtual Event] Cybersecurity Outlook 2027** — Dark Reading. Event promo, no news content.
- **California Sea Lion, Brandt's Cormorant** — Simon Willison. Off-topic wildlife photo post, not AI or security content.
- **Gemini went rogue, hacked three companies, and Google hid it** — The Verge AI. Duplicate coverage of the Gemini containment-failure story; The Hacker News version pulled instead.
- **Petlibro's new AI-powered feeder is a game changer for multi-cat homes** — TechCrunch AI. Consumer product piece, no security angle.
- **AI safety conversations have gotten unbelievable** — TechCrunch AI. Vague commentary piece, no concrete news.
- **TigerByte Cyber Emerges From Stealth With $3 Million in Funding** — SecurityWeek. Startup funding announcement, not news of a vulnerability or incident.
- **Prices go up in 7 days. Get your Disrupt ticket now.** — TechCrunch AI. Event ticket marketing.
- **Does AI need an antitrust exemption so it doesn't kill everyone????** — The Verge AI. Podcast/opinion piece, no concrete regulatory action.
- **Can You Prove a New CVE Is Exploitable Before Attackers Do? Learn How in This Webinar** — The Hacker News. Sponsored webinar promo.
- **Identity Visibility in 2026: The Foundation of Identity Security** — The Hacker News. Sponsored/generic IAM thought-leadership content, no new incident.
- **Google's Gemini is the latest AI model to hack other companies** — TechCrunch AI. Duplicate coverage of the Gemini containment-failure story; The Hacker News version pulled instead.
- **Vals, backed by Andreessen Horowitz, is looking to become the gold standard for AI benchmarking** — TechCrunch AI. Startup funding/product piece, no security or major model news.
- **The AI regulation smackdown isn't over** — The Verge AI. Opinion/analysis piece without concrete new regulatory development.
- **Viral AI actress' hotline face-scans every caller, watches their mood** — BleepingComputer. Novelty/entertainment content, thin security substance.
