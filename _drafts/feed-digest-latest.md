# Digest — 2026-07-11 PM

- Window: last 14h
- Raw items considered: 5
- Relevant: 3
- Skippable: 2

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Critical Zimbra Flaw Could Let Crafted Emails Run Malicious Code in User Sessions — `2026-07-11-critical-zimbra-xss-flaw.md`
- [x] **[HIGH]** 'Ghostcommit' Hides Prompt Injection in Images to Fool AI Agents, Steal Secrets — `2026-07-11-ghostcommit-prompt-injection-ai-agents.md`
- [x] **[MEDIUM]** Ghost Accounts Abuse GitHub API in Mass Recon Campaign — `2026-07-11-ghost-accounts-github-api-recon.md`

## Relevant (details)

### 1. Critical Zimbra Flaw Could Let Crafted Emails Run Malicious Code in User Sessions
- **Source:** The Hacker News — https://thehackernews.com/2026/07/critical-zimbra-flaw-could-let-crafted_0483473395.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `xss`, `vulnerability`, `appsec`
- **Slug:** `critical-zimbra-xss-flaw`
- **Must-know:** no
- **Summary:** Zimbra is urging customers to patch a critical stored XSS vulnerability in its Classic Web Client that lets crafted emails execute malicious scripts in a user's session, potentially resulting in code execution. No CVE has been assigned yet and no active exploitation was reported.

### 2. 'Ghostcommit' Hides Prompt Injection in Images to Fool AI Agents, Steal Secrets
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/ghostcommit-hides-prompt-injection-in-images-to-fool-ai-agents-steal-secrets/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `supply-chain`, `github`
- **Slug:** `ghostcommit-prompt-injection-ai-agents`
- **Must-know:** no
- **Summary:** Researchers demonstrated "Ghostcommit," which hides prompt injection payloads in PNG images to bypass AI code reviewers CodeRabbit and Bugbot (which don't open images) and trick a coding agent into leaking a repo's .env secrets. It highlights a gap in AI-assisted code review pipelines around unvetted image content.

### 3. Ghost Accounts Abuse GitHub API in Mass Recon Campaign
- **Source:** SecurityWeek — https://www.securityweek.com/ghost-accounts-abuse-github-api-in-mass-recon-campaign/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `github`, `appsec`
- **Slug:** `ghost-accounts-github-api-recon`
- **Must-know:** no
- **Summary:** Multiple campaigns are using disposable ghost GitHub accounts to enumerate organizations at scale via the GitHub API, mapping repositories and members — likely reconnaissance ahead of follow-on attacks. Reporting is thin on further technical detail.

## Skippable

- **Australia warns of global campaign targeting vulnerable CMS platforms** — BleepingComputer. Government advisory without new IOCs or technical detail beyond "patch your CMS."
- **OpenAI bets on families as ChatGPT goes deeper into households** — TechCrunch AI. Product/hiring roadmap item (job posting for a PM role), no security angle or substantive launch.
