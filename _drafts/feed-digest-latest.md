# Digest — 2026-06-19 AM

- Window: last 14h
- Raw items considered: 17
- Relevant: 8
- Skippable: 9

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** FortiBleed Leak Exposes ~74,000 Fortinet Credentials, CISA Warns — `2026-06-19-fortibleed-fortinet-credentials-leak-cisa-warning.md`
- [x] **[CRITICAL]** Salesforce Disables Klue Integration After OAuth Token Abuse Exposes Customer Data — `2026-06-19-klue-supply-chain-attack-salesforce.md`
- [x] **[CRITICAL]** Splunk Enterprise RCE Flaw Exploited Days After Disclosure — `2026-06-19-splunk-enterprise-rce-actively-exploited.md`
- [x] **[HIGH]** Gentlemen Ransomware Deploys Multiple EDR Killers to Blind Defenses — `2026-06-18-gentlemen-ransomware-edr-killers.md`
- [x] **[HIGH]** Apple Patches Beats Studio Buds Bluetooth Flaw Enabling Nearby Eavesdropping — `2026-06-19-apple-beats-studio-buds-bluetooth-flaw.md`
- [x] **[MEDIUM]** Operation Endgame Takes Down SocGholish Botnet, Cleans 15,000 WordPress Sites — `2026-06-19-socgholish-botnet-takedown.md`
- [x] **[INFORMATIONAL]** Datasette Apps Lets You Run Sandboxed HTML Apps Against Your Data — `2026-06-18-datasette-apps-sandboxed-launch.md`

## Relevant (details)

### 1. FortiBleed Leak Exposes ~74,000 Fortinet Credentials, CISA Warns
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cisa-warns-fortinet-users-to-secure-devices-after-fortibleed-leak/
- **Severity:** critical
- **Tags:** `data-breach`, `iam`, `fortinet`
- **Summary:** A leak dubbed "FortiBleed" exposed nearly 74,000 Fortinet firewall/VPN credentials; CISA is urging customers to secure devices and rotate credentials immediately.

### 2. Salesforce Disables Klue Integration After OAuth Token Abuse Exposes Customer Data
- **Source:** The Hacker News — https://thehackernews.com/2026/06/salesforce-disables-klue-app.html
- **Severity:** critical
- **Tags:** `supply-chain`, `data-breach`
- **Summary:** Salesforce disabled the Klue Battlecards integration after OAuth tokens were abused to exfiltrate data from customer Salesforce instances, including Huntress and Recorded Future.

### 3. Splunk Enterprise RCE Flaw Exploited Days After Disclosure
- **Source:** SecurityWeek — https://www.securityweek.com/splunk-enterprise-vulnerability-exploited-in-attacks-days-after-disclosure/
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `rce`
- **Summary:** CVE-2026-20253, a critical unauthenticated RCE in Splunk Enterprise, is being actively exploited days after disclosure; CISA gave federal agencies a three-day patch deadline.

### 4. Gentlemen Ransomware Deploys Multiple EDR Killers to Blind Defenses
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/gentlemen-ransomware-uses-multiple-edr-killers-to-disable-defenses/
- **Severity:** high
- **Tags:** `ransomware`, `malware`
- **Summary:** The Gentlemen RaaS operation maintains multiple EDR-killer tools to disable endpoint defenses before deploying ransomware, hedging against any single tool being blocked.

### 5. Apple Patches Beats Studio Buds Bluetooth Flaw Enabling Nearby Eavesdropping
- **Source:** The Hacker News — https://thehackernews.com/2026/06/apple-patches-beats-studio-buds-flaw.html
- **Severity:** high
- **Tags:** `vulnerability`, `cve`
- **Summary:** CVE-2025-20701 (CVSS 8.8) in the Airoha Bluetooth audio SDK let nearby attackers pair with Beats Studio Buds without consent and eavesdrop via the microphone; Apple has patched it.

### 6. Operation Endgame Takes Down SocGholish Botnet, Cleans 15,000 WordPress Sites
- **Source:** SecurityWeek — https://www.securityweek.com/15000-wordpress-websites-cleaned-up-in-socgholish-botnet-takedown/
- **Severity:** medium
- **Tags:** `malware`
- **Summary:** Law enforcement and partners took down 106 SocGholish C2 servers/domains under Operation Endgame, cleaning up roughly 15,000 compromised WordPress sites.

### 7. Datasette Apps Lets You Run Sandboxed HTML Apps Against Your Data
- **Source:** Simon Willison — https://simonwillison.net/2026/Jun/18/datasette-apps/#atom-everything
- **Severity:** informational
- **Tags:** `appsec`, `llm`
- **Summary:** Datasette launched a plugin that runs self-contained HTML/JS apps inside an iframe sandbox, restricted to read-only SQL by default — a useful pattern for safely embedding untrusted or AI-generated frontend code.

## Skippable

- **FortiBleed: 86,000 Fortinet Device Credentials Compromised** — SecurityWeek. Duplicate coverage of the FortiBleed leak; see the BleepingComputer/CISA version above.
- **CISA: Splunk Enterprise flaw actively exploited, patch by Sunday** — BleepingComputer. Duplicate coverage of the Splunk RCE story; SecurityWeek version above has the CVE ID.
- **NY man charged after harassing college student with AI-generated nudes** — BleepingComputer. Regional individual harassment case, no broader technical or policy angle.
- **The US says ASML's top chip tool may be in China. ASML says it isn't** — TechCrunch AI. Geopolitical/export-control dispute, no security or AI-launch substance.
- **Cisco to Acquire WideField Security to Boost Splunk's Agentic SOC** — SecurityWeek. M&A announcement, not a tool release with technical detail.
- **Barret Zoph is out at OpenAI again after just five months** — The Verge AI. Personnel/executive departure, no model or safety news value.
- **Source: Elastic agrees to buy CRV-backed DeductiveAI for up to $85M** — TechCrunch AI. Acquisition/funding news, no new capability or security substance.
- **Announcing Amazon EC2 G7 instances accelerated by NVIDIA RTX PRO 4500 Blackwell Server Edition GPUs** — AWS News Blog. Generic GPU instance launch, no security implications.
- **AI inference startup Baseten reportedly raising $1.5B months after its last mega-round** — TechCrunch AI. Funding round news, not a model or capability launch.
