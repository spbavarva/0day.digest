# Digest — 2026-06-08 AM

- Window: last 14h
- Raw items considered: 15
- Relevant: 8
- Skippable: 7

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** VerdantBamboo Deploys BSD Variant of BRICKSTORM on Linux Appliances — `2026-06-08-verdantbamboo-brickstorm-bsd-linux-backdoor.md`
- [x] **[HIGH]** SolarWinds Serv-U Vulnerability Exploited in the Wild — `2026-06-08-solarwinds-serv-u-vulnerability-exploited.md`
- [x] **[HIGH]** Meta: 20,000 Instagram Accounts Hijacked via Abuse of AI-Powered Support Tool — `2026-06-08-meta-instagram-ai-support-tool-account-hijacking.md`
- [x] **[MEDIUM]** Silent Ransom Group Uses DNS Fast Flux to Hide C2 Infrastructure — `2026-06-08-silent-ransom-group-dns-fast-flux.md`
- [x] **[MEDIUM]** UNC3753 Combines Vishing and Physical Intrusion in U.S. Data Theft Extortion Campaign — `2026-06-08-unc3753-vishing-physical-intrusion-extortion.md`
- [x] **[INFORMATIONAL]** OpenAI Expands ChatGPT Account Security Controls — `2026-06-08-openai-chatgpt-account-security-controls.md`
- [x] **[INFORMATIONAL]** Anthropic Calls for Industry Coordination on AI Development 'Pause' Mechanism — `2026-06-08-anthropic-ai-pause-coordination-proposal.md`
- [x] **[INFORMATIONAL]** VS Code Adds 2-Hour Delay to Extension Auto-Updates to Curb Supply Chain Attacks — `2026-06-08-vscode-extension-auto-update-delay-supply-chain.md`

## Relevant (details)

### 1. VerdantBamboo Deploys BSD Variant of BRICKSTORM on Linux Appliances
- **Source:** The Hacker News — https://thehackernews.com/2026/06/verdantbamboo-deploys-bsd-variant-of.html
- **Severity:** high
- **Tags:** `malware`, `apt`
- **Summary:** Volexity attributes a new espionage campaign to a China-nexus cluster it tracks as VerdantBamboo (overlapping with Microsoft's "Clay Typhoon"), deploying a BSD variant of the BRICKSTORM backdoor plus two new malware families (PLENET/GRIMBOLT, AGENTPSD) against Linux appliances.

### 2. SolarWinds Serv-U Vulnerability Exploited in the Wild
- **Source:** SecurityWeek — https://www.securityweek.com/solarwinds-patches-exploited-serv-u-vulnerability/
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `cve`
- **Summary:** SolarWinds patched a Serv-U flaw under active exploitation; unauthenticated attackers can crash the service via crafted POST requests, causing denial of service. Patching is urgent given confirmed in-the-wild exploitation.

### 3. Meta: 20,000 Instagram Accounts Hijacked via Abuse of AI-Powered Support Tool
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/meta-ai-support-data-breach-affects-20-000-instagram-accounts/
- **Severity:** high
- **Tags:** `data-breach`, `meta`, `llm`
- **Summary:** Meta disclosed that 20,225 Instagram accounts were hijacked after attackers abused its AI-powered account-recovery support system to reset passwords, illustrating how AI-driven support automation can itself become an attack surface.

### 4. Silent Ransom Group Uses DNS Fast Flux to Hide C2 Infrastructure
- **Source:** SecurityWeek — https://www.securityweek.com/silent-ransom-group-uses-dns-fast-flux-in-attacks/
- **Severity:** medium
- **Tags:** `ransomware`, `malware`
- **Summary:** The Silent Ransom Group is using DNS fast-flux to obscure its C2 infrastructure while focusing campaigns on U.S. law firms, complicating takedown and attribution for defenders.

### 5. UNC3753 Combines Vishing and Physical Intrusion in U.S. Data Theft Extortion Campaign
- **Source:** The Hacker News — https://thehackernews.com/2026/06/unc3753-used-vishing-and-physical.html
- **Severity:** medium
- **Tags:** `phishing`, `data-breach`
- **Summary:** Google Mandiant/GTIG attributed a financially motivated data-theft extortion campaign (Jan–May 2026, dozens of U.S. legal/financial/professional services firms) to UNC3753, which combined vishing with physical intrusions to gain access before exfiltrating data.

### 6. OpenAI Expands ChatGPT Account Security Controls
- **Source:** SecurityWeek — https://www.securityweek.com/openai-rolling-out-chatgpt-account-security-controls/
- **Severity:** informational
- **Tags:** `openai`, `llm`, `appsec`
- **Summary:** OpenAI is broadening availability of Active Sessions and Lockdown Mode, two ChatGPT account security features that give users more visibility and control over account access.

### 7. Anthropic Calls for Industry Coordination on AI Development 'Pause' Mechanism
- **Source:** SecurityWeek — https://www.securityweek.com/anthropic-urges-industry-coordination-to-allow-for-a-pause-in-ai-development-if-risks-grow/
- **Severity:** informational
- **Tags:** `anthropic`, `ai-safety`
- **Summary:** Anthropic is urging the AI industry to build coordination/verification mechanisms so major labs could confirm rivals have genuinely slowed development, enabling a credible industry-wide "pause" if AI risk grows too high.

### 8. VS Code Adds 2-Hour Delay to Extension Auto-Updates to Curb Supply Chain Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/06/vs-code-adds-2-hour-extension-auto.html
- **Severity:** informational
- **Tags:** `supply-chain`, `microsoft`, `devsecops`
- **Summary:** Microsoft will delay automatic VS Code extension updates by two hours after publication, giving the security community a window to flag malicious releases before they reach most users — a direct response to IDE supply chain attacks.

## Skippable

- **174,000 Impacted by Lansing Community College Data Breach** — SecurityWeek. Generic breach disclosure without technical detail (TTPs/IOCs not described).
- **Oxford University discloses data breach after careers platform hack** — BleepingComputer. Third-party platform breach disclosure without technical substance.
- **Building Pakistan Notice Helper: A Small AI Tool for a Very Local Safety Problem** — Hugging Face Blog. Hackathon project writeup, no broad model launch or security relevance.
- **WWDC 2026: How to watch and what to expect** — The Verge AI. Event preview/scheduling content, no security or substantive AI angle.
- **Meta Says 20,000 Instagram Accounts Hacked via AI Tool Abuse** — SecurityWeek. Duplicate coverage of the Meta/Instagram AI-support hijacking story; the BleepingComputer version above carries more technical detail and was selected instead.
- **datasette-agent-edit 0.1a0** — Simon Willison. Niche alpha-stage plugin release note, limited practitioner relevance.
- **Hands on with Intelligent Terminal, an AI-powered Windows Terminal** — BleepingComputer. Hands-on feature/review piece on a niche open-source terminal fork, no security substance.
