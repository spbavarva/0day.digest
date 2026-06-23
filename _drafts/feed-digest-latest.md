# Digest — 2026-06-23 PM

- Window: last 14h
- Raw items considered: 49
- Relevant: 20
- Skippable: 29

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** LastPass Confirms Data Breach Tied to Klue Supply Chain Attack — `2026-06-23-lastpass-data-breach-klue-supply-chain.md`
- [x] **[CRITICAL]** FortiBleed Attackers Use Golang Sniffer to Harvest 110 Million Credentials — `2026-06-23-fortibleed-credential-stealing-campaign.md`
- [x] **[CRITICAL]** CISA Adds Four Actively Exploited Vulnerabilities to KEV Catalog — `2026-06-23-cisa-kev-catalog-four-vulnerabilities.md`
- [x] **[HIGH]** Data Exposure Flaws Threaten Dify AI Platform Used by 1 Million Apps — `2026-06-23-dify-ai-platform-data-exposure-flaws.md`
- [x] **[HIGH]** Fake AI Agent Skill Bypassed Every Security Scanner, Reached 26,000 Agents — `2026-06-23-fake-ai-agent-skill-bypasses-scanners.md`
- [x] **[HIGH]** Eight-Year-Old Samsung KNOX Flaw Exposed Millions of Galaxy Devices to Kernel Attacks — `2026-06-23-samsung-knox-flaw-galaxy-kernel.md`
- [x] **[HIGH]** Siemens Patches OpenSSL Buffer Overflow Across Multiple Product Lines — `2026-06-23-siemens-openssl-buffer-overflow-rce.md`
- [x] **[HIGH]** Siemens SINEC INS Vulnerable to OS Command Injection and Path Traversal — `2026-06-23-siemens-sinec-ins-os-command-injection.md`
- [x] **[HIGH]** Public Exploits Available for Linux Kernel Flaws Affecting B&R Industrial Products — `2026-06-23-br-linux-kernel-vulnerabilities-poc.md`
- [x] **[HIGH]** FFmpeg PixelSmash Flaw Allows RCE on Video Players, Media Servers, NAS Appliances — `2026-06-23-ffmpeg-pixelsmash-rce-flaw.md`
- [x] **[HIGH]** Malicious npm Packages Impersonate PostCSS Tools to Deliver Windows RAT — `2026-06-23-malicious-npm-postcss-packages-rat.md`
- [x] **[MEDIUM]** New macOS ClickFix Campaign Uses Mounted DMGs to Push Infostealer — `2026-06-23-macos-clickfix-dmg-infostealer.md`
- [x] **[MEDIUM]** GitHub Hardens actions/checkout Against Pwn Request Attacks — `2026-06-23-github-actions-checkout-pwn-request-protection.md`
- [x] **[MEDIUM]** SocGholish Takedown Exposes Malicious Traffic Distribution System Used by Evil Corp — `2026-06-23-socgholish-takedown-tds-evil-corp.md`
- [x] **[MEDIUM]** WhatsApp Campaign Uses Fake Documents to Deliver VBScript and RMM Tools — `2026-06-23-whatsapp-vbscript-rmm-campaign.md`
- [x] **[INFORMATIONAL]** Five Eyes Agencies Warn AI Is Accelerating Cybersecurity Threats — `2026-06-23-five-eyes-ai-cybersecurity-threat-alert.md`
- [x] **[INFORMATIONAL]** Anthropic Launches Claude Tag, an Always-On Slack AI Teammate — `2026-06-23-anthropic-claude-tag-slack.md`
- [x] **[INFORMATIONAL]** Google Cloud Expands Confidential Computing for AI Workloads — `2026-06-23-google-cloud-confidential-computing-ai.md`
- [x] **[INFORMATIONAL]** Trump Order Sets 2030 Deadline for Federal Post-Quantum Crypto Migration — `2026-06-23-trump-eo-post-quantum-crypto-migration.md`
- [x] **[INFORMATIONAL]** OpenAI Refocuses Daybreak Cybersecurity Initiative on Patching Over Discovery — `2026-06-23-openai-daybreak-patching-focus.md`

## Relevant (details)

### 1. LastPass Confirms Data Breach Tied to Klue Supply Chain Attack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/lastpass-confirms-data-breach-in-klue-supply-chain-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `data-breach`
- **Slug:** `2026-06-23-lastpass-data-breach-klue-supply-chain`
- **Must-know:** yes
- **Summary:** LastPass confirmed hackers accessed customer data from its Salesforce environment after stealing OAuth tokens in the Klue supply chain attack disclosed earlier this month. It's a new confirmed downstream victim of the broader Klue compromise.

