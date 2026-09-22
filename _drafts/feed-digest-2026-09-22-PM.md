# Digest — 2026-09-22 PM

- Window: last 14h
- Raw items considered: 25
- Relevant: 16
- Skippable: 9

Note: 16 relevant raw items were consolidated into 13 draft posts. Three
reports on the same Zyxel/Veeam KEV-catalog exploitation (SecurityWeek,
BleepingComputer, The Hacker News) were merged into one post, and two
reports on the same malicious npm package (SecurityWeek, The Hacker News)
were merged into one post, to avoid duplicate posts about one story.

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Malicious npm Package 'indexed-btree' Impersonates sorted-btree, Hides Loader in Runtime Code — `2026-09-22-indexed-btree-malicious-npm-package.md`
- [x] **[HIGH]** Linux Kernel Flaw Lets ARM64 KVM Guests Read/Write Host Memory (CVE-2026-89775) — `2026-09-22-linux-kernel-arm64-kvm-host-memory-flaw.md`
- [x] **[HIGH]** SharePoint Flaw Microsoft Called 'Spoofing' Is Actually Authenticated RCE (CVE-2026-65660) — `2026-09-22-sharepoint-authenticated-rce-cve-2026-65660.md`
- [x] **[MEDIUM]** WordPress Patches 'Click2Shell' Vulnerability — `2026-09-22-wordpress-click2shell-vulnerability.md`
- [x] **[MEDIUM]** Cisco Talos Reports First Fully Autonomous AI-Driven C2 Implant — `2026-09-22-closedquorum-autonomous-ai-c2-implant.md`
- [x] **[INFORMATIONAL]** Cisco Talos Launches CAIRN, a Tracking Toolkit for AI-Integrated Malware — `2026-09-22-cisco-talos-cairn-ai-malware-tracking.md`
- [x] **[HIGH]** New Windows Defender Zero-Day Blocks Microsoft Antivirus Updates — `2026-09-22-windows-defender-zero-day-blocks-updates.md`
- [x] **[INFORMATIONAL]** Japan Dismantles First North Korean Laptop Farm; Allies Detail WaterPlum Scheme — `2026-09-22-japan-north-korea-laptop-farm-waterplum.md`
- [x] **[MEDIUM]** Hidden Meta Muse Setting Lets On-Device Malware Turn the AI Assistant Into a Backdoor — `2026-09-22-meta-muse-hidden-setting-backdoor.md`
- [x] **[HIGH]** WordPress 'Comment2Shell' Flaw Turns Anonymous Comment XSS Into Admin RCE (CVE-2026-93485) — `2026-09-22-wordpress-comment2shell-cve-2026-93485.md`
- [x] **[HIGH]** Zyxel Switch Flaw Under Active Exploitation by Chinese Hackers; CISA Orders Federal Patch — `2026-09-22-zyxel-veeam-flaws-active-exploitation.md`
- [x] **[INFORMATIONAL]** US Proposes AI Incident Alert System in Talks With China — `2026-09-22-us-ai-incident-alert-system-china-talks.md`
- [x] **[INFORMATIONAL]** Jev Introduces 'System One' Decision Models — a New LLM Output Shape — `2026-09-21-jev-system-one-decision-models.md`

## Relevant (details)

### 1. Malicious npm Package 'indexed-btree' Impersonates sorted-btree, Hides Loader in Runtime Code
- **Source:** SecurityWeek — https://www.securityweek.com/malicious-b-tree-npm-package-accumulates-millions-of-downloads/
- **Source:** The Hacker News — https://thehackernews.com/2026/09/malicious-npm-package-indexed-btree-hid.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`
- **Slug:** `indexed-btree-malicious-npm-package`
- **Must-know:** yes
- **Summary:** A malicious npm package, "indexed-btree," impersonated the legitimate sorted-btree utility and accumulated millions of downloads. It hid its malicious trigger inside a prototype method in application runtime code rather than lifecycle install scripts, likely to evade tooling that watches for install-script abuse.

