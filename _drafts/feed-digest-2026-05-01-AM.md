# Digest — 2026-05-01 AM

- Window: last 14h
- Raw items considered: 22
- Relevant: 9
- Skippable: 13

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** TeamPCP 'Mini Shai-Hulud' Supply Chain Attack Hits SAP npm Packages — `2026-05-01-teampcp-sap-npm-supply-chain.md`
- [x] **[HIGH]** Hugging Face and ClawHub Abused as Malware Distribution Platforms — `2026-05-01-hugging-face-clawhub-malware.md`
- [x] **[HIGH]** Ransomware Negotiators Sentenced for Secretly Aiding BlackCat Attacks — `2026-05-01-blackcat-insider-ransomware-sentencing.md`
- [x] **[HIGH]** UK AI Security Institute Finds GPT-5.5 Matches Claude Mythos on Cyber Capabilities — `2026-04-30-gpt55-cyber-aisi-evaluation.md`
- [x] **[HIGH]** High-Risk AI Browser Extensions Intercepting Prompts and Stealing Passwords — `2026-04-30-ai-browser-extensions-credential-theft.md`
- [x] **[HIGH]** Anthropic Launches Claude Security to Accelerate Defender Response to AI-Powered Attacks — `2026-04-30-anthropic-claude-security-launch.md`
- [x] **[MEDIUM]** AI-Assisted Scan Surfaces 9-Year-Old Linux Vulnerability with 10-Line PoC Exploit — `2026-04-30-ai-assisted-linux-vulnerability.md`
- [x] **[MEDIUM]** OpenAI Restricts GPT-5.5 Cyber Model to Critical Defenders Only — `2026-04-30-openai-gpt55-cyber-access-restriction.md`
- [x] **[MEDIUM]** Bluekit PhaaS Launches with AI Assistant and 40 Phishing Templates — `2026-04-30-bluekit-phishing-ai-assistant.md`

## Relevant (details)

### 1. TeamPCP 'Mini Shai-Hulud' Supply Chain Attack Hits SAP npm Packages
- **Source:** SecurityWeek — https://www.securityweek.com/1800-hit-in-mini-shai-hulud-attack-on-sap-lightning-intercom/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`
- **Slug:** `teampcp-sap-npm-supply-chain`
- **Must-know:** yes
- **Summary:** The TeamPCP group has compromised multiple SAP cloud ecosystem npm packages—including Lightning and Intercom—which together have nearly 10 million monthly downloads. 1,800 systems were directly hit in this wave; SAP developers should audit dependencies and update immediately.

### 2. Hugging Face and ClawHub Abused as Malware Distribution Platforms
- **Source:** SecurityWeek — https://www.securityweek.com/hugging-face-clawhub-abused-for-malware-distribution/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `phishing`, `llm`
- **Slug:** `hugging-face-clawhub-malware`
- **Must-know:** no
- **Summary:** Threat actors are leveraging social engineering to distribute malware through Hugging Face and ClawHub, exploiting the trusted reputation of AI model repositories. Malicious files are disguised as models or datasets, targeting developers who assume platform-hosted content is safe.

