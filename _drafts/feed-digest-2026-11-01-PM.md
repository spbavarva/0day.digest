# Digest — 2026-11-01 PM

- Window: last 14h
- Raw items considered: 6
- Relevant: 4
- Skippable: 2

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[HIGH]** CVSS 10.0 LXD/MicroCloud Flaw Lets Attackers Impersonate Trusted Clients — `2026-11-01-lxd-microcloud-critical-auth-bypass.md`
- [x] **[HIGH]** Hackers Steal $2.7 Million From Polymarket Traders via Hijacked DebugBear Script — `2026-11-01-polymarket-debugbear-supply-chain-theft.md`
- [x] **[CRITICAL]** FBI Links North Korea's TraderTraitor to Record $6.43 Billion Binance Crypto Heist — `2026-11-01-tradertraitor-binance-6-43b-heist-fbi.md`
- [x] **[HIGH]** NetamLoader Malware Targets Government Windows 10 Systems in Asia via .NET Injection — `2026-11-01-netamloader-malware-asia-government.md`

## Relevant (details)

### 1. CVSS 10.0 LXD/MicroCloud Flaw Lets Attackers Impersonate Trusted Clients Without a Private Key
- **Source:** The Hacker News — https://thehackernews.com/2026/11/critical-lxd-and-microcloud-flaw-cvss.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `container-security`
- **Slug:** `lxd-microcloud-critical-auth-bypass`
- **Must-know:** no
- **Summary:** A maximum-severity (CVSS 10.0) flaw in Canonical's LXD and MicroCloud lets an attacker impersonate a trusted client on the clustering API without holding that client's private key, requiring only network access and the client's public certificate. No confirmed active exploitation yet, so rated high rather than critical.

### 2. Hackers Steal About $2.7 Million From Polymarket Traders via Hijacked DebugBear Script
- **Source:** The Hacker News — https://thehackernews.com/2026/11/hackers-steal-about-27-million-from.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `appsec`
- **Slug:** `polymarket-debugbear-supply-chain-theft`
- **Must-know:** no
- **Summary:** A compromised third-party page-speed script from analytics vendor DebugBear let attackers drain about $2.7 million from Polymarket traders on Oct 29. Polymarket is refunding the roughly 726 affected wallets; about $2.64 million in stolen funds has been traced on-chain.

### 3. FBI Links North Korea's TraderTraitor to Record $6.43 Billion Binance Crypto Heist
- **Source:** The Hacker News — https://thehackernews.com/2026/11/fbi-links-north-koreas-tradertraitor-to.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `malware`, `crypto-heist`
- **Slug:** `tradertraitor-binance-6-43b-heist-fbi`
- **Must-know:** no
- **Summary:** The FBI, Secret Service, and IRS-CI formally attributed the theft of over $6.43 billion in crypto from Binance to TraderTraitor, a North Korea-aligned group also tracked as Jade Sleet/Pressure Chollima/UNC4899. It's one of the largest crypto heists on record; no new IOCs were disclosed.

### 4. NetamLoader Malware Targets Government Windows 10 Systems in Asia via .NET Injection
- **Source:** The Hacker News — https://thehackernews.com/2026/11/netamloader-malware-targets-government.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`
- **Slug:** `netamloader-malware-asia-government`
- **Must-know:** no
- **Summary:** Kaspersky disclosed "NetamLoader," a sophisticated infection chain using a previously undocumented .NET assembly-loading framework, targeting a custom Windows 10 build used exclusively by government organizations in Asia.

## Skippable

- **OpenAI says it's doubling Pro usage limits and bringing Work features to Chat** — BleepingComputer. Product/usage-limit announcement with no security angle or model capability change.
- **Northstar Security Exits Stealth With $7M to Expose Toxic Risk Combinations** — SecurityWeek. Startup funding announcement; marketing content, not news of a specific incident or technique.
