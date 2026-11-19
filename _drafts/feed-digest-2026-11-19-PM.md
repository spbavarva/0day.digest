# Digest — 2026-11-19 PM

- Window: last 14h
- Raw items considered: 68
- Relevant: 20
- Skippable: 48

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Hackers Steal Data of 1.6 Million SBC Medical Group Customers — `2026-11-19-sbc-medical-group-data-breach-1-6-million.md`
- [x] **[HIGH]** ASUS Warns of Critical Hard-Coded Key Flaw in Control Center Express — `2026-11-19-asus-control-center-express-hardcoded-key.md`
- [x] **[INFORMATIONAL]** AWS Launches New WAF Security Analytics Dashboard — `2026-11-19-aws-waf-security-analytics-dashboard.md`
- [x] **[CRITICAL]** Newly Patched VMware vCenter Flaw Exploited as Zero-Day by Chinese APT — `2026-11-19-vmware-vcenter-zeroday-chinese-apt.md`
- [x] **[INFORMATIONAL]** Gemini on Mac Can Now Use Your Computer — `2026-11-19-gemini-mac-computer-use.md`
- [x] **[MEDIUM]** Transport for London Breach Exposes 265,000 Oyster Card Users' Data — `2026-11-19-tfl-oyster-card-breach.md`
- [x] **[INFORMATIONAL]** Google Introduces Tool Retrieval in the Gemini API — `2026-11-19-gemini-api-tool-retrieval.md`
- [x] **[HIGH]** Meta's AI Agent Muse Mixes Up Conversations, Exposing Private Data — `2026-11-19-meta-muse-ai-agent-privacy-incident.md`
- [x] **[HIGH]** PHP Patches 18 Flaws, Including Critical 'phpAfterShell' RCE Chain — `2026-11-19-php-critical-rce-phpaftershell.md`
- [x] **[MEDIUM]** UK Court Confirms British Government Served Apple With Secret Encryption Notice — `2026-11-19-uk-apple-encryption-notice.md`
- [x] **[HIGH]** European Commission Confirms Cyberattack, Says Hackers Used AI Tool — `2026-11-19-european-commission-ai-cyberattack-artex.md`
- [x] **[HIGH]** Critical NGINX 'NGINX2Root' Bugs Let Attackers Hijack Servers — `2026-11-19-nginx2root-critical-rce-flaws.md`
- [x] **[MEDIUM]** Drupal Patches Critical Installer Flaw That Could Give Unauthenticated Attackers Site Control — `2026-11-19-drupal-critical-installer-flaw.md`
- [x] **[HIGH]** Hackers Exploit Cisco Expressway Vulnerability Soon After PoC Release — `2026-11-19-cisco-expressway-vulnerability-exploited.md`
- [x] **[HIGH]** Critical Apache Roller, Axis Vulnerabilities Exploited in Attacks — `2026-11-19-apache-roller-axis-vulnerabilities-exploited.md`
- [x] **[HIGH]** CISA Warns of Critical Flaws in Elecbrakes Trailer Brake Controllers — `2026-11-19-cisa-elecbrakes-brake-vulnerability.md`
- [x] **[HIGH]** Attackers Exploited PAN-OS Management Interfaces via PHP Vulnerabilities — `2026-11-19-pan-os-php-firewall-exploitation.md`
- [x] **[INFORMATIONAL]** Microsoft Tests New Edge Lockdown Mode That Disables GPU APIs — `2026-11-19-microsoft-edge-lockdown-mode.md`
- [x] **[HIGH]** Splunk Patches Nearly 140 Flaws Across Three Core Products — `2026-11-19-splunk-patches-140-flaws.md`
- [x] **[HIGH]** Hackers Breach N-able Cloud Server, Disrupting Email Security Management Across 3 Regions — `2026-11-19-n-able-cloud-breach.md`

## Relevant (details)

### 1. Hackers Steal Data of 1.6 Million SBC Medical Group Customers
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-steal-data-of-16-million-sbc-medical-group-customers/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `sbc-medical-group-data-breach-1-6-million`
- **Must-know:** no
- **Summary:** SBC Medical Group disclosed in an SEC filing that two separate incidents exposed personal data belonging to 1.6 million customers and employees. No attacker has been publicly named and the specific data types per incident weren't broken out.

