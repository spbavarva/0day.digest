# Digest — 2026-04-27 PM

- Window: last 14h
- Raw items considered: 44
- Relevant: 19
- Skippable: 25

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Incomplete Windows Patch Exposes Systems to Zero-Click APT28 Attack Vector — `2026-04-27-windows-patch-bypass-zero-click-apt28.md`
- [x] **[CRITICAL]** PyPI Package 'elementary-data' with 1.1M Monthly Downloads Backdoored to Steal Credentials — `2026-04-27-pypi-elementary-data-supply-chain-infostealer.md`
- [x] **[HIGH]** ADT Data Breach Confirmed at 5.5 Million Records; ShinyHunters Identified as Attacker — `2026-04-27-adt-55m-breach-shinyhunters-confirmed.md`
- [x] **[HIGH]** Checkmarx Confirms GitHub Repository Data Published on Dark Web After March Supply Chain Attack — `2026-04-27-checkmarx-github-data-dark-web.md`
- [x] **[HIGH]** Medtronic Confirms Breach After Hackers Claim 9 Million Records Stolen — `2026-04-27-medtronic-breach-9m-records.md`
- [x] **[HIGH]** Unpatched 'PhantomRPC' Windows Flaw Yields Five Privilege Escalation Paths via RPC — `2026-04-27-phantomrpc-windows-unpatched-privilege-escalation.md`
- [x] **[HIGH]** 15-Year-Old OpenSSH Flaw Allowed Full Root Shell Access via Certificate Principal Parsing Bug — `2026-04-27-openssh-15-year-root-shell-flaw.md`
- [x] **[HIGH]** Hackers Impersonate Microsoft Teams Help Desk Agents to Deploy Data-Stealing Malware — `2026-04-27-microsoft-teams-helpdesk-impersonation-malware.md`
- [x] **[HIGH]** 73 Fake VS Code Extensions on Open VSX Deliver GlassWorm v2 Infostealer — `2026-04-27-fake-vscode-extensions-glassworm-v2-infostealer.md`
- [x] **[HIGH]** PhantomCore Chains Three TrueConf Vulnerabilities for RCE Against Russian Networks — `2026-04-27-phantomcore-trueconf-exploit-chain-russia.md`
- [x] **[HIGH]** Energy and Water Management Firm Itron Confirms April Breach of Corporate Systems — `2026-04-27-itron-energy-water-utility-hack.md`
- [x] **[HIGH]** 'Pack2TheRoot' PackageKit Race Condition Lets Unprivileged Linux Users Escalate to Root — `2026-04-27-pack2theroot-linux-packagekit-privilege-escalation.md`
- [x] **[MEDIUM]** Google: Indirect Prompt Injection Attacks on AI Systems Increasing, Sophistication Still Low — `2026-04-27-google-ai-prompt-injection-attacks-increasing.md`
- [x] **[MEDIUM]** Claude Mythos Accelerates Vulnerability Discovery—but Remediation Teams Aren't Keeping Pace — `2026-04-27-mythos-vulnerability-discovery-remediation-gap.md`
- [x] **[MEDIUM]** Newly Discovered 'fast16' Malware Predates Stuxnet by Five Years, Rewriting Cyber Sabotage History — `2026-04-27-fast16-malware-predates-stuxnet.md`
- [x] **[MEDIUM]** UNC6692 Combines Email Bombing and Social Engineering to Deploy Persistent 'Snow' Malware Family — `2026-04-27-unc6692-snow-malware-email-bombing.md`
- [x] **[MEDIUM]** CVE-2026-6770: Firefox Flaw Enables Fingerprinting and Deanonymization of Tor Browser Users — `2026-04-27-cve-2026-6770-firefox-tor-user-fingerprinting.md`
- [x] **[MEDIUM]** Fake CAPTCHA Campaign Linked to 120 Keitaro Instances Drives Large-Scale IRSF SMS Fraud — `2026-04-27-fake-captcha-irsf-keitaro-sms-fraud.md`
- [x] **[INFORMATIONAL]** OpenAI and Microsoft Restructure Partnership: AGI Clause Dropped, AWS Sales Unlocked — `2026-04-27-openai-microsoft-partnership-restructure-agi-clause-dropped.md`

## Relevant (details)

### 1. Incomplete Windows Patch Exposes Systems to Zero-Click APT28 Attack Vector
- **Source:** SecurityWeek — https://www.securityweek.com/incomplete-windows-patch-opens-door-to-zero-click-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `microsoft`, `apt`
- **Slug:** `windows-patch-bypass-zero-click-apt28`
- **Must-know:** yes
- **Summary:** A Windows security patch was found incomplete, leaving systems exposed to zero-click attacks. The original vulnerability was actively exploited by APT28 against Ukraine and EU targets, and the patch fails to fully close the attack surface.

