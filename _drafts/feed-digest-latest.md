# Digest — 2026-04-25 AM

- Window: last 14h
- Raw items considered: 18
- Relevant: 9
- Skippable: 9

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Firestarter: State-Sponsored Malware Survives Patches on Cisco ASA and FTD Firewalls — `2026-04-24-firestarter-malware-cisco-firewall-persistence.md`
- [x] **[HIGH]** CISA Adds 4 Actively Exploited CVEs to KEV: SimpleHelp, Samsung MagicINFO, D-Link Routers — `2026-04-25-cisa-kev-simplehelp-samsung-dlink.md`
- [x] **[HIGH]** ADT Confirms Data Breach After ShinyHunters Threatens to Leak Stolen Data — `2026-04-24-adt-data-breach-shinyhunters.md`
- [x] **[HIGH]** Unit 42 Maps npm Attack Surface: Wormable Malware, CI/CD Persistence, and Multi-Stage Chains — `2026-04-24-npm-threat-landscape-unit42.md`
- [x] **[HIGH]** BlackFile: New Extortion Group Targets Retail and Hospitality via Vishing Since February 2026 — `2026-04-24-blackfile-extortion-vishing-retail.md`
- [x] **[MEDIUM]** US Officials: Iran's Cyber Threat Is 'Low and Slow,' Not Shock and Awe — `2026-04-24-iran-cyber-threat-low-and-slow.md`
- [x] **[MEDIUM]** Microsoft Rolls Out Entra Passkeys on Windows for Phishing-Resistant Auth in Late April — `2026-04-24-microsoft-entra-passkeys.md`
- [x] **[INFORMATIONAL]** Google Commits Up to $40B in Anthropic Investment Amid Cybersecurity AI Race — `2026-04-24-google-40b-investment-anthropic.md`
- [x] **[INFORMATIONAL]** AWS Publishes Post-Quantum Cryptography Migration Guide: Addressing Harvest Now, Decrypt Later — `2026-04-24-aws-post-quantum-cryptography.md`

## Relevant (details)

### 1. Firestarter: State-Sponsored Malware Survives Patches on Cisco ASA and FTD Firewalls
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/firestarter-malware-survives-cisco-firewall-updates-security-patches/
- **Severity:** critical
- **Tags:** `malware`, `vulnerability`, `cisco`
- **Summary:** US and UK agencies issued a joint warning about Firestarter, a custom implant persisting on Cisco Firepower/ASA/FTD devices even after patches and firmware updates. Patch application alone is insufficient — organizations must verify device integrity and treat suspected compromises as active incidents.

### 2. CISA Adds 4 Actively Exploited CVEs to KEV
- **Source:** The Hacker News — https://thehackernews.com/2026/04/cisa-adds-4-exploited-flaws-to-kev-sets.html
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `zero-day`
- **Summary:** CISA added four actively exploited flaws to KEV: CVE-2024-57726 (CVSS 9.9, missing auth in SimpleHelp), plus flaws in Samsung MagicINFO 9 Server and D-Link DIR-823X routers. Federal agencies have a May 2026 deadline; the SimpleHelp flaw is especially critical for MSP environments.

### 3. ADT Confirms Data Breach After ShinyHunters Threatens to Leak Stolen Data
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/adt-confirms-data-breach-after-shinyhunters-leak-threat/
- **Severity:** high
- **Tags:** `data-breach`, `ransomware`
- **Summary:** ADT confirmed a breach after ShinyHunters threatened to release stolen customer data unless paid. ADT has millions of residential and commercial customers; full scope of affected data has not been disclosed.

### 4. Unit 42 Maps npm Attack Surface Post-Shai Hulud
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `malware`, `appsec`, `devsecops`
- **Summary:** Unit 42's analysis identifies wormable npm malware with CI/CD persistence and multi-stage attack chains propagating across developer environments. Environments that pulled compromised packages should be treated as potentially pivoted, not just patched.

### 5. BlackFile: New Extortion Group Targets Retail and Hospitality via Vishing
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-blackfile-extortion-gang-targets-retail-and-hospitality-orgs/
- **Severity:** high
- **Tags:** `ransomware`, `phishing`, `data-breach`
- **Summary:** BlackFile has conducted data theft and extortion against retail and hospitality organizations since February 2026 using vishing as its primary initial access technique. The social engineering playbook mirrors Scattered Spider; affected sectors should reinforce helpdesk verification and MFA fatigue mitigations.

### 6. US Officials: Iran's Cyber Threat Is 'Low and Slow'
- **Source:** The Record (Recorded Future) — https://therecord.media/iran-cyber-warfare-haugh
- **Severity:** medium
- **Tags:** `threat-intel`
- **Summary:** US officials assess Iran's most likely cyber posture as quiet opportunistic intrusion rather than destructive attacks, favoring long-term access and deniability. Defenders should prioritize detection of low-noise lateral movement.

### 7. Microsoft Rolls Out Entra Passkeys for Phishing-Resistant Auth
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-to-roll-out-entra-passkeys-on-windows-in-late-april/
- **Severity:** medium
- **Tags:** `iam`, `microsoft`, `phishing`
- **Summary:** Microsoft is deploying Windows-bound passkeys for Entra-protected resources starting late April, enabling phishing-resistant passwordless authentication. Security teams should update Conditional Access policies and plan for shared device and service account edge cases.

### 8. Google Commits Up to $40B in Anthropic
- **Source:** TechCrunch AI — https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/
- **Severity:** informational
- **Tags:** `anthropic`, `google`, `ai-launch`, `llm`
- **Summary:** Google is committing up to $40B in Anthropic through cash and compute following the Mythos cybersecurity model launch. The investment will likely accelerate Mythos-powered capabilities through Google Cloud's security product line.

### 9. AWS Post-Quantum Cryptography Migration Guide
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/protecting-your-secrets-from-tomorrows-quantum-risks/
- **Severity:** informational
- **Tags:** `cloud-security`, `aws`, `cryptography`
- **Summary:** AWS published guidance on client-side PQC migration addressing the harvest-now-decrypt-later threat model. Organizations with long data retention requirements should begin migrating to NIST-standardized PQC algorithms now.

## Skippable

- **GPT-5.5 prompting guide** — Simon Willison. Tips post for a model already covered; no new security angle.
- **llm 0.31** — Simon Willison. Minor CLI version bump adding GPT-5.5 support; not substantive.
- **The people do not yearn for automation** — Simon Willison. Opinion essay on AI attitudes; no news value.
- **Meta's loss is Thinking Machines' gain** — TechCrunch AI. Talent transfer gossip; no security angle.
- **TGR-STA-1030: New Activity in Central and South America** — Unit 42. Thin summary on regional threat actor; insufficient detail.
- **Windows Update gets new controls to reduce forced restarts** — BleepingComputer. Generic Windows feature; no security angle.
- **ComfyUI hits $500M valuation** — TechCrunch AI. AI image generation funding news; no security angle.
- **8 Gemini tips for organizing your space** — Google AI Blog. Marketing/productivity content; no security angle.
- **ADT says customer data stolen in cyber intrusion** — The Record. Duplicate of the ADT breach item; BleepingComputer used as primary.
