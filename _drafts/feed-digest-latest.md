# Digest — 2026-05-02 PM

- Window: last 14h
- Raw items considered: 5
- Relevant: 3
- Skippable: 2

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Trellix Confirms Source Code Breach via Unauthorized Repository Access — `2026-05-02-trellix-source-code-breach.md`
- [x] **[HIGH]** ConsentFix v3 Automates OAuth Consent Abuse Against Azure Tenants — `2026-05-02-consentfix-v3-azure-oauth-abuse.md`
- [x] **[MEDIUM]** Bluekit Phishing Kit Bundles AI Assistant and Automated Domain Registration — `2026-05-02-bluekit-phishing-kit-ai-assistant.md`

## Relevant (details)

### 1. Trellix Confirms Source Code Breach via Unauthorized Repository Access
- **Source:** The Hacker News — https://thehackernews.com/2026/05/trellix-confirms-source-code-breach.html
- **Severity:** critical
- **Tags:** `data-breach`, `supply-chain`, `appsec`
- **Summary:** Trellix confirmed unauthorized access to a portion of its source code repository. A source code leak from a security vendor is high-risk — attackers can reverse-engineer it to find undisclosed vulnerabilities or develop evasion techniques against Trellix's defensive products.

### 2. ConsentFix v3 Automates OAuth Consent Abuse Against Azure Tenants
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/consentfix-v3-attacks-target-azure-with-automated-oauth-abuse/
- **Severity:** high
- **Tags:** `azure`, `iam`, `cloud-security`, `phishing`
- **Summary:** A new Azure-targeting toolkit circulating on hacker forums adds automation to OAuth consent-phishing, scaling attacks against Azure tenants beyond what earlier manual variants supported. Defenders should restrict third-party OAuth app consent grants and audit enterprise app registrations.

### 3. Bluekit Phishing Kit Bundles AI Assistant and Automated Domain Registration
- **Source:** SecurityWeek — https://www.securityweek.com/new-bluekit-phishing-kit-features-ai-assistant/
- **Severity:** medium
- **Tags:** `phishing`, `llm`, `appsec`
- **Summary:** Bluekit, still under development, embeds an AI assistant and automated domain registration in a phishing kit — lowering the skill floor for running campaigns. Represents the emerging trend of LLMs integrated directly into offensive tooling.

## Skippable

- **Sightings** — Simon Willison. Personal blog post about adding bird photos to a personal site; no security or AI news value.
- **The best AI dictation apps, tested and ranked** — TechCrunch AI. Consumer product roundup with no security angle.