### 2. FortiBleed Attackers Use Golang Sniffer to Harvest 110 Million Credentials
- **Source:** Dark Reading — https://www.darkreading.com/cyberattacks-data-breaches/fortibleed-attackers-firewalls-credentials-stealers
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `malware`, `vulnerability`, `data-breach`
- **Slug:** `2026-06-23-fortibleed-credential-stealing-campaign`
- **Must-know:** yes
- **Summary:** A threat actor engineered a Golang-based sniffer to target 430,000 FortiGate firewalls and has captured 110 million credentials in an ongoing campaign. SecurityWeek separately attributes the activity to a Russian initial access broker.

### 3. CISA Adds Four Actively Exploited Vulnerabilities to KEV Catalog
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/alerts/2026/06/23/cisa-adds-four-known-exploited-vulnerabilities-catalog
- **Section:** Government / Advisory
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Slug:** `2026-06-23-cisa-kev-catalog-four-vulnerabilities`
- **Must-know:** yes
- **Summary:** CISA added four vulnerabilities to its KEV catalog based on evidence of active exploitation, covering a Lantronix EDS5000 code injection flaw and three Ubiquiti UniFi OS vulnerabilities. Federal agencies must remediate under BOD 26-04.

### 4. Data Exposure Flaws Threaten Dify AI Platform Used by 1 Million Apps
- **Source:** SecurityWeek — https://www.securityweek.com/data-exposure-flaws-threaten-dify-ai-platform-powering-over-1-million-apps/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `llm`, `privilege-escalation`, `cloud-security`
- **Slug:** `2026-06-23-dify-ai-platform-data-exposure-flaws`
- **Must-know:** no
- **Summary:** Flaws in Dify's multi-tenant cloud service could let attackers read other tenants' private chats, preview their documents, and reach internal APIs. Dify powers more than 1 million apps.

### 5. Fake AI Agent Skill Bypassed Every Security Scanner, Reached 26,000 Agents
- **Source:** The Hacker News — https://thehackernews.com/2026/06/fake-ai-agent-skill-passed-security.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `supply-chain`, `ai-safety`
- **Slug:** `2026-06-23-fake-ai-agent-skill-bypasses-scanners`
- **Must-know:** no
- **Summary:** Security firm AIR pushed a fake AI agent skill through a marketplace and an Instagram ad, reaching roughly 26,000 agents including corporate accounts. Every scanner tested against it marked it safe.

### 6. Eight-Year-Old Samsung KNOX Flaw Exposed Millions of Galaxy Devices to Kernel Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/eight-year-old-samsung-knox-flaw-exposed-millions-of-galaxy-devices-to-kernel-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`
- **Slug:** `2026-06-23-samsung-knox-flaw-galaxy-kernel`
- **Must-know:** no
- **Summary:** A high-severity use-after-free vulnerability in Samsung's KNOX framework affected Galaxy devices from the S9 through S25, exposing millions of devices to kernel-level attacks.

### 7. Siemens Patches OpenSSL Buffer Overflow Across Multiple Product Lines
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-174-03
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `vulnerability`, `rce`
- **Slug:** `2026-06-23-siemens-openssl-buffer-overflow-rce`
- **Must-know:** no
- **Summary:** A stack-based OpenSSL buffer overflow (CVE-2025-15467) affects multiple Siemens product lines, including its AI Lightweight Inference Server, with potential for DoS or remote code execution.

### 8. Siemens SINEC INS Vulnerable to OS Command Injection and Path Traversal
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-174-04
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `vulnerability`, `rce`
- **Slug:** `2026-06-23-siemens-sinec-ins-os-command-injection`
- **Must-know:** no
- **Summary:** Siemens SINEC INS versions before V1.0 SP2 Update 6 carry multiple flaws including an OS command injection rated CVSS v3 8.8, plus path traversal and privilege issues.

