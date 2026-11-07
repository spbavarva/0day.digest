# Digest — 2026-11-07 PM

- Window: last 14h
- Raw items considered: 6
- Relevant: 3
- Skippable: 3

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[MEDIUM]** METR Report: Anthropic's AI Models Improving Twice as Fast as Last Year — `2026-11-07-anthropic-metr-ai-development-report.md`
- [x] **[HIGH]** SonicWall Patches Exploited SonicOS Flaw That Let Attackers Bypass SAML VPN Logins — `2026-11-07-sonicwall-sonicos-saml-mfa-bypass-cve-2026-19868.md`
- [x] **[HIGH]** Claude Code's "Don't Ask Again" Setting Exposed Secrets in 1,122 Public GitHub Repos — `2026-11-07-claude-code-dont-ask-again-secrets-exposure.md`

## Relevant (details)

### 1. METR Report: Anthropic's AI Models Improving Twice as Fast as Last Year
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/1029126/anthropic-metr-report-accelerating-ai-development
- **Severity:** medium
- **Tags:** `ai-safety`, `anthropic`
- **Summary:** METR found after an 11-week investigation that Anthropic's models are improving roughly twice as fast as a year ago, with no sign of slowing. Researchers called the acceleration alarming.

### 2. SonicWall Patches Exploited SonicOS Flaw That Let Attackers Bypass SAML VPN Logins
- **Source:** SecurityWeek — https://www.securityweek.com/sonicwall-patches-exploited-sonicos-bug-that-weakens-vpn-logins/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Summary:** CVE-2026-19868 lets attackers who hold credentials for one login method bypass SAML checks (including SAML-enforced MFA) on SonicOS VPN logins. Exploited in the wild; SonicWall has released a patch.

### 3. Claude Code's "Don't Ask Again" Setting Exposed Secrets in 1,122 Public GitHub Repos
- **Source:** The Hacker News — https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html
- **Severity:** high
- **Tags:** `anthropic`, `llm`
- **Summary:** Selecting "don't ask again" in Claude Code can save an approved command verbatim — including embedded secrets — to a project settings file. Apiiro found passwords and API keys from these files in 1,122 public GitHub repos.

## Skippable

- **Crusoe sells troubled Wyoming data center project to Google** — TechCrunch AI. Generic AI-infrastructure business deal, no security or capability angle.
- **SonicWall warns of new SSL-VPN MFA bypass flaw exploited in attacks** — BleepingComputer. Duplicate coverage of the same SonicWall SAML/SSL-VPN auth-bypass patch; SecurityWeek's writeup has the specific CVE and mechanism.
- **OpenAI valued at $1.25 trillion, as rival Anthropic nears its IPO** — The Verge AI. Funding/valuation news, no technical or security substance.
