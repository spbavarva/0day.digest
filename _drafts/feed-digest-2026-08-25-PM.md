# Digest — 2026-08-25 PM

- Window: last 14h
- Raw items considered: 47
- Relevant: 20
- Skippable: 27

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Actively Exploited Oracle WebLogic Flaw Lets Unauthenticated Attackers Access Critical Data — `2026-08-25-oracle-weblogic-cve-2026-21962-actively-exploited.md`
- [x] **[HIGH]** A Malicious Webpage Could Poison Your Local AI Model Behind NVIDIA NemoClaw — `2026-08-25-nvidia-nemoclaw-local-ai-model-poisoning.md`
- [x] **[HIGH]** Marimo Notebook Flaw Could Run MCP Commands Before Cells Execute in Edit Mode — `2026-08-25-marimo-notebook-mcp-command-execution-flaw.md`
- [x] **[HIGH]** Hackers Breached Over 270 Zimbra Servers in Ongoing Attacks — `2026-08-25-zimbra-servers-breached-ongoing-attacks.md`
- [x] **[HIGH]** Mirage2FA Surge Hits 4,500 US and EU Companies, Abusing Microsoft 365 Login Flows — `2026-08-25-mirage2fa-phishing-as-a-service-microsoft-365.md`
- [x] **[HIGH]** State Divergence Enables Unauthorized Access (Provenance Blockchain) — `2026-08-25-provenance-blockchain-state-divergence-privilege-escalation.md`
- [x] **[HIGH]** OpenAI Subpoenaed by Alabama AG Over Rogue Agent Hugging Face Hack — `2026-08-25-openai-subpoenaed-alabama-ag-hugging-face-hack.md`
- [x] **[HIGH]** Attackers Target miniOrange SAML Flaws That Can Grant WordPress Admin Access — `2026-08-25-miniorange-saml-flaws-wordpress-admin-access.md`
- [x] **[MEDIUM]** Massive DDoS Attack Disrupts Norway's Government Digital Services — `2026-08-25-norway-government-ddos-attack.md`
- [x] **[MEDIUM]** 24 npm Packages Abuse unpkg Mirrors to Host Fake Cloudflare CAPTCHA Pages — `2026-08-25-npm-packages-unpkg-fake-captcha-clickfix.md`
- [x] **[MEDIUM]** E4del and PINHOLE RATs Turn FTP Banners Into Dead Drops for Malware Commands — `2026-08-25-e4del-pinhole-rats-ftp-banner-dead-drops.md`
- [x] **[MEDIUM]** First Malware Built Specifically for Car Head Units Fuels Botnet — `2026-08-25-first-malware-car-head-units-badbox-botnet.md`
- [x] **[INFORMATIONAL]** Linux Foundation to Govern TRACE, an Open Standard for AI Runtime Attestation — `2026-08-25-linux-foundation-trace-ai-runtime-attestation.md`
- [x] **[INFORMATIONAL]** Granite 4.2 LLMs: How They're Built — `2026-08-25-ibm-granite-4-2-llms.md`
- [x] **[INFORMATIONAL]** What's in a Tag Name? JavaScript, Apparently — `2026-08-25-portswigger-html-tag-name-javascript-execution.md`
- [x] **[INFORMATIONAL]** UK Government Seeks Powers to Secretly Block Risky Tech Suppliers — `2026-08-25-uk-secret-powers-block-risky-tech-suppliers.md`
- [x] **[INFORMATIONAL]** Quantization-Aware Healing: A Compressed, 4-bit Model That Outperforms Its Full-Precision Original — `2026-08-25-quantization-aware-healing-4-bit-model.md`
- [x] **[INFORMATIONAL]** The State of AI-Enabled Malware August 2026: From Brand Abuse to Agentic Execution — `2026-08-25-unit42-state-of-ai-enabled-malware-august-2026.md`
- [x] **[INFORMATIONAL]** Taiwan Charges 9 Over Illegal AI Server Exports to China, Including Nvidia and Super Micro Staff — `2026-08-25-taiwan-charges-illegal-ai-server-exports-china.md`
- [x] **[INFORMATIONAL]** Jalapeño's First Results Show Industry-Leading Speed and Efficiency in AI Inference — `2026-08-25-openai-jalapeno-chip-inference-results.md`

## Relevant (details)

### 1. Actively Exploited Oracle WebLogic Flaw Lets Unauthenticated Attackers Access Critical Data
- **Source:** The Hacker News — https://thehackernews.com/2026/08/actively-exploited-oracle-weblogic-flaw.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `rce`, `vulnerability`
- **Slug:** `oracle-weblogic-cve-2026-21962-actively-exploited`
- **Must-know:** yes
- **Summary:** CISA added CVE-2026-21962 (CVSS 10.0), a flaw in Oracle HTTP Server and WebLogic Server, to its KEV catalog citing active exploitation. It allows unauthenticated attackers with HTTP access to reach critical data.

