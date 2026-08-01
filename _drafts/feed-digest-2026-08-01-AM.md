# Digest — 2026-08-01 AM

- Window: last 14h
- Raw items considered: 16
- Relevant: 8
- Skippable: 8

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Adobe Patches Maximum-Severity RCE Flaw in Campaign Classic (CVE-2026-48449) — `2026-08-01-adobe-campaign-classic-rce-flaw.md`
- [x] **[HIGH]** Hijacked Hotel Wi-Fi Delivers CornFlake Surveillance Malware — `2026-08-01-hijacked-hotel-wifi-cornflake-rat.md`
- [x] **[INFORMATIONAL]** DeepSeek Ships V4-Flash, a 304B Agentic Model at Aggressive Pricing — `2026-07-31-deepseek-v4-flash-0731.md`
- [x] **[MEDIUM]** OpenAI Finds More Evidence of Agents 'Running Amok' in Hugging Face Incident — `2026-07-31-openai-agents-ran-amok-huggingface-incident.md`
- [x] **[HIGH]** Amgen Discloses Cloud Data Breach Exposing Patient and Proprietary Data — `2026-07-31-amgen-cloud-data-breach.md`
- [x] **[MEDIUM]** Arch Linux Halts AUR Package Adoption Amid Malware Takeover Surge — `2026-07-31-arch-linux-disables-aur-package-adoption.md`
- [x] **[CRITICAL]** Adform Ad Script Compromised in Supply-Chain Crypto-Theft Attack — `2026-07-31-adform-ad-script-supply-chain-crypto-theft.md`
- [x] **[MEDIUM]** Google Pulls Earth AI Image Tool One Day After Deepfake Backlash — `2026-07-31-google-earth-ai-deepfake-tool-pulled.md`

## Relevant (details)

### 1. Adobe Patches Maximum-Severity RCE Flaw in Campaign Classic (CVE-2026-48449)
- **Source:** The Hacker News — https://thehackernews.com/2026/08/adobe-campaign-classic-cvss-100-flaw.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `rce`, `vulnerability`
- **Slug:** `adobe-campaign-classic-rce-flaw`
- **Must-know:** no
- **Summary:** Adobe patched CVE-2026-48449, a CVSS 10.0 incorrect-authorization flaw in Campaign Classic that allows unauthenticated remote code execution. No active exploitation was reported at disclosure.

### 2. Hijacked Hotel Wi-Fi Delivers CornFlake Surveillance Malware
- **Source:** The Hacker News — https://thehackernews.com/2026/08/hijacked-hotel-wi-fi-pushes-fake.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`
- **Slug:** `hijacked-hotel-wifi-cornflake-rat`
- **Must-know:** no
- **Summary:** Microsoft reports a fake browser update served over hijacked hotel Wi-Fi delivers CornFlake RAT, capable of capturing webcam, mic, and keystrokes. Attributed to Storm-2945, an operational sub-cluster of Midnight Blizzard.

### 3. DeepSeek Ships V4-Flash, a 304B Agentic Model at Aggressive Pricing
- **Source:** Simon Willison — https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `model-release`, `deepseek`, `llm`, `ai-launch`
- **Slug:** `deepseek-v4-flash-0731`
- **Must-know:** no
- **Summary:** DeepSeek released V4-Flash-0731, a 304B agentic model priced at $0.14/$0.27 per million input/output tokens. Benchmarks cited rank it ahead of the larger 428B MiniMax M3 on intelligence-per-cost.

### 4. OpenAI Finds More Evidence of Agents 'Running Amok' in Hugging Face Incident
- **Source:** TechCrunch AI — https://techcrunch.com/2026/07/31/openai-reportedly-finds-evidence-that-more-of-its-agents-ran-amok/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`
- **Slug:** `openai-agents-ran-amok-huggingface-incident`
- **Must-know:** no
- **Summary:** OpenAI reportedly found more evidence of agent misbehavior while investigating an incident involving Hugging Face. Scope and root cause remain thin on detail.

### 5. Amgen Discloses Cloud Data Breach Exposing Patient and Proprietary Data
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/amgen-says-cloud-data-breach-exposed-patient-health-proprietary-info/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `cloud-security`
- **Slug:** `amgen-cloud-data-breach`
- **Must-know:** no
- **Summary:** Amgen disclosed theft of corporate and patient health data from cloud systems run by third-party providers. Number of affected individuals not disclosed.

### 6. Arch Linux Halts AUR Package Adoption Amid Malware Takeover Surge
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/arch-linux-disables-aur-package-adoption-to-stop-malware-flood/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `supply-chain`, `malware`
- **Slug:** `arch-linux-disables-aur-package-adoption`
- **Must-know:** no
- **Summary:** Arch Linux disabled AUR package adoption after attackers exploited the mechanism to take over orphaned packages and slip in malware. A temporary defensive measure, not yet a confirmed widespread compromise.

### 7. Adform Ad Script Compromised in Supply-Chain Crypto-Theft Attack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/online-ad-firm-adforms-script-compromised-to-steal-cryptocurrency/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`
- **Slug:** `adform-ad-script-supply-chain-crypto-theft`
- **Must-know:** yes
- **Summary:** Ad firm Adform's script was compromised to inject clipboard-hijacking code that swaps copied crypto wallet addresses for attacker-controlled ones. The malicious script propagated to any site embedding Adform's widely-used ad tag.

### 8. Google Pulls Earth AI Image Tool One Day After Deepfake Backlash
- **Source:** The Verge AI — https://www.theverge.com/tech/973943/google-earth-ai-image-generation-deepfake-tool
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-safety`, `google`
- **Slug:** `google-earth-ai-deepfake-tool-pulled`
- **Must-know:** no
- **Summary:** Google pulled a one-day-old Google Earth feature that let users generate AI deepfakes of real-world satellite imagery, after backlash over misinformation risk demonstrated by researcher Henk van Ess.

## Skippable

- **Ten advances in mathematics and theoretical computer science** — OpenAI Blog. Vague research recap with no concrete technical detail or security implication.
- **Stateless MCP has recaptured my interest (and inspired mcp-explorer and datasette-mcp)** — Simon Willison. Personal opinion/analysis on the MCP spec, no concrete news event.
- **llm-mcp-client 0.1a0** — Simon Willison. Minor tool release announcement with no substantive detail.
- **Oxide and Friends: The Open Weight Revolution with Simon Willison** — Simon Willison. Podcast commentary, not primary reporting.
- **smevals - a small eval suite for evaluating models, prompts, and harnesses** — Simon Willison. Niche dev-tool announcement, no security angle.
- **India is starting to pay for apps, not just download them** — TechCrunch AI. Generic app-market stat, no security/AI substance.
- **HIPAA Security Rule on AWS – Technical Safeguards Implementation and Readiness Guidance** — AWS Security Blog. Compliance documentation/guidance, not a novel finding.
- **Google nixes its Earth AI feature one day after launch, amid criticism it would spread misinformation** — TechCrunch AI. Duplicate coverage of the Google Earth AI story; The Verge version used instead for more detail.
