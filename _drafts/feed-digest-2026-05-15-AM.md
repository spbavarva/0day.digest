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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `supply-chain`, `npm`, `pypi`, `openai`, `appsec`
- **Slug:** `2026-05-15-tanstack-npm-supply-chain-ai-companies`
- **Must-know:** yes
- **Summary:** The popular open-source TanStack JavaScript library has been compromised as part of an expanding supply chain campaign also affecting additional npm and PyPI packages linked to multiple AI companies. OpenAI has asked its macOS users to update their software in response.

### 2. Cisco SD-WAN CVE-2026-20182 Zero-Day Exploited by UAT-8616, CISA Issues Emergency Directive
- **Source:** SecurityWeek — https://www.securityweek.com/cisco-patches-another-sd-wan-zero-day-the-sixth-exploited-in-2026/
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `zero-day`, `cve`, `vulnerability`, `rce`, `cisco`
- **Slug:** `2026-05-15-cisco-sd-wan-cve-2026-20182-zero-day-uat-8616`
- **Must-know:** yes
- **Summary:** Cisco has patched CVE-2026-20182, a CVSS 10.0 authentication bypass in Catalyst SD-WAN Controller exploited in targeted zero-day attacks by the sophisticated actor UAT-8616. This is the sixth Cisco SD-WAN vulnerability exploited in 2026; CISA added it to the KEV catalog with a May 17 federal remediation deadline.

### 3. Microsoft Exchange Server CVE-2026-42897 Actively Exploited via Crafted Email
- **Source:** The Hacker News — https://thehackernews.com/2026/05/on-prem-microsoft-exchange-server-cve.html
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `xss`, `microsoft`
- **Slug:** `2026-05-15-exchange-server-cve-2026-42897-active-exploit`
- **Must-know:** no
- **Summary:** Microsoft has disclosed CVE-2026-42897 (CVSS 8.1), an actively exploited spoofing vulnerability in on-premises Exchange Server that stems from a cross-site scripting flaw and is triggered via crafted email. On-prem Exchange administrators should patch immediately given in-the-wild exploitation.

### 4. Chrome 148 Patches Critical Use-After-Free Vulnerabilities
- **Source:** SecurityWeek — https://www.securityweek.com/chrome-148-update-patches-critical-vulnerabilities/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `cve`, `vulnerability`, `appsec`
- **Slug:** `2026-05-15-chrome-148-critical-patches`
- **Must-know:** no
- **Summary:** Google released Chrome 148 resolving critical-severity use-after-free bugs and other flaws across multiple browser components. Use-after-free vulnerabilities in browser engines are frequently leveraged for sandbox escapes and RCE; users should apply the update immediately.

### 5. TeamPCP Advertises Mistral AI Source Code Repositories for Sale
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/teampcp-hackers-advertise-mistral-ai-code-repos-for-sale/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `supply-chain`, `malware`, `ai-safety`, `openai`
- **Slug:** `2026-05-15-teampcp-mistral-ai-source-code`
- **Must-know:** no
- **Summary:** The TeamPCP threat actor group is advertising Mistral AI source code repositories for sale on criminal forums, threatening to leak the data publicly if no buyer is found. No confirmation from Mistral AI on the breach's scope or authenticity has been reported.

### 6. WordPress Burst Statistics Plugin Auth Bypass Actively Exploited
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/security/hackers-exploit-auth-bypass-flaw-in-burst-statistics-wordpress-plugin/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `appsec`, `privilege-escalation`
- **Slug:** `2026-05-15-burst-statistics-wordpress-auth-bypass`
- **Must-know:** no
- **Summary:** Threat actors are actively exploiting a critical authentication bypass vulnerability in the Burst Statistics WordPress plugin, obtaining admin-level access to affected sites. WordPress site owners using this plugin should update or disable it immediately.