### 3. Ransomware Negotiators Sentenced for Secretly Aiding BlackCat Attacks
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/us-ransomware-negotiators-get-4-years-in-prison-over-blackcat-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`
- **Slug:** `blackcat-insider-ransomware-sentencing`
- **Must-know:** no
- **Summary:** Two former incident response employees—from Sygnia and DigitalMint—were sentenced to four years each for facilitating BlackCat ransomware attacks against U.S. companies while ostensibly serving as defenders. The case is the first known prosecution of ransomware double agents embedded in IR firms with privileged victim access.

### 4. UK AI Security Institute Finds GPT-5.5 Matches Claude Mythos on Cyber Capabilities
- **Source:** Simon Willison — https://simonwillison.net/2026/Apr/30/gpt-55-cyber-capabilities/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** high
- **Tags:** `llm`, `openai`, `anthropic`, `ai-safety`
- **Slug:** `gpt55-cyber-aisi-evaluation`
- **Must-know:** no
- **Summary:** The UK AI Security Institute evaluated GPT-5.5 for vulnerability discovery and found its capability comparable to Anthropic's Claude Mythos, while noting that unlike the restricted Mythos, GPT-5.5 is generally available. This widens the policy gap as multiple frontier models now demonstrate verified offensive cyber capability.

### 5. High-Risk AI Browser Extensions Intercepting Prompts and Stealing Passwords
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/high-risk-gen-ai-browser-extensions/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `malware`, `llm`, `appsec`, `phishing`
- **Slug:** `ai-browser-extensions-credential-theft`
- **Must-know:** no
- **Summary:** Unit 42 has catalogued a class of malicious AI productivity browser extensions that intercept prompts, steal passwords from form inputs, and exfiltrate session data under the guise of email writing assistance. Organizations should audit installed extensions and enforce allowlist-only policies for enterprise browsers.

### 6. Anthropic Launches Claude Security to Accelerate Defender Response to AI-Powered Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/anthropic-unveils-claude-security-to-counter-ai-powered-exploit-surge/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `anthropic`, `ai-safety`, `llm`
- **Slug:** `anthropic-claude-security-launch`
- **Must-know:** no
- **Summary:** Anthropic has unveiled Claude Security, a defender-focused AI product positioned to help security teams match the pace of AI-powered exploitation as time-to-exploit shrinks to hours. The launch is a direct response to the threat landscape enabled by models like Mythos and GPT-5.5 Cyber.

### 7. AI-Assisted Scan Surfaces 9-Year-Old Linux Vulnerability with 10-Line PoC Exploit
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/ai-assisted-software-scan-linux-bug
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `ai-safety`
- **Slug:** `ai-assisted-linux-vulnerability`
- **Must-know:** no
- **Summary:** An AI-assisted code audit has uncovered a nine-year-old bug in the Linux kernel, with a proof-of-concept exploit of just 10 lines—demonstrating how AI lowers the barrier to finding long-dormant vulnerabilities. A patch is already available; Linux operators should verify they are running patched kernel versions.

### 8. OpenAI Restricts GPT-5.5 Cyber Model to Critical Defenders Only
- **Source:** TechCrunch AI — https://techcrunch.com/2026/04/30/after-dissing-anthropic-for-limiting-mythos-openai-restricts-access-to-cyber-too/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `openai`, `ai-safety`, `llm`
- **Slug:** `openai-gpt55-cyber-access-restriction`
- **Must-know:** no
- **Summary:** OpenAI has reversed course and restricted its GPT-5.5 Cyber model to "critical cyber defenders" only—mirroring the access controls it had publicly criticized Anthropic for applying to Mythos. The policy shift underscores the dual-use dilemma for AI labs as frontier models with verified offensive capability near general release.

### 9. Bluekit PhaaS Launches with AI Assistant and 40 Phishing Templates
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-bluekit-phishing-service-includes-an-ai-assistant-40-templates/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `phishing`, `llm`, `malware`
- **Slug:** `bluekit-phishing-ai-assistant`
- **Must-know:** no
- **Summary:** The Bluekit phishing-as-a-service platform has launched with 40 templates targeting popular consumer and enterprise services, plus a built-in AI assistant for generating lure content. The AI component lowers the skill floor for phishing operators, enabling convincing campaign drafts without copywriting expertise.

## Skippable

- **FBI Warns of Surge in Hacker-Enabled Cargo Theft** — SecurityWeek. FBI advisory about freight broker hacking without new IOCs or technical guidance; covered separately by The Record as the same story.
- **ChatGPT Images 2.0 is a hit in India** — TechCrunch AI. Regional product adoption story with no security angle.
- **Codex CLI 0.128.0 adds /goal** — Simon Willison. Minor developer tool update to OpenAI's CLI agent; no security angle.
- **Sources: Anthropic potential $900B+ valuation round** — TechCrunch AI. Business/funding news with no technical or security substance.
- **The craziest part of Musk v. Altman happened while the jury was out** — The Verge AI. Legal procedural drama with no security or technical substance.
- **Apple was surprised by AI-driven demand for Macs** — TechCrunch AI. Business/hardware supply story, no security angle.
- **Congress punts FISA renewal to June** — The Record. Policy delay with no new IOCs or actionable technical guidance.
- **Quoting Andrew Kelley** — Simon Willison. Opinion on detecting LLM use in code contributions; no news value.
- **TeamPCP Hits SAP Packages With 'Mini Shai-Hulud' Attack** — Dark Reading. Duplicate of SecurityWeek item 4; SecurityWeek has more concrete impact figures.
- **Hackers earning millions from hijacked cargo, FBI says** — The Record. Duplicate of SecurityWeek item 2.
- **Legal AI startup Legora hits $5.6B valuation** — TechCrunch AI. Business/funding news with no security angle.
- **Anthropic's Mythos Has Landed: Here's What Comes Next for Cyber** — Dark Reading. Editorial video segment; no new reporting beyond what SecurityWeek and TechCrunch have covered.
- **AI Fuels 'Industrial' Cybercrime as Time-to-Exploit Shrinks to Hours** — SecurityWeek. Trend analysis piece without new research, IOCs, or incident reports; the underlying story is covered in the Anthropic Claude Security item.
