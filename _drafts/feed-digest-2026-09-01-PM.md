# Digest — 2026-09-01 PM

- Window: last 14h
- Raw items considered: 19
- Relevant: 10
- Skippable: 9

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[MEDIUM]** ClickFix Overtakes Other Techniques as Top Initial Access Method — `2026-09-01-clickfix-most-common-initial-access-technique.md`
- [x] **[CRITICAL]** Critical JFrog Artifactory Vulnerability Exploited in the Wild — `2026-09-01-jfrog-artifactory-critical-vuln-exploited.md`
- [x] **[CRITICAL]** 9.5 Million Impacted by Aesto Health Data Breach — `2026-09-01-aesto-health-data-breach-9-5-million.md`
- [x] **[HIGH]** Attackers Steal METR API Key, Rack Up $600,000 in AI Credits — `2026-09-01-metr-api-key-theft-ai-credits.md`
- [x] **[HIGH]** WatchGuard Patches Critical Fireware OS Vulnerabilities — `2026-09-01-watchguard-critical-vulnerabilities.md`
- [x] **[HIGH]** Russia-Aligned UAC-0099 Uses Prompt Injection to Disrupt AI-Assisted Malware Analysis — `2026-09-01-uac-0099-guardbreaker-prompt-injection.md`
- [x] **[CRITICAL]** Patched PaperCut Zero-Days Now Used in Data Theft Attacks — `2026-09-01-papercut-zero-days-data-theft.md`
- [x] **[CRITICAL]** Attackers Exploit Critical Langflow and Ruby on Rails Flaws for Credential Probing and C2 — `2026-09-01-langflow-rails-critical-flaws-exploited.md`
- [x] **[MEDIUM]** Mirage Kitten Deploys New NodeRabbit and PollCat Malware Against Aviation and FinTech Targets — `2026-09-01-mirage-kitten-noderabbit-pollcat-malware.md`
- [x] **[MEDIUM]** Apple Presents Evidence Against Ex-Employee Accused of Stealing Data for OpenAI — `2026-09-01-apple-openai-trade-secret-theft-case.md`

## Relevant (details)

### 1. ClickFix Overtakes Other Techniques as Top Initial Access Method
- **Source:** The Hacker News — https://thehackernews.com/2026/09/threat-actors-dont-want-better-attacks.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `malware`
- **Slug:** `clickfix-most-common-initial-access-technique`
- **Must-know:** no
- **Summary:** Microsoft's threat intelligence team found ClickFix — a social-engineering technique that tricks victims into pasting a clipboard-injected command into their own terminal — was the most common initial access method observed last year. The finding highlights a broader shift toward repeatable, low-cost social-engineering techniques over novel exploits.

### 2. Critical JFrog Artifactory Vulnerability Exploited in the Wild
- **Source:** SecurityWeek — https://www.securityweek.com/critical-jfrog-artifactory-vulnerability-reportedly-exploited-in-the-wild/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `devsecops`, `appsec`
- **Slug:** `jfrog-artifactory-critical-vuln-exploited`
- **Must-know:** no
- **Summary:** An authentication bypass vulnerability in JFrog Artifactory (CVE-2026-82329) is being actively exploited just days after public disclosure. Organizations running Artifactory should patch immediately.

### 3. 9.5 Million Impacted by Aesto Health Data Breach
- **Source:** SecurityWeek — https://www.securityweek.com/9-5-million-impacted-by-aesto-health-data-breach/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `data-breach`, `cloud-security`, `aws`
- **Slug:** `aesto-health-data-breach-9-5-million`
- **Must-know:** yes
- **Summary:** Healthcare technology company Aesto Health disclosed that hackers stole personal and health information belonging to 9.5 million individuals from its AWS infrastructure. No detail on the initial access vector was provided.

### 4. Attackers Steal METR API Key, Rack Up $600,000 in AI Credits
- **Source:** The Hacker News — https://thehackernews.com/2026/09/attackers-steal-metr-api-key-and.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `ai-safety`
- **Slug:** `metr-api-key-theft-ai-credits`
- **Must-know:** no
- **Summary:** AI safety nonprofit METR disclosed two security incidents in which external actors used a stolen API key to consume roughly $600,000 in AI compute credits. METR said no sensitive information is believed to have been exposed.

