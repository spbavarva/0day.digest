# Digest — 2026-05-15 AM

- Window: last 14h
- Raw items considered: 24
- Relevant: 9
- Skippable: 15

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** TanStack npm Supply Chain Attack Hits Multiple AI Companies — `2026-05-15-tanstack-npm-supply-chain-ai-companies.md`
- [x] **[CRITICAL]** Cisco SD-WAN CVE-2026-20182 Zero-Day Exploited by UAT-8616, CISA Issues Emergency Directive — `2026-05-15-cisco-sd-wan-cve-2026-20182-zero-day-uat-8616.md`
- [x] **[HIGH]** Microsoft Exchange Server CVE-2026-42897 Actively Exploited via Crafted Email — `2026-05-15-exchange-server-cve-2026-42897-active-exploit.md`
- [x] **[HIGH]** Chrome 148 Patches Critical Use-After-Free Vulnerabilities — `2026-05-15-chrome-148-critical-patches.md`
- [x] **[HIGH]** TeamPCP Advertises Mistral AI Source Code Repositories for Sale — `2026-05-15-teampcp-mistral-ai-source-code.md`
- [x] **[HIGH]** WordPress Burst Statistics Plugin Auth Bypass Actively Exploited — `2026-05-15-burst-statistics-wordpress-auth-bypass.md`
- [x] **[MEDIUM]** Taiwan Student's SDR Experiment Shuts Down Bullet Trains, Exposes Rail Control Gaps — `2026-05-15-taiwan-rail-sdr-security-incident.md`
- [x] **[INFORMATIONAL]** OpenAI Brings Codex to ChatGPT Mobile App — `2026-05-15-openai-codex-mobile-chatgpt.md`
- [x] **[INFORMATIONAL]** AWS IAM Identity Center Gains Multi-Region Replication and Custom Domain Support — `2026-05-15-aws-iam-identity-center-multiregion-custom-domains.md`

## Relevant (details)

### 1. TanStack npm Supply Chain Attack Hits Multiple AI Companies
- **Source:** The Record (Recorded Future) — https://therecord.media/openai-asks-macos-users-to-update-tanstack-npm
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `pypi`, `openai`, `appsec`
- **Summary:** The popular open-source TanStack JavaScript library has been compromised as part of an expanding supply chain campaign also affecting additional npm and PyPI packages linked to multiple AI companies. OpenAI has asked its macOS users to update their software in response.

### 2. Cisco SD-WAN CVE-2026-20182 Zero-Day Exploited by UAT-8616, CISA Issues Emergency Directive
- **Source:** SecurityWeek — https://www.securityweek.com/cisco-patches-another-sd-wan-zero-day-the-sixth-exploited-in-2026/
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `vulnerability`, `cisco`
- **Summary:** Cisco has patched CVE-2026-20182, a CVSS 10.0 authentication bypass in Catalyst SD-WAN Controller exploited by sophisticated actor UAT-8616. This is the sixth Cisco SD-WAN vulnerability exploited in 2026; CISA added it to the KEV catalog with a May 17 federal remediation deadline.

### 3. Microsoft Exchange Server CVE-2026-42897 Actively Exploited via Crafted Email
- **Source:** The Hacker News — https://thehackernews.com/2026/05/on-prem-microsoft-exchange-server-cve.html
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `xss`, `microsoft`
- **Summary:** Microsoft has disclosed CVE-2026-42897 (CVSS 8.1), an actively exploited spoofing vulnerability in on-premises Exchange Server stemming from a cross-site scripting flaw triggered via crafted email. On-prem Exchange administrators should patch immediately.

### 4. Chrome 148 Patches Critical Use-After-Free Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/chrome-148-update-patches-critical-vulnerabilities/
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `appsec`
- **Summary:** Google released Chrome 148 resolving critical-severity use-after-free bugs and other flaws across multiple browser components. Use-after-free vulnerabilities in browser engines are frequently leveraged for sandbox escapes; users should update immediately.

