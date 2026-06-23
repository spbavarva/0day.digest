# Digest — 2026-06-23 AM

- Window: last 14h
- Raw items considered: 19
- Relevant: 10
- Skippable: 9

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Malicious npm Packages Impersonate PostCSS Tools to Deliver Windows RAT — `2026-06-23-npm-postcss-packages-windows-rat.md`
- [x] **[INFORMATIONAL]** Trump Signs Executive Order Accelerating Post-Quantum Cryptography Migration — `2026-06-23-trump-eo-post-quantum-cryptography-migration.md`
- [x] **[HIGH]** Xsolis Data Breach Affects 1.4 Million Individuals — `2026-06-23-xsolis-data-breach-1-4-million.md`
- [x] **[MEDIUM]** WhatsApp VBScript Campaign Installs ManageEngine RMM Tool via Fake Documents — `2026-06-23-whatsapp-vbscript-manageengine-rmm-campaign.md`
- [x] **[MEDIUM]** OpenAI Expands Daybreak With GPT-5.5-Cyber for Vulnerability Patching — `2026-06-23-openai-daybreak-gpt-5-5-cyber.md`
- [x] **[INFORMATIONAL]** Research Frames Prompt Injection as Role Confusion — `2026-06-22-prompt-injection-role-confusion.md`
- [x] **[INFORMATIONAL]** AWS Lambda Introduces MicroVMs for Isolated Sandbox Workloads — `2026-06-22-aws-lambda-microvms-isolated-sandboxes.md`
- [x] **[HIGH]** Unit 42 Details Universal Bucket Hijacking Technique Across Major Clouds — `2026-06-22-unit42-global-namespace-bucket-hijacking.md`
- [x] **[MEDIUM]** JaredFromSubway MEV Bot Loses $15 Million to Logic Manipulation Attack — `2026-06-22-jaredfromsubway-mev-bot-15-million-theft.md`
- [x] **[HIGH]** FFmpeg Patches PixelSmash Flaw Enabling RCE on Jellyfin and DoS Elsewhere — `2026-06-22-ffmpeg-pixelsmash-rce-flaw.md`

## Relevant (details)

### 1. Malicious npm Packages Impersonate PostCSS Tools to Deliver Windows RAT
- **Source:** The Hacker News — https://thehackernews.com/2026/06/malicious-npm-packages-pose-as-postcss.html
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `malware`
- **Summary:** A set of malicious npm packages impersonating PostCSS tooling were found delivering a Windows RAT. They were published by a single npm account over the past month with combined downloads in the low hundreds.

### 2. Trump Signs Executive Order Accelerating Post-Quantum Cryptography Migration
- **Source:** SecurityWeek — https://www.securityweek.com/trump-signs-executive-order-accelerating-post-quantum-cryptography-migration/
- **Severity:** informational
- **Tags:** `post-quantum`
- **Summary:** A new executive order requires federal agencies to migrate high-value and high-impact systems to post-quantum cryptography by 2030/2031. Accelerates existing federal PQC migration timelines.

### 3. Xsolis Data Breach Affects 1.4 Million Individuals
- **Source:** SecurityWeek — https://www.securityweek.com/xsolis-data-breach-affects-1-4-million-individuals/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** Healthcare utilization-management vendor Xsolis disclosed a breach exposing personal and protected health information for roughly 1.4 million individuals. No intrusion-vector details disclosed.

### 4. WhatsApp VBScript Campaign Installs ManageEngine RMM Tool via Fake Documents
- **Source:** The Hacker News — https://thehackernews.com/2026/06/whatsapp-vbscript-campaign-uses-fake.html
- **Severity:** medium
- **Tags:** `phishing`, `malware`
- **Summary:** An active campaign distributes malicious VBScript via WhatsApp direct messages disguised as business documents, installing a legitimate ManageEngine RMM tool for remote access. Kaspersky tracked it across 9 countries.

