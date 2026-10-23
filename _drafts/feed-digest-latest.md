# Digest — 2026-10-23 PM

- Window: last 14h
- Raw items considered: 20
- Relevant: 11
- Skippable: 9

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[INFORMATIONAL]** AI Agents as Insider Threats: Microsoft Bets on Guardian Agents — `2026-10-23-microsoft-ai-agents-insider-threats-guardian-agents.md`
- [x] **[MEDIUM]** PHP Warns of New Unpatched RCE Days After PHP2Shell Patches — `2026-10-23-php-new-unpatched-rce-cve-2026-115560.md`
- [x] **[HIGH]** Russian-Linked Hackers Used New Mesh Network Backdoor in Destructive Ukraine Attack — `2026-10-23-sandworm-mesh-network-backdoor-ukraine-attack.md`
- [x] **[HIGH]** China APT Uses AI Pentest Tool Artex in ConnectWise Attacks — `2026-10-23-china-apt-ai-pentest-tool-artex-connectwise.md`
- [x] **[CRITICAL]** Attackers Exploit Third VeloCloud Orchestrator Zero-Day in Four Months — `2026-10-23-velocloud-orchestrator-third-zero-day-exploited.md`
- [x] **[HIGH]** Critical Flaw in Python's Pillow Image Library Allows Code Execution via Crafted Image — `2026-10-23-pillow-critical-rce-crafted-image-cve-2026-112900.md`
- [x] **[HIGH]** Node2Shell RCE Demonstrated on Official Node.js Build via Crafted Brotli Data — `2026-10-23-node2shell-rce-nodejs-brotli-cve-2026-111497.md`
- [x] **[MEDIUM]** Critical x402 SDK Flaw Could Let Malicious APIs Drain AI Agents' Token Balances — `2026-10-23-x402-sdk-flaw-drains-ai-agent-token-balances.md`
- [x] **[HIGH]** 11 Million Impacted by Capcom Data Breach — `2026-10-23-capcom-data-breach-11-million.md`
- [x] **[CRITICAL]** LiteLLM Compromised in Fresh Supply Chain Attack — `2026-10-23-litellm-supply-chain-attack-compromised.md`
- [x] **[HIGH]** PHP2Shell Exploit Attempts Hit Millions as Attackers Try to Deploy Mirai Malware — `2026-10-23-php2shell-exploit-attempts-mirai-botnet.md`

## Relevant (details)

### 1. AI Agents as Insider Threats: Microsoft Bets on Guardian Agents
- **Source:** Dark Reading — https://www.darkreading.com/cybersecurity-operations/ai-agents-insider-threats-inside-microsoft-unified-security-stack
- **Severity:** informational
- **Tags:** `ai-safety`, `microsoft`, `llm`
- **Summary:** Microsoft's Project Perception adds "Guardian Agents" to monitor and contain anomalous AI agents as part of a unified security stack. Experts warn that policing unpredictable agents with other agents may multiply, rather than contain, the risk.

### 2. PHP Warns of New Unpatched RCE Days After PHP2Shell Patches
- **Source:** The Hacker News — https://thehackernews.com/2026/10/urgent-php-warns-of-another-unpatched.html
- **Severity:** medium
- **Tags:** `rce`, `vulnerability`, `cve`
- **Summary:** PHP disclosed CVE-2026-115560, a second RCE issue two days after emergency PHP2Shell patches. PHP considers it an unlikely risk limited to unusually configured apps and is not issuing an emergency fix, recommending a feature be disabled instead.

### 3. Russian-Linked Hackers Used New Mesh Network Backdoor in Destructive Ukraine Attack
- **Source:** The Hacker News — https://thehackernews.com/2026/10/russian-linked-hackers-used-new-mesh.html
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Summary:** ESET reports Sandworm teamed up with UAC-0099 (Earth Sirrush) to run a destructive wiping attack on a Ukrainian logistics company, gaining access via spear-phishing and deploying a new mesh-network backdoor.

### 4. China APT Uses AI Pentest Tool Artex in ConnectWise Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/china-apt-uses-ai-pentest-tool-artex-in-connectwise-attacks/
- **Severity:** high
- **Tags:** `malware`, `privilege-escalation`, `llm`
- **Summary:** State-sponsored Chinese hackers used an AI-driven pentest tool called Artex to target hundreds of organizations via ConnectWise, gaining privileged access to some environments.

