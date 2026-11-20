# Digest — 2026-11-20 PM

- Window: last 14h
- Raw items considered: 28
- Relevant: 15
- Skippable: 13

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** SBC Medical Group Data Breach Impacts Over 2 Million — `2026-11-20-sbc-medical-group-data-breach.md`
- [x] **[CRITICAL]** F5 Releases Emergency Patches for Critical BIG-IP RCE Flaws — `2026-11-20-f5-big-ip-critical-rce-patches.md`
- [x] **[CRITICAL]** Hackers Exploit Critical Cisco Expressway Flaw to Breach Internal Networks — `2026-11-20-cisco-expressway-exploited.md`
- [x] **[CRITICAL]** China-Linked Hackers Exploited VMware vCenter Zero-Day for Months — `2026-11-20-vmware-vcenter-zero-day-china.md`
- [x] **[HIGH]** Linux KVM Flaw Lets Guest VMs Read Host Memory on AMD Clouds — `2026-11-20-linux-kvm-amd-host-memory-flaw.md`
- [x] **[HIGH]** Ruby Patches Ruby2Shell Vulnerability That Could Lead to RCE — `2026-11-20-ruby-ruby2shell-rce-patch.md`
- [x] **[HIGH]** JPMorgan, Visa, Mastercard Cite Third-Party Incidents Amid Data Leak — `2026-11-20-jpmorgan-visa-mastercard-data-leak.md`
- [x] **[MEDIUM]** Dozens of Credit Unions Hit by Supplier Breach That Went Unnoticed for Six Weeks — `2026-11-20-credit-unions-supplier-breach.md`
- [x] **[MEDIUM]** N-able Security Breach Leads to Major Service Outage — `2026-11-20-n-able-breach-service-outage.md`
- [x] **[MEDIUM]** European Commission Confirms AI-Assisted Cyberattack Disrupted Services — `2026-11-20-eu-commission-ai-assisted-cyberattack.md`
- [x] **[MEDIUM]** SonicWall Warns Gen 6 Firewalls Won't Get Security Patches — `2026-11-20-sonicwall-gen6-firewall-eol.md`
- [x] **[MEDIUM]** ROMULUS ClickFix Attacks Deliver RAT That Spies on Victims — `2026-11-20-romulus-clickfix-rat.md`
- [x] **[MEDIUM]** Unpatched Windows 0-Day 'FastUnlock' Lets Attackers Run Programs on Locked PCs — `2026-11-20-windows-fastunlock-zero-day.md`
- [x] **[INFORMATIONAL]** How a Cloud Pentest Works: Mapping the Trust Boundaries — `2026-11-20-cloud-pentest-trust-boundaries.md`
- [x] **[INFORMATIONAL]** Signal Blocks Gemini and Siri From Reading Your Screen — `2026-11-20-signal-blocks-ai-screenshots.md`

## Relevant (details)

### 1. SBC Medical Group Data Breach Impacts Over 2 Million
- **Source:** SecurityWeek — https://www.securityweek.com/sbc-medical-group-data-breach-impacts-over-2-million/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `data-breach`
- **Slug:** `sbc-medical-group-data-breach`
- **Must-know:** yes
- **Summary:** Threat actors accessed databases containing customer information tied to SBC Medical Group clinics in Japan, affecting more than 2 million individuals. No technical detail on the attack vector has been disclosed.

### 2. F5 Releases Emergency Patches for Critical BIG-IP RCE Flaws
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/f5-releases-emergency-patches-for-critical-big-ip-rce-flaws/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `f5-big-ip-critical-rce-patches`
- **Must-know:** no
- **Summary:** F5 issued emergency patches for five critical BIG-IP vulnerabilities that attackers can exploit for denial-of-service or remote code execution. BIG-IP's broad enterprise deployment makes unpatched instances a high-value target.

### 3. Hackers Exploit Critical Cisco Expressway Flaw, Breach Four Devices and Reach Internal Network
- **Source:** The Hacker News — https://thehackernews.com/2026/11/hackers-exploit-critical-cisco.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `rce`, `cisco`
- **Slug:** `cisco-expressway-exploited`
- **Must-know:** no
- **Summary:** Attackers exploited CVE-2026-76466 (CVSS 9.8) in Cisco Expressway to breach a Russian organization shortly after a public PoC exploit appeared. Four devices were confirmed breached, with attackers reaching the internal network.