### 2. ASUS Warns of Critical Hard-Coded Key Flaw in Control Center Express
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/asus-warns-of-critical-hard-coded-key-flaw-in-control-center-express/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Slug:** `asus-control-center-express-hardcoded-key`
- **Must-know:** no
- **Summary:** ASUS shipped Control Center Express v1.7.29 to fix three critical flaws, including a hard-coded key that could give a remote attacker administrative control of the management console and the devices it oversees.

### 3. AWS Launches New WAF Security Analytics Dashboard
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/introducing-the-new-aws-waf-security-analytics-dashboard/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `aws`, `cloud-security`, `appsec`
- **Slug:** `aws-waf-security-analytics-dashboard`
- **Must-know:** no
- **Summary:** AWS introduced a consolidated dashboard for WAF security analytics, letting teams see blocked-request spikes and lockouts across web ACLs, Regions, and CloudFront distributions in one place rather than per protection pack.

### 4. Newly Patched VMware vCenter Flaw Exploited as Zero-Day by Chinese APT
- **Source:** SecurityWeek — https://www.securityweek.com/newly-patched-vmware-vcenter-flaw-exploited-as-zero-day-by-chinese-apt/ (additional: The Hacker News — https://thehackernews.com/2026/11/critical-vmware-vcenter-flaw-cvss-98.html)
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`
- **Slug:** `vmware-vcenter-zeroday-chinese-apt`
- **Must-know:** yes
- **Summary:** Google says a China-linked espionage group exploited a critical (CVSS 9.8) VMware vCenter auth-bypass as a zero-day before Broadcom patched it. Fixes are out for all supported branches with no workaround.

### 5. Gemini on Mac Can Now Use Your Computer
- **Source:** The Verge AI — https://www.theverge.com/tech/1037902/google-gemini-macos-ai-computer-use
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-launch`, `llm`, `google`
- **Slug:** `gemini-mac-computer-use`
- **Must-know:** no
- **Summary:** Google's Gemini app for macOS gained a computer-use feature that can perform multi-step tasks across files, apps, and the web — raising the same prompt-injection/permission concerns as other computer-use agents.

### 6. Transport for London Breach Exposes 265,000 Oyster Card Users' Data
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/transport-for-london-breach-exposes-265-000-oyster-card-users-data/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `tfl-oyster-card-breach`
- **Must-know:** no
- **Summary:** TfL disclosed that about 265,000 Oyster photocard customers may have had account details exposed, following the agency's larger 2024 breach.

### 7. Google Introduces Tool Retrieval in the Gemini API
- **Source:** Google AI Blog — https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `ai-launch`, `llm`, `google`
- **Slug:** `gemini-api-tool-retrieval`
- **Must-know:** no
- **Summary:** The Gemini API now auto-selects relevant tools from large registered tool sets instead of requiring every definition in context — relevant to teams enforcing least-privilege tool access in agents.

### 8. Meta's AI Agent Muse Mixes Up Conversations, Exposing Private Data
- **Source:** TechCrunch AI — https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/
- **Section:** AI — News & Analysis
- **Severity:** high
- **Tags:** `ai-safety`, `llm`, `data-breach`, `meta`
- **Slug:** `meta-muse-ai-agent-privacy-incident`
- **Must-know:** no
- **Summary:** Meta employees say the Muse AI agent has surfaced other users' private messages, orders, and bank balances — a cross-tenant data-isolation failure rather than an external attack.

