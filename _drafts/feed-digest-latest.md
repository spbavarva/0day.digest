# Digest — 2026-08-21 PM

- Window: last 14h
- Raw items considered: 37
- Relevant: 13
- Skippable: 24

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Hundreds of Leaked AWS Keys Give Full Control Over Corporate Accounts — `2026-08-21-leaked-aws-keys-corporate-accounts.md`
- [x] **[CRITICAL]** Rust Supply Chain Attack Linked to North Korean Hackers — `2026-08-21-rust-arrayref-supply-chain-attack-north-korea.md`
- [x] **[CRITICAL]** GitLab CVE-2026-19478 Comes Under Active Exploitation Within Days of Disclosure — `2026-08-21-gitlab-cve-2026-19478-active-exploitation.md`
- [x] **[CRITICAL]** Microsoft Entra ID Flaw (CVSS 10.0) Exploited in Wild, Allows Remote Code Execution — `2026-08-21-microsoft-entra-id-cvss10-rce-exploited.md`
- [x] **[HIGH]** Microsoft Defender's Own Driver Can Be Weaponized to Delete Security Software at Boot — `2026-08-21-microsoft-defender-driver-weaponized.md`
- [x] **[HIGH]** Encrypted Prompts Bypass AI Safety Guardrails in Grok and Gemini — `2026-08-21-encrypted-prompts-bypass-ai-guardrails.md`
- [x] **[HIGH]** New Phishing Toolkit Uses Passkeys to Maintain Access After Password Resets — `2026-08-21-phishing-toolkit-passkeys-password-reset-bypass.md`
- [x] **[HIGH]** Critical Isolated-vm Vulnerability Leads to RCE on Host — `2026-08-21-isolated-vm-critical-rce-vulnerability.md`
- [x] **[HIGH]** CISA Urges Immediate Patching of Exploited TrueConf Vulnerabilities — `2026-08-21-cisa-trueconf-active-exploitation.md`
- [x] **[HIGH]** Cisco Patches Nine Crosswork and Secure Workload Flaws, Five Scoring CVSS 10.0 — `2026-08-21-cisco-crosswork-secure-workload-flaws.md`
- [x] **[MEDIUM]** The Invisible Passenger in Your Car: Android Head Unit Malware — `2026-08-21-android-head-unit-malware-proxy-botnet.md`
- [x] **[MEDIUM]** Hackers Abuse FTP Server Banners to Deliver New Windows Malware — `2026-08-21-ftp-banner-malware-e4del-pinhole.md`
- [x] **[INFORMATIONAL]** OpenAI Adds Controls That Should've Been There Already — `2026-08-21-openai-adds-ai-security-controls.md`

## Relevant (details)

### 1. Hundreds of Leaked AWS Keys Give Full Control Over Corporate Accounts
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hundreds-of-leaked-aws-keys-give-full-control-over-corporate-accounts/
- **Severity:** critical
- **Tags:** `aws`, `iam`, `cloud-security`, `data-breach`
- **Summary:** More than 9,300 AWS access keys publicly exposed between August 2022 and August 2026 are still active and valid, giving attackers full control over the affected corporate accounts.

### 2. Microsoft Defender's Own Driver Can Be Weaponized to Delete Security Software at Boot
- **Source:** The Hacker News — https://thehackernews.com/2026/08/microsoft-defenders-own-driver-can-be.html
- **Severity:** high
- **Tags:** `vulnerability`, `microsoft`
- **Summary:** Check Point Research disclosed a technique abusing Defender's legitimately signed boot-time remediation driver (BTR.sys) to perform arbitrary kernel-level file/registry operations across Windows 7–11 25H2, without exploiting a software flaw.

### 3. The Invisible Passenger in Your Car: Android Head Unit Malware
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/android-head-unit-malware/121106/
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** Kaspersky found a new Android malware family spreading via built-in updaters of DoFun vehicle head unit firmware, serving ads and enrolling devices into a proxy botnet.

### 4. Encrypted Prompts Bypass AI Safety Guardrails in Grok and Gemini
- **Source:** SecurityWeek — https://www.securityweek.com/encrypted-prompts-bypass-ai-safety-guardrails-in-grok-and-gemini/
- **Severity:** high
- **Tags:** `ai-safety`, `llm`, `prompt-injection`, `google`
- **Summary:** A "Cryptographic Context Injection" technique conceals malicious instructions in encrypted form, decrypting them only inside a trusted execution environment to bypass safety guardrails in Grok and Gemini.

### 5. New Phishing Toolkit Uses Passkeys to Maintain Access After Password Resets
- **Source:** SecurityWeek — https://www.securityweek.com/new-phishing-toolkit-uses-passkeys-to-maintain-access-after-password-resets/
- **Severity:** high
- **Tags:** `phishing`
- **Summary:** The iAuthFlow V2 toolkit can register an attacker-controlled passkey during a phishing session, giving persistent access that survives password resets and session revocation.

### 6. OpenAI Adds Controls That Should've Been There Already
- **Source:** Dark Reading — https://www.darkreading.com/application-security/openai-adds-controls-already
- **Severity:** informational
- **Tags:** `ai-safety`, `openai`, `appsec`
- **Summary:** OpenAI rolled out new AI security controls following last month's Hugging Face incident; coverage notes many should have existed already.

### 7. Critical Isolated-vm Vulnerability Leads to RCE on Host
- **Source:** SecurityWeek — https://www.securityweek.com/critical-isolated-vm-vulnerability-leads-to-rce-on-host/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Summary:** A type confusion bug in the widely used isolated-vm npm package enables a V8 sandbox escape and host process control-flow hijacking, leading to RCE. No active exploitation reported.

