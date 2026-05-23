# Digest — 2026-05-23 AM

- Window: last 14h
- Raw items considered: 9
- Relevant: 4
- Skippable: 5

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** LiteSpeed cPanel Plugin CVE-2026-48172 Exploited to Run Scripts as Root — `2026-05-23-litespeed-cpanel-cve-2026-48172-root-exploit.md`
- [x] **[HIGH]** Drupal Core SQL Injection Bug Actively Exploited, Added to CISA KEV — `2026-05-23-drupal-core-sqli-cve-2026-9082-cisa-kev.md`
- [x] **[HIGH]** FBI Warns of Kali365 Phishing-as-a-Service Stealing Microsoft 365 OAuth Tokens — `2026-05-23-kali365-phaas-microsoft-365-oauth-token-theft.md`
- [x] **[MEDIUM]** AI Used to Reconstruct Dead Pilots' Voices from NTSB Cockpit Recordings — `2026-05-23-ai-voice-reconstruction-ntsb-cockpit-recordings.md`

## Relevant (details)

### 1. LiteSpeed cPanel Plugin CVE-2026-48172 Exploited to Run Scripts as Root
- **Source:** The Hacker News — https://thehackernews.com/2026/05/litespeed-cpanel-plugin-cve-2026-48172.html
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `cve`, `privilege-escalation`, `rce`, `zero-day`, `vulnerability`
- **Slug:** `2026-05-23-litespeed-cpanel-cve-2026-48172-root-exploit`
- **Must-know:** yes
- **Summary:** CVE-2026-48172 (CVSS 10.0) in the LiteSpeed cPanel plugin is under active exploitation. Any cPanel user can abuse an incorrect privilege assignment to run arbitrary scripts as root, making shared hosting environments a high-blast-radius target.

### 2. Drupal Core SQL Injection Bug Actively Exploited, Added to CISA KEV
- **Source:** The Hacker News — https://thehackernews.com/2026/05/drupal-core-sql-injection-bug-actively.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `sqli`, `vulnerability`, `zero-day`
- **Slug:** `2026-05-23-drupal-core-sqli-cve-2026-9082-cisa-kev`
- **Must-know:** no
- **Summary:** CISA added CVE-2026-9082, a SQL injection bug in Drupal Core affecting all supported versions, to its KEV catalog following confirmed exploitation. Federal agencies have mandatory patch deadlines; all Drupal operators should treat this as urgent.

### 3. FBI Warns of Kali365 Phishing-as-a-Service Stealing Microsoft 365 OAuth Tokens
- **Source:** The Record (Recorded Future) — https://therecord.media/fbi-warns-of-kali365-phishing-attacks
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `phishing`, `iam`, `microsoft`, `vulnerability`
- **Slug:** `2026-05-23-kali365-phaas-microsoft-365-oauth-token-theft`
- **Must-know:** no
- **Summary:** Kali365 is a Telegram-based PhaaS kit that captures live OAuth tokens by proxying victims through real M365 login pages, bypassing MFA entirely. The FBI issued an advisory after April 2026 attacks leveraged the service against Microsoft 365 environments.

### 4. AI Used to Reconstruct Dead Pilots' Voices from NTSB Cockpit Recordings
- **Source:** TechCrunch AI — https://techcrunch.com/2026/05/22/ai-is-being-used-to-resurrect-the-voices-of-dead-pilots/
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`, `appsec`
- **Slug:** `2026-05-23-ai-voice-reconstruction-ntsb-cockpit-recordings`
- **Must-know:** no
- **Summary:** Researchers used AI to invert spectrogram images of NTSB cockpit recordings into intelligible audio, prompting the agency to temporarily block docket access. This demonstrates that media-format conversions (audio→spectrogram) previously assumed to be irreversible are now recoverable with ML.

## Skippable

- **Towards Speed-of-Light Text Generation with Nemotron-Labs Diffusion Language Models** — Hugging Face Blog. Model release blog post with no summary provided and no security angle; low signal for this digest.
- **The memory shortage is causing a repricing of consumer electronics** — Simon Willison. Economics analysis of DRAM/HBM pricing; no security relevance.
- **Google goes for the glitter with disco-ball icons** — TechCrunch AI. Consumer UI feature for Pixel; no AI or security substance.
- **How VCs and founders use inflated 'ARR' to crown AI startups** — TechCrunch AI. Opinion/business piece on revenue metric gaming; no news value for practitioners.
- **Meta settles school district lawsuit claiming addictive design harmed students' mental health** — The Record. Legal settlement news; no technical substance and no breach data angle.