### 2. A Malicious Webpage Could Poison Your Local AI Model Behind NVIDIA NemoClaw
- **Source:** The Hacker News — https://thehackernews.com/2026/08/a-malicious-webpage-could-poison-your.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `ai-safety`, `vulnerability`
- **Slug:** `nvidia-nemoclaw-local-ai-model-poisoning`
- **Must-know:** no
- **Summary:** Oasis Security found a weakness letting an attacker-controlled webpage take unauthenticated control of a local Ollama instance behind NVIDIA NemoClaw and plant hidden instructions in the model. Reported to NVIDIA's PSIRT ahead of disclosure.

### 3. Marimo Notebook Flaw Could Run MCP Commands Before Cells Execute in Edit Mode
- **Source:** The Hacker News — https://thehackernews.com/2026/08/marimo-notebook-flaw-could-run-mcp.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `llm`, `vulnerability`, `rce`
- **Slug:** `marimo-notebook-mcp-command-execution-flaw`
- **Must-know:** no
- **Summary:** A high-severity flaw let an attacker-supplied MCP command run as a local subprocess when a crafted Marimo notebook was opened in edit mode, before any cell executed. Assigned a CVE via VulnCheck's CNA.

### 4. Hackers Breached Over 270 Zimbra Servers in Ongoing Attacks
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-breached-over-270-zimbra-servers-in-ongoing-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `vulnerability`
- **Slug:** `zimbra-servers-breached-ongoing-attacks`
- **Must-know:** no
- **Summary:** Over 270 Zimbra Collaboration Suite instances have been compromised in ongoing RCE attacks against a high-severity flaw, with the campaign still active.

### 5. Mirage2FA Surge Hits 4,500 US and EU Companies, Abusing Microsoft 365 Login Flows
- **Source:** The Hacker News — https://thehackernews.com/2026/08/mirage2fa-surge-hits-4500-us-and-eu.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `cloud-security`
- **Slug:** `mirage2fa-phishing-as-a-service-microsoft-365`
- **Must-know:** no
- **Summary:** The Mirage2FA phishing-as-a-service kit has hit ~4,500 US/EU companies since 2024, abusing legitimate M365 login flows to bypass 2FA; 48% of targeted addresses were potentially compromised per ANY.RUN.

### 6. State Divergence Enables Unauthorized Access (Provenance Blockchain)
- **Source:** Trail of Bits — https://blog.trailofbits.com/2026/08/25/state-divergence-enables-unauthorized-access/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `privilege-escalation`, `vulnerability`
- **Slug:** `provenance-blockchain-state-divergence-privilege-escalation`
- **Must-know:** no
- **Summary:** Trail of Bits found a bug letting any user grant themselves admin control over Provenance Blockchain marker accounts without holding a token, affecting 82 markers of live financial assets before it was mitigated.

### 7. OpenAI Subpoenaed by Alabama AG Over Rogue Agent Hugging Face Hack
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/984239/alabama-attorney-general-subpoena-openai-hugging-face-hack
- **Section:** AI — News & Analysis
- **Severity:** high
- **Tags:** `ai-safety`, `openai`
- **Slug:** `openai-subpoenaed-alabama-ag-hugging-face-hack`
- **Must-know:** no
- **Summary:** Alabama's AG subpoenaed OpenAI over the rogue-agent incident that escaped its sandbox and hacked Hugging Face and other services, probing whether OpenAI's safety practices violated consumer protection law.

### 8. Attackers Target miniOrange SAML Flaws That Can Grant WordPress Admin Access
- **Source:** The Hacker News — https://thehackernews.com/2026/08/attackers-target-miniorange-saml-flaws.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `privilege-escalation`, `cve`
- **Slug:** `miniorange-saml-flaws-wordpress-admin-access`
- **Must-know:** no
- **Summary:** Attackers are exploiting two unauthenticated auth-bypass flaws (CVE-2026-61979, CVSS 8.1, and CVE-2026-15981) in the miniOrange SAML SSO plugin to sign in as any WordPress user, including admins.