### 4. China-Linked Hackers Exploit Critical VMware vCenter Zero-Day to Gain Admin Access and Steal Data
- **Source:** The Hacker News — https://thehackernews.com/2026/11/china-linked-hackers-exploit-critical.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `vulnerability`, `privilege-escalation`
- **Slug:** `vmware-vcenter-zero-day-china`
- **Must-know:** yes
- **Summary:** A China-nexus espionage group (Armory Castle, formerly UNC5221) exploited a zero-day authentication bypass in VMware vCenter Server, CVE-2026-123890 (CVSS 9.8), to gain admin access and steal data starting in early September 2026.

### 5. Linux KVM Flaw CVE-2026-99312 Lets Guest VMs Access Host Memory on AMD Hosts
- **Source:** The Hacker News — https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `cloud-security`, `linux`
- **Slug:** `linux-kvm-amd-host-memory-flaw`
- **Must-know:** no
- **Summary:** A KVM flaw let researchers read ~127 GB of a cloud host's memory from inside their own VM on DigitalOcean. CVE-2026-99312 affects AMD hosts with nested virtualization enabled; fixed kernels have shipped.

### 6. Ruby Patches Ruby2Shell Vulnerability That Could Lead to RCE
- **Source:** SecurityWeek — https://www.securityweek.com/ruby-patches-ruby2shell-vulnerability-that-could-lead-to-rce/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `ruby-ruby2shell-rce-patch`
- **Must-know:** no
- **Summary:** Ruby patched a heap-based buffer overflow, CVE-2026-132825 (nicknamed Ruby2Shell), that could lead to remote code execution. No in-the-wild exploitation has been disclosed.

### 7. JPMorgan, Visa, Mastercard Cite Third-Party Incidents Amid Data Leak
- **Source:** SecurityWeek — https://www.securityweek.com/jpmorgan-visa-mastercard-cite-third-party-incidents-amid-data-leak/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `supply-chain`
- **Slug:** `jpmorgan-visa-mastercard-data-leak`
- **Must-know:** no
- **Summary:** JPMorgan, Visa, and Mastercard each pointed to third-party providers after the N0n extortion group leaked data allegedly tied to their customers. None has confirmed a direct breach of its own systems.

### 8. Dozens of Credit Unions Hit by Supplier Breach That Went Unnoticed for Six Weeks
- **Source:** The Record (Recorded Future) — https://therecord.media/dozens-of-credit-unions-hit-by-supplier-breach
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `supply-chain`, `data-breach`
- **Slug:** `credit-unions-supplier-breach`
- **Must-know:** no
- **Summary:** Ireland's Data Protection Commission received more than 40 breach notifications from credit unions that used a Belfast-based company as a data processor. The breach went unnoticed for six weeks.

### 9. N-able Says Recent Security Breach Led to Major Service Outage
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/n-able-says-recent-security-breach-led-to-major-service-outage/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `supply-chain`, `data-breach`
- **Slug:** `n-able-breach-service-outage`
- **Must-know:** no
- **Summary:** A breach of an N-able server caused a major outage affecting Mail Assure and SpamExperts Hosted Cloud worldwide. N-able's RMM software is widely used by managed service providers.

### 10. European Commission Confirms AI-Assisted Cyberattack Disrupted Services
- **Source:** SecurityWeek — https://www.securityweek.com/european-commission-confirms-ai-assisted-cyberattack-disrupted-services/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`, `ai-assisted-attack`
- **Slug:** `eu-commission-ai-assisted-cyberattack`
- **Must-know:** no
- **Summary:** The European Commission confirmed an AI-assisted cyberattack disrupted some of its services, taking certain systems offline to contain the incident. It says it has no evidence of a data breach.

