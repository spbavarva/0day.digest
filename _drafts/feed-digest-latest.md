# Digest — 2026-05-17 PM

- Window: last 14h
- Raw items considered: 8
- Relevant: 4
- Skippable: 4

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** NGINX CVE-2026-42945: Heap Buffer Overflow Exploited in the Wild, RCE Risk — `2026-05-17-nginx-cve-2026-42945-rce-active-exploitation.md`
- [x] **[CRITICAL]** Grafana GitHub Token Breach: Codebase Downloaded, Extortion Attempted — `2026-05-17-grafana-github-token-breach-codebase-extortion.md`
- [x] **[HIGH]** Tycoon2FA PhaaS Kit Adds Device-Code Phishing to Hijack Microsoft 365 — `2026-05-17-tycoon2fa-device-code-phishing-microsoft-365.md`
- [x] **[INFORMATIONAL]** NHS Closes Open Source Repos After Vuln Reports; UK GDS Pushes Back — `2026-05-17-nhs-open-source-retreat-gds-vulnerability-response.md`

## Relevant (details)

### 1. NGINX CVE-2026-42945: Heap Buffer Overflow Exploited in the Wild, RCE Risk
- **Source:** The Hacker News — https://thehackernews.com/2026/05/nginx-cve-2026-42945-exploited-in-wild.html
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `rce`, `zero-day`
- **Summary:** A heap buffer overflow (CVSS 9.2) in NGINX's ngx_http_rewrite_module is actively exploited days after public disclosure, affecting versions 0.6.27–1.30.0. Exploitation can crash worker processes and enable RCE across a massive segment of global web infrastructure.

### 2. Grafana GitHub Token Breach: Codebase Downloaded, Extortion Attempted
- **Source:** The Hacker News — https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html
- **Severity:** critical
- **Tags:** `data-breach`, `github`, `grafana`, `supply-chain`
- **Summary:** An unauthorized party obtained a GitHub token, accessed Grafana's GitHub environment, downloaded the full codebase, and attempted extortion. No customer data was accessed, but the source code exfiltration creates latent supply chain risk for the widely-used observability platform.

### 3. Tycoon2FA PhaaS Kit Adds Device-Code Phishing to Hijack Microsoft 365
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/tycoon2fa-hijacks-microsoft-365-accounts-via-device-code-phishing/
- **Severity:** high
- **Tags:** `phishing`, `microsoft`, `iam`
- **Summary:** The Tycoon2FA phishing kit now supports device-code phishing, bypassing MFA to hijack Microsoft 365 accounts while abusing Trustifi click-tracking URLs to evade detection. Organizations should restrict the OAuth device-code grant flow in Entra ID where not required.

### 4. NHS Closes Open Source Repos After Vuln Reports; UK GDS Pushes Back
- **Source:** Simon Willison — https://simonwillison.net/2026/May/17/gds-weighs-in/#atom-everything
- **Severity:** informational
- **Tags:** `appsec`, `devsecops`, `vulnerability`
- **Summary:** The UK NHS closed public access to its open source repositories after vulnerability reports via Project Glasswing, prompting criticism of security-through-obscurity. The UK GDS recommended open-by-default policies, surfacing a broader tension between disclosure and transparency in public sector security.

## Skippable

- **University of Arizona students boo Eric Schmidt's AI cheerleading during commencement** — The Verge AI. Social commentary on student reaction to AI optimism at graduation; no security or technical angle.
- **If you're giving a commencement speech in 2026, maybe don't mention AI** — TechCrunch AI. Duplicate coverage of the same Eric Schmidt commencement story; no independent news value.
- **TechCrunch Mobility: The AI skills arms race is coming for automotive** — TechCrunch AI. Generic automotive industry newsletter; no security or substantive AI launch content.
- **Chatbots at the drive-thru are just the beginning** — The Verge AI. Consumer AI opinion piece about fast food AI; no security angle, no new model or tool launch.
