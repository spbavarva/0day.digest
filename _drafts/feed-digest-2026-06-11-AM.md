# Digest — 2026-06-11 AM

- Window: last 14h
- Raw items considered: 22
- Relevant: 11
- Skippable: 11

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Microsoft Patches Exploited Exchange Server Zero-Day CVE-2026-42897 — `2026-06-11-microsoft-patches-exploited-exchange-cve-2026-42897.md`
- [x] **[CRITICAL]** Max Severity Ivanti Sentry Vulnerability Now Exploited in Attacks — `2026-06-11-max-severity-ivanti-sentry-vulnerability-exploited.md`
- [x] **[HIGH]** Splunk, Palo Alto Networks Patch Severe Vulnerabilities — `2026-06-11-splunk-palo-alto-networks-patch-severe-vulnerabilities.md`
- [x] **[HIGH]** 'GreatXML' Zero-Day Exploit Bypasses BitLocker — `2026-06-11-greatxml-zero-day-bypasses-bitlocker.md`
- [x] **[HIGH]** University of Nottingham Data Breach Exposes 450,000+ Records (ShinyHunters) — `2026-06-11-university-of-nottingham-data-breach-shinyhunters.md`
- [x] **[HIGH]** Path Traversal Flaw in AI Dev Platform Langflow Exploited in Attacks (CVE-2026-5027) — `2026-06-10-langflow-path-traversal-cve-2026-5027-exploited.md`
- [x] **[MEDIUM]** OceanLotus Hits Vietnam Investors With SPECTRALVIPER in FireAnt Attack — `2026-06-11-oceanlotus-spectralviper-fireant-vietnam.md`
- [x] **[MEDIUM]** GitHub to Disable npm Install Scripts by Default to Stop Supply Chain Attacks — `2026-06-11-github-disables-npm-install-scripts-by-default.md`
- [x] **[MEDIUM]** Anthropic Walks Back Policy That Could Have Limited Claude for Frontier AI Researchers — `2026-06-11-anthropic-walks-back-frontier-llm-safeguard-policy.md`
- [x] **[MEDIUM]** xAI Fired Engineer Who Raised Grok Safety Concerns, Lawsuit Claims — `2026-06-10-xai-fired-engineer-grok-safety-lawsuit.md`
- [x] **[INFORMATIONAL]** Trust No Skill: Integrity Verification for AI Agent Supply Chains — `2026-06-11-trust-no-skill-ai-agent-supply-chain-integrity.md`

## Relevant (details)

### 1. Microsoft Patches Exploited Exchange Server Zero-Day CVE-2026-42897
- **Source:** SecurityWeek — https://www.securityweek.com/microsoft-patches-exploited-exchange-server-vulnerability/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `zero-day`, `vulnerability`, `microsoft`
- **Slug:** `microsoft-patches-exploited-exchange-cve-2026-42897`
- **Must-know:** yes
- **Summary:** Microsoft patched CVE-2026-42897, an Exchange Server vulnerability it warned was being exploited as a zero-day starting May 14. On-prem Exchange admins should patch immediately and check logs for prior compromise.

### 2. Max Severity Ivanti Sentry Vulnerability Now Exploited in Attacks
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/max-severity-ivanti-sentry-vulnerability-now-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `vulnerability`, `rce`, `privilege-escalation`
- **Slug:** `max-severity-ivanti-sentry-vulnerability-exploited`
- **Must-know:** no
- **Summary:** A maximum-severity, recently patched Ivanti Sentry flaw is now being exploited to gain root code execution on Internet-exposed secure mobile gateways. Unpatched internet-facing instances should be considered at risk.

### 3. Splunk, Palo Alto Networks Patch Severe Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/splunk-palo-alto-networks-patch-severe-vulnerabilities/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `appsec`
- **Slug:** `splunk-palo-alto-networks-patch-severe-vulnerabilities`
- **Must-know:** no
- **Summary:** Both vendors patched severe flaws that could let attackers create or modify arbitrary files and access or modify protected resources. No active exploitation has been reported yet.

### 4. 'GreatXML' Zero-Day Exploit Bypasses BitLocker
- **Source:** SecurityWeek — https://www.securityweek.com/greatxml-zero-day-exploit-bypasses-bitlocker/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `zero-day`, `vulnerability`, `microsoft`, `privilege-escalation`
- **Slug:** `greatxml-zero-day-bypasses-bitlocker`
- **Must-know:** no
- **Summary:** A PoC zero-day named "GreatXML" abuses Microsoft Defender's offline scan to spawn a SYSTEM shell from Windows Recovery Mode, potentially bypassing BitLocker for an attacker with physical access.

### 5. University of Nottingham Data Breach Exposes 450,000+ Records (ShinyHunters)
- **Source:** SecurityWeek — https://www.securityweek.com/university-of-nottingham-confirms-breach-after-hackers-leak-data/ (also BleepingComputer)
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `university-of-nottingham-data-breach-shinyhunters`
- **Must-know:** no
- **Summary:** ShinyHunters claimed a breach of the University of Nottingham's student records system, leaking 450,000+ email addresses and other data on current students and alumni.

