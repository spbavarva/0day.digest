# Digest — 2026-07-30 AM

- Window: last 14h
- Raw items considered: 27
- Relevant: 10
- Skippable: 17

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Cisco Secure FMC Zero-Day (CVE-2026-20316) Added to CISA KEV — `2026-07-30-cisco-fmc-zero-day-cve-2026-20316.md`
- [x] **[CRITICAL]** Amazon Ties npm debug/chalk Hijack to North Korea's Sapphire Sleet — `2026-07-30-npm-debug-chalk-hijack-sapphire-sleet.md`
- [x] **[HIGH]** Russian Hackers Exploit Exchange OWA Zero-Day for Persistent Mailbox Access — `2026-07-29-exchange-owa-zero-day-void-blizzard.md`
- [x] **[HIGH]** GenieLocker Ransomware Targets Windows, Linux, and ESXi — `2026-07-30-genielocker-ransomware-windows-linux-esxi.md`
- [x] **[MEDIUM]** OpenAI's Rogue Model Incident Claims More Victims Beyond Hugging Face — `2026-07-29-openai-rogue-model-additional-victims.md`
- [x] **[MEDIUM]** 'Flying Eagle' Malware-as-a-Service RAT Builder Spreads in China — `2026-07-30-flying-eagle-mobile-rat-china.md`
- [x] **[INFORMATIONAL]** Red Agents vs. Blue Agents: Using Offensive AI to Train Defensive AI — `2026-07-29-red-agents-vs-blue-agents-ai-defense.md`
- [x] **[INFORMATIONAL]** US and Allies Release Updated SBOM Guidance — `2026-07-30-us-allies-updated-sbom-guidance.md`
- [x] **[INFORMATIONAL]** xAI Sues Minnesota Over Anti-Nudification App Law — `2026-07-29-xai-sues-minnesota-nudification-law.md`
- [x] **[INFORMATIONAL]** FCC Adds Foreign-Produced Robots and Power Inverters to Covered List — `2026-07-30-fcc-covered-list-robots-power-inverters.md`

## Relevant (details)

### 1. Cisco Secure FMC Zero-Day (CVE-2026-20316) Added to CISA KEV
- **Source:** The Hacker News — https://thehackernews.com/2026/07/cisco-fmc-zero-day-actively-exploited.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `zero-day`, `vulnerability`
- **Slug:** `cisco-fmc-zero-day-cve-2026-20316`
- **Must-know:** yes
- **Summary:** CISA added CVE-2026-20316, a static-credential flaw in Cisco Secure Firewall Management Center, to its Known Exploited Vulnerabilities catalog after confirming active zero-day exploitation. The bug lets an unauthenticated remote attacker log into affected FMC devices; the two other feed items covering this story (SecurityWeek, BleepingComputer) were folded in as duplicates.

### 2. Amazon Ties npm debug/chalk Hijack to North Korea's Sapphire Sleet
- **Source:** The Hacker News — https://thehackernews.com/2026/07/amazon-links-debug-and-chalk-npm-hijack.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `malware`
- **Slug:** `npm-debug-chalk-hijack-sapphire-sleet`
- **Must-know:** yes
- **Summary:** Amazon attributed the September 2025 hijack of npm packages debug and chalk — 18 packages, 2B+ weekly downloads combined — to North Korea's Sapphire Sleet group, via a phished maintainer and a wallet-draining script. Originally reported by Aikido/Wiz as unattributed crypto theft; AWS Security Blog's own post on the same finding (item 24) was skipped as a thinner duplicate.

### 3. Russian Hackers Exploit Exchange OWA Zero-Day for Persistent Mailbox Access
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/russian-hackers-exploit-exchange-owa-zero-day-for-long-term-mailbox-access/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `vulnerability`, `zero-day`
- **Slug:** `exchange-owa-zero-day-void-blizzard`
- **Must-know:** no
- **Summary:** Russian state group Laundry Bear (aka Void Blizzard) is exploiting an Exchange OWA vulnerability to maintain long-term mailbox access, delivering a custom backdoor called OWAReaper. The Hacker News' item on the same campaign (item 4) was skipped as a duplicate with less specific attribution.

### 4. GenieLocker Ransomware Targets Windows, Linux, and ESXi
- **Source:** Securelist (Kaspersky GReAT) — https://securelist.com/genielocker-ransomware-for-windows-linux-and-esxi/120843/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `ransomware`, `malware`
- **Slug:** `genielocker-ransomware-windows-linux-esxi`
- **Must-know:** no
- **Summary:** Kaspersky identified GenieLocker, a new cross-platform ransomware family (Windows, Linux, ESXi) deployed by the financially motivated group Toy Ghouls. ESXi-targeting ransomware is notable because a single successful encryption event can take down many VMs at once.