### 5. OpenAI Expands Daybreak With GPT-5.5-Cyber for Vulnerability Patching
- **Source:** The Hacker News — https://thehackernews.com/2026/06/openai-expands-daybreak-with-gpt-55.html
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`, `openai`
- **Summary:** OpenAI is giving trusted defenders an improved GPT-5.5-Cyber model under its Daybreak initiative, aimed at finding and patching software vulnerabilities across large codebases.

### 6. Research Frames Prompt Injection as Role Confusion
- **Source:** Simon Willison — https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/#atom-everything
- **Severity:** informational
- **Tags:** `ai-safety`, `llm`
- **Summary:** New research frames prompt injection as a role-confusion problem, since models struggle to distinguish their own privileged role-tagged text from untrusted user input. Comes with an accessible blog-style writeup.

### 7. AWS Lambda Introduces MicroVMs for Isolated Sandbox Workloads
- **Source:** AWS News Blog — https://aws.amazon.com/blogs/aws/run-isolated-sandboxes-with-full-lifecycle-control-aws-lambda-introduces-microvms/
- **Severity:** informational
- **Tags:** `aws`, `cloud-security`
- **Summary:** AWS launched Lambda MicroVMs, a serverless primitive offering VM-level isolated sandboxes with no shared kernel between sessions, rapid launch/resume, and up to 8 hours of state preservation.

### 8. Unit 42 Details Universal Bucket Hijacking Technique Across Major Clouds
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/
- **Severity:** high
- **Tags:** `cloud-security`, `vulnerability`
- **Summary:** Unit 42 details a technique exploiting global bucket-name uniqueness to hijack storage buckets and redirect data streams, working across major cloud providers and enabling data exfiltration.

### 9. JaredFromSubway MEV Bot Loses $15 Million to Logic Manipulation Attack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/jaredfromsubway-mev-bot-hacked-in-15-million-crypto-theft/
- **Severity:** medium
- **Tags:** `vulnerability`, `defi`
- **Summary:** An attacker manipulated the JaredFromSubway MEV bot's opportunity-detection logic with fake trading signals, causing it to execute trades that lost $15 million.

### 10. FFmpeg Patches PixelSmash Flaw Enabling RCE on Jellyfin and DoS Elsewhere
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/ffmpeg-fixes-pixelsmash-flaw-in-widely-used-video-decoder/
- **Severity:** high
- **Tags:** `rce`, `vulnerability`
- **Summary:** FFmpeg fixed a flaw ("PixelSmash") in its video decoder that can lead to RCE on Jellyfin servers and DoS in other apps bundling FFmpeg, including Kodi, Emby, Nextcloud, PhotoPrism, and OBS Studio.

## Skippable

- **Canadian Electricity Provider London Hydro Discloses Data Breach** — SecurityWeek. Generic regional breach disclosure with no technical detail.
- **The running list: major tech layoffs in 2026 where employers cited AI** — TechCrunch AI. Running listicle/analysis, no single news event or security angle.
- **OpenAI launches new initiative to help find and patch open source bugs** — TechCrunch AI. Duplicate coverage of the Daybreak/GPT-5.5-Cyber story; The Hacker News version has more technical detail.
- **How Omio is building the future of conversational travel** — OpenAI Blog. Customer-story marketing content, no security or launch substance.
- **Shipping huggingface_hub every week with AI, open tools, and a human in the loop** — Hugging Face Blog. Internal dev-process post, not a model launch or security item.
- **Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code** — Simon Willison. Personal hobby project port, not a lab model launch, no security angle.
- **Nvidia says its AI data center design runs hotter to use a lot less water** — The Verge AI. Infrastructure marketing claim, no security relevance.
- **WhatsApp phishing attack uses fake business docs to hack PCs** — BleepingComputer. Duplicate coverage of the WhatsApp VBScript campaign; The Hacker News/Kaspersky version has more detail.
- **The AI world is getting 'loopy'** — TechCrunch AI. Opinion/trend piece on agentic AI swarms, no concrete news or security substance.