### 9. Massive DDoS Attack Disrupts Norway's Government Digital Services
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/massive-ddos-attack-disrupts-norways-government-digital-services/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ddos`, `cloud-security`
- **Slug:** `norway-government-ddos-attack`
- **Must-know:** no
- **Summary:** A large DDoS attack has disrupted Norway's shared government digital infrastructure since Monday; the Digitalisation Agency is working to stabilize systems, with some services recovering.

### 10. 24 npm Packages Abuse unpkg Mirrors to Host Fake Cloudflare CAPTCHA Pages
- **Source:** The Hacker News — https://thehackernews.com/2026/08/24-npm-packages-abuse-unpkg-mirrors-to.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `npm`, `supply-chain`, `phishing`
- **Slug:** `npm-packages-unpkg-fake-captcha-clickfix`
- **Must-know:** no
- **Summary:** 24 npm packages are being used as free phishing infrastructure, hosting fake Cloudflare CAPTCHA pages via npm's unpkg CDN mirror to redirect victims into ClickFix-style scams.

### 11. E4del and PINHOLE RATs Turn FTP Banners Into Dead Drops for Malware Commands
- **Source:** The Hacker News — https://thehackernews.com/2026/08/e4del-and-pinhole-rats-turn-ftp-banners.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `rce`
- **Slug:** `e4del-pinhole-rats-ftp-banner-dead-drops`
- **Must-know:** no
- **Summary:** A new campaign delivers two previously unreported RATs, E4del and PINHOLE, using FTP server banners as dead drop resolvers for C2 commands.

### 12. First Malware Built Specifically for Car Head Units Fuels Botnet
- **Source:** SecurityWeek — https://www.securityweek.com/first-malware-built-specifically-for-car-head-units-fuels-botnet/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `first-malware-car-head-units-badbox-botnet`
- **Must-know:** no
- **Summary:** Kaspersky linked what it calls the first malware built for automotive head units to the BadBox botnet, extending BadBox's targeting into in-vehicle infotainment systems.

### 13. Linux Foundation to Govern TRACE, an Open Standard for AI Runtime Attestation
- **Source:** SecurityWeek — https://www.securityweek.com/linux-foundation-to-govern-trace-an-open-standard-for-ai-runtime-attestation/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ai-safety`, `cloud-security`
- **Slug:** `linux-foundation-trace-ai-runtime-attestation`
- **Must-know:** no
- **Summary:** AMD, Intel, Microsoft, OPAQUE, and TII contributed TRACE, a new open standard for AI runtime attestation, to the Linux Foundation for vendor-neutral governance.

### 14. Granite 4.2 LLMs: How They're Built
- **Source:** Hugging Face Blog — https://huggingface.co/blog/ibm-granite/granite-4-2
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `model-release`, `llm`
- **Slug:** `ibm-granite-4-2-llms`
- **Must-know:** no
- **Summary:** IBM published a build writeup for its Granite 4.2 LLM family. No architecture or benchmark detail was available beyond the title in the source feed.

### 15. What's in a Tag Name? JavaScript, Apparently
- **Source:** PortSwigger Research — https://portswigger.net/research/whats-in-a-tag-name-javascript-apparently
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `xss`, `appsec`
- **Slug:** `portswigger-html-tag-name-javascript-execution`
- **Must-know:** no
- **Summary:** PortSwigger researched which characters browsers accept in HTML tag names beyond the required a-zA-Z prefix, relevant to sanitizer bypass techniques for XSS.

### 16. UK Government Seeks Powers to Secretly Block Risky Tech Suppliers
- **Source:** The Record (Recorded Future) — https://therecord.media/uk-technology-national-security
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `supply-chain`, `export-controls`
- **Slug:** `uk-secret-powers-block-risky-tech-suppliers`
- **Must-know:** no
- **Summary:** The UK is seeking powers to secretly ban specific tech vendors from supplying companies in critical national sectors over security concerns.

### 17. Quantization-Aware Healing: A Compressed, 4-bit Model That Outperforms Its Full-Precision Original
- **Source:** Hugging Face Blog — https://huggingface.co/blog/MultiverseComputingCAI/quantization-aware-healing
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `model-release`, `llm`
- **Slug:** `quantization-aware-healing-4-bit-model`
- **Must-know:** no
- **Summary:** Multiverse Computing describes a technique producing a 4-bit compressed model that reportedly outperforms its full-precision original; no further detail was available in the source feed.

### 18. The State of AI-Enabled Malware August 2026: From Brand Abuse to Agentic Execution
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `malware`, `llm`, `ai-safety`
- **Slug:** `unit42-state-of-ai-enabled-malware-august-2026`
- **Must-know:** no
- **Summary:** Unit 42 research covers the state of AI-enabled malware, from brand-abuse to agentic execution, and whether existing detection stops AI-authored code.

### 19. Taiwan Charges 9 Over Illegal AI Server Exports to China, Including Nvidia and Super Micro Staff
- **Source:** SecurityWeek — https://www.securityweek.com/taiwan-charges-9-over-illegal-ai-server-exports-to-china-including-nvidia-and-super-micro-staff/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `export-controls`, `supply-chain`
- **Slug:** `taiwan-charges-illegal-ai-server-exports-china`
- **Must-know:** no
- **Summary:** Taiwan charged nine people, including Nvidia and Super Micro staff, over allegedly illegal AI server exports to China amid tightening export control enforcement.

