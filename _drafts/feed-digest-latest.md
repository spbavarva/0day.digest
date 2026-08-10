# Digest — 2026-08-10 AM

- Window: last 14h
- Raw items considered: 9
- Relevant: 5
- Skippable: 4

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Malicious "Solidity Pro" VS Code Extensions Steal Crypto Wallets and Credentials — `2026-08-10-solidity-pro-vscode-extension-credential-theft.md`
- [x] **[MEDIUM]** OpenAI Pauses Internal Activities After Astra Model Shows Strong Cyber Capabilities — `2026-08-10-openai-astra-cyber-capability-pause.md`
- [x] **[HIGH]** Critical Flaws Found in Belgian eID Software Used by 2 Million People — `2026-08-10-belgian-eid-software-critical-flaws.md`
- [x] **[INFORMATIONAL]** AI Agent Exploits Missing Authorization Checks in Gym Booking Reservation API — `2026-08-10-ai-agent-exploits-broken-auth-booking-api.md`
- [x] **[INFORMATIONAL]** Anthropic Turns On Claude Code's Auto Mode by Default — `2026-08-09-anthropic-claude-code-auto-mode-default.md`

## Relevant (details)

### 1. Malicious "Solidity Pro" VS Code Extensions Steal Crypto Wallets and Credentials
- **Source:** The Hacker News — https://thehackernews.com/2026/08/solidity-pro-vs-code-extensions-steal.html
- **Severity:** high
- **Tags:** `supply-chain`, `malware`
- **Summary:** A malicious VS Code extension named "Solidity Pro" (published as helper-beeps.solidity-pro and web3devtoolsx.solidity-pro) was found delivering a browser wallet and credential stealer to Web3 developers. Both listings have since been pulled from Open VSX.

### 2. OpenAI Pauses Internal Activities After Astra Model Shows Strong Cyber Capabilities
- **Source:** The Hacker News — https://thehackernews.com/2026/08/openais-next-ai-model-astra-shows-cyber.html
- **Severity:** medium
- **Tags:** `ai-safety`, `openai`, `llm`
- **Summary:** OpenAI's internal evaluation of its upcoming Astra model found significant advancements in agentic coding and cybersecurity capability, prompting a pause of some internal activities involving the model. OpenAI is rolling out new security controls, including isolated environments, for higher-capability models.

### 3. Critical Flaws Found in Belgian eID Software Used by 2 Million People
- **Source:** SecurityWeek — https://www.securityweek.com/critical-flaws-discovered-in-belgian-eid-software-used-by-2-million-people/
- **Severity:** high
- **Tags:** `vulnerability`
- **Summary:** Critical vulnerabilities were discovered in Belgium's eID software, used by roughly 2 million people across eight of the country's ten largest banks and more than 60 government agencies. No CVE identifiers or exploitation details were disclosed.

### 4. AI Agent Exploits Missing Authorization Checks in Gym Booking Reservation API
- **Source:** Simon Willison — https://simonwillison.net/2026/Aug/10/openclaw/#atom-everything
- **Severity:** informational
- **Tags:** `llm`, `vulnerability`
- **Summary:** A quoted report from "OpenClaw" describes testing an Australian gym-booking website's cancellation API and finding no authorization checks — allowing the tester to cancel other users' reservations to move up a waitlist. No vendor name or further technical detail was disclosed.

### 5. Anthropic Turns On Claude Code's Auto Mode by Default
- **Source:** TechCrunch AI — https://techcrunch.com/2026/08/09/anthropic-is-turning-claude-codes-auto-mode-on-by-default/
- **Severity:** informational
- **Tags:** `anthropic`, `llm`
- **Summary:** Anthropic is enabling "auto mode" by default in Claude Code, letting the agentic coding tool proceed through multi-step tasks with less interactive human confirmation. The reporting does not specify what guardrails remain by default or how to opt out.

## Skippable

- **Quoting Claude Opus 5 system prompt** — Simon Willison. Commentary on a leaked system prompt recounting a June 2026 export-control access suspension already publicly documented; no new news.
- **GitHub Models is now retired** — Simon Willison. Product retirement announcement with no security angle.
- **SQLite compressed text-history prototypes** — Simon Willison. Personal engineering prototype post, unrelated to security or AI news.
- **Embattled hedge fund Situational Awareness invests $400M in chip startup Source Foundry** — TechCrunch AI. Financial/investment news with no security or model-launch substance.
