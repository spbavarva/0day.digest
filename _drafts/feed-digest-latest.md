# Digest — 2026-08-04 AM

- Window: last 14h
- Raw items considered: 17
- Relevant: 8
- Skippable: 9

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** 150,000 Impacted by Madera Community Hospital Data Breach — `2026-08-04-madera-community-hospital-data-breach.md`
- [x] **[HIGH]** CISA Adds Exploited N-able N-central Flaw to KEV After Customer Compromises — `2026-08-04-n-able-n-central-kev-active-exploitation.md`
- [x] **[HIGH]** Hotel Wi-Fi Attacks Use Custom Malware to Breach Microsoft 365 Accounts — `2026-08-04-hotel-wifi-apt29-microsoft-365-attacks.md`
- [x] **[HIGH]** New Pass-ta-key Attacks Let Malware Hijack Google-Synced Passkeys — `2026-08-03-pass-ta-key-google-passkey-hijack.md`
- [x] **[INFORMATIONAL]** New Tool Traces AI Videos Back to Their Source — `2026-08-03-ai-video-provenance-tracing-tool.md`
- [x] **[MEDIUM]** Anthropic: Claude Attacks Result of Security Gaps, Not Model Issues — `2026-08-03-anthropic-claude-attacks-security-gaps.md`
- [x] **[HIGH]** Bitcoin Hardware Wallet Maker Destroys Inventory After $88 Million Stolen — `2026-08-03-coldcard-bitcoin-wallet-88-million-theft.md`
- [x] **[HIGH]** New DOUBLECUP ClickFix Service Hides Malware in Browser Cache Images — `2026-08-03-doublecup-clickfix-malware-browser-cache.md`

## Relevant (details)

### 1. 150,000 Impacted by Madera Community Hospital Data Breach
- **Source:** SecurityWeek — https://www.securityweek.com/150000-impacted-by-madera-community-hospital-data-breach/
- **Severity:** high
- **Tags:** `data-breach`
- **Summary:** An extortion group stole personal, financial, and medical data belonging to roughly 150,000 patients from Madera Community Hospital's network.

### 2. CISA Adds Exploited N-able N-central Flaw to KEV After Customer Compromises
- **Source:** The Hacker News — https://thehackernews.com/2026/08/cisa-adds-exploited-n-able-n-central.html
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `privilege-escalation`
- **Summary:** CISA added CVE-2026-18577 (CVSS 8.2), an incomplete-patch authentication bypass in N-able N-central, to its KEV catalog after confirmed active exploitation gave attackers admin access to RMM servers.

### 3. Hotel Wi-Fi Attacks Use Custom Malware to Breach Microsoft 365 Accounts
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hotel-wi-fi-attacks-use-custom-malware-to-breach-microsoft-365-accounts/
- **Severity:** high
- **Tags:** `malware`, `microsoft`, `cloud-security`
- **Summary:** Microsoft linked a global hospitality Wi-Fi campaign to Midnight Blizzard (APT29), which used custom malware to breach guests' Microsoft 365 accounts.

### 4. New Pass-ta-key Attacks Let Malware Hijack Google-Synced Passkeys
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-pass-ta-key-attacks-let-malware-hijack-google-synced-passkeys/
- **Severity:** high
- **Tags:** `malware`, `google`, `vulnerability`
- **Summary:** Researchers disclosed three techniques letting malware on an already-compromised Windows device abuse Google Password Manager's synced passkeys, bypassing user verification and extracting private keys.

### 5. New Tool Traces AI Videos Back to Their Source
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/new-tool-advances-ai-generated-video-detection
- **Severity:** informational
- **Tags:** `ai-safety`
- **Summary:** Researchers introduced a tool for tracing AI-generated videos to their source, aimed at industry collaboration on detection.

### 6. Anthropic: Claude Attacks Result of Security Gaps, Not Model Issues
- **Source:** Dark Reading — https://www.darkreading.com/cyber-risk/anthropic-ai-issues-result-security-gaps
- **Severity:** medium
- **Tags:** `anthropic`, `ai-safety`, `llm`
- **Summary:** Anthropic attributed last month's incidents involving a Claude-powered agent breaching real-world systems to deployment over-permissioning (unrestricted internet access), not model flaws.

### 7. Bitcoin Hardware Wallet Maker Destroys Inventory After $88 Million Stolen
- **Source:** The Record (Recorded Future) — https://therecord.media/bitcoin-theft-coldcard-cyberattack
- **Severity:** high
- **Tags:** `vulnerability`
- **Summary:** Coinkite destroyed part of its Coldcard hardware wallet inventory after a firmware vulnerability let attackers steal over $88 million from customers.

### 8. New DOUBLECUP ClickFix Service Hides Malware in Browser Cache Images
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/new-doublecup-clickfix-service-hides-malware-in-browser-cache-images/
- **Severity:** high
- **Tags:** `malware`, `phishing`
- **Summary:** A new loader-as-a-service, DOUBLECUP, uses ClickFix social engineering to hide malicious code in cached browser PNG images, delivering CountLoader and a new RAT (DeviceManager).

## Skippable

- **Device Code Phishing Up 1,500% in 2026; Vishing Doubles** — Dark Reading. Statistics/trend report with no new IOCs or specific technique detail.
- **Microsoft Bug Bounty Program: $20 Million Paid to 500 Researchers** — SecurityWeek. Program recap, no actionable security content.
- **New York Awards $9 Million to Strengthen Cybersecurity at 153 Water Systems** — SecurityWeek. Regional government funding announcement, not a security event.
- **Quoting Steve Yegge** — Simon Willison. Opinion/commentary on coding agents, no news value.
- **Don't be a meat proxy** — Simon Willison. Opinion piece on AI use etiquette, no news value.
- **After killer quarter, Palantir CEO Alex Karp calls AI industry 'Marxist'** — TechCrunch. Executive commentary/opinion, no technical substance.
- **Apple is getting this wrong** — OpenAI Blog. OpenAI's response to an Apple lawsuit; legal dispute, not a launch or safety incident.
- **Attackers Exploit N-able Patch Bypass Flaw on RMM Servers** — Dark Reading. Duplicate coverage of CVE-2026-18577; merged into The Hacker News item above.
- **AWS is helping vibe-coding startup Superblocks, and the implications are big** — TechCrunch. Business partnership news, no direct security angle.
