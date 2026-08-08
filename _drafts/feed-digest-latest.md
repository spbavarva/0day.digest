# Digest — 2026-08-08 PM

- Window: last 14h
- Raw items considered: 8
- Relevant: 6
- Skippable: 2

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Metabase Zero-Day Under Active Exploitation Grants Unauthenticated Admin Access — `2026-08-08-metabase-zero-day-unauthenticated-admin-access.md`
- [x] **[HIGH]** Hackers Trojanize TrueConf Installers With Backdoors — `2026-08-08-trueconf-trojanized-installers-backdoor.md`
- [x] **[HIGH]** Atlassian Rovo AI Assistant Tricked Into Leaking Jira and Confluence Data — `2026-08-08-atlassian-rovo-prompt-injection-data-leak.md`
- [x] **[HIGH]** New CSS-Based Attacks Break Webmail Isolation to Steal Passwords and Tokens — `2026-08-08-css-attacks-webmail-password-token-theft.md`
- [x] **[HIGH]** N-able Ships Second N-central Hotfix as Attackers Persist on Managed Systems — `2026-08-08-n-able-n-central-hotfix-2-active-exploitation.md`
- [x] **[HIGH]** CISA Adds Progress Kemp LoadMaster Command Injection Flaw to KEV Catalog — `2026-08-08-kemp-loadmaster-cve-2026-8037-cisa-kev.md`

## Relevant (details)

### 1. Metabase Zero-Day Under Active Exploitation Grants Unauthenticated Admin Access
- **Source:** The Hacker News — https://thehackernews.com/2026/08/metabase-zero-day-exploited-in-wild.html
- **Severity:** critical
- **Tags:** `zero-day`, `sqli`, `vulnerability`
- **Summary:** A maximum-severity, uncredentialed SQL injection flaw (CVSS 10.0, no CVE) in Metabase is being actively exploited in the wild to gain unauthenticated admin access. No patch guidance was confirmed in the source at time of writing.

### 2. Hackers Trojanize TrueConf Installers With Backdoors
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-breach-trueconf-to-trojanize-client-installers-with-backdoors/
- **Severity:** high
- **Tags:** `supply-chain`, `malware`
- **Summary:** The Head Mare hacktivist group is exploiting unpatched, internet-facing TrueConf servers to swap legitimate client installers for backdoored versions. Impact is limited to organizations running vulnerable, compromised TrueConf instances rather than a central distribution channel.

### 3. Atlassian Rovo AI Assistant Tricked Into Leaking Jira and Confluence Data
- **Source:** The Hacker News — https://thehackernews.com/2026/08/atlassian-rovo-can-be-tricked-into.html
- **Severity:** high
- **Tags:** `llm`, `prompt-injection`, `vulnerability`
- **Summary:** PromptArmor and Varonis independently found that hidden, attacker-controlled instructions can make Atlassian's Rovo assistant exfiltrate Jira/Confluence data the signed-in user can access. Only one of the two discovered routes has been confirmed closed by Atlassian.

### 4. New CSS-Based Attacks Break Webmail Isolation to Steal Passwords and Tokens
- **Source:** The Hacker News — https://thehackernews.com/2026/08/new-css-attacks-can-break-webmail.html
- **Severity:** high
- **Tags:** `xss`, `appsec`, `vulnerability`
- **Summary:** PortSwigger research demonstrates CSS-based attack chains against Outlook, Gmail, Fastmail, Proton Mail, Yahoo Mail, and AOL Mail that can steal passwords/tokens, hijack UI actions, and manipulate AI tools reading email. Provider-by-provider patch status is unconfirmed.

### 5. N-able Ships Second N-central Hotfix as Attackers Persist on Managed Systems
- **Source:** The Hacker News — https://thehackernews.com/2026/08/n-central-attackers-reach-managed.html
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`
- **Summary:** N-able issued a second hotfix for N-central after ongoing active exploitation of a previously disclosed RMM flaw, warning attackers are still reaching and persisting on managed systems. MSP-managed environments are the primary exposure path.

### 6. CISA Adds Progress Kemp LoadMaster Command Injection Flaw to KEV Catalog
- **Source:** The Hacker News — https://thehackernews.com/2026/08/progress-kemp-loadmaster-flaw-hits-cisa.html
- **Severity:** high
- **Tags:** `cve`, `rce`, `vulnerability`
- **Summary:** CISA added CVE-2026-8037 (CVSS 9.6), a command injection flaw in Progress Kemp LoadMaster, to its KEV catalog after 792 reported exploit attempts. Federal agencies face a mandated remediation deadline; all LoadMaster operators should patch.

## Skippable

- **Now we have a timeline of the OpenAI accidental attack against Hugging Face** — Simon Willison. Opinion/commentary post reacting to a Hacker News thread; speculative ("I think", "I suspect") with no confirmed technical details in the feed summary.
- **Critical One-Click Vulnerability in Atlassian's Rovo AI Exposed Enterprise Data** — SecurityWeek. Duplicate coverage of the Atlassian Rovo story; The Hacker News item has more technical detail (attribution to PromptArmor/Varonis, remediation status) and was used instead.
