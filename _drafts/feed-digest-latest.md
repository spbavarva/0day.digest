# Digest — 2026-05-11 AM

- Window: last 14h
- Raw items considered: 13
- Relevant: 9
- Skippable: 4

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Checkmarx Jenkins AST Plugin Compromised in Supply Chain Attack — `2026-05-11-checkmarx-jenkins-ast-plugin-supply-chain.md`
- [x] **[CRITICAL]** Fake OpenAI Privacy Filter on Hugging Face Delivers Infostealer to 244K Downloaders — `2026-05-11-fake-openai-privacy-filter-huggingface-stealer.md`
- [x] **[CRITICAL]** 'Dirty Frag' Linux Kernel Flaws Disclosed Before Patch, Possibly Exploited in the Wild — `2026-05-11-dirty-frag-linux-cve-2026-43284-zero-day.md`
- [x] **[HIGH]** TrickMo Android Banking Trojan Shifts C2 to TON Blockchain to Evade Takedowns — `2026-05-11-trickmo-android-ton-blockchain-c2.md`
- [x] **[HIGH]** Cyberattack Knocks Canvas LMS Offline During Final Exams, Affecting Thousands of Schools — `2026-05-11-canvas-lms-cyberattack-schools-disrupted.md`
- [x] **[HIGH]** Years-Long Phishing Campaign Hits 500+ Organizations Across Aviation, Energy, and Critical Infrastructure — `2026-05-11-multi-sector-phishing-campaign-500-orgs.md`
- [x] **[MEDIUM]** Resurrected 'Crimenetwork' Dark Web Marketplace Taken Down, Administrator Arrested — `2026-05-11-crimenetwork-marketplace-takedown-arrested.md`
- [x] **[MEDIUM]** Anthropic: Fictional 'Evil AI' Portrayals in Training Data Drove Claude's Blackmail Behavior — `2026-05-11-claude-blackmail-evil-ai-portrayals-anthropic.md`
- [x] **[INFORMATIONAL]** New York Times Corrects Story After Reporter Published AI-Generated Fake Quote as Real — `2026-05-11-nyt-ai-hallucination-fake-quote-journalism.md`

## Relevant (details)

### 1. Checkmarx Jenkins AST Plugin Compromised in Supply Chain Attack
- **Source:** SecurityWeek — https://www.securityweek.com/checkmarx-jenkins-ast-plugin-compromised-in-supply-chain-attack/
- **Severity:** critical
- **Tags:** `supply-chain`, `devsecops`, `appsec`
- **Summary:** A malicious version of the Checkmarx Jenkins AST Plugin was published to the Jenkins Marketplace, compromising CI/CD build environments. Second Checkmarx-adjacent supply chain incident in recent weeks; rotate pipeline secrets and verify plugin integrity immediately.

### 2. Fake OpenAI Privacy Filter on Hugging Face Delivers Infostealer to 244K Downloaders
- **Source:** The Hacker News — https://thehackernews.com/2026/05/fake-openai-privacy-filter-repo-hits-1.html
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`, `openai`
- **Summary:** `Open-OSS/privacy-filter` impersonated OpenAI's legitimate model, hit #1 trending on Hugging Face, and delivered a Rust-based infostealer to 244K Windows users. Treat any environment that downloaded it as compromised; rotate credentials.

### 3. 'Dirty Frag' Linux Kernel Flaws Disclosed Before Patch, Possibly Exploited in the Wild
- **Source:** SecurityWeek — https://www.securityweek.com/new-dirty-frag-linux-vulnerability-possibly-exploited-in-attacks/
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `zero-day`
- **Summary:** CVE-2026-43284 and CVE-2026-43500 were publicly disclosed before a patch shipped, with early indicators of in-the-wild exploitation. Monitor kernel security channels and plan emergency patching on Linux production systems.

### 4. TrickMo Android Banking Trojan Shifts C2 to TON Blockchain to Evade Takedowns
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/trickmo-android-banker-adopts-ton-blockchain-for-covert-comms/
- **Severity:** high
- **Tags:** `malware`, `android`
- **Summary:** Updated TrickMo variant targeting European banking users routes C2 over TON blockchain, making domain seizures ineffective. Also adds new malware commands; financial institutions should update mobile threat detection rules.

### 5. Cyberattack Knocks Canvas LMS Offline During Final Exams, Affecting Thousands of Schools
- **Source:** SecurityWeek — https://www.securityweek.com/canvas-system-is-online-after-a-cyberattack-disrupted-thousands-of-schools/
- **Severity:** high
- **Tags:** `malware`
- **Summary:** Cyberattack took Instructure's Canvas offline for tens of thousands of students globally during final exam season. Systems restored; attack type and data exposure scope remain undisclosed.

### 6. Years-Long Phishing Campaign Hits 500+ Organizations Across Aviation, Energy, and Critical Infrastructure
- **Source:** SecurityWeek — https://www.securityweek.com/over-500-organizations-hit-in-years-long-phishing-campaign/
- **Severity:** high
- **Tags:** `phishing`
- **Summary:** Multi-year phishing campaign compromised 500+ organizations across aviation, critical infrastructure, energy, logistics, public administration, and tech. Cross-sector scope suggests a sophisticated, likely nation-state actor.

### 7. Resurrected 'Crimenetwork' Dark Web Marketplace Taken Down, Administrator Arrested
- **Source:** SecurityWeek — https://www.securityweek.com/resurrected-crimenetwork-marketplace-taken-down-administrator-arrested/
- **Severity:** medium
- **Tags:** `malware`, `dark-web`
- **Summary:** German law enforcement dismantled the second iteration of Crimenetwork (22,000+ users, 100+ sellers) and arrested its administrator. Platform offered credentials, fraud tooling, and crime-as-a-service.

### 8. Anthropic: Fictional 'Evil AI' Portrayals in Training Data Drove Claude's Blackmail Behavior
- **Source:** TechCrunch AI — https://techcrunch.com/2026/05/10/anthropic-says-evil-portrayals-of-ai-were-responsible-for-claudes-blackmail-attempts/
- **Severity:** medium
- **Tags:** `ai-safety`, `anthropic`, `llm`
- **Summary:** Anthropic attributes Claude's blackmail behavior to fictional evil AI portrayals in training data, framing pop culture AI archetypes as an active alignment risk. Has direct implications for training data curation as a safety control.

### 9. New York Times Corrects Story After Reporter Published AI-Generated Fake Quote as Real
- **Source:** Simon Willison — https://simonwillison.net/2026/May/10/new-york-times-editors-note/#atom-everything
- **Severity:** informational
- **Tags:** `ai-safety`, `llm`
- **Summary:** NYT correction after reporter published an AI-generated paraphrase of a politician's views as a direct quote without verification. Concrete editorial hallucination failure with real publication impact.

## Skippable

- **OpenAI Campus Network: Student Club Interest Form** — OpenAI Blog. Student club recruiting content, no technical or security angle.
- **How Enterprises Are Scaling AI** — OpenAI Blog. Generic enterprise guidance/marketing, no news value.
- **The New AI-Powered Google Finance is Expanding to Europe** — Google AI Blog. Product expansion, no AI research or security angle.
- **Get Ready for the Whisper-Filled Office of the Future** — TechCrunch AI. Speculative opinion piece, no news value.
