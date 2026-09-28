# Digest — 2026-09-28 PM

- Window: last 14h
- Raw items considered: 26
- Relevant: 10
- Skippable: 16

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Citrix Confirms Two NetScaler Zero-Days Under Active Exploitation — `2026-09-28-citrix-netscaler-zero-days-cve-2026-88771-88772.md`
- [x] **[CRITICAL]** Bitget Resumes Bitcoin Withdrawals After $387.5 Million Crypto Heist — `2026-09-28-bitget-387-million-crypto-heist.md`
- [x] **[HIGH]** 80,000+ Organizations Had AI Logins Stolen: From Shadow AI to LLMjacking — `2026-09-28-80000-organizations-ai-logins-stolen.md`
- [x] **[HIGH]** Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes AI Agent — `2026-09-28-carbonato-botnet-docker-hermes-ai-agent.md`
- [x] **[HIGH]** DC Health Agency Exposes 400,000 Beneficiary Records — `2026-09-28-dc-health-agency-exposes-400000-records.md`
- [x] **[HIGH]** Google Warns of ShinyHunters' Fresh Oracle PeopleSoft Campaign — `2026-09-28-shinyhunters-oracle-peoplesoft-cve-2026-35273.md`
- [x] **[HIGH]** JADEPUFFER-Linked Attackers Used Compromised Service Principals to Delete Azure Resources — `2026-09-28-jadepuffer-azure-service-principals-destructive.md`
- [x] **[MEDIUM]** Kiteworks Urges Server Shutdown, Finds Advanced Forms Vulnerability — `2026-09-28-kiteworks-server-shutdown-forms-vulnerability.md`
- [x] **[INFORMATIONAL]** Nvidia Unveils AI Agent Safety Platform With Hardware-Based Watchdog — `2026-09-28-nvidia-ai-agent-safety-platform.md`
- [x] **[INFORMATIONAL]** Holo4: Powering Generalist Computer-Use Agents — `2026-09-28-holo4-computer-use-agents.md`

## Relevant (details)

### 1. Citrix Confirms Two NetScaler Zero-Days Under Active Exploitation
- **Source:** The Hacker News, SecurityWeek, BleepingComputer
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `vulnerability`
- **Summary:** CISA added CVE-2026-88771 (CVSS 9.5) and CVE-2026-88772, two critical NetScaler ADC/Gateway flaws, to its KEV catalog after confirming active exploitation. Citrix has patches available and CISA has ordered federal agencies to patch by Wednesday.

### 2. Bitget Resumes Bitcoin Withdrawals After $387.5 Million Crypto Heist
- **Source:** BleepingComputer
- **Severity:** critical
- **Tags:** `malware`, `cryptocurrency`
- **Summary:** Bitget resumed withdrawals after suspected North Korean hackers stole over $350M (reported as $387.5M) from the exchange last week.

### 3. 80,000+ Organizations Had AI Logins Stolen: From Shadow AI to LLMjacking
- **Source:** BleepingComputer
- **Severity:** high
- **Tags:** `data-breach`, `malware`, `llm`, `ai-safety`
- **Summary:** Infostealer logs exposed AI credentials/sessions tied to 80,000+ corporate domains per SOCRadar, driven by shadow AI usage and a growing market for LLMjacking.

### 4. Carbonato Botnet Compromises Docker Hosts to Deploy Telegram-Controlled Hermes AI Agent
- **Source:** The Hacker News
- **Severity:** high
- **Tags:** `malware`, `container-security`, `llm`, `ai-safety`
- **Summary:** New botnet targets exposed Docker daemons and deploys the unmodified open-source Hermes Agent framework, overwriting its persona file with a prompt that takes commands over Telegram.

### 5. DC Health Agency Exposes 400,000 Beneficiary Records
- **Source:** SecurityWeek
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** A DC health agency exposed Medicaid IDs and other personal data for roughly 400,000 beneficiaries; details on cause are thin.

