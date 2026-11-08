# Raw feed pull — 2026-11-08 13:57 UTC

- Window: last 14h
- Feeds: 26 (25 ok, 0 empty, 1 error)
- Items kept after dedup: 2 (seen-skipped: 0, near-dup-skipped: 0)

## Feed health

- [OK] The Hacker News (0 items)
- [OK] BleepingComputer (0 items)
- [OK] Krebs on Security (0 items)
- [OK] Dark Reading (0 items)
- [OK] The Record (Recorded Future) (0 items)
- [OK] SecurityWeek (1 items)
- [ERR] SentinelOne Labs (0 items) — HTTP 429
- [OK] Cisco Talos (0 items)
- [OK] Unit 42 (Palo Alto) (0 items)
- [OK] Flashpoint (0 items)
- [OK] PortSwigger Research (0 items)
- [OK] Trail of Bits (0 items)
- [OK] Google Project Zero (0 items)
- [OK] Securelist (Kaspersky GReAT) (0 items)
- [OK] OpenAI Blog (0 items)
- [OK] Google DeepMind (0 items)
- [OK] Google AI Blog (0 items)
- [OK] Hugging Face Blog (0 items)
- [OK] TechCrunch AI (0 items)
- [OK] Simon Willison (1 items)
- [OK] Lilian Weng (OpenAI) (0 items)
- [OK] The Verge AI (0 items)
- [OK] AWS Security Blog (0 items)
- [OK] AWS News Blog (0 items)
- [OK] Google Cloud Security (0 items)
- [OK] CISA Alerts (0 items)

## Items

### 1. Brava Security Emerges From Stealth With $15 Million in Funding
- Section: Cybersecurity — Primary
- Source: SecurityWeek
- URL: https://www.securityweek.com/brava-security-emerges-from-stealth-with-15-million-in-funding/
- Published: 2026-11-08T12:14:00+00:00
- Summary: Its multi-agent AI platform generates the telemetry an attack would produce to fix gaps in enterprise defenses.
The post Brava Security Emerges From Stealth With $15 Million in Funding appeared first on SecurityWeek.

### 2. datasette #3046: Don't serve link: rel=next HTTP headers to Firefox for HTML pages
- Section: AI — News & Analysis
- Source: Simon Willison
- URL: https://simonwillison.net/2026/Nov/7/link-rel-next/
- Published: 2026-11-07T23:57:46+00:00
- Summary: datasette #3046: Don&#x27;t serve link: rel=next HTTP headers to Firefox for HTML pages
I was looking at the Firefox network panel today when I noticed that requests to a Datasette table page were triggering an HTTP prefetch to the next page of rows in that table.
This was happening because Datasette pages serve an HTTP link header like this:
link: &lt;https://latest.datasette.io/fixtures/compound_three_primary_keys?_next=a%2Cd%2Cv&gt;; rel="next"
This is bad. A tiny fraction of the visitors to one of those pages will click the "next" link, which means their browser is fetching unnecessary dat
