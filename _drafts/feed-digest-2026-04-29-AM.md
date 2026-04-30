# Digest — 2026-04-29 AM

- Window: last 14h
- Raw items considered: 16
- Relevant: 8
- Skippable: 8

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Critical GitHub RCE CVE-2026-3854 Exposed Millions of Repositories — `2026-04-29-github-rce-cve-2026-3854-millions-repos.md`
- [x] **[CRITICAL]** LiteLLM CVE-2026-42208 SQL Injection Under Active Exploit Within 36 Hours — `2026-04-29-litellm-sqli-cve-2026-42208-active-exploitation.md`
- [x] **[HIGH]** CISA Adds Actively Exploited ConnectWise ScreenConnect and Windows Flaws to KEV — `2026-04-29-cisa-kev-connectwise-windows-active-exploit.md`
- [x] **[HIGH]** BlueNoroff Uses AI Deepfakes and Fake Zoom Calls to Target Crypto Executives — `2026-04-28-bluenoroff-ai-deepfake-zoom-crypto-attack.md`
- [x] **[HIGH]** Vidar Rises to Top of Infostealer Market After Lumma and Rhadamanthys Takedowns — `2026-04-28-vidar-infostealer-rises-lumma-gap.md`
- [x] **[MEDIUM]** VECT 2.0 Ransomware Permanently Destroys Large Files Due to Broken Encryption — `2026-04-28-vect-2-ransomware-broken-encryption-wiper.md`
- [x] **[MEDIUM]** Rival Ransomware Groups 0APT and KryBit Leak Each Other's Infrastructure Data — `2026-04-28-feuding-ransomware-groups-infra-leak.md`
- [x] **[INFORMATIONAL]** AWS Offers OpenAI Models on Bedrock After Microsoft Drops Exclusivity — `2026-04-28-aws-openai-models-microsoft-exclusivity.md`

## Relevant (details)

### 1. Critical GitHub RCE CVE-2026-3854 Exposed Millions of Repositories
- **Source:** SecurityWeek — https://www.securityweek.com/critical-github-vulnerability-exposed-millions-of-repositories/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`, `github`
- **Slug:** `2026-04-29-github-rce-cve-2026-3854-millions-repos`
- **Must-know:** no
- **Summary:** CVE-2026-3854 is a critical RCE in GitHub.com and GitHub Enterprise Server that exposed millions of repositories before being patched. No confirmed active exploitation, but GHES administrators must verify they are running the patched version.

### 2. LiteLLM CVE-2026-42208 SQL Injection Under Active Exploit Within 36 Hours
- **Source:** The Hacker News — https://thehackernews.com/2026/04/litellm-cve-2026-42208-sql-injection.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `sqli`, `cve`, `vulnerability`, `llm`
- **Slug:** `2026-04-29-litellm-sqli-cve-2026-42208-active-exploitation`
- **Must-know:** no
- **Summary:** CVE-2026-42208 (CVSS 9.3) is a pre-auth SQL injection in BerriAI's LiteLLM that was exploited within 36 hours of disclosure. Attackers can modify the underlying database, potentially exposing stored AI provider API keys.

### 3. CISA Adds Actively Exploited ConnectWise ScreenConnect and Windows Flaws to KEV
- **Source:** The Hacker News — https://thehackernews.com/2026/04/cisa-adds-actively-exploited.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `rce`
- **Slug:** `2026-04-29-cisa-kev-connectwise-windows-active-exploit`
- **Must-know:** no
- **Summary:** CISA added CVE-2024-1708 (ConnectWise ScreenConnect path traversal, CVSS 8.4) and a Windows vulnerability to the KEV catalog under evidence of active exploitation. Both require urgent patching given federal BOD 22-01 mandates and broad MSP deployment of ScreenConnect.

