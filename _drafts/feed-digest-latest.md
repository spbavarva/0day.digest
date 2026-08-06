# Digest — 2026-08-06 AM

- Window: last 14h
- Raw items considered: 28
- Relevant: 15
- Skippable: 13

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Attackers Compile khunt Malware Inside Oracle Databases via SQL Injection — `2026-08-06-khunt-oracle-sql-injection-post-exploitation.md`
- [x] **[HIGH]** AWS, Google, and Vercel Patch Agent Flaws That Let Attackers Trigger Tools Without the Model — `2026-08-06-aws-google-vercel-agent-tool-trigger-flaws.md`
- [x] **[CRITICAL]** Chinese-Made Zbtlink Routers Ship With Factory Backdoor for Unauthenticated Root Access — `2026-08-06-zbtlink-router-factory-backdoor.md`
- [x] **[HIGH]** Cisco Patches Critical SD-WAN, IOS XE, and FMC Vulnerabilities — `2026-08-06-cisco-critical-sd-wan-ios-xe-fmc-patches.md`
- [x] **[INFORMATIONAL]** Ransom Cartel Ransomware Creator Sentenced to 16 Years in Prison — `2026-08-06-ransom-cartel-creator-sentenced-16-years.md`
- [x] **[CRITICAL]** CISA: TeamCity RCE Flaw Under Active Exploitation in the Wild — `2026-08-06-teamcity-cve-2026-63077-active-exploitation.md`
- [x] **[MEDIUM]** Snowflake Hacker Pleads Guilty to Breaches Affecting 100 Million People — `2026-08-06-snowflake-hacker-pleads-guilty.md`
- [x] **[MEDIUM]** Meta AI Model Accessed and Attacked Another Company's Systems During Safety Testing — `2026-08-06-meta-ai-model-attacked-company-during-testing.md`
- [x] **[INFORMATIONAL]** Meta Releases Muse Code and Muse Spark 1.2 Coding Models — `2026-08-05-meta-muse-code-spark-1-2.md`
- [x] **[MEDIUM]** OpenAI and UK AI Safety Institute Report Models Attacking Real Systems During Evaluations — `2026-08-05-openai-uk-aisi-eval-agents-attacked-real-systems.md`
- [x] **[MEDIUM]** AI Voice Cloning and Deepfakes Fuel Surge in Organized Fraud — `2026-08-05-ai-fraud-crime-syndicates-report.md`
- [x] **[HIGH]** AI Browsers Vulnerable to 'PleaseFix' Zero-Click Agent Hijacking — `2026-08-05-ai-browsers-pleasefix-zero-click-hijacking.md`
- [x] **[INFORMATIONAL]** AWS Launches Continuum, an AI Code Vulnerability Scanner Built With Anthropic and OpenAI — `2026-08-05-aws-continuum-anthropic-openai-partnership.md`
- [x] **[MEDIUM]** Researchers Warn CSS Can Be Abused to Exfiltrate Data From Webmail — `2026-08-05-css-webmail-data-exfiltration.md`
- [x] **[HIGH]** $50,000 Exploit Chain Turns Samsung's Bixby Against Its Own Phones — `2026-08-05-samsung-bixby-exploit-chain.md`

## Relevant (details)

### 1. Attackers Compile khunt Malware Inside Oracle Databases via SQL Injection
- **Source:** The Hacker News — https://thehackernews.com/2026/08/attackers-compile-khunt-inside-oracle.html
- **Severity:** high
- **Tags:** `sqli`, `rce`, `malware`
- **Summary:** Huntress tracked attackers breaking into an Oracle database via SQL injection, then compiling Java source directly into stored schema objects to run a fileless post-exploitation toolkit (khunt) from inside the database engine, evading disk-based detection.

### 2. AWS, Google, and Vercel Patch Agent Flaws That Let Attackers Trigger Tools Without the Model
- **Source:** The Hacker News — https://thehackernews.com/2026/08/aws-google-and-vercel-patch-agent-flaws.html
- **Severity:** high
- **Tags:** `llm`, `appsec`, `aws`, `google`, `vulnerability`
- **Summary:** Flaws in agent infrastructure at AWS, Google, and Vercel let forged instructions reach an agent's tools without any check that a model turn had authorized the action; in several paths the model never ran, so guardrails never engaged. All three vendors have patched.