### 5. Attackers Exploit Third VeloCloud Orchestrator Zero-Day in Four Months
- **Source:** SecurityWeek — https://www.securityweek.com/attackers-exploit-third-velocloud-orchestrator-zero-day-in-four-months/
- **Severity:** critical
- **Tags:** `sqli`, `zero-day`, `cve`, `privilege-escalation`
- **Summary:** Attackers are actively exploiting a critical SQL injection zero-day in VeloCloud Orchestrator — the third such zero-day in four months — to access privileged internal functionality and gain operator privileges.

### 6. Critical Flaw in Python's Pillow Image Library Allows Code Execution via Crafted Image
- **Source:** The Hacker News — https://thehackernews.com/2026/10/critical-flaw-in-pythons-popular-pillow.html
- **Severity:** high
- **Tags:** `rce`, `cve`, `vulnerability`, `pypi`
- **Summary:** CVE-2026-112900 in Pillow, the most widely used Python image library, allows RCE via a crafted EPS image because Pillow passes the untrusted filename to Ghostscript without validation.

### 7. Node2Shell RCE Demonstrated on Official Node.js Build via Crafted Brotli Data
- **Source:** The Hacker News — https://thehackernews.com/2026/10/researchers-demonstrate-node2shell-rce.html
- **Severity:** high
- **Tags:** `rce`, `cve`, `vulnerability`
- **Summary:** Imperva researchers demonstrated "Node2Shell," an RCE PoC against the official Node.js 24.22.0 build, by feeding crafted data to the bundled Brotli decoder (CVE-2026-111497) with no custom build required.

### 8. Critical x402 SDK Flaw Could Let Malicious APIs Drain AI Agents' Token Balances
- **Source:** The Hacker News — https://thehackernews.com/2026/10/critical-x402-sdk-flaw-could-let.html
- **Severity:** medium
- **Tags:** `llm`, `vulnerability`, `ai-safety`
- **Summary:** V12 found that x402 SDKs let AI agents sign payments for their full token balance if a malicious API requested it, because the default client set no spending limit until an August 18 fix.

### 9. 11 Million Impacted by Capcom Data Breach
- **Source:** SecurityWeek — https://www.securityweek.com/11-million-impacted-by-capcom-data-breach/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** Hackers stole roughly 11 million email addresses from Capcom ID and changed login passwords for 196 accounts.

### 10. LiteLLM Compromised in Fresh Supply Chain Attack
- **Source:** SecurityWeek — https://www.securityweek.com/litellm-compromised-in-fresh-supply-chain-attack/
- **Severity:** critical
- **Tags:** `supply-chain`, `pypi`, `github`, `llm`
- **Summary:** Attackers used compromised GitHub CLI OAuth tokens to push and approve malicious LiteLLM packages on PyPI and Docker, compromising the widely used multi-LLM-provider library.

### 11. PHP2Shell Exploit Attempts Hit Millions as Attackers Try to Deploy Mirai Malware
- **Source:** The Hacker News — https://thehackernews.com/2026/10/php2shell-exploit-attempts-hit-millions.html
- **Severity:** high
- **Tags:** `rce`, `cve`, `malware`
- **Summary:** Attackers made millions of mostly unsuccessful attempts to exploit the PHP2Shell flaws (CVE-2026-109618, CVE-2026-109619, CVSS 9.2) to recruit systems into the Mirai variant "Potassium."

## Skippable

- **Retro gaming is being overrun with AI** — The Verge AI. Generic AI culture piece, no security angle.
- **Quest Diagnostics Reports Cyber Breach Affecting 'Certain Patient Records'** — SecurityWeek. Regulatory filing is vague with no breach scale or technical detail disclosed.
- **Atlassian Patches 75 Flaws in Data Center and Server Products** — SecurityWeek. Routine patch bulletin; no single CVE flagged as critical and actively exploited.
- **Iran's Prince of Persia APT Hosts C&C in US for First Time Since 2016** — SecurityWeek. Thin technical detail — an infrastructure/geo note without new IOCs or TTPs.
- **Uber rival inDrive eyes 2027 robotaxi tests in Central Asia with Pony.ai and Nvidia** — TechCrunch AI. No security angle.
- **State Bank of India Suffers a Customer PII Data Leak** — Dark Reading. Regional breach disclosure without scale or technical substance.
- **Left alone with nothing to do, AI agents started playing** — TechCrunch AI. Human-interest research piece, not practitioner-relevant security or model news.
- **OpenAI and Poland's NASK partner to advance AI safety and security** — OpenAI Blog. Generic partnership announcement, no actionable detail.
- **Turning Database Grading into RL Rewards: Post-Training Agents with ThinkingBox** — Hugging Face Blog. Technical research/tutorial post, not a launch or notable news event.
