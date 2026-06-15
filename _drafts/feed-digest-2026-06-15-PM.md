# Digest — 2026-06-15 PM

- Window: last 14h
- Raw items considered: 19
- Relevant: 7
- Skippable: 12

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Trusted WordPress Plugin Scripts Tampered to Plant Hidden Admin Backdoors — `2026-06-15-wordpress-plugin-supply-chain-backdoor-pushengage-optinmonster.md`
- [x] **[HIGH]** ShinyHunters Salesforce Breach Exposes 137,000 Infinite Campus School Staff Accounts — `2026-06-15-infinite-campus-data-breach-shinyhunters.md`
- [x] **[HIGH]** Hacker Breaches France's Tchap Government Messaging Platform, ~73,000 Accounts Affected — `2026-06-15-french-government-tchap-messaging-platform-breached.md`
- [x] **[HIGH]** Palo Alto Warns of Active Exploitation of PAN-OS GlobalProtect Auth Bypass (CVE-2026-0257) — `2026-06-15-panos-globalprotect-cve-2026-0257-active-exploitation.md`
- [x] **[MEDIUM]** ShinyHunters Claims Council of Europe Hack, Threatens to Leak 297GB of Data — `2026-06-15-shinyhunters-claims-council-of-europe-hack.md`
- [x] **[MEDIUM]** 152 Malicious Chrome Wallpaper Extensions With 105K Installs Linked to Adware Network — `2026-06-15-chrome-wallpaper-extensions-adware-105k-installs.md`
- [x] **[MEDIUM]** FBI and Google Dismantle 'Outsider Enterprise' Phishing Service Tied to $1.9B in Losses — `2026-06-15-fbi-google-dismantle-outsider-enterprise-phishing.md`

## Relevant (details)

### 1. Trusted WordPress Plugin Scripts Tampered to Plant Hidden Admin Backdoors
- **Source:** The Hacker News — https://thehackernews.com/2026/06/popular-wordpress-plugin-scripts.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`, `appsec`
- **Slug:** `wordpress-plugin-supply-chain-backdoor-pushengage-optinmonster`
- **Must-know:** yes
- **Summary:** Attackers tampered with trusted JS files used by the PushEngage, OptinMonster, and TrustPulse WordPress plugins to silently create admin backdoor accounts when a logged-in admin loaded a page. A hidden plugin maintains persistent access; ordinary visitors are unaffected.

### 2. ShinyHunters Salesforce Breach Exposes 137,000 Infinite Campus School Staff Accounts
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/infinite-campus-data-breach-affects-137-000-school-staff-accounts/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `supply-chain`
- **Slug:** `infinite-campus-data-breach-shinyhunters`
- **Must-know:** no
- **Summary:** ShinyHunters stole personal data for 137,000+ school staff accounts from Infinite Campus via a Salesforce data-theft attack in March 2026. The incident is part of ShinyHunters' broader campaign against Salesforce customers.

### 3. Hacker Breaches France's Tchap Government Messaging Platform, ~73,000 Accounts Affected
- **Source:** SecurityWeek — https://www.securityweek.com/french-government-messaging-platform-breached-by-mysterious-misere-hacker/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `french-government-tchap-messaging-platform-breached`
- **Must-know:** no
- **Summary:** A hacker going by "Misere" breached Tchap, France's sovereign government messaging platform, affecting roughly 73,000 accounts. The attacker claims to have stolen messages and user data; French officials have not detailed the access vector.

### 4. Palo Alto Warns of Active Exploitation of PAN-OS GlobalProtect Auth Bypass (CVE-2026-0257)
- **Source:** The Hacker News — https://thehackernews.com/2026/06/palo-alto-warns-of-active-exploitation.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`
- **Slug:** `panos-globalprotect-cve-2026-0257-active-exploitation`
- **Must-know:** no
- **Summary:** Palo Alto Networks confirmed active exploitation of CVE-2026-0257 (CVSS 7.8), an authentication bypass affecting PAN-OS GlobalProtect portal and gateway components. An unknown threat actor is using it to gain unauthorized portal access.

### 5. ShinyHunters Claims Council of Europe Hack, Threatens to Leak 297GB of Data
- **Source:** SecurityWeek — https://www.securityweek.com/shinyhunters-claims-council-of-europe-hack/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`
- **Slug:** `shinyhunters-claims-council-of-europe-hack`
- **Must-know:** no
- **Summary:** ShinyHunters claims to have hacked the Council of Europe and threatens to leak ~297GB of data including employee personal information. The Council of Europe has not confirmed the breach or its scope.

### 6. 152 Malicious Chrome Wallpaper Extensions With 105K Installs Linked to Adware Network
- **Source:** The Hacker News — https://thehackernews.com/2026/06/152-chrome-wallpaper-extensions-with.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `appsec`
- **Slug:** `chrome-wallpaper-extensions-adware-105k-installs`
- **Must-know:** no
- **Summary:** 152 Chrome "new tab" wallpaper extensions, installed 105,000+ times across 38 publisher accounts and three brand backends, were found distributing adware and generating fake traffic.

### 7. FBI and Google Dismantle 'Outsider Enterprise' Phishing Service Tied to $1.9B in Losses
- **Source:** SecurityWeek — https://www.securityweek.com/fbi-google-dismantle-outsider-enterprise-phishing-service/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`
- **Slug:** `fbi-google-dismantle-outsider-enterprise-phishing`
- **Must-know:** no
- **Summary:** The FBI and Google dismantled "Outsider Enterprise," a phishing-as-a-service platform that ran 9,000+ phishing sites and is estimated to have stolen nearly 4 million credit cards, causing ~$1.9 billion in losses.

## Skippable

- **US Cracks Down on Anthropic AI Models Amid Abuse Concerns** — Dark Reading. Duplicate coverage of the Fable 5/Mythos 5 export control directive story already published on 2026-06-13.
- **Webinar: How behavioral AI stops phishing and account takeovers** — BleepingComputer. Sponsored webinar content, no news value.
- **A satellite just learned to find things on its own — here's what that means** — TechCrunch AI. General AI capability story with no security angle.
- **AWS Weekly Roundup: AWS FinOps Agent in preview, Gemma 4 on Bedrock, Kiro Pro Max, and more** — AWS News Blog. Marketing roundup aggregating multiple announcements without standalone technical substance.
- **Ukrainian Man Pleads Guilty in US to Conti Ransomware Charges** — SecurityWeek. Legal/prosecution news with no new TTPs or IOCs.
- **The Onboarding Password Mistake That Creates Unnecessary Risk** — The Hacker News. Generic security advice/marketing content.
- **Ozempic Maker Novo Nordisk Says Hackers Breached IT Systems** — SecurityWeek. Generic breach disclosure with no scope or technical details.
- **Maine Disables Data Breach Portal Due to Fake Submissions** — SecurityWeek. Regional administrative issue, no technical substance.
- **The AI layoff wave is becoming a powder keg** — TechCrunch AI. Opinion piece without news value.
- **Sniper Dz Scams Target MENA Users via Fake Facebook Offers and Browser Alerts** — The Hacker News. Regional phishing campaign without novel technique.
- **Quoting Julia Evans** — Simon Willison. Short quote, no security/AI news value.
- **Why AI hasn't replaced software engineers, and won't** — Simon Willison. Opinion/analysis piece without news value.