### 4. BlueNoroff Uses AI Deepfakes and Fake Zoom Calls to Target Crypto Executives
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/bluenoroff-turns-victims-into-new-attack-lures
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Slug:** `2026-04-28-bluenoroff-ai-deepfake-zoom-crypto-attack`
- **Must-know:** no
- **Summary:** BlueNoroff (North Korea) is using AI-generated avatars and stolen victim video in fake Zoom calls to deliver malware to crypto executives, then reusing victims' identities to lure their contacts. A notable escalation in AI-augmented nation-state social engineering.

### 5. Vidar Rises to Top of Infostealer Market After Lumma and Rhadamanthys Takedowns
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/vidar-top-chaotic-infostealer-market
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`
- **Slug:** `2026-04-28-vidar-infostealer-rises-lumma-gap`
- **Must-know:** no
- **Summary:** Vidar has consolidated to the top of the MaaS infostealer market following last year's law enforcement disruptions of Lumma and Rhadamanthys. Targets browser credentials, session tokens, and crypto wallets; expect elevated deployment volumes.

### 6. VECT 2.0 Ransomware Permanently Destroys Large Files Due to Broken Encryption
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/broken-vect-20-ransomware-acts-as-a-data-wiper-for-large-files/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ransomware`, `malware`
- **Slug:** `2026-04-28-vect-2-ransomware-broken-encryption-wiper`
- **Must-know:** no
- **Summary:** A nonce reuse bug in VECT 2.0 permanently destroys large files instead of encrypting them. Incident responders should treat any VECT 2.0 infection as a destructive attack and begin backup recovery immediately regardless of ransom status.

### 7. Rival Ransomware Groups 0APT and KryBit Leak Each Other's Infrastructure Data
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/feuding-ransomware-groups-leak-data
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ransomware`, `malware`
- **Slug:** `2026-04-28-feuding-ransomware-groups-infra-leak`
- **Must-know:** no
- **Summary:** 0APT and KryBit attacked each other's infrastructure, inadvertently leaking operational data that gives defenders rare insight into ransomware group operations. Threat intel teams should mine the leaked data for IOCs and C2 infrastructure.

### 8. AWS Offers OpenAI Models on Bedrock After Microsoft Drops Exclusivity
- **Source:** TechCrunch AI — https://techcrunch.com/2026/04/28/amazon-is-already-offering-new-openai-products-on-aws/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `openai`, `aws`, `ai-launch`
- **Slug:** `2026-04-28-aws-openai-models-microsoft-exclusivity`
- **Must-know:** no
- **Summary:** AWS announced OpenAI model offerings including a new agent service, one day after OpenAI and Microsoft restructured their partnership to drop Microsoft's exclusive cloud rights. OpenAI models are now available on both AWS Bedrock and Google Vertex AI.

## Skippable

- **Microsoft Teams Free outage** — BleepingComputer. Backend change broke chat and calls for some users; service disruption, no security angle.
- **At his OpenAI trial, Musk relitigates an old friendship** — TechCrunch AI. Court coverage of Musk v. Altman, no technical or security content.
- **Elon Musk appeared more petty than prepared** — The Verge AI. Opinion piece on Musk trial testimony; duplicate trial coverage, no news value.
- **Quoting OpenAI Codex base_instructions** — Simon Willison. Amusing system prompt curiosity ("no goblins") from GPT-5.5; no security angle.
- **Hackers are exploiting a critical LiteLLM pre-auth SQLi flaw** — BleepingComputer. Duplicate coverage of CVE-2026-42208; The Hacker News item (with 36-hour timeline) selected instead.
- **Elon Musk tells the jury that all he wants to do is save humanity** — The Verge AI. Duplicate Musk trial coverage; no security or technical content.
- **NSA Chief During Snowden Affair Shares Regrets, Reflections 13 Years Later** — Dark Reading. Retrospective opinion piece; no current news value.
- **Taylor Swift is stepping up the legal war on AI copycats** — The Verge AI. Celebrity trademark filings; no security or technical angle.
