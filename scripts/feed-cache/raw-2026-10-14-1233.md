# Raw feed pull — 2026-10-14 12:33 UTC

- Window: last 14h
- Feeds: 26 (25 ok, 0 empty, 1 error)
- Items kept after dedup: 27 (seen-skipped: 0, near-dup-skipped: 0)

## Feed health

- [OK] The Hacker News (7 items)
- [OK] BleepingComputer (2 items)
- [OK] Krebs on Security (1 items)
- [OK] Dark Reading (1 items)
- [OK] The Record (Recorded Future) (1 items)
- [OK] SecurityWeek (6 items)
- [ERR] SentinelOne Labs (0 items) — HTTP 404
- [OK] Cisco Talos (0 items)
- [OK] Unit 42 (Palo Alto) (0 items)
- [OK] Flashpoint (0 items)
- [OK] PortSwigger Research (0 items)
- [OK] Trail of Bits (1 items)
- [OK] Google Project Zero (0 items)
- [OK] Securelist (Kaspersky GReAT) (0 items)
- [OK] OpenAI Blog (1 items)
- [OK] Google DeepMind (1 items)
- [OK] Google AI Blog (0 items)
- [OK] Hugging Face Blog (0 items)
- [OK] TechCrunch AI (5 items)
- [OK] Simon Willison (1 items)
- [OK] Lilian Weng (OpenAI) (0 items)
- [OK] The Verge AI (0 items)
- [OK] AWS Security Blog (0 items)
- [OK] AWS News Blog (0 items)
- [OK] Google Cloud Security (0 items)
- [OK] CISA Alerts (0 items)

## Items

### 1. Hirudo Android malware replaces banking apps to evade security checks
- Section: Cybersecurity — Primary
- Source: BleepingComputer
- URL: https://www.bleepingcomputer.com/news/security/hirudo-android-malware-replaces-banking-apps-to-evade-security-checks/
- Published: 2026-10-14T11:41:20+00:00
- Summary: A new Android malware called Hirudo steals bank account credentials by replacing legitimate banking apps with modified versions that disable security checks. [...]

### 2. Researchers Used a Public OpenAI Model to Build a $250,000 Chrome Full-Chain Exploit in Six Days
- Section: Cybersecurity — Primary
- Source: The Hacker News
- URL: https://thehackernews.com/2026/10/researchers-used-public-openai-model-to.html
- Published: 2026-10-14T11:19:02+00:00
- Summary: A team at security firm XBOW chained three then-unknown Google Chrome bugs into a single attack that runs code on a Windows computer when the user only loads a web page, the company said.

Its researchers built the attack in six days by directing AI agents running OpenAI's publicly available GPT-5.6 Sol model. Google has since confirmed all three bugs,&nbsp;fixed them, and paid XBOW its top $

### 3. Hirudo Android Trojan Uses Patched Banking Apps to Bypass Their Built-In Security Checks
- Section: Cybersecurity — Primary
- Source: The Hacker News
- URL: https://thehackernews.com/2026/10/hirudo-android-trojan-uses-patched.html
- Published: 2026-10-14T11:08:22+00:00
- Summary: Cybersecurity researchers have disclosed details of a new Android banking trojan called Hirudo that works by replacing legitimate banking apps with purpose-built patched versions designed to bypass security checks from inside the app itself, marking a new escalation in financial fraud.&nbsp;

Dutch mobile security company ThreatFabric said it identified replacements for eight Indonesian banking

### 4. An AI Agent Found a Critical OTP Bypass in Production. The Attack Was the Easy Part.
- Section: Cybersecurity — Primary
- Source: The Hacker News
- URL: https://thehackernews.com/2026/10/an-ai-agent-found-critical-otp-bypass.html
- Published: 2026-10-14T11:00:00+00:00
- Summary: The bug was simple: the login let you choose where your sign-in code went. Proving it on a live website was the hard part.

TL;DR


  During an authorized assessment, an AI pentesting agent found a critical authentication bypass on a major insurer's production website, on its own.
  One login request let the user choose where the one-time passcode went.
  The attack was the easy part. Proving it