### 2. PyPI Package 'elementary-data' with 1.1M Monthly Downloads Backdoored to Steal Credentials
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/pypi-package-with-11m-monthly-downloads-hacked-to-push-infostealer/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `pypi`, `malware`
- **Slug:** `pypi-elementary-data-supply-chain-infostealer`
- **Must-know:** yes
- **Summary:** The `elementary-data` PyPI package (1.1M monthly downloads) was compromised to deliver an infostealer targeting developer credentials and crypto wallets. Any environment that pulled the package should be treated as compromised and credentials rotated.

### 3. ADT Data Breach Confirmed at 5.5 Million Records; ShinyHunters Identified as Attacker
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/home-security-giant-adt-data-breach-affects-55-million-people/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `ransomware`
- **Slug:** `adt-55m-breach-shinyhunters-confirmed`
- **Must-know:** no
- **Summary:** ShinyHunters stole personal data from 5.5 million ADT customers, confirmed via Have I Been Pwned. This is a scope update to ADT's initial breach disclosure from earlier this month.

### 4. Checkmarx Confirms GitHub Repository Data Published on Dark Web After March Supply Chain Attack
- **Source:** The Hacker News — https://thehackernews.com/2026/04/checkmarx-confirms-github-repository.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `github`, `data-breach`
- **Slug:** `checkmarx-github-data-dark-web`
- **Must-know:** no
- **Summary:** Checkmarx confirmed its GitHub repository data is on the dark web, accessed via the March 23 supply chain attack. Organizations using Checkmarx should rotate any tokens or credentials in shared repository configurations.

### 5. Medtronic Confirms Breach After Hackers Claim 9 Million Records Stolen
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/medtronic-confirms-breach-after-hackers-claim-9-million-records-theft/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `healthcare`
- **Slug:** `medtronic-breach-9m-records`
- **Must-know:** no
- **Summary:** Medtronic confirmed unauthorized access to corporate IT systems; hackers claim 9 million records stolen. Healthcare organizations with Medtronic integrations should review shared credential exposure.

### 6. Unpatched 'PhantomRPC' Windows Flaw Yields Five Privilege Escalation Paths via RPC
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/unpatched-phantomrpc-flaw-windows-privilege-escalation
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`, `microsoft`, `zero-day`
- **Slug:** `phantomrpc-windows-unpatched-privilege-escalation`
- **Must-know:** no
- **Summary:** An unpatched architectural weakness in Windows RPC exposes five distinct privilege escalation paths. No patch is available; organizations should monitor for a Microsoft advisory and tune endpoint detection for atypical RPC patterns.

### 7. 15-Year-Old OpenSSH Flaw Allowed Full Root Shell Access via Certificate Principal Parsing Bug
- **Source:** SecurityWeek — https://www.securityweek.com/openssh-flaw-allowing-full-root-shell-access-lurked-for-15-years/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `rce`, `privilege-escalation`, `cve`
- **Slug:** `openssh-15-year-root-shell-flaw`
- **Must-know:** no
- **Summary:** A 15-year-old OpenSSH bug in certificate principal handling (comma interpreted as list separator) enabled full root shell access and has now been patched. Certificate-based SSH environments should update immediately.

### 8. Hackers Impersonate Microsoft Teams Help Desk Agents to Deploy Data-Stealing Malware
- **Source:** The Record (Recorded Future) — https://therecord.media/microsoft-teams-hackers-mandiant
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `malware`, `microsoft`
- **Slug:** `microsoft-teams-helpdesk-impersonation-malware`
- **Must-know:** no
- **Summary:** Mandiant identified attackers impersonating Teams IT support workers via external Teams messages to install data-stealing malware. Bypasses email phishing filters; organizations should restrict external Teams comms and train staff to verify IT identity out-of-band.

### 9. 73 Fake VS Code Extensions on Open VSX Deliver GlassWorm v2 Infostealer
- **Source:** The Hacker News — https://thehackernews.com/2026/04/researchers-uncover-73-fake-vs-code.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `developer-tools`
- **Slug:** `fake-vscode-extensions-glassworm-v2-infostealer`
- **Must-know:** no
- **Summary:** 73 cloned VS Code extensions on Open VSX are linked to the GlassWorm v2 infostealer campaign targeting developer credentials. Affects VSCodium and Eclipse Theia users; six confirmed malicious extensions identified.

### 10. PhantomCore Chains Three TrueConf Vulnerabilities for RCE Against Russian Networks
- **Source:** The Hacker News — https://thehackernews.com/2026/04/phantomcore-exploits-trueconf.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `rce`, `apt`
- **Slug:** `phantomcore-trueconf-exploit-chain-russia`
- **Must-know:** no
- **Summary:** Pro-Ukrainian group PhantomCore has been actively exploiting a three-bug chain in TrueConf video conferencing servers since September 2025. Organizations outside Russia running TrueConf must patch all three CVEs to break the kill chain.

### 11. Energy and Water Management Firm Itron Confirms April Breach of Corporate Systems
- **Source:** SecurityWeek — https://www.securityweek.com/energy-and-water-management-firm-itron-hacked/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `ics`
- **Slug:** `itron-energy-water-utility-hack`
- **Must-know:** no
- **Summary:** Itron, a utility technology provider serving smart grids and water systems globally, confirmed a breach discovered April 13. Scope limited to corporate IT per current disclosure; utilities running Itron products should verify with vendor and monitor for IOCs.

### 12. 'Pack2TheRoot' PackageKit Race Condition Lets Unprivileged Linux Users Escalate to Root
- **Source:** SecurityWeek — https://www.securityweek.com/easily-exploitable-pack2theroot-linux-vulnerability-leads-to-root-access/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`, `cve`
- **Slug:** `pack2theroot-linux-packagekit-privilege-escalation`
- **Must-know:** no
- **Summary:** An easily exploitable race condition in PackageKit allows unprivileged local Linux users to gain root. Affects Fedora, Ubuntu, openSUSE, and other major distributions; patch immediately.

