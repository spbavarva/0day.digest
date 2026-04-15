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
- **Section:** Cybersecurity — Primary
- **Severity:** critical
- **Tags:** `vulnerability`, `cve`, `rce`
- **Slug:** `2026-04-15-fortinet-fortisandbox-critical-auth-bypass-rce`
- **Must-know:** no
- **Summary:** Fortinet patched critical flaws in FortiSandbox allowing remote auth bypass and RCE via HTTP requests. No confirmed active exploitation, but FortiSandbox sits in the malware analysis path and compromise could let attackers whitelist samples.

### 2. $10 Domain Registration Could Have Handed Attackers 25K Endpoints in OT and Gov Networks
- **Source:** SecurityWeek — https://www.securityweek.com/10-domain-could-have-handed-hackers-25k-endpoints-including-in-ot-and-gov-networks/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `malware`, `vulnerability`
- **Slug:** `2026-04-15-cheap-domain-25k-ot-gov-endpoints-adware`
- **Must-know:** no
- **Summary:** Researchers found a lapsed or unclaimed domain that 25,000 adware-infected endpoints were beaconing to — including hosts on OT and government networks. Registering it for $10 would have granted C2 access; the adware can kill security products and drop secondary payloads.

### 3. ICS Patch Tuesday: Eight Industrial Giants Publish Security Advisories
- **Source:** SecurityWeek — https://www.securityweek.com/ics-patch-tuesday-8-industrial-giants-publish-new-security-advisories/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `ics`
- **Slug:** `2026-04-15-ics-patch-tuesday-eight-industrial-vendors`
- **Must-know:** no
- **Summary:** Siemens, Schneider Electric, Aveva, Rockwell Automation, ABB, Phoenix Contact, Mitsubishi Electric, and Moxa all released security advisories in April's ICS Patch Tuesday. OT teams should pull each vendor's PSIRT advisory and prioritize internet-exposed assets.

### 4. Threat Actors Abusing n8n Agentic AI Workflow Platform in Email Attack Campaigns
- **Source:** Cisco Talos — https://blog.talosintelligence.com/the-n8n-n8mare/
- **Section:** Cybersecurity — Research & Threat Intel
- **Severity:** high
- **Tags:** `malware`, `phishing`, `llm`
- **Slug:** `2026-04-15-n8n-agentic-ai-workflow-abuse-email-campaigns`
- **Must-know:** no
- **Summary:** Cisco Talos documented threat actors abusing n8n, an agentic AI workflow automation platform, in email campaigns from October 2025 through March 2026. Attackers chain AI calls, webhooks, and external services to orchestrate delivery workflows — a pattern that mirrors RMM tool abuse.

### 5. Ivanti Neurons for ITSM Patches Auth Bypass and Cross-Session Data Disclosure
- **Source:** SecurityWeek — https://www.securityweek.com/two-vulnerabilities-patched-in-ivanti-neurons-for-itsm/
- **Section:** Cybersecurity — Primary
- **Severity:** high
- **Tags:** `vulnerability`, `cve`, `privilege-escalation`
- **Slug:** `2026-04-15-ivanti-neurons-itsm-auth-bypass-session-disclosure`
- **Must-know:** no
- **Summary:** Ivanti patched two flaws in Neurons for ITSM: a persistence bypass that lets disabled accounts maintain access, and a cross-session information disclosure. ITSM platforms hold broad infrastructure permissions, making the persistence flaw especially dangerous for incident response scenarios.

### 6. Study: 194 Ad Services Ignore Legally Required Opt-Out Signals Despite Regulatory Endorsement
- **Source:** The Record (Recorded Future) — https://therecord.media/big-tech-fails-to-opt-out-users-requesting-not-to-be-tracked
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `data-breach`, `privacy`
- **Slug:** `2026-04-15-big-tech-ad-tracking-opt-out-ignored`
- **Must-know:** no
- **Summary:** webXray audited California web traffic and found 194 ad services ignoring legally defined opt-out signals endorsed by regulators. Organizations relying on GPC headers and browser privacy signals for CCPA compliance should audit enforcement contractually, not just technically.

