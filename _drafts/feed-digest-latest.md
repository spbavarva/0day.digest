# Digest — 2026-05-12 AM

- Window: last 14h
- Raw items considered: 22
- Relevant: 10
- Skippable: 12

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Mini Shai-Hulud Worm Hits TanStack, Mistral AI, Guardrails AI and More in Fresh Supply Chain Spree — `2026-05-12-mini-shai-hulud-supply-chain-npm-pypi.md`
- [x] **[CRITICAL]** Official Checkmarx Jenkins AST Plugin Backdoored with Infostealer — `2026-05-11-checkmarx-jenkins-plugin-infostealer.md`
- [x] **[HIGH]** Instructure Pays Off ShinyHunters to Suppress 3.65TB Canvas LMS Data Leak — `2026-05-12-instructure-canvas-shinyhunters-ransom.md`
- [x] **[HIGH]** OpenAI Launches Daybreak: AI-Powered Vulnerability Detection and Automated Patch Validation — `2026-05-12-openai-daybreak-vulnerability-detection.md`
- [x] **[HIGH]** Unit 42 Unpacks AD CS Escalation: Template Misconfigs, Shadow Credentials, and Detection Guidance — `2026-05-11-adcs-escalation-shadow-credentials.md`
- [x] **[MEDIUM]** Kaspersky: State of Ransomware 2026 — EDR Killers Rising, Shift from Encryption to Extortion — `2026-05-12-state-of-ransomware-2026.md`
- [x] **[MEDIUM]** iOS 26.5 Rolls Out Default End-to-End Encrypted RCS Between iPhone and Android — `2026-05-12-ios-265-e2ee-rcs.md`
- [x] **[MEDIUM]** GhostLock PoC: Legitimate Windows File API Abused to Block Local and SMB File Access — `2026-05-11-ghostlock-windows-file-lock-abuse.md`
- [x] **[MEDIUM]** GM Settles for $12.75M Over Unauthorized Sale of California Drivers' Data Under CCPA — `2026-05-11-gm-ccpa-settlement-drivers-data.md`
- [x] **[INFORMATIONAL]** FCC Eases Foreign Router Ban: Deadline Extensions and Scope Reductions for TP-Link and Others — `2026-05-11-fcc-foreign-router-ban-softened.md`

## Relevant (details)

### 1. Mini Shai-Hulud Worm Hits TanStack, Mistral AI, Guardrails AI and More
- **Source:** The Hacker News — https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `pypi`, `malware`, `appsec`, `devsecops`
- **Summary:** TeamPCP expanded the Shai-Hulud supply chain campaign to npm and PyPI packages from TanStack, UiPath, Mistral AI, OpenSearch, and Guardrails AI, injecting an obfuscated `router_init.js` profiling payload. The targeting of AI framework packages elevates risk for ML development pipelines.