### 9. PHP Patches 18 Flaws, Including Critical 'phpAfterShell' RCE Chain
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/php-security-updates-fix-18-flaws-including-critical-rce-bugs/ (additional: The Hacker News — https://thehackernews.com/2026/11/phpaftershell-explained-how-hackers.html)
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `cve`, `vulnerability`
- **Slug:** `php-critical-rce-phpaftershell`
- **Must-know:** no
- **Summary:** PHP fixed 18 flaws including a critical session-storage race condition dubbed "phpAfterShell" (CVE-2026-126714) that can lead to RCE when chained with an app-side gadget chain; exploitability varies by configuration.

### 10. UK Court Confirms British Government Served Apple With Secret Encryption Notice
- **Source:** The Record (Recorded Future) — https://therecord.media/apple-uk-encryption-notice
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `encryption`, `appsec`
- **Slug:** `uk-apple-encryption-notice`
- **Must-know:** no
- **Summary:** A UK tribunal confirmed the government served Apple a secret notice targeting iCloud encryption protections, ending nearly two years of official denial.

### 11. European Commission Confirms Cyberattack, Says Hackers Used AI Tool
- **Source:** The Record (Recorded Future) — https://therecord.media/european-commission-confirms-cyberattack-using-ai
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ai-safety`, `malware`, `llm`
- **Slug:** `european-commission-ai-cyberattack-artex`
- **Must-know:** no
- **Summary:** The European Commission confirmed attackers used ARTEX, an open-source AI hacking platform the FBI recently flagged as used by both criminal and state-sponsored groups.

### 12. Critical NGINX 'NGINX2Root' Bugs Let Attackers Hijack Servers
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/critical-nginx-nginx2root-bugs-let-attackers-hijack-servers/ (additional: SecurityWeek — https://www.securityweek.com/f5-patches-critical-nginx2root-flaws-as-poc-exploits-go-public/)
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `privilege-escalation`, `cve`, `vulnerability`
- **Slug:** `nginx2root-critical-rce-flaws`
- **Must-know:** no
- **Summary:** Two critical unauthenticated-RCE NGINX bugs, chainable with a Linux kernel flaw for root, now have public PoCs; F5 has patched but urgency is high given NGINX's install base.

### 13. Drupal Patches Critical Installer Flaw That Could Give Unauthenticated Attackers Site Control
- **Source:** The Hacker News — https://thehackernews.com/2026/11/drupal-patches-critical-installer-flaw.html (additional: BleepingComputer — https://www.bleepingcomputer.com/news/security/drupal-patches-critical-rce-flaw-warns-exploits-may-surface-quickly/)
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `drupal-critical-installer-flaw`
- **Must-know:** no
- **Summary:** Drupal patched a critical installer-abuse flaw that can lead to site takeover under uncommon configurations; the project warns exploits may surface quickly now that it's public.

### 14. Hackers Exploit Cisco Expressway Vulnerability Soon After PoC Release
- **Source:** SecurityWeek — https://www.securityweek.com/hackers-exploit-cisco-expressway-vulnerability-soon-after-poc-release/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `cisco-expressway-vulnerability-exploited`
- **Must-know:** no
- **Summary:** Attackers compromised clustered Cisco Expressway devices at a Russian org shortly after a PoC went public, and staged lateral-movement tooling.

### 15. Critical Apache Roller, Axis Vulnerabilities Exploited in Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/critical-apache-roller-axis-vulnerabilities-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`, `cve`
- **Slug:** `apache-roller-axis-vulnerabilities-exploited`
- **Must-know:** no
- **Summary:** Confluence Data Center is being actively targeted via an Axis flaw, and Apache separately warned of attacks against Roller — both confirmed under active exploitation.

### 16. CISA Warns of Critical Flaws in Elecbrakes Trailer Brake Controllers
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-02
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `ics`
- **Slug:** `cisa-elecbrakes-brake-vulnerability`
- **Must-know:** no
- **Summary:** CISA disclosed flaws (CVSS up to 9.6) in Elecbrakes trailer brake controllers that could let an attacker remotely control or disable a trailer's brakes — no active exploitation reported, but the physical-safety impact is severe.

### 17. Attackers Exploited PAN-OS Management Interfaces via PHP Vulnerabilities
- **Source:** The Hacker News — https://thehackernews.com/2026/11/everything-is-web-application-including.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `appsec`, `vulnerability`
- **Slug:** `pan-os-php-firewall-exploitation`
- **Must-know:** no
- **Summary:** Palo Alto confirmed in late October that attackers exploited two PHP vulnerabilities (CVE-2026-109618/109619) for unauthenticated RCE against internet-exposed PAN-OS management interfaces.

### 18. Microsoft Tests New Edge Lockdown Mode That Disables GPU APIs
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-tests-new-edge-lockdown-mode-that-disables-gpu-apis/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `appsec`, `microsoft`
- **Slug:** `microsoft-edge-lockdown-mode`
- **Must-know:** no
- **Summary:** Microsoft is testing an Edge Lockdown Mode that disables WebGL/WebGL2/WebGPU to shrink the browser's attack surface, trading GPU rendering features for fewer exploit primitives.

### 19. Splunk Patches Nearly 140 Flaws Across Three Core Products
- **Source:** SecurityWeek — https://www.securityweek.com/splunk-patches-nearly-140-flaws-across-three-core-products/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`, `rce`
- **Slug:** `splunk-patches-140-flaws`
- **Must-know:** no
- **Summary:** Splunk patched nearly 140 flaws across three products, including critical/high issues enabling auth bypass, RCE, and privilege escalation — no active exploitation reported.

### 20. Hackers Breach N-able Cloud Server, Disrupting Email Security Management Across 3 Regions
- **Source:** The Hacker News — https://thehackernews.com/2026/11/n-able-confirms-hackers-accessed-cloud.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `data-breach`
- **Slug:** `n-able-cloud-breach`
- **Must-know:** no
- **Summary:** N-able disclosed unauthorized access to a Mail Assure/Spam Experts cloud server, disabling management interfaces across 3 regions — impactful since MSPs rely on N-able to run downstream customers' email security.

## Skippable

- **Qwen Incidents Show Self-Hosted AI Models Need Stronger Steering** — Dark Reading. Vague "several incidents" framing without named incident detail; opinion-adjacent.
- **Apple is hiring engineers to build its own AI agent** — The Verge AI. Job-listing speculation, not a launch or incident.
- **Your AWS Security, Identity, and Governance guide to re:Invent 2026** — AWS Security Blog. Event/marketing invite.
- **A brief history of Nvidia's recent stock fluctuations** — The Verge AI. Financial news, no security angle.
- **Meta's new Muse Charm device may cost $300** — TechCrunch AI. Product pricing speculation; duplicate of Verge item below.
- **These tech outages are giving Y2K, AI agent style** — TechCrunch AI. Speculative opinion piece, no confirmed technical cause.
- **Lawmakers launch new AI safety caucus amid rising security concerns** — The Record. Caucus formation, no concrete regulatory action yet.
- **PostgreSQL 19 Released** — Simon Willison. Database release, not a security or AI-launch story.
- **Meta's Muse Charm might cost $300** — The Verge AI. Duplicate of TechCrunch item above.
- **The unfolding Jensen Huang scandal: a timeline** — TechCrunch AI. Personal/corporate scandal, no security or technical AI substance.
- **Second Norwegian Energy Company Breached in Two Days** — Dark Reading. No technical detail or confirmed link between incidents.
- **Google is putting AI chats right on the homepage** — The Verge AI. Product feature, no security angle.
- **Critical PHP Flaws Allow Code Execution, But Don't Panic 'PHP2Shell'-Style** — Dark Reading. Duplicate/context coverage of the PHP patch story (see item 9).
- **Navigating Vulnerability Hysteria in the AI Era** — Dark Reading. Opinion piece referencing the same PHP disclosures.
- **How AWS Security Incident Response triages your security findings** — AWS Security Blog. Explainer on an existing feature, not news.
- **Anthropic's IPO could deliver $156B to charity** — TechCrunch AI. Financial/business news, no security angle.
- **The internet needs a nap (and you do, too)** — Cisco Talos. Culture/opinion piece, no news value.
- **ThreatsDay: GPT-6.2 Jailbreak Flaws, BubbleLoader PNG Malware, $500M Ransom Demands + 17 More Stories** — The Hacker News. Weekly link roundup without a single actionable, specific detail.
- **Google gives Gemini the ability to use your Mac for you** — TechCrunch AI. Duplicate of Verge item (see item 5).
- **DOJ, DHS partner on new unit tackling scams and cybercrime** — The Record. Administrative reorg announcement, no immediate technical detail.
- **Insider Threat Report: Dark Web Recruitment & Access Trends** — Flashpoint. Generic recurring trend report, no specific IOCs given.
- **CISA nominee LoSapio vows to bolster cyber defenses while denying Jan. 6 Capitol attack** — The Record. Political confirmation hearing, no technical content.
- **Walter Isaacson on curiosity and creativity in the AI age** — Google AI Blog. Interview/opinion content, no news value.
- **Former Alibaba exec's Everful raises $48.5M** — TechCrunch AI. Generic VC funding news, unrelated to security.
- **phpAfterShell Explained: How Hackers Could Turn a PHP Session Flaw Into Code Execution** — The Hacker News. Merged as additional source into item 9.
- **Anthropic hits Nasdaq exchanges at $111, 33% above IPO price** — TechCrunch AI. Financial news, part of Anthropic IPO cluster, no security angle.
- **Anthropic starts trading on Wall Street** — The Verge AI. Duplicate of the Anthropic IPO cluster.
- **Anthropic CEO recommits to pacing AI development** — TechCrunch AI. Statement/opinion, part of Anthropic IPO cluster.
- **PHP Patches Seven Critical RCE Vulnerabilities** — SecurityWeek. Duplicate coverage of the PHP patch story (see item 9).
- **PHP Fixes 7 Critical Flaws, Including Bugs That Could Allow Remote Code Execution** — The Hacker News. Duplicate coverage of the PHP patch story (see item 9).
- **ChatGPT can transcribe as you speak now with Live Dictation** — The Verge AI. Product feature, no security angle.
- **Critical VMware vCenter Flaw (CVSS 9.8) Lets Network Attackers Bypass Authentication** — The Hacker News. Merged as additional source into item 4.
- **Five warning signs of ransomware breach before encryption or data theft** — BleepingComputer. Generic listicle, no IOCs or new technique.
- **Anthropic's IPO puts AI's circular financing boom to the test** — TechCrunch AI. Analysis piece, part of Anthropic IPO cluster.
- **With the biggest IPO of all time, Anthropic's 'good guy' reputation is on the line** — The Verge AI. Opinion piece, part of Anthropic IPO cluster.
- **Nvidia Responds to Gentlemen Ransomware Claim** — SecurityWeek. Ransomware claim with denial, no TTPs/IOCs; duplicate of BleepingComputer item below.
- **Why Holiday Security Can't Wait for Black Friday** — Dark Reading. Generic seasonal advice listicle.
- **Superhuman pushes its Go assistant everywhere** — TechCrunch AI. Product news, no security angle.
- **Drupal patches critical RCE flaw, warns exploits may surface quickly** — BleepingComputer. Merged as additional source into item 13.
- **I let Apple's always-listening AI summarize my life for two weeks** — The Verge AI. Personal review/opinion piece.
- **Canva adds an AI 'off' button** — The Verge AI. Minor UI feature, no security substance.
- **StepSecurity Secures $20 Million to Expand Supply Chain Protection** — SecurityWeek. Funding announcement, no new technical capability detailed.
- **The Governance Gap in Open-Weight AI and What to Do About It** — SecurityWeek. Opinion/analysis piece, no concrete news event.
- **libumqtt** — CISA Alerts. Routine ICS advisory for a narrower embedded library, no active exploitation.
- **Autonomy Logic OpenPLC Runtime** — CISA Alerts. Routine ICS advisory, narrower product scope, no active exploitation.
- **Microsoft confirms app installation, launch issues after hotpatch** — BleepingComputer. Operational bug report, not a security issue.
- **F5 Patches Critical NGINX2Root Flaws as PoC Exploits Go Public** — SecurityWeek. Merged as additional source into item 12.
- **NVIDIA investigating Gentlemen ransomware breach claims** — BleepingComputer. Duplicate of the SecurityWeek item above; claim under investigation, no TTPs/IOCs confirmed.
