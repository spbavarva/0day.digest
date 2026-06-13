# Digest — 2026-06-13 PM

- Window: last 14h
- Raw items considered: 12
- Relevant: 5
- Skippable: 4

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Critical Splunk Enterprise Flaw (CVE-2026-20253) Allows Unauthenticated Remote Code Execution — `2026-06-13-splunk-enterprise-unauth-rce-cve-2026-20253.md`
- [x] **[HIGH]** Chinese Hackers Hijacked Authentication Flow to Spy on Isolated Network for a Decade — `2026-06-13-chinese-apt-decade-long-auth-hijack.md`
- [x] **[HIGH]** US Orders Anthropic to Suspend Fable 5 and Mythos 5 for Foreign Nationals; Anthropic Takes Both Models Offline Worldwide — `2026-06-13-us-orders-anthropic-suspend-fable-mythos.md`
- [x] **[INFORMATIONAL]** npm 12 Will Disable Dependency Install Scripts by Default to Curb Supply Chain Attacks — `2026-06-13-npm-12-blocks-install-scripts-supply-chain.md`
- [x] **[INFORMATIONAL]** OpenAI Faces Investigation From Multiple State Attorneys General — `2026-06-13-openai-state-ag-investigation.md`

## Relevant (details)

### 1. Critical Splunk Enterprise Flaw (CVE-2026-20253) Allows Unauthenticated Remote Code Execution
- **Source:** The Hacker News — https://thehackernews.com/2026/06/critical-splunk-enterprise-flaw-lets.html
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `rce`, `appsec`
- **Summary:** Splunk patched CVE-2026-20253 (CVSS 9.8), a critical flaw in Splunk Enterprise versions below 10.2.4 and 10.0.7 that lets an unauthenticated attacker perform arbitrary file operations and achieve remote code execution. Given the unauthenticated, remote nature of the bug, affected deployments should be patched immediately.

### 2. Chinese Hackers Hijacked Authentication Flow to Spy on Isolated Network for a Decade
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/chinese-hackers-hijack-auth-flow-spy-on-isolated-network-for-a-decade/
- **Severity:** high
- **Tags:** `apt`, `privilege-escalation`, `iam`
- **Summary:** A China-linked threat actor took control of a target organization's authentication stack and maintained persistent access with full visibility into administrative activity for roughly a decade. The target network was described as isolated, indicating the intrusion bypassed the segmentation meant to protect it.

### 3. US Orders Anthropic to Suspend Fable 5 and Mythos 5 for Foreign Nationals; Anthropic Takes Both Models Offline Worldwide
- **Source:** The Hacker News — https://thehackernews.com/2026/06/us-orders-anthropic-to-suspend-fable-5.html
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/us-gov-asks-anthropic-to-ban-foreign-national-access-to-fable-mythos/
- **Source:** SecurityWeek — https://www.securityweek.com/anthropic-says-it-has-taken-its-latest-ai-models-offline-to-comply-with-new-export-controls/
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/949553/anthropic-fable-5-mythos-5-government-national-security
- **Severity:** high
- **Tags:** `anthropic`, `ai-safety`, `llm`
- **Summary:** The US government ordered Anthropic, citing national security concerns, to block all foreign nationals — including its own employees — from accessing Claude Fable 5 and Mythos 5; Anthropic complied by taking both models offline worldwide. Anthropic disputes the order's basis, calling the cited jailbreak narrow and the underlying capability widely available elsewhere.

### 4. npm 12 Will Disable Dependency Install Scripts by Default to Curb Supply Chain Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/npm-12-will-change-script-execution-behavior-to-prevent-supply-chain-attacks/
- **Severity:** informational
- **Tags:** `npm`, `supply-chain`, `devsecops`
- **Summary:** npm 12 will stop running dependency lifecycle scripts (preinstall/install/postinstall) by default, requiring projects to explicitly opt in — closing off a common npm supply chain attack vector. Projects that rely on install scripts for legitimate build steps will need to allow them explicitly once npm 12 ships.

### 5. OpenAI Faces Investigation From Multiple State Attorneys General
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/13/openai-faces-investigation-from-state-attorneys-general/
- **Severity:** informational
- **Tags:** `openai`, `privacy`, `llm`
- **Summary:** Multiple US state attorneys general have opened an investigation into OpenAI covering topics including its advertising policies and handling of users' health data; the states involved haven't been disclosed. No findings or enforcement actions have been announced yet.

## Skippable

- **My yard is dying, so I made an app for that** — The Verge AI. Personal vibe-coding anecdote about building a gardening app, no security or news substance.
- **Apple's new AI photo editing tools mostly work, for better and worse** — The Verge AI. Hands-on review of iOS 27 AI photo editing features, no security angle.
- **The future of Hollywood isn't feeding prompts into vanilla gen AI models** — The Verge AI. Opinion piece on AI's role in filmmaking, no news or security value.
- **Andrew Yang thinks the next big startup opportunity is lowering the cost of living** — TechCrunch AI. General startup/economic opinion piece, no AI or security substance.