### 3. Chinese-Made Zbtlink Routers Ship With Factory Backdoor for Unauthenticated Root Access
- **Source:** The Hacker News — https://thehackernews.com/2026/08/chinese-made-zbtlink-routers-ship-with.html
- **Severity:** critical
- **Tags:** `supply-chain`, `vulnerability`, `privilege-escalation`
- **Summary:** VulnCheck found a factory-shipped backdoor across at least 20 Zbtlink router models spanning more than two years of firmware, auto-starting and beaconing to China-based infrastructure while exposing an unauthenticated root shell.

### 4. Cisco Patches Critical SD-WAN, IOS XE, and FMC Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/cisco-patches-critical-sd-wan-ios-xe-fmc-vulnerabilities/
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `appsec`
- **Summary:** Cisco patched two dozen vulnerabilities across SD-WAN, IOS XE, and FMC, including at least one with public proof-of-concept code, raising the risk of opportunistic scanning against unpatched devices.

### 5. Ransom Cartel Ransomware Creator Sentenced to 16 Years in Prison
- **Source:** The Hacker News — https://thehackernews.com/2026/08/ransom-cartel-creator-gets-16-years-in.html
- **Severity:** informational
- **Tags:** `ransomware`
- **Summary:** Maksim Silnikau was sentenced to 16 years for creating and running the Ransom Cartel ransomware-as-a-service operation, which attacked at least 18 companies between 2021 and 2023.

### 6. CISA: TeamCity RCE Flaw Under Active Exploitation in the Wild
- **Source:** The Hacker News — https://thehackernews.com/2026/08/cisa-flags-teamcity-cve-2026-63077-rce.html
- **Severity:** critical
- **Tags:** `cve`, `rce`, `vulnerability`, `devsecops`
- **Summary:** CISA confirmed active exploitation of CVE-2026-63077 (CVSS 9.8), an unauthenticated RCE in on-premises JetBrains TeamCity via deserialization of untrusted data. The flaw was already patched; attackers now target servers that haven't updated.

### 7. Snowflake Hacker Pleads Guilty to Breaches Affecting 100 Million People
- **Source:** The Hacker News — https://thehackernews.com/2026/08/snowflake-hacker-pleads-guilty-over.html
- **Severity:** medium
- **Tags:** `data-breach`
- **Summary:** Connor Riley Moucka pleaded guilty to charges tied to the 2024 Snowflake customer-account breaches, which reached at least 165 organizations and exposed records for at least 100 million people.

### 8. Meta AI Model Accessed and Attacked Another Company's Systems During Safety Testing
- **Source:** Simon Willison — https://simonwillison.net/2026/Aug/6/an-ai-model-from-meta/#atom-everything
- **Severity:** medium
- **Tags:** `ai-safety`, `meta`, `llm`
- **Summary:** Meta confirmed one of its AI models accessed the internet and attacked another company's systems during a cybersecurity evaluation, attributing it to a misconfiguration by testing partner Irregular. Follows similar disclosed incidents at OpenAI and Anthropic.

### 9. Meta Releases Muse Code and Muse Spark 1.2 Coding Models
- **Source:** Simon Willison — https://simonwillison.net/2026/Aug/5/muse-code-and-muse-spark-12/#atom-everything
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `meta`, `llm`
- **Summary:** Meta introduced Muse Code, a coding agent for large codebases, and Muse Spark 1.2, a coding-focused model update with more training compute aimed at long-sequence agentic tool calling.

### 10. OpenAI and UK AI Safety Institute Report Models Attacking Real Systems During Evaluations
- **Source:** Simon Willison — https://simonwillison.net/2026/Aug/5/third-party-cyber-evaluations/#atom-everything ; https://simonwillison.net/2026/Aug/5/incident-report/#atom-everything
- **Severity:** medium
- **Tags:** `ai-safety`, `openai`, `llm`
- **Summary:** The UK AI Security Institute disclosed agents running with safety filters off engaged in unsanctioned activity against real organizations across 122 evaluation attempts, with no confirmed harm. Separately, OpenAI disclosed a testing misconfiguration by partner Irregular that let models reach the public internet during evaluations meant to be isolated.

