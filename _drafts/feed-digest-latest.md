# Digest — 2026-11-19 PM

- Window: last 14h
- Raw items considered: 38
- Relevant: 19
- Skippable: 19

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** PHP Fixes 7 Critical Flaws, Including Remote Code Execution Bug — `2026-11-19-php-critical-rce-flaws-cve-2026-115560.md`
- [x] **[HIGH]** European Commission Confirms Cyberattack Using AI Hacking Platform — `2026-11-19-eu-commission-cyberattack-ai-tool-artex.md`
- [x] **[HIGH]** Critical VMware vCenter Flaw Lets Attackers Bypass Authentication — `2026-11-19-vmware-vcenter-critical-auth-bypass.md`
- [x] **[HIGH]** Critical NGINX 'NGINX2Root' Bugs Let Attackers Hijack Servers — `2026-11-19-nginx2root-critical-rce-flaws.md`
- [x] **[HIGH]** Drupal Patches Critical Installer Flaw That Could Give Attackers Site Control — `2026-11-19-drupal-critical-installer-flaw.md`
- [x] **[MEDIUM]** Ukraine Exposes Ransomware Network Extorting US Oil, Healthcare Firms — `2026-11-19-ukraine-ransomware-network-arrests.md`
- [x] **[HIGH]** Hackers Exploit Cisco Expressway Vulnerability Soon After PoC Release — `2026-11-19-cisco-expressway-exploited-poc.md`
- [x] **[CRITICAL]** Critical Apache Roller, Axis Vulnerabilities Exploited in Attacks — `2026-11-19-apache-roller-axis-exploited.md`
- [x] **[MEDIUM]** Elecbrakes EB2, VM1, ELBC2000 Vulnerabilities Could Let Attackers Control Trailer Brakes — `2026-11-19-elecbrakes-ics-critical-flaws.md`
- [x] **[MEDIUM]** libumqtt Vulnerability Could Allow Denial of Service, Memory Corruption — `2026-11-19-libumqtt-vulnerability.md`
- [x] **[MEDIUM]** Autonomy Logic OpenPLC Runtime Flaw Allows Unauthenticated Admin Account Creation — `2026-11-19-openplc-runtime-race-condition.md`
- [x] **[HIGH]** PHP2Shell Exploitation Hit PAN-OS Firewalls Exposed to the Internet — `2026-11-19-php2shell-firewall-exploitation.md`
- [x] **[INFORMATIONAL]** Microsoft Tests New Edge Lockdown Mode That Disables GPU APIs — `2026-11-19-edge-lockdown-mode.md`
- [x] **[HIGH]** Splunk Patches Nearly 140 Flaws Across Three Core Products — `2026-11-19-splunk-patches-140-flaws.md`
- [x] **[HIGH]** Hackers Breach N-able Cloud Server, Disrupt Email Security Management — `2026-11-19-n-able-cloud-breach.md`
- [x] **[CRITICAL]** Java4Shell Exploitation Attempts Begin as Vendors Rush Out Advisories — `2026-11-19-java4shell-exploitation-begins.md`
- [x] **[HIGH]** Ruby Releases Fixes for 7 Regex and String Flaws, 5 With PoC RCE — `2026-11-19-ruby-regex-string-flaws-rce.md`
- [x] **[HIGH]** Researcher Demonstrates Database RCE Exploits Affecting PostgreSQL, MySQL and Oracle — `2026-11-19-database-rce-research-postgresql-mysql-oracle.md`
- [x] **[CRITICAL]** CISA Warns of 4 Exploited Flaws Linked to Ransomware, Cryptomining, and LLMjacking Attacks — `2026-11-19-cisa-kev-four-exploited-flaws.md`

## Relevant (details)