### 7. Apple Threatened to Ban Grok from App Store Over Nonconsensual Deepfakes on X
- **Source:** The Verge AI — https://www.theverge.com/ai-artificial-intelligence/912297/apple-app-store-ban-grok-x-deepfakes
- **Section:** AI — News & Analysis
- **Severity:** medium
- **Tags:** `ai-safety`, `llm`
- **Slug:** `2026-04-15-grok-deepfakes-x-apple-app-store-ban-threat`
- **Must-know:** no
- **Summary:** Apple privately threatened to remove Grok from the App Store in January over a surge of nonconsensual sexual deepfakes on X. The threat was made behind closed doors; Grok remained available. Illustrates how app store distribution constraints can serve as informal AI content moderation levers.

### 8. Microsoft April 2026 Update Triggers BitLocker Recovery Mode on Windows Server 2025
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-some-windows-servers-ask-for-bitlocker-key-after-april-updates/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `microsoft`, `vulnerability`
- **Slug:** `2026-04-15-windows-server-2025-bitlocker-recovery-april-update`
- **Must-know:** no
- **Summary:** KB5082063 causes some Windows Server 2025 systems to boot into BitLocker recovery, requiring the recovery key before the OS loads. Not a vulnerability, but an operational risk — especially on headless or remote-only servers where recovery key access may not be pre-arranged.

### 9. Microsoft Patches Bug That Silently Upgraded Windows Server 2019/2022 to Server 2025
- **Source:** BleepingComputer — https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-bug-behind-windows-server-2025-automatic-upgrades/
- **Section:** Cybersecurity — Primary
- **Severity:** medium
- **Tags:** `microsoft`, `vulnerability`
- **Slug:** `2026-04-15-windows-server-auto-upgrade-bug-fixed`
- **Must-know:** no
- **Summary:** Microsoft resolved a bug causing Windows Server 2019 and 2022 systems to auto-upgrade to Server 2025. Admins should verify no unintended upgrades occurred and assess licensing and compatibility for any systems that self-upgraded during the affected window.

### 10. Datasette Drops CSRF Tokens in Favor of Sec-Fetch-Site Header Protection
- **Source:** Simon Willison — https://simonwillison.net/2026/Apr/14/replace-token-based-csrf/#atom-everything
- **Section:** AI — News & Analysis
- **Severity:** informational
- **Tags:** `appsec`
- **Slug:** `2026-04-15-datasette-csrf-sec-fetch-site-header`
- **Must-know:** no
- **Summary:** Datasette merged a PR replacing CSRF token protection with Sec-Fetch-Site header validation, based on Filippo Valsorda's research. Reduces template boilerplate and server-side token state; the tradeoff is reliance on modern browsers sending the header correctly.

## Skippable

- **Trump Urges Extending Foreign Surveillance Program** — SecurityWeek. Policy/legislative update on FISA reauthorization with no technical content or new IOCs.
- **Meet HoloTab by HCompany** — Hugging Face Blog. AI browser companion product announcement with no summary content and no security angle.
- **Microsoft Issues Patches for SharePoint Zero-Day and 168 Other New Vulnerabilities** — The Hacker News. Duplicate coverage of April 2026 Patch Tuesday; post already published on 2026-04-14.
- **OpenAI Launches GPT-5.4-Cyber with Expanded Access for Security Teams** — The Hacker News. Duplicate coverage; post already published on 2026-04-14.
- **Anthropic's Rise is Giving Some OpenAI Investors Second Thoughts** — TechCrunch AI. Investor sentiment and valuation story; no technical content.
- **Zig 0.16.0 Release Notes: "Juicy Main"** — Simon Willison. Programming language release with no security or AI-safety angle.
- **Microsoft Bets $10 Billion to Boost Japan's AI, Cybersecurity** — Dark Reading. Investment/partnership announcement with no technical substance.
- **AWS Interconnect is Now Generally Available** — AWS News Blog. Infrastructure networking GA with no security implications highlighted.