### 13. Google: Indirect Prompt Injection Attacks on AI Systems Increasing, Sophistication Still Low
- **Source:** SecurityWeek — https://www.securityweek.com/malicious-ai-prompt-injection-attacks-increasing-but-sophistication-still-low-google/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `llm`, `ai-safety`, `vulnerability`, `google`
- **Slug:** `google-ai-prompt-injection-attacks-increasing`
- **Must-know:** no
- **Summary:** Google research documents growing frequency of indirect prompt injection attempts against AI systems, with some confirmed malicious exploits. Low sophistication currently; organizations deploying AI agents should implement input validation and output monitoring.

### 14. Claude Mythos Accelerates Vulnerability Discovery—but Remediation Teams Aren't Keeping Pace
- **Source:** The Hacker News — https://thehackernews.com/2026/04/mythos-changed-math-on-vulnerability.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `anthropic`, `llm`, `vulnerability`, `ai-safety`
- **Slug:** `mythos-vulnerability-discovery-remediation-gap`
- **Must-know:** no
- **Summary:** Analysis post-Mythos Preview launch flags an asymmetry where AI-accelerated discovery is outpacing human-paced remediation pipelines. Teams using AI-assisted scanning need equal investment in remediation workflow automation.

### 15. Newly Discovered 'fast16' Malware Predates Stuxnet by Five Years
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/20-year-old-malware-rewrites-history-of-cyber-sabotage
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `apt`
- **Slug:** `fast16-malware-predates-stuxnet`
- **Must-know:** no
- **Summary:** The "fast16" malware framework predates Stuxnet by ~5 years, revising the timeline of nation-state destructive operations. Historical finding with implications for ICS threat models and APT attribution research.

### 16. UNC6692 Combines Email Bombing and Social Engineering to Deploy Persistent 'Snow' Malware Family
- **Source:** SecurityWeek — https://www.securityweek.com/unc6692-uses-email-bombing-social-engineering-to-deploy-snow-malware/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`, `apt`
- **Slug:** `unc6692-snow-malware-email-bombing`
- **Must-know:** no
- **Summary:** UNC6692 uses inbox flooding to panic targets into contacting fake IT support, where Snow malware (Snowbelt/Snowglaze/Snowbasin) is installed for persistent access. Mirrors the Teams helpdesk impersonation TTP seen in another item today.

### 17. CVE-2026-6770: Firefox Flaw Enables Fingerprinting and Deanonymization of Tor Browser Users
- **Source:** SecurityWeek — https://www.securityweek.com/firefox-vulnerability-allows-tor-user-fingerprinting/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `cve`, `privacy`
- **Slug:** `cve-2026-6770-firefox-tor-user-fingerprinting`
- **Must-know:** no
- **Summary:** CVE-2026-6770 allows fingerprinting of Tor Browser users, undermining anonymity for journalists and activists. Patched in Firefox 150 and Tor Browser 15.0.10; update immediately.