### 5. Package managers have an integrity problem
- Section: Cybersecurity — Research & Threat Intel
- Source: Trail of Bits
- URL: https://blog.trailofbits.com/2026/10/14/package-managers-have-an-integrity-problem/
- Published: 2026-10-14T11:00:00+00:00
- Summary: I tested 25 of the most popular package managers to check whether they detect a compromised package repository injecting malicious code into legitimate packages. This code integrity problem could be solved using cryptographic hashes or signatures, but many package managers are still vulnerable to this threat. Of the 25 package managers reviewed1, fewer than half used lockfiles that checked for tampering by default, and only two verified the integrity of every package they downloaded.
Supply-chain attacks caused by developer compromise are a common story, but imagine what happens if ongoing mit

### 6. Scimplify raises $25M to challenge China’s grip on critical materials with AI
- Section: AI — News & Analysis
- Source: TechCrunch AI
- URL: https://techcrunch.com/2026/10/14/scimplify-raises-25m-to-challenge-chinas-grip-on-critical-materials-with-ai/
- Published: 2026-10-14T11:00:00+00:00
- Summary: Scimplify's annualized revenue run rate has tripled to $200 million as it eyes U.S. expansion.

### 7. US Arrests Two in Crackdown on North Korean IT Worker Laptop Farms
- Section: Cybersecurity — Primary
- Source: SecurityWeek
- URL: https://www.securityweek.com/us-arrests-two-in-crackdown-on-north-korean-it-worker-laptop-farms/
- Published: 2026-10-14T10:55:21+00:00
- Summary: Investigators stormed 40 locations in Texas and seized 187 laptops used by North Korean IT workers to hide their location.
The post US Arrests Two in Crackdown on North Korean IT Worker Laptop Farms appeared first on SecurityWeek.

### 8. Microsoft: Recent Windows updates may trigger Remote Desktop failures
- Section: Cybersecurity — Primary
- Source: BleepingComputer
- URL: https://www.bleepingcomputer.com/news/security/microsoft-recent-windows-updates-may-trigger-remote-desktop-failures/
- Published: 2026-10-14T10:48:09+00:00
- Summary: Microsoft has confirmed that non-admin users may be unable to connect to devices via Remote Desktop after installing recent Windows updates if the "Administrator protection" security feature is enabled. [...]

### 9. AI-Found Linux Kernel Flaw Gives Local Users Root, and Can Break a Guest Out to the Host
- Section: Cybersecurity — Primary
- Source: The Hacker News
- URL: https://thehackernews.com/2026/10/ai-found-linux-kernel-flaw-gives-local.html
- Published: 2026-10-14T07:46:57+00:00
- Summary: A flaw in Linux's vhost subsystem lets a local user read and write kernel memory at will and become root across nearly a decade of kernel versions. In one virtualization setup, it lets an untrusted virtual machine write to the host's memory and hijack the program that runs the virtual machine.

The bug is tracked as&nbsp;CVE-2026-74580&nbsp;and named Vghost. Tencent Zhuque Lab, which found the

### 10. Chrome, Firefox Updates Patch 114 Flaws as Mozilla Unveils Firefox Enterprise
- Section: Cybersecurity — Primary
- Source: SecurityWeek
- URL: https://www.securityweek.com/chrome-firefox-updates-patch-114-flaws-as-mozilla-unveils-firefox-enterprise/
- Published: 2026-10-14T07:38:51+00:00
- Summary: Mozilla has introduced Firefox Enterprise for organizations with strict compliance, governance, and security requirements.
The post Chrome, Firefox Updates Patch 114 Flaws as Mozilla Unveils Firefox Enterprise appeared first on SecurityWeek.

### 11. Citrix, Fortinet, Ivanti Patch 29 Vulnerabilities Across Their Products
- Section: Cybersecurity — Primary
- Source: SecurityWeek
- URL: https://www.securityweek.com/citrix-fortinet-ivanti-patch-29-vulnerabilities-across-their-products/
- Published: 2026-10-14T07:26:35+00:00
- Summary: Critical-severity flaws could lead to authentication bypass, code execution, and sensitive authentication information leaks.
The post Citrix, Fortinet, Ivanti Patch 29 Vulnerabilities Across Their Products appeared first on SecurityWeek.