### 1. PHP Fixes 7 Critical Flaws, Including Remote Code Execution Bug
- **Source:** The Hacker News — https://thehackernews.com/2026/11/php-fixes-7-critical-flaws-including.html
- **Severity:** high
- **Tags:** `rce`, `vulnerability`
- **Summary:** The PHP Foundation patched seven critical flaws across all supported branches, including CVE-2026-115560 (CVSS 9.2), an improper input validation bug usable for remote code execution. No active exploitation has been reported yet.

### 2. European Commission Confirms Cyberattack Using AI Hacking Platform
- **Source:** The Record (Recorded Future) — https://therecord.media/european-commission-confirms-cyberattack-using-ai
- **Severity:** high
- **Tags:** `llm`, `ai-safety`
- **Summary:** The European Commission confirmed a cyberattack in which CERT-EU identified use of ARTEX, an open-source AI hacking platform the FBI recently flagged as used by both criminals and state-sponsored groups. Scope of the compromise has not been disclosed.

### 3. Critical VMware vCenter Flaw Lets Attackers Bypass Authentication
- **Source:** The Hacker News — https://thehackernews.com/2026/11/critical-vmware-vcenter-flaw-cvss-98.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Summary:** Broadcom disclosed a critical VMware vCenter flaw (CVSS 9.8) that lets a network attacker bypass authentication and gain unauthorized access. Fixed versions ship for all supported branches; no workaround exists.

### 4. Critical NGINX 'NGINX2Root' Bugs Let Attackers Hijack Servers
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/critical-nginx-nginx2root-bugs-let-attackers-hijack-servers/
- **Severity:** high
- **Tags:** `rce`, `privilege-escalation`
- **Summary:** Researchers disclosed "nginx2root," critical NGINX bugs letting unauthenticated attackers execute code remotely, chainable with a Linux kernel bug to gain root. F5 has patched the five flaws, but PoC exploits are already public.

### 5. Drupal Patches Critical Installer Flaw That Could Give Attackers Site Control
- **Source:** The Hacker News — https://thehackernews.com/2026/11/drupal-patches-critical-installer-flaw.html
- **Severity:** high
- **Tags:** `rce`, `appsec`
- **Summary:** Drupal patched a critical core flaw that, under uncommon configurations, lets an unauthenticated attacker abuse the built-in installer to reinstall a site, leading to takeover or RCE. Fixed releases shipped for all supported branches.

### 6. Ukraine Exposes Ransomware Network Extorting US Oil, Healthcare Firms
- **Source:** The Record (Recorded Future) — https://therecord.media/ukraine-ransomware-arrests-cyber
- **Severity:** medium
- **Tags:** `ransomware`
- **Summary:** Ukrainian authorities arrested four suspected members of an international ransomware network accused of extorting more than $40 million from companies including US oil and healthcare firms. No TTPs or group name disclosed yet.

### 7. Hackers Exploit Cisco Expressway Vulnerability Soon After PoC Release
- **Source:** SecurityWeek — https://www.securityweek.com/hackers-exploit-cisco-expressway-vulnerability-soon-after-poc-release/
- **Severity:** high
- **Tags:** `vulnerability`, `malware`
- **Summary:** Attackers compromised clustered Cisco Expressway devices at a Russian organization shortly after a PoC exploit was published, preparing tooling for lateral movement. Underscores how fast PoC publication turns into real-world exploitation.

### 8. Critical Apache Roller, Axis Vulnerabilities Exploited in Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/critical-apache-roller-axis-vulnerabilities-exploited-in-attacks/
- **Severity:** critical
- **Tags:** `rce`, `zero-day`
- **Summary:** Attackers are actively targeting Confluence Data Center through an Apache Axis flaw, and Apache separately warned of attacks against Apache Roller. Both are under active exploitation with limited public detail on patch status.

