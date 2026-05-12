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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `pypi`, `malware`, `appsec`, `devsecops`
- **Slug:** `2026-05-12-mini-shai-hulud-supply-chain-npm-pypi`
- **Must-know:** yes
- **Summary:** TeamPCP expanded their Shai-Hulud supply chain campaign to npm and PyPI packages from TanStack, UiPath, Mistral AI, OpenSearch, and Guardrails AI, injecting an obfuscated `router_init.js` profiling payload. The cross-ecosystem targeting of AI framework packages elevates risk for ML development pipelines and CI/CD environments.

### 2. Official Checkmarx Jenkins AST Plugin Backdoored with Infostealer
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/official-checkmarx-jenkins-package-compromised-with-infostealer/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`, `appsec`, `devsecops`, `github`
- **Slug:** `2026-05-11-checkmarx-jenkins-plugin-infostealer`
- **Must-know:** yes
- **Summary:** A rogue build of the official Checkmarx Jenkins AST plugin carrying an infostealer was published to the Jenkins Marketplace over the weekend. Any pipeline that installed the malicious version should treat credentials and secrets as compromised and rotate immediately.

### 3. Instructure Pays Off ShinyHunters to Suppress 3.65TB Canvas LMS Data Leak
- **Source:** The Hacker News — https://thehackernews.com/2026/05/instructure-reaches-ransom-agreement.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `ransomware`
- **Slug:** `2026-05-12-instructure-canvas-shinyhunters-ransom`
- **Must-know:** no
- **Summary:** Instructure confirmed it reached an "agreement" (implied payment) with ShinyHunters to prevent release of 3.65TB stolen from Canvas LMS systems serving thousands of schools and universities. ShinyHunters has a track record of secondary data sales despite ransom payments.

### 4. OpenAI Launches Daybreak: AI-Powered Vulnerability Detection and Patch Validation
- **Source:** The Hacker News — https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `openai`, `ai-launch`, `appsec`, `llm`, `vulnerability`
- **Slug:** `2026-05-12-openai-daybreak-vulnerability-detection`
- **Must-know:** no
- **Summary:** OpenAI's Daybreak initiative uses frontier models and the Codex Security agent to build threat models from codebases, identify attack paths, validate vulnerabilities, and automate patch suggestions. It positions OpenAI directly in competition with Anthropic's Mythos-based security tooling.

### 5. Unit 42 Unpacks AD CS Escalation: Template Misconfigs, Shadow Credentials, and Detection Guidance
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/active-directory-certificate-services-exploitation/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `privilege-escalation`, `iam`, `vulnerability`, `appsec`
- **Slug:** `2026-05-11-adcs-escalation-shadow-credentials`
- **Must-know:** no
- **Summary:** Unit 42 published updated analysis of AD CS exploitation techniques — template misconfigurations and shadow credential abuse — along with behavioral detection patterns. AD CS escalation paths remain a top post-exploitation vector in enterprise environments.

### 6. Kaspersky: State of Ransomware 2026
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/state-of-ransomware-in-2026/119761/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** medium
- **Tags:** `ransomware`, `malware`, `vulnerability`
- **Slug:** `2026-05-12-state-of-ransomware-2026`
- **Must-know:** no
- **Summary:** Kaspersky GReAT's 2026 ransomware report calls out EDR-killing tooling as a standard kill-chain component and a notable shift from file encryption to pure data-leak extortion. The encryption-free extortion model bypasses recovery playbooks centered on backup restoration.

### 7. iOS 26.5 Rolls Out Default E2EE RCS Between iPhone and Android
- **Source:** The Hacker News — https://thehackernews.com/2026/05/ios-265-brings-default-end-to-end.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `apple`, `microsoft`
- **Slug:** `2026-05-12-ios-265-e2ee-rcs`
- **Must-know:** no
- **Summary:** Apple released iOS 26.5 with E2EE RCS messaging enabled by default for iPhone-to-Android cross-platform messaging using the MLS protocol. This closes a longstanding plaintext gap for enterprises managing mixed-device environments.

### 8. GhostLock PoC: Windows File API Abused to Block Local and SMB File Access
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-ghostlock-tool-abuses-windows-api-to-block-file-access/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `malware`, `microsoft`
- **Slug:** `2026-05-11-ghostlock-windows-file-lock-abuse`
- **Must-know:** no
- **Summary:** A researcher released GhostLock, a PoC abusing a legitimate Windows file-locking API to deny access to local and SMB-hosted files without file modification or encryption — meaning traditional ransomware detections won't trigger. The technique could be incorporated into destructive attacks or denial-of-service campaigns.

### 9. GM Settles for $12.75M Over CCPA Violations Selling Drivers' Data
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/legal/gm-agrees-to-1275m-california-settlement-over-sale-of-drivers-data/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`, `iam`
- **Slug:** `2026-05-11-gm-ccpa-settlement-drivers-data`
- **Must-know:** no
- **Summary:** California AG settled with GM over selling precise driving behavior data to insurance companies without adequate consumer consent under CCPA. This is a landmark CCPA enforcement action against automotive telemetry, with implications for all connected-product data monetization practices.

### 10. FCC Eases Foreign Router Ban with Deadline Extensions
- **Source:** Dark Reading — https://www.darkreading.com/endpoint-security/fcc-softens-foreign-router-ban
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `supply-chain`, `cloud-security`
- **Slug:** `2026-05-11-fcc-foreign-router-ban-softened`
- **Must-know:** no
- **Summary:** The FCC pushed back compliance deadlines and eased some scope restrictions for its foreign-manufactured router ban, though the underlying national security rationale and ban remain in effect. Organizations already planning router hardware refreshes should stay on their existing schedules.

## Skippable

- **Instructure/ShinyHunters agreement** — BleepingComputer. Duplicate coverage of item #3 (The Hacker News version has more detail, including the 3.65TB figure).
- **Thinking Machines wants to build an AI that actually listens** — TechCrunch AI. AI startup product direction announcement with no actual model or tool release to evaluate.
- **Robinhood preps second retail venture IPO** — TechCrunch AI. Venture fund financial news; no AI or security substance.
- **Thoughts on GitLab's workforce reduction** — Simon Willison. Business/HR restructuring commentary; no technical security or AI-capability angle.
- **Building Blocks for Foundation Model Training and Inference on AWS** — Hugging Face Blog. No summary provided; generic cloud/ML infrastructure content.
- **OpenAI just released its answer to Claude Mythos** — The Verge AI. Duplicate of item #4 (The Hacker News Daybreak coverage).
- **GM just laid off hundreds of IT workers to hire AI skills** — TechCrunch AI. Corporate restructuring/HR news; duplicate GM story with no security angle.
- **Here's what Mira Murati's AI company is up to** — The Verge AI. Duplicate of TechCrunch Thinking Machines item; no product released.
- **Navigating the Threat Landscape of the 2026 FIFA World Cup** — Flashpoint. Generic pre-event security advisory without novel threat intelligence or IOCs.
- **Texas sues Netflix over data practices** — The Record. Privacy lawsuit announcement; limited technical security substance for practitioners.
- **Tech Can't Stop These Threats — Your People Can** — Dark Reading. Opinion/advice piece without news value; no novel techniques or incidents reported.
- **Quoting James Shore** — Simon Willison. Commentary on AI maintenance costs; no news value.
