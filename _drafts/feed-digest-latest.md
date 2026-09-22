# Digest — 2026-09-22 PM

- Window: last 14h
- Raw items considered: 25
- Relevant: 16
- Skippable: 9

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
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`
- **Summary:** A malicious npm package, "indexed-btree," impersonated the legitimate sorted-btree utility and accumulated millions of downloads. It hid its malicious trigger inside a prototype method in application runtime code rather than lifecycle install scripts.

### 2. Linux Kernel Flaw Lets ARM64 KVM Guests Read/Write Host Memory (CVE-2026-89775)
- **Source:** The Hacker News — https://thehackernews.com/2026/09/new-linux-kernel-flaw-gives-arm64-kvm.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Summary:** A Linux kernel KVM flaw on ARM64 with nested virtualization enabled exposes freed host memory to guest VMs, letting a guest escape and run code on the host.

### 3. SharePoint Flaw Microsoft Called 'Spoofing' Is Actually Authenticated RCE (CVE-2026-65660)
- **Source:** The Hacker News — https://thehackernews.com/2026/09/sharepoint-flaw-initially-listed-as.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Summary:** A SharePoint flaw Microsoft originally rated as low-severity "spoofing" actually enables authenticated remote code execution. Affects SharePoint Server 2016, 2019, and Subscription Edition; patches available.

### 4. WordPress Patches 'Click2Shell' Vulnerability
- **Source:** SecurityWeek — https://www.securityweek.com/wordpress-patches-click2shell-vulnerability/
- **Severity:** medium
- **Tags:** `vulnerability`, `rce`
- **Summary:** WordPress patched a bug that lets attackers automatically install and preview themes, potentially leading to remote code execution.

### 5. Cisco Talos Reports First Fully Autonomous AI-Driven C2 Implant
- **Source:** Cisco Talos — https://blog.talosintelligence.com/the-closed-quorum-inside-the-first-reported-autonomous-ai-c2-implant/
- **Severity:** medium
- **Tags:** `malware`, `ai-safety`, `llm`
- **Summary:** Cisco Talos discovered CLOSEDQUORUM, a malware binary with fully autonomous C2 behavior — the first reported implant able to run expanding portions of an attack chain without operator involvement.

### 6. Cisco Talos Launches CAIRN, a Tracking Toolkit for AI-Integrated Malware
- **Source:** Cisco Talos — https://blog.talosintelligence.com/introducing-cairn-frontier-tracking-for-ai-integrated-malware/
- **Severity:** informational
- **Tags:** `malware`, `ai-safety`
- **Summary:** Talos released CAIRN, a research toolkit for hunting, classifying, and tracking AI-integrated malware.

### 7. New Windows Defender Zero-Day Blocks Microsoft Antivirus Updates
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-windows-defender-zero-day-blocks-microsoft-antivirus-updates/
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`
- **Summary:** A researcher released a proof-of-concept for a new Microsoft Defender zero-day that blocks antivirus updates. No patch was available at disclosure.

### 8. Japan Dismantles First North Korean Laptop Farm; Allies Detail WaterPlum Scheme
- **Source:** SecurityWeek — https://www.securityweek.com/japan-dismantles-first-north-korean-laptop-farm-as-us-and-allies-detail-wider-scheme/
- **Severity:** informational
- **Tags:** `nation-state`
- **Summary:** Japan dismantled its first identified North Korean "laptop farm." The US, Japan, Germany, and Australia jointly published a report on North Korea's WaterPlum campaign.

### 9. Hidden Meta Muse Setting Lets On-Device Malware Turn the AI Assistant Into a Backdoor
- **Source:** The Hacker News — https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`, `malware`
- **Summary:** A researcher showed malware already on a Mac can flip a hidden Meta Muse setting so dictated voice prompts are redirected to an attacker. Requires an existing malware foothold.

### 10. WordPress 'Comment2Shell' Flaw Turns Anonymous Comment XSS Into Admin RCE (CVE-2026-93485)
- **Source:** The Hacker News — https://thehackernews.com/2026/09/wordpress-comment2shell-flaw-can-turn.html
- **Severity:** high
- **Tags:** `xss`, `rce`, `cve`, `vulnerability`
- **Summary:** A WordPress core flaw let an anonymous comment plant a hidden script that executed via an admin's session when the admin viewed the page. Fixed in 7.1.1.

### 11. Zyxel Switch Flaw Under Active Exploitation by Chinese Hackers; CISA Orders Federal Patch
- **Source:** The Hacker News — https://thehackernews.com/2026/09/zyxel-and-veeam-flaws-under-active.html
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-orders-feds-to-patch-actively-exploited-zyxel-flaw-by-thursday/
- **Source:** SecurityWeek — https://www.securityweek.com/recent-zyxel-switch-vulnerability-exploited-by-chinese-hackers/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Summary:** CISA added a Zyxel switch flaw (CVE-2026-7273, CVSS 8.8) and a related Veeam flaw to its KEV catalog after confirming active exploitation. A Chinese threat actor reportedly exfiltrated data from nearly 1,000 switches. CISA ordered federal agencies to patch by Thursday.

### 12. US Proposes AI Incident Alert System in Talks With China
- **Source:** SecurityWeek — https://www.securityweek.com/us-proposes-ai-incident-alert-system-in-talks-with-china-bessent-says/
- **Severity:** informational
- **Tags:** `ai-safety`
- **Summary:** Treasury Secretary Bessent said the US proposed an AI incident alert system in talks with China.

### 13. Jev Introduces 'System One' Decision Models — a New LLM Output Shape
- **Source:** Simon Willison — https://simonwillison.net/2026/Sep/21/jev/
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `llm`
- **Summary:** TypeSafe AI unveiled Jev, a "System One model" that takes text input but returns floating-point category/rating/confidence scores instead of text output.

## Skippable

- **[Virtual Event] Cybersecurity Outlook 2027** — Dark Reading. Event/webinar listing, not news.
- **More Than a Third of Industrial Orgs See Cybersecurity Risk as a Top Obstacle to Growth, Study Finds** — Dark Reading. Generic industry survey/marketing, no technical substance.
- **DORA Year Two: Can Your SOC Actually See the Attack?** — The Hacker News. Sponsored-style compliance opinion piece, no concrete news.
- **SideCopy Broadens India Targeting to Academia With ReverseRAT Spear-Phishing** — The Hacker News. Routine APT campaign expansion using a known technique, no new IOCs.
- **Transformers now runs llama.cpp quants** — Hugging Face Blog. Minor library interoperability feature, not a launch or capability jump.
- **Jun Kim, oMLX creator and maintainer, joins Hugging Face** — Hugging Face Blog. Personnel/hiring announcement, no news value.
- **The man who built Apple's stores doesn't buy Silicon Valley's bet on AI shopping** — TechCrunch AI. Opinion piece, no news value.
- **Russia's internet shutdowns disrupt warnings about incoming drone attacks** — The Record. Geopolitical/telecom story, no technical security or AI substance.
- **Cloudflare Python Workers are now generally available** — Simon Willison. Developer platform GA announcement, no security angle.
