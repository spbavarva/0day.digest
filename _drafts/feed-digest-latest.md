# Digest — 2026-08-26 AM

- Window: last 14h
- Raw items considered: 18
- Relevant: 7
- Skippable: 11

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Critical Gitea RCE Actively Exploited as Attackers Drop Miner-Like Payload — `2026-08-26-gitea-rce-actively-exploited-cve-2026-60004.md`
- [x] **[HIGH]** Fake Apple Support AI Calls Target Stolen-Device Owners for Passcodes — `2026-08-26-anonymouskit-ai-voice-phishing-apple-support.md`
- [x] **[MEDIUM]** Hackers Abuse npm Mirrors to Host Phishing Redirect Pages — `2026-08-25-npm-mirrors-abused-for-phishing-redirects.md`
- [x] **[MEDIUM]** Hidden Prompts Trick AI Into False Email Summaries — `2026-08-25-hidden-prompts-trick-ai-email-summaries.md`
- [x] **[HIGH]** Networking Flaw in NVIDIA's OpenClaw Allows LLM Poisoning via Ollama API — `2026-08-25-openclaw-ollama-llm-poisoning-flaw.md`
- [x] **[HIGH]** Employee Benefits Platform Paylogix Says Akira Ransomware Stole Financial and Health Data — `2026-08-25-paylogix-akira-ransomware-breach.md`
- [x] **[INFORMATIONAL]** Claude Cowork Finally Remembers What You Told the App in Chat — `2026-08-25-claude-cowork-shared-memory.md`

## Relevant (details)

### 1. Critical Gitea RCE Actively Exploited as Attackers Drop Miner-Like Payload
- **Source:** The Hacker News — https://thehackernews.com/2026/08/critical-gitea-rce-actively-exploited.html
- **Severity:** critical
- **Tags:** `rce`, `cve`, `vulnerability`, `appsec`
- **Summary:** CISA warned of active exploitation of CVE-2026-60004 (CVSS 9.8), a critical RCE in Gitea patched in late July. Reported attacks are dropping a miner-like payload on unpatched instances.

### 2. Fake Apple Support AI Calls Target Stolen-Device Owners for Passcodes
- **Source:** The Hacker News — https://thehackernews.com/2026/08/fake-apple-support-ai-calls-target.html
- **Severity:** high
- **Tags:** `phishing`, `llm`
- **Summary:** A phishing-as-a-service platform called AnonyMousKIT uses rented AI voice agents posing as Apple Support to trick theft victims into giving up device passcodes and 2FA codes. It's built to strip Activation Lock from stolen devices.

### 3. Hackers Abuse npm Mirrors to Host Phishing Redirect Pages
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-abuse-npm-mirrors-to-host-phishing-redirect-pages/
- **Severity:** medium
- **Tags:** `npm`, `phishing`, `supply-chain`
- **Summary:** Threat actors are hosting fake Cloudflare CAPTCHA pages on npm and its mirrors to redirect visitors to attacker-controlled sites, leveraging trusted npm infrastructure to dodge domain-reputation filtering.

### 4. Hidden Prompts Trick AI Into False Email Summaries
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/hidden-prompts-trick-ai-false-email-summaries
- **Severity:** medium
- **Tags:** `llm`, `ai-safety`, `phishing`
- **Summary:** Researchers demonstrated hiding HTML invisible to human readers in emails to manipulate AI-powered email summarizers into producing attacker-influenced summaries — a prompt-injection variant targeting AI email features.

### 5. Networking Flaw in NVIDIA's OpenClaw Allows LLM Poisoning via Ollama API
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/nemo-claw-networking-llm-poisoning-openclaw
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `vulnerability`
- **Summary:** A bug dubbed "Nemo(Claw)" in NVIDIA's OpenClaw gives attackers unauthenticated access to the local model server via the Ollama API, enabling persistent corruption of an AI agent running on the host.

### 6. Employee Benefits Platform Paylogix Says Akira Ransomware Stole Financial and Health Data
- **Source:** The Record (Recorded Future) — https://therecord.media/paylogix-cyberattack-akira-ransomware
- **Severity:** high
- **Tags:** `ransomware`, `data-breach`
- **Summary:** Paylogix disclosed that the Akira ransomware group stole financial and health data on tens of thousands of people. As a benefits management platform, the exposure likely extends to employees of client companies.

### 7. Claude Cowork Finally Remembers What You Told the App in Chat
- **Source:** TechCrunch AI — https://techcrunch.com/2026/08/25/claude-cowork-finally-remembers-what-you-told-the-app-in-chat/
- **Severity:** informational
- **Tags:** `anthropic`, `ai-launch`
- **Summary:** Anthropic is adding shared memory across Claude's chat and Cowork surfaces so users don't have to repeatedly re-brief the AI on projects and preferences.

## Skippable

- **CISA Warns of Exploited Gitea Vulnerability** — SecurityWeek. Duplicate coverage of the same CVE-2026-60004 story; The Hacker News version has more detail.
- **India's Ringg gets backing from Peak XV as it pushes voice AI past the phone call** — TechCrunch AI. Funding round, no security angle.
- **Robotics startup Generalist reaches $3B valuation, sources say** — TechCrunch AI. Funding round, no security or model-capability substance.
- **OpenAI loses a top data center exec as stream of high-profile departures continues** — TechCrunch AI. Personnel/career news, no security or model substance.
- **EVE Online: The Move to Python 3 Begins!** — Simon Willison. General software engineering post, no AI or security angle.
- **LACMA data breach last year exposed social security and medical data** — BleepingComputer. Generic breach disclosure; no victim count or technical detail available to assess scale or substance.
- **Fast Track ISM-ready cloud environments and IRAP Assessments with Landing Zone Accelerator on AWS** — AWS Security Blog. Compliance-report/marketing announcement, no new vulnerability or technical substance.
- **58 arrested in international cybercrime crackdown** — The Record (Recorded Future). Law enforcement news without new IOCs or TTPs.
- **AnonyMousKIT PhaaS uses voice AI agents to phish iPhone passcodes** — BleepingComputer. Duplicate coverage of the same AnonyMousKIT story; The Hacker News version used instead.
- **Stability AI, maker of image generator Stable Diffusion, raises $76 million in fresh funding** — TechCrunch AI. Funding round, no security or model-launch substance.
- **U.S. Sanctions Iran-Linked Hackers Behind Critical Infrastructure Breaches** — The Hacker News. Sanctions announcement with no new IOCs or technical detail for practitioners.
