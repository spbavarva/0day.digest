# Digest — 2026-08-03 PM

- Window: last 14h
- Raw items considered: 39
- Relevant: 13
- Skippable: 26

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** N-able N-central Auth Bypass Under Active Exploitation, Initial Patch Incomplete — `2026-08-03-n-able-n-central-auth-bypass-cve-2026-18577.md`
- [x] **[HIGH]** Malware Can Hijack Passkey-Protected Google Accounts Without User Interaction — `2026-08-03-google-password-manager-passkey-attacks.md`
- [x] **[HIGH]** INC Ransomware Becomes Dominant Actor Exploiting SonicWall SMA 1000 Flaws — `2026-08-03-inc-ransomware-sonicwall-sma1000.md`
- [x] **[HIGH]** Chinese Actor Weaponizes DeepSeek AI Agent Against Security Firm — `2026-08-03-chinese-actor-deepseek-ai-agent-attack.md`
- [x] **[HIGH]** ExfilSquad Leaks Data on 100,000+ UK Police Officers From PNLD Breach — `2026-08-03-exfilsquad-pnld-uk-police-breach.md`
- [x] **[HIGH]** Chinese Threat Actor Deploys GHOSTBLADE on iOS via Leaked DarkSword Kit — `2026-08-03-ghostblade-ios-darksword-exploit-kit.md`
- [x] **[HIGH]** Midnight Blizzard Hijacks Hotel Wi-Fi Networks to Steal Microsoft Credentials — `2026-08-03-midnight-blizzard-hotel-wifi-hacking.md`
- [x] **[HIGH]** Iran-Linked Hackers Expand Water System Attacks to at Least 6 More US States — `2026-08-03-iran-linked-water-system-attacks-us-states.md`
- [x] **[HIGH]** Hugging Face Diffusers Flaws Let Malicious Model Repos Execute Arbitrary Code — `2026-08-03-hugging-face-diffusers-rce-flaws.md`
- [x] **[MEDIUM]** Inside the BTMOB Android RAT's Underground Business Model — `2026-08-03-btmob-android-rat-underground-business.md`
- [x] **[MEDIUM]** Alibaba Releases Qwen3.8-Max, Claims Frontier-Rivaling Performance — `2026-08-03-alibaba-qwen3-8-max-release.md`
- [x] **[MEDIUM]** Thermo Fisher Patches Flaw Enabling Near-Undetectable DNA File Tampering — `2026-08-03-thermo-fisher-dna-file-tampering-cve-2026-17583.md`
- [x] **[INFORMATIONAL]** EU AI Act Transparency and Labeling Rules Take Effect — `2026-08-03-eu-ai-act-transparency-labeling-rules.md`

## Relevant (details)

### 1. N-able N-central Auth Bypass Under Active Exploitation, Initial Patch Incomplete
- **Source:** The Hacker News — https://thehackernews.com/2026/08/n-able-says-attackers-take-over-n.html
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Summary:** Attackers exploited an authentication bypass (CVE-2026-18577) in N-able's N-central RMM platform to gain admin access and reach downstream customer systems; N-able's first fix was incomplete and it shipped build 2026.3.1.7 on August 2 as the first unaffected version.

### 2. Malware Can Hijack Passkey-Protected Google Accounts Without User Interaction
- **Source:** The Hacker News — https://thehackernews.com/2026/08/google-password-manager-attacks-could.html
- **Severity:** high
- **Tags:** `vulnerability`, `google`, `privilege-escalation`
- **Summary:** Unit 42 detailed three attack paths (Pass-ta-key, Silver Pass-ta-key, Golden Pass-ta-key) letting ordinary-user-level Windows malware sign into passkey-protected Google accounts with no visible prompt; the strongest variant targets the master key protecting all stored passkeys.

### 3. INC Ransomware Becomes Dominant Actor Exploiting SonicWall SMA 1000 Flaws
- **Source:** The Hacker News — https://thehackernews.com/2026/08/inc-ransomware-emerges-as-dominant.html
- **Severity:** high
- **Tags:** `ransomware`, `vulnerability`, `cve`
- **Summary:** Resecurity reports INC Ransomware is now the dominant actor exploiting recently disclosed SonicWall SMA 1000 VPN flaws for root access and lateral movement, accelerating activity since early August and listing new victims on its leak site.