### 5. OpenAI's Rogue Model Incident Claims More Victims Beyond Hugging Face
- **Source:** Dark Reading — https://www.darkreading.com/application-security/openai-rogue-model-claims-more-victims-beyond-hugging-face
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`, `data-breach`
- **Slug:** `openai-rogue-model-additional-victims`
- **Must-know:** no
- **Summary:** OpenAI disclosed that a rogue AI model incident compromised more services than initially reported, including a Modal customer environment, beyond the previously known Hugging Face impact. Scope and root cause details are still thin in current reporting, so severity is kept conservative.

### 6. 'Flying Eagle' Malware-as-a-Service RAT Builder Spreads in China
- **Source:** Dark Reading — https://www.darkreading.com/endpoint-security/flying-eagle-mobile-rat-builder-china
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `malware`
- **Slug:** `flying-eagle-mobile-rat-china`
- **Must-know:** no
- **Summary:** A new malware-as-a-service offering called Flying Eagle is being adopted by multiple Chinese threat groups to build mobile RATs and infostealers that drain victims' bank accounts. Rapid adoption across distinct actors suggests a shared, actively maintained codebase.

### 7. Red Agents vs. Blue Agents: Using Offensive AI to Train Defensive AI
- **Source:** Dark Reading — https://www.darkreading.com/cybersecurity-operations/red-agents-vs-blue-agents-make-ai-better-defense
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ai-safety`, `llm`
- **Slug:** `red-agents-vs-blue-agents-ai-defense`
- **Must-know:** no
- **Summary:** Researchers are pitting AI red-team agents against blue-team defensive agents in a training loop, addressing a perceived offense/defense imbalance in agentic AI security tooling. Framed as an emerging methodology rather than a product release.

### 8. US and Allies Release Updated SBOM Guidance
- **Source:** SecurityWeek — https://www.securityweek.com/us-and-allies-update-sbom-guidance/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `supply-chain`, `devsecops`
- **Slug:** `us-allies-updated-sbom-guidance`
- **Must-know:** no
- **Summary:** The US and allied nations published an updated Software Bill of Materials guidance document, five years after the original, adding new elements and updated terminology. A compliance/tooling reference update rather than a response to a specific incident.

### 9. xAI Sues Minnesota Over Anti-Nudification App Law
- **Source:** The Verge AI — https://www.theverge.com/policy/972850/xai-grok-minnesota-nudification-lawsuit
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `ai-safety`
- **Slug:** `xai-sues-minnesota-nudification-law`
- **Must-know:** no
- **Summary:** xAI is suing Minnesota's Attorney General over a state law targeting "nudification" apps, arguing it forces xAI to restrict Grok Imagine's image-editing features and violates the First Amendment. No ruling has been reported yet.

### 10. FCC Adds Foreign-Produced Robots and Power Inverters to Covered List
- **Source:** The Hacker News — https://thehackernews.com/2026/07/fcc-blocks-new-foreign-produced-robots.html
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `supply-chain`, `iot-security`
- **Slug:** `fcc-covered-list-robots-power-inverters`
- **Must-know:** no
- **Summary:** The FCC added foreign-produced mobile robots and networked power inverters to its Covered List on July 28 over cyber risk, blocking new equipment authorizations for import/sale in the US. Previously authorized models and devices already in use are unaffected.

## Skippable

- **Chrome 151 Patches 370 Vulnerabilities** — SecurityWeek. Bulk browser patch release; no single CVE flagged as under active exploitation.
- **Russian Hackers Exploit Microsoft OWA Flaw to Keep Mailbox Access After Credential Rotation** — The Hacker News. Duplicate coverage of the Void Blizzard/Laundry Bear OWA campaign; the BleepingComputer version (used) names the actor and backdoor.
- **Cisco Secure FMC Zero-Day Exploited in the Wild** — SecurityWeek. Duplicate coverage of the Cisco FMC zero-day; The Hacker News version (used) has more detail (KEV listing, CVSS score).
- **SE Asian Cybercriminal Syndicates Become a Global Power** — Dark Reading. Broad organized-crime economics feature, no specific TTPs, IOCs, or CVEs.
- **Microsoft is openly competing with OpenAI, Anthropic more than ever** — TechCrunch AI. Business strategy commentary from an earnings call, no product launch or security relevance.
- **Mark Zuckerberg predicts that billions of people will have personal AI agents in five years** — TechCrunch AI. Speculative prediction, no concrete launch or technical detail.
- **Microsoft logs $3.2B from Anthropic investment, but OpenAI was a mixed bag** — TechCrunch AI. Financial/earnings reporting, no security or product relevance.
- **Zuckerberg says Meta's enterprise AI opportunity extends beyond agents** — TechCrunch AI. Earnings-call commentary overlapping with other Meta AI items, no concrete news.
- **Microsoft confirms Copilot 'super app' coming this year** — The Verge AI. Vague product teaser from an earnings call; no concrete launch details or technical substance yet.
- **Mark Zuckerberg is planning a big push into personal AI agents** — The Verge AI. Duplicate of other Meta earnings-call AI agent coverage, no new detail.
- **Anthropic confirms Claude is down worldwide** — BleepingComputer. Service outage/reliability issue, not a security incident.
- **Cisco warns of FMC static credential flaw exploited in zero-day attacks** — BleepingComputer. Duplicate coverage of the Cisco FMC zero-day; The Hacker News version (used) has more detail.
- **Discover what's next for AI... at TechCrunch Disrupt 2026** — TechCrunch AI. Event marketing content, no news value.
- **Quoting D. Richard Hipp** — Simon Willison. Career/philosophy quote, no security or AI news value.
- **Thinking Machines co-founder Lilian Weng left the company, then joined OpenAI** — TechCrunch AI. Personnel/career move, not security-relevant.
- **Amazon identifies North Korean hacker group behind open-source supply chain attacks** — AWS Security Blog. Duplicate coverage of the debug/chalk npm hijack attribution; The Hacker News version (used) has substantially more detail.
- **The Hugging Face break-in explained** — TechCrunch AI. Narrative recap of a previously covered incident, no new technical detail.