### 2. Official Checkmarx Jenkins AST Plugin Backdoored with Infostealer
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/official-checkmarx-jenkins-package-compromised-with-infostealer/
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`, `appsec`, `devsecops`
- **Summary:** A rogue build of the official Checkmarx Jenkins AST plugin carrying an infostealer was published to the Jenkins Marketplace. Any pipeline that installed the malicious version should treat credentials and secrets as compromised and rotate immediately.

### 3. Instructure Pays Off ShinyHunters to Suppress 3.65TB Canvas LMS Data Leak
- **Source:** The Hacker News — https://thehackernews.com/2026/05/instructure-reaches-ransom-agreement.html
- **Severity:** high
- **Tags:** `data-breach`, `ransomware`
- **Summary:** Instructure reached a ransom "agreement" with ShinyHunters to suppress release of 3.65TB stolen from Canvas LMS systems at thousands of schools and universities. ShinyHunters has a track record of secondary data sales despite payments.

### 4. OpenAI Launches Daybreak: AI-Powered Vulnerability Detection and Patch Validation
- **Source:** The Hacker News — https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html
- **Severity:** high
- **Tags:** `openai`, `ai-launch`, `appsec`, `llm`, `vulnerability`
- **Summary:** OpenAI's Daybreak initiative layers frontier models and the Codex Security agent to build threat models, validate vulnerabilities, and automate patch suggestions — a direct competitor to Anthropic's Mythos-based security tooling.

### 5. Unit 42 Unpacks AD CS Escalation: Template Misconfigs, Shadow Credentials, and Detection Guidance
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/active-directory-certificate-services-exploitation/
- **Severity:** high
- **Tags:** `privilege-escalation`, `iam`, `vulnerability`, `appsec`
- **Summary:** Updated analysis of AD CS exploitation covering template misconfiguration and shadow credential abuse as escalation primitives, with behavioral detection patterns. AD CS escalation remains a top post-exploitation vector in enterprise environments.

### 6. Kaspersky: State of Ransomware 2026
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/state-of-ransomware-in-2026/119761/
- **Severity:** medium
- **Tags:** `ransomware`, `malware`
- **Summary:** Kaspersky's 2026 ransomware report highlights EDR-killing as a standard kill-chain component and a structural shift from file encryption to pure data-leak extortion. The encryption-free model bypasses backup-based recovery playbooks.

### 7. iOS 26.5 Rolls Out Default E2EE RCS Between iPhone and Android
- **Source:** The Hacker News — https://thehackernews.com/2026/05/ios-265-brings-default-end-to-end.html
- **Severity:** medium
- **Tags:** `apple`
- **Summary:** Apple released iOS 26.5 with E2EE RCS messaging enabled by default for cross-platform iPhone-to-Android messaging via MLS protocol. Closes the longstanding plaintext SMS gap for mixed-device enterprise environments.

### 8. GhostLock PoC: Windows File API Abused to Block Local and SMB File Access
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-ghostlock-tool-abuses-windows-api-to-block-file-access/
- **Severity:** medium
- **Tags:** `vulnerability`, `malware`, `microsoft`
- **Summary:** Researcher released GhostLock, a PoC abusing a legitimate Windows file-locking API to deny access to files without encryption — bypassing traditional ransomware behavioral detections. Could be used in destructive attacks or denial-of-service scenarios.

### 9. GM Settles for $12.75M Over CCPA Violations Selling Drivers' Data
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/legal/gm-agrees-to-1275m-california-settlement-over-sale-of-drivers-data/
- **Severity:** medium
- **Tags:** `data-breach`, `iam`
- **Summary:** California AG reached a $12.75M CCPA settlement with GM over selling precise driving behavior data to insurers without adequate consent. Landmark enforcement action against automotive telemetry with implications for all connected-product data monetization.

### 10. FCC Eases Foreign Router Ban with Deadline Extensions
- **Source:** Dark Reading — https://www.darkreading.com/endpoint-security/fcc-softens-foreign-router-ban
- **Severity:** informational
- **Tags:** `supply-chain`, `cloud-security`
- **Summary:** FCC pushed back compliance deadlines and eased scope restrictions for its foreign-manufactured router ban; the underlying ban remains in effect. Organizations planning hardware refreshes should continue on schedule.

## Skippable

- **Instructure/ShinyHunters agreement** — BleepingComputer. Duplicate of item #3 (THN has the 3.65TB detail).
- **Thinking Machines wants to build an AI that actually listens** — TechCrunch AI. AI startup product direction with no actual model or tool release.
- **Robinhood preps second retail venture IPO** — TechCrunch AI. Venture fund financial news; no security or AI substance.
- **Thoughts on GitLab's workforce reduction** — Simon Willison. Business/HR commentary; no technical security or AI-capability angle.
- **Building Blocks for Foundation Model Training and Inference on AWS** — Hugging Face Blog. No summary; generic cloud/ML infrastructure content.
- **OpenAI just released its answer to Claude Mythos** — The Verge AI. Duplicate of item #4 (Daybreak).
- **GM just laid off hundreds of IT workers to hire AI skills** — TechCrunch AI. Corporate HR restructuring; no security angle.
- **Here's what Mira Murati's AI company is up to** — The Verge AI. Duplicate of TechCrunch Thinking Machines item; no product released.
- **Navigating the Threat Landscape of the 2026 FIFA World Cup** — Flashpoint. Generic event security advisory without novel threat intelligence.
- **Texas sues Netflix over data practices** — The Record. Privacy lawsuit; limited technical substance for practitioners.
- **Tech Can't Stop These Threats — Your People Can** — Dark Reading. Opinion piece; no novel techniques or incidents.
- **Quoting James Shore** — Simon Willison. Commentary on AI maintenance costs; no news value.