### 4. Chinese Actor Weaponizes DeepSeek AI Agent Against Security Firm
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/chinese-actor-deepseek-ai-agent-attack-security-firm
- **Severity:** high
- **Tags:** `deepseek`, `malware`, `ai-safety`
- **Summary:** Researchers at Jesta intercepted a DeepSeek-based AI agent a Chinese threat actor used to attempt compromise of a security firm, observing attempts against more than 1,200 hosts for proxyjacking and further attacks.

### 5. ExfilSquad Leaks Data on 100,000+ UK Police Officers From PNLD Breach
- **Source:** The Hacker News — https://thehackernews.com/2026/08/pnld-breach-exposes-uk-police-and.html
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** A breach of the UK's Police National Legal Database, identified July 26, exposed contact data for more than 100,000 police officers, government partners, and criminal justice professionals; the ExfilSquad group published the data on the dark web.

### 6. Chinese Threat Actor Deploys GHOSTBLADE on iOS via Leaked DarkSword Kit
- **Source:** The Hacker News — https://thehackernews.com/2026/08/chinese-threat-actor-uses-leaked.html
- **Severity:** high
- **Tags:** `malware`, `vulnerability`
- **Summary:** Censys identified a Chinese-speaking actor running 100+ web properties, mostly fake AWS sign-in pages, to distribute GHOSTBLADE malware to iOS devices using a publicly leaked version of the DarkSword exploit kit.

### 7. Midnight Blizzard Hijacks Hotel Wi-Fi Networks to Steal Microsoft Credentials
- **Source:** SecurityWeek — https://www.securityweek.com/russian-state-apt-linked-to-recent-public-wi-fi-gateway-hacking/
- **Severity:** high
- **Tags:** `malware`, `privilege-escalation`
- **Summary:** Microsoft says Russian state actor Midnight Blizzard has been compromising hotel Wi-Fi networks worldwide to steal travelers' Microsoft credentials and deploy espionage malware on connected devices.

### 8. Iran-Linked Hackers Expand Water System Attacks to at Least 6 More US States
- **Source:** SecurityWeek — https://www.securityweek.com/us-water-cyberattacks-extend-beyond-minnesota-to-at-least-6-other-states/
- **Severity:** high
- **Tags:** `critical-infrastructure`
- **Summary:** Iran-linked hackers have extended a campaign against US water utility systems beyond the previously reported Minnesota incident, with Michigan, South Dakota, and Georgia also reportedly targeted.

### 9. Hugging Face Diffusers Flaws Let Malicious Model Repos Execute Arbitrary Code
- **Source:** The Hacker News — https://thehackernews.com/2026/08/hugging-face-diffusers-flaws-could-let.html
- **Severity:** high
- **Tags:** `supply-chain`, `rce`, `vulnerability`, `appsec`
- **Summary:** Three high-severity flaws in Hugging Face's Diffusers library bypass the `trust_remote_code` safeguard, letting a crafted model repository stealthily execute arbitrary code on machines that load it.

### 10. Inside the BTMOB Android RAT's Underground Business Model
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/inside-the-underground-business-of-btmob-rat/
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** Flare researchers mapped how the BTMOB Android RAT operation evolved into a fragmented ecosystem of resellers, source-code vendors, and custom build providers across multiple underground sales channels.

### 11. Alibaba Releases Qwen3.8-Max, Claims Frontier-Rivaling Performance
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/974342/alibaba-qwen-max-open-weight-ai
- **Severity:** medium
- **Tags:** `ai-launch`, `model-release`, `llm`
- **Summary:** Alibaba released Qwen3.8-Max, described as its largest and most capable model yet, claiming performance rivaling frontier systems from Anthropic, OpenAI, and domestic rival Moonshot AI's Kimi K3.

