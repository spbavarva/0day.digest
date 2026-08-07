# Digest — 2026-08-07 AM

- Window: last 14h
- Raw items considered: 20
- Relevant: 10
- Skippable: 10

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** 3.8 Million Impacted by Unlimited Technology Systems Data Breach — `2026-08-07-unlimited-technology-systems-data-breach.md`
- [x] **[HIGH]** Critical Vulnerabilities Patched With Chrome 151 Update — `2026-08-07-chrome-151-critical-vulnerabilities-patched.md`
- [x] **[HIGH]** TeamPCP Linked To Redis Attacks Dating Back To 2020 And Later Supply Chain Campaign — `2026-08-07-teampcp-redis-attacks-supply-chain-campaign.md`
- [x] **[MEDIUM]** ClickFix Attack Pushes macOS Infostealer For Crypto Theft — `2026-08-06-clickfix-macos-infostealer-crypto-theft.md`
- [x] **[CRITICAL]** ChainDrop: Inside a Self-Propagating npm Worm — `2026-08-06-chaindrop-npm-worm-supply-chain.md`
- [x] **[INFORMATIONAL]** Automate Certificates With ACME Support in AWS Certificate Manager — `2026-08-06-aws-acm-acme-certificate-automation.md`
- [x] **[MEDIUM]** CSS: The Bomb Inside Your Inbox — `2026-08-06-css-bomb-inside-your-inbox.md`
- [x] **[HIGH]** Researcher Claims Control of ChatGPT Secure Sandbox — `2026-08-06-researcher-claims-control-chatgpt-sandbox.md`
- [x] **[INFORMATIONAL]** Route Amazon Bedrock Guardrails Interventions to Amazon Security Lake — `2026-08-06-bedrock-guardrails-security-lake-integration.md`
- [x] **[MEDIUM]** Datasette SQL Injection Fix (1.0a38) — `2026-08-06-datasette-sql-injection-fix.md`

## Relevant (details)

### 1. 3.8 Million Impacted by Unlimited Technology Systems Data Breach
- **Source:** SecurityWeek — https://www.securityweek.com/3-8-million-impacted-by-unlimited-technology-systems-data-breach/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `unlimited-technology-systems-data-breach`
- **Must-know:** no
- **Summary:** Hackers stole personal, medical, and health insurance information belonging to roughly 3.8 million people from Unlimited Technology Systems' data center. No attack vector or attribution has been disclosed yet.

### 2. Critical Vulnerabilities Patched With Chrome 151 Update
- **Source:** SecurityWeek — https://www.securityweek.com/critical-vulnerabilities-patched-with-chrome-151-update/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `appsec`, `google`
- **Slug:** `chrome-151-critical-vulnerabilities-patched`
- **Must-know:** no
- **Summary:** Chrome 151 fixes more than two dozen memory-safety bugs, including several critical use-after-free flaws. No indication the flaws were under active exploitation prior to the patch.

### 3. TeamPCP Linked To Redis Attacks Dating Back To 2020 And Later Supply Chain Campaign
- **Source:** The Hacker News — https://thehackernews.com/2026/08/teampcp-linked-to-redis-attacks-dating.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `malware`
- **Slug:** `teampcp-redis-attacks-supply-chain-campaign`
- **Must-know:** no
- **Summary:** Analysis attributes years of Redis-targeting infrastructure attacks dating to 2020 to the same threat actor, TeamPCP, that later pivoted into a software supply chain campaign. Attribution rests on overlapping domains, deployment paths, and infrastructure.

### 4. ClickFix Attack Pushes macOS Infostealer For Crypto Theft
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/clickfix-attack-pushes-macos-infostealer-for-crypto-theft-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Slug:** `clickfix-macos-infostealer-crypto-theft`
- **Must-know:** no
- **Summary:** A Go-based infostealer delivered via ClickFix-style social engineering targets macOS users, harvesting crypto wallets, browser-stored passwords, Keychain data, and cached credentials.

