# Digest — 2026-05-25 AM

- Window: last 14h
- Raw items considered: 10
- Relevant: 6
- Skippable: 4

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Megalodon Supply Chain Attack Infects 5,500+ GitHub Repositories — `2026-05-25-megalodon-github-supply-chain-5500-repos.md`
- [x] **[CRITICAL]** TrapDoor Supply Chain Attack Targets npm, PyPI, and Crates.io — `2026-05-25-trapdoor-supply-chain-npm-pypi-crates.md`
- [x] **[CRITICAL]** Laravel-Lang Packages Poisoned to Exfiltrate CI Secrets — `2026-05-25-laravel-lang-supply-chain-backdoor-ci-secrets.md`
- [x] **[HIGH]** Lazarus Group Deploys RemotePE Memory-Only RAT Against Financial and Crypto Firms — `2026-05-25-lazarus-remotepe-memory-rat-financial-crypto.md`
- [x] **[HIGH]** DocketWise Data Breach Exposes 143,000 Records Including SSNs — `2026-05-25-docketwise-data-breach-143k.md`
- [x] **[HIGH]** Anthropic Mythos Flags 23,000 Potential Vulnerabilities Across 1,000 OSS Projects — `2026-05-25-anthropic-mythos-23k-vulnerabilities-oss.md`

## Relevant (details)

### 1. Megalodon Supply Chain Attack Infects 5,500+ GitHub Repositories
- **Source:** SecurityWeek — https://www.securityweek.com/over-5500-github-repositories-infected-in-megalodon-supply-chain-attack/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `github`, `malware`, `devsecops`
- **Slug:** `megalodon-github-supply-chain-5500-repos`
- **Must-know:** yes
- **Summary:** The Megalodon campaign injected fake automated commits into 5,500+ GitHub repositories, embedding malicious GitHub Actions workflows that steal credentials, CI secrets, API keys, and tokens. Scope and credential-exfiltration mechanism make this a critical supply chain event for any org with public or private GitHub repos.

### 2. TrapDoor Supply Chain Attack Targets npm, PyPI, and Crates.io
- **Source:** The Hacker News — https://thehackernews.com/2026/05/trapdoor-supply-chain-attack-spreads.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `pypi`, `malware`, `crates-io`
- **Slug:** `trapdoor-supply-chain-npm-pypi-crates`
- **Must-know:** yes
- **Summary:** TrapDoor is a coordinated campaign spanning 34+ malicious packages across 384+ versions on npm, PyPI, and Crates.io, publishing credential-stealing malware in waves since May 22. Cross-ecosystem scope and rapid iteration across registries indicate a well-resourced, ongoing threat actor.

### 3. Laravel-Lang Packages Poisoned to Exfiltrate CI Secrets
- **Source:** SecurityWeek — https://www.securityweek.com/laravel-lang-packages-poisoned-for-malware-delivery/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `malware`, `github`, `devsecops`
- **Slug:** `laravel-lang-supply-chain-backdoor-ci-secrets`
- **Must-know:** yes
- **Summary:** Attackers poisoned Laravel-Lang packages by publishing malicious tags within a 15-minute burst, injecting backdoors designed to exfiltrate CI secrets. Any pipeline consuming affected Laravel-Lang versions during that window should treat CI credentials as compromised.

### 4. Lazarus Group Deploys RemotePE Memory-Only RAT Against Financial and Crypto Firms
- **Source:** The Hacker News — https://thehackernews.com/2026/05/lazarus-deploys-remotepe-memory-only.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `lazarus`
- **Slug:** `lazarus-remotepe-memory-rat-financial-crypto`
- **Must-know:** no
- **Summary:** Fox-IT (NCC Group) disclosed RemotePE, a cross-platform, memory-only RAT used by North Korea's Lazarus Group in a multi-stage campaign against financial and cryptocurrency organizations. The attack chain uses two loaders — DPAPILoader and RemotePELoader — to decrypt and execute the payload entirely in memory, evading disk-based detection.

### 5. DocketWise Data Breach Exposes 143,000 Records Including SSNs
- **Source:** SecurityWeek — https://www.securityweek.com/docketwise-data-breach-impacts-143000/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `data-breach`
- **Slug:** `docketwise-data-breach-143k`
- **Must-know:** no
- **Summary:** Hackers accessed DocketWise third-party partner repositories, exfiltrating names, addresses, Social Security numbers, financial information, and medical data for 143,000 individuals. The combination of SSNs and medical data raises identity theft and HIPAA exposure risk for affected users.

### 6. Anthropic Mythos Flags 23,000 Potential Vulnerabilities Across 1,000 OSS Projects
- **Source:** SecurityWeek — https://www.securityweek.com/anthropic-mythos-detected-23000-potential-vulnerabilities-across-1000-oss-projects/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `anthropic`, `llm`, `vulnerability`, `appsec`
- **Slug:** `anthropic-mythos-23k-vulnerabilities-oss`
- **Must-know:** no
- **Summary:** Anthropic's Mythos AI system has identified 23,000 potential vulnerabilities across 1,000 open-source software projects, with many confirmed as critical or high severity. Anthropic notes the count will grow as the scan continues, signaling a step-change in AI-assisted vulnerability discovery at scale.

## Skippable

- **datasette 1.0a30** — Simon Willison. Alpha release of a data exploration tool with a new "Jump to" menu; no security angle.
- **datasette-agent 0.1a4** — Simon Willison. Alpha plugin adding an agent chat interface to datasette; no security angle.
- **Everyone is navigating AI security in real time — even Google** — TechCrunch AI. Opinion/commentary piece with no concrete news; summary is a single vague sentence.
- **datasette-fixtures 0.1a0** — Simon Willison. Alpha plugin for datasette test fixtures; no security angle.
