# Digest — 2026-09-19 AM

- Window: last 14h
- Raw items considered: 15
- Relevant: 7
- Skippable: 8

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws — `2026-09-19-claude-opus-5-openai-account-takeover.md`
- [x] **[HIGH]** SolarWinds Patches ARM Hard-Coded Key Flaw Enabling Unauthenticated RCE — `2026-09-19-solarwinds-arm-hardcoded-key-rce.md`
- [x] **[CRITICAL]** Critical Pre-Auth RCE in Orkes Conductor Workflow Platform Exploited in the Wild — `2026-09-19-orkes-conductor-critical-rce-exploited.md`
- [x] **[HIGH]** Google Gemini Broke Into Real Company Systems After Security Test Domain Mix-Up — `2026-09-19-google-gemini-breaks-into-company-systems.md`
- [x] **[CRITICAL]** CrowdSec Says TanStack npm Attack Led to Copy of 170 Private GitHub Repositories — `2026-09-19-crowdsec-tanstack-npm-attack-github-repos.md`
- [x] **[CRITICAL]** CISA Flags Three Linux Kernel Vulnerabilities Exploited in the Wild — `2026-09-19-cisa-linux-kernel-kev-three-flaws.md`
- [x] **[HIGH]** AI Hallucination Nearly Triggers US Military Operation — `2026-09-18-ai-hallucination-military-operation.md`

## Relevant (details)

### 1. Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts via Chained Flaws
- **Source:** The Hacker News — https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `anthropic`, `openai`, `appsec`, `privilege-escalation`
- **Slug:** `claude-opus-5-openai-account-takeover`
- **Must-know:** no
- **Summary:** Researchers at security firm Hacktron used Anthropic's Claude Opus 5 to chain a help-forum bug with a login weakness, taking over OpenAI employees' ChatGPT/Codex accounts and reaching an internal code repository. The work was disclosed as authorized security research.

### 2. SolarWinds Patches ARM Hard-Coded Key Flaw Enabling Unauthenticated RCE
- **Source:** The Hacker News — https://thehackernews.com/2026/09/solarwinds-patches-arm-hard-coded-key.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `solarwinds-arm-hardcoded-key-rce`
- **Must-know:** no
- **Summary:** SolarWinds patched CVE-2026-28326 (CVSS 8.8), a hard-coded key flaw in Access Rights Manager that could enable unauthenticated RCE. It affects all ARM versions 2026.2 and prior.

### 3. Critical Pre-Auth RCE in Orkes Conductor Workflow Platform Exploited in the Wild
- **Source:** The Hacker News — https://thehackernews.com/2026/09/critical-pre-auth-rce-in-orkes.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `rce`, `zero-day`
- **Slug:** `orkes-conductor-critical-rce-exploited`
- **Must-know:** yes
- **Summary:** CVE-2026-58138 (CVSS 9.8), an unauthenticated pre-auth RCE in Orkes Conductor versions 3.21.21–3.30.2, is being actively exploited in the wild per Fortinet.

### 4. Google Gemini Broke Into Real Company Systems After Security Test Domain Mix-Up
- **Source:** The Hacker News — https://thehackernews.com/2026/09/google-gemini-broke-into-real-company.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `google`, `ai-safety`, `llm`
- **Slug:** `google-gemini-breaks-into-company-systems`
- **Must-know:** no
- **Summary:** Google's Gemini accessed real company systems during a May 2026 cybersecurity evaluation run by Israeli firm Irregular, reportedly due to a domain mix-up. First reported by the Wall Street Journal; Irregular was previously involved in similar incidents at other labs.

### 5. CrowdSec Says TanStack npm Attack Led to Copy of 170 Private GitHub Repositories
- **Source:** The Hacker News — https://thehackernews.com/2026/09/crowdsec-says-tanstack-npm-attack-led.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `github`, `data-breach`
- **Slug:** `crowdsec-tanstack-npm-attack-github-repos`
- **Must-know:** yes
- **Summary:** An attacker used a departed employee's still-active GitHub access to copy ~170 of CrowdSec's private repos on May 22. CrowdSec says the employee's laptop was compromised in the earlier TanStack npm supply chain attack.

### 6. CISA Flags Three Linux Kernel Vulnerabilities Exploited in the Wild
- **Source:** The Hacker News — https://thehackernews.com/2026/09/cisa-flags-three-linux-kernel.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `zero-day`
- **Slug:** `cisa-linux-kernel-kev-three-flaws`
- **Must-know:** yes
- **Summary:** CISA added three actively-exploited Linux kernel flaws to its KEV catalog, including CVE-2025-39682 (CVSS 9.8) in the TLS receive path. Federal agencies must remediate within mandated timelines.

### 7. AI Hallucination Nearly Triggers US Military Operation
- **Source:** TechCrunch AI — https://techcrunch.com/2026/09/18/ai-hallucination-nearly-triggers-us-military-operation/
- **Section:** AI — News & Analysis
- **Severity:** high
- **Tags:** `ai-safety`, `llm`
- **Slug:** `ai-hallucination-military-operation`
- **Must-know:** no
- **Summary:** A GovAI research scholar warned that an AI hallucination nearly triggered a US military operation, underscoring the risk of relying on LLM output in high-stakes operational decisions.

## Skippable

- **[Virtual Event] Cybersecurity Outlook 2027** — Dark Reading. Event promo, no news value.
- **Calling viral AI actress Tilly Norwood? Agree to a face scan first** — BleepingComputer. Consumer privacy curiosity piece about a viral AI avatar service; no vulnerability, breach, or launch to report.
- **India forces caller-ID apps to feed spam reports to telcos** — TechCrunch AI. Telecom data-sharing regulation, not an AI security or launch story.
- **Tilly Norwood's press tour is going about as well as you'd expect for an AI** — TechCrunch AI. Opinion/entertainment piece, no news substance.
- **Gemini Hacked Three Companies in First Known Breakout by Google's AI** — Simon Willison. Duplicate coverage of the Gemini/Irregular story; The Hacker News picked as primary source.
- **A startup that builds other startups raised $100M and is all-in on physical AI** — TechCrunch AI. Generic funding news, no security or notable model-launch angle.
- **Anthropic is operating a lab that conducts biology experiments** — TechCrunch AI. Thin, editorial framing without concrete technical or safety detail.
- **Anthropic's first embedded evaluator is … Accenture?** — TechCrunch AI. Opinion-toned partnership blurb, insufficient factual detail to report.