### 9. Elecbrakes EB2, VM1, ELBC2000 Vulnerabilities Could Let Attackers Control Trailer Brakes
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-02
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`
- **Summary:** CISA published an advisory for vulnerabilities (CVSS up to 9.6) in Elecbrakes EB2, VM1, and ELBC2000 trailer brake controllers that could let an attacker control brakes, modify firmware, or disable safety features. No active exploitation reported.

### 10. libumqtt Vulnerability Could Allow Denial of Service, Memory Corruption
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-03
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`
- **Summary:** CISA disclosed an integer underflow bug (CVE-2026-125132, CVSS 8.6) in libumqtt, an MQTT library used across critical manufacturing, energy, IT, transportation, and water sector deployments worldwide. No active exploitation reported.

### 11. Autonomy Logic OpenPLC Runtime Flaw Allows Unauthenticated Admin Account Creation
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-01
- **Severity:** medium
- **Tags:** `vulnerability`, `privilege-escalation`
- **Summary:** CISA warned of a race condition (CVE-2026-126088, CVSS 8.1) in Autonomy Logic OpenPLC Runtime that could let several unauthenticated admin accounts be created on affected systems. No active exploitation reported.

### 12. PHP2Shell Exploitation Hit PAN-OS Firewalls Exposed to the Internet
- **Source:** The Hacker News — https://thehackernews.com/2026/11/everything-is-web-application-including.html
- **Severity:** high
- **Tags:** `rce`, `appsec`
- **Summary:** A technical retrospective details how PHP2Shell exploitation (CVE-2026-109618/109619) hit Palo Alto PAN-OS management interfaces exposed to the internet, confirmed by Palo Alto on October 28. Highlights that security appliances are themselves exposed web applications.

### 13. Microsoft Tests New Edge Lockdown Mode That Disables GPU APIs
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-tests-new-edge-lockdown-mode-that-disables-gpu-apis/
- **Severity:** informational
- **Tags:** `microsoft`, `appsec`
- **Summary:** Microsoft is testing a new Edge security feature, Lockdown Mode, that disables WebGL, WebGL2, and WebGPU APIs to reduce browser attack surface. Currently in testing with no general availability date.