### 9. Public Exploits Available for Linux Kernel Flaws Affecting B&R Industrial Products
- **Source:** CISA Alerts — https://www.cisa.gov/news-events/ics-advisories/icsa-26-174-06
- **Section:** Government / Advisory
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`
- **Slug:** `2026-06-23-br-linux-kernel-vulnerabilities-poc`
- **Must-know:** no
- **Summary:** B&R industrial products ship with Linux kernel versions affected by known privilege-escalation vulnerabilities, and public proof-of-concept exploits are already available.

### 10. FFmpeg PixelSmash Flaw Allows RCE on Video Players, Media Servers, NAS Appliances
- **Source:** SecurityWeek — https://www.securityweek.com/ffmpeg-pixelsmash-flaw-allows-rce-on-video-players-media-servers-nas-appliances/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `rce`
- **Slug:** `2026-06-23-ffmpeg-pixelsmash-rce-flaw`
- **Must-know:** no
- **Summary:** A flaw dubbed PixelSmash in FFmpeg's libavcodec library lets attackers execute code via crafted media files, affecting any application that embeds the widely-used library.

### 11. Malicious npm Packages Impersonate PostCSS Tools to Deliver Windows RAT
- **Source:** The Hacker News — https://thehackernews.com/2026/06/malicious-npm-packages-pose-as-postcss.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `malware`
- **Slug:** `2026-06-23-malicious-npm-postcss-packages-rat`
- **Must-know:** no
- **Summary:** Malicious npm packages impersonating PostCSS tooling (including postcss-minify-selector and postcss-minify-selector-parser) were found delivering a Windows RAT, published by a single account over the past month.

### 12. New macOS ClickFix Campaign Uses Mounted DMGs to Push Infostealer
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-macos-clickfix-attack-silently-mounts-dmgs-to-push-infostealer/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `2026-06-23-macos-clickfix-dmg-infostealer`
- **Must-know:** no
- **Summary:** A new macOS ClickFix campaign tricks users into running Terminal commands that silently download, mount, and launch an info-stealer from a malicious DMG file.

### 13. GitHub Hardens actions/checkout Against Pwn Request Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/06/github-updates-actionscheckout-to-block.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `supply-chain`, `github`, `devsecops`
- **Slug:** `2026-06-23-github-actions-checkout-pwn-request-protection`
- **Must-know:** no
- **Summary:** GitHub updated its official actions/checkout action to block "pwn request" attacks that abuse the pull_request_target trigger, effective June 18, 2026.

### 14. SocGholish Takedown Exposes Malicious Traffic Distribution System Used by Evil Corp
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/socgholish-takedown-malicious-tds-threats
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `2026-06-23-socgholish-takedown-tds-evil-corp`
- **Must-know:** no
- **Summary:** A takedown targeted SocGholish infrastructure, a malware framework using traffic distribution systems to provide initial access for cybercrime groups including Evil Corp.

### 15. WhatsApp Campaign Uses Fake Documents to Deliver VBScript and RMM Tools
- **Source:** The Hacker News — https://thehackernews.com/2026/06/whatsapp-vbscript-campaign-uses-fake.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `phishing`
- **Slug:** `2026-06-23-whatsapp-vbscript-rmm-campaign`
- **Must-know:** no
- **Summary:** An active campaign distributes malicious VBScript files via WhatsApp direct messages disguised as documents, installing legitimate RMM software for malicious use across multiple countries.

### 16. Five Eyes Agencies Warn AI Is Accelerating Cybersecurity Threats
- **Source:** The Record (Recorded Future) — https://therecord.media/five-eyes-alert-artificial-intelligence
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ai-safety`, `llm`
- **Slug:** `2026-06-23-five-eyes-ai-cybersecurity-threat-alert`
- **Must-know:** no
- **Summary:** Five Eyes intelligence agencies issued a joint alert warning that AI is accelerating cybersecurity threats on a "months, not years" timeline.

### 17. Anthropic Launches Claude Tag, an Always-On Slack AI Teammate
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/23/anthropics-claude-tag-is-learning-your-company-one-slack-message-at-a-time/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `anthropic`, `ai-launch`
- **Slug:** `2026-06-23-anthropic-claude-tag-slack`
- **Must-know:** no
- **Summary:** Anthropic launched Claude Tag, an always-on AI teammate for Slack, positioned as a way to capture organizational context and institutional knowledge over time.

### 18. Google Cloud Expands Confidential Computing for AI Workloads
- **Source:** Google Cloud Security — https://cloud.google.com/blog/products/identity-security/verifiable-trust-in-the-ai-era-whats-new-in-confidential-computing/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `cloud-security`, `gcp`, `ai-safety`
- **Slug:** `2026-06-23-google-cloud-confidential-computing-ai`
- **Must-know:** no
- **Summary:** Google Cloud expanded Confidential Computing capabilities for AI workloads, scaling hardware-based TEEs globally to protect data used in AI inference and fine-tuning.

### 19. Trump Order Sets 2030 Deadline for Federal Post-Quantum Crypto Migration
- **Source:** The Hacker News — https://thehackernews.com/2026/06/trump-order-sets-2030-deadline-for.html
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `post-quantum-crypto`
- **Slug:** `2026-06-23-trump-eo-post-quantum-crypto-migration`
- **Must-know:** no
- **Summary:** An executive order signed June 22 sets hard deadlines for federal agencies to migrate high-value systems to post-quantum cryptography: key establishment by end of 2030, signatures by end of 2031.

