# Digest — 2026-11-26 PM

- Window: last 14h
- Raw items considered: 22
- Relevant: 13 (11 draft posts; 2 duplicate sources merged into existing entries)
- Skippable: 9

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[MEDIUM]** Fake Paid Expert Interviews Impersonate Brands to Steal Google Logins — `2026-11-26-goodguys-phishing-paid-expert-interviews.md`
- [x] **[MEDIUM]** Remus Infostealer Steals Gmail Messages via Fake Google Sheets Chrome Extension — `2026-11-26-remus-infostealer-fake-google-sheets-extension.md`
- [x] **[HIGH]** North Korea-Linked PolinRider Poisons Over 7,600 GitHub Repositories to Spread Malware — `2026-11-26-polinrider-north-korea-github-supply-chain.md`
- [x] **[CRITICAL]** Critical Juniper Session Smart Conductor Flaw Exploited in Attacks — `2026-11-26-juniper-session-smart-conductor-cve-2026-103406.md`
- [x] **[MEDIUM]** SYS010 Malware Abuses Browser Management to Spy on Gmail, Outlook — `2026-11-26-sys010-malware-browser-management-gmail-outlook.md`
- [x] **[CRITICAL]** Mitel MiCollab Zero-Days Exploited in Suspected AI-Assisted Attacks — `2026-11-26-mitel-micollab-zero-days-ai-assisted-attacks.md`
- [x] **[CRITICAL]** 1Password Hacked: Customer Data and Source Code Stolen in GitHub Account Breach — `2026-11-26-1password-github-breach-source-code-customer-data.md`
- [x] **[MEDIUM]** 42 State Attorneys General Move to Stop Character.AI From Selling Users' Chats — `2026-11-26-character-ai-state-ags-block-chat-data-sale.md`
- [x] **[CRITICAL]** Drupal Warns of New Highly Critical Site Takeover Vulnerability Under Active Exploitation — `2026-11-26-drupal-critical-site-takeover-cve-2026-136716.md`
- [x] **[INFORMATIONAL]** Building on Nemotron 3.5 Parse: Open Data, Fine-Tuning, and Faster Inference — `2026-11-26-nemotron-3-5-parse-open-data-fine-tuning.md`
- [x] **[MEDIUM]** 13 Malicious NuGet Packages Turn Fake .NET Job Assessments Into Malware Delivery Traps — `2026-11-26-malicious-nuget-packages-fake-net-job-assessments.md`

## Relevant (details)

### 1. Fake Paid Expert Interviews Impersonate Brands to Steal Google Logins
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/apple/fake-paid-expert-interviews-impersonate-brands-to-steal-google-logins/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `iam`
- **Slug:** `goodguys-phishing-paid-expert-interviews`
- **Must-know:** no
- **Summary:** An ongoing campaign dubbed "GoodGuys" impersonates Google, Nvidia, Accenture, and SpaceX using fake paid expert-interview invitations to steal corporate Google and Okta credentials. The lure is a novel twist on business-themed phishing aimed at corporate identity infrastructure.

### 2. Remus Infostealer Steals Gmail Messages via Fake Google Sheets Chrome Extension
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/remus-malware-steals-gmail-messages-via-fake-google-sheets-extension/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`, `google`
- **Slug:** `remus-infostealer-fake-google-sheets-extension`
- **Must-know:** no
- **Summary:** The Remus infostealer spreads via a malicious Chrome extension disguised as a Google Sheets add-on and reads Gmail messages from the browser session. Operators have marketed the capability as a Gmail "zero-day," though it's a browser-extension abuse technique rather than a flaw in Gmail itself.

### 3. North Korea-Linked PolinRider Poisons Over 7,600 GitHub Repositories to Spread Malware
- **Source:** The Hacker News — https://thehackernews.com/2026/11/north-korea-linked-polinrider-poisons.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `github`
- **Slug:** `polinrider-north-korea-github-supply-chain`
- **Must-know:** no
- **Summary:** The North Korea-linked PolinRider campaign has planted a Python loader hidden in utils packages or conftest.py files across more than 7,600 GitHub repositories. Evidence suggests the campaign has run since February 2025, making it a long-running, large-scale supply chain poisoning effort.

### 4. Critical Juniper Session Smart Conductor Flaw Exploited in Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/critical-juniper-session-smart-conductor-flaw-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `rce`, `vulnerability`
- **Slug:** `juniper-session-smart-conductor-cve-2026-103406`
- **Must-know:** no
- **Summary:** CVE-2026-103406, a critical flaw in Juniper's Session Smart Conductor, allows remote attackers to execute arbitrary commands as root and is being actively exploited. Affected organizations should patch immediately.

### 5. SYS010 Malware Abuses Browser Management to Spy on Gmail, Outlook
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/sys010-malware-abuses-browser-management-to-spy-on-gmail-outlook/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `google`, `microsoft`
- **Slug:** `sys010-malware-browser-management-gmail-outlook`
- **Must-know:** no
- **Summary:** A new SYS01 variant, SYS010, is delivered via malicious Meta ads and enrolls victim browsers into enterprise-style management to force-install a data-stealing extension. The extension reads Gmail and Outlook webmail content directly from the browser session.

### 6. Mitel MiCollab Zero-Days Exploited in Suspected AI-Assisted Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/mitel-micollab-zero-days-exploited-in-suspected-ai-assisted-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `vulnerability`, `cve`
- **Slug:** `mitel-micollab-zero-days-ai-assisted-attacks`
- **Must-know:** yes
- **Summary:** Accenture says attackers exploited zero-day flaws in Mitel MiCollab before Mitel's advisory was published, in a suspected extortion campaign that may have used AI to speed exploit development. Related MiCollab CVEs were separately added to CISA's KEV catalog this week.

### 7. 1Password Hacked: Customer Data and Source Code Stolen in GitHub Account Breach
- **Source:** The Hacker News — https://thehackernews.com/2026/11/1password-hacked-customer-data-and.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `data-breach`, `github`
- **Slug:** `1password-github-breach-source-code-customer-data`
- **Must-know:** yes
- **Summary:** 1Password disclosed that an attacker compromised an employee's GitHub account to push malicious code and access backend systems, exposing some customer information and internal source code. The company says customer password vaults and other secrets were not accessed.

### 8. 42 State Attorneys General Move to Stop Character.AI From Selling Users' Chats
- **Source:** The Verge AI — https://www.theverge.com/policy/1042620/character-ai-sale-state-ags-block-selling-users-chats
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-safety`, `ai-regulation`, `llm`
- **Slug:** `character-ai-state-ags-block-chat-data-sale`
- **Must-know:** no
- **Summary:** A coalition of 42 state attorneys general is seeking to block Character.AI from selling user data during its Chapter 11 bankruptcy proceedings, arguing it could otherwise auction off chat histories from more than 21 million U.S. accounts. No ruling has been issued yet.