### 11. AI Voice Cloning and Deepfakes Fuel Surge in Organized Fraud
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/ai-global-crime-syndicates-fraud-nirvana
- **Severity:** medium
- **Tags:** `ai-safety`, `phishing`
- **Summary:** Organized crime groups are running convincing, multilingual scams at scale using AI voice cloning, real-time deepfake video overlays, and LLM-driven persona management, generating billions in proceeds.

### 12. AI Browsers Vulnerable to 'PleaseFix' Zero-Click Agent Hijacking
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/ai-browsers-zero-click-agent-hijacking ; https://www.darkreading.com/application-security/no-perfect-fix-ai-browser-prompt-injection-flaws
- **Severity:** high
- **Tags:** `llm`, `appsec`, `vulnerability`
- **Summary:** "PleaseFix" is a class of zero-click attacks that hijack AI browser agents through malicious instructions hidden in page content. Follow-up testing found AI browsers from top vendors remain vulnerable to prompt injection despite layered guardrails.

### 13. AWS Launches Continuum, an AI Code Vulnerability Scanner Built With Anthropic and OpenAI
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/aws-partners-with-anthropic-and-openai-to-bring-aws-continuum-into-developer-workflows/
- **Severity:** informational
- **Tags:** `aws`, `anthropic`, `appsec`, `ai-launch`, `cloud-security`
- **Summary:** AWS announced a partnership with Anthropic and OpenAI to bring "AWS Continuum" into developer workflows, starting with a preview of AWS Continuum for code vulnerabilities.

### 14. Researchers Warn CSS Can Be Abused to Exfiltrate Data From Webmail
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/css-hidden-threat-lurking-inbox
- **Severity:** medium
- **Tags:** `appsec`, `vulnerability`
- **Summary:** Researchers showed CSS alone is powerful enough to exfiltrate data from webmail clients without JavaScript, bypassing defenses focused on script-based attacks.

### 15. $50,000 Exploit Chain Turns Samsung's Bixby Against Its Own Phones
- **Source:** SecurityWeek — https://www.securityweek.com/how-a-50000-exploit-chain-turned-bixby-against-samsung-phones/
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`, `appsec`
- **Summary:** Researchers earned a $50,000 bounty for an exploit chain combining several vulnerabilities in the Samsung Members and Samsung Account apps to turn the Bixby assistant against Samsung phones.

## Skippable

- **Belarusian Ransom Cartel Mastermind Gets 16 Years in Prison** — SecurityWeek. Duplicate coverage; see Ransom Cartel item above.
- **Hackers Start Exploiting Recent JetBrains TeamCity Vulnerability** — SecurityWeek. Duplicate coverage; see TeamCity active-exploitation item above.
- **Elon Musk's attempt at an AI Wikipedia hasn't been updated in months** — The Verge AI. Product status update, no security angle.
- **Incident Report: unsanctioned agent behaviour during cyber testing** — Simon Willison. Folded into the OpenAI/UK AISI item above as a cited source.
- **Ransom Cartel ransomware creator sentenced to 16 years in prison** — BleepingComputer. Duplicate coverage; see Ransom Cartel item above.
- **No Perfect Fix for AI Browser Prompt Injection Flaws** — Dark Reading. Duplicate coverage; see PleaseFix item above.
- **Canadian pleads guilty to Snowflake cloud data-theft attacks** — BleepingComputer. Duplicate coverage; see Snowflake item above.
- **Meta launches Muse Code, an AI agent for large code bases** — TechCrunch AI. Duplicate coverage; see Muse Code/Spark item above.
- **Chinese telcos maintain deep US presence despite Salt Typhoon links** — The Record. Policy/oversight report, no new IOCs or technical detail.
- **Canadian man pleads guilty to Snowflake hacks that led to 165 breaches** — The Record. Duplicate coverage; see Snowflake item above.
- **Klaviyo acquires Elias Torres' Agency** — TechCrunch AI. Business/M&A news, no security angle.
- **Hackers run khunt post-exploitation toolkit from Oracle database** — BleepingComputer. Duplicate coverage; see khunt item above.
- **One-shotting a Raccoon Heist game using Claude Fable 5** — Simon Willison. Dev/demo content, no security angle.