### 6. Google Warns of ShinyHunters' Fresh Oracle PeopleSoft Campaign
- **Source:** SecurityWeek
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `data-breach`
- **Summary:** ShinyHunters modified its exploit for PeopleSoft CVE-2026-35273 in a new attack wave, per Google.

### 7. JADEPUFFER-Linked Attackers Used Compromised Service Principals to Delete Azure Resources
- **Source:** The Hacker News
- **Severity:** high
- **Tags:** `azure`, `cloud-security`, `privilege-escalation`
- **Summary:** JADEPUFFER (Microsoft's Storm-3168) used compromised Azure service principals to delete resources over an 18-hour destructive operation in June 2026.

### 8. Kiteworks Urges Server Shutdown, Finds Advanced Forms Vulnerability
- **Source:** SecurityWeek
- **Severity:** medium
- **Tags:** `vulnerability`, `appsec`
- **Summary:** Kiteworks urged a precautionary server shutdown after finding a vulnerability in its Advanced Forms feature; no evidence of compromise so far.

### 9. Nvidia Unveils AI Agent Safety Platform With Hardware-Based Watchdog
- **Source:** SecurityWeek, The Verge
- **Severity:** informational
- **Tags:** `ai-safety`, `ai-launch`
- **Summary:** Nvidia launched an Open Agent Safety Platform combining open source software and a hardware-based watchdog to quarantine rogue AI agents within milliseconds, in response to a wave of agent-hacking incidents.

### 10. Holo4: Powering Generalist Computer-Use Agents
- **Source:** Hugging Face Blog
- **Severity:** informational
- **Tags:** `ai-launch`, `model-release`, `llm`
- **Summary:** Hugging Face published a model release for Holo4, aimed at powering generalist computer-use agents. Feed provided no further detail.

## Skippable

- **Modulate raises $25M for its voice models and analysis suite** — TechCrunch AI. Funding announcement, no security news value.
- **Weekly Recap: $387M Crypto Hack, Citrix Exploits, AI Agents Go Off-Script** — The Hacker News. Aggregation/recap of stories already covered individually.
- **Your final chance to grab your exhibit table at TechCrunch Disrupt 2026** — TechCrunch AI. Event marketing.
- **Insuretech Outmarket raises $34.5M** — TechCrunch AI. Funding announcement, no security angle.
- **The SaaSpocalypse that wasn't, with Atlassian CEO Mike Cannon-Brookes** — The Verge AI. Podcast/opinion, no news value.
- **Viral AI agent Instinct raises $1B Series C** — TechCrunch AI. Funding announcement, no security angle.
- **Nvidia says its new AI safety platform can contain rogue agents within 'milliseconds'** — The Verge AI. Duplicate coverage, merged into item 9 above.
- **Cyberattack on Polish medical software provider exposes patient data** — The Record. Regional breach without technical substance.
- **Former US soldier gets nearly six-year sentence for hacking, extorting telecoms** — The Record. Duplicate coverage of the same sentencing; legal outcome, no new technical substance.
- **Prison Sentence for Former US Soldier Who Hacked AT&T and Verizon** — SecurityWeek. Duplicate coverage of same sentencing story.
- **Webinar: How to Govern AI Agents, Reduce Excessive Access, and Control Shadow AI** — The Hacker News. Vendor webinar promotion.
- **New Mexico Jury Finds Facebook Liable for Deceiving Users About Privacy Protections** — SecurityWeek. Legal ruling without technical security substance.
- **US soldier gets 70 months in prison for extorting 10 tech, telecom firms** — BleepingComputer. Duplicate coverage of same sentencing story (best detail, but still a routine legal outcome, no TTPs/IOCs).
- **Citrix Confirms 2 NetScaler Zero-Days After Admins Pulled the Plug** — SecurityWeek. Duplicate coverage, merged into item 1 above.
- **CISA orders feds to patch exploited Citrix flaws by Wednesday** — BleepingComputer. Duplicate coverage, merged into item 1 above.
- **Quoting Muse AI Agent** — Simon Willison. Single anecdotal quote about an AI agent's auto-reply mishap; no broader technical or news substance.