### 8. CISA Urges Immediate Patching of Exploited TrueConf Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/cisa-urges-immediate-patching-of-exploited-trueconf-vulnerabilities/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Summary:** CISA ordered federal agencies to prioritize patching two actively exploited TrueConf Server flaws; the Head Mare hacktivist group is exploiting them to deploy PhantomCore malware.

### 9. Cisco Patches Nine Crosswork and Secure Workload Flaws, Five Scoring CVSS 10.0
- **Source:** The Hacker News — https://thehackernews.com/2026/08/cisco-patches-nine-crosswork-and-secure.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `cisco`
- **Summary:** Cisco patched nine Crosswork/Secure Workload flaws — five rated a maximum CVSS 10.0 — as part of an ongoing internal security review.

### 10. Hackers Abuse FTP Server Banners to Deliver New Windows Malware
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-abuse-ftp-server-banners-to-deliver-new-windows-malware/
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** Threat actors hide commands inside FTP server banners to deliver two previously undocumented RATs, E4del and PINHOLE, onto Windows systems.

### 11. Rust Supply Chain Attack Linked to North Korean Hackers
- **Source:** SecurityWeek — https://www.securityweek.com/rust-supply-chain-attack-linked-to-north-korean-hackers/
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`
- **Summary:** A poisoned version of the popular Rust `arrayref` crate added a dependency that fetches a malicious payload from a remote server; researchers link it to North Korean hackers.

### 12. GitLab CVE-2026-19478 Comes Under Active Exploitation Within Days of Disclosure
- **Source:** The Hacker News — https://thehackernews.com/2026/08/gitlab-cve-2026-19478-comes-under.html
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `gitlab`
- **Summary:** CVE-2026-19478 (CVSS 9.4), a GitLab code injection flaw, is under active exploitation days after disclosure — allowing unauthenticated attackers to modify or delete public GitLab projects.

### 13. Microsoft Entra ID Flaw (CVSS 10.0) Exploited in Wild, Allows Remote Code Execution
- **Source:** The Hacker News — https://thehackernews.com/2026/08/microsoft-entra-id-flaw-cvss-100.html
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `microsoft`, `rce`, `iam`
- **Summary:** CVE-2026-69836 (CVSS 10.0), a maximum-severity RCE flaw in Entra ID, has been exploited in the wild; Microsoft says no customer action is required for the fix.

## Skippable

- **Former NSA Director Paul Nakasone Launches National Security Advisory Firm** — SecurityWeek. Career/business news, no technical security substance.
- **U.S. Bank says breach claims related to fourth-party incident** — The Record. Generic disclosure; no evidence own systems compromised.
- **Stop Making TUIs** — Simon Willison. Opinion piece, no security/news value.
- **Cloud CISO Perspectives: Sticking to security fundamentals in the AI era** — Google Cloud Security. Generic newsletter intro, no specific news.
- **Android Car Malware Spreads Through Built-In Updaters for Ad Fraud, Proxy Botnet** — The Hacker News. Duplicate of the Securelist research above.
- **In Other News: Zombie Card Attack, T-Mobile Cut Cable to Stop Hackers, GitHub Denies AI Caused Bug** — SecurityWeek. Roundup of minor stories.
- **Quoting Matt Webb** — Simon Willison. Quote/opinion, no news value.
- **Canada's Hospital for Sick Children attacked by cybercriminals again as employee data stolen** — The Record. Regional breach without TTPs; duplicate below.
- **Microsoft blames Windows gaming issues on RGB lighting devices** — BleepingComputer. Not a security story.
- **Is Online Privacy Possible? How Digital Identities Can Help** — BleepingComputer. Generic privacy advice, marketing content.
- **Calling on Cyber Pros to Help Defend City Hall** — Dark Reading. Recruitment/volunteer content.
- **Starcloud raises $250 million for orbital data centers as launch options dry up** — TechCrunch AI. Funding news, no security/model substance.
- **The DOJ is investigating a16z. What does this mean for venture capital?** — TechCrunch AI. VC/antitrust news, no security angle.
- **Russian network monitoring firm confirms cyberattack claimed by pro-Ukraine hackers** — The Record. Hacktivist claim, no technical detail or IOCs.
- **Microsoft rolls out Classic Outlook theme for New Outlook users** — BleepingComputer. Not a security story.
- **Major YouTube creators are facing backlash for accepting AI money** — The Verge AI. Creator drama, no security/model substance.
- **The Good, the Bad and the Ugly in Cybersecurity – Week 34** — SentinelOne Labs. Weekly roundup; underlying stories already covered individually above.
- **CISA orders feds to patch actively exploited TrueConf Server flaws** — BleepingComputer. Duplicate of SecurityWeek coverage above.
- **From Atari to EVE Online: Building on 15 Years of AI Research in Games** — Google DeepMind. Retrospective research post, no launch/safety substance.
- **Wazuh and AI For Enhanced SOC Workflows** — The Hacker News. Vendor/sponsored content.
- **Microsoft warns of max severity Entra ID flaw exploited in attacks** — BleepingComputer. Duplicate of Hacker News coverage above.
- **SickKids data breach exposes employee and job applicant info** — BleepingComputer. Regional breach without TTPs; duplicate of The Record coverage above.
- **Contractors' CMMC Confidence Rises as Ability to Prove It Falls Behind** — SecurityWeek. Compliance survey, no actionable security news.
- **Microsoft Patches Exploited Entra ID Vulnerability** — SecurityWeek. Duplicate of Hacker News coverage above.