### 20. OpenAI Refocuses Daybreak Cybersecurity Initiative on Patching Over Discovery
- **Source:** SecurityWeek — https://www.securityweek.com/openai-refocuses-cybersecurity-efforts-on-patching-over-discovery/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `openai`, `ai-safety`, `devsecops`
- **Slug:** `2026-06-23-openai-daybreak-patching-focus`
- **Must-know:** no
- **Summary:** OpenAI expanded its Daybreak cybersecurity initiative with new tools and partnerships, shifting emphasis toward patching known issues over discovering new ones.

## Skippable

- **AI Threat Report: How AI Is Used Across Illicit Communities** — Flashpoint. Recurring monthly report with no specific new finding; reads as a blog teaser.
- **Feds seize alleged cyber-scam infrastructure connected to Southeast Asian company** — The Record. Law enforcement seizure action, no new technical detail for practitioners.
- **Dragos Unveils AI for OT Security** — SecurityWeek. Vendor product announcement (EmberAI) with thin technical detail, reads as a press release.
- **Trump directs federal agencies to protect US data from quantum threats** — The Record. Duplicate coverage of the PQC executive order; see The Hacker News item above.
- **How GPT-5 helped immunologist Derya Unutmaz solve a 3-year-old mystery** — OpenAI Blog. Anecdotal marketing case study, no new model capability or technical news.
- **Why corporate AI super PACs spent $27 million on a local election** — The Verge AI. Opinion/newsletter content, low signal for a security/AI practitioner feed.
- **Scattered Spider Hackers Plead Guilty on Day 1 of Trial** — Krebs on Security. Guilty plea with no new TTPs or IOCs beyond what's already known.
- **Something's off with Midjourney's pivot to body scanners** — The Verge AI. Product opinion piece, no security angle.
- **Scattered Spider members plead guilty to hacking Transport for London** — BleepingComputer. Duplicate coverage of the same guilty plea.
- **Compromise kids online safety bill unveiled by House leaders, with key omission** — The Record. General social-media policy, not closely tied to AI/security infrastructure.
- **The Fitbit Air takes a smarter approach to the AI health dumpster fire** — The Verge AI. Consumer product review, no security angle.
- **The Exploit Doesn't Exist. You Can Still Prove It Works Against You** — BleepingComputer/Picus Security. Vendor explainer content, no specific incident.
- **Webinar: Why email security teams are drowning in alerts** — BleepingComputer. Vendor webinar promotion.
- **4 days left to save up to $190 on TechCrunch Founder Summit 2026** — TechCrunch AI. Event marketing.
- **Sony's AI Camera Assistant is exactly as bad as it looks** — The Verge AI. Consumer product review, no security angle.
- **Two Scattered Spider members plead guilty over cyberattack that crippled London transit** — The Record. Duplicate coverage of the same guilty plea.
- **Fika Jobs raises $4M to build a video-first hiring platform** — TechCrunch AI. Startup funding news, no security/AI substance.
- **Meta launches cheaper smart glasses without Ray-Ban** — The Verge AI. Consumer hardware launch, no security angle.
- **Build real agentic apps using CUGA** — Hugging Face Blog. Feed summary was empty/truncated; insufficient content to draft a factual post without fabricating detail.
- **CISO Conversations: Carl Froggett – Combining CISO and CIO at Deep Instinct** — SecurityWeek. Profile/career content, low actionable signal.
- **Algerian Man Extradited to US for Running Cybercrime Marketplaces** — SecurityWeek. Law enforcement action, no new TTPs.
- **Hubbell Aclara Metrum Cellular Web Interface** — CISA Alerts. Routine ICS advisory (CVSS 7.5, missing auth), no active exploitation.
- **Siemens WinCC Certificate Manager** — CISA Alerts. Routine ICS advisory, narrow scope (key material exposure).
- **ABB Freelance Security Lock** — CISA Alerts. Routine ICS advisory, narrow scope, depends on local config.
- **Siemens SIPROTEC 5 Using DIGSI5 Protocol** — CISA Alerts. Routine ICS advisory requiring authenticated access, narrow scope.
- **Agentic AI: The Weapon That No Longer Needs a Warrior** — The Hacker News. Philosophical opinion piece, no concrete news.
- **Russian Initial Access Broker Behind FortiBleed Campaign** — SecurityWeek. Duplicate coverage of the FortiBleed campaign; attribution detail folded into the Dark Reading item above.
- **Canadian Electricity Provider London Hydro Discloses Data Breach** — SecurityWeek. Breach disclosure without technical substance or affected-user count.
- **Trump Signs Executive Order Accelerating Post-Quantum Cryptography Migration** — SecurityWeek. Duplicate coverage of the PQC executive order; see The Hacker News item above.