### 5. TeamPCP Advertises Mistral AI Source Code Repositories for Sale
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/teampcp-hackers-advertise-mistral-ai-code-repos-for-sale/
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `ai-safety`
- **Summary:** The TeamPCP threat actor group is advertising Mistral AI source code repositories for sale on criminal forums, threatening public release if no buyer is found. No confirmation from Mistral AI on the breach's scope or authenticity has been reported.

### 6. WordPress Burst Statistics Plugin Auth Bypass Actively Exploited
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-exploit-auth-bypass-flaw-in-burst-statistics-wordpress-plugin/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`, `privilege-escalation`
- **Summary:** Threat actors are actively exploiting a critical authentication bypass in the Burst Statistics WordPress plugin to gain admin-level access to affected sites. Site owners should update or disable the plugin immediately.

### 7. Taiwan Student's SDR Experiment Shuts Down Bullet Trains, Exposes Rail Control Gaps
- **Source:** Dark Reading — https://www.darkreading.com/ics-ot-security/taiwan-incident-highlights-cybersecurity-gaps
- **Severity:** medium
- **Tags:** `vulnerability`, `ics-ot`
- **Summary:** A student in Taiwan experimenting with software-defined radio inadvertently disrupted rail control signals, halting three bullet trains for nearly an hour and triggering an anti-terrorism response. The incident exposes weak RF security in rail control systems.

### 8. OpenAI Brings Codex to ChatGPT Mobile App
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/930763/openai-codex-chatgpt-ios-android-app-preview
- **Severity:** informational
- **Tags:** `openai`, `llm`, `ai-launch`
- **Summary:** OpenAI is rolling Codex into the ChatGPT mobile app on iOS and Android as a preview, competing directly with Anthropic's Claude Code in the agentic coding tool space.

### 9. AWS IAM Identity Center Gains Multi-Region Replication and Custom Domain Support
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/regional-routing-for-aws-access-portals-implementing-custom-vanity-domains-for-iam-identity-center/
- **Severity:** informational
- **Tags:** `iam`, `aws`, `cloud-security`
- **Summary:** AWS IAM Identity Center now supports multi-Region replication with custom vanity domain routing for access portals, improving resilience for globally distributed workforces without requiring changes to existing application integrations.

## Skippable

- **CISA Adds Cisco SD-WAN CVE-2026-20182 to KEV** — The Hacker News. Duplicate coverage of CVE-2026-20182; merged into item #2.
- **Maximum Severity Cisco SD-WAN Bug Exploited in the Wild** — Dark Reading. Duplicate coverage of CVE-2026-20182; merged into item #2.
- **Cisco warns of new critical SD-WAN flaw exploited in zero-day attacks** — BleepingComputer. Duplicate coverage of CVE-2026-20182; merged into item #2.
- **OpenAI says Codex is coming to your phone** — TechCrunch AI. Duplicate of The Verge Codex mobile item; merged into item #8.
- **Not so locked in any more** — Simon Willison. Opinion commentary on programming language lock-in; no security news value.
- **Quoting Mitchell Hashimoto** — Simon Willison. Quote curation on Bun/Zig/Rust; no security angle.
- **What the jury will actually decide in the case of Elon Musk vs. Sam Altman** — TechCrunch AI. Legal analysis of the Musk v. Altman trial; no technical security angle.
- **Closing time** — The Verge AI. Color commentary on Musk v. Altman closing arguments; no technical security angle.
- **Behold, the Elon Musk jackass trophy** — The Verge AI. Trial color piece with no security value.
- **Elon Musk's SpaceXAI has been bleeding staff since its merger** — TechCrunch AI. Business/HR news with no security angle.
- **Amazon Bedrock introduces new advanced prompt optimization and migration tool** — AWS News Blog. AI product feature announcement; no security implications.
- **Sea's View on the Future of Agentic Software Development with Codex** — OpenAI Blog. Customer success story / marketing content.
- **SecurityScorecard Snags Driftnet to Level Up Threat Intelligence** — Dark Reading. Vendor acquisition with no new technical findings.
- **How Mergers and Acquisitions Expand Your Attack Surface Overnight** — Flashpoint. Vendor marketing; no new technical findings.
- **What happens when AI starts building itself?** — TechCrunch AI. Startup pitch piece; no technical substance.