### 11. SonicWall Warns Gen 6 Firewalls Won't Get Security Patches, Even for Critical Flaws
- **Source:** The Hacker News — https://thehackernews.com/2026/11/sonicwall-warns-gen-6-firewalls-wont.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `appsec`, `ai-assisted-attack`
- **Slug:** `sonicwall-gen6-firewall-eol`
- **Must-know:** no
- **Summary:** SonicWall is urging customers to retire internet-facing Generation 6 firewalls, which will no longer receive security patches even for critical flaws. The vendor cited rising AI-assisted automated exploitation of unsupported edge devices.

### 12. ROMULUS ClickFix Attacks Deliver RAT That Can Spy on Users and Control PCs
- **Source:** The Hacker News — https://thehackernews.com/2026/11/romulus-clickfix-attacks-deliver-rat.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`, `rat`
- **Slug:** `romulus-clickfix-rat`
- **Must-know:** no
- **Summary:** The ROMULUS ClickFix delivery platform is distributing a previously undocumented RAT related to CNCMachineRMS, using ClickFix social-engineering lures and signed binary sideloading alongside Legion Loader.

### 13. New Unpatched Windows 0-Day FastUnlock Lets Someone Holding a Locked PC Run Programs on It
- **Source:** The Hacker News — https://thehackernews.com/2026/11/new-unpatched-windows-0-day-fastunlock.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `zero-day`, `vulnerability`, `microsoft`
- **Slug:** `windows-fastunlock-zero-day`
- **Must-know:** no
- **Summary:** A researcher disclosed FastUnlock, an unpatched technique letting someone with physical access to a locked Windows PC run programs without signing in. It grants only a limited account, not admin control.

### 14. Transcending the Trust Boundaries: How a Cloud Pentest Works
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/how-a-cloud-pentest-works/121921/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `cloud-security`, `appsec`, `kubernetes`
- **Slug:** `cloud-pentest-trust-boundaries`
- **Must-know:** no
- **Summary:** First in a series on cloud penetration testing, covering External, Overlay, and Underlay cloud layers, common architectures (OpenStack, Kubernetes), and attack chains drawn from real-world incidents.

### 15. Signal Is Blocking Gemini and Siri AI From Reading Your Screen
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/1038390/signal-blocking-ai-agent-screenshots-mobile-app
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-safety`, `privacy`, `google`
- **Slug:** `signal-blocks-ai-screenshots`
- **Must-know:** no
- **Summary:** Signal is restricting screenshots on Android and iOS to stop OS-level AI agents from reading users' messages and on-screen data, saying agentic AI features in Gemini and Siri undermine its privacy guarantees.

## Skippable

- **The Flashpoint Threat Intelligence Brief: Middle East** — Flashpoint. Recurring geopolitical roundup, no specific technical content.
- **Still tracking company passwords in spreadsheets? You're flying blind.** — BleepingComputer. NordPass marketing content, not news.
- **In Other News: Norwegian Energy Firm Cyberattacks, Supercomputer Hack, New Nightmare Eclipse Exploit** — SecurityWeek. Roundup of items covered individually elsewhere or without technical substance.
- **The fallout from Nvidia's Jensen Huang scandal continues** — TechCrunch AI. Podcast/business news, no security or technical AI substance.
- **Cyber Director Cairncross out as White House resets cyber leadership** — The Record. Personnel/leadership change, no technical substance.
- **The week everything fell apart** — The Verge AI. General tech outage retrospective podcast, not actionable.
- **Six AI-powered gadgets that could make your home office smarter** — TechCrunch AI. Product listicle, no security angle.
- **Industry Reactions to Major Outages and AI Patching Debate: Feedback Friday** — SecurityWeek. Opinion roundup without new technical detail.
- **Microsoft now automatically installs Windows 11 26H2 on unmanaged devices** — BleepingComputer. Generic IT rollout news, not security-critical.
- **The Path to AI Autonomy in the SOC** — The Hacker News. Survey-based opinion piece on AI SOC adoption trends, no concrete news.
- **Windows 11 KB5132057 update released with 28 changes and fixes** — BleepingComputer. Routine feature update, not security-critical.
- **N-able Blames Service Disruption on Cyberattack** — SecurityWeek. Duplicate coverage of the N-able breach; BleepingComputer item has more detail.
- **Token fraud is here and it's BAD (YouTube)** — Simon Willison. Anecdotal business-fraud commentary, not a disclosed vulnerability or attack technique.
