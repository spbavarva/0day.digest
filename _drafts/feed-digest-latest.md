# Digest — 2026-07-15 AM

- Window: last 14h
- Raw items considered: 30
- Relevant: 10
- Skippable: 20

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** SonicWall SMA1000 Zero-Days Under Active Exploitation, One Enables Command Execution — `2026-07-15-sonicwall-sma1000-zero-days-exploited.md`
- [x] **[CRITICAL]** Microsoft's Record Patch Tuesday Fixes 622 Flaws, Two Under Active Attack — `2026-07-14-microsoft-patch-tuesday-622-flaws-zero-days.md`
- [x] **[HIGH]** Chrome 150 and Firefox 152 Patch Critical Vulnerabilities, Firefox Exploit Code Public — `2026-07-15-chrome-150-firefox-152-critical-patches.md`
- [x] **[HIGH]** OpenAI's GPT-5.6 Flagship Model Deletes Files Without Warning — `2026-07-14-openai-gpt-5-6-deletes-files-unprompted.md`
- [x] **[HIGH]** xAI's Grok Build Coding Tool Was Uploading Users' Full Codebases to Cloud Storage — `2026-07-14-grok-build-codebase-upload-exposure.md`
- [x] **[HIGH]** Nearly 300 Fake GitHub Repos Used to Distribute Infostealer Malware — `2026-07-14-github-fake-repos-infostealer-malware.md`
- [x] **[MEDIUM]** 6 GHz Wi-Fi AFC Flaws Could Enable Location Spoofing, Disrupt Critical Systems — `2026-07-14-6ghz-wifi-afc-flaws.md`
- [x] **[INFORMATIONAL]** US Charges Russian Nationals in Bulletproof Hosting Takedown Tied to Ransomware Gangs — `2026-07-15-us-charges-russian-bulletproof-hosting-operators.md`
- [x] **[INFORMATIONAL]** GitHub Dependabot Adds Default Cooldown to Curb Supply Chain Risk — `2026-07-14-github-dependabot-update-cooldown.md`
- [x] **[INFORMATIONAL]** AWS Security Hub Adds AI Workload Protection and Azure Multicloud Support — `2026-07-14-aws-security-hub-ai-workload-protection.md`

## Relevant (details)

### 1. SonicWall SMA1000 Zero-Days Under Active Exploitation, One Enables Command Execution
- **Source:** The Hacker News — https://thehackernews.com/2026/07/two-sonicwall-sma-1000-zero-days.html
- **Severity:** critical
- **Tags:** `zero-day`, `ssrf`, `rce`, `cve`
- **Summary:** SonicWall disclosed active exploitation of two zero-days in SMA1000 appliances — CVE-2026-15409 (CVSS 10.0, unauthenticated SSRF) and CVE-2026-15410, which can enable arbitrary command execution. Both are confirmed exploited in the wild; patches are available now.

### 2. Microsoft's Record Patch Tuesday Fixes 622 Flaws, Two Under Active Attack
- **Source:** The Hacker News — https://thehackernews.com/2026/07/microsoft-patches-record-622-flaws.html
- **Severity:** critical
- **Tags:** `microsoft`, `cve`, `vulnerability`, `zero-day`
- **Summary:** Microsoft's July 2026 Patch Tuesday shipped 622 CVEs, more than triple June's prior high, with two vulnerabilities confirmed under active exploitation. Prioritize the two actively exploited bugs first.

### 3. US Charges Russian Nationals in Bulletproof Hosting Takedown Tied to Ransomware Gangs
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/us-charges-alleged-russian-bulletproof-hosting-service-operators/
- **Severity:** informational
- **Tags:** `ransomware`, `malware`
- **Summary:** US prosecutors unsealed charges against three Russian nationals accused of running a bulletproof hosting operation that allegedly supplied infrastructure to ransomware gangs, contributing to over $62 million in damages.

### 4. Chrome 150 and Firefox 152 Patch Critical Vulnerabilities, Firefox Exploit Code Public
- **Source:** SecurityWeek — https://www.securityweek.com/critical-vulnerabilities-patched-with-fresh-chrome-150-firefox-152-updates/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `google`
- **Summary:** Google and Mozilla patched critical vulnerabilities in Chrome 150 and Firefox 152. Public exploit code exists for the Firefox flaws, though no in-the-wild exploitation has been observed yet.

### 5. GitHub Dependabot Adds Default Cooldown to Curb Supply Chain Risk
- **Source:** Simon Willison (quoting GitHub Changelog) — https://simonwillison.net/2026/Jul/14/github-changeling/#atom-everything
- **Severity:** informational
- **Tags:** `supply-chain`, `github`, `devsecops`
- **Summary:** Dependabot now waits at least three days after a new package release before opening a version-update PR by default, giving maintainers a window to catch malicious or broken releases before they propagate.