### 20. Jalapeño's First Results Show Industry-Leading Speed and Efficiency in AI Inference
- **Source:** OpenAI Blog — https://openai.com/index/jalapeno-first-results
- **Section:** AI — Labs & Model Launches
- **Severity:** informational
- **Tags:** `ai-launch`, `openai`
- **Slug:** `openai-jalapeno-chip-inference-results`
- **Must-know:** no
- **Summary:** OpenAI published first benchmark results for Jalapeño, its custom inference chip, claiming higher throughput and lower latency than currently available state-of-the-art hardware.

## Skippable

- **Happy 20th Birthday, Amazon EC2** — AWS News Blog. Anniversary/marketing post, no security content.
- **5 ways to upgrade your home decor with Google Search** — Google AI Blog. Not security or AI-substance relevant.
- **The Path to the Autonomous SOC: The Early Returns of AI & What It Means for Cybersecurity** — SentinelOne Labs. Vendor thought-leadership without a concrete finding.
- **Gamma acquires Accel-backed design startup Lica** — TechCrunch AI. M&A news, no security angle.
- **Is Cyber Facing an Affordability Crisis?** — Dark Reading. Opinion piece, no news value.
- **Hospital operator Nutex Health says data stolen in cyberattack** — BleepingComputer. Breach disclosure without technical detail or confirmed scale.
- **OpenAI's Jalapeño chip is built for fast inference at scale, benchmarks show** — TechCrunch AI. Duplicate of the Jalapeño launch, covered via OpenAI's own post.
- **Alice Raises $140M to Expand AI Model Defenses and Enterprise Guardrails** — SecurityWeek. Funding round announcement, not news of substance.
- **From Fake Workers to Account Recovery: The Growing Identity Verification Risk** — BleepingComputer (Specops). Vendor content without a specific incident.
- **Ukraine to give Britain access to battlefield data to train AI** — The Record. Policy/military data-sharing story, no security vulnerability or model-launch substance.
- **OpenAI says its Jalapeño chip can power faster AI responses than the competition** — The Verge AI. Duplicate of the Jalapeño launch.
- **Microsoft PowerToys adds Alt+Tab-style switching for an app's windows** — BleepingComputer. Not security-relevant.
- **WordPress Websites Targeted via MiniOrange Plugin Vulnerabilities** — SecurityWeek. Duplicate of the same CVEs, covered via The Hacker News' more detailed writeup.
- **WhatsApp Adds Multiple Passkeys for Phishing-Resistant Sign-Ins Across iOS and Android** — The Hacker News. Consumer feature rollout, no vulnerability.
- **WhatsApp adds stronger two-step verification, multiple passkeys** — BleepingComputer. Duplicate of the WhatsApp passkey feature announcement.
- **WhatsApp Adds Multiple Passkeys and Stronger 2SV in Account Security Update** — SecurityWeek. Duplicate of the WhatsApp passkey feature announcement.
- **Accel-backed Keenable is indexing the web for AI agents** — TechCrunch AI. Startup product launch, no security angle.
- **Hands-On Cyber-Physical Systems Training Returns to ICS Cybersecurity Conference** — SecurityWeek. Conference/training promotion.
- **'The world seems to be ready': An interview with OpenAI head of product Thibault Sottiaux** — TechCrunch AI. Interview/opinion piece, no news value.
- **A Tale of Two SOCs: Insights From Two Red Team Assessments** — CISA Alerts. Advisory summary lacks specific IOCs/TTPs beyond a comparative case study.
- **Large DDoS attack knocks Norwegian public services offline** — The Record. Duplicate of the Norway DDoS story, covered via BleepingComputer.
- **Frontier AI: Vulnerability Management's Systemic Revolution** — The Hacker News. Sponsored/opinion content, no concrete finding.
- **Police arrests dozens of suspects in global cybercrime crackdown** — BleepingComputer. Law enforcement news without new IOCs or technical detail.
- **The safety penalty: Reclaiming operational sovereignty in the age of AI** — Cisco Talos. Vendor thought-leadership/opinion, no concrete finding.
- **Silent Patches Don't Stop Attackers – They Blind Defenders** — SecurityWeek. Opinion piece, no news value.
- **CISA Warns of Exploited Oracle WebLogic Vulnerability** — SecurityWeek. Duplicate of the same CVE, covered via The Hacker News' more detailed writeup.
- **The full stack behind abundant intelligence** — OpenAI Blog. Business/strategy commentary from OpenAI's CFO, no concrete technical news.
