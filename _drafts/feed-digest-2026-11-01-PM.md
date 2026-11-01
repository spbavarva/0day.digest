# Digest — 2026-11-01 PM

- Window: last 14h
- Raw items considered: 9
- Relevant: 5
- Skippable: 4

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** Alpine Linux Rebuilds GitLab Server After Attempted RCE Attack — `2026-11-01-alpine-linux-rebuilds-gitlab-after-rce-attack.md`
- [x] **[HIGH]** CVSS 10.0 Flaw in Canonical LXD, MicroCloud Lets Attackers Impersonate Trusted Clients — `2026-11-01-lxd-microcloud-cvss-10-authentication-bypass.md`
- [x] **[HIGH]** Hackers Steal $2.7M From Polymarket Traders via Hijacked DebugBear Script — `2026-11-01-polymarket-hijacked-debugbear-supply-chain-attack.md`
- [x] **[HIGH]** FBI Links North Korea's TraderTraitor to Record $6.43 Billion Binance Heist — `2026-11-01-fbi-links-tradertraitor-to-record-binance-heist.md`
- [x] **[HIGH]** NetamLoader Malware Targets Government Windows 10 Systems in Asia — `2026-11-01-netamloader-malware-targets-government-windows-10-asia.md`

## Relevant (details)

### 1. Alpine Linux Rebuilds GitLab Server After Attempted RCE Attack
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/alpine-linux-rebuilds-gitlab-after-attempted-rce-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `rce`, `supply-chain`, `vulnerability`
- **Slug:** `alpine-linux-rebuilds-gitlab-after-rce-attack`
- **Must-know:** no
- **Summary:** Attackers attempted to exploit a critical GitLab vulnerability against Alpine Linux's dev infrastructure on October 20-21. The project rebuilt its GitLab server and reset all passwords as a precaution.

### 2. CVSS 10.0 Flaw in Canonical LXD, MicroCloud Lets Attackers Impersonate Trusted Clients
- **Source:** The Hacker News — https://thehackernews.com/2026/11/critical-lxd-and-microcloud-flaw-cvss.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`, `container-security`
- **Slug:** `lxd-microcloud-cvss-10-authentication-bypass`
- **Must-know:** no
- **Summary:** A CVSS 10.0 authentication bypass in LXD/MicroCloud lets an attacker impersonate a trusted client without its private key, gaining cluster and VM access. No active-exploitation claims accompany the disclosure.

### 3. Hackers Steal $2.7M From Polymarket Traders via Hijacked DebugBear Script
- **Source:** The Hacker News — https://thehackernews.com/2026/11/hackers-steal-about-27-million-from.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `data-breach`
- **Slug:** `polymarket-hijacked-debugbear-supply-chain-attack`
- **Must-know:** no
- **Summary:** A compromised third-party page-speed script loaded by Polymarket drained funds from 726 trader wallets on October 29, a classic third-party script supply-chain attack. Polymarket is refunding roughly $2.7 million.

### 4. FBI Links North Korea's TraderTraitor to Record $6.43 Billion Binance Heist
- **Source:** The Hacker News — https://thehackernews.com/2026/11/fbi-links-north-koreas-tradertraitor-to.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`, `malware`
- **Slug:** `fbi-links-tradertraitor-to-record-binance-heist`
- **Must-know:** no
- **Summary:** The FBI, Secret Service, and IRS-CI formally attributed the record $6.3B+ Binance crypto theft to North Korea's TraderTraitor group. This is attribution of a prior heist, not a new breach disclosure.

### 5. NetamLoader Malware Targets Government Windows 10 Systems in Asia
- **Source:** The Hacker News — https://thehackernews.com/2026/11/netamloader-malware-targets-government.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`
- **Slug:** `netamloader-malware-targets-government-windows-10-asia`
- **Must-know:** no
- **Summary:** Kaspersky disclosed a sophisticated infection chain, dubbed NetamLoader, targeting a custom Windows 10 build used exclusively by Asian government entities via a novel .NET assembly-loading framework.

## Skippable

- **FBI links $6.3 billion Binance crypto heist to North Korean hackers** — BleepingComputer. Duplicate coverage of the TraderTraitor/Binance attribution story; The Hacker News version has more detail and was kept instead.
- **Quoting Kyle Kingsbury** — Simon Willison. Opinion/commentary quote on LLM trust erosion, no news value.
- **OpenAI says it's doubling Pro usage limits and bringing Work features to Chat** — BleepingComputer. Product/feature update, no security angle.
- **Northstar Security Exits Stealth With $7M to Expose Toxic Risk Combinations** — SecurityWeek. Startup funding announcement, marketing content.
