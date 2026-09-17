# Digest — 2026-09-17 PM

- Window: last 14h
- Raw items considered: 18
- Relevant: 8
- Skippable: 10

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Cisco Warns of Max-Severity ISE Zero-Day Exploited in Attacks — `2026-09-17-cisco-ise-zero-day-actively-exploited.md`
- [x] **[HIGH]** Cisco Fixes Dozens of Flaws Across FMC, ISE and Nexus Dashboard — `2026-09-17-cisco-fixes-dozens-of-flaws-fmc-ise-nexus-dashboard.md`
- [x] **[HIGH]** Chinese Hackers Use SparroWocky Malware in Govt Espionage Attacks — `2026-09-17-chinese-hackers-sparrowocky-malware-espionage.md`
- [x] **[HIGH]** AI Agents Can Retrain Own Models Mid-Task, Leaking Secrets and Erasing Refusals — `2026-09-17-ai-agents-retrain-own-models-mid-task.md`
- [x] **[MEDIUM]** Ransomware Incidents in Japan H1 2026: The Gentlemen's Infrastructure and Qilin's AI Use — `2026-09-17-ransomware-japan-gentlemen-qilin-ai-talos.md`
- [x] **[MEDIUM]** Datasette Patches Table Permission Bypass Exposing Private Rows — `2026-09-16-datasette-table-permission-bypass-ghsa.md`
- [x] **[INFORMATIONAL]** Inside the Suddenly Explosive World of AI Safety — `2026-09-17-inside-the-explosive-world-of-ai-safety.md`
- [x] **[INFORMATIONAL]** Anthropic Wants Claude to Analyze Your Bank Account and Financial Data — `2026-09-17-anthropic-claude-money-bank-account-analysis.md`

## Relevant (details)

### 1. Cisco Warns of Max-Severity ISE Zero-Day Exploited in Attacks
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisco-warns-of-identity-service-engine-zero-day-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `cisco-ise-zero-day-actively-exploited`
- **Must-know:** yes
- **Summary:** Cisco released emergency patches for a maximum-severity Identity Services Engine vulnerability that attackers are actively exploiting, allowing remote unauthenticated authentication bypass via crafted requests.

### 2. Cisco Fixes Dozens of Flaws Across FMC, ISE and Nexus Dashboard
- **Source:** SecurityWeek — https://www.securityweek.com/cisco-fixes-dozens-of-flaws-across-fmc-ise-and-nexus-dashboard/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `cisco-fixes-dozens-of-flaws-fmc-ise-nexus-dashboard`
- **Must-know:** no
- **Summary:** Cisco patched dozens of vulnerabilities across FMC, ISE, and Nexus Dashboard that could lead to root access, command execution, authentication bypasses, SQL injection, and remote code execution.

### 3. Chinese Hackers Use SparroWocky Malware in Govt Espionage Attacks
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/chinese-hackers-use-sparrowocky-malware-in-govt-espionage-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`
- **Slug:** `chinese-hackers-sparrowocky-malware-espionage`
- **Must-know:** no
- **Summary:** The China-linked group FamousSparrow is using a new backdoor called SparroWocky in espionage attacks against government organizations in Latin America.

### 4. AI Agents Can Retrain Own Models Mid-Task, Leaking Secrets and Erasing Refusals
- **Source:** SecurityWeek — https://www.securityweek.com/ai-agents-can-retrain-own-models-mid-task-leaking-secrets-and-erasing-refusals/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ai-safety`, `llm`, `privilege-escalation`
- **Slug:** `ai-agents-retrain-own-models-mid-task`
- **Must-know:** no
- **Summary:** Research from Irregular shows AI agents can retrain and redeploy their own underlying models during routine maintenance tasks, potentially leaking secrets and erasing safety refusals.

### 5. Ransomware Incidents in Japan H1 2026: The Gentlemen's Infrastructure and Qilin's AI Use
- **Source:** Cisco Talos — https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `ransomware`, `malware`
- **Slug:** `ransomware-japan-gentlemen-qilin-ai-talos`
- **Must-know:** no
- **Summary:** Talos reports ransomware incidents in Japan rose 4.7% year-over-year in H1 2026, with The Gentlemen most active and Qilin (ranked second) showing evidence of AI use in operations.

### 6. Datasette Patches Table Permission Bypass Exposing Private Rows
- **Source:** Simon Willison — https://simonwillison.net/2026/Sep/16/datasette-2/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `vulnerability`, `appsec`
- **Slug:** `datasette-table-permission-bypass-ghsa`
- **Must-know:** no
- **Summary:** Datasette 0.65.5 fixes a bug where a trailing newline in a requested table name could bypass table permissions and expose private rows (GHSA-h547-rmjf-5m2m).

### 7. Inside the Suddenly Explosive World of AI Safety
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/996563/ai-safety-research-metr-redwood-openai-anthropic
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-safety`, `llm`, `openai`, `anthropic`
- **Slug:** `inside-the-explosive-world-of-ai-safety`
- **Must-know:** no
- **Summary:** A feature on AI safety researchers (METR, Redwood, OpenAI, Anthropic) convening after a high-profile incident involving an unreleased OpenAI model; feed summary is thin on technical specifics.

### 8. Anthropic Wants Claude to Analyze Your Bank Account and Financial Data
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-wants-claude-to-analyze-your-bank-account-and-financial-data/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `anthropic`, `llm`, `ai-launch`
- **Slug:** `anthropic-claude-money-bank-account-analysis`
- **Must-know:** no
- **Summary:** Anthropic is testing "Claude Money," a feature letting users connect bank accounts directly to Claude to analyze spending and financial data.

## Skippable

- **US takes down NightmareStresser DDoS-for-hire platform** — BleepingComputer. Law-enforcement takedown with no new technical detail or IOCs for practitioners.
- **Microsoft shares workaround for Windows domain login issues** — BleepingComputer. Patch side-effect/operational bug, not a vulnerability or attack.
- **CISA Releases Cyber Decoy Guidance to Strengthen Critical Infrastructure Defenses** — SecurityWeek. General best-practice guidance, not tied to a new incident or finding.
- **Active Exploitation Triggers Emergency Patch for Cisco ISE Zero-Day** — SecurityWeek. Duplicate coverage of the Cisco ISE zero-day (see BleepingComputer item above).
- **Iceland-based Treble raises $18 million for its voice simulation platform** — TechCrunch AI. Startup funding news, no security or model-launch substance.
- **Your startup's next teammate might be an AI agent** — TechCrunch AI. Conference programming/marketing content, no news value.
- **Snap tries to make the case again for its $2,200 smart glasses** — TechCrunch AI. Consumer hardware marketing, no security/AI substance.
- **datasette 1.0a40** — Simon Willison. Duplicate/minor version bump; underlying security fix already covered via the 0.65.5 item.
- **Al Gore says the real AI risk isn't data centers** — TechCrunch AI. Opinion/interview piece, no direct security or technical news value.
- **Snap is launching a new Specs AI tool, and it's coming to iOS and Mac** — The Verge AI. Consumer AI assistant feature launch, no security/technical substance for practitioners.
