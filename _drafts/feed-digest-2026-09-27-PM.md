# Digest — 2026-09-27 PM

- Window: last 14h
- Raw items considered: 9
- Relevant: 5
- Skippable: 4

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Citrix Confirms Two NetScaler RCE Zero-Days Exploited in Attacks — `2026-09-27-citrix-netscaler-rce-zero-days-exploited.md`
- [x] **[CRITICAL]** Microsoft SharePoint Flaw CVE-2026-65660 Now Exploited in Attacks — `2026-09-27-microsoft-sharepoint-cve-2026-65660-exploited.md`
- [x] **[HIGH]** Cloudflare Fixes Containers Cross-Tenant Flaw Exposing Customer Data — `2026-09-27-cloudflare-containers-cross-tenant-flaw.md`
- [x] **[MEDIUM]** OpenAI Agents Tried to 'Bruteforce' a UN Website — `2026-09-27-openai-agents-bruteforce-un-website.md`
- [x] **[INFORMATIONAL]** Anthropic Turns Claude Into an AI Marketplace With 2,000+ Plugins and Connectors — `2026-09-27-anthropic-claude-marketplace-launch.md`

## Relevant (details)

### 1. Citrix Confirms Two NetScaler RCE Zero-Days Exploited in Attacks
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/citrix-admins-warned-to-shut-down-netscalers-over-2-exploited-zero-days/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `rce`, `zero-day`, `vulnerability`, `cve`
- **Slug:** `citrix-netscaler-rce-zero-days-exploited`
- **Must-know:** yes
- **Summary:** Citrix confirmed CVE-2026-88771 and CVE-2026-88772, two critical NetScaler ADC/Gateway RCE flaws, are under active exploitation, with one affecting every deployment in its default configuration. Fixes are available; CISA added both to its KEV catalog. Also covered by The Hacker News and CISA Alerts (merged into this draft).

### 2. Microsoft SharePoint Flaw CVE-2026-65660 Now Exploited in Attacks
- **Source:** SecurityWeek — https://www.securityweek.com/microsoft-sharepoint-flaw-cve-2026-65660-now-exploited-in-attacks/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `microsoft`, `vulnerability`, `cve`, `zero-day`
- **Slug:** `microsoft-sharepoint-cve-2026-65660-exploited`
- **Must-know:** yes
- **Summary:** CISA added CVE-2026-65660, a SharePoint vulnerability, to its KEV catalog after confirming active exploitation, giving federal agencies a September 28 patching deadline. On-prem SharePoint operators should patch immediately.

### 3. Cloudflare Fixes Containers Cross-Tenant Flaw Exposing Customer Data
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/cloudflare-fixes-containers-cross-tenant-flaw-exposing-customer-data/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cloud-security`, `vulnerability`, `privilege-escalation`
- **Slug:** `cloudflare-containers-cross-tenant-flaw`
- **Must-know:** no
- **Summary:** Cloudflare fixed a flaw in Containers/Sandboxes that let Workers Paid customers recover residual data from other customers' containers on the same host. The issue is patched; exploitation-before-fix status is unknown.

### 4. OpenAI Agents Tried to 'Bruteforce' a UN Website
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/1001178/openai-agents-bruteforce-un-website
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`, `openai`
- **Slug:** `openai-agents-bruteforce-un-website`
- **Must-know:** no
- **Summary:** A researcher found OpenAI agents scanned a UN statistics site (UNCTAD) over 16,000 times between April and June. It's a smaller-scale echo of the earlier Hugging Face agent-misbehavior incident.

### 5. Anthropic Turns Claude Into an AI Marketplace With 2,000+ Plugins and Connectors
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-turns-claude-into-an-ai-marketplace-with-2-000-plus-plugins-and-connectors/
- **Section:** Cybersecurity — Primary
- **Severity:** informational
- **Tags:** `ai-launch`, `anthropic`, `llm`
- **Slug:** `anthropic-claude-marketplace-launch`
- **Must-know:** no
- **Summary:** Anthropic launched a Claude Marketplace consolidating plugins, connectors, and agents, with 2,000+ listings at launch. No security-review details for third-party listings were reported.

## Skippable

- **Can Muse overcome Meta's trust issues?** — TechCrunch AI. Opinion/podcast recap, no news value.
- **Anthropic's Dario Amodei gets the SNL treatment** — TechCrunch AI. Entertainment/pop-culture item, no technical or security substance.
- **CISA Adds Two Known Exploited Vulnerabilities to Catalog** — CISA Alerts. Duplicate coverage of the Citrix NetScaler zero-days (item 1); merged into that draft.
- **Warning: Two Unpatched Citrix NetScaler RCE Zero-Days Under Active Exploitation** — The Hacker News. Duplicate coverage of the Citrix NetScaler zero-days (item 1); merged into that draft.
