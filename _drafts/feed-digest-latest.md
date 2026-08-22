# Digest — 2026-08-22 AM

- Window: last 14h
- Raw items considered: 10
- Relevant: 6
- Skippable: 4

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[INFORMATIONAL]** TechCrunch Bypasses Anthropic's Opus 4.6 Content Restrictions in NSFW Test — `2026-08-21-anthropic-opus-4-6-nsfw-jailbreak.md`
- [x] **[INFORMATIONAL]** Unit 42: Attackers Increasingly Target CI/CD Pipelines Over Application Code — `2026-08-21-sdlc-supply-chain-security-blueprint.md`
- [x] **[INFORMATIONAL]** Lawmakers Push for Investigation Into Impact of CISA Staffing Cuts — `2026-08-21-cisa-staffing-cuts-investigation.md`
- [x] **[HIGH]** 14 Trojanized npm Packages Deliver RedC2 4.0 Linux Backdoor With AI-Assisted C2 — `2026-08-21-redc2-npm-trojanized-packages-linux-backdoor.md`
- [x] **[MEDIUM]** New SynkLoader Malware Spread via Microsoft Teams Phishing Campaign — `2026-08-21-synkloader-malware-teams-phishing.md`
- [x] **[INFORMATIONAL]** OWASP Publishes New Top 10 List for AI Skill Risks — `2026-08-21-owasp-ai-skill-risks-top-10.md`

## Relevant (details)

### 1. TechCrunch Bypasses Anthropic's Opus 4.6 Content Restrictions in NSFW Test
- **Source:** TechCrunch AI — https://techcrunch.com/2026/08/21/anthropics-opus-4-6-is-a-smut-machine/
- **Severity:** informational
- **Tags:** `anthropic`, `ai-safety`, `llm`
- **Summary:** TechCrunch testing found Anthropic's ban on sexually explicit content in Opus 4.6 could be bypassed without much effort. No technique detail or Anthropic response was available in the source.

### 2. Unit 42: Attackers Increasingly Target CI/CD Pipelines Over Application Code
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/sdlc-supply-chain/
- **Severity:** informational
- **Tags:** `supply-chain`, `devsecops`, `appsec`
- **Summary:** Unit 42 research argues attackers are shifting toward CI/CD pipelines and developer tooling instead of application code, calling for full SDLC visibility and stricter controls. It's a general blueprint, not tied to a specific incident.

### 3. Lawmakers Push for Investigation Into Impact of CISA Staffing Cuts
- **Source:** The Record (Recorded Future) — https://therecord.media/lawmakers-call-for-investigation-into-impact-of-cisa-cuts
- **Severity:** informational
- **Tags:** `policy`
- **Summary:** U.S. lawmakers want an investigation into how recent CISA staffing cuts have affected the agency's capabilities and whether lost institutional knowledge has been replaced. Source detail is thin.

### 4. 14 Trojanized npm Packages Deliver RedC2 4.0 Linux Backdoor With AI-Assisted C2
- **Source:** The Hacker News — https://thehackernews.com/2026/08/14-trojanized-npm-packages-drop-redc2.html
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `malware`
- **Summary:** 14 npm packages posing as calendar/streak utilities were found dropping RedC2 4.0, an AI-assisted Linux backdoor, per Trend Micro's TrendAI research. The module marks a bundled binary executable and launches it as a background process.

### 5. New SynkLoader Malware Spread via Microsoft Teams Phishing Campaign
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-synkloader-malware-pushed-in-microsoft-teams-phishing-campaign/
- **Severity:** medium
- **Tags:** `phishing`, `malware`
- **Summary:** A previously unknown malware family, SynkLoader, is being spread via Microsoft Teams phishing using a fake lock screen to steal credentials. No IOCs were available in the source summary.

### 6. OWASP Publishes New Top 10 List for AI Skill Risks
- **Source:** Dark Reading — https://www.darkreading.com/application-security/owasp-flags-top-ai-skill-risks-security-blueprint
- **Severity:** informational
- **Tags:** `appsec`, `ai-safety`, `llm`
- **Summary:** OWASP released a new top 10 list covering security risks in AI "skills"/agent add-ons, introducing a Universal Skill Format meant to standardize security review of AI add-ons.

## Skippable

- **Nvidia partners with data center developer Cloverleaf** — TechCrunch AI. Generic data center business/investment news, no security angle.
- **Over 1 million people have clicked LinkedIn's AI slop button** — The Verge AI. Product feature usage stat, no security or model-launch substance.
- **Nvidia just showed that the harness, not the AI model, is now the real hero** — TechCrunch AI. Opinion/analysis piece on agent harness design, no concrete news or actionable detail.
- **AWS Glue 6.0 now available with 30% lower price and full Apache Iceberg v3 support** — AWS News Blog. Pricing/performance update, no security implications.