### 5. ChainDrop: Inside a Self-Propagating npm Worm
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`
- **Slug:** `chaindrop-npm-worm-supply-chain`
- **Must-know:** yes
- **Summary:** ChainDrop is a self-propagating npm supply chain worm that extracts GitHub Actions runner secrets and uses Ethereum smart contracts for C2 routing, a technique that complicates takedown efforts.

### 6. Automate Certificates With ACME Support in AWS Certificate Manager
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/automate-certificates-with-acme-support-in-aws-certificate-manager/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `aws`, `cloud-security`
- **Slug:** `aws-acm-acme-certificate-automation`
- **Must-know:** no
- **Summary:** AWS Certificate Manager now supports the ACME protocol for automated cert issuance and renewal, timed to a CA/Browser Forum mandate shrinking max public cert validity to 100 days by 2027 and 47 days by 2029.

### 7. CSS: The Bomb Inside Your Inbox
- **Source:** PortSwigger Research — https://portswigger.net/research/css-the-bomb-inside-your-inbox
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `appsec`, `vulnerability`
- **Slug:** `css-bomb-inside-your-inbox`
- **Must-know:** no
- **Summary:** PortSwigger research shows CSS sanitizers used by webmail clients to make untrusted CSS "safe" inside a trusted UI can be bypassed, a class of technique relevant to anyone sanitizing untrusted HTML/CSS for email rendering.

### 8. Researcher Claims Control of ChatGPT Secure Sandbox
- **Source:** Dark Reading — https://www.darkreading.com/cloud-security/researcher-claims-control-chatgpt-secure-sandbox
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `openai`
- **Slug:** `researcher-claims-control-chatgpt-sandbox`
- **Must-know:** no
- **Summary:** A researcher presented a proof-of-concept attack chain at Black Hat USA 2026 showing C2-style influence over ChatGPT's isolated code execution sandbox. No patch status or technique detail was given in the available summary.

### 9. Route Amazon Bedrock Guardrails Interventions to Amazon Security Lake
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/route-amazon-bedrock-guardrails-interventions-to-amazon-security-lake/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `aws`, `cloud-security`, `ai-safety`
- **Slug:** `bedrock-guardrails-security-lake-integration`
- **Must-know:** no
- **Summary:** AWS can now route Amazon Bedrock Guardrails intervention events (blocked prompt injections, redactions) into Amazon Security Lake, letting teams query AI guardrail signals alongside their broader security telemetry.

### 10. Datasette SQL Injection Fix (1.0a38)
- **Source:** Simon Willison — https://simonwillison.net/2026/Aug/6/datasette/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `sqli`, `vulnerability`
- **Slug:** `datasette-sql-injection-fix`
- **Must-know:** no
- **Summary:** Datasette 1.0a38 (backported to 0.65.3) fixes a SQL injection bug affecting instances serving mixed public/private tables, where a user with access to any public table could reach private tables via SQL injection even with execute-sql disabled.

## Skippable

- **Runtime instances: persistent compute for production AI agents on Amazon Bedrock AgentCore** — AWS News Blog. Product/infra feature launch with no explicit security angle in the summary.
- **OpenAI rolls out a major ChatGPT upgrade, even if you don't pay for it** — BleepingComputer. Generic product update, no security angle.
- **OpenAI's new AI smart speaker will reportedly sell for between $300 and $400** — TechCrunch AI. Hardware rumor, no security relevance.
- **The Coordination Gap: How Attackers Are Outpacing Law Enforcement** — Dark Reading. Opinion/analysis piece without new technical findings.
- **Jony Ive's first OpenAI gadget is reportedly a hockey puck-sized smart speaker** — The Verge AI. Duplicate hardware-rumor coverage of the OpenAI speaker story above, no security angle.
- **Beyond Cyber: How CTI Teams Are Solving Converged Threat Use Cases** — Flashpoint. Vendor thought-leadership piece, no concrete news event.
- **Hedge fund cyberattacks tied to BlackFile-linked UNC6671 extortion group** — BleepingComputer. Victim disclosure without TTPs or IOCs in the available summary.
- **From Bobmojis to Bobbleheads: How the Democratic Party Built a Security-First Culture** — Dark Reading. Culture/human-interest piece, not a technical security event.
- **datasette 0.65.3** — Simon Willison. Backport of the same SQL injection fix already covered in the 1.0a38 entry above.
- **Swiss government SharePoint breach compromised 200 accounts** — BleepingComputer. Regional government incident, small scope (~200 accounts), thin technical detail.