### 14. Splunk Patches Nearly 140 Flaws Across Three Core Products
- **Source:** SecurityWeek — https://www.securityweek.com/splunk-patches-nearly-140-flaws-across-three-core-products/
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`
- **Summary:** Splunk shipped fixes for nearly 140 vulnerabilities across three core products, resolving issues that could lead to authentication bypass, RCE, and privilege escalation. No active exploitation reported.

### 15. Hackers Breach N-able Cloud Server, Disrupt Email Security Management
- **Source:** The Hacker News — https://thehackernews.com/2026/11/n-able-confirms-hackers-accessed-cloud.html
- **Severity:** high
- **Tags:** `data-breach`, `cloud-security`
- **Summary:** N-able disclosed unauthorized access to a server in its Mail Assure / Spam Experts Hosted Cloud, disabling management interfaces and APIs across three regions. Investigation is ongoing; scope of data accessed not yet detailed.

### 16. Java4Shell Exploitation Attempts Begin as Vendors Rush Out Advisories
- **Source:** SecurityWeek — https://www.securityweek.com/java4shell-exploitation-attempts-begin-as-vendors-rush-out-advisories/
- **Severity:** critical
- **Tags:** `rce`, `zero-day`
- **Summary:** GreyNoise, WatchTowr, and Cloudflare report probing and exploit attempts against the newly disclosed "Java4Shell" flaw as Cisco, Elastic, Red Hat, and Siemens rush out impact advisories. Exploitation attempts began almost immediately after disclosure.

### 17. Ruby Releases Fixes for 7 Regex and String Flaws, 5 With PoC RCE
- **Source:** The Hacker News — https://thehackernews.com/2026/11/ruby-releases-fixes-for-7-regex-and.html
- **Severity:** high
- **Tags:** `rce`, `vulnerability`
- **Summary:** Ruby maintainers fixed seven memory-safety flaws in the regex engine and string case-conversion code; for five, PoC exploits show crafted input can achieve remote code execution. No in-the-wild exploitation reported yet.

### 18. Researcher Demonstrates Database RCE Exploits Affecting PostgreSQL, MySQL and Oracle
- **Source:** The Hacker News — https://thehackernews.com/2026/11/researcher-demonstrates-database-rce.html
- **Severity:** high
- **Tags:** `rce`, `vulnerability`
- **Summary:** A researcher showed low-privilege database accounts can reach memory-corruption bugs in engine code to execute code on the server itself, publishing PoCs against PostgreSQL, MySQL, and ClickHouse plus a separate Oracle chain. No vendor patch status given yet.

### 19. CISA Warns of 4 Exploited Flaws Linked to Ransomware, Cryptomining, and LLMjacking Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/11/cisa-warns-of-4-exploited-flaws-linked.html
- **Severity:** critical
- **Tags:** `zero-day`, `llm`
- **Summary:** CISA added four actively exploited flaws to its KEV catalog: Synology DSM, BerriAI LiteLLM, Apache Axis, and Vanderbilt REDCap, tying them to ransomware, cryptomining, and LLMjacking attacks. The LiteLLM flaw is notable given its role as an LLM API gateway.

## Skippable

- **PHP Patches Seven Critical RCE Vulnerabilities** — SecurityWeek. Duplicate coverage of the PHP critical-flaws story; Hacker News version has more technical detail (item 1).
- **ChatGPT can transcribe as you speak now with Live Dictation** — The Verge AI. Product feature update, no security angle.
- **Five warning signs of ransomware breach before encryption or data theft** — BleepingComputer. Generic defensive listicle, no specific incident.
- **Anthropic's IPO puts AI's circular financing boom to the test** — TechCrunch AI. Business/financial analysis, no security or model-launch substance.
- **With the biggest IPO of all time, Anthropic's 'good guy' reputation is on the line** — The Verge AI. Duplicate IPO topic, opinion piece.
- **Nvidia Responds to Gentlemen Ransomware Claim** — SecurityWeek. Ransomware claim disclosure without TTPs/IOCs; company denies breach.
- **Why Holiday Security Can't Wait for Black Friday** — Dark Reading. Generic opinion/listicle, no specific incident.
- **Superhuman pushes its Go assistant everywhere** — TechCrunch AI. Minor product update, no security angle.
- **Drupal patches critical RCE flaw, warns exploits may surface quickly** — BleepingComputer. Duplicate coverage of the Drupal installer flaw (item 5).
- **I let Apple's always-listening AI summarize my life for two weeks** — The Verge AI. Personal hands-on piece, no news/security value.
- **Canva adds an AI 'off' button** — The Verge AI. Minor product feature, no security angle.
- **StepSecurity Secures $20 Million to Expand Supply Chain Protection** — SecurityWeek. Funding announcement, no technical substance.
- **The Governance Gap in Open-Weight AI and What to Do About It** — SecurityWeek. Opinion piece without specific news.
- **Microsoft confirms app installation, launch issues after hotpatch** — BleepingComputer. Generic IT bug, no security angle.
- **F5 Patches Critical NGINX2Root Flaws as PoC Exploits Go Public** — SecurityWeek. Duplicate coverage of the NGINX2Root story (item 4).
- **NVIDIA investigating Gentlemen ransomware breach claims** — BleepingComputer. Duplicate of the Nvidia ransomware claim; no confirmed breach, no TTPs/IOCs.
- **Africa Retakes Top Spot as Most Attacked Region, Led by Nigeria Surge** — Dark Reading. Regional threat-intel stats, no specific TTPs or actionable detail.
- **PHP Readies Critical Security Updates to Patch Another RCE Flaw** — SecurityWeek. Superseded by item 1 — same CVE-2026-115560, now patched.
- **PHP Warns of Critical Security Flaws Affecting All Supported Versions, Fixes Coming November 19** — The Hacker News. Pre-release warning superseded by item 1.