### 2. Linux Kernel Flaw Lets ARM64 KVM Guests Read/Write Host Memory (CVE-2026-89775)
- **Source:** The Hacker News — https://thehackernews.com/2026/09/new-linux-kernel-flaw-gives-arm64-kvm.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Slug:** `linux-kernel-arm64-kvm-host-memory-flaw`
- **Must-know:** no
- **Summary:** A Linux kernel KVM flaw on ARM64 with nested virtualization enabled exposes freed host memory to guest VMs, letting a guest read/write host kernel memory. The discoverer says it can be used to escape the guest and run code on the host.

### 3. SharePoint Flaw Microsoft Called 'Spoofing' Is Actually Authenticated RCE (CVE-2026-65660)
- **Source:** The Hacker News — https://thehackernews.com/2026/09/sharepoint-flaw-initially-listed-as.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `sharepoint-authenticated-rce-cve-2026-65660`
- **Must-know:** no
- **Summary:** A SharePoint Server flaw Microsoft originally rated as low-severity "spoofing" (CVSS 6.5) actually enables authenticated remote code execution, per full technical details from a Viettel Cyber Security researcher. Affects SharePoint Server 2016, 2019, and Subscription Edition; patches are available.

### 4. WordPress Patches 'Click2Shell' Vulnerability
- **Source:** SecurityWeek — https://www.securityweek.com/wordpress-patches-click2shell-vulnerability/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `rce`
- **Slug:** `wordpress-click2shell-vulnerability`
- **Must-know:** no
- **Summary:** WordPress patched a bug dubbed "Click2Shell" that lets attackers automatically install and preview themes, which could lead to remote code execution. Disclosure details on affected versions and exploitation path were limited.

### 5. Cisco Talos Reports First Fully Autonomous AI-Driven C2 Implant
- **Source:** Cisco Talos — https://blog.talosintelligence.com/the-closed-quorum-inside-the-first-reported-autonomous-ai-c2-implant/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `malware`, `ai-safety`, `llm`
- **Slug:** `closedquorum-autonomous-ai-c2-implant`
- **Must-know:** no
- **Summary:** Cisco Talos discovered CLOSEDQUORUM, a malware binary with fully autonomous command-and-control behavior, via its CAIRN project. Talos calls it the first reported implant able to execute expanding portions of an attack chain without operator involvement.

### 6. Cisco Talos Launches CAIRN, a Tracking Toolkit for AI-Integrated Malware
- **Source:** Cisco Talos — https://blog.talosintelligence.com/introducing-cairn-frontier-tracking-for-ai-integrated-malware/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `malware`, `ai-safety`
- **Slug:** `cisco-talos-cairn-ai-malware-tracking`
- **Must-know:** no
- **Summary:** Talos released CAIRN, a research toolkit for hunting, classifying, and tracking AI-integrated malware. It's the project that led to the CLOSEDQUORUM discovery.

### 7. New Windows Defender Zero-Day Blocks Microsoft Antivirus Updates
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-windows-defender-zero-day-blocks-microsoft-antivirus-updates/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`
- **Slug:** `windows-defender-zero-day-blocks-updates`
- **Must-know:** no
- **Summary:** Researcher Abdelhamid Naceri released a proof-of-concept for a new Microsoft Defender zero-day that blocks antivirus updates. No patch was available at disclosure.

### 8. Japan Dismantles First North Korean Laptop Farm; Allies Detail WaterPlum Scheme
- **Source:** SecurityWeek — https://www.securityweek.com/japan-dismantles-first-north-korean-laptop-farm-as-us-and-allies-detail-wider-scheme/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `nation-state`
- **Slug:** `japan-north-korea-laptop-farm-waterplum`
- **Must-know:** no
- **Summary:** Japan dismantled its first identified North Korean "laptop farm" used to place DPRK IT workers as remote employees at Western firms. The US, Japan, Germany, and Australia jointly published a report on the scope of North Korea's WaterPlum campaign.

### 9. Hidden Meta Muse Setting Lets On-Device Malware Turn the AI Assistant Into a Backdoor
- **Source:** The Hacker News — https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`, `malware`
- **Slug:** `meta-muse-hidden-setting-backdoor`
- **Must-know:** no
- **Summary:** Researcher Patrick Wardle showed that malware already running on a Mac can flip a hidden Meta Muse setting so that dictated voice prompts are redirected to the attacker instead of Meta. Requires an existing malware foothold — it's a post-compromise technique, not a standalone remote exploit.