### 6. Path Traversal Flaw in AI Dev Platform Langflow Exploited in Attacks (CVE-2026-5027)
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/path-traversal-flaw-in-ai-dev-platform-langflow-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `llm`, `appsec`
- **Slug:** `langflow-path-traversal-cve-2026-5027-exploited`
- **Must-know:** no
- **Summary:** Attackers are actively exploiting CVE-2026-5027, a high-severity path traversal flaw in Langflow that allows arbitrary file writes on exposed servers.

### 7. OceanLotus Hits Vietnam Investors With SPECTRALVIPER in FireAnt Attack
- **Source:** The Hacker News — https://thehackernews.com/2026/06/oceanlotus-hits-vietnam-investors-with.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`, `supply-chain`
- **Slug:** `oceanlotus-spectralviper-fireant-vietnam`
- **Must-know:** no
- **Summary:** OceanLotus's "FireAnt" campaigns deployed the SPECTRALVIPER backdoor against a Vietnamese infrastructure/transport firm and, via a supply chain attack, against domestic stock investors.

### 8. GitHub to Disable npm Install Scripts by Default to Stop Supply Chain Attacks
- **Source:** The Hacker News — https://thehackernews.com/2026/06/github-to-disable-npm-install-scripts.html
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `supply-chain`, `npm`, `github`, `devsecops`
- **Slug:** `github-disables-npm-install-scripts-by-default`
- **Must-know:** no
- **Summary:** npm v12 will disable install-script lifecycle hooks by default to combat malicious packages that auto-execute code on install, following recent campaigns like Shai-Hulud/Miasma.

### 9. Anthropic Walks Back Policy That Could Have Limited Claude for Frontier AI Researchers
- **Source:** Simon Willison (via Wired) — https://simonwillison.net/2026/Jun/11/anthropic-walks-back-policy/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-safety`, `anthropic`, `llm`
- **Slug:** `anthropic-walks-back-frontier-llm-safeguard-policy`
- **Must-know:** no
- **Summary:** After Wired reporting and public backlash, Anthropic is reversing a system-card policy where Mythos-class Claude models would silently "limit effectiveness" for users it judged to be doing frontier LLM development.

### 10. xAI Fired Engineer Who Raised Grok Safety Concerns, Lawsuit Claims
- **Source:** TechCrunch AI — https://techcrunch.com/2026/06/10/xai-fired-an-engineer-who-raised-alarms-about-grok-safety-new-lawsuit-claims/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-safety`
- **Slug:** `xai-fired-engineer-grok-safety-lawsuit`
- **Must-know:** no
- **Summary:** A former xAI engineer is suing xAI and SpaceX, claiming he was fired for raising Grok safety concerns shortly before SpaceX's IPO.

### 11. Trust No Skill: Integrity Verification for AI Agent Supply Chains
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/ai-agent-supply-chain-risks/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** informational
- **Tags:** `ai-safety`, `supply-chain`, `llm`
- **Slug:** `trust-no-skill-ai-agent-supply-chain-integrity`
- **Must-know:** no
- **Summary:** Unit 42 research on auditing third-party "skills"/plugins for enterprise AI agents to catch hidden vulnerabilities and multi-stage attack chains before deployment.

## Skippable

- **FBI Seizes 13 Websites That Officials Say Were Used by China to Target and Recruit US Workers** — SecurityWeek. Law enforcement seizure announcement, no new technical IOCs or TTPs.
- **Microsoft fixes BitLocker recovery bug on Windows Server 2025** — BleepingComputer. Reliability bug fix for a post-update boot issue, not a security vulnerability.
- **Deezer launches an AI music detector for other streaming services** — The Verge AI. Product feature launch, no security angle and not a major model release.
- **Nottingham University data breach affects over 450,000 students** — BleepingComputer. Duplicate coverage of item 5 (combined with SecurityWeek into one post).
- **Opendoor's India exit is fueling a bigger conversation about AI and outsourcing** — TechCrunch AI. Business/economic commentary on outsourcing trends, no security or technical AI substance.
- **Anthropic's Dario Amodei has just one direct report** — TechCrunch AI. Opinion/fluff piece about org structure, no news value.
- **Chinese, N. Korean Threat Groups Build on Asia-Pacific Success** — Dark Reading. General threat-landscape trend piece, no new IOCs or technical detail.
- **How an astrophysicist uses Codex to help simulate black holes** — OpenAI Blog. Marketing case study, no security angle.
- **Supporting Europe's work in ensuring a trustworthy AI ecosystem** — OpenAI Blog. Policy positioning around the EU AI Code of Practice, no concrete new regulatory action or technical detail.
- **Profiling in PyTorch (Part 2): From nn.Linear to a Fused MLP** — Hugging Face Blog. ML performance deep-dive, no security angle.
- **datasette-agent 0.2a0** — Simon Willison. Minor open-source alpha release for a niche tool, no security angle.
