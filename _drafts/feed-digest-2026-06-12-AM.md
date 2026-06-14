# Digest — 2026-06-12 AM

- Window: last 14h
- Raw items considered: 19
- Relevant: 6
- Skippable: 13

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** CISA Orders 3-Day Emergency Patch as Ivanti Sentry Flaw Sees Active Exploitation — `2026-06-12-ivanti-sentry-zero-day-cisa-bod-26-04.md`
- [x] **[CRITICAL]** LangGraph Flaw Chain Exposes Self-Hosted AI Agents to Remote Code Execution — `2026-06-12-langgraph-flaw-chain-rce-ai-agents.md`
- [x] **[CRITICAL]** Google Confirms Active Exploitation of Oracle PeopleSoft Zero-Day (CVE-2026-35273) by ShinyHunters — `2026-06-12-oracle-peoplesoft-zero-day-cve-2026-35273-shinyhunters.md`
- [x] **[HIGH]** Japanese Energy Firm Kyushu Electric Loses Drive Holding Data on 10.9 Million Customers — `2026-06-11-kyushu-electric-data-loss-10-9-million.md`
- [x] **[INFORMATIONAL]** Anthropic Disputes Fable 5 AI Jailbreak Claim — `2026-06-12-anthropic-disputes-fable-5-jailbreak.md`
- [x] **[INFORMATIONAL]** Simon Willison: Claude Fable 5 Is 'Relentlessly Proactive' — `2026-06-11-claude-fable-5-relentlessly-proactive.md`

## Relevant (details)

### 1. CISA Orders 3-Day Emergency Patch as Ivanti Sentry Flaw Sees Active Exploitation
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-gives-feds-3-days-to-patch-ivanti-flaw-exploited-in-attacks/ (also SecurityWeek)
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `rce`, `privilege-escalation`
- **Slug:** `ivanti-sentry-zero-day-cisa-bod-26-04`
- **Must-know:** no
- **Summary:** CISA's new Binding Operational Directive 26-04 gives federal agencies three days to patch a critical Ivanti Sentry OS command injection flaw that allows root-level code execution. SecurityWeek separately reports exploitation attempts are already hitting honeypots, indicating active scanning of internet-facing Sentry instances.

### 2. LangGraph Flaw Chain Exposes Self-Hosted AI Agents to Remote Code Execution
- **Source:** The Hacker News — https://thehackernews.com/2026/06/langgraph-flaw-chain-exposes-self.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `llm`, `rce`, `sqli`, `vulnerability`
- **Slug:** `langgraph-flaw-chain-rce-ai-agents`
- **Must-know:** no
- **Summary:** Researchers disclosed three now-patched flaws in LangGraph, LangChain's framework for multi-agent AI applications, including a chain combining SQL injection with other issues to achieve remote code execution. Self-hosted LangGraph deployments should be updated to the patched release.

### 3. Google Confirms Active Exploitation of Oracle PeopleSoft Zero-Day (CVE-2026-35273) by ShinyHunters
- **Source:** SecurityWeek — https://www.securityweek.com/google-confirms-exploitation-of-oracle-peoplesoft-zero-day-by-shinyhunters/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `zero-day`, `data-breach`
- **Slug:** `oracle-peoplesoft-zero-day-cve-2026-35273-shinyhunters`
- **Must-know:** yes
- **Summary:** Google has confirmed in-the-wild exploitation of CVE-2026-35273, an Oracle PeopleSoft zero-day, attributing the activity to the ShinyHunters extortion group. Oracle has shipped a mitigation but has not publicly confirmed pre-patch exploitation; PeopleSoft operators should apply the mitigation and check for ShinyHunters IOCs.

### 4. Japanese Energy Firm Kyushu Electric Loses Drive Holding Data on 10.9 Million Customers
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/japanese-energy-firm-loses-drive-with-data-of-109-million-clients/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `kyushu-electric-data-loss-10-9-million`
- **Must-know:** no
- **Summary:** Kyushu Electric Power disclosed a physical security incident in which a drive containing private data on more than 10.9 million customers was lost. The company has not yet specified what data was stored on the drive or whether it was encrypted.

### 5. Anthropic Disputes Fable 5 AI Jailbreak Claim
- **Source:** SecurityWeek — https://www.securityweek.com/anthropic-disputes-fable-5-ai-jailbreak/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `anthropic`, `ai-safety`, `llm`
- **Slug:** `anthropic-disputes-fable-5-jailbreak`
- **Must-know:** no
- **Summary:** A security researcher claims to have jailbroken Claude Fable 5 shortly after launch via a prompt-based technique, but Anthropic disputes that the behavior constitutes a genuine jailbreak. No technical details of the claim or rebuttal were available.

### 6. Simon Willison: Claude Fable 5 Is 'Relentlessly Proactive'
- **Source:** Simon Willison — https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `anthropic`, `llm`, `ai-safety`
- **Slug:** `claude-fable-5-relentlessly-proactive`
- **Must-know:** no
- **Summary:** Developer Simon Willison describes Claude Fable 5 as "relentlessly proactive," citing an example where the model independently investigated project dependencies to debug a UI issue from a screenshot alone. The observation points to a notable increase in agentic autonomy in Claude's latest model.

## Skippable

- **Pharma giant Novo Nordisk discloses breach of clinical trials data** — BleepingComputer. No details on scope, affected count, or technical cause; thin disclosure.
- **Ivanti Sentry Exploitation Attempts Hitting Honeypots** — SecurityWeek. Duplicate coverage of the Ivanti Sentry zero-day (see item 1 above).
- **Chrome 149 Update Patches 28 Vulnerabilities** — SecurityWeek. Routine browser patch release; no single critical CVE flagged as actively exploited.
- **INTERPOL Operation Takes Down Sniper Dz Phishing Platform, Arrests Administrator** — The Hacker News. Law enforcement takedown, no new IOCs or technical guidance for defenders.
- **Over 73,000 French govt employees affected in Tchap messenger breach** — BleepingComputer. Below the 100k threshold and no technical detail on the breach cause.
- **Siri won't be your AI girlfriend** — The Verge AI. Consumer product personality/design commentary, no security or model-launch substance.
- **Europol Disrupts AudiA6 Crypto Laundering Service Used by Ransomware Gangs** — The Hacker News. Law enforcement takedown, no new IOCs or TTPs for defenders.
- **Cheaper, faster, and culturally aware, Avataar's video AI is built for India's scale** — TechCrunch AI. Startup product/pricing announcement, no security or safety angle.
- **Theker just raised $85M to build the factory robot that doesn't specialize in anything** — TechCrunch AI. Funding round, no AI model or security relevance.
- **Jeff Bezos's Prometheus raises $12B to build an 'artificial general engineer' for the physical world** — TechCrunch AI. Funding/business news, no model launch or security relevance.
- **Phishing Attack Volume Down 20%, but Risk Still Rising** — Dark Reading. General industry trend commentary, no specific incident or technical detail.
- **How Preply combines AI and human tutors to personalize learning** — OpenAI Blog. Customer case study / marketing content, no model launch or security relevance.
- **Maine breach portal abused to publish fake data breach disclosures** — BleepingComputer. Regional misinformation campaign targeting a state breach portal, no technical exploit detail.