### 10. WordPress 'Comment2Shell' Flaw Turns Anonymous Comment XSS Into Admin RCE (CVE-2026-93485)
- **Source:** The Hacker News — https://thehackernews.com/2026/09/wordpress-comment2shell-flaw-can-turn.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `xss`, `rce`, `cve`, `vulnerability`
- **Slug:** `wordpress-comment2shell-cve-2026-93485`
- **Must-know:** no
- **Summary:** A WordPress core flaw, CVE-2026-93485 ("Comment2Shell"), let an anonymous comment plant a hidden script that would execute code on the server via an admin's session when a logged-in administrator viewed the page. Fixed in version 7.1.1 on September 17.

### 11. Zyxel Switch Flaw Under Active Exploitation by Chinese Hackers; CISA Orders Federal Patch
- **Source:** The Hacker News — https://thehackernews.com/2026/09/zyxel-and-veeam-flaws-under-active.html
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-zyxel-flaw-by-thursday/
- **Source:** SecurityWeek — https://www.securityweek.com/recent-zyxel-switch-vulnerability-exploited-by-chinese-hackers/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Slug:** `zyxel-veeam-flaws-active-exploitation`
- **Must-know:** no
- **Summary:** CISA added a Zyxel GS1900 switch flaw, CVE-2026-7273 (CVSS 8.8, stack-based buffer overflow), to its KEV catalog after confirming active exploitation; a related Veeam flaw was added alongside it. SecurityWeek reports a Chinese threat actor used the Zyxel bug to exfiltrate data from nearly 1,000 switches. CISA ordered federal agencies to patch by Thursday.

### 12. US Proposes AI Incident Alert System in Talks With China
- **Source:** SecurityWeek — https://www.securityweek.com/us-proposes-ai-incident-alert-system-in-talks-with-china-bessent-says/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ai-safety`
- **Slug:** `us-ai-incident-alert-system-china-talks`
- **Must-know:** no
- **Summary:** Treasury Secretary Bessent said the US proposed an AI incident alert system in talks with China. The administration has resisted domestic AI slowdowns, arguing that would let China close the gap.

### 13. Jev Introduces 'System One' Decision Models — a New LLM Output Shape
- **Source:** Simon Willison — https://simonwillison.net/2026/Sep/21/jev/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `llm`
- **Slug:** `jev-system-one-decision-models`
- **Must-know:** no
- **Summary:** TypeSafe AI unveiled Jev, described as the first "System One model" (aka decision model): it takes text input but returns floating-point numbers representing categories, yes/no answers, ratings, and confidence scores instead of text output.

## Skippable

- **[Virtual Event] Cybersecurity Outlook 2027** — Dark Reading. Event/webinar listing, not news.
- **More Than a Third of Industrial Orgs See Cybersecurity Risk as a Top Obstacle to Growth, Study Finds** — Dark Reading. Generic industry survey/marketing, no technical substance.
- **DORA Year Two: Can Your SOC Actually See the Attack?** — The Hacker News. Sponsored-style compliance opinion piece, no concrete news.
- **SideCopy Broadens India Targeting to Academia With ReverseRAT Spear-Phishing** — The Hacker News. Routine APT campaign expansion using a known technique (mshta.exe abuse), no new IOCs or novel method.
- **Transformers now runs llama.cpp quants** — Hugging Face Blog. Minor library interoperability feature, not a model launch or capability jump.
- **Jun Kim, oMLX creator and maintainer, joins Hugging Face** — Hugging Face Blog. Personnel/hiring announcement, no security or technical news value.
- **The man who built Apple's stores doesn't buy Silicon Valley's bet on AI shopping** — TechCrunch AI. Opinion piece, no news value.
- **Russia's internet shutdowns disrupt warnings about incoming drone attacks** — The Record. Geopolitical/telecom story, no technical security or AI substance.
- **Cloudflare Python Workers are now generally available** — Simon Willison. Developer platform GA announcement, no security angle.
