# Digest — 2026-04-15 PM

- Window: last 14h
- Raw items considered: 18
- Relevant: 10
- Skippable: 8

## Select items to publish

> All items checked by default. **Uncheck** items you don't want, then merge.

- [x] **[CRITICAL]** Fortinet Patches Critical FortiSandbox Vulnerabilities Enabling Auth Bypass and RCE — `2026-04-15-fortinet-fortisandbox-critical-auth-bypass-rce.md`
- [x] **[HIGH]** $10 Domain Registration Could Have Handed Attackers 25K Endpoints in OT and Gov Networks — `2026-04-15-cheap-domain-25k-ot-gov-endpoints-adware.md`
- [x] **[HIGH]** ICS Patch Tuesday: Eight Industrial Giants Publish Security Advisories — `2026-04-15-ics-patch-tuesday-eight-industrial-vendors.md`
- [x] **[HIGH]** Threat Actors Abusing n8n Agentic AI Workflow Platform in Email Attack Campaigns — `2026-04-15-n8n-agentic-ai-workflow-abuse-email-campaigns.md`
- [x] **[HIGH]** Ivanti Neurons for ITSM Patches Auth Bypass and Cross-Session Data Disclosure — `2026-04-15-ivanti-neurons-itsm-auth-bypass-session-disclosure.md`
- [x] **[MEDIUM]** Study: 194 Ad Services Ignore Legally Required Opt-Out Signals — `2026-04-15-big-tech-ad-tracking-opt-out-ignored.md`
- [x] **[MEDIUM]** Apple Threatened to Ban Grok from App Store Over Nonconsensual Deepfakes on X — `2026-04-15-grok-deepfakes-x-apple-app-store-ban-threat.md`
- [x] **[MEDIUM]** Microsoft April 2026 Update Triggers BitLocker Recovery Mode on Windows Server 2025 — `2026-04-15-windows-server-2025-bitlocker-recovery-april-update.md`
- [x] **[MEDIUM]** Microsoft Patches Bug That Silently Upgraded Windows Server 2019/2022 to Server 2025 — `2026-04-15-windows-server-auto-upgrade-bug-fixed.md`
- [x] **[INFORMATIONAL]** Datasette Drops CSRF Tokens in Favor of Sec-Fetch-Site Header Protection — `2026-04-15-datasette-csrf-sec-fetch-site-header.md`

## Relevant (details)

### 1. Fortinet Patches Critical FortiSandbox Vulnerabilities Enabling Auth Bypass and RCE
- **Source:** SecurityWeek — https://www.securityweek.com/fortinet-patches-critical-fortisandbox-vulnerabilities/
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `rce`
- **Summary:** Fortinet patched critical flaws allowing remote auth bypass and RCE via HTTP in FortiSandbox. No active exploitation confirmed, but compromise of this sandboxing layer could let attackers whitelist malicious samples across the organization.

### 2. $10 Domain Registration Could Have Handed Attackers 25K Endpoints in OT and Gov Networks
- **Source:** SecurityWeek — https://www.securityweek.com/10-domain-could-have-handed-hackers-25k-endpoints-including-in-ot-and-gov-networks/
- **Severity:** high
- **Tags:** `malware`, `vulnerability`
- **Summary:** A lapsed domain beaconed by 25,000 adware-infected endpoints — including OT and gov systems — could have been seized for $10. The adware kills security products and drops secondary payloads; researchers sinkholed the domain to map the infection.

### 3. ICS Patch Tuesday: Eight Industrial Giants Publish Security Advisories
- **Source:** SecurityWeek — https://www.securityweek.com/ics-patch-tuesday-8-industrial-giants-publish-new-security-advisories/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `ics`
- **Summary:** Siemens, Schneider Electric, Aveva, Rockwell Automation, ABB, Phoenix Contact, Mitsubishi Electric, and Moxa released coordinated ICS security advisories. OT teams should pull vendor-specific PSIRTs and prioritize internet-exposed or DMZ-connected assets.

### 4. Threat Actors Abusing n8n Agentic AI Workflow Platform in Email Attack Campaigns
- **Source:** Cisco Talos — https://blog.talosintelligence.com/the-n8n-n8mare/
- **Severity:** high
- **Tags:** `malware`, `phishing`, `llm`
- **Summary:** Cisco Talos tracked threat actors abusing n8n, an agentic AI workflow platform, in email attack campaigns from October 2025 through March 2026. Attackers chain AI calls, webhooks, and external services into delivery pipelines — treating AI automation tooling like a C2 framework.