### 18. Fake CAPTCHA Campaign Linked to 120 Keitaro Instances Drives Large-Scale IRSF SMS Fraud
- **Source:** The Hacker News — https://thehackernews.com/2026/04/fake-captcha-irsf-scam-and-120-keitaro.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `malware`, `fraud`
- **Slug:** `fake-captcha-irsf-keitaro-sms-fraud`
- **Must-know:** no
- **Summary:** Fake CAPTCHA pages trick users into triggering premium-rate international SMS messages generating IRSF revenue for attackers, linked to ~120 Keitaro TDS instances. Telecom operators and enterprises should monitor for unexpected international SMS volume.

### 19. OpenAI and Microsoft Restructure Partnership: AGI Clause Dropped, AWS Sales Unlocked
- **Source:** OpenAI Blog — https://openai.com/index/next-phase-of-microsoft-partnership
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `openai`, `microsoft`, `ai-launch`
- **Slug:** `openai-microsoft-partnership-restructure-agi-clause-dropped`
- **Must-know:** no
- **Summary:** OpenAI and Microsoft's amended deal removes the AGI clause and allows OpenAI to sell on AWS, ending Microsoft's exclusive cloud position. Enterprises building on OpenAI APIs gain new deployment options beyond Azure.

## Skippable

- **OpenAI ends Microsoft legal peril over its $50B Amazon deal** — TechCrunch AI. Duplicate coverage of the OpenAI/Microsoft restructure; official OpenAI Blog post selected instead.
- **Speech translation in Google Meet now rolling out to mobile** — Simon Willison. Consumer AI feature launch, no security angle.
- **DeepMind's David Silver raises $1.1B for Ineffable Intelligence** — TechCrunch AI. VC funding announcement for new AI lab; no security or technical substance.
- **FTC: Americans lost over $2.1 billion to social media scams in 2025** — BleepingComputer. Statistical report with no new technical attack detail or actionable IOCs for practitioners.
- **Microsoft and OpenAI's famed AGI agreement is dead** — The Verge AI. Duplicate coverage of the OpenAI/Microsoft restructure; official OpenAI Blog post selected instead.
- **Investors back Skye's AI home screen app for iPhone** — TechCrunch AI. Non-security SaaS/consumer app launch, no security angle.
- **Can I do that with policy? Understanding AWS Service Authorization Reference** — AWS Security Blog. Educational IAM explainer, not news.
- **Elon Musk and Sam Altman's court battle over the future of OpenAI** — The Verge AI. Legal/business coverage with no technical security substance.
- **Disinformation campaign targeted Tibetan parliament-in-exile elections** — The Record. Influence operations item; no practitioner-actionable technical content.
- **Italy extradites alleged Chinese state hacker to US** — The Record. Law enforcement action; no technical attack details or IOCs.
- **AWS Weekly Roundup: Anthropic & Meta partnership, AWS Lambda S3 Files, etc.** — AWS News Blog. Marketing roundup; individual items already covered elsewhere where relevant.
- **Canva apologizes after AI tool replaces 'Palestine' in designs** — The Verge AI. AI content moderation controversy, not a security incident.
- **Webinar: Spotting cyberattacks before they begin** — BleepingComputer. Sponsored event marketing.
- **⚡ Weekly Recap: Fast16 Malware, XChat Launch, Federal Backdoor, AI Employee Tracking & More** — The Hacker News. Roundup article; individual stories covered separately where relevant.
- **China blocks Meta's $2B Manus deal after months-long probe** — TechCrunch AI. Geopolitical/business item; no technical security content.
- **OpenAI could be making a phone with AI agents replacing apps** — TechCrunch AI. Speculative product rumors, no confirmed news or security angle.
- **Money launderer linked to $230M crypto heist gets 70 months in prison** — BleepingComputer. Law enforcement sentencing; no new technical details.
- **Deepfake Voice Attacks are Outpacing Defenses: What Security Leaders Should Know** — BleepingComputer. Sponsored/vendor marketing content from Adaptive Security.
- **Parsing Agentic Offensive Security's Existential Threat** — Dark Reading. Opinion/analysis piece without new research or news value.
- **Join the new AI Agents Vibe Coding Course from Google and Kaggle** — Google AI Blog. Educational course announcement, not news.
- **The AI-designed car is taking shape** — The Verge AI. Automotive design/technology piece, no security relevance.
- **Meta inks deal for solar power at night, beamed from space** — TechCrunch AI. Energy infrastructure business deal, off-topic.
- **US Launches Sweeping Crackdown on Southeast Asia Cyberscams and Sanctions Cambodian Senator** — SecurityWeek. Policy enforcement action; limited technical content for practitioners.
- **Announcing our partnership with the Republic of Korea** — Google DeepMind. Business/diplomatic partnership announcement, no technical or security substance.
- **Microsoft says Outlook.com outage is causing sign-in failures** — BleepingComputer. Service availability outage, not a security incident.
