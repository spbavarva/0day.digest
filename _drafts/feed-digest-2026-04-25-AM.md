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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `malware`, `vulnerability`, `cisco`
- **Slug:** `2026-04-24-firestarter-malware-cisco-firewall-persistence`
- **Must-know:** no
- **Summary:** US and UK agencies have issued a joint warning about Firestarter, a custom implant that persists on Cisco Firepower/ASA/FTD devices even after patches and firmware updates. Patch application alone is insufficient — organizations must verify device integrity against the advisory's indicators and treat suspected compromises as active incidents requiring full response.

### 2. CISA Adds 4 Actively Exploited CVEs to KEV
- **Source:** The Hacker News — https://thehackernews.com/2026/04/cisa-adds-4-exploited-flaws-to-kev-sets.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `zero-day`
- **Slug:** `2026-04-25-cisa-kev-simplehelp-samsung-dlink`
- **Must-know:** no
- **Summary:** CISA added four actively exploited flaws to KEV: CVE-2024-57726 (CVSS 9.9, missing auth in SimpleHelp), plus vulnerabilities in Samsung MagicINFO 9 Server and D-Link DIR-823X routers. Federal agencies have a May 2026 deadline; the SimpleHelp flaw is especially critical for MSP-hosted environments.

### 3. ADT Confirms Data Breach After ShinyHunters Threatens to Leak Stolen Data
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/adt-confirms-data-breach-after-shinyhunters-leak-threat/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `ransomware`
- **Slug:** `2026-04-24-adt-data-breach-shinyhunters`
- **Must-know:** no
- **Summary:** ADT confirmed a breach after ShinyHunters threatened to release stolen customer data unless paid. ADT has millions of residential and commercial customers; the scope of data affected has not been fully disclosed. ShinyHunters has a history of large-scale breaches used for follow-on phishing.

### 4. Unit 42 Maps npm Attack Surface Post-Shai Hulud
- **Source:** Unit 42 (Palo Alto) — https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `supply-chain`, `npm`, `malware`, `appsec`, `devsecops`
- **Slug:** `2026-04-24-npm-threat-landscape-unit42`
- **Must-know:** no
- **Summary:** Unit 42's analysis identifies wormable npm malware with CI/CD persistence, multi-stage attack chains, and propagation across developer environments. Organizations that pulled recently compromised packages should treat connected environments as potentially pivoted, not just patched.

### 5. BlackFile: New Extortion Group Targets Retail and Hospitality via Vishing
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-blackfile-extortion-gang-targets-retail-and-hospitality-orgs/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `ransomware`, `phishing`, `data-breach`
- **Slug:** `2026-04-24-blackfile-extortion-vishing-retail`
- **Must-know:** no
- **Summary:** BlackFile has been conducting data theft and extortion against retail and hospitality organizations since February 2026 using vishing as its primary initial access technique. The social engineering-heavy playbook mirrors Scattered Spider; affected sectors should reinforce helpdesk verification procedures and MFA fatigue mitigations.

### 6. US Officials: Iran's Cyber Threat Is 'Low and Slow'
- **Source:** The Record (Recorded Future) — https://therecord.media/iran-cyber-warfare-haugh
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `threat-intel`
- **Slug:** `2026-04-24-iran-cyber-threat-low-and-slow`
- **Must-know:** no
- **Summary:** US officials assess Iran's most likely cyber threat posture as quiet opportunistic intrusion rather than destructive campaigns, favoring deniability and long-term access. Defenders should prioritize detection of low-noise lateral movement rather than preparing exclusively for wiper-style attacks.

### 7. Microsoft Rolls Out Entra Passkeys for Phishing-Resistant Auth
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-to-roll-out-entra-passkeys-on-windows-in-late-april/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `iam`, `microsoft`, `phishing`
- **Slug:** `2026-04-24-microsoft-entra-passkeys`
- **Must-know:** no
- **Summary:** Microsoft is deploying Windows-bound passkeys for Entra-protected resources starting late April, enabling phishing-resistant passwordless auth that cannot be replayed. Security teams should update Conditional Access policies to require phishing-resistant MFA and plan for shared device and service account edge cases.

### 8. Google Commits Up to $40B in Anthropic
- **Source:** TechCrunch AI — https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `anthropic`, `google`, `ai-launch`, `llm`
- **Slug:** `2026-04-24-google-40b-investment-anthropic`
- **Must-know:** no
- **Summary:** Google is committing up to $40B in Anthropic through cash and compute following the Mythos cybersecurity model launch. The investment will likely accelerate availability of Mythos-powered capabilities through Google Cloud's security product line.

### 9. AWS Post-Quantum Cryptography Migration Guide
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/protecting-your-secrets-from-tomorrows-quantum-risks/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `cloud-security`, `aws`, `cryptography`
- **Slug:** `2026-04-24-aws-post-quantum-cryptography`
- **Must-know:** no
- **Summary:** AWS published guidance on client-side PQC migration addressing the harvest-now-decrypt-later threat model. Organizations in regulated industries with long data retention requirements should begin migrating TLS and key exchange to NIST-standardized PQC algorithms now.

## Skippable

- **GPT-5.5 prompting guide** — Simon Willison. Tips and tricks post for a model already covered; no new security angle.
- **llm 0.31** — Simon Willison. Minor CLI tool version bump adding GPT-5.5 support; not substantive enough for a post.
- **The people do not yearn for automation** — Simon Willison. Opinion/commentary essay on AI attitudes; no news value.
- **Meta's loss is Thinking Machines' gain** — TechCrunch AI. Talent transfer gossip between Meta and Thinking Machines Lab; no security angle.
- **TGR-STA-1030: New Activity in Central and South America** — Unit 42. Thin summary on a regional threat actor; insufficient detail to draft a useful post.
- **Windows Update gets new controls to reduce forced restarts** — BleepingComputer. Generic Windows feature rollout; no security angle.
- **ComfyUI hits $500M valuation** — TechCrunch AI. AI image generation funding news; no security angle.
- **8 Gemini tips for organizing your space** — Google AI Blog. Marketing/productivity lifestyle content; no security angle.
- **ADT says customer data stolen in cyber intrusion** — The Record. Duplicate coverage of the ADT breach; BleepingComputer item (item 4) used as primary source.