### 12. Microsoft Patches Record 1,413 Vulnerabilities, Including Exploited Windows Zero-Day
- Section: Cybersecurity — Primary
- Source: SecurityWeek
- URL: https://www.securityweek.com/microsoft-patches-record-1413-vulnerabilities-including-exploited-windows-zero-day/
- Published: 2026-10-14T07:16:12+00:00
- Summary: The most important is CVE-2026-96951, a security feature bypass flaw in Windows that has been exploited in the wild.
The post Microsoft Patches Record 1,413 Vulnerabilities, Including Exploited Windows Zero-Day appeared first on SecurityWeek.

### 13. SAP Patches Critical NetWeaver, S/4HANA Vulnerabilities
- Section: Cybersecurity — Primary
- Source: SecurityWeek
- URL: https://www.securityweek.com/sap-patches-critical-netweaver-s-4hana-vulnerabilities/
- Published: 2026-10-14T06:12:10+00:00
- Summary: The bugs could allow attackers to invoke internal operations and execute code, completely compromising the system.
The post SAP Patches Critical NetWeaver, S/4HANA Vulnerabilities appeared first on SecurityWeek.

### 14. Four-Byte Write and Timing Bug Let Researchers Run Code in Windows SmartScreen Enclave
- Section: Cybersecurity — Primary
- Source: The Hacker News
- URL: https://thehackernews.com/2026/10/four-byte-write-and-timing-bug-let.html
- Published: 2026-10-14T05:52:28+00:00
- Summary: Security researchers ran their own code inside a protected part of Windows that is meant to stay sealed off even when the rest of the computer is taken over.

The protected area is a VBS enclave, an isolated slice of memory the operating system uses to guard secrets, and the one they broke into handles passwords for a Windows anti-phishing feature.

The work was done in a lab as a proof of

### 15. Ransomware Gangs Embrace Physical Threats, Family Stalking?
- Section: Cybersecurity — Primary
- Source: Dark Reading
- URL: https://www.darkreading.com/cybersecurity-analytics/ransomware-gangs-physical-threats-family-stalking
- Published: 2026-10-14T05:00:00+00:00
- Summary: Organizations are reporting that employees face threats to their families, stalking, physical violence, and abduction. But these alarming claims are hard to verify.

### 16. Microsoft Patches Record 1,413 Flaws, Including Exploited Windows Shell Bug
- Section: Cybersecurity — Primary
- Source: The Hacker News
- URL: https://thehackernews.com/2026/10/microsoft-patches-record-1413-flaws.html
- Published: 2026-10-14T04:34:43+00:00
- Summary: Microsoft on Tuesday shattered its own Patch Tuesday record by shipping patches for a whopping 1,413 vulnerabilities, including one that it said has come under active exploitation.

These include 1,102 flaws in Windows, 134 in Office, 61 in Developer Tools, 36 in SharePoint Server, and 22 in SQL Server. Of these, more than 670 relate to privilege escalation, followed by over 300 remote code

### 17. Google DeepMind and Singapore Government collaborate to build fine-tuned AI model for scam detection
- Section: AI — Labs & Model Launches
- Source: Google DeepMind
- URL: https://deepmind.google/blog/on-device-ai-scam-detection-mddi/
- Published: 2026-10-14T02:00:14+00:00
- Summary: Learn how Google DeepMind and GovTech Singapore uses lightweight on-device Gemma models to intercept conversational scams in private chats with zero cloud data egress.

### 18. OpenAI Employee Arrested for Allegedly Planting Hidden Recorder in Executive Conference Room
- Section: Cybersecurity — Primary
- Source: The Hacker News
- URL: https://thehackernews.com/2026/10/openai-employee-arrested-for-allegedly.html
- Published: 2026-10-14T01:59:25+00:00
- Summary: A Saudi national and employee of OpenAI has been arrested for allegedly planting a hidden recording device in an executive conference room at the company's San Francisco offices to covertly record sensitive conversations.

Abdulrahman Alfozan, 35, has been charged with using or endeavoring to use an electronic, mechanical, or other device to intercept oral communications. He was arrested by

### 19. The EU’s next chapter in AI is agentic
- Section: AI — Labs & Model Launches
- Source: OpenAI Blog
- URL: https://openai.com/index/the-eus-next-chapter-in-ai-is-agentic
- Published: 2026-10-14T00:00:00+00:00
- Summary: New analysis shows how agentic AI adoption is growing across EU enterprises and small businesses—and where deeper use could unlock more value.