### 5. WatchGuard Patches Critical Fireware OS Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/watchguard-patches-critical-vulnerabilities/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `watchguard-critical-vulnerabilities`
- **Must-know:** no
- **Summary:** WatchGuard patched three critical vulnerabilities in the Fireware OS iked process that could let an unauthenticated attacker execute arbitrary code remotely. No active exploitation was reported at time of disclosure.

### 6. Russia-Aligned UAC-0099 Uses Prompt Injection to Disrupt AI-Assisted Malware Analysis
- **Source:** The Hacker News — https://thehackernews.com/2026/09/russia-aligned-uac-0099-plants-nuclear.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `malware`
- **Slug:** `uac-0099-guardbreaker-prompt-injection`
- **Must-know:** no
- **Summary:** ESET disclosed a technique called GuardBreaker used by Russia-aligned actor UAC-0099 against a target in Ukraine, embedding a prompt in malware designed to trip an LLM's safety mechanisms and block AI-assisted analysis of the sample.

### 7. Patched PaperCut Zero-Days Now Used in Data Theft Attacks
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/recently-patched-papercut-zero-days-used-in-data-theft-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `vulnerability`, `data-breach`
- **Slug:** `papercut-zero-days-data-theft`
- **Must-know:** yes
- **Summary:** Two PaperCut NG/MF vulnerabilities (CVE-2026-82078, CVE-2026-81578), patched last week after being exploited as zero-days, are now being abused in data theft attacks. CISA has added both to its KEV catalog.

### 8. Attackers Exploit Critical Langflow and Ruby on Rails Flaws for Credential Probing and C2
- **Source:** The Hacker News — https://thehackernews.com/2026/09/attackers-exploit-critical-langflow-and.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `llm`, `rce`, `cve`, `vulnerability`
- **Slug:** `langflow-rails-critical-flaws-exploited`
- **Must-know:** no
- **Summary:** VulnCheck reports active exploitation of CVE-2026-0768 (CVSS 9.8, unauthenticated RCE in the Langflow AI workflow tool) and CVE-2026-66066 (Ruby on Rails), used for credential probing and C2 setup.

### 9. Mirage Kitten Deploys New NodeRabbit and PollCat Malware Against Aviation and FinTech Targets
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `mirage-kitten-noderabbit-pollcat-malware`
- **Must-know:** no
- **Summary:** Kaspersky identified new Mirage Kitten activity against aviation and fintech organizations in the Middle East and Africa, using two previously undocumented malware families: NodeRabbit (Node.js) and PollCat (JavaScript).

### 10. Apple Presents Evidence Against Ex-Employee Accused of Stealing Data for OpenAI
- **Source:** TechCrunch AI — https://techcrunch.com/2026/08/31/apple-shares-shocking-evidence-against-former-employee-accused-of-stealing-company-data-for-openai/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `data-breach`, `openai`
- **Slug:** `apple-openai-trade-secret-theft-case`
- **Must-know:** no
- **Summary:** Apple says it has evidence a former employee destroyed proof of data theft after learning he was under investigation, alleging the data was intended for use at OpenAI. Scope of the exposed data was not detailed.

## Skippable

- **[Virtual Event] What Every Enterprise Should Know About Securing Cloud Assets in the Age of AI** — Dark Reading. Event listing, not news.
- **[Virtual Event] Building a Secure AI Strategy for the Enterprise** — Dark Reading. Event listing, not news.
- **Hackers Start Exploiting Critical Langflow Vulnerability** — SecurityWeek. Duplicate coverage of the Langflow CVE-2026-0768 story, covered in more detail by The Hacker News item.
- **Five Venezuelans Plead Guilty in US Court to ATM Jackpotting** — SecurityWeek. Legal outcome of an old case, no new TTPs or IOCs.
- **Ransomware Gang Claims Nutex Health Data Breach** — SecurityWeek. Unconfirmed ransomware-gang claim, no victim count or technical detail provided.
- **Five Venezuelans plead guilty to ATM jackpotting attacks in US** — BleepingComputer. Duplicate of the SecurityWeek item on the same guilty plea.
- **PaperCut Exploitation Escalates to Active Intrusions** — SecurityWeek. Duplicate coverage of the PaperCut zero-day story, covered in more detail by the BleepingComputer item.
- **Introducing wrapture** — Simon Willison. General Python tracing/testing library, no AI or security angle.
- **Quoting Andrew Digby** — Simon Willison. Kakapo conservation news, unrelated to AI or security.