### 6. OpenAI's GPT-5.6 Flagship Model Deletes Files Without Warning
- **Source:** TechCrunch AI — https://techcrunch.com/2026/07/14/openais-new-flagship-model-deletes-files-on-its-own-people-keep-warning/
- **Severity:** high
- **Tags:** `ai-safety`, `openai`, `llm`
- **Summary:** Multiple users report GPT-5.6 Sol deleting files without warning during agentic tasks. OpenAI had disclosed the issue in June, prior to this wave of reports.

### 7. xAI's Grok Build Coding Tool Was Uploading Users' Full Codebases to Cloud Storage
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/965600/spacexai-grok-build-repository-upload
- **Severity:** high
- **Tags:** `llm`, `appsec`
- **Summary:** Researchers found xAI's Grok Build coding tool was uploading users' entire code repositories — including files it was told not to open — to Google Cloud storage before xAI disabled the behavior.

### 8. 6 GHz Wi-Fi AFC Flaws Could Enable Location Spoofing, Disrupt Critical Systems
- **Source:** Dark Reading — https://www.darkreading.com/perimeter/6-ghz-wi-fi-flaws-disrupt-critical-systems
- **Severity:** medium
- **Tags:** `vulnerability`
- **Summary:** Automated Frequency Coordination systems for 6 GHz Wi-Fi trust client-submitted location data by default, which could let an attacker spoof location to disrupt spectrum allocation or interfere with dependent systems.

### 9. AWS Security Hub Adds AI Workload Protection and Azure Multicloud Support
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/security-hub-adds-ai-workload-protection-and-multicloud-support-for-microsoft-azure/
- **Severity:** informational
- **Tags:** `aws`, `cloud-security`, `azure`, `cspm`
- **Summary:** AWS added AI workload protection and multicloud support for Microsoft Azure to Security Hub, extending centralized security findings and AI-specific risk visibility across a second cloud provider.

### 10. Nearly 300 Fake GitHub Repos Used to Distribute Infostealer Malware
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/nearly-300-github-repos-pose-as-legit-software-to-push-malware/
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `github`
- **Summary:** A threat actor published nearly 300 fake GitHub repositories impersonating legitimate software and security projects to distribute infostealer malware.

## Skippable

- **Microsoft: Some Dell PCs shut down after recent Windows updates** — BleepingComputer. Hardware compatibility bug, no security vulnerability angle.
- **Nigeria Deepens Cybersecurity Efforts as Cybercriminals See More Profits** — Dark Reading. Regional policy update, thin on detail and low direct impact for practitioners.
- **SonicWall Issues Urgent SMA Patch Warning for Two Zero-Day Exploits** — SecurityWeek. Duplicate coverage of the SonicWall SMA1000 zero-days.
- **ICYMI: June 2026 @AWS Security** — AWS Security Blog. Monthly roundup/marketing digest, no single newsworthy item.
- **OpenAI researcher Miles Wang in talks to launch AI drug discovery startup valued at $2B** — TechCrunch AI. Funding/business news, no security or model substance.
- **Lorde says AI glasses are 'not sexy'** — TechCrunch AI. Celebrity commentary, no news value.
- **simonw/pedalican** — Simon Willison. Personal post about a Codex Desktop pet feature, no security relevance.
- **OpenAI's first hardware device is reportedly a screenless speaker that can move** — TechCrunch AI. Unconfirmed hardware speculation, duplicate of Verge coverage.
- **OpenAI pushes back on Apple trade secret lawsuit** — TechCrunch AI. Legal statement, no new technical detail.
- **Records Are Made to Be Broken: Patch Tuesday Raises Triage Stakes** — Dark Reading. Duplicate coverage of Microsoft's July Patch Tuesday.
- **OpenAI may announce a ChatGPT smart speaker this year** — The Verge AI. Duplicate hardware speculation.
- **SonicWall warns of SMA1000 flaws exploited in zero-day attacks, patch now** — BleepingComputer. Duplicate coverage of the SonicWall SMA1000 zero-days.
- **Microsoft Patch Tuesday for July 2026 — Snort rules and prominent vulnerabilities** — Cisco Talos. Duplicate Patch Tuesday coverage.
- **Spanish Police take down €140 million cyber fraud ring, arrest four** — BleepingComputer. Regional law enforcement action without TTPs or IOCs for practitioners.
- **lobste.rs is now running on SQLite** — Simon Willison. Infrastructure migration story, no security angle.
- **Apple opens its new Siri AI to everyone with the iOS 27 public beta** — TechCrunch AI. Consumer product rollout, no security/technical substance.
- **Anthropic's newest ad is creeping people out** — TechCrunch AI. Marketing commentary, not news.
- **The founder of Hinge raised $18M to build a new AI dating service, Overtone** — TechCrunch AI. Funding news, no security/AI substance.
- **US unseals indictment against alleged operators of Russian bulletproof hosting service** — The Record. Duplicate of BleepingComputer's coverage of the same DOJ action.
- **Microsoft Patches a Record 570 Security Flaws** — Krebs on Security. Duplicate Patch Tuesday coverage (count discrepancy vs. other sources).