### 7. Taiwan Student's SDR Experiment Shuts Down Bullet Trains, Exposes Rail Control Gaps
- **Source:** Dark Reading — https://www.darkreading.com/ics-ot-security/taiwan-incident-highlights-cybersecurity-gaps
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `vulnerability`, `ics-ot`
- **Slug:** `2026-05-15-taiwan-rail-sdr-security-incident`
- **Must-know:** no
- **Summary:** A Taiwanese student experimenting with software-defined radio technology inadvertently disrupted rail control signals, halting three bullet trains for nearly an hour and triggering an anti-terrorism response. The incident highlights weak radio frequency security in rail control systems and the low barrier SDR tooling presents for interference with critical transportation infrastructure.

### 8. OpenAI Brings Codex to ChatGPT Mobile App
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/930763/openai-codex-chatgpt-ios-android-app-preview
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `openai`, `llm`, `ai-launch`
- **Slug:** `2026-05-15-openai-codex-mobile-chatgpt`
- **Must-know:** no
- **Summary:** OpenAI is rolling Codex, its AI coding agent, into the ChatGPT mobile app on iOS and Android as a preview. The move is framed as a competitive response to the surge in popularity of Anthropic's Claude Code.

### 9. AWS IAM Identity Center Gains Multi-Region Replication and Custom Domain Support
- **Source:** AWS Security Blog — https://aws.amazon.com/blogs/security/regional-routing-for-aws-access-portals-implementing-custom-vanity-domains-for-iam-identity-center/
- **Section:** Cloud Security & Infrastructure
- **Severity:** informational
- **Tags:** `iam`, `aws`, `cloud-security`
- **Slug:** `2026-05-15-aws-iam-identity-center-multiregion-custom-domains`
- **Must-know:** no
- **Summary:** AWS IAM Identity Center now supports multi-Region replication with custom vanity domain routing for access portals, improving resilience and reducing latency for globally distributed workforces without changing existing application integrations.

## Skippable

- **CISA Adds Cisco SD-WAN CVE-2026-20182 to KEV** — The Hacker News. Duplicate coverage of the same Cisco SD-WAN zero-day; merged into item #2 above.
- **Maximum Severity Cisco SD-WAN Bug Exploited in the Wild** — Dark Reading. Duplicate coverage of CVE-2026-20182; merged into item #2 above.
- **Cisco warns of new critical SD-WAN flaw exploited in zero-day attacks** — BleepingComputer. Duplicate coverage of CVE-2026-20182; merged into item #2 above.
- **OpenAI says Codex is coming to your phone** — TechCrunch AI. Duplicate of The Verge item on Codex mobile; merged into item #8 above.
- **Not so locked in any more** — Simon Willison. Opinion/commentary on programming language lock-in with coding agents; no security news value.
- **Quoting Mitchell Hashimoto** — Simon Willison. Quote curation on Bun/Zig/Rust portability; no security angle.
- **What the jury will actually decide in the case of Elon Musk vs. Sam Altman** — TechCrunch AI. Legal analysis of the Musk v. Altman trial; no technical security angle.
- **Closing time** — The Verge AI. Color commentary on Musk v. Altman closing arguments; no technical security angle.
- **Behold, the Elon Musk jackass trophy** — The Verge AI. Trial color piece with no technical or security value.
- **Elon Musk's SpaceXAI has been bleeding staff since its merger** — TechCrunch AI. Business/HR news with no security angle.
- **Amazon Bedrock introduces new advanced prompt optimization and migration tool** — AWS News Blog. Marketing announcement for an AI product feature; no security implications.
- **Sea's View on the Future of Agentic Software Development with Codex** — OpenAI Blog. Customer success story / marketing content for OpenAI Codex.
- **SecurityScorecard Snags Driftnet to Level Up Threat Intelligence** — Dark Reading. Vendor acquisition announcement with no technical findings; marketing content.
- **How Mergers and Acquisitions Expand Your Attack Surface Overnight** — Flashpoint. Thought-leadership marketing from a vendor; no new technical findings.
- **What happens when AI starts building itself?** — TechCrunch AI. Startup pitch piece about a self-improving AI company; no news with technical substance.