### 9. Drupal Warns of New Highly Critical Site Takeover Vulnerability Under Active Exploitation
- **Source:** The Hacker News — https://thehackernews.com/2026/11/drupal-warns-of-new-highly-critical.html (also SecurityWeek — https://www.securityweek.com/drupal-installer-patch-left-a-gap-attackers-are-already-exploiting/)
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`
- **Slug:** `drupal-critical-site-takeover-cve-2026-136716`
- **Must-know:** yes
- **Summary:** Drupal disclosed CVE-2026-136716, a highly critical site-takeover flaw already under active exploitation, caused by installer states left vulnerable after an earlier patch for CVE-2026-132165 (Fail2Install). Site operators should apply the newest update rather than relying on the prior fix.

### 10. Building on Nemotron 3.5 Parse: Open Data, Fine-Tuning, and Faster Inference
- **Source:** Hugging Face Blog — https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `model-release`, `ai-launch`
- **Slug:** `nemotron-3-5-parse-open-data-fine-tuning`
- **Must-know:** no
- **Summary:** NVIDIA published a follow-up on its Nemotron 3.5 Parse model covering open training data, fine-tuning workflows, and faster inference. The source summary was thin, so no further technical detail is available.

### 11. 13 Malicious NuGet Packages Turn Fake .NET Job Assessments Into Malware Delivery Traps
- **Source:** The Hacker News — https://thehackernews.com/2026/11/13-malicious-nuget-packages-turn-fake.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `supply-chain`, `malware`, `nuget`
- **Slug:** `malicious-nuget-packages-fake-net-job-assessments`
- **Must-know:** no
- **Summary:** Socket researchers found 13 malicious NuGet packages, mostly posing as WinUI 3 and WPF button controls, distributed as fake take-home .NET job assessments. Building or running the packages triggers malware delivery, turning a common recruiting technique into a supply chain attack vector.

## Skippable

- **FIFA Says It Has Been Victim of a Cyberattack** — SecurityWeek. Generic breach disclosure; FIFA didn't disclose timing or technical nature of the incident.
- **As Anthropic IPOs, Grand Theft Auto VI proves why efficiency isn't a virtue** — TechCrunch AI. Opinion piece using the Anthropic IPO as a hook; no substantive AI news.
- **Quoting Jack Despain Zhou** — Simon Willison. Commentary/quote post on AI "de-individualization," no news value.
- **Introducing the llama.cpp benchmark dashboard for AMD Ryzen and Radeon** — Hugging Face Blog. Generic benchmarking tooling announcement, no capability jump or security angle.
- **Most Wanted: The Phishing Kits and Techniques Getting Past Security Controls** — The Hacker News (Push Security). Vendor survey/marketing content; no specific novel technique disclosed in the summary.
- **Cyprus Becomes Espionage Target for Iranian Hackers** — Dark Reading. Regional espionage report, thin on technical detail or IOCs.
- **Hackers Exploit 10 Vulnerabilities Across Mitel, Juniper, Vates, and Danfoss Products** — The Hacker News (CISA KEV). Mitel and Juniper flaws already covered individually above; Vates/Danfoss entries lack technical detail in this roundup.
- **sqlite3_rsync: Database Remote-Copy Tool For SQLite** — Simon Willison. Generic database tooling post, no security angle.
- **The New York Times warns photographers not to update Photoshop over AI features** — Simon Willison. Opinion/commentary, no news value.
