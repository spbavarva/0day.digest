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
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`
- **Summary:** The TeamPCP group has compromised multiple SAP cloud ecosystem npm packages—including Lightning and Intercom—which together have nearly 10 million monthly downloads. 1,800 systems were directly hit; SAP developers should audit dependencies and update immediately.

### 2. Hugging Face and ClawHub Abused as Malware Distribution Platforms
- **Source:** SecurityWeek — https://www.securityweek.com/hugging-face-clawhub-abused-for-malware-distribution/
- **Severity:** high
- **Tags:** `malware`, `phishing`, `llm`
- **Summary:** Threat actors are using social engineering to distribute malware through Hugging Face and ClawHub, disguising malicious files as AI models or datasets. Developers who assume platform-hosted content is safe are the primary target.

### 3. Ransomware Negotiators Sentenced for Secretly Aiding BlackCat Attacks
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/us-ransomware-negotiators-get-4-years-in-prison-over-blackcat-attacks/
- **Severity:** high
- **Tags:** `ransomware`
- **Summary:** Two former IR firm employees were sentenced to four years each for facilitating BlackCat ransomware attacks while posing as defenders with privileged victim access. First known prosecution of ransomware double agents embedded in incident response firms.

### 4. UK AI Security Institute Finds GPT-5.5 Matches Claude Mythos on Cyber Capabilities
- **Source:** Simon Willison — https://simonwillison.net/2026/Apr/30/gpt-55-cyber-capabilities/#atom-everything
- **Severity:** high
- **Tags:** `llm`, `openai`, `anthropic`, `ai-safety`
- **Summary:** The UK AISI evaluated GPT-5.5 for vulnerability discovery and found it comparable to Claude Mythos—but GPT-5.5 is generally available while Mythos is restricted, widening the policy gap. Multiple frontier models now have verified offensive cyber capability.

### 5. High-Risk AI Browser Extensions Intercepting Prompts and Stealing Passwords
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/high-risk-gen-ai-browser-extensions/
- **Severity:** high
- **Tags:** `malware`, `llm`, `appsec`, `phishing`
- **Summary:** Unit 42 identified malicious AI productivity browser extensions that intercept AI prompts, steal passwords from form inputs, and exfiltrate session data under the guise of email assistance tools. Enterprise browsers should enforce extension allowlists immediately.

### 6. Anthropic Launches Claude Security to Accelerate Defender Response to AI-Powered Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/anthropic-unveils-claude-security-to-counter-ai-powered-exploit-surge/
- **Severity:** high
- **Tags:** `anthropic`, `ai-safety`, `llm`
- **Summary:** Anthropic has unveiled Claude Security as a defender-focused product to help security teams match the pace of AI-powered exploitation as time-to-exploit shrinks to hours. The launch directly responds to the threat landscape enabled by models like Mythos and GPT-5.5 Cyber.

### 7. AI-Assisted Scan Surfaces 9-Year-Old Linux Vulnerability with 10-Line PoC Exploit
- **Source:** Dark Reading — https://www.darkreading.com/vulnerabilities-threats/ai-assisted-software-scan-linux-bug
- **Severity:** medium
- **Tags:** `vulnerability`, `ai-safety`
- **Summary:** An AI-powered code audit uncovered a nine-year-old Linux kernel bug with a 10-line proof-of-concept exploit, illustrating how AI tools are accelerating discovery of dormant vulnerabilities. A patch is already available.

### 8. OpenAI Restricts GPT-5.5 Cyber Model to Critical Defenders Only
- **Source:** TechCrunch AI — https://techcrunch.com/2026/04/30/after-dissing-anthropic-for-limiting-mythos-openai-restricts-access-to-cyber-too/
- **Severity:** medium
- **Tags:** `openai`, `ai-safety`, `llm`
- **Summary:** OpenAI has reversed its public criticism of Anthropic's Mythos restrictions and applied similar controls to GPT-5.5 Cyber, limiting access to verified critical defenders. The policy reversal highlights the unresolved dual-use dilemma across AI labs.

### 9. Bluekit PhaaS Launches with AI Assistant and 40 Phishing Templates
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-bluekit-phishing-service-includes-an-ai-assistant-40-templates/
- **Severity:** medium
- **Tags:** `phishing`, `llm`, `malware`
- **Summary:** Bluekit is a new phishing-as-a-service platform with 40 templates targeting popular services and a built-in AI assistant for generating campaign lures. The AI component removes the copywriting barrier for phishing operators.

## Skippable

- **FBI Warns of Surge in Hacker-Enabled Cargo Theft** — SecurityWeek. FBI advisory about freight broker hacking without new IOCs or technical guidance.
- **Hackers earning millions from hijacked cargo, FBI says** — The Record. Duplicate of above FBI cargo theft advisory.
- **ChatGPT Images 2.0 is a hit in India** — TechCrunch AI. Regional product adoption story, no security angle.
- **Codex CLI 0.128.0 adds /goal** — Simon Willison. Minor agentic feature update to OpenAI CLI, no security angle.
- **Sources: Anthropic potential $900B+ valuation round** — TechCrunch AI. Business/funding news, no technical substance.
- **The craziest part of Musk v. Altman** — The Verge AI. Legal procedural drama, no security or technical substance.
- **Apple was surprised by AI-driven demand for Macs** — TechCrunch AI. Hardware supply story, no security angle.
- **Congress punts FISA renewal to June** — The Record. Policy delay, no new IOCs or actionable technical guidance.
- **Quoting Andrew Kelley** — Simon Willison. Opinion on detecting LLM use in code; no news value.
- **TeamPCP Hits SAP Packages With 'Mini Shai-Hulud' Attack** — Dark Reading. Duplicate of SecurityWeek item; SecurityWeek has more concrete impact figures.
- **Legal AI startup Legora hits $5.6B valuation** — TechCrunch AI. Business/funding news, no security angle.
- **Anthropic's Mythos Has Landed: Here's What Comes Next for Cyber** — Dark Reading. Editorial video, no new reporting beyond SecurityWeek and TechCrunch coverage.
- **AI Fuels 'Industrial' Cybercrime as Time-to-Exploit Shrinks to Hours** — SecurityWeek. Trend analysis without new research or incidents; the story is captured in the Claude Security launch item.
