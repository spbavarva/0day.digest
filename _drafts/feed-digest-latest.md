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
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`, `github`
- **Summary:** CVE-2026-3854 is a critical RCE in GitHub.com and GitHub Enterprise Server that exposed millions of repositories before being patched. No confirmed active exploitation, but GHES administrators must verify they are on the patched version.

### 2. LiteLLM CVE-2026-42208 SQL Injection Under Active Exploit Within 36 Hours
- **Source:** The Hacker News — https://thehackernews.com/2026/04/litellm-cve-2026-42208-sql-injection.html
- **Severity:** critical
- **Tags:** `sqli`, `cve`, `vulnerability`, `llm`
- **Summary:** CVE-2026-42208 (CVSS 9.3) is a pre-auth SQL injection in BerriAI's LiteLLM that was under active exploitation within 36 hours of disclosure. Attackers can modify the underlying database and may have exfiltrated stored AI provider API keys.

### 3. CISA Adds Actively Exploited ConnectWise ScreenConnect and Windows Flaws to KEV
- **Source:** The Hacker News — https://thehackernews.com/2026/04/cisa-adds-actively-exploited.html
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `rce`
- **Summary:** CISA added CVE-2024-1708 (ConnectWise ScreenConnect path traversal, CVSS 8.4) and a Windows flaw to the KEV catalog based on confirmed active exploitation. MSPs and enterprise IT teams using ScreenConnect should patch immediately.

### 4. BlueNoroff Uses AI Deepfakes and Fake Zoom Calls to Target Crypto Executives
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/bluenoroff-turns-victims-into-new-attack-lures
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Summary:** North Korean APT BlueNoroff is using AI-generated avatars and stolen victim video in fake Zoom calls to deliver malware to crypto executives. Compromised victims' identities are recycled into subsequent attacks, making this a self-amplifying attack chain.

### 5. Vidar Rises to Top of Infostealer Market After Lumma and Rhadamanthys Takedowns
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/vidar-top-chaotic-infostealer-market
- **Severity:** high
- **Tags:** `malware`
- **Summary:** Vidar has consolidated to the top of the MaaS infostealer market following last year's law enforcement disruptions of Lumma and Rhadamanthys. Vidar targets browser credentials, session tokens, and crypto wallets via affiliate-distributed campaigns.

### 6. VECT 2.0 Ransomware Permanently Destroys Large Files Due to Broken Encryption
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/broken-vect-20-ransomware-acts-as-a-data-wiper-for-large-files/
- **Severity:** medium
- **Tags:** `ransomware`, `malware`
- **Summary:** A nonce reuse bug in VECT 2.0 permanently destroys large files instead of encrypting them, making it effectively a wiper. Paying the ransom will not restore large files; responders should prioritize backup recovery from the start.

### 7. Rival Ransomware Groups 0APT and KryBit Leak Each Other's Infrastructure Data
- **Source:** Dark Reading — https://www.darkreading.com/threat-intelligence/feuding-ransomware-groups-leak-data
- **Severity:** medium
- **Tags:** `ransomware`, `malware`
- **Summary:** 0APT and KryBit attacked each other, leaking operational infrastructure data that gives defenders rare IOCs and insight into ransomware group operations. Reflects growing fragmentation in the criminal ecosystem post-law-enforcement disruptions.

### 8. AWS Offers OpenAI Models on Bedrock After Microsoft Drops Exclusivity
- **Source:** TechCrunch AI — https://techcrunch.com/2026/04/28/amazon-is-already-offering-new-openai-products-on-aws/
- **Severity:** informational
- **Tags:** `openai`, `aws`, `ai-launch`
- **Summary:** AWS announced OpenAI model offerings on Bedrock — including a new agent service — one day after OpenAI and Microsoft dropped their exclusive cloud partnership. OpenAI models are now available on both AWS and Google Cloud.

## Skippable

- **Microsoft Teams Free outage** — BleepingComputer. Backend change broke chat and calls for some users; service disruption, no security angle.
- **At his OpenAI trial, Musk relitigates an old friendship** — TechCrunch AI. Court coverage of Musk v. Altman; no technical or security content.
- **Elon Musk appeared more petty than prepared** — The Verge AI. Opinion piece on Musk trial testimony; duplicate trial coverage.
- **Quoting OpenAI Codex base_instructions** — Simon Willison. System prompt curiosity from GPT-5.5; no security angle.
- **Hackers are exploiting a critical LiteLLM pre-auth SQLi flaw** — BleepingComputer. Duplicate of CVE-2026-42208 coverage; The Hacker News version selected.
- **Elon Musk tells the jury that all he wants to do is save humanity** — The Verge AI. Duplicate Musk trial coverage.
- **NSA Chief During Snowden Affair Shares Regrets, Reflections 13 Years Later** — Dark Reading. Retrospective opinion piece; no current news value.
- **Taylor Swift is stepping up the legal war on AI copycats** — The Verge AI. Celebrity trademark filings; no security or technical angle.