### 20. Microsoft Patches More Than 1,400 Security Flaws
- Section: Cybersecurity — Primary
- Source: Krebs on Security
- URL: https://krebsonsecurity.com/2026/10/microsoft-patches-more-than-1400-security-flaws/
- Published: 2026-10-13T23:24:53+00:00
- Summary: Microsoft today issued updates to fix more than 1,400 security vulnerabilities in its Windows operating systems and other software. Today's epic patch batch dwarfs September's record of nearly 1,000 fixes, which was already about ten times the normal monthly patch load from Redmond.

### 21. Science Corporation implants its vision-restoring chip in its first Stargardt disease patient
- Section: AI — News & Analysis
- Source: TechCrunch AI
- URL: https://techcrunch.com/2026/10/13/science-corporation-implants-its-vision-restoring-chip-in-its-first-stargardt-disease-patient/
- Published: 2026-10-13T23:13:31+00:00
- Summary: Max Hodak, the former president and co-founder of Neuralink, detailed onstage at TechCrunch Disrupt how his company's work with PRIMA is part of its path toward a novel brain-computer interface (BCI).

### 22. Employee Arrested After Listening Device Found in OpenAI Conference Room, FBI and the Company Say
- Section: Cybersecurity — Primary
- Source: SecurityWeek
- URL: https://www.securityweek.com/employee-arrested-after-listening-device-found-in-openai-conference-room-fbi-and-the-company-say/
- Published: 2026-10-13T23:07:00+00:00
- Summary: Saudi national Abdulrahman Alfozan was arrested Friday and terminated by OpenAI.
The post Employee Arrested After Listening Device Found in OpenAI Conference Room, FBI and the Company Say appeared first on SecurityWeek.

### 23. Cerebras CEO says we’re nearing a future where everyone has a personal AI assistant at home
- Section: AI — News & Analysis
- Source: TechCrunch AI
- URL: https://techcrunch.com/2026/10/13/cerebras-ceo-says-were-nearing-a-future-where-everyone-has-a-personal-ai-assistant-at-home/
- Published: 2026-10-13T23:05:34+00:00
- Summary: Cerebras CEO Andrew Feldman predicts a future where personal AI assistants become as commonplace as household appliances, running partly on local devices and partly in the cloud.

### 24. Redesigning source control at Anthropic
- Section: AI — News & Analysis
- Source: Simon Willison
- URL: https://simonwillison.net/2026/Oct/13/redesigning-source-control-at-anthropic/
- Published: 2026-10-13T23:00:06+00:00
- Summary: Redesigning source control at Anthropic
Interesting piece from Anthropic describing why and how they built their own custom alternative to Git, based on the dramatic increase in rate of changes to their code after the past six months.

In May 2026, Anthropic averaged around 2,500 code changes merged per day; as of September, we merged over 30,000 per day.

They included a chart showing those changes. I had Claude modify their chart (code here) to add markers for the public releases of each of their models in 2026:

This shows public release dates, not the date when models became available for 

### 25. Saudi national charged with planting spy device in OpenAI executive conference room
- Section: Cybersecurity — Primary
- Source: The Record (Recorded Future)
- URL: https://therecord.media/saudi-national-charged-with-spy-device-openai
- Published: 2026-10-13T23:00:00+00:00
- Summary: Abdulrahman Alfozan, 35, a Saudi national working as an engineer for OpenAI, was charged Tuesday with secretly bugging an executive conference room at one of the company’s buildings in San Francisco.

### 26. Industrial Next wants factory robots to switch tasks in minutes, not weeks
- Section: AI — News & Analysis
- Source: TechCrunch AI
- URL: https://techcrunch.com/2026/10/13/industrial-next-wants-factory-robots-to-switch-tasks-in-minutes-not-weeks/
- Published: 2026-10-13T23:00:00+00:00
- Summary: Industrial Next helps manufacturers automate complex, delicate tasks that have traditionally required human labor.

### 27. Cerebras CEO pushes back on AI doomsday warnings
- Section: AI — News & Analysis
- Source: TechCrunch AI
- URL: https://techcrunch.com/2026/10/13/cerebras-ceo-pushes-back-on-ai-doomsday-warnings/
- Published: 2026-10-13T22:36:59+00:00
- Summary: Cerebras CEO Andrew Feldman has a message for AI leaders spreading doomsday warnings: Maybe stop talking? At TechCrunch Disrupt, he argued that the industry's focus on AI's risks is drowning out its potential benefits.