### 5. Ivanti Neurons for ITSM Patches Auth Bypass and Cross-Session Data Disclosure
- **Source:** SecurityWeek — https://www.securityweek.com/two-vulnerabilities-patched-in-ivanti-neurons-for-itsm/
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Summary:** Two Ivanti ITSM flaws patched: one lets disabled accounts maintain persistent access, another exposes cross-session data. ITSM platforms hold broad IT infrastructure permissions; account-disablement bypass directly undermines incident response containment.

### 6. Study: 194 Ad Services Ignore Legally Required Opt-Out Signals Despite Regulatory Endorsement
- **Source:** The Record (Recorded Future) — https://therecord.media/big-tech-fails-to-opt-out-users-requesting-not-to-be-tracked
- **Severity:** medium
- **Tags:** `data-breach`, `privacy`
- **Summary:** webXray found 194 ad services ignoring CCPA opt-out signals in California web traffic audits from March 2026. Privacy compliance teams should treat technical opt-out signals as unenforceable without contractual backing.

### 7. Apple Threatened to Ban Grok from App Store Over Nonconsensual Deepfakes on X
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/912297/apple-app-store-ban-grok-x-deepfakes
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`
- **Summary:** Apple privately threatened to remove Grok from the App Store in January over nonconsensual deepfakes on X; the app remained available. Demonstrates how app store gatekeeping can function as an informal AI content enforcement mechanism outside formal regulatory channels.

### 8. Microsoft April 2026 Update Triggers BitLocker Recovery Mode on Windows Server 2025
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-some-windows-servers-ask-for-bitlocker-key-after-april-updates/
- **Severity:** medium
- **Tags:** `microsoft`, `vulnerability`
- **Summary:** KB5082063 causes some Windows Server 2025 systems to enter BitLocker recovery on boot. Not a vulnerability but an operational disruption — admins should ensure recovery keys are documented before patching, especially for headless remote servers.

### 9. Microsoft Patches Bug That Silently Upgraded Windows Server 2019/2022 to Server 2025
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-bug-behind-windows-server-2025-automatic-upgrades/
- **Severity:** medium
- **Tags:** `microsoft`, `vulnerability`
- **Summary:** A bug caused Windows Server 2019/2022 to auto-upgrade to Server 2025, now fixed. Admins should audit for unintended upgrades during the affected window and verify licensing and application compatibility on any self-upgraded systems.

### 10. Datasette Drops CSRF Tokens in Favor of Sec-Fetch-Site Header Protection
- **Source:** Simon Willison — https://simonwillison.net/2026/Apr/14/replace-token-based-csrf/#atom-everything
- **Severity:** informational
- **Tags:** `appsec`
- **Summary:** Datasette replaced CSRF token middleware with Sec-Fetch-Site header validation, following Filippo Valsorda's research. Removes server-side token state and template boilerplate; works well for modern-browser audiences and API-first web apps.

## Skippable

- **Trump Urges Extending Foreign Surveillance Program** — SecurityWeek. FISA reauthorization policy update, no technical content or new IOCs.
- **Meet HoloTab by HCompany** — Hugging Face Blog. AI product announcement with no summary and no security angle.
- **Microsoft Issues Patches for SharePoint Zero-Day and 168 Other New Vulnerabilities** — The Hacker News. Duplicate Patch Tuesday coverage; post already published on 2026-04-14.
- **OpenAI Launches GPT-5.4-Cyber with Expanded Access for Security Teams** — The Hacker News. Duplicate coverage; post already published on 2026-04-14.
- **Anthropic's Rise is Giving Some OpenAI Investors Second Thoughts** — TechCrunch AI. Investor valuation/sentiment story; no technical substance.
- **Zig 0.16.0 Release Notes: "Juicy Main"** — Simon Willison. Programming language release with no security angle.
- **Microsoft Bets $10 Billion to Boost Japan's AI, Cybersecurity** — Dark Reading. Investment announcement with no technical content.
- **AWS Interconnect is Now Generally Available** — AWS News Blog. Infrastructure networking GA with no security implications.