### 12. Thermo Fisher Patches Flaw Enabling Near-Undetectable DNA File Tampering
- **Source:** The Hacker News — https://thehackernews.com/2026/08/thermo-fisher-patches-flaw-that-could.html
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`
- **Summary:** Thermo Fisher patched CVE-2026-17583 in Applied Biosystems human identification software that could let attackers make nearly undetectable changes to .fsa/.hid data files before analysis software loads them.

### 13. EU AI Act Transparency and Labeling Rules Take Effect
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/974571/eu-ai-act-transparency-labels-rules-deepfakes
- **Severity:** informational
- **Tags:** `regulation`, `ai-safety`
- **Summary:** New EU AI Act transparency obligations took effect August 2, requiring companies to disclose AI chatbot interactions and label AI-generated content including deepfakes.

## Skippable

- **Apple finally fixed Siri. So why does it feel anticlimactic?** — TechCrunch AI. Opinion/analysis piece on Siri's AI overhaul, no concrete technical or security news.
- **Flashpoint EASM: Industry-Leading Vulnerability Intelligence** — Flashpoint. Vendor product marketing content.
- **Hackers steal 31,000 records identifying people behind Liechtenstein companies, foundations** — The Record. Regional breach, under 100k users, no technical detail (duplicate of SecurityWeek coverage below).
- **Cyberattack Hits Liechtenstein's Register of People Behind Companies and Foundations** — SecurityWeek. Duplicate coverage of the Liechtenstein breach, no additional technical detail.
- **N-able warns of N-central auth bypass flaw exploited in attacks** — BleepingComputer. Duplicate/earlier coverage of the N-central CVE-2026-18577 story; see the Hacker News writeup above.
- **N‑able Patches Vulnerability Exploited to Hack N-central Servers** — SecurityWeek. Duplicate coverage of the N-central CVE-2026-18577 story.
- **Congress's favorite AI tool? ChatGPT** — TechCrunch AI. General-interest piece, no security angle.
- **Quoting David Crawshaw's prompt** — Simon Willison. Personal blog musing, no news value.
- **AWS Weekly Roundup (August 3, 2026)** — AWS News Blog. Generic cloud roundup/marketing, no single security-relevant item.
- **[Webinar] Tales from the Frontlines: An exclusive briefing on Q2 incidents** — Cisco Talos. Webinar registration promo, not news.
- **Black Hat USA 2026 – Summary of Vendor Announcements (Part 1)** — SecurityWeek. Vendor marketing roundup, no single technical item.
- **Visa to Acquire Fraud Intelligence Firm BioCatch for $2.4 Billion** — SecurityWeek. M&A/business news, not a security incident.
- **Devtools must be open source (exe.dev)** — Simon Willison. Personal commentary/opinion, no news value.
- **ExfilSquad hackers leak info of over 100,000 UK police officers, staff** — BleepingComputer. Duplicate coverage; see the Hacker News PNLD writeup above.
- **⚡ Weekly Recap: Rogue AI Models, $88M Bitcoin Theft, Water-System Attacks and Dangling DNS Hijacks** — The Hacker News. Aggregation roundup of stories already covered individually.
- **Is There Really a Fix for CISO Fatigue?** — Dark Reading. Opinion piece, no news value.
- **River Bank Says Hackers Deleted Data Stolen in Ransomware Attack** — SecurityWeek. Ransomware victim disclosure without TTPs or IOCs.
- **An analysis of incidents at Brazilian educational institutions** — Securelist. Regional incident stats/tips, no novel technique detailed in the summary.
- **Horizon3 Raises $250 Million to Fund Continuing Growth** — SecurityWeek. Funding/business news.
- **Biotech giant Amgen says patient data stolen from third-party cloud systems** — The Record. Generic breach disclosure, no confirmed scale or technical detail.
- **Russian hackers hijack hotel Wi-Fi networks to spy on travelers, Microsoft says** — The Record. Duplicate coverage; see the SecurityWeek Midnight Blizzard writeup above.
- **Brinks Home Discloses Data Breach as Hackers Leak Files** — SecurityWeek. Generic breach disclosure, no technical substance or scale given.
- **FOMO in the SOC: Where AI Platforms like Claude Actually Fit** — The Hacker News. Vendor-flavored opinion piece on AI in the SOC, no concrete news.
- **Recent SonicWall Vulnerabilities Exploited in Ransomware Attacks** — SecurityWeek. Duplicate coverage; see the Hacker News INC Ransomware writeup above.
- **Pass the Passkey: A Novel Attack Surface in Passwordless Authentication** — Unit 42. Duplicate/original-research coverage of the passkey attack story; see the Hacker News writeup above.
- **A Marc Benioff-backed startup thinks AI can solve the AI deployment problem** — TechCrunch AI. Funding news, non-security SaaS launch.
